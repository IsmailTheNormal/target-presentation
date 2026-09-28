#!/usr/bin/env python3
"""
Target International School — In-Place i18n Converter
Converts verbose triple-tag presentations (<h2 lang="uz">... <h2 lang="ru">... <h2 lang="en">...)
into clean in-place data-ru / data-en attributes with zero-blank fallback.
"""
import glob
import os
import re
import sys

def convert_to_inplace(html: str) -> str:
    # 1. Convert 3 adjacent tags: <TAG lang="uz">... <TAG lang="ru">... <TAG lang="en">...
    tag_pattern = re.compile(
        r'<([a-zA-Z0-9]+)([^>]*?)\s+lang=["\']uz["\']([^>]*?)>(.*?)</\1>\s*'
        r'<\1[^>]*?\s+lang=["\']ru["\'][^>]*?>(.*?)</\1>\s*'
        r'<\1[^>]*?\s+lang=["\']en["\'][^>]*?>(.*?)</\1>',
        re.DOTALL
    )
    def tag_repl(m):
        tag = m.group(1)
        attr1 = m.group(2).strip()
        attr2 = m.group(3).strip()
        uz_txt = m.group(4)
        ru_txt = m.group(5).strip().replace('"', '&quot;')
        en_txt = m.group(6).strip().replace('"', '&quot;')
        combined_attrs = f'{attr1} {attr2}'.strip()
        attr_str = f' {combined_attrs}' if combined_attrs else ''
        return f'<{tag}{attr_str} data-ru="{ru_txt}" data-en="{en_txt}">{uz_txt}</{tag}>'

    prev = None
    while prev != html:
        prev = html
        html = tag_pattern.sub(tag_repl, html)

    # 2. Convert span.t with 3 spans:
    span_t_pattern = re.compile(
        r'<span\s+class=["\']t["\']>\s*'
        r'<span\s+lang=["\']uz["\']>(.*?)</span>\s*'
        r'<span\s+lang=["\']ru["\']>(.*?)</span>\s*'
        r'<span\s+lang=["\']en["\']>(.*?)</span>\s*'
        r'</span>',
        re.DOTALL
    )
    def span_repl(m):
        uz_txt = m.group(1)
        ru_txt = m.group(2).strip().replace('"', '&quot;')
        en_txt = m.group(3).strip().replace('"', '&quot;')
        return f'<span class="t" data-ru="{ru_txt}" data-en="{en_txt}">{uz_txt}</span>'

    html = span_t_pattern.sub(span_repl, html)

    # 3. Convert inline spans:
    inline_span_pattern = re.compile(
        r'<span\s+lang=["\']uz["\']>(.*?)</span>\s*'
        r'<span\s+lang=["\']ru["\']>(.*?)</span>\s*'
        r'<span\s+lang=["\']en["\']>(.*?)</span>',
        re.DOTALL
    )
    def inline_repl(m):
        uz_txt = m.group(1)
        ru_txt = m.group(2).strip().replace('"', '&quot;')
        en_txt = m.group(3).strip().replace('"', '&quot;')
        return f'<span data-ru="{ru_txt}" data-en="{en_txt}">{uz_txt}</span>'

    html = inline_span_pattern.sub(inline_repl, html)

    # 4. Convert <th> and <td> table triplets:
    th_td_pattern = re.compile(
        r'<(th|td)([^>]*?)\s+lang=["\']uz["\']([^>]*?)>(.*?)</\1>\s*'
        r'<\1[^>]*?\s+lang=["\']ru["\'][^>]*?>(.*?)</\1>\s*'
        r'<\1[^>]*?\s+lang=["\']en["\'][^>]*?>(.*?)</\1>',
        re.DOTALL
    )
    html = th_td_pattern.sub(tag_repl, html)

    return html

def main():
    target_files = []
    if len(sys.argv) > 1:
        target_files = sys.argv[1:]
    else:
        target_files = sorted(glob.glob('/home/dpdp/target/classes/*/*/*/prezentatsiya.html'))

    print(f"Converting {len(target_files)} presentation files to in-place i18n format...")
    total_saved = 0
    converted_count = 0

    for fpath in target_files:
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            orig = f.read()

        conv = convert_to_inplace(orig)
        saved = len(orig) - len(conv)
        total_saved += saved

        if orig != conv:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(conv)
            converted_count += 1

    print(f"Done! Converted {converted_count}/{len(target_files)} files.")
    print(f"Total HTML reduction: {total_saved:,} bytes ({total_saved // 1024} KB).")

if __name__ == '__main__':
    main()
