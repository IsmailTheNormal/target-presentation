#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Target International School — Interactive Test & Email Dispatch Generator
Generates standalone, responsive, trilingual test.html files for all exam classes.
When a student passes the test, it captures the student's email and dispatches
the complete answers and score directly to the teacher's email: usmonovismoiljon12@gmail.com.
"""

import os
import json
import re
import html

TEACHER_EMAIL = "usmonovismoiljon12@gmail.com"

def split_title_and_code(text):
    """Splits question title into text prompt and code block if present"""
    parts = text.split("\n\n")
    if len(parts) > 1 and any(kw in parts[1] for kw in ["app.", "const ", "let ", "SELECT", "import ", "function", "docker ", "npm ", "<form", "router.", "def ", "curl ", "python", "CREATE ", "SELECT "]):
        return parts[0], "\n\n".join(parts[1:])
    return text, None

def generate_test_html(exam):
    folder_path = exam["folder_path"]
    title = exam["title"]
    desc = exam["description"]
    questions = exam["questions"]
    classes = exam.get("classes", ["A", "B"])
    cohort_id = exam["cohort_id"]
    lesson_id = exam["lesson_id"]

    # Build questions HTML
    q_html_parts = []
    for idx, q in enumerate(questions):
        q_num = idx + 1
        q_id = q["id"]
        pts = q["points"]
        
        # Title in 3 languages & separated code
        t_uz = q["title"]["uz"]
        t_ru = q["title"]["ru"]
        t_en = q["title"]["en"]
        t_uz_text, code_uz = split_title_and_code(t_uz)
        t_ru_text, _ = split_title_and_code(t_ru)
        t_en_text, _ = split_title_and_code(t_en)
        code_html = f'<pre class="code-box"><code>{html.escape(code_uz)}</code></pre>' if code_uz else ""

        choices_html = []
        for c_idx, c in enumerate(q["choices"]):
            choice_letter = chr(65 + c_idx)
            is_corr = "true" if c["correct"] else "false"
            c_uz = c["text"]["uz"]
            c_ru = c["text"]["ru"]
            c_en = c["text"]["en"]
            
            choices_html.append(f"""
            <label class="choice-card" data-correct="{is_corr}" onclick="selectChoice('{q_id}', {c_idx})">
              <input type="radio" name="{q_id}" value="{c_idx}" style="display:none;">
              <span class="choice-letter">{choice_letter}</span>
              <span class="choice-text" data-ru="{html.escape(c_ru)}" data-en="{html.escape(c_en)}">{html.escape(c_uz)}</span>
            </label>""")

        fb_corr_uz = q.get("feedback_correct", {}).get("uz", "To'g'ri!")
        fb_corr_ru = q.get("feedback_correct", {}).get("ru", "Правильно!")
        fb_corr_en = q.get("feedback_correct", {}).get("en", "Correct!")
        
        fb_inc_uz = q.get("feedback_incorrect", {}).get("uz", "Noto'g'ri javob.")
        fb_inc_ru = q.get("feedback_incorrect", {}).get("ru", "Неверно.")
        fb_inc_en = q.get("feedback_incorrect", {}).get("en", "Incorrect.")

        q_html_parts.append(f"""
        <!-- Question {q_num} -->
        <div class="question-card" id="card_{q_id}" data-points="{pts}">
          <div class="q-header">
            <span class="q-badge" data-ru="ВОПРОС {q_num} · {pts} БАЛЛА" data-en="QUESTION {q_num} · {pts} PTS">SAVOL {q_num} · {pts} BALL</span>
            <span class="q-status" id="status_{q_id}"></span>
          </div>
          <div class="q-title">
            <div class="q-title-text" data-ru="{html.escape(t_ru_text)}" data-en="{html.escape(t_en_text)}">{html.escape(t_uz_text)}</div>
            {code_html}
          </div>
          <div class="choices-list">
            {"".join(choices_html)}
          </div>
          <div class="feedback-box" id="feedback_{q_id}" style="display:none;" 
               data-corr-uz="{html.escape(fb_corr_uz)}" data-corr-ru="{html.escape(fb_corr_ru)}" data-corr-en="{html.escape(fb_corr_en)}"
               data-inc-uz="{html.escape(fb_inc_uz)}" data-inc-ru="{html.escape(fb_inc_ru)}" data-inc-en="{html.escape(fb_inc_en)}">
          </div>
        </div>""")

    class_options_html = "\n".join([f'<option value="{c}">{c}</option>' for c in classes])

    questions_json = json.dumps(questions, ensure_ascii=False)

    page_html = f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="{html.escape(title['ru'])}" data-en="{html.escape(title['en'])}">{html.escape(title['uz'])}</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap">

<style>
:root {{
  --bg: #07152D;
  --panel: #0E2246;
  --panel-2: #142E5C;
  --panel-hover: #19386D;
  --ink: #F0F4FA;
  --ink-2: #A5B6D0;
  --ink-3: #6C819F;
  --rule: #1B355A;
  --rule-light: rgba(255, 255, 255, 0.08);
  --accent: #FF3B26;
  --accent-ink: #FF7563;
  --accent-soft: rgba(255, 59, 38, 0.12);
  --blue-soft: #12284E;
  --green: #10B981;
  --green-soft: rgba(16, 185, 129, 0.12);
  --green-border: rgba(16, 185, 129, 0.4);
  --red: #EF4444;
  --red-soft: rgba(239, 68, 68, 0.12);
  --red-border: rgba(239, 68, 68, 0.4);
  --glass-bg: rgba(14, 34, 70, 0.88);
  --glass-border: rgba(255, 255, 255, 0.12);
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --shadow-sm: 0 4px 12px rgba(0, 0, 0, 0.25);
  --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.45);
}}

:root[data-theme="light"] {{
  --bg: #F8FAFD;
  --panel: #FFFFFF;
  --panel-2: #EDF2F9;
  --panel-hover: #E3EAF5;
  --ink: #00214A;
  --ink-2: #384A68;
  --ink-3: #7586A2;
  --rule: #DCE4EF;
  --rule-light: rgba(0, 33, 74, 0.06);
  --accent: #FF1100;
  --accent-ink: #C21000;
  --accent-soft: #FFEAE6;
  --blue-soft: #EBF2FE;
  --green: #0B6B4F;
  --green-soft: #DDF0E8;
  --green-border: rgba(11, 107, 79, 0.35);
  --red: #C21000;
  --red-soft: #FDE8E6;
  --red-border: rgba(194, 16, 0, 0.35);
  --glass-bg: rgba(255, 255, 255, 0.92);
  --glass-border: rgba(0, 33, 74, 0.12);
  --shadow-sm: 0 2px 8px rgba(0, 33, 74, 0.06);
  --shadow-lg: 0 12px 32px rgba(0, 33, 74, 0.12);
}}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: "Source Sans 3", sans-serif;
  background: var(--bg);
  color: var(--ink);
  line-height: 1.5;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  transition: background 0.2s ease, color 0.2s ease;
  padding-bottom: 80px;
}}

/* Floating Header Nav */
.top-nav {{
  position: sticky;
  top: 14px;
  z-index: 100;
  max-width: 900px;
  width: calc(100% - 32px);
  margin: 0 auto 24px;
  background: var(--glass-bg);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--glass-border);
  padding: 8px 18px;
  border-radius: 999px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: var(--shadow-sm);
}}

.nav-brand {{
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--ink);
}}

.nav-brand .logo-box img {{
  height: 22px;
  width: auto;
  display: block;
}}

.nav-brand .name {{
  font-family: "Manrope", sans-serif;
  font-weight: 800;
  font-size: 14px;
  letter-spacing: 0.04em;
}}

.nav-brand .tag {{
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--ink-2);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding-left: 8px;
  border-left: 1px solid var(--rule);
}}

.nav-tools {{
  display: flex;
  align-items: center;
  gap: 4px;
}}

.dock-btn {{
  background: transparent;
  border: none;
  color: var(--ink-2);
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  padding: 6px 12px;
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.18s ease;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}}

.dock-btn:hover {{
  color: var(--ink);
  background: var(--rule-light);
}}

.dock-btn.active {{
  color: var(--ink);
  background: var(--panel-2);
  border: 1px solid var(--rule);
  box-shadow: 0 2px 6px rgba(0,0,0,0.12);
}}

/* Main Container */
.container {{
  max-width: 900px;
  width: calc(100% - 32px);
  margin: 0 auto;
}}

/* Header Banner */
.hero-card {{
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: var(--radius-lg);
  padding: 32px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
  position: relative;
  overflow: hidden;
}}

.hero-card::before {{
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--accent) 0%, #6366F1 100%);
}}

.eyebrow {{
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  color: var(--accent);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}}

h1.test-title {{
  font-family: "Manrope", sans-serif;
  font-size: clamp(24px, 3.2vw, 36px);
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.2;
  color: var(--ink);
  margin-bottom: 12px;
}}

p.test-desc {{
  font-size: 15px;
  color: var(--ink-2);
  line-height: 1.6;
  white-space: pre-line;
}}

/* Student Info Grid */
.student-card {{
  background: var(--panel-2);
  border: 1px solid var(--rule);
  border-radius: var(--radius-md);
  padding: 20px;
  margin-top: 20px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
}}

.input-group label {{
  display: block;
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--ink-3);
  margin-bottom: 6px;
}}

.input-field {{
  width: 100%;
  padding: 10px 14px;
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: var(--radius-sm);
  font-family: "Source Sans 3", sans-serif;
  font-size: 14.5px;
  color: var(--ink);
  outline: none;
  transition: border-color 0.15s ease;
}}

.input-field:focus {{
  border-color: #6366F1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.25);
}}

select.input-field {{
  appearance: none;
  -webkit-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%23A5B6D0' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 14px center;
  padding-right: 36px;
  cursor: pointer;
}}

select.input-field option {{
  background: var(--panel);
  color: var(--ink);
  padding: 8px 12px;
}}

/* Questions List */
.questions-list {{
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 24px;
}}

.question-card {{
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: var(--radius-md);
  padding: 24px;
  box-shadow: var(--shadow-sm);
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}}

.question-card.correct {{
  border-color: var(--green);
  box-shadow: 0 0 0 1px var(--green);
}}

.question-card.wrong {{
  border-color: var(--red);
  box-shadow: 0 0 0 1px var(--red);
}}

.q-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}}

.q-badge {{
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  font-weight: 700;
  background: var(--accent-soft);
  color: var(--accent-ink);
  padding: 3px 10px;
  border-radius: 999px;
}}

.q-title {{
  font-size: 16.5px;
  font-weight: 600;
  color: var(--ink);
  line-height: 1.5;
  margin-bottom: 16px;
}}

.q-title-text {{
  margin-bottom: 8px;
}}

.code-box {{
  background: var(--bg);
  border: 1px solid var(--rule);
  border-radius: var(--radius-sm);
  padding: 12px 16px;
  font-family: "JetBrains Mono", monospace;
  font-size: 13px;
  color: var(--ink);
  overflow-x: auto;
  margin: 10px 0;
}}

/* Choice Options */
.choices-list {{
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.choice-card {{
  background: var(--panel-2);
  border: 1.5px solid var(--rule);
  border-radius: var(--radius-sm);
  padding: 12px 16px;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  cursor: pointer;
  transition: all 0.15s ease;
  user-select: none;
}}

.choice-card:hover {{
  border-color: var(--ink-3);
  background: var(--panel-hover);
}}

.choice-card.selected {{
  border-color: #6366F1;
  background: rgba(99, 102, 241, 0.1);
}}

.choice-card.is-correct {{
  border-color: var(--green) !important;
  background: var(--green-soft) !important;
}}

.choice-card.is-wrong {{
  border-color: var(--red) !important;
  background: var(--red-soft) !important;
}}

.choice-letter {{
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: var(--panel);
  border: 1px solid var(--rule);
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  color: var(--ink-2);
}}

.choice-card.selected .choice-letter {{
  background: #6366F1;
  color: #fff;
  border-color: #6366F1;
}}

.choice-card.is-correct .choice-letter {{
  background: var(--green);
  color: #fff;
  border-color: var(--green);
}}

.choice-card.is-wrong .choice-letter {{
  background: var(--red);
  color: #fff;
  border-color: var(--red);
}}

.choice-text {{
  font-size: 14.5px;
  color: var(--ink);
  line-height: 1.45;
  padding-top: 2px;
}}

/* Explanatory Feedback */
.feedback-box {{
  margin-top: 14px;
  padding: 12px 16px;
  border-radius: var(--radius-sm);
  font-size: 13.5px;
  line-height: 1.5;
}}

.feedback-box.correct-fb {{
  background: var(--green-soft);
  border: 1px solid var(--green-border);
  color: var(--green);
}}

.feedback-box.wrong-fb {{
  background: var(--red-soft);
  border: 1px solid var(--red-border);
  color: var(--red);
}}

/* Action Dock */
.submit-dock {{
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: var(--radius-md);
  padding: 20px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
  box-shadow: var(--shadow-sm);
}}

.btn-submit {{
  background: linear-gradient(135deg, #10B981 0%, #059669 100%);
  color: #FFFFFF;
  border: none;
  font-family: "Manrope", sans-serif;
  font-size: 15px;
  font-weight: 700;
  padding: 12px 28px;
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}}

.btn-submit:hover:not(:disabled) {{
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(16, 185, 129, 0.35);
}}

.btn-submit:disabled {{
  opacity: 0.6;
  cursor: not-allowed;
}}

/* Results Modal / Banner */
.results-card {{
  display: none;
  background: var(--panel);
  border: 2px solid var(--green);
  border-radius: var(--radius-lg);
  padding: 32px;
  margin-bottom: 24px;
  text-align: center;
  box-shadow: var(--shadow-lg);
  animation: popIn 0.3s ease;
}}

.results-card.failed {{
  border-color: var(--red);
}}

@keyframes popIn {{
  0% {{ transform: scale(0.95); opacity: 0; }}
  100% {{ transform: scale(1); opacity: 1; }}
}}

.score-circle {{
  width: 90px;
  height: 90px;
  border-radius: 50%;
  background: var(--green-soft);
  border: 3px solid var(--green);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px;
  font-family: "JetBrains Mono", monospace;
  font-size: 26px;
  font-weight: 800;
  color: var(--green);
}}

.results-card.failed .score-circle {{
  background: var(--red-soft);
  border-color: var(--red);
  color: var(--red);
}}

.email-status {{
  margin-top: 14px;
  font-size: 14px;
  padding: 10px 16px;
  border-radius: var(--radius-sm);
  background: var(--panel-2);
  display: inline-block;
  color: var(--ink-2);
}}
</style>
</head>
<body>

<!-- Floating Header Nav -->
<nav class="top-nav">
  <a href="/index.html" class="nav-brand">
    <div class="logo-box"><img src="/assets/target-logo.png" alt="Target Logo"></div>
    <span class="name">TARGET</span>
    <span class="tag">{cohort_id.upper()} · TEST</span>
  </a>
  <div class="nav-tools">
    <button type="button" class="dock-btn lang-btn active" data-lang="uz" onclick="setLang('uz')">UZ</button>
    <button type="button" class="dock-btn lang-btn" data-lang="ru" onclick="setLang('ru')">RU</button>
    <button type="button" class="dock-btn lang-btn" data-lang="en" onclick="setLang('en')">EN</button>
    <button type="button" class="dock-btn" onclick="toggleTheme()" title="Mavzu" data-title-ru="Тема" data-title-en="Theme">🌓</button>
    <a href="/index.html" class="dock-btn back-btn" title="Bosh sahifa" data-title-ru="Главная" data-title-en="Home">🏠</a>
  </div>
</nav>

<div class="container">

  <!-- Results Card (Revealed after submission) -->
  <div class="results-card" id="resultsCard">
    <div class="score-circle" id="scoreCircle">10/10</div>
    <h2 id="resultTitle" style="font-family:'Manrope',sans-serif; margin-bottom:8px;" data-ru="Тест успешно завершен!" data-en="Test Completed Successfully!">Sinov Muvaffaqiyatli Yakunlandi!</h2>
    <p id="resultSubtitle" style="color:var(--ink-2); font-size:16px;" data-ru="Результаты подсчитаны." data-en="Your score has been calculated.">Natijalaringiz hisoblandi.</p>
    <div class="email-status" id="emailStatus">
      📨 <span data-ru="Результаты отправляются учителю на" data-en="Sending results to instructor at">O'qituvchiga natijangiz yuborilmoqda:</span> (<b id="targetEmailLabel">{TEACHER_EMAIL}</b>)...
    </div>
    <div style="margin-top:16px;">
      <a href="#card_q1" class="back-btn" onclick="document.getElementById('card_q1').scrollIntoView({{behavior:'smooth'}})" data-ru="🔍 Подробный разбор ответов" data-en="🔍 Review Detailed Answers">🔍 Javoblar Tahlilini Ko'rish</a>
    </div>
  </div>

  <!-- Hero Card -->
  <div class="hero-card">
    <div class="eyebrow" data-ru="РУБЕЖНЫЙ КОНТРОЛЬ · ОЛИМПИАДА" data-en="MIDTERM EXAM · CYBER CHALLENGE">1-CHORAK ORALIQ NAZORAT · KIBER-TEST</div>
    <h1 class="test-title" data-ru="{html.escape(title['ru'])}" data-en="{html.escape(title['en'])}">{html.escape(title['uz'])}</h1>
    <p class="test-desc" data-ru="{html.escape(desc['ru'])}" data-en="{html.escape(desc['en'])}">{html.escape(desc['uz'])}</p>

    <!-- Student Identity -->
    <div class="student-card">
      <div class="input-group">
        <label data-ru="Ф.И.О. Ученика *" data-en="Student Full Name *">O'quvchi F.I.Sh. *</label>
        <input type="text" id="studentName" class="input-field" placeholder="Masalan: Sardor Alimov" data-placeholder-ru="Например: Сардор Алимов" data-placeholder-en="E.g.: Sardor Alimov" oninput="saveStudentProfile()">
      </div>
      <div class="input-group">
        <label data-ru="Ваш Email (для отчета) *" data-en="Your Email (for report) *">O'quvchi Emaili *</label>
        <input type="email" id="studentEmail" class="input-field" placeholder="nomi@maktab.uz yoki shaxsiy email" data-placeholder-ru="name@school.uz или личный email" data-placeholder-en="name@school.uz or personal email" oninput="saveStudentProfile()">
      </div>
      <div class="input-group">
        <label data-ru="Класс *" data-en="Class / Cohort *">Sinfni Tanlang *</label>
        <select id="studentClass" class="input-field" onchange="saveStudentProfile()">
          {class_options_html}
        </select>
      </div>
    </div>
  </div>

  <!-- Questions List -->
  <div class="questions-list">
    {"".join(q_html_parts)}
  </div>

  <!-- Submit Dock -->
  <div class="submit-dock">
    <div>
      <div style="font-family:'Manrope',sans-serif; font-weight:800; font-size:16px;" data-ru="Готовы отправить результат?" data-en="Ready to submit your test?">Testni topshirishga tayyormisiz?</div>
      <p style="font-size:13px; color:var(--ink-3);" data-ru="Результаты и ваш email будут отправлены учителю на {TEACHER_EMAIL}" data-en="Answers and your email will be submitted to the instructor at {TEACHER_EMAIL}">Natijangiz va javoblaringiz o'qituvchiga ({TEACHER_EMAIL}) yuboriladi.</p>
    </div>
    <button type="button" class="btn-submit" id="submitBtn" onclick="submitTest()">
      <span>🚀</span>
      <span data-ru="Завершить и Отправить Учителю" data-en="Complete and Submit to Instructor">Testni Yakunlash va Yuborish</span>
    </button>
  </div>

</div>

<script>
var TEACHER_EMAIL = "{TEACHER_EMAIL}";
var EXAM_DATA = {questions_json};
var EXAM_TITLE = {json.dumps(title, ensure_ascii=False)};
var currentLang = 'uz';
var answers = {{}};
var isSubmitted = false;

function setLang(lang) {{
  currentLang = lang;
  try {{ localStorage.setItem('target_lang', lang); }} catch(e) {{}}
  document.documentElement.lang = lang;
  document.querySelectorAll('.lang-btn').forEach(function(b) {{
    b.classList.toggle('active', b.getAttribute('data-lang') === lang);
  }});

  // Update in-place translations
  document.querySelectorAll('[data-ru], [data-en]').forEach(function(el) {{
    if (!el.getAttribute('data-uz-orig')) {{
      el.setAttribute('data-uz-orig', el.innerHTML);
    }}
    if (lang === 'uz') {{
      el.innerHTML = el.getAttribute('data-uz-orig');
    }} else if (lang === 'ru' && el.getAttribute('data-ru')) {{
      el.innerHTML = el.getAttribute('data-ru');
    }} else if (lang === 'en' && el.getAttribute('data-en')) {{
      el.innerHTML = el.getAttribute('data-en');
    }}
  }});

  var placeholders = document.querySelectorAll('[data-placeholder-ru], [data-placeholder-en]');
  placeholders.forEach(function(el) {{
    if (!el.getAttribute('data-ph-uz-orig')) {{
      el.setAttribute('data-ph-uz-orig', el.getAttribute('placeholder') || '');
    }}
    if (lang === 'uz') {{
      el.setAttribute('placeholder', el.getAttribute('data-ph-uz-orig'));
    }} else if (lang === 'ru' && el.getAttribute('data-placeholder-ru')) {{
      el.setAttribute('placeholder', el.getAttribute('data-placeholder-ru'));
    }} else if (lang === 'en' && el.getAttribute('data-placeholder-en')) {{
      el.setAttribute('placeholder', el.getAttribute('data-placeholder-en'));
    }}
  }});

  // Update feedback boxes if test already submitted
  if (isSubmitted) {{
    updateFeedbackTexts();
  }}
}}

function toggleTheme() {{
  var cur = document.documentElement.getAttribute('data-theme') || 'dark';
  var next = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  try {{ localStorage.setItem('target_theme', next); }} catch(e) {{}}
}}

function selectChoice(qId, choiceIdx) {{
  if (isSubmitted) return;
  answers[qId] = choiceIdx;
  var card = document.getElementById('card_' + qId);
  var choices = card.querySelectorAll('.choice-card');
  choices.forEach(function(c, idx) {{
    c.classList.toggle('selected', idx === choiceIdx);
    var radio = c.querySelector('input[type="radio"]');
    if (radio) radio.checked = (idx === choiceIdx);
  }});
}}

function saveStudentProfile() {{
  var profile = {{
    name: document.getElementById('studentName').value.trim(),
    email: document.getElementById('studentEmail').value.trim(),
    sClass: document.getElementById('studentClass').value
  }};
  try {{ localStorage.setItem('target_student_profile', JSON.stringify(profile)); }} catch(e) {{}}
}}

function loadStudentProfile() {{
  try {{
    var raw = localStorage.getItem('target_student_profile');
    if (raw) {{
      var p = JSON.parse(raw);
      if (p.name) document.getElementById('studentName').value = p.name;
      if (p.email) document.getElementById('studentEmail').value = p.email;
      if (p.sClass) document.getElementById('studentClass').value = p.sClass;
    }}
  }} catch(e) {{}}
}}

function updateFeedbackTexts() {{
  EXAM_DATA.forEach(function(q) {{
    var fb = document.getElementById('feedback_' + q.id);
    if (!fb || fb.style.display === 'none') return;
    var userChoice = answers[q.id];
    var isCorr = (userChoice !== undefined && q.choices[userChoice] && q.choices[userChoice].correct);
    var prefix = isCorr ? 'corr' : 'inc';
    var text = fb.getAttribute('data-' + prefix + '-' + currentLang) || fb.getAttribute('data-' + prefix + '-uz');
    fb.innerHTML = (isCorr ? '<b>✅ ' : '<b>❌ ') + (currentLang === 'ru' ? 'Пояснение: ' : (currentLang === 'en' ? 'Explanation: ' : 'Tushuntirish: ')) + '</b>' + text;
  }});
}}

function submitTest() {{
  var name = document.getElementById('studentName').value.trim();
  var email = document.getElementById('studentEmail').value.trim();
  var sClass = document.getElementById('studentClass').value;

  if (!name || !email) {{
    alert(currentLang === 'ru' ? 'Пожалуйста, введите ваше имя и email!' : (currentLang === 'en' ? 'Please enter your name and email!' : 'Iltimos, ismingiz va emailingizni kiriting!'));
    document.getElementById(name ? 'studentEmail' : 'studentName').focus();
    return;
  }}

  var answeredCount = Object.keys(answers).length;
  if (answeredCount < EXAM_DATA.length) {{
    if (!confirm(currentLang === 'ru' ? 'Вы ответили не на все вопросы. Все равно завершить?' : (currentLang === 'en' ? 'You have unanswered questions. Submit anyway?' : 'Barcha savollarga javob bermadingiz. Shunda ham topshirasizmi?'))) {{
      return;
    }}
  }}

  isSubmitted = true;
  document.getElementById('submitBtn').disabled = true;

  // Grade test
  var totalPoints = 0;
  var earnedPoints = 0;
  var breakdown = [];

  EXAM_DATA.forEach(function(q, idx) {{
    totalPoints += q.points;
    var card = document.getElementById('card_' + q.id);
    var userChoice = answers[q.id];
    var isCorr = (userChoice !== undefined && q.choices[userChoice] && q.choices[userChoice].correct);
    
    if (isCorr) {{
      earnedPoints += q.points;
      card.classList.add('correct');
      document.getElementById('status_' + q.id).innerHTML = '<span style="color:var(--green); font-weight:700;">+' + q.points + ' ball ✅</span>';
    }} else {{
      card.classList.add('wrong');
      document.getElementById('status_' + q.id).innerHTML = '<span style="color:var(--red); font-weight:700;">0 / ' + q.points + ' ❌</span>';
    }}

    // Reveal choices colors
    var choices = card.querySelectorAll('.choice-card');
    choices.forEach(function(c, cIdx) {{
      var isChoiceCorrect = (c.getAttribute('data-correct') === 'true');
      if (isChoiceCorrect) {{
        c.classList.add('is-correct');
      }} else if (cIdx === userChoice && !isChoiceCorrect) {{
        c.classList.add('is-wrong');
      }}
    }});

    // Show feedback
    var fb = document.getElementById('feedback_' + q.id);
    fb.style.display = 'block';
    fb.className = 'feedback-box ' + (isCorr ? 'correct-fb' : 'wrong-fb');

    var selectedText = (userChoice !== undefined && q.choices[userChoice]) ? q.choices[userChoice].text.uz : "Javob berilmadi";
    breakdown.push((idx + 1) + ") " + q.title.uz.split('\\n')[0] + "\\n   O'quvchi javobi: " + selectedText + " (" + (isCorr ? "+" + q.points + " ball" : "0 ball") + ")");
  }});

  updateFeedbackTexts();

  var pct = Math.round((earnedPoints / totalPoints) * 100);
  var passed = earnedPoints >= 7;

  // Show Results Banner
  var resCard = document.getElementById('resultsCard');
  resCard.style.display = 'block';
  resCard.classList.toggle('failed', !passed);
  document.getElementById('scoreCircle').textContent = earnedPoints + '/' + totalPoints;
  
  if (passed) {{
    document.getElementById('resultTitle').textContent = currentLang === 'ru' ? '🎉 Поздравляем! Вы успешно сдали тест!' : (currentLang === 'en' ? '🎉 Congratulations! You passed the test!' : '🎉 Tabriklaymiz! Siz sinovdan muvaffaqiyatli o\'tdingiz!');
    document.getElementById('resultSubtitle').textContent = (currentLang === 'ru' ? 'Вы набрали ' : (currentLang === 'en' ? 'You scored ' : 'Siz ')) + earnedPoints + ' / ' + totalPoints + ' (' + pct + '% · ' + (pct >= 90 ? 'A\'LO' : 'YAXSHI') + ')';
  }} else {{
    document.getElementById('resultTitle').textContent = currentLang === 'ru' ? '⚠️ Баллов недостаточно (порог: 7 баллов)' : (currentLang === 'en' ? '⚠️ Score insufficient (passing mark: 7 pts)' : '⚠️ Natija yetarli emas (o\'tish bali: 7 ball)');
    document.getElementById('resultSubtitle').textContent = earnedPoints + ' / ' + totalPoints + ' (' + pct + '%). Savollar tahlilini ko\'rib chiqing va qayta urinib ko\'ring.';
  }}

  resCard.scrollIntoView({{ behavior: 'smooth' }});

  // Prepare submission payload to teacher
  var subject = "Target Test: " + name + " (" + sClass + ") — " + earnedPoints + "/" + totalPoints + " ball (" + (passed ? "O'TDI" : "YIQILDI") + ")";
  var payload = {{
    _subject: subject,
    "O'quvchi F.I.Sh.": name,
    "O'quvchi Emaili": email,
    "Sinf": sClass,
    "Imtihon": EXAM_TITLE.uz,
    "To'plangan Ball": earnedPoints + " / " + totalPoints + " (" + pct + "%)",
    "Holat": passed ? "PASSED (O'TDI)" : "FAILED (YIQILDI)",
    "Topshirilgan Vaqt": new Date().toLocaleString(),
    "Batafsil Javoblar": breakdown.join("\\n\\n")
  }};

  var emailStatusEl = document.getElementById('emailStatus');
  emailStatusEl.innerHTML = '📨 O\\'qituvchiga (<b>' + TEACHER_EMAIL + '</b>) yuborilmoqda...';

  // Send to FormSubmit endpoint
  fetch('https://formsubmit.co/ajax/' + TEACHER_EMAIL, {{
    method: 'POST',
    headers: {{
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }},
    body: JSON.stringify(payload)
  }})
  .then(function(res) {{ return res.json(); }})
  .then(function(data) {{
    emailStatusEl.innerHTML = '✅ <b>Natijangiz va javoblaringiz o\\'qituvchiga (' + TEACHER_EMAIL + ') muvaffaqiyatli yetkazildi!</b>';
    emailStatusEl.style.background = 'var(--green-soft)';
    emailStatusEl.style.color = 'var(--green)';
  }})
  .catch(function(err) {{
    // Fallback: Direct mailto link
    var mailtoUrl = 'mailto:' + TEACHER_EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(
      "O'quvchi: " + name + " (" + sClass + ")\\nEmail: " + email + "\\nBall: " + earnedPoints + "/" + totalPoints + "\\n\\n" + breakdown.join("\\n\\n")
    );
    emailStatusEl.innerHTML = '⚠️ Avtomatik yuborishda tarmoq xatosi. <a href="' + mailtoUrl + '" style="color:var(--accent); font-weight:700; text-decoration:underline;">Bu yerni bosing va xat orqali yuboring</a>.';
  }});
}}

document.addEventListener('DOMContentLoaded', function() {{
  var savedTheme = 'dark';
  try {{ savedTheme = localStorage.getItem('target_theme') || 'dark'; }} catch(e) {{}}
  document.documentElement.setAttribute('data-theme', savedTheme);
  var savedLang = 'uz';
  try {{ savedLang = localStorage.getItem('target_lang') || 'uz'; }} catch(e) {{}}
  setLang(savedLang);
  loadStudentProfile();
}});
</script>
</body>
</html>
"""

    target_file = os.path.join(folder_path, "test.html")
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"✓ Generated {target_file}")
    return target_file

def main():
    with open("scripts/google_forms_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    generated = []
    for exam in data:
        f = generate_test_html(exam)
        generated.append(f)

    print(f"\nAll {len(generated)} interactive test pages generated successfully with direct email dispatch to {TEACHER_EMAIL}!")

if __name__ == "__main__":
    main()
