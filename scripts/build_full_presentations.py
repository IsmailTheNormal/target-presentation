#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import html

# We will read the CSS template and JS template from 28-dars
with open("classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/prezentatsiya.html", "r", encoding="utf-8") as f:
    t28 = f.read()

# Extract head CSS
css_chunk = t28[t28.find("<style>"):t28.find("</style>") + 8]

# Common floating header and dock template
def get_floating_elements(cohort_tag):
    return f"""
<a href="/index.html" class="floating-brand" title="Bosh sahifa / Home" data-title-ru="Главная страница / Home" data-title-en="Home Page">
  <div class="logo-box">
    <img src="/assets/target-logo.png" alt="Target Logo">
  </div>
  <span class="name">TARGET</span>
  <span class="tag">{cohort_tag}</span>
</a>

<!-- Floating Top-Right Controls Dock -->
<div class="floating-dock">
  <button class="dock-btn lang-btn" data-lang="uz" onclick="setLang('uz')" title="O'zbek tili" data-title-ru="Узбекский язык" data-title-en="Uzbek language">UZ</button>
  <button class="dock-btn lang-btn" data-lang="ru" onclick="setLang('ru')" title="Rus tili" data-title-ru="Русский язык" data-title-en="Russian language">RU</button>
  <button class="dock-btn lang-btn" data-lang="en" onclick="setLang('en')" title="Ingliz tili" data-title-ru="Английский язык" data-title-en="English language">EN</button>
  <button class="dock-btn" onclick="toggleTheme()" title="Mavzuni almashtirish" data-title-ru="Переключить тему" data-title-en="Toggle Theme">🌓</button>
  <button class="dock-btn" onclick="toggleNotes()" title="O'qituvchi izohlari (N)" data-title-ru="Заметки преподавателя (N)" data-title-en="Teacher Notes (N)">📝</button>
  <button class="dock-btn" onclick="toggleHelp()" title="Klavishlar yordami (?)" data-title-ru="Справка клавиш (?)" data-title-en="Keyboard Help (?)">⌨️</button>
</div>

<!-- Floating Slide Counter -->
<div class="floating-counter">
  <span class="curr" id="slide-curr">01</span> / <span id="slide-total">12</span>
</div>

<!-- Floating Phase Badge -->
<div class="floating-phase" id="slide-phase" data-phase="KIRISH|ВВЕДЕНИЕ|INTRO">
  KIRISH
</div>
"""

# Common Modals
def get_modals():
    return """
<!-- Teacher Notes Modal -->
<div class="notes-modal" id="notesModal" onclick="if(event.target===this)toggleNotes()">
  <div class="modal-box">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
      <h3 style="margin:0;" data-ru="Заметки преподавателя" data-en="Teacher Notes">O'qituvchi izohlari</h3>
      <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:var(--ink-2); cursor:pointer;" onclick="toggleNotes()">[ESC]</span>
    </div>
    <div class="notes-body" id="notesContent">...</div>
  </div>
</div>

<!-- Keyboard Help Modal -->
<div class="notes-modal" id="helpModal" onclick="if(event.target===this)toggleHelp()">
  <div class="modal-box">
    <h3 data-ru="Горячие клавиши" data-en="Keyboard Shortcuts">Klaviatura buyruqlari</h3>
    <table>
      <tr><td data-ru="→ / Space" data-en="→ / Space"><kbd>→</kbd> / <kbd>Space</kbd></td><td data-ru="Следующий слайд" data-en="Next slide">Keyingi slayd</td></tr>
      <tr><td data-ru="←" data-en="←"><kbd>←</kbd></td><td data-ru="Предыдущий слайд" data-en="Previous slide">Oldingi slayd</td></tr>
      <tr><td data-ru="L" data-en="L"><kbd>L</kbd></td><td data-ru="Сменить язык (UZ / RU / EN)" data-en="Toggle language (UZ / RU / EN)">Tilni almashtirish (UZ / RU / EN)</td></tr>
      <tr><td data-ru="T" data-en="T"><kbd>T</kbd></td><td data-ru="Светлая / Темная тема" data-en="Toggle Dark / Light theme">Yorug' / Qorong'i mavzu</td></tr>
      <tr><td data-ru="N" data-en="N"><kbd>N</kbd></td><td data-ru="Заметки учителя" data-en="Teacher notes">O'qituvchi izohlari</td></tr>
      <tr><td data-ru="?" data-en="?"><kbd>?</kbd></td><td data-ru="Справка клавиш" data-en="Keyboard help">Yordam oynasi</td></tr>
    </table>
  </div>
</div>
"""

print("Base generator helpers ready!")
