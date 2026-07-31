"""
FastAPI 后端:Java 面试知识库问答系统
- POST /api/ask     问答接口(检索+生成,返回回答和参考来源)
- GET  /api/health  健康检查
- GET  /            静态前端页面

启动: uvicorn main:app --reload --port 8000 (在 app/ 目录下)
"""

import sys
from contextlib import asynccontextmanager
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from hybrid_search import HybridSearcher
from rag_engine import ask_llm, build_prompt, load_env

load_env()

searcher: HybridSearcher = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用启动时加载检索服务(模型加载较慢,启动时一次性初始化)"""
    global searcher
    searcher = HybridSearcher()
    yield


app = FastAPI(title="Java 面试知识库问答", lifespan=lifespan)


class AskRequest(BaseModel):
    question: str
    top_k: int = 3


class Source(BaseModel):
    title: str
    file: str
    snippet: str


class AskResponse(BaseModel):
    answer: str
    sources: list[Source]


@app.get("/api/health")
def health():
    return {"status": "ok", "docs_in_index": searcher.collection.count()}


@app.post("/api/ask", response_model=AskResponse)
def ask(req: AskRequest):
    question = req.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="问题不能为空")
    if len(question) > 200:
        raise HTTPException(status_code=400, detail="问题过长(最多200字)")

    # 检索 → 组装 prompt → 生成
    hits = searcher.search(question, top_k=req.top_k)
    if not hits:
        raise HTTPException(status_code=404, detail="知识库中没有检索到相关内容")

    try:
        answer = ask_llm(build_prompt(question, hits))
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"大模型调用失败: {e}")

    # 来源详情:标题、源文件、内容片段(前端展示可点击的来源卡片)
    sources = [
        Source(
            title=h["title"],
            file=h["id"].split(":")[0] if ":" in h["id"] else h["id"],
            snippet=h["text"][:120],
        )
        for h in hits
    ]
    return AskResponse(answer=answer, sources=sources)


# 静态前端页面(同源托管,无跨域问题)
app.mount("/", StaticFiles(directory=str(Path(__file__).resolve().parent / "static"), html=True), name="static")
