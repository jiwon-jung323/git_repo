import pandas as pd
from datetime import datetime, timedelta

"""
[장기(5년) 데이터 전처리 파이프라인]
이 스크립트는 최근 5년간의 거래 데이터를 추출하고,
물품 거래가 아닌 서비스/기타 대행 등의 데이터를 1차적으로 필터링하여
장기 트렌드 분석을 위한 베이스 데이터를 생성합니다.
"""

# =====================================================================
# 1. 데이터 로드 (DB 추출본)
# =====================================================================
order_main = pd.read_csv('sample_order_main.csv')
order_product = pd.read_csv('sample_order_product.csv')
participation = pd.read_csv('sample_participation.csv')
join_product = pd.read_csv('sample_join_product.csv')

# 유효 참여건 필터링
participation = participation[participation['participation_status'] == 'Y']

# 병합
merged_step1 = order_product.merge(join_product, on=['order_id', 'product_seq'], how='left')
merged_final = merged_step1.merge(order_main, on=['order_id'], how='left')
merged_final = merged_final.dropna(subset=['participation_status']).copy()

# =====================================================================
# 2. 분석 기준 일자 필터링 (최근 5년)
# =====================================================================
order_valid = order_main[order_main['order_seq'] != 0].copy()
order_valid['order_start_date'] = pd.to_datetime(order_valid['order_start_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

today = datetime(2024, 1, 1) # 임의의 분석 기준일 설정
five_years_ago = today - timedelta(days=365*5)
order_recent_5y = order_valid[order_valid['order_start_date'] >= five_years_ago].copy()

# 물품 거래건 필터링
order_type_A = order_recent_5y[order_recent_5y['transaction_type'] == 'A'][['order_id', 'transaction_type']]
# 앞에서 시간 및 거래 유형(물품)으로 필터링한 대상(order_type_A)만 메인 데이터셋에 남깁니다.
df_target = merged_final.merge(order_type_A[['order_id']], on='order_id', how='inner')

# =====================================================================
# 3. 비물품/가짜상품 키워드 1차 필터링
# =====================================================================
exclude_keywords = ['Keyword_A', 'Keyword_B', 'Keyword_C', '참조', 'url', 'http']
pattern = '|'.join(exclude_keywords)

mask_name = df_target['product_name'].str.contains(pattern, case=False, na=False)
mask_spec = df_target['product_spec'].str.contains(pattern, case=False, na=False)
flag_mask = mask_name | mask_spec

df_clean = df_target.loc[~flag_mask].copy()

# =====================================================================
# 4. 단일 상품 거래건 고유 ID 추출 및 저장
# =====================================================================
order_id_seq2 = df_clean.loc[df_clean['product_seq'] == 2, 'order_id'].drop_duplicates()
order_id_seq1 = df_clean.loc[df_clean['product_seq'] == 1, 'order_id'].drop_duplicates()

overlap_mask = order_id_seq1.isin(order_id_seq2)
unique_single_orders = order_id_seq1[~overlap_mask].reset_index(drop=True).to_frame(name='order_id')
unique_single_orders['is_unique'] = 1

unique_single_orders.to_csv('unique_single_orders_5year.csv', index=False, encoding='utf-8-sig')
df_clean = df_clean.sort_values('order_id').reset_index(drop=True)
df_clean.to_csv('5year_data_cleaned.csv', index=False, encoding='utf-8-sig')
