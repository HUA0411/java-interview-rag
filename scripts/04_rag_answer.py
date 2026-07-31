"""
步骤4: RAG 问答 —— 检索 + 组装 prompt + 大模型生成
这是 RAG 的"增强"环节:把查到的资料和问题拼成 prompt,让大模型基于资料回答。

输入: 用户问题(命令行参数或交互输入)
输出: 大模型回答 + 参考来源列表

用法: python scripts/04_rag_answer.py "你的问题"
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import requests
from hybrid_search import HybridSearcher

# ---------- 配置 ----------
API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"


def load_env():
    """极简 .env 读取(不依赖第三方库):DEEPSEEK_API_KEY=sk-xxx"""
    env_file = Path(__file__).resolve().parent.parent / ".env"
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


def build_prompt(question: str, hits: list[dict]) -> str:
    """
    组装 prompt:【参考资料】+【用户问题】
    关键设计:
    1. 资料带标题编号,回答时模型可以引用
    2. 明确告知模型:只基于资料回答,资料不足要明说 —— 这就是"防幻觉"
    """
    refs = "\n\n".join(
        f"[参考资料{i + 1} | 标题:{hit['title']}]\n{hit['text']}"
        for i, hit in enumerate(hits)
    )
    return (
        "你是 Java 面试辅导助手。请严格基于以下参考资料回答用户问题。\n"
        "规则:\n"
        "1. 只使用参考资料中的信息,不要编造资料里没有的内容\n"
        "2. 如果参考资料不足以回答,请明确说明'资料中没有找到相关信息'\n"
        "3. 回答时如果引用了某份资料,用 [参考资料N] 标注\n\n"
        f"【参考资料】\n{refs}\n\n"
        f"【用户问题】\n{question}"
    )


def ask_llm(prompt: str, api_key: str) -> str:
    """调用 DeepSeek API(OpenAI 兼容协议)"""
    resp = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,  # 低温度:让回答更忠实于资料,减少自由发挥
            "stream": False,
        },
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def main():
    load_env()
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("错误: 未找到 DEEPSEEK_API_KEY,请检查 .env 文件")
        sys.exit(1)

    # 支持命令行传参,也支持交互输入
    question = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("请输入问题: ")

    print(f"❓ 问题: {question}\n")

    searcher = HybridSearcher()
    hits = searcher.search(question, top_k=3)

    print(f"📚 检索到 {len(hits)} 份资料:")
    for i, hit in enumerate(hits, 1):
        print(f"   [{i}] {hit['title']}")

    print("\n🤖 大模型生成中 ...\n")
    prompt = build_prompt(question, hits)
    answer = ask_llm(prompt, api_key)
    print("--- 回答 ---")
    print(answer)


if __name__ == "__main__":
    main()
