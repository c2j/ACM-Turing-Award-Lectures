#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在中文译文中已存在的图题占位符/图题行前插入图片引用行。

支持三种图题样式:
  1. 〔图 N:图题〕            (hennessy/aho/clarke/naur/sutherland/tarjan/iverson 等)
  2. > **图 N.** 图题        (milner 的 blockquote 样式)
  3. **图 N. 图题**           (scott 样式)

用法:
    python3 scripts/insert-figures.py <md> <assets_dir> [--skip-missing]

规则:
  - 对每个图号 N,若 zh/assets/<assets_dir>/fig-NN.png 存在,则在图题行前插入
    ![图 N:图题](assets/<assets_dir>/fig-NN.png) 与空行;
  - 图片名按两位编号(fig-01.png ... fig-25.png);
  - --skip-missing: 图号对应 PNG 不存在时跳过(保留原占位符)。
"""
import argparse
import os
import re

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("assets_dir")
    ap.add_argument("--skip-missing", action="store_true")
    args = ap.parse_args()

    lines = open(args.md, encoding="utf-8").read().split("\n")
    out = []
    inserted = 0
    skipped = 0
    for line in lines:
        m = None
        cap = None
        n = None
        # style 1: 〔图 N:图题〕
        m1 = re.match(r"^〔图\s*(\d+)\s*[:：](.*?)〕$", line)
        # style 2: > **图 N.** 图题
        m2 = re.match(r"^>\s*\*\*图\s*(\d+)\.?\s*(.*?)\*\*", line)
        # style 3: **图 N. 图题**
        m3 = re.match(r"^\*\*图\s*(\d+)\.?\s*(.*?)\*\*$", line)
        if m1:
            n, cap = int(m1.group(1)), m1.group(2)
        elif m2:
            n, cap = int(m2.group(1)), m2.group(2)
        elif m3:
            n, cap = int(m3.group(1)), m3.group(2)
        if n:
            png = os.path.join("zh", "assets", args.assets_dir, f"fig-{n:02d}.png")
            already = any(re.match(rf"^!\[图 {n}:", x) for x in out[-4:])
            if already:
                pass  # 该图题上方已有图片行,跳过
            elif os.path.exists(png):
                cap_clean = cap.strip().rstrip("。.")
                out.append(f"![图 {n}:{cap_clean}](assets/{args.assets_dir}/fig-{n:02d}.png)")
                out.append("")
                inserted += 1
            elif args.skip_missing:
                skipped += 1
            else:
                print(f"[warn] fig {n}: {png} 不存在,未插入(用 --skip-missing 跳过)")
        out.append(line)
    open(args.md, "w", encoding="utf-8").write("\n".join(out))
    print(f"{args.md}: 插入 {inserted} 行图片引用" + (f", 跳过缺失 {skipped}" if skipped else ""))

if __name__ == "__main__":
    main()
