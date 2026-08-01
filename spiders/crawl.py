"""
通用网页爬虫:把网页正文转成 markdown,供知识库入库
输出: data/collected/<域名>/<页面标题>.md

三种用法:
  1. 单个 URL:    python spiders/crawl.py --url https://example.com/page
  2. URL 列表:    python spiders/crawl.py --file urls.txt (每行一个URL)
  3. 种子抓取:    python spiders/crawl.py --seed https://example.com --max-pages 10
                  (自动抓取同域名下所有链接,深度1层)

设计要点:
  - 正文提取:密度算法(统计<p>/<li>等文本块长度,去掉导航/广告等噪音)
  - 转 markdown:保留 h2/h3 标题结构(与切分脚本的 ## 约定对齐)
  - 基本礼貌:浏览器 UA、请求间隔 delay 秒、只抓 https
"""

import argparse
import re
import time
import urllib.parse
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "collected"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
}

# 这些标签是"正文信号":文本块在这些标签里才算正文内容
CONTENT_TAGS = {"p", "li", "h1", "h2", "h3", "h4", "pre", "blockquote", "td", "th"}
# 这些容器里的内容基本是导航/广告/脚本,直接剔除
SKIP_SELECTORS = [
    "script", "style", "nav", "footer", "header", "aside", "form",
    ".ad", ".ads", ".advertisement", ".sidebar", ".menu", ".nav",
    "[class*=nav]", "[class*=ad-]", "[id*=ad-]",
]


def fetch(url: str, timeout: int = 15) -> str:
    """下载页面,失败抛异常"""
    resp = requests.get(url, headers=HEADERS, timeout=timeout)
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding or "utf-8"
    return resp.text


def extract_content(html: str) -> tuple[str, str]:
    """
    正文提取:返回 (页面标题, markdown 正文)
    策略:去掉噪音节点后,按标签层次输出 markdown
    """
    soup = BeautifulSoup(html, "lxml")
    for sel in SKIP_SELECTORS:
        for node in soup.select(sel):
            node.decompose()

    title = soup.title.get_text(strip=True) if soup.title else "untitled"

    lines: list[str] = []
    # 按文档顺序遍历正文信号标签
    for el in soup.find_all(CONTENT_TAGS):
        text = el.get_text(" ", strip=True)
        if not text or len(text) < 8:      # 过滤空块和太短的无意义块
            continue
        # 去掉只剩标点/装饰字符的噪音
        if not re.search(r"[\w一-鿿]", text):
            continue
        tag = el.name
        if tag.startswith("h"):
            lines.append(f"\n## {text}")   # 标题统一成 ##,与切分脚本约定一致
        elif tag == "li":
            lines.append(f"- {text}")
        elif tag == "pre":
            lines.append(f"\n```\n{el.get_text()}\n```")
        else:
            lines.append(text)
    return title, "\n".join(lines)


def save_md(title: str, content: str, source_url: str, domain: str) -> Path:
    """保存为 markdown 文件,返回路径"""
    # 文件名:标题清理 + 截断,防路径非法字符
    safe = re.sub(r'[\\/:*?"<>|\r\n]', "_", title)[:60]
    out_dir = OUTPUT_DIR / domain
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{safe}.md"
    if path.exists():
        path = out_dir / f"{safe}_{int(time.time())}.md"
    md = f"# {title}\n\n> 来源: {source_url}\n\n{content}\n"
    path.write_text(md, encoding="utf-8")
    return path


def crawl_url(url: str, delay: float = 1.0) -> Path | None:
    """爬单个 URL → markdown。失败返回 None(不中断批量)"""
    try:
        print(f"  ⬇  {url}")
        html = fetch(url)
    except Exception as e:
        print(f"  ✗  失败: {e}")
        return None
    title, content = extract_content(html)
    if len(content) < 100:
        print(f"  ✗  正文过短({len(content)}字),可能被反爬或页面无内容")
        return None
    path = save_md(title, content, url, urllib.parse.urlparse(url).netloc)
    print(f"  ✓  {path.name} ({len(content)}字)")
    time.sleep(delay)   # 礼貌限速
    return path


def crawl_seed(seed: str, max_pages: int, delay: float):
    """种子抓取:抓首页 → 提取同域名链接 → 逐个抓取"""
    from urllib.parse import urljoin, urlparse

    print(f"种子: {seed}, 目标 {max_pages} 页")
    domain = urlparse(seed).netloc
    html = fetch(seed)
    title, _ = extract_content(html)
    save_md(title + "_index", _extract_index(html), seed, domain)

    soup = BeautifulSoup(html, "lxml")
    links: list[str] = []
    for a in soup.find_all("a", href=True):
        href = urljoin(seed, a["href"])
        u = urlparse(href)
        if u.netloc == domain and u.scheme == "https" and href not in links:
            links.append(href)
    print(f"发现 {len(links)} 个同域名链接,抓取前 {max_pages} 个 ...")

    count = 0
    for link in links:
        if count >= max_pages:
            break
        if crawl_url(link, delay):
            count += 1


def _extract_index(html: str) -> str:
    """种子页正文(首页内容也入库)"""
    soup = BeautifulSoup(html, "lxml")
    for sel in SKIP_SELECTORS:
        for node in soup.select(sel):
            node.decompose()
    return soup.get_text(" ", strip=True)[:2000]


def main():
    parser = argparse.ArgumentParser(description="网页 → markdown 知识库爬虫")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="单个 URL")
    group.add_argument("--file", help="URL 列表文件(每行一个)")
    group.add_argument("--seed", help="种子页,自动抓取同域名链接")
    parser.add_argument("--max-pages", type=int, default=10, help="种子模式最多抓取页数")
    parser.add_argument("--delay", type=float, default=1.0, help="请求间隔秒数")
    args = parser.parse_args()

    print(f"输出目录: {OUTPUT_DIR}\n")
    if args.url:
        crawl_url(args.url, args.delay)
    elif args.file:
        urls = [l.strip() for l in Path(args.file).read_text(encoding="utf-8").splitlines() if l.strip()]
        for u in urls:
            crawl_url(u, args.delay)
    elif args.seed:
        crawl_seed(args.seed, args.max_pages, args.delay)
    print("\n完成!运行 01_split_docs.py + 02_build_vectorstore.py 即可入库。")


if __name__ == "__main__":
    main()
