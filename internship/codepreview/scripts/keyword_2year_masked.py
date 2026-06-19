import pandas as pd
import re
import unicodedata
import itertools

"""
[2년치 데이터 상품명 정규화 및 키워드 매핑 파이프라인]
상품명(name)과 규격(spec) 텍스트를 자연어 처리(NLP) 기법으로 정규화하고,
중복되거나 포함 관계에 있는 유사 상품명을 하나의 그룹으로 묶습니다.
또한 수동 검수를 위해 엑셀 파일로 색상을 입혀 추출합니다.
"""

# =====================================================================
# 1. 데이터 로드 및 유효 키워드 필터링
# =====================================================================
df_base = pd.read_csv('2year_data_cleaned.csv')
keyword_code = pd.read_csv('sample_keyword_code.csv')
keyword_mapping = pd.read_csv('sample_keyword_mapping.csv')

# 키워드 마스터 정보 병합
keyword = keyword_mapping.merge(keyword_code, on='keyword_code', how='left')

# 특정 유효 키워드 타입('A', 'G')만 사용
invalid_keyword = keyword[~keyword['keyword_type'].isin(['A', 'G'])]
invalid_order_list = invalid_keyword['order_id'].dropna().unique()

use_keyword = keyword[~keyword['order_id'].isin(invalid_order_list)].copy()
keyword_has = use_keyword[['order_id', 'use_yn']].drop_duplicates(subset=['order_id'])

# 베이스 데이터와 유효 키워드 데이터 내부 조인
df_merge = df_base.merge(keyword_has, on='order_id', how='inner')

# =====================================================================
# 2. 상품명 + 규격 조합 고유 키(Group Key) 생성
# =====================================================================
df_merge['product_key'] = df_merge.groupby(['product_name', 'product_spec'], dropna=False).ngroup()

df_product = (
    df_merge[['product_key', 'product_name', 'product_spec']]
    .drop_duplicates()
    .sort_values('product_key')
    .reset_index(drop=True)
)

# =====================================================================
# 3. 텍스트 정규화 (Normalization)
# =====================================================================
def normalize_text(s: pd.Series) -> pd.Series:
    return (
        s.fillna('')
         .str.normalize('NFKC')               # 전각/반각 통일
         .str.strip()
         .str.lower()                         # 소문자 변환
         .str.replace(r'[\"\'“”‘’]', '', regex=True) # 따옴표 제거
         .str.replace(r'[^0-9a-z가-힣/()*+\-\. ]', '', regex=True) # 불필요 특문 제거
    )

df_product['name_norm'] = normalize_text(df_product['product_name'])
df_product['spec_norm'] = normalize_text(df_product['product_spec'])

# 물리적 단위(ml, kg 등) 및 앞선 숫자 제거 로직 적용
unit_tokens = r'(ml|l|cm|mm|kg|g)'
pattern = re.compile(rf'(\d+)\s+(?={unit_tokens}\b)', flags=re.IGNORECASE)

for col in ['name_norm', 'spec_norm']:
    df_product[col] = df_product[col].fillna('').str.replace(pattern, r'\1', regex=True)

# 규격에서 상품명과 중복되는 단어 토큰 제거
def drop_name_tokens_from_std(row):
    name_tokens = set(str(row['name_norm'] or '').split())
    std_tokens  = set(str(row['spec_norm'] or '').split())
    kept = [t for t in std_tokens if t not in name_tokens]
    return ' '.join(kept).strip()

df_product['spec_norm_clean'] = df_product.apply(drop_name_tokens_from_std, axis=1)

# =====================================================================
# 4. 문자열 포함 관계 기반의 유사 상품명 그룹핑
# =====================================================================
df_product['combined_norm'] = df_product['name_norm'] + df_product['spec_norm_clean']
df_product['combined_norm'] = df_product['combined_norm'].str.replace(r'\s+', '', regex=True)

# 그룹핑을 위해 가장 긴 문자열을 대표값으로 채택
counts = df_product['combined_norm'].value_counts()
longest_idx = df_product.groupby('combined_norm')['product_name'].apply(lambda s: s.str.len().idxmax())
longest_map = df_product.loc[longest_idx, ['combined_norm', 'product_name']].set_index('combined_norm')['product_name']

df_product['result_base'] = df_product['product_name']
mask_dup = df_product['combined_norm'].map(counts) >= 2
df_product.loc[mask_dup, 'result_base'] = df_product.loc[mask_dup, 'combined_norm'].map(longest_map)

# =====================================================================
# 5. 수동 검수용 엑셀 파일 시각화(Coloring) 및 추출
# =====================================================================
df_final_export = df_product[['product_key', 'product_name', 'result_base']].copy()
df_final_export = df_final_export.rename(columns={'result_base': 'final_normalized_name'})

# 검수용 빈 컬럼 추가
df_final_export['check'] = ''
df_final_export['note'] = ''

# 그룹 단위로 파스텔 톤 색상을 부여하여 엑셀 저장
outfile = 'product_list_for_review_colored.xlsx'
palette = ['#ffe0b2', '#bbdefb', '#f8bbd0', '#d1c4e9', '#fff9c4', '#cfd8dc']

unique_norms = df_final_export['final_normalized_name'].dropna().unique()
color_map = dict(zip(unique_norms, itertools.islice(itertools.cycle(palette), len(unique_norms))))

with pd.ExcelWriter(outfile, engine='xlsxwriter') as writer:
    df_final_export.to_excel(writer, index=False, sheet_name='Sheet1')
    wb = writer.book
    ws = writer.sheets['Sheet1']

    for r, norm_val in enumerate(df_final_export['final_normalized_name'], start=1):
        color = color_map.get(norm_val)
        if color:
            fmt = wb.add_format({'bg_color': color})
            for c in range(len(df_final_export.columns)):
                ws.write(r, c, df_final_export.iloc[r-1, c], fmt)

print(f"검수용 파일 생성 완료: {outfile}")
