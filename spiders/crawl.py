"""
通用网页爬虫:把网页正文转成 markdown,供知识库入库
输出: data/collected/<域名>/<页面路径>.md

四种用法:
  1. 单个 URL:    python spiders/crawl.py --url https://example.com/page
  2. URL 列表:    python spiders/crawl.py --file urls.txt (每行一个URL)
  3. 多轮爬取:    python spiders/crawl.py --seed https://example.com/tutorial/
                  --depth 3 --max-pages 50
                  (BFS逐层发现链接,完整爬取整个知识体系)

设计要点:
  - 正文提取:密度算法(统计<p>/<li>等文本块长度,去掉导航/广告等噪音)
  - 转 markdown:保留 h2/h3 标题结构(与切分脚本的 ## 约定对齐)
  - 基本礼貌:浏览器 UA、请求间隔 delay 秒、只抓 https
  - 多轮爬取:URL规范化去重、深度控制、页数上限防失控
"""

import argparse
import re
import time
import urllib.parse
from collections import deque
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

# 明显的非内容链接关键词(登录/注册/下载/分享等),多轮爬取时跳过
SKIP_HREF_RE = re.compile(
    r"(login|logout|register|signin|signup|download|share|weibo|weixin|"
    r"javascript:|mailto:|\.jpg|\.png|\.gif|\.pdf|\.zip|#)", re.IGNORECASE
)


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


def _normalize_url(url: str) -> str:
    """URL 规范化:去 #fragment、去尾斜杠,用于去重"""
    u = urllib.parse.urlparse(url)
    return urllib.parse.urlunparse((u.scheme, u.netloc, u.path.rstrip("/"), "", "", ""))


def _discover_links(html: str, base_url: str, domain: str, path_prefix: str = "") -> list[str]:
    """从页面提取同域名、https、排除噪音的链接(规范化+去重)
    path_prefix: 只保留该路径前缀下的链接,用于限定知识体系范围"""
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    for a in soup.find_all("a", href=True):
        href = urllib.parse.urljoin(base_url, a["href"])
        u = urllib.parse.urlparse(href)
        if u.scheme != "https" or u.netloc != domain:
            continue
        if SKIP_HREF_RE.search(u.path + u.query):
            continue
        if path_prefix and not u.path.startswith(path_prefix):
            continue
        norm = _normalize_url(href)
        if norm not in seen:
            seen.add(norm)
    return list(seen)


def crawl_site(seed: str, max_pages: int, depth: int, delay: float, path_prefix: str = ""):
    """
    多轮 BFS 爬取整个知识体系:
    第1轮爬种子页 → 提取链接入队 → 第2轮爬链接页 → 再发现链接 ……
    直到队列耗尽或达到 max_pages 上限
    """
    from urllib.parse import urlparse

    domain = urlparse(seed).netloc
    scope = f" | 限定路径前缀 {path_prefix}" if path_prefix else ""
    print(f"🌐 多轮爬取: {seed}\n   域名 {domain}{scope} | 深度 {depth} 层 | 上限 {max_pages} 页\n")

    queue: deque[tuple[str, int]] = deque([(seed, 0)])   # (url, 当前深度)
    visited: set[str] = set()
    saved = 0
    failed = 0

    while queue and saved + failed < max_pages:
        url, d = queue.popleft()
        norm = _normalize_url(url)
        if norm in visited:
            continue
        visited.add(norm)

        try:
            print(f"  ⬇ [深度{d}] {url}")
            html = fetch(url)
        except Exception as e:
            print(f"  ✗ 下载失败: {e}")
            failed += 1
            continue

        title, content = extract_content(html)
        if len(content) >= 100:
            # 文件名用 URL 路径,保持体系结构
            path_part = urlparse(url).path.strip("/").replace("/", "_") or "index"
            out_dir = OUTPUT_DIR / domain
            out_dir.mkdir(parents=True, exist_ok=True)
            fname = re.sub(r'[\\/:*?"<>|\r\n]', "_", path_part)[:80]
            (out_dir / f"{fname}.md").write_text(
                f"# {title}\n\n> 来源: {url}\n\n{content}\n", encoding="utf-8"
            )
            saved += 1
            print(f"  ✓ {fname}.md ({len(content)}字) [累计{saved}/{max_pages}]")
        else:
            print(f"  - 正文过短,跳过({len(content)}字)")

        # 发现新链接入队(还有剩余层数才继续)
        if d < depth and saved + failed < max_pages:
            for link in _discover_links(html, url, domain, path_prefix):
                if _normalize_url(link) not in visited:
                    queue.append((link, d + 1))

        time.sleep(delay)

    print(f"\n✅ 爬取结束: 成功 {saved} 页, 失败 {failed} 页, 发现过但未访问 {len(queue)} 个链接")
    print("下一步: python build_all.py (清洗+切分+入库)")


def main():
    parser = argparse.ArgumentParser(description="网页 → markdown 知识库爬虫")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", help="单个 URL")
    group.add_argument("--file", help="URL 列表文件(每行一个)")
    group.add_argument("--seed", help="种子页,多轮爬取整个知识体系")
    parser.add_argument("--depth", type=int, default=2, help="多轮爬取深度(链接的链接)")
    parser.add_argument("--max-pages", type=int, default=30, help="最多抓取页数")
    parser.add_argument("--delay", type=float, default=1.0, help="请求间隔秒数")
    parser.add_argument("--path-prefix", default="", help="只爬该路径前缀下的链接(限定知识体系范围)")
    args = parser.parse_args()

    print(f"输出目录: {OUTPUT_DIR}\n")
    if args.url:
        crawl_url(args.url, args.delay)
    elif args.file:
        urls = [l.strip() for l in Path(args.file).read_text(encoding="utf-8").splitlines() if l.strip()]
        for u in urls:
            crawl_url(u, args.delay)
    elif args.seed:
        crawl_site(args.seed, args.max_pages, args.depth, args.delay, args.path_prefix)
    if not args.seed:
        print("\n完成!运行 build_all.py 清洗+切分+入库即可。")


if __name__ == "__main__":
    main()
