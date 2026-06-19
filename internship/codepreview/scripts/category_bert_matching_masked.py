import pandas as pd
import numpy as np
import re
from sentence_transformers import SentenceTransformer

"""
[BERT 임베딩 기반 카테고리/상품명 유사도 매칭 알고리즘]
자사 상품명과 타사(외부 쇼핑몰) 카탈로그 상품명 간의 의미적 유사도를 측정하기 위해,
다국어 문장 임베딩 AI 모델(SBERT)을 사용하여 코사인 유사도(Cosine Similarity)를 계산하고
가장 유사한 Top-K 후보군을 도출하는 스크립트입니다.
"""

# =====================================================================
# 1. 텍스트 정규화 및 데이터 로드
# =====================================================================
target_mall_df = pd.read_csv('sample_external_catalog.csv') # 타사 카탈로그
internal_df = pd.read_csv('sample_internal_products.csv')   # 자사 상품 마스터

def normalize_product_name(s: str) -> str:
    """기본적인 텍스트 노이즈만 제거하여 임베딩 품질을 높임"""
    if pd.isna(s): return ''
    s = str(s).strip().lower()
    s = re.sub(r"\s+", " ", s) # 다중 공백 제거
    s = s.replace('[', '(').replace(']', ')')
    return s

target_mall_df['name_norm'] = target_mall_df['product_name'].map(normalize_product_name)
internal_df['name_norm'] = internal_df['product_name'].map(normalize_product_name)

# =====================================================================
# 2. 문장 임베딩(Sentence Embedding) 추출
# =====================================================================
# 빠르고 다국어(한국어/영어 혼합) 지원이 잘 되는 경량화 모델 사용
MODEL_NAME = 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'
model = SentenceTransformer(MODEL_NAME)

c_names = target_mall_df['name_norm'].tolist()
b_names = internal_df['name_norm'].tolist()

# normalize_embeddings=True를 주면 내적(Dot Product) 연산이 곧 코사인 유사도가 됨
c_emb = model.encode(c_names, batch_size=256, show_progress_bar=True, normalize_embeddings=True)
b_emb = model.encode(b_names, batch_size=256, show_progress_bar=True, normalize_embeddings=True)

# =====================================================================
# 3. 코사인 유사도 연산 및 Top-K 매칭 (Nearest Neighbors)
# =====================================================================
def topk_cosine_search(query_emb, key_emb, top_k=5):
    """Sklearn을 활용한 K-최근접 이웃(KNN) 유사도 탐색"""
    from sklearn.neighbors import NearestNeighbors
    nn = NearestNeighbors(n_neighbors=top_k, metric='cosine')
    nn.fit(key_emb)
    dist, idx = nn.kneighbors(query_emb, return_distance=True)
    scores = 1.0 - dist # Cosine Distance -> Cosine Similarity 변환
    return scores, idx

SIM_THRESHOLD = 0.80 # 유사도 임계치
TOP_K = 5

scores, indices = topk_cosine_search(b_emb, c_emb, top_k=TOP_K)

# 매칭 결과 테이블 정리
rows = []
for bi in range(len(internal_df)):
    if not b_names[bi]: continue # 이름이 없는 경우 스킵
    
    cand = []
    for rank in range(TOP_K):
        ci = int(indices[bi, rank])
        sc = float(scores[bi, rank])
        cand.append((ci, sc, target_mall_df.loc[ci, 'product_name']))
        
    best_ci, best_sc, best_name = cand[0]
    rows.append({
        'internal_name': internal_df.loc[bi, 'product_name'],
        'best_match_name': best_name,
        'best_score': best_sc,
        'top_k_candidates': ' | '.join([f"{sc:.3f}:{nm}" for (_, sc, nm) in cand])
    })

match_df = pd.DataFrame(rows)

# =====================================================================
# 4. 임계치(Threshold) 기준 매칭 성공/실패 분류
# =====================================================================
matched = match_df[match_df['best_score'] >= SIM_THRESHOLD].copy()
unmatched = match_df[match_df['best_score'] < SIM_THRESHOLD].copy()

print(f"기준 임계치({SIM_THRESHOLD}) 달성 매칭 성공: {len(matched)}건")
print(f"매칭 실패 (수동 검수 필요): {len(unmatched)}건")

matched.to_csv('bert_matched_results.csv', index=False, encoding='utf-8-sig')
unmatched.to_csv('bert_unmatched_review.csv', index=False, encoding='utf-8-sig')
