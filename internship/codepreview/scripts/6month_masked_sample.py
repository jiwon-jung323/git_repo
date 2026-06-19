import pandas as pd
from datetime import datetime, timedelta

"""
[데이터 추출 및 전처리 요약]
이 스크립트는 최근 2년간의 입찰/주문 데이터를 기반으로, 
단순 참조용 데이터나 서비스/비물품 등의 데이터를 제외하고 
'실제 물품(상품)'에 대한 유효 거래 내역만 추출하기 위한 전처리 과정을 담고 있습니다.
"""

# =====================================================================
# 1. 데이터 로드 (보안을 위해 실제 DB 추출 과정 및 파일명은 마스킹 처리)
# =====================================================================
# 실제 사내 DB에서 '주문 기본 정보', '주문 상품 상세 정보', '참여 기업 정보' 등을 추출한 결과라고 가정합니다.
order_main = pd.read_csv('sample_order_main.csv')          # 메인 주문 정보
order_product = pd.read_csv('sample_order_product.csv')    # 상품 상세 정보
participation = pd.read_csv('sample_participation.csv')    # 거래 참여 정보

# =====================================================================
# 2. 유효한 참여 기록 필터링
# =====================================================================
# 참여 상태가 'Y'(정상 참여/승인)인 건들만 분석 대상으로 필터링합니다.
participation = participation[participation['participation_status'] == 'Y']

# =====================================================================
# 3. 키워드 및 카테고리 정보 결합
# =====================================================================
# 상품별 부여된 카테고리 및 키워드 코드를 병합하여 확장합니다.
keyword_code = pd.read_csv('sample_keyword_code.csv')
keyword_mapping = pd.read_csv('sample_keyword_mapping.csv')
keyword_merged = keyword_mapping.merge(keyword_code, on='keyword_code', how='left')

# =====================================================================
# 4. 주문 - 상품 - 참여 정보 병합 (Merge)
# =====================================================================
# DB의 정규화된 테이블 구조(주문-상품상세-참여정보)를 분석을 위해 하나의 데이터프레임으로 결합합니다.
# (원본의 식별자(ID) 및 시퀀스 등을 일반 명칭으로 추상화)
join_product = pd.read_csv('sample_join_product.csv')

# 4-1. 상품 정보에 참여 정보를 결합
merged_step1 = order_product.merge(join_product, left_on=['order_id', 'product_seq'], right_on=['order_id', 'product_seq'], how='left')

# 4-2. 최종적으로 주문 마스터 정보와 결합
merged_final = merged_step1.merge(order_main, on=['order_id'], how='left')
merged_final = merged_final.dropna(subset=['participation_status']).copy()

# =====================================================================
# 5. 분석 기준 일자 필터링 (최근 2년 데이터 추출)
# =====================================================================
# 데이터 기준일(예: 2024-01-01)로부터 최근 2년간의 데이터만 필터링합니다.
order_valid = order_main[order_main['order_seq'] != 0].copy() # 취소/비정상 건 제외
order_valid['order_start_date'] = pd.to_datetime(order_valid['order_start_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

today = datetime(2024, 1, 1) # 임의의 분석 기준일 설정
two_years_ago = today - timedelta(days=365*2)
order_recent_2y = order_valid[order_valid['order_start_date'] >= two_years_ago].copy()
order_recent_2y['is_participated'] = 'y'

# =====================================================================
# 6. 특정 거래 유형 필터링 (물품 거래건만 추출)
# =====================================================================
# 거래 종류(transaction_type)가 'A'(예: 일반 물품 거래)인 경우만 타겟팅합니다.
# 기존 비즈니스 플래그명은 일반화 처리합니다.
order_type_A = order_recent_2y[order_recent_2y['transaction_type'] == 'A'][['order_id', 'transaction_type']]

# =====================================================================
# 7. 텍스트 패턴 기반 제외 대상 필터링 (이상치 및 비물품 서비스 건 제거)
# =====================================================================
# 물품이 아닌 'Keyword_A', 'Keyword_B', 'Keyword_C' 이거나, 단순 '참조', 'url', 'http' 등의 
# 가짜 상품명/규격이 들어간 데이터를 제외 처리합니다.
# 앞에서 시간 및 거래 유형(물품)으로 필터링한 대상(order_type_A)만 메인 데이터셋에 남깁니다.
df_target = merged_final.merge(order_type_A[['order_id']], on='order_id', how='inner')

exclude_name_keywords = ['Keyword_A', 'Keyword_B', 'Keyword_C', '참조', 'url', 'http']
exclude_spec_keywords = ['참조', 'url', 'http']

name_pattern = '|'.join(exclude_name_keywords)
spec_pattern = '|'.join(exclude_spec_keywords)

mask_name = df_target['product_name'].str.contains(name_pattern, case=False, na=False)
mask_spec = df_target['product_spec'].str.contains(spec_pattern, case=False, na=False)
flag_mask = mask_name | mask_spec

# 패턴에 걸리지 않은 순수 '물품' 데이터만 남김
df_clean = df_target.loc[~flag_mask].copy()

# =====================================================================
# 8. 단일 상품 거래건 고유 ID 추출 (중복 제거)
# =====================================================================
# 여러 상품이 포함된 거래(product_seq == 2 이상)와 단일 상품 거래(product_seq == 1)를 구분하고,
# 순수하게 단일 상품만 거래된 고유 order_id를 추출합니다.
order_id_seq2 = df_clean.loc[df_clean['product_seq'] == 2, 'order_id'].drop_duplicates()
order_id_seq1 = df_clean.loc[df_clean['product_seq'] == 1, 'order_id'].drop_duplicates()

# 복수 상품 거래에 포함되지 않은, 순수 단일 상품 주문 건만 도출
overlap_mask = order_id_seq1.isin(order_id_seq2)
unique_single_orders = order_id_seq1[~overlap_mask].reset_index(drop=True).to_frame(name='order_id')
unique_single_orders['is_unique'] = 1

# 최종 결과를 CSV로 저장 (분석용 Base 데이터)
unique_single_orders.to_csv('unique_single_orders_base.csv', index=False, encoding='utf-8-sig')
