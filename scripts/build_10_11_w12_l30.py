#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_10_11_w12_l30.py — Builder for 10–11th Grade, Week 12, Lesson 30

Mavzu: Agentik Veb-Brauzing va Headless Avtomatlashtirish: DOM Tahlili, Vision-Action Tsikli va Browser-Use
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 10-11-sinf (Senior AI & Enterprise Cybersecurity Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "10-11-sinf", "12-hafta", "30-dars-agentik-veb-brauzing-va-avtomatlashtirish")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "simulator"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides for 80-min Double Block)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="10–11-КЛАСС · 12-Я НЕДЕЛЯ · УРОК 30" data-en="GRADES 10–11 · WEEK 12 · LESSON 30">10–11-SINF · 12-HAFTA · 30-DARS</span></div>
    <h1 class="display" data-ru="Агентный Веб-Браузинг и Headless Автоматизация: DOM Анализ и Browser-Use" data-en="Autonomous Web Browsing & Headless Automation: DOM Parsing & Browser-Use">Agentik Veb-Brauzing va Headless Avtomatlashtirish: DOM Tahlili va Browser-Use</h1>
    <p class="lede" data-ru="Выход ИИ-агентов в открытый интернет: преодоление ограничений API через Playwright, дистилляция Accessibility Tree из 1 МБ HTML в 5 КБ токенов, гибридный цикл Vision-Action и защищенная архитектура Browser-Use." data-en="Extending AI agents into the live open web: breaking beyond APIs with Playwright, distilling 1MB raw HTML into 5KB Accessibility Trees, hybrid Vision-Action execution loops, and robust Browser-Use architecture.">AI agentlarning jonli ochiq internetga chiqishi: Playwright orqali API chegaralarini yorib o'tish, 1 MB HTML-ni 5 KB Accessibility Tree ga qisqartirish, gibrid Vision-Action tsikli va mustahkam Browser-Use arxitekturasi.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="DOM Дистилляция" data-en="DOM Distillation">Tree Pruning va Tokenlar</h3>
        <p data-ru="Как сжать 20,000 строк разметки в компактный интерактивный граф элементов без потери ссылок и кнопок." data-en="How to compress 20,000 lines of messy HTML into a compact interactive element graph without losing clickable nodes.">Qanday qilib 20,000 qatorli chalkash HTML-ni tugmalar va maydonlarni yo'qotmasdan 50 barobar kichraytirish mumkin.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Browser-Use Studio</div>
        <h3 data-ru="Автономный Скрапер" data-en="Autonomous Scraper">Avtonom Veb-Agent</h3>
        <p data-ru="Каждый ученик запрограммирует агента, способного открыть магазин, найти товар, обойти модальное окно и собрать JSON-отчет." data-en="Each student programs an agent capable of opening an e-commerce store, searching items, handling popups, and extracting JSON tables.">Har bir o'quvchi do'konga kirib, qidiruv berib, pop-up oynani chetlab o'tib, narxlar jadvalini JSON formatida yig'uvchi agentni ishga tushiradi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 29-УРОКА" data-en="LESSON 29 HOMEWORK REVIEW">29-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Автономный TDD Цикл: Регрессионные Ошибки и Ловушка Полного Переписывания" data-en="Autonomous TDD Loops: Regression Traps & Blind Rewrites">Avtonom TDD Tsikli: Regressiya Qopqoni va Noldan Qayta Yozish Xatosi</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Типичная ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h4 data-ru="Coder переписывает весь файл с нуля при одной ошибке" data-en="Coder rewrites whole module upon single failing assertion">Bitta test yiqilganda Coder butun faylni noldan qayta yozishi</h4>
        <p style="font-size:12px;" data-ru="Когда PyTest выдал 1 падение из 5 тестов, Coder сгенерировал код заново, исправил этот баг, но сломал 3 ранее работавших теста (Regression). Потрачено 40,000 лишних токенов!" data-en="When PyTest reported 1 failure out of 5, Coder generated the entire codebase from scratch, fixing that bug but breaking 3 previously passed assertions (Regression). Over 40,000 tokens wasted!">PyTest 5 ta testdan 1 tasida xato topganda, Coder butun modulni noldan yozib, o'sha xatoni tuzatdi, ammo ilgari o'tgan 3 ta testni sindirib qo'ydi (Regressiya). 40,000 ortiqcha token yonib ketdi!</p>
        <pre><code class="language-python"># ❌ Xato: Butun kodni yangidan generatsiya qilish
prompt = f"Mana bu test yiqildi: {err}. Kodni noldan qayta yoz!"</code></pre>
      </div>
      <div class="box" style="border:1px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой стандарт (Golden Solution)" data-en="Golden Standard">Oltin Standart Yechim</div>
        <h4 data-ru="Surgical Diff: Critic указывает точную строку и патч" data-en="Surgical Diff: Critic pinpoints failing line & targeted patch">Nuqtali Diff (Surgical Patch): Faqat xato qatorni tuzatish</h4>
        <p style="font-size:12px;" data-ru="Critic парсит traceback, находит конкретный line number и генерирует только замену функции или строчки. Сохраняются все существующие инварианты." data-en="Critic parses stack traces, isolates exact line numbers, and drafts surgical diff replacements preserving existing invariants.">Critic traceback tahlil qilib aniq xato satrni topadi va faqat o'sha funksiyaga nuqtali yamoq (patch) kiritadi. Barcha o'tgan testlar 100% yashilligicha qoladi.</p>
        <pre><code class="language-python"># ✅ To'g'ri: Faqat xato funksiya uchun patch
prompt = f"Traceback line 42: {err}. Faqat _evict() funksiyasini tuzatib qaytar."</code></pre>
      </div>
    </div>
    <div class="grid-2" style="margin-top:10px;">
      <div class="box">
        <div class="tag" data-ru="30-секундный Блиц" data-en="30-Sec Blitz">30 Soniyalik Blitz</div>
        <p style="font-size:11px;" data-ru="Почему запуск непроверенного ИИ-кода прямо в терминале сервера — это критическая уязвимость?" data-en="Why is executing unverified AI code directly in the server host a critical vulnerability?">Nega tekshirilmagan AI kodini to'g'ridan-to'g'ri server terminalida ishga tushirish falokatli zaiflik hisoblanadi?</p>
        <div style="font-size:11px; color:var(--accent); font-weight:700;" data-ru="Ответ: Риск RCE (Remote Code Execution) и удаление данных. Необходим Docker/gVisor песочница." data-en="Answer: RCE threat and filesystem deletion. Sandboxed execution with timeout limits is mandatory.">Javob: RCE (Remote Code Execution) va fayllar o'chib ketish xavfi. Timeout chekloviga ega sandbox shart!</div>
      </div>
      <div class="box">
        <div class="tag" data-ru="Мост к теме 30" data-en="Bridge to Lesson 30">Bugungi Mavzuga Ko'prik</div>
        <p style="font-size:11px;" data-ru="TDD автоматизировал код. Но что если данные для нашего кода лежат на веб-сайтах без API? Нам нужен Агентный Браузер!" data-en="TDD automated our code. But what if the data lives on websites without public APIs? We need an Autonomous Web Agent!">TDD kodimizni avtomatlashtirdi. Ammo kerakli ma'lumotlar ochiq API-si bo'lmagan veb-saytlarda bo'lsa-chi? Bizga Veb-Agent kerak!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: PROBLEM OF RAW WEB -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="АРХИТЕКТУРНЫЙ БАРЬЕР" data-en="ARCHITECTURAL BARRIER">ARXITEKTURA TO'SIG'I</span></div>
    <h2 data-ru="Почему LLM не может просто «прочитать» современный веб-сайт?" data-en="Why Can't Raw LLMs Simply 'Read' Modern Web Pages?">Nega Oddiy LLM Zamonaviy Veb-Saytni Shunchaki O'qiy Olmaydi?</h2>
    <div class="grid-3">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="1. Взрыв Контекста" data-en="1. Context Overflow">1. Tokenlar Portlashi</div>
        <h4 data-ru="1–3 МБ сырого HTML на страницу" data-en="1–3 MB raw HTML per page">1 Sahifa = 1–3 MB Xom HTML</h4>
        <p style="font-size:12px;" data-ru="Современные SPA (Amazon, Uzum, LinkedIn) напичканы встроенными SVG, inline-стилями, скриптами трекеров и 30,000 строками мусора. 128k контекстное окно заполняется за 1 запрос!" data-en="Modern SPAs contain inline styles, tracking scripts, base64 assets, and 30k lines of noise. A 128k context window is exhausted in a single call!">Zamonaviy veb-sahifalar inline CSS, SVG, reklama trekerlari va 30,000 qator ortiqcha kodga ega. Bitta sahifaning o'zi 128k kontekst oynasini to'ldirib tashlaydi!</p>
      </div>
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="2. Динамический DOM" data-en="2. Dynamic DOM">2. Dinamik DOM va JS</div>
        <h4 data-ru="curl и requests получают пустышку" data-en="cURL and requests get blank shells">curl / requests bo'sh sahifa oladi</h4>
        <p style="font-size:12px;" data-ru="Классический парсинг (BeautifulSoup) видит только пустой `<div id='root'></div>`. Реальные данные подгружаются через React/Vue по WebSockets и API после рендеринга в браузере." data-en="Traditional scrapers receive empty shells. Real datasets hydrate via client-side JavaScript execution, async REST calls, and WebSockets.">Oddiy scraperlar faqat bo'sh `&lt;div id="root"&gt;&lt;/div&gt;` tegini ko'radi. Haqiqiy ma'lumotlar esa brauzerda JavaScript ishga tushgandan so'ng yuklanadi.</p>
      </div>
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="3. Интерактивные Барьеры" data-en="3. Interaction Gates">3. Dinamik To'siqlar</div>
        <h4 data-ru="Попапы, куки, бесконечный скролл" data-en="Popups, cookie gates, infinite scroll">Modal oynalar, Cookie va Slayderlar</h4>
        <p style="font-size:12px;" data-ru="Чтобы увидеть таблицу цен, нужно кликнуть «Принять куки», закрыть баннер акции, проскроллить вниз и переключить вкладку. Статичный парсер бессилен!" data-en="Unlocking pricing tables requires accepting cookies, dismissing promotional modals, scrolling viewport, and switching tabs. Static scrapers fail completely!">Jadvalni ko'rish uchun avval "Cookie qabul qilish", aksiyani yopish, sahifani pastga aylantirish va tabni bosish kerak. Statik skript bu yerda ojiz!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: HEADLESS ARCHITECTURE -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="ТЕХНОЛОГИЧЕСКИЙ СТЕК" data-en="TECH STACK">TEXNOLOGIK STEK</span></div>
    <h2 data-ru="Архитектура Headless-Браузера: CDP и Playwright" data-en="Headless Browser Architecture: CDP & Playwright">Headless Brauzer Arxitekturasi: CDP va Playwright</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" data-ru="Chrome DevTools Protocol (CDP)" data-en="Chrome DevTools Protocol (CDP)">CDP Mexanizmi</div>
        <h4 data-ru="Прямой JSON-RPC сокет с ядром Chromium" data-en="Direct JSON-RPC socket to Chromium core">Chromium yadrosi bilan to'g'ridan-to'g'ri JSON-RPC</h4>
        <p style="font-size:12px;" data-ru="Headless браузер — это полноценный Chrome без графического интерфейса (GUI). Мы управляем им через протокол WebSocket CDP: передаем команды `DOM.enable`, `Page.navigate`, `Input.dispatchMouseEvent`." data-en="Headless browsers are full Chromium engines running without a GUI display. We pilot them via WebSocket CDP exchanging low-level commands like input events and DOM snapshots.">Headless brauzer — bu grafik oynasisiz (GUI) ishlovchi to'liq Chromium brauzeri. Biz uni CDP protokoli orqali boshqaramiz: klaviatura, sichqoncha va DOM hodisalarini uzatamiz.</p>
        <pre><code class="language-python"># Playwright orqali headless sessiya
from playwright.async_api import async_playwright

async with async_playwright() as p:
    browser = await p.chromium.launch(headless=True)
    page = await browser.new_page()
    await page.goto("https://market.uz")</code></pre>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Сравнение Фреймворков" data-en="Framework Spectrum">Veb-Agent Vositalari</div>
        <div style="font-size:11px; margin-top:6px; line-height:1.6;">
          <div style="border-bottom:1px solid var(--hair); padding-bottom:6px;">
            <strong>Selenium:</strong> <span style="color:var(--ink-2);" data-ru="Тяжелый, медленный WebDriver, устаревший для LLM-агентов." data-en="Heavy legacy WebDriver, outdated and slow for fast LLM feedback loops.">Eski, sekin ishlovchi WebDriver. Tezkor AI tsikllar uchun og'ir.</span>
          </div>
          <div style="border-bottom:1px solid var(--hair); padding:6px 0;">
            <strong>Playwright:</strong> <span style="color:var(--accent);" data-ru="Быстрый, стабильный, авто-ожидание селекторов (Auto-waiting), эмуляция устройств." data-en="Lightning fast, natively async, auto-waits elements, excellent mobile/desktop emulation.">Tezyurar, asinxron, element paydo bo'lishini avtomatik kutadi.</span>
          </div>
          <div style="border-bottom:1px solid var(--hair); padding:6px 0;">
            <strong>Browser-Use / Stagehand:</strong> <span style="color:var(--green);" data-ru="Агентная надстройка над Playwright: Vision + Accessibility Tree + Action Executor." data-en="Agentic layer on top of Playwright: Vision + Accessibility Trees + Structured Action Schema.">Playwright ustidagi AI qatlam: Vision + DOM Pruning + Harakatlar bajaruvchisi.</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: ACCESSIBILITY TREE & DOM PRUNING -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="СЕКРЕТ ЭКОНОМИИ ТОКЕНОВ" data-en="TOKEN OPTIMIZATION SECRET">TOKENLARNI TEJASH S達RI</span></div>
    <h2 data-ru="Дистилляция DOM: Accessibility Tree и Чистка Мусора" data-en="DOM Distillation: Accessibility Trees & Noise Pruning">DOM Distillyatsiyasi: Accessibility Tree va Elementlar Idexatsiyasi</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Сырой HTML (1 000 000 символов)" data-en="Raw HTML (1,000,000 chars)">1. Xom HTML (To'la Chiqindi)</div>
        <pre><code class="language-html">&lt;div class="nav-wrapper-v2_flex__8x7a" style="margin:0; padding:12px; display:flex;"&gt;
  &lt;svg viewBox="0 0 24 24" class="svg-icon-search_v1"&gt;
    &lt;path d="M12 2a10 10 0..."/&gt;
  &lt;/svg&gt;
  &lt;input type="text" placeholder="Qidirish" class="search-input_dark" id="q_input" /&gt;
  &lt;button class="btn-primary-329" onclick="doSearch()"&gt;Izlash&lt;/button&gt;
&lt;/div&gt;</code></pre>
        <p style="font-size:11px; color:var(--red);" data-ru="95% разметки — стили, классы Tailwind, SVG координаты и пустые div." data-en="95% of characters are styling, tailwind junk, SVG paths, and nesting divs.">95% matn — Tailwind klasslari, CSS uslublar va SVG koordinatalar.</p>
      </div>
      <div class="box" style="border:1px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Accessibility Tree (500 символов)" data-en="Accessibility Tree (500 chars)">2. Distillangan Interaktiv Tree</div>
        <pre><code class="language-yaml"># Faqat interaktiv elementlar va ularning indekslari
[4] input "Qidirish" (id="q_input")
[5] button "Izlash"
[6] link "Savatcha (3)"
[7] table "Narxlar jadvali"
    row 1: ["MacBook M3", "14 500 000 so'm"]
    row 2: ["ThinkPad X1", "12 800 000 so'm"]</code></pre>
        <p style="font-size:11px; color:var(--green);" data-ru="LLM получает только кнопки, поля ввода и текст. Экономия 98% токенов!" data-en="LLM receives only interactable nodes, labels, and bounding indexes. 98% token savings!">LLM faqat tugmalar, maydonlar va matnlarni oladi. 98% token tejaladi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: VISION-ACTION DUAL LOOP -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ГИБРИДНЫЙ ПОДХОД" data-en="HYBRID APPROACH">GIBRID YONDASHUV</span></div>
    <h2 data-ru="Цикл Vision-Action: Скриншот против DOM-Селекторов" data-en="Vision-Action Loop: Screenshots vs DOM Selectors">Vision-Action Tsikli: Skrinshot va DOM Selektorlar Gibridi</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag" data-ru="1. Восприятие (Observe)" data-en="1. Observe">1. Kuzatish (Observe)</div>
        <h4 data-ru="Скриншот + SoM разметка" data-en="Screenshot + SoM tagging">Skrinshot + Set-of-Mark (SoM)</h4>
        <p style="font-size:11px;" data-ru="Браузер делает снимок экрана и поверх каждой кликабельной кнопки рисует цветную рамку с номером `[12]`. Мультимодальная модель видит визуальное расположение." data-en="Browser captures viewport and overlays numbered bounding boxes `[12]` on all clickable items (Set-of-Mark). Vision model sees human UI.">Brauzer skrinshot oladi va barcha bosiladigan elementlarga raqamli ramka `[12]` qo'yadi (Set-of-Mark). AI inson kabi ko'radi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);" data-ru="2. Решение (Plan)" data-en="2. Plan">2. Fikrlash (Plan)</div>
        <h4 data-ru="Анализ цели и выбор действия" data-en="Goal analysis & action picking">Maqsad tahlili va reja</h4>
        <p style="font-size:11px;" data-ru="Агент сверяет текущий экран с целью пользователя: «Баннер закрывает поиск. Сначала нужно нажать крестик [3], затем ввести запрос в поле [12]»." data-en="Agent checks goal against current view: 'Promo modal blocks search bar. Action: dismiss modal [3], then type into input [12]'.">Agent maqsad bilan ekranni solishtiradi: "Reklama oynasi qidiruvni to'syapti. Avval [3] ni yopish, keyin [12] ga qidiruv kiritish kerak".</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="3. Действие (Act)" data-en="3. Act">3. Bajarish (Act)</div>
        <h4 data-ru="Отправка события в Playwright" data-en="Dispatching event to Playwright">Playwright orqali hodisa</h4>
        <p style="font-size:11px;" data-ru="Агент выдает строгий JSON: `{\"action\": \"click\", \"index\": 3}`. Playwright отправляет реальный клик мыши и ждет изменения сетевых запросов." data-en="Agent returns strict JSON: `{\"action\": \"click\", \"index\": 3}`. Playwright dispatches real hardware-level click and waits for network idle.">Agent qat'iy JSON chiqaradi: `{"action": "click", "index": 3}`. Playwright apparat darajasida klik qiladi va DOM yangilanishini kutadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: AGENT ACTION SCHEMA -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="СПЕЦИФИКАЦИЯ КОМАНД" data-en="COMMAND SPECIFICATION">BUYRUQLAR SPETSIFIKATSIYASI</span></div>
    <h2 data-ru="Схема Действий Агента: Строгий JSON Протокол" data-en="Agent Action Schema: Strict JSON Execution Protocol">Agent Harakatlar Sxemasi: Qat'iy JSON Protokoli</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" data-ru="Типизированные Действия" data-en="Typed Actions">Mavjud Harakatlar To'plami</div>
        <ul style="font-size:12px; line-height:1.7; margin-top:6px;">
          <li><code>click(index)</code> — <span class="t" data-ru="Клик по элементу с указанным ID" data-en="Click element by index number">Berilgan indeksli tugma/havolani bosish</span></li>
          <li><code>type(index, text)</code> — <span class="t" data-ru="Ввод текста в инпут с очисткой старого" data-en="Clear input field and type string">Maydonni tozalab, matn yozish</span></li>
          <li><code>scroll(direction, px)</code> — <span class="t" data-ru="Прокрутка 'up' или 'down' на N пикселей" data-en="Scroll viewport up/down by pixels">Sahifani pastga/yuqoriga aylantirish</span></li>
          <li><code>wait(seconds)</code> — <span class="t" data-ru="Пауза для завершения AJAX-запросов" data-en="Wait for dynamic AJAX hydration">AJAX ma'lumotlari yuklanishini kutish</span></li>
          <li><code>extract(schema)</code> — <span class="t" data-ru="Парсинг таблицы/карточек в JSON" data-en="Scrape targeted elements into JSON">Ko'ringan ma'lumotlarni JSON ga olish</span></li>
          <li><code>finish(summary)</code> — <span class="t" data-ru="Завершение миссии с финальным ответом" data-en="Mission accomplished terminal state">Vazifa yakunlanganini e'lon qilish</span></li>
        </ul>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);" data-ru="Пример Ответа Модели" data-en="Model Response Payload">Model JSON Chiqishi</div>
        <pre><code class="language-json">{
  "thought": "Do'kon qidiruv maydoni [4] raqamida topildi. 'MacBook' so'zini yozamiz va [5] Izlash tugmasini bosamiz.",
  "action": {
    "name": "type",
    "params": {
      "index": 4,
      "text": "MacBook Pro M3"
    }
  },
  "follow_up": {
    "name": "click",
    "params": { "index": 5 }
  }
}</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: ANTI-BOT & SAFETY GUARDRAILS -->
  <section class="slide" data-phase="Kiberxavfsizlik|Кибербезопасность|Security" data-time="40:00–45:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="КИБЕР-ГИГИЕНА И ЭТИКА" data-en="CYBER HYGIENE & ETHICS">KIBERXAVFSIZLIK VA XAVFSIZ CHEGARALAR</span></div>
    <h2 data-ru="Защита от Блокировок: Rate Limiting и Человеческий Фактор" data-en="Anti-Bot Resilience: Rate Limiting & Human-in-the-Loop">Bloklanishdan Himoya: Rate Limiting va Inson Nazorati (HITL)</h2>
    <div class="grid-3">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="1. CAPTCHA Правило" data-en="1. CAPTCHA Rule">1. CAPTCHA Qat'iy Qoidasi</div>
        <h4 data-ru="Никакого взлома капчи" data-en="Never bypass CAPTCHAs">Avtomat CAPTCHA buzilmaydi</h4>
        <p style="font-size:11px;" data-ru="Агент НИКОГДА не должен пытаться программно обойти Cloudflare Turnstile или reCAPTCHA. При обнаружении капчи агент обязан вызвать HITL (Human-in-the-Loop) и попросить человека кликнуть в реальном браузере." data-en="Agents must NEVER compute bypasses for CAPTCHAs or Cloudflare challenges. Pause execution, alert human operator (HITL), and resume once verified.">Agent HECH QACHON Cloudflare yoki reCAPTCHA ni avtomat yorishga urinmasligi shart. Captcha chiqqanda jarayon to'xtatilib, insonga (HITL) topshiriladi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="2. Человеческие Задержки" data-en="2. Human Jitter">2. Tabiiy Insoniy Kechikish</div>
        <h4 data-ru="Jitter: 300–800 мс между кликами" data-en="Jitter: 300–800ms delays">Tasodifiy kechikish (Jitter)</h4>
        <p style="font-size:11px;" data-ru="Если агент кликает 50 ссылок за 1 секунду, WAF (Web Application Firewall) моментально банит IP по маске бота. Добавляем случайные паузы и плавное движение курсора." data-en="Firing 50 clicks/sec instantly triggers WAF bot mitigations and IP bans. Inject Gaussian jitter delays and human-like cursor paths.">Agar agent sekundiga 50 ta so'rov bersa, WAF server IP manzilni darhol bloklaydi. Harakatlar orasiga 300-800 ms tabiiy kechikish qo'shiladi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="3. Учетные Данные" data-en="3. Credential Vault">3. Parollar va .env Himoyasi</div>
        <h4 data-ru="Никаких паролей в системном промпте" data-en="No secrets in system prompts">Parollar promptda berilmaydi</h4>
        <p style="font-size:11px;" data-ru="Логины и пароли передаются только через переменные окружения `.env` и подставляются на уровне Playwright API, не попадая в контекст и логирование LLM." data-en="Passwords remain in secure `.env` vaults and inject directly at the Playwright driver layer, completely isolated from LLM context logs.">Parollar hech qachon LLM promptiga yozilmaydi. Ular `.env` fayldan to'g'ridan-to'g'ri Playwright drayveriga kiritiladi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: INTERACTIVE SMARTBOARD DEMO -->
  <section class="slide" data-phase="Jonli Sinov|Живой Тест|Live Test" data-time="45:00–52:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ИНТЕРАКТИВНЫЙ ТРЕНАЖЕР" data-en="INTERACTIVE SIMULATOR">SMARTBOARD BOSHQARUVI</span></div>
    <h2 data-ru="Симуляция Browser-Use: Агент Ищет Ноутбук в Магазине" data-en="Browser-Use Live Simulation: Agent Searching Laptops">Browser-Use Jonli Simulyatori: Magazinda Mahsulot Qidirish</h2>
    <div style="background:var(--surface); border:1px solid var(--hair); border-radius:8px; padding:12px; margin-top:8px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <div>
          <span style="font-size:11px; font-weight:700; color:var(--accent);" data-ru="СТАТУС АГЕНТА:" data-en="AGENT STATUS:">AGENT HOLATI:</span>
          <span id="demoAgentStatus" style="font-size:12px; font-weight:700; margin-left:6px; color:var(--yellow);" data-ru="Готов к запуску" data-en="Ready to launch">Boshlashga tayyor</span>
        </div>
        <div style="font-size:11px; color:var(--ink-2);">
          <span data-ru="Токены DOM:" data-en="DOM Tokens:">DOM Tokenlari:</span> <strong id="demoTokens" style="color:var(--ink);">0</strong>
          <span style="margin-left:12px;" data-ru="Шаг:" data-en="Step:">Qadam:</span> <strong id="demoStep" style="color:var(--ink);">0 / 4</strong>
        </div>
      </div>
      <!-- Mini Browser Window Representation -->
      <div style="display:grid; grid-template-columns:1.2fr 1fr; gap:12px;">
        <div style="background:#0f172a; border-radius:6px; padding:10px; border:1px solid #334155; font-family:monospace; font-size:11px;">
          <div style="display:flex; gap:6px; margin-bottom:8px; border-bottom:1px solid #1e293b; padding-bottom:6px;">
            <div style="width:8px; height:8px; border-radius:50%; background:#ef4444;"></div>
            <div style="width:8px; height:8px; border-radius:50%; background:#eab308;"></div>
            <div style="width:8px; height:8px; border-radius:50%; background:#22c55e;"></div>
            <span style="color:#94a3b8; font-size:10px; margin-left:6px;">https://tech-store.uz/catalog</span>
          </div>
          <div id="mockBrowserContent" style="min-height:130px; color:#cbd5e1; font-size:11px; line-height:1.5;">
            <div id="mockBanner" style="background:#ef4444; color:#fff; padding:6px; border-radius:4px; margin-bottom:8px; display:flex; justify-content:space-between;">
              <span data-ru="🔥 Скидка 50% Реклама!" data-en="🔥 50% Discount Promo!">🔥 50% Chegirma Reklamasi!</span>
              <button onclick="dismissMockBanner()" style="background:#000; color:#fff; border:none; padding:1px 6px; border-radius:3px; cursor:pointer;" data-ru="[1] ✕ Закрыть" data-en="[1] ✕ Close">[1] ✕ Yopish</button>
            </div>
            <div style="display:flex; gap:6px; margin-bottom:8px;">
              <input id="mockInput" type="text" placeholder="[2] Qidirish..." data-placeholder-ru="[2] Поиск..." data-placeholder-en="[2] Search..." style="flex:1; background:#1e293b; border:1px solid #475569; color:#fff; padding:4px 8px; border-radius:4px; font-size:11px;" />
              <button id="mockSearchBtn" style="background:var(--accent); color:#fff; border:none; padding:4px 10px; border-radius:4px; cursor:pointer;" data-ru="[3] Поиск" data-en="[3] Search">[3] Qidiruv</button>
            </div>
            <div id="mockResults" style="color:#64748b; font-size:10px;" data-ru="Результатов поиска нет..." data-en="No search results yet...">Qidiruv natijalari yo‘q...</div>
          </div>
        </div>
        <div style="background:#0b1120; border-radius:6px; padding:10px; border:1px solid #1e293b; font-family:monospace; font-size:10px; max-height:180px; overflow-y:auto;">
          <div style="color:#38bdf8; font-weight:700; margin-bottom:4px;">🤖 Agent Fikrlash Logi (Telemetry):</div>
          <div id="demoLog" style="color:#94a3b8; line-height:1.4;">[00.00s] Kutilmoqda. "▶️ Veb-Agentni Ishga Tushirish" tugmasini bosing...</div>
        </div>
      </div>
      <div style="margin-top:10px; display:flex; gap:8px;">
        <button id="btnRunWebAgent" onclick="runWebAgentDemo()" class="btn-primary" style="padding:6px 14px; font-size:12px; cursor:pointer;" data-ru="▶️ Запустить Веб-Агента" data-en="▶️ Run Web Agent">▶️ Veb-Agentni Ishga Tushirish</button>
        <button onclick="resetWebAgentDemo()" style="background:var(--surface-2); border:1px solid var(--hair); color:var(--ink); padding:6px 12px; font-size:12px; border-radius:4px; cursor:pointer;" data-ru="Сброс" data-en="Reset">Qayta o'rnatish</button>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: QUIZ -->
  <section class="slide" data-phase="Viktorina|Викторина|Quiz" data-time="52:00–58:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА ЗНАНИЙ" data-en="KNOWLEDGE CHECK">BILIMNI TEKSHIRISH</span></div>
    <h2 data-ru="Экспресс-Тест: Архитектура Веб-Агентов и Токены" data-en="Quick Quiz: Web Agent Architecture & Tokens">Tezkor Test: Veb-Agentlar Arxitekturasi va Xavfsizlik</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag">Savol 1</div>
        <h4 data-ru="Зачем нужна дистилляция DOM вместо отправки всего HTML?" data-en="Why distill DOM instead of sending full HTML?">Nega butun HTML o'rniga Accessibility Tree yuboriladi?</h4>
        <div style="font-size:11px; margin-top:6px; line-height:1.5;">
          <div>A) Rasmlarni chiroyli qilish</div>
          <div style="color:var(--green); font-weight:700;">B) 95% ortiqcha stillar va skriptlarni qisqartirib tokenni tejash</div>
          <div>C) Internet tezligini oshirish</div>
        </div>
      </div>
      <div class="box">
        <div class="tag">Savol 2</div>
        <h4 data-ru="Что обязан сделать агент при появлении CAPTCHA?" data-en="What must an agent do upon facing a CAPTCHA?">Agent saytda CAPTCHA to'sig'iga duch kelsa nima qilishi shart?</h4>
        <div style="font-size:11px; margin-top:6px; line-height:1.5;">
          <div>A) Tezda 100 ta variantni sinab ko'rish</div>
          <div style="color:var(--green); font-weight:700;">B) Jarayonni to'xtatib, inson yechishi uchun HITL signali berish</div>
          <div>C) Saytni buzib o'tish</div>
        </div>
      </div>
      <div class="box">
        <div class="tag">Savol 3</div>
        <h4 data-ru="Чем отличается Browser-Use от обычного Playwright?" data-en="How does Browser-Use differ from raw Playwright?">Browser-Use oddiy Playwright drayveridan nimasi bilan farq qiladi?</h4>
        <div style="font-size:11px; margin-top:6px; line-height:1.5;">
          <div>A) Faqat Firefox brauzerida ishlaydi</div>
          <div style="color:var(--green); font-weight:700;">B) LLM Vision + Action tsiklini avtomatik boshqaradi</div>
          <div>C) U hech qanday kod talab qilmaydi</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: ARENA LAB -->
  <section class="slide" data-phase="Amaliyot|Практика|Practice" data-time="58:00–72:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="БОЛЬШАЯ ЛАБОРАТОРИЯ · 25 МИНУТ" data-en="GRAND LAB · 25 MINUTES">KATTA LABORATORIYA · 25 DAQIQA</span></div>
    <h2 data-ru="Kiber-Arena: Автономный Скрапинг Цен на Ноутбуки" data-en="Cyber Arena: Autonomous Laptop Price Scraping">Kiber-Arena: Noutbuklar Narxini Avtonom Yig'uvchi Veb-Agent</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Техническое Задание (PRD)" data-en="Technical Task (PRD)">Texnik Topshiriq (PRD)</div>
        <ol style="font-size:12px; line-height:1.7; margin-top:6px;">
          <li data-ru="Откройте студию simulator/index.html." data-en="Open the studio at simulator/index.html."><code>simulator/index.html</code> studiyasini oching.</li>
          <li data-ru="Дайте задание агенту: «Собери 3 самых доступных ноутбука и выведи цены в JSON»." data-en="Assign prompt to agent: 'Extract 3 most affordable laptops and output prices in JSON'.">Agentga topshiriq bering: <em>"TexnoStore-dan 3 ta eng arzon noutbukni top va narxini JSON qilib ber"</em>.</li>
          <li data-ru="Агент обязан закрыть модальный баннер и ввести запрос «Laptop» в поиск." data-en="The agent must close the promotional banner and type 'Laptop' into search.">Agent reklama bannerini yopishi va qidiruvga "Laptop" yozishi shart.</li>
          <li data-ru="Сохраните собранные данные в формате [{&quot;name&quot;: &quot;...&quot;, &quot;price&quot;: &quot;...&quot;}]." data-en="Save extracted datasets in [{&quot;name&quot;: &quot;...&quot;, &quot;price&quot;: &quot;...&quot;}] schema.">To'plangan ma'lumotlarni <code>[{"name": "...", "price": "..."}]</code> shaklida saqlash.</li>
        </ol>
      </div>
      <div class="box" style="border:1px solid var(--accent);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Критерии Успеха (Exit Criteria)" data-en="Exit Criteria">Muvaffaqiyat Mezoni (100%)</div>
        <ul style="font-size:12px; line-height:1.7; margin-top:6px;">
          <li data-ru="✅ Агент не зависает при появлении модальных окон (Self-Healing)." data-en="✅ Agent recovers gracefully from dynamic modal obstructions (Self-Healing).">✅ Banner to'sqinlik qilganda qotib qolmaslik (Self-Healing).</li>
          <li data-ru="✅ Общий расход токенов не превышает 6,000 токенов." data-en="✅ Total token consumption remains strictly under 6,000 tokens.">✅ Jami token sarfi <strong>6,000 tokendan oshmasligi</strong>.</li>
          <li data-ru="✅ Число действий агента строго менее 5 шагов." data-en="✅ Step execution depth stays under 5 discrete actions.">✅ Qadamlar soni <strong>5 ta harakatdan kam</strong> bo'lishi.</li>
          <li data-ru="✅ Результирующий JSON проходит 100% валидацию типов." data-en="✅ Extracted JSON passes 100% schema validation.">✅ Natijaviy JSON 100% to'g'ri validatsiyadan o'tishi.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: PEER-REVIEW -->
  <section class="slide" data-phase="Ko'rik|Ревью|Review" data-time="72:00–76:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМНЫЙ АУДИТ" data-en="PEER REVIEW">JUFTLIKDA O'ZARO AUDIT</span></div>
    <h2 data-ru="Чек-лист Проверки: Защита от Зацикливания и Селекторы" data-en="Review Checklist: Loop Prevention & Resilient Selectors">O'zaro Audit: Cheksiz Sikllar va Selektorlar Mustahkamligi</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag">1. Loop Guard</div>
        <h4 data-ru="Лимит на 10 шагов" data-en="Max 10 steps limit">Maksimal 10 ta qadam</h4>
        <p style="font-size:11px;" data-ru="Убедитесь, что у напарника стоит `max_steps = 10`. Если кнопка не нажимается, агент не должен кликать её 100 раз подряд." data-en="Verify your peer sets `max_steps = 10`. If an element fails to respond, the agent must abort instead of burning 100 retries.">Partadoshingiz kodida `max_steps = 10` borligini tekshiring. Agar tugma bosilmasa, 100 marta qayta bosib token yoqmasin.</p>
      </div>
      <div class="box">
        <div class="tag">2. Dynamic Selectors</div>
        <h4 data-ru="Селекторы без хрупких классов" data-en="No brittle class hashes">Tasodifiy klasslarsiz selektorlar</h4>
        <p style="font-size:11px;" data-ru="Использует ли агент семантические селекторы `button:has-text('Qidiruv')` вместо хрупких хэшей `.btn-v2_7a9x`?" data-en="Does the agent use resilient text selectors instead of ephemeral hashed build classes like `.btn-v2_7a9x`?">Agent `.btn-v2_7a9x` kabi ertaga o'zgarib ketuvchi klasslar o'rniga matnli yoki rol bo'yicha selektor ishlatganmi?</p>
      </div>
      <div class="box">
        <div class="tag">3. Data Validation</div>
        <h4 data-ru="Проверка JSON типов" data-en="JSON Schema validation">JSON turlari aniqligi</h4>
        <p style="font-size:11px;" data-ru="Извлеченные цены приведены к числам `12500000`, а не оставлены строками с пробелами и символами валют." data-en="Are prices converted into integer numbers rather than unparsed strings with currency symbols?">Narxlar bo'sh joyli matn emas, haqiqiy son (`integer`) ko'rinishiga keltirilganmi?</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: RUBRIC -->
  <section class="slide" data-phase="Baholash|Оценка|Rubric" data-time="76:00–78:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="КРИТЕРИИ ОЦЕНИВАНИЯ" data-en="GRADING RUBRIC">10 BALLIK BAHOLASH MEZONI</span></div>
    <h2 data-ru="Рубрика Оценки 30-Урока (10 Баллов)" data-en="Lesson 30 Grading Rubric (10 Points)">30-Dars Bo'yicha 10 Ballik Baholash Rubrikasi</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">4 Ball (Baza)</div>
        <h4 data-ru="DOM Дистилляция и Селекторы" data-en="DOM Distillation & Selectors">DOM Distillyatsiyasi va Selektorlar</h4>
        <p style="font-size:11px;" data-ru="Ученик понимает концепцию Accessibility Tree, умеет изолировать кликабельные элементы и генерировать валидный JSON-экшн." data-en="Student comprehends Accessibility Trees, isolates interactable DOM elements, and formulates valid JSON action payloads.">Accessibility Tree tushunchasini biladi, interaktiv elementlarni ajratadi va to'g'ri JSON harakatini shakllantira oladi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">4 Ball (Amaliy)</div>
        <h4 data-ru="Автономный Цикл и Скрапинг" data-en="Autonomous Loop & Extraction">Avtonom Tsikl va Ma'lumot Chiqarish</h4>
        <p style="font-size:11px;" data-ru="Агент успешно обходит модальное окно, заполняет поле поиска, кликает и извлекает структурированный список товаров." data-en="Agent handles modal obstructions, fills search fields, triggers clicks, and scrapes clean product datasets.">Agent modal oynani chetlab o'tadi, qidiruvni bajaradi, mahsulotlarni filtrlaydi va tartibli ma'lumotlar ro'yxatini chiqaradi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);">2 Ball (Challenge)</div>
        <h4 data-ru="Анти-Бот и HITL Безопасность" data-en="Anti-Bot & HITL Guardrails">Kiber-Himoya va HITL Qalqoni</h4>
        <p style="font-size:11px;" data-ru="Внедрен счетчик шагов (max_steps), обнаружение CAPTCHA с безопасной передачей управления оператору (HITL)." data-en="Configures step guards (max_steps) and graceful CAPTCHA detection pausing for human operator verification.">Qadamlar cheklovi (max_steps), jitter kechikishi va captcha chiqqanda xavfsiz to'xtash mexanizmi sozlangan.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & HOMEWORK -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="78:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="SUMMARY & HOMEWORK">XULOSA VA UY VAZIFASI</span></div>
    <h2 data-ru="Главные Выводы и Домашний Проект" data-en="Key Takeaways & Homework Assignment">Asosiy Xulosalar va 31-Darsga Ko'prik</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Домашнее Задание" data-en="Homework Assignment">Uy Vazifasi (vazifa.html)</div>
        <p style="font-size:12px; line-height:1.6;" data-ru="<strong>1-Уровень (4 б):</strong> Написать спецификацию Accessibility Tree для формы логина.<br><strong>2-Уровень (4 б):</strong> Создать Playwright-скрипт с обходом модального окна и сбором таблицы.<br><strong>3-Уровень (2 б):</strong> Реализовать обнаружение reCAPTCHA и паузу для оператора (HITL)." data-en="<strong>Tier 1 (4 pts):</strong> Write an Accessibility Tree spec for a login gateway.<br><strong>Tier 2 (4 pts):</strong> Code a Playwright script dismissing cookie banners and scraping tables.<br><strong>Tier 3 (2 pts):</strong> Implement CAPTCHA detection triggering human-in-the-loop pause."><strong>1-Daraja (4 b):</strong> Kirish sahifasi uchun Accessibility Tree spetsifikatsiyasini yozish.<br><strong>2-Daraja (4 b):</strong> Playwright orqali pop-up bannerlarni yopib, jadval ma'lumotlarini JSON ga yig'ish.<br><strong>3-Daraja (2 b):</strong> CAPTCHA chiqqanda to'xtab insonga xabar beruvchi HITL tizimini sozlash.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Анонс 31-Урока" data-en="Next Lesson 31">Keyingi Dars (31-Dars)</div>
        <h4 data-ru="Мультимодальные Vision-Агенты и Computer-Use" data-en="Multimodal Vision Agents & Computer-Use">Multi-Modal Vision Agentlar va Computer-Use</h4>
        <p style="font-size:12px;" data-ru="В следующий раз мы сделаем шаг вперед: агент будет управлять не только веб-браузером, но и всей операционной системой (мышь, клавиатура, десктопные приложения)!" data-en="In our next double block, we scale up: our AI agent will control not just web browsers, but full desktop OS environments via Anthropic Computer-Use APIs!">Keyingi juftlik darsimizda agentimiz nafaqat brauzerni, balki butun operatsion tizimni (sichqoncha, klaviatura, grafik dasturlar) boshqarishni o'rganadi!</p>
      </div>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. NOTES DATA (14 Slides Notes)
# -----------------------------------------------------------------------------
NOTES_DATA = {
    "uz": [
        ["Kirish va Dars Maqsadi", "O'quvchilarga bugungi mavzu: Veb-agentlar, headless brauzerlar va Browser-Use arxitekturasi ekanini e'lon qiling.", "Doskaga 1 MB HTML vs 5 KB Accessibility Tree taqqoslashini chizing."],
        ["Uy Vazifasi Tahlili", "29-darsdagi Coder-Critic tizimida bitta test yiqilganda butun faylni qayta yozish xatosini tushuntiring.", "Regressiya xavfi va nuqtali surgical patch tamoyilini takrorlang."],
        ["Arxitektura To'sig'i", "Nega oddiy LLM veb-saytni shunchaki o'qiy olmasligini tushuntiring.", "Tokenlar portlashi, dinamik React DOM va pop-uplar arxitekturasini tahlil qiling."],
        ["Headless Brauzer", "CDP (Chrome DevTools Protocol) orqali Chromium yadrosi bilan to'g'ridan-to'g'ri soket aloqasini ko'rsating.", "Playwright nima uchun Seleniumdan tezroq ekanini doskada ko'rsating."],
        ["DOM Distillyatsiyasi", "HTML-dagi 95% ortiqcha stillar va SVG koordinatalarni tozalashni tushuntiring.", "Faqat interaktiv ID-lar daraxtini hosil qilishni doskaga yozing."],
        ["Vision-Action Tsikli", "Set-of-Mark (SoM) orqali skrinshotga rangli raqamli ramkalar qo'yishni ko'rsating.", "Observe -> Plan -> Act tsiklini o'quvchilar bilan tahlil qiling."],
        ["Action Schema", "Agent faqat qat'iy JSON formatida javob berishini tushuntiring.", "Click, type, scroll, wait, finish buyruqlarini slayd orqali ko'rsating."],
        ["Kiberxavfsizlik Qoidalari", "CAPTCHA qoidasini qat'iy eslatib o'ting: Hech qachon avtomat buzilmaydi, faqat HITL ishlatiladi.", "WAF bloklaridan qochish uchun 300-800ms jitter qo'shish zaruratini tushuntiring."],
        ["Smartboard Simulyatsiyasi", "Doskadagi simulyatorda agentning reklama bannerini yopib, qidiruv berishini ko'rsating.", "O'quvchilarni ekranga chiqarib harakatlar ketma-ketligini kuzatishni buyuring."],
        ["Viktorina", "3 ta tezkor savol orqali butun sinfni uyg'oting.", "Faol javob bergan o'quvchilarga rag'bat ballari bering."],
        ["Katta Kiber-Arena", "25 daqiqalik amaliy arenani boshlang.", "O'quvchilar simulator/index.html da o'z veb-agentlarini sinashlarini nazorat qiling."],
        ["O'zaro Audit", "Partadoshlar bir-birining tizimiga cheksiz sikllar himoyasi qo'yilganini tekshiradilar.", "Juftliklarni almashtirib audit varaqasini to'ldirishni buyuring."],
        ["Baholash Rubrikasi", "10 ballik mezonni eslatib o'ting: 4 ball baza, 4 ball amaliyot, 2 ball kiber-himoya.", "O'quvchilar ballarini daftarga yozishlarini ta'minlang."],
        ["Xulosa va Keyingi Dars", "Darsni yakunlang va uy vazifasini belgilang.", "Keyingi Computer-Use mavzusiga qiziqish uyg'oting."]
    ],
    "ru": [
        ["Введение и Цель", "Объявите тему: автономные веб-агенты, headless браузеры и архитектура Browser-Use.", "Нарисуйте на доске сравнение 1 МБ HTML против 5 КБ Accessibility Tree."],
        ["Разбор ДЗ 29", "Разберите типичную ошибку: переписывание файла с нуля при падении одного теста.", "Напомните про регрессию и хирургические патчи."],
        ["Архитектурный Барьер", "Объясните, почему сырой HTML переполняет контекстное окно LLM.", "Разберите динамический рендеринг SPA и WebSockets."],
        ["Headless Браузер", "Расскажите про CDP сокет и преимущества асинхронного Playwright.", "Покажите разницу в скорости между Selenium и Playwright."],
        ["Дистилляция DOM", "Покажите, как из 20,000 строк извлекаются только интерактивные ноды.", "Напишите на доске схему древовидной структуры элементов."],
        ["Цикл Vision-Action", "Объясните технику Set-of-Mark и сопоставление визуальных рамок с DOM.", "Разберите три фазы: наблюдение, планирование и действие."],
        ["Схема Действий", "Разберите JSON команды: click, type, scroll, extract, finish.", "Покажите пример строгого ответа модели на слайде."],
        ["Кибербезопасность", "Строго напомните правило CAPTCHA: не взламывать, а вызывать человека (HITL).", "Объясните использование джиттера 300–800 мс против банов WAF."],
        ["Смартборд Демо", "Запустите интерактивную симуляцию агента на смартборде.", "Пригласите ученика протестировать закрытие модального окна."],
        ["Викторина", "Проведите экспресс-тест по 3 ключевым вопросам.", "Оцените активность класса и начислите баллы."],
        ["Большая Лаборатория", "Запустите 25-минутную практику в симуляторе.", "Помогайте ученикам настраивать селекторы цен на ноутбуки."],
        ["Взаимный Аудит", "Проконтролируйте проверку max_steps = 10 между соседями.", "Организуйте обмен экранами для поиска скрытых багов."],
        ["Критерии Оценки", "Напомните 10-балльную рубрику: база, практика, челлендж.", "Зафиксируйте предварительные оценки в журнале."],
        ["Итоги Урока", "Подведите итоги и выдайте домашнее задание.", "Анонсируйте тему Computer-Use на следующий урок."]
    ],
    "en": [
        ["Intro & Objectives", "Introduce Web Agents, headless automation, and Browser-Use architecture.", "Draw the 1MB HTML vs 5KB Accessibility Tree comparison on the board."],
        ["Lesson 29 Review", "Analyze the pitfall of full-file rewriting upon single assertion failure.", "Reinforce regression hazards and surgical diff patching."],
        ["Architectural Barrier", "Explain why raw HTML floods LLM context windows with noise.", "Analyze dynamic client-side hydration and SPA rendering bottlenecks."],
        ["Headless Browsers", "Highlight CDP sockets and Playwright async execution pipelines.", "Compare legacy Selenium performance against modern Playwright loops."],
        ["DOM Distillation", "Show how Accessibility Trees isolate only clickable nodes.", "Draft the distilled interactables list on the board."],
        ["Vision-Action Loop", "Explain Set-of-Mark prompting connecting vision boxes with DOM indices.", "Review the Observe -> Plan -> Act continuous cycle."],
        ["Action Schema", "Walk through structured JSON actions: click, type, scroll, finish.", "Examine typed parameter validation on the display."],
        ["Cybersecurity", "Enforce the CAPTCHA rule: never bypass, always trigger HITL.", "Demonstrate Gaussian delay jitter to avoid automated WAF mitigation."],
        ["Smartboard Demo", "Run the live agent search simulation on the interactive board.", "Have a student trigger the autonomous modal bypass live."],
        ["Knowledge Check", "Execute the 3-question rapid quiz.", "Engage the room and award bonus participation marks."],
        ["Grand Cyber Arena", "Commence the 25-minute hands-on lab in simulator/index.html.", "Guide students as they configure laptop price extraction pipelines."],
        ["Peer Review", "Ensure students audit each other's max_steps loop guards.", "Facilitate peer exchanges and validation of JSON outputs."],
        ["Grading Rubric", "Summarize the 10-point evaluation criteria across all tiers.", "Have students log their score targets in workbooks."],
        ["Summary & Next", "Wrap up the session and assign the 3-tier homework.", "Tease desktop Computer-Use for the upcoming lesson."]
    ]
}

# -----------------------------------------------------------------------------
# 3. INTERACTIVE SIMULATOR SCRIPT FOR PRESENTATION
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
var isRunningDemo = false;
function dismissMockBanner() {
  var b = document.getElementById('mockBanner');
  if (b) {
    b.style.display = 'none';
    var log = document.getElementById('demoLog');
    if (log) log.innerHTML += '<div style="color:#22c55e;">[Manual]: Reklama banneri yopildi.</div>';
  }
}

function runWebAgentDemo() {
  if (isRunningDemo) return;
  isRunningDemo = true;
  var btn = document.getElementById('btnRunWebAgent');
  if (btn) btn.disabled = true;

  var statusEl = document.getElementById('demoAgentStatus');
  var tokensEl = document.getElementById('demoTokens');
  var stepEl = document.getElementById('demoStep');
  var logEl = document.getElementById('demoLog');
  var inputEl = document.getElementById('mockInput');
  var resEl = document.getElementById('mockResults');

  logEl.innerHTML = '<div style="color:#38bdf8;">[00.01s] 🌐 Agent https://tech-store.uz sahifasini ochdi.</div>';
  statusEl.textContent = 'DOM Tahlili...';
  statusEl.style.color = 'var(--accent)';
  tokensEl.textContent = '840';
  stepEl.textContent = '1 / 4';

  setTimeout(function() {
    logEl.innerHTML += '<div style="color:#eab308;">[00.80s] ⚠️ Diqqat: [1] Reklama banneri qidiruv maydonini to‘smoqda.</div>';
    logEl.innerHTML += '<div style="color:#a855f7;">[01.10s] 🤖 Reja: {"action": "click", "index": 1, "target": "Yopish tugmasi"}</div>';
    statusEl.textContent = 'Banner Yopilmoqda...';
    stepEl.textContent = '2 / 4';
    tokensEl.textContent = '1,420';

    setTimeout(function() {
      var b = document.getElementById('mockBanner');
      if (b) b.style.display = 'none';
      logEl.innerHTML += '<div style="color:#22c55e;">[01.70s] ✅ Banner yopildi. DOM yangilandi.</div>';
      statusEl.textContent = 'Qidiruv Kiritilmoqda...';
      stepEl.textContent = '3 / 4';
      tokensEl.textContent = '2,150';

      setTimeout(function() {
        if (inputEl) inputEl.value = 'MacBook M3';
        logEl.innerHTML += '<div style="color:#a855f7;">[02.40s] 🤖 Reja: {"action": "type", "index": 2, "text": "MacBook M3"}</div>';
        logEl.innerHTML += '<div style="color:#a855f7;">[02.80s] 🤖 Reja: {"action": "click", "index": 3, "target": "Qidiruv tugmasi"}</div>';

        setTimeout(function() {
          if (resEl) {
            resEl.innerHTML = '<div style="color:#22c55e; font-weight:700; margin-top:4px;">Topilgan Mahsulotlar (JSON):</div>' +
              '<div style="background:#1e293b; padding:4px 6px; border-radius:4px; margin-top:2px; font-size:9px; color:#38bdf8;">' +
              '[{"title": "MacBook Pro M3 14\\"", "price": "17 200 000 so‘m", "stock": 4},<br>' +
              '{"title": "MacBook Air M3 13\\"", "price": "13 500 000 so‘m", "stock": 9}]</div>';
          }
          logEl.innerHTML += '<div style="color:#22c55e; font-weight:700;">[03.50s] 🎉 Missiya Yakunlandi! 2 ta mahsulot muvaffaqiyatli JSON ga olindi.</div>';
          statusEl.textContent = '✅ Muvaffaqiyat (Yakunlandi)';
          statusEl.style.color = 'var(--green)';
          stepEl.textContent = '4 / 4';
          tokensEl.textContent = '2,980';
          isRunningDemo = false;
          if (btn) btn.disabled = false;
        }, 1000);

      }, 1000);

    }, 1000);

  }, 1000);
}

function resetWebAgentDemo() {
  isRunningDemo = false;
  var b = document.getElementById('mockBanner');
  if (b) b.style.display = 'flex';
  var inputEl = document.getElementById('mockInput');
  if (inputEl) inputEl.value = '';
  var resEl = document.getElementById('mockResults');
  if (resEl) resEl.innerHTML = 'Qidiruv natijalari yo‘q...';
  var statusEl = document.getElementById('demoAgentStatus');
  if (statusEl) {
    statusEl.textContent = 'Boshlashga tayyor';
    statusEl.style.color = 'var(--yellow)';
  }
  var tokensEl = document.getElementById('demoTokens');
  if (tokensEl) tokensEl.textContent = '0';
  var stepEl = document.getElementById('demoStep');
  if (stepEl) stepEl.textContent = '0 / 4';
  var logEl = document.getElementById('demoLog');
  if (logEl) logEl.innerHTML = '[00.00s] Kutilmoqda. "▶️ Veb-Agentni Ishga Tushirish" tugmasini bosing...';
  var btn = document.getElementById('btnRunWebAgent');
  if (btn) btn.disabled = false;
}
"""

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "30-dars: Agentik Veb-Brauzing va Headless Avtomatlashtirish"
    title_ru = "Урок 30: Агентный Веб-Браузинг и Headless Автоматизация"
    title_en = "Lesson 30: Autonomous Web Browsing & Headless Automation"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="10–11 КЛАСС" data-en="GRADES 10–11">10–11-SINF</span>',
                 tpl)

    titles_json = json.dumps({"uz": title_uz, "ru": title_ru, "en": title_en}, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    stage_regex = r'<div class="stage">[\s\S]*?</div><!-- /stage -->'
    new_stage = f'<div class="stage">\n{SLIDES_HTML}\n  </div><!-- /stage -->'
    tpl = re.sub(stage_regex, new_stage, tpl)

    custom_script = f"<script>\n{SIMULATOR_JS}\n</script>\n</body>"
    tpl = tpl.replace("</body>", custom_script)

    out_path = os.path.join(DEST_DIR, "prezentatsiya.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

def build_worksheet():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "30-dars: Agentik Veb-Brauzing va Headless Avtomatlashtirish"
    title_ru = "Урок 30: Агентный Веб-Браузинг и Headless Автоматизация"
    title_en = "Lesson 30: Autonomous Web Browsing & Headless Automation"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<h1>.*?</h1>',
                 f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>',
                 tpl)

    sec1_html = """
    <p class="lead" style="font-size:12px; margin-bottom:8px;" data-ru="<strong>Миссия Урока:</strong> Спроектировать архитектуру автономного веб-агента на базе Playwright и Browser-Use, преобразующего тяжелый HTML (1 МБ) в компактное Accessibility Tree (5 КБ), способного закрывать модальные окна, заполнять формы и извлекать структурированные JSON-данные." data-en="<strong>Lesson Mission:</strong> Architect an autonomous web agent using Playwright and Browser-Use that distills 1MB messy DOM trees into 5KB Accessibility Trees, handles dynamic modals, and extracts clean structured JSON datasets."><strong>Dars Missiyasi:</strong> Playwright va Browser-Use yordamida 1 MB HTML-ni 5 KB Accessibility Tree ga aylantiruvchi, modal bannerlarni yopib, qidiruv beruvchi va natijalarni JSON ga yig'uvchi avtonom veb-agentni yaratish.</p>
    <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="3 Фазы Работы Веб-Агента:" data-en="3 Phases of Web Agent Execution:">Veb-Agent Ishining 3 Bosqichi:</div>
      <div>1. <strong>Observe (Kuzatish):</strong> <span data-ru="CDP делает снимок DOM, удаляет inline-стили и оставляет кликабельные элементы с номерами [SoM]." data-en="CDP captures DOM snapshots, strips styling bloat, and assigns indexed labels to interactables.">CDP orqali DOM olinadi, stillar tashlanib, faqat raqamlangan interaktiv elementlar daraxti tuziladi</span>.</div>
      <div>2. <strong>Plan (Fikrlash):</strong> <span data-ru="LLM сравнивает цель пользователя с элементами на экране и формирует типизированный JSON-экшн." data-en="LLM evaluates user intent against interactive nodes and produces typed action schemas.">LLM maqsadni ekrandagi tugmalar bilan taqqoslab, navbatdagi JSON harakatini rejalashtiradi</span>.</div>
      <div>3. <strong>Act (Bajarish):</strong> <span data-ru="Playwright эмулирует аппаратный клик/ввод текста и ожидает завершения AJAX-запросов." data-en="Playwright executes hardware-level events and pauses for network/DOM idle state.">Playwright apparat darajasida klik/yozishni bajaradi va AJAX yangilanishini kutadi</span>.</div>
    </div>
    """

    sec2_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="Спецификация типизированного JSON-ответа веб-агента:" data-en="Typed JSON action specification of the web agent:">Veb-agentning qat'iy JSON harakatlar kodi:</p>
    <pre style="background:var(--surface-2); padding:6px; font-size:11px; border-radius:4px; margin:0;"><code class="language-json">{
  "thought": "Banner qidiruvni to'smoqda. [1] '✕ Yopish' tugmasini bosamiz.",
  "action": {
    "name": "click",
    "params": { "index": 1 }
  },
  "max_steps": 10,
  "anti_bot": { "captcha_detected": false, "delay_ms": 450 }
}</code></pre>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Фаза Агента" data-en="Agent Phase">Agent Bosqichi</th>
            <th style="padding:4px 6px;" data-ru="Входные Данные" data-en="Input Data">Kiruvchi Ma'lumot</th>
            <th style="padding:4px 6px;" data-ru="Выходной Артефакт" data-en="Output Artifact">Natijaviy Hujjat</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="DOM Pruning" data-en="DOM Pruning">DOM Distillyatsiyasi</td>
            <td style="padding:4px 6px;">1.2 MB Xom HTML</td>
            <td style="padding:4px 6px;">4.8 KB Accessibility Tree</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ Bajarildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="Banner Bypass" data-en="Banner Bypass">Modal To'siqni Yopish</td>
            <td style="padding:4px 6px;">ID: [1] Modal ✕</td>
            <td style="padding:4px 6px;">click(1) hodisasi</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ Bajarildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="Search & Filter" data-en="Search & Filter">Qidiruv va Filtrlash</td>
            <td style="padding:4px 6px;">"Laptop M3" matni</td>
            <td style="padding:4px 6px;">type(2) + click(3)</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ Bajarildi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="JSON Extract" data-en="JSON Extract">Jadval Scraping</td>
            <td style="padding:4px 6px;">Natijalar konteyneri</td>
            <td style="padding:4px 6px;">products.json fayli</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ 100% Yashil</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    replacements = {
        "{{LESSON_NUM}}": "30",
        "{{LESSON_TITLE_UZ}}": "Agentik Veb-Brauzing va Headless Avtomatlashtirish",
        "{{LESSON_TITLE_RU}}": "Агентный Веб-Браузинг и Headless Автоматизация",
        "{{LESSON_TITLE_EN}}": "Autonomous Web Browsing & Headless Automation",
        "{{COHORT_LABEL_UZ}}": "10–11-sinf",
        "{{COHORT_LABEL_RU}}": "10–11 класс",
        "{{COHORT_LABEL_EN}}": "Grade 10–11",
        "{{TRACK_NAME_UZ}}": "Senior AI & Enterprise Cybersecurity Track",
        "{{TRACK_NAME_RU}}": "Senior AI & Enterprise Кибербезопасность",
        "{{TRACK_NAME_EN}}": "Senior AI & Enterprise Cybersecurity Track",
        "{{SECTION_1_CONTENT}}": sec1_html,
        "{{SECTION_2_CONTENT}}": sec2_html,
        "{{SECTION_3_CONTENT}}": sec3_html,
        "{{RUBRIC_T1_BALL}}": "4",
        "{{RUBRIC_T1_UZ}}": "1-Daraja: Baza (DOM Distillyatsiyasi va Accessibility Tree)",
        "{{RUBRIC_T1_RU}}": "Уровень 1: База (DOM Дистилляция и Accessibility Tree)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (DOM Distillation & Accessibility Tree)",
        "{{RUBRIC_T2_BALL}}": "4",
        "{{RUBRIC_T2_UZ}}": "2-Daraja: Amaliyot (Modal to'siqni yechish va JSON jadval scraping)",
        "{{RUBRIC_T2_RU}}": "Уровень 2: Практика (Обход модальных окон и сбор JSON)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Modal bypass & clean JSON extraction)",
        "{{RUBRIC_T3_BALL}}": "2",
        "{{RUBRIC_T3_UZ}}": "3-Daraja: Challenge (max_steps cheklovi va CAPTCHA HITL to'xtatuvchisi)",
        "{{RUBRIC_T3_RU}}": "Уровень 3: Челлендж (max_steps лимит и HITL пауза при CAPTCHA)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (max_steps guard & HITL pause on CAPTCHA)"
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "varaqa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: varaqa.html")

def build_homework():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "30-dars: Agentik Veb-Brauzing va Headless Avtomatlashtirish"
    title_ru = "Урок 30: Агентный Веб-Браузинг и Headless Автоматизация"
    title_en = "Lesson 30: Autonomous Web Browsing & Headless Automation"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tasks_html = """
    <!-- TIER 1 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1-Daraja (Baza — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Спецификация Accessibility Tree" data-en="Accessibility Tree Specification">Accessibility Tree Spetsifikatsiyasi</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите Python функцию parse_accessibility_tree(html_snippet: str) -> list[dict], которая отфильтровывает все теги script, style, svg и возвращает список интерактивных элементов: id, tag, text, selector." data-en="Write a Python function parse_accessibility_tree(html_snippet: str) -> list[dict] stripping script, style, and svg tags, returning only interactable elements: id, tag, text, and selector.">Berilgan HTML parchadan barcha script, style va svg teglarni olib tashlab, faqat interaktiv elementlarni (id, tag, text, selector) qaytaruvchi funksiyani yozing.</p>
      <textarea id="hw_code_t1" class="code-editor" style="width:100%; min-height:90px; background:#0f172a; color:#f8fafc; font-family:monospace; font-size:11px; padding:8px; border-radius:4px; border:1px solid #334155;"># 1-Daraja yechimingizni shu yerga yozing
def parse_accessibility_tree(html_snippet: str) -> list:
    import re
    # Tozalash va interaktiv elementlarni ajratish
    pass
</textarea>
    </div>

    <!-- TIER 2 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">2-Daraja (Amaliyot — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Playwright Action Executor" data-en="Playwright Action Executor">Playwright Harakatlar Bajaruvchisi</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Создайте асинхронный цикл execute_actions(page, action_list), который последовательно выполняет действия click, type и scroll. Если селектор не найден в течение 2 секунд, код не падает, а делает retry с запасным селектором." data-en="Create an async function execute_actions(page, action_list) that dispatches click, type, and scroll commands with a 2-second timeout and fallback selector retry.">Berilgan buyruqlar ro'yxatini (click, type, scroll) navbatma-navbat bajaruvchi asinxron funksiya yozing. Agar element 2 soniyada topilmasa, zaxira selektor bilan qayta urinish (fallback retry) qilsin.</p>
      <textarea id="hw_code_t2" class="code-editor" style="width:100%; min-height:100px; background:#0f172a; color:#f8fafc; font-family:monospace; font-size:11px; padding:8px; border-radius:4px; border:1px solid #334155;"># 2-Daraja yechimingizni shu yerga yozing
async def execute_actions(page, action_list: list):
    for act in action_list:
        # Kodni yozing
        pass
</textarea>
    </div>

    <!-- TIER 3 (2 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);">3-Daraja (Kiber-Challenge — 2 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="HITL Защитник при CAPTCHA" data-en="HITL Guard for CAPTCHA Detection">CAPTCHA Chiqqanda HITL Xavfsiz To'xtatuvchi</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Реализуйте проверку detect_captcha_and_pause(page). Если на странице найдены фреймы hCaptcha, reCAPTCHA или Cloudflare challenge, скрипт издает звуковой сигнал, выводит сообщение оператору и ждет ручного клика человека в окне браузера." data-en="Implement detect_captcha_and_pause(page). If Cloudflare Turnstile or reCAPTCHA iframes appear, the agent halts automation, emits an alert, and pauses for human-in-the-loop completion.">Sahifada Cloudflare yoki reCAPTCHA ramkasi paydo bo'lsa, avtomatlashtirishni to'xtatib, operatorga signal beruvchi va inson qo'lda yechishini kutuvchi HITL moduli kodini yozing.</p>
      <textarea id="hw_code_t3" class="code-editor" style="width:100%; min-height:90px; background:#0f172a; color:#f8fafc; font-family:monospace; font-size:11px; padding:8px; border-radius:4px; border:1px solid #334155;"># 3-Daraja yechimingizni shu yerga yozing
async def detect_captcha_and_pause(page):
    # CAPTCHA detektori va HITL kutish kodi
    pass
</textarea>
    </div>
    """

    replacements = {
        "{{LESSON_NUM}}": "30",
        "{{LESSON_TITLE_UZ}}": "Agentik Veb-Brauzing va Headless Avtomatlashtirish",
        "{{LESSON_TITLE_RU}}": "Агентный Веб-Браузинг и Headless Автоматизация",
        "{{LESSON_TITLE_EN}}": "Autonomous Web Browsing & Headless Automation",
        "{{COHORT_LABEL_UZ}}": "10–11-sinf",
        "{{COHORT_LABEL_RU}}": "10–11 класс",
        "{{COHORT_LABEL_EN}}": "Grade 10–11",
        "{{RUBRIC_T1_BALL}}": "4",
        "{{RUBRIC_T1_UZ}}": "1-Daraja: Baza (Accessibility Tree spetsifikatsiyasi)",
        "{{RUBRIC_T1_RU}}": "Уровень 1: База (Спецификация Accessibility Tree)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (Accessibility Tree parser spec)",
        "{{RUBRIC_T2_BALL}}": "4",
        "{{RUBRIC_T2_UZ}}": "2-Daraja: Amaliyot (Playwright action executor va fallback)",
        "{{RUBRIC_T2_RU}}": "Уровень 2: Практика (Playwright action executor и fallback)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Playwright action executor & retry)",
        "{{RUBRIC_T3_BALL}}": "2",
        "{{RUBRIC_T3_UZ}}": "3-Daraja: Challenge (CAPTCHA aniqlash va HITL xavfsiz to'xtatish)",
        "{{RUBRIC_T3_RU}}": "Уровень 3: Челлендж (Обнаружение CAPTCHA и HITL пауза)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (CAPTCHA detection & HITL pause)",
        "{{TASKS_HTML}}": tasks_html,
        "{{LESSON_SLUG}}": "10-11-w12-l30-agentik-veb-brauzing-va-avtomatlashtirish"
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    doc = """# 30-dars: Agentik Veb-Brauzing va Headless Avtomatlashtirish (O'qituvchi Metodologiyasi)

## Darsning Pasporti
- **Sinf:** 10–11-sinf (Senior AI & Enterprise Cybersecurity Track)
- **Davomiyligi:** 80 daqiqa (Juftlik Dars / Double Block)
- **Asosiy maqsad:** O'quvchilarga AI agentlarni faqat qat'iy API-lar bilan cheklamay, ochiq internetda inson kabi harakatlanuvchi avtonom brauzer tizimlarini (Browser-Use, Stagehand, Playwright) loyihalashni o'rgatish. 1 MB xom HTML-ni 5 KB Accessibility Tree-ga qisqartirish, Set-of-Mark (SoM) orqali vizual elementlarni aniqlash va modal bannerlarni chetlab o'tuvchi chidamli veb-agentlarni dasturlash.

---

## 80 Daqiqalik Aniq Vaqt Taqsimoti (Pacing)

### 1-Qism: Nazariya, Xatolar Tahlili va Jonli Test (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Motivatsiya | 1 | Veb-agentlar nega 2026-yilda AI sohasining eng talabgir yo'nalishi ekanini tushuntirish. | Diqqat bilan tinglaydilar va dars maqsadini belgilaydilar. |
| **04:00–12:00** | 29-dars HW Tahlili | 2 | Coder-Critic tizimida bitta test yiqilganda butun modulni noldan yozish xatosi (regressiya) tahlili. | Blitz savolga javob beradilar, surgical diff qoidasini yozib oladilar. |
| **12:00–18:00** | Arxitektura To'sig'i | 3 | Nega oddiy curl/requests yoki LLM xom HTML-ni o'qiy olmasligini ko'rsatish (tokenlar portlashi, dinamik DOM). | Real veb-sahifa og'irligini tushunadilar. |
| **18:00–24:00** | Headless Brauzer | 4 | CDP (Chrome DevTools Protocol) soket mexanizmi va Playwright arxitekturasini tushuntirish. | Selenium bilan farqini ko'rib chiqadilar. |
| **24:00–30:00** | DOM Distillyatsiyasi | 5 | 1 MB HTML dan 95% stillarni tozalab, Accessibility Tree (5 KB) yasash tamoyili. | Tokenlarni 98% tejash sirini o'rganadilar. |
| **30:00–35:00** | Vision-Action Tsikli | 6 | Set-of-Mark (SoM) raqamlangan ramkalar va multimodal ko'rish modelining ishlash tartibi. | Observe -> Plan -> Act zanjirini o'rganadilar. |
| **35:00–40:00** | Kiber-Himoya & Anti-Bot | 7–8 | CAPTCHA paydo bo'lganda HITL (Human-in-the-Loop) qoidasi va WAF banlaridan himoya (jitter). | Xavfsizlik chegaralarini yozib oladilar. |

### 2-Qism: Smartboard Sinovi, Katta Arena va Showcase (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **40:00–48:00** | Smartboard Simulyatori | 9 | Slayddagi Browser-Use simulyatorini ishga tushirish (Reklama bannerini yopish, qidiruv berish). | Agent qanday qilib modal oynani yopganini kuzatadilar. |
| **48:00–55:00** | Viktorina (Quiz) | 10 | 3 ta nazorat savoli bo'yicha tezkor viktorina o'tkazish. | Faol javob beradilar va o'z bilimlarini tekshiradilar. |
| **55:00–70:00** | 25 Daqiqalik Arena | 11 | 25:00 taymerni yoqish, partalar bo'ylab yurib ko'maklashish. | simulator/index.html da noutbuk narxlarini yig'uvchi agentni dasturlaydilar. |
| **70:00–74:00** | Partadosh Auditi | 12 | O'rin almashishni e'lon qilish, max_steps va selektorlar mustahkamligini tekshirish. | Bir-birining agentiga modal to'siq qo'yib, chidamliligini sinaydilar. |
| **74:00–77:00** | Katta Ekran Showcasi | 13 | Eng kam token sarflagan veb-agentni katta ekranga chiqarib ko'rsatish. | Sinfdoshlari natijasini tahlil qiladilar. |
| **77:00–80:00** | Uy Vazifasi va Yakun | 14 | 10 ballik uy vazifasini tushuntirish va Computer-Use mavzusiga ko'prik! | Kundaliklariga vazifani belgilaydilar. |

---

## O'qituvchi Uchun Muhim Blitz Savollari
1. **"Nega veb-agent uchun xom HTML yuborish falokatli hisoblanadi?"**
   - Javob: Chunki zamonaviy sahifada 1 MB dan ortiq Tailwind klasslari, SVG koordinatalar va bo'sh divlar bor. Bu butun kontekst oynasini to'ldirib, bir urinishdayoq 30,000 tokenni yoqib yuboradi.
2. **"Agar agent saytda Cloudflare CAPTCHA ga duch kelsa, qanday yo'l tutishi shart?"**
   - Javob: Hech qachon avtomat yechishga urinmasligi kerak. Jarayonni muzlatib, insonga (HITL) signal berishi va inson real oynada klik qilgach davom etishi shart.

---

## 10 Ballik Baholash Rubrikasi
- **4 Ball (Baza):** Accessibility Tree tuzilmasini tushunadi va interaktiv elementlar ro'yxatini to'g'ri filtrlaydi.
- **4 Ball (Amaliy):** Agent reklama bannerini yopib, qidiruv beradi va jadval ma'lumotlarini JSON formatida ajratadi.
- **2 Ball (Challenge):** max_steps=10 cheklovi, tabiiy jitter kechikishi va CAPTCHA chiqqanda HITL signali qo'shilgan!
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("  ✓ Created: TEACHER_READING.md")

def build_simulator():
    html = """<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title data-ru="Студия Browser-Use AI: Автономный Веб-Агент" data-en="Browser-Use AI Studio: Autonomous Web Agent">Browser-Use AI Studiyasi: Avtonom Veb-Agent</title>
<link rel="stylesheet" href="../../../../assets/brand.css">
<style>
:root {
  --bg-dark: #090d16;
  --surface-panel: #111827;
  --surface-border: #1f2937;
  --accent-cyan: #06b6d4;
  --accent-purple: #a855f7;
  --accent-green: #10b981;
}
body {
  margin: 0;
  padding: 0;
  background: var(--bg-dark);
  color: #f8fafc;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  height: 100vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
header {
  background: var(--surface-panel);
  border-bottom: 1px solid var(--surface-border);
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.brand-title {
  font-weight: 700;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.badge-tech {
  background: rgba(6,182,212,0.15);
  color: var(--accent-cyan);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-family: monospace;
}
.main-grid {
  flex: 1;
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 12px;
  padding: 12px;
  overflow: hidden;
}
.panel {
  background: var(--surface-panel);
  border: 1px solid var(--surface-border);
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.panel-header {
  background: rgba(0,0,0,0.25);
  border-bottom: 1px solid var(--surface-border);
  padding: 8px 14px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.browser-viewport {
  flex: 1;
  background: #0f172a;
  padding: 12px;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  position: relative;
}
.mock-toolbar {
  background: #1e293b;
  border-radius: 6px;
  padding: 6px 10px;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
  font-family: monospace;
  font-size: 11px;
}
.mock-dots {
  display: flex;
  gap: 4px;
}
.mock-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}
.mock-url {
  flex: 1;
  background: #0f172a;
  padding: 3px 8px;
  border-radius: 4px;
  color: #94a3b8;
  border: 1px solid #334155;
}
.product-card {
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 6px;
  padding: 10px;
  margin-bottom: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.2s;
}
.product-card.highlight {
  border-color: var(--accent-cyan);
  box-shadow: 0 0 10px rgba(6,182,212,0.3);
}
.agent-console {
  flex: 1;
  background: #050811;
  padding: 12px;
  font-family: monospace;
  font-size: 11px;
  overflow-y: auto;
  line-height: 1.5;
}
.telemetry-row {
  display: flex;
  gap: 16px;
  font-size: 11px;
  font-family: monospace;
}
.telemetry-val {
  font-weight: 700;
  color: var(--accent-cyan);
}
.btn {
  background: var(--accent-cyan);
  color: #000;
  border: none;
  padding: 6px 14px;
  border-radius: 4px;
  font-weight: 700;
  font-size: 11px;
  cursor: pointer;
  transition: opacity 0.2s;
}
.btn:hover { opacity: 0.9; }
.btn-secondary {
  background: #334155;
  color: #fff;
}
.som-tag {
  background: var(--accent-purple);
  color: #fff;
  font-size: 9px;
  padding: 1px 4px;
  border-radius: 3px;
  font-weight: 700;
  margin-right: 4px;
}
</style>
</head>
<body>

<header>
  <div class="brand-title">
    <span>Target International School</span>
    <span class="badge-tech">BROWSER-USE v2.4</span>
    <span data-ru="Лаборатория Веб-Агентов" data-en="Web Agent Lab">Veb-Agent Laboratoriyasi</span>
  </div>
  <div class="telemetry-row">
    <div><span data-ru="Токены:" data-en="Tokens:">Tokenlar:</span> <span id="telTokens" class="telemetry-val">0</span></div>
    <div><span data-ru="Шаги:" data-en="Steps:">Qadamlar:</span> <span id="telSteps" class="telemetry-val">0 / 10</span></div>
    <div><span data-ru="Статус:" data-en="Status:">Holat:</span> <span id="telStatus" class="telemetry-val" style="color:#eab308;" data-ru="Ожидание" data-en="Idle">Kutilmoqda</span></div>
  </div>
  <div style="display:flex; gap:8px;">
    <button id="btnStart" class="btn" onclick="startAutonomousAgent()" data-ru="▶️ Запустить Агента" data-en="▶️ Start Agent">▶️ Agentni Boshlash</button>
    <button class="btn btn-secondary" onclick="resetStudio()" data-ru="Сброс" data-en="Reset">Qayta o'rnatish</button>
  </div>
</header>

<div class="main-grid">
  <!-- LEFT: BROWSER VIEWPORT -->
  <div class="panel">
    <div class="panel-header">
      <span data-ru="ЭМУЛЯТОР HEADLESS CHROMIUM (VIEWPORT)" data-en="HEADLESS CHROMIUM EMULATOR (VIEWPORT)">HEADLESS CHROMIUM KO'RINISHI (VIEWPORT)</span>
      <span style="color:#64748b; font-size:10px;">1280x800 @ 60 FPS</span>
    </div>
    <div class="browser-viewport">
      <div class="mock-toolbar">
        <div class="mock-dots">
          <div class="mock-dot" style="background:#ef4444;"></div>
          <div class="mock-dot" style="background:#eab308;"></div>
          <div class="mock-dot" style="background:#22c55e;"></div>
        </div>
        <div class="mock-url">https://uzum-tech.uz/category/laptops</div>
      </div>

      <!-- POPUP MODAL BANNER -->
      <div id="promoModal" style="background:rgba(239,68,68,0.9); border:1px solid #f87171; border-radius:6px; padding:10px; margin-bottom:10px; display:flex; justify-content:space-between; align-items:center;">
        <div>
          <span class="som-tag">[1]</span>
          <strong style="color:#fff;" data-ru="Скидка 40% на первый заказ!" data-en="40% Discount On First Order!">Birinchi buyurtmaga 40% chegirma!</strong>
          <span style="font-size:10px; color:#fee2e2; margin-left:6px;" data-ru="(Модальное окно закрывает поиск)" data-en="(Modal blocks the search input)">(Modal oyna qidiruvni to'smoqda)</span>
        </div>
        <button onclick="closeModalDirect()" style="background:#000; color:#fff; border:none; padding:4px 10px; border-radius:4px; font-size:10px; cursor:pointer;" data-ru="✕ Закрыть" data-en="✕ Dismiss">✕ Yopish</button>
      </div>

      <!-- SEARCH BAR -->
      <div style="display:flex; gap:6px; margin-bottom:12px;">
        <span class="som-tag" style="align-self:center;">[2]</span>
        <input id="searchInput" type="text" placeholder="Qidirish... (Masalan: MacBook)" style="flex:1; background:#1e293b; border:1px solid #475569; color:#fff; padding:6px 10px; border-radius:4px; font-size:11px;" />
        <span class="som-tag" style="align-self:center;">[3]</span>
        <button id="searchButton" onclick="manualSearch()" class="btn" style="padding:6px 12px;" data-ru="Поиск" data-en="Search">Qidiruv</button>
      </div>

      <!-- PRODUCTS CONTAINER -->
      <div id="productContainer">
        <div class="product-card" id="card1">
          <div>
            <span class="som-tag">[4]</span>
            <strong style="color:#38bdf8;">Apple MacBook Pro 14" M3 Max</strong>
            <div style="font-size:10px; color:#94a3b8; margin-top:2px;">36GB RAM / 1TB SSD / Space Black</div>
          </div>
          <div style="text-align:right;">
            <div style="font-weight:700; color:#10b981;">34 500 000 so'm</div>
            <span class="som-tag" style="margin-top:4px; display:inline-block;">[5]</span>
            <button class="btn" style="background:#3b82f6; color:#fff; font-size:10px; padding:3px 8px;" data-ru="В корзину" data-en="Add to Cart">Savatga</button>
          </div>
        </div>

        <div class="product-card" id="card2">
          <div>
            <span class="som-tag">[6]</span>
            <strong style="color:#38bdf8;">Lenovo Legion Pro 7i Gen 9</strong>
            <div style="font-size:10px; color:#94a3b8; margin-top:2px;">Intel Core i9-14900HX / RTX 4080 / 32GB</div>
          </div>
          <div style="text-align:right;">
            <div style="font-weight:700; color:#10b981;">28 900 000 so'm</div>
            <span class="som-tag" style="margin-top:4px; display:inline-block;">[7]</span>
            <button class="btn" style="background:#3b82f6; color:#fff; font-size:10px; padding:3px 8px;" data-ru="В корзину" data-en="Add to Cart">Savatga</button>
          </div>
        </div>

        <div class="product-card" id="card3">
          <div>
            <span class="som-tag">[8]</span>
            <strong style="color:#38bdf8;">ASUS ROG Zephyrus G16 OLED</strong>
            <div style="font-size:10px; color:#94a3b8; margin-top:2px;">Ultra 9 185H / RTX 4070 / 2.5K 240Hz</div>
          </div>
          <div style="text-align:right;">
            <div style="font-weight:700; color:#10b981;">24 200 000 so'm</div>
            <span class="som-tag" style="margin-top:4px; display:inline-block;">[9]</span>
            <button class="btn" style="background:#3b82f6; color:#fff; font-size:10px; padding:3px 8px;" data-ru="В корзину" data-en="Add to Cart">Savatga</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- RIGHT: AGENT BRAIN CONSOLE -->
  <div class="panel">
    <div class="panel-header">
      <span data-ru="ТЕРМИНАЛ И ТЕЛЕМЕТРИЯ АГЕНТА (REASONING ENGINE)" data-en="AGENT REASONING & TELEMETRY TERMINAL">AGENT TELEMETRIYA VA REASONING TERMINALI</span>
      <span style="color:var(--accent-cyan); font-size:10px;">CDP WebSocket Active</span>
    </div>
    <div id="agentConsole" class="agent-console">
      <div style="color:#64748b;" data-ru="[Готов к сессии] Нажмите '▶️ Запустить Агента' для выполнения автономного сценария сбора данных." data-en="[Session Ready] Click '▶️ Start Agent' to trigger the autonomous crawling pipeline.">[Sessiya tayyor] Avtonom veb-skraping tsiklini boshlash uchun '▶️ Agentni Boshlash' tugmasini bosing.</div>
    </div>
  </div>
</div>

<script>
var agentRunning = false;
function log(msg, color) {
  var c = document.getElementById('agentConsole');
  var d = document.createElement('div');
  d.style.color = color || '#cbd5e1';
  d.style.marginBottom = '4px';
  d.innerHTML = msg;
  c.appendChild(d);
  c.scrollTop = c.scrollHeight;
}

function closeModalDirect() {
  var m = document.getElementById('promoModal');
  if (m) m.style.display = 'none';
  log('<span style="color:#22c55e;">[Manual] Modal banner foydalanuvchi tomonidan yopildi.</span>');
}

function manualSearch() {
  var inp = document.getElementById('searchInput');
  log('<span style="color:#38bdf8;">[Search] Qidiruv so‘rovi: "' + inp.value + '"</span>');
}

function startAutonomousAgent() {
  if (agentRunning) return;
  agentRunning = true;

  var btn = document.getElementById('btnStart');
  btn.disabled = true;
  btn.style.opacity = '0.5';

  var telTok = document.getElementById('telTokens');
  var telStp = document.getElementById('telSteps');
  var telStat = document.getElementById('telStatus');

  log('<span style="color:#06b6d4;">[00:01] 🚀 Browser-Use v2.4 ishga tushdi. Maqsad: Noutbuklar narxini JSON ga yig‘ish.</span>');
  telStat.textContent = 'DOM Distillyatsiyasi';
  telStat.style.color = 'var(--accent-cyan)';
  telTok.textContent = '950';
  telStp.textContent = '1 / 10';

  setTimeout(function() {
    log('<span style="color:#a855f7;">[00:02] 🧠 Accessibility Tree tuzildi. 2,400 xom teglardan 9 ta interaktiv element qoldi.</span>');
    log('<span style="color:#eab308;">[00:03] ⚠️ To‘siq aniqlandi: [1] Modal reklama oynasi qidiruv maydonini to‘smoqda.</span>');
    log('<span style="color:#a855f7;">[00:04] 📋 Action: {"name": "click", "index": 1, "reason": "Modalni yopish"}</span>');
    telStat.textContent = 'Modalni Yopish';
    telTok.textContent = '1,680';
    telStp.textContent = '2 / 10';

    setTimeout(function() {
      var m = document.getElementById('promoModal');
      if (m) m.style.display = 'none';
      log('<span style="color:#10b981;">[00:05] ✅ Playwright click(1) muvaffaqiyatli bajarildi. Modal yopildi.</span>');

      setTimeout(function() {
        telStat.textContent = 'Qidiruv Kiritish';
        telTok.textContent = '2,420';
        telStp.textContent = '3 / 10';
        var inp = document.getElementById('searchInput');
        inp.value = 'MacBook Pro';
        log('<span style="color:#a855f7;">[00:06] 📋 Action: {"name": "type", "index": 2, "text": "MacBook Pro"}</span>');

        setTimeout(function() {
          telStat.textContent = 'Jadval Scraping';
          telTok.textContent = '3,150';
          telStp.textContent = '4 / 10';
          var card1 = document.getElementById('card1');
          if (card1) card1.classList.add('highlight');
          log('<span style="color:#06b6d4;">[00:07] 🔍 Jadval elementlari skan qilindi. 3 ta noutbuk topildi.</span>');

          setTimeout(function() {
            var extractedJSON = JSON.stringify([
              {"name": "Apple MacBook Pro 14 M3 Max", "price": 34500000, "currency": "UZS"},
              {"name": "Lenovo Legion Pro 7i Gen 9", "price": 28900000, "currency": "UZS"},
              {"name": "ASUS ROG Zephyrus G16 OLED", "price": 24200000, "currency": "UZS"}
            ], null, 2);

            log('<pre style="background:#111827; padding:8px; border-radius:4px; color:#10b981; font-size:10px;">' + extractedJSON + '</pre>');
            log('<span style="color:#10b981; font-weight:700;">[00:09] 🏆 Missiya 100% muvaffaqiyat bilan yakunlandi! Jami 4 qadam, 3,150 token sarflandi.</span>');
            telStat.textContent = '✅ Muvaffaqiyat';
            telStat.style.color = 'var(--accent-green)';
            telStp.textContent = '4 / 10';
            agentRunning = false;
            btn.disabled = false;
            btn.style.opacity = '1';
          }, 1200);

        }, 1200);

      }, 1000);

    }, 1200);

  }, 1000);
}

function resetStudio() {
  agentRunning = false;
  var m = document.getElementById('promoModal');
  if (m) m.style.display = 'flex';
  var inp = document.getElementById('searchInput');
  if (inp) inp.value = '';
  var cards = document.querySelectorAll('.product-card');
  cards.forEach(function(c) { c.classList.remove('highlight'); });
  var c = document.getElementById('agentConsole');
  c.innerHTML = '<div style="color:#64748b;">[Sessiya qayta o‘rnatildi] Boshlash uchun "▶️ Agentni Boshlash" tugmasini bosing.</div>';
  document.getElementById('telTokens').textContent = '0';
  document.getElementById('telSteps').textContent = '0 / 10';
  document.getElementById('telStatus').textContent = 'Kutilmoqda';
  document.getElementById('telStatus').style.color = '#eab308';
  var btn = document.getElementById('btnStart');
  btn.disabled = false;
  btn.style.opacity = '1';
}
</script>

</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "simulator", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: simulator/index.html")

def main():
    print("📦 Building 10-11-sinf (Lesson 30: Autonomous Web Browsing & Headless Automation)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_simulator()
    print("🎉 Done! Generated Grade 10–11 Lesson 30.")

if __name__ == "__main__":
    main()
