#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Hugo site content from zh/ translations and papers-cn/ source papers.

- Reads zh/<year>-<author>-<title>.md (Chinese translation files).
- Writes content/lectures/<year>-<author>.md with front matter
  (title, date, weight) + body, with image paths rewritten to the
  site-absolute /assets/... (figures are copied to static/assets/).
- Copies zh/assets/ -> static/assets/.
- Reads papers-cn/ (two standalone papers + four Collected Works volumes)
  and writes content/papers/<volume>/<unit>.md pages. Unit order comes from
  each volume README.md unit table; unit URLs get explicit ASCII slugs so
  cross-links can be rewritten deterministically.
"""
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH = os.path.join(ROOT, "zh")
OUT = os.path.join(ROOT, "content", "lectures")
STATIC_ASSETS = os.path.join(ROOT, "static", "assets")

# --- papers-cn (Turing Collected Works + related source papers) -------------
PAPERS_CN = os.path.join(ROOT, "papers-cn")
OUT_PAPERS = os.path.join(ROOT, "content", "papers")
GITHUB_PAPERS_URL = (
    "https://github.com/c2j/ACM-Turing-Award-Lectures/blob/main/papers-cn/"
)
# Volumes in Collected Works series order: weight controls section ordering.
VOLUMES = [
    ("pure-mathematics",       "第一卷 · 纯数学",   "Pure Mathematics",       10),
    ("mathematical-logic",     "第二卷 · 数理逻辑", "Mathematical Logic",     20),
    ("mechanical-intelligence","第三卷 · 机械智能", "Mechanical Intelligence",30),
    ("morphogenesis",          "第四卷 · 形态发生", "Morphogenesis",          40),
]
STANDALONE_WEIGHT = {"church": 50, "sterrett": 51}
# Working/QA files that stay in the repo but are not published as site pages.
PAPERS_EXCLUDED = {"README.md", "翻译清单.md"}

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

def strip_h1(text):
    """Split markdown text into (h1, body). Drops the first '# ' heading."""
    h1 = ""
    body = []
    for l in text.split("\n"):
        if not h1 and l.startswith("# "):
            h1 = l[2:].strip()
            continue
        body.append(l)
    return (h1 or None), "\n".join(body)


def readme_unit_order(vol_dir):
    """Parse the volume README unit tables into an ordered list of filenames.

    Table rows look like `| ... | \`05-xxx.md\` |` or `... | [x.md](x.md) |`;
    the target file is the last .md name found in each row. Rows across all
    tables in document order define the canonical reading order.
    """
    readme = os.path.join(vol_dir, "README.md")
    order = []
    if not os.path.isfile(readme):
        return order
    for line in open(readme, encoding="utf-8"):
        if not line.lstrip().startswith("|"):
            continue
        m_all = re.findall(r"\]\((.+?\.md)\)|`([^`\n]+?\.md)`", line)
        if not m_all:
            continue
        name = os.path.basename(m_all[-1][0] or m_all[-1][1])
        if name not in order:
            order.append(name)
    return order


def make_slug(fname, idx, seen):
    """Deterministic ASCII slug for a unit page.

    Uses the leading ASCII run of the filename (e.g. '00', '1935-turing',
    '90-britton'); 未刊-N manuscripts become unpub-N; otherwise a two-digit
    fallback derived from the reading-order index. Duplicates get -2/-3...
    suffixes.
    """
    base = fname[:-3]
    m = re.match(r"^未刊-(\d+)", base)
    slug = f"unpub-{m.group(1)}" if m else ""
    if not slug:
        head = []
        for ch in base:
            if ord(ch) < 128:
                head.append(ch)
            else:
                break
        slug = "".join(head).strip("-").replace(" ", "-").lower()
    if not re.match(r"^[a-z0-9][a-z0-9\-]*$", slug):
        slug = f"{idx:02d}"
    while slug in seen:
        seen[slug] += 1
        slug = f"{slug}-{seen[slug]}"
    seen[slug] = 1
    return slug


def rewrite_md_links(body, src_dir, link_map):
    """Rewrite ](<name>.md) links to site URLs.

    - Same-directory files -> /papers/<volume>/<slug>/
    - 翻译清单.md (QA checklist, not published) -> GitHub blob URL
    - Unknown/unresolvable links are left untouched (many are math fragments
      like ](A) that merely end with a paren).
    """
    def repl(m):
        target = m.group(1)
        name = os.path.basename(target)
        entry = link_map.get(name) or {}
        url = entry.get("url")
        if url:
            return f"]({url})"
        if name == "翻译清单.md":
            rel = os.path.relpath(src_dir, PAPERS_CN).replace(os.sep, "/")
            subdir = "" if rel == "." else rel + "/"
            return f"]({GITHUB_PAPERS_URL}{subdir}翻译清单.md)"
        return m.group(0)

    return re.sub(r"\]\(([^)]+\.md)\)", repl, body)


def build_papers_section():
    """Generate content/papers/ from papers-cn/."""
    n_pages = 0

    # ---- section landing page -------------------------------------------
    os.makedirs(OUT_PAPERS, exist_ok=True)
    index_body = (
        "本栏目收录图灵相关原始文献的中文翻译：四卷《A. M. 图灵全集》"
        "(*Collected Works of A.M. Turing*, North-Holland/Elsevier)"
        "按丛书卷次排列，另有两篇独立论文(Church 1936、Sterrett 2012)。"
        "各卷首页附单元对照表(原文页码 → 中文文件)；正文含〔译注N〕，"
        "阅读时侧栏会自动跟随显示对应说明。原文 PDF 因版权不随仓库分发。\n"
    )
    with open(os.path.join(OUT_PAPERS, "_index.md"), "w", encoding="utf-8") as f:
        f.write(
            "---\n"
            'title: "图灵全集与相关文献"\n'
            'linkTitle: "图灵全集"\n'
            "weight: 30\n"
            "cascade:\n"
            "  type: docs\n"
            'description: "《图灵全集》四卷与 Church 1936、Sterrett 2012 的中文翻译"\n'
            "---\n\n" + index_body
        )
    n_pages += 1

    # ---- standalone papers at papers-cn root -----------------------------
    standalone = sorted(
        fn for fn in os.listdir(PAPERS_CN)
        if fn.endswith(".md") and fn not in PAPERS_EXCLUDED
    )
    # global map: filename -> URL, built after we know every slug; do two passes
    volume_files = {}   # vol dir -> ordered [(fname, slug)]
    for dirname, zh_title, en_title, weight in VOLUMES:
        vdir = os.path.join(PAPERS_CN, dirname)
        files = [
            fn for fn in os.listdir(vdir)
            if fn.endswith(".md") and fn not in PAPERS_EXCLUDED
        ]
        order = [f for f in readme_unit_order(vdir) if f in files]
        order += sorted(set(files) - set(order))
        seen = {}
        units = [(fn, make_slug(fn, i + 1, seen)) for i, fn in enumerate(order)]
        volume_files[dirname] = units

    # build lookup: basename -> url
    link_map = {}
    for dirname, _, _, _ in VOLUMES:
        for fn, slug in volume_files[dirname]:
            link_map[fn] = {"url": f"/papers/{dirname}/{slug}/"}
    for fn in standalone:
        key = "sterrett" if "sterrett" in fn else "church"
        link_map[fn] = {"url": f"/papers/{key}-{('2012' if key == 'sterrett' else '1936')}/"}

    # ---- volumes ---------------------------------------------------------
    for dirname, zh_title, en_title, weight in VOLUMES:
        vdir = os.path.join(PAPERS_CN, dirname)
        out_vdir = os.path.join(OUT_PAPERS, dirname)
        os.makedirs(out_vdir, exist_ok=True)

        # volume landing page from README.md (unit mapping table)
        readme_text = open(os.path.join(vdir, "README.md"), encoding="utf-8").read()
        r_h1, r_body = strip_h1(readme_text)
        r_body = rewrite_md_links(r_body, vdir, link_map)
        fm = [
            "---",
            f"title: {yq(zh_title)}",
            f"linkTitle: {yq(zh_title.split('·')[-1].strip())}",
            f"weight: {weight}",
            f"description: {yq(f'Collected Works of A.M. Turing: {en_title}')}",
            "---",
        ]
        with open(os.path.join(out_vdir, "_index.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(fm) + "\n\n" + r_body.strip() + "\n")
        n_pages += 1

        # unit pages in canonical order
        for i, (fn, slug) in enumerate(volume_files[dirname], start=1):
            src = os.path.join(vdir, fn)
            h1, body = strip_h1(open(src, encoding="utf-8").read())
            body = rewrite_md_links(body, vdir, link_map)
            title = h1 or fn[:-3]
            fm = ["---",
                  f"title: {yq(title)}",
                  f"linkTitle: {yq(title)}",
                  f"weight: {i}",
                  "params:",
                  f"  volume: \"{dirname}\"",
                  f"  source: \"papers-cn/{dirname}/{fn}\"",
                  "---"]
            out = os.path.join(out_vdir, f"{slug}.md")
            with open(out, "w", encoding="utf-8") as f:
                f.write("\n".join(fm) + "\n\n" + body.rstrip() + "\n")
            n_pages += 1

    # ---- standalone papers -------------------------------------------------
    for fn in standalone:
        key = "sterrett" if "sterrett" in fn else "church"
        weight = STANDALONE_WEIGHT[key]
        slug = f"{key}-{'2012' if key == 'sterrett' else '1936'}"
        src = os.path.join(PAPERS_CN, fn)
        h1, body = strip_h1(open(src, encoding="utf-8").read())
        body = rewrite_md_links(body, PAPERS_CN, link_map)
        title = h1 or fn[:-3]
        fm = ["---",
              f"title: {yq(title)}",
              f"linkTitle: {yq(title)}",
              f"weight: {weight}",
              f"slug: {slug}",
              "params:",
              f"  source: \"papers-cn/{fn}\"",
              "---"]
        with open(os.path.join(OUT_PAPERS, f"{slug}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(fm) + "\n\n" + body.rstrip() + "\n")
        n_pages += 1

    print(f"generated {n_pages} pages into content/papers/")


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
    build_papers_section()
    print(f"generated {n} lecture pages into content/lectures/")

if __name__ == "__main__":
    main()
