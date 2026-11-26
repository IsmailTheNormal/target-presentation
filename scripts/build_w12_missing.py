#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_w12_missing.py — completes the two Week 12 decks that were left
as generic scaffolds: 10-11 / Lesson 31 (Computer-Use) and 9 / Lesson 35 (NPM).

It reuses the canonical shell (CSS, touch controller, i18n engine, dock) from
the already finished decks of the same cohort and only replaces the slide stage
and the teacher NOTES object.
"""

import json
import os
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def slide(index, phase, time_value, inner, first=False):
    cls = "slide is-on" if first else "slide"
    return (
        f'  <section class="{cls}" data-phase="{phase}" data-time="{time_value}" '
        f'data-slide-index="{index}">\n{inner}\n  </section>'
    )


def build_deck(base_path, dest_path, slides, notes):
    with open(base_path, encoding="utf-8") as fh:
        html = fh.read()

    start = html.index('<div class="stage">') + len('<div class="stage">')
    end = html.index('</div><!-- /stage -->')
    html = html[:start] + "\n\n" + slides + "\n\n" + html[end:]

    notes_json = json.dumps(notes, ensure_ascii=False, indent=2)
    html, count = re.subn(
        r"var NOTES = \{[\s\S]*?\n\};",
        "var NOTES = " + notes_json + ";",
        html,
        count=1,
    )
    if count != 1:
        raise RuntimeError("NOTES block not found in " + base_path)

    with open(dest_path, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote", dest_path, len(html), "bytes")


# =============================================================================
# 10–11-SINF · 12-HAFTA · 31-DARS — Multi-Modal Vision Agents & Computer-Use
# =============================================================================
S10 = []

S10.append(slide(0, "Kirish|Введение|Intro", "00:00–03:00", """
    <div class="eyebrow"><span class="t" data-ru="10–11-КЛАСС · 12-Я НЕДЕЛЯ · УРОК 31" data-en="GRADES 10–11 · WEEK 12 · LESSON 31">10–11-SINF · 12-HAFTA · 31-DARS</span></div>
    <h1 class="display" data-ru="Мультимодальные Vision-Агенты и Computer-Use: Управление Экраном и Автоматизация Рабочего Стола" data-en="Multi-Modal Vision Agents & Computer-Use: Screen Control & Desktop Automation">Multi-Modal Vision Agentlar va Computer-Use: Ekran Boshqaruvi va Desktop Avtomatlashtirish</h1>
    <p class="lede" data-ru="Выходим за пределы DOM: агент видит экран как человек, находит кнопки по пикселям и управляет любым приложением — от калькулятора до Excel и Photoshop." data-en="Beyond the DOM: the agent sees the screen like a human, grounds buttons in pixels, and drives any application — from Calculator to Excel and Photoshop.">DOM chegarasidan chiqamiz: agent ekranni inson kabi ko'radi, tugmalarni piksellar bo'yicha topadi va har qanday ilovani — kalkulyatordan Excel va Photoshop gacha — boshqaradi.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">Yakka Dars · 40 daqiqa</div>
        <h3 data-ru="От DOM к Операционной Системе" data-en="From DOM to the Operating System">DOM'dan Operatsion Tizimga</h3>
        <p data-ru="Браузерные селекторы не работают в нативных приложениях. Учимся управлять экраном через скриншоты и координаты." data-en="Browser selectors do not exist in native apps. We learn to drive the screen through screenshots and coordinates.">Brauzer selektorlari native ilovalarda ishlamaydi. Ekranni skrinshot va koordinatalar orqali boshqarishni o'rganamiz.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Практический результат" data-en="Deliverable">Desktop OS Agent</div>
        <h3 data-ru="Калькулятор + Текстовый Редактор" data-en="Calculator + Text Editor">Kalkulyator + Matn Muharriri</h3>
        <p data-ru="Агент открывает калькулятор, считает 125 × 48 и записывает результат в текстовый файл — без единого DOM-селектора." data-en="The agent opens Calculator, computes 125 × 48, and writes the result into a text file — without a single DOM selector.">Agent kalkulyatorni ochadi, 125 × 48 ni hisoblaydi va natijani matn fayliga yozadi — birorta DOM selektorisiz.</p>
      </div>
    </div>
""", first=True))

S10.append(slide(1, "Tahlil|Разбор|Review", "03:00–10:00", """
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 30-УРОКА" data-en="LESSON 30 HOMEWORK REVIEW">30-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Разбор 30-урока: Ловушки Browser-Use и CAPTCHA" data-en="Lesson 30 Review: Browser-Use & CAPTCHA Traps">30-dars Tahlili: Browser-Use'dagi DOM va CAPTCHA Xatolari</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Типичная Ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Клик по устаревшему DOM-селектору" data-en="Clicking a Stale DOM Selector">Eskirgan DOM Selektoriga Bosish</h3>
        <p data-ru="SPA перерисовала страницу, а агент всё ещё держит старый ElementHandle. Селектор возвращает null, и агент молча кликает в пустоту или падает." data-en="The SPA re-rendered the page while the agent still holds an old ElementHandle. The selector returns null, so the agent silently clicks empty space or crashes.">SPA sahifani qayta chizdi, agent esa eski ElementHandle'ni ushlab turibdi. Selektor null qaytaradi va agent jimgina bo'sh joyga bosadi yoki yiqiladi.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#ef4444;">// XATO: sahifa yangilanganini tekshirmaslik</span>
await page.click('#buy-btn'); <span style="color:#ef4444;">// null → timeout</span>
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Золотой Стандарт" data-en="Golden Standard">Oltin Standart (Best Practice)</div>
        <h3 data-ru="Accessibility Tree + Set-of-Mark + HITL" data-en="Accessibility Tree + Set-of-Mark + HITL">Daraxt + Belgilash + Inson Tasdig'i</h3>
        <p data-ru="Сначала ждём стабильный DOM, затем строим компактное accessibility tree, накладываем номера (Set-of-Mark) и останавливаемся на CAPTCHA для человека." data-en="Wait for a stable DOM, build a compact accessibility tree, overlay numbered marks (Set-of-Mark), and stop at CAPTCHA for a human.">Avval barqaror DOMni kutamiz, keyin ixcham accessibility tree quramiz, ustiga raqamlar qo'yamiz (Set-of-Mark) va CAPTCHA'da inson uchun to'xtaymiz.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#22c55e;">// TO'G'RI: barqaror holat + HITL</span>
await page.waitForLoadState('networkidle');
const tree = await page.accessibility.snapshot();
if (captchaVisible) return askHuman();
        </div>
      </div>
    </div>
    <div class="grid-2" style="margin-top:14px;">
      <div class="box">
        <span class="badge" data-ru="Блиц-вопрос (30 сек)" data-en="Blitz Question (30s)">Blitz Savol</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="Почему 1 МБ HTML выгоднее сжать до 5 КБ accessibility tree, а не отправлять модели целиком?" data-en="Why compress 1 MB of HTML into a 5 KB accessibility tree instead of sending the raw page to the model?">Nega 1 MB HTMLni modelga to'liq yuborishdan ko'ra 5 KB accessibility tree'ga siqish foydali?</p>
      </div>
      <div class="box">
        <span class="badge" data-ru="Мост к теме" data-en="Bridge to Today">Bugungi Mavzuga Ko'prik</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="А что делать, если DOM вообще нет — Figma, Excel, калькулятор, терминал? Ответ: Computer-Use, где агент видит пиксели экрана." data-en="But what if there is no DOM at all — Figma, Excel, Calculator, Terminal? Answer: Computer-Use, where the agent sees screen pixels.">Agar DOM umuman bo'lmasa-chi — Figma, Excel, kalkulyator, terminal? Javob: Computer-Use, agent ekran piksellarini ko'radi.</p>
      </div>
    </div>
"""))

S10.append(slide(2, "Konsept|Концепт|Concept", "10:00–15:00", """
    <div class="eyebrow"><span class="t" data-ru="ГРАНИЦЫ DOM · ТРИ РАЗНЫХ МИРА" data-en="BEYOND THE DOM · THREE DIFFERENT WORLDS">DOM CHEGARASIDAN TASHQARI · UCH XIL DUNYO</span></div>
    <h2 data-ru="Почему DOM Недостаточно: Три Уровня Интерфейсов" data-en="Why the DOM Is Not Enough: Three Interface Layers">Nega DOM Yetarli Emas? Uch Xil Interfeys Qatlami</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Уровень 1" data-en="Layer 1">Web DOM</div>
        <h3 data-ru="Обычные сайты" data-en="Classic Websites">Oddiy Veb-Saytlar</h3>
        <p data-ru="Playwright и Browser-Use читают HTML, роли ARIA и селекторы. Это самый простой и надёжный уровень." data-en="Playwright and Browser-Use read HTML, ARIA roles, and selectors. This is the simplest and most reliable layer.">Playwright va Browser-Use HTML, ARIA rollari va selektorlarni o'qiydi. Bu eng sodda va ishonchli qatlam.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(234,179,8,0.15); color:var(--warning);" data-ru="Уровень 2" data-en="Layer 2">Canvas / WebGL</div>
        <h3 data-ru="Figma, Карты, Игры" data-en="Figma, Maps, Games">Figma, Xaritalar, O'yinlar</h3>
        <p data-ru="Внутри canvas нет отдельных кнопок — только пиксели. DOM-селектор здесь бессилен, нужна визуальная наводка." data-en="Inside canvas there are no individual buttons — only pixels. DOM selectors are useless here; visual grounding is required.">Canvas ichida alohida tugmalar yo'q — faqat piksellar. DOM selektori bu yerda kuchsiz, vizual nishonlash kerak.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Уровень 3" data-en="Layer 3">Desktop OS</div>
        <h3 data-ru="Excel, Photoshop, Терминал" data-en="Excel, Photoshop, Terminal">Excel, Photoshop, Terminal</h3>
        <p data-ru="Нативные приложения вообще не отдают DOM. Агент может работать только через скриншот, мышь и клавиатуру." data-en="Native applications expose no DOM at all. The agent can only work through screenshots, mouse, and keyboard.">Native ilovalar umuman DOM bermaydi. Agent faqat skrinshot, sichqoncha va klaviatura orqali ishlay oladi.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px;">
      <strong data-ru="Computer-Use = зрение + руки:" data-en="Computer-Use = eyes + hands:">Computer-Use = ko'z + qo'l:</strong>
      <p style="font-size:12px; margin-top:4px;" data-ru="Агент делает скриншот (зрение), модель возвращает координаты и действие (решение), PyAutoGUI или драйвер ОС выполняет клик (руки)." data-en="The agent takes a screenshot (eyes), the model returns coordinates and an action (decision), and PyAutoGUI or an OS driver performs the click (hands).">Agent skrinshot oladi (ko'z), model koordinata va harakatni qaytaradi (qaror), PyAutoGUI yoki OS drayveri klikni bajaradi (qo'l).</p>
    </div>
"""))

S10.append(slide(3, "Arxitektura|Архитектура|Architecture", "15:00–20:00", """
    <div class="eyebrow"><span class="t" data-ru="ANTHROPIC COMPUTER-USE API · ЦИКЛ ДЕЙСТВИЙ" data-en="ANTHROPIC COMPUTER-USE API · ACTION LOOP">ANTHROPIC COMPUTER-USE API · HARAKATLAR TSIKLI</span></div>
    <h2 data-ru="Computer-Use API: Скриншот → Решение → Действие" data-en="Computer-Use API: Screenshot → Decision → Action">Computer-Use API: Skrinshot → Qaror → Harakat</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Четыре Шага Цикла" data-en="Four Steps of the Loop">Tsiklning To'rt Bosqichi</h3>
        <ol style="font-size:12px; line-height:1.8; margin-top:8px; padding-left:18px;">
          <li data-ru="Скриншот текущего экрана отправляется модели как изображение." data-en="A screenshot of the current screen is sent to the model as an image.">Joriy ekran skrinshoti modelga rasm sifatida yuboriladi.</li>
          <li data-ru="Модель возвращает tool_use с действием и координатами [x, y]." data-en="The model returns tool_use with an action and [x, y] coordinates.">Model harakat va [x, y] koordinatalari bilan tool_use qaytaradi.</li>
          <li data-ru="Драйвер выполняет клик, ввод текста или нажатие клавиши." data-en="The driver performs a click, text input, or key press.">Drayver klik, matn kiritish yoki tugma bosishni bajaradi.</li>
          <li data-ru="Делается новый скриншот, и цикл повторяется до готового результата." data-en="A fresh screenshot is taken, and the loop repeats until the task is done.">Yangi skrinshot olinadi va natija tayyor bo'lguncha tsikl takrorlanadi.</li>
        </ol>
      </div>
      <div class="card">
        <h3 data-ru="Ответ Модели (tool_use)" data-en="Model Response (tool_use)">Model Javobi (tool_use)</h3>
        <div class="code-block" style="font-size:10.5px; line-height:1.55; margin-top:8px;">
{
  "role": "assistant",
  "content": [{
    "type": "tool_use",
    "name": "computer",
    "input": {
      "action": "left_click",
      "coordinate": [512, 384]
    }
  }]
}
        </div>
        <p style="font-size:11px; margin-top:8px; color:var(--ink-secondary);" data-ru="Координаты всегда нормированы под сетку модели (например, 1024×768), а не под ваш реальный монитор." data-en="Coordinates are always normalized to the model grid (e.g. 1024×768), not to your real monitor.">Koordinatalar har doim model to'riga (masalan, 1024×768) normallashtirilgan, real monitorga emas.</p>
      </div>
    </div>
"""))

S10.append(slide(4, "Matematika|Математика|Math", "20:00–25:00", """
    <div class="eyebrow"><span class="t" data-ru="VISUAL GROUNDING · ПЕРЕВОД КООРДИНАТ" data-en="VISUAL GROUNDING · COORDINATE TRANSLATION">VISUAL GROUNDING · KOORDINATALARNI O'TKAZISH</span></div>
    <h2 data-ru="Visual Grounding: Из Сетки 1024×768 в Реальные Пиксели" data-en="Visual Grounding: From the 1024×768 Grid to Real Pixels">Visual Grounding: 1024×768 To'ridan Haqiqiy Piksellarga</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Почему Координаты Смещаются?" data-en="Why Do Coordinates Drift?">Nega Koordinatalar Siljiydi?</h3>
        <p data-ru="Модель видит уменьшенный скриншот. Если нажать по её координатам напрямую на 4K-мониторе, курсор уйдёт на сотни пикселей в сторону." data-en="The model sees a downscaled screenshot. Clicking its raw coordinates on a 4K monitor shifts the cursor hundreds of pixels away.">Model kichraytirilgan skrinshotni ko'radi. Uning koordinatalari bo'yicha 4K monitorda to'g'ridan-to'g'ri bossangiz, kursor yuzlab piksel chetga ketadi.</p>
        <div class="box" style="margin-top:10px;">
          <strong data-ru="Формула:" data-en="Formula:">Formula:</strong>
          <p style="font-size:12px; margin-top:4px;" data-ru="scaleX = screen.width / 1024, scaleY = screen.height / 768, затем round()." data-en="scaleX = screen.width / 1024, scaleY = screen.height / 768, then round().">scaleX = screen.width / 1024, scaleY = screen.height / 768, so'ng round().</p>
        </div>
      </div>
      <div class="card">
        <h3 data-ru="Рабочий Код Драйвера" data-en="Working Driver Code">Ishchi Drayver Kodi</h3>
        <div class="code-block" style="font-size:11px; line-height:1.6; margin-top:8px;">
<span style="color:#64748b;">// Model qaytargan koordinatalar</span>
const apiX = 512, apiY = 384;
const apiW = 1024, apiH = 768;

<span style="color:#22c55e;">// Haqiqiy ekranga o'tkazish</span>
const realX = Math.round(apiX * (screen.width  / apiW));
const realY = Math.round(apiY * (screen.height / apiH));
pyautogui.click(realX, realY);
        </div>
        <p style="font-size:11px; margin-top:8px; color:var(--danger);" data-ru="HiDPI: учитывайте devicePixelRatio и делайте скриншот в том же масштабе, в котором работает модель." data-en="HiDPI: account for devicePixelRatio and capture the screenshot at the same scale the model expects.">HiDPI: devicePixelRatio'ni hisobga oling va skrinshotni model kutgan masshtabda oling.</p>
      </div>
    </div>
"""))

S10.append(slide(5, "Xavfsizlik|Безопасность|Security", "25:00–29:00", """
    <div class="eyebrow"><span class="t" data-ru="БЕЗОПАСНОСТЬ COMPUTER-USE · SANDBOX + HITL" data-en="COMPUTER-USE SECURITY · SANDBOX + HITL">COMPUTER-USE XAVFSIZLIGI · SANDBOX + HITL</span></div>
    <h2 data-ru="Опасности Экранного Агента и Три Уровня Защиты" data-en="Screen-Agent Risks & Three Layers of Defense">Ekran Agentining Xavflari va Uch Himoya Qatlami</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Риски" data-en="Risks">Xavflar</div>
        <ul style="font-size:12px; line-height:1.75; margin-top:8px;">
          <li data-ru="Prompt Injection на экране: вредоносный текст в чужом окне." data-en="On-screen prompt injection: malicious text inside another window.">Ekrandagi Prompt Injection: begona oynadagi zararli matn.</li>
          <li data-ru="Разрушительный клик: удаление файла или отправка платежа." data-en="Destructive click: deleting a file or sending a payment.">Vayronkor klik: faylni o'chirish yoki to'lov yuborish.</li>
          <li data-ru="Утечка секретов через буфер обмена и .env." data-en="Secret leakage via clipboard and .env files.">Clipboard va .env orqali sirlarning sizib chiqishi.</li>
        </ul>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Защита" data-en="Defense">Himoya</div>
        <ul style="font-size:12px; line-height:1.75; margin-top:8px;">
          <li data-ru="Sandbox: Docker + Xvfb, отдельный пользователь, без монтирования домашней папки." data-en="Sandbox: Docker + Xvfb, a separate user, no home-directory mounts.">Sandbox: Docker + Xvfb, alohida foydalanuvchi, uy papkasini mount qilmaslik.</li>
          <li data-ru="Least Privilege: только те приложения и папки, которые нужны для задачи." data-en="Least Privilege: only the apps and folders required for the task.">Least Privilege: faqat vazifa uchun kerakli ilova va papkalar.</li>
          <li data-ru="HITL: человек подтверждает удаление, отправку и оплату." data-en="HITL: a human confirms deletion, sending, and payment.">HITL: o'chirish, yuborish va to'lovni inson tasdiqlaydi.</li>
        </ul>
      </div>
    </div>
    <div class="code-block" style="margin-top:12px; font-size:11px;">
<span style="color:#eab308;"># Xavfsiz sandbox (Xvfb virtual ekran bilan)</span>
docker run --rm -p 6080:6080 --memory=2g --cpus=1 agent-sandbox
    </div>
"""))

S10.append(slide(6, "Viktorina|Викторина|Quiz", "29:00–33:00", """
    <div class="eyebrow"><span class="t" data-ru="ИНТЕРАКТИВНЫЙ ТЕСТ · 3 ВОПРОСА" data-en="INTERACTIVE QUIZ · 3 QUESTIONS">INTERAKTIV QUIZ · 3 TA SAVOL</span></div>
    <h2 data-ru="Блиц-Проверка: Computer-Use и Безопасность" data-en="Blitz Check: Computer-Use & Security">Blitz Tekshiruv: Computer-Use va Xavfsizlik</h2>
    <div class="quiz-box" style="margin-top:12px;">
      <div class="quiz-q" data-q="0">
        <p><strong data-ru="1. Почему DOM-селектор не работает в нативном Excel?" data-en="1. Why does a DOM selector fail inside native Excel?">1. Nega DOM selektori native Excel'da ishlamaydi?</strong></p>
        <div class="quiz-opts">
          <button class="q-opt" onclick="checkQuiz(0, 0, false)" data-ru="A) Слишком медленно" data-en="A) Too slow">A) Juda sekin</button>
          <button class="q-opt" onclick="checkQuiz(0, 1, true)" data-ru="B) В нативном приложении нет DOM" data-en="B) Native apps have no DOM">B) Native ilovada DOM yo'q</button>
          <button class="q-opt" onclick="checkQuiz(0, 2, false)" data-ru="C) Нужен другой браузер" data-en="C) Needs another browser">C) Boshqa brauzer kerak</button>
        </div>
      </div>
      <div class="quiz-q" data-q="1" style="margin-top:10px;">
        <p><strong data-ru="2. Что возвращает Computer-Use API для клика?" data-en="2. What does the Computer-Use API return for a click?">2. Computer-Use API klik uchun nima qaytaradi?</strong></p>
        <div class="quiz-opts">
          <button class="q-opt" onclick="checkQuiz(1, 0, false)" data-ru="A) HTML-таблицу" data-en="A) An HTML table">A) HTML jadval</button>
          <button class="q-opt" onclick="checkQuiz(1, 1, true)" data-ru="B) Действие и координаты [x, y]" data-en="B) Action and [x, y] coordinates">B) Harakat va [x, y] koordinatalar</button>
          <button class="q-opt" onclick="checkQuiz(1, 2, false)" data-ru="C) SQL-запрос" data-en="C) An SQL query">C) SQL so'rov</button>
        </div>
      </div>
      <div class="quiz-q" data-q="2" style="margin-top:10px;">
        <p><strong data-ru="3. Что защищает от удаления файлов экранным агентом?" data-en="3. What protects files from a screen agent's destructive click?">3. Ekran agentining vayronkor klikidan fayllarni nima himoya qiladi?</strong></p>
        <div class="quiz-opts">
          <button class="q-opt" onclick="checkQuiz(2, 0, true)" data-ru="A) Sandbox и HITL-подтверждение" data-en="A) Sandbox and HITL approval">A) Sandbox va HITL tasdig'i</button>
          <button class="q-opt" onclick="checkQuiz(2, 1, false)" data-ru="B) Более высокая temperature" data-en="B) Higher temperature">B) Yuqori temperature</button>
          <button class="q-opt" onclick="checkQuiz(2, 2, false)" data-ru="C) Темная тема" data-en="C) Dark theme">C) Tungi mavzu</button>
        </div>
      </div>
    </div>
"""))

S10.append(slide(7, "Amaliyot|Практика|Practice", "33:00–37:00", """
    <div class="eyebrow"><span class="t" data-ru="ЛАБОРАТОРИЯ · DESKTOP AGENT FLOW" data-en="LAB · DESKTOP AGENT FLOW">LABORATORIYA · DESKTOP AGENT FLOW</span></div>
    <h2 data-ru="Практика: Агент Считает в Калькуляторе и Пишет Отчёт" data-en="Lab: Agent Computes in Calculator & Writes a Report">Amaliyot: Agent Kalkulyatorda Hisoblaydi va Hisobot Yozadi</h2>
    <div class="grid-2">
      <div class="card">
        <span class="badge" style="background:var(--accent); color:#fff;">1</span>
        <h3 data-ru="Шаг 1: Sandbox" data-en="Step 1: Sandbox">1-Qadam: Sandbox</h3>
        <p data-ru="Запустите контейнер с Xvfb и откройте виртуальный экран в браузере." data-en="Start the Xvfb container and open the virtual screen in your browser.">Xvfb konteynerini ishga tushiring va brauzerda virtual ekranni oching.</p>
        <span class="badge" style="background:#a855f7; color:#fff; margin-top:8px;">2</span>
        <h3 data-ru="Шаг 2: Калькулятор" data-en="Step 2: Calculator">2-Qadam: Kalkulyator</h3>
        <p data-ru="Агент находит окно калькулятора по скриншоту и нажимает 1, 2, 5, ×, 4, 8, =." data-en="The agent finds Calculator by screenshot and presses 1, 2, 5, ×, 4, 8, =.">Agent skrinshot bo'yicha kalkulyator oynasini topadi va 1, 2, 5, ×, 4, 8, = ni bosadi.</p>
      </div>
      <div class="card">
        <span class="badge" style="background:var(--warning); color:#fff;">3</span>
        <h3 data-ru="Шаг 3: Проверка" data-en="Step 3: Verification">3-Qadam: Tekshirish</h3>
        <p data-ru="Сравните результат на экране с ожидаемым 6000. Если не совпало — сделайте новый скриншот и повторите." data-en="Compare the on-screen result with the expected 6000. If it differs, take a fresh screenshot and retry.">Ekrondagi natijani kutilgan 6000 bilan solishtiring. Mos kelmasa, yangi skrinshot oling va takrorlang.</p>
        <span class="badge" style="background:var(--success); color:#fff; margin-top:8px;">4</span>
        <h3 data-ru="Шаг 4: Отчёт" data-en="Step 4: Report">4-Qadam: Hisobot</h3>
        <p data-ru="Агент открывает текстовый редактор и печатает: «125 × 48 = 6000». Сохраните файл." data-en="The agent opens a text editor and types: '125 × 48 = 6000'. Save the file.">Agent matn muharririni ochadi va «125 × 48 = 6000» deb yozadi. Faylni saqlang.</p>
      </div>
    </div>
    <div class="box" style="margin-top:12px; text-align:center;">
      <strong data-ru="⏱ Время: 4 минуты" data-en="⏱ Time: 4 minutes">⏱ Vaqt: 4 daqiqa</strong>
      <p style="font-size:12px; margin-top:4px;" data-ru="Не забудьте про HITL: перед сохранением файла агент должен спросить разрешение." data-en="Do not forget HITL: the agent must ask permission before saving the file.">HITLni unutmang: faylni saqlashdan oldin agent ruxsat so'rashi shart.</p>
    </div>
"""))

S10.append(slide(8, "Refleksiya|Рефлексия|Reflection", "37:00–39:00", """
    <div class="eyebrow"><span class="t" data-ru="ПАРНАЯ ПРОВЕРКА · ЧЕК-ЛИСТ" data-en="PEER REVIEW · CHECKLIST">JUFTLIKDA TEKSHIRUV · CHEK-LIST</span></div>
    <h2 data-ru="Найдите Ошибки в Чужом Агенте за 2 Минуты" data-en="Find Bugs in a Classmate's Agent in 2 Minutes">Boshqaning Agentidagi Xatolarni 2 Daqiqada Toping</h2>
    <div class="grid-3">
      <div class="card">
        <h3 data-ru="Координаты" data-en="Coordinates">Koordinatalar</h3>
        <p data-ru="Есть ли scaleX/scaleY и round()? Проверьте на 4K и на обычном экране." data-en="Are scaleX/scaleY and round() present? Test on 4K and on a regular screen.">scaleX/scaleY va round() bormi? 4K va oddiy ekranda sinab ko'ring.</p>
      </div>
      <div class="card">
        <h3 data-ru="Свежесть Экрана" data-en="Screen Freshness">Ekran Yangiligi</h3>
        <p data-ru="Делается ли новый скриншот после каждого действия? Старый скриншот — главная причина промахов." data-en="Is a fresh screenshot taken after every action? A stale screenshot is the top cause of misses.">Har harakatdan keyin yangi skrinshot olinadimi? Eski skrinshot — asosiy xato manbai.</p>
      </div>
      <div class="card">
        <h3 data-ru="Защита" data-en="Safety">Himoya</h3>
        <p data-ru="Есть ли sandbox, запрет на домашнюю папку и HITL перед удалением или отправкой?" data-en="Is there a sandbox, a home-folder ban, and HITL before delete or send?">Sandbox, uy papkasini taqiqlash va o'chirish/yuborishdan oldin HITL bormi?</p>
      </div>
    </div>
"""))

S10.append(slide(9, "Xulosa|Итог|Summary", "39:00–40:00", """
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ · ДОМАШНЕЕ ЗАДАНИЕ" data-en="SUMMARY · HOMEWORK">XULOSA · UY VAZIFASI</span></div>
    <h2 data-ru="Итог: Экран — Это Тоже Интерфейс" data-en="Summary: The Screen Is an Interface Too">Xulosa: Ekran Ham Interfeys</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Уровень 1 · 4 балла" data-en="Tier 1 · 4 pts">1-Daraja · 4 ball</div>
        <h3 data-ru="Повторить Демо" data-en="Repeat the Demo">Demoni Takrorlash</h3>
        <p data-ru="Запустите агента в песочнице и повторите расчёт 125 × 48 без ошибок." data-en="Run the agent in the sandbox and repeat the 125 × 48 calculation without errors.">Agentni sandboxda ishga tushiring va 125 × 48 hisobini xatosiz takrorlang.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(234,179,8,0.15); color:var(--warning);" data-ru="Уровень 2 · 4 балла" data-en="Tier 2 · 4 pts">2-Daraja · 4 ball</div>
        <h3 data-ru="Добавить OCR" data-en="Add OCR">OCR Qo'shish</h3>
        <p data-ru="Считывайте результат не из DOM, а с пикселей через OCR (Tesseract) и сравните оба способа." data-en="Read the result from pixels via OCR (Tesseract) instead of the DOM, then compare both methods.">Natijani DOMdan emas, piksellardan OCR (Tesseract) orqali o'qing va ikkala usulni solishtiring.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Уровень 3 · 2 балла" data-en="Tier 3 · 2 pts">3-Daraja · 2 ball</div>
        <h3 data-ru="Аудит Безопасности" data-en="Security Audit">Xavfsizlik Auditi</h3>
        <p data-ru="Придумайте prompt injection на экране и докажите, что sandbox + HITL его блокируют." data-en="Craft an on-screen prompt injection and prove that sandbox + HITL block it.">Ekranga prompt injection o'ylab toping va sandbox + HITL uni bloklashini isbotlang.</p>
      </div>
    </div>
    <div class="box" style="margin-top:12px; text-align:center;">
      <p style="font-size:12px;" data-ru="📝 Интерактивное задание и 10-балльная рубрика: <a href='vazifa.html' style='color:var(--accent); font-weight:700;'>vazifa.html</a>" data-en="📝 Interactive homework and 10-point rubric: <a href='vazifa.html' style='color:var(--accent); font-weight:700;'>vazifa.html</a>">📝 Interaktiv vazifa va 10 ballik mezon: <a href="vazifa.html" style="color:var(--accent); font-weight:700;">vazifa.html</a></p>
    </div>
"""))

NOTES10 = {
    "uz": [
        ["Kirish va Maqsad", "Bugun DOM chegarasidan chiqib, ekranni ko'radigan va sichqonchani boshqaradigan Computer-Use agentlarini o'rganamiz.", "Mavzuni doskaga yozing va 40 daqiqalik rejani e'lon qiling."],
        ["Uy Vazifasi Tahlili", "30-darsda browser-use ishlatdik. Asosiy xato — SPA yangilangandan keyin eski selektorga bosish. Accessibility tree va HITL bu muammoni hal qiladi.", "Blitz savolga javob oling va bugungi mavzuga ko'prik quring."],
        ["DOM Chegarasi", "Uch xil dunyo bor: oddiy DOM, canvas va native OS. Har biri uchun boshqaruv usuli farq qiladi.", "O'quvchilardan native ilovalarga misol so'rang."],
        ["Computer-Use API", "API skrinshotni oladi, model tool_use va koordinata qaytaradi, drayver klikni bajaradi. Tsikl har safar yangi skrinshot bilan takrorlanadi.", "JSON javobini doskada tahlil qiling."],
        ["Visual Grounding", "Model koordinatalari 1024×768 to'rida keladi. scaleX/scaleY va round() bilan haqiqiy ekranga o'tkazamiz.", "Formulani daftarga yozdirib, bitta misol hisoblang."],
        ["Xavfsizlik", "Sandbox, least privilege va HITL — uch qatlamli himoya. Prompt injection ekranda ham uchraydi.", "Docker va Xvfb buyrug'ini ko'rsating."],
        ["Viktorina", "Uch savol orqali DOM, API va himoya tushunchalarini mustahkamlaymiz.", "Har bir savolga qo'l ko'tartirib javob oling."],
        ["Laboratoriya", "O'quvchilar sandboxda kalkulyator va matn muharririni boshqaradigan agent yasaydilar.", "Vaqtni 4 daqiqa bilan cheklang va HITLni eslatib turing."],
        ["Juftlikda Tekshiruv", "Partadoshlar koordinata, skrinshot yangiligi va himoya bo'yicha bir-birining ishini tekshiradi.", "Ikki juftlikni tanlab, xulosasini tinglang."],
        ["Xulosa va Uy Vazifasi", "Ekran ham interfeys ekanini tushundik. Uy vazifasi uch darajaga bo'lingan, 10 ballik mezon vazifa.html da.", "Barcha o'quvchilarga vazifa.html havolasini ko'rsating."],
    ],
    "ru": [
        ["Введение и Цель", "Сегодня выходим за пределы DOM и изучаем Computer-Use агентов, которые видят экран и управляют мышью.", "Запишите тему на доске и объявите план на 40 минут."],
        ["Разбор Домашнего Задания", "На 30-м уроке мы использовали browser-use. Главная ошибка — клик по старому селектору после перерисовки SPA. Accessibility tree и HITL решают эту проблему.", "Получите ответ на блиц-вопрос и перейдите к новой теме."],
        ["Граница DOM", "Есть три мира: обычный DOM, canvas и нативная ОС. Для каждого нужен свой способ управления.", "Попросите учеников привести примеры нативных приложений."],
        ["Computer-Use API", "API делает скриншот, модель возвращает tool_use и координаты, драйвер выполняет клик. Цикл повторяется с новым скриншотом.", "Разберите JSON-ответ на доске."],
        ["Visual Grounding", "Координаты модели приходят в сетке 1024×768. Через scaleX/scaleY и round() переводим их в реальные пиксели.", "Запишите формулу в тетрадь и решите один пример."],
        ["Безопасность", "Sandbox, least privilege и HITL — три уровня защиты. Prompt injection встречается и на экране.", "Покажите команду Docker и Xvfb."],
        ["Викторина", "Три вопроса закрепляют DOM, API и защиту.", "Соберите ответы поднятием руки."],
        ["Лаборатория", "Ученики в песочнице управляют калькулятором и текстовым редактором.", "Ограничьте время четырьмя минутами и напоминайте про HITL."],
        ["Парная Проверка", "Одноклассники проверяют координаты, свежесть скриншота и защиту друг у друга.", "Выберите две пары и заслушайте выводы."],
        ["Итог и Домашнее Задание", "Мы поняли, что экран — тоже интерфейс. Домашка трёхуровневая, рубрика на 10 баллов в vazifa.html.", "Покажите всем ссылку на vazifa.html."],
    ],
    "en": [
        ["Intro & Goal", "Today we leave the DOM behind and study Computer-Use agents that see the screen and drive the mouse.", "Write the topic on the board and announce the 40-minute plan."],
        ["Homework Review", "In Lesson 30 we used browser-use. The main bug was clicking a stale selector after an SPA re-render. Accessibility tree and HITL solve it.", "Take the blitz answer and bridge into today's topic."],
        ["Beyond the DOM", "There are three worlds: plain DOM, canvas, and native OS. Each needs a different control strategy.", "Ask students for examples of native apps."],
        ["Computer-Use API", "The API takes a screenshot, the model returns tool_use and coordinates, and the driver clicks. The loop repeats with a fresh screenshot.", "Walk through the JSON response on the board."],
        ["Visual Grounding", "Model coordinates arrive in a 1024×768 grid. scaleX/scaleY plus round() maps them to real pixels.", "Have students write the formula and solve one example."],
        ["Security", "Sandbox, least privilege, and HITL form three layers of defense. Prompt injection also appears on screen.", "Show the Docker and Xvfb command."],
        ["Quiz", "Three questions reinforce DOM, API, and safety.", "Collect answers by a show of hands."],
        ["Lab", "Students drive Calculator and a text editor inside the sandbox.", "Cap the time at four minutes and keep reminding them about HITL."],
        ["Peer Review", "Classmates audit coordinates, screenshot freshness, and safety.", "Pick two pairs and hear their findings."],
        ["Summary & Homework", "We learned that the screen is an interface too. Homework has three tiers and a 10-point rubric in vazifa.html.", "Show everyone the vazifa.html link."],
    ],
}

# =============================================================================
# 9-SINF · 12-HAFTA · 35-DARS — NPM Ecosystem & Supply Chain Security
# =============================================================================
S9 = []

S9.append(slide(0, "Kirish|Введение|Intro", "00:00–05:00", """
    <div class="eyebrow"><span class="t" data-ru="9-КЛАСС · 12-Я НЕДЕЛЯ · УРОК 35" data-en="GRADE 9 · WEEK 12 · LESSON 35">9-SINF · 12-HAFTA · 35-DARS</span></div>
    <h1 class="display" data-ru="Экосистема NPM и Безопасность Цепочки Поставок: package.json, Lockfile и npm audit" data-en="NPM Ecosystem & Supply Chain Security: package.json, Lockfile & npm audit">NPM Ekotizimi va Ta'minot Zanjiri Xavfsizligi: package.json, Lockfile va npm audit</h1>
    <p class="lede" data-ru="Каждый npm install запускает чужой код на вашем компьютере. Учимся читать зависимости, проверять lockfile, ловить typosquatting и закрывать уязвимости до продакшена." data-en="Every npm install executes someone else's code on your machine. Learn to read dependencies, verify the lockfile, catch typosquatting, and patch vulnerabilities before production.">Har bir npm install kompyuteringizda boshqa birovning kodini ishga tushiradi. Bog'liqliklarni o'qish, lockfile'ni tekshirish, typosquatting'ni ushlash va zaifliklarni produksiyadan oldin yopishni o'rganamiz.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">Juftlik Dars · 80 daqiqa</div>
        <h3 data-ru="Цепочка Поставок (Supply Chain)" data-en="The Software Supply Chain">Ta'minot Zanjiri</h3>
        <p data-ru="Ваш код — это вершина айсберга. Под ним сотни транзитивных пакетов, которые вы никогда не читали." data-en="Your code is the tip of the iceberg. Beneath it sit hundreds of transitive packages you never read.">Sizning kodingiz aysbergning uchi. Uning ostida siz hech qachon o'qimagan yuzlab tranzitiv paketlar yotadi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Практический результат" data-en="Deliverable">NPM Security Audit</div>
        <h3 data-ru="Аудит и Чистый Lockfile" data-en="Audit & Clean Lockfile">Audit va Toza Lockfile</h3>
        <p data-ru="Находим подозрительный пакет, убираем postinstall-скрипт, чиним уязвимости и коммитим проверенный lockfile." data-en="Find a suspicious package, remove a postinstall script, patch vulnerabilities, and commit a verified lockfile.">Shubhali paketni topamiz, postinstall skriptini olib tashlaymiz, zaifliklarni yopamiz va tekshirilgan lockfile'ni commit qilamiz.</p>
      </div>
    </div>
""", first=True))

S9.append(slide(1, "Tahlil|Разбор|Review", "05:00–13:00", """
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 34-УРОКА" data-en="LESSON 34 HOMEWORK REVIEW">34-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Разбор 34-урока: Валидация Только на Клиенте и ReDoS" data-en="Lesson 34 Review: Client-Only Validation & ReDoS">34-dars Tahlili: Faqat Client-Side Validatsiya va ReDoS</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Типичная Ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Проверка Только в Браузере" data-en="Browser-Only Validation">Faqat Brauzerda Tekshirish</h3>
        <p data-ru="Красная рамка в форме ничего не значит: злоумышленник отправляет запрос через curl и обходит всю клиентскую проверку. Плюс жадная регулярка может вызвать ReDoS." data-en="A red border in the form means nothing: an attacker sends a curl request and bypasses all client-side checks. A greedy regex can also trigger ReDoS.">Formadagi qizil hoshiya hech narsani anglatmaydi: hujumchi curl orqali so'rov yuborib, butun client tekshiruvini chetlab o'tadi. Ustiga greedy regex ReDoS keltirib chiqarishi mumkin.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#ef4444;">// XATO: faqat frontendda tekshirish</span>
if (!email.includes('@')) return;
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Золотой Стандарт" data-en="Golden Standard">Oltin Standart (Best Practice)</div>
        <h3 data-ru="Сервер + Якорная Регулярка" data-en="Server + Anchored Regex">Server + Ankralangan Regex</h3>
        <p data-ru="Валидируем на сервере, используем ^...$ и ограничиваем длину. Клиентская проверка — только для удобства пользователя." data-en="Validate on the server, use ^...$ and enforce a length limit. Client checks are only for user experience.">Serverda tekshiramiz, ^...$ ishlatamiz va uzunlikni cheklaymiz. Client tekshiruvi faqat qulaylik uchun.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#22c55e;">// TO'G'RI: server-side + anchor</span>
const EMAIL = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/;
if (!EMAIL.test(email) || email.length > 254) reject();
        </div>
      </div>
    </div>
    <div class="grid-2" style="margin-top:14px;">
      <div class="box">
        <span class="badge" data-ru="Блиц-вопрос (30 сек)" data-en="Blitz Question (30s)">Blitz Savol</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="Почему без якорей ^ и $ регулярка пропускает строку с мусором в начале или конце?" data-en="Why does a regex without ^ and $ accept a string with garbage at the start or end?">Nega ^ va $ ankorlarisiz regex boshida yoki oxirida axlat bo'lgan satrni o'tkazib yuboradi?</p>
      </div>
      <div class="box">
        <span class="badge" data-ru="Мост к теме" data-en="Bridge to Today">Bugungi Mavzuga Ko'prik</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="Мы защитили форму. Но что если вредоносный код приходит не от пользователя, а из пакета, который мы сами установили?" data-en="We secured the form. But what if malicious code comes not from a user, but from a package we installed ourselves?">Formani himoya qildik. Ammo zararli kod foydalanuvchidan emas, o'zimiz o'rnatgan paketdan kelsa-chi?</p>
      </div>
    </div>
"""))

S9.append(slide(2, "Konsept|Концепт|Concept", "13:00–19:00", """
    <div class="eyebrow"><span class="t" data-ru="ЭКОСИСТЕМА NPM · МАСШТАБ РИСКА" data-en="THE NPM ECOSYSTEM · SCALE OF RISK">NPM EKOTIZIMI · XAVF MASSHTABI</span></div>
    <h2 data-ru="Почему NPM — Это Цепочка Поставок, а Не Просто Папка" data-en="Why NPM Is a Supply Chain, Not Just a Folder">Nega NPM Bu Shunchaki Papka Emas, Ta'minot Zanjiri?</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Масштаб" data-en="Scale">Masshtab</div>
        <h3 data-ru="2+ Миллиона Пакетов" data-en="2M+ Packages">2+ Million Paket</h3>
        <p data-ru="В реестре NPM более двух миллионов пакетов. Один package.json может незаметно притянуть сотни зависимостей." data-en="The NPM registry hosts over two million packages. A single package.json can silently pull in hundreds of dependencies.">NPM reyestrада ikki milliondan ortiq paket bor. Bitta package.json jimgina yuzlab bog'liqliklarni tortib kelishi mumkin.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(234,179,8,0.15); color:var(--warning);" data-ru="Транзитивность" data-en="Transitivity">Tranzitivlik</div>
        <h3 data-ru="Зависимости Зависимостей" data-en="Dependencies of Dependencies">Bog'liqliklarning Bog'liqligi</h3>
        <p data-ru="Вы устанавливаете один пакет, а он тянет 40 своих. Вы не читали их код и не знаете, что там внутри." data-en="You install one package and it pulls 40 of its own. You never read their code and do not know what is inside.">Bitta paket o'rnatasiz, u o'zining 40 tasini tortadi. Siz ularning kodini o'qimagan va ichida nima borligini bilmaysiz.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Исполнение" data-en="Execution">Ijro</div>
        <h3 data-ru="Код Запускается Сам" data-en="Code Runs Itself">Kod O'zi Ishga Tushadi</h3>
        <p data-ru="postinstall-скрипт выполняется при установке. Это легальный механизм сборки — и идеальная лазейка для вредоносного кода." data-en="A postinstall script executes on install. It is a legitimate build hook — and a perfect backdoor for malicious code.">postinstall skripti o'rnatish paytida bajariladi. Bu qonuniy build mexanizmi — va zararli kod uchun ideal orqa eshik.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px;">
      <strong data-ru="Главная мысль:" data-en="Key takeaway:">Asosiy fikr:</strong>
      <p style="font-size:12px; margin-top:4px;" data-ru="npm install — это не «скачать файлы», а «запустить чужой код с вашими правами»." data-en="npm install is not 'download files'; it is 'execute someone else's code with your permissions'.">npm install — bu «fayllarni yuklab olish» emas, balki «boshqa birovning kodini sizning huquqlaringiz bilan ishga tushirish».</p>
    </div>
"""))

S9.append(slide(3, "Arxitektura|Архитектура|Architecture", "19:00–25:00", """
    <div class="eyebrow"><span class="t" data-ru="PACKAGE.JSON VS PACKAGE-LOCK.JSON" data-en="PACKAGE.JSON VS PACKAGE-LOCK.JSON">PACKAGE.JSON VA PACKAGE-LOCK.JSON</span></div>
    <h2 data-ru="Два Файла, Которые Решают Всё" data-en="Two Files That Decide Everything">Hammasini Hal Qiladigan Ikki Fayl</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Намерение" data-en="Intent">Niyat</div>
        <h3 data-ru="package.json" data-en="package.json">package.json</h3>
        <p data-ru="Описывает, что вы хотите: имя проекта, скрипты и диапазоны версий зависимостей." data-en="Describes what you want: project name, scripts, and dependency version ranges.">Nimani xohlayotganingizni yozadi: loyiha nomi, skriptlar va bog'liqlik versiya diapazonlari.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
{
  "scripts": { "test": "jest" },
  "dependencies": {
    "express": "^4.19.2"
  }
}
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Факт" data-en="Reality">Fakt</div>
        <h3 data-ru="package-lock.json" data-en="package-lock.json">package-lock.json</h3>
        <p data-ru="Фиксирует, что реально установилось: точные версии, дерево зависимостей и хеши целостности sha512." data-en="Locks what was actually installed: exact versions, the dependency tree, and sha512 integrity hashes.">Aslida nima o'rnatilganini qotiradi: aniq versiyalar, bog'liqlik daraxti va sha512 yaxlitlik xeshlari.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
"express": {
  "version": "4.19.2",
  "integrity": "sha512-..."
}
        </div>
      </div>
    </div>
    <div class="box" style="margin-top:12px;">
      <p style="font-size:12px;" data-ru="💡 Lockfile обязателен в Git. Без него у коллеги и на сервере установятся разные версии — и баг «работает у меня» станет нормой." data-en="💡 The lockfile must be committed to Git. Without it, a teammate and the server install different versions — and 'works on my machine' becomes the norm.">💡 Lockfile Git'ga majburiy qo'shiladi. Usiz hamkasb va serverda turli versiyalar o'rnatiladi — «menda ishlayapti» xatosi odatiy holga aylanadi.</p>
    </div>
"""))

S9.append(slide(4, "SemVer|SemVer|SemVer", "25:00–31:00", """
    <div class="eyebrow"><span class="t" data-ru="SEMANTIC VERSIONING · ^ И ~" data-en="SEMANTIC VERSIONING · ^ AND ~">SEMANTIK VERSIYALASH · ^ VA ~</span></div>
    <h2 data-ru="Символ ^ Может Незаметно Обновить Проект" data-en="A Single ^ Can Silently Upgrade Your Project">Bitta ^ Loyihani Jimgina Yangilashi Mumkin</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Точно" data-en="Exact">Aniq</div>
        <h3 data-ru="1.2.3" data-en="1.2.3">1.2.3</h3>
        <p data-ru="Установится ровно 1.2.3. Максимальная предсказуемость, но нет патчей безопасности автоматически." data-en="Installs exactly 1.2.3. Maximum predictability, but no automatic security patches.">Aynan 1.2.3 o'rnatiladi. Maksimal bashoratlilik, lekin xavfsizlik yamoqlari avtomatik kelmaydi.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(234,179,8,0.15); color:var(--warning);" data-ru="Патч" data-en="Patch">Patch</div>
        <h3 data-ru="~1.2.3" data-en="~1.2.3">~1.2.3</h3>
        <p data-ru="Разрешены только патчи: 1.2.4, 1.2.9. Мажор и минор зафиксированы." data-en="Only patches allowed: 1.2.4, 1.2.9. Major and minor are locked.">Faqat patslarga ruxsat: 1.2.4, 1.2.9. Major va minor qulflangan.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Минор" data-en="Minor">Minor</div>
        <h3 data-ru="^1.2.3" data-en="^1.2.3">^1.2.3</h3>
        <p data-ru="Разрешены минорные обновления: 1.3.0, 1.9.9. Новые функции могут сломать совместимость." data-en="Minor updates allowed: 1.3.0, 1.9.9. New features may break compatibility.">Minor yangilanishlarga ruxsat: 1.3.0, 1.9.9. Yangi funksiyalar moslikni buzishi mumkin.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px;">
      <strong data-ru="Кейс left-pad (2016):" data-en="The left-pad incident (2016):">left-pad keysi (2016):</strong>
      <p style="font-size:12px; margin-top:4px;" data-ru="Автор удалил 11 строк кода из реестра — и тысячи проектов по всему миру перестали собираться за одну ночь. Зависимость от чужого кода — это реальный риск." data-en="The author unpublished 11 lines of code — and thousands of projects worldwide stopped building overnight. Depending on someone else's code is a real risk.">Muallif 11 qator kodni reyestrdan o'chirdi — va dunyo bo'ylab minglab loyihalar bir kechada yig'ilmay qoldi. Boshqa birovning kodiga bog'liq bo'lish — real xavf.</p>
    </div>
"""))

S9.append(slide(5, "Standart|Стандарт|Standard", "31:00–37:00", """
    <div class="eyebrow"><span class="t" data-ru="DEPENDENCIES VS DEVDEPENDENCIES" data-en="DEPENDENCIES VS DEVDEPENDENCIES">DEPENDENCIES VA DEVDEPENDENCIES</span></div>
    <h2 data-ru="Не Тащите Тестовые Пакеты в Продакшен" data-en="Do Not Ship Test Packages to Production">Test Paketlarini Produksiyaga Olib Bormang</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="dependencies" data-en="dependencies">dependencies</h3>
        <p data-ru="Нужны приложению в рантайме: express, pg, jsonwebtoken. Они попадут на сервер." data-en="Needed at runtime: express, pg, jsonwebtoken. They ship to the server.">Ilova ishlashi uchun kerak: express, pg, jsonwebtoken. Ular serverga boradi.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
"dependencies": {
  "express": "^4.19.2",
  "pg": "^8.11.0"
}
        </div>
      </div>
      <div class="card">
        <h3 data-ru="devDependencies" data-en="devDependencies">devDependencies</h3>
        <p data-ru="Нужны только для сборки и тестов: jest, eslint, nodemon. В продакшене не нужны." data-en="Only for build and tests: jest, eslint, nodemon. Not needed in production.">Faqat build va testlar uchun: jest, eslint, nodemon. Produksiyada kerak emas.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
"devDependencies": {
  "jest": "^29.7.0",
  "eslint": "^8.57.0"
}
        </div>
      </div>
    </div>
    <div class="box" style="margin-top:12px;">
      <strong data-ru="Команда для сервера:" data-en="Server install command:">Server uchun buyruq:</strong>
      <p style="font-size:12px; margin-top:4px;" data-ru="npm ci --omit=dev устанавливает только рантайм-зависимости строго по lockfile. Меньше пакетов — меньше поверхность атаки." data-en="npm ci --omit=dev installs only runtime dependencies strictly from the lockfile. Fewer packages means a smaller attack surface.">npm ci --omit=dev faqat runtime bog'liqliklarini lockfile bo'yicha o'rnatadi. Kamroq paket — kichikroq hujum yuzasi.</p>
    </div>
"""))

S9.append(slide(6, "Xavfsizlik|Безопасность|Security", "37:00–43:00", """
    <div class="eyebrow"><span class="t" data-ru="TYPO SQUATTING · POSTINSTALL" data-en="TYPO SQUATTING · POSTINSTALL">TYPO SQUATTING · POSTINSTALL</span></div>
    <h2 data-ru="Как Выглядят Атаки на Цепочку Поставок" data-en="What Supply-Chain Attacks Look Like">Ta'minot Zanjiriga Hujumlar Qanday Ko'rinadi</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Атака 1" data-en="Attack 1">Hujum 1</div>
        <h3 data-ru="Typosquatting" data-en="Typosquatting">Typosquatting</h3>
        <p data-ru="Злоумышленник публикует пакет с опечаткой в имени: crossenv вместо cross-env. Вы ставите его, думая, что это оригинал." data-en="An attacker publishes a package with a typo: crossenv instead of cross-env. You install it thinking it is the original.">Hujumchi nomida xatoli paket chop etadi: cross-env o'rniga crossenv. Siz uni original deb o'rnatasiz.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#ef4444;"># XATO: nomni tekshirmaslik</span>
npm install crossenv
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Атака 2" data-en="Attack 2">Hujum 2</div>
        <h3 data-ru="postinstall-Скрипт" data-en="postinstall Script">postinstall Skripti</h3>
        <p data-ru="Пакет при установке запускает свой скрипт: читает .env, отправляет токены на сервер злоумышленника." data-en="On install, the package runs its script: reads .env and sends tokens to the attacker's server.">Paket o'rnatilganda o'z skriptini ishga tushiradi: .env ni o'qiydi va tokenlarni hujumchi serveriga yuboradi.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
"scripts": {
  "postinstall": "node ./collect.js"
}
        </div>
      </div>
    </div>
    <div class="box" style="margin-top:12px;">
      <strong data-ru="Защита:" data-en="Defense:">Himoya:</strong>
      <p style="font-size:12px; margin-top:4px;" data-ru="Проверяйте имя пакета, количество загрузок и репозиторий. Ставьте с --ignore-scripts, если скрипты не нужны. Читайте diff lockfile перед коммитом." data-en="Check the package name, download count, and repository. Install with --ignore-scripts when scripts are not needed. Read the lockfile diff before committing.">Paket nomi, yuklab olishlar soni va repozitoriyni tekshiring. Skriptlar kerak bo'lmasa, --ignore-scripts bilan o'rnating. Commit oldidan lockfile diffini o'qing.</p>
    </div>
"""))

S9.append(slide(7, "Viktorina|Викторина|Quiz", "43:00–48:00", """
    <div class="eyebrow"><span class="t" data-ru="ИНТЕРАКТИВНЫЙ ТЕСТ · 4 ВОПРОСА" data-en="INTERACTIVE QUIZ · 4 QUESTIONS">INTERAKTIV QUIZ · 4 TA SAVOL</span></div>
    <h2 data-ru="Блиц-Проверка: Зависимости и Атаки" data-en="Blitz Check: Dependencies & Attacks">Blitz Tekshiruv: Bog'liqliklar va Hujumlar</h2>
    <div class="quiz-box" style="margin-top:12px;">
      <div class="quiz-q" data-q="0">
        <p><strong data-ru="1. Какой файл фиксирует точные версии и хеши целостности?" data-en="1. Which file locks exact versions and integrity hashes?">1. Qaysi fayl aniq versiyalar va yaxlitlik xeshlarini qotiradi?</strong></p>
        <div class="quiz-opts">
          <button class="q-opt" onclick="checkQuiz(0, 0, false)" data-ru="A) package.json" data-en="A) package.json">A) package.json</button>
          <button class="q-opt" onclick="checkQuiz(0, 1, true)" data-ru="B) package-lock.json" data-en="B) package-lock.json">B) package-lock.json</button>
          <button class="q-opt" onclick="checkQuiz(0, 2, false)" data-ru="C) README.md" data-en="C) README.md">C) README.md</button>
        </div>
      </div>
      <div class="quiz-q" data-q="1" style="margin-top:10px;">
        <p><strong data-ru="2. Что разрешает диапазон ^1.2.3?" data-en="2. What does the ^1.2.3 range allow?">2. ^1.2.3 diapazoni nimaga ruxsat beradi?</strong></p>
        <div class="quiz-opts">
          <button class="q-opt" onclick="checkQuiz(1, 0, false)" data-ru="A) Только 1.2.3" data-en="A) Only 1.2.3">A) Faqat 1.2.3</button>
          <button class="q-opt" onclick="checkQuiz(1, 1, true)" data-ru="B) Минорные и патч-обновления" data-en="B) Minor and patch updates">B) Minor va patch yangilanishlar</button>
          <button class="q-opt" onclick="checkQuiz(1, 2, false)" data-ru="C) Любую версию" data-en="C) Any version">C) Har qanday versiya</button>
        </div>
      </div>
      <div class="quiz-q" data-q="2" style="margin-top:10px;">
        <p><strong data-ru="3. Что такое typosquatting?" data-en="3. What is typosquatting?">3. Typosquatting nima?</strong></p>
        <div class="quiz-opts">
          <button class="q-opt" onclick="checkQuiz(2, 0, true)" data-ru="A) Пакет с опечаткой в имени" data-en="A) A package with a typo in its name">A) Nomida xatoli paket</button>
          <button class="q-opt" onclick="checkQuiz(2, 1, false)" data-ru="B) Быстрый сервер" data-en="B) A fast server">B) Tez server</button>
          <button class="q-opt" onclick="checkQuiz(2, 2, false)" data-ru="C) Новый фреймворк" data-en="C) A new framework">C) Yangi framework</button>
        </div>
      </div>
      <div class="quiz-q" data-q="3" style="margin-top:10px;">
        <p><strong data-ru="4. Какая команда ставит только рантайм-зависимости по lockfile?" data-en="4. Which command installs only runtime deps from the lockfile?">4. Qaysi buyruq lockfile bo'yicha faqat runtime bog'liqliklarini o'rnatadi?</strong></p>
        <div class="quiz-opts">
          <button class="q-opt" onclick="checkQuiz(3, 0, false)" data-ru="A) npm install --save" data-en="A) npm install --save">A) npm install --save</button>
          <button class="q-opt" onclick="checkQuiz(3, 1, true)" data-ru="B) npm ci --omit=dev" data-en="B) npm ci --omit=dev">B) npm ci --omit=dev</button>
          <button class="q-opt" onclick="checkQuiz(3, 2, false)" data-ru="C) npm publish" data-en="C) npm publish">C) npm publish</button>
        </div>
      </div>
    </div>
"""))

S9.append(slide(8, "Amaliyot|Практика|Practice", "48:00–53:00", """
    <div class="eyebrow"><span class="t" data-ru="NPM AUDIT · ДИАГНОСТИКА" data-en="NPM AUDIT · DIAGNOSTICS">NPM AUDIT · DIAGNOSTIKA</span></div>
    <h2 data-ru="npm audit: Находим Уязвимости за 10 Секунд" data-en="npm audit: Find Vulnerabilities in 10 Seconds">npm audit: Zaifliklarni 10 Soniyada Topish</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Три Команды" data-en="Three Commands">Uch Buyruq</h3>
        <div class="code-block" style="font-size:11px; line-height:1.7; margin-top:8px;">
<span style="color:#22c55e;">npm audit</span>            <span style="color:#64748b;"># severity jadvali</span>
<span style="color:#eab308;">npm audit --json</span>     <span style="color:#64748b;"># mashina o'qiydigan</span>
<span style="color:#3b82f6;">npm audit fix</span>        <span style="color:#64748b;"># xavfsiz patch</span>
        </div>
        <p style="font-size:11px; margin-top:8px; color:var(--danger);" data-ru="npm audit fix --force может поставить мажорную версию и сломать проект. Сначала читайте отчёт." data-en="npm audit fix --force may install a major version and break the project. Read the report first.">npm audit fix --force major versiyani o'rnatib, loyihani buzishi mumkin. Avval hisobotni o'qing.</p>
      </div>
      <div class="card">
        <h3 data-ru="Уровни Severity" data-en="Severity Levels">Severity Darajalari</h3>
        <ul style="font-size:12px; line-height:1.8; margin-top:8px;">
          <li data-ru="🔴 critical — немедленно патчить, блокирует релиз." data-en="🔴 critical — patch immediately, blocks release.">🔴 critical — darhol yamoqlash, relizni bloklaydi.</li>
          <li data-ru="🟠 high — исправить до продакшена." data-en="🟠 high — fix before production.">🟠 high — produksiyadan oldin tuzatish.</li>
          <li data-ru="🟡 moderate — планируем в спринт." data-en="🟡 moderate — plan for the sprint.">🟡 moderate — sprintga rejalashtirish.</li>
          <li data-ru="⚪ low — принимаем риск осознанно." data-en="⚪ low — accept the risk consciously.">⚪ low — xavfni ongli qabul qilish.</li>
        </ul>
      </div>
    </div>
"""))

S9.append(slide(9, "CI/CD|CI/CD|CI/CD", "53:00–58:00", """
    <div class="eyebrow"><span class="t" data-ru="LOCKFILE И CI · ВОСПРОИЗВОДИМОСТЬ" data-en="LOCKFILE & CI · REPRODUCIBILITY">LOCKFILE VA CI · TAKRORLANUVCHANLIK</span></div>
    <h2 data-ru="npm ci: Одинаковая Установка на Любой Машине" data-en="npm ci: The Same Install on Every Machine">npm ci: Har Qanday Mashinada Bir Xil O'rnatish</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="npm install vs npm ci" data-en="npm install vs npm ci">npm install va npm ci</h3>
        <p data-ru="npm install может обновить lockfile и поставить другие версии. npm ci удаляет node_modules и ставит строго по lockfile — идеально для CI." data-en="npm install may update the lockfile and install different versions. npm ci wipes node_modules and installs strictly from the lockfile — ideal for CI.">npm install lockfile'ni yangilashi va boshqa versiyalarni o'rnatishi mumkin. npm ci node_modules'ni o'chirib, qat'iy lockfile bo'yicha o'rnatadi — CI uchun ideal.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#22c55e;">npm ci --omit=dev</span>
<span style="color:#22c55e;">npm audit --audit-level=high</span>
        </div>
      </div>
      <div class="card">
        <h3 data-ru="GitHub Actions" data-en="GitHub Actions">GitHub Actions</h3>
        <div class="code-block" style="font-size:10.5px; line-height:1.55; margin-top:8px;">
- uses: actions/setup-node@v4
  with: { node-version: 20 }
- run: npm ci
- run: npm audit --audit-level=high
- run: npm test
        </div>
        <p style="font-size:11px; margin-top:8px; color:var(--ink-secondary);" data-ru="Если audit находит high/critical — сборка падает (exit code 1) и плохой код не попадает в прод." data-en="If audit finds high/critical, the build fails (exit code 1) and bad code never reaches production.">Agar audit high/critical topsa, build yiqiladi (exit code 1) va yomon kod prodga tushmaydi.</p>
      </div>
    </div>
"""))

S9.append(slide(10, "Laboratoriya|Лаборатория|Lab", "58:00–68:00", """
    <div class="eyebrow"><span class="t" data-ru="ЛАБОРАТОРИЯ · АУДИТ ПРОЕКТА" data-en="LAB · PROJECT AUDIT">LABORATORIYA · LOYIHA AUDITI</span></div>
    <h2 data-ru="Практика: Найди Троян и Почини Проект (20 Минут)" data-en="Lab: Find the Trojan & Fix the Project (20 Minutes)">Amaliyot: Troyanni Top va Loyihani Tuzat (20 Daqiqa)</h2>
    <div class="grid-2">
      <div class="card">
        <span class="badge" style="background:var(--accent); color:#fff;">1</span>
        <h3 data-ru="Шаг 1: Осмотр" data-en="Step 1: Inspect">1-Qadam: Ko'rik</h3>
        <p data-ru="Откройте package.json из папки lab. Найдите пакет с опечаткой и postinstall-скрипт." data-en="Open package.json from the lab folder. Find the typo package and the postinstall script.">Lab papkasidagi package.json'ni oching. Xatoli paket va postinstall skriptini toping.</p>
        <span class="badge" style="background:#a855f7; color:#fff; margin-top:8px;">2</span>
        <h3 data-ru="Шаг 2: Удаление" data-en="Step 2: Remove">2-Qadam: Olib Tashlash</h3>
        <p data-ru="Удалите подозрительный пакет и запретите скрипты установки." data-en="Remove the suspicious package and disable install scripts.">Shubhali paketni olib tashlang va o'rnatish skriptlarini taqiqlang.</p>
      </div>
      <div class="card">
        <span class="badge" style="background:var(--warning); color:#fff;">3</span>
        <h3 data-ru="Шаг 3: Аудит" data-en="Step 3: Audit">3-Qadam: Audit</h3>
        <p data-ru="Запустите npm audit и npm audit fix. Запишите, какие уязвимости закрыты." data-en="Run npm audit and npm audit fix. Record which vulnerabilities were closed.">npm audit va npm audit fix ni ishga tushiring. Qaysi zaifliklar yopilganini yozib oling.</p>
        <span class="badge" style="background:var(--success); color:#fff; margin-top:8px;">4</span>
        <h3 data-ru="Шаг 4: Отчёт" data-en="Step 4: Report">4-Qadam: Hisobot</h3>
        <p data-ru="Составьте отчёт: пакет, риск, действие, результат. 10-балльная рубрика — в varaqa." data-en="Write a report: package, risk, action, result. The 10-point rubric is in the worksheet.">Hisobot tuzing: paket, xavf, harakat, natija. 10 ballik mezon varaqada.</p>
      </div>
    </div>
"""))

S9.append(slide(11, "Refleksiya|Рефлексия|Reflection", "68:00–74:00", """
    <div class="eyebrow"><span class="t" data-ru="ПАРНАЯ ПРОВЕРКА · АУДИТ АУДИТА" data-en="PEER REVIEW · AUDIT THE AUDIT">JUFTLIKDA TEKSHIRUV · AUDITNI AUDIT QILISH</span></div>
    <h2 data-ru="Проверьте Отчёт Одноклассника по 5 Пунктам" data-en="Review a Classmate's Report in 5 Checks">Partadoshingiz Hisobotini 5 Bandda Tekshiring</h2>
    <div class="grid-3">
      <div class="card">
        <h3 data-ru="Lockfile" data-en="Lockfile">Lockfile</h3>
        <p data-ru="Закоммичен ли package-lock.json? Совпадают ли версии с package.json?" data-en="Is package-lock.json committed? Do the versions match package.json?">package-lock.json commit qilinganmi? Versiyalar package.json bilan mosmi?</p>
      </div>
      <div class="card">
        <h3 data-ru="Скрипты" data-en="Scripts">Skriptlar</h3>
        <p data-ru="Остались ли postinstall/preinstall? Если да — объяснено ли, зачем они нужны?" data-en="Any postinstall/preinstall left? If yes, is their purpose explained?">postinstall/preinstall qolganmi? Qolgan bo'lsa, nima uchun kerakligi tushuntirilganmi?</p>
      </div>
      <div class="card">
        <h3 data-ru="Audit" data-en="Audit">Audit</h3>
        <p data-ru="Есть ли вывод npm audit до и после? Снизился ли severity?" data-en="Is there npm audit output before and after? Did severity drop?">npm audit natijasi oldin va keyin bormi? Severity pasayganmi?</p>
      </div>
    </div>
"""))

S9.append(slide(12, "Demo|Демо|Demo", "74:00–77:00", """
    <div class="eyebrow"><span class="t" data-ru="ДЕМО · ЧЕК-ЛИСТ БЕЗОПАСНОСТИ" data-en="DEMO · SECURITY CHECKLIST">DEMO · XAVFSIZLIK CHEK-LISTI</span></div>
    <h2 data-ru="Две Команды Показывают Результат" data-en="Two Teams Present Their Result">Ikki Jamoa Natijani Ko'rsatadi</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Что Показать" data-en="What to Show">Nimani Ko'rsatish</h3>
        <ul style="font-size:12px; line-height:1.75; margin-top:8px;">
          <li data-ru="Подозрительный пакет до исправления." data-en="The suspicious package before the fix.">Tuzatishdan oldingi shubhali paket.</li>
          <li data-ru="Diff package.json и lockfile." data-en="The package.json and lockfile diff.">package.json va lockfile diffi.</li>
          <li data-ru="Вывод npm audit до и после." data-en="npm audit output before and after.">npm audit natijasi oldin va keyin.</li>
        </ul>
      </div>
      <div class="card">
        <h3 data-ru="Чек-лист Безопасности" data-en="Security Checklist">Xavfsizlik Chek-Listi</h3>
        <ul style="font-size:12px; line-height:1.75; margin-top:8px;">
          <li data-ru="✅ Lockfile в Git" data-en="✅ Lockfile in Git">✅ Lockfile Git'da</li>
          <li data-ru="✅ Точные версии для критичных пакетов" data-en="✅ Exact versions for critical packages">✅ Muhim paketlar uchun aniq versiyalar</li>
          <li data-ru="✅ Нет лишних postinstall" data-en="✅ No unnecessary postinstall">✅ Ortiqcha postinstall yo'q</li>
          <li data-ru="✅ npm audit без high/critical" data-en="✅ npm audit clean of high/critical">✅ npm audit'da high/critical yo'q</li>
          <li data-ru="✅ devDependencies отделены" data-en="✅ devDependencies separated">✅ devDependencies ajratilgan</li>
        </ul>
      </div>
    </div>
"""))

S9.append(slide(13, "Xulosa|Итог|Summary", "77:00–80:00", """
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ · ДОМАШНЕЕ ЗАДАНИЕ" data-en="SUMMARY · HOMEWORK">XULOSA · UY VAZIFASI</span></div>
    <h2 data-ru="Итог: Доверяй, Но Проверяй Зависимости" data-en="Summary: Trust, but Verify Your Dependencies">Xulosa: Ishon, Lekin Bog'liqliklarni Tekshir</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Уровень 1 · 4 балла" data-en="Tier 1 · 4 pts">1-Daraja · 4 ball</div>
        <h3 data-ru="Повторить Аудит" data-en="Repeat the Audit">Auditni Takrorlash</h3>
        <p data-ru="Запустите npm audit в своём проекте и запишите все high/critical уязвимости." data-en="Run npm audit in your project and list every high/critical vulnerability.">Loyihangizda npm audit ishga tushiring va barcha high/critical zaifliklarni yozing.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(234,179,8,0.15); color:var(--warning);" data-ru="Уровень 2 · 4 балла" data-en="Tier 2 · 4 pts">2-Daraja · 4 ball</div>
        <h3 data-ru="Свой Lockfile" data-en="Your Own Lockfile">O'z Lockfile'ingiz</h3>
        <p data-ru="Создайте проект, зафиксируйте версии, закоммитьте lockfile и настройте npm ci в CI." data-en="Create a project, pin versions, commit the lockfile, and wire npm ci into CI.">Loyiha yarating, versiyalarni qulflang, lockfile'ni commit qiling va CI'da npm ci sozlang.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Уровень 3 · 2 балла" data-en="Tier 3 · 2 pts">3-Daraja · 2 ball</div>
        <h3 data-ru="Сценарий Атаки" data-en="Attack Scenario">Hujum Ssenariysi</h3>
        <p data-ru="Опишите, как typosquatting + postinstall украдёт .env, и предложите три защиты." data-en="Describe how typosquatting + postinstall would steal .env, and propose three defenses.">Typosquatting + postinstall .env ni qanday o'g'irlashini yozing va uchta himoya taklif qiling.</p>
      </div>
    </div>
    <div class="box" style="margin-top:12px; text-align:center;">
      <p style="font-size:12px;" data-ru="📝 Интерактивное задание и 10-балльная рубрика: <a href='vazifa.html' style='color:var(--accent); font-weight:700;'>vazifa.html</a>" data-en="📝 Interactive homework and 10-point rubric: <a href='vazifa.html' style='color:var(--accent); font-weight:700;'>vazifa.html</a>">📝 Interaktiv vazifa va 10 ballik mezon: <a href="vazifa.html" style="color:var(--accent); font-weight:700;">vazifa.html</a></p>
    </div>
"""))

NOTES9 = {
    "uz": [
        ["Kirish va Maqsad", "Bugun npm ekotizimi va ta'minot zanjiri xavfsizligini o'rganamiz. Har bir npm install begona kodni ishga tushiradi.", "Mavzuni e'lon qiling va 80 daqiqalik rejani tushuntiring."],
        ["Uy Vazifasi Tahlili", "34-darsda formalarni tekshirdik. Asosiy xato — faqat client-side validatsiya va ReDoS. Server-side va ankorlangan regex kerak.", "Blitz savolga javob oling va paketlar xavfiga ko'prik quring."],
        ["NPM Ekotizimi", "Ikki milliondan ortiq paket, tranzitiv bog'liqliklar va postinstall skriptlari. npm install — bu kod ijrosi.", "O'quvchilardan o'z loyihalaridagi paketlar sonini so'rang."],
        ["package.json va lockfile", "package.json niyatni, lockfile faktni yozadi. Lockfile Git'da bo'lishi shart.", "Ikkala faylni doskada taqqoslang."],
        ["SemVer", "^ minor va patch, ~ faqat patch. left-pad keysi bog'liqlik riskini ko'rsatadi.", "Har bir belgiga misol keltiring."],
        ["dependencies va devDependencies", "Runtime va build paketlarini ajratamiz. Serverda npm ci --omit=dev ishlatamiz.", "package.json namunasini ko'rsating."],
        ["Typosquatting va postinstall", "crossenv kabi xatoli nomlar va postinstall orqali .env o'g'irlash. --ignore-scripts va audit bilan himoyalanamiz.", "Hujum sxemasini doskada chizing."],
        ["Viktorina", "To'rt savol orqali lockfile, SemVer, typosquatting va npm ci ni mustahkamlaymiz.", "Javoblarni qo'l ko'tarish orqali oling."],
        ["npm audit", "Audit zaifliklarni severity bo'yicha ko'rsatadi. --force bilan ehtiyot bo'ling.", "Buyruqlarni terminalda ko'rsating."],
        ["Lockfile va CI", "npm ci lockfile bo'yicha qat'iy o'rnatadi. CI'da audit high/critical bo'lsa build yiqiladi.", "GitHub Actions YAMLni tushuntiring."],
        ["Laboratoriya", "O'quvchilar lab papkasidagi troyan paketni topib, olib tashlab, audit qiladilar.", "20 daqiqa vaqt bering va har bir qadamni tekshiring."],
        ["Juftlikda Tekshiruv", "Partadoshlar lockfile, skriptlar va audit natijasini tekshiradi.", "Ikki juftlikni tanlab, xulosasini tinglang."],
        ["Demo va Chek-list", "Ikki jamoa natijani ko'rsatadi. Besh bandli xavfsizlik chek-listini yodda tuting.", "Vaqtni 3 daqiqa bilan cheklang."],
        ["Xulosa va Uy Vazifasi", "Bog'liqliklarni tekshirish — professional odat. Uy vazifasi uch darajali, mezon vazifa.html da.", "Barcha o'quvchilarga havolani ko'rsating."],
    ],
    "ru": [
        ["Введение и Цель", "Сегодня изучаем экосистему npm и безопасность цепочки поставок. Каждый npm install запускает чужой код.", "Объявите тему и план на 80 минут."],
        ["Разбор Домашнего Задания", "На 34-м уроке мы валидировали формы. Главная ошибка — только клиентская проверка и ReDoS. Нужен сервер и якорная регулярка.", "Получите ответ на блиц-вопрос и перейдите к пакетам."],
        ["Экосистема NPM", "Два миллиона пакетов, транзитивные зависимости и postinstall-скрипты. npm install — это исполнение кода.", "Спросите учеников, сколько пакетов в их проектах."],
        ["package.json и lockfile", "package.json описывает намерение, lockfile — факт. Lockfile обязан быть в Git.", "Сравните оба файла на доске."],
        ["SemVer", "^ разрешает минор и патч, ~ только патч. Кейс left-pad показывает риск зависимостей.", "Приведите пример на каждый символ."],
        ["dependencies и devDependencies", "Разделяем runtime и build-пакеты. На сервере используем npm ci --omit=dev.", "Покажите пример package.json."],
        ["Typosquatting и postinstall", "Опечатки вроде crossenv и кража .env через postinstall. Защита — --ignore-scripts и audit.", "Нарисуйте схему атаки на доске."],
        ["Викторина", "Четыре вопроса закрепляют lockfile, SemVer, typosquatting и npm ci.", "Соберите ответы поднятием руки."],
        ["npm audit", "Audit показывает уязвимости по severity. С --force будьте осторожны.", "Покажите команды в терминале."],
        ["Lockfile и CI", "npm ci ставит строго по lockfile. В CI при high/critical сборка падает.", "Объясните YAML GitHub Actions."],
        ["Лаборатория", "Ученики находят троянский пакет в папке lab, удаляют его и запускают audit.", "Дайте 20 минут и проверяйте каждый шаг."],
        ["Парная Проверка", "Одноклассники проверяют lockfile, скрипты и результаты audit.", "Выберите две пары и заслушайте выводы."],
        ["Демо и Чек-лист", "Две команды показывают результат. Запомните чек-лист из пяти пунктов.", "Ограничьте демо тремя минутами."],
        ["Итог и Домашнее Задание", "Проверять зависимости — профессиональная привычка. Домашка трёхуровневая, рубрика в vazifa.html.", "Покажите всем ссылку."],
    ],
    "en": [
        ["Intro & Goal", "Today we study the npm ecosystem and supply-chain security. Every npm install executes someone else's code.", "Announce the topic and the 80-minute plan."],
        ["Homework Review", "In Lesson 34 we validated forms. The main bug was client-only validation and ReDoS. We need server-side checks and anchored regex.", "Take the blitz answer and bridge into packages."],
        ["NPM Ecosystem", "Two million packages, transitive dependencies, and postinstall scripts. npm install is code execution.", "Ask students how many packages their projects have."],
        ["package.json & lockfile", "package.json describes intent, the lockfile records reality. The lockfile must be committed.", "Compare both files on the board."],
        ["SemVer", "^ allows minor and patch, ~ only patch. The left-pad incident shows dependency risk.", "Give an example for each symbol."],
        ["dependencies & devDependencies", "Separate runtime and build packages. Use npm ci --omit=dev on the server.", "Show a package.json example."],
        ["Typosquatting & postinstall", "Typos like crossenv and .env theft via postinstall. Defend with --ignore-scripts and audit.", "Draw the attack flow on the board."],
        ["Quiz", "Four questions reinforce lockfile, SemVer, typosquatting, and npm ci.", "Collect answers by a show of hands."],
        ["npm audit", "Audit lists vulnerabilities by severity. Be careful with --force.", "Show the commands in the terminal."],
        ["Lockfile & CI", "npm ci installs strictly from the lockfile. In CI, high/critical fails the build.", "Explain the GitHub Actions YAML."],
        ["Lab", "Students find the trojan package in the lab folder, remove it, and run audit.", "Allow 20 minutes and check each step."],
        ["Peer Review", "Classmates audit the lockfile, scripts, and audit output.", "Pick two pairs and hear their findings."],
        ["Demo & Checklist", "Two teams present. Remember the five-point security checklist.", "Cap the demo at three minutes."],
        ["Summary & Homework", "Verifying dependencies is a professional habit. Homework has three tiers and a rubric in vazifa.html.", "Show everyone the link."],
    ],
}


def main():
    build_deck(
        os.path.join(REPO_ROOT, "classes", "10-11-sinf", "12-hafta",
                     "32-dars-avtonom-cli-agentlar-va-opencode", "prezentatsiya.html"),
        os.path.join(REPO_ROOT, "classes", "10-11-sinf", "12-hafta",
                     "31-dars-vision-agentlar-va-computer-use", "prezentatsiya.html"),
        "\n\n".join(S10),
        NOTES10,
    )
    build_deck(
        os.path.join(REPO_ROOT, "classes", "9-sinf", "12-hafta",
                     "36-dars-veb-ilova-tezligi-kesh-assetlar-va-lighthouse-auditi", "prezentatsiya.html"),
        os.path.join(REPO_ROOT, "classes", "9-sinf", "12-hafta",
                     "35-dars-npm-ekotizimi-va-xavfsizlik-auditi", "prezentatsiya.html"),
        "\n\n".join(S9),
        NOTES9,
    )


if __name__ == "__main__":
    main()
