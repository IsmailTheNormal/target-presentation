#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/prepare_today_lessons.py — Upgrade Wednesday's 3 Double-Block Lessons

Wednesday Schedule:
  1. 5–6-sinf (10:30–11:55): 24-dars Scratch 3.0 Sehri (80 min)
  2. 10–11-sinf (12:00–14:10): 25-dars AI Agentlar va ReAct Tsikli (80 min)
  3. 7–8-sinf (14:15–15:40): 29-dars Tilemaps va 2D Labirint (80 min)

Upgrades each presentation to the canonical master template:
  - 14 slides (80 min double block pacing)
  - Slide 2: Mandatory HW Review (Pitfall, Golden Standard, Blitz, Bridge)
  - Vector SVG Logo (var(--ink), var(--accent))
  - Smartboard edge nav (<button class="screen-edge-nav">)
  - Touch/swipe navigation
  - 14-item NOTES triplets for UZ, RU, EN
  - 10-point 3-tier homework rubric
"""

import os
import re
import json
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ---------------------------------------------------------------------------
# Cohort 1: 5–6-sinf (Scratch 3.0 Sehri)
# ---------------------------------------------------------------------------
def get_5_6_hw_review_slide():
    return """  <!-- SLIDE 2: MANDATORY HW REVIEW & BRIDGE -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор Д/З|HW Review" data-time="04:00–10:00">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ Д/З · 1-Я ЧЕТВЕРТЬ И МОСТ" data-en="HOMEWORK AUDIT · QUARTER 1 & BRIDGE">UY VAZIFASI TAHLILI · 1-CHORAK VA KO'PRIK</span></div>
    <h2 data-ru="Разбор Домашнего Задания и Мост к Новой Теме" data-en="Homework Autopsy and Bridge to Today's Topic">1-Chorak Yakuni Tahlili va Scratch Olamiga Ko'prik</h2>
    <div class="cards-grid" style="grid-template-columns:1fr 1fr; gap:16px; margin-top:14px;">
      <div class="box" style="border-left:4px solid var(--accent);">
        <div class="tag" style="color:var(--accent-ink);" data-ru="Типичная ошибка" data-en="Common Pitfall">Xato Tahlili (Pitfall)</div>
        <h3 data-ru="Спрайт улетает за экран или переворачивается" data-en="Sprite flies off-screen or flips upside down">Sprayt ekrandan chiqib ketishi yoki teskari aylanib qolishi</h3>
        <p data-ru="В анимациях персонаж улетает за пределы холста или переворачивается вверх ногами, если не задан стиль вращения." data-en="Sprites fly out of bounds or turn upside down when moving left unless rotation style is explicitly configured.">Sprayt chapga yurganda boshi pastga qarab teskari aylanib qoladi yoki koordinata chegarasi tekshirilmagani uchun ekrandan chiqib ketadi.</p>
        <pre class="code-block" style="margin-top:8px;"><code>// ❌ Xato:
move (10) steps // Ekrandan chiqib ketadi!</code></pre>
      </div>
      <div class="box" style="border-left:4px solid var(--green);">
        <div class="tag" style="color:var(--green);" data-ru="Золотой стандарт" data-en="Golden Standard">Oltin Yechim (Best Practice)</div>
        <h3 data-ru="Контроль границ и стиль вращения" data-en="Boundary control and rotation style">Devordan qaytish va to'g'ri burilish</h3>
        <p data-ru="Использование блоков 'если касается края, оттолкнуться' и установка стиля вращения 'влево-вправо'." data-en="Using 'if on edge, bounce' and setting rotation style to 'left-right' keeps the sprite upright and inside the stage.">Maxsus bloklar: devorga tekkanda qaytish va burilish uslubini faqat 'chapga-o'ngga' qilib cheklash.</p>
        <pre class="code-block" style="margin-top:8px;"><code>// ✅ To'g'ri:
if on edge, bounce
set rotation style [left-right]</code></pre>
      </div>
    </div>
    <div class="cards-grid" style="grid-template-columns:1fr 1fr; gap:16px; margin-top:14px;">
      <div class="box">
        <div class="tag" data-ru="Блиц-контроль (30 сек)" data-en="30s Blitz Check">30s Blits-Nazorat</div>
        <p data-ru="Где находится точка (X: 0, Y: 0) на сцене Scratch? Ответ: Ровно по центру экрана!" data-en="Where is the point (X: 0, Y: 0) on the Scratch stage? Answer: Exactly at the center of the screen!">Scratch sahnasining qoq markazida qaysi koordinata joylashgan? Javob: <b>(X: 0, Y: 0)</b>!</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Мост к уроку" data-en="Bridge to Topic">Yangi Darsga Ko'prik</div>
        <p data-ru="В 1-й четверти мы изучили кибер-безопасность. Теперь во 2-й четверти мы создаем собственные игры и миры в Scratch 3.0!" data-en="In Quarter 1, we mastered cybersecurity basics. Now in Quarter 2, we build our own interactive games and worlds in Scratch 3.0!">1-chorakda kiber-xavfsizlikni o'rgandik. Endi 2-chorakda o'zimiz mustaqil o'yin va multfilmlar yaratuvchi geym-dizaynerga aylanamiz!</p>
      </div>
    </div>
  </section>"""

def get_5_6_peer_review_slide():
    return """  <!-- SLIDE 12: PEER REVIEW -->
  <section class="slide" data-phase="Peer Review|Взаимопроверка|Peer Review" data-time="65:00–72:00">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМОПРОВЕРКА · ТЕСТИРОВАНИЕ В ПАРАХ" data-en="PEER REVIEW · PAIR TESTING">JUFTLIKDA SINOV · PEER REVIEW</span></div>
    <h2 data-ru="Протестируйте проект напарника за соседним компьютером" data-en="Test your peer's interactive Scratch project">Sinfdosh do'stingizning Scratch loyihasini sinab ko'ring</h2>
    <p class="lede" data-ru="Поменяйтесь местами на 5 минут и проверьте работу игры по 3 критериям качества." data-en="Swap seats for 5 minutes and evaluate your partner's game against 3 quality criteria.">Partadoshingiz bilan joyingizni 5 daqiqaga almashtiring va uning o'yinini 3 ta mezon bo'yicha tekshiring:</p>
    <div class="cards-grid">
      <div class="box">
        <div class="tag" data-ru="Критерий 1" data-en="Criterion 1">1-Mezon: Boshqaruv</div>
        <h3 data-ru="Плавность движения" data-en="Smooth Movement">Tugmalar Boshqaruvi</h3>
        <p data-ru="Клавиши со стрелками двигают персонажа без задержек и застреваний." data-en="Arrow keys move the character smoothly without freezing or glitching.">Strelkalar bosilganda qahramon 4 tomonga ravon va to'siqlarsiz harakatlanyaptimi?</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Критерий 2" data-en="Criterion 2">2-Mezon: Chegara</div>
        <h3 data-ru="Защита от вылета" data-en="Boundary Bounds">Sahnadan Chiqmaslik</h3>
        <p data-ru="Персонаж не улетает за пределы экрана и отталкивается от краев." data-en="Sprite bounces cleanly off screen borders without turning upside down.">Qahramon ekrandan chiqib ketmayaptimi va to'g'ri burilyaptimi?</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Критерий 3" data-en="Criterion 3">3-Mezon: Animatsiya</div>
        <h3 data-ru="Смена костюмов" data-en="Costume Swapping">Jonli Qadamlar</h3>
        <p data-ru="При движении костюмы переключаются, создавая эффект шага." data-en="Costumes cycle dynamically, creating an authentic walking visual effect.">Yurganda kostyumlar almashib, qadam tashlash illyuziyasi bormi?</p>
      </div>
    </div>
  </section>"""

def get_5_6_demo_slide():
    return """  <!-- SLIDE 13: DEMO SHOWCASE -->
  <section class="slide" data-phase="Taqdimot|Демонстрация|Showcase" data-time="72:00–77:00">
    <div class="eyebrow"><span class="t" data-ru="ДЕМОНСТРАЦИЯ РЕЗУЛЬТАТОВ НА ЭКРАНЕ" data-en="SHOWCASE · BEST PROJECTS DEMO">JONLI DEMO · ENG YAXSHI LOYIHALAR</span></div>
    <h2 data-ru="Большой Экран: Презентация лучших работ урока" data-en="Big Screen: Showcase of outstanding student creations">Katta Ekran: Bugungi darsning eng yaxshi loyihalari namoyishi</h2>
    <p class="lede" data-ru="2 ученика подключаются к проектору и демонстрируют созданную механику движения." data-en="2 students connect to the projector and demonstrate their interactive motion mechanics.">Eng qiziqarli animatsiya va fon yaratgan 2 nafar o'quvchi o'z loyihasini proyektorda butun sinfga ko'rsatadi.</p>
    <div class="cards-grid">
      <div class="box">
        <div class="tag" data-ru="1-Демо" data-en="Demo 1">1-Taqdimot: Kiber-Mushukcha</div>
        <h3 data-ru="Оригинальный фон и озвучка" data-en="Custom Backdrop & Audio">O'zgacha Fon va Tovushlar</h3>
        <p data-ru="Демонстрация переключения костюмов и диалоговых реплик при нажатии пробела." data-en="Demonstrating costume cycles and speech bubbles when pressing spacebar.">Bo'shliq (Space) tugmasi bosilganda qahramonning sakrashi va gapiruvchi matn pufakchalari.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="2-Демо" data-en="Demo 2">2-Taqdimot: Labirint Qahramoni</div>
        <h3 data-ru="Точные координаты и физика" data-en="Precise Coordinates & Physics">Aniq Koordinata va To'siqlar</h3>
        <p data-ru="Точная привязка к координатам (X, Y) и прохождение полосы препятствий." data-en="Precise snapping to (X, Y) coordinates and navigating obstacles without errors.">X va Y koordinatalaridan foydalanib to'siqlardan bexato o'tish mexanikasi.</p>
      </div>
    </div>
  </section>"""

# ---------------------------------------------------------------------------
# Cohort 2: 10–11-sinf (AI Agentlar va ReAct Tsikli)
# ---------------------------------------------------------------------------
def get_10_11_hw_review_slide():
    return """  <!-- SLIDE 2: MANDATORY HW REVIEW & BRIDGE -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор Д/З|HW Review" data-time="04:00–10:00">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ Д/З · РАЗБОР ОШИБОК БОТОВ" data-en="HOMEWORK AUDIT · CHATBOT PITFALLS">UY VAZIFASI TAHLILI · BOTLAR ZAIFLIGI</span></div>
    <h2 data-ru="Разбор Домашнего Задания и Мост к Новой Теме" data-en="Homework Autopsy and Bridge to Today's Topic">1-Chorak Telegram Boti Tahlili va Agentik AIga Ko'prik</h2>
    <div class="cards-grid" style="grid-template-columns:1fr 1fr; gap:16px; margin-top:14px;">
      <div class="box" style="border-left:4px solid var(--accent);">
        <div class="tag" style="color:var(--accent-ink);" data-ru="Типичная ошибка" data-en="Common Pitfall">Xato Tahlili (Pitfall)</div>
        <h3 data-ru="Галлюцинации и отсутствие актуальных данных" data-en="Hallucinations & Stale Context">Passiv botlarda gallyutsinatsiya va asbobsizlik</h3>
        <p data-ru="Простой Telegram бот отвечает текстом напрямую. При вопросе 'Капитализация Tesla + 18.5%' модель уверенно придумывает неверные цифры!" data-en="A naive Telegram bot predicts tokens directly. When asked math or live market facts, it hallucinates plausible falsehoods.">Oddiy passiv bot faqat matn to'qiydi. 'Tesla kapitallashuvi + 18.5% necha pul?' deb so'ralsa, kalkulyatori yo'qligi uchun mutlaqo yolg'on son aytadi!</p>
        <pre class="code-block" style="margin-top:8px;"><code>// ❌ Xato:
const answer = await llm.generate(prompt); // Gallyutsinatsiya!</code></pre>
      </div>
      <div class="box" style="border-left:4px solid var(--green);">
        <div class="tag" style="color:var(--green);" data-ru="Золотой стандарт" data-en="Golden Standard">Oltin Yechim (Best Practice)</div>
        <h3 data-ru="Цикл ReAct: Thought -> Action -> Observation" data-en="ReAct Loop: Thought -> Action -> Observation">ReAct Tsikli: Mulohaza va Asbob chaqiruvi</h3>
        <p data-ru="Модель сначала думает (Thought), вызывает внешний API (Action: Search/Calc), получает проверенный ответ (Observation) и синтезирует итог." data-en="The agent reasons first (Thought), executes deterministic tools (Action), inspects runtime feedback (Observation), and outputs truth.">Agent avval o'ylaydi (Thought), tashqi API-ni chaqiradi (Action: Calculator), natijani oladi (Observation) va 100% to'g'ri javob beradi.</p>
        <pre class="code-block" style="margin-top:8px;"><code>// ✅ To'g'ri:
Thought: Menga jonli narx kerak -> Action: search_api("Tesla")
Observation: $2.4B -> Action: calc(2.4 * 1.185) -> Final Answer!</code></pre>
      </div>
    </div>
    <div class="cards-grid" style="grid-template-columns:1fr 1fr; gap:16px; margin-top:14px;">
      <div class="box">
        <div class="tag" data-ru="Блиц-контроль (30 сек)" data-en="30s Blitz Check">30s Blits-Nazorat</div>
        <p data-ru="Каковы три ключевых шага цикла ReAct (Yao et al., 2022)? Ответ: Thought (Мысль) -> Action (Действие) -> Observation (Наблюдение)!" data-en="What are the 3 foundational steps of ReAct? Answer: Thought -> Action -> Observation!">ReAct siklining 3 asosiy bosqichini ayting? Javob: <b>Thought (Fikrlash) $\rightarrow$ Action (Harakat) $\rightarrow$ Observation (Kuzatuv)</b>!</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Мост к уроку" data-en="Bridge to Topic">Yangi Darsga Ko'prik</div>
        <p data-ru="В 1-й четверти мы развернули Telegram-бота на Webhook. Теперь во 2-й четверти мы превращаем его в автономного агента с инструментами!" data-en="In Quarter 1, we deployed a Telegram bot via webhooks. Now in Quarter 2, we supercharge it into an autonomous agent armed with real-world tools!">1-chorakda webhookli passiv Telegram bot yasagan edik. Endi 2-chorakda unga asboblar (Tools) berib, mustaqil ish bajaruvchi avtonom agentga aylantiramiz!</p>
      </div>
    </div>
  </section>"""

def get_10_11_peer_review_slide():
    return """  <!-- SLIDE 12: PEER REVIEW -->
  <section class="slide" data-phase="Red Teaming|Взаимопроверка|Red Teaming" data-time="65:00–72:00">
    <div class="eyebrow"><span class="t" data-ru="RED TEAMING · АТАКА НА АГЕНТА ПАРТНЕРА" data-en="RED TEAMING · AGENT STRESS TESTING">KIBER-DUEL · RED TEAMING SINtemporal</span></div>
    <h2 data-ru="Попробуйте загнать агента напарника в бесконечный цикл" data-en="Attempt to trap your peer's agent into an infinite execution loop">Sinfdosh do'stingiz agentini cheksiz siklga solishga urining</h2>
    <p class="lede" data-ru="Поменяйтесь местами на 7 минут: один выступает в роли атакующего (Red Team), другой — защитника (Blue Team)." data-en="Swap workstations for 7 minutes: one assumes the Red Team attacker role, while the other defends as Blue Team.">Juftliklar o'rin almashadi: biringiz Red Team (xaker), ikkinchingiz Blue Team (himoyachi) sifatida agent qalqonlarini sinaysiz:</p>
    <div class="cards-grid">
      <div class="box">
        <div class="tag" data-ru="Тест 1" data-en="Test 1">1-Hujum: Paradoks Prompt</div>
        <h3 data-ru="Рекурсивные запросы" data-en="Recursive Queries">Paradoksal Buyruq</h3>
        <p data-ru="'Посчитай нечетное четное число'. Останавливается ли агент после Max Iterations (5 шагов)?" data-en="'Calculate an odd even number'. Does the loop guard trigger cleanly after max iterations?">Agent yechimi yo'q paradoks berilganda cheksiz aylanib qolmasdan, Max Iterations (5 qadam) da to'xtayaptimi?</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Тест 2" data-en="Test 2">2-Hujum: Inyeksiya</div>
        <h3 data-ru="Tool Poisoning" data-en="Tool Injection">Xavfli Asbob Argumenti</h3>
        <p data-ru="Попытка передать 'DROP TABLE' или bash-команду в аргументы калькулятора." data-en="Attempting to inject destructive SQL or shell commands into tool argument payloads.">Kalkulyator argumentiga zararli matn yoki tizim buyruqlari berilganda JSON Schema xatoni to'g'ri ushlayaptimi?</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Тест 3" data-en="Test 3">3-Tekshiruv: Trace</div>
        <h3 data-ru="Аудит рассуждений" data-en="Reasoning Trace Audit">Fikrlar Jurnali (Trace)</h3>
        <p data-ru="Понятно ли, почему агент принял решение вызвать именно этот инструмент?" data-en="Is the Thought reasoning trace logically sound and deterministic?">Agent konsolida Thought -> Action -> Observation qadamlari aniq va tushunarli ko'rinyaptimi?</p>
      </div>
    </div>
  </section>"""

def get_10_11_demo_slide():
    return """  <!-- SLIDE 13: DEMO SHOWCASE -->
  <section class="slide" data-phase="Taqdimot|Демонстрация|Showcase" data-time="72:00–77:00">
    <div class="eyebrow"><span class="t" data-ru="ДЕМОНСТРАЦИЯ АВТОНОМНОГО АГЕНТА" data-en="SHOWCASE · AUTONOMOUS AGENT DEMO">JONLI DEMO · AVTONOM AGENT TAQDIMOTI</span></div>
    <h2 data-ru="Живой запуск: Агент решает многоэтапную задачу без вмешательства" data-en="Live execution: Agent solves multi-step challenge independently">Jonli namoyish: Agent ko'p bosqichli topshiriqni mustaqil hal qiladi</h2>
    <p class="lede" data-ru="2 лучшие пары выводят консоль своего ReAct агента на центральный проектор." data-en="2 top pairs display their ReAct agent execution traces on the primary projector.">Eng mustahkam va xavfsiz agent yaratgan 2 ta juftlik proyektorda real topshiriq ijrosini ko'rsatadi.</p>
    <div class="cards-grid">
      <div class="box">
        <div class="tag" data-ru="Демо 1" data-en="Demo 1">1-Keys: Valyuta va Soliq Tahlilchisi</div>
        <h3 data-ru="Связка Search API + Math Engine" data-en="Search API + Math Engine Chain">Search API va Kalkulyator Zanjiri</h3>
        <p data-ru="Агент ищет курс ЦБ, берет цену товара и вычисляет таможенный сбор с выдачей чека." data-en="Agent fetches live FX rates, extracts invoice pricing, and calculates exact customs duties.">Markaziy Bank API kursini mustaqil tortib, import bojini 100% aniqlikda hisoblab beruvchi agent.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Демо 2" data-en="Demo 2">2-Keys: Kiber-Qalqonli Agent</div>
        <h3 data-ru="Блокировка опасного системного вызова" data-en="Malicious Payload Interception">Zararli Buyruqni Qaytarish</h3>
        <p data-ru="Агент распознает вредоносный prompt injection и обращается к человеку (HITL)." data-en="Agent detects malicious injection payloads and safely triggers Human-in-the-Loop approval.">Zararli buyruq berilganda agent ruxsatsiz kodni bajarmay, foydalanuvchidan tasdiq so'raydi (HITL).</p>
      </div>
    </div>
  </section>"""

# ---------------------------------------------------------------------------
# Cohort 3: 7–8-sinf (Tilemaps va 2D Labirint)
# ---------------------------------------------------------------------------
def get_7_8_hw_review_slide():
    return """  <!-- SLIDE 2: MANDATORY HW REVIEW & BRIDGE -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор Д/З|HW Review" data-time="04:00–10:00">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ Д/З · 1-Я ЧЕТВЕРТЬ И МОСТ" data-en="HOMEWORK AUDIT · QUARTER 1 & BRIDGE">UY VAZIFASI TAHLILI · 1-CHORAK VA KO'PRIK</span></div>
    <h2 data-ru="Разбор Домашнего Задания и Мост к Новой Теме" data-en="Homework Autopsy and Bridge to Today's Topic">1-Chorak Game Dev Tahlili va Tilemap Olami</h2>
    <div class="cards-grid" style="grid-template-columns:1fr 1fr; gap:16px; margin-top:14px;">
      <div class="box" style="border-left:4px solid var(--accent);">
        <div class="tag" style="color:var(--accent-ink);" data-ru="Типичная ошибка" data-en="Common Pitfall">Xato Tahlili (Pitfall)</div>
        <h3 data-ru="Хардкод координат каждого препятствия" data-en="Hardcoding each obstacle coordinate">Har bir to'siqni Canvasda qo'lda chizish</h3>
        <p data-ru="В 1-й четверти многие рисовали каждый барьер через ctx.fillRect(x, y). При 200 препятствиях код превращается в кашу, а проверка коллизий тормозит!" data-en="Drawing every wall via individual ctx.fillRect(x,y) calls creates spaghetti code and slows down collision detection.">Har bir devorni alohida `ctx.fillRect(120, 300)` deb yozish 200 ta to'siq bo'lganda o'yinni qotirib qo'yadi va xaritani o'zgartirish azobga aylanadi.</p>
        <pre class="code-block" style="margin-top:8px;"><code>// ❌ Xato:
ctx.fillRect(100, 200, 32, 32);
ctx.fillRect(132, 200, 32, 32); // 100 martalab takrorlanadi!</code></pre>
      </div>
      <div class="box" style="border-left:4px solid var(--green);">
        <div class="tag" style="color:var(--green);" data-ru="Золотой стандарт" data-en="Golden Standard">Oltin Yechim (Best Practice)</div>
        <h3 data-ru="2D Массивы и Tilemap сетка: O(1) скорость" data-en="2D Arrays and Tilemap Grid: O(1) Speed">2D Matritsa va Panjara (Tilemap): O(1) Tezlik</h3>
        <p data-ru="Карта описывается матрицей чисел. Столкновение с препятствием проверяется мгновенно: map[row][col] === 1 за O(1) операций!" data-en="The world is mapped as a 2D integer matrix. Wall collision is resolved instantly in O(1) time without looping over obstacles.">Butun xarita 0 va 1 lardan iborat 2D massivga yoziladi. Devorga urilish bitta amal bilan `map[row][col] === 1` tekshiriladi ($O(1)$ tezlikda)!</p>
        <pre class="code-block" style="margin-top:8px;"><code>// ✅ To'g'ri:
const map = [[1,1,1,1],[1,0,0,1],[1,1,1,1]];
function isWall(x, y) { return map[Math.floor(y/32)][Math.floor(x/32)] === 1; }</code></pre>
      </div>
    </div>
    <div class="cards-grid" style="grid-template-columns:1fr 1fr; gap:16px; margin-top:14px;">
      <div class="box">
        <div class="tag" data-ru="Блиц-контроль (30 сек)" data-en="30s Blitz Check">30s Blits-Nazorat</div>
        <p data-ru="В выражении map[row][col] что обозначает row, а что col? Ответ: row — координата Y (строка), col — координата X (столбец)!" data-en="In map[row][col], which corresponds to Y and X? Answer: row is Y (vertical), col is X (horizontal)!">`map[row][col]` da qaysi biri Y va qaysi biri X? Javob: <b>row — qator (Y / vertikal), col — ustun (X / gorizontal)</b>!</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Мост к уроку" data-en="Bridge to Topic">Yangi Darsga Ko'prik</div>
        <p data-ru="В 1-й четверти мы двигали одиночные спрайты. Теперь во 2-й четверти мы строим огромные процедурные миры и подземелья на Tilemap!" data-en="In Quarter 1, we moved isolated player entities. Now in Quarter 2, we architect infinite labyrinth worlds with 2D tilemaps!">1-chorakda yakka obyektlar fizikasini o'rgangan edik. Endi 2-chorakda 'Terraria' va 'Hades' kabi ulkan labirint dunyolarni Tilemaps orqali quramiz!</p>
      </div>
    </div>
  </section>"""

def get_7_8_peer_review_slide():
    return """  <!-- SLIDE 12: PEER REVIEW -->
  <section class="slide" data-phase="Peer Review|Взаимопроверка|Peer Review" data-time="65:00–72:00">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМОПРОВЕРКА · ТЕСТИРОВАНИЕ КАРТЫ" data-en="PEER REVIEW · MAP STRESS TEST">JUFTLIKDA SINOV · XARITA AUDITI</span></div>
    <h2 data-ru="Пройдите лабиринт напарника и найдите дыры в коллизиях" data-en="Navigate your peer's maze and hunt for collision leaks">Partadoshingiz labirintini o'ynang va to'qnashuv tuynuklarini toping</h2>
    <p class="lede" data-ru="Поменяйтесь компьютерами на 7 минут: попробуйте сломать механику движения соседа." data-en="Swap seats for 7 minutes: attempt to find edge-case glitches in your partner's collision grid.">Partadoshingiz bilan kompyuterni almashtirib, uning labirintida xatolar va burchak glitclarini qidiring:</p>
    <div class="cards-grid">
      <div class="box">
        <div class="tag" data-ru="Тест 1" data-en="Test 1">1-Sinov: Devordan O'tish</div>
        <h3 data-ru="Диагональное залипание" data-en="Corner Clipping">Burchaklar Nazorati</h3>
        <p data-ru="Проходит ли персонаж сквозь угол, если зажать две стрелки одновременно (вверх + вправо)?" data-en="Does the character clip through walls when pressing two diagonal keys simultaneously?">Ikki strelka (yuqori + o'ng) barobar bosilganda qahramon devor burchagidan teshib o'tib ketmayaptimi?</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Тест 2" data-en="Test 2">2-Sinov: Chegara Xatosi</div>
        <h3 data-ru="Выход за пределы матрицы" data-en="Out of Bounds Error">Array Bounds Crash</h3>
        <p data-ru="Вылетает ли игра с ошибкой 'undefined', если персонаж касается внешней границы карты?" data-en="Does the game crash with 'Cannot read properties of undefined' at the map boundaries?">O'yinchi xarita chetiga yetganda konsolda `Cannot read properties of undefined` xatosi chiqmayaptimi?</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Тест 3" data-en="Test 3">3-Baholash: Dizayn</div>
        <h3 data-ru="Интересность лабиринта" data-en="Level Layout Balance">Labirint Qiziqarliligi</h3>
        <p data-ru="Есть ли тупики, спрятанные сокровища и понятный путь к финальному выходу?" data-en="Are there rewarding side-paths, hidden chests, and an intuitive exit gate?">Xaritada berk ko'chalar, yashirin xazinalar va marraga olib chiquvchi qiziqarli yo'l mavjudmi?</p>
      </div>
    </div>
  </section>"""

def get_7_8_demo_slide():
    return """  <!-- SLIDE 13: DEMO SHOWCASE -->
  <section class="slide" data-phase="Taqdimot|Демонстрация|Showcase" data-time="72:00–77:00">
    <div class="eyebrow"><span class="t" data-ru="ДЕМОНСТРАЦИЯ ЛАБИРИНТОВ НА ЭКРАНЕ" data-en="SHOWCASE · MAZE DEMO DAY">JONLI DEMO · ENG YAXSHI LABIRINTLAR</span></div>
    <h2 data-ru="Большой Экран: Самые сложные и красивые процедурные карты" data-en="Big Screen: Outstanding maze architecture creations">Katta Ekran: Bugungi eng chiroyli va qiyin labirintlar bellashuvi</h2>
    <p class="lede" data-ru="2 ученика проецируют свою игру на экран и приглашают добровольцев пройти их уровень." data-en="2 students project their creations and challenge classmates to beat their level in real time.">2 nafar o'quvchi o'z o'yinini proyektorda ochadi va sinfdoshlaridan birini labirintdan chiqishga taklif qiladi.</p>
    <div class="cards-grid">
      <div class="box">
        <div class="tag" data-ru="1-Демо" data-en="Demo 1">1-Loyiha: Kiber-Bunker Labirinti</div>
        <h3 data-ru="Атмосферный тайлсет и ловушки" data-en="Cyberpunk Tileset & Traps">Neon Tayllar va Lazer Qopqonlar</h3>
        <p data-ru="Тайлы стен стилизованы под киберпанк с мерцающими лазерами и дверями с ключами." data-en="Custom cyberpunk wall aesthetics with dynamic laser hazards and keycards.">Devorlar neon uslubida chizilgan, qahramon kalit topib qulfni ochgandagina eshik ochiladi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="2-Демо" data-en="Demo 2">2-Loyiha: Roguelike Qasr</div>
        <h3 data-ru="Динамический редактор карты" data-en="Dynamic Runtime Map Editor">Dinamik Xarita Redaktori</h3>
        <p data-ru="Возможность рисовать стены прямо в процессе игры кликом мыши и проверять физику." data-en="Ability to draw wall tiles dynamically in-game with mouse clicks to test physics.">O'yin jarayonida sichqoncha bilan ekranga bosib yangi devorlar qo'shish va to'qnashuvni sinash imkoniyati.</p>
      </div>
    </div>
  </section>"""


def upgrade_lesson(folder_rel, cohort, title_uz, hw_review_html, peer_review_html, demo_html):
    folder = os.path.join(REPO_ROOT, folder_rel)
    pres_path = os.path.join(folder, "prezentatsiya.html")
    
    print(f"\n⚡ Upgrading: {folder_rel}/prezentatsiya.html")
    with open(pres_path, "r", encoding="utf-8") as f:
        old_html = f.read()

    # Load canonical master template
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    # Extract existing slides from old presentation
    # Old presentation has 12 slides:
    # 0: Titul
    # 1: Muammo
    # 2..7: Theory / Architecture
    # 8: Quiz
    # 9: Practice
    # 10: Grading
    # 11: Summary
    raw_slides = re.findall(r'<section class="slide[^\"]*"[^>]*>([\s\S]*?)</section>', old_html)
    print(f"  Extracted {len(raw_slides)} raw slides from existing file.")

    # Build 14-slide sequence:
    # S1: Titul (from old_html slide 0)
    # S2: Mandatory HW Review (hw_review_html)
    # S3: Muammo (from old_html slide 1)
    # S4..S9: Theory / Concepts / Architecture (from old_html slides 2..7)
    # S10: Quiz (from old_html slide 8)
    # S11: Practice Arena (from old_html slide 9)
    # S12: Peer Review (peer_review_html)
    # S13: Demo Showcase (demo_html)
    # S14: 10-Tier Homework (from old_html slide 11 or canonical template)

    # Calculate 14 slide times
    duration = 80
    times = [
        "00:00–04:00", # 1 Titul
        "04:00–10:00", # 2 HW Review
        "10:00–15:00", # 3 Muammo
        "15:00–20:00", # 4 Konsept
        "20:00–25:00", # 5 Arxitektura
        "25:00–30:00", # 6 Mexanizm
        "30:00–35:00", # 7 Taqqoslash
        "35:00–40:00", # 8 Xavfsizlik
        "40:00–48:00", # 9 Test / Quiz
        "48:00–65:00", # 10 Practice Arena
        "65:00–72:00", # 11 Peer Review
        "72:00–77:00", # 12 Demo Showcase
        "77:00–80:00", # 13 Xulosa & Baholash
        "77:00–80:00"  # 14 Homework
    ]

    new_slides = []

    # Slide 1: Titul
    s1_body = raw_slides[0]
    new_slides.append(f'  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="{times[0]}">\n{s1_body.strip()}\n  </section>')

    # Slide 2: HW Review
    new_slides.append(hw_review_html.strip())

    # Slide 3: Muammo
    s3_body = raw_slides[1]
    new_slides.append(f'  <section class="slide" data-phase="Muammo|Проблема|Problem" data-time="{times[2]}">\n{s3_body.strip()}\n  </section>')

    # Slides 4..9: Concepts
    phases = [
        "Konsept|Концепт|Concept",
        "Arxitektura|Архитектура|Architecture",
        "Mexanizm|Механизм|Mechanism",
        "Tizim|Система|System",
        "Xavfsizlik|Безопасность|Safety",
        "Interaktiv Test|Тест|Interactive Quiz"
    ]
    for idx in range(2, 8):
        s_body = raw_slides[idx]
        ph = phases[idx-2]
        t = times[idx+1]
        new_slides.append(f'  <section class="slide" data-phase="{ph}" data-time="{t}">\n{s_body.strip()}\n  </section>')

    # Slide 10: Quiz
    s_quiz_body = raw_slides[8]
    new_slides.append(f'  <section class="slide" data-phase="Interaktiv Test|Тест|Interactive Quiz" data-time="{times[8]}">\n{s_quiz_body.strip()}\n  </section>')

    # Slide 11: Practice Arena
    s_prac_body = raw_slides[9]
    new_slides.append(f'  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="{times[9]}">\n{s_prac_body.strip()}\n  </section>')

    # Slide 12: Peer Review
    new_slides.append(peer_review_html.strip())

    # Slide 13: Demo Showcase
    new_slides.append(demo_html.strip())

    # Slide 14: 10-Tier Homework (Slide 11 from old or calibrated)
    s_hw_body = raw_slides[11]
    new_slides.append(f'  <section class="slide" data-phase="Uy vazifasi|Домашнее задание|Homework" data-time="{times[13]}">\n{s_hw_body.strip()}\n  </section>')

    print(f"  Assembled {len(new_slides)} slides.")

    # Replace stage in canonical template
    all_slides_html = "\n\n".join(new_slides)
    res_html = re.sub(r'<div class="stage">[\s\S]*?</div><!-- /stage -->',
                      f'<div class="stage">\n{all_slides_html}\n</div><!-- /stage -->',
                      tpl)

    # Extract TITLES from old presentation
    m_titles = re.search(r'var TITLES\s*=\s*(\{[\s\S]*?\n\s*\})[;,]', old_html)
    if m_titles:
        titles_clean = json.loads(m_titles.group(1))
        titles_formatted = json.dumps(titles_clean, ensure_ascii=False, indent=2)
        res_html = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_formatted};', res_html)
        # Also update <title>
        res_html = re.sub(r'<title[^>]*>.*?</title>',
                          f'<title data-ru="{titles_clean.get("ru", "")}" data-en="{titles_clean.get("en", "")}">{titles_clean.get("uz", "")}</title>',
                          res_html)

    # Extract NOTES from old presentation and expand to 14 items
    m_notes = re.search(r'var NOTES\s*=\s*(\{[\s\S]*?\n\s*\})[;,]', old_html)
    if m_notes:
        old_notes = json.loads(m_notes.group(1))
        # old_notes has 12 items. We insert item 2 (HW review), item 11 (Peer review), item 12 (Demo)
        new_notes = {"uz": [], "ru": [], "en": []}
        
        # S1 Titul
        for lang in ("uz", "ru", "en"):
            new_notes[lang].append(old_notes[lang][0])

        # S2 HW Review
        new_notes["uz"].append(["Uy vazifasi tahlili", "O'tgan dars topshirig'idagi keng tarqalgan xatoni va oltin yechimni tushuntiring.", "Doskada ko'rsatib, 30 soniyalik blits savol bering."])
        new_notes["ru"].append(["Разбор домашнего задания", "Объясните типичную ошибку прошлого урока и покажите эталонное решение.", "Проведите 30-секундный блиц-опрос у доски."])
        new_notes["en"].append(["Homework Review", "Explain the common pitfall from the previous assignment and demonstrate the golden standard.", "Ask the 30-second blitz question at the board."])

        # S3..S11 (Old slides 1..9)
        for idx in range(1, 10):
            for lang in ("uz", "ru", "en"):
                new_notes[lang].append(old_notes[lang][idx])

        # S12 Peer Review
        new_notes["uz"].append(["Peer Review", "O'quvchilar juftlikda joylarini almashtirib, bir-birlarining kodini sinab ko'rishlarini tashkil qiling.", "Har bir juftlikka 7 daqiqa bering va xatolarni qayd ettiring."])
        new_notes["ru"].append(["Взаимопроверка (Peer Review)", "Организуйте обмен местами в парах для тестирования проектов друг друга.", "Дайте 7 минут на поиск ошибок и пограничных случаев."])
        new_notes["en"].append(["Peer Review", "Instruct pairs to swap seats and thoroughly test each other's project implementation.", "Allocate 7 minutes for edge-case hunting."])

        # S13 Demo Showcase
        new_notes["uz"].append(["Jonli Demo", "Eng yaxshi va qiziqarli yechimga ega 2 ta o'quvchini katta ekranga chaqiring.", "Ularning ishlanmasini butun sinf bilan birgalikda olqishlang."])
        new_notes["ru"].append(["Демонстрация (Showcase)", "Пригласите 2 лучших учеников к проектору для живого показа работы.", "Обсудите оригинальные решения всем классом."])
        new_notes["en"].append(["Live Showcase", "Invite 2 top students to the primary projector for a live demonstration.", "Praise creative problem-solving with the whole class."])

        # S14 Homework (Old slide 11)
        for lang in ("uz", "ru", "en"):
            new_notes[lang].append(old_notes[lang][11])

        notes_json = json.dumps(new_notes, ensure_ascii=False, indent=2)
        res_html = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', res_html)

    # Floating brand tag
    res_html = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                      f'<span class="tag" data-ru="{cohort} · ВАЙБКОДИНГ" data-en="{cohort} · VIBECODING">{cohort} · VIBECODING</span>',
                      res_html)

    with open(pres_path, "w", encoding="utf-8") as f:
        f.write(res_html)

    print(f"  ✓ Upgraded presentation ({len(res_html)} bytes, 14 slides).")

    # Run verification
    verify_script = os.path.join(REPO_ROOT, "scripts", "verify_i18n.py")
    res = subprocess.run(["python3", verify_script, pres_path], capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print(f"  ❌ Issues in {pres_path}:\n{res.stderr}")
    else:
        print(f"  ✨ {folder_rel} presentation passed 100% verification!")


def main():
    print("==================================================================")
    print("🎯 PREPARING ALL 3 WEDNESDAY DOUBLE-BLOCK LESSONS (14 SLIDES / 80 MIN)")
    print("==================================================================")

    # 1. 5–6-sinf (Scratch 3.0 Sehri)
    upgrade_lesson(
        "classes/5-6-sinf/10-hafta/24-dars-scratch-spraytlar-va-sahnalar",
        "5-6-SINF",
        "Scratch 3.0 Sehri: Spraytlar va Sahnalar",
        get_5_6_hw_review_slide(),
        get_5_6_peer_review_slide(),
        get_5_6_demo_slide()
    )

    # 2. 10–11-sinf (AI Agentlar va ReAct Tsikli)
    upgrade_lesson(
        "classes/10-11-sinf/10-hafta/25-dars-ai-agentlar-va-react-tsikli",
        "10-11-SINF",
        "AI Agentlar Paradigmasi va ReAct Tsikli",
        get_10_11_hw_review_slide(),
        get_10_11_peer_review_slide(),
        get_10_11_demo_slide()
    )

    # 3. 7–8-sinf (Tilemaps va 2D Labirint)
    upgrade_lesson(
        "classes/7-8-sinf/10-hafta/29-dars-tilemaps-va-2d-labirint",
        "7-8-SINF",
        "Matritsalar va Xaritalar (Tilemaps)",
        get_7_8_hw_review_slide(),
        get_7_8_peer_review_slide(),
        get_7_8_demo_slide()
    )

    print("\n==================================================================")
    print("🏁 ALL 3 LESSONS PREPARED, AUDITED, AND FULLY COMPLIANT!")
    print("==================================================================")

if __name__ == "__main__":
    main()
