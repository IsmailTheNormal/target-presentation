#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_5_6_w11_l28.py — Builder for 5–6th Grade, Week 11, Lesson 28

Mavzu: Scratch Katta Yakuni: O'z Kiber-O'yiningni Yarat! (Mini Game Jam va Loyiha Sintezi)
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 5-6-sinf (Junior Creators Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "5-6-sinf", "11-hafta", "28-dars-scratch-katta-yakuniy-loyiha")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "playground"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides for 80-min Double Block)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="5–6-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 28" data-en="GRADE 5–6 · WEEK 11 · LESSON 28">5–6-SINF · 11-HAFTA · 28-DARS</span></div>
    <h1 class="display" data-ru="Финал Модуля Scratch: Создай Свою Кибер-Игру! (Mini Game Jam)" data-en="Scratch Grand Finale: Build Your Cyber Game! (Mini Game Jam)">Scratch Katta Yakuni: O'z Kiber-O'yiningni Yarat!</h1>
    <p class="lede" data-ru="Финальный проект модуля Scratch: объединяем спрайты, костюмы, циклы «всегда», клавиатурное управление и сбор кристаллов в одну готовую играбельную аркаду." data-en="Scratch module capstone: bringing together sprites, costumes, 'forever' loops, keyboard controls, and crystal collecting into one finished playable arcade game.">Scratch modulining katta yakuni: spraytlar, harakat koordinatalari, qadam animatsiyasi, cheksiz sikllar va to'qnashuvlarni bitta to'liq o'yinga jamlaymiz!</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Синтез Знаний" data-en="Skills Synthesis">Bilimlar Sintezi</h3>
        <p data-ru="Координаты X/Y, анимация шага костюмами, бесконечные циклы движения и детекция касаний." data-en="X/Y coordinates, costume walk cycles, endless motion loops, and collision sensing.">X/Y koordinatalar, kostyumlarni almashtirish, uzluksiz harakat sikllari va to'qnashuvni sezish.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Game Jam Loyihasi</div>
        <h3 data-ru="Собственная Игра" data-en="Playable Arcade">Tayyor Kiber-O'yin</h3>
        <p data-ru="Каждый ученик создаст и защитит перед классом готовую игру с очками, препятствиями и условием победы." data-en="Each student builds and showcases a finished game featuring scoring, moving obstacles, and victory conditions.">Har bir o'quvchi to'siqlar, yig'iladigan tangalar va g'alaba shartiga ega shaxsiy o'yinini yaratadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 27-УРОКА" data-en="LESSON 27 HOMEWORK REVIEW">27-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Бесконечные Циклы: Ловушка Вращения и Зависаний" data-en="Endless Loops: Rotation & Freeze Traps">Cheksiz Sikllar: Teskari Qulash va Qotish Tuzog'i</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Типичная ошибка" data-en="Common Mistake">Keng Tarqalgan Xato</div>
        <h4 data-ru="1. Вращение вверх ногами и бешеный полет" data-en="1. Upside-down flipping & crazy spinning">1. Boshi bilan qulash va o'ta tez uchish</h4>
        <p style="font-size:12px;" data-ru="Блок «если касается края, оттолкнуться» без настройки стиля вращения переворачивает персонажа вверх ногами. А цикл без задержки «ждать 0.05 сек» грузит процессор на 60 FPS." data-en="The 'if on edge, bounce' block flips sprites upside down without rotation style controls. A loop lacking a 'wait 0.05s' delay spins at maximum speed and stutters.">Aylanish uslubi berilmaganda qahramon devorga urilib teskari aylanadi. Sikl ichida <code>0.05 soniya kut</code> bo'lmasa, sprayt ko'z ilg'amas tezlikda aylanib ketadi.</p>
      </div>
      <div class="box" style="border:1px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой стандарт" data-en="Golden Standard">Oltin Standart Yechim</div>
        <h4 data-ru="Стиль вращения + пауза 0.05 сек" data-en="Rotation style + 0.05s pause">To'g'ri Aylanish + 0.05s Sekinlashuv</h4>
        <pre style="margin:0; font-size:11px; background:var(--surface-2); padding:6px; border-radius:4px;"><code class="language-scratch">boshlanganda:
  aylanish uslubi [chap-o'ng] ga o'rnatilsin
  doimiy takrorlash:
    5 qadam oldinga
    agar chekkaga yetsa, qaytish
    0.05 soniya kut</code></pre>
      </div>
    </div>
    <div class="box" style="margin-top:12px; background:var(--surface-2);">
      <div style="font-size:12px; font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="⚡ Блиц-Вопрос и Мост к Теме:" data-en="⚡ Blitz Question & Lesson Bridge:">⚡ Blitz Savol va Bugungi Mavzuga Ko'prik:</div>
      <p style="font-size:12px; margin:0;" data-ru="<strong>Вопрос:</strong> Какой блок нужен, чтобы персонаж не переворачивался вверх ногами при отскоке? <em>(Ответ: «стиль вращения влево-вправо»)</em>.<br><strong>Мост:</strong> Сегодня мы соединим этот бесконечный цикл движения врага с управлением героем и создадим полноценную игру!" data-en="<strong>Question:</strong> Which block prevents a sprite from flipping upside down when bouncing off the stage edge? <em>(Answer: 'set rotation style [left-right]')</em>.<br><strong>Bridge:</strong> Today we will bind these autonomous obstacle loops with active player controls to build a complete game!"><strong>Savol:</strong> Qahramon devorga urilganda boshi pastga qulab qolmasligi uchun qaysi blok kerak? <em>(Javob: «aylanish uslubini [chap-o'ng] ga o'rnatish»)</em>.<br><strong>Ko'prik:</strong> Bugun biz dushmanning ana shu cheksiz harakatini qahramonimiz va yig'iladigan tangalar bilan birlashtirib, birinchi to'liq arkada o'yinimizni quramiz!</p>
    </div>
  </section>

  <!-- SLIDE 3: GAME BLUEPRINT -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="АРХИТЕКТУРА ИГРЫ" data-en="GAME ARCHITECTURE">O'YINNING 4 ASOSIY USTUNI</span></div>
    <h2 data-ru="Из Чего Состоит Любая Игра в Scratch?" data-en="What Makes Up Every Scratch Game?">Har Qanday O'yin Nimadan Tashkil Topadi?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="В реальной разработке игра — это не один случайный блок, а согласованная работа 4 независимых систем." data-en="In real development, a game is not random blocks, but the harmony of 4 distinct systems.">O'yin tasodifiy bloklar to'plami emas. U 4 ta mustaqil tizimning o'zaro do'stona hamkorligidir.</p>
        <ul class="clean-list">
          <li data-ru="<strong>1. Главный Герой (Player):</strong> Управляется стрелками или WASD, меняет костюмы при беге." data-en="<strong>1. Player Sprite:</strong> Controlled via keyboard arrows, animates footsteps via costumes."><strong>1. Bosh Qahramon (Player):</strong> Strelkalar orqali boshqariladi, yugurish animatsiyasiga ega.</li>
          <li data-ru="<strong>2. Автономное Препятствие (Obstacle):</strong> Летает или падает бесконечно по циклу <code>всегда</code>." data-en="<strong>2. Autonomous Obstacle:</strong> Flies or drops continuously inside a <code>forever</code> loop."><strong>2. Avtonom To'siq (Dushman):</strong> <code>doimiy takrorlash</code> siklida to'xtovsiz uchib yuradi.</li>
          <li data-ru="<strong>3. Награда (Collectible Star):</strong> Появляется в случайном месте, дает очки при касании." data-en="<strong>3. Collectible Star:</strong> Appears randomly, awards points when collected."><strong>3. Kiber-Tanga / Yulduz:</strong> Tasodifiy koordinatada paydo bo'ladi, tekkanda ball beradi.</li>
          <li data-ru="<strong>4. Правила Игры (Win / Lose):</strong> 3 жизни закончились — Проигрыш, 5 очков — Победа!" data-en="<strong>4. Game Rules (Win / Lose):</strong> 3 lives lost = Game Over, 5 points earned = Victory!"><strong>4. O'yin Qoidalari:</strong> Jonlar tugasa — Mag'lubiyat, 5 ta tanga yig'ilsa — G'alaba!</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); display:flex; flex-direction:column; justify-content:center; align-items:center; gap:8px;">
        <div style="font-size:36px;">🐱 ➔ ⚡ ➔ ⭐ ➔ 🏆</div>
        <div style="font-weight:700; color:var(--accent); font-size:13px;" data-ru="Схема Взаимодействия" data-en="Interaction Pipeline">O'zaro Aloqa Sxemasi</div>
        <div style="font-size:11px; color:var(--ink-2); text-align:center; line-height:1.5;" data-ru="Герой избегает Препятствия ➔ Собирает Звезду ➔ Получает Очки ➔ Достигает Финала!" data-en="Hero dodges Obstacle ➔ Collects Star ➔ Earns Points ➔ Triggers Victory!">Qahramon To'siqdan Qochadi ➔ Tangani Olib Ball Yig'adi ➔ G'alaba Qozonadi!</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: PLAYER CONTROLLER -->
  <section class="slide" data-phase="Qahramon Boshqaruvi|Управление Героем|Player Controls" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="УПРАВЛЕНИЕ ГЕРОЕМ" data-en="PLAYER CONTROLS">QAHRAMON MANTIG'I</span></div>
    <h2 data-ru="Стрелки Клавиатуры и Анимация Шага" data-en="Keyboard Controls & Walk Cycle Animation">Klaviaturadagi Strelkalar va Qadam Animatsiyasi</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Чтобы кот двигался отзывчиво, мы используем событие нажатия клавиш и смену костюма для эффекта живого бега." data-en="For responsive controls, we link key press events to coordinate shifts and costume changes.">Qahramon tirik ko'rinishi uchun tugma bosilganda nafaqat koordinata, balki uning kostyumi ham o'zgarishi shart!</p>
        <ul class="clean-list">
          <li data-ru="<strong>Вправо:</strong> изменить X на 10, повернуть в направлении 90, следующий костюм." data-en="<strong>Right:</strong> change X by 10, point in direction 90, next costume."><strong>O'ngga:</strong> X ni 10 ga oshirish, 90 burchakka burilish, keyingi kostyum.</li>
          <li data-ru="<strong>Влево:</strong> изменить X на -10, повернуть в направлении -90, следующий костюм." data-en="<strong>Left:</strong> change X by -10, point in direction -90, next costume."><strong>Chapga:</strong> X ni -10 ga kamaytirish, -90 burchakka burilish, keyingi kostyum.</li>
          <li data-ru="<strong>Старт игры:</strong> перейти в X: 0, Y: -120 (нижний центр сцены)." data-en="<strong>Game Start:</strong> go to X: 0, Y: -120 (bottom center)."><strong>Boshlang'ich Nuqta:</strong> har doim X: 0, Y: -120 (sahna pastki markazi).</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:12px; line-height:1.6;">
        <div style="color:var(--accent); font-weight:700; margin-bottom:6px;">[Qahramon Boshqaruv Skripti]</div>
        <pre><code class="language-scratch">qachonki [o'ngga strelka] bosilganda:
  yo'nalishni (90) ga qaratish
  x koordinatani (10) ga o'zgartirish
  keyingi kostyum

qachonki [chapga strelka] bosilganda:
  yo'nalishni (-90) ga qaratish
  x koordinatani (-10) ga o'zgartirish
  keyingi kostyum</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: AUTONOMOUS OBSTACLE -->
  <section class="slide" data-phase="Avtonom To'siq|Автономный Враг|Autonomous Obstacle" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="АВТОНОМНОЕ ПРЕПЯТСТВИЕ" data-en="AUTONOMOUS OBSTACLE">DUSHMAN SIKLI</span></div>
    <h2 data-ru="Падающий Метеорит: Цикл «Всегда» и Случайные Координаты" data-en="Falling Meteor: Forever Loop & Random Spawns">Tushuvchi Meteorit: Cheksiz Sikl va Tasodifiy Nuqta</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Препятствие должно жить своей жизнью! Сверху вниз летит метеорит. Достигнув дна сцены, он снова телепортируется наверх." data-en="Obstacles must move independently! A meteor drops down continuously, teleporting back to the top when reaching the floor.">Dushman kompyuter yordamida o'z hayotini yashaydi: u tepadan pastga tushadi va polga yetganda yana tepaga sakraydi.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Падение:</strong> <code>изменить Y на -7</code> в бесконечном цикле." data-en="<strong>Dropping:</strong> <code>change Y by -7</code> inside a forever loop."><strong>Pastga tushish:</strong> cheksiz siklda <code>y ni -7 ga o'zgartirish</code>.</li>
          <li data-ru="<strong>Случайная позиция:</strong> <code>выдать случайное от -200 до 200</code> для координаты X." data-en="<strong>Random spawn:</strong> <code>pick random -200 to 200</code> for the X axis."><strong>Tasodifiy joy:</strong> X o'qi bo'yicha <code>tasodifiy son -200 dan 200 gacha</code>.</li>
          <li data-ru="<strong>Сброс высоты:</strong> когда Y < -160, переносим обратно на Y: 160." data-en="<strong>Height reset:</strong> when Y < -160, teleport back up to Y: 160."><strong>Qayta tug'ilish:</strong> Y < -160 bo'lsa, uni yana tepaga Y: 160 ga ko'chiramiz.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:12px; line-height:1.6;">
        <div style="color:var(--red); font-weight:700; margin-bottom:6px;">[Meteorit Harakat Skripti]</div>
        <pre><code class="language-scratch">yashil bayroqcha bosilganda:
  doimiy takrorlash:
    y koordinatani (-7) ga o'zgartirish
    agar (y holati < -160) bo'lsa:
      x: (tasodifiy -200 dan 200 gacha) y: (160) ga bor
    0.03 soniya kut</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: SENSING & COLLISION -->
  <section class="slide" data-phase="To'qnashuv Sezgirligi|Детекция Касаний|Sensing & Collisions" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ДЕТЕКЦИЯ КАСАНИЙ" data-en="COLLISION SENSING">SEZGIRLIK VA TO'QNASHUV</span></div>
    <h2 data-ru="Что Происходит При Столкновении? (Касается Игрока?)" data-en="What Happens on Impact? (Touching Player?)">To'qnashuv Yuz Berganda Nima Bo'ladi?</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">Sensor / Sezish</div>
        <h4 data-ru="Касается Игрока?" data-en="Touching Player?">Qahramonga Tegdimi?</h4>
        <p style="font-size:12px;" data-ru="Блок из категории «Сенсоры» мгновенно проверяет, пересекаются ли пиксели спрайтов." data-en="Sensing block detects whether sprite boundaries overlap on the screen.">Sezgirlik bloki qahramon va to'siq piksellari bir-biriga tegdimi yo'qmi tekshiradi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);">Reaksiya / Ziyon</div>
        <h4 data-ru="Потеря Жизни (HP)" data-en="Life Loss (HP)">Jon Kamayishi</h4>
        <p style="font-size:12px;" data-ru="Воспроизводится звук удара «Boing», и количество жизней уменьшается на 1." data-en="A hit sound plays and the player loses 1 life point.">Zarba ovozi ("Boing") yangraydi va qahramon joni 1 taga kamayadi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">Xavfsizlik / Reset</div>
        <h4 data-ru="Телепорт в Безопасность" data-en="Safety Teleport">Boshiga Qaytarish</h4>
        <p style="font-size:12px;" data-ru="Метеорит мгновенно улетает наверх, чтобы не наносить урон повторно." data-en="Meteor instantly teleports back to top to avoid continuous damage.">To'siq yana zudlik bilan tepaga uchib ketadi, qahramon qotib qolmaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: COLLECTIBLES & WIN -->
  <section class="slide" data-phase="Tangalar va G'alaba|Сбор Очков и Победа|Collectibles & Win" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ОЧКИ И ПОБЕДА" data-en="SCORING & VICTORY">XAZINALAR VA G'ALABA</span></div>
    <h2 data-ru="Сбор Звезд: Увеличение Счета и Финал Игры" data-en="Star Collection: Scoring & Game Completion">Yulduz Yig'ish: Ballar va Buyuk G'alaba</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Какой смысл играть, если нет цели? Добавим золотую звезду, которая дает очки и завершает игру при победе!" data-en="Every great game needs a goal! Add a golden star that awards points and triggers celebration.">O'yin maqsadsiz bo'lmaydi! Kiber-Yulduzcha qahramonga ball to'plash va g'alaba qozonish zavqini beradi.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Сбор Звезды:</strong> если касается кота, звук «Coin» и <code>изменить Счет на 1</code>." data-en="<strong>Star Pickup:</strong> if touching cat, play 'Coin' audio and <code>change Score by 1</code>."><strong>Yulduzni olish:</strong> mushuk tekkanda "Coin" ovozi va <code>Ballni 1 ga oshirish</code>.</li>
          <li data-ru="<strong>Новая позиция:</strong> звезда сразу перескакивает в случайную точку экрана." data-en="<strong>Random jump:</strong> star immediately jumps to a new random stage position."><strong>Yangi nuqta:</strong> yulduz darhol yangi tasodifiy joyga sakrab o'tadi.</li>
          <li data-ru="<strong>Условие Победы:</strong> если Счет = 5, сказать «Победа!» и <code>стоп все</code>." data-en="<strong>Victory Condition:</strong> if Score reaches 5, speak 'Victory!' and <code>stop all</code>."><strong>G'alaba:</strong> agar Ball 5 ga yetsa, qahramon "G'alaba!" deb baqiradi va <code>hammasini to'xtatish</code>.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:12px; line-height:1.6;">
        <div style="color:var(--green); font-weight:700; margin-bottom:6px;">[Yulduzcha va G'alaba Skripti]</div>
        <pre><code class="language-scratch">doimiy takrorlash:
  agar (mushukka tegdimi?) bo'lsa:
    ovoz [Coin] ni chal
    ballni (1) ga oshir
    tasodifiy pozitsiyaga bor
    agar (ball = 5) bo'lsa:
      [Buyuk G'alaba! 🎉] deb (2) soniya ayt
      hammasini to'xtatish</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: IN-DECK INTERACTIVE SIMULATOR -->
  <section class="slide" data-phase="Smartboard Simulyatori|Интерактив на Доске|In-Deck Simulator" data-time="40:00–48:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="СИМУЛЯТОР НА СМАРТБОРДЕ" data-en="SMARTBOARD ARCADE">JONLI O'YIN MAYDONI</span></div>
    <h2 data-ru="Тестируем Готовую Игру Прямо на Доске!" data-en="Playtest the Complete Game Right on the Smartboard!">Tayyor O'yinni Taqdimotning O'zida Sinab Ko'ring!</h2>
    <div style="display:grid; grid-template-columns: 1fr 280px; gap:14px; align-items:start;">
      <div style="background:#020617; border-radius:8px; border:2px solid var(--accent); position:relative; overflow:hidden; height:240px;" id="deckGameContainer">
        <!-- Canvas/Game Stage -->
        <canvas id="deckGameCanvas" width="460" height="240" style="display:block; width:100%; height:100%;"></canvas>
        <div id="deckGameOverlay" style="position:absolute; inset:0; background:rgba(0,0,0,0.75); display:flex; flex-direction:column; justify-content:center; align-items:center; color:#fff; text-align:center;">
          <h3 style="margin:0 0 8px; color:var(--accent);" data-ru="🎮 Scratch Mini Game Jam" data-en="🎮 Scratch Mini Game Jam">🎮 Scratch Mini Game Jam</h3>
          <p style="font-size:12px; max-width:280px; margin:0 0 12px; color:#cbd5e1;" data-ru="Управляйте Котом стрелками. Избегайте метеоритов и соберите 5 звезд!" data-en="Control the Cat with arrows. Dodge meteors and collect 5 Stars!">Strelkalar orqali Mushukni boshqaring. Meteoritlardan qoching va 5 ta Yulduz yig'ing!</p>
          <button class="btn" onclick="startDeckGame()" style="background:var(--green); color:#fff; font-weight:700;" data-ru="▶️ Начать Игру" data-en="▶️ Start Game">▶️ O'yinni Boshlash</button>
        </div>
      </div>
      <div class="box" style="display:flex; flex-direction:column; gap:8px;">
        <div style="display:flex; justify-content:space-between; font-weight:700; font-size:13px;">
          <span>⭐ Ball: <strong id="deckScore" style="color:var(--accent);">0 / 5</strong></span>
          <span>❤️ Jon: <strong id="deckLives" style="color:var(--red);">3</strong></span>
        </div>
        <div style="font-size:11px; color:var(--ink-2); line-height:1.4;">
          <strong>Boshqaruv:</strong> Klaviaturadagi ⬅️ ➡️ ⬆️ ⬇️ strelkalari yoki sensorli doskada quyidagi tugmalar:
        </div>
        <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:4px; max-width:160px; margin:0 auto;">
          <div></div>
          <button class="btn" onclick="moveDeckCat(0, -20)" style="padding:6px;">⬆️</button>
          <div></div>
          <button class="btn" onclick="moveDeckCat(-20, 0)" style="padding:6px;">⬅️</button>
          <button class="btn" onclick="moveDeckCat(0, 20)" style="padding:6px;">⬇️</button>
          <button class="btn" onclick="moveDeckCat(20, 0)" style="padding:6px;">➡️</button>
        </div>
        <button class="btn" onclick="resetDeckGame()" style="font-size:11px; background:var(--surface-2); border:1px solid var(--hair);" data-ru="🔄 Перезапуск" data-en="🔄 Reset">🔄 Qayta Boshlash</button>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: INTERACTIVE QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Quiz" data-time="48:00–55:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА ЗНАНИЙ" data-en="KNOWLEDGE CHECK">KIBER-VIKTORINA</span></div>
    <h2 data-ru="3 Вопроса по Механике Scratch Game Jam" data-en="3 Questions on Scratch Game Mechanics">O'yin Mexanikasi Bo'yicha 3 Ta Tezkor Savol</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:var(--accent); color:#fff;">1-Savol</div>
        <p style="font-size:12px; margin-bottom:10px;" data-ru="Какой блок заставляет препятствие двигаться непрерывно, без остановки?" data-en="Which block keeps the obstacle moving indefinitely without stopping?">Dushman to'xtovsiz harakatlanishi uchun qaysi blok kerak?</p>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! Doimiy takrorlash (forever) to‘xtovsiz aylantiradi.')" style="font-size:11px;" data-ru="A) Повторять всегда" data-en="A) Forever">A) doimiy takrorlash</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri. 10 marta takrorlash amalni bajarib to‘xtab qoladi.')" style="font-size:11px;" data-ru="B) Повторить 10 раз" data-en="B) Repeat 10">B) 10 marta takrorlash</button>
        </div>
      </div>
      <div class="box">
        <div class="tag" style="background:var(--purple); color:#fff;">2-Savol</div>
        <p style="font-size:12px; margin-bottom:10px;" data-ru="Какой блок определяет момент сбора монеты или удара об препятствие?" data-en="Which block detects when a player picks up a star or hits an obstacle?">Qahramon tangaga tegganini qaysi blok tekshiradi?</p>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! «Касается [Спрайта]?» bloki to‘qnashuvni sezadi.')" style="font-size:11px;" data-ru="A) Касается [Спрайта]?" data-en="A) Touching [Sprite]?">A) [Mushukcha] ga tegdimi?</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri. Rang almashtirish bu tashqi ko‘rinish bloki.')" style="font-size:11px;" data-ru="B) Следующий костюм" data-en="B) Next costume">B) keyingi kostyum</button>
        </div>
      </div>
      <div class="box">
        <div class="tag" style="background:var(--green); color:#fff;">3-Savol</div>
        <p style="font-size:12px; margin-bottom:10px;" data-ru="Какой блок мгновенно останавливает всю игру при победе или проигрыше?" data-en="Which block immediately halts the entire game upon victory or defeat?">G'alaba yoki mag'lubiyatda o'yinni to'xtatuvchi blok qaysi?</p>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! «Стоп все» o‘yindagi barcha harakatlarni muzlatadi.')" style="font-size:11px;" data-ru="A) Стоп [все]" data-en="A) Stop [all]">A) hammasini to'xtatish</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri. Bayroqcha o‘yinni to‘xtatmaydi, qayta boshlaydi.')" style="font-size:11px;" data-ru="B) Когда нажат флаг" data-en="B) When flag clicked">B) bayroqcha bosilganda</button>
        </div>
      </div>
    </div>
    <div id="quizFeedback" style="margin-top:10px; font-weight:700; font-size:12px; min-height:18px;"></div>
  </section>

  <!-- SLIDE 10: 25-MIN ARENA -->
  <section class="slide" data-phase="Amaliy Arena|Практическая Арена|Hands-on Arena" data-time="55:00–70:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКАЯ АРЕНА (25 МИНУТ)" data-en="HANDS-ON ARENA (25 MIN)">AMALIY ARENA (25 DAQIQA)</span></div>
    <h2 data-ru="Scratch Game Jam: Создай Свою Кибер-Игру!" data-en="Scratch Game Jam: Build Your Playable Cyber Game!">Scratch Game Jam: O'z Kiber-O'yiningni Noldan Yarat!</h2>
    <div class="grid-2">
      <div>
        <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
          <button class="btn" id="arenaTimerBtn" onclick="toggleArenaTimer()" style="background:var(--accent); color:#fff; font-weight:700;" data-ru="⏱️ Запустить Таймер" data-en="⏱️ Start Timer">⏱️ Taymerni Boshlash</button>
          <span id="arenaTimerDisplay" style="font-family:var(--font-mono); font-size:24px; font-weight:700; color:var(--red);">25:00</span>
        </div>
        <p class="lede" style="font-size:13px; margin-bottom:8px;" data-ru="Откройте Scratch 3.0 или нашу встроенную студию и реализуйте 3 обязательных этапа:" data-en="Open Scratch 3.0 or our playground and complete the 3 core game milestones:">Scratch 3.0 dasturini oching va 3 ta asosiy bosqichni amalga oshiring:</p>
        <ul class="clean-list" style="font-size:12px;">
          <li data-ru="<strong>1-й Шаг (5 мин):</strong> Выберите героя и фон. Настройте движение стрелками с анимацией костюмов." data-en="<strong>Step 1 (5 min):</strong> Choose hero and backdrop. Setup arrow controls with costume animations."><strong>1-Qadam (5 min):</strong> Qahramon va fon tanlang. Strelkalar bilan harakat va kostyum almashtirishni ulang.</li>
          <li data-ru="<strong>2-й Шаг (10 мин):</strong> Добавьте препятствие. Запустите цикл «всегда» с падением и случайным спавном." data-en="<strong>Step 2 (10 min):</strong> Add falling obstacle. Program a forever loop with random spawn coordinates."><strong>2-Qadam (10 min):</strong> To'siq qo'shing. <code>doimiy takrorlash</code> sikli va tasodifiy koordinatalar bering.</li>
          <li data-ru="<strong>3-й Шаг (10 мин):</strong> Добавьте сбор монет со звуком, подсчет очков и победу при 5 очках!" data-en="<strong>Step 3 (10 min):</strong> Implement star pickup with audio, score counter, and 5-point victory screen!"><strong>3-Qadam (10 min):</strong> Ovozli tanga yig'ish, ballar hisobi va 5 ball to'plaganda g'alaba ekranini qo'ying!</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="font-weight:700; color:var(--accent); margin-bottom:6px;" data-ru="Критерии 10 Баллов:" data-en="10 Points Rubric:">10 Ballik Mezon:</div>
          <div style="font-size:11px; line-height:1.6;">
            <div>✅ <strong>4 Ball:</strong> Qahramon erkin yuradi va kostyumlari almashadi.</div>
            <div>✅ <strong>4 Ball:</strong> To'siq cheksiz harakatlanadi va tekkanda jon kamayadi.</div>
            <div>✅ <strong>2 Ball:</strong> Tanga yig'ish, tovush effektlari va g'alaba ekrani ishlaydi!</div>
          </div>
        </div>
        <div style="margin-top:10px; text-align:right;">
          <a href="playground/index.html" target="_blank" class="btn" style="background:var(--purple); color:#fff; font-size:11px;" data-ru="Открыть Студию Scratch" data-en="Launch Scratch Studio">Katta Studiyani Ochish ➔</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: PEER REVIEW -->
  <section class="slide" data-phase="Partadosh Auditi|Взаимный Аудит|Peer Review" data-time="70:00–74:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМНОЕ ТЕСТИРОВАНИЕ" data-en="PEER CODE AUDIT">PARTADOSH AUDITI</span></div>
    <h2 data-ru="Поменяйтесь Местами: Протестируйте Игру Друга!" data-en="Swap Desks: Playtest Your Classmate's Game!">O'rin Almashib Sinfdosh O'yinini Tekshiramiz!</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Настоящие гейм-дизайнеры всегда тестируют игры друг друга. Проверьте проект по 4 пунктам:" data-en="Real game designers always playtest each other's games. Audit the project using 4 criteria:">Haqiqiy geym-dizaynerlar o'yinni do'stlariga o'ynatib ko'radilar. 4 ta mezon bo'yicha baholang:</p>
        <ul class="clean-list">
          <li data-ru="<strong>1. Отзывчивость:</strong> Двигается ли персонаж при нажатии стрелок без лагов?" data-en="<strong>1. Responsiveness:</strong> Does the hero move smoothly on arrow presses without lagging?"><strong>1. Harakat:</strong> Strelkalar bosilganda qahramon ravon yuryaptimi?</li>
          <li data-ru="<strong>2. Автономность:</strong> Летит ли препятствие бесконечно само по себе?" data-en="<strong>2. Autonomy:</strong> Does the obstacle drop continuously inside its forever loop?"><strong>2. Avtonomiya:</strong> To'siq cheksiz siklda o'zi mustaqil harakatlanyaptimi?</li>
          <li data-ru="<strong>3. Касания:</strong> Работает ли детекция столкновения и сбор звезд?" data-en="<strong>3. Sensing:</strong> Do collisions register and award points or reduce lives?"><strong>3. To'qnashuv:</strong> Tangalar olinib, to'siqqa tekkanda reaksiya bormi?</li>
          <li data-ru="<strong>4. Финал:</strong> Срабатывает ли блок «стоп все» при победе или поражении?" data-en="<strong>4. Completion:</strong> Does the game halt properly with 'stop all' on game over?"><strong>4. Yakun:</strong> G'alaba yoki mag'lubiyatda o'yin to'g'ri to'xtayaptimi?</li>
        </ul>
      </div>
      <div class="box" style="border:1px dashed var(--accent); background:rgba(59,130,246,0.05); display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
        <div style="font-size:40px; margin-bottom:8px;">🤝 🎮 ⭐️</div>
        <h4 data-ru="Культура Взаимопомощи" data-en="Constructive Feedback">Do'stona Yordam</h4>
        <p style="font-size:12px; color:var(--ink-2); max-width:240px; margin:0;" data-ru="Если нашли баг — помогите другу исправить блок! Настоящие программисты работают в команде." data-en="If you spot a bug, help your friend fix the block! Real programmers succeed together.">Agar xato topsangiz, kulmasdan qaysi blokni to'g'rilash kerakligini ko'rsating. Dasturchilar jamoa bo'lib o'sadilar!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: SHOWCASE -->
  <section class="slide" data-phase="Katta Ekran|Шоукейс|Showcase" data-time="74:00–77:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ПРЕЗЕНТАЦИЯ НА ДОСКЕ" data-en="SMARTBOARD SHOWCASE">KATTA EKRAN SHOWCASI</span></div>
    <h2 data-ru="Шоукейс: Играем в Лучшие Игры Класса на Доске!" data-en="Showcase: Play the Best Student Games on the Big Board!">Katta Doskada Eng Yaxshi O'yinlarni O'ynaymiz!</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid var(--accent);">
        <h4 data-ru="1. Космический Рейнджер" data-en="1. Cosmic Ranger">1. Kosmik Sarguzasht</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Лазерные вспышки, метеоритный дождь и сбор светящихся кристаллов." data-en="Laser effects, meteor storm, and glowing space crystal collection.">Meteoritlar yomg'iri va kosmik kristallarni chaqqonlik bilan yig'ish.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--purple);">
        <h4 data-ru="2. Подводная Одиссея" data-en="2. Ocean Odyssey">2. Suv Osti Odisseyasi</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Акула патрулирует дно океана, а рыбка собирает драгоценные жемчужины." data-en="Shark patrolling the seabed while the fish hunts for precious pearls.">Akuladan qochib, dengiz tubidagi sehrli marvaridlarni terish.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--green);">
        <h4 data-ru="3. Кибер-Ниндзя" data-en="3. Cyber Ninja">3. Kiber-Ninja</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Прыжки через лазерные барьеры и сбор сюрикенов с победным салютом." data-en="Jumping over laser barriers and collecting shurikens with fireworks.">Lazerli to'siqlardan sakrab, 5 ta tanga bilan buyuk g'alabaga erishish.</p>
      </div>
    </div>
    <div class="box" style="margin-top:12px; background:rgba(16,185,129,0.08); border:1px solid var(--green); text-align:center;">
      <span style="font-weight:700; color:var(--green); font-size:13px;" data-ru="🎉 Поздравляем! Каждый ученик успешно создал свою первую игру в Scratch!" data-en="🎉 Congratulations! Every student successfully engineered their first complete Scratch arcade game!">🎉 Tabriklaymiz! Har bir o'quvchi Scratchda o'zining birinchi haqiqiy o'yinini yaratdi!</span>
    </div>
  </section>

  <!-- SLIDE 13: TIERED HOMEWORK -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Homework" data-time="77:00–79:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ДОМАШНЕЕ ЗАДАНИЕ (10 БАЛЛОВ)" data-en="HOMEWORK (10 POINTS)">UY VAZIFASI (10 BALL)</span></div>
    <h2 data-ru="3 Уровня: От Базовой Игры до Двойной Угрозы" data-en="3 Challenge Tiers: From Base Game to Double Threat">3 Darajali Kiber-Vazifa: O'yinni Boyitish</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid var(--accent);">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1-Daraja (Baza)</div>
        <h4 data-ru="Базовая Игра (4 Балла)" data-en="Base Game (4 Points)">Baza O'yini (4 Ball)</h4>
        <p style="font-size:12px;" data-ru="Повторите классный проект: управляемый герой, 1 падающее препятствие и 1 собираемая звезда." data-en="Replicate the in-class game: playable hero, 1 falling obstacle, and 1 collectible star.">Darsdagi o'yinni takrorlang: harakatlanuvchi qahramon, 1 ta tushuvchi to'siq va 1 ta tanga.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--purple);">
        <div class="tag" style="background:rgba(147,51,234,0.15); color:var(--purple);">2-Daraja (Amaliy)</div>
        <h4 data-ru="Звук и Эффекты (4 Балла)" data-en="Audio & FX (4 Points)">Ovoz va Effektlar (4 Ball)</h4>
        <p style="font-size:12px;" data-ru="Добавьте фоновую музыку, звук подбора монеты и смену фона на экране Победы." data-en="Add background music loop, star pickup audio, and victory backdrop switch.">O'yinga orqa fon musiqasi, tanga olinganda maxsus ovoz va g'alaba fonini qo'shing.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">3-Daraja (Challenge)</div>
        <h4 data-ru="Второй Враг (2 Балла)" data-en="Dual Obstacle (2 Points)">Ikkinchi Dushman (2 Ball)</h4>
        <p style="font-size:12px;" data-ru="Добавьте 2-е препятствие с другой скоростью или 30-секундный таймер обратного отсчета!" data-en="Add a 2nd obstacle moving at a different speed or a 30-second countdown timer!">Turli tezlikda tushuvchi 2-to'siqni qo'shing yoki 30 soniyalik teskari hisob taymerini qo'ying!</p>
      </div>
    </div>
    <div style="margin-top:12px; text-align:right;">
      <a href="vazifa.html" class="btn" style="background:var(--purple); color:#fff; font-size:12px;" data-ru="Открыть ДЗ" data-en="Open HW">Vazifalar Ilovasini Ochish ➔</a>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ МОДУЛЯ" data-en="MODULE WRAP-UP">XULOSA VA YANGI BOSQICH</span></div>
    <h2 data-ru="Scratch Освоен! Впереди — Текстовый Код и ИИ" data-en="Scratch Mastered! Ahead: Textual Code & AI">Scratch Zabt Etildi! Oldinda — Matnli Kod va AI</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="За эти недели мы прошли весь путь визуального программирования: от первой точки на сетке координат до комплексной игры с искусственным интеллектом врагов." data-en="Over these weeks we advanced across the entire visual coding journey: from simple coordinates to complex multi-sprite game logic.">Ushbu darslar davomida biz vizual blokli dasturlashning butun asosini egalladik: koordinatalar, kostyumlar animatsiyasi, cheksiz sikllar va to'qnashuvlar!</p>
        <ul class="clean-list">
          <li data-ru="<strong>Координатная сетка:</strong> Понимание X/Y и направления движения." data-en="<strong>Coordinate Grid:</strong> Deep mastery of X/Y spatial positioning."><strong>Koordinatalar:</strong> X/Y o'qlari va burchaklarni erkin boshqarish.</li>
          <li data-ru="<strong>Циклы:</strong> Умение оживлять мир без ручного дублирования команд." data-en="<strong>Loops:</strong> Animating characters tirelessly without code repetition."><strong>Sikllar:</strong> Qahramonlarni to'xtovsiz harakatlantirish mahorati.</li>
          <li data-ru="<strong>Гейм-логика:</strong> Детекция касаний, жизни, счет и условия победы." data-en="<strong>Game Logic:</strong> Collision sensing, lives, score, and victory states."><strong>O'yin Mantig'i:</strong> To'qnashuvlar, ochkolar va g'alaba shartlari.</li>
        </ul>
      </div>
      <div class="box" style="border-left:4px solid var(--purple); background:rgba(147,51,234,0.08);">
        <strong style="color:var(--purple); font-size:14px;" data-ru="Следующий Модуль:" data-en="Next Module:">🚀 Keyingi Bosqich Ko'prigi:</strong>
        <p style="font-size:12px; margin-top:6px; line-height:1.5;" data-ru="<strong>От Блоков к Настоящему Коду:</strong> Переход к текстовому синтаксису и созданию собственных умных AI-ассистентов и веб-приложений!" data-en="<strong>From Blocks to Real Code:</strong> Transitioning towards typed code and building your own intelligent AI apps!"><strong>Bloklardan Haqiqiy Kodga:</strong> Vizual bloklardan keyingi jiddiy qadam — matnli dasturlash asoslari va sun'iy intellekt vositalari bilan ishlash!</p>
      </div>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. IN-DECK INTERACTIVE SIMULATOR SCRIPT (Slide 8)
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
// Slide 8: Interactive In-Deck Game Jam Arcade
var deckGameRunning = false;
var deckCat = { x: 220, y: 190, size: 24, speed: 20 };
var deckMeteor = { x: 200, y: 20, size: 18, speed: 4 };
var deckStar = { x: 100, y: 100, size: 14 };
var deckScore = 0;
var deckLives = 3;
var deckGameTimer = null;

function initDeckCanvas() {
  var canvas = document.getElementById('deckGameCanvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  drawDeckGame(ctx);
}

function startDeckGame() {
  var overlay = document.getElementById('deckGameOverlay');
  if (overlay) overlay.style.display = 'none';
  deckGameRunning = true;
  deckScore = 0;
  deckLives = 3;
  deckCat.x = 220;
  deckCat.y = 190;
  deckMeteor.x = Math.floor(Math.random() * 400) + 30;
  deckMeteor.y = 10;
  spawnDeckStar();
  updateDeckUI();

  if (deckGameTimer) clearInterval(deckGameTimer);
  deckGameTimer = setInterval(updateDeckGameLoop, 35);
}

function resetDeckGame() {
  deckGameRunning = false;
  if (deckGameTimer) clearInterval(deckGameTimer);
  var overlay = document.getElementById('deckGameOverlay');
  if (overlay) overlay.style.display = 'flex';
  deckScore = 0;
  deckLives = 3;
  updateDeckUI();
  initDeckCanvas();
}

function spawnDeckStar() {
  deckStar.x = Math.floor(Math.random() * 380) + 40;
  deckStar.y = Math.floor(Math.random() * 140) + 40;
}

function moveDeckCat(dx, dy) {
  if (!deckGameRunning) return;
  deckCat.x = Math.max(20, Math.min(440, deckCat.x + dx));
  deckCat.y = Math.max(30, Math.min(220, deckCat.y + dy));
  checkDeckCollisions();
}

function updateDeckGameLoop() {
  if (!deckGameRunning) return;
  var canvas = document.getElementById('deckGameCanvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');

  // Obstacle movement (Forever loop in JS)
  deckMeteor.y += deckMeteor.speed;
  if (deckMeteor.y > 230) {
    deckMeteor.y = 10;
    deckMeteor.x = Math.floor(Math.random() * 400) + 30;
  }

  checkDeckCollisions();
  drawDeckGame(ctx);
}

function checkDeckCollisions() {
  // Check Star collection
  var distStar = Math.hypot(deckCat.x - deckStar.x, deckCat.y - deckStar.y);
  if (distStar < deckCat.size + deckStar.size) {
    deckScore++;
    spawnDeckStar();
    updateDeckUI();
    if (deckScore >= 5) {
      endDeckGame(true);
    }
  }

  // Check Meteor hit
  var distMeteor = Math.hypot(deckCat.x - deckMeteor.x, deckCat.y - deckMeteor.y);
  if (distMeteor < deckCat.size + deckMeteor.size - 4) {
    deckLives--;
    deckMeteor.y = 10;
    deckMeteor.x = Math.floor(Math.random() * 400) + 30;
    updateDeckUI();
    if (deckLives <= 0) {
      endDeckGame(false);
    }
  }
}

function updateDeckUI() {
  var sEl = document.getElementById('deckScore');
  var lEl = document.getElementById('deckLives');
  if (sEl) sEl.textContent = deckScore + ' / 5';
  if (lEl) lEl.textContent = deckLives;
}

function endDeckGame(won) {
  deckGameRunning = false;
  if (deckGameTimer) clearInterval(deckGameTimer);
  var overlay = document.getElementById('deckGameOverlay');
  if (!overlay) return;
  overlay.style.display = 'flex';
  if (won) {
    overlay.innerHTML = '<h2 style="color:var(--green); margin:0 0 8px;">🎉 BUYUK G‘ALABA!</h2><p style="font-size:13px; color:#cbd5e1; margin:0 0 12px;">Siz barcha 5 ta kiber-yulduzni to‘pladingiz!</p><button class="btn" onclick="startDeckGame()" style="background:var(--green); color:#fff;">Yana O‘ynash</button>';
  } else {
    overlay.innerHTML = '<h2 style="color:var(--red); margin:0 0 8px;">💥 GAME OVER</h2><p style="font-size:13px; color:#cbd5e1; margin:0 0 12px;">Jonlaringiz tugadi! To‘siqlardan ehtiyot bo‘ling.</p><button class="btn" onclick="startDeckGame()" style="background:var(--accent); color:#fff;">Qayta Urinish</button>';
  }
}

function drawDeckGame(ctx) {
  ctx.fillStyle = '#0f172a';
  ctx.fillRect(0, 0, 460, 240);

  // Background stars
  ctx.fillStyle = 'rgba(255,255,255,0.2)';
  for (var i = 0; i < 20; i++) {
    ctx.fillRect((i * 47) % 460, (i * 31) % 240, 2, 2);
  }

  // Draw Star (Collectible)
  ctx.fillStyle = '#f59e0b';
  ctx.beginPath();
  ctx.arc(deckStar.x, deckStar.y, deckStar.size, 0, Math.PI * 2);
  ctx.fill();
  ctx.font = '14px sans-serif';
  ctx.fillText('⭐', deckStar.x - 7, deckStar.y + 5);

  // Draw Meteor (Obstacle)
  ctx.fillStyle = '#ef4444';
  ctx.beginPath();
  ctx.arc(deckMeteor.x, deckMeteor.y, deckMeteor.size, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillText('☄️', deckMeteor.x - 8, deckMeteor.y + 6);

  // Draw Cat (Player)
  ctx.fillStyle = '#38bdf8';
  ctx.beginPath();
  ctx.arc(deckCat.x, deckCat.y, deckCat.size, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillText('🐱', deckCat.x - 8, deckCat.y + 6);
}

// Arrow key listener for in-deck game
window.addEventListener('keydown', function(e) {
  if (!deckGameRunning) return;
  if (e.key === 'ArrowUp' || e.key === 'w') { moveDeckCat(0, -20); e.preventDefault(); }
  else if (e.key === 'ArrowDown' || e.key === 's') { moveDeckCat(0, 20); e.preventDefault(); }
  else if (e.key === 'ArrowLeft' || e.key === 'a') { moveDeckCat(-20, 0); e.preventDefault(); }
  else if (e.key === 'ArrowRight' || e.key === 'd') { moveDeckCat(20, 0); e.preventDefault(); }
});

setTimeout(initDeckCanvas, 500);

// Slide 10 Arena Countdown Timer
var arenaSeconds = 25 * 60;
var arenaTimerInterval = null;
function toggleArenaTimer() {
  var btn = document.getElementById('arenaTimerBtn');
  var display = document.getElementById('arenaTimerDisplay');
  if (arenaTimerInterval) {
    clearInterval(arenaTimerInterval);
    arenaTimerInterval = null;
    btn.textContent = '▶️ Davom Ettirish';
  } else {
    btn.textContent = '⏸️ To‘xtatish';
    arenaTimerInterval = setInterval(function() {
      if (arenaSeconds > 0) {
        arenaSeconds--;
        var m = Math.floor(arenaSeconds / 60);
        var s = arenaSeconds % 60;
        display.textContent = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
      } else {
        clearInterval(arenaTimerInterval);
        display.textContent = '00:00 - VAQT TUGADI!';
      }
    }, 1000);
  }
}

// Slide 9 Quiz Feedback
function checkQuiz(btn, isCorrect, feedbackText) {
  var fb = document.getElementById('quizFeedback');
  if (isCorrect) {
    btn.style.background = 'var(--green)';
    btn.style.color = '#fff';
    fb.style.color = 'var(--green)';
    fb.textContent = '✅ ' + feedbackText;
  } else {
    btn.style.background = 'var(--red)';
    btn.style.color = '#fff';
    fb.style.color = 'var(--red)';
    fb.textContent = '❌ ' + feedbackText;
  }
}
"""

# Notes array for 14 slides
NOTES_DATA = {
    "uz": [
        ["Kirish va Maqsad", "O'quvchilarga bugungi dars Scratch modulining katta yakuniy loyihasi — Game Jam ekanini e'lon qiling.", "Doskaga o'yinning 4 ta ustunini chizib bering."],
        ["Uy Vazifasi Tahlili", "27-darsdagi cheksiz sikllarda 0.05s kutish unutilishi va qahramon teskari qulashi xatolarini tushuntiring.", "Oltin yechim: chap-o'ng aylanish uslubi va sekinlashuv pauzasi ekanini ko'rsating."],
        ["O'yinning 4 Ustuni", "O'yin tasodifiy emasligini, Player, Obstacle, Collectible va Rules tizimlari birlashuvidan hosil bo'lishini tushuntiring.", "Real geym-dizayn tamoyillarini keltiring."],
        ["Qahramon Boshqaruvi", "Strelkalar bosilganda X/Y koordinatalarni o'zgartirish va keyingi kostyum bloklarini ko'rsating.", "Boshlang'ich nuqtaga o'rnatish muhimligini ayting."],
        ["Dushman Harakati", "Cheksiz sikl ichida Y ni kamaytirib pastga tushirish va tasodifiy X koordinata bilan qayta tug'ilish formulasini tushuntiring.", "pick random blokini eslating."],
        ["To'qnashuv va Sezgirlik", "touching bloki qanday qilib piksellarni tekshirishini va zarba ovozi hamda jon kamayishini ko'rsating.", "To'siq darhol tepaga qaytishi kerakligini ta'kidlang."],
        ["Xazinalar va G'alaba", "Tanga olinganda ball qo'shilishi va 5 ball to'planganda stop all bilan o'yin g'alaba qozonishini tushuntiring.", "O'yinchiga g'alaba zavqini berish zarurligini ayting."],
        ["Smartboard Simulyatori", "Taqdimot ichidagi interaktiv arkadani doskada o'ynab bering.", "Bolalarni doskaga chaqirib, 5 ta ball to'plashni sinab ko'ring."],
        ["Bilimni Sinash (Quiz)", "3 ta viktorina savolini sinf bilan birga yeching.", "Nega forever, touching va stop all bloklari kerakligini so'rang."],
        ["25 Daqiqalik Arena", "O'quvchilarga Scratch 3.0 yoki playground/index.html ni ochishni buyuring.", "Har bir partada 3 bosqichli o'yin qurilishini nazorat qiling."],
        ["Partadosh Auditi", "O'rin almashib, 4 ta mezon bo'yicha partadosh o'yinini o'ynab ko'rishsin.", "Xatolarni samimiy topib, to'g'rilashga yordam berishni rag'batlantiring."],
        ["Katta Ekran Showcasi", "Eng qiziqarli 3 ta o'quvchi loyihasini katta doskaga chiqarib, butun sinf bilan o'ynang.", "Dasturchilarni qarsaklar bilan olqishlang."],
        ["3 Darajali Uy Vazifasi", "10 ballik uy vazifasini tushuntiring.", "2-darajadagi ovoz effektlari va 3-darajadagi ikkinchi to'siqni aytib o'ting."],
        ["Xulosa va Yangi Bosqich", "Scratch modulini rasman muvaffaqiyatli yakunlang.", "Keyingi bosqichda matnli kodlash va AI vositalari sari qadam qo'yilishini e'lon qiling."]
    ],
    "ru": [
        ["Введение и Цель", "Объявите ребятам финал модуля Scratch — большой школьный Mini Game Jam.", "Нарисуйте на доске 4 столпа любой игры: Герой, Враг, Звезда и Правила."],
        ["Разбор Домашнего Задания", "Разберите типичные ошибки 27-урока: вращение вверх ногами и отсутствие задержки 0.05 сек.", "Покажите золотой стандарт с фиксацией стиля вращения [влево-вправо]."],
        ["4 Столпа Игры", "Объясните архитектуру игры: слаженная работа 4 систем (Player, Obstacle, Collectible, Rules).", "Приведите примеры из известных аркадных игр."],
        ["Управление Героем", "Покажите привязку стрелок к координатам X/Y и анимацию шага через смену костюмов.", "Подчеркните обязательность установки начальной позиции X:0 Y:-120."],
        ["Автономный Враг", "Объясните бесконечный цикл падения метеорита с телепортацией наверх через случайный X.", "Напомните блок «выдать случайное от -200 до 200»."],
        ["Детекция Касаний", "Покажите блок «касается [Спрайта]?», проигрывание звука удара и уменьшение жизней.", "Объясните, почему метеорит должен сразу исчезнуть наверх."],
        ["Очки и Победа", "Покажите увеличение счета при сборе звезды и проверку условия победы через «стоп все».", "Подчеркните важность понятного финала игры."],
        ["Интерактив на Доске", "Сыграйте во встроенную в слайд аркаду прямо на смартборде.", "Пригласите 1-2 учеников собрать 5 звезд перед классом."],
        ["Тест (Квиз)", "Проведите веселое тестирование из 3 вопросов.", "Обсудите правильные ответы со всем классом."],
        ["Практическая Арена (25 мин)", "Дайте команду открыть Scratch 3.0 или playground/index.html.", "Курируйте создание игры каждым учеником по 3 этапам."],
        ["Взаимный Аудит", "Организуйте обмен местами за партами по 4 критериям чек-листа.", "Поощряйте взаимовыручку и совместный поиск багов."],
        ["Шоукейс на Доске", "Выведите 3 лучших проекта на смартборд и сыграйте в них всем классом.", "Похвалите авторов аплодисментами."],
        ["Домашнее Задание", "Объясните 3 уровня 10-балльного домашнего задания.", "Обратите внимание на вызов 3-го уровня с добавлением второго врага."],
        ["Итоги Модуля", "Подведите итоги всего модуля визуального программирования Scratch.", "Анонсируйте следующий шаг: переход к текстовому коду и AI-ассистентам!"]
    ],
    "en": [
        ["Intro & Objectives", "Announce the Scratch module capstone: the big class Mini Game Jam.", "Diagram the 4 game pillars on the whiteboard: Player, Obstacle, Star, and Rules."],
        ["Homework Review", "Review common pitfalls from Lesson 27: upside-down flipping and omitting a 0.05s pause.", "Showcase the golden solution with [left-right] rotation style constraints."],
        ["4 Pillars of Game Dev", "Explain game architecture: harmonizing Player, Obstacle, Collectibles, and Victory logic.", "Relate these pillars to iconic arcade video games."],
        ["Player Controller", "Demonstrate mapping arrow keys to X/Y coordinates coupled with costume walk cycles.", "Highlight the necessity of an initial spawn point at X:0 Y:-120."],
        ["Autonomous Obstacle", "Walk through the forever loop dropping the meteor and re-spawning it across random X positions.", "Review the 'pick random -200 to 200' block."],
        ["Collision Sensing", "Explain the 'touching [Player]?' sensor, impact sound triggers, and life deductions.", "Stress why obstacles must immediately reset upwards upon impact."],
        ["Scoring & Victory", "Demonstrate incrementing score upon star collision and triggering victory via 'stop all'.", "Emphasize rewarding players with clear win states."],
        ["Smartboard Arcade", "Play through the embedded in-deck arcade game directly on the Smartboard.", "Invite students up to collect 5 stars in front of the room."],
        ["Knowledge Check (Quiz)", "Lead students through the 3 quick questions.", "Discuss each mechanic collaboratively."],
        ["Hands-on Arena (25 min)", "Instruct students to open Scratch 3.0 or playground/index.html.", "Supervise each student building their game across the 3 milestones."],
        ["Peer Code Audit", "Facilitate seat swapping to playtest classmate games using the 4-point rubric.", "Encourage teamwork and constructive bug hunting."],
        ["Smartboard Showcase", "Project the 3 top games onto the main Smartboard and play them together.", "Celebrate student achievements with rounds of applause."],
        ["Tiered Homework", "Explain the 3-tiered 10-point homework assignment.", "Highlight Tier 3's dual obstacle challenge."],
        ["Module Finale", "Celebrate the official completion of the Scratch visual coding module.", "Preview the upcoming transition into typed coding and AI builders!"]
    ]
}

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "28-dars: Scratch Katta Yakuni: O'z Kiber-O'yiningni Yarat!"
    title_ru = "Урок 28: Финал Модуля Scratch: Создай Свою Кибер-Игру!"
    title_en = "Lesson 28: Scratch Grand Finale: Build Your Cyber Game!"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="5–6 КЛАСС" data-en="GRADE 5–6">5–6-SINF</span>',
                 tpl)

    titles_json = json.dumps({"uz": title_uz, "ru": title_ru, "en": title_en}, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    stage_regex = r'<div class="stage">[\s\S]*?</div><!-- /stage -->'
    new_stage = f'<div class="stage">\n{SLIDES_HTML}\n  </div><!-- /stage -->'
    tpl = re.sub(stage_regex, new_stage, tpl)

    # Inject simulator script into presentation
    custom_script = f"<script>\n{SIMULATOR_JS}\n</script>\n</body>"
    tpl = tpl.replace("</body>", custom_script)

    out_path = os.path.join(DEST_DIR, "prezentatsiya.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

def build_worksheet():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "28-dars: Scratch Katta Yakuni: O'z Kiber-O'yiningni Yarat!"
    title_ru = "Урок 28: Финал Модуля Scratch: Создай Свою Кибер-Игру!"
    title_en = "Lesson 28: Scratch Grand Finale: Build Your Cyber Game!"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<h1>.*?</h1>',
                 f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>',
                 tpl)

    sec1_html = """
    <p class="lead" style="font-size:12px; margin-bottom:8px;" data-ru="<strong>Миссия Урока:</strong> Объединить все знания визуального программирования (спрайты, костюмы, циклы «всегда», клавиатурное управление и сбор кристаллов) в готовую играбельную аркаду!" data-en="<strong>Lesson Mission:</strong> Bring together all visual coding fundamentals (sprites, costumes, forever loops, keyboard controls, and collision sensing) into a finished playable arcade game!"><strong>Dars Missiyasi:</strong> Scratchda o'rgangan barcha bilimlarimizni (spraytlar, animatsiya, cheksiz sikllar, klaviatura boshqaruvi va to'qnashuvlar) yagona to'liq kiber-arkadaga jamlash!</p>
    <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="4 Столпа Моей Игры:" data-en="4 Pillars of My Game:">O'yinimning 4 Asosiy Ustuni:</div>
      <div>1. <strong>Qahramon (Player):</strong> <span data-ru="Управляется стрелками, меняет костюмы при беге" data-en="Controlled via arrows, changes costumes when running">Strelkalar bilan harakatlanadi, kostyumlari almashadi</span>.</div>
      <div>2. <strong>To'siq (Obstacle):</strong> <span data-ru="Падает сверху вниз в бесконечном цикле «всегда»" data-en="Falls from top to bottom inside a forever loop">Cheksiz <code>doimiy takrorlash</code> siklida tepadan tushadi</span>.</div>
      <div>3. <strong>Tanga (Star):</strong> <span data-ru="Появляется случайно, дает очки при касании" data-en="Appears randomly, grants points upon contact">Tasodifiy nuqtada paydo bo'ladi, tekkanda ball beradi</span>.</div>
      <div>4. <strong>G'alaba Qoidasi:</strong> <span data-ru="3 жизни закончились — Game Over, 5 очков — Победа!" data-en="3 lives lost = Game Over, 5 points = Victory!">3 ta jon ketsa — Game Over, 5 ta ball to'plansa — G'alaba!</span></div>
    </div>
    """

    sec2_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="Ниже приведен алгоритм автономного падения метеорита с телепортацией:" data-en="Below is the autonomous falling obstacle algorithm with random teleportation:">Quyida to'siqning cheksiz tushishi va tasodifiy koordinatada qayta tug'ilish algoritmi keltirilgan:</p>
    <pre style="background:var(--surface-2); padding:6px; font-size:11px; border-radius:4px; margin:0;"><code class="language-scratch">doimiy takrorlash:
  y koordinatani (-7) ga o'zgartirish
  agar (y holati < -160) bo'lsa:
    x: (tasodifiy -200 dan 200 gacha) y: (160) ga bor
  0.03 soniya kut</code></pre>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Scratch Блок" data-en="Scratch Block">Scratch Bloki</th>
            <th style="padding:4px 6px;" data-ru="Категория" data-en="Category">Kategoriyasi</th>
            <th style="padding:4px 6px;" data-ru="Что Делает в Игре" data-en="Role in Game">O'yindagi Vazifasi</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="когда стрелка нажата" data-en="when key pressed"><code>[strelka] bosilganda</code></td>
            <td style="padding:4px 6px;" data-ru="События (Events)" data-en="Events">Hodisalar (Events)</td>
            <td style="padding:4px 6px;" data-ru="Управляет героем с клавиатуры" data-en="Controls player from keyboard">Qahramonni klaviaturadan yurgizadi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Выполнено" data-en="[ &nbsp; ] Done">[ &nbsp; ] Bajarildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="повторять всегда" data-en="forever"><code>doimiy takrorlash</code></td>
            <td style="padding:4px 6px;" data-ru="Управление (Control)" data-en="Control">Boshqaruv (Control)</td>
            <td style="padding:4px 6px;" data-ru="Бесконечно двигает препятствие" data-en="Moves obstacle endlessly">Dushmanni to'xtovsiz harakatlantiradi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Выполнено" data-en="[ &nbsp; ] Done">[ &nbsp; ] Bajarildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="касается [Спрайта]?" data-en="touching [Sprite]?"><code>[Qahramon] ga tegdimi?</code></td>
            <td style="padding:4px 6px;" data-ru="Сенсоры (Sensing)" data-en="Sensing">Sezgirlik (Sensing)</td>
            <td style="padding:4px 6px;" data-ru="Определяет удар или сбор монеты" data-en="Detects hits or coin pickups">Zarba yoki tanga olinganini sezadi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Выполнено" data-en="[ &nbsp; ] Done">[ &nbsp; ] Bajarildi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="стоп [все]" data-en="stop [all]"><code>hammasini to'xtatish</code></td>
            <td style="padding:4px 6px;" data-ru="Управление (Control)" data-en="Control">Boshqaruv (Control)</td>
            <td style="padding:4px 6px;" data-ru="Завершает игру при победе" data-en="Ends the game upon victory">G'alaba yoki mag'lubiyatda o'yinni muzlatadi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Выполнено" data-en="[ &nbsp; ] Done">[ &nbsp; ] Bajarildi</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    sec4_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="Спроектируйте свою игру перед началом кодинга в Scratch:" data-en="Blueprint your game before starting to code in Scratch:">O'yinni Scratchda kodlashdan oldin uning dizayn rejasini to'ldiring:</p>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:11px;">
      <div style="border:1px dashed var(--hair); padding:6px; border-radius:4px;">
        <strong data-ru="Мой Главный Герой:" data-en="My Main Hero:">Mening Qahramonim:</strong>
        <div style="height:20px; border-bottom:1px solid var(--hair); margin-top:4px;"></div>
        <span style="color:var(--ink-2); font-size:10px;" data-ru="Имя персонажа и цвет" data-en="Character name & color">(Sprayt nomi va rangi)</span>
      </div>
      <div style="border:1px dashed var(--hair); padding:6px; border-radius:4px;">
        <strong data-ru="Моё Препятствие:" data-en="My Obstacle:">Mening To'sig'im (Dushman):</strong>
        <div style="height:20px; border-bottom:1px solid var(--hair); margin-top:4px;"></div>
        <span style="color:var(--ink-2); font-size:10px;" data-ru="Что угрожает герою?" data-en="What threatens the hero?">(Qahramonga nima xavf soladi?)</span>
      </div>
      <div style="border:1px dashed var(--hair); padding:6px; border-radius:4px;">
        <strong data-ru="Моя Награда (Звезда):" data-en="My Collectible:">Mening Kiber-Xazinam:</strong>
        <div style="height:20px; border-bottom:1px solid var(--hair); margin-top:4px;"></div>
        <span style="color:var(--ink-2); font-size:10px;" data-ru="Что собирает игрок?" data-en="What does player collect?">(Nima yig'ilganda ball oshadi?)</span>
      </div>
      <div style="border:1px dashed var(--hair); padding:6px; border-radius:4px;">
        <strong data-ru="Условие Победы:" data-en="Win Condition:">G'alaba Qoidasi:</strong>
        <div style="height:20px; border-bottom:1px solid var(--hair); margin-top:4px;"></div>
        <span style="color:var(--ink-2); font-size:10px;" data-ru="Сколько очков для победы?" data-en="How many points to win?">(Nechta ball to'planishi kerak?)</span>
      </div>
    </div>
    """

    sec5_html = """
    <div style="font-size:11px; line-height:1.6;">
      <div>[ &nbsp; ] <strong>4 Ball (Baza):</strong> Qahramon strelkalar bilan 4 tomonga erkin yuryapti va kostyumlari almashmoqda.</div>
      <div>[ &nbsp; ] <strong>4 Ball (Amaliy):</strong> Dushman cheksiz siklda pastga tushib, tekkanda jonni kamaytirmoqda.</div>
      <div>[ &nbsp; ] <strong>2 Ball (Challenge):</strong> Tanga olinganda ball oshadi, ovoz yangraydi va 5 ball to'planganda g'alaba bo'ladi!</div>
      <div style="margin-top:6px; border-top:1px solid var(--hair); padding-top:4px; font-weight:700; color:var(--accent);" data-ru="Итоговый балл: _____ / 10 &nbsp; Подпись учителя: ____________" data-en="Total Score: _____ / 10 &nbsp; Teacher Signature: ____________">Jami to'plangan ball: _____ / 10 &nbsp; O'qituvchi imzosi: ____________</div>
    </div>
    """

    replacements = {
        "{{LESSON_NUM}}": "28",
        "{{TITLE_UZ}}": "Scratch Katta Yakuni: O'z Kiber-O'yiningni Yarat! (Mini Game Jam)",
        "{{TITLE_RU}}": "Финал Модуля Scratch: Создай Свою Кибер-Игру! (Mini Game Jam)",
        "{{TITLE_EN}}": "Scratch Grand Finale: Build Your Cyber Game! (Mini Game Jam)",
        "{{COHORT_LABEL_UZ}}": "5–6-SINF",
        "{{COHORT_LABEL_RU}}": "5–6 КЛАСС",
        "{{COHORT_LABEL_EN}}": "GRADES 5–6",
        "{{META_UZ}}": "11-Hafta · Juftlik Dars (80 daqiqa) · Junior Creators & Kiber-O'yinlar Track",
        "{{META_RU}}": "11-я Неделя · Сдвоенный Урок (80 минут) · Направление Junior Creators",
        "{{META_EN}}": "Week 11 · Double Block (80 min) · Junior Creators Track",
        "{{MISSION_UZ}}": "Scratch 3.0 vizual dasturlashda o'rganilgan barcha bilimlar: spraytlar, kostyumlar animatsiyasi, doimiy cheksiz sikllar, klaviatura boshqaruvi va to'qnashuvlarni birlashtirib, o'ynaladigan to'liq mini-arkada o'yinini yaratish va do'stlar bilan sinash.",
        "{{MISSION_RU}}": "Объединить все навыки визуального программирования Scratch 3.0: спрайты, анимацию костюмов, бесконечные циклы, управление клавиатурой и столкновения в полноценную играбельную аркаду.",
        "{{MISSION_EN}}": "Unify all Scratch 3.0 visual coding fundamentals: sprites, costume animations, forever loops, arrow controls, and collision sensing into a complete playable mini-arcade game.",
        "{{SEC1_TITLE_UZ}}": "O'yinning 4 Asosiy Ustuni (Arxitektura)",
        "{{SEC1_TITLE_RU}}": "4 Столпа Моей Игры (Архитектура)",
        "{{SEC1_TITLE_EN}}": "4 Pillars of My Game (Architecture)",
        "{{SEC1_CONTENT}}": sec1_html,
        "{{SEC2_TITLE_UZ}}": "To'siqning Cheksiz Tushish Algoritmi",
        "{{SEC2_TITLE_RU}}": "Алгоритм Бесконечного Падения Препятствия",
        "{{SEC2_TITLE_EN}}": "Autonomous Falling Obstacle Algorithm",
        "{{SEC2_CONTENT}}": sec2_html,
        "{{SEC3_TITLE_UZ}}": "O'yin Komponentlari Tekshiruv Jadvali",
        "{{SEC3_TITLE_RU}}": "Чек-лист Компонентов Игры",
        "{{SEC3_TITLE_EN}}": "Game Components Checklist",
        "{{SEC3_CONTENT}}": sec3_html + sec4_html,
        "{{SEC4_CONTENT}}": sec5_html
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

    title_uz = "28-dars: Scratch Katta Yakuni: O'z Kiber-O'yiningni Yarat!"
    title_ru = "Урок 28: Финал Модуля Scratch: Создай Свою Кибер-Игру!"
    title_en = "Lesson 28: Scratch Grand Finale: Build Your Cyber Game!"

    tasks_html = """
    <!-- TIER 1 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1-Daraja (Baza — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Базовая Аркада: Управление и Препятствие" data-en="Base Arcade: Controls & Falling Obstacle">Baza O'yini: Qahramon va Tushuvchi To'siq</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите псевдокод или Scratch-скрипт движения персонажа стрелками и падения метеорита в бесконечном цикле «всегда»." data-en="Write pseudocode or Scratch script for player arrow controls and falling obstacle inside a forever loop.">Qahramonni strelkalar orqali yurgizish hamda to'siqni cheksiz siklda tepadan tushirish algoritmini yozing.</p>
      <textarea class="answer-area" id="ans_task_1" rows="6" placeholder="Scratch skriptingizni bu yerga yozing..." data-placeholder-ru="Напишите ваш скрипт Scratch здесь..." data-placeholder-en="Write your Scratch script here..." oninput="saveAnswers()"></textarea>
      <div class="solution-box" id="sol_task_1" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px; font-family:var(--font-mono);">
        <strong>Namunaviy Yechim:</strong><br>
        <code>qachonki [o'ngga strelka] bosilganda: x ni 10 ga oshir, keyingi kostyum</code><br>
        <code>qachonki [chapga strelka] bosilganda: x ni -10 ga oshir, keyingi kostyum</code><br>
        <code>doimiy takrorlash: y ni -7 ga o'zgartir, agar y &lt; -160 bo'lsa: x: tasodifiy y: 160 ga bor</code>
      </div>
    </div>

    <!-- TIER 2 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(147,51,234,0.15); color:var(--purple);">2-Daraja (Amaliy — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Сбор Звезд, Очки и Звуковые Эффекты" data-en="Star Collecting, Score & Audio Effects">Tanga Yig'ish, Ballar va Tovush Effektlari</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Опишите, как работает сбор звезды: детекция касания, увеличение переменной «Счет» на 1, воспроизведение звука «Coin» и телепортация в новое случайное место." data-en="Describe how star collection works: touch detection, incrementing Score variable by 1, playing 'Coin' sound, and teleporting to a new random location.">Tanga qanday yig'ilishini tushuntiring: <code>tegdimi?</code> sezgirligi, <code>Ballni 1 ga oshirish</code>, tovush chalish va yangi nuqtaga sakrash.</p>
      <textarea class="answer-area" id="ans_task_2" rows="6" placeholder="Tanga skriptini bu yerga yozing..." data-placeholder-ru="Напишите скрипт звезды здесь..." data-placeholder-en="Write star collection script here..." oninput="saveAnswers()"></textarea>
      <div class="solution-box" id="sol_task_2" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px; font-family:var(--font-mono);">
        <strong>Namunaviy Yechim:</strong><br>
        <code>doimiy takrorlash:</code><br>
        <code>&nbsp;&nbsp;agar (mushukka tegdimi?) bo'lsa:</code><br>
        <code>&nbsp;&nbsp;&nbsp;&nbsp;ovoz [Coin] ni chal</code><br>
        <code>&nbsp;&nbsp;&nbsp;&nbsp;ballni (1) ga oshir</code><br>
        <code>&nbsp;&nbsp;&nbsp;&nbsp;tasodifiy pozitsiyaga bor</code>
      </div>
    </div>

    <!-- TIER 3 (2 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">3-Daraja (Challenge — 2 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Второй Враг или 30-Секундный Таймер" data-en="Second Obstacle or 30s Countdown Timer">Kiber-Challenge: 2-To'siq yoki Taymer</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Как запрограммировать второе препятствие (например, летящую горизонтально ракету) или обратный отсчет таймера (30..0) с проигрышем, если время истекло?" data-en="How would you code a 2nd obstacle moving horizontally, or a 30s countdown timer with a Game Over if time runs out?">O'yinga gorizontal uchuvchi 2-to'siqni yoki 30 soniyalik teskari hisob taymerini qanday bloklar bilan qo'shish mumkin?</p>
      <textarea class="answer-area" id="ans_task_3" rows="6" placeholder="Challenge yechimingizni bu yerga yozing..." data-placeholder-ru="Напишите решение челленджа здесь..." data-placeholder-en="Write challenge solution here..." oninput="saveAnswers()"></textarea>
      <div class="solution-box" id="sol_task_3" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px; font-family:var(--font-mono);">
        <strong>Namunaviy Yechim:</strong><br>
        <code>Taymer: [Vaqt] ni (30) ga o'rnat.</code><br>
        <code>takrorla (30) marta: 1 soniya kut, [Vaqt] ni (-1) ga o'zgartir.</code><br>
        <code>agar (ball &lt; 5) bo'lsa: [Vaqt Tugadi! Mag'lubiyat] deb ayt, hammasini to'xtatish.</code>
      </div>
    </div>
    """

    replacements = {
        "{{TITLE_UZ}}": "28-dars: Scratch Katta Yakuni: O'z Kiber-O'yiningni Yarat!",
        "{{TITLE_RU}}": "Урок 28: Финал Модуля Scratch: Создай Свою Кибер-Игру!",
        "{{TITLE_EN}}": "Lesson 28: Scratch Grand Finale: Build Your Cyber Game!",
        "{{COHORT_LABEL_UZ}}": "5–6-SINF",
        "{{HERO_TAG_UZ}}": "11-Hafta · Junior Creators Track",
        "{{HERO_DESC_UZ}}": "Scratch 3.0 da o'z mustaqil arkada o'yiningizni yaratish: boshqaruv, to'siqlar, tangalar va g'alaba shartlari bo'yicha 3 darajali topshiriqlar.",
        "{{HERO_DESC_RU}}": "Создание собственной игры на Scratch 3.0: управление, препятствия, сбор звезд и условия победы — 3 уровня сложности.",
        "{{HERO_DESC_EN}}": "Creating your own arcade game in Scratch 3.0: controls, falling obstacles, collectibles, and victory rules across 3 tiers.",
        "{{RUBRIC_T1_UZ}}": "1-Bosqich: Baza (Strelkalar va tushuvchi to'siq)",
        "{{RUBRIC_T1_RU}}": "1-й Уровень: База (Управление стрелками и препятствие)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (Arrow controls & falling obstacle)",
        "{{RUBRIC_T2_UZ}}": "2-Bosqich: Amaliyot (Tanga yig'ish va ballar)",
        "{{RUBRIC_T2_RU}}": "2-й Уровень: Практика (Сбор монет и счет)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Coin collecting & scoring)",
        "{{RUBRIC_T3_UZ}}": "3-Bosqich: Kiber-Chaqiruv (2-to'siq yoki 30s taymer)",
        "{{RUBRIC_T3_RU}}": "3-й Уровень: Вызов (Второй враг или таймер)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (Second obstacle or timer)",
        "{{TASKS_HTML}}": tasks_html,
        "{{LESSON_SLUG}}": "5-6-w11-l28-scratch-katta-yakuniy-loyiha"
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    doc = """# 28-dars: Scratch Katta Yakuni: O'z Kiber-O'yiningni Yarat! (O'qituvchi Metodologiyasi)

## Darsning Pasporti
- **Sinf:** 5–6-sinf (Junior Creators Track)
- **Davomiyligi:** 80 daqiqa (Juftlik Dars / Double Block)
- **Asosiy maqsad:** Scratch 3.0 vizual dasturlash modulini yakunlash. O'quvchilarga koordinata harakati, kostyumlar animatsiyasi, cheksiz sikllar, to'qnashuvlarni sezish (sensing), ballar hisobi va g'alaba/mag'lubiyat qoidalarini yagona o'yinda birlashtirishni o'rgatish.

---

## 80 Daqiqalik Aniq Vaqt Taqsimoti (Pacing)

### 1-Qism: Nazariya, Xatolar Tahlili va Jonli Test (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Motivatsiya | 1 | Game Jam konseptsiyasini va 4 ta ustunni tushuntirish. | Diqqat bilan tinglaydilar va maqsadni belgilaydilar. |
| **04:00–12:00** | 27-dars HW Tahlili | 2 | 0.05s kutish bo'lmaganda qotish va boshi pastga qulash xatolarini tahlil qilish. | Blitz savolga javob beradilar, xatolarini to'g'rilaydilar. |
| **12:00–18:00** | O'yinning 4 Ustuni | 3 | Player, Obstacle, Collectible va Rules tizimlarini chizib berish. | O'z o'yinlari uchun qahramon va to'siqni tanlaydilar. |
| **18:00–24:00** | Qahramon Boshqaruvi | 4 | Strelkalar, X/Y koordinata o'zgarishi va kostyum almashishini ko'rsatish. | Qahramon skripti sintaksisini eslab qoladilar. |
| **24:00–30:00** | Dushman Harakati | 5 | Cheksiz siklda tushish va tasodifiy X koordinata formulasini tushuntirish. | Tasodifiy koordinatalar qanday ishlashini tushunadilar. |
| **30:00–35:00** | To'qnashuv va Sezgirlik | 6 | touching bloki, zarba ovozi va jonlar kamayishi mantig'ini ko'rsatish. | Ziyon mexanikasini o'rganadilar. |
| **35:00–40:00** | Tangalar va G'alaba | 7 | Tanga yig'ish, ball oshishi va stop all g'alaba shartini o'rgatish. | O'yinni yutish qoidasini rejalashtiradilar. |

### 2-Qism: Smartboard Sinovi, Katta Arena va Showcase (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **40:00–48:00** | Smartboard Simulyatori | 8 | Taqdimot ichidagi arkadani doskada o'ynab berish, bolalarni doskaga chiqarish. | Smartboardda 5 ta tanga yig'ib o'yinni sinaydilar. |
| **48:00–55:00** | Viktorina (Quiz) | 9 | 3 ta nazorat savoli bo'yicha viktorina o'tkazish. | Faol javob beradilar va o'z bilimlarini tekshiradilar. |
| **55:00–70:00** | 25 Daqiqalik Arena | 10 | 25:00 taymerni yoqish, partalar bo'ylab yurib ko'maklashish. | O'z shaxsiy o'yinlarini Scratch 3.0 da noldan yaratadilar. |
| **70:00–74:00** | Partadosh Auditi | 11 | O'rin almashishni e'lon qilish, 4 mezonli auditni nazorat qilish. | Bir-birining o'yinini o'ynab, xatolarni tuzatadilar. |
| **74:00–77:00** | Katta Ekran Showcasi | 12 | Eng yaxshi 3 ta o'yinni doskaga chiqarish va butun sinf bilan olqishlash. | Sinfdoshlari loyihasini tomosha qilib, zavqlanadilar. |
| **77:00–80:00** | Uy Vazifasi va Yakun | 13–14 | 10 ballik vazifani tushuntirish va Scratch modulini rasman yakunlash! | Kundaliklariga vazifani belgilaydilar. |

---

## O'qituvchi Uchun Muhim Blitz Savollari
1. **"Nega to'siq mushukka tekkandan keyin zudlik bilan yana tepaga sakrashi kerak?"**
   - Javob: Chunki agar to'siq mushuk ustida turib qolsa, har millisekundda touching ishlavorib, 3 ta jon bir zumda 0 ga tushib ketadi!
2. **"Tanga olinganda 'stop all' qo'ymasak nima bo'ladi?"**
   - Javob: O'yin cheksiz davom etaveradi va g'alaba holati yuz bermaydi. O'yinchiga aniq maqsad va g'alaba zavqi kerak.

---

## 10 Ballik Baholash Rubrikasi
- **4 Ball (Baza):** Qahramon strelkalar orqali ravon yuryapti, kostyumi almashmoqda va boshlang'ich nuqtaga tushadi.
- **4 Ball (Amaliy):** To'siq cheksiz siklda tushmoqda, tasodifiy koordinatadan qayta tug'ilmoqda va tekkanda jon kamaymoqda.
- **2 Ball (Challenge):** Tanga yig'ilganda ovoz chiqishi, ball qo'shilishi va 5 ball to'planganda g'alaba ekrani ko'rsatilib o'yin to'xtashi!
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("  ✓ Created: TEACHER_READING.md")

def build_playground():
    html = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Студия Scratch Game Jam: Создай Свою Игру!" data-en="Scratch Game Jam Studio: Build Your Game!">Scratch Game Jam Studiyasi: O'z O'yiningni Yarat!</title>
  <style>
    :root {
      --bg: #090d16;
      --surface: #131b2e;
      --surface-2: #1e293b;
      --ink: #f8fafc;
      --ink-2: #94a3b8;
      --accent: #38bdf8;
      --accent-glow: rgba(56,189,248,0.3);
      --green: #10b981;
      --red: #ef4444;
      --yellow: #f59e0b;
      --purple: #a855f7;
      --font: system-ui, -apple-system, sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--ink);
      font-family: var(--font);
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    header {
      background: var(--surface);
      border-bottom: 1px solid rgba(255,255,255,0.08);
      padding: 10px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
      font-size: 16px;
      color: var(--accent);
    }
    .hud {
      display: flex;
      gap: 16px;
      align-items: center;
      font-weight: 700;
      font-size: 14px;
    }
    .hud-badge {
      background: var(--surface-2);
      padding: 6px 12px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    main {
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 16px;
      padding: 16px;
      overflow: hidden;
    }
    .game-stage-wrapper {
      background: #020617;
      border: 2px solid var(--accent);
      border-radius: 12px;
      position: relative;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    #gameCanvas {
      display: block;
      width: 100%;
      height: 100%;
      image-rendering: pixelated;
    }
    .game-overlay {
      position: absolute;
      inset: 0;
      background: rgba(2,6,23,0.85);
      backdrop-filter: blur(4px);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 20px;
      z-index: 10;
    }
    .sidebar {
      background: var(--surface);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      overflow-y: auto;
    }
    .control-box {
      background: var(--surface-2);
      padding: 12px;
      border-radius: 8px;
    }
    .control-box h4 {
      font-size: 12px;
      color: var(--accent);
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .d-pad {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
      max-width: 160px;
      margin: 0 auto;
    }
    .btn {
      background: var(--accent);
      color: #000;
      border: none;
      border-radius: 6px;
      padding: 8px 14px;
      font-weight: 700;
      cursor: pointer;
      font-size: 13px;
      transition: all 0.2s;
    }
    .btn:hover { opacity: 0.9; transform: scale(1.02); }
    .btn-green { background: var(--green); color: #fff; }
    .btn-red { background: var(--red); color: #fff; }
    .btn-gray { background: #475569; color: #fff; }
    .block-card {
      background: #0f172a;
      border-left: 4px solid var(--accent);
      padding: 6px 10px;
      font-family: monospace;
      font-size: 11px;
      border-radius: 0 4px 4px 0;
      margin-bottom: 4px;
      line-height: 1.4;
    }
  </style>
</head>
<body>

<header>
  <div class="brand">
    <span>🐱 Scratch 3.0 Game Jam Arena</span>
    <span style="font-size:11px; background:rgba(56,189,248,0.15); color:var(--accent); padding:2px 8px; border-radius:12px;">5–6-Sinf</span>
  </div>
  <div class="hud">
    <div class="hud-badge">⭐ <span data-ru="Счет:" data-en="Score:">Ball:</span> <strong id="hudScore" style="color:var(--yellow); font-size:16px;">0 / 5</strong></div>
    <div class="hud-badge">❤️ <span data-ru="Жизни:" data-en="Lives:">Jon:</span> <strong id="hudLives" style="color:var(--red); font-size:16px;">3</strong></div>
    <div class="hud-badge">⏱️ <span data-ru="Время:" data-en="Time:">Vaqt:</span> <strong id="hudTimer" style="color:var(--ink); font-size:16px;">00s</strong></div>
  </div>
</header>

<main>
  <div class="game-stage-wrapper">
    <canvas id="gameCanvas" width="800" height="500"></canvas>
    
    <div class="game-overlay" id="overlay">
      <h2 style="font-size:28px; margin-bottom:8px; color:var(--accent);" data-ru="🎮 Scratch Kiber-Arkada" data-en="🎮 Scratch Cyber Arcade">🎮 Scratch Kiber-Arkada</h2>
      <p style="font-size:14px; color:var(--ink-2); max-width:400px; margin-bottom:16px;" data-ru="Управляйте Котом с клавиатуры (Стрелки / WASD) или сенсорным пультом. Избегайте метеоритов и соберите 5 звезд!" data-en="Control the Cat via arrows or touch D-Pad. Dodge falling meteors and collect 5 cyber stars to win!">Qahramonni strelkalar yoki quyidagi pult orqali boshqaring. Meteoritlardan qoching va 5 ta Kiber-Yulduzni to'plang!</p>
      <button class="btn btn-green" onclick="startGame()" style="font-size:16px; padding:10px 24px;" data-ru="▶️ Начать Игру" data-en="▶️ Start Game">▶️ O'yinni Boshlash</button>
    </div>
  </div>

  <div class="sidebar">
    <div class="control-box">
      <h4 data-ru="Сенсорный Пульт (Для Доски)" data-en="Touch Controller (Smartboard)">Sensorli Boshqaruv (Doska Uchun)</h4>
      <div class="d-pad">
        <div></div>
        <button class="btn btn-gray" onpointerdown="triggerMove(0, -30)">⬆️</button>
        <div></div>
        <button class="btn btn-gray" onpointerdown="triggerMove(-30, 0)">⬅️</button>
        <button class="btn btn-gray" onpointerdown="triggerMove(0, 30)">⬇️</button>
        <button class="btn btn-gray" onpointerdown="triggerMove(30, 0)">➡️</button>
      </div>
    </div>

    <div class="control-box">
      <h4 data-ru="Параметры Игры" data-en="Game Parameters">O'yin Sozlamalari</h4>
      <div style="font-size:12px; display:flex; flex-direction:column; gap:8px;">
        <label style="display:flex; justify-content:space-between;">
          <span data-ru="Скорость Метеоритов:" data-en="Meteor Speed:">Meteorit Tezligi:</span>
          <select id="selSpeed" style="background:#0f172a; color:#fff; border:1px solid #334155; border-radius:4px; padding:2px 6px;">
            <option value="4" selected data-ru="Нормальная (4)" data-en="Normal (4)">Oddiy (4)</option>
            <option value="7" data-ru="Быстрая (7)" data-en="Fast (7)">Tezkor (7)</option>
            <option value="10" data-ru="Хардкор (10)" data-en="Hardcore (10)">Kiber-Tezlik (10)</option>
          </select>
        </label>
        <label style="display:flex; justify-content:space-between;">
          <span data-ru="Количество Врагов:" data-en="Obstacle Count:">To'siqlar Soni:</span>
          <select id="selCount" style="background:#0f172a; color:#fff; border:1px solid #334155; border-radius:4px; padding:2px 6px;">
            <option value="1" data-ru="1 Метеорит" data-en="1 Meteor">1 ta Meteorit</option>
            <option value="2" selected data-ru="2 Метеорита" data-en="2 Meteors">2 ta Meteorit</option>
            <option value="3" data-ru="3 Метеорита" data-en="3 Meteors">3 ta Meteorit</option>
          </select>
        </label>
      </div>
      <button class="btn btn-gray" onclick="resetGame()" style="width:100%; margin-top:10px; font-size:12px;" data-ru="🔄 Перезапустить" data-en="🔄 Reset Game">🔄 Qayta Boshlash</button>
    </div>

    <div class="control-box">
      <h4 data-ru="Активные Блоки Scratch" data-en="Active Scratch Blocks">Ishlayotgan Scratch Bloklari</h4>
      <div class="block-card" style="border-left-color:var(--yellow);" data-ru="когда нажат флаг" data-en="when green flag clicked">🚩 yashil bayroqcha bosilganda</div>
      <div class="block-card" style="border-left-color:var(--purple);" data-ru="повторять всегда" data-en="forever">🔄 doimiy takrorlash:</div>
      <div class="block-card" style="border-left-color:var(--accent); margin-left:8px;" data-ru="изменить Y на -Скорость" data-en="change Y by -Speed">⬇️ y koordinatani (-Speed) ga o'zgartir</div>
      <div class="block-card" style="border-left-color:var(--green); margin-left:8px;" data-ru="если касается Кота? то" data-en="if touching Cat? then">⚡ agar (Mushukka tegdimi?) bo'lsa:</div>
      <div class="block-card" style="border-left-color:var(--red); margin-left:16px;" data-ru="изменить Жизни на -1" data-en="change Lives by -1">💔 jonni (-1) ga kamaytir</div>
    </div>
  </div>
</main>

<script>
var canvas = document.getElementById('gameCanvas');
var ctx = canvas.getContext('2d');

var audioCtx = null;
function playTone(freq, type, duration) {
  try {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    var osc = audioCtx.createOscillator();
    var gain = audioCtx.createGain();
    osc.type = type;
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + duration);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + duration);
  } catch(e) {}
}

var gameRunning = false;
var score = 0;
var lives = 3;
var gameSeconds = 0;
var timerInterval = null;
var loopInterval = null;

var cat = { x: 400, y: 420, size: 30, speed: 25 };
var meteors = [];
var star = { x: 400, y: 150, size: 22 };

function initMeteors() {
  meteors = [];
  var count = parseInt(document.getElementById('selCount').value) || 2;
  var spd = parseInt(document.getElementById('selSpeed').value) || 4;
  for (var i = 0; i < count; i++) {
    meteors.push({
      x: Math.floor(Math.random() * 700) + 50,
      y: Math.floor(Math.random() * -200) - 20,
      size: 24,
      speed: spd + Math.random() * 2
    });
  }
}

function startGame() {
  document.getElementById('overlay').style.display = 'none';
  gameRunning = true;
  score = 0;
  lives = 3;
  gameSeconds = 0;
  cat.x = 400;
  cat.y = 420;
  initMeteors();
  spawnStar();
  updateHUD();

  if (timerInterval) clearInterval(timerInterval);
  timerInterval = setInterval(function() {
    if (!gameRunning) return;
    gameSeconds++;
    document.getElementById('hudTimer').textContent = (gameSeconds < 10 ? '0' : '') + gameSeconds + 's';
  }, 1000);

  if (loopInterval) clearInterval(loopInterval);
  loopInterval = setInterval(gameLoop, 30);
  playTone(523.25, 'sine', 0.2);
}

function resetGame() {
  gameRunning = false;
  if (timerInterval) clearInterval(timerInterval);
  if (loopInterval) clearInterval(loopInterval);
  var overlay = document.getElementById('overlay');
  overlay.style.display = 'flex';
  overlay.innerHTML = '<h2 style="font-size:28px; margin-bottom:8px; color:var(--accent);">🎮 Scratch Kiber-Arkada</h2><p style="font-size:14px; color:var(--ink-2); max-width:400px; margin-bottom:16px;">Tayyor bo‘lsangiz, o‘yinni boshlang!</p><button class="btn btn-green" onclick="startGame()" style="font-size:16px; padding:10px 24px;">▶️ O‘yinni Boshlash</button>';
  score = 0;
  lives = 3;
  updateHUD();
  drawScene();
}

function spawnStar() {
  star.x = Math.floor(Math.random() * 700) + 50;
  star.y = Math.floor(Math.random() * 260) + 60;
}

function triggerMove(dx, dy) {
  if (!gameRunning) return;
  cat.x = Math.max(35, Math.min(765, cat.x + dx));
  cat.y = Math.max(40, Math.min(460, cat.y + dy));
  playTone(330, 'triangle', 0.05);
}

window.addEventListener('keydown', function(e) {
  if (!gameRunning) return;
  if (e.key === 'ArrowUp' || e.key === 'w') { triggerMove(0, -cat.speed); e.preventDefault(); }
  else if (e.key === 'ArrowDown' || e.key === 's') { triggerMove(0, cat.speed); e.preventDefault(); }
  else if (e.key === 'ArrowLeft' || e.key === 'a') { triggerMove(-cat.speed, 0); e.preventDefault(); }
  else if (e.key === 'ArrowRight' || e.key === 'd') { triggerMove(cat.speed, 0); e.preventDefault(); }
});

function gameLoop() {
  if (!gameRunning) return;

  // Move meteors (Forever cycle)
  for (var i = 0; i < meteors.length; i++) {
    var m = meteors[i];
    m.y += m.speed;
    if (m.y > 520) {
      m.y = -30;
      m.x = Math.floor(Math.random() * 700) + 50;
    }

    // Check hit
    var distM = Math.hypot(cat.x - m.x, cat.y - m.y);
    if (distM < cat.size + m.size - 6) {
      lives--;
      m.y = -40;
      m.x = Math.floor(Math.random() * 700) + 50;
      playTone(150, 'sawtooth', 0.25);
      updateHUD();
      if (lives <= 0) {
        endGame(false);
        return;
      }
    }
  }

  // Check Star pickup
  var distS = Math.hypot(cat.x - star.x, cat.y - star.y);
  if (distS < cat.size + star.size) {
    score++;
    playTone(880, 'sine', 0.15);
    spawnStar();
    updateHUD();
    if (score >= 5) {
      endGame(true);
      return;
    }
  }

  drawScene();
}

function updateHUD() {
  document.getElementById('hudScore').textContent = score + ' / 5';
  document.getElementById('hudLives').textContent = lives;
}

function endGame(won) {
  gameRunning = false;
  if (timerInterval) clearInterval(timerInterval);
  if (loopInterval) clearInterval(loopInterval);
  var overlay = document.getElementById('overlay');
  overlay.style.display = 'flex';
  if (won) {
    playTone(659.25, 'sine', 0.4);
    setTimeout(function(){ playTone(880, 'sine', 0.6); }, 200);
    overlay.innerHTML = '<h2 style="font-size:32px; color:var(--green); margin-bottom:8px;">🏆 BUYUK G‘ALABA!</h2><p style="font-size:14px; color:#cbd5e1; max-width:400px; margin-bottom:16px;">Siz barcha 5 ta kiber-yulduzni ' + gameSeconds + ' soniyada yig‘dingiz!</p><button class="btn btn-green" onclick="startGame()" style="font-size:16px; padding:10px 24px;">Yana O‘ynash</button>';
  } else {
    playTone(100, 'sawtooth', 0.5);
    overlay.innerHTML = '<h2 style="font-size:32px; color:var(--red); margin-bottom:8px;">💥 GAME OVER</h2><p style="font-size:14px; color:#cbd5e1; max-width:400px; margin-bottom:16px;">Meteoritlar barcha jonlaringizni tugatdi. Xavfsiz masofani saqlang!</p><button class="btn btn-red" onclick="startGame()" style="font-size:16px; padding:10px 24px;">Qayta Urinish</button>';
  }
}

function drawScene() {
  ctx.fillStyle = '#020617';
  ctx.fillRect(0, 0, 800, 500);

  // Background Grid / Stars
  ctx.fillStyle = 'rgba(255,255,255,0.15)';
  for (var i = 0; i < 40; i++) {
    ctx.fillRect((i * 67) % 800, (i * 43) % 500, 2, 2);
  }

  // Draw Star
  ctx.fillStyle = '#f59e0b';
  ctx.beginPath();
  ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
  ctx.fill();
  ctx.font = '22px sans-serif';
  ctx.fillText('⭐', star.x - 11, star.y + 8);

  // Draw Meteors
  for (var j = 0; j < meteors.length; j++) {
    var m = meteors[j];
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.arc(m.x, m.y, m.size, 0, Math.PI * 2);
    ctx.fill();
    ctx.font = '22px sans-serif';
    ctx.fillText('☄️', m.x - 11, m.y + 8);
  }

  // Draw Player Cat
  ctx.fillStyle = '#38bdf8';
  ctx.beginPath();
  ctx.arc(cat.x, cat.y, cat.size, 0, Math.PI * 2);
  ctx.fill();
  ctx.font = '24px sans-serif';
  ctx.fillText('🐱', cat.x - 12, cat.y + 8);
}

drawScene();
</script>

</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "playground", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: playground/index.html")

def main():
    print("📦 Building 5-6-sinf (Lesson 28: Scratch Katta Yakuni / Mini Game Jam)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_playground()
    print("🎉 Done! Generated Grade 5–6 Lesson 28.")

if __name__ == "__main__":
    main()
