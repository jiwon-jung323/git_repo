import pandas as pd

"""
[특수 키워드 및 타입 탐색 (Exploration)]
특정 키워드 타입(A, G) 외에 예외적으로 들어오는 키워드 코드를 식별하고
분석에서 제외할지 판단하기 위한 탐색용 스크립트입니다.
"""

# 베이스 데이터와 키워드 마스터 로드
df_base = pd.read_csv('sample_5year_base.csv')
keyword_code = pd.read_csv('sample_keyword_code.csv')
keyword_mapping = pd.read_csv('sample_keyword_mapping.csv')

# 키워드 결합
keyword = keyword_mapping.merge(keyword_code, on='keyword_code', how='left')

# 정상 타입(A, G)에 속하는 키워드 집합 분리
code_A = set(keyword_code[keyword_code['keyword_type'] == 'A']['keyword_code'])
code_G = set(keyword_code[keyword_code['keyword_type'] == 'G']['keyword_code'])

mask_valid = keyword['keyword_code'].isin(code_A.union(code_G))

keyword_valid = keyword[mask_valid].copy()
keyword_invalid = keyword[~mask_valid].copy()

# 비정상 타입에 매핑된 주문건의 특성(상품명, 규격 등) 확인
df_merge = df_base.merge(keyword, on='order_id', how='left')
df_merge = df_merge[df_merge['keyword_type'].notna()]

# 메인 키워드(A)가 아닌 예외 케이스 추출 (데이터 정합성 검증용)
df_exception_cases = df_merge[df_merge['keyword_type'] != 'A'][['order_id', 'keyword_type', 'product_name']]
