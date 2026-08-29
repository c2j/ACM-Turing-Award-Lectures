#!/usr/bin/env python3
"""Convert $...$ inline math to \(...\) in markdown files, skipping code blocks,
inline code, $$...$$ blocks, and YAML front matter."""

import re
import os
import sys


def convert_file(filepath, dry_run=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    result = []
    in_fenced_code = False
    in_front_matter = False
    modified = False

    for line in lines:
        stripped = line.strip()

        # Track YAML front matter
        if stripped == '---' and not in_fenced_code:
            in_front_matter = not in_front_matter
            result.append(line)
            continue

        # Track fenced code blocks
        if stripped.startswith('```') and not in_front_matter:
            in_fenced_code = not in_fenced_code
            result.append(line)
            continue

        if in_fenced_code or in_front_matter:
            result.append(line)
            continue

        # Find protected ranges (inline code in backticks)
        protected_ranges = []
        for m in re.finditer(r'`[^`]*`', line):
            protected_ranges.append((m.start(), m.end()))

        # Convert $...$ to \(...\) - negative lookbehind/lookahead to avoid $$
        new_line = re.sub(
            r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', 
            r'\(\1\)', 
            line
        )

        # Revert conversions inside backtick-protected ranges
        reverted = False
        for m in re.finditer(r'\(.+?\)', new_line):
            start, end = m.start(), m.end()
            inside_protected = any(ps <= start and end <= pe for ps, pe in protected_ranges)
            if inside_protected:
                inner = m.group(0)[1:-1]  # strip ( and )
                new_line = new_line[:start] + '$' + inner + '$' + new_line[end:]
                reverted = True

        if new_line != line or reverted:
            modified = True
            result.append(new_line)
        else:
            result.append(line)

    new_content = '\n'.join(result)

    if modified and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return modified


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 convert_inline_math.py <dir> [--dry-run]")
        sys.exit(1)

    root = sys.argv[1]
    dry_run = '--dry-run' in sys.argv

    if not os.path.isdir(root):
        print(f"Error: {root} is not a directory")
        sys.exit(1)

    modified_count = 0
    total_count = 0

    for dirpath, dirnames, filenames in os.walk(root):
        # Skip hidden dirs
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        for fn in sorted(filenames):
            if not fn.endswith('.md'):
                continue
            filepath = os.path.join(dirpath, fn)
            if convert_file(filepath, dry_run=dry_run):
                modified_count += 1
                rel = os.path.relpath(filepath, root)
                label = "WOULD MODIFY" if dry_run else "MODIFIED"
                print(f"[{label}] {rel}")
            total_count += 1

    print(f"\nScanned {total_count} .md files, {'would modify' if dry_run else 'modified'} {modified_count}")


if __name__ == '__main__':
    main()