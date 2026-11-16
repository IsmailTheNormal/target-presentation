#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_7_8_w11_l31.py — Builder for 7–8th Grade, Week 11, Lesson 31

Mavzu: Procedural Dunyo Generatsiyasi: Tasodifiy Labirintlar va Xazinalar (Random Walker Algoritmi)
Format: Yakka Dars (40 daqiqa), 10 slayd
Kohorta: 7-8-sinf (Game Dev, Interaktiv Veb & FUT Creator Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "7-8-sinf", "11-hafta", "31-dars-procedural-dunyo-generatsiyasi")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "simulator"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (10 Slides)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="7–8-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 31" data-en="GRADE 7–8 · WEEK 11 · LESSON 31">7–8-SINF · 11-HAFTA · 31-DARS</span></div>
    <h1 class="display" data-ru="Процедурная Генерация Мира: Случайные Лабиринты и Сокровища" data-en="Procedural World Generation: Random Mazes & Treasures">Procedural Dunyo Generatsiyasi: Tasodifiy Labirintlar va Xazinalar</h1>
    <p class="lede" data-ru="Алгоритм Random Walker (Пьяный шахтер) на JavaScript: генерация бесконечных подземелий, гарантированная проходимость и умное размещение сундуков." data-en="Random Walker algorithm in JavaScript: generating infinite dungeons, guaranteed path connectivity, and procedural placement of loot chests.">JavaScript-da Random Walker (Mast konchi) algoritmi: cheksiz yangi yer osti labirintlari, 100% kafolatlangan o'tish yo'li va xazinalarni joylashtirish.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">40 daqiqalik Yakka Dars</div>
        <h3 data-ru="Магия Процедурности" data-en="PCG Magic">PCG Geym-Dizayn</h3>
        <p data-ru="Как Minecraft, Hades и Spelunky создают уникальные миры без участия дизайнера уровней." data-en="How Minecraft, Hades, and Spelunky build unique worlds without manual level design.">Qanday qilib Minecraft, Hades va Spelunky har safar dizaynersiz yangi, betakror dunyo yaratadi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Jonli Generator</div>
        <h3 data-ru="Случайный Лабиринт" data-en="Procedural Maze">Cheksiz Roguelike Dunyo</h3>
        <p data-ru="Каждый ученик напишет генератор подземелий, создающий проходимую карту с золотом и порталом выхода." data-en="Each student writes a dungeon generator creating navigable maps with gold chests and exit portals.">Har bir o'quvchi xazinalar va chiqish eshigiga ega o'tib bo'ladigan tasodifiy xarita generatorini kodlaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–08:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 30-УРОКА" data-en="LESSON 30 HOMEWORK REVIEW">30-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Тайлмапы и Туман Войны: Ловушка Статической Карты" data-en="Tilemaps & Fog of War: The Static Map Bottleneck">Tayllar va Urush Tumani: Statik Xarita Qopqoni</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Типичная ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Жестко прописанная матрица в коде игры" data-en="Hardcoded Dungeon Matrix in Source Code">Kod Ichiga Qotirilgan Statik 2D Massiv</h3>
        <p data-ru="Ученики вручную нарисовали матрицу 10x10 в коде. Проблема: игрок проходит лабиринт один раз, запоминает все повороты, и игра мгновенно теряет всякий интерес." data-en="Students hand-coded a static 10x10 matrix. Problem: players beat the maze once, memorize all routes, and replay value drops to zero.">O'quvchilar kod ichida qotirilgan 10x10 matritsa yozdilar. Muammo: o'yinchi labirintni bir marta yutgach, barcha burchaklarni yodlab oladi va o'yin qiziqsiz bo'lib qoladi.</p>
        <pre><code>// ❌ Statik xarita: Har doim bir xil va zerikarli
const MAP = [
  [1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]
];</code></pre>
      </div>
      <div class="box success-border">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой стандарт (Golden Solution)" data-en="Golden Standard">Oltin Standart (Golden Solution)</div>
        <h3 data-ru="Динамическая процедурная генерация" data-en="Dynamic Procedural Generation">Dinamik Procedural Generatsiya (PCG)</h3>
        <p data-ru="Вместо фиксированного массива запускается алгоритм. При каждом перезапуске создается абсолютно новая геометрия комнат, коридоров и сундуков с гарантией проходимости." data-en="Instead of static arrays, an algorithm runs. Every restart spawns fresh room geometry, corridors, and chests with guaranteed connectivity.">Qotirilgan massiv o'rniga algoritm ishlaydi. Har safar o'yin boshlanganda mutlaqo yangi xonalar, yo'laklar va xazinalar paydo bo'ladi.</p>
        <pre><code>// ✅ Procedural: Har safar yangi dunyo yaratiladi!
const MAP = generateDungeon(15, 15, 60); // 60 qadamli labirint</code></pre>
      </div>
    </div>
    <div class="bridge-card" style="margin-top:12px; padding:10px 16px; border-radius:10px; background:rgba(59,130,246,0.08); border-left:4px solid var(--accent); display:flex; justify-content:space-between; align-items:center;">
      <div>
        <strong style="color:var(--accent);" data-ru="Блиц-вопрос (30 сек):" data-en="Blitz Question (30s):">⚡ Blitz-Savol (30s):</strong>
        <span data-ru="Почему нельзя просто заполнить карту случайными стенами через Math.random() < 0.4?" data-en="Why can't we simply place walls via Math.random() < 0.4?">Nega xaritani shunchaki Math.random() &lt; 0.4 deb tasodifiy devorlar bilan to'ldirib bo'lmaydi?</span>
      </div>
      <span class="badge" style="font-size:11px;" data-ru="Игрок застрянет!" data-en="Trapped Player!">Chiqish berkilib qoladi!</span>
    </div>
  </section>

  <!-- SLIDE 3: WHAT IS PCG? -->
  <section class="slide" data-phase="Konsept|Концепт|Concept" data-time="08:00–12:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ОСНОВЫ G障碍ME DEV" data-en="GAME DEV FOUNDATIONS">PROCEDURAL KONTENT NIMA?</span></div>
    <h2 data-ru="Магия PCG: Как Игры Генерируют Бесконечные Миры?" data-en="PCG Magic: How Games Generate Infinite Worlds?">PCG Sehri: O'yinlar Qanday Qilib Cheksiz Dunyo Yaratadi?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:15px; margin-bottom:12px;" data-ru="<strong>PCG (Procedural Content Generation):</strong> создание игрового контента с помощью алгоритмов вместо ручного труда художников." data-en="<strong>PCG (Procedural Content Generation):</strong> algorithmic creation of game assets and levels rather than manual authoring."><strong>PCG (Procedural Content Generation):</strong> o'yin darajalarini dizayner qo'li bilan emas, balki matematika va algoritmlar yordamida avtomatik yasash.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Реиграбельность:</strong> Каждый раз новый опыт — игрок никогда не попадает в один и тот же лабиринт." data-en="<strong>Replayability:</strong> Infinite fresh experiences — players never face the identical layout twice."><strong>Replayability (Qayta o'ynash zavqi):</strong> Har safar yangi tuyg'u — o'yinchi hech qachon bir xil labirintga tushmaydi.</li>
          <li data-ru="<strong>Минимальный размер файлов:</strong> Не нужно хранить гигабайты карт — 30 строк кода создают миллионы миров!" data-en="<strong>Tiny File Footprint:</strong> No need to store gigabytes of maps — 30 lines of code generate millions of layouts!"><strong>Kichik Fayl Hajmi:</strong> Millionlab xaritalarni saqlash shart emas — faqat 30 qatorli generator kodi yetarli!</li>
          <li data-ru="<strong>Гарантированная связность:</strong> Алгоритм математически обеспечивает непрерывный проход от спавна к выходу." data-en="<strong>Guaranteed Path:</strong> The algorithm mathematically ensures an open corridor connects spawn to exit."><strong>Kafolatlangan Bog'liqlik:</strong> Boshlang'ich nuqtadan chiqish eshigigacha yo'l doimo ochiq bo'lishi shart!</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-size:12px; line-height:1.6;">
        <div style="font-weight:700; color:var(--accent); margin-bottom:6px;" data-ru="Легендарные PCG Игры Мира:" data-en="Legendary PCG Games Worldwide:">Mashhur PCG O'yinlari:</div>
        <div style="display:flex; flex-direction:column; gap:8px;">
          <div style="background:rgba(255,255,255,0.03); padding:6px 10px; border-radius:6px; border-left:3px solid var(--green);">
            <strong>Minecraft:</strong> Cheksiz tog'lar, g'orlar va daryolarni Perlin Noise algoritmi bilan generatsiya qiladi.
          </div>
          <div style="background:rgba(255,255,255,0.03); padding:6px 10px; border-radius:6px; border-left:3px solid var(--purple);">
            <strong>Spelunky / Hades:</strong> Roguelike xonalar va qopqonlarni xona shablonlari va Random Walker bilan quradi.
          </div>
          <div style="background:rgba(255,255,255,0.03); padding:6px 10px; border-radius:6px; border-left:3px solid var(--amber);">
            <strong>Target Dungeon 3.0:</strong> Bugun o'zimiz yaratadigan tasodifiy Roguelike labirinti!
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: RANDOM WALKER ALGORITHM -->
  <section class="slide" data-phase="Algoritm|Алгоритм|Algorithm" data-time="12:00–16:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="АЛГОРИТМ RANDOM WALKER" data-en="RANDOM WALKER ALGORITHM">RANDOM WALKER (MAST KONCHI)</span></div>
    <h2 data-ru="Как Работает Алгоритм «Пьяного Шахтера»?" data-en="How Does the 'Drunk Miner' Algorithm Work?">Random Walker (Mast Konchi) Algoritmi Qanday Ishlaydi?</h2>
    <div class="grid-4" style="gap:10px;">
      <div class="box" style="border-top:3px solid var(--red);">
        <div class="tag" style="color:var(--red);">1. Boshlanish</div>
        <h4 style="margin:6px 0;" data-ru="Сплошная Стена" data-en="Solid Wall">To'liq Qora Devor</h4>
        <p style="font-size:12px;" data-ru="Вся сетка 15x15 заполняется цифрой 1 (непроходимая горная порода)." data-en="The entire 15x15 grid is filled with 1s (solid impassable rock).">Barcha 15x15 kataklar devor (1) bilan to'ldiriladi. Ichkarida hech qanday yo'l yo'q.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--accent);">
        <div class="tag" style="color:var(--accent);">2. Qazish</div>
        <h4 style="margin:6px 0;" data-ru="Шахтер Копает" data-en="Miner Digs">Konchi Yo'l O'yadi</h4>
        <p style="font-size:12px;" data-ru="Шахтер ставится в центр (startX, startY). Текущая клетка превращается в 0 (пол)." data-en="The miner spawns at center (startX, startY). Current tile is carved into 0 (floor).">Konchi markazga tushadi va turgan joyini yo'l (0) qiladi. Bu boshlang'ich nuqta bo'ladi.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--purple);">
        <div class="tag" style="color:var(--purple);">3. Tasodifiy Qadam</div>
        <h4 style="margin:6px 0;" data-ru="4 Направления" data-en="4 Directions">Tasodifiy Burilish</h4>
        <p style="font-size:12px;" data-ru="Выбирается случайное направление (Вверх, Вниз, Влево, Вправо) и делается шаг." data-en="A random direction (Up, Down, Left, Right) is chosen, stepping forward.">4 tomondan biri tasodifiy tanlanadi: Yuqoriga, Pastga, Chapga yoki O'ngga qadam bosiladi.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--green);">
        <div class="tag" style="color:var(--green);">4. Chiqish va Xazina</div>
        <h4 style="margin:6px 0;" data-ru="Размещение Целей" data-en="Goal Placement">Xazina va Chiqish</h4>
        <p style="font-size:12px;" data-ru="Последняя выкопанная клетка = Выход (E). Тупиковые коридоры = Сундуки (C)." data-en="Last carved tile becomes Exit (E). Dead-ends become Treasure Chests (C).">Eng oxirgi qazilgan nuqta = Chiqish eshigi. Berk ko'chalar = Oltin sandiqlar!</p>
      </div>
    </div>
    <div style="margin-top:12px; background:var(--surface-2); padding:8px 14px; border-radius:6px; font-size:12px; color:var(--ink-2); display:flex; justify-content:space-between; align-items:center;">
      <span data-ru="💡 Почему этот метод 100% проходим? Шахтер физически не может оторваться от выкопанного пути!" data-en="💡 Why is this 100% navigable? The miner physically never leaves the carved path!">💡 Nega bu usul 100% kafolatlangan? Chunki konchi faqat o'zi qadam bosgan uzluksiz yo'lni o'yadi!</span>
      <span class="badge" style="background:var(--green); color:#fff;" data-ru="100% Связный Путь" data-en="100% Connected Path">100% Uzluksiz Yo'l</span>
    </div>
  </section>

  <!-- SLIDE 5: RULES & BOUNDARIES -->
  <section class="slide" data-phase="Qoidalar|Правила|Rules" data-time="16:00–20:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="ПРАВИЛА БЕЗОПАСНОСТИ КАРТЫ" data-en="MAP INTEGRITY RULES">CHEGARALAR VA CHEKKA HOLATLAR</span></div>
    <h2 data-ru="3 Правила Лабиринта: Границы, Тупики и Выход" data-en="3 Rules of Maze Integrity: Borders, Dead-Ends & Exits">Labirintning 3 Oltin Qoidasi: Chegara, Berk Ko'cha va Chiqish</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);">1. Chegara Devori</div>
        <h4 data-ru="Не Выходить за Карту" data-en="Stay Within Bounds">Tashqariga Chiqmaslik</h4>
        <p style="font-size:12px;" data-ru="Координаты шахтера строго ограничены: <code>1 &lt;= x &lt; cols - 1</code>. Края карты всегда остаются стеной (1), иначе массив выдаст undefined." data-en="Miner coords are strictly bounded: <code>1 &lt;= x &lt; cols - 1</code>. Map edges always remain solid wall (1).">Konchi koordinatasi <code>1 &lt;= x &lt; cols - 1</code> bo'lishi shart. Eng chekka kataklar doim devor (1) bo'lib qoladi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(245,158,11,0.15); color:var(--amber);">2. Dead-End Qopqonlari</div>
        <h4 data-ru="Сундук в Тупике" data-en="Chests in Dead-Ends">Berk Ko'chalarga Sandiq</h4>
        <p style="font-size:12px;" data-ru="Если у клетки ровно 3 соседа — стены (1), значит это тупик! Идеальное место для золотого сундука или ключа." data-en="If a floor tile has exactly 3 wall neighbors (1), it's a dead-end! Perfect spot for treasure chests or keys.">Agar biror katakning 3 tomoni devor bo'lsa, bu berk ko'cha! U yerga xazina sandig'i qo'yiladi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">3. Chiqish Eshigi</div>
        <h4 data-ru="Финальная Точка" data-en="Final Destination">Eng Uzoq Chiqish</h4>
        <p style="font-size:12px;" data-ru="Выход помещается в самую последнюю точку пути. Это гарантирует максимальную длину прохождения подземелья." data-en="The exit portal is placed at the final carved location. This ensures the longest possible dungeon run.">Chiqish portali (Exit) qazishning eng oxirgi nuqtasiga qo'yiladi. Bu o'yinchi uchun eng uzun sarguzashtni ta'minlaydi.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px; background:var(--surface-2); font-family:var(--font-mono); font-size:11px;">
      <strong style="color:var(--accent);">Xaritadagi Belgilar Standarti:</strong><br>
      <code>0 = Bo'sh Yo'l (Floor)</code> · <code>1 = Tosh Devor (Wall)</code> · <code>P = O'yinchi (Player Spawn)</code> · <code>C = Oltin Sandiq (Chest)</code> · <code>E = Chiqish Portali (Exit)</code>
    </div>
  </section>

  <!-- SLIDE 6: CODE IMPLEMENTATION -->
  <section class="slide" data-phase="Kod Mexanizmi|Реализация в Коде|Code Mechanics" data-time="20:00–24:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ЧИСТЫЙ JAVASCRIPT КОД" data-en="CLEAN JAVASCRIPT CODE">GENERATOR FUNKSIYASI KODI</span></div>
    <h2 data-ru="Функция Генерации Подземелья на JavaScript" data-en="JavaScript Dungeon Generator Function">JavaScript-da generateDungeon() Generator Kodi</h2>
    <div class="grid-2">
      <div>
        <pre><code class="language-js">function generateDungeon(cols, rows, maxFloors) {
  // 1. To'liq devor bilan to'ldirish (1)
  const map = Array.from({ length: rows }, () => Array(cols).fill(1));

  let x = Math.floor(cols / 2);
  let y = Math.floor(rows / 2);
  map[y][x] = 0; // Spawn nuqtasi

  let carved = 1;
  const dirs = [
    { dx: 0, dy: -1 }, // Yuqori
    { dx: 0, dy: 1 },  // Past
    { dx: -1, dy: 0 }, // Chap
    { dx: 1, dy: 0 }   // O'ng
  ];

  while (carved < maxFloors) {
    const dir = dirs[Math.floor(Math.random() * dirs.length)];
    const nx = x + dir.dx;
    const ny = y + dir.dy;

    // Chegarani tekshirish (chekkada devor qolishi shart)
    if (nx > 0 && nx < cols - 1 && ny > 0 && ny < rows - 1) {
      x = nx;
      y = ny;
      if (map[y][x] === 1) {
        map[y][x] = 0;
        carved++;
      }
    }
  }
  return { map, exit: { x, y } };
}</code></pre>
      </div>
      <div>
        <h4 style="margin-bottom:6px; color:var(--accent);" data-ru="Как это работает шаг за шагом:" data-en="Step-by-step breakdown:">Kodning Qadamma-qadam Ishlashi:</h4>
        <ul class="clean-list" style="font-size:12px;">
          <li data-ru="<code>Array.from(..., fill(1))</code>: Создает 2D массив, полностью закрытый стенами (1)." data-en="<code>Array.from(..., fill(1))</code>: Initializes 2D array completely blocked with walls (1)."><strong>Massiv Yaratish:</strong> Barcha kataklar 1 (devor) qilinadi.</li>
          <li data-ru="<code>while (carved &lt; maxFloors)</code>: Шахтер копает, пока не откроет требуемое число ячеек пола." data-en="<code>while (carved &lt; maxFloors)</code>: Miner keeps tunneling until desired floor count is reached."><strong>Qazish Tsikli:</strong> Kerakli miqdordagi yo'l ochilguncha davom etadi.</li>
          <li data-ru="<code>if (map[y][x] === 1)</code>: Счетчик увеличивается только при сносе новой стены. Ходьба по старому полу не дублирует счет!" data-en="<code>if (map[y][x] === 1)</code>: Only uncarved rock increments floor count. Walking over old floor doesn't duplicate count!"><strong>Takrorlanishdan Himoya:</strong> Konchi eski yo'ldan o'tsa, <code>carved</code> ortmaydi. Faqat yangi devor ochilganda sanaladi!</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: IN-DECK INTERACTIVE SIMULATOR -->
  <section class="slide" data-phase="Jonli Sinov|Интерактив|Live Demo" data-time="24:00–28:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="СИМУЛЯТОР В ПРЕЗЕНТАЦИИ" data-en="IN-DECK SIMULATOR">SMARTBOARDDA JONLI GENERATOR</span></div>
    <h2 data-ru="Интерактивный Симулятор: Наблюдайте за Работой Шахтера" data-en="Interactive Studio: Watch the Miner Dig in Real-Time">Jonli Sinov: Mast Konchining Qazishini Kuzating!</h2>
    <div class="box" style="padding:12px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <div style="display:flex; gap:10px; align-items:center;">
          <button class="btn" onclick="deckStepMiner()" style="background:var(--accent); color:#fff; padding:6px 14px; font-size:12px;" data-ru="⛏️ 1 Шаг" data-en="⛏️ 1 Step">⛏️ 1 Qadam</button>
          <button class="btn" onclick="deckAutoDig()" id="btnDeckAuto" style="background:var(--green); color:#fff; padding:6px 14px; font-size:12px;" data-ru="⚡ Авто-Копка" data-en="⚡ Auto-Dig">⚡ Avto-Qazish</button>
          <button class="btn" onclick="deckResetMaze()" style="padding:6px 10px; font-size:12px;" data-ru="Сброс" data-en="Reset">Qayta Boshlash</button>
        </div>
        <div style="font-family:var(--font-mono); font-size:12px; color:var(--ink-2);">
          Qazilgan: <strong style="color:var(--green);" id="deckCarvedCount">1</strong> / 45 katak | Sandiqlar: <strong style="color:var(--amber);" id="deckChestCount">0</strong>
        </div>
      </div>
      <div style="display:flex; justify-content:center;">
        <canvas id="deckMazeCanvas" width="360" height="270" style="background:#000; border-radius:8px; border:1px solid var(--hair);"></canvas>
      </div>
      <div style="margin-top:8px; font-size:11px; color:var(--ink-2); display:flex; justify-content:space-between;">
        <span data-ru="🟢 Зеленый: Спавн | 🟡 Желтый: Шахтер | 📦 Золото: Сундук | 🚪 Красный: Выход" data-en="🟢 Green: Spawn | 🟡 Yellow: Miner | 📦 Gold: Chest | 🚪 Red: Exit">🟢 Yashil: Qahramon | 🟡 Sariq: Konchi | 📦 Oltin: Sandiq | 🚪 Qizil: Chiqish Portali</span>
        <span id="deckMazeStatus" style="color:var(--accent);" data-ru="Статус: Готов к генерации" data-en="Status: Ready">Status: Qazishga tayyor</span>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: INTERACTIVE QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Quiz" data-time="28:00–32:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА ЗНАНИЙ" data-en="KNOWLEDGE CHECK">3-SAVOLLI INTERAKTIV TEST</span></div>
    <h2 data-ru="Блиц-Тест: Процедурная Генерация и Random Walker" data-en="Fast Quiz: Procedural Generation & Random Walker">Bilimni Sinash: Procedural Dunyo va Random Walker</h2>
    <div class="quiz-container" style="display:flex; flex-direction:column; gap:12px;">
      <!-- Q1 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="1. Почему алгоритм Random Walker гарантирует 100% проходимость лабиринта?" data-en="1. Why does the Random Walker algorithm guarantee 100% maze navigability?">1. Nega Random Walker algoritmi o'tib bo'ladigan yo'lga 100% kafolat beradi?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! Konchi har qadamda o‘zidan oldingi yo‘lga tutash katakni o‘yadi.')" style="font-size:12px;" data-ru="A) Шахтер копает строго непрерывную цепочку клеток" data-en="A) The miner carves a strictly continuous chain of tiles">A) Konchi faqat uzluksiz tutash zanjir bo'ylab qaziydi</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri! Devorlarni buzuvchi bomba yo‘q.')" style="font-size:12px;" data-ru="B) Игрок может телепортироваться сквозь стены" data-en="B) The player can teleport through solid walls">B) Qahramon devorlarni teshib o'ta oladi</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Xarita to‘liq tasodifiy emas, qazish mantiqiga ega.')" style="font-size:12px;" data-ru="C) Все клетки открываются одновременно" data-en="C) All tiles are revealed simultaneously">C) Barcha kataklar birdaniga ochiladi</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
      <!-- Q2 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="2. Куда логичнее всего поместить выходной портал (Exit) из лабиринта?" data-en="2. Where is it most logical to place the dungeon exit portal?">2. Chiqish portalini (Exit) xaritaning qaysi joyiga qo'yish eng to'g'ri?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Spawn yoniga qo‘yilsa o‘yin darhol tugaydi!')" style="font-size:12px;" data-ru="A) Прямо рядом со спавном игрока" data-en="A) Directly adjacent to player spawn">A) Qahramon spawn bo'lgan nuqtaning yoniga</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'Aynan shunday! Bu eng uzoq va qiziqarli yo‘lni kafolatlaydi.')" style="font-size:12px;" data-ru="B) В самую последнюю точку, выкопанную шахтером" data-en="B) At the very last tile carved by the miner">B) Konchi qazigan eng oxirgi nuqtaga</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Devor ichiga qo‘yilsa unga yetib bo‘lmaydi.')" style="font-size:12px;" data-ru="C) В случайную невыкопанную стену" data-en="C) Inside an uncarved solid wall">C) Qazilmagan tosh devor ichiga</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
      <!-- Q3 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="3. Что произойдет, если разрешить шахтеру копать ячейки на самом краю (x = 0 или y = 0)?" data-en="3. What happens if the miner is allowed to dig edge tiles (x = 0 or y = 0)?">3. Agar konchiga xarita chekkasini (x = 0 yoki y = 0) qazishga ruxsat berilsa nima bo'ladi?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! Qahramon chetga chiqib undefined xatolik beradi.')" style="font-size:12px;" data-ru="A) Игрок может выпасть за границы массива (undefined)" data-en="A) Player may step outside array bounds (undefined)">A) Qahramon massiv chegarasidan chiqib undefined beradi</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Ranglar o‘zgarmaydi.')" style="font-size:12px;" data-ru="B) Экран станет черным" data-en="B) Screen turns completely black">B) Ekran o'chib qoladi</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'FPS ga ta‘siri yo‘q.')" style="font-size:12px;" data-ru="C) Скорость игры упадет" data-en="C) Game framerate drops">C) O'yin sekinlashadi</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: HANDS-ON ARENA -->
  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="32:00–37:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКАЯ МИССИЯ" data-en="HANDS-ON LAB MISSION">15 DAQIQALIK KIBER-ARENA</span></div>
    <h2 data-ru="Лаборатория: Запрограммируй Свой Генератор Подземелий" data-en="Lab Mission: Code Your Dungeon Generator">Kiber-Missiya: O'z Procedural Labirintingni Kodla</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:10px;" data-ru="Откройте симулятор simulator/index.html и запрограммируйте функцию генерации подземелья." data-en="Open simulator/index.html and program the procedural dungeon generation function.">Darsning <a href="simulator/index.html" target="_blank" style="color:var(--accent); font-weight:700;">simulator/index.html</a> ilovasini oching va procedural labirint generatorini ishga tushiring.</p>
        <ul class="clean-list">
          <li data-ru="<strong>1-Шаг:</strong> Создайте массив 15x15 со всеми стенами (1) и установите точку спавна (0)." data-en="<strong>Step 1:</strong> Build 15x15 array of walls (1) and place spawn tile (0)."><strong>1-Qadam:</strong> 15x15 o'lchamli devorlar massivini tuzing va spawn nuqtasini belgilang.</li>
          <li data-ru="<strong>2-Шаг:</strong> Запустите цикл копки на 45 клеток с проверкой границ." data-en="<strong>Step 2:</strong> Implement 45-step tunneling loop with boundary clamping."><strong>2-Qadam:</strong> Chegaralarni tekshirgan holda 45 ta yo'l katagini o'yuvchi sikl yozing.</li>
          <li data-ru="<strong>3-Шаг:</strong> Найдите тупики и поставьте в них минимум 2 сундука с сокровищами." data-en="<strong>Step 3:</strong> Detect dead-ends and spawn at least 2 treasure chests."><strong>3-Qadam:</strong> Berk ko'chalarni aniqlab, kamida 2 ta oltin sandiq va chiqish eshigini joylashtiring.</li>
        </ul>
      </div>
      <div class="box" style="border-left:4px solid var(--accent);">
        <h4 style="margin-bottom:8px;" data-ru="10-Балльная Рубрика Оценки:" data-en="10-Point Grading Rubric:">10 Ballik Baholash Mezoni:</h4>
        <div style="font-size:12px; line-height:1.8;">
          <div><strong style="color:var(--green);">4 Ball:</strong> Random Walker xaritani to'g'ri o'yadi, chegaralar buzilmaydi.</div>
          <div><strong style="color:var(--accent);">4 Ball:</strong> Chiqish eshigi (Exit) va kamida 2 ta sandiq to'g'ri joylashtiriladi.</div>
          <div><strong style="color:var(--purple);">2 Ball (Bonus):</strong> Qahramon klaviatura (WASD) orqali xaritada yurib sandiqlarni yig'a oladi!</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: TIERED HOMEWORK & SUMMARY -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Tiered Homework" data-time="37:00–40:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="SUMMARY & HOMEWORK">XULOSA VA 3 DARAJALI VAZIFA</span></div>
    <h2 data-ru="Итоги 31-Урока и Мост к Поиску Пути (Pathfinding)" data-en="Lesson 31 Recap & Bridge to Pathfinding AI">Xulosa va Keyingi Darsga Kiber-Ko'prik</h2>
    <div class="grid-3" style="gap:10px;">
      <div class="box" style="border-top:3px solid var(--green);">
        <div class="tag" style="color:var(--green);">1-Daraja: Baza (4 ball)</div>
        <h4 data-ru="Генератор 15x15" data-en="15x15 Generator">Baza Labirint Generator</h4>
        <p style="font-size:12px;" data-ru="Напишите функцию генерации 15x15 лабиринта с 40 выкопанными ячейками пола." data-en="Write a 15x15 maze generator with 40 carved floor tiles.">40 ta katakni o'yuvchi 15x15 o'lchamli labirint generatori funksiyasini yozing.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--accent);">
        <div class="tag" style="color:var(--accent);">2-Daraja: Loyiha (4 ball)</div>
        <h4 data-ru="Детектор Тупиков" data-en="Dead-End Detector">Berk Ko'chalar va Xazina</h4>
        <p style="font-size:12px;" data-ru="Автоматически найдите все ячейки с 3 стенами вокруг и превратите их в сундуки (2) и выход (3)." data-en="Automatically detect tiles with 3 adjacent walls and assign chests (2) and exit (3).">3 tomoni devor bo'lgan barcha berk ko'chalarni topib, ularga sandiqlar joylashtiring.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--purple);">
        <div class="tag" style="color:var(--purple);">3-Daraja: Challenge (2 ball)</div>
        <h4 data-ru="Инерция Шахтера" data-en="Directional Momentum">Konchi Inersiyasi</h4>
        <p style="font-size:12px;" data-ru="Добавьте инерцию: с шансом 60% шахтер продолжает идти в том же направлении, создавая длинные коридоры." data-en="Add momentum: 60% chance to persist in the current direction, forming longer corridors.">60% ehtimollik bilan konchi oldingi yo'nalishida davom etsin (uzunroq koridorlar hosil bo'ladi).</p>
      </div>
    </div>
    <div class="bridge-card" style="margin-top:12px; padding:10px 16px; border-radius:10px; background:rgba(147,51,234,0.08); border-left:4px solid var(--purple); display:flex; justify-content:space-between; align-items:center;">
      <div>
        <strong style="color:var(--purple);" data-ru="Следующий Шаг (AI & Pathfinding):" data-en="Next Step (AI & Pathfinding):">🚀 Keyingi Dars Ko'prigi:</strong>
        <span data-ru="Как враг найдет путь к игроку сквозь лабиринт? Алгоритмы поиска пути BFS и A*!" data-en="How will enemies hunt the player across procedural mazes? BFS & A* Pathfinding algorithms!">Dushman labirint ichida qahramonni qanday qilib topib quvadi? BFS va A* Pathfinding qidiruv algoritmlari!</span>
      </div>
      <a href="vazifa.html" class="btn" style="background:var(--purple); color:#fff; font-size:12px;" data-ru="Открыть ДЗ" data-en="Open HW">Vazifani Ochish ➔</a>
    </div>
  </section>
"""

# In-deck JS for Slide 7 interactive maze generator
IN_DECK_JS = """
// --- IN-DECK RANDOM WALKER SIMULATOR ---
var deckCols = 16;
var deckRows = 12;
var deckGrid = [];
var deckMiner = { x: 8, y: 6 };
var deckSpawn = { x: 8, y: 6 };
var deckExit = { x: 8, y: 6 };
var deckChests = [];
var deckCarved = 1;
var deckMaxFloors = 45;
var deckAutoTimer = null;

function deckInitMaze() {
  deckGrid = [];
  for (var r = 0; r < deckRows; r++) {
    var row = [];
    for (var c = 0; c < deckCols; c++) row.push(1);
    deckGrid.push(row);
  }
  deckMiner = { x: Math.floor(deckCols / 2), y: Math.floor(deckRows / 2) };
  deckSpawn = { x: deckMiner.x, y: deckMiner.y };
  deckExit = { x: deckMiner.x, y: deckMiner.y };
  deckChests = [];
  deckGrid[deckMiner.y][deckMiner.x] = 0;
  deckCarved = 1;
  document.getElementById('deckCarvedCount').textContent = deckCarved;
  document.getElementById('deckChestCount').textContent = '0';
  document.getElementById('deckMazeStatus').textContent = 'Status: Qazishga tayyor';
  deckDrawMaze();
}

function deckStepMiner() {
  if (deckCarved >= deckMaxFloors) {
    document.getElementById('deckMazeStatus').textContent = 'Status: Labirint to‘liq qazildi!';
    return false;
  }
  var dirs = [{dx:0, dy:-1}, {dx:0, dy:1}, {dx:-1, dy:0}, {dx:1, dy:0}];
  var d = dirs[Math.floor(Math.random() * dirs.length)];
  var nx = deckMiner.x + d.dx;
  var ny = deckMiner.y + d.dy;

  if (nx > 0 && nx < deckCols - 1 && ny > 0 && ny < deckRows - 1) {
    deckMiner.x = nx;
    deckMiner.y = ny;
    if (deckGrid[ny][nx] === 1) {
      deckGrid[ny][nx] = 0;
      deckCarved++;
      deckExit = { x: nx, y: ny };
      document.getElementById('deckCarvedCount').textContent = deckCarved;

      // Check for dead-end
      var walls = 0;
      dirs.forEach(function(di) {
        if (deckGrid[ny + di.dy][nx + di.dx] === 1) walls++;
      });
      if (walls === 3 && deckChests.length < 3 && Math.random() < 0.5) {
        deckChests.push({ x: nx, y: ny });
        document.getElementById('deckChestCount').textContent = deckChests.length;
      }
    }
  }
  deckDrawMaze();
  return true;
}

function deckAutoDig() {
  if (deckAutoTimer) {
    clearInterval(deckAutoTimer);
    deckAutoTimer = null;
    document.getElementById('btnDeckAuto').textContent = '⚡ Avto-Qazish';
    return;
  }
  document.getElementById('btnDeckAuto').textContent = '⏸️ To‘xtatish';
  document.getElementById('deckMazeStatus').textContent = 'Status: Qazilmoqda...';
  deckAutoTimer = setInterval(function() {
    var cont = deckStepMiner();
    if (!cont) {
      clearInterval(deckAutoTimer);
      deckAutoTimer = null;
      document.getElementById('btnDeckAuto').textContent = '⚡ Avto-Qazish';
    }
  }, 40);
}

function deckResetMaze() {
  if (deckAutoTimer) {
    clearInterval(deckAutoTimer);
    deckAutoTimer = null;
    document.getElementById('btnDeckAuto').textContent = '⚡ Avto-Qazish';
  }
  deckInitMaze();
}

function deckDrawMaze() {
  var canvas = document.getElementById('deckMazeCanvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var tileW = canvas.width / deckCols;
  var tileH = canvas.height / deckRows;

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (var r = 0; r < deckRows; r++) {
    for (var c = 0; c < deckCols; c++) {
      if (deckGrid[r][c] === 1) {
        ctx.fillStyle = '#1e293b'; // Wall
        ctx.fillRect(c * tileW, r * tileH, tileW, tileH);
        ctx.strokeStyle = '#0f172a';
        ctx.strokeRect(c * tileW, r * tileH, tileW, tileH);
      } else {
        ctx.fillStyle = '#0f172a'; // Floor
        ctx.fillRect(c * tileW, r * tileH, tileW, tileH);
      }
    }
  }

  // Chests
  deckChests.forEach(function(ch) {
    ctx.fillStyle = '#f59e0b';
    ctx.fillRect(ch.x * tileW + 4, ch.y * tileH + 4, tileW - 8, tileH - 8);
  });

  // Exit
  if (deckCarved >= deckMaxFloors) {
    ctx.fillStyle = '#ef4444';
    ctx.fillRect(deckExit.x * tileW + 3, deckExit.y * tileH + 3, tileW - 6, tileH - 6);
  }

  // Spawn
  ctx.fillStyle = '#10b981';
  ctx.fillRect(deckSpawn.x * tileW + 4, deckSpawn.y * tileH + 4, tileW - 8, tileH - 8);

  // Miner
  ctx.fillStyle = '#eab308';
  ctx.beginPath();
  ctx.arc(deckMiner.x * tileW + tileW/2, deckMiner.y * tileH + tileH/2, tileW/3, 0, Math.PI * 2);
  ctx.fill();
}

// Auto init on load
setTimeout(deckInitMaze, 400);

function checkQuiz(btn, isCorrect, feedbackText) {
  var parent = btn.closest('.box');
  var allBtns = parent.querySelectorAll('.quiz-btn');
  allBtns.forEach(function(b) {
    b.disabled = true;
    b.style.opacity = '0.6';
  });
  btn.style.opacity = '1';
  var fb = parent.querySelector('.quiz-feedback');
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

# Notes array for 10 slides
NOTES_DATA = {
    "uz": [
        ["Kirish va PCG", "O'quvchilarga bugungi dars mavzusi: Procedural Dunyo Generatsiyasi va Random Walker algoritmi haqida gapiring.", "Doskaga Minecraft va Hades misolini keltirib, darajalar qanday avtomatik yaratilishini ayting."],
        ["Uy Vazifasi Tahlili", "O'tgan darsdagi xato: statik 2D massivni kodga qotirib qo'yish o'yinni zerikarli qilib qo'yishini tushuntiring.", "Oltin yechim: har safar yangi dunyo yaratuvchi algoritm yozish ekanini ko'rsating."],
        ["PCG Falsafasi", "Procedural kontent generatsiyasi tushunchasini tushuntiring.", "Kichik kod hajmi va cheksiz qayta o'ynash (replayability) ustunligini ko'rsating."],
        ["Random Walker Qoidalari", "Mast konchi algoritmini 4 ta qadamga ajrating: tosh devor, konchi spawn, tasodifiy burilish, xazinalar.", "Nega bu labirintdan doim chiqish borligini matematik tushuntiring."],
        ["Chegaralar va Xazinalar", "Konchi xarita chekkasidagi devorni buzmasligi shartligini (1 <= x < cols-1) ta'kidlang.", "Berk ko'chalarga qanday qilib sandiqlar qo'yilishini doskada chizing."],
        ["Kod Mexanizmi", "generateDungeon() funksiyasini qatorma-qator tahlil qiling.", "dx va dy yo'nalishlar massivini tushuntirib bering."],
        ["Smartboardda Jonli Sinov", "Slayd ichidagi simulyatorda Avto-Qazish tugmasini bosing.", "Konchi qanday qilib yo'l ochayotgani va sandiqlar paydo bo'lishini ko'rsating."],
        ["Bilimni Sinash (Quiz)", "3 ta savol bo'yicha tezkor blitz o'tkazing.", "Noto'g'ri javoblarning sabablarini tahlil qiling."],
        ["Amaliy Missiya", "O'quvchilarga simulator/index.html ni ochishni buyuring.", "15 daqiqa ichida o'z generatorlarini yozishlarini nazorat qiling."],
        ["Xulosa va Keyingi Dars", "3 darajali uy vazifasini tushuntiring.", "Keyingi darsda labirint ichidagi dushman AI va Pathfinding algoritmlarini o'rganishimizni anons qiling!"]
    ],
    "ru": [
        ["Введение и PCG", "Представьте тему: процедурная генерация уровней и алгоритм Random Walker.", "Приведите примеры Minecraft и Spelunky, объясните бесконечную реиграбельность."],
        ["Разбор Домашнего Задания", "Разберите ошибку жестко прописанной статической матрицы, убивающей интерес к игре.", "Покажите золотой стандарт процедурного построения карты."],
        ["Философия PCG", "Объясните концепцию Procedural Content Generation.", "Подчеркните компактность кода и бесконечные вариации миров."],
        ["Алгоритм Random Walker", "Разберите 4 шага «пьяного шахтера»: стена, спавн, случайный шаг, размещение целей.", "Поясните гарантию 100% проходимости пути."],
        ["Границы и Сокровища", "Объясните запрет выхода за границы (1 <= x < cols-1).", "Покажите поиск тупиков для золотых сундуков."],
        ["Реализация в Коде", "Разберите построчно функцию generateDungeon().", "Объясните массив смещений dx и dy."],
        ["Интерактив на Доске", "Запустите генерацию в слайде, покажите работу шахтера.", "Продемонстрируйте появление сундуков и выхода."],
        ["Тест (Квиз)", "Проведите опрос по 3 контрольным вопросам.", "Разберите ошибки."],
        ["Практическая Лаборатория", "Дайте команду открыть simulator/index.html.", "Курируйте написание алгоритма генерации за 15 минут."],
        ["Итоги и Анонс", "Объясните 3 уровня домашнего задания.", "Анонсируйте следующую тему: искусственный интеллект врагов и поиск пути (Pathfinding)!"]
    ],
    "en": [
        ["Intro & PCG Concepts", "Introduce procedural world generation and the Random Walker algorithm.", "Discuss Minecraft & Hades level design to illustrate algorithmic generation."],
        ["Homework Review", "Explain why hardcoding static 2D matrices ruins replayability.", "Present the golden solution: dynamic algorithm-driven dungeons."],
        ["PCG Philosophy", "Clarify the core principles of Procedural Content Generation.", "Highlight microscopic file footprints and infinite variability."],
        ["Random Walker Steps", "Break down the 4 steps: solid fill, miner spawn, random turns, objective placement.", "Demonstrate mathematically why path connectivity is 100% guaranteed."],
        ["Boundaries & Loot", "Emphasize boundary constraints (1 <= x < cols-1) to prevent undefined errors.", "Illustrate dead-end detection for treasure chests."],
        ["Code Mechanics", "Walk students through generateDungeon() step-by-step.", "Clarify dx/dy offset vectors."],
        ["In-Deck Live Demo", "Trigger auto-dig on the interactive deck canvas.", "Show how rooms, dead-ends, and chests emerge dynamically."],
        ["Knowledge Check (Quiz)", "Lead the class through the 3 check questions.", "Explain each distractor."],
        ["Hands-on Lab Mission", "Instruct students to open simulator/index.html.", "Guide them through the 15-minute dungeon generation challenge."],
        ["Summary & Next Class", "Outline the 3-tiered homework assignment.", "Preview next week: enemy AI & pathfinding algorithms across procedural dungeons!"]
    ]
}

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "31-dars: Procedural Dunyo Generatsiyasi: Tasodifiy Labirintlar"
    title_ru = "Урок 31: Процедурная Генерация Мира: Случайные Лабиринты"
    title_en = "Lesson 31: Procedural World Generation: Random Mazes"

    # Replace <title>
    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    # Floating brand tag
    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="7–8 КЛАСС" data-en="GRADE 7–8">7–8-SINF</span>',
                 tpl)

    # Replace TITLES variable
    titles_json = json.dumps({"uz": title_uz, "ru": title_ru, "en": title_en}, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    # Replace NOTES variable
    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    # Replace stage content
    stage_regex = r'<div class="stage">[\s\S]*?</div><!-- /stage -->'
    new_stage = f'<div class="stage">\n{SLIDES_HTML}\n  </div><!-- /stage -->'
    tpl = re.sub(stage_regex, new_stage, tpl)

    # Inject in-deck simulator JS right before closing body or script end
    tpl = tpl.replace("</script>\n</body>", f"\n{IN_DECK_JS}\n</script>\n</body>")

    out_path = os.path.join(DEST_DIR, "prezentatsiya.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

# -----------------------------------------------------------------------------
# 2. WORKSHEET (varaqa.html)
# -----------------------------------------------------------------------------
def build_worksheet():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("{{COHORT_LABEL}}", "7–8-sinf")
    tpl = tpl.replace("{{WEEK_NUM}}", "11")
    tpl = tpl.replace("{{LESSON_NUM}}", "31")
    tpl = tpl.replace("{{TRACK_UZ}}", "Game Dev, Interaktiv Veb & FUT Creator Track")
    tpl = tpl.replace("{{TRACK_RU}}", "Game Dev, Интерактивный Веб & FUT Creator")
    tpl = tpl.replace("{{TRACK_EN}}", "Game Dev, Interactive Web & FUT Creator Track")
    tpl = tpl.replace("{{LESSON_TITLE_UZ}}", "Procedural Dunyo Generatsiyasi: Tasodifiy Labirintlar va Xazinalar")
    tpl = tpl.replace("{{LESSON_TITLE_RU}}", "Процедурная Генерация Мира: Случайные Лабиринты и Сокровища")
    tpl = tpl.replace("{{LESSON_TITLE_EN}}", "Procedural World Generation: Random Mazes & Treasures")

    sec1_html = """
    <p style="font-size:12px; line-height:1.5; margin-bottom:8px;" data-ru="В реальных играх уровни не рисуют вручную. Алгоритмы процедурной генерации (PCG) создают бесконечные уникальные лабиринты. Метод Random Walker моделирует шахтера, который копает непрерывные туннели, гарантируя проходимость." data-en="Modern roguelikes do not author maps manually. Procedural Content Generation (PCG) algorithms craft infinite unique dungeons. The Random Walker method models a tunneling miner guaranteeing complete path connectivity.">Zamonaviy o'yinlarda labirintlar qo'lda chizilmaydi. Procedural Kontent Generatsiyasi (PCG) cheksiz betakror labirintlar yaratadi. Random Walker algoritmi konchini modellashtirib, uzluksiz yo'l ochadi va doim o'tib bo'ladigan xarita beradi.</p>
    <div style="background:var(--surface-2); padding:6px 10px; border-radius:6px; font-size:11px; font-family:var(--font-mono); border-left:3px solid var(--accent);">
      <strong>Asosiy Standart:</strong> 2D Devor Massivi (1) + Random Walker (0) + Chegara Qoidasi (1 &lt;= x &lt; cols - 1) + Berk Ko'chalar (Dead-Ends) va Xazinalar.
    </div>
    """

    sec2_html = """
    <pre style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; font-family:var(--font-mono); line-height:1.4; border:1px solid var(--hair);"><code>// Random Walker Konchi Sikli
while (carved < targetFloors) {
  const dir = dirs[Math.floor(Math.random() * dirs.length)];
  const nx = x + dir.dx;
  const ny = y + dir.dy;
  if (nx > 0 && nx < cols - 1 && ny > 0 && ny < rows - 1) {
    x = nx; y = ny;
    if (grid[y][x] === 1) {
      grid[y][x] = 0; // Yo'l o'yildi
      carved++;
    }
  }
}</code></pre>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Элемент Карты" data-en="Map Element">Xarita Elementi</th>
            <th style="padding:4px 6px;" data-ru="Значение в Матрице" data-en="Matrix Value">Matritsa Qiymati</th>
            <th style="padding:4px 6px;" data-ru="Правило Размещения" data-en="Placement Rule">Joylashtirish Qoidasi</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="Tosh Devor (Wall)" data-en="Solid Wall">Tosh Devor (Wall)</td>
            <td style="padding:4px 6px;"><code>1</code></td>
            <td style="padding:4px 6px;" data-ru="Все непроходимые блоки" data-en="All impassable rock blocks">Barcha to'siq kataklar</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="Yo'l (Floor)" data-en="Carved Floor">Yo'l (Floor)</td>
            <td style="padding:4px 6px;"><code>0</code></td>
            <td style="padding:4px 6px;" data-ru="Выкопано шахтером" data-en="Carved by the miner">Konchi o'ygan ochiq yo'l</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="Xazina Sandig'i (Chest)" data-en="Treasure Chest">Xazina Sandig'i (Chest)</td>
            <td style="padding:4px 6px;"><code>2 (yoki C)</code></td>
            <td style="padding:4px 6px;" data-ru="Тупик (3 соседние стены)" data-en="Dead-end (3 wall neighbors)">Berk ko'cha (3 tomoni devor)</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="Chiqish Portali (Exit)" data-en="Exit Portal">Chiqish Portali (Exit)</td>
            <td style="padding:4px 6px;"><code>3 (yoki E)</code></td>
            <td style="padding:4px 6px;" data-ru="Самая последняя выкопанная клетка" data-en="The very last carved tile">Eng oxirgi qazilgan nuqta</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    sec4_html = """
    <p style="font-size:12px; margin-bottom:6px;" data-ru="Запустите генератор в симуляторе. Сгенерируйте подземелье на 50 ячеек. Запишите координаты спавна игрока и выхода:" data-en="Run the generator in the simulator. Generate a 50-tile dungeon. Record spawn and exit coordinates:">Simulyatorda generatorni ishga tushiring. 50 ta katakli labirint yarating. Qahramon spawn va chiqish koordinatalarini yozing:</p>
    <div style="border:1px dashed var(--hair); border-radius:6px; height:80px; padding:8px; font-family:var(--font-mono); font-size:11px; color:var(--ink-2);" data-ru="[Координаты спавна, выхода и количество найденных сундуков]" data-en="[Spawn coords, exit coords, and chests count]">
      // Boshlang'ich nuqta (Spawn): x = _______, y = _______<br>
      // Chiqish portali (Exit): x = _______, y = _______<br>
      // Topilgan oltin sandiqlar soni: _______ ta
    </div>
    """

    rubric_html = """
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px; font-size:11px;">
      <div style="border-left:3px solid var(--green); padding-left:6px;">
        <strong style="color:var(--green);" data-ru="4 Балла: База" data-en="4 Pts: Base">4 Ball: Baza</strong>
        <p style="margin:2px 0;" data-ru="Массив 15x15 заполнен стенами, Random Walker выкапывает 40 ячеек пола." data-en="15x15 array populated, Random Walker carves 40 floor tiles.">15x15 massiv yaratilgan, Random Walker 40 ta yo'l katagini o'yadi.</p>
      </div>
      <div style="border-left:3px solid var(--accent); padding-left:6px;">
        <strong style="color:var(--accent);" data-ru="4 Балла: Проект" data-en="4 Pts: Project">4 Ball: Loyiha</strong>
        <p style="margin:2px 0;" data-ru="Размещены точка выхода (Exit) и сундуки в тупиках, карта отрисована на Canvas." data-en="Exit and chests placed in dead-ends, rendered to Canvas.">Chiqish portali va berk ko'chalarda sandiqlar joylashtirilgan.</p>
      </div>
      <div style="border-left:3px solid var(--purple); padding-left:6px;">
        <strong style="color:var(--purple);" data-ru="2 Балла: Challenge" data-en="2 Pts: Challenge">2 Ball: Challenge</strong>
        <p style="margin:2px 0;" data-ru="Управление игроком с клавиатуры (WASD) и сбор сундуков со счетчиком очков." data-en="Keyboard controls (WASD) and collecting chests with score tracking.">Qahramon harakati (WASD) va sandiqlarni terish mexanikasi ishlaydi.</p>
      </div>
    </div>
    """

    tpl = tpl.replace("{{SEC1_CONTENT}}", sec1_html)
    tpl = tpl.replace("{{SEC2_CONTENT}}", sec2_html)
    tpl = tpl.replace("{{SEC3_CONTENT}}", sec3_html)
    tpl = tpl.replace("{{SEC4_CONTENT}}", sec4_html)
    tpl = tpl.replace("{{RUBRIC_CONTENT}}", rubric_html)

    out_path = os.path.join(DEST_DIR, "varaqa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: varaqa.html")

# -----------------------------------------------------------------------------
# 3. INTERACTIVE HOMEWORK (vazifa.html)
# -----------------------------------------------------------------------------
def build_homework():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("{{COHORT_LABEL}}", "7–8-sinf")
    tpl = tpl.replace("{{WEEK_NUM}}", "11")
    tpl = tpl.replace("{{LESSON_NUM}}", "31")
    tpl = tpl.replace("{{TRACK_UZ}}", "Game Dev, Interaktiv Veb & FUT Creator Track")
    tpl = tpl.replace("{{TRACK_RU}}", "Game Dev, Интерактивный Веб & FUT Creator")
    tpl = tpl.replace("{{TRACK_EN}}", "Game Dev, Interactive Web & FUT Creator Track")
    tpl = tpl.replace("{{LESSON_TITLE_UZ}}", "Procedural Dunyo Generatsiyasi: Tasodifiy Labirintlar va Xazinalar")
    tpl = tpl.replace("{{LESSON_TITLE_RU}}", "Процедурная Генерация Мира: Случайные Лабиринты и Сокровища")
    tpl = tpl.replace("{{LESSON_TITLE_EN}}", "Procedural World Generation: Random Mazes & Treasures")
    tpl = tpl.replace("{{TOTAL_TASKS}}", "3")

    tasks_html = """
  <!-- 1-DARAJA: BAZA -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-1" data-ru="1-Уровень: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Базовый Алгоритм Random Walker" data-en="Basic Random Walker Function">Baza Random Walker Generator Funksiyasi</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Напишите функцию <code>createMaze(cols, rows, floorCount)</code>, которая создает 2D массив, заполненный единицами (стенами), и выкапывает ровно <code>floorCount</code> ячеек пола (нули), не выходя за пределы границ карты." data-en="Write <code>createMaze(cols, rows, floorCount)</code> that initializes a 2D array of 1s (walls) and carves exactly <code>floorCount</code> floor tiles (0s) within boundaries.">1 lar (devorlar) bilan to'ldirilgan 2D massiv yaratuvchi va xarita chegarasidan chiqmasdan roppa-rosa <code>floorCount</code> ta yo'l katagini (0) o'yuvchi <code>createMaze(cols, rows, floorCount)</code> funksiyasini yozing.</p>
    <textarea class="answer-area" id="ans_task_1" rows="7" placeholder="JavaScript kodingizni bu yerga yozing..." data-placeholder-ru="Напишите ваш код здесь..." data-placeholder-en="Write your code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_1">
      <strong style="color:var(--green);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>function createMaze(cols, rows, floorCount) {
  const map = Array.from({ length: rows }, () => Array(cols).fill(1));
  let x = Math.floor(cols / 2), y = Math.floor(rows / 2);
  map[y][x] = 0;
  let carved = 1;
  const dirs = [{dx:0,dy:-1},{dx:0,dy:1},{dx:-1,dy:0},{dx:1,dy:0}];

  while (carved < floorCount) {
    const d = dirs[Math.floor(Math.random() * dirs.length)];
    const nx = x + d.dx, ny = y + d.dy;
    if (nx > 0 && nx < cols - 1 && ny > 0 && ny < rows - 1) {
      x = nx; y = ny;
      if (map[y][x] === 1) {
        map[y][x] = 0;
        carved++;
      }
    }
  }
  return map;
}</code></pre>
    </div>
  </div>

  <!-- 2-DARAJA: AMALIYOT -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-2" data-ru="2-Уровень: Проект (4 балла)" data-en="Tier 2: Project (4 pts)">2-Daraja: Amaliyot (4 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Поиск Тупиков и Размещение Сундуков" data-en="Dead-End Detection & Chest Spawning">Berk Ko'chalarni Topish va Xazinalar Joylashtirish</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Напишите функцию <code>placeChests(map)</code>, которая обходит карту, находит все ячейки пола (0), у которых ровно 3 соседа являются стенами (1), и превращает их в сундуки со значением 2." data-en="Write <code>placeChests(map)</code> that iterates over the grid, finds all floor tiles (0) with exactly 3 wall neighbors (1), and marks them as chests with value 2.">Xaritani tekshirib, aynan 3 tomoni devor (1) bo'lgan barcha berk ko'chalarni topuvchi va ularni qiymati 2 bo'lgan xazina sandig'iga aylantiruvchi <code>placeChests(map)</code> funksiyasini yozing.</p>
    <textarea class="answer-area" id="ans_task_2" rows="8" placeholder="placeChests kodingizni bu yerga yozing..." data-placeholder-ru="Напишите код поиска тупиков здесь..." data-placeholder-en="Write dead-end detector code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_2">
      <strong style="color:var(--accent);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>function placeChests(map) {
  const rows = map.length;
  const cols = map[0].length;
  const dirs = [{dx:0,dy:-1},{dx:0,dy:1},{dx:-1,dy:0},{dx:1,dy:0}];
  let chestCount = 0;

  for (let r = 1; r < rows - 1; r++) {
    for (let c = 1; c < cols - 1; c++) {
      if (map[r][c] === 0) {
        let walls = 0;
        dirs.forEach(d => {
          if (map[r + d.dy][c + d.dx] === 1) walls++;
        });
        if (walls === 3) {
          map[r][c] = 2; // Sandiq qo'yildi
          chestCount++;
        }
      }
    }
  }
  return { map, chestCount };
}</code></pre>
    </div>
  </div>

  <!-- 3-DARAJA: CHALLENGE -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-3" data-ru="3-Уровень: Challenge (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Инерция Шахтера: Генерация Длинных Коридоров" data-en="Miner Momentum: Corridors vs Blobs">Konchi Inersiyasi: Uzun Koridorlar Generatsiyasi</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Обычный Random Walker часто топчется на месте, создавая круглые кляксы. Модифицируйте алгоритм: с вероятностью 70% шахтер должен сохранять предыдущее направление движения, создавая красивые длинные коридоры." data-en="Pure Random Walker often turns in place creating circular blobs. Modify the algorithm: with 70% probability the miner persists in its previous direction, generating realistic long corridors.">Oddiy Random Walker bir joyda aylanib doira hosil qilib qo'yishi mumkin. Algoritmga inersiya qo'shing: 70% ehtimollik bilan konchi oldingi yo'nalishida davom etsin, natijada chiroyli uzun koridorlar hosil bo'lsin.</p>
    <textarea class="answer-area" id="ans_task_3" rows="8" placeholder="Inersiya kodingizni bu yerga yozing..." data-placeholder-ru="Напишите код с инерцией здесь..." data-placeholder-en="Write momentum code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_3">
      <strong style="color:var(--purple);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>function createCorridorDungeon(cols, rows, maxFloors) {
  const map = Array.from({ length: rows }, () => Array(cols).fill(1));
  let x = Math.floor(cols / 2), y = Math.floor(rows / 2);
  map[y][x] = 0;
  let carved = 1;
  const dirs = [{dx:0,dy:-1},{dx:0,dy:1},{dx:-1,dy:0},{dx:1,dy:0}];
  let lastDir = dirs[0];

  while (carved < maxFloors) {
    // 70% inersiya: oldingi yo'nalishda davom etish
    let dir = (Math.random() < 0.7) ? lastDir : dirs[Math.floor(Math.random() * dirs.length)];
    const nx = x + dir.dx, ny = y + dir.dy;

    if (nx > 0 && nx < cols - 1 && ny > 0 && ny < rows - 1) {
      x = nx; y = ny;
      lastDir = dir;
      if (map[y][x] === 1) {
        map[y][x] = 0;
        carved++;
      }
    } else {
      // Devorga urilsa majburiy yangi yo'nalish
      lastDir = dirs[Math.floor(Math.random() * dirs.length)];
    }
  }
  return map;
}</code></pre>
    </div>
  </div>
    """

    tpl = tpl.replace("{{TASKS_CONTENT}}", tasks_html)
    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

# -----------------------------------------------------------------------------
# 4. TEACHER READING GUIDE (TEACHER_READING.md)
# -----------------------------------------------------------------------------
def build_teacher_reading():
    content = """# 7–8-sinf, 11-hafta, 31-dars: O'qituvchi Qo'llanmasi
## Procedural Dunyo Generatsiyasi: Tasodifiy Labirintlar va Xazinalar

### Dars Haqida Ma'lumot:
- **Kohorta:** 7–8-sinf (Game Dev, Interaktiv Veb & FUT Creator Track)
- **Format:** 40 daqiqalik Yakka Dars (Single Block)
- **Asosiy maqsad:** O'quvchilarga procedural dunyo generatsiyasi (PCG) tushunchasini o'rgatish, Random Walker (Mast konchi) algoritmi orqali doimo o'tib bo'ladigan xaritalar yasash, chegaralarni himoyalash va berk ko'chalarga xazinalar joylashtirish.

---

### 40 Daqiqalik Dars Pacing Xaritasi:

| Vaqt | Bosqich | Slayd | O'qituvchi Harakati | Kutiladigan Natija |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va PCG | 1 | Dars mavzusini e'lon qilish, Minecraft va Hades qanday qilib darajalarni avtomatik yasashini aytish. | O'quvchilar PCG ning o'yinlardagi ahamiyatini tushunishadi. |
| **04:00–08:00** | O'tgan Dars HW Tahlili | 2 | 30-darsdagi statik 2D massiv xatosini tahlil qilish. Blitz savoli. | O'quvchilar nega statik xaritalar zerikarli bo'lib qolishini anglaydilar. |
| **08:00–12:00** | PCG Falsafasi | 3 | Replayability va kichik fayl hajmi ustunliklarini doskada tushuntirish. | Algoritmik dunyo yaratish tamoyillari o'zlashtiriladi. |
| **12:00–16:00** | Random Walker Qadamlari | 4 | 4 ta qadam: 1 bilan to'ldirish, konchi spawn, tasodifiy burilish, xazinalar. Nega bu yo'l 100% bog'liq ekanini ko'rsatish. | Random Walker qoidalari o'rganiladi. |
| **16:00–20:00** | Chegaralar va Berk Ko'chalar | 5 | Chegaradan chiqmaslik sharti (1 &lt;= x &lt; cols - 1) va berk ko'cha (dead-end) tushunchasini chizib berish. | Sandiqlar va chiqish eshigi qayerga qo'yilishi tushuniladi. |
| **20:00–24:00** | Kod Mexanizmi | 6 | `generateDungeon()` kodini qatorma-qator tahlil qilish, `dx/dy` yo'nalishlar massivini ko'rsatish. | JavaScript generator sintaksisi o'rganiladi. |
| **24:00–28:00** | Jonli Smartboard Demo | 7 | Slayd ichidagi simulyatorda Avto-Qazish tugmasini bosib, konchining real-vaqtda yo'l ochishini ko'rsatish. | Vizual idrok mustahkamlanadi. |
| **28:00–32:00** | Bilimni Sinash (Quiz) | 8 | 3 ta savol bo'yicha interaktiv viktorina o'tkazish. | O'quvchilar tushunchalari mustahkamlanadi. |
| **32:00–37:00** | 15 Daqiqalik Arena | 9 | `simulator/index.html` ilovasida o'quvchilarga o'z generatorlarini yozishni buyurish. | Har bir o'quvchi o'z labirintini generatsiya qiladi. |
| **37:00–40:00** | Baholash va Keyingi Dars | 10 | 10 ballik mezonni e'lon qilish, 3 darajali uy vazifasini tushuntirish va dushman AI mavzusiga ko'prik. | Uy vazifasi tushuniladi. |

---

### Keng Tarqalgan Savollar va Pedagogik Ko'rsatmalar:
1. **"Nega konchi xaritadan chiqib ketmasligi kerak?"**
   - Javob: Agar konchi `x < 0` yoki `x >= cols` bo'lib qolsa, JavaScript `map[y][x]` da `undefined` xatolik beradi va o'yin qotib qoladi.
2. **"Dead-end (berk ko'cha) qanday aniqlanadi?"**
   - Javob: Katakning 4 ta qo'shnisi tekshiriladi: agar 3 tasi devor (1) bo'lsa va faqat bittasi yo'l (0) bo'lsa, bu katak berk ko'cha hisoblanadi. O'yinda o'yinchi berk ko'chaga borganda mukofot olishi uchun u yerga oltin sandiq qo'yiladi!
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Created: TEACHER_READING.md")

# -----------------------------------------------------------------------------
# 5. STANDALONE SIMULATOR (simulator/index.html)
# -----------------------------------------------------------------------------
def build_simulator():
    sim_html = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title data-ru="Procedural Лабиринт Студия — 7–8 Класс" data-en="Procedural Dungeon Studio — Grade 7–8">Procedural Labirint Studiyasi — 7–8-Sinf</title>
  <link rel="stylesheet" href="../../../../assets/brand.css" />
  <style>
    :root {
      --bg: #090d16;
      --surface: #111827;
      --surface-2: #1f293d;
      --hair: #374151;
      --ink: #f3f4f6;
      --ink-2: #9ca3af;
      --accent: #3b82f6;
      --green: #10b981;
      --red: #ef4444;
      --amber: #f59e0b;
      --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
    }
    body {
      margin: 0;
      padding: 20px;
      background: var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    .header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--hair);
    }
    .btn {
      padding: 8px 16px;
      border-radius: 6px;
      border: 1px solid var(--hair);
      background: var(--surface-2);
      color: var(--ink);
      cursor: pointer;
      font-weight: 600;
      font-size: 13px;
      transition: all 0.15s ease;
    }
    .btn:hover { filter: brightness(1.1); }
    .btn-accent { background: var(--accent); color: #fff; border-color: var(--accent); }
    .btn-green { background: var(--green); color: #fff; border-color: var(--green); }
    .canvas-container {
      display: flex;
      gap: 20px;
    }
    canvas {
      background: #000;
      border-radius: 8px;
      border: 2px solid var(--hair);
    }
    .panel {
      flex: 1;
      background: var(--surface);
      border: 1px solid var(--hair);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .stat-row {
      display: flex;
      justify-content: space-between;
      padding: 8px 10px;
      background: var(--surface-2);
      border-radius: 6px;
      font-size: 13px;
    }
    .lang-btn {
      padding: 4px 10px;
      border-radius: 6px;
      background: transparent;
      border: 1px solid var(--hair);
      color: var(--ink-2);
      font-size: 12px;
      cursor: pointer;
    }
    .lang-btn.active {
      background: var(--accent);
      color: #fff;
      border-color: var(--accent);
    }
  </style>
</head>
<body>

  <div class="header-bar">
    <div>
      <h2 style="margin:0 0 4px 0;" data-ru="Procedural Генератор Подземелий" data-en="Procedural Dungeon Generator">Procedural Labirint va Dunyo Studiyasi</h2>
      <span style="font-size:12px; color:var(--ink-2);" data-ru="7–8-Класс · 11-Неделя · 31-Урок · Алгоритм Random Walker и поиск тупиков" data-en="Grade 7–8 · Week 11 · Lesson 31 · Random Walker Algorithm & Dead-End Mining">7–8-Sinf · 11-Hafta · 31-Dars · Random Walker algoritmi va xazinalarni joylashtirish</span>
    </div>
    <div style="display:flex; gap:10px; align-items:center;">
      <div style="display:flex; gap:4px;">
        <button class="lang-btn active" onclick="setLang('uz')">UZ</button>
        <button class="lang-btn" onclick="setLang('ru')">RU</button>
        <button class="lang-btn" onclick="setLang('en')">EN</button>
      </div>
    </div>
  </div>

  <div style="margin-bottom:16px; display:flex; gap:10px; align-items:center;">
    <button class="btn btn-accent" onclick="startGeneration()" data-ru="⚡ Сгенерировать Новый Мир" data-en="⚡ Generate New Dungeon">⚡ Yangi Dunyo Generatsiyasi</button>
    <button class="btn btn-green" onclick="toggleAutoDig()" id="btnAutoDig" data-ru="⛏️ Пошаговая Копка" data-en="⛏️ Step-by-Step Dig">⛏️ Qadamma-qadam Qazish</button>
    <button class="btn" onclick="resetDungeon()" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta O'rnatish</button>
    <span style="font-size:12px; color:var(--ink-2); margin-left:auto;" data-ru="🎮 Управление игроком: Клавиши W, A, S, D или стрелки" data-en="🎮 Player controls: WASD or arrow keys">🎮 Qahramonni boshqarish: WASD yoki strelkalar</span>
  </div>

  <div class="canvas-container">
    <canvas id="gameCanvas" width="480" height="360"></canvas>
    
    <div class="panel">
      <h3 style="margin:0;" data-ru="Параметры Лабиринта" data-en="Dungeon Metrics">Labirint Ko'rsatkichlari</h3>
      <div class="stat-row">
        <span data-ru="Размер Сетки:" data-en="Grid Size:">Matritsa O'lchami:</span>
        <strong id="statGrid">20 x 15 (300 katak)</strong>
      </div>
      <div class="stat-row">
        <span data-ru="Выкопано Пола:" data-en="Floor Tiles Carved:">Qazilgan Yo'l Kataklari:</span>
        <strong style="color:var(--green);" id="statFloors">0 / 80</strong>
      </div>
      <div class="stat-row">
        <span data-ru="Сундуков Найдено:" data-en="Chests Discovered:">Oltin Sandiqlar:</span>
        <strong style="color:var(--amber);" id="statChests">0 ta</strong>
      </div>
      <div class="stat-row">
        <span data-ru="Счет Игрока:" data-en="Player Score:">Qahramon Balli:</span>
        <strong style="color:var(--accent);" id="statScore">0 Ball</strong>
      </div>

      <div style="margin-top:auto; background:var(--surface-2); padding:10px; border-radius:8px; font-size:12px; line-height:1.5; color:var(--ink-2);">
        <strong style="color:var(--ink);" data-ru="Правила Прохождения:" data-en="Dungeon Rules:">O'yin Qoidalari:</strong><br>
        <span data-ru="🟢 Зеленый: Начало (Spawn)<br>🟡 Желтый: Шахтер<br>📦 Оранжевый: Сундуки (+10 очков)<br>🚪 Красный: Портал Выхода (Победа!)" data-en="🟢 Green: Start (Spawn)<br>🟡 Yellow: Miner<br>📦 Orange: Chests (+10 pts)<br>🚪 Red: Exit Portal (Victory!)">🟢 Yashil: Qahramon (Spawn)<br>🟡 Sariq: Konchi<br>📦 Oltin: Sandiqlar (+10 ball)<br>🚪 Qizil: Chiqish Portali (G'alaba!)</span>
      </div>
    </div>
  </div>

  <script>
    var currentLang = 'uz';
    var canvas = document.getElementById('gameCanvas');
    var ctx = canvas.getContext('2d');
    var cols = 20;
    var rows = 15;
    var tileW = canvas.width / cols;
    var tileH = canvas.height / rows;

    var grid = [];
    var miner = { x: 10, y: 7 };
    var player = { x: 10, y: 7 };
    var spawn = { x: 10, y: 7 };
    var exit = { x: 10, y: 7 };
    var chests = [];
    var targetFloors = 80;
    var carvedCount = 0;
    var score = 0;
    var autoTimer = null;

    function setLang(lang) {
      currentLang = lang;
      document.querySelectorAll('.lang-btn').forEach(function(b) {
        b.classList.toggle('active', b.textContent.toLowerCase() === lang);
      });
      document.querySelectorAll('[data-' + lang + ']').forEach(function(el) {
        el.textContent = el.getAttribute('data-' + lang);
      });
    }

    function initDungeon() {
      grid = [];
      for (var r = 0; r < rows; r++) {
        var row = [];
        for (var c = 0; c < cols; c++) row.push(1);
        grid.push(row);
      }
      miner = { x: Math.floor(cols / 2), y: Math.floor(rows / 2) };
      player = { x: miner.x, y: miner.y };
      spawn = { x: miner.x, y: miner.y };
      exit = { x: miner.x, y: miner.y };
      chests = [];
      grid[miner.y][miner.x] = 0;
      carvedCount = 1;
      score = 0;
      updateStats();
      draw();
    }

    function stepDig() {
      if (carvedCount >= targetFloors) return false;
      var dirs = [{dx:0,dy:-1},{dx:0,dy:1},{dx:-1,dy:0},{dx:1,dy:0}];
      var d = dirs[Math.floor(Math.random() * dirs.length)];
      var nx = miner.x + d.dx;
      var ny = miner.y + d.dy;

      if (nx > 0 && nx < cols - 1 && ny > 0 && ny < rows - 1) {
        miner.x = nx;
        miner.y = ny;
        if (grid[ny][nx] === 1) {
          grid[ny][nx] = 0;
          carvedCount++;
          exit = { x: nx, y: ny };

          // Dead end check
          var walls = 0;
          dirs.forEach(function(di) {
            if (grid[ny + di.dy][nx + di.dx] === 1) walls++;
          });
          if (walls === 3 && chests.length < 5 && Math.random() < 0.6) {
            chests.push({ x: nx, y: ny });
          }
        }
      }
      updateStats();
      draw();
      return true;
    }

    function startGeneration() {
      resetDungeon();
      while (carvedCount < targetFloors) {
        stepDig();
      }
    }

    function toggleAutoDig() {
      if (autoTimer) {
        clearInterval(autoTimer);
        autoTimer = null;
        document.getElementById('btnAutoDig').textContent = '⛏️ Qadamma-qadam Qazish';
      } else {
        document.getElementById('btnAutoDig').textContent = '⏸️ To‘xtatish';
        autoTimer = setInterval(function() {
          var ok = stepDig();
          if (!ok) {
            clearInterval(autoTimer);
            autoTimer = null;
            document.getElementById('btnAutoDig').textContent = '⛏️ Qadamma-qadam Qazish';
          }
        }, 30);
      }
    }

    function resetDungeon() {
      if (autoTimer) {
        clearInterval(autoTimer);
        autoTimer = null;
        document.getElementById('btnAutoDig').textContent = '⛏️ Qadamma-qadam Qazish';
      }
      initDungeon();
    }

    function updateStats() {
      document.getElementById('statFloors').textContent = carvedCount + ' / ' + targetFloors;
      document.getElementById('statChests').textContent = chests.length + ' ta';
      document.getElementById('statScore').textContent = score + ' Ball';
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      for (var r = 0; r < rows; r++) {
        for (var c = 0; c < cols; c++) {
          if (grid[r][c] === 1) {
            ctx.fillStyle = '#1e293b';
            ctx.fillRect(c * tileW, r * tileH, tileW, tileH);
            ctx.strokeStyle = '#0f172a';
            ctx.strokeRect(c * tileW, r * tileH, tileW, tileH);
          } else {
            ctx.fillStyle = '#0f172a';
            ctx.fillRect(c * tileW, r * tileH, tileW, tileH);
          }
        }
      }

      // Exit
      if (carvedCount >= targetFloors) {
        ctx.fillStyle = '#ef4444';
        ctx.fillRect(exit.x * tileW + 4, exit.y * tileH + 4, tileW - 8, tileH - 8);
      }

      // Chests
      chests.forEach(function(ch) {
        ctx.fillStyle = '#f59e0b';
        ctx.fillRect(ch.x * tileW + 5, ch.y * tileH + 5, tileW - 10, tileH - 10);
      });

      // Player
      ctx.fillStyle = '#10b981';
      ctx.beginPath();
      ctx.arc(player.x * tileW + tileW/2, player.y * tileH + tileH/2, tileW/3, 0, Math.PI * 2);
      ctx.fill();

      // Miner (if still digging)
      if (carvedCount < targetFloors) {
        ctx.fillStyle = '#eab308';
        ctx.beginPath();
        ctx.arc(miner.x * tileW + tileW/2, miner.y * tileH + tileH/2, tileW/4, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    window.addEventListener('keydown', function(e) {
      var dx = 0, dy = 0;
      if (e.key === 'ArrowUp' || e.key === 'w' || e.key === 'W') dy = -1;
      else if (e.key === 'ArrowDown' || e.key === 's' || e.key === 'S') dy = 1;
      else if (e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') dx = -1;
      else if (e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') dx = 1;
      else return;

      var nx = player.x + dx;
      var ny = player.y + dy;

      if (nx >= 0 && nx < cols && ny >= 0 && ny < rows && grid[ny][nx] === 0) {
        player.x = nx;
        player.y = ny;

        // Collect chest
        for (var i = chests.length - 1; i >= 0; i--) {
          if (chests[i].x === nx && chests[i].y === ny) {
            chests.splice(i, 1);
            score += 10;
            updateStats();
          }
        }

        // Win condition
        if (carvedCount >= targetFloors && nx === exit.x && ny === exit.y) {
          alert('🎉 TABRIKLAYMIZ! Siz procedural labirintdan chiqishga muvaffaq bo‘ldingiz! Jami ball: ' + (score + 20));
        }

        draw();
      }
    });

    initDungeon();
  </script>
</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "simulator", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(sim_html)
    print("  ✓ Created: simulator/index.html")

def main():
    print("📦 Building 7–8-sinf (Lesson 31: Procedural Dunyo Generatsiyasi)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_simulator()
    print("🎉 Done! Generated Grade 7–8 Lesson 31.")

if __name__ == "__main__":
    main()
