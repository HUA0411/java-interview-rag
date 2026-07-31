FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

# 模型下载走国内镜像
ENV HF_ENDPOINT=https://hf-mirror.com
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# 启动前先构建向量库(容器里没有持久化的 vectorstore),再起服务
CMD ["sh", "-c", "python scripts/02_build_vectorstore.py && cd app && python -m uvicorn main:app --host 0.0.0.0 --port 8000"]
