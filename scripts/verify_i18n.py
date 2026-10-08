#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Target International School — Comprehensive Localization (i18n) Validator

Guarantees 100% trilingual coverage (UZ, RU, EN) across all lesson presentations,
worksheets, and lab simulators.

Usage:
    python3 scripts/verify_i18n.py classes/9-sinf/4-hafta/18-dars-malumotlar-bazasi-va-sql
    python3 scripts/verify_i18n.py classes/9-sinf/4-hafta/18-dars-malumotlar-bazasi-va-sql/prezentatsiya.html
    python3 scripts/verify_i18n.py --staged
    python3 scripts/verify_i18n.py --all
"""

import os
import sys
import re
import json
import pathlib
import subprocess
from html.parser import HTMLParser

VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
             "meta", "param", "source", "track", "wbr"}

TEXT_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "th", "td", "li", "button", "label"}

# Exclude pure code expressions, numeric counters, bracket boxes, etc.
PURE_CODE_RE = re.compile(r"^[A-Za-z0-9_.]+\s*\(.*?\);?$")
CODE_BLOCK_RE = re.compile(r"^(--|SELECT|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER|BEGIN|COMMIT|ROLLBACK|PRAGMA|\$|\#|\.\/)")
PUNCT_OR_NUM_RE = re.compile(r"^[\s\d\W_]+$")
FILENAME_RE = re.compile(r"^[a-zA-Z0-9_\-]+\.(db|json|html|css|js|py|sql|png|jpg|svg|txt|md|sh)$")


def needs_translation(text, tag, attrs):
    txt = text.strip()
    if not txt or len(txt) <= 1:
        return False
    # If the tag is pure code or inside pre/code and looks like code:
    cls = attrs.get("class", "").split()
    if "mono" in cls or "code-block" in cls:
        return False
    # Technical file names
    if FILENAME_RE.match(txt):
        return False
    # Language switcher buttons (RU, EN, UZ) and theme toggle (managed dynamically)
    if "data-l" in attrs or "lg" in cls:
        return False
    if attrs.get("id") == "themeBtn" or "theme-btn" in cls:
        return False
    if tag == "button" and txt in {"RU", "EN", "UZ", "←", "→", "✕", "▲", "▼", "★"}:
        return False
    if PURE_CODE_RE.match(txt) or CODE_BLOCK_RE.match(txt):
        return False
    if PUNCT_OR_NUM_RE.match(txt):
        return False
    # Check if there is actual natural language words (Uzbek, Russian, English)
    words = re.findall(r"[A-Za-zА-Яа-яЎўҚқҒғҲҳЁё']+", txt)
    if not words:
        return False
    # If it's just pure numbers/symbols with 1 short word like "10 ms" or "PK" or "id INT"
    if len(words) == 1 and len(words[0]) <= 3 and any(ch.isdigit() for ch in txt):
        return False
    return True


class HTMLNode:
    __slots__ = ("tag", "attrs", "children", "text", "line", "parent")

    def __init__(self, tag, attrs, line, parent=None):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []
        self.text = ""
        self.line = line
        self.parent = parent

    def all_text(self):
        return (self.text + "".join(c.all_text() for c in self.children)).strip()

    def direct_text(self):
        return self.text.strip()

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()

    def has_i18n_attr(self):
        ru = self.attrs.get("data-ru", "").strip()
        en = self.attrs.get("data-en", "").strip()
        return bool(ru and en)

    def has_i18n_descendant(self):
        for c in self.children:
            if c.has_i18n_attr():
                return True
            if c.has_i18n_descendant():
                return True
        return False

    def is_inside_code(self):
        cur = self
        while cur:
            if cur.tag in ("code", "pre"):
                return True
            cls = cur.attrs.get("class", "").split()
            if "code-block" in cls or "prompt" in cls:
                return True
            cur = cur.parent
        return False


class DOMParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = HTMLNode("#root", [], 0)
        self.stack = [self.root]
        self.errors = []
        self.raw_tag = None

    def handle_starttag(self, tag, attrs):
        if self.raw_tag:
            return
        node = HTMLNode(tag, attrs, self.getpos()[0], self.stack[-1])
        self.stack[-1].children.append(node)
        if tag in ("script", "style"):
            self.raw_tag = tag
            return
        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        if self.raw_tag:
            return
        self.stack[-1].children.append(HTMLNode(tag, attrs, self.getpos()[0], self.stack[-1]))

    def handle_endtag(self, tag):
        if self.raw_tag:
            if tag == self.raw_tag:
                self.raw_tag = None
            return
        if tag in VOID_TAGS:
            return
        for k in range(len(self.stack) - 1, 0, -1):
            if self.stack[k].tag == tag:
                if k != len(self.stack) - 1:
                    unclosed = ", ".join(x.tag for x in self.stack[k + 1:])
                    self.errors.append(f"Line {self.getpos()[0]}: </{tag}> closed prematurely, unclosed: {unclosed}")
                del self.stack[k:]
                return
        self.errors.append(f"Line {self.getpos()[0]}: Unexpected dangling closing tag </{tag}>")

    def handle_data(self, data):
        if not self.raw_tag and self.stack:
            self.stack[-1].text += data


def parse_html(html_str):
    p = DOMParser()
    p.feed(html_str)
    p.close()
    errs = list(p.errors)
    if len(p.stack) > 1:
        unclosed = ", ".join(f"{n.tag}(line {n.line})" for n in p.stack[1:])
        errs.append(f"Unclosed DOM tags at EOF: {unclosed}")
    return p.root, errs


# =====================================================================
# CHECK PRESENTATION
# =====================================================================
def verify_presentation(path, rel_name):
    issues = []
    text = path.read_text(encoding="utf-8")
    root, parse_errs = parse_html(text)
    issues.extend(parse_errs)

    # 1. Slide count and structure
    slides = [n for n in root.walk() if n.tag == "section" and "slide" in n.attrs.get("class", "").split()]
    if not slides:
        issues.append("No <section class='slide'> elements found.")
        return issues

    slide_count = len(slides)

    # 2. Slide metadata (data-phase, data-time)
    for idx, s in enumerate(slides, start=1):
        phase = s.attrs.get("data-phase", "")
        if not phase:
            issues.append(f"Slide {idx} (line {s.line}): Missing 'data-phase' attribute.")
        elif phase.count("|") != 2:
            issues.append(f"Slide {idx} (line {s.line}): 'data-phase=\"{phase}\"' must have exactly 3 parts (Uz|Ru|En).")

        time_val = s.attrs.get("data-time", "")
        if not time_val:
            issues.append(f"Slide {idx} (line {s.line}): Missing 'data-time' attribute.")

    # 3. Speaker Notes & Titles Verification
    m_notes = re.search(r'NOTES\s*=\s*(\{[\s\S]*?\n\s*\})[;,]', text)
    if not m_notes:
        issues.append("JavaScript 'NOTES' object could not be parsed.")
    else:
        try:
            notes_obj = json.loads(m_notes.group(1))
            for lang in ("uz", "ru", "en"):
                if lang not in notes_obj:
                    issues.append(f"Speaker notes missing language key '{lang}'.")
                elif len(notes_obj[lang]) != slide_count:
                    issues.append(f"Speaker notes '{lang}' length ({len(notes_obj[lang])}) does not match slide count ({slide_count}).")
                else:
                    for s_idx, note_tuple in enumerate(notes_obj[lang], start=1):
                        if not isinstance(note_tuple, list) or len(note_tuple) != 3:
                            issues.append(f"Slide {s_idx} notes[{lang}] must be [title, say, do] triplet.")
                        elif not note_tuple[0] or not note_tuple[1] or not note_tuple[2]:
                            issues.append(f"Slide {s_idx} notes[{lang}] has empty title, say, or do.")
        except Exception as e:
            issues.append(f"JSON parse error in NOTES object: {e}")

    m_titles = re.search(r'TITLES\s*=\s*(\{[\s\S]*?\n\s*\})[;,]', text)
    if m_titles:
        try:
            titles_obj = json.loads(m_titles.group(1))
            for lang in ("uz", "ru", "en"):
                if lang not in titles_obj or not titles_obj[lang].strip():
                    issues.append(f"Page TITLES missing or empty for '{lang}'.")
        except Exception as e:
            issues.append(f"JSON parse error in TITLES object: {e}")

    # 4. In-Place i18n DOM Coverage
    for node in root.walk():
        audit_node_attributes(node, issues)
        # Check li inside ul.plain (trap #1)
        if node.tag == "li" and node.parent and node.parent.tag == "ul" and "plain" in node.parent.attrs.get("class", "").split():
            t_spans = [c for c in node.children if "t" in c.attrs.get("class", "").split()]
            if not t_spans and not node.has_i18n_attr():
                if needs_translation(node.all_text(), node.tag, node.attrs):
                    issues.append(f"Line {node.line}: <li> in ul.plain missing <span class='t'> wrapper (Trap #1): \"{node.all_text()[:50]}...\"")

        # Check all text elements
        cls = node.attrs.get("class", "").split()
        is_candidate = (node.tag in TEXT_TAGS) or ("t" in cls) or ("eyebrow" in cls) or ("lede" in cls) or ("callout" in cls)

        if is_candidate and not node.is_inside_code():
            txt = node.direct_text() if node.tag in ("div", "section") else node.all_text()
            if needs_translation(txt, node.tag, node.attrs):
                ru = node.attrs.get("data-ru", "")
                en = node.attrs.get("data-en", "")
                has_ru = bool(ru and ru.strip())
                has_en = bool(en and en.strip())

                if has_ru and not has_en:
                    issues.append(f"Line {node.line}: <{node.tag}> has data-ru but missing data-en: \"{txt[:50]}...\"")
                elif has_en and not has_ru:
                    issues.append(f"Line {node.line}: <{node.tag}> has data-en but missing data-ru: \"{txt[:50]}...\"")
                elif not has_ru and not has_en:
                    # Check if children have full i18n
                    if not node.has_i18n_descendant():
                        # Exclude pure code inside td
                        if not (node.tag == "td" and (CODE_BLOCK_RE.match(txt) or PURE_CODE_RE.match(txt))):
                            issues.append(f"Line {node.line}: <{node.tag}> untranslated (missing data-ru & data-en): \"{txt[:50]}...\"")

    return issues


def audit_node_attributes(node, issues):
    # 1. Audit placeholder
    ph = node.attrs.get("placeholder", "").strip()
    if ph and needs_translation(ph, node.tag, node.attrs):
        ph_ru = node.attrs.get("data-placeholder-ru", "").strip()
        ph_en = node.attrs.get("data-placeholder-en", "").strip()
        if not ph_ru or not ph_en:
            issues.append(f"Line {node.line}: <{node.tag}> placeholder \"{ph[:40]}\" missing data-placeholder-ru or data-placeholder-en")

    # 2. Audit title (tooltips)
    ttl = node.attrs.get("title", "").strip()
    if ttl and needs_translation(ttl, node.tag, node.attrs):
        ttl_ru = node.attrs.get("data-title-ru", "").strip()
        ttl_en = node.attrs.get("data-title-en", "").strip()
        if not ttl_ru or not ttl_en:
            issues.append(f"Line {node.line}: <{node.tag}> title \"{ttl[:40]}\" missing data-title-ru or data-title-en")


# =====================================================================
# CHECK WORKSHEET (VARAQA)
# =====================================================================
def verify_worksheet(path, rel_name):
    issues = []
    text = path.read_text(encoding="utf-8")
    root, parse_errs = parse_html(text)
    issues.extend(parse_errs)

    # 1. Print theme CSS (Trap #3)
    pr = re.search(r"@media print\s*\{([\s\S]*?)\n\}", text)
    if not pr:
        issues.append("Missing @media print block.")
    else:
        blk = pr.group(1)
        required_selectors = [
            ":root,",
            ':root:not([data-theme="light"]),',
            ':root[data-theme="dark"],',
            ':root[data-theme="light"]{'
        ]
        for sel in required_selectors:
            if sel not in blk:
                issues.append(f"@media print missing '{sel}' (Trap #3).")

    if "@page" not in text:
        issues.append("Missing @page rule.")

    # 2. Text elements in worksheet
    for node in root.walk():
        audit_node_attributes(node, issues)
        if node.tag in TEXT_TAGS and not node.is_inside_code():
            txt = node.all_text()
            if needs_translation(txt, node.tag, node.attrs):
                ru = node.attrs.get("data-ru", "")
                en = node.attrs.get("data-en", "")
                has_ru = bool(ru and ru.strip())
                has_en = bool(en and en.strip())

                if has_ru != has_en:
                    issues.append(f"Line {node.line}: <{node.tag}> asymmetric i18n (ru={has_ru}, en={has_en}): \"{txt[:50]}...\"")
                elif not has_ru and not node.has_i18n_descendant():
                    if not (node.tag == "td" and (CODE_BLOCK_RE.match(txt) or PURE_CODE_RE.match(txt))):
                        issues.append(f"Line {node.line}: <{node.tag}> untranslated: \"{txt[:50]}...\"")

    return issues


# =====================================================================
# CHECK LAB SIMULATOR
# =====================================================================
def verify_lab(path, rel_name):
    issues = []
    text = path.read_text(encoding="utf-8")
    root, parse_errs = parse_html(text)
    issues.extend(parse_errs)

    # Check interactive controls, tab buttons, badges, tree nodes, placeholders, and tooltips
    for node in root.walk():
        audit_node_attributes(node, issues)

        if node.is_inside_code():
            continue

        cls = node.attrs.get("class", "").split()
        is_candidate = (node.tag in ("button", "label", "h1", "h2", "h3", "h4", "th", "td", "p", "option")) or ("res-badge" in cls) or ("acc-name" in cls) or ("acc-delta" in cls) or ("t-node" in cls)

        if is_candidate:
            txt = node.direct_text() if node.tag in ("div", "section") else node.all_text()
            if needs_translation(txt, node.tag, node.attrs):
                ru = node.attrs.get("data-ru", "").strip()
                en = node.attrs.get("data-en", "").strip()
                if (ru and not en) or (en and not ru):
                    issues.append(f"Line {node.line}: <{node.tag}> asymmetric i18n: \"{txt[:50]}...\"")
                elif not ru and not node.has_i18n_descendant():
                    if not txt.startswith("SQL>") and len(txt) > 2:
                        issues.append(f"Line {node.line}: <{node.tag}> missing data-ru / data-en: \"{txt[:50]}...\"")

    # Check for DBError or classifyError definition in SQL script
    if "malumotlar-bazasi-va-sql" in str(rel_name):
        if "class DBError" not in text or "classifyError" not in text:
            issues.append("Missing DBError or classifyError localization engine in <script>.")

    return issues


COMMON_REPLACEMENTS = [
    (
        '<button id="printBtn">ПЕЧАТЬ</button>',
        '<button id="printBtn" data-ru="ПЕЧАТЬ" data-en="PRINT">CHOP ETISH</button>'
    ),
    (
        '<button class="lg theme" id="themeBtn">◐ АВТО</button>',
        '<button class="lg theme" id="themeBtn" data-ru="◐ АВТО" data-en="◐ AUTO">◐ AVTO</button>'
    ),
    (
        '<button class="navbtn" id="prev" title="Предыдущий (←)">←</button>',
        '<button class="navbtn" id="prev" title="Oldingi (←)" data-title-ru="Предыдущий (←)" data-title-en="Previous (←)">←</button>'
    ),
    (
        '<button class="navbtn" id="next" title="Следующий (→)">→</button>',
        '<button class="navbtn" id="next" title="Keyingi (→)" data-title-ru="Следующий (→)" data-title-en="Next (→)">→</button>'
    ),
    (
        '<button class="navbtn" id="cleanBtn" title="Скрыть панель (H)">Скрыть</button>',
        '<button class="navbtn" id="cleanBtn" title="Panelni yashirish (H)" data-title-ru="Скрыть панель (H)" data-title-en="Hide bar (H)" data-ru="Скрыть" data-en="Hide">Yashirish</button>'
    ),
    (
        '<button class="navbtn" id="cleanBtn" title="Скрыть (H)">Скрыть</button>',
        '<button class="navbtn" id="cleanBtn" title="Panelni yashirish (H)" data-title-ru="Скрыть панель (H)" data-title-en="Hide bar (H)" data-ru="Скрыть" data-en="Hide">Yashirish</button>'
    ),
    (
        '<button class="navbtn" id="cleanBtn" title="Panelni yashirish (H)" data-ru="Скрыть" data-en="Hide">Yashirish</button>',
        '<button class="navbtn" id="cleanBtn" title="Panelni yashirish (H)" data-title-ru="Скрыть панель (H)" data-title-en="Hide bar (H)" data-ru="Скрыть" data-en="Hide">Yashirish</button>'
    ),
    (
        '<button class="navbtn" id="notesBtn" title="Заметки учителя (N)">Заметки (N)</button>',
        '<button class="navbtn" id="notesBtn" title="O\'qituvchi izohlari (N)" data-title-ru="Заметки учителя (N)" data-title-en="Teacher notes (N)" data-ru="Заметки (N)" data-en="Notes (N)">Izohlar (N)</button>'
    ),
    (
        '<button class="navbtn" id="notesBtn" title="O\'qituvchi izohlari (N)" data-ru="Заметки (N)" data-en="Notes (N)">Izohlar (N)</button>',
        '<button class="navbtn" id="notesBtn" title="O\'qituvchi izohlari (N)" data-title-ru="Заметки учителя (N)" data-title-en="Teacher notes (N)" data-ru="Заметки (N)" data-en="Notes (N)">Izohlar (N)</button>'
    ),
    (
        '<button class="bar-restore-btn" id="barRestoreBtn" type="button" title="Panelni ko\'rsatish (H)">',
        '<button class="bar-restore-btn" id="barRestoreBtn" type="button" title="Panelni ko\'rsatish (H)" data-title-ru="Показать панель (H)" data-title-en="Show bar (H)">'
    ),
    (
        '<button class="navbtn theme-btn" id="themeBtn">◐ АВТО</button>',
        '<button class="navbtn theme-btn" id="themeBtn" title="Mavzu (T)" data-title-ru="Тема (T)" data-title-en="Theme (T)" data-ru="◐ АВТО" data-en="◐ AUTO">◐ AVTO</button>'
    ),
    (
        '<b id="nTitle">Заметки спикера</b>',
        '<b id="nTitle" data-ru="Заметки спикера" data-en="Speaker Notes">Ma\'ruzachi izohlari</b>'
    ),
]


def auto_fix_file(file_path):
    text = file_path.read_text(encoding="utf-8")
    modified = False
    for old_s, new_s in COMMON_REPLACEMENTS:
        if old_s in text:
            text = text.replace(old_s, new_s)
            modified = True
    if modified:
        file_path.write_text(text, encoding="utf-8")
        return True
    return False


def verify_targets(target_paths, do_fix=False):
    cwd = pathlib.Path.cwd().resolve()
    all_issues = {}
    files_to_check = set()

    for target_path in target_paths:
        target = pathlib.Path(target_path).resolve()
        if target.is_file():
            files_to_check.add(target)
        elif target.is_dir():
            for f in target.rglob("*.html"):
                files_to_check.add(f.resolve())
        else:
            print(f"Warning: Path '{target_path}' does not exist.")

    checked_count = 0
    fixed_count = 0
    for f in sorted(files_to_check):
        # Exclude vendor / third-party / external downloads
        parts = f.parts
        if any(p in ("node_modules", "eduvisit", ".git", "emaktab") for p in parts):
            continue

        try:
            rel_path = f.relative_to(cwd)
        except ValueError:
            rel_path = f
        fname = f.name.lower()

        if do_fix:
            if auto_fix_file(f):
                fixed_count += 1
                print(f"  \033[36m⚡ Auto-fixed common template omissions:\033[0m {rel_path}")

        if fname == "prezentatsiya.html":
            checked_count += 1
            errs = verify_presentation(f, rel_path)
            if errs:
                all_issues[str(rel_path)] = errs
            else:
                print(f"  \033[32m✓\033[0m {rel_path} (prezentatsiya i18n OK)")
        elif fname == "varaqa.html":
            checked_count += 1
            errs = verify_worksheet(f, rel_path)
            if errs:
                all_issues[str(rel_path)] = errs
            else:
                print(f"  \033[32m✓\033[0m {rel_path} (varaqa i18n OK)")
        elif any(p in f.parts for p in ("lab", "studio", "editor", "game", "arena", "aha", "scanner", "simulator", "market", "builder", "ctf")) and fname == "index.html":
            checked_count += 1
            errs = verify_lab(f, rel_path)
            if errs:
                all_issues[str(rel_path)] = errs
            else:
                print(f"  \033[32m✓\033[0m {rel_path} (interactive app i18n OK)")

    if checked_count == 0:
        print("No presentation, worksheet, or lab HTML files found to verify.")
        return 0

    if all_issues:
        print("\n\033[1;31mLocalization Verification Failed:\033[0m")
        for fpath, err_list in all_issues.items():
            print(f"\n  \033[1;31m✗ {fpath}\033[0m ({len(err_list)} issues):")
            for e in err_list:
                print(f"      • {e}")
        return 1

    print(f"\n\033[1;32mAll {checked_count} checked file(s) passed 100% localization validation!\033[0m")
    return 0


def get_staged_html_files():
    cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"]
    out = subprocess.check_output(cmd, encoding="utf-8").strip()
    if not out:
        return []
    return [p for p in out.splitlines() if p.endswith(".html")]


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    do_fix = "--fix" in args
    args = [a for a in args if a != "--fix"]

    if not args or args[0] == "--staged":
        staged = get_staged_html_files()
        if not staged:
            print("No staged HTML files to verify.")
            sys.exit(0)
        sys.exit(verify_targets(staged, do_fix=do_fix))

    if args[0] == "--all":
        sys.exit(verify_targets(["classes"], do_fix=do_fix))

    sys.exit(verify_targets(args, do_fix=do_fix))

