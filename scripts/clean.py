"""
数据清洗:爬虫采集内容的后处理(采集 → 清洗 → 切分 → 入库)

处理 data/collected/ 下的 markdown:
  1. 行级清洗:删除噪音行(评论区/广告/版权模板/无效字符)
  2. 格式规范化:压缩多余空行、清理残留HTML标签、全角空格
  3. 内容去重:完全相同/高度相似的文件只保留一份
  4. 质量过滤:过短、无有效内容的文件删除

用法: python scripts/clean.py
"""

import hashlib
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
COLLECTED_DIR = BASE_DIR / "data" / "collected"

MIN_FILE_LEN = 150          # 文件正文少于该字数视为无效
NOISE_RE = re.compile(
    r"^(comments?|评论(区)?|相关推荐|推荐文章|广告|推广|分享到|点赞|打赏|"
    r"copyright|©|all rights reserved|版权所有|沪ICP|粤ICP|备案号|"
    r"扫码|微信扫一扫|关注我们|订阅我们|返回顶部|上一页|下一页|目录|"
    r"cookie|隐私政策|使用条款|转载声明|未经许可)[^一-鿿]*$",
    re.IGNORECASE,
)
HTML_TAG_RE = re.compile(r"<[^>]+>")


def clean_text(text: str) -> tuple[str, int]:
    """清洗单篇文档,返回 (清洗后文本, 删除的噪音行数)"""
    lines = text.splitlines()
    kept = []
    removed = 0

    for line in lines:
        s = line.strip()
        # 1. 噪音行:短小且命中噪音词
        if len(s) <= 40 and NOISE_RE.match(s):
            removed += 1
            continue
        # 2. 残留 HTML 标签(某些网站正文里混入)
        if HTML_TAG_RE.search(s) and not s.startswith("```"):
            s = HTML_TAG_RE.sub("", s).strip()
            if not s:
                removed += 1
                continue
        # 3. 乱码/异常字符
        if "�" in s:          # U+FFFD 替换符 = 解码乱码
            removed += 1
            continue
        kept.append(s)

    # 4. 压缩多余空行(最多连续2行)
    out = []
    blank = 0
    for s in kept:
        if not s:
            blank += 1
            if blank >= 2:
                continue
        else:
            blank = 0
        out.append(s)
    return "\n".join(out).strip(), removed


def clean_file(path: Path) -> tuple[int, int]:
    """清洗单文件,返回 (删除行数, 清洗后长度)"""
    text = path.read_text(encoding="utf-8", errors="replace")
    cleaned, removed = clean_text(text)
    path.write_text(cleaned, encoding="utf-8")
    return removed, len(cleaned)


def main():
    if not COLLECTED_DIR.exists():
        print("没有 collected/ 目录,无需清洗")
        return

    files = list(COLLECTED_DIR.rglob("*.md"))
    print(f"发现 {len(files)} 个采集文件,开始清洗 ...\n")

    # 第一遍:逐文件清洗 + 质量过滤
    cleaned_files = []
    total_removed = 0
    for path in sorted(files):
        removed, length = clean_file(path)
        total_removed += removed
        if length < MIN_FILE_LEN:
            print(f"  ✗ 删除(内容过短 {length}字): {path.name}")
            path.unlink()
        else:
            cleaned_files.append(path)
            print(f"  ✓ {path.name}: 删噪音行 {removed} 条 → {length} 字")

    # 第二遍:内容去重(相同内容文件只留一份)
    seen_hashes: dict[str, Path] = {}
    dup_removed = 0
    for path in cleaned_files:
        digest = hashlib.md5(path.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
        if digest in seen_hashes:
            print(f"  ✗ 删除(重复内容): {path.name} == {seen_hashes[digest].name}")
            path.unlink()
            dup_removed += 1
        else:
            seen_hashes[digest] = path

    print(f"\n清洗完成: 删除噪音行 {total_removed} 条, 去重 {dup_removed} 个, 有效文件 {len(cleaned_files) - dup_removed} 个")
    print("下一步: python scripts/01_split_docs.py && python scripts/02_build_vectorstore.py")


if __name__ == "__main__":
    main()
