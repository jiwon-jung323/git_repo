import pandas as pd
from datetime import datetime, timedelta
import re

"""
[중기(2년) 데이터 전처리 및 키워드 정제 파이프라인]
이 스크립트는 최근 2년간의 거래 데이터를 추출하고,
단순 참조/서비스/기타/비인가 품목 등의 비물품 거래를 제외하며,
상품명/규격에 포함된 불필요한 문구(예: '긴급', 괄호 등)를 정제하는 과정을 담고 있습니다.
"""

# =====================================================================
# 1. 데이터 로드 (DB 추출본)
# =====================================================================
order_main = pd.read_csv('sample_order_main.csv')
order_product = pd.read_csv('sample_order_product.csv')
participation = pd.read_csv('sample_participation.csv')
join_product = pd.read_csv('sample_join_product.csv')

# 유효한 참여 기록 필터링
participation = participation[participation['participation_status'] == 'Y']

# 주문-상품-참여 정보 병합
merged_step1 = order_product.merge(join_product, on=['order_id', 'product_seq'], how='left')
merged_final = merged_step1.merge(order_main, on=['order_id'], how='left')
merged_final = merged_final.dropna(subset=['participation_status']).copy()

# =====================================================================
# 2. 분석 기준 일자 필터링 (최근 2년)
# =====================================================================
order_valid = order_main[(order_main['order_seq'] != 0) & (order_main['contract_status'] != 'D')].copy()
order_valid['order_start_date'] = pd.to_datetime(order_valid['order_start_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

today = datetime(2024, 1, 1) # 임의의 분석 기준일 설정
two_years_ago = today - timedelta(days=365*2)
order_recent_2y = order_valid[order_valid['order_start_date'] >= two_years_ago].copy()

# 물품 거래건만 필터링
order_type_A = order_recent_2y[order_recent_2y['transaction_type'] == 'A'][['order_id', 'transaction_type']]

# 앞에서 시간 및 거래 유형(물품)으로 필터링한 대상(order_type_A)만 메인 데이터셋에 남깁니다.
df_target = merged_final.merge(order_type_A[['order_id']], on='order_id', how='inner')

# =====================================================================
# 3. 비물품/가짜상품 키워드 필터링 (행 제거)
# =====================================================================
# 특정 비인가 도메인 등 물품이 아닌 카테고리를 제외합니다.
exclude_keywords = ['Keyword_A', 'Keyword_B', 'Keyword_C', '참조', 'url', 'http', '입찰', '제외도메인1', '제외도메인2']
pattern = '|'.join(exclude_keywords)

mask_name = df_target['product_name'].str.contains(pattern, case=False, na=False)
mask_spec = df_target['product_spec'].str.contains(pattern, case=False, na=False)
flag_mask = mask_name | mask_spec

df_clean = df_target.loc[~flag_mask].copy()

# =====================================================================
# 4. 상품명 및 규격 텍스트 정제 (문구 제거)
# =====================================================================
def remove_words_and_empty_brackets(s: pd.Series, words_to_remove):
    # 1) 지정 단어 제거 (대소문자 무시)
    if words_to_remove:
        pattern = r'(' + '|'.join(map(re.escape, words_to_remove)) + r')'
        s = s.fillna('').str.replace(pattern, '', regex=True, flags=re.IGNORECASE)
    else:
        s = s.fillna('')

    # 2) 단독으로 남은 빈 괄호/대괄호/꺾쇠 제거
    s = s.str.replace(r'\(\s*\)', '', regex=True)
    s = s.str.replace(r'\[\s*\]', '', regex=True)
    s = s.str.replace(r'<\s*>', '', regex=True)

    # 3) 다중 공백 정리
    s = s.str.replace(r'\s+', ' ', regex=True).str.strip()
    return s

# 분석에 불필요한 접두사/접미사 제거
words_to_remove_name = ['배부용', '긴급', '입니다.']
words_to_remove_spec = ['배부용', '긴급', '입니다.', '부탁드립니다', '으로']

df_clean['product_name'] = remove_words_and_empty_brackets(df_clean['product_name'], words_to_remove_name)
df_clean['product_spec'] = remove_words_and_empty_brackets(df_clean['product_spec'], words_to_remove_spec)

# =====================================================================
# 5. 단일 상품 거래건 고유 ID 추출 및 저장
# =====================================================================
order_id_seq2 = df_clean.loc[df_clean['product_seq'] == 2, 'order_id'].drop_duplicates()
order_id_seq1 = df_clean.loc[df_clean['product_seq'] == 1, 'order_id'].drop_duplicates()

overlap_mask = order_id_seq1.isin(order_id_seq2)
unique_single_orders = order_id_seq1[~overlap_mask].reset_index(drop=True).to_frame(name='order_id')
unique_single_orders['is_unique'] = 1

# 결과 저장
unique_single_orders.to_csv('unique_single_orders_2year.csv', index=False, encoding='utf-8-sig')
df_clean = df_clean.sort_values('order_id', ascending=True)
df_clean.to_csv('2year_data_cleaned.csv', index=False, encoding='utf-8-sig')
