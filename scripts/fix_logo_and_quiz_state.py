#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/fix_logo_and_quiz_state.py
Fixes:
1. Target Logo embedding with base64 data URI and dark mode filter across all test.html, vazifa.html, prezentatsiya.html
2. Fixes logo target link (href) to relative ../../../../index.html
3. Adds class dropdown placeholder '-- Sinfni Tanlang * --', 'Choice: IT', and visual 'is-selected' feedback
4. Upgrades quiz questions selected state (border, background, radio, and '✓ Tanlandi' badge)
"""

import os
import re
import glob
import pathlib

# Load the base64 logo URI from assets/logo-light.txt
with open("assets/logo-light.txt", "r", encoding="utf-8") as f:
    LOGO_DATA_URI = f.read().strip()

LOGO_CSS_DARK_FILTER = """
:root[data-theme="dark"] .logo-box img,
:root[data-theme="dark"] .nav-brand .logo-box img,
:root[data-theme="dark"] .floating-brand .logo-box img,
:root[data-theme="dark"] .brandmark img {
  filter: brightness(0) invert(1) !important;
}
"""

QUIZ_SELECTED_CSS = """
/* Enhanced Quiz Choice Selected State & Select Dropdown */
select.input-field.is-selected {
  border-color: #10B981 !important;
  background-color: rgba(16, 185, 129, 0.08) !important;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.25) !important;
}

.choice-card.selected {
  border-color: #6366F1 !important;
  background: rgba(99, 102, 241, 0.18) !important;
  box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.4), 0 4px 16px rgba(99, 102, 241, 0.15);
}

:root[data-theme="dark"] .choice-card.selected {
  background: rgba(99, 102, 241, 0.32) !important;
  border-color: #818CF8 !important;
  box-shadow: 0 0 0 2px rgba(129, 140, 248, 0.5), 0 4px 20px rgba(99, 102, 241, 0.25);
}

.choice-card.selected .choice-letter {
  background: #6366F1 !important;
  color: #FFFFFF !important;
  border-color: #6366F1 !important;
  transform: scale(1.1);
  box-shadow: 0 2px 8px rgba(99, 102, 241, 0.5);
}
"""

def fix_test_html(filepath):
    p = pathlib.Path(filepath)
    if not p.is_file():
        return
    content = p.read_text(encoding="utf-8")

    # 1. Inject dark mode filter & quiz selected CSS
    if "select.input-field.is-selected" not in content:
        content = content.replace("</style>", QUIZ_SELECTED_CSS + "\n" + LOGO_CSS_DARK_FILTER + "\n</style>", 1)

    # 2. Fix Logo src to base64 DATA URI
    content = re.sub(
        r'<div class="logo-box"><img src="[^"]*" alt="Target Logo"></div>',
        f'<div class="logo-box"><img src="{LOGO_DATA_URI}" alt="Target Logo"></div>',
        content
    )

    # 3. Fix Logo target link & Home button link to relative path
    # Depth for classes/*/*/*/test.html is 4 levels deep
    content = re.sub(
        r'<a href="/index\.html" class="nav-brand">',
        r'<a href="../../../../index.html" class="nav-brand" title="Bosh sahifa / Home" data-title-ru="Главная страница / Home" data-title-en="Home Page">',
        content
    )
    content = re.sub(
        r'<a href="/index\.html" class="dock-btn back-btn" title="Bosh sahifa" data-title-ru="Главная" data-title-en="Home">🏠</a>',
        r'<a href="../../../../index.html" class="dock-btn back-btn" title="Bosh sahifa" data-title-ru="Главная" data-title-en="Home">🏠</a>',
        content
    )

    # 4. Fix select dropdown options: add placeholder & Choice IT
    # Determine cohort from path
    path_str = str(filepath)
    cohort_options = []
    if "9-sinf" in path_str:
        cohort_options = ["9-A", "9-B", "Choice: IT"]
    elif "10-11-sinf" in path_str:
        cohort_options = ["10-A", "10-B", "11-A", "11-B", "Choice: IT"]
    elif "7-8-sinf" in path_str:
        cohort_options = ["7-A", "7-B", "8-A", "8-B"]
    elif "5-6-sinf" in path_str:
        cohort_options = ["5-A", "5-B", "6-A", "6-B"]

    opts_html = '<option value="" disabled selected data-ru="-- Выберите класс --" data-en="-- Select Class --">-- Sinfni Tanlang * --</option>\n'
    for c in cohort_options:
        opts_html += f'          <option value="{c}">{c}</option>\n'

    # Replace <select id="studentClass" ...> ... </select>
    content = re.sub(
        r'<select id="studentClass"[^>]*>.*?</select>',
        f'<select id="studentClass" class="input-field" onchange="onClassChange()">\n          {opts_html}        </select>',
        content,
        flags=re.DOTALL
    )

    # 5. Add onClassChange() and enhance selectChoice() in JS
    on_class_change_js = """
function onClassChange() {
  var sel = document.getElementById('studentClass');
  if (sel.value) {
    sel.classList.add('is-selected');
  } else {
    sel.classList.remove('is-selected');
  }
  saveStudentProfile();
}
"""
    if "function onClassChange()" not in content:
        content = content.replace("function saveStudentProfile()", on_class_change_js + "\nfunction saveStudentProfile()", 1)

    # Enhance selectChoice to update status badge on question
    old_select_choice = """function selectChoice(qId, choiceIdx) {
  if (isSubmitted) return;
  answers[qId] = choiceIdx;
  var card = document.getElementById('card_' + qId);
  var choices = card.querySelectorAll('.choice-card');
  choices.forEach(function(c, idx) {
    c.classList.toggle('selected', idx === choiceIdx);
    var radio = c.querySelector('input[type="radio"]');
    if (radio) radio.checked = (idx === choiceIdx);
  });
}"""

    new_select_choice = """function selectChoice(qId, choiceIdx) {
  if (isSubmitted) return;
  answers[qId] = choiceIdx;
  var card = document.getElementById('card_' + qId);
  var choices = card.querySelectorAll('.choice-card');
  choices.forEach(function(c, idx) {
    c.classList.toggle('selected', idx === choiceIdx);
    var radio = c.querySelector('input[type="radio"]');
    if (radio) radio.checked = (idx === choiceIdx);
  });

  var statusBadge = document.getElementById('status_' + qId);
  if (statusBadge && !isSubmitted) {
    statusBadge.innerHTML = '<span style="color:#10B981; font-weight:700; font-size:12px; background:rgba(16,185,129,0.12); padding:3px 8px; border-radius:6px; border:1px solid rgba(16,185,129,0.3);">✓ ' + 
      (currentLang === 'ru' ? 'Выбрано' : (currentLang === 'en' ? 'Selected' : 'Tanlandi')) + '</span>';
  }
}"""
    content = content.replace(old_select_choice, new_select_choice)

    # Enhance submitTest to validate sClass
    old_sub_val = "  if (!name || !email) {"
    new_sub_val = """  if (!sClass) {
    alert(currentLang === 'ru' ? 'Пожалуйста, выберите ваш класс!' : (currentLang === 'en' ? 'Please select your class!' : 'Iltimos, sinfingizni tanlang!'));
    document.getElementById('studentClass').focus();
    return;
  }

  if (!name || !email) {"""
    if "if (!sClass)" not in content:
        content = content.replace(old_sub_val, new_sub_val, 1)

    # Enhance loadStudentProfile to restore is-selected class
    old_load = "if (p.sClass) document.getElementById('studentClass').value = p.sClass;"
    new_load = """if (p.sClass) {
        document.getElementById('studentClass').value = p.sClass;
        document.getElementById('studentClass').classList.add('is-selected');
      }"""
    if "sel.classList.add('is-selected')" not in content:
        content = content.replace(old_load, new_load, 1)

    p.write_text(content, encoding="utf-8")
    print(f"✓ Fixed test.html: {filepath}")

def fix_presentation_html(filepath):
    p = pathlib.Path(filepath)
    if not p.is_file():
        return
    content = p.read_text(encoding="utf-8")

    # Inject dark mode logo filter if missing
    if "filter: brightness(0) invert(1)" not in content:
        content = content.replace("</style>", LOGO_CSS_DARK_FILTER + "\n</style>", 1)

    # Fix Logo src to base64 DATA URI
    content = re.sub(
        r'<div class="logo-box">\s*<img src="[^"]*" alt="Target Logo">\s*</div>',
        f'<div class="logo-box"><img src="{LOGO_DATA_URI}" alt="Target Logo"></div>',
        content
    )

    # Fix floating-brand href to relative path
    content = re.sub(
        r'<a href="/index\.html" class="floating-brand"',
        r'<a href="../../../../index.html" class="floating-brand"',
        content
    )
    content = re.sub(
        r'<a href="/index\.html" class="brandmark"',
        r'<a href="../../../../index.html" class="brandmark"',
        content
    )

    p.write_text(content, encoding="utf-8")
    print(f"✓ Fixed prezentatsiya.html: {filepath}")

def fix_vazifa_html(filepath):
    p = pathlib.Path(filepath)
    if not p.is_file():
        return
    content = p.read_text(encoding="utf-8")

    # Inject dark mode logo filter if missing
    if "filter: brightness(0) invert(1)" not in content:
        content = content.replace("</style>", LOGO_CSS_DARK_FILTER + "\n</style>", 1)

    # Fix Logo src to base64 DATA URI
    content = re.sub(
        r'<div class="logo-box"><img src="[^"]*" alt="Target Logo"></div>',
        f'<div class="logo-box"><img src="{LOGO_DATA_URI}" alt="Target Logo"></div>',
        content
    )

    # Fix nav-brand href to relative path
    content = re.sub(
        r'<a href="/index\.html" class="nav-brand"',
        r'<a href="../../../../index.html" class="nav-brand"',
        content
    )
    content = re.sub(
        r'<a href="/index\.html" class="dock-btn back-btn"',
        r'<a href="../../../../index.html" class="dock-btn back-btn"',
        content
    )

    p.write_text(content, encoding="utf-8")
    print(f"✓ Fixed vazifa.html: {filepath}")

def main():
    print("Fixing Logo and Quiz Selection State across all files...")
    
    # 1. Fix all test.html
    for test_file in sorted(glob.glob("classes/**/test.html", recursive=True)):
        fix_test_html(test_file)

    # 2. Fix all vazifa.html
    for vazifa_file in sorted(glob.glob("classes/**/vazifa.html", recursive=True)):
        fix_vazifa_html(vazifa_file)

    # 3. Fix all prezentatsiya.html
    for pres_file in sorted(glob.glob("classes/**/prezentatsiya.html", recursive=True)):
        fix_presentation_html(pres_file)

if __name__ == "__main__":
    main()
