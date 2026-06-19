import pandas as pd

"""
[태그 상호 배제 플래그화 및 최종 병합 검증]
사전 정의된 특정 비즈니스 태그(예: 타겟군 A vs 타겟군 B)가
서로 논리적으로 공존할 수 없는 경우, 우선순위에 따라 배제 처리를 수행하고
최종 상품 마스터 테이블과 정상적으로 1:1 병합되었는지 무결성을 검증합니다.
"""

# =====================================================================
# 1. 데이터 로드 및 라벨링 정보 매핑
# =====================================================================
product_df = pd.read_csv('sample_product_info.csv')
keyword_df = pd.read_csv('sample_keyword_mapped.csv')
label_df = pd.read_excel('sample_business_label.xlsx')

# 상품별 추출된 키워드 정보에 수동 라벨링 데이터 결합
keyword_use = keyword_df.merge(label_df, on='product_id', how='left')

# =====================================================================
# 2. 상호 배타적(Mutually Exclusive) 비즈니스 룰 적용
# =====================================================================
# 예: 특정 상품이 'VIP용'과 '일반판촉용' 둘 다 라벨링된 경우,
# 수동으로 지정한 메인 type에 따라 반대쪽 플래그를 0으로 무효화 처리
mask_vip = keyword_use['type'].eq('VIP') # 기존: 특수목적군A
mask_promo = keyword_use['type'].eq('Promo') # 기존: 특수목적군B

keyword_use.loc[mask_vip, 'Promo'] = 0
keyword_use.loc[mask_promo, 'VIP'] = 0

keyword_use[['VIP', 'Promo']] = keyword_use[['VIP', 'Promo']].fillna(0).astype(int)

# =====================================================================
# 3. 상품 마스터와 병합 및 누락 데이터(Outer Join) 검증
# =====================================================================
# 마스터 테이블(product_df)과 처리된 키워드 테이블을 병합
merge_check = product_df.merge(
    keyword_use[['product_id']].drop_duplicates(),
    on='product_id',
    how='outer',
    indicator=True
)

# Left Only (상품은 있으나 키워드가 없는 경우)
master_only_ids = merge_check.loc[merge_check['_merge'] == 'left_only', 'product_id']
master_dropped = product_df[product_df['product_id'].isin(master_only_ids)].copy()

# Right Only (키워드는 있으나 상품 마스터에 없는 고아 데이터)
keyword_only_ids = merge_check.loc[merge_check['_merge'] == 'right_only', 'product_id']
keyword_dropped = keyword_use[keyword_use['product_id'].isin(keyword_only_ids)].copy()

print(f"매칭 누락된 마스터 상품 수: {len(master_dropped)}")
print(f"상품 정보가 없는 잉여 키워드 수: {len(keyword_dropped)}")

# 정상 병합된 최종 데이터
final_merged_df = product_df.merge(keyword_use, on='product_id', how='inner')
final_merged_df.to_csv('final_product_with_keywords.csv', index=False)
