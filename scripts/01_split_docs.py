"""
步骤1: 文档解析 + 切分
输入: data/java_questions/ 下的 .md 或 .pdf 文档(任意领域,知识库不关心内容)
输出: data/chunks.json —— 切分好的文本块列表 [{id, title, text, source}]

为什么这样切:
1. 按 Markdown 标题(##)切 —— 每个问题自带语义边界
2. 超长块按字数二次切分 + 重叠(overlap),避免语义断裂
3. 保留标题作为每块的"上下文",检索命中时方便溯源
"""

import json
import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
OUTPUT = DATA_DIR / "chunks.json"

# 知识库来源目录:手工文档 + 爬虫采集,都会进入切分
SOURCE_DIRS = [DATA_DIR / "java_questions", DATA_DIR / "collected"]

CHUNK_SIZE = 400      # 每块目标字符数
CHUNK_OVERLAP = 50    # 相邻块重叠字符数
MIN_CHUNK_LEN = 20    # 过滤过短的杂质块(如纯标题、空行)


def parse_pdf(path: Path) -> list[dict]:
    """PDF 解析:按页提取文本,每页作为一个 section(标题为页码)"""
    import fitz  # PyMuPDF

    sections = []
    doc = fitz.open(path)
    for page_num in range(len(doc)):
        text = doc[page_num].get_text().strip()
        if text:
            sections.append({"title": f"第{page_num + 1}页", "content": text})
    doc.close()
    return sections


def parse_markdown(text: str) -> list[dict]:
    """按 Markdown 二级标题把文档切成若干小节,返回 [{title, content}]"""
    sections = []
    current_title = "未分类"
    current_lines = []

    for line in text.splitlines():
        # 匹配 "## xxx" 形式的二级标题
        m = re.match(r"^##\s+(.+)$", line.strip())
        if m:
            # 遇到新标题,把上一节收尾
            if current_lines:
                sections.append({"title": current_title, "content": "\n".join(current_lines)})
            current_title = m.group(1)
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        sections.append({"title": current_title, "content": "\n".join(current_lines)})
    return sections


def split_long_section(title: str, content: str, source: str) -> list[dict]:
    """超长小节按字数二次切分,带重叠"""
    chunks = []
    start = 0
    length = len(content)
    idx = 0
    while start < length:
        end = min(start + CHUNK_SIZE, length)
        chunk_text = content[start:end].strip()
        if chunk_text:
            chunks.append({
                "id": f"{source}:{title}:{idx}",
                "title": title,
                "text": chunk_text,
                "source": source,
            })
            idx += 1
        # 下一个块的起点向前挪 CHUNK_OVERLAP 个字符,实现重叠
        if end >= length:
            break
        start = end - CHUNK_OVERLAP
    return chunks


def main():
    all_chunks = []
    doc_files = []
    for src_dir in SOURCE_DIRS:
        if src_dir.exists():
            # rglob 递归:collected/ 下有按域名分的子目录
            doc_files += list(src_dir.rglob("*.md")) + list(src_dir.rglob("*.pdf"))

    for doc_file in sorted(doc_files):
        print(f"解析 {doc_file} ...")
        if doc_file.suffix.lower() == ".pdf":
            sections = parse_pdf(doc_file)
        else:
            sections = parse_markdown(doc_file.read_text(encoding="utf-8"))
        # 来源标识:目录名/文件名,区分手工文档与不同爬虫来源
        source = f"{doc_file.parent.name}/{doc_file.name}"
        for sec in sections:
            content = sec["content"].strip()
            # 数据清洗:跳过纯标题、空内容等杂质块
            if len(content) < MIN_CHUNK_LEN:
                continue
            if len(content) <= CHUNK_SIZE:
                # 短小节:整块保留
                all_chunks.append({
                    "id": f"{source}:{sec['title']}:0",
                    "title": sec["title"],
                    "text": content,
                    "source": source,
                })
            else:
                # 长小节:二次切分
                all_chunks.extend(split_long_section(sec["title"], content, source))

    # id 必须全局唯一:同一文档内可能出现重复标题(如多个"实例代码"小节),
    # 用全局序号保证唯一性(ChromaDB 按 id upsert,重复 id 会报错)
    for i, chunk in enumerate(all_chunks):
        chunk["id"] = f"{chunk['source']}:{chunk['title']}:{i}"

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(json.dumps(all_chunks, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"完成!共生成 {len(all_chunks)} 个文本块,保存到 {OUTPUT}")


if __name__ == "__main__":
    main()
