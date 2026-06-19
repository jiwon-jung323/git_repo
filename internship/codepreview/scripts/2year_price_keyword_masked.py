import pandas as pd

"""
[상품 카테고리 매핑 및 특수 태그 플래그화 로직]
이 스크립트는 2년치 거래 데이터에 상품 카테고리를 1:1로 매핑합니다.
하나의 상품에 여러 카테고리가 맵핑될 경우 빈도수(최빈값)로 결정하며,
동률일 경우 수동 검수 데이터(엑셀)를 활용해 최종 카테고리를 확정합니다.
추가로 특정 비즈니스 태그(예: 타겟 상품군)를 원핫인코딩(One-hot) 방식으로 부착합니다.
"""

# =====================================================================
# 1. 데이터 로드 (분류/카테고리 마스터 테이블 및 검수 데이터)
# =====================================================================
category_code = pd.read_csv('sample_category_code.csv')
category_mapping = pd.read_csv('sample_category_mapping.csv')
merged_base = pd.read_csv('sample_category_merged_base.csv') # 전처리된 기본 거래 내역
manual_check_df = pd.read_excel("sample_manual_check_category.xlsx") # 수동 검수 데이터

# 카테고리 타입이 'A'(주요 분류)인 마스터 코드만 필터링
category_master = category_code[category_code['category_type'] == 'A']

# 거래내역에 카테고리 정보 결합
keyword_combined = category_mapping.merge(category_master, on='category_code', how='left')
keyword_combined = keyword_combined[keyword_combined['category_type'].notna()]
df_merge = merged_base.merge(keyword_combined, on='order_id', how='left')

# =====================================================================
# 2. 상품별 대표 카테고리 도출 (빈도 기반 및 동률 처리)
# =====================================================================
# 2-1. 상품(product_id)별 카테고리(category_class) 등장 빈도 집계
cnt = (
    df_merge[['product_id', 'category_class']]
    .dropna(subset=['product_id', 'category_class'])
    .groupby(['product_id', 'category_class'])
    .size()
    .reset_index(name='cnt')
)

# 2-2. 최빈값 추출 및 동률(Tie) 확인
max_cnt = cnt.groupby('product_id')['cnt'].transform('max')
top = cnt[cnt['cnt'] == max_cnt].copy()

tie_ids = top.groupby('product_id').size()
tie_ids = tie_ids[tie_ids > 1].index

# 명확히 단일 카테고리로 확정된 그룹 vs 동률 발생 그룹 분리
df_category_clear = top[~top['product_id'].isin(tie_ids)].sort_values(['product_id']).reset_index(drop=True)
df_category_tie = top[top['product_id'].isin(tie_ids)].reset_index(drop=True)

# 2-3. 동률 그룹에 대해 수동 검수 엑셀 데이터(check==1)를 적용해 해결
check_pick = manual_check_df[manual_check_df['check'] == 1][['product_id', 'category_class']].copy()
check_pick['product_id'] = pd.to_numeric(check_pick['product_id'], errors='coerce')
check_pick['category_class'] = check_pick['category_class'].astype(str)

df_category_tie['category_class'] = df_category_tie['category_class'].astype(str)

resolved_tie = (
    df_category_tie
    .merge(check_pick, on=['product_id', 'category_class'], how='inner')
    [['product_id', 'category_class']]
    .drop_duplicates()
)

# 2-4. 자동 확정본 + 동률 해결본 병합 (최종 1:1 카테고리 매핑)
df_category_final = (
    pd.concat([df_category_clear[['product_id', 'category_class']], resolved_tie], ignore_index=True)
    .drop_duplicates(subset=['product_id'], keep='first')
)

# =====================================================================
# 3. 특정 타겟 상품군(비즈니스 플래그) 추출
# =====================================================================
# 예: 특정 목적(VIP용, 판촉용 등)으로 분류되는 태그를 컬럼화하여 원핫인코딩 처리
target_tags = ['Target_A', 'Target_B'] # 주요 타겟 태그

_tags = (
    df_merge.loc[df_merge['category_name'].isin(target_tags), ['product_id', 'category_name']]
    .dropna()
    .drop_duplicates()
)

# 피벗을 통해 Flag(1/0) 컬럼 생성
tag_flag = (
    _tags.assign(flag=1)
    .pivot_table(index='product_id', columns='category_name', values='flag', aggfunc='max', fill_value=0)
    .reset_index()
)

# 메인 데이터에 플래그 병합
df_category_final = df_category_final.merge(tag_flag, on='product_id', how='left')
for tag in target_tags:
    if tag not in df_category_final.columns:
        df_category_final[tag] = 0
df_category_final[target_tags] = df_category_final[target_tags].fillna(0).astype(int)

# 둘 다 포함되는 교집합 플래그 추가
df_category_final['Target_Both'] = (
    (df_category_final['Target_A'] == 1) & (df_category_final['Target_B'] == 1)
).astype(int)

# =====================================================================
# 4. 최종 데이터 추출
# =====================================================================
df_category_final.to_csv('final_category_mapped.csv', index=False, encoding='utf-8-sig')

# 교집합 타겟 데이터만 별도 추출
df_both = df_category_final[df_category_final['Target_Both'] == 1]
df_both.to_excel('Target_Both_List.xlsx', index=False)
