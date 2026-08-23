#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Hugo site content from zh/ translations.

- Reads zh/<year>-<author>-<title>.md (Chinese translation files).
- Writes content/lectures/<year>-<author>.md with front matter
  (title, date, weight) + body, with image paths rewritten to the
  site-absolute /assets/... (figures are copied to static/assets/).
- Copies zh/assets/ -> static/assets/.
"""
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = os.path.join(ROOT, "zh")
OUT = os.path.join(ROOT, "content", "lectures")
STATIC_ASSETS = os.path.join(ROOT, "static", "assets")

def derive_meta(fname):
    """<year>-<author>-<title>.md -> (year, author, chinese_title)"""
    base = fname[:-3]  # strip .md
    m = re.match(r"^(\d{4})-", base)
    year = int(m.group(1)) if m else 0
    rest = base[len(str(year)) + 1:] if year else base
    # Prefix titles are Chinese (non-ASCII), so the author is the leading
    # ASCII run (letters/digits/hyphens), which keeps multi-word authors like
    # "aho-ullman" intact. Strip a trailing '-' separator before the title.
    am = re.match(r"^([A-Za-z0-9][A-Za-z0-9\-]*)", rest)
    if am:
        author = am.group(1).rstrip("-")
        chinese = rest[len(am.group(1)):].lstrip("-")
    else:
        author = rest
        chinese = ""
    return year, author, chinese

def yq(s):
    """YAML-safe double-quoted value: escape backslash and double quote."""
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

def build_front_matter(year, author, title, h1):
    fm = [f'---']
    fm.append(f'title: {yq(h1)}')
    fm.append(f'linkTitle: {yq(h1)}')
    if year:
        fm.append(f'date: {year}-01-01')
        fm.append(f'weight: {year - 1960}')
    fm.append(f'params:')
    fm.append(f'  author: "{author}"')
    fm.append(f'  year: {year}')
    fm.append(f'---')
    return "\n".join(fm)

def main():
    os.makedirs(OUT, exist_ok=True)
    # copy figures
    if os.path.isdir(os.path.join(ZH, "assets")):
        shutil.copytree(os.path.join(ZH, "assets"), STATIC_ASSETS, dirs_exist_ok=True)
        print(f"copied zh/assets/ -> static/assets/")
    # index page for the lectures section
    with open(os.path.join(OUT, "_index.md"), "w", encoding="utf-8") as f:
        f.write("---\ntitle: 全部演讲\nlinkTitle: 全部演讲\nweight: 20\n---\n\n本区域收录 1966–2024 年 ACM 图灵奖获奖演讲的中文翻译(含插图),按获奖年份排序。\n")
    n = 0
    for fn in sorted(os.listdir(ZH)):
        if not fn.endswith(".md"):
            continue
        year, author, _ = derive_meta(fn)
        src = os.path.join(ZH, fn)
        lines = open(src, encoding="utf-8").read().split("\n")
        # first non-empty line that starts with '# ' -> H1 title
        h1 = ""
        body = []
        started = False
        for l in lines:
            if not h1 and l.startswith("# "):
                h1 = l[2:].strip()
                continue  # drop the H1 (theme renders title from front matter)
            body.append(l)
        if not h1:
            h1 = fn[:-3]
        # rewrite image paths to site-absolute
        body_s = "\n".join(body)
        body_s = re.sub(r"\]\(assets/", "](/assets/", body_s)
        # rewrite zh/<other>.md cross-references -> lecture page (best-effort)
        body_s = re.sub(r"zh/(\d{4}-[^)\s]+)\.md", r"/lectures/\1/", body_s)
        slug = f"{year}-{author}" if year else author
        out = os.path.join(OUT, slug + ".md")
        with open(out, "w", encoding="utf-8") as f:
            f.write(build_front_matter(year, author, h1, h1) + "\n\n" + body_s.rstrip() + "\n")
        n += 1
    print(f"generated {n} lecture pages into content/lectures/")

if __name__ == "__main__":
    main()
