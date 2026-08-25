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

def build_front_matter(year, author, title, h1, authors_full=None):
    fm = [f'---']
    fm.append(f'title: {yq(h1)}')
    fm.append(f'linkTitle: {yq(h1)}')
    if year:
        fm.append(f'date: {year}-01-01')
        fm.append(f'weight: {year - 1960}')
    fm.append(f'params:')
    fm.append(f'  author: "{author}"')
    if authors_full:
        fm.append(f'  authors: {yq(authors_full)}')
    fm.append(f'  year: {year}')
    fm.append(f'---')
    return "\n".join(fm)

def main():
    os.makedirs(OUT, exist_ok=True)
    # load award metadata (year/author full name) for extra front matter
    import yaml
    slug_authors = {}
    try:
        with open(os.path.join(ROOT, "data", "turing.yaml"), encoding="utf-8") as f:
            for aw in yaml.safe_load(f).get("awards", []):
                if aw.get("status") == "translated" and aw.get("slug"):
                    slug_authors[aw["slug"]] = aw.get("authors", "")
    except Exception as e:
        print("warn: could not load turing.yaml:", e)
    # copy figures
    if os.path.isdir(os.path.join(ZH, "assets")):
        shutil.copytree(os.path.join(ZH, "assets"), STATIC_ASSETS, dirs_exist_ok=True)
        print(f"copied zh/assets/ -> static/assets/")
    # index page for the lectures section
    with open(os.path.join(OUT, "_index.md"), "w", encoding="utf-8") as f:
        f.write("---\ntitle: 全部演讲\nlinkTitle: 全部演讲\nweight: 20\ncascade:\n  type: docs\n---\n\n本页为 **1966–2024 年 ACM 图灵奖获奖演讲总览**，按获奖年份列出每位获奖者及其属别、演讲概要。凡已有中文译稿者以 **中文译稿** 标注并可进入正文；仅有 ACM 演讲视频者以 **ACM 视频** 标注；**空缺** 表示该年无书面讲稿、ACM 演讲页亦无视频存档。\n")
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
            f.write(build_front_matter(year, author, h1, h1, slug_authors.get(slug)) + "\n\n" + body_s.rstrip() + "\n")
        n += 1
    print(f"generated {n} lecture pages into content/lectures/")

if __name__ == "__main__":
    main()
