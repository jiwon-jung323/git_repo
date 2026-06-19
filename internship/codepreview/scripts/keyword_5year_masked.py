import pandas as pd

"""
[5년치 데이터 키워드 1차 매핑 파이프라인]
2년치 코드와 동일한 방식의 초기 키워드 정제를 수행합니다.
유효하지 않은 키워드 타입을 제거하고, 5년치 베이스 데이터에 매핑합니다.
"""

# =====================================================================
# 1. 데이터 로드 및 병합
# =====================================================================
df_base = pd.read_csv('5year_data_cleaned.csv')
keyword_code = pd.read_csv('sample_keyword_code.csv')
keyword_mapping = pd.read_csv('sample_keyword_mapping.csv')

# 키워드 병합
keyword = keyword_mapping.merge(keyword_code, on='keyword_code', how='left')

# =====================================================================
# 2. 유효 키워드 타입 필터링 ('A', 'G'만 남김)
# =====================================================================
invalid_keyword = keyword[~keyword['keyword_type'].isin(['A', 'G'])]
invalid_order_list = invalid_keyword['order_id'].dropna().unique()

use_keyword = keyword[~keyword['order_id'].isin(invalid_order_list)].copy()

# =====================================================================
# 3. 5년치 데이터와 내부 조인 (Inner Join)
# =====================================================================
# 유효한 키워드를 가진 주문건만 남김
df_merge = df_base.merge(use_keyword, on='order_id', how='inner')

# 향후 정규화 로직 적용을 위해 베이스 데이터 저장
df_merge.to_csv('5year_keyword_merged_base.csv', index=False, encoding='utf-8-sig')
