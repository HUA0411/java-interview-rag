# 💼 Java 面试知识库智能问答系统(RAG)

基于 **RAG(检索增强生成)** 的 Java 面试知识库问答系统。内置 20 道高频 Java 面试题知识库,支持提问并返回**带出处引用**的回答。

## ✨ 功能特性

- 🔍 **混合检索**:BM25 关键词检索 + BGE 向量语义检索 + RRF 排名融合
- 🧠 **大模型生成**:DeepSeek API 基于检索资料生成回答,防幻觉提示词,回答可溯源
- 🌐 **Web 服务**:FastAPI 提供 REST API + 内置简洁前端页面
- 🐳 **可部署**:Docker 镜像一键构建,可部署到任意云平台

## 🏗️ 系统架构

```
用户提问
   │
   ▼
┌───────────────────── 检索阶段 ─────────────────────┐
│  问题向量化(bge-small-zh) ──┐                     │
│  问题分词(jieba) ──┐        │                     │
│   ┌──────┴──────┐  │        │                     │
│   │ 向量检索     │  │        │                     │
│   │ (ChromaDB)  │──┴─ RRF 融合 ──► top-k 文本块    │
│   │ BM25 检索    │                               │
│   └──────┬──────┘                               │
└──────────┼───────────────────────────────────────┘
           ▼
┌───────────────────── 生成阶段 ─────────────────────┐
│  Prompt 组装(问题 + 参考资料 + 防幻觉规则)          │
│  DeepSeek API ──► 带 [参考资料N] 标注的回答          │
└───────────────────────────────────────────────────┘
```

## 📁 项目结构

```
java-interview-rag/
├── data/
│   ├── java_questions/      # 知识库原始文档(可替换/扩充)
│   └── vectorstore/         # ChromaDB 向量库(脚本生成)
├── scripts/
│   ├── 01_split_docs.py     # 步骤1: 文档解析与切分
│   ├── 02_build_vectorstore.py  # 步骤2: 向量化 + 入库
│   ├── hybrid_search.py     # 步骤3: 混合检索服务(向量+BM25+RRF)
│   ├── rag_engine.py        # 公共模块: prompt组装 + LLM调用
│   └── 04_rag_answer.py     # 步骤4: 命令行问答
├── app/
│   ├── main.py              # FastAPI 后端
│   └── static/index.html    # 前端页面
├── requirements.txt
├── Dockerfile
└── .env                     # DEEPSEEK_API_KEY=sk-xxx (勿提交)
```

## 🚀 快速开始

### 0. 前置条件

- Python 3.10+、Git
- DeepSeek API Key:https://platform.deepseek.com → API Keys → 创建

### 1. 安装与配置

```bash
git clone <你的仓库地址> && cd java-interview-rag
python -m venv .venv

# Windows
.venv\Scripts\pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# macOS/Linux
.venv/bin/pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 配置密钥(写入 .env,已被 .gitignore 忽略)
echo "DEEPSEEK_API_KEY=sk-你的key" > .env
```

### 2. 构建知识库(首次运行自动下载中文嵌入模型,约100MB)

```bash
# Windows
.venv\Scripts\python scripts\02_build_vectorstore.py
# macOS/Linux
HF_ENDPOINT=https://hf-mirror.com .venv/bin/python scripts/02_build_vectorstore.py
```

### 3. 命令行问答

```bash
.venv\Scripts\python scripts\04_rag_answer.py "Spring 事务什么时候会失效?"
```

### 4. 启动 Web 服务

```bash
cd app
# Windows
..\.venv\Scripts\python -m uvicorn main:app --port 8000
# macOS/Linux
HF_ENDPOINT=https://hf-mirror.com ../.venv/bin/python -m uvicorn main:app --port 8000
```

打开 http://localhost:8000 即可使用网页版问答。

## 📡 API 文档

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/health` | 健康检查,返回索引文档数 |
| POST | `/api/ask` | 问答接口,请求 `{"question": "...", "top_k": 3}` |
| GET | `/` | 前端页面 |

调用示例:

```bash
curl -X POST http://localhost:8000/api/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "什么是缓存雪崩?"}'
```

响应:

```json
{
  "answer": "根据参考资料,缓存雪崩是指... [参考资料1]",
  "sources": ["15. 什么是缓存穿透、击穿、雪崩?", "..."]
}
```

## 🐳 Docker 部署

```bash
docker build -t java-interview-rag .
docker run -d -p 8000:8000 -e DEEPSEEK_API_KEY=sk-你的key java-interview-rag
```

部署到云平台(Railway / Render / 云服务器):
1. 推送镜像到镜像仓库,或直接在平台构建
2. 设置环境变量 `DEEPSEEK_API_KEY`
3. 分配公网地址,即可获得线上 demo 链接

## 📚 扩充知识库

往 `data/java_questions/` 放入 `.md` 或 `.pdf` 文档(建议用 `##` 标题分节),重新运行:

```bash
.venv\Scripts\python scripts\01_split_docs.py   # 重新切分
.venv\Scripts\python scripts\02_build_vectorstore.py  # 重新入库
```

## 🛠️ 技术栈

Python · FastAPI · ChromaDB · BGE(bge-small-zh-v1.5) · BM25(rank_bm25 + jieba) · DeepSeek API · Docker

## ⚠️ 安全说明

- `.env` 存放 API Key,已被 `.gitignore` 忽略,**切勿提交**。
- Docker 部署时通过环境变量注入密钥,不写入镜像。
