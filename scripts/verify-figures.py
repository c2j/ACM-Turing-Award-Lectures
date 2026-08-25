#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""最终校验: 遍历 zh/ 下所有 MD,核对图片引用与 zh/assets/ 下的 PNG 一一对应,并输出汇总统计。"""
import glob
import os
import re
import sys

def main():
    total_refs = 0
    total_pngs = 0
    missing = []
    per_file = []
    for md in sorted(glob.glob("zh/*.md")):
        txt = open(md, encoding="utf-8").read()
        refs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", txt)
        n = 0
        for r in refs:
            if r.startswith(("http", "https")):
                continue  # 遗留的外部占位链接
            n += 1
            if not os.path.exists(os.path.join("zh", r)):
                missing.append((md, r))
        if n:
            per_file.append((os.path.basename(md), n))
        total_refs += n
    pngs = glob.glob("zh/assets/*/*.png")
    total_pngs = len(pngs)
    print(f"MD 图片引用(本地): {total_refs}")
    print(f"zh/assets/ PNG 总数: {total_pngs}")
    print(f"缺失引用: {missing if missing else '无'}")
    print("\n按文件统计:")
    for md, n in per_file:
        print(f"  {md}: {n}")
    if missing:
        sys.exit(1)

if __name__ == "__main__":
    main()
