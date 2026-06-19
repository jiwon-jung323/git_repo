import pandas as pd

"""
[최빈값 기반 키워드 대표 클래스 선정 로직]
정규화가 완료된 상품명을 기준으로, 가장 많이 매핑된(최빈값) 키워드 카테고리를 
해당 상품명의 '대표 카테고리'로 확정하는 파이프라인입니다.
"""

# =====================================================================
# 1. 데이터 로드
# =====================================================================
df_merged = pd.read_csv('sample_normalized_keyword_data.csv')
unique_orders = pd.read_csv('sample_unique_single_orders.csv')

# 단일 상품 거래 데이터만 필터링
df_target = df_merged.merge(unique_orders, on='order_id', how='inner')

# =====================================================================
# 2. 정규화된 상품명 기준, 카테고리 최빈값 계산
# =====================================================================
# 상품명(name_norm)과 키워드 클래스(keyword_class) 조합별 빈도수 계산
class_counts = (
    df_target
    .groupby(['product_name_norm', 'keyword_class'], dropna=False)
    .size()
    .reset_index(name='cnt')
)

# 각 상품명에서 가장 높은 빈도수를 가진 클래스만 추출
class_top = class_counts[
    class_counts['cnt'].eq(class_counts.groupby('product_name_norm')['cnt'].transform('max'))
]

# =====================================================================
# 3. 동률(Tie) 클래스 분리 및 최종 대표 채택
# =====================================================================
# 최빈값이 2개 이상 동일한 경우(동률) 분리
class_ties = class_top[class_top.duplicated('product_name_norm', keep=False)]

# 동률이 없는 깔끔한 건들만 최종 클래스로 채택
final_class = (
    class_top[~class_top['product_name_norm'].isin(class_ties['product_name_norm'])]
    .rename(columns={'keyword_class': 'final_keyword_class', 'cnt': 'final_class_cnt'})
)

print(f"동률 발생 건수: {len(class_ties)}")
print(f"최종 단일 채택 건수: {len(final_class)}")

# =====================================================================
# 4. 원본 데이터에 최종 대표 클래스 병합 (Mapping 보정)
# =====================================================================
# 최종 채택된 대표 클래스를 원본 데이터프레임에 병합
df_final_mapped = df_target.merge(
    final_class[['product_name_norm', 'final_keyword_class', 'final_class_cnt']],
    on='product_name_norm',
    how='left',
    validate='m:1'
)

# 병합된 final_keyword_class 로 기존 keyword_class를 덮어씌워 일원화 보정
df_final_mapped['keyword_class'] = df_final_mapped['final_keyword_class'].fillna(df_final_mapped['keyword_class'])

# 누락이나 미스매치 검증 로직
buy_all = set(df_final_mapped['order_id'])
buy_matched = set(df_final_mapped.dropna(subset=['final_keyword_class'])['order_id'])

print(f"전체 고유 주문 수: {len(buy_all)}")
print(f"대표 카테고리 매칭 완료 수: {len(buy_matched)}")

# 최종 정제본 저장
df_final_mapped.to_csv('final_keyword_cleaned_data.csv', index=False, encoding='utf-8-sig')
