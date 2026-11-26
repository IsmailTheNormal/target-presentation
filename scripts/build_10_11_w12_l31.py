#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_10_11_w12_l31.py — Builder for 10–11th Grade, Week 12, Lesson 31

Mavzu: Multi-Modal Vision Agentlar va Computer-Use: Ekran Boshqaruvi va Desktop Avtomatlashtirish
Format: Yakka Dars (40 daqiqa), 10 slayd
Kohorta: 10-11-sinf (Senior AI & Enterprise Cybersecurity Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "10-11-sinf", "12-hafta", "31-dars-vision-agentlar-va-computer-use")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "simulator"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (10 Slides for 40-min Single Block)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="10–11-КЛАСС · 12-Я НЕДЕЛЯ · УРОК 31" data-en="GRADES 10–11 · WEEK 12 · LESSON 31">10–11-SINF · 12-HAFTA · 31-DARS</span></div>
    <h1 class="display" data-ru="Мультимодальные Vision Агенты и Computer-Use: Управление Экраном и Десктопом" data-en="Multi-Modal Vision Agents & Computer-Use: Screen Control & OS Automation">Multi-Modal Vision Agentlar va Computer-Use: Ekran Boshqaruvi va Desktop Avtomatlashtirish</h1>
    <p class="lede" data-ru="Выход ИИ-агентов за пределы браузера: скриншотное восприятие интерфейса, координатное заземление (Visual Grounding), масштабирование HiDPI и безопасный цикл управления мышью и клавиатурой через Anthropic Computer-Use API." data-en="Taking AI agents beyond web browsers: screenshot-based UI perception, coordinate visual grounding, HiDPI scaling, and the safety-governed mouse & keyboard OS execution loop via Anthropic Computer-Use API.">AI agentlarning brauzer chegarasidan to'liq operatsion tizimga chiqishi: skrinshot orqali interfeysni idrok qilish, koordinata bog'lash (Visual Grounding), HiDPI masshtablash va Anthropic Computer-Use API orqali sichqoncha va klaviaturani avtonom boshqarish tsikli.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">40 daqiqalik Yakka Dars</div>
        <h3 data-ru="Visual Grounding" data-en="Visual Grounding">Pikseldan Koordinataga</h3>
        <p data-ru="Как нейросеть определяет координаты [x, y] кнопок на экране и преобразует физическое разрешение 4K/Retina в нормализованную сетку API." data-en="How vision models pinpoint UI coordinates [x, y] and map high-density 4K/Retina displays to normalized API grids.">Neyrotarmoq qanday qilib ekrandagi tugmalar koordinatalarini [x, y] aniqlaydi va fizik 4K/Retina piksellarni API koordinata panjarasiga moslaydi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Computer-Use Studio</div>
        <h3 data-ru="Автономный OS Агент" data-en="Autonomous OS Agent">Desktop OS Boshqaruvi</h3>
        <p data-ru="Интерактивный симулятор десктопа: скриншот экрана, предсказание координат мыши, нажатия клавиш и протокол защиты от опасных действий (HITL)." data-en="Interactive desktop sandbox: screen snapshot, mouse coordinate prediction, key stroke execution, and destructive action guardrails (HITL).">Interaktiv desktop simulyatori: skrinshot tahlili, sichqoncha koordinatasini hisoblash, klaviatura kiritish va xavfli buyruqlarni tasdiqlash protokoli (HITL).</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Tahlil|Разбор|Review" data-time="04:00–09:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ · УРОК 30" data-en="HOMEWORK REVIEW · LESSON 30">UY VAZIFASI TAHLILI · 30-DARS</span></div>
    <h2 data-ru="Разбор 30-урока: DOM Pruning, Accessibility Tree и Rate Limiting" data-en="Lesson 30 Review: DOM Pruning, Accessibility Tree & Rate Limiting">30-dars Tahlili: DOM Pruning, Accessibility Tree va Rate Limiting</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Типичная Ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Сырой HTML вместо дерева" data-en="Raw HTML Token Explosion">Butun HTML-ni LLM-ga yuborish</h3>
        <p data-ru="Отправка всего DOM-дерева страницы (1.2 МБ) приводила к переполнению контекстного окна (120,000 токенов за 1 шаг) и мгновенному лимиту API (429 Rate Limit)." data-en="Feeding raw 1.2MB HTML documents blew past context windows (120k tokens/step) and triggered immediate 429 Rate Limit rejections.">1.2 MB li butun sahifa HTML kodini to'g'ridan-to'g'ri LLM ga yuborish bir qadamdayoq 120,000 tokenni yoqib, API blokirovkasiga (429 Rate Limit) sabab bo'ldi.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#ef4444;">// XATO: 1.2 MB axlat va script teglari</span>
<span style="color:#94a3b8;">const</span> html = <span style="color:#94a3b8;">await</span> page.content();
llm.invoke(html); <span style="color:#ef4444;">// 120,000 token!</span>
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Золотой Стандарт" data-en="Golden Standard">Oltin Standart (Best Practice)</div>
        <h3 data-ru="Accessibility Tree + RoI" data-en="Accessibility Tree + RoI">Daraxtni Tozalash va Snapshot</h3>
        <p data-ru="Использование Playwright Accessibility Snapshot сокращает разметку до 4 КБ интерактивных узлов с селекторами aria-ref, экономя 97% токенов." data-en="Extracting Playwright Accessibility Snapshots strips junk, reducing payloads to 4KB of aria-ref nodes while saving 97% of tokens.">Playwright Accessibility Snapshot yordamida faqat bosing bo'ladigan tugma va maydonlarni ajratib, 4 KB lik toza daraxt hosil qilish va tokenlarni 97% tejash.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#22c55e;">// TO'G'RI: Tozalangan A11y daraxti</span>
<span style="color:#94a3b8;">const</span> tree = <span style="color:#94a3b8;">await</span> page.accessibility.snapshot();
llm.invoke(JSON.stringify(tree)); <span style="color:#22c55e;">// 3,500 token!</span>
        </div>
      </div>
    </div>
    <div class="grid-2" style="margin-top:14px;">
      <div class="box">
        <span class="badge" data-ru="Блиц-вопрос (30 сек)" data-en="Blitz Question (30s)">Blitz Savol</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="Почему веб-агент не может нажать кнопку в Canvas-приложении или десктопном Excel через Accessibility Tree?" data-en="Why can't a DOM-based web agent click a button inside a Canvas app or desktop Excel via Accessibility Tree?">Nega an'anaviy veb-agent Canvas-ga chizilgan o'yin yoki desktop Excel dasturidagi tugmani Accessibility Tree orqali bosa olmaydi?</p>
      </div>
      <div class="box">
        <span class="badge" data-ru="Мост к теме" data-en="Bridge to Today">Bugungi Mavzuga Ko'prik</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="Canvas, десктопные окна и старые программы не имеют DOM! Единственный способ управлять ими — смотреть глазами (Vision) и кликать мышью." data-en="Canvas, desktop windows, and legacy apps have zero DOM! The only solution is visual perception (Vision) and simulated OS mouse events.">Canvas, desktop oynalar va korporativ dasturlarda DOM umuman yo'q! Ularni boshqarishning birdan-bir yo'li — insondek skrinshotga qarab (Vision) va sichqoncha bilan bosishdir.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: PROBLEM - BEYOND THE DOM -->
  <section class="slide" data-phase="Konsept|Концепт|Concept" data-time="09:00–14:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ДЕФИЦИТ DOM-ПОДХОДА · ГРАНИЦЫ ВЕБА" data-en="THE LIMITS OF DOM · BEYOND THE BROWSER">DOM YONDASHUVI CHEGARASI · VEBDAN TASHQARIGA</span></div>
    <h2 data-ru="Почему DOM-агенты слепы в реальном мире ОС?" data-en="Why DOM Agents Are Blind in Desktop Operating Systems?">Nega DOM-agentlar operatsion tizimda ko'r bo'lib qoladi?</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="HTML / DOM Chegarasi" data-en="DOM Boundary">Faqat Brauzer Ichida</div>
        <h3 data-ru="Отсутствие ОС-контекста" data-en="No OS Native Context">OS Konteksti Yo'q</h3>
        <p data-ru="DOM-агенты живут в песочнице Chrome. Они не видят файловый менеджер Finder/Explorer, терминал, десктопные Slack, Photoshop или VS Code." data-en="DOM agents live inside Chrome sandbox. They cannot see Finder/Explorer file managers, terminals, desktop Slack, Photoshop or VS Code.">DOM-agentlar faqat Chrome ichida yashaydi. Ular OS fayl menejeri (Finder/Explorer), terminal, Telegram, Photoshop yoki VS Code dasturlarini ko'ra olmaydi.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(234,179,8,0.15); color:var(--warning);" data-ru="Piksel Grafikasi" data-en="Pixel Canvas Graphics">Canvas va WebGL</div>
        <h3 data-ru="Черный ящик пикселей" data-en="Black-Box Pixels">Piksellar Qora Qutisi</h3>
        <p data-ru="Figma, Google Maps, онлайн-игры и сложные графики рендерятся в один HTML5 &lt;canvas&gt;. Внутри нет тегов &lt;button&gt; или &lt;input&gt; — только сырые пиксели." data-en="Figma, Google Maps, web games, and rich charts render into a single &lt;canvas&gt;. There are zero &lt;button&gt; or &lt;input&gt; tags — strictly raw pixels.">Figma, Google Maps, 3D o'yinlar bitta HTML5 &lt;canvas&gt; ichiga chiziladi. U yerda &lt;button&gt; teglari yo'q — faqat rangli piksellar mavjud.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(168,85,247,0.15); color:#a855f7;" data-ru="Универсальное решение" data-en="Universal Paradigm">Yagona Yechim: Vision</div>
        <h3 data-ru="Эмуляция Человека" data-en="Human Emulation">Inson Kabi Ko'rish</h3>
        <p data-ru="Компьютер создавался для человека с глазами и пальцами. Vision-модель делает скриншот и эмулирует клавиатуру и мышь на уровне ОС." data-en="Computers were built for humans with eyes and fingers. A Vision VLM takes screenshots and drives OS-level keyboard & mouse events.">Kompyuter ko'z va barmoqlarga ega inson uchun yaratilgan. Vision VLM skrinshot oladi va operatsion tizim sathida sichqoncha va klaviaturani boshqaradi.</p>
      </div>
    </div>
    <div class="table-wrap" style="margin-top:14px;">
      <table>
        <thead>
          <tr>
            <th data-ru="Характеристика" data-en="Feature">Mezon</th>
            <th data-ru="DOM-Агент (Playwright / Puppeteer)" data-en="DOM-based Agent">DOM-Agent (Playwright)</th>
            <th data-ru="Vision Computer-Use Агент (Anthropic / OSWorld)" data-en="Vision Computer-Use Agent">Vision Computer-Use Agent</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Qo'llanish doirasi</strong></td>
            <td data-ru="Только веб-страницы в браузере" data-en="Web pages inside browser only">Faqat brauzerdagi veb-sahifalar</td>
            <td data-ru="Любые программы: ОС, Терминал, Excel, Игры" data-en="Any software: OS, Terminal, Excel, Native Apps">Barcha dasturlar: OS, Terminal, Excel, Photoshop</td>
          </tr>
          <tr>
            <td><strong>Qabul qiluvchi organ</strong></td>
            <td data-ru="HTML / DOM / Accessibility Tree (текст)" data-en="HTML / DOM / A11y Tree (text)">HTML / DOM / Accessibility Tree (matn)</td>
            <td data-ru="Скриншот экрана (PNG / RGB пиксели)" data-en="Screen Screenshot (PNG / RGB pixels)">Ekran skrinshoti (PNG / RGB piksellar)</td>
          </tr>
          <tr>
            <td><strong>Harakat vositasi</strong></td>
            <td data-ru="page.click('css-selector') (JS инъекция)" data-en="page.click('css-selector') (JS injection)">CSS selektorlar bo'yicha JS chaqiruvlari</td>
            <td data-ru="Движение курсора мыши и нажатие клавиш ОС" data-en="OS mouse movements & hardware keystrokes">OS sathidagi sichqoncha koordinatasi [x, y] va tugmalar</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SLIDE 4: ARCHITECTURE & RE-ACT LOOP -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="14:00–19:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="АРХИТЕКТУРА СИСТЕМЫ · ПЕТЛЯ ДЕЙСТВИЙ" data-en="SYSTEM ARCHITECTURE · THE ACTION LOOP">TIZIM ARXITEKTURASI · HARAKATLAR TSIKLI</span></div>
    <h2 data-ru="Петля Computer-Use: Скриншот, Модель, Координата, Действие" data-en="The Computer-Use Execution Loop: Screen, Model, Coordinate, Action">Computer-Use Tsikli: Skrinshot, Model, Koordinata, Ijro</h2>
    <div class="grid-2">
      <div>
        <div class="card" style="padding:14px; margin-bottom:10px;">
          <div style="display:flex; align-items:center; gap:8px;">
            <span class="badge" style="background:var(--accent); color:#fff;">1</span>
            <strong data-ru="Захват Экрана (Screenshot)" data-en="Capture Screenshot">Ekran Tasvirini Olish (Screenshot)</strong>
          </div>
          <p style="font-size:12px; margin-top:4px;" data-ru="Операционная система делает снимок экрана и конвертирует его в Base64 PNG с нужным сжатием." data-en="OS grabs active screen frame and encodes it to Base64 PNG at configured display resolution.">Operatsion tizim displey kadrini oladi va uni Base64 PNG formatiga o'tkazadi.</p>
        </div>
        <div class="card" style="padding:14px; margin-bottom:10px;">
          <div style="display:flex; align-items:center; gap:8px;">
            <span class="badge" style="background:#a855f7; color:#fff;">2</span>
            <strong data-ru="VLM Рассуждение (Thought)" data-en="VLM Visual Reasoning">VLM Idrok va Rejalashtirish (Thought)</strong>
          </div>
          <p style="font-size:12px; margin-top:4px;" data-ru="Claude 3.5 Sonnet анализирует изображение, находит нужную кнопку 'Save' и вычисляет её центр в координатах [x: 742, y: 318]." data-en="Claude 3.5 Sonnet inspects visual layout, locates target 'Save' button, and computes center point [x: 742, y: 318].">Model tasvirni tahlil qilib, kerakli 'Saqlash' tugmasini topadi va uning markaziy koordinatasini [x: 742, y: 318] hisoblaydi.</p>
        </div>
        <div class="card" style="padding:14px; margin-bottom:10px;">
          <div style="display:flex; align-items:center; gap:8px;">
            <span class="badge" style="background:var(--success); color:#fff;">3</span>
            <strong data-ru="Вызов Инструмента (Tool Call)" data-en="OS Tool Execution">OS Harakatini Bajarish (Action)</strong>
          </div>
          <p style="font-size:12px; margin-top:4px;" data-ru="Драйвер эмулирует перемещение мыши, клик левой кнопкой или ввод текста через PyAutoGUI / xdotool." data-en="OS driver executes mouse glide, left click, or hardware keystrokes via PyAutoGUI / xdotool.">Drayver OS sathida sichqonchani ko'rsatilgan nuqtaga siljitadi va chertishni amalga oshiradi.</p>
        </div>
        <div class="card" style="padding:14px;">
          <div style="display:flex; align-items:center; gap:8px;">
            <span class="badge" style="background:var(--warning); color:#fff;">4</span>
            <strong data-ru="Пауза и Проверка (Observation)" data-en="Wait & UI Verification">Kutish va Natijani Kuzatish (Observation)</strong>
          </div>
          <p style="font-size:12px; margin-top:4px;" data-ru="Система ждет 500-1000 мс на рендер интерфейса, делает новый скриншот и проверяет, открылось ли диалоговое окно." data-en="System waits 500-1000ms for UI re-render, captures fresh screenshot, and verifies modal visibility.">Tizim interfeys yangilanishi uchun 500-1000 ms kutadi va keyingi skrinshot orqali muvaffaqiyatni tekshiradi.</p>
        </div>
      </div>
      <div class="card" style="display:flex; flex-direction:column; justify-content:center;">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Архитектурная схема" data-en="Architecture Flowchart">Tsikl Sxemasi</div>
        <div class="code-block" style="font-size:11px; margin-top:10px; line-height:1.6;">
[ OS Desktop UI ] 
       │
       ▼ (1. Grab Frame)
[ Screenshot Buffer (PNG) ]
       │
       ▼ (2. Multi-Modal Vision)
[ Claude 3.5 Sonnet / VLM ]
       │  Thought: "Fayl menyusini ochishim kerak"
       │  Tool: mouse_move + click [x: 48, y: 12]
       ▼ (3. Tool Call JSON)
[ Local Execution Driver (xdotool) ]
       │
       ▼ (4. OS Input Event)
[ OS Desktop UI Updated ] ──► (Qayta tsikl)
        </div>
        <p style="font-size:12px; margin-top:10px; color:var(--ink-secondary);" data-ru="Важно: один шаг занимает от 1.5 до 3 секунд из-за задержки отправки скриншота и инференса зрения нейросети." data-en="Note: each roundtrip takes 1.5 to 3 seconds due to image transmission latency and vision token processing.">Eslatma: har bir qadam tasvirni uzatish va model tahlili sababli 1.5 dan 3 soniyagacha vaqt oladi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: COORDINATE GROUNDING & HiDPI SCALING -->
  <section class="slide" data-phase="Muhandislik|Инженерия|Engineering" data-time="19:00–24:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="КООРДИНАТНОЕ ЗАЗЕМЛЕНИЕ · HiDPI И МАСШТАБИРОВАНИЕ" data-en="COORDINATE GROUNDING · HiDPI & SCALING">KOORDINATA HISOBI · HiDPI VA MASSHTABLASH</span></div>
    <h2 data-ru="Математика Координат: Физические Пиксели против API" data-en="Coordinate Mathematics: Physical Pixels vs API Space">Koordinatalar Matematikasi: Fizik Piksellar vs API Fazosi</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Проблема Retina / 4K Дисплеев" data-en="The Retina / 4K Dilemma">Retina va 4K Displeylar Muammosi</h3>
        <p data-ru="Современные ноутбуки имеют разрешение 2560×1600 (Retina 2x scale). Отправка такого изображения целиком съедает 2,000+ токенов и перегружает канал связи." data-en="Modern MacBooks feature 2560×1600 displays (Retina 2x). Sending full raw images consumes 2,000+ tokens and causes bandwidth bottlenecks.">Zamonaviy noutbuklar 2560×1600 (Retina 2x) pikselga ega. Ushbu ulkan tasvirni to'liq yuborish har bir qadamda 2,000 dan ortiq token sarflaydi.</p>
        <div class="box" style="margin-top:12px;">
          <strong data-ru="Стандарт API Разрешений" data-en="API Resolution Standards">API Standart O'lchamlari:</strong>
          <p style="font-size:12px; margin-top:4px;" data-ru="Anthropic рекомендует масштабировать экран до 1024×768 или максимум 1280×800. Нейросеть возвращает координаты именно в этой сетке!" data-en="Anthropic recommends scaling views down to 1024×768 or 1280×800. The VLM generates coordinates inside this virtual frame!">Anthropic ekranni 1024×768 yoki ko'pi bilan 1280×800 formatga keltirishni tavsiya qiladi. Neyrotarmoq aynan shu masshtabdagi [x, y] larni qaytaradi!</p>
        </div>
      </div>
      <div class="card">
        <h3 data-ru="Формула Масштабирования (Scaling)" data-en="Coordinate Translation Formula">Koordinatalarni O'tkazish Formulasi</h3>
        <p data-ru="Чтобы мышь кликнула в правильную точку физического экрана, координаты API необходимо умножить на коэффициент масштабирования (Scale Factor):" data-en="To ensure hardware cursor clicks the true pixel target, API coordinates must be mapped back via display scaling factors:">Sichqoncha fizik ekranning to'g'ri nuqtasiga tushishi uchun API koordinatalari masshtab koeffitsientiga (Scale Factor) ko'paytiriladi:</p>
        <div class="code-block" style="margin-top:10px; font-size:12px;">
<span style="color:#a855f7;">// Koeffitsientlar hisobi</span>
const scaleX = physicalWidth / apiWidth;   <span style="color:#64748b;">// 2560 / 1024 = 2.5</span>
const scaleY = physicalHeight / apiHeight; <span style="color:#64748b;">// 1600 / 768 = 2.083</span>

<span style="color:#22c55e;">// Fizik nuqtaga o'tkazish</span>
const realX = Math.round(apiX * scaleX);
const realY = Math.round(apiY * scaleY);

<span style="color:#3b82f6;">// OS sathida bosish:</span>
osDriver.click(realX, realY);
        </div>
        <p style="font-size:11px; margin-top:8px; color:var(--danger);" data-ru="Критическая ошибка: если забыть масштаб, клик сместится на 1,000 пикселей в сторону и нажмет чужую кнопку!" data-en="Critical pitfall: omitting scale factor shifts clicks by 1,000+ pixels, clicking random elements or closing windows!">Muhim ogohlantirish: agar masshtab inobatga olinmasa, sichqoncha 1,000 piksel chetga adashib, butunlay boshqa dasturni yopib qo'yishi mumkin!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: ANTHROPIC COMPUTER-USE API PROTOCOL -->
  <section class="slide" data-phase="Standart|Стандарт|Standard" data-time="24:00–28:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ПРОТОКОЛ API · СПЕЦИФИКАЦИЯ ИНСТРУМЕНТА" data-en="API SPECIFICATION · THE COMPUTER TOOL">API PROTOKOLI · COMPUTER TOOL SPETSIFIKATSIYASI</span></div>
    <h2 data-ru="Инструмент Computer-Use: JSON-Спецификация и Действия" data-en="The Computer-Use Tool: JSON Specification & Actions">Computer-Use Vositasi: JSON Spetsifikatsiyasi va Harakatlar</h2>
    <div class="grid-2">
      <div>
        <div class="code-block" style="font-size:11px; line-height:1.5;">
<span style="color:#64748b;">// LLM-ga uzatiladigan Tool ta'rifi</span>
{
  <span style="color:#3b82f6;">"type"</span>: <span style="color:#22c55e;">"computer_20241022"</span>,
  <span style="color:#3b82f6;">"name"</span>: <span style="color:#22c55e;">"computer"</span>,
  <span style="color:#3b82f6;">"display_width_px"</span>: 1024,
  <span style="color:#3b82f6;">"display_height_px"</span>: 768,
  <span style="color:#3b82f6;">"display_number"</span>: 1
}

<span style="color:#64748b;">// Model javobida keluvchi harakat namunasi</span>
{
  <span style="color:#3b82f6;">"action"</span>: <span style="color:#22c55e;">"mouse_move"</span>,
  <span style="color:#3b82f6;">"coordinate"</span>: [512, 384]
}
        </div>
      </div>
      <div>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th data-ru="Действие (action)" data-en="Action Type">Harakat turi</th>
                <th data-ru="Параметры" data-en="Parameters">Parametrlar</th>
                <th data-ru="Описание" data-en="Description">Vazifasi</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><code>screenshot</code></td>
                <td>-</td>
                <td data-ru="Сделать снимок экрана" data-en="Take screen capture">Yangi skrinshot olish</td>
              </tr>
              <tr>
                <td><code>mouse_move</code></td>
                <td><code>coordinate: [x, y]</code></td>
                <td data-ru="Переместить курсор мыши" data-en="Move mouse cursor">Kursor koordinatasini o'zgartirish</td>
              </tr>
              <tr>
                <td><code>left_click</code></td>
                <td><code>coordinate: [x, y]</code></td>
                <td data-ru="Клик левой кнопкой мыши" data-en="Left click at [x,y]">Chap tugma bilan bosish</td>
              </tr>
              <tr>
                <td><code>type</code></td>
                <td><code>text: "hello"</code></td>
                <td data-ru="Ввести символы текста" data-en="Type alphanumeric text">Klaviatura orqali matn kiritish</td>
              </tr>
              <tr>
                <td><code>key</code></td>
                <td><code>text: "Return"</code></td>
                <td data-ru="Нажать служебную клавишу" data-en="Press special key">Enter, Tab, Esc kabi tugmalarni bosish</td>
              </tr>
              <tr>
                <td><code>hotkey</code></td>
                <td><code>text: "ctrl+s"</code></td>
                <td data-ru="Комбинация горячих клавиш" data-en="Key combination">Kombinatsiyalarni bajarish (Ctrl+C, Ctrl+V)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: CYBERSECURITY & HITL GUARD -->
  <section class="slide" data-phase="Xavfsizlik|Безопасность|Security" data-time="28:00–32:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="КИБЕРБЕЗОПАСНОСТЬ · ИЗОЛЯЦИЯ И ЗАЩИТА" data-en="CYBERSECURITY · OS ISOLATION & GUARDRAILS">KIBERXAVFSIZLIK · IZOLYATSIYA VA QIZIL CHIZIQLAR</span></div>
    <h2 data-ru="Песочница и Human-in-the-Loop (HITL): Защита от Катастрофы" data-en="Sandboxing & Human-in-the-Loop (HITL): Preventing Catastrophes">Qumloq (Sandbox) va HITL: Kiber-Halokatdan Himoyalanish</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Главная Опасность" data-en="Threat Vector">Eng Katta Xavf: Xost OS Boshqaruvi</div>
        <h3 data-ru="Автономная Ошибка Агента" data-en="Autonomous Agent Glitch">Avtonom Qaltis Buyruqlar</h3>
        <p data-ru="Если предоставить агенту прямой доступ к вашему рабочему компьютеру, галлюцинация или ошибка зрения может привести к удалению файлов (rm -rf), форматированию диска или отправке приватных документов в сеть." data-en="Granting an agent direct bare-metal OS access invites disaster: a single hallucination can wipe files (rm -rf), delete databases, or leak confidential files.">Agar agentga to'g'ridan-to'g'ri o'z shaxsiy kompyuteringizni topshirsangiz, bitta ko'rish xatosi sababli terminalda "rm -rf", muhim fayllarni o'chirish yoki shaxsiy arxivlarni internetga yuborish xavfi tug'iladi.</p>
        <div class="box" style="margin-top:10px;">
          <strong data-ru="Золотое правило контейнеризации:" data-en="Container Rule:">Konteynerlashtirish Qoidasi:</strong>
          <p style="font-size:12px; margin-top:4px;" data-ru="Никогда не запускайте Computer-Use на физической машине разработчика! Только Docker с виртуальным X11 (Xvfb) экраном." data-en="Never run raw Computer-Use on your daily driver host OS! Enforce Docker containers with virtual X11 (Xvfb) displays.">Hech qachon Computer-Use agentini shaxsiy asosiy kompyuteringizda ishlatmang! Faqat Docker + virtual X11 (Xvfb) ekrani ichida izolyatsiyalangan holda ishga tushiring.</p>
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Архитектура Защиты" data-en="Defense Architecture">HITL: Inson Ruxsati va Tasdig'i</div>
        <h3 data-ru="Политика Критических Действий" data-en="Destructive Policy Gate">Destruktiv Buyruqlarni To'xtatish</h3>
        <p data-ru="Любые необратимые действия блокируются шлюзом безопасности до явного одобрения человеком (Human-in-the-Loop):" data-en="All irreversible actions are gated behind a human approval interceptor (Human-in-the-Loop):">Qaytarib bo'lmaydigan har qanday amal inson tasdiqlamaguncha tizim tomonidan bloklanadi (Human-in-the-Loop):</p>
        <ul style="font-size:12px; line-height:1.7; margin-top:8px;">
          <li data-ru="💳 <strong>Финансовые транзакции:</strong> Кнопки 'Купить', ввод реквизитов карты, перевод средств." data-en="💳 <strong>Financial operations:</strong> 'Confirm Payment' buttons, card inputs, wire transfers.">💳 <strong>Moliyaviy operatsiyalar:</strong> "To'lovni tasdiqlash", karta raqamini kiritish yoki pul o'tkazish.</li>
          <li data-ru="🗑️ <strong>Удаление данных:</strong> Кнопки 'Delete Database', 'Drop Table', системные утилиты." data-en="🗑️ <strong>Permanent deletion:</strong> 'Delete Database', disk formatters, recursive file removal.">🗑️ <strong>Ma'lumotlarni o'chirish:</strong> "Delete Database", arxivni tozalash, tizim fayllari.</li>
          <li data-ru="🔑 <strong>Изменение учетных записей:</strong> Смена паролей, создание админов, экспорт SSH-ключей." data-en="🔑 <strong>Identity & credentials:</strong> Password resets, creating root users, exporting SSH keys.">🔑 <strong>Hisob va parollar:</strong> Parolni almashtirish, admin qo'shish, SSH kalitlarni ko'chirish.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: CODE IMPLEMENTATION (PYTHON ANTHROPIC SDK) -->
  <section class="slide" data-phase="Kod|Код|Code" data-time="32:00–35:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="РЕАЛИЗАЦИЯ НА PYTHON · ANTHROPIC SDK" data-en="PYTHON IMPLEMENTATION · ANTHROPIC SDK">PYTHON DASTURLASH · ANTHROPIC SDK IMPLEMENTATSIYASI</span></div>
    <h2 data-ru="Минимальный Агент Компьютера: Код Драйвера" data-en="Minimal Computer Agent: Driver Implementation">Minimal Kompyuter Agenti: Drayver Kodi</h2>
    <div class="code-block" style="font-size:11.5px; line-height:1.5;">
<span style="color:#a855f7;">import</span> anthropic, pyautogui, base64

client = anthropic.Anthropic()

<span style="color:#64748b;"># 1. Ekran tasvirini olish va Base64 ga aylantirish</span>
<span style="color:#3b82f6;">def</span> <span style="color:#22c55e;">take_screenshot</span>():
    pyautogui.screenshot(<span style="color:#22c55e;">"/tmp/screen.png"</span>)
    <span style="color:#a855f7;">with</span> open(<span style="color:#22c55e;">"/tmp/screen.png"</span>, <span style="color:#22c55e;">"rb"</span>) <span style="color:#a855f7;">as</span> f:
        <span style="color:#a855f7;">return</span> base64.b64encode(f.read()).decode(<span style="color:#22c55e;">"utf-8"</span>)

<span style="color:#64748b;"># 2. Agentga vosita (tool) va so'rov yuborish</span>
response = client.beta.messages.create(
    model=<span style="color:#22c55e;">"claude-3-5-sonnet-20241022"</span>,
    max_tokens=1024,
    tools=[{<span style="color:#22c55e;">"type"</span>: <span style="color:#22c55e;">"computer_20241022"</span>, <span style="color:#22c55e;">"name"</span>: <span style="color:#22c55e;">"computer"</span>, <span style="color:#22c55e;">"display_width_px"</span>: 1024, <span style="color:#22c55e;">"display_height_px"</span>: 768}],
    messages=[{
        <span style="color:#22c55e;">"role"</span>: <span style="color:#22c55e;">"user"</span>,
        <span style="color:#22c55e;">"content"</span>: [
            {<span style="color:#22c55e;">"type"</span>: <span style="color:#22c55e;">"text"</span>, <span style="color:#22c55e;">"text"</span>: <span style="color:#22c55e;">"Kalkulyatorni och va 125 * 8 hisobla"</span>},
            {<span style="color:#22c55e;">"type"</span>: <span style="color:#22c55e;">"image"</span>, <span style="color:#22c55e;">"source"</span>: {<span style="color:#22c55e;">"type"</span>: <span style="color:#22c55e;">"base64"</span>, <span style="color:#22c55e;">"media_type"</span>: <span style="color:#22c55e;">"image/png"</span>, <span style="color:#22c55e;">"data"</span>: take_screenshot()}}
        ]
    }]
)
    </div>
    <p style="font-size:12px; margin-top:8px; color:var(--ink-secondary);" data-ru="Ответ модели содержит блок tool_use с типом действия (left_click) и координатами, которые затем передаются в pyautogui.click(x, y)." data-en="The model response yields a tool_use block with action type (left_click) and coordinates, dispatched straight to pyautogui.click(x, y).">Model javobida tool_use bloki keladi va undagi harakat (left_click) hamda koordinatalar pyautogui.click(x, y) orqali bajariladi.</p>
  </section>

  <!-- SLIDE 9: INTERACTIVE ARENA (STUDIO PREVIEW) -->
  <section class="slide" data-phase="Amaliyot|Практика|Practice" data-time="35:00–38:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКИЙ СИМУЛЯТОР · COMPUTER-USE STUDIO" data-en="INTERACTIVE LAB · COMPUTER-USE STUDIO">AMALIY ARENA · COMPUTER-USE STUDIO</span></div>
    <h2 data-ru="Лаборатория: Автономное Управление Рабочим Столом" data-en="Hands-on Lab: Autonomous Desktop OS Automation">Laboratoriya: Avtonom Desktop Boshqaruv Simulyatori</h2>
    <div class="hero-split">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Сценарий Миссии" data-en="Mission Scenario">Kiber-Missiya Topshirig'i</div>
        <h3 data-ru="Расчет Сметы и Сохранение" data-en="Invoice Math & Saving">Kalkulyator va Hisobot Yozish</h3>
        <p data-ru="Агенту поступает задача: найти и открыть иконку Калькулятора на рабочем столе, перемножить 125 × 8, скопировать ответ и вставить в открытый текстовый редактор Notes." data-en="The agent receives an OS goal: locate and open desktop Calculator, compute 125 × 8, copy the result, and append it into active Notes editor.">Agentga vazifa beriladi: Ish stolidan Kalkulyator dasturini topib ochish, 125 × 8 amalini bajarish, natijani nusxalab, yonidagi Matn Muharririga yozib saqlash.</p>
        <div class="box" style="margin-top:12px;">
          <strong data-ru="Что мы увидим в симуляторе:" data-en="What you observe live:">Simulyatorda nima kuzatiladi:</strong>
          <ul style="font-size:12px; line-height:1.6; margin-top:4px;">
            <li data-ru="🎯 <strong>Зеленый прицел мыши:</strong> плавное перемещение курсора к координатам [x, y]." data-en="🎯 <strong>Mouse Crosshair:</strong> smooth motion toward predicted target coordinates [x, y].">🎯 <strong>Yashil kursor nishoni:</strong> sichqonchaning aniq [x, y] koordinatalariga siljishi.</li>
            <li data-ru="📸 <strong>Кадры скриншотов:</strong> как VLM видит экран после каждого нажатия клавиши." data-en="📸 <strong>Screenshot Snapshots:</strong> how the vision model reads screen changes post-click.">📸 <strong>Skrinshot kadrlar:</strong> model har bir harakatdan so'ng ekranni qanday ko'rishi.</li>
            <li data-ru="🛡️ <strong>HITL-шлюз:</strong> запрос подтверждения при попытке закрыть несохраненный файл." data-en="🛡️ <strong>HITL Interceptor:</strong> human prompt triggered on closing unsaved notes.">🛡️ <strong>HITL qalqoni:</strong> faylni saqlamay yopishda inson tasdig'ini so'rash mexanizmi.</li>
          </ul>
        </div>
      </div>
      <div class="card" style="display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:rgba(15,23,42,0.6);">
        <div style="font-size:42px; margin-bottom:10px;">🖥️ 🤖 🖱️</div>
        <h3 data-ru="Запуск Симулятора ОС" data-en="Launch OS Simulator">Desktop OS Sandbox</h3>
        <p style="font-size:13px; max-width:320px; color:var(--ink-secondary);" data-ru="Откройте папку simulator/index.html для запуска интерактивной визуализации всех 6 шагов агента." data-en="Open simulator/index.html to experience interactive 6-step desktop execution with live visual grounding.">Interaktiv 6 bosqichli agent ishini va jonli koordinatalar tahlilini ko'rish uchun quyidagi ilovadan foydalaning.</p>
        <a href="simulator/index.html" target="_blank" style="display:inline-block; margin-top:14px; padding:10px 20px; border-radius:10px; background:var(--accent); color:#fff; text-decoration:none; font-weight:700; font-size:13px;" data-ru="🚀 Открыть Симулятор ОС" data-en="🚀 Open OS Simulator">🚀 OS Simulyatorini Ochish</a>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: SUMMARY & 3-TIER HOMEWORK -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="38:00–40:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ УРОКА И ДОМАШНЕЕ ЗАДАНИЕ · 10 БАЛЛОВ" data-en="LESSON SUMMARY & 3-TIER HOMEWORK · 10 POINTS">XULOSA VA 3 DARAJALI UY VAZIFASI · 10 BALL</span></div>
    <h2 data-ru="Архитектурный Итог и Домашнее Задание" data-en="Architectural Summary & Homework">Xulosa va 3 Darajali Uy Vazifasi</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Уровень 1: База (4 балла)" data-en="Tier 1: Core (4 pts)">1-Daraja: Baza (4 ball)</div>
        <h3 data-ru="Конфигурация Инструмента" data-en="Tool Definition">Tool JSON va Masshtab</h3>
        <p data-ru="Описать спецификацию инструмента computer_20241022 для экрана 1280×800 и написать формулу конвертации координат для 4K монитора (3840×2160)." data-en="Write computer_20241022 tool specification for 1280×800 and derive coordinate scaling formulas for a 4K display (3840×2160).">1280×800 o'lchamdagi ekran uchun computer_20241022 vositasini ta'riflash va 4K monitor (3840×2160) uchun koordinatalarni masshtablash formulasini yozish.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Уровень 2: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</div>
        <h3 data-ru="Петля Нажатия и Ввода" data-en="Click & Type Pipeline">PyAutoGUI Drayver Loop</h3>
        <p data-ru="Реализовать функцию dispatch_action(action_dict), которая принимает ответ модели (mouse_move, left_click, type) и безопасно исполняет его в ОС." data-en="Implement dispatch_action(action_dict) routing model actions (mouse_move, left_click, type) to safe OS executions via PyAutoGUI.">Model javobidagi harakatlarni (mouse_move, left_click, type) qabul qilib, ularni PyAutoGUI orqali xatolarsiz bajaruvchi dispatch_action funksiyasini yozish.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Уровень 3: Челлендж (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</div>
        <h3 data-ru="HITL Защитный Шлюз" data-en="HITL Security Interceptor">HITL Guardrail Filtr</h3>
        <p data-ru="Создать перехватчик, который парсит вводимый текст или кликаемые зоны: при совпадении с паттернами rm, delete, format, buy останавливает процесс и требует ввода пароля." data-en="Build a security guardrail intercepting text or click targets: if 'rm', 'delete', 'format', or 'buy' are detected, it pauses execution for human override.">Xavfsizlik filtrini yaratish: agar kiritilayotgan matn yoki bosilayotgan tugmada 'rm', 'delete', 'format' yoki 'to'lov' uchrasa, ishni to'xtatib, o'qituvchi parolini so'rash.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px; text-align:center;">
      <p style="font-size:13px;" data-ru="💡 Практическое домашнее задание доступно в файле vazifa.html с автоматической проверкой и сохранением в LocalStorage." data-en="💡 Interactive homework is bundled in vazifa.html with instant client-side testing and LocalStorage persistence.">💡 Interaktiv uy vazifasi <a href="vazifa.html" style="color:var(--accent); font-weight:700;">vazifa.html</a> faylida joylashgan bo'lib, avtomatik testlar va LocalStorage saqlash tizimiga ega.</p>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. TEACHER NOTES JSON (Triplets: [title, say, do])
# -----------------------------------------------------------------------------
NOTES_DATA = {
  "uz": [
    ["Kirish va Maqsad", "Bugun AI agentlarni brauzer oynasidan butun kompyuter maydoniga olib chiqamiz. Anthropic Computer-Use API orqali sichqoncha va klaviaturani avtonom boshqarishni o'rganamiz.", "Doskaga mavzuni yozing va slaydni oching."],
    ["Uy Vazifasi Tahlili", "O'tgan darsdagi eng katta xato butun 1 MB lik HTML-ni modelga yuborish bo'ldi. A11y daraxti tokenlarni 97% tejaydi. Ammo Canvas yoki desktop dasturlarda DOM yo'qligini eslatamiz.", "O'quvchilardan 30 soniyalik blits savolga javob oling."],
    ["DOM Chegarasi", "Nega DOM yetarli emas? Photoshop, terminal, Excel yoki Figma kabi dasturlarda HTML teglari yo'q. Yagona yo'l — inson ko'zi kabi ekran skrinshotini ko'rish.", "Slayddagi taqqoslash jadvalini bosqichma-bosqich tushuntiring."],
    ["Computer-Use Tsikli", "Bu tsikl 4 qadamdan iborat: Skrinshot olish, model tasvirni tahlil qilib fikrlashi, harakat buyrug'ini chiqarishi va OS drayveri uni bajarishi.", "Doskada aylana ReAct tsiklini ko'rsating."],
    ["Koordinatalar va HiDPI", "Retina va 4K monitorlarda piksellar soni juda ko'p. Shuning uchun API 1024x768 ga tushiriladi va koordinatalarni masshtablash formulasidan foydalaniladi.", "Masshtablash formulasi bo'yicha kichik hisob-kitobni o'quvchilar bilan birga bajaring."],
    ["API Spetsifikatsiyasi", "Anthropic spetsifikatsiyasidagi computer_20241022 vositasi qanday tuzilganini ko'rib chiqamiz. Harakat turlari: mouse_move, left_click, type va key.", "JSON parametrlarini va har bir harakat vazifasini tahlil qiling."],
    ["Kiberxavfsizlik va HITL", "Computer-Use agentiga o'z kompyuteringizni berish xavfli! Faqat Docker konteynerda ishlatiladi. Muhim amallar (o'chirish, to'lov) faqat inson tasdig'i bilan bo'lishi shart.", "Kiber-xatarlar misollarini keltirib, qizil chiziqlarni ta'kidlang."],
    ["Python SDK Kodu", "PyAutoGUI va Anthropic SDK yordamida qanday qilib bir necha qator kod bilan skrinshot olib, modelga uzatish mumkinligini ko'ramiz.", "Kod blokidagi 1 va 2-bosqichlarni tushuntiring."],
    ["Amaliy Simulyator", "Endi simulyator orqali agentning ish stolidagi kalkulyatorni ochib hisob-kitob qilishini va matn muharririga yozishini jonli kuzatamiz.", "Sinf bilan birgalikda simulator/index.html ni ochib, qadamlarni bajaring."],
    ["Xulosa va Vazifa", "Bugun biz eng zamonaviy Computer-Use arxitekturasini o'rgandik. 3 darajali vazifa vazifa.html faylida berilgan, 10 ballik mezonni bajaring.", "O'quvchilarga vazifa talablarini va muddatini eslatib darsni yakunlang."]
  ],
  "ru": [
    ["Введение и Цель", "Сегодня мы выводим ИИ-агентов из браузера на весь рабочий стол компьютера. Изучаем Anthropic Computer-Use API для управления мышью и клавиатурой.", "Запишите тему на доске и откройте первый слайд."],
    ["Разбор Домашнего Задания", "Главная ошибка прошлого урока — отправка сырого 1 МБ HTML. A11y дерево спасает 97% токенов. Но в десктопных программах и Canvas DOM отсутствует.", "Примите ответы учеников на 30-секундный блиц-вопрос."],
    ["Границы DOM", "Почему DOM недостаточно? В приложениях вроде Photoshop, Excel, терминала или Figma нет HTML-тегов. Единственный выход — визуальное зрение VLM.", "Объясните сравнительную таблицу по пунктам."],
    ["Петля Computer-Use", "Цикл состоит из 4 фаз: скриншот, рассуждение модели, генерация команды инструмента и исполнение ОС-драйвером.", "Изобразите циклический граф на доске."],
    ["Координаты и HiDPI", "Экраны Retina и 4K содержат миллионы пикселей. API сжимает их до 1024x768, требуя пересчета координат через коэффициент масштаба.", "Разберите математическую формулу масштабирования вместе с классом."],
    ["Спецификация API", "Рассматриваем спецификацию инструмента computer_20241022. Типы действий: mouse_move, left_click, type и key.", "Поясните поля JSON-схемы и назначение каждого действия."],
    ["Кибербезопасность и HITL", "Давать агенту прямой доступ к хост-системе опасно! Запуск только в Docker-песочнице. Критические действия требуют Human-in-the-Loop.", "Подчеркните правила изоляции и риски случайного удаления файлов."],
    ["Код на Python SDK", "Демонстрируем, как с помощью PyAutoGUI и Anthropic SDK сделать снимок экрана и отправить запрос модели в несколько строк.", "Поясните этапы 1 и 2 в коде драйвера."],
    ["Практический Симулятор", "В симуляторе наблюдаем, как агент находит калькулятор, производит вычисления и вставляет результат в блокнот.", "Запустите simulator/index.html на смартборде и разберите шаги."],
    ["Итоги и Задание", "Мы изучили архитектуру Computer-Use. 3-уровневое домашнее задание доступно в vazifa.html с критериями на 10 баллов.", "Напомните критерии оценки и завершите занятие."]
  ],
  "en": [
    ["Intro & Objectives", "Today we expand AI agents from the browser sandbox to the entire desktop OS using the Anthropic Computer-Use API.", "Write lesson title on board and project slide 1."],
    ["Homework Review", "The major pitfall in lesson 30 was sending 1MB raw HTML. A11y trees save 97% tokens. However, desktop apps and canvas lack DOM entirely.", "Collect quick answers to the 30-second blitz question."],
    ["Limits of DOM", "Why is DOM not enough? Apps like Photoshop, Excel, terminals, or Figma have zero HTML tags. Visual grounding via screenshots is required.", "Explain the comparative table step-by-step."],
    ["Computer-Use Loop", "The loop spans 4 stages: frame capture, visual reasoning, tool dispatch, and OS driver execution.", "Sketch the execution loop on the smartboard."],
    ["Coordinates & HiDPI", "Retina and 4K displays pack dense pixels. The API normalizes to 1024x768, requiring reverse scaling calculations.", "Walk students through the coordinate scaling formula."],
    ["API Specification", "Review the computer_20241022 tool specification. Available actions: mouse_move, left_click, type, and key.", "Walk through JSON properties and action mechanics."],
    ["Cybersecurity & HITL", "Granting agents raw OS privileges invites catastrophic accidents! Restrict to Docker and enforce Human-in-the-Loop approvals.", "Emphasize security isolation and destructive action gates."],
    ["Python SDK Code", "Explore minimal driver code capturing a desktop frame via PyAutoGUI and querying Claude 3.5 Sonnet.", "Explain steps 1 and 2 in the Python snippet."],
    ["Interactive Simulator", "Watch the agent navigate the desktop, launch Calculator, compute formulas, and write notes in real time.", "Open simulator/index.html and step through the mission."],
    ["Summary & Homework", "We mastered autonomous Computer-Use engineering. The 3-tier homework is ready in vazifa.html for 10 total points.", "Summarize key concepts and assign homework."]
  ]
}

def build_presentation():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    # Replace Title
    tpl = tpl.replace("<title>Taqdimot shabloni — Target Maktabi</title>", "<title>10-11-sinf: Vision Agentlar va Computer-Use</title>")
    
    # Replace Total Slides in meta
    tpl = re.sub(r'name="total-slides"\s+content="\d+"', 'name="total-slides" content="10"', tpl)
    tpl = re.sub(r'id="totalSlides">0</span>', 'id="totalSlides">10</span>', tpl)

    # Replace Stage Content
    stage_regex = r'<div class="stage" id="stage">[\s\S]*?</div>\s*<!-- \.stage -->'
    new_stage = f'<div class="stage" id="stage">\n{SLIDES_HTML}\n  </div><!-- .stage -->'
    tpl = re.sub(stage_regex, lambda m: new_stage, tpl)

    # Replace NOTES Object
    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    notes_regex = r'var NOTES\s*=\s*\{[\s\S]*?\};\s*// \.NOTES'
    tpl = re.sub(notes_regex, lambda m: f'var NOTES = {notes_json};\n// .NOTES', tpl)

    out_path = os.path.join(DEST_DIR, "prezentatsiya.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

def build_worksheet():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Amaliy Ish Varaqasi — Target Maktabi</title>", "<title>Ish Varaqasi: Vision Agentlar va Computer-Use — 10-11-sinf</title>")
    tpl = tpl.replace("1-AMALIY ISH VARAQASI", "31-AMALIY ISH VARAQASI")
    tpl = tpl.replace("Mavzu: Kirish va Vibecoding asoslari", "Mavzu: Vision Agentlar va Computer-Use: Ekran Boshqaruvi va Desktop Avtomatlashtirish")

    # Replace mission / tasks in worksheet
    worksheet_body = """
  <div class="mission-box">
    <div class="mission-title" data-ru="МИССИЯ УРОКА: ИНЖЕНЕРИЯ COMPUTER-USE" data-en="LESSON MISSION: COMPUTER-USE ENGINEERING">DARSNING KIBER-MISSIYASI: COMPUTER-USE ARXITEKTURASI</div>
    <p style="font-size:12px; margin-top:4px;" data-ru="Понять ограничения DOM-подхода, освоить спецификацию Anthropic Computer-Use API, рассчитать формулу масштабирования координат для Retina/4K экранов и разработать защитный фильтр Human-in-the-Loop (HITL) для деструктивных действий." data-en="Master Anthropic Computer-Use API specifications, calculate coordinate translation formulas across HiDPI/Retina screens, and implement Human-in-the-Loop (HITL) safety filters for destructive OS actions.">DOM-yondashuvi chegaralarini tahlil qilish, Anthropic Computer-Use API spetsifikatsiyasini o'rganish, Retina/4K ekranlar uchun koordinata masshtablash formulasini hisoblash va destruktiv buyruqlar uchun Human-in-the-Loop (HITL) xavfsizlik to'sig'ini loyihalash.</p>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">1</span>
      <h3 data-ru="Теоретический Анализ: DOM vs Vision-Based Агенты (2 балла)" data-en="Theoretical Analysis: DOM vs Vision-Based Agents (2 pts)">Nazariy Tahlil: DOM vs Vision-Based Agentlar (2 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Заполните сравнительную таблицу архитектур агентов:" data-en="Complete the agent architecture comparison table:">Agent arxitekturalari taqqoslash jadvalini to'ldiring:</p>
    <table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:11px;">
      <thead>
        <tr style="background:var(--card-bg, #f1f5f9);">
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Параметр" data-en="Feature">Mezon</th>
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="DOM-Агент (Playwright)" data-en="DOM-based Agent">DOM-Agent (Playwright)</th>
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Computer-Use Агент (Anthropic)" data-en="Computer-Use Agent">Computer-Use Agent (Anthropic)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;"><strong>Ko'rish manbasi</strong></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="HTML DOM / A11y Tree" data-en="HTML DOM / A11y Tree">HTML DOM / A11y Tree</td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Скриншот экрана (RGB/Base64)" data-en="Screen Screenshot (RGB/Base64)">________________________</td>
        </tr>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;"><strong>Qo'llanish maydoni</strong></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="Только веб-браузер" data-en="Web browser only">Faqat veb-brauzer</td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Вся ОС (Excel, Терминал, Десктоп)" data-en="Entire OS (Excel, Terminal, Desktop)">________________________</td>
        </tr>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;"><strong>Harakat mexanizmi</strong></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="JS клик по CSS селектору" data-en="JS click by CSS selector">CSS selektor orqali JS chaqiruv</td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Координаты [x, y] мыши и клавиши ОС" data-en="OS mouse [x, y] coordinates & keystrokes">________________________</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">2</span>
      <h3 data-ru="Математический Расчет: Масштабирование Координат (3 балла)" data-en="Mathematical Calculation: Coordinate Scaling (3 pts)">Matematik Hisob: Koordinatalarni Masshtablash (3 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Разработчик запустил модель с виртуальным экраном API: 1024×768. Физический экран ноутбука ученика: 2560×1600 (Retina). Модель вернула клик по координатам [x: 420, y: 310]. Вычислите реальные координаты для мыши ОС:" data-en="The agent operates on API frame 1024×768. The physical display is 2560×1600 (Retina). Model returns target coordinates [x: 420, y: 310]. Calculate the physical OS click coordinates:">Agent API virtual o'lchami 1024×768 da ishlayapti. O'quvchining fizik ekrani esa 2560×1600 (Retina). Model [x: 420, y: 310] nuqtani bosishni buyurdi. Fizik OS koordinatalarini hisoblang:</p>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:10px; margin-top:8px; font-family:monospace; font-size:11px;">
      1) scaleX = Physical_Width / API_Width = 2560 / 1024 = ________<br>
      2) scaleY = Physical_Height / API_Height = 1600 / 768 = ________<br>
      3) Real_X = round(420 * scaleX) = ________<br>
      4) Real_Y = round(310 * scaleY) = ________
    </div>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">3</span>
      <h3 data-ru="Анализ Безопасности: Human-in-the-Loop Защита (3 балла)" data-en="Security Engineering: Human-in-the-Loop Guardrail (3 pts)">Kiberxavfsizlik: HITL Qizil Chiziqlari (3 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Опишите 3 типа действий в операционной системе, которые ИИ-агенту КАТЕГОРИЧЕСКИ ЗАПРЕЩЕНО выполнять без подтверждения пользователя:" data-en="List 3 OS action categories that an autonomous agent is STRICTLY FORBIDDEN to execute without human approval:">AI agentga insonning to'g'ridan-to'g'ri ruxsatisiz bajarishi QAT'IYAN TAQIQLANGAN 3 ta operatsiyani yozing:</p>
    <div style="margin-top:6px; font-size:12px; line-height:1.8;">
      1. ________________________________________________________________________________<br>
      2. ________________________________________________________________________________<br>
      3. ________________________________________________________________________________
    </div>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">4</span>
      <h3 data-ru="Критерии Оценки и Рефлексия (2 балла)" data-en="Evaluation Rubric & Reflection (2 pts)">Baholash Mezoni va Xulosa (2 ball)</h3>
    </div>
    <div style="display:flex; justify-content:space-between; font-size:11px; margin-top:6px;">
      <span>[ ] 1-Daraja: Nazariya & Formula (4 ball)</span>
      <span>[ ] 2-Daraja: PyAutoGUI Kod & Scaling (4 ball)</span>
      <span>[ ] 3-Daraja: HITL Guardrail (2 ball)</span>
    </div>
  </div>
"""
    # Replace content between main tags if needed or inject into container
    tpl = re.sub(r'<div class="sheet">[\s\S]*?</div>\s*<!-- \.sheet -->', lambda m: f'<div class="sheet">\n{worksheet_body}\n</div><!-- .sheet -->', tpl)

    out_path = os.path.join(DEST_DIR, "varaqa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: varaqa.html")

def build_homework():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Vazifa Shabloni — Target Maktabi</title>", "<title>Uy Vazifasi: Vision Agentlar va Computer-Use — 10-11-sinf</title>")
    tpl = tpl.replace("1-AMALIY VAZIFA", "31-AMALIY VAZIFA")
    tpl = tpl.replace("Mavzu: Kirish va Vibecoding Asoslari", "Mavzu: Vision Agentlar va Computer-Use: Ekran Boshqaruvi va Desktop Avtomatlashtirish")

    hw_body = """
  <div class="hw-card">
    <div class="hw-header">
      <span class="badge" style="background:var(--accent); color:#fff;" data-ru="Уровень 1: База (4 балла)" data-en="Tier 1: Core (4 pts)">1-Daraja: Baza (4 ball)</span>
      <h3 data-ru="Конфигурация computer_20241022 и Масштабирование" data-en="Tool Specification & Coordinate Translation">Tool Ta'rifi va Koordinata Masshtabi</h3>
    </div>
    <p style="font-size:13px;" data-ru="Заполните пропуски в коде драйвера для нормализации координат из API (1024×768) в 4K экран (3840×2160):" data-en="Fill in the blanks to correctly scale API coordinates (1024×768) to a native 4K display (3840×2160):">API (1024×768) koordinatalarini 4K displeyga (3840×2160) to'g'ri o'tkazish kodini to'ldiring:</p>
    <div class="code-area">
      <textarea id="codeTier1" rows="7" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="Введите код расчета координат..." data-placeholder-en="Write coordinate scaling code here...">
def translate_coordinates(api_x, api_y, api_w=1024, api_h=768, phys_w=3840, phys_h=2160):
    scale_x = phys_w / api_w
    scale_y = phys_h / api_h
    real_x = round(api_x * scale_x)
    real_y = round(api_y * scale_y)
    return real_x, real_y
</textarea>
    </div>
    <button onclick="testTier1()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--accent); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить расчет" data-en="Verify Calculation">Tekshirish</button>
    <span id="resTier1" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <div class="hw-card" style="margin-top:16px;">
    <div class="hw-header">
      <span class="badge" style="background:var(--success); color:#fff;" data-ru="Уровень 2: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</span>
      <h3 data-ru="Драйвер Выполнения Действий ОС" data-en="OS Action Dispatcher Driver">Harakatlarni Bajaruvchi Drayver</h3>
    </div>
    <p style="font-size:13px;" data-ru="Напишите функцию dispatch_action(action, data), которая обрабатывает команды 'mouse_move', 'left_click', 'type' и 'key':" data-en="Write dispatch_action(action, data) routing 'mouse_move', 'left_click', 'type', and 'key' events:">'mouse_move', 'left_click', 'type' va 'key' buyruqlarini qabul qilib, mos harakatni bajaruvchi drayver funksiyasini yozing:</p>
    <div class="code-area">
      <textarea id="codeTier2" rows="9" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="def dispatch_action(action, data): ..." data-placeholder-en="def dispatch_action(action, data): ...">
def dispatch_action(action, data):
    if action == "mouse_move":
        x, y = data["coordinate"]
        return f"MOVE_TO({x}, {y})"
    elif action == "left_click":
        x, y = data["coordinate"]
        return f"CLICK({x}, {y})"
    elif action == "type":
        return f"TYPE_TEXT('{data['text']}')"
    elif action == "key":
        return f"PRESS_KEY('{data['text']}')"
    return "UNKNOWN_ACTION"
</textarea>
    </div>
    <button onclick="testTier2()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--success); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить диспетчер" data-en="Verify Dispatcher">Drayverni Sinash</button>
    <span id="resTier2" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <div class="hw-card" style="margin-top:16px;">
    <div class="hw-header">
      <span class="badge" style="background:var(--danger); color:#fff;" data-ru="Уровень 3: Челлендж (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</span>
      <h3 data-ru="HITL Guardrail Защитный Фильтр" data-en="HITL Security Interceptor Gate">HITL Xavfsizlik Qalqoni</h3>
    </div>
    <p style="font-size:13px;" data-ru="Реализуйте функцию validate_safety(action, text), которая возвращает False (Блокировка), если в тексте содержатся опасные ключевые слова ('rm -rf', 'format', 'delete_account', 'transfer_money'):" data-en="Implement validate_safety(action, text) returning False (BLOCKED) whenever dangerous keywords ('rm -rf', 'format', 'delete_account', 'transfer_money') appear:">Agar harakat matnida xavfli so'zlar ('rm -rf', 'format', 'delete_account', 'transfer_money') uchrasa, harakatni to'xtatib False qaytaruvchi xavfsizlik funksiyasini yozing:</p>
    <div class="code-area">
      <textarea id="codeTier3" rows="8" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="def validate_safety(action, text): ..." data-placeholder-en="def validate_safety(action, text): ...">
def validate_safety(action, text):
    danger_keywords = ["rm -rf", "format", "delete_account", "transfer_money", "drop database"]
    for word in danger_keywords:
        if word in text.lower():
            return False  # BLOCKED - Requires Human-in-the-Loop Confirmation
    return True  # SAFE
</textarea>
    </div>
    <button onclick="testTier3()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--danger); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить защиту" data-en="Test Guardrail">Qalqonni Sinash</button>
    <span id="resTier3" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <script>
    function testTier1() {
      var txt = document.getElementById('codeTier1').value;
      var res = document.getElementById('resTier1');
      if (txt.includes('phys_w / api_w') && txt.includes('phys_h / api_h') && txt.includes('round(')) {
        res.textContent = "✅ To'g'ri! Masshtab koeffitsientlari mukammal hisoblandi (+4 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: phys_w / api_w va round() funksiyalaridan foydalaning!";
        res.style.color = "var(--danger)";
      }
    }

    function testTier2() {
      var txt = document.getElementById('codeTier2').value;
      var res = document.getElementById('resTier2');
      if (txt.includes('mouse_move') && txt.includes('left_click') && txt.includes('type') && txt.includes('key')) {
        res.textContent = "✅ Ajoyib! Harakat drayveri barcha amallarni to'g'ri ajratdi (+4 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: mouse_move, left_click, type va key holatlarini tekshiring!";
        res.style.color = "var(--danger)";
      }
    }

    function testTier3() {
      var txt = document.getElementById('codeTier3').value;
      var res = document.getElementById('resTier3');
      if (txt.includes('rm -rf') && txt.includes('delete') && txt.includes('False')) {
        res.textContent = "✅ Mukammal! Destruktiv xavflar aniqlandi va HITL to'sig'i qo'yildi (+2 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: 'rm -rf' yoki 'delete' kabi xavfli so'zlarni filtrlang!";
        res.style.color = "var(--danger)";
      }
    }
  </script>
"""
    tpl = re.sub(r'<div class="hw-container">[\s\S]*?</div>\s*<!-- \.hw-container -->', lambda m: f'<div class="hw-container">\n{hw_body}\n</div><!-- .hw-container -->', tpl)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    doc = """# O'qituvchi Qo'llanmasi (Teacher Reading)
## 10–11-sinf · 12-hafta · 31-dars
### Mavzu: Multi-Modal Vision Agentlar va Computer-Use: Ekran Boshqaruvi va Desktop Avtomatlashtirish
**Dars formati:** Yakka Dars (Single Block — 40 daqiqa)

---

### 1. Darsning Pedagogik Maqsadi va Falsafasi
O'tgan 30-darsda o'quvchilar brauzer ichida Playwright va Accessibility Tree orqali veb-sahifalarni tahlil qilishni o'rgandilar.
Bugungi 31-darsning vazifasi — o'quvchilarga DOM faqat brauzer bilan cheklanganini, ammo real biznesda korporativ dasturlar (Excel, Photoshop, Terminal, ERP, buxgalteriya dasturlari) mavjud bo'lib, ularda DOM umuman yo'qligini tushuntirishdir.
Anthropic tomonidan taqdim etilgan **Computer-Use** arxitekturasi AI agentga inson kabi ko'rish (Vision VLM) va klaviatura/sichqoncha orqali butun operatsion tizimni boshqarish imkonini beradi.

---

### 2. Vaqt Taqsimoti (40 Daqiqalik Aniq Reja)

| Daqiqa | Bosqich | O'qituvchi Faoliyati | O'quvchi Faoliyati |
|---|---|---|---|
| **00:00–04:00** | Kirish va Titul | Mavzuni e'lon qilish, dars maqsadi va kutilayotgan natijani ko'rsatish | Diqqatni jamlash, daftarga mavzuni yozish |
| **04:00–09:00** | 30-Dars Uy Vazifasi Tahlili | Keng tarqalgan xato (1.2 MB HTML yuborish), A11y afzalligi va 30 sek blitz savol | Blits savolga javob berish, xatolar tahlili |
| **09:00–14:00** | Nega DOM yetarli emas? | Canvas, Desktop dasturlar va OS chegaralarini tushuntirish | DOM va Vision farqlarini solishtirish |
| **14:00–19:00** | Computer-Use Tsikli | Screenshot -> VLM -> Action -> Observation zanjirini ko'rsatish | Tsikl ketma-ketligini tahlil qilish |
| **19:00–24:00** | Koordinatalar va HiDPI | Retina / 4K masshtab formulasi (scaleX, scaleY) va hisob-kitob | Formulani daftarga yozish, hisoblash |
| **24:00–28:00** | API Spetsifikatsiyasi | computer_20241022 JSON sxemasi va action turlari | Tool chaqiruv sintaksisini ko'rish |
| **28:00–32:00** | Kiberxavfsizlik va HITL | Docker izolyatsiyasi va inson tasdig'i (HITL) qoidalarini singdirish | Qaysi buyruqlar xavfli ekanini muhokama qilish |
| **32:00–35:00** | Python SDK Kodu | PyAutoGUI + Claude 3.5 Sonnet kodini ko'rsatish | Kod arxitekturasini o'rganish |
| **35:00–38:00** | Amaliy Simulyator | `simulator/index.html` da Kalkulyator va Notes missiyasini namoyish etish | Simulyatorda agent qadamlarini kuzatish |
| **38:00–40:00** | Xulosa va Uy Vazifasi | 3 darajali topshiriqni tushuntirish va darsni yakunlash | Vazifani belgilab olish |

---

### 3. Savol-Javob va Interaktiv Fikrlar

1. **Savol:** Nega neyrotarmoqqa 4K (3840×2160) tasvirni to'g'ridan-to'g'ri yuborish yomon g'oya?
   - **Javob:** Katta tasvirlar kontekst oynasini tezda to'ldiradi (har qadamda 2,000+ token), internet trafigini oshiradi va javob qaytish tezligini (latency) 5-10 soniyagacha sekinlashtiradi. Shu sababli 1024×768 ga siqiladi.
2. **Savol:** Nega agentni o'z shaxsiy Mac yoki Windows kompyuteringizda to'g'ridan-to'g'ri ishlatish xavfli?
   - **Javob:** Ko'rish xatosi yoki gallyutsinatsiya tufayli agent "Terminal" ochib tizim fayllarini o'chirib yuborishi (`rm -rf`) yoki shaxsiy xatlarni tarqatib yuborishi mumkin. Faqat Docker / Xvfb virtual qumloqda ishlatilishi shart.
3. **Savol:** Human-in-the-Loop (HITL) nima?
   - **Javob:** Agent moliyaviy operatsiya yoki fayllarni qaytarib bo'lmas darajada o'chirishdan oldin inson tasdig'ini (Confirmation Dialog) so'rashi shart bo'lgan xavfsizlik to'sig'i.
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("  ✓ Created: TEACHER_READING.md")

def build_simulator():
    html = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Симулятор Компьютера и ОС: Vision Agent" data-en="OS Desktop Simulator: Vision Agent">Desktop OS Sandbox: Vision Computer-Use Agent</title>
  <style>
    :root {
      --bg: #0b0f19;
      --panel: #111827;
      --card: #1f2937;
      --border: #374151;
      --ink: #f9fafb;
      --ink-dim: #9ca3af;
      --accent: #3b82f6;
      --accent-hover: #2563eb;
      --success: #22c55e;
      --danger: #ef4444;
      --warning: #eab308;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg);
      color: var(--ink);
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    header {
      background: var(--panel);
      border-bottom: 1px solid var(--border);
      padding: 10px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .badge-sub {
      background: rgba(59,130,246,0.2);
      color: var(--accent);
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 700;
    }
    .main-grid {
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 340px;
      overflow: hidden;
    }
    /* Simulated OS Desktop */
    .desktop-area {
      position: relative;
      background: radial-gradient(circle at 50% 50%, #1e293b 0%, #0f172a 100%);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .desktop-icons {
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      z-index: 2;
    }
    .os-icon {
      width: 72px;
      display: flex;
      flex-direction: column;
      align-items: center;
      cursor: pointer;
      user-select: none;
      padding: 6px;
      border-radius: 8px;
    }
    .os-icon:hover { background: rgba(255,255,255,0.1); }
    .os-icon .ico { font-size: 32px; }
    .os-icon .label { font-size: 11px; margin-top: 4px; text-align: center; }

    /* Floating OS Windows */
    .os-window {
      position: absolute;
      background: #1e293b;
      border: 1px solid #475569;
      border-radius: 8px;
      box-shadow: 0 20px 25px -5px rgba(0,0,0,0.5);
      z-index: 10;
      display: none;
      flex-direction: column;
      overflow: hidden;
    }
    .win-header {
      background: #334155;
      padding: 6px 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      font-weight: 600;
      cursor: move;
    }
    .win-controls { display: flex; gap: 6px; }
    .win-btn { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
    .win-btn.close { background: #ef4444; }
    .win-btn.min { background: #eab308; }
    .win-btn.max { background: #22c55e; }
    .win-content { padding: 12px; }

    /* Calculator Specifics */
    #winCalc { width: 220px; top: 80px; left: 160px; }
    .calc-screen {
      background: #0f172a;
      border: 1px solid #334155;
      color: #38bdf8;
      font-family: monospace;
      font-size: 18px;
      padding: 8px;
      text-align: right;
      border-radius: 4px;
      margin-bottom: 8px;
    }
    .calc-keys {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 4px;
    }
    .calc-btn {
      background: #475569;
      color: #fff;
      border: none;
      padding: 8px 0;
      border-radius: 4px;
      font-weight: 700;
      cursor: pointer;
      font-size: 12px;
    }
    .calc-btn.op { background: var(--accent); }

    /* Notes App Specifics */
    #winNotes { width: 280px; top: 120px; left: 420px; }
    .notes-area {
      width: 100%;
      height: 120px;
      background: #0f172a;
      border: 1px solid #334155;
      color: #fff;
      padding: 8px;
      font-family: monospace;
      font-size: 11px;
      border-radius: 4px;
      resize: none;
    }

    /* Virtual Mouse Cursor */
    #virtualCursor {
      position: absolute;
      width: 24px;
      height: 24px;
      pointer-events: none;
      z-index: 100;
      transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);
      transform: translate(-4px, -4px);
    }
    .cursor-dot {
      width: 10px;
      height: 10px;
      background: var(--success);
      border: 2px solid #fff;
      border-radius: 50%;
      box-shadow: 0 0 10px var(--success);
    }
    .cursor-coord {
      position: absolute;
      left: 14px;
      top: -6px;
      background: rgba(0,0,0,0.8);
      color: #38bdf8;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 10px;
      font-family: monospace;
      white-space: nowrap;
    }

    /* Side Control Panel */
    .agent-panel {
      background: var(--panel);
      border-left: 1px solid var(--border);
      display: flex;
      flex-direction: column;
    }
    .agent-panel-header {
      padding: 14px;
      border-bottom: 1px solid var(--border);
    }
    .console-logs {
      flex: 1;
      padding: 12px;
      background: #0b0f19;
      font-family: monospace;
      font-size: 11px;
      overflow-y: auto;
      line-height: 1.6;
    }
    .log-item { margin-bottom: 8px; padding-bottom: 6px; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .log-thought { color: #a855f7; }
    .log-action { color: #38bdf8; }
    .log-hitl { color: #ef4444; font-weight: 700; background: rgba(239,68,68,0.1); padding: 4px; border-radius: 4px; }

    /* Taskbar */
    .os-taskbar {
      margin-top: auto;
      height: 38px;
      background: rgba(15, 23, 42, 0.9);
      border-top: 1px solid #334155;
      display: flex;
      align-items: center;
      padding: 0 14px;
      gap: 12px;
      z-index: 50;
    }
  </style>
</head>
<body>

<header>
  <div style="display:flex; align-items:center; gap:12px;">
    <strong data-ru="Computer-Use Студия ОС" data-en="Computer-Use OS Studio">Computer-Use OS Studio</strong>
    <span class="badge-sub" data-ru="Claude 3.5 Sonnet Vision" data-en="Claude 3.5 Sonnet Vision">Claude 3.5 Sonnet Vision</span>
  </div>
  <div style="display:flex; gap:10px;">
    <button onclick="toggleLang()" class="calc-btn" style="padding:4px 10px; background:#374151;" id="langBtn" data-ru="UZ / RU / EN" data-en="UZ / RU / EN">UZ / RU / EN</button>
    <button onclick="runAgentMission()" class="calc-btn op" style="padding:4px 14px;" id="btnRun" data-ru="▶️ Запустить Агента" data-en="▶️ Start Agent">▶️ Agentni Boshlash</button>
    <button onclick="resetDesktop()" class="calc-btn" style="padding:4px 10px; background:#475569;" data-ru="Сброс" data-en="Reset">Qayta yuklash</button>
  </div>
</header>

<div class="main-grid">
  <!-- Simulated OS Desktop -->
  <div class="desktop-area" id="desktop">
    <!-- Desktop Icons -->
    <div class="desktop-icons">
      <div class="os-icon" id="iconCalc" onclick="openWindow('winCalc')">
        <div class="ico">🧮</div>
        <div class="label" data-ru="Калькулятор" data-en="Calculator">Kalkulyator</div>
      </div>
      <div class="os-icon" id="iconNotes" onclick="openWindow('winNotes')">
        <div class="ico">📝</div>
        <div class="label" data-ru="Блокнот" data-en="Notes">Notes</div>
      </div>
      <div class="os-icon" id="iconTrash">
        <div class="ico">🗑️</div>
        <div class="label" data-ru="Корзина" data-en="Trash">Savat</div>
      </div>
    </div>

    <!-- Calculator Window -->
    <div class="os-window" id="winCalc">
      <div class="win-header">
        <span data-ru="Калькулятор" data-en="Calculator">Kalkulyator</span>
        <div class="win-controls">
          <span class="win-btn min"></span>
          <span class="win-btn max"></span>
          <span class="win-btn close" onclick="closeWindow('winCalc')"></span>
        </div>
      </div>
      <div class="win-content">
        <div class="calc-screen" id="calcScreen">0</div>
        <div class="calc-keys">
          <button class="calc-btn" onclick="pressCalc('C')">C</button>
          <button class="calc-btn" onclick="pressCalc('/')">/</button>
          <button class="calc-btn" onclick="pressCalc('*')">*</button>
          <button class="calc-btn op" onclick="pressCalc('-')">-</button>
          <button class="calc-btn" onclick="pressCalc('7')">7</button>
          <button class="calc-btn" onclick="pressCalc('8')">8</button>
          <button class="calc-btn" onclick="pressCalc('9')">9</button>
          <button class="calc-btn op" onclick="pressCalc('+')">+</button>
          <button class="calc-btn" onclick="pressCalc('4')">4</button>
          <button class="calc-btn" onclick="pressCalc('5')">5</button>
          <button class="calc-btn" onclick="pressCalc('6')">6</button>
          <button class="calc-btn op" onclick="pressCalc('=')">=</button>
          <button class="calc-btn" onclick="pressCalc('1')">1</button>
          <button class="calc-btn" onclick="pressCalc('2')">2</button>
          <button class="calc-btn" onclick="pressCalc('3')">3</button>
          <button class="calc-btn" onclick="pressCalc('0')">0</button>
        </div>
      </div>
    </div>

    <!-- Notes Window -->
    <div class="os-window" id="winNotes">
      <div class="win-header">
        <span data-ru="Блокнот (Notes.txt)" data-en="Notes.txt">Notes.txt</span>
        <div class="win-controls">
          <span class="win-btn min"></span>
          <span class="win-btn max"></span>
          <span class="win-btn close" onclick="closeWindow('winNotes')"></span>
        </div>
      </div>
      <div class="win-content">
        <textarea class="notes-area" id="notesArea" placeholder="Hisobot matni..." data-placeholder-ru="Текст отчета..." data-placeholder-en="Report text..."></textarea>
      </div>
    </div>

    <!-- Virtual Mouse -->
    <div id="virtualCursor" style="left: 50px; top: 50px;">
      <div class="cursor-dot"></div>
      <div class="cursor-coord" id="cursorCoord">[x: 50, y: 50]</div>
    </div>

    <!-- Taskbar -->
    <div class="os-taskbar">
      <div style="font-weight:700; font-size:12px; color:var(--accent);">TargetOS v2.4</div>
      <div style="font-size:11px; color:#64748b;" id="tbStatus" data-ru="Система готова" data-en="System ready">Tizim tayyor</div>
      <div style="margin-left:auto; font-size:11px; font-family:monospace; color:#94a3b8;">12:00 PM</div>
    </div>
  </div>

  <!-- Agent Telemetry & Log Console -->
  <div class="agent-panel">
    <div class="agent-panel-header">
      <h3 style="font-size:13px;" data-ru="Телеметрия Агента" data-en="Agent Telemetry">Agent Telemetriyasi</h3>
      <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:11px; color:var(--ink-dim);">
        <div><span data-ru="Шаги:" data-en="Steps:">Qadamlar:</span> <strong id="telSteps" style="color:#fff;">0 / 6</strong></div>
        <div><span data-ru="Токены:" data-en="Tokens:">Tokenlar:</span> <strong id="telTokens" style="color:#fff;">0</strong></div>
      </div>
    </div>
    <div class="console-logs" id="consoleLogs">
      <div style="color:#64748b;" data-ru="[Ожидание] Нажмите 'Запустить Агента' для симуляции." data-en="[Waiting] Press 'Start Agent' to begin OS simulation.">[Kutilmoqda] Boshlash uchun "Agentni Boshlash" tugmasini bosing.</div>
    </div>
  </div>
</div>

<script>
var curLang = 'uz';
var running = false;

function toggleLang() {
  if (curLang === 'uz') curLang = 'ru';
  else if (curLang === 'ru') curLang = 'en';
  else curLang = 'uz';
  document.getElementById('langBtn').textContent = curLang.toUpperCase();
  applyLang();
}

function applyLang() {
  var els = document.querySelectorAll('[data-ru]');
  els.forEach(function(el) {
    if (curLang === 'ru') el.textContent = el.getAttribute('data-ru');
    else if (curLang === 'en') el.textContent = el.getAttribute('data-en');
  });
}

function openWindow(id) {
  var w = document.getElementById(id);
  if (w) w.style.display = 'flex';
}
function closeWindow(id) {
  var w = document.getElementById(id);
  if (w) w.style.display = 'none';
}
function pressCalc(val) {
  var s = document.getElementById('calcScreen');
  if (val === 'C') s.textContent = '0';
  else if (val === '=') {
    try { s.textContent = eval(s.textContent); } catch(e) { s.textContent = 'ERR'; }
  } else {
    if (s.textContent === '0' || s.textContent === 'ERR') s.textContent = val;
    else s.textContent += val;
  }
}

function moveMouse(x, y, callback) {
  var cur = document.getElementById('virtualCursor');
  var label = document.getElementById('cursorCoord');
  cur.style.left = x + 'px';
  cur.style.top = y + 'px';
  label.textContent = '[x: ' + x + ', y: ' + y + ']';
  setTimeout(callback, 600);
}

function logEvent(type, msg) {
  var c = document.getElementById('consoleLogs');
  var d = document.createElement('div');
  d.className = 'log-item';
  if (type === 'thought') d.innerHTML = '<span class="log-thought">🤔 [Thought]:</span> ' + msg;
  else if (type === 'action') d.innerHTML = '<span class="log-action">⚡ [Tool Call]:</span> ' + msg;
  else if (type === 'hitl') d.innerHTML = '<span class="log-hitl">🛡️ [HITL Intercept]:</span> ' + msg;
  else d.textContent = msg;
  c.appendChild(d);
  c.scrollTop = c.scrollHeight;
}

function runAgentMission() {
  if (running) return;
  running = true;
  document.getElementById('btnRun').disabled = true;
  document.getElementById('btnRun').style.opacity = '0.5';

  var c = document.getElementById('consoleLogs');
  c.innerHTML = '';
  document.getElementById('telSteps').textContent = '1 / 6';
  document.getElementById('telTokens').textContent = '1,650';

  // Step 1: Open Calculator
  logEvent('thought', 'Ish stolidan Kalkulyator ikonkasini qidiryapman. Koordinata: [x: 48, y: 48].');
  moveMouse(48, 48, function() {
    logEvent('action', 'computer.left_click([48, 48])');
    openWindow('winCalc');
    document.getElementById('telSteps').textContent = '2 / 6';
    document.getElementById('telTokens').textContent = '3,200';

    // Step 2: Calculate 125 * 8
    setTimeout(function() {
      logEvent('thought', 'Kalkulyator ochildi. 125 * 8 kiritishim kerak.');
      moveMouse(230, 210, function() {
        document.getElementById('calcScreen').textContent = '125*8';
        logEvent('action', 'computer.type("125*8")');
        
        setTimeout(function() {
          moveMouse(290, 240, function() {
            logEvent('action', 'computer.left_click([290, 240]) -> "=" tugmasi');
            pressCalc('='); // 1000
            document.getElementById('telSteps').textContent = '3 / 6';
            document.getElementById('telTokens').textContent = '4,850';

            // Step 3: Open Notes
            setTimeout(function() {
              logEvent('thought', 'Natija 1000 chiqdi. Endi Notes matn muharririni ochaman.');
              moveMouse(48, 110, function() {
                logEvent('action', 'computer.left_click([48, 110])');
                openWindow('winNotes');
                document.getElementById('telSteps').textContent = '4 / 6';
                document.getElementById('telTokens').textContent = '6,400';

                // Step 4: Write to Notes
                setTimeout(function() {
                  moveMouse(460, 180, function() {
                    logEvent('action', 'computer.type("Jami hisob: 1000 so\'m")');
                    document.getElementById('notesArea').value = "Jami hisob: 1000 so'm\\nHolat: Tasdiqlandi.";
                    document.getElementById('telSteps').textContent = '5 / 6';
                    document.getElementById('telTokens').textContent = '7,950';

                    // Step 5: HITL Security Trigger
                    setTimeout(function() {
                      logEvent('thought', 'Faylni o\'chirish buyrug\'i (rm notes.txt) berilmoqda.');
                      logEvent('hitl', 'XAVF: Destruktiv amal aniqlandi! Inson tasdig\'i talab qilinadi.');
                      document.getElementById('telSteps').textContent = '6 / 6';
                      document.getElementById('tbStatus').textContent = 'To\'xtatildi (HITL Guard)';
                      document.getElementById('tbStatus').style.color = '#ef4444';
                      running = false;
                      document.getElementById('btnRun').disabled = false;
                      document.getElementById('btnRun').style.opacity = '1';
                    }, 1200);

                  });
                }, 1000);

              });
            }, 1000);

          });
        }, 800);

      });
    }, 1000);

  });
}

function resetDesktop() {
  running = false;
  closeWindow('winCalc');
  closeWindow('winNotes');
  document.getElementById('calcScreen').textContent = '0';
  document.getElementById('notesArea').value = '';
  document.getElementById('consoleLogs').innerHTML = '<div style="color:#64748b;">[Qayta yuklandi] Boshlash uchun "Agentni Boshlash" tugmasini bosing.</div>';
  document.getElementById('telSteps').textContent = '0 / 6';
  document.getElementById('telTokens').textContent = '0';
  document.getElementById('tbStatus').textContent = 'Tizim tayyor';
  document.getElementById('tbStatus').style.color = '#64748b';
  document.getElementById('btnRun').disabled = false;
  document.getElementById('btnRun').style.opacity = '1';
  var cur = document.getElementById('virtualCursor');
  cur.style.left = '50px';
  cur.style.top = '50px';
  document.getElementById('cursorCoord').textContent = '[x: 50, y: 50]';
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
    print("📦 Building 10-11-sinf (Lesson 31: Multi-Modal Vision Agents & Computer-Use)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_simulator()
    print("🎉 Done! Generated Grade 10–11 Lesson 31.")

if __name__ == "__main__":
    main()
