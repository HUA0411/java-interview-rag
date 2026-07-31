"""
步骤4: RAG 问答(命令行版)—— 检索 + 组装 prompt + 大模型生成
用法: python scripts/04_rag_answer.py "你的问题"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from hybrid_search import HybridSearcher
from rag_engine import ask_llm, build_prompt, load_env


def main():
    load_env()
    question = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("请输入问题: ")

    print(f"❓ 问题: {question}\n")

    searcher = HybridSearcher()
    hits = searcher.search(question, top_k=3)

    print(f"📚 检索到 {len(hits)} 份资料:")
    for i, hit in enumerate(hits, 1):
        print(f"   [{i}] {hit['title']}")

    print("\n🤖 大模型生成中 ...\n")
    answer = ask_llm(build_prompt(question, hits))
    print("--- 回答 ---")
    print(answer)


if __name__ == "__main__":
    main()
