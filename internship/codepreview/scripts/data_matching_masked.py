import pandas as pd

"""
[데이터 분류 및 특수 카테고리 매칭 로직]
추출된 데이터에서 특정 도메인(예: 특수 카테고리A, 특수자재 등) 데이터를 분리하고,
외부 쇼핑몰의 복잡한 Depth(1~3차) 카테고리를 하나의 조합형 이름으로 맵핑하는 스크립트입니다.
"""

# =====================================================================
# 1. 도메인별 데이터 분리 (예: 일반 상품 vs 특수 목적 상품)
# =====================================================================
df_base = pd.read_csv('sample_cleaned_base.csv')

# 특정 카테고리를 메인 데이터에서 분리하여 별도 분석 데이터셋 생성
df_special = df_base[df_base['category_class'] == 'Special_Domain_A'] # 기존 특정 도메인 분류
df_normal = df_base[df_base['category_class'] != 'Special_Domain_A']

df_normal[['product_id', 'product_name']].to_csv('product_list_normal.csv', index=False)
df_special[['product_id', 'product_name']].to_csv('product_list_special.csv', index=False)

# =====================================================================
# 2. 다중 Depth 카테고리 조합명(Unique Combos) 생성
# =====================================================================
category_master = pd.read_excel('sample_shopping_mall_category.xlsx')

# 존재하는 N차 분류 컬럼을 자동 추출하여 공백 정리
combo_cols = [c for c in ['depth1', 'depth2', 'depth3'] if c in category_master.columns]
cat_df = category_master[combo_cols].copy()

for c in cat_df.columns:
    cat_df[c] = cat_df[c].astype('string').str.strip()

cat_df = cat_df.replace({'': pd.NA}).dropna(how='any')

# 유니크한 카테고리 경로 조합 및 발생 빈도 추출
unique_combos = cat_df.drop_duplicates().reset_index(drop=True)
combo_counts = cat_df.groupby(combo_cols, dropna=False).size().reset_index(name='count')

# =====================================================================
# 3. 특수 도메인 전용 표시명(Display Name) 생성
# =====================================================================
# 2차 분류와 3차 분류를 시각적으로 결합하여 "[2차명]3차명" 형태로 포맷팅
special_cat_df = pd.read_excel('sample_special_domain_category.xlsx')

def make_display_name(row):
    depth2 = str(row.get('depth2_name', '')).strip()
    depth3 = str(row.get('depth3_name', '')).strip()
    
    if depth3 and depth3 != 'nan':
        return f"[{depth2}]{depth3}"
    return depth2

special_cat_df['display_name'] = special_cat_df.apply(make_display_name, axis=1)

# 처리된 특수 도메인 카테고리 포맷 저장
special_cat_df[['display_name']].drop_duplicates().to_csv('formatted_special_category.csv', index=False)
