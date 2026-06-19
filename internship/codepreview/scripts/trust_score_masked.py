import pandas as pd
from datetime import datetime, timedelta
import numpy as np

"""
[회원 신뢰도(Trust Score) 산출 파이프라인]
활동 데이터(거래 참여, 계약 횟수, 총 거래액/수수료, 인증 여부 등)를 기반으로
구간별 점수(Tier/Cumulative)를 부여하여 최종 고객 신뢰도 점수 및 랭킹을 산출합니다.
"""

# =====================================================================
# 1. 데이터 로드 및 기본 필터링 (테스트 계정 제외)
# =====================================================================
member_df = pd.read_csv('sample_member_info.csv')
order_df = pd.read_csv('sample_order_main.csv')
cert_df = pd.read_csv('sample_certification_info.csv')

# 상호명에 '테스트'가 포함되거나, ID가 숫자+test 조합인 테스트 계정 제외
mask_test_name = member_df['company_name'].astype(str).str.contains('테스트', na=False)
mask_test_id = member_df['member_id'].astype(str).str.contains(r'^\d*test\d*$', case=False, regex=True)
member_use = member_df[~(mask_test_name | mask_test_id)].copy()

# =====================================================================
# 2. 파생 지표 1: 기업 인증 점수 산출 (증명서, 라이선스 등록 건수)
# =====================================================================
# (보안: 실제 인증서 종류 로직 마스킹)
cert_cnt = cert_df.groupby('member_id').size().reset_index(name='cert_count')
member_use = member_use.merge(cert_cnt, on='member_id', how='left')

# 등록된 인증서 개수 기반 점수 산출 (최대 5점 캡핑)
member_use['cert_score'] = member_use['cert_count'].fillna(0).clip(upper=5).astype(int)

# =====================================================================
# 3. 파생 지표 2: 거래 활동 지표 산출 (최근 3년 기준)
# =====================================================================
# 참여 횟수, 계약 횟수, 누적 거래액, 누적 수수료 등을 Aggregation
trade_stats = (
    order_df.groupby('member_id')
    .agg(
        trade_join_cnt=('order_id', 'nunique'),
        contract_cnt=('is_success', lambda x: (x == 'Y').sum()),
        total_trade_amt=('trade_amount', 'sum'),
        total_fee_amt=('fee_amount', 'sum')
    ).reset_index()
)

member_final = member_use.merge(trade_stats, on='member_id', how='left').fillna(0)

# =====================================================================
# 4. 파생 지표 3: 인접 참여(활성도) 지표 산출
# =====================================================================
# 마지막 참여일과 그 다음 참여일의 간격이 60일 이하인 '연속/활성 참여' 횟수 계산
order_df['join_date'] = pd.to_datetime(order_df['join_date'], errors='coerce')
order_sorted = order_df.dropna(subset=['join_date']).sort_values(['member_id', 'join_date'])
order_sorted['gap_days'] = order_sorted.groupby('member_id')['join_date'].diff().dt.days

recent_active_cnt = (
    order_sorted.assign(is_active=order_sorted['gap_days'].le(60))
    .groupby('member_id')['is_active'].sum()
    .reset_index(name='active_join_cnt')
)

member_final = member_final.merge(recent_active_cnt, on='member_id', how='left').fillna(0)

# =====================================================================
# 5. 구간별 점수 부여 알고리즘 (Scoring Engine)
# =====================================================================
# (보안: 실제 비즈니스 점수 배점표(Threshold)는 가상의 비율로 대체하여 마스킹)
def score_by_thresholds(series, thresholds, points):
    x = pd.to_numeric(series, errors='coerce').fillna(0)
    out = pd.Series(0.0, index=series.index)
    for i, t in enumerate(thresholds):
        out[x >= t] = points[i] # 해당 구간 이상일 경우 점수 갱신 (Tier 방식)
    return out

SCORE_RULES = {
    'trade_join_cnt':  {'thresh': [1, 5, 15, 50, 100], 'pts': [3, 6, 9, 15, 20]},
    'contract_cnt':    {'thresh': [1, 3, 10, 30, 100], 'pts': [3, 6, 12, 17, 20]},
    'total_trade_amt': {'thresh': [10000, 500000, 1000000], 'pts': [2, 5, 10]}, # 가상 금액
    'total_fee_amt':   {'thresh': [1000, 50000, 100000], 'pts': [1, 3, 5]},
    'active_join_cnt': {'thresh': [1, 3, 10, 30], 'pts': [1, 2, 4, 5]},
}

for col, rule in SCORE_RULES.items():
    member_final[f'{col}_score'] = score_by_thresholds(member_final[col], rule['thresh'], rule['pts'])

# =====================================================================
# 6. 총점 산출 및 랭킹 부여
# =====================================================================
score_cols = ['cert_score'] + [f'{col}_score' for col in SCORE_RULES.keys()]
member_final['total_trust_score'] = member_final[score_cols].sum(axis=1)

# 총점수 기준 정렬 및 등수(Competition Ranking) 산출
valid_members = member_final[member_final['total_trust_score'] > 0].copy()
valid_members = valid_members.sort_values(['total_trust_score', 'cert_score'], ascending=[False, False])
valid_members['rank'] = valid_members['total_trust_score'].rank(method='min', ascending=False).astype(int)

valid_members.to_excel('final_trust_score_ranking.xlsx', index=False)
