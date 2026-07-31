"""
步骤2: 向量化 + 存入向量库
输入: data/chunks.json(步骤1产出)
输出: data/vectorstore/(ChromaDB 持久化目录)

链路: 文本块 → bge中文嵌入模型转成向量 → 存入 ChromaDB
验证: 随机抽一个问题,检索 top-3,观察返回的块和相似度
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CHUNKS_FILE = DATA_DIR / "chunks.json"
VECTORSTORE_DIR = DATA_DIR / "vectorstore"

# 中文嵌入模型:国产开源,效果对标 OpenAI 的 text-embedding,可免费本地跑
EMBED_MODEL = "BAAI/bge-small-zh-v1.5"


def load_chunks():
    with open(CHUNKS_FILE, encoding="utf-8") as f:
        return json.load(f)


def build():
    chunks = load_chunks()
    print(f"加载 {len(chunks)} 个文本块")

    # 第一次运行会自动下载模型(约 100MB),之后走本地缓存
    from sentence_transformers import SentenceTransformer
    print(f"加载嵌入模型 {EMBED_MODEL} ...")
    model = SentenceTransformer(EMBED_MODEL)

    # 批量编码:一条文本 → 一个向量,normalize_embeddings 让相似度计算用点积即可(等价余弦)
    texts = [c["text"] for c in chunks]
    print(f"编码 {len(texts)} 条文本为向量 ...")
    vectors = model.encode(texts, normalize_embeddings=True, show_progress_bar=True)

    # 存向量库
    import chromadb
    client = chromadb.PersistentClient(path=str(VECTORSTORE_DIR))
    collection = client.get_or_create_collection(
        name="java_interview",
        metadata={"hnsw:space": "cosine"},  # 用余弦相似度衡量距离
    )

    # upsert:文本、向量、元数据(出处信息)一起存
    collection.upsert(
        ids=[c["id"] for c in chunks],
        embeddings=vectors.tolist(),
        documents=[c["text"] for c in chunks],
        metadatas=[{"title": c["title"], "source": c["source"]} for c in chunks],
    )
    print(f"完成!共存入 {collection.count()} 条到 {VECTORSTORE_DIR}")


def verify():
    """验证:模拟用户提问,检索 top-3 看看召回质量"""
    from sentence_transformers import SentenceTransformer
    import chromadb

    client = chromadb.PersistentClient(path=str(VECTORSTORE_DIR))
    collection = client.get_collection("java_interview")

    model = SentenceTransformer(EMBED_MODEL)

    questions = [
        "Spring 事务什么时候会失效?",
        "HashMap 底层是怎么实现的?",
        "什么是缓存雪崩?",
    ]
    for q in questions:
        # 问题 → 向量 → 在库里找最相似的 3 块
        q_vec = model.encode([q], normalize_embeddings=True)
        results = collection.query(query_embeddings=q_vec.tolist(), n_results=3)
        print(f"\n❓ 问题: {q}")
        for i, (doc, meta, dist) in enumerate(
            zip(results["documents"][0], results["metadatas"][0], results["distances"][0])
        ):
            # ChromaDB 的 cosine 距离 = 1 - 相似度,所以相似度 = 1 - dist
            print(f"  #{i+1} 相似度 {1-dist:.3f} | {meta['title']}")
            print(f"     {doc[:60]}...")


if __name__ == "__main__":
    build()
    verify()
