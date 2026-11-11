#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_lesson.py — Universal Rapid Lesson Compiler & Scaffolder

Target International School · Vibecoding (5–11-sinflar)
Author: Ismoiljon Usmonov / Antigravity

This tool replaces repetitive 1,200-line monolithic scripts with a single,
blazing-fast compiler that generates:
  1. prezentatsiya.html  (Canonical master presentation with touch controls, SVG logo, quiz, timer, notes)
  2. varaqa.html         (2-page printable A4 worksheet with 10-point rubric)
  3. vazifa.html         (Interactive homework app with LocalStorage auto-save)
  4. TEACHER_READING.md  (Pedagogical guide & timing roadmap)

Usage:
  # Quick scaffold with compliant defaults:
  python3 scripts/build_lesson.py --scaffold \
      --cohort 10-11-sinf --week 11 --lesson 26 \
      --title "Agentik Tool Calling va Funksiyalar" \
      --duration 80

  # Compile from a compact python lesson spec:
  python3 scripts/build_lesson.py spec_file.py
"""

import os
import sys
import json
import re
import argparse
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

COHORT_DATA = {
    "10-11-sinf": {
        "tag": "10-11-SINF",
        "track_uz": "Senior AI & Enterprise Kiberxavfsizlik Track",
        "track_ru": "Senior AI & Enterprise Кибербезопасность",
        "track_en": "Senior AI & Enterprise Cybersecurity Track",
        "label_uz": "10–11-sinf",
        "label_ru": "10–11 класс",
        "label_en": "Grade 10–11"
    },
    "9-sinf": {
        "tag": "9-SINF",
        "track_uz": "Junior Vibecoders, Full-Stack & DevOps Track",
        "track_ru": "Junior Vibecoders, Full-Stack & DevOps",
        "track_en": "Junior Vibecoders, Full-Stack & DevOps Track",
        "label_uz": "9-sinf",
        "label_ru": "9 класс",
        "label_en": "Grade 9"
    },
    "7-8-sinf": {
        "tag": "7-8-SINF",
        "track_uz": "Game Dev, Interaktiv Veb & FUT Creator Track",
        "track_ru": "Game Dev, Интерактивный Веб & FUT Creator",
        "track_en": "Game Dev, Interactive Web & FUT Creator Track",
        "label_uz": "7–8-sinf",
        "label_ru": "7–8 класс",
        "label_en": "Grade 7–8"
    },
    "5-6-sinf": {
        "tag": "5-6-SINF",
        "track_uz": "Junior Creators & Kiber-Gigiyena Track",
        "track_ru": "Junior Creators & Кибер-Гигиена",
        "track_en": "Junior Creators & Cyber Hygiene Track",
        "label_uz": "5–6-sinf",
        "label_ru": "5–6 класс",
        "label_en": "Grade 5–6"
    }
}

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text).strip("-")
    return text

def ensure_i18n_dict(val, default_uz="", default_ru=None, default_en=None):
    if default_ru is None:
        default_ru = default_uz
    if default_en is None:
        default_en = default_uz
    if isinstance(val, dict):
        uz = val.get("uz", default_uz)
        ru = val.get("ru", default_ru)
        en = val.get("en", default_en)
        return {"uz": uz, "ru": ru, "en": en}
    elif isinstance(val, str):
        # If val is a string, if default_ru was provided and different from default_uz, use it
        ru_val = default_ru if default_ru != default_uz else val
        en_val = default_en if default_en != default_uz else val
        return {"uz": val, "ru": ru_val, "en": en_val}
    return {"uz": default_uz, "ru": default_ru, "en": default_en}

def generate_notes_array(slides_count, custom_notes=None):
    notes = {"uz": [], "ru": [], "en": []}
    for i in range(slides_count):
        if custom_notes and i < len(custom_notes):
            n = custom_notes[i]
            t = ensure_i18n_dict(n.get("title", f"Slayd {i+1}"))
            s = ensure_i18n_dict(n.get("say", "Asosiy tushunchalarni diqqat bilan tushuntiring."))
            d = ensure_i18n_dict(n.get("do", "Doskaga misol yozing va o'quvchilardan fikr so'rang."))
            notes["uz"].append([t["uz"], s["uz"], d["uz"]])
            notes["ru"].append([t["ru"], s["ru"], d["ru"]])
            notes["en"].append([t["en"], s["en"], d["en"]])
        else:
            notes["uz"].append([f"Slayd {i+1} tahlili", "Asosiy tushunchalarni tushuntiring.", "Doskada ko'rsating va savol-javob qiling."])
            notes["ru"].append([f"Анализ слайда {i+1}", "Объясните ключевые концепции темы.", "Продемонстрируйте пример на доске."])
            notes["en"].append([f"Slide {i+1} Breakdown", "Explain core principles clearly.", "Demonstrate example on the board."])
    return notes

def build_presentation_html(spec):
    template_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html")
    with open(template_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    cohort = spec["cohort"]
    cinfo = COHORT_DATA.get(cohort, COHORT_DATA["10-11-sinf"])
    week = spec["week"]
    lesson_no = spec["lesson_no"]
    title = ensure_i18n_dict(spec["title"])
    lede = ensure_i18n_dict(spec.get("lede", "Zamonaviy IT va Vibecoding amaliyoti."))
    duration = spec.get("duration", 80)

    # Replace Title & Header
    deck_title_uz = f"{lesson_no}-dars: {title['uz']}"
    deck_title_ru = f"Урок {lesson_no}: {title['ru']}"
    deck_title_en = f"Lesson {lesson_no}: {title['en']}"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{deck_title_ru}" data-en="{deck_title_en}">{deck_title_uz}</title>',
                 tpl)

    # Floating brand tag
    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 f'<span class="tag" data-ru="{cinfo["label_ru"].upper()}" data-en="{cinfo["label_en"].upper()}">{cinfo["label_uz"].upper()}</span>',
                 tpl)

    # TITLES dict formatted with indent for verify_i18n.py compatibility
    titles_dict = {"uz": deck_title_uz, "ru": deck_title_ru, "en": deck_title_en}
    titles_json = json.dumps(titles_dict, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    # Build Slides
    slides_markup = []
    
    # Slide 1: Titul
    s1 = f"""  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00">
    <div class="eyebrow"><span class="t" data-ru="{cinfo['label_ru']} · {week}-Я НЕДЕЛЯ · УРОК {lesson_no}" data-en="{cinfo['label_en']} · WEEK {week} · LESSON {lesson_no}">{cinfo['label_uz']} · {week}-HAFTA · {lesson_no}-DARS</span></div>
    <h1 class="display" data-ru="{title['ru']}" data-en="{title['en']}">{title['uz']}</h1>
    <p class="lede" data-ru="{lede['ru']}" data-en="{lede['en']}">{lede['uz']}</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Class Format">{duration} daqiqalik {'Juftlik Blok' if duration > 45 else 'Yakka Dars'}</div>
        <h3 data-ru="Практическая миссия" data-en="Hands-on Mission">Amaliy Missiya</h3>
        <p data-ru="Каждый ученик реализует работающий компонент и проходит тестирование." data-en="Each student implements a functional component and undergoes testing.">Har bir o'quvchi dars oxirida ishlaydigan natijaga erishadi va kiber-testdan o'tadi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Стандарт оценки" data-en="Assessment Rubric">10 Ballik Mezon</div>
        <h3 data-ru="3 Уровня сложности" data-en="3-Tier Homework">3 Darajali Rubrika</h3>
        <p data-ru="4 балла: База · 4 балла: Проект · 2 балла: Кибер-Вызов." data-en="4 pts: Base · 4 pts: Project · 2 pts: Cyber-Challenge.">4 ball: Baza · 4 ball: Amaliy Loyiha · 2 ball: Kiber-Chaqiruv.</p>
      </div>
    </div>
  </section>"""
    slides_markup.append(s1)

    # Slide 2: MANDATORY HW REVIEW
    hw_rev = spec.get("hw_review", {})
    pitfall = hw_rev.get("pitfall", {
        "title": {"uz": "Keng Tarqalgan Xato (Pitfall)", "ru": "Типичная Ошибка (Pitfall)", "en": "Common Pitfall"},
        "desc": {"uz": "O'tgan dars vazifasida sintaksis yoki xatoliklar tekshirilmagan holat.",
                 "ru": "В домашнем задании прошлого урока отсутствовала проверка ошибок или параметров.",
                 "en": "Missing error checks or input validation in previous homework."},
        "code": "// ❌ Xato kod namunalari"
    })
    solution = hw_rev.get("solution", {
        "title": {"uz": "Oltin Yechim (Golden Standard)", "ru": "Золотой Стандарт (Golden Solution)", "en": "Golden Standard Solution"},
        "desc": {"uz": "Toza muhandislik amaliyoti va to'liq himoyalangan kod.",
                 "ru": "Чистая инженерная практика и полностью защищенная реализация.",
                 "en": "Clean engineering best practice with robust safeguards."},
        "code": "// ✅ To'g'ri va xavfsiz yechim"
    })
    blitz = hw_rev.get("blitz", {
        "uz": "O'tgan mavzu bo'yicha 30 soniyalik tezkor savol.",
        "ru": "30-секундный блиц-опрос по ключевому материалу прошлого урока.",
        "en": "30-second rapid blitz question on key concepts."
    })
    bridge = hw_rev.get("bridge", {
        "uz": "Nega bugungi yangi mavzu aynan shu muammoni hal qilish uchun kerak?",
        "ru": "Почему сегодняшняя тема необходима для решения этой фундаментальной проблемы?",
        "en": "Why today's new topic is essential to solve this fundamental challenge?"
    })

    pit_t = ensure_i18n_dict(pitfall.get("title"))
    pit_d = ensure_i18n_dict(pitfall.get("desc"))
    sol_t = ensure_i18n_dict(solution.get("title"))
    sol_d = ensure_i18n_dict(solution.get("desc"))
    blitz_t = ensure_i18n_dict(blitz)
    bridge_t = ensure_i18n_dict(bridge)

    s2 = f"""  <!-- SLIDE 2: MANDATORY HW REVIEW & BRIDGE -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор Д/З|HW Review" data-time="04:00–10:00">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ Д/З · РАЗБОР ОШИБОК" data-en="HOMEWORK AUDIT · PITFALL REVIEW">UY VAZIFASI TAHLILI · XATOLAR REVIZIYASI</span></div>
    <h2 data-ru="Разбор Домашнего Задания и Мост к Новой Теме" data-en="Homework Autopsy and Bridge to Today's Topic">O'tgan Dars Vazifasi Tahlili va Yangi Mavzuga Ko'prik</h2>
    <div class="cards-grid" style="grid-template-columns:1fr 1fr; gap:16px; margin-top:14px;">
      <div class="box" style="border-left:4px solid var(--accent);">
        <div class="tag" style="color:var(--accent-ink);" data-ru="Типичная ошибка" data-en="Common Pitfall">Xato Tahlili (Pitfall)</div>
        <h3 data-ru="{pit_t['ru']}" data-en="{pit_t['en']}">{pit_t['uz']}</h3>
        <p data-ru="{pit_d['ru']}" data-en="{pit_d['en']}">{pit_d['uz']}</p>
        <pre class="code-block" style="margin-top:8px;"><code>{pitfall.get('code', '// Buggy snippet')}</code></pre>
      </div>
      <div class="box" style="border-left:4px solid var(--green);">
        <div class="tag" style="color:var(--green);" data-ru="Золотой стандарт" data-en="Golden Standard">Oltin Yechim (Best Practice)</div>
        <h3 data-ru="{sol_t['ru']}" data-en="{sol_t['en']}">{sol_t['uz']}</h3>
        <p data-ru="{sol_d['ru']}" data-en="{sol_d['en']}">{sol_d['uz']}</p>
        <pre class="code-block" style="margin-top:8px;"><code>{solution.get('code', '// Verified snippet')}</code></pre>
      </div>
    </div>
    <div class="cards-grid" style="grid-template-columns:1fr 1fr; gap:16px; margin-top:14px;">
      <div class="box">
        <div class="tag" data-ru="Блиц-контроль (30 сек)" data-en="30s Blitz Check">30s Blits-Nazorat</div>
        <p data-ru="{blitz_t['ru']}" data-en="{blitz_t['en']}">{blitz_t['uz']}</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Мост к уроку" data-en="Bridge to Topic">Yangi Darsga Ko'prik</div>
        <p data-ru="{bridge_t['ru']}" data-en="{bridge_t['en']}">{bridge_t['uz']}</p>
      </div>
    </div>
  </section>"""
    slides_markup.append(s2)

    target_total = 14 if duration >= 70 else 9

    def get_slide_time(idx, total):
        if idx == 1:
            return "00:00–04:00"
        elif idx == 2:
            return "04:00–10:00"
        elif idx == total:
            return f"{duration-5:02d}:00–{duration:02d}:00"
        elif idx == total - 1:
            return f"{max(0, duration-30):02d}:00–{duration-5:02d}:00"
        elif idx == total - 2:
            return f"{max(0, duration-40):02d}:00–{max(0, duration-30):02d}:00"
        else:
            st = 10 + (idx - 3) * 3
            en = min(duration - 40, st + 3)
            return f"{st:02d}:00–{en:02d}:00"

    # Custom or Template Slides
    custom_slides = spec.get("slides", [])
    if custom_slides:
        for idx, cs in enumerate(custom_slides, start=3):
            phase = cs.get("phase", "Nazariya|Теория|Theory")
            stime = cs.get("time", get_slide_time(idx, len(custom_slides) + 5))
            eyebrow = ensure_i18n_dict(cs.get("eyebrow", f"MODUL {idx} · KONSEPT"))
            stitle = ensure_i18n_dict(cs.get("title", f"Mavzu {idx}"))
            slede = ensure_i18n_dict(cs.get("lede", ""))
            content_html = cs.get("body", "")
            slide_html = f"""  <!-- SLIDE {idx}: {stitle['uz']} -->
  <section class="slide" data-phase="{phase}" data-time="{stime}">
    <div class="eyebrow"><span class="t" data-ru="{eyebrow['ru']}" data-en="{eyebrow['en']}">{eyebrow['uz']}</span></div>
    <h2 data-ru="{stitle['ru']}" data-en="{stitle['en']}">{stitle['uz']}</h2>
    {f'<p class="lede" data-ru="{slede["ru"]}" data-en="{slede["en"]}">{slede["uz"]}</p>' if slede['uz'] else ''}
    {content_html}
  </section>"""
            slides_markup.append(slide_html)
    else:
        # Generate default slides matching target duration
        target_count = target_total
        for idx in range(3, target_count - 2):
            stime = get_slide_time(idx, target_count)
            s_def = f"""  <!-- SLIDE {idx} -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="{stime}">
    <div class="eyebrow"><span class="t" data-ru="КОНЦЕПТ {idx-2} · АРХИТЕКТУРА" data-en="CONCEPT {idx-2} · ARCHITECTURE">KONSEPT {idx-2} · ARXITEKTURA</span></div>
    <h2 data-ru="Архитектура и Основные Принципы #{idx-2}" data-en="Architecture and Core Principles #{idx-2}">Arxitektura va Asosiy Mexanizmlar #{idx-2}</h2>
    <p class="lede" data-ru="Ключевые механизмы реализации в реальных проектах." data-en="Key mechanisms in real-world production.">Real loyihalarda qo'llaniladigan asosiy muhandislik mexanizmlari.</p>
    <div class="cards-grid">
      <div class="box">
        <div class="tag" data-ru="Компонент A" data-en="Component A">A Komponent</div>
        <h3 data-ru="Входные данные" data-en="Input Stream">Kiruvchi Ma'lumotlar</h3>
        <p data-ru="Структурированные данные и валидация схемы." data-en="Structured data stream and schema validation.">Tizimga kiruvchi ma'lumotlar oqimi va ularning xavfsizlik tekshiruvi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Компонент B" data-en="Component B">B Komponent</div>
        <h3 data-ru="Обработка и логика" data-en="Business Logic">Mantiqiy Qayta Ishlash</h3>
        <p data-ru="Выполнение асинхронных операций без блокировки." data-en="Non-blocking asynchronous task execution.">Asinxron operatsiyalar va resurslarni optimallashtirish.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Компонент C" data-en="Component C">C Komponent</div>
        <h3 data-ru="Проверенный результат" data-en="Verified Output">Tasdiqlangan Natija</h3>
        <p data-ru="Гарантированный вывод и логирование событий." data-en="Guaranteed output and deterministic logging.">Kutilgan yakuniy natija va xatoliklarni qayd etish.</p>
      </div>
    </div>
  </section>"""
            slides_markup.append(s_def)

    # Interactive Quiz Slide
    quiz = spec.get("quiz", {
        "question": {"uz": "Ushbu arxitekturada eng xavfsiz va to'g'ri yondashuv qaysi?",
                     "ru": "Какой подход является наиболее безопасным и надежным в этой архитектуре?",
                     "en": "Which approach is most secure and robust in this architecture?"},
        "options": [
            {"uz": "Faqat bir martalik tekshiruv bilan cheklanish", "ru": "Ограничиться однократной проверкой", "en": "Relying on a single unverified check", "correct": False},
            {"uz": "Barcha kiruvchi parametrlarni validatsiya qilish va xatolarni ushlash", "ru": "Валидация всех параметров и строгий перехват ошибок", "en": "Strict input validation and explicit error handling", "correct": True},
            {"uz": "Xatolarni jim e'tiborsiz qoldirish", "ru": "Игнорирование ошибок в тихом режиме", "en": "Silently suppressing runtime errors", "correct": False}
        ],
        "reveal": {"uz": "To'g'ri javob: B! Barcha kiruvchi ma'lumotlar tekshirilishi va try/catch bilan o'ralishi shart.",
                   "ru": "Правильный ответ: B! Все входные параметры должны быть валидированы и защищены try/catch.",
                   "en": "Correct answer: B! All input arguments must be validated with explicit try/catch guards."}
    })
    q_text = ensure_i18n_dict(quiz["question"])
    q_rev = ensure_i18n_dict(quiz["reveal"])

    opts_html = []
    for opt in quiz["options"]:
        opt_t = ensure_i18n_dict(opt)
        cls = "quiz-opt correct" if opt.get("correct") else "quiz-opt"
        opts_html.append(f'<button type="button" class="{cls}" onclick="checkQuiz(this)" data-ru="{opt_t["ru"]}" data-en="{opt_t["en"]}">{opt_t["uz"]}</button>')

    quiz_time = get_slide_time(target_total - 2, target_total)
    quiz_slide = f"""  <!-- SLIDE QUIZ -->
  <section class="slide" data-phase="Interaktiv Test|Тест|Interactive Quiz" data-time="{quiz_time}">
    <div class="eyebrow"><span class="t" data-ru="КИБЕР-ТЕСТ · ПРОВЕРКА ПОНИМАНИЯ" data-en="CYBER QUIZ · KNOWLEDGE CHECK">KIBER-TEST · BILIMNI TEKSHIRISH</span></div>
    <h2 data-ru="{q_text['ru']}" data-en="{q_text['en']}">{q_text['uz']}</h2>
    <div class="quiz-box">
      <div class="quiz-options">
        {"".join(opts_html)}
      </div>
      <div class="quiz-feedback" id="quizFeedback"></div>
      <div style="margin-top:14px; display:flex; gap:10px; align-items:center;">
        <button type="button" class="dock-btn" onclick="toggleQuizReveal()" data-ru="Показать решение (R)" data-en="Reveal Solution (R)">Yechimni ko'rish (R)</button>
      </div>
      <div class="quiz-reveal" id="quizReveal" hidden>
        <p data-ru="{q_rev['ru']}" data-en="{q_rev['en']}">{q_rev['uz']}</p>
      </div>
    </div>
  </section>"""
    slides_markup.append(quiz_slide)

    # Practical / Arena Slide
    practice = spec.get("practice", {
        "title": "Katta Amaliy Arena",
        "time_min": 25 if duration >= 70 else 12,
        "task": "Berilgan spetsifikatsiya asosida modulni dasturlang va testlardan o'tkazing.",
        "steps": ["Asosiy funksiyani yozish", "Xatoliklarni ushlash", "Juftlikda tekshirish (Peer Review)"]
    })
    prac_t = ensure_i18n_dict(practice["title"])
    prac_task = ensure_i18n_dict(practice["task"])
    p_steps = "".join([f'<li data-ru="{s}" data-en="{s}">{s}</li>' for s in practice["steps"]])

    prac_time = get_slide_time(target_total - 1, target_total)
    prac_slide = f"""  <!-- SLIDE PRACTICE -->
  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="{prac_time}">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКАЯ АРЕНА" data-en="HANDS-ON ARENA">AMALIY ARENA</span></div>
    <h2 data-ru="{prac_t['ru']}" data-en="{prac_t['en']}">{prac_t['uz']}</h2>
    <p class="lede" data-ru="{prac_task['ru']}" data-en="{prac_task['en']}">{prac_task['uz']}</p>
    <div class="timer-box">
      <div class="timer-display" id="timerDisplay">25:00</div>
      <div class="timer-controls">
        <button type="button" class="dock-btn" onclick="startTimer(25*60)" data-ru="Старт (25 мин)" data-en="Start (25 min)">Boshlash (25 min)</button>
        <button type="button" class="dock-btn" onclick="resetTimer()" data-ru="Сброс" data-en="Reset">Qayta o'rnatish</button>
      </div>
    </div>
    <div class="box" style="margin-top:16px;">
      <h3 data-ru="Пошаговый план лаборатории" data-en="Step-by-step Lab Checklist">Amaliyot Bosqichlari</h3>
      <ol style="margin-left:20px; line-height:1.7;">
        {p_steps}
      </ol>
    </div>
  </section>"""
    slides_markup.append(prac_slide)

    # Slide Homework (3-Tiered)
    hw = spec.get("homework", {})
    t1 = ensure_i18n_dict(
        hw.get("tier1"),
        default_uz="1-Daraja (Baza, 4 ball): Darsdagi asosiy sintaksis va tuzilmani xatolarsiz takrorlash.",
        default_ru="1-й Уровень (База, 4 балла): Точное воспроизведение синтаксиса и архитектуры без ошибок.",
        default_en="Tier 1 (Base, 4 pts): Accurate reproduction of core syntax and architecture."
    )
    t2 = ensure_i18n_dict(
        hw.get("tier2"),
        default_uz="2-Daraja (Amaliy Loyiha, 4 ball): Qo'shimcha parametrlar va to'liq ishlovchi interfeys qo'shish.",
        default_ru="2-й Уровень (Проект, 4 балла): Добавление параметров и рабочей функциональности.",
        default_en="Tier 2 (Project, 4 pts): Implementing functional components and clean interfaces."
    )
    t3 = ensure_i18n_dict(
        hw.get("tier3"),
        default_uz="3-Daraja (Kiber-Chaqiruv, 2 ball): Xavfsizlik, chegaraviy holatlar (edge cases) va optimallik.",
        default_ru="3-й Уровень (Кибер-Вызов, 2 балла): Защита от ошибок, обработка edge cases и оптимизация.",
        default_en="Tier 3 (Cyber Challenge, 2 pts): Security hardening, edge-case handling, and optimization."
    )

    hw_time = get_slide_time(target_total, target_total)
    hw_slide = f"""  <!-- SLIDE HOMEWORK (3-TIER RUBRIC) -->
  <section class="slide" data-phase="Uy vazifasi|Домашнее задание|Homework" data-time="{hw_time}">
    <div class="eyebrow"><span class="t" data-ru="10-БАЛЛЬНАЯ СИСТЕМА · 3 УРОВНЯ" data-en="10-POINT RUBRIC · 3 TIERS">10 BALLIK MEZON · 3 BOSQICH</span></div>
    <h2 data-ru="Mustaqil Vazifa va Baholash Standarti" data-en="Independent Homework and Assessment Standards">Mustaqil Vazifa va 10 Ballik Baholash Standarti</h2>
    <div class="cards-grid">
      <div class="box">
        <div class="tag" style="color:var(--accent-ink);" data-ru="4 балла" data-en="4 points">1-Bosqich · 4 Ball</div>
        <h3 data-ru="База / Синтаксис" data-en="Base / Syntax">Baza va Sintaksis</h3>
        <p data-ru="{t1['ru']}" data-en="{t1['en']}">{t1['uz']}</p>
      </div>
      <div class="box">
        <div class="tag" style="color:var(--accent-ink);" data-ru="4 балла" data-en="4 points">2-Bosqich · 4 Ball</div>
        <h3 data-ru="Инженерия / Проект" data-en="Engineering / Project">Amaliy Loyiha</h3>
        <p data-ru="{t2['ru']}" data-en="{t2['en']}">{t2['uz']}</p>
      </div>
      <div class="box">
        <div class="tag" style="color:var(--accent-ink);" data-ru="2 балла" data-en="2 points">3-Bosqich · 2 Ball</div>
        <h3 data-ru="Кибер-Вызов / Защита" data-en="Cyber Challenge">Kiber-Chaqiruv</h3>
        <p data-ru="{t3['ru']}" data-en="{t3['en']}">{t3['uz']}</p>
      </div>
    </div>
    <div class="callout" style="margin-top:16px;">
      <p data-ru="Интерактивное выполнение доступно в файле vazifa.html (с автосохранением в LocalStorage) или в печатном листе varaqa.html." data-en="Interactive completion available in vazifa.html (with LocalStorage auto-save) or printable varaqa.html.">Topshiriqni <b>vazifa.html</b> ilovasida (LocalStorage avto-saqlash bilan) yoki <b>varaqa.html</b> qog'oz varaqasida topshirishingiz mumkin.</p>
    </div>
  </section>"""
    slides_markup.append(hw_slide)

    all_slides_html = "\n\n".join(slides_markup)

    # Replace stage slides
    tpl = re.sub(r'<div class="stage">[\s\S]*?</div><!-- /stage -->',
                 f'<div class="stage">\n{all_slides_html}\n</div><!-- /stage -->',
                 tpl)

    # Generate NOTES matching exact slide count
    slides_count = len(slides_markup)
    notes_obj = generate_notes_array(slides_count, spec.get("notes"))
    notes_json = json.dumps(notes_obj, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    return tpl

def build_varaqa_html(spec):
    template_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html")
    with open(template_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    cohort = spec["cohort"]
    cinfo = COHORT_DATA.get(cohort, COHORT_DATA["10-11-sinf"])
    week = spec["week"]
    lesson_no = spec["lesson_no"]
    title = ensure_i18n_dict(spec["title"])
    mission = ensure_i18n_dict(
        spec.get("mission"),
        default_uz="Darsdagi asosiy texnologik tamoyillarni amalda sinash va xatolarsiz natijaga erishish.",
        default_ru="Применение основных технологических принципов на практике и достижение безошибочного результата.",
        default_en="Hands-on testing of core technological principles and achieving robust, error-free results."
    )

    tpl = tpl.replace("{{LESSON_NUM}}", str(lesson_no))
    tpl = tpl.replace("{{TITLE_UZ}}", title["uz"])
    tpl = tpl.replace("{{TITLE_RU}}", title["ru"])
    tpl = tpl.replace("{{TITLE_EN}}", title["en"])
    tpl = tpl.replace("{{COHORT_LABEL_UZ}}", cinfo["label_uz"])
    tpl = tpl.replace("{{COHORT_LABEL_RU}}", cinfo["label_ru"])
    tpl = tpl.replace("{{COHORT_LABEL_EN}}", cinfo["label_en"])

    meta_uz = f"2-Chorak · {week}-hafta · {lesson_no}-dars · {cinfo['track_uz']}"
    meta_ru = f"2-я четверть · {week}-я неделя · {lesson_no}-й урок · {cinfo['track_ru']}"
    meta_en = f"Quarter 2 · Week {week} · Lesson {lesson_no} · {cinfo['track_en']}"
    tpl = tpl.replace("{{META_UZ}}", meta_uz)
    tpl = tpl.replace("{{META_RU}}", meta_ru)
    tpl = tpl.replace("{{META_EN}}", meta_en)

    tpl = tpl.replace("{{MISSION_UZ}}", mission["uz"])
    tpl = tpl.replace("{{MISSION_RU}}", mission["ru"])
    tpl = tpl.replace("{{MISSION_EN}}", mission["en"])

    # Section 1
    tpl = tpl.replace("{{SEC1_TITLE_UZ}}", "Arxitektura va Asosiy Mexanizmlar")
    tpl = tpl.replace("{{SEC1_TITLE_RU}}", "Архитектура и Ключевые Механизмы")
    tpl = tpl.replace("{{SEC1_TITLE_EN}}", "Architecture and Key Mechanisms")
    sec1_html = """    <div class="box-grid">
      <div class="box">
        <h4 data-ru="Теоретический базис" data-en="Theoretical Basis">Nazariy Asos</h4>
        <p data-ru="Опишите принцип работы ключевого компонента и его влияние на надежность." data-en="Describe the core component mechanism and its system impact.">Asosiy komponentning ishlash printsipi va uning tizimga ta'sirini yozing:</p>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="Анализ рисков" data-en="Risk Analysis">Xavflar Tahlili</h4>
        <p data-ru="Какие ошибки возникают при отсутствии защитных проверок?" data-en="What risks emerge without proper validation guards?">Himoya tekshiruvlari bo'lmaganda qanday zaifliklar yuzaga keladi?</p>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
    </div>"""
    tpl = tpl.replace("{{SEC1_CONTENT}}", sec1_html)

    # Section 2
    tpl = tpl.replace("{{SEC2_TITLE_UZ}}", "Kod Tahlili va Xatolarni Qidirish")
    tpl = tpl.replace("{{SEC2_TITLE_RU}}", "Анализ Кода и Поиск Ошибок")
    tpl = tpl.replace("{{SEC2_TITLE_EN}}", "Code Analysis and Bug Finding")
    sec2_html = """    <div class="code-snippet">// ⚠️ Xatoni toping va to'g'rilang:
function processData(input) {
  return input.trim().toLowerCase(); // input null bo'lsa nima bo'ladi?
}</div>
    <div class="write-line"></div>"""
    tpl = tpl.replace("{{SEC2_CONTENT}}", sec2_html)

    # Section 3
    tpl = tpl.replace("{{SEC3_TITLE_UZ}}", "Amaliy Laboratoriya Topshirig'i")
    tpl = tpl.replace("{{SEC3_TITLE_RU}}", "Практическое Лабораторное Задание")
    tpl = tpl.replace("{{SEC3_TITLE_EN}}", "Hands-on Lab Assignment")
    sec3_html = """    <div class="box">
      <p data-ru="Разработайте и протестируйте функциональный модуль. Запишите контрольный результат выполнения:" data-en="Develop and verify the target module. Record execution output:">Berilgan modulni dasturlang va testdan o'tkazing. Olingan natijani qayd eting:</p>
      <div class="write-line"></div>
      <div class="write-line"></div>
      <div class="write-line"></div>
    </div>"""
    tpl = tpl.replace("{{SEC3_CONTENT}}", sec3_html)

    # Section 4
    hw = spec.get("homework", {})
    t1 = ensure_i18n_dict(
        hw.get("tier1"),
        default_uz="Darsdagi asosiy sintaksisni takrorlash.",
        default_ru="Повторение и закрепление основного синтаксиса урока.",
        default_en="Reproduction and consolidation of core lesson syntax."
    )
    t2 = ensure_i18n_dict(
        hw.get("tier2"),
        default_uz="Yangi xususiyat yoki parametr qo'shish.",
        default_ru="Добавление новых параметров и функциональных возможностей.",
        default_en="Adding new parameters and functional capabilities."
    )
    t3 = ensure_i18n_dict(
        hw.get("tier3"),
        default_uz="Chekka holat (edge-case) yoki optimallashtirish.",
        default_ru="Обработка граничных случаев (edge cases) и оптимизация.",
        default_en="Handling edge cases and performance optimization."
    )

    sec4_html = f"""    <div class="box-grid" style="margin-top:8px;">
      <div class="box">
        <h4 data-ru="1-Уровень (4 балла)" data-en="Tier 1 (4 pts)">1-Bosqich (4 ball)</h4>
        <p data-ru="{t1['ru']}" data-en="{t1['en']}">{t1['uz']}</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="2-Уровень (4 балла)" data-en="Tier 2 (4 pts)">2-Bosqich (4 ball)</h4>
        <p data-ru="{t2['ru']}" data-en="{t2['en']}">{t2['uz']}</p>
        <div class="write-line"></div>
      </div>
    </div>
    <div class="box" style="margin-top:6px;">
      <h4 data-ru="3-Уровень: Кибер-Вызов (2 балла)" data-en="Tier 3: Cyber Challenge (2 pts)">3-Bosqich: Kiber-Chaqiruv (2 ball)</h4>
      <p data-ru="{t3['ru']}" data-en="{t3['en']}">{t3['uz']}</p>
      <div class="write-line"></div>
    </div>"""
    tpl = tpl.replace("{{SEC4_CONTENT}}", sec4_html)

    return tpl

def build_vazifa_html(spec):
    template_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html")
    with open(template_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    cohort = spec["cohort"]
    cinfo = COHORT_DATA.get(cohort, COHORT_DATA["10-11-sinf"])
    week = spec["week"]
    lesson_no = spec["lesson_no"]
    title = ensure_i18n_dict(spec["title"])
    slug = spec.get("slug", f"{lesson_no}-dars-{slugify(title['uz'])}")

    tpl = tpl.replace("{{TITLE_UZ}}", title["uz"])
    tpl = tpl.replace("{{TITLE_RU}}", title["ru"])
    tpl = tpl.replace("{{TITLE_EN}}", title["en"])
    tpl = tpl.replace("{{COHORT_LABEL_UZ}}", cinfo["label_uz"])
    tpl = tpl.replace("{{LESSON_SLUG}}", slug)
    tpl = tpl.replace("{{HERO_TAG_UZ}}", f"{cinfo['label_uz']} · {week}-hafta · {lesson_no}-dars")

    hero_desc_uz = f"{title['uz']} bo'yicha amaliy topshiriqlar va avtomatik saqlanuvchi sinov maydoni."
    hero_desc_ru = f"Практические задания и интерактивная среда тестирования по теме «{title['ru']}»."
    hero_desc_en = f"Hands-on exercises and interactive testing environment for '{title['en']}'."
    tpl = tpl.replace("{{HERO_DESC_UZ}}", hero_desc_uz)
    tpl = tpl.replace("{{HERO_DESC_RU}}", hero_desc_ru)
    tpl = tpl.replace("{{HERO_DESC_EN}}", hero_desc_en)

    hw = spec.get("homework", {})
    t1 = ensure_i18n_dict(
        hw.get("tier1"),
        default_uz="Fundamental tushuncha va asosiy sintaksis.",
        default_ru="Фундаментальные концепции и базовый синтаксис.",
        default_en="Fundamental concepts and core syntax."
    )
    t2 = ensure_i18n_dict(
        hw.get("tier2"),
        default_uz="Ishlaydigan toza kod va amaliy loyiha.",
        default_ru="Рабочий чистый код и практический проект.",
        default_en="Functional clean code and hands-on project."
    )
    t3 = ensure_i18n_dict(
        hw.get("tier3"),
        default_uz="Chegaraviy holatlar, kiber-himoya va sinov.",
        default_ru="Граничные случаи, кибер-защита и тестирование.",
        default_en="Edge cases, cyber security, and testing."
    )

    tpl = tpl.replace("{{RUBRIC_T1_UZ}}", t1["uz"])
    tpl = tpl.replace("{{RUBRIC_T1_RU}}", t1["ru"])
    tpl = tpl.replace("{{RUBRIC_T1_EN}}", t1["en"])
    tpl = tpl.replace("{{RUBRIC_T2_UZ}}", t2["uz"])
    tpl = tpl.replace("{{RUBRIC_T2_RU}}", t2["ru"])
    tpl = tpl.replace("{{RUBRIC_T2_EN}}", t2["en"])
    tpl = tpl.replace("{{RUBRIC_T3_UZ}}", t3["uz"])
    tpl = tpl.replace("{{RUBRIC_T3_RU}}", t3["ru"])
    tpl = tpl.replace("{{RUBRIC_T3_EN}}", t3["en"])

    tasks_html = f"""    <!-- TASK 1 -->
    <div class="task-card">
      <div class="task-head">
        <span class="task-badge" data-ru="Задание 1 · База" data-en="Task 1 · Base">1-Topshiriq · Baza</span>
        <span class="task-score" data-ru="4 балла" data-en="4 points">4 BALL</span>
      </div>
      <h3 data-ru="Фундаментальный Концепт" data-en="Core Concept">Asosiy Konsept va Nazariya</h3>
      <p data-ru="{t1['ru']}" data-en="{t1['en']}">{t1['uz']}</p>
      <textarea class="answer-area" placeholder="Javobingizni shu yerga yozing..." data-placeholder-ru="Напишите ваш ответ здесь..." data-placeholder-en="Write your answer here..."></textarea>
      <div class="btn-group">
        <button type="button" class="btn btn-outline" onclick="toggleSolution('sol1')" data-ru="Показать решение" data-en="Reveal Solution">Yechimni ko'rish / Fix</button>
      </div>
      <div class="solution-box" id="sol1" hidden>
        <h4 data-ru="Эталонное решение" data-en="Reference Solution">Oltin Yechim:</h4>
        <p data-ru="Ключевой алгоритм должен проверять все входные данные перед выполнением." data-en="The core algorithm must validate all incoming parameters before execution.">Asosiy algoritm kiruvchi ma'lumotlarni to'liq tekshirishi va aniq javob qaytarishi lozim.</p>
      </div>
    </div>

    <!-- TASK 2 -->
    <div class="task-card">
      <div class="task-head">
        <span class="task-badge" data-ru="Задание 2 · Проект" data-en="Task 2 · Project">2-Topshiriq · Amaliy Loyiha</span>
        <span class="task-score" data-ru="4 балла" data-en="4 points">4 BALL</span>
      </div>
      <h3 data-ru="Практическая Реализация Кода" data-en="Hands-on Implementation">Amaliy Kod Yozish</h3>
      <p data-ru="{t2['ru']}" data-en="{t2['en']}">{t2['uz']}</p>
      <div class="code-box">// Ushbu kodni to'ldiring:
function executeSolution() {{
  // Sizning kodingiz
}}</div>
      <textarea class="answer-area" placeholder="Kodingizni shu yerga yozing..." data-placeholder-ru="Напишите ваш код здесь..." data-placeholder-en="Write your code here..."></textarea>
      <div class="btn-group">
        <button type="button" class="btn btn-outline" onclick="toggleSolution('sol2')" data-ru="Показать решение" data-en="Reveal Solution">Yechimni ko'rish / Fix</button>
      </div>
      <div class="solution-box" id="sol2" hidden>
        <h4 data-ru="Эталонное решение" data-en="Reference Solution">Oltin Yechim:</h4>
        <pre><code>function executeSolution() {{
  try {{
    return {{ success: true }};
  }} catch (err) {{
    return {{ success: false, error: err.message }};
  }}
}}</code></pre>
      </div>
    </div>

    <!-- TASK 3 -->
    <div class="task-card">
      <div class="task-head">
        <span class="task-badge" data-ru="Задание 3 · Вызов" data-en="Task 3 · Challenge">3-Topshiriq · Kiber-Chaqiruv</span>
        <span class="task-score" data-ru="2 балла" data-en="2 points">2 BALL</span>
      </div>
      <h3 data-ru="Кибер-Защита и Edge Cases" data-en="Cyber Defense & Edge Cases">Kiber-Himoya va Murakkab Sinov</h3>
      <p data-ru="{t3['ru']}" data-en="{t3['en']}">{t3['uz']}</p>
      <textarea class="answer-area" placeholder="Xavfsizlik yechimini yozing..." data-placeholder-ru="Напишите решение по безопасности..." data-placeholder-en="Write your security solution..."></textarea>
      <div class="btn-group">
        <button type="button" class="btn btn-outline" onclick="toggleSolution('sol3')" data-ru="Показать решение" data-en="Reveal Solution">Yechimni ko'rish / Fix</button>
      </div>
      <div class="solution-box" id="sol3" hidden>
        <h4 data-ru="Эталонное решение" data-en="Reference Solution">Oltin Yechim:</h4>
        <p data-ru="Реализуйте лимит итераций (max iterations) и фильтрацию вредоносных символов." data-en="Implement loop limits (max iterations) and strict input sanitization.">Cheksiz sikllardan saqlanish uchun max_iterations qo'yish va kiruvchi belgilarni sanitarizatsiya qilish shart.</p>
      </div>
    </div>"""

    tpl = tpl.replace("{{TASKS_HTML}}", tasks_html)
    return tpl

def build_teacher_reading_md(spec):
    cohort = spec["cohort"]
    cinfo = COHORT_DATA.get(cohort, COHORT_DATA["10-11-sinf"])
    week = spec["week"]
    lesson_no = spec["lesson_no"]
    title = ensure_i18n_dict(spec["title"])
    duration = spec.get("duration", 80)

    md = f"""# O'qituvchi Uchun Metodik Qo'llanma (Teacher Reading Guide)

**Dars:** {lesson_no}-dars · {title['uz']}  
**Kohorta:** {cinfo['label_uz']} ({cinfo['track_uz']})  
**Hafta:** {week}-hafta  
**Davomiyligi:** {duration} daqiqa ({'Juftlik blok (2 x 40 min)' if duration >= 70 else 'Yakka dars (40 min)'})  

---

## 1. Darsning Pedagogik Maqsadi
* O'quvchilarda mavzu bo'yicha chuqur muhandislik tushunchasini shakllantirish.
* 2-slayd orqali o'tgan dars uy vazifasidagi odatiy xatolarni (pitfalls) tahlil qilish va yangi mavzuga mantiqiy ko'prik yasash.
* Amaliy arena / laboratoriya orqali ishlaydigan natijaga erishish.

---

## 2. Vaqt Taqsimoti (Pacing Roadmap)
"""
    if duration >= 70:
        md += """* **00:00–08:00 (8 daq):** Salomlashish va o'tgan dars uy vazifasi tahlili (Slide 2: Pitfall vs Golden Solution).
* **08:00–25:00 (17 daq):** Yangi mavzu bayoni, inline arxitektura sxemalari va taqqoslashlar.
* **25:00–35:00 (10 daq):** Interaktiv kiber-quiz va javoblarni tahlil qilish.
* **35:00–40:00 (5 daq):** Qisqa xulosa, ko'z mashqi va amaliy laboratoriyaga o'tish.
* **40:00–65:00 (25 daq):** Katta amaliy laboratoriya / arena (taymer ostida mustaqil kod yozish).
* **65:00–72:00 (7 daq):** Juftliklararo sinov (Peer-Review).
* **72:00–77:00 (5 daq):** Eng yaxshi natijalar taqdimoti (Demo).
* **77:00–80:00 (3 daq):** 10 ballik uy vazifasi tushuntirilishi va dars yakuni.
"""
    else:
        md += """* **00:00–06:00 (6 daq):** Kirish va o'tgan dars uy vazifasi tahlili (Slide 2).
* **06:00–20:00 (14 daq):** Yangi tushuncha va mini-demo.
* **20:00–26:00 (6 daq):** Interaktiv kiber-quiz.
* **26:00–36:00 (10 daq):** Mini-amaliyot va natijani tekshirish.
* **36:00–40:00 (4 daq):** Xulosa va 10 ballik uy vazifasi.
"""

    md += """---

## 3. Asosiy Savollar va Tekshiruv Nuqtalari
1. O'quvchilar xatoliklarni qay darajada tushundi?
2. Doskada ko'rsatilgan namuna toza muhandislik tamoyillariga mos keladimi?
3. Vazifaning 3-bosqichidagi kiber-chaqiruvni necha nafar o'quvchi uddaladi?
"""
    return md

def compile_lesson(spec):
    cohort = spec["cohort"]
    week = spec["week"]
    lesson_no = spec["lesson_no"]
    title = ensure_i18n_dict(spec["title"])
    slug = spec.get("slug", f"{lesson_no}-dars-{slugify(title['uz'])}")

    folder = os.path.join(REPO_ROOT, "classes", cohort, f"{week}-hafta", slug)
    os.makedirs(folder, exist_ok=True)

    print(f"\n🚀 \033[1;36mTarget Lesson Compiler:\033[0m Building lesson in \033[33m{folder}\033[0m")

    # 1. Prezentatsiya
    pres_html = build_presentation_html(spec)
    pres_path = os.path.join(folder, "prezentatsiya.html")
    with open(pres_path, "w", encoding="utf-8") as f:
        f.write(pres_html)
    print(f"  ✓ Created: {os.path.relpath(pres_path, REPO_ROOT)} ({len(pres_html)} bytes)")

    # 2. Varaqa
    var_html = build_varaqa_html(spec)
    var_path = os.path.join(folder, "varaqa.html")
    with open(var_path, "w", encoding="utf-8") as f:
        f.write(var_html)
    print(f"  ✓ Created: {os.path.relpath(var_path, REPO_ROOT)} ({len(var_html)} bytes)")

    # 3. Vazifa
    vaz_html = build_vazifa_html(spec)
    vaz_path = os.path.join(folder, "vazifa.html")
    with open(vaz_path, "w", encoding="utf-8") as f:
        f.write(vaz_html)
    print(f"  ✓ Created: {os.path.relpath(vaz_path, REPO_ROOT)} ({len(vaz_html)} bytes)")

    # 4. Teacher Reading
    tr_md = build_teacher_reading_md(spec)
    tr_path = os.path.join(folder, "TEACHER_READING.md")
    with open(tr_path, "w", encoding="utf-8") as f:
        f.write(tr_md)
    print(f"  ✓ Created: {os.path.relpath(tr_path, REPO_ROOT)} ({len(tr_md)} bytes)")

    # Run verification immediately
    verify_script = os.path.join(REPO_ROOT, "scripts", "verify_i18n.py")
    if os.path.exists(verify_script):
        print("\n🔍 Running verify_i18n.py validation...")
        res = subprocess.run([sys.executable, verify_script, folder], capture_output=True, text=True)
        print(res.stdout)
        if res.returncode != 0:
            print(f"\033[31mValidation reported issues:\033[0m\n{res.stderr}")
        else:
            print(f"\033[32m✨ 100% SUCCESS: All files compiled and validated!\033[0m\n")

    return folder

def main():
    parser = argparse.ArgumentParser(description="Universal Rapid Lesson Compiler & Scaffolder")
    parser.add_argument("spec_file", nargs="?", help="Path to Python or JSON spec file")
    parser.add_argument("--scaffold", action="store_true", help="Quickly scaffold a new lesson")
    parser.add_argument("--cohort", default="10-11-sinf", choices=list(COHORT_DATA.keys()))
    parser.add_argument("--week", type=int, default=11)
    parser.add_argument("--lesson", type=int, default=26)
    parser.add_argument("--title", default="Yangi Dars Mavzusi")
    parser.add_argument("--duration", type=int, default=80, choices=[40, 80])

    args = parser.parse_args()

    if args.spec_file:
        if args.spec_file.endswith(".py"):
            import importlib.util
            spec_path = os.path.abspath(args.spec_file)
            spec_name = os.path.splitext(os.path.basename(spec_path))[0]
            spec_mod = importlib.util.spec_from_file_location(spec_name, spec_path)
            mod = importlib.util.module_from_spec(spec_mod)
            spec_mod.loader.exec_module(mod)
            spec = getattr(mod, "LESSON_SPEC", getattr(mod, "LESSON", None))
            if not spec:
                print("Error: spec_file must define LESSON_SPEC or LESSON dictionary.")
                sys.exit(1)
        elif args.spec_file.endswith(".json"):
            with open(args.spec_file, "r", encoding="utf-8") as f:
                spec = json.load(f)
        else:
            print("Error: Unsupported file format. Use .py or .json")
            sys.exit(1)
        compile_lesson(spec)
    elif args.scaffold:
        spec = {
            "cohort": args.cohort,
            "week": args.week,
            "lesson_no": args.lesson,
            "title": {"uz": args.title, "ru": args.title, "en": args.title},
            "duration": args.duration
        }
        compile_lesson(spec)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
