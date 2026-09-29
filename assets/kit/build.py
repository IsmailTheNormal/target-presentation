# -*- coding: utf-8 -*-
"""
Dars qurish to'plami (lesson kit).

Shassi `classes/10-11-sinf/3-hafta/14-dars-tool-calling-va-funksiyalar/` dan
olingan. CSS, tema tizimi, til almashtirish, taymer, logotip — tegilmaydi.
Faqat slaydlar, NOTES va varaqa tanasi almashtiriladi (AGENTS.md).

In-place i18n standarti: o'zbekcha — element ichidagi birlamchi matn,
ruscha — data-ru, inglizcha — data-en. Uchalasi HAR DOIM to'ldiriladi.
"""

import json
import pathlib

KIT = pathlib.Path(__file__).resolve().parent
ROOT = KIT.parent.parent

PREZ_HEAD = (KIT / "prez_head.html").read_text(encoding="utf-8")
PREZ_TAIL = (KIT / "prez_tail.html").read_text(encoding="utf-8")
VARAQA_HEAD = (KIT / "varaqa_head.html").read_text(encoding="utf-8")
VARAQA_TAIL = (KIT / "varaqa_tail.html").read_text(encoding="utf-8")


# ---------------------------------------------------------------- i18n yordamchilari

def a(s):
    """Atribut qiymati. Repo konvensiyasi: faqat qo'shtirnoq qochiriladi —
    <b>, &nbsp; kabi HTML atribut ichida tirik qoladi va innerHTML bilan
    to'g'ri render bo'ladi."""
    return str(s).replace('"', "&quot;")


def i18n(uz, ru, en):
    """data-ru / data-en juftligi. Bo'sh qolsa shassi o'zbekchaga qaytadi."""
    return 'data-ru="%s" data-en="%s"' % (a(ru), a(en))


def el(tag, uz, ru, en, cls=None, extra=""):
    c = ' class="%s"' % cls if cls else ""
    x = " " + extra if extra else ""
    return "<%s%s%s %s>%s</%s>" % (tag, c, x, i18n(uz, ru, en), uz, tag)


def li(uz, ru, en):
    """Ma'lum tuzoq #1: `li` grid — butun matn bitta <span class="t"> ichida."""
    return '  <li><span class="t" %s>%s</span></li>' % (i18n(uz, ru, en), uz)


def ul(items, cls="plain"):
    return '<ul class="%s">\n%s\n</ul>' % (cls, "\n".join(li(*t) for t in items))


def phase(uz, ru, en):
    """data-phase / data-time ajratgichi `|`: ru|en|uz (JS ORDER tartibi)."""
    return "%s|%s|%s" % (ru, en, uz)


def box(kind, h, items=None, p=None, extra_html=""):
    """kind: '', 'accent', 'green', 'purple'. h/p — (uz, ru, en) uchligi."""
    cls = "box " + kind if kind else "box"
    out = ['<div class="%s">' % cls, "  " + el("h3", *h)]
    if p:
        out.append("  " + el("p", *p))
    if items:
        out.append("  " + ul(items).replace("\n", "\n  "))
    if extra_html:
        out.append("  " + extra_html)
    out.append("</div>")
    return "\n".join(out)


def code(text):
    esc = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return '<pre class="code-block">%s</pre>' % esc


def slide(ph, time, eyebrow, title, body, first=False):
    """ph/eyebrow/title — (uz, ru, en) uchligi. body — tayyor HTML."""
    cls = "slide is-on title-slide" if first else "slide"
    return (
        '<section class="%s" data-phase="%s" data-time="%s">\n'
        '  <div class="eyebrow"><span %s>%s</span></div>\n'
        "  %s\n"
        "%s\n"
        "</section>"
    ) % (cls, phase(*ph), time, i18n(*eyebrow), eyebrow[0],
         el("h2", *title), body)


def title_slide(ph, time, eyebrow, h1, lede, meta):
    """meta — [(uz, ru, en), ...] uchliklari ro'yxati."""
    metas = "\n".join("    <span %s>%s</span>" % (i18n(*m), m[0]) for m in meta)
    return (
        '<section class="slide is-on title-slide" data-phase="%s" data-time="%s">\n'
        '  <div class="eyebrow"><span %s>%s</span></div>\n'
        '  <div class="title-meta">\n%s\n  </div>\n'
        "  %s\n"
        "  %s\n"
        "</section>"
    ) % (phase(*ph), time, i18n(*eyebrow), eyebrow[0], metas,
         el("h1", *h1), el("p", *lede, cls="lede"))


# ---------------------------------------------------------------- qurish

class Lesson:
    def __init__(self, outdir, titles, sheet_titles, key, slides, notes,
                 varaqa_body):
        self.outdir = ROOT / outdir
        self.titles = titles            # {'uz','ru','en'}
        self.sheet_titles = sheet_titles
        self.key = key                  # localStorage kaliti, masalan 'vc-notes-5-15'
        self.slides = slides            # HTML bloklari ro'yxati
        self.notes = notes              # {'ru': [[sarlavha, gap, amal], ...], ...}
        self.varaqa_body = varaqa_body

    def _check(self):
        n = len(self.slides)
        for lg in ("ru", "en", "uz"):
            got = len(self.notes[lg])
            if got != n:
                raise SystemExit(
                    "%s: %s izohlari soni (%d) slaydlar soniga (%d) teng emas"
                    % (self.outdir.name, lg, got, n))

    def build(self):
        self._check()
        self.outdir.mkdir(parents=True, exist_ok=True)

        j = lambda o: json.dumps(o, ensure_ascii=False, indent=2)

        prez = (PREZ_HEAD.replace("{{TITLE_RU}}", self.titles["ru"])
                + "\n\n" + "\n\n".join(self.slides) + "\n\n"
                + PREZ_TAIL.replace("{{TITLES_JSON}}", j(self.titles))
                           .replace("{{NOTES_JSON}}", j(self.notes))
                           .replace("{{NOTESKEY}}", self.key))
        (self.outdir / "prezentatsiya.html").write_text(prez, encoding="utf-8")

        varaqa = (VARAQA_HEAD.replace("{{TITLE_RU}}", self.sheet_titles["ru"])
                  + "\n" + self.varaqa_body + "\n"
                  + VARAQA_TAIL.replace("{{TITLES_JSON}}", j(self.sheet_titles))
                               .replace("{{SHEETKEY}}", self.key.replace("notes", "sheet")))
        (self.outdir / "varaqa.html").write_text(varaqa, encoding="utf-8")

        return self.outdir


# ---------------------------------------------------------------- varaqa yordamchilari

def sheet_header(h1, sub):
    """h1/sub — (uz, ru, en) uchligi."""
    return """  <div>
    <div class="brandrule"></div>
    <header>
      <div>
        %s
        <div style="font-family:'JetBrains Mono',monospace; font-size:7.5pt; color:var(--ink-2); margin-top:2px;" %s>%s</div>
      </div>
      <div class="meta">
        <span><span %s>Talaba:</span> <i class="s" style="width:90px;"></i></span>
        <span><span %s>Sinf:</span> <i class="s" style="width:40px;"></i> &nbsp;|&nbsp; <span %s>Sana:</span> <i class="s" style="width:52px;"></i></span>
        <span><span %s>Baho:</span> <b style="color:var(--accent-ink); font-size:9pt;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ 10</b></span>
      </div>
    </header>
""" % (el("h1", *h1), i18n(*sub), sub[0],
       i18n("Talaba:", "Студент:", "Student:"),
       i18n("Sinf:", "Класс:", "Class:"),
       i18n("Sana:", "Дата:", "Date:"),
       i18n("Baho:", "Оценка:", "Grade:"))


def mission(h, p):
    return '    <div class="mission-box">\n      %s\n      %s\n    </div>\n' % (
        el("h3", *h), el("p", *p))


def table(headers, rows):
    """headers — (uz,ru,en) uchliklari ro'yxati. rows — katak uchliklari
    ro'yxatlari; bo'sh satr uchun None yozing (o'quvchi to'ldiradi)."""
    th = "".join("<th %s>%s</th>" % (i18n(*h), h[0]) for h in headers)
    out = ['    <table class="lab-table">',
           "      <tr>%s</tr>" % th]
    for r in rows:
        tds = "".join(
            "<td></td>" if c is None else "<td %s>%s</td>" % (i18n(*c), c[0])
            for c in r)
        out.append("      <tr>%s</tr>" % tds)
    out.append("    </table>")
    return "\n".join(out) + "\n"


def sheet_box(h, body_html):
    return '    <div class="box">\n      %s\n%s\n    </div>' % (el("h4", *h), body_html)


def rubric(items, total):
    """items — ((uz,ru,en), '4') juftliklari. total — umumiy ball matni."""
    lis = "\n".join(
        '        <li><span %s>%s</span> <b>%s</b></li>' % (i18n(*t), t[0], b)
        for t, b in items)
    lis += '\n        <li><span %s>%s</span> <b>%s</b></li>' % (
        i18n("JAMI", "ИТОГО", "TOTAL"), "JAMI", total)
    return '      <ul class="rubric-list">\n%s\n      </ul>' % lis


def writelines(n, label=None):
    """Yozish uchun bo'sh chiziqlar."""
    line = ('<div style="border-bottom:1px solid var(--write); height:11pt; '
            'margin-top:5px;"></div>')
    head = ("      " + el("p", *label, extra='style="font-size:7.6pt; color:var(--ink-3); margin:0"') + "\n") if label else ""
    return head + "      " + ("\n      ".join([line] * n))


def sign_box(teacher="Musulmonov Mamarajab"):
    return """
  <div class="sign-box">
    <span %s>O'qituvchi: %s</span>
    <span %s>O'qituvchi imzosi: _______________</span>
    <span %s>Target International School</span>
  </div>""" % (
        i18n("O'qituvchi: " + teacher, "Учитель: " + teacher,
             "Instructor: " + teacher), teacher,
        i18n("O'qituvchi imzosi: _______________",
             "Подпись учителя: _______________",
             "Teacher signature: _______________"),
        i18n("Target International School", "Target International School",
             "Target International School"))
