#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_9_w10_l30.py — 9-sinf (10-hafta 30-dars)
Mavzu: Komponentlar Falsafasi va UI Arxitekturasi: Reusable Components, Props & State
Track: Junior Vibecoders, Full-Stack & DevOps Track
Duration: 80 daqiqa (Double block / 2-hour class)
"""

import os
import sys
import json
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LESSON_DIR = os.path.join(REPO_ROOT, "classes", "9-sinf", "10-hafta", "30-dars-komponentlar-falsafasi-va-ui-arxitekturasi")
STUDIO_DIR = os.path.join(LESSON_DIR, "studio")
LAB_DIR = os.path.join(LESSON_DIR, "lab")
os.makedirs(STUDIO_DIR, exist_ok=True)
os.makedirs(LAB_DIR, exist_ok=True)

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
    TPL_PRES = f.read()

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
    TPL_VAR = f.read()

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
    TPL_VAZ = f.read()

def build_9_lesson():
    print("📦 Generating 9-sinf (30-dars: Komponentlar Falsafasi va UI Arxitekturasi)...")

    title_uz = "30-dars: Komponentlar Falsafasi va UI Arxitekturasi: Reusable Components, Props & State"
    title_ru = "Урок 30: Философия Компонентов и UI Архитектура: Reusable Components, Props & State"
    title_en = "Lesson 30: Component Philosophy & UI Architecture: Reusable Components, Props & State"

    # ============================================================
    # 1. PREZENTATSIYA.HTML (14 Slides, 80 Minutes)
    # ============================================================
    tpl = TPL_PRES
    tpl = re.sub(r"<title[^>]*>.*?</title>", f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>', tpl)
    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>', '<span class="tag" data-ru="9 · ВАЙБКОДИНГ" data-en="9 · VIBECODING">9 · VIBECODING</span>', tpl, count=1)
    tpl = tpl.replace('<span id="totalSlides">6</span>', '<span id="totalSlides">14</span>')

    titles_dict = {"uz": title_uz, "ru": title_ru, "en": title_en}
    titles_json = json.dumps(titles_dict, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    slides = []

    # Slide 1: Titul
    slides.append("""  <!-- SLIDE 1: TITUL -->
  <section class="slide is-on" data-phase="Kirish|Введение|Introduction" data-time="00:00–04:00">
    <div class="eyebrow" data-ru="9-СИНФ · 10-Я НЕДЕЛЯ · УРОК 30" data-en="GRADE 9 · WEEK 10 · LESSON 30">9-SINF · 10-HAFTA · 30-DARS</div>
    <h1 data-ru="Философия Компонентов и UI Архитектура: Reusable Components, Props & State" data-en="Component Philosophy & UI Architecture: Reusable Components, Props & State">Komponentlar Falsafasi va UI Arxitekturasi: Reusable Components, Props & State</h1>
    <p class="lede" data-ru="Переходим от монолитного спагетти-кода к корпоративной компонентной архитектуре: инкапсуляция разметки, однонаправленный поток данных (Props Down) и реактивное состояние (State)." data-en="Evolving beyond monolithic spaghetti DOM into enterprise component architecture: scoped encapsulation, unidirectional data flow (Props Down), and reactive state isolation.">Monolit spaghetti DOM kodidan korporativ komponentli arxitekturaga o'tamiz: shablon, uslub va mantiqni yagona blokda birlashtirish, bir tomonlama ma'lumotlar oqimi (Props Down) va reaktiv holat (State).</p>
    <div class="grid c3" style="margin-top:24px;">
      <div class="card">
        <h3 data-ru="Формат занятия" data-en="Lesson Format">Format va Davomiylik</h3>
        <p data-ru="Спаренный блок: 2 x 40 минут = 80 минут глубокой фронтенд-инженерии" data-en="Double block: 2 x 40 min = 80 min intensive frontend engineering">Juftlik blok: 2 x 40 daqiqa = 80 daqiqalik chuqur frontend arxitekturasi</p>
      </div>
      <div class="card">
        <h3 data-ru="Главная миссия" data-en="Core Mission">Amaliy Missiya</h3>
        <p data-ru="Спроектировать собственную библиотеку Cyber UI компонентов (Badge, Card, Terminal)" data-en="Architect custom Cyber UI component library (Badge, Card, Terminal)">O'z shaxsiy Cyber UI komponentlar kutubxonasini (Badge, Card, Terminal) yaratish</p>
      </div>
      <div class="card">
        <h3 data-ru="10-Балльная система" data-en="10-Point Rubric">Baholash Mezoni</h3>
        <p data-ru="4 балла: Props & Template · 4 балла: Reactive State · 2 балла: CustomEvent" data-en="4 pts: Props & Template · 4 pts: Reactive State · 2 pts: CustomEvent">4 ball: Props & Shablon · 4 ball: State mantiq · 2 ball: CustomEvent</p>
      </div>
    </div>
  </section>""")

    # Slide 2: Mandatory HW Review
    slides.append("""  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00">
    <div class="eyebrow" data-ru="РАЗБОР ДОМАШНЕГО ЗАДАНИЯ · МОСТ К НОВОЙ ТЕМЕ" data-en="HOMEWORK REVIEW · BRIDGE TO NEW TOPIC">UY VAZIFASI TAHLILI VA O'TGAN DARS KO'PRIGI</div>
    <h2 data-ru="29-Урок: Модули ES6 и Мутация Объектов" data-en="Lesson 29 Review: ES6 Modules & Object Mutation">29-Dars Tahlili: ES6 Modullar va Obyektlar Mutatsiyasi</h2>
    <p class="lede" data-ru="На прошлом уроке мы освоили экспорт/импорт модулей и цикл событий Event Loop. Разберём критическую ошибку поверхностного копирования:" data-en="Last lesson we mastered ES modules import/export and the Event Loop queue. Let's inspect a critical reference-mutation pitfall:">29-darsda kodni ES modullarga ajratish va Event Loop mexanizmini o'rgandik. Keng tarqalgan xotira mutatsiyasi xatosini tahlil qilamiz:</p>
    
    <div class="grid c2" style="margin-top:16px;">
      <div class="card" style="border-left:4px solid var(--accent);">
        <span class="pill" style="background:var(--accent-soft); color:var(--accent-ink);" data-ru="Типичная Ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</span>
        <h3 style="margin-top:8px;" data-ru="Мутация по ссылке вместо клонирования" data-en="Reference Mutation instead of Clone">Link Orqali Xotirani Buzish</h3>
        <pre><code style="font-size:12px;">// ❌ XATO: user2 va user1 bitta xotiraga qaraydi!
const user1 = { name: "Ali", role: "Dev" };
const user2 = user1; 
user2.role = "Admin"; // user1.role ham "Admin" bo'lib qoldi!</code></pre>
        <p style="font-size:12.5px; color:var(--ink-2); margin-top:6px;" data-ru="При прямом присваивании копируется лишь ссылка в куче (Heap). Одно изменение ломает состояние всей системы." data-en="Direct assignment copies pointer address in heap. A single mutation cascades into silent state corruption across the UI.">To'g'ridan-to'g'ri tenglash faqat Heap manzilini ko'chiradi. Bitta o'zgarish butun tizim holatini buzadi.</p>
      </div>

      <div class="card" style="border-left:4px solid var(--green);">
        <span class="pill" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой Стандарт (Golden Solution)" data-en="Golden Standard">Oltin Yechim (Immutability)</span>
        <h3 style="margin-top:8px;" data-ru="Spread-клонирование и чистый экспорт" data-en="Spread Cloning & Pure Export">Spread Operator bilan Klonlash</h3>
        <pre><code style="font-size:12px;">// ✅ TOZA STANDART: Mustaqil yangi obyekt!
const user1 = { name: "Ali", role: "Dev" };
const user2 = { ...user1, role: "Admin" };

// user1.role haligacha "Dev"! Safe State update.</code></pre>
        <p style="font-size:12.5px; color:var(--ink-2); margin-top:6px;" data-ru="Оператор spread (...) создает независимую копию. Именно так обновляется State в современных компонентах!" data-en="The spread (...) operator provisions a clean clone. This immutability pattern powers modern component state engines!">Spread (...) mustaqil yangi nusxa oladi. Komponentlar holati (State) aynan shu tarzda xavfsiz yangilanadi!</p>
      </div>
    </div>

    <div class="card" style="margin-top:14px; background:rgba(255,255,255,0.7); display:flex; align-items:center; justify-content:space-between; gap:16px;">
      <div>
        <span class="pill" style="background:#00214a; color:#fff;" data-ru="30-Секундный Блиц" data-en="30-Second Blitz">30 Soniyalik Blitz</span>
        <b style="margin-left:8px;" data-ru="Где выполняются промисы: в Microtask или Macrotask очереди?" data-en="Where do Promise callbacks execute: Microtask or Macrotask queue?">Promise `.then()` va `await` qaysi navbatda bajariladi: Microtask yoki Macrotask?</b>
      </div>
      <div style="font-size:13px; font-weight:700; color:var(--green);" data-ru="Ответ: Microtask (перед перерисовкой экрана!)" data-en="Answer: Microtask (prior to frame repaint!)">Javob: Microtask navbatida!</div>
    </div>
  </section>""")

    # Slide 3: Muammo
    slides.append("""  <!-- SLIDE 3: PROBLEM -->
  <section class="slide" data-phase="Muammo|Проблема|Problem" data-time="12:00–18:00">
    <div class="eyebrow" data-ru="ПРОБЛЕМА · МОНОЛИТНЫЙ АД" data-en="PROBLEM · MONOLITHIC SPAGHETTI">AQLIY HUJUM · REAL MUAMMO</div>
    <h2 data-ru="Почему Копипаста HTML Убивает Большие Веб-Приложения?" data-en="Why Does HTML Copy-Paste Ruin Large Web Applications?">Nega HTML Nusxalash (Copy-Paste) Katta Saytlarni Halokatga Elitadi?</h2>
    <p class="lede" data-ru="Представьте интернет-магазин или дашборд с 50 карточками товаров. Если дизайнер меняет кнопку — вам придется переписать 500 строк в 10 файлах!" data-en="Imagine a dashboard or e-commerce shop with 50 product cards. When design updates a button style, you must manually edit 500 lines across 10 files!">50 ta kartochkasi bor interfeysni tasavvur qiling. Agar dizayner tugma rangini o'zgartirsa, 10 ta sahifadagi 500 qator HTML kodni qo'lda tahrirlashga majbur bo'lasiz!</p>
    
    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <span class="pill" style="background:#fee2e2; color:#b91c1c;" data-ru="1. Дублирование Кода" data-en="1. Code Duplication">1. Kod Takrorlanishi</span>
        <h3 style="margin-top:10px;" data-ru="Copy-Paste Кошмар" data-en="Copy-Paste Chaos">40 Qatorlik Nusxalar</h3>
        <p data-ru="Один и тот же блок разметки размножен по всему проекту. Опечатка в одном месте ломает всю страницу." data-en="Identical HTML blocks copy-pasted across views. A single typo triggers layout breakage.">Bir xil tuzilma qayta-qayta ko'chiriladi. Bitta xato butun sahifa tartibini buzib tashlaydi.</p>
      </div>

      <div class="card">
        <span class="pill" style="background:#fef3c7; color:#b45309;" data-ru="2. Коллизия Стилей" data-en="2. Style Clashes">2. CSS To'qnashuvi</span>
        <h3 style="margin-top:10px;" data-ru="Глобальная Утечка" data-en="Global Scope Bleed">.card va .btn Urushi</h3>
        <p data-ru="Класс .card из профиля внезапно переопределяет карточку товара в каталоге из-за общего файла styles.css." data-en="Class .card declared in profile accidentally overrides catalog product styling due to global CSS leakage.">Profil uchun yozilgan `.card` klassi umumiy styles.css tufayli do'kondagi mahsulot kartasini buzadi.</p>
      </div>

      <div class="card">
        <span class="pill" style="background:#ede9fe; color:#6d28d9;" data-ru="3. Хрупкое Состояние" data-en="3. Fragile State">3. Mo'rt DOM Boshqaruvi</span>
        <h3 style="margin-top:10px;" data-ru="document.getElementById Ад" data-en="getElementById Hell">20 ta getElementById</h3>
        <p data-ru="Чтобы обновить одну цифру, код ищет элементы по всему DOM. Если ID изменился — JavaScript падает с ошибкой null." data-en="Updating one counter demands querying DOM globally. Renaming an ID throws Uncaught TypeError: null.">Bitta raqamni o'zgartirish uchun butun sahifa ID lari titiladi. Bitta ID o'zgarsa — `null` xatoligi beradi.</p>
      </div>
    </div>
  </section>""")

    # Slide 4: Konsept
    slides.append("""  <!-- SLIDE 4: CONCEPT -->
  <section class="slide" data-phase="Konsept|Концепт|Concept" data-time="18:00–24:00">
    <div class="eyebrow" data-ru="ФИЛОСОФИЯ КОМПОНЕНТОВ" data-en="COMPONENT PHILOSOPHY">YANGI PARADIGMA · LEGO MODELI</div>
    <h2 data-ru="Что Такое UI-Компонент: Анатомия из 4 Частей" data-en="What is a UI Component: The 4-Pillar Anatomy">UI Komponent Nima: 4 Qismdan Iborat Mustaqil Lego Bloki</h2>
    <p class="lede" data-ru="Компонент — это самодостаточный программный блок, который объединяет разметку, стили, входные параметры и внутреннюю память:" data-en="A component is an encapsulated software unit marrying markup, styles, input configuration, and state memory:">Komponent — bu tashqi dunyoga bog'liq bo'lmagan, o'zining shabloni, stillari, parametrlari va ichki xotirasiga ega bo'lgan mustaqil dasturiy blok:</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="4 Столпа UI-Компонента" data-en="4 Pillars of a Component">Komponentning 4 Ta Asosi</h3>
        <ul style="margin-left:18px; line-height:1.9; font-size:13.5px; margin-top:10px;">
          <li data-ru="1. Template (Шаблон): Каркас HTML и слоты данных (Placeholder)." data-en="1. Template: HTML skeleton and data placeholders."><b style="color:var(--accent);">1. Template (Shablon):</b> HTML skeleti va ma'lumot joylashuv o'rinlari (Placeholder).</li>
          <li data-ru="2. Props (Свойства): Неизменяемые параметры (Read-only), передаваемые родителем." data-en="2. Props: Immutable configurations (Read-only) delegated from parent."><b style="color:var(--green);">2. Props (Xususiyatlar):</b> Tashqaridan (ota komponentdan) uzatiladigan o'zgarmas sozlamalar (Read-only).</li>
          <li data-ru="3. State (Состояние): Локальная изменяемая память компонента (count: 5, isOpen: true)." data-en="3. State: Encapsulated mutable reactive memory (count: 5, isOpen: true)."><b style="color:#d97706;">3. State (Ichki Holat):</b> Komponentning ichida yashovchi va o'zgaruvchi shaxsiy xotirasi (Masalan: `count: 5`, `isOpen: true`).</li>
          <li data-ru="4. Events (События): Отправка сигнала родителю при действии (CustomEvent)." data-en="4. Events: Dispatched notifications signaling upwards (CustomEvent)."><b style="color:#2563eb;">4. Events (Hodisalar):</b> Tugma bosilganda ota elementga signal jo'natish (`CustomEvent`).</li>
        </ul>
      </div>

      <div class="card" style="background:#0a0e17; color:#f1f5f9; border-color:#1e293b;">
        <span class="pill" style="background:#1e293b; color:#38bdf8;" data-ru="Визуальная Формула" data-en="Visual Formula">Matematik Formula</span>
        <div style="font-family:'JetBrains Mono',monospace; font-size:16px; font-weight:700; color:#38bdf8; margin:16px 0 10px 0;">UI = Component(Props, State)</div>
        <p style="font-size:12.5px; color:#94a3b8; line-height:1.6;" data-ru="Интерфейс больше не пишется вручную! Он вычисляется как чистая функция от переданных свойств (Props) и текущего состояния (State)." data-en="UI is no longer handcrafted imperatively! It is computed reactively as a pure projection of input Props and internal State.">Interfeys endi qo'lda qatorma-qator yozilmaydi! U berilgan <b>Props</b> va joriy <b>State</b> qiymatiga qarab avtomatik generatsiya qilinadi.</p>
        <div style="margin-top:14px; padding:8px 12px; background:rgba(56,189,248,0.1); border-radius:6px; font-size:11.5px; color:#7dd3fc;">
          💡 Lego qoidasi: Har qanday murakkab sayt 10-15 ta kichik komponentdan yig'iladi!
        </div>
      </div>
    </div>
  </section>""")

    # Slide 5: Data Flow Architecture
    slides.append("""  <!-- SLIDE 5: ARCHITECTURE -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="24:00–30:00">
    <div class="eyebrow" data-ru="ПОТОК ДАННЫХ В СИСТЕМЕ" data-en="SYSTEM DATA FLOW">ARXITEKTURA VA ALOQA QOIDALARI</div>
    <h2 data-ru="Однонаправленный Поток: Props Down, Events Up" data-en="Unidirectional Flow: Props Down, Events Up">Bir Tomonlama Oqim: Props Pastga, Events Yuqoriga</h2>
    <p class="lede" data-ru="Главное правило enterprise-архитектуры: родитель передает данные вниз, ребенок сообщает о действиях наверх через события:" data-en="The cardinal law of enterprise frontend: parents delegate data downwards, children communicate upwards via events:">Korporativ dasturlashning oltin qoidasi: ota element parametrlarni pastga uzatadi, farzand esa faqat hodisa (Event) chaqirib xabar beradi:</p>

    <div class="grid c2" style="margin-top:16px;">
      <!-- Diagram Card -->
      <div class="card" style="text-align:center; padding:16px;">
        <svg viewBox="0 0 520 230" style="width:100%; max-height:220px; display:block; margin:0 auto;">
          <!-- Parent Box -->
          <rect x="130" y="10" width="260" height="48" rx="8" fill="var(--surface-2, #f1f5f9)" stroke="var(--ink)" stroke-width="2"/>
          <text x="260" y="38" text-anchor="middle" font-family="'JetBrains Mono',monospace" font-weight="700" font-size="14" fill="var(--ink)" data-ru="App Контейнер (Родитель)" data-en="App Container (Parent)">App Container (Ota)</text>

          <!-- Props Down Arrow -->
          <path d="M 180 60 L 180 140" stroke="var(--green)" stroke-width="3" marker-end="url(#arrowGreen)"/>
          <rect x="90" y="88" width="120" height="24" rx="4" fill="rgba(16,185,129,0.15)"/>
          <text x="150" y="104" text-anchor="middle" font-size="11" font-weight="700" fill="var(--green)" data-ru="Props (Данные Вниз) ↓" data-en="Props (Data Down) ↓">Props (Data Down) ↓</text>

          <!-- Events Up Arrow -->
          <path d="M 340 140 L 340 60" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrowRed)"/>
          <rect x="310" y="88" width="140" height="24" rx="4" fill="var(--accent-soft)"/>
          <text x="380" y="104" text-anchor="middle" font-size="11" font-weight="700" fill="var(--accent-ink)" data-ru="CustomEvent (Вверх) ↑" data-en="CustomEvent (Up) ↑">CustomEvent (Up) ↑</text>

          <!-- Child Component -->
          <rect x="130" y="150" width="260" height="52" rx="8" fill="var(--panel, #ffffff)" stroke="var(--ink)" stroke-width="2"/>
          <text x="260" y="174" text-anchor="middle" font-family="'JetBrains Mono',monospace" font-weight="700" font-size="13" fill="var(--ink)" data-ru="&lt;CyberBadge /&gt;" data-en="&lt;CyberBadge /&gt;">&lt;CyberBadge /&gt;</text>
          <text x="260" y="192" text-anchor="middle" font-size="10.5" fill="var(--ink-2)" data-ru='Props: text="ONLINE", variant="green"' data-en='Props: text="ONLINE", variant="green"'>Props: text="ONLINE", variant="green"</text>

          <!-- Markers -->
          <defs>
            <marker id="arrowGreen" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 8 5 L 0 9 z" fill="var(--green)"/>
            </marker>
            <marker id="arrowRed" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1 L 8 5 L 0 9 z" fill="var(--accent)"/>
            </marker>
          </defs>
        </svg>
      </div>

      <!-- Principles Card -->
      <div class="card">
        <h3 data-ru="3 Железных Закона Компонента" data-en="3 Iron Laws of Components">3 Ta Temir Qoida</h3>
        <ol style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="Props неизменяемы: Ребенок никогда не переписывает props.text = '...' напрямую!" data-en="Props are immutable: Child components never write props.text = '...' directly!"><b>Props O'zgarmasdir:</b> Farzand komponent hech qachon o'ziga berilgan propsni o'zgartirmaydi!</li>
          <li data-ru="State локален: Внутреннее состояние принадлежит только этому компоненту." data-en="State is strictly local: Internal reactive variables belong only to that instance."><b>State Shaxiydir:</b> Komponent xotirasi boshqa elementlardan yopiq saqlanadi.</li>
          <li data-ru="События всплывают: Ребенок кричит наружу через new CustomEvent('delete', { detail })." data-en="Events bubble upwards: Child notifies parent via new CustomEvent('delete', { detail })."><b>Hodisalar Chaqiriladi:</b> Farzand o'zgarish haqida <code>CustomEvent</code> orqali xabar beradi.</li>
        </ol>
      </div>
    </div>
  </section>""")

    # Slide 6: Code Patterns
    slides.append("""  <!-- SLIDE 6: CODE PATTERNS -->
  <section class="slide" data-phase="Kod Mexanizmi|Паттерны Кода|Code Patterns" data-time="30:00–35:00">
    <div class="eyebrow" data-ru="ПРАКТИЧЕСКИЙ РЕАЛИЗАЦИЯ" data-en="IMPLEMENTATION PATTERNS">IKKI XIL USUL: FACTORY VS WEB COMPONENTS</div>
    <h2 data-ru="Как Создать Компонент на Чистом JavaScript" data-en="How to Author Components in Vanilla JavaScript">Vanilla JavaScriptda Komponent Yaratishning 2 Ta Usuli</h2>
    <p class="lede" data-ru="Вам не нужен React или Angular, чтобы писать компонентный код! Современный браузер поддерживает нативные Web Components:" data-en="You don't need heavy frameworks like React to build modular UIs. Modern browsers natively support Web Components:">Modulli interfeys qurish uchun React yoki boshqa og'ir kutubxonalar shart emas. Brauzerning o'zida 2 ta toza usul mavjud:</p>

    <div class="grid c2" style="margin-top:14px;">
      <!-- Pattern 1: Factory -->
      <div class="card">
        <span class="pill" style="background:#e0f2fe; color:#0369a1;" data-ru="1. Паттерн Фабричной Функции" data-en="1. Factory Function Pattern">1. Factory Function Pattern</span>
        <pre><code style="font-size:11.5px;">export function createBadge(props) {
  const el = document.createElement("span");
  el.className = `badge badge-${props.variant}`;
  el.textContent = props.text;
  
  el.onclick = () => {
    el.dispatchEvent(new CustomEvent("badge-click", {
      bubbles: true,
      detail: { text: props.text }
    }));
  };
  return el;
}</code></pre>
        <p style="font-size:11.5px; color:var(--ink-2); margin-top:6px;" data-ru="Простой, легкий и быстрый подход. Создает и возвращает DOM элемент." data-en="Lightweight, pure, and fast. Constructs and returns a configured DOM node.">Oddiy, yengil va tezkor. DOM elementini yasab qaytaradi.</p>
      </div>

      <!-- Pattern 2: Web Component Custom Element -->
      <div class="card">
        <span class="pill" style="background:#fef3c7; color:#b45309;" data-ru="2. Нативный Web Component (Стандарт W3C)" data-en="2. Native Web Component (W3C Standard)">2. Native Web Component (W3C Standart)</span>
        <pre><code style="font-size:11.5px;">class CyberBadge extends HTMLElement {
  connectedCallback() {
    const text = this.getAttribute("text") || "BADGE";
    const variant = this.getAttribute("variant") || "info";
    this.innerHTML = `
      &lt;span class="badge ${variant}"&gt;${text}&lt;/span&gt;
    `;
  }
}
customElements.define("cyber-badge", CyberBadge);
// HTMLda ishlatish: &lt;cyber-badge text="ONLINE" variant="green"&gt;&lt;/cyber-badge&gt;</code></pre>
        <p style="font-size:11.5px; color:var(--ink-2); margin-top:6px;" data-ru="Встраивается в браузер как настоящий HTML-тег. Используется прямо в разметке!" data-en="Natively registered in the browser engine. Can be directly authored in raw HTML!">HTML teglari kabi brauzerga o'rnatiladi. HTML fayl ichida bevosita ochiladi!</p>
      </div>
    </div>
  </section>""")

    # Slide 7: State & Re-rendering
    slides.append("""  <!-- SLIDE 7: STATE MANAGEMENT -->
  <section class="slide" data-phase="Holat Boshqaruvi|Управление Состоянием|State Management" data-time="35:00–40:00">
    <div class="eyebrow" data-ru="ДИНАМИЧЕСКИЙ РЕНДЕРИНГ" data-en="DYNAMIC RE-RENDERING">HOLAT BOSHQARUVI VA REAKTIV RE-RENDER</div>
    <h2 data-ru="Как Компонент Перерисовывается: Механика setState" data-en="How Components Re-render: The setState Engine">Komponent Qanday Yangilanadi: setState Mexanikasi</h2>
    <p class="lede" data-ru="Когда данные внутри меняются, компонент не перегружает страницу целиком, а точечно обновляет свой внутренний HTML:" data-en="When internal data updates, the component avoids a full-page reload, surgically refreshing only its owned DOM subtree:">Ichki ma'lumotlar o'zgarganda sahifa butunlay qayta yuklanmaydi, faqat ushbu komponentning o'zi avtomatik yangilanadi (Targeted Re-render):</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Алгоритм Реактивного Обновления" data-en="Reactive State Cycle">Holat Tsikli Qadamlari</h3>
        <ol style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="Событие: Пользователь нажимает кнопку (Click)." data-en="Event: User clicks an interactive trigger (Click)."><b>Hodisa sodir bo'ladi:</b> Foydalanuvchi tugmani bosadi (Click).</li>
          <li data-ru="Вызов setState: this.setState({ count: this.state.count + 1 })." data-en="Invoke setState: this.setState({ count: this.state.count + 1 })."><b>setState chaqiriladi:</b> <code>this.setState({ count: this.state.count + 1 })</code>.</li>
          <li data-ru="Клонирование: Старая память не мутируется, создается новый объект состояния." data-en="Immutability: Old state is untouched, fresh immutable snapshot written."><b>Nusxa olinadi:</b> Eski xotira mutatsiya qilinmaydi, yangi holat yoziladi.</li>
          <li data-ru="Точечный рендер: Только шаблон этого компонента перерисовывается с новыми данными." data-en="Targeted render: Only this component's template refreshes with new payload."><b>Targeted render:</b> Faqat komponent shabloni yangi qiymat bilan qayta chiziladi.</li>
        </ol>
        <div style="margin-top:12px; font-size:12px; color:var(--green); font-weight:700;">
          ✓ Natija: Qolgan 99 ta komponent o'z joyida qoladi, xotira va protsessor tejaladi!
        </div>
      </div>

      <div class="card">
        <span class="pill" style="background:#fee2e2; color:#b91c1c;" data-ru="Анти-паттерн" data-en="Anti-pattern">Mutlaqo Taqiqlanadi</span>
        <pre><code style="font-size:11.5px;">// ❌ XATO: DOMni qo'lda o'zgartirish!
button.onclick = () => {
  document.getElementById("cnt").innerText = 10;
};

// ✅ TO'G'RI: State orqali boshqarish!
button.onclick = () => {
  counter.setState({ value: counter.state.value + 1 });
};</code></pre>
        <p style="font-size:12px; color:var(--ink-2); margin-top:6px;" data-ru="Компоненты никогда не должны трогать чужой DOM! Источник правды (Single Source of Truth) — только State." data-en="Components must never reach into foreign DOM trees. The single source of truth is always the State.">Komponentlar hech qachon begona ID larni tahrirlamaydi! Yagona haqiqat manbasi (Single Source of Truth) — faqat State bo'lishi shart.</p>
      </div>
    </div>
  </section>""")

    # Slide 8: In-Deck Interactive Simulator
    slides.append("""  <!-- SLIDE 8: IN-DECK INTERACTIVE SIMULATOR -->
  <section class="slide" data-phase="Jonli Sinov|Интерактив|Live Demo" data-time="40:00–48:00">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНЫЙ ТРЕНАЖЕР НА ЭКРАНЕ" data-en="INTERACTIVE SMARTBOARD LAB">JONLI KOMPONENT SIMULYATORI</div>
    <h2 data-ru="Лаборатория Props и State на Экране" data-en="In-Deck Props & State Interactive Studio">Smartboardda Props va State Jonli Tajribasi</h2>
    <p class="lede" data-ru="Управляйте свойствами и состоянием компонента MetricCard прямо в презентации:" data-en="Test live Props and State reactivity inside this presentation component runner:">MetricCard komponentining Props parametrlarini va ichki State xotirasini jonli sinab ko'ring:</p>

    <div class="grid c2" style="margin-top:14px; align-items:flex-start;">
      <!-- Interactive Component Render Box -->
      <div class="card" style="padding:18px; text-align:center;">
        <span class="pill" style="background:var(--accent-soft); color:var(--accent-ink);" data-ru="Живой UI Компонент" data-en="Live UI Component">Jonli UI Komponent</span>
        
        <div id="deckDemoBox" style="margin-top:16px; padding:20px; background:#0b1120; border:2px solid #38bdf8; border-radius:12px; color:#fff; text-align:left; box-shadow:0 10px 25px rgba(0,0,0,0.4);">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span id="demoCardLabel" style="font-size:11px; font-family:'JetBrains Mono',monospace; color:#94a3b8; text-transform:uppercase;">API LATENCY</span>
            <span id="demoBadge" style="font-size:10px; font-weight:700; padding:2px 8px; border-radius:4px; background:rgba(16,185,129,0.2); color:#34d399;">ONLINE</span>
          </div>
          <div id="demoCardValue" style="font-size:32px; font-weight:800; font-family:'JetBrains Mono',monospace; color:#38bdf8; margin:10px 0 4px 0;">24 ms</div>
          <div style="font-size:11.5px; color:#94a3b8; display:flex; justify-content:space-between;">
            <span>Requests: <b id="demoReqCount" style="color:#f1f5f9;">1,420</b></span>
            <span style="color:#34d399;">▲ 99.9% Uptime</span>
          </div>
        </div>

        <div style="margin-top:12px; display:flex; justify-content:center; gap:8px;">
          <button class="btn" onclick="sendDemoSignal()" style="background:var(--accent); color:#fff; border-color:var(--accent);" data-ru="⚡ Отправить запрос (+1)" data-en="⚡ Dispatch Request (+1)">⚡ So'rov Yuborish (+1)</button>
          <button class="btn" onclick="resetDemoSignal()" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta o'rnatish</button>
        </div>
      </div>

      <!-- Controls & Inspector -->
      <div class="card">
        <h3 data-ru="Инспектор Props & State" data-en="Props & State Inspector">Props va State Telemetriyasi</h3>
        <div style="margin-top:10px; display:flex; flex-direction:column; gap:8px;">
          <div>
            <label style="font-size:12px; color:var(--ink-2); display:block; margin-bottom:4px;" data-ru="Изменить Props (Label):" data-en="Modify Props (Label):">Props (Nomi):</label>
            <div style="display:flex; gap:6px;">
              <button class="btn" onclick="setDemoProps('API LATENCY', '24 ms')" style="font-size:11px; padding:4px 8px;" data-ru="API Задержка" data-en="API Latency">API Latency</button>
              <button class="btn" onclick="setDemoProps('CPU LOAD', '48%')" style="font-size:11px; padding:4px 8px;" data-ru="Нагрузка CPU" data-en="CPU Load">CPU Load</button>
              <button class="btn" onclick="setDemoProps('MEMORY USAGE', '512 MB')" style="font-size:11px; padding:4px 8px;" data-ru="ОЗУ Память" data-en="RAM Usage">RAM Usage</button>
            </div>
          </div>

          <div>
            <label style="font-size:12px; color:var(--ink-2); display:block; margin-bottom:4px;" data-ru="Изменить Props (Статус):" data-en="Modify Props (Status):">Props (Holat Badge):</label>
            <div style="display:flex; gap:6px;">
              <button class="btn" onclick="setDemoBadge('ONLINE', '#34d399', 'rgba(16,185,129,0.2)')" style="font-size:11px; padding:4px 8px; color:#10b981;" data-ru="В сети" data-en="Online">Online</button>
              <button class="btn" onclick="setDemoBadge('WARNING', '#fbbf24', 'rgba(245,158,11,0.2)')" style="font-size:11px; padding:4px 8px; color:#d97706;" data-ru="Внимание" data-en="Warning">Warning</button>
              <button class="btn" onclick="setDemoBadge('CRITICAL', '#f87171', 'rgba(239,68,68,0.2)')" style="font-size:11px; padding:4px 8px; color:#ef4444;" data-ru="Критический" data-en="Critical">Critical</button>
            </div>
          </div>

          <div style="margin-top:6px; font-family:'JetBrains Mono',monospace; font-size:11.5px; background:rgba(0,0,0,0.25); padding:10px; border-radius:6px; line-height:1.6;">
            <div>State.requests = <span id="telReqCount" style="color:var(--accent); font-weight:700;">1420</span>;</div>
            <div>Component.render() count = <span id="telRenderCount" style="color:var(--green); font-weight:700;">1</span>;</div>
          </div>
        </div>
      </div>
    </div>
  </section>""")

    # Slide 9: Interactive Quiz
    slides.append("""  <!-- SLIDE 9: QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Interactive Quiz" data-time="48:00–54:00">
    <div class="eyebrow" data-ru="ПРОВЕРКА ЗНАНИЙ (3 ВОПРОСА)" data-en="KNOWLEDGE CHECK (3 QUESTIONS)">INTERAKTIV QUIZ</div>
    <h2 data-ru="Блиц-Тест: Архитектура Компонентов" data-en="Fast Quiz: Component Architecture">Bilimni Sinash: Komponentlar va Props/State</h2>
    <div class="grid c3" style="margin-top:16px;">
      <!-- Q1 -->
      <div class="card quiz-card">
        <span class="pill" data-ru="Вопрос 1" data-en="Question 1">1-Savol</span>
        <h4 style="margin:10px 0;" data-ru="В чем главное отличие Props от State?" data-en="What is the core difference between Props and State?">Props bilan State o'rtasidagi asosiy farq nima?</h4>
        <div style="display:flex; flex-direction:column; gap:6px; margin-top:8px;">
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="A) Оба они неизменяемы" data-en="A) Both are immutable">A) Ikkalasi ham o'zgarmasdir</button>
          <button class="btn" onclick="checkDeckQuiz(this, true)" style="text-align:left; font-size:11.5px;" data-ru="B) Props приходят извне (read-only), State — внутренняя память" data-en="B) Props come from outside (read-only), State is internal">B) Props tashqaridan keladi (read-only), State ichki xotira</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="C) Props хранят только цифры" data-en="C) Props only store numbers">C) Props faqat raqam saqlaydi</button>
        </div>
      </div>

      <!-- Q2 -->
      <div class="card quiz-card">
        <span class="pill" data-ru="Вопрос 2" data-en="Question 2">2-Savol</span>
        <h4 style="margin:10px 0;" data-ru="Как ребенок должен передать сигнал родителю?" data-en="How should a child component send data to parent?">Farzand komponent ota komponentga qanday xabar beradi?</h4>
        <div style="display:flex; flex-direction:column; gap:6px; margin-top:8px;">
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="A) Напрямую меняет parent.state" data-en="A) Mutates parent.state directly">A) parent.state ni to'g'ridan-to'g'ri o'zgartiradi</button>
          <button class="btn" onclick="checkDeckQuiz(this, true)" style="text-align:left; font-size:11.5px;" data-ru="B) Вызывает CustomEvent (Events Up)" data-en="B) Dispatches CustomEvent (Events Up)">B) CustomEvent dispatch qiladi (Events Up)</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="C) Перезагружает всю страницу" data-en="C) Reloads the entire window">C) Barcha oynani reload qiladi</button>
        </div>
      </div>

      <!-- Q3 -->
      <div class="card quiz-card">
        <span class="pill" data-ru="Вопрос 3" data-en="Question 3">3-Savol</span>
        <h4 style="margin:10px 0;" data-ru="Почему нельзя мутировать State напрямую?" data-en="Why must you avoid mutating state directly?">Nega State to'g'ridan-to'g'ri mutatsiya qilinmaydi (`state.val++`)?</h4>
        <div style="display:flex; flex-direction:column; gap:6px; margin-top:8px;">
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="A) JavaScript запрещает это" data-en="A) JavaScript forbids it">A) JavaScript buni ruxsat bermaydi</button>
          <button class="btn" onclick="checkDeckQuiz(this, true)" style="text-align:left; font-size:11.5px;" data-ru="B) Re-render не вызовется и интерфейс устареет" data-en="B) Re-render will not trigger and UI goes stale">B) Re-render chaqirilmaydi va UI eskirib qoladi</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="C) Отключится интернет" data-en="C) Internet will disconnect">C) Internet o'chib qoladi</button>
        </div>
      </div>
    </div>
  </section>""")

    # Slide 10: 25-Min Practice Cyber Arena
    slides.append("""  <!-- SLIDE 10: ARENA LAB -->
  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="54:00–69:00">
    <div class="eyebrow" data-ru="БОЛЬШАЯ ПРАКТИЧЕСКАЯ АРЕНА (25 МИНУТ)" data-en="25-MINUTE CYBER ARENA">AMALIY ARENA</div>
    <h2 data-ru="Задание: Собери Библиотеку Cyber UI Компонентов" data-en="Mission: Construct Cyber UI Component Library">Kiber-Missiya: Shaxsiy Cyber UI Kutubxonasini Yaratish</h2>
    <p class="lede" data-ru="Откройте студию studio/index.html и выполните 3 инженерных шага за 25 минут:" data-en="Launch studio/index.html and accomplish 3 engineering milestones within 25 minutes:">Kompyuteringizda <b>studio/index.html</b> faylini oching va 25 daqiqada 3 ta mustaqil komponentni yarating:</p>
    
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Чек-лист Разработчика" data-en="Developer Checklist">Muhandislik Bosqichlari</h3>
        <ol style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="Создать компонент &lt;cyber-badge&gt; с динамическим props variant (green, amber, red)" data-en="Create &lt;cyber-badge&gt; with dynamic variant props (green, amber, red)">Dinamik `variant` (green, amber, red) propsga ega bo'lgan <code>&lt;cyber-badge&gt;</code> komponentini yaratish</li>
          <li data-ru="Собрать карточку метрики &lt;metric-card&gt; с внутренним счетчиком кликов" data-en="Build stateful &lt;metric-card&gt; with internal state and click counter">O'zining ichki State xotirasiga ega bo'lgan <code>&lt;metric-card&gt;</code> komponentini qurish</li>
          <li data-ru="Реализовать диспетчер CustomEvent для отправки логов в терминал дашборда" data-en="Implement CustomEvent dispatcher streaming action logs into dashboard terminal">Tugma bosilganda ota konteynerga ma'lumot uzatuvchi <code>CustomEvent</code> mexanizmini ulash!</li>
        </ol>
        <div style="margin-top:16px;">
          <a href="studio/index.html" target="_blank" class="btn" style="text-decoration:none; display:inline-flex; align-items:center; gap:8px; font-size:13px; font-weight:700; padding:10px 18px; background:var(--accent); color:#fff; border-color:var(--accent);" data-ru="🚀 Открыть Студию Компонентов (studio/index.html)" data-en="🚀 Launch Component Studio (studio/index.html)">🚀 Studiyani Ochish (studio/index.html)</a>
        </div>
      </div>

      <!-- Live 25-Min Timer Card -->
      <div class="card" style="text-align:center; padding:16px;">
        <span class="pill" data-ru="Таймер Лаборатории" data-en="Arena Timer">Arena Taymeri</span>
        <div id="deckTimerDisplay" style="font-family:'JetBrains Mono',monospace; font-size:44px; font-weight:800; color:var(--accent); margin:12px 0;">25:00</div>
        <div style="display:flex; justify-content:center; gap:8px;">
          <button class="btn" id="deckTimerBtn" onclick="toggleDeckTimer()" data-ru="▶ Старт (25 мин)" data-en="▶ Start (25m)">▶ Boshlash (25m)</button>
          <button class="btn" onclick="resetDeckTimer()" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta o'rnatish</button>
        </div>
        <div style="font-size:12px; color:var(--ink-2); margin-top:10px;" data-ru="Учитель проходит по рядам и помогает настроить props и events" data-en="Teacher navigates floor assisting component scoping and event bubbles">O'qituvchi o'quvchilarga props uzatish va hodisalarni bog'lashda yordam beradi</div>
      </div>
    </div>
  </section>""")

    # Slide 11: Peer Review
    slides.append("""  <!-- SLIDE 11: PEER REVIEW -->
  <section class="slide" data-phase="Kiber-Audit|Код-Ревью|Peer Review" data-time="69:00–74:00">
    <div class="eyebrow" data-ru="ПАРНЫЙ КОНТРОЛЬ КАЧЕСТВА" data-en="PAIR QUALITY CONTROL">JUFTLIKDA PEER-REVIEW (KIBER-AUDIT)</div>
    <h2 data-ru="Обменяйтесь Экранами: Чек-лист из 4 Пунктов" data-en="Swap Screens: 4-Point Component Checklist">Partadosh Bilan Almashing: 4 Bosqichli Kod Auditi</h2>
    <p class="lede" data-ru="Инженерное правило: код не считается готовым, пока его не проверил напарник. Проверьте компоненты соседа:" data-en="Engineering standard: code is never production-ready until reviewed by a peer. Inspect your neighbor's components:">Professional muhandislik qoidasi: sherigingiz tekshirmaguncha kod tayyor hisoblanmaydi. Partadoshingiz kodini sinang:</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Чек-лист Инспекции" data-en="Inspection Checklist">Tekshirish Mezonlari</h3>
        <ul style="margin-left:18px; line-height:2.0; font-size:13px; margin-top:8px;">
          <li data-ru="[ ] Props не мутируются: Никаких props.text = '...' внутри метода!" data-en="[ ] Props immutability: Zero direct props.text = '...' writes inside child!">[ ] <b>Props Butunligi:</b> Farzand ichida props o'zgartirilmaganmi?</li>
          <li data-ru="[ ] Изоляция стилей: Классы внутри компонента не ломают общий экран." data-en="[ ] Scoped styles: Component classes do not corrupt outer layouts.">[ ] <b>Stillar Izolyatsiyasi:</b> Komponent klasslari boshqa elementlarni buzmayaptimi?</li>
          <li data-ru="[ ] CustomEvent с деталями: Событие передает detail: { id, value }." data-en="[ ] CustomEvent details: Emits structured detail: { id, value } payload.">[ ] <b>CustomEvent:</b> Hodisada `detail` obyekti to'g'ri shakllantirilganmi?</li>
          <li data-ru="[ ] Чистый рендер: При нажатии на кнопку перерисовывается только этот блок." data-en="[ ] Targeted render: Clicking buttons only re-renders the targeted card.">[ ] <b>Toza Re-render:</b> Tugma bosilganda faqat bitta kartochka yangilanyaptimi?</li>
        </ul>
      </div>

      <div class="card" style="display:flex; flex-direction:column; justify-content:center; text-align:center;">
        <div style="font-size:36px; margin-bottom:8px;">🔍🤝💻</div>
        <h3 data-ru="Роль: Lead Frontend Architect" data-en="Role: Lead Frontend Architect">Siz Bosh Arxitektorsiz!</h3>
        <p style="font-size:12.5px; color:var(--ink-2); margin-top:6px;" data-ru="Если нашли ошибку прямой мутации — помогите товарищу переписать на правильный spread {...state}!" data-en="If you spot direct state mutation — guide your teammate to refactor with safe spread {...state}!">Agar sherigingiz kodida to'g'ridan-to'g'ri mutatsiyani ko'rsangiz — unga toza `...state` spread usulini qo'llashni o'rgating!</p>
      </div>
    </div>
  </section>""")

    # Slide 12: Showcase Demo
    slides.append("""  <!-- SLIDE 12: SHOWCASE DEMO -->
  <section class="slide" data-phase="Taqdimot|Демонстрация|Showcase Arena" data-time="74:00–77:00">
    <div class="eyebrow" data-ru="ДЕМОНСТРАЦИЯ КОМПОНЕНТОВ НА ДОСКЕ" data-en="SMARTBOARD COMPONENT SHOWCASE">O'QUVCHILAR DEMOSI</div>
    <h2 data-ru="Презентация Разработанных Компонентов" data-en="Student Component Showcase">Kiber-Showcase: Katta Ekranda Komponentlar Demusi</h2>
    <p class="lede" data-ru="2 лучшие пары разработчиков подключаются к экрану и демонстрируют реактивность своей библиотеки:" data-en="Top 2 student pairs take the smartboard to showcase their reactive component library live:">Eng tezkor 2 ta juftlik o'zlarining yangi yaratgan komponentlarini sinf oldida namoyish etadi:</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card" style="text-align:center; padding:20px;">
        <span class="pill" style="background:var(--accent-soft); color:var(--accent-ink);" data-ru="Демо 1" data-en="Demo 1">Demo 1</span>
        <h3 style="margin-top:10px;" data-ru="Интерактивный MetricCard" data-en="Interactive MetricCard">Interaktiv MetricCard</h3>
        <p style="font-size:12.5px; color:var(--ink-2);" data-ru="Показ мгновенного обновления цвета и значения при смене Props." data-en="Demonstrate instant color and metric refreshes when props mutate.">Props o'zgarganda kartochka rangi va qiymati bir zumda qanday yangilanishini ko'rsatish.</p>
      </div>
      <div class="card" style="text-align:center; padding:20px;">
        <span class="pill" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Демо 2" data-en="Demo 2">Demo 2</span>
        <h3 style="margin-top:10px;" data-ru="Ловушка Событий (Event Bus)" data-en="Event Bus Dispatcher">Hodisalar Qopqoni (Event Bus)</h3>
        <p style="font-size:12.5px; color:var(--ink-2);" data-ru="Демонстрация вызова CustomEvent из ребенка и перехват в родительском терминале." data-en="Demonstrate CustomEvent bubbling from child and real-time capture in parent terminal.">Farzand komponentdan chiqqan CustomEvent ota terminalda real vaqtda qayd etilishini namoyish etish.</p>
      </div>
    </div>
  </section>""")

    # Slide 13: 3-Tier Homework
    slides.append("""  <!-- SLIDE 13: HOMEWORK -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Tiered Homework" data-time="77:00–79:00">
    <div class="eyebrow" data-ru="ДОМАШНЕЕ ЗАДАНИЕ (10 БАЛЛОВ)" data-en="HOMEWORK ASSIGNMENT (10 POINTS)">MUSTAQIL AMALIYOT</div>
    <h2 data-ru="3 Уровня Домашнего Задания" data-en="3-Tiered Homework Assignment">10 Ballik Mezonli 3 Darajali Uy Vazifasi</h2>
    <p class="lede" data-ru="Задание выполняется в интерактивном приложении vazifa.html с автосохранением в браузере:" data-en="Complete your tasks inside the standalone vazifa.html app featuring local autosave:">Vazifa <b>vazifa.html</b> ilovasida bajariladi va brauzer xotirasida (LocalStorage) avtomatik saqlanadi:</p>

    <div class="grid c3" style="margin-top:20px;">
      <div class="card" style="border-top:3px solid var(--ink);">
        <span class="pill" data-ru="1-Уровень: База" data-en="Tier 1: Base">1-Bosqich: Baza</span>
        <div style="font-size:18px; font-weight:800; color:var(--accent); margin:6px 0;">4 BALL</div>
        <h3 data-ru="Два Чистых Компонента" data-en="Two Pure Components">Ikkita Toza Komponent</h3>
        <p data-ru="Написать &lt;status-badge&gt; и &lt;cyber-button&gt; с поддержкой props (variant, text)." data-en="Author &lt;status-badge&gt; and &lt;cyber-button&gt; components driven by props (variant, text).">Props qabul qiluvchi ikkita mustaqil vizual komponent shablonini yozish.</p>
      </div>

      <div class="card" style="border-top:3px solid var(--accent);">
        <span class="pill" data-ru="2-Уровень: Проект" data-en="Tier 2: Engineering">2-Bosqich: Muhandislik</span>
        <div style="font-size:18px; font-weight:800; color:var(--accent); margin:6px 0;">4 BALL</div>
        <h3 data-ru="State и CustomEvent" data-en="State & CustomEvent">Holatli Hisoblagich</h3>
        <p data-ru="Создать счетчик со своим состоянием count и отправкой CustomEvent наверх при изменении." data-en="Build stateful counter component emitting CustomEvent upwards upon each increment.">O'zining ichki State xotirasi bo'lgan va o'zgarganda CustomEvent chiqaruvchi hisoblagich yaratish.</p>
      </div>

      <div class="card" style="border-top:3px solid var(--green);">
        <span class="pill" data-ru="3-Уровень: Вызов" data-en="Tier 3: Challenge">3-Bosqich: Kiber-Sinov</span>
        <div style="font-size:18px; font-weight:800; color:var(--green); margin:6px 0;">2 BALL</div>
        <h3 data-ru="Native Web Component" data-en="Native Web Component">W3C Web Component</h3>
        <p data-ru="Реализовать customElements.define с реактивным observedAttributes для авто-обновления." data-en="Implement customElements.define with observedAttributes for reactive DOM updates.">Brauzer HTML atributi o'zgarganda avtomatik yangilanuvchi rasmiy Web Component yaratish.</p>
      </div>
    </div>
  </section>""")

    # Slide 14: Summary & Bridge
    slides.append("""  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00">
    <div class="eyebrow" data-ru="ИТОГИ УРОКА И АНОНС 11 НЕДЕЛИ" data-en="LESSON SUMMARY & WEEK 11 TEASER">DARS XULOSASI VA KELGUSI QADAM</div>
    <h2 data-ru="Компоненты — Фундамент Современного Веба" data-en="Components: The Bedrock of Modern Web">Komponentlar — Zamonaviy Vebning Asosi</h2>
    <p class="lede" data-ru="Сегодня мы научились мыслить модульными блоками: шаблоны изолированы, свойства идут сверху вниз, события всплывают вверх!" data-en="Today we adopted component-driven thinking: encapsulated markup, unidirectional props, and event bubbles!">Bugun biz mustaqil bloklarda fikrlashni o'rgandik: shablonlar izolyatsiyalangan, ma'lumotlar oqimi toza, hodisalar xavfsiz boshqariladi!</p>

    <div class="grid c2" style="margin-top:20px;">
      <div class="card">
        <h3 data-ru="Что мы освоили сегодня" data-en="Today's Milestones">Bugungi Yutuqlarimiz</h3>
        <ul style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="Освоили фундаментальную разницу между Props (read-only) и State (реактивная память)." data-en="Mastered the architectural divide between Props (read-only) and State (reactive memory).">Props (read-only) va State (ichki reaktiv xotira) farqini o'rgandik.</li>
          <li data-ru="Закрепили защиту от мутаций с помощью spread-оператора {...state}." data-en="Reinforced immutability guarantees through spread operator {...state} cloning.">Spread operatori bilan xotirani buzmasdan xavfsiz klonlash qoidasini mustahkamladik.</li>
          <li data-ru="Построили архитектуру взаимодействия 'Props вниз, CustomEvent вверх'." data-en="Architected component communication pipeline: 'Props Down, CustomEvents Up'.">CustomEvent orqali farzanddan otaga xabar jo'natuvchi arxitekturani qurdik.</li>
        </ul>
      </div>

      <div class="card" style="background:#00214a; color:#fff;">
        <span class="pill" style="background:var(--accent); color:#fff;" data-ru="Анонс 11 Недели" data-en="Week 11 Preview">Keyingi 11-Haftada</span>
        <h3 style="color:#fff; margin-top:8px;" data-ru="SPA (Single Page Application) и Роутинг" data-en="SPA & Client-Side Routing">SPA va Client-Side Routing</h3>
        <p style="font-size:12.5px; color:#cbd5e1; margin-top:6px;" data-ru="Мы объединим эти компоненты в полноценное SPA-приложение, меняющее экраны без единой перезагрузки страницы!" data-en="We will weave these components into a seamless Single Page Application switching views with zero page reloads!">Biz yaratgan ushbu komponentlarni sahifa bir marta ham yangilanmasdan o'zgaruvchi to'liq <b>SPA (Single Page Application)</b> tizimiga birlashtiramiz!</p>
      </div>
    </div>
  </section>""")

    # Inject slides into presentation
    all_slides_html = "\n\n".join(slides)
    tpl = re.sub(r'<div class="stage">[\s\S]*?</div><!-- /stage -->', f'<div class="stage">\n{all_slides_html}\n</div><!-- /stage -->', tpl)

    # Teacher notes
    notes = {
        "uz": [
            ["Darsga Kirish", "9-sinflar bilan 2-chorakning 30-darsiga xush kelibsiz. Komponentli arxitektura sababini e'lon qiling.", "Doskaga Lego g'ishtchasini misol qilib keltiring."],
            ["Uy Vazifasi Tahlili", "29-darsdagi link orqali xotirani mutatsiya qilish xatosini ko'rsating. Spread operatorini eslating.", "30 soniyalik blits savolni bering."],
            ["Muammo: Spaghetti Monolit", "Nega 3000 qatorli bitta fayl yoki HTMLni 10 marta nusxalash halokat ekanini tushuntiring.", "Katta korporatsiyalar (Google, Meta) qanday ishlashini ayting."],
            ["Komponent Konsepti", "Shablon + Stillar + Props + State formulasi qanday ishlashini doskada chizing.", "UI = f(Props, State) matematikasini tushuntiring."],
            ["Props Down, Events Up", "Bir tomonlama ma'lumotlar oqimini tushuntiring: bola ota xotirasiga to'g'ridan-to'g'ri tegmaydi.", "CustomEvent mexanizmini ko'rsating."],
            ["Factory vs Web Components", "createBadge factory funksiyasi va rasmiy customElements.define klassini solishtiring.", "Brauzer ichki imkoniyatlarini tushuntiring."],
            ["State va Targeted Re-render", "setState qanday qilib faqat kerakli kartani yangilashini, butun sahifa qotmasligini ko'rsating.", "Immutability qoidasini ta'kidlang."],
            ["Jonli Simulyator", "Ekranda MetricCard komponentining Props va State xotirasini bosib ko'rsating.", "O'quvchilarni ekranga chaqiring."],
            ["Interaktiv Kiber-Quiz", "3 ta savol bo'yicha blits o'tkazing va to'g'ri javoblarni ekranda belgilang.", "Natijalarni mustahkamlang."],
            ["25 Minutlik Kiber-Arena", "O'quvchilar studio/index.html da kod yozadilar. 25 daqiqalik taymerni yoqing.", "Sinf bo'ylab aylanib har bir juftlikka yordam bering."],
            ["Juftlikda Peer-Review", "O'quvchilar partadoshining kodini 4 ta qoida bo'yicha tekshiradilar.", "Xatolarni birgalikda tuzatishni nazorat qiling."],
            ["O'quvchilar Demosi", "2 ta juftlik doskaga chiqib o'z komponentlar kutubxonasini ko'rsatadi.", "Yaxshi yechimlarni olqishlang."],
            ["3 Darajali Uy Vazifasi", "vazifa.html ilovasidagi 10 ballik mezonni tushuntiring. Local auto-save borligini eslating.", "O'quvchilarga vazifa formatini tushuntiring."],
            ["Dars Xulosasi", "11-haftadagi SPA (Single Page Application) va Client-Side Routing mavzusini anons qiling.", "Faol o'quvchilarni baholang."]
        ],
        "ru": [
            ["Введение в Урок", "Приветствие 9-го класса на 30-м уроке 2-й четверти. Анонсируйте компонентную архитектуру.", "Приведите пример кубиков Lego."],
            ["Разбор ДЗ", "Покажите ошибку мутации по ссылке из 29-го урока. Напомните про оператор spread.", "Задайте 30-секундный блиц-вопрос."],
            ["Проблема Монолита", "Почему файл на 3000 строк или копирование HTML 10 раз ведет к катастрофе.", "Расскажите, как строят UI в Google и Meta."],
            ["Концепт Компонента", "Нарисуйте формулу Шаблон + Стили + Props + State на доске.", "Объясните формулу UI = f(Props, State)."],
            ["Props Down, Events Up", "Объясните однонаправленный поток: ребенок не трогает память родителя напрямую.", "Покажите механизм CustomEvent."],
            ["Factory vs Web Components", "Сравните фабричную функцию createBadge и нативный customElements.define.", "Покажите стандартные теги браузера."],
            ["State и Re-render", "Как setState перерисовывает точечно только один блок, экономя ресурсы.", "Подчеркните правило иммутабельности."],
            ["Живой Демо-Тренажер", "Нажимайте параметры Props и State карточки MetricCard на экране.", "Вызовите учеников для демонстрации."],
            ["Интерактивный Квиз", "Проведите опрос по 3 вопросам и закрепите пройденные правила.", "Нажимайте варианты ответов на экране."],
            ["Практическая Арена", "Ученики пишут код в studio/index.html. Запустите 25-минутный таймер.", "Помогайте парам учеников в классе."],
            ["Парный Код-Ревью", "Ученики меняются экранами и проверяют код соседа по 4 критериям.", "Следите за корректной обратной связью."],
            ["Демонстрация Работ", "2 пары выходят к доске и показывают свои компоненты в действии.", "Похвалите лучшие архитектурные решения."],
            ["Домашнее Задание 10 Баллов", "Разберите 10-балльную рубрику в vazifa.html и напомните об автосохранении.", "Покажите интерфейс приложения."],
            ["Итоги и Анонс 11 Недели", "Анонсируйте тему 11-й недели — SPA (Single Page Application) и клиентский роутинг.", "Выставите оценки за занятие."]
        ],
        "en": [
            ["Lesson Introduction", "Welcome 9th graders to Lesson 30 of Quarter 2. Announce component-driven architecture.", "Use Lego building blocks analogy."],
            ["Homework Review", "Demonstrate reference mutation pitfall from Lesson 29. Reiterate object spread immutability.", "Prompt 30-second blitz question."],
            ["Spaghetti Monolith Problem", "Explain why monolithic 3000-line files or copy-pasting HTML causes systemic fragility.", "Contrast with Google and Meta design systems."],
            ["Component Concept", "Illustrate Template + Scoped Styles + Props + State formula on the board.", "Explain UI = f(Props, State) projection."],
            ["Props Down, Events Up", "Explain unidirectional data flow: children never mutate parent state directly.", "Showcase CustomEvent dispatching."],
            ["Factory vs Web Components", "Contrast createBadge factory pattern with W3C customElements.define standard.", "Inspect native browser custom elements."],
            ["State & Targeted Re-render", "Show how setState executes surgical DOM updates without freezing the frame loop.", "Enforce immutable state updates."],
            ["In-Deck Live Simulator", "Interact with MetricCard props and internal state variables live on smartboard.", "Invite students to test button clicks."],
            ["Interactive Cyber Quiz", "Run rapid blitz check on 3 questions to solidify core principles.", "Click quiz choices on smartboard."],
            ["25-Min Cyber Arena", "Students build component library in studio/index.html. Start 25-min timer.", "Guide student pairs across the room."],
            ["Peer Review Quality Audit", "Students swap screens auditing component code across 4 checkpoints.", "Ensure constructive peer debugging."],
            ["Student Showcase Arena", "2 student pairs take the smartboard demonstrating reactive components.", "Celebrate clean engineering solutions."],
            ["Tiered Homework Rubric", "Explain 10-point rubric in vazifa.html and highlight local autosave in browser.", "Preview homework web application."],
            ["Summary & Week 11 Teaser", "Tease Week 11 topic — Single Page Applications (SPA) & Client-Side Routing.", "Record student achievements."]
        ]
    }
    notes_json = json.dumps(notes, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    # In-Deck Simulator & Timer scripts
    demo_js = """
// ============================================================
// IN-DECK INTERACTIVE SIMULATOR (Slide 8: Props & State)
// ============================================================
var demoState = {
  label: "API LATENCY",
  value: "24 ms",
  badgeText: "ONLINE",
  badgeColor: "#34d399",
  badgeBg: "rgba(16,185,129,0.2)",
  requests: 1420,
  renderCount: 1
};

function renderDemoCard() {
  var lEl = document.getElementById("demoCardLabel");
  var vEl = document.getElementById("demoCardValue");
  var bEl = document.getElementById("demoBadge");
  var rEl = document.getElementById("demoReqCount");
  var tReq = document.getElementById("telReqCount");
  var tRend = document.getElementById("telRenderCount");

  if (lEl) lEl.textContent = demoState.label;
  if (vEl) vEl.textContent = demoState.value;
  if (bEl) {
    bEl.textContent = demoState.badgeText;
    bEl.style.color = demoState.badgeColor;
    bEl.style.background = demoState.badgeBg;
  }
  if (rEl) rEl.textContent = demoState.requests.toLocaleString();
  if (tReq) tReq.textContent = demoState.requests;
  if (tRend) tRend.textContent = demoState.renderCount;
}

function setDemoProps(label, val) {
  demoState.label = label;
  demoState.value = val;
  demoState.renderCount++;
  renderDemoCard();
}

function setDemoBadge(text, color, bg) {
  demoState.badgeText = text;
  demoState.badgeColor = color;
  demoState.badgeBg = bg;
  demoState.renderCount++;
  renderDemoCard();
}

function sendDemoSignal() {
  demoState.requests++;
  demoState.renderCount++;
  renderDemoCard();
}

function resetDemoSignal() {
  demoState.label = "API LATENCY";
  demoState.value = "24 ms";
  demoState.badgeText = "ONLINE";
  demoState.badgeColor = "#34d399";
  demoState.badgeBg = "rgba(16,185,129,0.2)";
  demoState.requests = 1420;
  demoState.renderCount = 1;
  renderDemoCard();
}

// ============================================================
// ARENA PRACTICE TIMER (Slide 10: 25 Minutes)
// ============================================================
var deckTimerInterval = null;
var deckTimerSeconds = 25 * 60;

function updateDeckTimerDisplay() {
  var el = document.getElementById("deckTimerDisplay");
  if (!el) return;
  var m = Math.floor(deckTimerSeconds / 60);
  var s = deckTimerSeconds % 60;
  el.textContent = (m < 10 ? "0" : "") + m + ":" + (s < 10 ? "0" : "") + s;
}

function startDeckTimer(min) {
  if (min && !deckTimerInterval && deckTimerSeconds === 25 * 60) {
    deckTimerSeconds = min * 60;
  }
  toggleDeckTimer();
}

function toggleDeckTimer() {
  var btn = document.getElementById("deckTimerBtn") || document.querySelector("button[onclick*='DeckTimer']");
  if (deckTimerInterval) {
    clearInterval(deckTimerInterval);
    deckTimerInterval = null;
    if (btn) btn.textContent = currentLang === "ru" ? "▶ Продолжить" : (currentLang === "en" ? "▶ Resume" : "▶ Davom etish");
  } else {
    if (deckTimerSeconds <= 0) deckTimerSeconds = 25 * 60;
    deckTimerInterval = setInterval(function() {
      if (deckTimerSeconds > 0) {
        deckTimerSeconds--;
        updateDeckTimerDisplay();
      } else {
        clearInterval(deckTimerInterval);
        deckTimerInterval = null;
        var disp = document.getElementById("deckTimerDisplay");
        if (disp) disp.style.color = "var(--green)";
        if (btn) btn.textContent = currentLang === "ru" ? "▶ Старт (25 мин)" : (currentLang === "en" ? "▶ Start (25m)" : "▶ Boshlash (25m)");
        alert(currentLang === 'ru' ? 'Время практики истекло!' : (currentLang === 'en' ? 'Arena lab time is up!' : 'Amaliy arena vaqti yakunlandi!'));
      }
    }, 1000);
    if (btn) btn.textContent = currentLang === "ru" ? "⏸ Пауза" : (currentLang === "en" ? "⏸ Pause" : "⏸ Pauza");
  }
}

function resetDeckTimer() {
  if (deckTimerInterval) {
    clearInterval(deckTimerInterval);
    deckTimerInterval = null;
  }
  deckTimerSeconds = 25 * 60;
  var disp = document.getElementById("deckTimerDisplay");
  if (disp) disp.style.color = "var(--accent)";
  var btn = document.getElementById("deckTimerBtn");
  if (btn) btn.textContent = currentLang === "ru" ? "▶ Старт (25 мин)" : (currentLang === "en" ? "▶ Start (25m)" : "▶ Boshlash (25m)");
  updateDeckTimerDisplay();
}

function checkDeckQuiz(btn, isCorrect) {
  var parent = btn.parentElement;
  var allBtns = parent.querySelectorAll("button");
  allBtns.forEach(function(b) {
    b.disabled = true;
    b.style.opacity = "0.7";
  });
  btn.style.opacity = "1";
  if (isCorrect) {
    btn.style.background = "var(--green)";
    btn.style.color = "#fff";
    btn.style.borderColor = "var(--green)";
  } else {
    btn.style.background = "var(--accent)";
    btn.style.color = "#fff";
    btn.style.borderColor = "var(--accent)";
  }
}

window.addEventListener("DOMContentLoaded", function() {
  renderDemoCard();
});
"""
    tpl = tpl.replace("</script>\n</body>", f"{demo_js}\n</script>\n</body>")

    with open(os.path.join(LESSON_DIR, "prezentatsiya.html"), "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

    # ============================================================
    # 2. VARAQA.HTML (Printable A4 Worksheet)
    # ============================================================
    v_tpl = TPL_VAR
    v_tpl = v_tpl.replace("{{LESSON_NUM}}", "30")
    v_tpl = v_tpl.replace("{{TITLE_UZ}}", "Komponentlar Falsafasi va UI Arxitekturasi")
    v_tpl = v_tpl.replace("{{TITLE_RU}}", "Философия Компонентов и UI Архитектура")
    v_tpl = v_tpl.replace("{{TITLE_EN}}", "Component Philosophy & UI Architecture")
    v_tpl = v_tpl.replace("{{COHORT_LABEL_UZ}}", "9-sinf")
    v_tpl = v_tpl.replace("{{COHORT_LABEL_RU}}", "9 класс")
    v_tpl = v_tpl.replace("{{COHORT_LABEL_EN}}", "Grade 9")

    v_tpl = v_tpl.replace("{{META_UZ}}", "2-Chorak · 10-hafta · 30-dars · 80 daqiqa (Juftlik blok)")
    v_tpl = v_tpl.replace("{{META_RU}}", "2-я четверть · 10-я неделя · 30-й урок · 80 минут (Спаренный блок)")
    v_tpl = v_tpl.replace("{{META_EN}}", "Quarter 2 · Week 10 · Lesson 30 · 80 minutes (Double block)")

    v_tpl = v_tpl.replace("{{MISSION_UZ}}", "Qayta ishlatiluvchi mustaqil UI komponentlar (Badge, Card, Terminal) yaratish, bir tomonlama Props oqimini joriy etish va CustomEvent yordamida aloqa o'rnatish.")
    v_tpl = v_tpl.replace("{{MISSION_RU}}", "Создание переиспользуемых UI-компонентов (Badge, Card, Terminal), внедрение однонаправленного потока Props и связывание через CustomEvent.")
    v_tpl = v_tpl.replace("{{MISSION_EN}}", "Authoring reusable modular UI components (Badge, Card, Terminal), enforcing unidirectional Props flow, and establishing CustomEvent event channels.")

    v_tpl = v_tpl.replace("{{SEC1_TITLE_UZ}}", "1-Qism: Komponent Anatomiyasi — Props va State")
    v_tpl = v_tpl.replace("{{SEC1_TITLE_RU}}", "Часть 1: Анатомия Компонента — Props и State")
    v_tpl = v_tpl.replace("{{SEC1_TITLE_EN}}", "Part 1: Component Anatomy — Props vs State")
    v_sec1 = """    <div class="box-grid">
      <div class="box">
        <h4 data-ru="1. Props (Параметры)" data-en="1. Props (Properties)">1. Props (Tashqi Xususiyatlar)</h4>
        <p data-ru="Откуда приходят Props и почему дочерний компонент не имеет права их мутировать?" data-en="Where do Props originate from, and why must child components treat them as read-only?">Props qayerdan uzatiladi va nega farzand komponent uni o'zgartira olmaydi?</p>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="2. State (Внутреннее Состояние)" data-en="2. State (Internal Memory)">2. State (Ichki Holat)</h4>
        <p data-ru="Чем State отличается от обычной переменной и что происходит при вызове setState?" data-en="How does State differ from a local variable, and what triggers upon calling setState?">State oddiy o'zgaruvchidan nimasi bilan farq qiladi va setState chaqirilganda nima ro'y beradi?</p>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC1_CONTENT}}", v_sec1)

    v_tpl = v_tpl.replace("{{SEC2_TITLE_UZ}}", "2-Qism: Kod Tahlili — Xavfsiz Reaktiv Hisoblagich")
    v_tpl = v_tpl.replace("{{SEC2_TITLE_RU}}", "Часть 2: Анализ Кода — Безопасный Реактивный Счетчик")
    v_tpl = v_tpl.replace("{{SEC2_TITLE_EN}}", "Part 2: Code Analysis — Defensive Reactive Counter")
    v_sec2 = """    <div class="code-snippet">// ⚠️ Kodni to'g'rilang: State mutatsiyasini bartaraf eting va CustomEvent chiqaring:
class CounterComponent {
  constructor(initialCount = 0) {
    this.state = { count: initialCount };
  }
  increment() {
    // ❌ XATO: this.state.count++; (Direct mutation!)
    // ✅ TO'G'RI:
    this.state = { ________________________________________ };
    this.dispatchChange();
  }
  dispatchChange() {
    window.dispatchEvent(new CustomEvent("count-change", {
      detail: { __________________________________________ }
    }));
  }
}</div>
    <p style="margin-top:4px;" data-ru="Запишите правильное spread-обновление и поле payload события:" data-en="Fill in safe spread update and event detail payload:">Bo'sh joylarga toza spread yangilanishini va event detail obyektini yozing:</p>
    <div class="write-line"></div>"""
    v_tpl = v_tpl.replace("{{SEC2_CONTENT}}", v_sec2)

    v_tpl = v_tpl.replace("{{SEC3_TITLE_UZ}}", "3-Qism: Amaliy Laboratoriya (Cyber UI Komponentlar)")
    v_tpl = v_tpl.replace("{{SEC3_TITLE_RU}}", "Часть 3: Практическая Лаборатория (Cyber UI Компоненты)")
    v_tpl = v_tpl.replace("{{SEC3_TITLE_EN}}", "Part 3: Hands-on Lab (Cyber UI Components Table)")
    v_sec3 = """    <p data-ru="Проверьте работу компонентов в studio/index.html и заполните таблицу аудита:" data-en="Verify component behavior inside studio/index.html and complete audit table:"><b>studio/index.html</b> ilovasida komponentlarni sinab, natijalarni qayd eting:</p>
    <div class="box" style="margin-top:6px;">
      <table style="width:100%; border-collapse:collapse; font-size:8.5pt;">
        <thead>
          <tr style="border-bottom:1px solid var(--rule); text-align:left;">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Компонент" data-en="Component">Komponent</th>
            <th style="padding:4px 6px;" data-ru="Переданный Props" data-en="Dispatched Props">Props Parametrlari</th>
            <th style="padding:4px 6px;" data-ru="Результат / Событие" data-en="Result / Emitted Event">Natija va Chiqqan Event</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="&lt;cyber-badge&gt;" data-en="&lt;cyber-badge&gt;"><code>&lt;cyber-badge&gt;</code></td>
            <td style="padding:4px 6px;" data-ru='text="ONLINE", variant="green"' data-en='text="ONLINE", variant="green"'><code>text="ONLINE", variant="green"</code></td>
            <td style="padding:4px 6px;" data-ru="Зеленая капсула, событие click" data-en="Green capsule, click event">Yashil kapsula, click hodisasi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] OK" data-en="[ &nbsp; ] OK">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="&lt;metric-card&gt;" data-en="&lt;metric-card&gt;"><code>&lt;metric-card&gt;</code></td>
            <td style="padding:4px 6px;" data-ru='title="CPU", value="48%"' data-en='title="CPU", value="48%"'><code>title="CPU", value="48%"</code></td>
            <td style="padding:4px 6px;" data-ru="Заполнить результат" data-en="Fill in result"><div class="write-line" style="margin:2px 0;"></div></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] OK" data-en="[ &nbsp; ] OK">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="&lt;agent-terminal&gt;" data-en="&lt;agent-terminal&gt;"><code>&lt;agent-terminal&gt;</code></td>
            <td style="padding:4px 6px;" data-ru='maxLines=5, autoScroll=true' data-en='maxLines=5, autoScroll=true'><code>maxLines=5, autoScroll=true</code></td>
            <td style="padding:4px 6px;" data-ru="Заполнить результат" data-en="Fill in result"><div class="write-line" style="margin:2px 0;"></div></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] OK" data-en="[ &nbsp; ] OK">[ &nbsp; ] OK</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="&lt;action-btn&gt;" data-en="&lt;action-btn&gt;"><code>&lt;action-btn&gt;</code></td>
            <td style="padding:4px 6px;" data-ru='action="PURGE_CACHE"' data-en='action="PURGE_CACHE"'><code>action="PURGE_CACHE"</code></td>
            <td style="padding:4px 6px;" data-ru='CustomEvent("action", { action })' data-en='CustomEvent("action", { action })'>CustomEvent("action", { action })</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] OK" data-en="[ &nbsp; ] OK">[ &nbsp; ] OK</td>
          </tr>
        </tbody>
      </table>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC3_CONTENT}}", v_sec3)

    v_sec4 = """    <div class="box-grid" style="margin-top:6px;">
      <div class="box">
        <h4 data-ru="1-Уровень: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</h4>
        <p data-ru="Написать два чистых компонента (Badge и Button), управляемых только входными Props." data-en="Author 2 pure components (Badge and Button) strictly driven by input Props.">Faqat kiruvchi Props orqali boshqariluvchi 2 ta toza komponent shablonini yozish.</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="2-Уровень: Проект (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Amaliyot (4 ball)</h4>
        <p data-ru="Создать компонент счетчика со своим State и отправкой CustomEvent наверх." data-en="Build stateful counter component dispatching CustomEvent notifications upwards.">Ichki State xotirasiga ega bo'lgan va o'zgarganda CustomEvent chaqiruvchi hisoblagich yaratish.</p>
        <div class="write-line"></div>
      </div>
    </div>
    <div class="box" style="margin-top:6px;">
      <h4 data-ru="3-Уровень: Кибер-Вызов (2 балла)" data-en="Tier 3: Cyber Challenge (2 pts)">3-Daraja: Kiber-Chaqiruv (2 ball)</h4>
      <p data-ru="Реализовать нативный Web Component с observedAttributes для реактивного обновления." data-en="Implement native Web Component with observedAttributes lifecycle triggering targeted re-render.">Atributi o'zgarganda avtomatik yangilanuvchi rasmiy W3C Web Component (customElements) yaratish.</p>
      <div class="write-line"></div>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC4_CONTENT}}", v_sec4)

    with open(os.path.join(LESSON_DIR, "varaqa.html"), "w", encoding="utf-8") as f:
        f.write(v_tpl)
    print("  ✓ Created: varaqa.html")

    # ============================================================
    # 3. VAZIFA.HTML (Interactive Homework App)
    # ============================================================
    vz_tpl = TPL_VAZ
    vz_tpl = vz_tpl.replace("{{TITLE_UZ}}", "30-dars: Komponentlar Falsafasi va UI Arxitekturasi")
    vz_tpl = vz_tpl.replace("{{TITLE_RU}}", "Урок 30: Философия Компонентов и UI Архитектура")
    vz_tpl = vz_tpl.replace("{{TITLE_EN}}", "Lesson 30: Component Philosophy & UI Architecture")
    vz_tpl = vz_tpl.replace("{{LESSON_SLUG}}", "9-w10-l30-component-architecture")
    vz_tpl = vz_tpl.replace("{{COHORT_LABEL_UZ}}", "9-SINF · 10-HAFTA")
    vz_tpl = vz_tpl.replace("{{HERO_TAG_UZ}}", "UI ARXITEKTURA & REUSABLE KOMPONENTLAR")
    vz_tpl = vz_tpl.replace("{{HERO_DESC_UZ}}", "Komponentlar falsafasi, bir tomonlama Props oqimi, State reaktivligi va CustomEvent aloqalari bo'yicha 3 darajali topshiriqlarni bajaring.")
    vz_tpl = vz_tpl.replace("{{HERO_DESC_RU}}", "Выполните 3 уровня задач по философии компонентов, однонаправленному потоку Props, реактивности State и событиям CustomEvent.")
    vz_tpl = vz_tpl.replace("{{HERO_DESC_EN}}", "Complete 3 challenge tiers mastering component encapsulation, unidirectional Props, reactive State updates, and CustomEvent telemetry.")

    vz_tpl = vz_tpl.replace("{{RUBRIC_T1_UZ}}", "Props bilan boshqariluvchi &lt;cyber-badge&gt; shablonini yozish (4 ball)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T1_RU}}", "Создание компонента &lt;cyber-badge&gt; с поддержкой входных props (4 балла)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T1_EN}}", "Authoring pure &lt;cyber-badge&gt; component driven by input props (4 pts)")

    vz_tpl = vz_tpl.replace("{{RUBRIC_T2_UZ}}", "Holatli hisoblagich va CustomEvent chiqarish mexanizmi (4 ball)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T2_RU}}", "Реализация счетчика со State и отправкой CustomEvent наверх (4 балла)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T2_EN}}", "Building stateful counter emitting bubbling CustomEvents upwards (4 pts)")

    vz_tpl = vz_tpl.replace("{{RUBRIC_T3_UZ}}", "observedAttributes bilan reaktiv W3C Web Component (2 ball)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T3_RU}}", "Реализация нативного Web Component с observedAttributes (2 балла)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T3_EN}}", "Implementing native Web Component with observedAttributes re-rendering (2 pts)")

    tasks_9 = """  <!-- TASK 1 -->
  <article class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="1-Уровень: База" data-en="Tier 1: Base">1-Bosqich: Baza</span>
      <span class="task-score">4 BALL</span>
    </div>
    <h3 data-ru="Создание Компонента createBadge(props)" data-en="Authoring createBadge(props) Component">createBadge(props) Funksional Komponentini Yozish</h3>
    <p data-ru="Напишите фабричную функцию createBadge(props), которая принимает { text, variant } и возвращает стилизованный DOM элемент &lt;span&gt;. Значение variant по умолчанию должно быть 'info':" data-en="Write a factory function createBadge(props) taking { text, variant } and returning a styled &lt;span&gt; DOM node. Default variant to 'info':"><code>{ text, variant }</code> parametrlarini qabul qiluvchi va stillangan <code>&lt;span&gt;</code> DOM elementini qaytaruvchi <code>createBadge(props)</code> factory funksiyasini yozing. Standart variant 'info' bo'lsin:</p>
    <div class="code-box">// Kutilayotgan funksiya:
function createBadge({ text = "DEFAULT", variant = "info" }) {
  // 1. createElement("span")
  // 2. className = `badge badge-${variant}`
  // 3. textContent = text
  // 4. elementni qaytarish
}</div>
    <textarea class="answer-area" id="ans_task_1" rows="7" placeholder="JavaScript kodingizni bu yerga yozing..." data-placeholder-ru="Напишите ваш JavaScript код здесь..." data-placeholder-en="Write your JavaScript code here..." oninput="saveAnswers()"></textarea>
    <div style="margin-top:12px;">
      <button class="btn btn-outline teacher-solution-only" onclick="toggleSolution('sol_1')" data-ru="🔒 Эталон Решения (Учитель)" data-en="🔒 Solution (Teacher)">🔒 Etalon Yechim (O'qituvchi)</button>
      <div class="solution-box teacher-solution-only" id="sol_1" hidden>
        <h4 data-ru="✅ Эталонная Функция" data-en="✅ Reference Implementation">✅ Etalon Yechim</h4>
        <pre><code>export function createBadge({ text = "STATUS", variant = "info" } = {}) {
  const el = document.createElement("span");
  el.className = `badge badge-${variant}`;
  el.textContent = text;
  return el;
}</code></pre>
      </div>
    </div>
  </article>

  <!-- TASK 2 -->
  <article class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="2-Уровень: Проект" data-en="Tier 2: Engineering">2-Bosqich: Muhandislik</span>
      <span class="task-score">4 BALL</span>
    </div>
    <h3 data-ru="Реактивный Счетчик с CustomEvent" data-en="Reactive Counter with CustomEvent">Holatli Hisoblagich va CustomEvent Yuborish</h3>
    <p data-ru="Создайте класс CounterComponent со свойством state = { count: 0 }. При вызове increment() обновите state через spread ({ ...this.state, count: this.state.count + 1 }) и отправьте CustomEvent 'counter-updated' наверх:" data-en="Create class CounterComponent holding state = { count: 0 }. Inside increment(), update state immutably via spread and dispatch CustomEvent 'counter-updated':">Ichida <code>state = { count: 0 }</code> bo'lgan <code>CounterComponent</code> klassini yarating. <code>increment()</code> metodi chaqirilganda state-ni spread orqali yangilab, <code>new CustomEvent('counter-updated', { bubbles: true, detail: { count: this.state.count } })</code> hodisasini chaqiring:</p>
    <div class="code-box">class CounterComponent {
  constructor(initial = 0) {
    this.state = { count: initial };
  }
  increment() {
    // 1. Immutably update this.state
    // 2. Dispatch CustomEvent 'counter-updated'
  }
}</div>
    <textarea class="answer-area" id="ans_task_2" rows="8" placeholder="Klass kodini bu yerga yozing..." data-placeholder-ru="Напишите код класса здесь..." data-placeholder-en="Write class code here..." oninput="saveAnswers()"></textarea>
    <div style="margin-top:12px;">
      <button class="btn btn-outline teacher-solution-only" onclick="toggleSolution('sol_2')" data-ru="🔒 Эталон Решения (Учитель)" data-en="🔒 Solution (Teacher)">🔒 Etalon Yechim (O'qituvchi)</button>
      <div class="solution-box teacher-solution-only" id="sol_2" hidden>
        <h4 data-ru="✅ Эталонная Реализация" data-en="✅ Reference Implementation">✅ Etalon Yechim</h4>
        <pre><code>export class CounterComponent {
  constructor(initial = 0, targetElement = document.body) {
    this.state = { count: initial };
    this.target = targetElement;
  }
  increment() {
    this.state = { ...this.state, count: this.state.count + 1 };
    this.target.dispatchEvent(new CustomEvent("counter-updated", {
      bubbles: true,
      detail: { count: this.state.count }
    }));
  }
}</code></pre>
      </div>
    </div>
  </article>

  <!-- TASK 3 -->
  <article class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="3-Уровень: Вызов" data-en="Tier 3: Challenge">3-Bosqich: Kiber-Sinov</span>
      <span class="task-score">2 BALL</span>
    </div>
    <h3 data-ru="Нативный Web Component с observedAttributes" data-en="Native Web Component with observedAttributes">W3C Standartidagi Rasmiy Web Component</h3>
    <p data-ru="Зарегистрируйте пользовательский элемент customElements.define('metric-pill', MetricPill). Реализуйте статический геттер observedAttributes = ['value'] и метод attributeChangedCallback, чтобы элемент автоматически перерисовывался при изменении атрибута:" data-en="Register custom element customElements.define('metric-pill', MetricPill). Implement static observedAttributes = ['value'] and attributeChangedCallback for reactive re-render:"><code>customElements.define('metric-pill', MetricPill)</code> yordamida brauzerga yangi HTML teg o'rnating. <code>static get observedAttributes()</code> va <code>attributeChangedCallback</code> metodini qo'shib, HTMLdagi 'value' atributi o'zgarganda ekranni avtomatik yangilang:</p>
    <div class="code-box">class MetricPill extends HTMLElement {
  static get observedAttributes() { return ['value']; }
  attributeChangedCallback(name, oldVal, newVal) {
    // Re-render when 'value' changes!
  }
}
customElements.define('metric-pill', MetricPill);</div>
    <textarea class="answer-area" id="ans_task_3" rows="8" placeholder="Web Component kodini bu yerga yozing..." data-placeholder-ru="Напишите код компонента здесь..." data-placeholder-en="Write component code here..." oninput="saveAnswers()"></textarea>
    <div style="margin-top:12px;">
      <button class="btn btn-outline teacher-solution-only" onclick="toggleSolution('sol_3')" data-ru="🔒 Эталон Решения (Учитель)" data-en="🔒 Solution (Teacher)">🔒 Etalon Yechim (O'qituvchi)</button>
      <div class="solution-box teacher-solution-only" id="sol_3" hidden>
        <h4 data-ru="✅ Эталонный Web Component" data-en="✅ Reference Web Component">✅ Etalon Yechim</h4>
        <pre><code>class MetricPill extends HTMLElement {
  static get observedAttributes() {
    return ['value', 'label'];
  }
  connectedCallback() {
    this.render();
  }
  attributeChangedCallback(name, oldVal, newVal) {
    if (oldVal !== newVal) this.render();
  }
  render() {
    const val = this.getAttribute('value') || '0';
    const lbl = this.getAttribute('label') || 'METRIC';
    this.innerHTML = `&lt;span class="pill"&gt;&lt;b&gt;${lbl}:&lt;/b&gt; ${val}&lt;/span&gt;`;
  }
}
customElements.define('metric-pill', MetricPill);</code></pre>
      </div>
    </div>
  </article>"""
    vz_tpl = vz_tpl.replace("{{TASKS_CONTENT}}", tasks_9)

    with open(os.path.join(LESSON_DIR, "vazifa.html"), "w", encoding="utf-8") as f:
        f.write(vz_tpl)
    print("  ✓ Created: vazifa.html")

    # ============================================================
    # 4. TEACHER_READING.MD (80-Min Lesson Plan & Pacing)
    # ============================================================
    teacher_md = """# 30-Dars: O'qituvchi Uchun Metodik Qo'llanma va Yechimlar Kaliti
**Target International School // 9-Sinf // 10-Hafta (2-Chorak 2-Darsi: 80 daqiqa / Juftlik Blok)**
**Mavzu:** Komponentlar Falsafasi va UI Arxitekturasi: Reusable Components, Props & State
**Kohorta:** `9-sinf` (Junior Vibecoders, Full-Stack & DevOps Track)

---

## 1. Asosiy Pedagogik Maqsad
Bugungi 80 daqiqalik juftlik darsda 9-sinf o'quvchilari korporativ darajadagi **Komponentlar Falsafasi**ni amalda o'rganadilar:
1. **Lego Modeli:** Shablon (Template), Xususiyatlar (Props), Holat (State) va Hodisalar (Events) izolyatsiyasi.
2. **Bir Tomonlama Oqim (Props Down, Events Up):** Ota komponent bolaga props uzatadi, bola esa faqat CustomEvent chaqirib signal beradi.
3. **Immutability Qoidasi:** State-ni to'g'ridan-to'g'ri o'zgartirmasdan, spread (`{ ...this.state }`) orqali xavfsiz klonlash.
4. **Mustaqil Cyber UI Kutubxonasi:** `studio/index.html` laboratoriyasida Badge, MetricCard va Terminal komponentlarini mustaqil qurish.

---

## 2. 80 Daqiqalik Dars Reglamenti

### 1-Bosqich (00:00 – 40:00): Nazariya, Uy Vazifasi Tahlili va Jonli Test
* **00:00 – 04:00 (4 min):** Titul, Dars maqsadi va 80 daqiqalik kiber-missiya anonsi (Slayd 1).
* **04:00 – 12:00 (8 min):** Majburiy Uy Vazifasi Tahlili: 29-darsdagi Heap link mutatsiyasi xatosi va Spread klonlash oltin yechimi (Slayd 2).
* **12:00 – 18:00 (6 min):** Muammo: Spaghetti monolit va 50 ta faylni copy-paste qilish dahshati (Slayd 3).
* **18:00 – 24:00 (6 min):** Komponent anatomiyasi: Template, Props, State va Events (Slayd 4).
* **24:00 – 30:00 (6 min):** Arxitektura: Props Down, Events Up oqim diagrammasi (Slayd 5).
* **30:00 – 35:00 (5 min):** Kod mexanizmi: Factory function vs Native Web Components (Slayd 6).
* **35:00 – 40:00 (5 min):** State reaktivligi va Targeted Re-render mexanikasi (Slayd 7).

### 2-Bosqich (40:00 – 80:00): Jonli Simulyator, Kiber-Arena va Peer-Review
* **40:00 – 48:00 (8 min):** Jonli Simulyator: Smartboardda MetricCard Props va State o'zgarishlarini sinash (Slayd 8).
* **48:00 – 54:00 (6 min):** Interaktiv Quiz: 3 ta savol bo'yicha blits nazorat (Slayd 9).
* **54:00 – 69:00 (15 min):** Katta Kiber-Arena: `studio/index.html` da CyberBadge va MetricCard komponentlarini yozish (Slayd 10).
* **69:00 – 74:00 (5 min):** Juftlikda Peer-Review: 4 ta mezon bo'yicha partadosh kodini tekshirish (Slayd 11).
* **74:00 – 77:00 (3 min):** O'quvchilar Demosi: 2 ta juftlik o'z komponentini doskada ko'rsatadi (Slayd 12).
* **77:00 – 80:00 (3 min):** 10 ballik uy vazifasi tushuntiriladi va 11-haftaga (SPA & Routing) ko'prik tashlanadi (Slayd 13-14).

---

## 3. Topshiriqlar va Viktorina Yechimlari

### Viktorina (Slayd 9):
1. **Props va State farqi:** **B) Props tashqaridan keladi (read-only), State — ichki xotira.**
2. **Bolaning otaga aloqasi:** **B) CustomEvent dispatch qiladi (Events Up).**
3. **Nega direct mutation taqiqlangan:** **B) Re-render chaqirilmaydi va UI eskirib qoladi.**

### Amaliy Laboratoriya Yechimi:
```javascript
// studio/index.html etalon kodi:
export function createMetricCard(props) {
  const card = document.createElement("div");
  card.className = "cyber-card";
  card.innerHTML = `
    <div class="card-title">${props.title}</div>
    <div class="card-val">${props.value}</div>
  `;
  card.onclick = () => {
    card.dispatchEvent(new CustomEvent("metric-click", {
      bubbles: true,
      detail: { title: props.title }
    }));
  };
  return card;
}
```

---

## 4. 10 Ballik Baholash Rubrikasi

* **1-Daraja: Baza (4 ball):** Kiruvchi props asosida toza DOM element yasovchi `<cyber-badge>` komponenti.
* **2-Daraja: Muhandislik (4 ball):** O'zining State xotirasiga ega va CustomEvent chiqaruvchi hisoblagich.
* **3-Daraja: Kiber-Chaqiriq (2 ball):** `observedAttributes` bilan W3C rasmiy Web Component yaratish.
"""
    with open(os.path.join(LESSON_DIR, "TEACHER_READING.md"), "w", encoding="utf-8") as f:
        f.write(teacher_md)
    print("  ✓ Created: TEACHER_READING.md")

    # ============================================================
    # 5. STUDIO/INDEX.HTML (Interactive Component Studio)
    # ============================================================
    studio_html = """<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Cyber UI Component Studio — 9 Класс" data-en="Cyber UI Component Studio — Grade 9">Cyber UI Component Studio — 9-sinf</title>
  <link rel="stylesheet" href="../../../../../assets/brand.css">
  <style>
    :root {
      --bg: #090d16;
      --surface: #121826;
      --surface-2: #1b2337;
      --ink: #f1f5f9;
      --ink-2: #94a3b8;
      --rule: #28354d;
      --accent: #ef4444;
      --accent-soft: rgba(239, 68, 68, 0.15);
      --accent-ink: #fca5a5;
      --green: #10b981;
      --amber: #f59e0b;
      --blue: #38bdf8;
      --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
    }
    :root[data-theme="light"] {
      --bg: #f8fafc;
      --surface: #ffffff;
      --surface-2: #f1f5f9;
      --ink: #0f172a;
      --ink-2: #475569;
      --rule: #e2e8f0;
      --accent: #dc2626;
      --accent-soft: rgba(220, 38, 38, 0.12);
      --accent-ink: #991b1b;
      --green: #059669;
      --amber: #d97706;
      --blue: #0284c7;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      padding: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: var(--font-sans, system-ui, sans-serif);
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
      user-select: none;
    }
    header {
      padding: 10px 20px;
      background: var(--surface);
      border-bottom: 1px solid var(--rule);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-shrink: 0;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 700;
      font-size: 15px;
    }
    .brand span.tag {
      font-size: 11px;
      font-family: 'JetBrains Mono', monospace;
      padding: 3px 8px;
      background: var(--accent-soft);
      color: var(--accent-ink);
      border-radius: 4px;
    }
    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    main {
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 360px;
      gap: 16px;
      padding: 16px;
      box-sizing: border-box;
      min-height: 0;
    }
    .workbench {
      display: flex;
      flex-direction: column;
      gap: 16px;
      overflow-y: auto;
    }
    .component-stage {
      background: var(--surface);
      border-radius: 12px;
      border: 1px solid var(--rule);
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .stage-title {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 14px;
      font-weight: 700;
    }
    .component-render-area {
      min-height: 120px;
      background: #060911;
      border: 1px dashed var(--rule);
      border-radius: 8px;
      padding: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
    }
    /* Cyber Components Styles */
    .cyber-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      padding: 4px 10px;
      border-radius: 999px;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.15s;
    }
    .cyber-badge.green {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.4);
    }
    .cyber-badge.amber {
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border-color: rgba(245, 158, 11, 0.4);
    }
    .cyber-badge.red {
      background: rgba(239, 68, 68, 0.15);
      color: #f87171;
      border-color: rgba(239, 68, 68, 0.4);
    }
    .cyber-card {
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 16px;
      min-width: 220px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.4);
      cursor: pointer;
      transition: all 0.15s;
    }
    .cyber-card:hover {
      border-color: var(--blue);
      transform: translateY(-2px);
    }
    .card-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      color: #94a3b8;
      font-family: 'JetBrains Mono', monospace;
    }
    .card-val {
      font-size: 28px;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      color: #38bdf8;
      margin: 8px 0 4px 0;
    }
    .sidebar {
      background: var(--surface);
      border-radius: 12px;
      border: 1px solid var(--rule);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      overflow-y: auto;
    }
    .sidebar h2 {
      margin: 0;
      font-size: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .telemetry {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      background: var(--surface-2);
      border: 1px solid var(--rule);
      border-radius: 8px;
      padding: 10px 12px;
      line-height: 1.8;
    }
    .btn {
      padding: 6px 12px;
      background: var(--surface-2);
      color: var(--ink);
      border: 1px solid var(--rule);
      border-radius: 6px;
      font-weight: 600;
      font-size: 11.5px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.15s;
    }
    .btn:hover {
      background: var(--accent);
      color: #fff;
      border-color: var(--accent);
    }
    .btn.active {
      background: var(--accent-soft);
      color: var(--accent-ink);
      border-color: var(--accent);
    }
    .event-log {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      background: #030712;
      border: 1px solid var(--rule);
      border-radius: 8px;
      padding: 10px;
      height: 160px;
      overflow-y: auto;
      color: #94a3b8;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .event-entry {
      color: #34d399;
      word-break: break-all;
    }
  </style>
</head>
<body>

<header>
  <div class="brand">
    <span class="tag">TARGET VIBECODING</span>
    <span data-ru="Студия UI Компонентов (Vanilla JS & Web Components)" data-en="Cyber UI Component Studio (Vanilla JS & Web Components)">Cyber UI Component Studio (Vanilla JS & Web Components)</span>
  </div>
  <div class="header-actions">
    <button class="btn" onclick="toggleTheme()" aria-label="Theme">🌓</button>
    <div style="display:flex; gap:4px;">
      <button class="btn lang-btn active" data-lang="uz" onclick="setAppLang('uz')">UZ</button>
      <button class="btn lang-btn" data-lang="ru" onclick="setAppLang('ru')">RU</button>
      <button class="btn lang-btn" data-lang="en" onclick="setAppLang('en')">EN</button>
    </div>
  </div>
</header>

<main>
  <!-- Workbench -->
  <div class="workbench">
    <!-- Component 1: CyberBadge -->
    <div class="component-stage">
      <div class="stage-title">
        <span data-ru="1. &lt;cyber-badge&gt; Компонент (Props)" data-en="1. &lt;cyber-badge&gt; Component (Props)">1. &lt;cyber-badge&gt; Component (Props Driven)</span>
        <div style="display:flex; gap:6px;">
          <button class="btn" onclick="addBadge('ONLINE', 'green')" data-ru="+ Зеленый" data-en="+ Green">+ Green</button>
          <button class="btn" onclick="addBadge('DEGRADED', 'amber')" data-ru="+ Желтый" data-en="+ Amber">+ Amber</button>
          <button class="btn" onclick="addBadge('OFFLINE', 'red')" data-ru="+ Красный" data-en="+ Red">+ Red</button>
        </div>
      </div>
      <div class="component-render-area" id="badgeContainer">
        <span class="cyber-badge green" onclick="handleBadgeClick('ONLINE')">● ONLINE</span>
        <span class="cyber-badge amber" onclick="handleBadgeClick('RATE_LIMITED')">▲ RATE_LIMITED</span>
        <span class="cyber-badge red" onclick="handleBadgeClick('DOWN')">■ DOWN</span>
      </div>
    </div>

    <!-- Component 2: MetricCard -->
    <div class="component-stage">
      <div class="stage-title">
        <span data-ru="2. &lt;metric-card&gt; Компонент (State & События)" data-en="2. &lt;metric-card&gt; Component (State & Events)">2. &lt;metric-card&gt; Component (Stateful & Click Events)</span>
        <div style="display:flex; gap:6px;">
          <button class="btn" onclick="addMetricCard('API Latency', '24 ms')" data-ru="+ Карточка Задержки" data-en="+ Latency Card">+ Latency Card</button>
          <button class="btn" onclick="addMetricCard('Active Agents', '8 units')" data-ru="+ Карточка Агентов" data-en="+ Agents Card">+ Agents Card</button>
        </div>
      </div>
      <div class="component-render-area" id="cardContainer">
        <div class="cyber-card" onclick="handleCardClick('API Latency')">
          <div class="card-head"><span>API LATENCY</span><span style="color:#34d399;">● OK</span></div>
          <div class="card-val">24 ms</div>
          <div style="font-size:11px; color:#94a3b8;">Clicks: <b style="color:#f1f5f9;">0</b> · Target: <span style="color:#38bdf8;">Production</span></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Sidebar Telemetry & Event Bus -->
  <div class="sidebar">
    <h2>
      <span data-ru="Шина Событий (Event Bus)" data-en="Event Bus Telemetry">Hodisalar Shinalari (Event Bus)</span>
      <button class="btn" onclick="clearEventLog()" data-ru="Очистить" data-en="Clear">Tozalash</button>
    </h2>

    <div class="telemetry">
      <div data-ru="Активные компоненты: " data-en="Active Components: ">Active Components: <span id="telCount" style="color:var(--blue); font-weight:700;">4</span></div>
      <div data-ru="Событий CustomEvent: " data-en="CustomEvents Dispatched: ">CustomEvents Dispatched: <span id="telEvents" style="color:var(--accent); font-weight:700;">0</span></div>
      <div data-ru="Единый источник правды: " data-en="Single Source of Truth: ">Single Source of Truth: <span style="color:var(--green); font-weight:700;">ENFORCED</span></div>
    </div>

    <h2 style="margin-top:6px;" data-ru="Логи Событий CustomEvent" data-en="CustomEvent Action Stream">Real-Vaqt Event Oqimi</h2>
    <div class="event-log" id="eventLog">
      <div style="color:#64748b;" data-ru="// Лог событий будет здесь..." data-en="// Event stream will appear here...">// CustomEvent hodisalari bu yerda oqib chiqadi...</div>
    </div>

    <div style="margin-top:auto; font-size:11px; color:var(--ink-2); line-height:1.5;" data-ru="💡 Каждый компонент имеет собственный шаблон и общается с родительским окном через new CustomEvent()." data-en="💡 Each component owns its scoped markup and notifies parent container via new CustomEvent().">
      💡 Har bir komponent o'zining ichki shabloniga ega va ota oynaga <code>new CustomEvent()</code> orqali xabar uzatadi.
    </div>
  </div>
</main>

<script>
var appLang = "uz";
var eventCounter = 0;

function setAppLang(l) {
  appLang = l;
  document.documentElement.lang = l;
  document.querySelectorAll(".lang-btn").forEach(function(b) {
    b.classList.toggle("active", b.getAttribute("data-lang") === l);
  });
  document.querySelectorAll("[data-" + l + "]").forEach(function(el) {
    if (el.children.length === 0 || el.tagName === "TITLE") {
      el.textContent = el.getAttribute("data-" + l);
    }
  });
}

function toggleTheme() {
  var cur = document.documentElement.getAttribute("data-theme") || "dark";
  var next = (cur === "dark") ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", next);
}

function logEvent(type, detail) {
  eventCounter++;
  document.getElementById("telEvents").textContent = eventCounter;
  var log = document.getElementById("eventLog");
  var entry = document.createElement("div");
  entry.className = "event-entry";
  entry.textContent = `[${new Date().toLocaleTimeString()}] ${type} -> ${JSON.stringify(detail)}`;
  log.prepend(entry);
}

function clearEventLog() {
  document.getElementById("eventLog").innerHTML = '<div style="color:#64748b;">// Log tozalandi</div>';
}

function updateComponentCount() {
  var bCount = document.querySelectorAll(".cyber-badge").length;
  var cCount = document.querySelectorAll(".cyber-card").length;
  document.getElementById("telCount").textContent = bCount + cCount;
}

function handleBadgeClick(text) {
  logEvent("CustomEvent('badge-click')", { text: text });
}

function addBadge(text, variant) {
  var container = document.getElementById("badgeContainer");
  var el = document.createElement("span");
  el.className = `cyber-badge ${variant}`;
  el.textContent = (variant === "green" ? "● " : (variant === "amber" ? "▲ " : "■ ")) + text;
  el.onclick = function() { handleBadgeClick(text); };
  container.appendChild(el);
  updateComponentCount();
  logEvent("ComponentCreated", { type: "cyber-badge", variant: variant, text: text });
}

function handleCardClick(title) {
  logEvent("CustomEvent('metric-selected')", { metric: title });
}

function addMetricCard(title, val) {
  var container = document.getElementById("cardContainer");
  var card = document.createElement("div");
  card.className = "cyber-card";
  var clicks = 0;
  card.innerHTML = `
    <div class="card-head"><span>${title.toUpperCase()}</span><span style="color:#34d399;">● OK</span></div>
    <div class="card-val">${val}</div>
    <div style="font-size:11px; color:#94a3b8;">Clicks: <b class="click-counter" style="color:#f1f5f9;">0</b> · Target: <span style="color:#38bdf8;">Live</span></div>
  `;
  card.onclick = function() {
    clicks++;
    card.querySelector(".click-counter").textContent = clicks;
    logEvent("CustomEvent('metric-click')", { title: title, count: clicks });
  };
  container.appendChild(card);
  updateComponentCount();
  logEvent("ComponentCreated", { type: "metric-card", title: title, initialValue: val });
}

window.addEventListener("DOMContentLoaded", function() {
  updateComponentCount();
});
</script>
</body>
</html>
"""
    with open(os.path.join(STUDIO_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(studio_html)
    with open(os.path.join(LAB_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(studio_html)
    print("  ✓ Created: studio/index.html & lab/index.html")

    print(f"🎉 9-sinf (30-dars) generation finished in {LESSON_DIR}!")

if __name__ == "__main__":
    build_9_lesson()
