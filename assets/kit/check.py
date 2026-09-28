# -*- coding: utf-8 -*-
"""Dars sahifalarini tekshirish — AGENTS.md va CURRICULUM_STATE.md dagi
"ma'lum tuzoqlar" qaytarilmasligi uchun.

Ishlatish:  python3 assets/kit/check.py classes/5-6-sinf/4-hafta/*/

MUHIM: atribut qiymatlari ichida <b> kabi teglar bo'ladi, shuning uchun
regex bilan emas, HTMLParser bilan tahlil qilinadi.
"""

import json
import pathlib
import re
import sys
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

TEXT_TAGS = ("h1", "h2", "h3", "h4", "p", "th", "td", "li")

# Belgi, raqam, katak ("[  ]", "/ 3") va kod identifikatorlari
# ("get_stock_price(ticker)") tarjima talab qilmaydi.
_CODEISH = re.compile(r"^[A-Za-z_][A-Za-z0-9_.]*\s*\(.*\)$")


def NEEDS_TRANSLATION(txt):
    if not re.search(r"[A-Za-zА-Яа-яЁё]", txt):
        return False                      # faqat belgi/raqam
    if _CODEISH.match(txt):
        return False                      # funksiya nomi
    return len(re.findall(r"[A-Za-zА-Яа-яЁё']+", txt)) > 1  # bir so'zli yorliq emas


class Node:
    __slots__ = ("tag", "attrs", "kids", "text", "line")

    def __init__(self, tag, attrs, line):
        self.tag = tag
        self.attrs = dict(attrs)
        self.kids = []
        self.text = ""
        self.line = line

    def all_text(self):
        return (self.text + "".join(k.all_text() for k in self.kids)).strip()

    def walk(self):
        yield self
        for k in self.kids:
            yield from k.walk()

    def has_i18n_descendant(self):
        for k in self.kids:
            if k.attrs.get("data-ru") and k.attrs.get("data-en"):
                return True
            if k.has_i18n_descendant():
                return True
        return False


class Dom(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", [], 0)
        self.stack = [self.root]
        self.errors = []
        self.in_raw = None

    def handle_starttag(self, tag, attrs):
        if self.in_raw:
            return
        n = Node(tag, attrs, self.getpos()[0])
        self.stack[-1].kids.append(n)
        if tag in ("script", "style"):
            self.in_raw = tag
            return
        if tag not in VOID:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        if self.in_raw:
            return
        self.stack[-1].kids.append(Node(tag, attrs, self.getpos()[0]))

    def handle_endtag(self, tag):
        if self.in_raw:
            if tag == self.in_raw:
                self.in_raw = None
            return
        if tag in VOID:
            return
        for k in range(len(self.stack) - 1, 0, -1):
            if self.stack[k].tag == tag:
                if k != len(self.stack) - 1:
                    self.errors.append(
                        "qator %d: </%s> yopdi, lekin %s ochiq qolgan"
                        % (self.getpos()[0], tag,
                           ", ".join(x.tag for x in self.stack[k + 1:])))
                del self.stack[k:]
                return
        self.errors.append("qator %d: ortiqcha </%s>" % (self.getpos()[0], tag))

    def handle_data(self, data):
        if not self.in_raw and self.stack:
            self.stack[-1].text += data


def parse(t):
    d = Dom()
    d.feed(t)
    d.close()
    errs = list(d.errors)
    if len(d.stack) > 1:
        errs.append("yopilmagan teglar: %s"
                    % ", ".join("%s(qator %d)" % (n.tag, n.line) for n in d.stack[1:]))
    return d.root, errs


# ---------------------------------------------------------------- tekshiruvlar

def check_i18n(root, name, errs):
    # tuzoq #1 faqat `ul.plain li` uchun: o'sha `li` da `display:grid` bor.
    # Varaqadagi `.rubric-list li` — `display:flex`, ikki bola ataylab.
    grid_li = set()
    for n in root.walk():
        if n.tag == "ul" and "plain" in n.attrs.get("class", "").split():
            grid_li.update(id(k) for k in n.kids if k.tag == "li")

    for n in root.walk():
        if n.tag == "li" and id(n) in grid_li:
            if n.all_text() and not any(
                    "t" in k.attrs.get("class", "").split() for k in n.kids):
                errs.append("%s qator %d: <li> ichida <span class=\"t\"> yo'q (tuzoq #1): %s"
                            % (name, n.line, n.all_text()[:55]))
        if n.tag in TEXT_TAGS or ("t" in n.attrs.get("class", "").split()):
            txt = n.all_text()
            if not txt or not NEEDS_TRANSLATION(txt):
                continue
            ru, en = n.attrs.get("data-ru"), n.attrs.get("data-en")
            if ru and en:
                if not ru.strip() or not en.strip():
                    errs.append("%s qator %d: <%s> bo'sh tarjima: %s"
                                % (name, n.line, n.tag, txt[:55]))
            elif not n.has_i18n_descendant():
                errs.append("%s qator %d: <%s> tarjimasiz: %s"
                            % (name, n.line, n.tag, txt[:55]))


def check_prez(p, errs):
    t = p.read_text(encoding="utf-8")

    if "</div><!-- /stage -->" not in t:
        errs.append("stage yopuvchi </div> yo'q (tuzoq #2)")
    elif t.index("</div><!-- /stage -->") > t.index('<div class="bar">'):
        errs.append("stage bar dan keyin yopilgan (tuzoq #2)")

    if ".notes[hidden]{display:none !important}" not in t:
        errs.append(".notes[hidden] qoidasi yo'q — izohlar yashirilmaydi")
    if "setLang(savedLang);" not in t:
        errs.append("setLang chaqiruvi yo'q — til almashtirish ishlamaydi")

    slides = re.findall(r'<section class="slide', t)
    m = re.search(r"NOTES = (\{.*?\n\}),\n", t, re.S)
    if not m:
        errs.append("NOTES bloki topilmadi")
    else:
        notes = json.loads(m.group(1))
        for lg in ("uz", "ru", "en"):
            if lg not in notes:
                errs.append("NOTES da '%s' tili yo'q" % lg)
            elif len(notes[lg]) != len(slides):
                errs.append("NOTES[%s]=%d, slaydlar=%d — mos emas"
                            % (lg, len(notes[lg]), len(slides)))
            else:
                for k, n in enumerate(notes[lg]):
                    if len(n) != 3 or not all(str(x).strip() for x in n):
                        errs.append("NOTES[%s][%d] to'liq emas" % (lg, k))

    for v in re.findall(r'data-phase="([^"]*)"', t):
        if v.count("|") != 2:
            errs.append("data-phase='%s' — uch qism emas" % v)

    return t, len(slides)


def check_varaqa(p, errs):
    t = p.read_text(encoding="utf-8")
    pr = re.search(r"@media print \{(.*?)\n\}", t, re.S)
    if not pr:
        errs.append("@media print bloki yo'q")
    else:
        blk = pr.group(1)
        for sel in (":root,", ':root:not([data-theme="light"]),',
                    ':root[data-theme="dark"],', ':root[data-theme="light"]{'):
            if sel not in blk:
                errs.append("@media print ichida '%s' yo'q (tuzoq #3)" % sel)
    if "@page" not in t:
        errs.append("@page qoidasi yo'q")
    return t


def check_dir(d):
    d = pathlib.Path(d)
    errs = []
    prez, varaqa = d / "prezentatsiya.html", d / "varaqa.html"
    n = 0
    if not prez.exists():
        errs.append("prezentatsiya.html yo'q")
    else:
        t, n = check_prez(prez, errs)
        root, e = parse(t)
        errs += ["prezentatsiya: " + x for x in e]
        check_i18n(root, "prezentatsiya", errs)
    if not varaqa.exists():
        errs.append("varaqa.html yo'q")
    else:
        t = check_varaqa(varaqa, errs)
        root, e = parse(t)
        errs += ["varaqa: " + x for x in e]
        check_i18n(root, "varaqa", errs)
    if n and n < 10:
        errs.append("faqat %d slayd — talab 10-12 (AGENTS.md)" % n)
    return errs, n


if __name__ == "__main__":
    bad = 0
    for d in sys.argv[1:]:
        errs, n = check_dir(d)
        name = pathlib.Path(d).name
        if errs:
            bad += 1
            print("✗ %s  (%d slayd)" % (name, n))
            for e in errs:
                print("    " + e)
        else:
            print("✓ %s  — %d slayd, uch til to'liq" % (name, n))
    sys.exit(1 if bad else 0)
