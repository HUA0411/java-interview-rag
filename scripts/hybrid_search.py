"""
步骤3: 混合检索服务(向量 + BM25 + RRF 融合)
供后续 LLM 接入、FastAPI 复用:from scripts.hybrid_search import HybridSearcher

为什么混合:
- 向量检索:语义匹配强,但长文本相似度被稀释、同义词权重不敏感
- BM25:   关键词精确命中,但不懂语义
- RRF:    只看排名融合,免疫两种算法分数尺度不同的差异
"""

import json
import sys
from pathlib import Path

import chromadb
import jieba
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
VECTORSTORE_DIR = DATA_DIR / "vectorstore"

EMBED_MODEL = "BAAI/bge-small-zh-v1.5"
K1, B, TOP_K = 1.5, 0.75, 5   # BM25 标准参数 + 默认返回条数

import re

# 停用词:无检索价值的高频词(注意:显式写多字词,不能用 set("字符串") 那样会被拆成单字)
STOPWORDS = {
    "的", "了", "是", "么", "吗", "呢", "啊", "呀", "吧", "着", "过",
    "怎么", "什么", "为什么", "怎样", "哪个", "哪些", "如何",
    "一个", "一种", "一些", "有", "没有", "用", "在", "与", "和", "或", "跟", "及",
    "等", "还", "也", "都", "就", "这", "那", "不", "要", "能", "会", "为", "对",
}

def tokenize(text: str) -> list[str]:
    """jieba 分词 + 过滤停用词和纯标点。英文专有名词(HashMap/JDK)原样保留。"""
    tokens = []
    for w in jieba.cut(text):
        w = w.strip()
        if not w:
            continue
        # 纯标点/符号词(如 '-', ',', ';', '/')无检索价值
        if not re.search(r"[\w一-鿿]", w):
            continue
        if w in STOPWORDS:
            continue
        tokens.append(w)
    return tokens


class HybridSearcher:
    def __init__(self):
        print("初始化检索服务 ...")
        # 1. 加载向量库
        self.client = chromadb.PersistentClient(path=str(VECTORSTORE_DIR))
        self.collection = self.client.get_collection("java_interview")
        # 2. 加载嵌入模型(问题也要转成向量)
        self.model = SentenceTransformer(EMBED_MODEL)
        # 3. 重建 BM25 索引:把库里所有文档取出来做分词
        self.docs = self.collection.get(include=["documents", "metadatas"])
        self.doc_ids = self.docs["ids"]          # ChromaDB 的 id 是独立字段
        self.doc_texts = self.docs["documents"]
        self.doc_metas = self.docs["metadatas"]
        # 中文分词 + 停用词过滤后建索引
        tokenized = [tokenize(t) for t in self.doc_texts]
        self.bm25 = BM25Okapi(tokenized)
        print(f"就绪: 向量库 {self.collection.count()} 条, BM25 索引 {len(self.doc_texts)} 条")

    def _vector_search(self, query: str, top_k: int):
        q_vec = self.model.encode([query], normalize_embeddings=True)
        results = self.collection.query(
            query_embeddings=q_vec.tolist(), n_results=top_k,
            include=["documents", "metadatas", "distances"],
        )
        out = []
        for doc_id, doc, meta, dist in zip(
            results["ids"][0], results["documents"][0],
            results["metadatas"][0], results["distances"][0],
        ):
            out.append({"id": doc_id, "text": doc, "title": meta["title"], "score": 1 - dist})
        return out

    def _bm25_search(self, query: str, top_k: int):
        tokens = tokenize(query)
        if not tokens:
            return []
        scores = self.bm25.get_scores(tokens)
        # 按分数降序取 top-k,score=0 的(完全没命中关键词)不要
        ranked = sorted(
            (i for i, s in enumerate(scores) if s > 0),
            key=lambda i: scores[i], reverse=True,
        )[:top_k]
        return [
            {
                "id": self.doc_ids[i],
                "text": self.doc_texts[i],
                "title": self.doc_metas[i]["title"],
                "score": float(scores[i]),
            }
            for i in ranked
        ]

    @staticmethod
    def _rrf_fuse(list1, list2, k=60):
        """RRF 融合:分数 = Σ 1/(k + 排名)。只看排名,不看原始分数。"""
        score_map = {}
        for lst in (list1, list2):
            for rank, item in enumerate(lst):
                score_map.setdefault(item["id"], {"item": item, "score": 0.0})
                score_map[item["id"]]["score"] += 1.0 / (k + rank + 1)
        fused = sorted(score_map.values(), key=lambda v: v["score"], reverse=True)
        return [v["item"] for v in fused]

    def search(self, query: str, top_k: int = TOP_K):
        """混合检索入口:向量 + BM25 → RRF 融合 → top_k"""
        vector_hits = self._vector_search(query, top_k=top_k * 2)
        bm25_hits = self._bm25_search(query, top_k=top_k * 2)
        return self._rrf_fuse(vector_hits, bm25_hits)[:top_k]


def demo():
    """对比纯向量 vs 混合检索的召回效果"""
    searcher = HybridSearcher()
    questions = [
        "Spring 事务什么时候会失效?",
        "HashMap 底层是怎么实现的?",
        "什么是缓存雪崩?",
    ]
    for q in questions:
        print(f"\n❓ {q}")
        for rank, hit in enumerate(searcher.search(q), 1):
            print(f"  #{rank} [{hit['title']}]")


if __name__ == "__main__":
    demo()
