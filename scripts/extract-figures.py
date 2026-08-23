#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 PDF 中按坐标裁剪图形并保存为去白边的 PNG,用于把原文插图嵌入中文 Markdown 翻译。

用法:
    python3 scripts/extract-figures.py <pdf> <spec.tsv> [--outdir <dir>] [--dpi 300] [--pad 6]

spec.tsv 每行一个图形,制表符分隔,列:
    out_name    page    x0    y0    x1    y1    [note]

坐标单位为 PDF 点(pt),原点在页面左上角,向下为 y 正方向
(pdftotext -bbox 输出的 xMin/yMin 即此坐标系)。page 从 1 开始。

如何确定坐标:
    1. pdftotext -bbox <pdf> out.xml,找到图题(如 "Figure 1:")前后正文行的
       xMin/xMax/yMin/yMax;
    2. 图中文字元素(坐标轴刻度、图内标题)的坐标即图形边界;
    3. 四边各留 15-30 pt 余量,避免裁掉轴线和外框。
    4. 位图照片的位置可用 pdftocairo -svg 的 <image> 变换矩阵推算
       (注意 poppler 的 SVG y 坐标有翻转,tiff/像素验证为准)。

依赖: poppler (pdftoppm), Pillow。无 Pillow 时用 --no-trim 只做裁剪。
"""
import argparse
import os
import subprocess
import sys
import tempfile

def parse_spec(path):
    specs = []
    with open(path, encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 6:
                print(f"[warn] spec line {ln} skipped (need >=6 columns): {line}")
                continue
            name, page, x0, y0, x1, y1 = parts[:6]
            note = parts[6] if len(parts) > 6 else ""
            specs.append(dict(name=name, page=int(page),
                              x0=float(x0), y0=float(y0),
                              x1=float(x1), y1=float(y1), note=note))
    return specs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("spec")
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--pad", type=int, default=6, help="去白边后保留的空白像素")
    ap.add_argument("--no-trim", action="store_true", help="不去白边")
    args = ap.parse_args()

    if not os.path.exists(args.pdf):
        sys.exit(f"pdf not found: {args.pdf}")
    specs = parse_spec(args.spec)
    if not specs:
        sys.exit("no specs")
    os.makedirs(args.outdir, exist_ok=True)

    scale = args.dpi / 72.0
    with tempfile.TemporaryDirectory() as tmp:
        for s in specs:
            x = int(round(s["x0"] * scale))
            y = int(round(s["y0"] * scale))
            w = int(round((s["x1"] - s["x0"]) * scale))
            h = int(round((s["y1"] - s["y0"]) * scale))
            raw = os.path.join(tmp, "raw")
            cmd = ["pdftoppm", "-singlefile", "-png", "-r", str(args.dpi),
                   "-f", str(s["page"]), "-l", str(s["page"]),
                   "-x", str(x), "-y", str(y), "-W", str(w), "-H", str(h),
                   args.pdf, raw]
            subprocess.run(cmd, check=True, capture_output=True)
            src = os.path.join(tmp, "raw.png")
            if not os.path.exists(src):
                sys.exit(f"pdftoppm produced no output for {s['name']}")
            dst = os.path.join(args.outdir, s["name"])
            if args.no_trim:
                os.replace(src, dst)
            else:
                try:
                    from PIL import Image
                except ImportError:
                    print("[warn] Pillow missing, falling back to raw crop")
                    os.replace(src, dst)
                    continue
                im = Image.open(src).convert("RGB")
                px = im.load()
                W, H = im.size
                minx, miny, maxx, maxy = W, H, -1, -1
                for yy in range(H):
                    for xx in range(W):
                        r, g, b = px[xx, yy]
                        if min(r, g, b) < 245:  # 非近白像素
                            minx = min(minx, xx); maxx = max(maxx, xx)
                            miny = min(miny, yy); maxy = max(maxy, yy)
                if maxx < 0:
                    print(f"[warn] {s['name']}: all-white crop, kept as-is")
                    os.replace(src, dst)
                    continue
                p = args.pad
                box = (max(0, minx - p), max(0, miny - p),
                       min(W, maxx + p), min(H, maxy + p))
                im.crop(box).save(dst)
            note = f"  ({s['note']})" if s["note"] else ""
            print(f"ok  {dst}  page {s['page']}  {s['x0']:.0f},{s['y0']:.0f}->{s['x1']:.0f},{s['y1']:.0f}{note}")

if __name__ == "__main__":
    main()
