"""
RAG 引擎公共模块:prompt 组装 + LLM 调用
供 04_rag_answer.py(命令行)和 app/main.py(FastAPI)复用
"""

import os
from pathlib import Path

import requests

API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"


def load_env():
    """极简 .env 读取(不依赖第三方库)"""
    env_file = Path(__file__).resolve().parent.parent / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


def build_prompt(question: str, hits: list[dict]) -> str:
    """组装 prompt:资料带编号引用,强制基于资料回答(防幻觉)"""
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


def _call_api(prompt: str, api_key: str, stream: bool, timeout: int = 60) -> requests.Response:
    """DeepSeek API 公共调用(OpenAI 兼容协议)"""
    return requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "stream": stream,
        },
        stream=stream,
        timeout=timeout,
    )


def ask_llm(prompt: str, api_key: str = None, timeout: int = 60) -> str:
    """调用 DeepSeek API,一次性返回完整回答"""
    api_key = api_key or os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("未找到 DEEPSEEK_API_KEY,请检查 .env 文件")

    resp = _call_api(prompt, api_key, stream=False, timeout=timeout)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def ask_llm_stream(prompt: str, api_key: str = None, timeout: int = 120):
    """
    流式调用:逐块 yield 回答增量文本(生成器)。
    大模型不是一次性吐完,而是像打字一样逐个 token 返回,
    SSE 格式: data: {"choices":[{"delta":{"content":"..."}}]}\n
    """
    api_key = api_key or os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("未找到 DEEPSEEK_API_KEY,请检查 .env 文件")

    resp = _call_api(prompt, api_key, stream=True, timeout=timeout)
    resp.raise_for_status()

    for line in resp.iter_lines():
        if not line:
            continue
        line = line.decode("utf-8", errors="ignore")
        if not line.startswith("data: "):
            continue
        data = line[6:].strip()
        if data == "[DONE]":
            break
        try:
            import json
            delta = json.loads(data)["choices"][0]["delta"].get("content", "")
        except (json.JSONDecodeError, KeyError, IndexError):
            continue
        if delta:
            yield delta
