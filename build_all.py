"""
一键构建知识库:清洗 → 切分 → 向量化入库
用法: python build_all.py
"""

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PY = sys.executable


def run(script: str):
    print(f"\n{'=' * 50}\n▶ {script}\n{'=' * 50}")
    subprocess.run([PY, str(BASE_DIR / "scripts" / script)], check=True)


def main():
    run("clean.py")
    run("01_split_docs.py")
    run("02_build_vectorstore.py")
    print("\n✅ 知识库构建完成!重启服务即可生效。")


if __name__ == "__main__":
    main()
