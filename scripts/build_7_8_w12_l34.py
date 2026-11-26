#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_7_8_w12_l34.py — Builder for 7–8th Grade, Week 12, Lesson 34

Mavzu: Dushman AI va Pathfinding: To'siqlarni Aylanib Quvish va BFS Qidiruv Algoritmi
Format: Yakka Dars (40 daqiqa), 10 slayd
Kohorta: 7-8-sinf (Game Dev, Interaktiv Veb & FUT Creator Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "7-8-sinf", "12-hafta", "34-dars-dushman-ai-va-pathfinding")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "simulator"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (10 Slides for 40-min Single Block)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="7–8-КЛАСС · 12-Я НЕДЕЛЯ · УРОК 34" data-en="GRADES 7–8 · WEEK 12 · LESSON 34">7–8-SINF · 12-HAFTA · 34-DARS</span></div>
    <h1 class="display" data-ru="ИИ Врагов и Pathfinding: Обход Препятствий и Поиск BFS" data-en="Enemy AI & Pathfinding: Obstacle Avoidance & BFS Search">Dushman AI va Pathfinding: To'siqlarni Aylanib Quvish va BFS Qidiruv</h1>
    <p class="lede" data-ru="Делаем врагов по-настоящему умными в Canvas 2D: почему прямолинейное преследование застревает в стенах, как граф сетки рассчитывает кратчайший путь через BFS, восстанавливает маршрут и держит стабильные 60 FPS." data-en="Making enemies truly intelligent in Canvas 2D: why naive tracking gets stuck on walls, how grid graphs calculate shortest paths via BFS, reconstruct waypoints, and maintain a rock-solid 60 FPS.">Canvas 2D-da dushmanlarni chinakam aqlli qilish: nega oddiy quvish devorga botib qoladi, qanday qilib BFS algoritmi labirintdagi eng qisqa yo'lni topadi va barqaror 60 FPS tezlikni ta'minlaydi.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">40 daqiqalik Yakka Dars</div>
        <h3 data-ru="Алгоритм BFS" data-en="BFS Algorithm">To'lqinsimon Qidiruv</h3>
        <p data-ru="Очередь FIFO и поиск в ширину (Breadth-First Search) как фундамент искусственного интеллекта в Pac-Man и Roguelike." data-en="FIFO queues and Breadth-First Search (BFS) as the foundational AI logic behind Pac-Man and Roguelike games.">FIFO navbati va kenglik bo'yicha qidiruv: Pac-Man va roguelike o'yinlaridagi sun'iy intellekt asosi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">AI Pathfinding Arena</div>
        <h3 data-ru="Умный Дроид" data-en="Smart AI Bot">Aqlli Kiber-Dushman</h3>
        <p data-ru="Каждый ученик запрограммирует вражеского бота, способного обойти любые лабиринты и настичь игрока." data-en="Each student programs an autonomous enemy bot capable of navigating complex mazes to hunt the player.">Har bir o'quvchi har qanday devorlarni aylanib o'tib, o'yinchini ta'qib qiluvchi aqlli dushman botini yaratadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–08:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 33-УРОКА" data-en="LESSON 33 HOMEWORK REVIEW">33-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="GTA 2D Cyber City: Враги Застревают в Стенах и Слепое Движение" data-en="GTA 2D Cyber City: Enemies Getting Stuck In Walls & Blind Motion">33-Darsdagi Keng Tarqalgan Xato: Dushmanlarning Devorga Botib Qolishi</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Типичная ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h4 data-ru="Прямолинейное движение врага к координатам игрока" data-en="Direct straight-line movement toward player coordinates">Koordinata bo'yicha to'g'ridan-to'g'ri ko'r-ko'rona yugurish</h4>
        <p style="font-size:12px;" data-ru="Ученики написали простейшую физику: `enemy.x += (player.x - enemy.x) * speed`. Но как только между игроком и врагом появилась стена дома, враг уперся лбом в стену и беспомощно дрожал на месте!" data-en="Students used naive vector physics: `enemy.x += (player.x - enemy.x) * speed`. But as soon as a building wall stood in between, the enemy pushed straight into the barrier and vibrated helplessly!">O'quvchilar sodda mantiq yozishdi: dushman o'yinchiga qarab to'g'ri yugursin. Ammo o'rtada uy devori paydo bo'lishi bilan dushman devorga yopishib, qaltirab qotib qoldi!</p>
        <pre><code class="language-javascript">// ❌ Xato: To'siqlarni hisobga olmasdan to'g'ri intilish
enemy.x += Math.sign(player.x - enemy.x) * speed; // Devorga botadi!</code></pre>
      </div>
      <div class="box" style="border:1px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой стандарт (Golden Solution)" data-en="Golden Standard">Oltin Standart Yechim</div>
        <h4 data-ru="Сетка Смежности + Алгоритм Поиска Пути (Pathfinding)" data-en="Adjacency Grid + Pathfinding Algorithms">Katakli Graf + Yo'l Qidirish (Pathfinding)</h4>
        <p style="font-size:12px;" data-ru="Игровое поле разбивается на сетку 2D. Дроны не идут напролом, а опрашивают граф: «Какой соседний тайл приведет к игроку в обход препятствия?» и плавно обходят угол." data-en="The world is discretized into a 2D grid graph. Instead of pushing blindly, enemies query the graph for the next walkable node leading around the corner.">O'yin maydoni 2D kataklarga bo'linadi. Dushman to'g'riga qaramaydi, balki grafdan so'raydi: "Qaysi qo'shni katak orqali devorni aylanib o'tib o'yinchiga yetib boraman?".</p>
        <pre><code class="language-javascript">// ✅ To'g'ri: Eng qisqa yo'lning navbatdagi katagiga qadam
const nextTile = bfs(grid, enemyTile, playerTile)[0];</code></pre>
      </div>
    </div>
    <div class="grid-2" style="margin-top:10px;">
      <div class="box">
        <div class="tag" data-ru="30-секундный Блиц" data-en="30-Sec Blitz">30 Soniyalik Blitz</div>
        <p style="font-size:11px;" data-ru="Какая структура данных используется в алгоритме BFS: стек (LIFO) или очередь (FIFO)?" data-en="Which data structure powers BFS search: a Stack (LIFO) or a Queue (FIFO)?">BFS (kenglik bo'yicha qidiruv) algoritmining asosi qaysi ma'lumotlar tuzilmasi: Stek (LIFO) yoki Navbat (FIFO)?</p>
        <div style="font-size:11px; color:var(--accent); font-weight:700;" data-ru="Ответ: Очередь FIFO (First In, First Out) — первый пришел, первый обработан." data-en="Answer: Queue FIFO (First In, First Out).">Javob: Navbat FIFO (First In, First Out) — birinchi kelgan birinchi tekshiriladi!</div>
      </div>
      <div class="box">
        <div class="tag" data-ru="Мост к теме 34" data-en="Bridge to Lesson 34">Bugungi Mavzuga Ko'prik</div>
        <p style="font-size:11px;" data-ru="В GTA 2D мы научились стрелять и ездить на авто. Сегодня мы сделаем полицию и охранных ботов по-настоящему смертоносными и умными!" data-en="In GTA 2D we built drifting cars and blasters. Today we give police and security drones true spatial intelligence!">GTA 2D o'yinimizda mashina haydash va otishmani o'rgandik. Bugun esa politsiya va robotlarni labirintda o'yinchini topadigan aqlli qilamiz!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: GRID GRAPH CONVERSION -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="08:00–14:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="МАТЕМАТИЧЕСКАЯ МОДЕЛЬ" data-en="MATHEMATICAL MODEL">MATEMATIK GRAF MODELI</span></div>
    <h2 data-ru="Как Превратить 2D-Тайлы в Граф для ИИ?" data-en="Transforming 2D Tilemaps into AI Navigable Graphs">2D Tayl Xaritasini Sun'iy Intellekt Uchun Grafga Aylantirish</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" data-ru="Матрица Смежности" data-en="Grid Matrix">Tayl Matritsasi (0 va 1)</div>
        <p style="font-size:12px;" data-ru="Для алгоритма весь мир — это двумерный массив чисел: 0 — проходимый пол, 1 — каменная стена." data-en="To pathfinding algorithms, the world is a 2D integer array: 0 represents walkable floor, 1 represents impassable stone walls.">Algoritm uchun butun o'yin dunyosi — bu 2D sonlar massivi: 0 — o'tib bo'ladigan yo'lak, 1 — tosh devor.</p>
        <pre><code class="language-javascript">const grid = [
  [0, 0, 1, 0, 0],
  [0, 1, 1, 0, 0],
  [0, 0, 0, 0, 1],
  [1, 1, 0, 1, 1],
  [0, 0, 0, 0, 0]
];</code></pre>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="4 Направления Движения" data-en="4 Movement Directions">4 Tomonlama Qo'shnilar</div>
        <p style="font-size:12px;" data-ru="Из любой клетки (x, y) бот может сделать 1 шаг в 4 стороны, если там не стена:" data-en="From any cell (x, y), the AI explores 4 cardinal directions unless blocked by a wall:">Har bir (x, y) katakdan bot 4 tomonga 1 qadam tashlashi mumkin:</p>
        <ul style="font-size:12px; line-height:1.7;">
          <li data-ru="Вверх: (x, y - 1)" data-en="Up: (x, y - 1)"><code>Yuqoriga: (x, y - 1)</code></li>
          <li data-ru="Вправо: (x + 1, y)" data-en="Right: (x + 1, y)"><code>O'ngga: (x + 1, y)</code></li>
          <li data-ru="Вниз: (x, y + 1)" data-en="Down: (x, y + 1)"><code>Pastga: (x, y + 1)</code></li>
          <li data-ru="Влево: (x - 1, y)" data-en="Left: (x - 1, y)"><code>Chapga: (x - 1, y)</code></li>
        </ul>
        <p style="font-size:11px; color:var(--accent);" data-ru="Проверка границ: x &gt;= 0 &amp;&amp; x &lt; cols &amp;&amp; y &gt;= 0 &amp;&amp; y &lt; rows." data-en="Boundary checks ensure x &gt;= 0 &amp;&amp; x &lt; cols &amp;&amp; y &gt;= 0 &amp;&amp; y &lt; rows.">Chegaradan chiqib ketmaslik sharti: x &gt;= 0 &amp;&amp; x &lt; cols &amp;&amp; y &gt;= 0 &amp;&amp; y &lt; rows.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: BFS MECHANICS -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="14:00–20:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="АЛГОРИТМ ПОИСКА" data-en="SEARCH ALGORITHM">BFS QIDIRUV MEXANIZMI</span></div>
    <h2 data-ru="Поиск в Ширину (BFS): Волновая Экспансия" data-en="Breadth-First Search (BFS): Wave Expansion Mechanics">Kenglik Bo'yicha Qidiruv (BFS): To'lqinsimon Tarqalish</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1. FIFO Navbati</div>
        <h4 data-ru="Очередь queue.push / shift" data-en="Queue queue.push / shift">queue.push() va shift()</h4>
        <p style="font-size:11px;" data-ru="Начальная клетка кладется в очередь. Мы достаем первый элемент `queue.shift()` и опрашиваем всех его соседей." data-en="Starting node enters the queue. We extract the head `queue.shift()` and explore all valid neighbours.">Boshlang'ich katak navbatga qo'yiladi. Biz birinchi elementni olib, uning barcha qo'shnilarini tekshiramiz.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);">2. Visited To'plami</div>
        <h4 data-ru="Защита от зацикливания" data-en="Loop prevention set">visited Set() to'plami</h4>
        <p style="font-size:11px;" data-ru="Каждая посещенная клетка записывается в `visited.add('x,y')`. Это гарантирует, что мы не будем бесконечно ходить по кругу." data-en="Every explored cell is marked in `visited.add('x,y')`. This guarantees zero infinite circular loops.">Tekshirilgan har bir katak `visited` ga yoziladi. Bu dushmanning bir joyda doira bo'ylab aylanib qolishini oldini oladi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">3. Parent Xaritasi</div>
        <h4 data-ru="Кто привел в эту клетку?" data-en="Parent backpointers">parent[qo'shni] = joriy</h4>
        <p style="font-size:11px;" data-ru="Для каждого соседа мы запоминаем, из какой клетки мы пришли. Это нужно, чтобы потом восстановить путь назад!" data-en="We store which node discovered each neighbour, allowing us to backtrack the shortest route.">Har bir qo'shniga kimdan kelinganini yozib boramiz. Shu orqali o'yinchigacha bo'lgan yo'l tiklanadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: RECONSTRUCTING PATH -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="20:00–25:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="ВОССТАНОВЛЕНИЕ МАРШРУТА" data-en="PATH RECONSTRUCTION">YO'LNI ORQAGA TIKLASH</span></div>
    <h2 data-ru="Бэктрекинг Маршрута: Как Дроиду Понять, Куда Сделать Первый Шаг?" data-en="Path Backtracking: Identifying the Bot's Immediate Step">Backtracking: Dushman Birinchi Qadamni Qayoqqa Qo'yishi Kerak?</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" data-ru="Алгоритм Восстановления" data-en="Backtracking Algorithm">Orqaga Tiklash Mantig'i</div>
        <p style="font-size:12px; line-height:1.6;" data-ru="Когда волна BFS достигла игрока (Target), мы начинаем идти в обратную сторону от игрока к врагу по цепочке <code>parent</code>:<br>1. Игрок: (4, 4) &larr; пришел из (3, 4)<br>2. (3, 4) &larr; пришел из (2, 4)<br>3. ...<br>4. Враг: (0, 0)<br>Переворачиваем массив <code>path.reverse()</code> — получаем точный пошаговый маршрут!" data-en="When BFS reaches the target player, we walk backwards along <code>parent</code> links from Target to Start:<br>1. Player (4, 4) &larr; from (3, 4)<br>2. (3, 4) &larr; from (2, 4)<br>3. ...<br>4. Enemy (0, 0)<br>Reverse array via <code>path.reverse()</code> to yield the optimal step-by-step path!">To'lqin o'yinchiga yetganda, biz `parent` zanjiri bo'yicha o'yinchidan dushmanga qarab orqaga qaytamiz va massivni `path.reverse()` qilib aylantiramiz!</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="JavaScript Реализация" data-en="JavaScript Implementation">JS Tiklash Kodi</div>
        <pre><code class="language-javascript">function reconstructPath(parent, startKey, targetKey) {
  const path = [];
  let curr = targetKey;
  while (curr && curr !== startKey) {
    path.push(curr);
    curr = parent[curr];
  }
  return path.reverse(); // [keyingi_katak, ..., o'yinchi]
}</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: FINITE STATE MACHINE -->
  <section class="slide" data-phase="Geym-Dizayn|Гейм-Дизайн|Game Design" data-time="25:00–29:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ПАТТЕРН ПОВЕДЕНИЯ" data-en="BEHAVIOUR PATTERN">XULQ-ATVOR MASHINASI</span></div>
    <h2 data-ru="Конечный Автомат Врага (State Machine): Патруль ➔ Погоня ➔ Атака" data-en="Enemy State Machine: Patrol ➔ Chase ➔ Attack">Dushman Holat Mashinasi: Patrul ➔ Ta'qib ➔ Hujum</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag" style="background:rgba(100,116,139,0.15); color:#94a3b8;">1. PATROL (Patrul)</div>
        <h4 data-ru="Спокойный обход точек" data-en="Calm waypoint wandering">Sokin aylanib yurish</h4>
        <p style="font-size:11px;" data-ru="Пока игрок далеко (дистанция &gt; 8 тайлов), бот не напрягает процессор поиском пути, а спокойно ходит между 2 точками патрулирования." data-en="While the player remains outside detection range (&gt; 8 tiles), the bot walks between 2 patrol waypoints without running heavy BFS.">O'yinchi uzoqda bo'lsa (masofa &gt; 8 katak), dushman protsessorni qiynamasdan, faqat belgilangan 2 ta nuqta orasida aylanib yuradi.</p>
      </div>
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);">2. CHASE (Ta'qib)</div>
        <h4 data-ru="Игрок замечен в радиусе!" data-en="Player detected in radius!">O'yinchi ko'rish maydonida!</h4>
        <p style="font-size:11px;" data-ru="Дистанция &lt; 8 тайлов! Загорается красная тревога (!), запускается алгоритм BFS, и бот на полной скорости бежит кратчайшим путем к игроку." data-en="Distance &lt; 8 tiles! Red alert triggers, BFS calculates the shortest path, and the bot sprints around walls toward the player.">Masofa &lt; 8 katak! Qizil trevoga yoqiladi, BFS chaqirilib dushman eng qisqa yo'l bilan o'yinchini aylanib quva boshlaydi.</p>
      </div>
      <div class="box" style="border:1px solid var(--accent);">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">3. ATTACK (Hujum)</div>
        <h4 data-ru="Дистанция удара / выстрела" data-en="Melee / Blaster range">Zarba berish masofasi</h4>
        <p style="font-size:11px;" data-ru="Дистанция &lt; 1.5 тайла! Бот останавливается и наносит урон игроку или открывает лазерный огонь по вычисленному углу Math.atan2." data-en="Distance &lt; 1.5 tiles! Bot stops and delivers melee damage or fires laser blasters calculated via Math.atan2 angle.">Masofa &lt; 1.5 katak! Bot to'xtaydi va o'yinchiga zarba beradi yoki Math.atan2 burchagi bo'yicha lazerdan o't ochadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: 60 FPS PERFORMANCE THROTTLE -->
  <section class="slide" data-phase="Optimizatsiya|Оптимизация|Optimization" data-time="29:00–33:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ГЕЙМДЕВ-ОПТИМИЗАЦИЯ" data-en="GAMEDEV OPTIMIZATION">60 FPS TEZLIK QOIDASI</span></div>
    <h2 data-ru="Как Не Уронить FPS: Троттлинг и Кэширование Пути" data-en="Maintaining 60 FPS: Throttling & Path Caching">FPS Tushib Ketmasligi Uchun: BFS Qidiruvini Keshlashtirish</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Ошибка Новичков: 60 BFS/сек" data-en="Beginner Flaw: 60 BFS/sec">Boshlovchilar Xatosi: Sekundiga 60 ta BFS</div>
        <p style="font-size:12px;" data-ru="Если вызывать `bfs()` в каждом кадре игрового цикла <code>requestAnimationFrame</code> для 10 врагов, игра начнет тормозить и FPS упадет до 12 кадров/сек!" data-en="Calling full `bfs()` on every frame inside <code>requestAnimationFrame</code> for 10 enemies causes massive CPU lag, plummeting FPS to 12!">Har kadrda 10 ta dushman uchun noldan to'liq `bfs()` chaqirilsa, protsessor qiziydi va o'yin qotib, FPS 12 ga tushib ketadi!</p>
        <pre><code class="language-javascript">// ❌ Xato: Har kadrda (sekundiga 60 marta) BFS chaqirish
function update() {
  enemy.path = bfs(grid, enemy, player); // O'yin qotadi!
}</code></pre>
      </div>
      <div class="box" style="border:1px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Профессиональный Троттлинг" data-en="Professional Throttling">Oltin Standart: 0.5s Taymer va Kesh</div>
        <p style="font-size:12px;" data-ru="Путь пересчитывается ТОЛЬКО когда:<br>1. Прошло 500 мс (таймер троттлинга)<br>2. Или игрок перешел на совершенно новую клетку сетки!<br>В остальных кадрах бот просто плавно идет по уже готовому маршруту." data-en="Recompute path ONLY when:<br>1. 500ms has elapsed (throttle timer)<br>2. Or the player moved to a different grid tile!<br>Between re-evaluations, bot simply interpolates along the cached path.">Yo'l FAQAT 500 ms o'tganda yoki o'yinchi butunlay boshqa katakka o'tgandagina qayta hisoblanadi. Qolgan vaqtda bot mavjud keshdagi yo'l bo'yicha yuradi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: SMARTBOARD INTERACTIVE DEMO -->
  <section class="slide" data-phase="Jonli Sinov|Живой Тест|Live Test" data-time="33:00–37:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ИНТЕРАКТИВНЫЙ ТРЕНАЖЕР" data-en="INTERACTIVE SIMULATOR">SMARTBOARD BOSHQARUVI</span></div>
    <h2 data-ru="Лаборатория Pathfinding: Построй Стену и Запусти Волну BFS" data-en="Pathfinding Lab: Draw Walls & Trigger BFS Waves">Pathfinding Sinovi: Devor Quring va BFS To'lqinini Kuzating</h2>
    <div style="background:var(--surface); border:1px solid var(--hair); border-radius:8px; padding:12px; margin-top:8px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <div>
          <span style="font-size:11px; font-weight:700; color:var(--accent);" data-ru="РЕЖИМ КЛИКА:" data-en="CLICK MODE:">BOSISH REJIMI:</span>
          <span id="demoModeLabel" style="font-size:12px; font-weight:700; color:var(--green); margin-left:6px;" data-ru="Рисовать Стены" data-en="Draw Walls">Devor Qirish</span>
        </div>
        <div style="display:flex; gap:6px;">
          <button onclick="setGridTool('wall')" class="btn" style="padding:4px 8px; font-size:10px;" data-ru="Стена" data-en="Wall">Devor</button>
          <button onclick="setGridTool('clear')" style="background:#334155; color:#fff; border:none; padding:4px 8px; border-radius:4px; font-size:10px; cursor:pointer;" data-ru="Очистить" data-en="Clear">Tozalash</button>
          <button onclick="runBfsDemo()" class="btn" style="background:var(--accent); padding:4px 10px; font-size:10px;" data-ru="▶️ Пуск BFS" data-en="▶️ Run BFS">▶️ BFS Qidiruv</button>
        </div>
      </div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
        <div style="background:#0f172a; padding:10px; border-radius:6px; border:1px solid #334155; display:flex; justify-content:center;">
          <canvas id="miniGridCanvas" width="220" height="220" style="background:#020617; border-radius:4px; cursor:pointer;"></canvas>
        </div>
        <div style="background:#090d16; padding:10px; border-radius:6px; border:1px solid #1e293b; font-family:monospace; font-size:10px; line-height:1.5;">
          <div style="color:var(--accent); font-weight:700; margin-bottom:4px;" data-ru="Телеметрия Поиска Пути:" data-en="Pathfinding Telemetry:">Yo'l Qidirish Telemetriyasi:</div>
          <div id="demoTelemetry" style="color:#94a3b8;" data-ru="Кликните по сетке, чтобы поставить препятствия, затем нажмите '▶️ Пуск BFS'." data-en="Click on the grid to place obstacles, then click '▶️ Run BFS'.">Katakka bosing va devor quring, so‘ng '▶️ BFS Qidiruv' tugmasini bosing.</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: QUICK QUIZ -->
  <section class="slide" data-phase="Viktorina|Викторина|Quiz" data-time="37:00–39:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ЭКСПРЕСС-ТЕСТ" data-en="RAPID QUIZ">TEZKOR TEST</span></div>
    <h2 data-ru="3 Вопроса по ИИ и Алгоритмам Поиска Пути" data-en="3 Questions on Game AI & Pathfinding">Geymdev Sun'iy Intellekti Bo'yicha 3 Savol</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag">Savol 1</div>
        <h4 data-ru="Почему простой векторный бег приводит к застреванию?" data-en="Why does naive vector tracking lead to getting stuck?">Nega oddiy koordinatali intilish devorga botib qolishga olib keladi?</h4>
        <div style="font-size:11px; margin-top:6px; line-height:1.5;">
          <div>A) Dushmanning joni tugaydi</div>
          <div style="color:var(--green); font-weight:700;">B) U to'siqlarni aylanib o'tish yo'lini hisoblamaydi</div>
          <div>C) Canvas tezligi past</div>
        </div>
      </div>
      <div class="box">
        <div class="tag">Savol 2</div>
        <h4 data-ru="Какое свойство BFS гарантирует нахождение кратчайшего пути?" data-en="What property of BFS guarantees the shortest path?">BFS algoritmining qaysi xususiyati eng qisqa yo'lni kafolatlaydi?</h4>
        <div style="font-size:11px; margin-top:6px; line-height:1.5;">
          <div>A) Tasodifiy qadam tashlash</div>
          <div style="color:var(--green); font-weight:700;">B) To'lqin barcha yo'nalishlarga bir tekis (1 qadamdan) tarqalishi</div>
          <div>C) Faqat bitta yo'lni tekshirishi</div>
        </div>
      </div>
      <div class="box">
        <div class="tag">Savol 3</div>
        <h4 data-ru="Зачем нужен троттлинг 500 мс для вызова BFS?" data-en="Why throttle BFS re-computations to 500ms?">Nega BFS chaqiruviga 500 ms lik kesh/taymer qo'yiladi?</h4>
        <div style="font-size:11px; margin-top:6px; line-height:1.5;">
          <div>A) O'yin qiyinroq bo'lishi uchun</div>
          <div style="color:var(--green); font-weight:700;">B) Protsessorni yuklamasdan 60 FPS tezlikni saqlab qolish uchun</div>
          <div>C) Dushmanga dam berish uchun</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: SUMMARY & HOMEWORK -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="39:00–40:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="SUMMARY & HOMEWORK">XULOSA VA UY VAZIFASI</span></div>
    <h2 data-ru="Итоги 34-Урока и Домашний Проект" data-en="Lesson 34 Takeaways & Homework Assignment">34-Dars Xulosalari va Kiber-Dushman Loyihasi</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Домашнее Задание" data-en="Homework Assignment">Uy Vazifasi (vazifa.html)</div>
        <p style="font-size:12px; line-height:1.6;" data-ru="<strong>1-Уровень (4 б):</strong> Создать сетку 10x10 с поиском соседей по 4 сторонам.<br><strong>2-Уровень (4 б):</strong> Реализовать алгоритм BFS с восстановлением кратчайшего пути.<br><strong>3-Уровень (2 б):</strong> Внедрить конечный автомат состояний (PATROL / CHASE / ATTACK)." data-en="<strong>Tier 1 (4 pts):</strong> Create a 10x10 grid with 4-cardinal neighbour lookups.<br><strong>Tier 2 (4 pts):</strong> Code a complete BFS algorithm backtracking shortest path waypoints.<br><strong>Tier 3 (2 pts):</strong> Integrate a 3-stage finite state machine (PATROL / CHASE / ATTACK)."><strong>1-Daraja (4 b):</strong> 10x10 katakli xaritada 4 tomonlama qo'shnilarni topuvchi funksiya yozish.<br><strong>2-Daraja (4 b):</strong> BFS algoritmi va orqaga tiklash (backtracking) orqali eng qisqa yo'lni topish.<br><strong>3-Daraja (2 b):</strong> 3 bosqichli holat mashinasini (PATROL / CHASE / ATTACK) o'yinga kiritish.</p>
      </div>
      <div class="box" style="border:1px solid var(--accent);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Анонс 35-Урока" data-en="Next Lesson 35">Keyingi Dars (35-Dars)</div>
        <h4 data-ru="Инвентарь и Предметы: Drag-and-Drop и Артефакты" data-en="Inventory System: Drag-and-Drop & Power-Ups">Inventar va Buyumlar Tizimi: Drag-and-Drop va Artefaktlar</h4>
        <p style="font-size:12px;" data-ru="В следующий раз мы соберем систему инвентаря: ячейки слотов, перетаскивание мечей и зелий через HTML5 Drag-and-Drop, баффы к характеристикам героя!" data-en="Next time we build an RPG inventory engine: slot grids, dragging weapons and potions via HTML5 Drag-and-Drop, and applying hero stat modifiers!">Keyingi darsimizda qahramonimiz uchun to'liq inventar tizimini quramiz: slotlar, HTML5 Drag-and-Drop bilan qilich va ziyon vositalarini siljitish va kuchaytirgichlar!</p>
      </div>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. NOTES DATA (10 Slides Notes for 40-min Single Block)
# -----------------------------------------------------------------------------
NOTES_DATA = {
    "uz": [
        ["Kirish va Maqsad", "O'quvchilarga bugungi mavzu: Geymdev sun'iy intellekti va BFS pathfinding ekanini e'lon qiling.", "Doskaga devorga botib qolgan sodda bot rasmini chizing."],
        ["Uy Vazifasi Tahlili", "33-darsdagi GTA 2D o'yinida dushmanlarning devorga botib qolishi sababini tushuntiring.", "Katakli graf va pathfinding algoritmi bu muammoni qanday yechishini ayting."],
        ["Grafga Aylantirish", "Canvas dunyosini 2D sonlar massiviga (0 yo'l, 1 devor) o'tkazishni ko'rsating.", "4 tomonlama qo'shnilar va chegaralarni tekshirishni tushuntiring."],
        ["BFS Mexanikasi", "FIFO navbati (queue.shift) va visited to'plami orqali to'lqinsimon qidiruvni tushuntiring.", "Nega BFS eng qisqa yo'lni kafolatlashini ko'rsating."],
        ["Yo'lni Qayta Tiklash", "Parent zanjiri bo'yicha o'yinchidan dushmanga qarab orqaga qadam tashlashni o'rgating.", "path.reverse() orqali navbatdagi qadamni topishni ko'rsating."],
        ["Holat Mashinasi", "PATROL, CHASE va ATTACK holatlari o'rtasidagi farqni tushuntiring.", "Masofa 8 katakdan kamayganda qizil trevoga yoqilishini ko'rsating."],
        ["60 FPS Optimizatsiyasi", "Har kadrda BFS chaqirish o'yinni qotirib qo'yishini (lag) tushuntiring.", "500 ms taymer va kesh orqali tezlikni saqlab qolish sirini ayting."],
        ["Smartboard Sinovi", "Doskadagi simulyatorda devorlar chizib, BFS to'lqinini ishga tushiring.", "O'quvchini doskaga chiqarib labirint qurg'azing."],
        ["Tezkor Viktorina", "3 ta nazorat savoli orqali mavzuni mustahkamlang.", "To'g'ri javob bergan o'quvchilarga rag'bat ballari bering."],
        ["Xulosa va Vazifa", "Darsni yakunlang va 10 ballik uy vazifasini belgilang.", "Keyingi Inventar va Drag-and-Drop mavzusiga qiziqish uyg'oting."]
    ],
    "ru": [
        ["Введение и Цель", "Объявите тему: игровой искусственный интеллект и поиск пути BFS.", "Нарисуйте на доске застрявшего в стене простого врага."],
        ["Разбор ДЗ 33", "Разберите ошибку в GTA 2D: застревание врагов в стенах зданий.", "Покажите, как сетка навигации и BFS решают эту проблему."],
        ["Превращение в Граф", "Объясните преобразование Canvas мира в 2D-матрицу (0 пол, 1 стена).", "Разберите 4 направления соседей и проверку границ."],
        ["Механика BFS", "Объясните очередь FIFO и множество visited для волнового поиска.", "Покажите, почему BFS математически находит кратчайший путь."],
        ["Восстановление Пути", "Научите двигаться назад по ссылкам parent от цели к старту.", "Объясните реверс массива path.reverse() для первого шага."],
        ["Конечный Автомат", "Разберите 3 состояния: PATROL, CHASE и ATTACK.", "Покажите дистанцию агра 8 тайлов для включения тревоги."],
        ["Оптимизация 60 FPS", "Предупредите об ошибке вызова BFS в каждом кадре игрового цикла.", "Научите использовать троттлинг 500 мс и кэш пути."],
        ["Смартборд Тест", "Запустите интерактивный тренажер и постройте лабиринт на смартборде.", "Пригласите ученика запустить волну поиска."],
        ["Экспресс-Тест", "Проведите быстрый опрос по 3 вопросам на слайде.", "Поставьте баллы за правильные ответы."],
        ["Итоги Урока", "Подведите итоги и выдайте домашнее задание.", "Анонсируйте тему Инвентаря и Drag-and-Drop на следующий урок."]
    ],
    "en": [
        ["Intro & Objectives", "Announce today's topic: Game AI navigation and BFS pathfinding.", "Draw a simple enemy stuck against a solid obstacle on the board."],
        ["Lesson 33 Review", "Analyze the pitfall of straight-line pursuit getting blocked by city walls in GTA 2D.", "Explain how 2D grid graphs and BFS solve obstacle avoidance."],
        ["Grid Graph Conversion", "Show how Canvas coordinates discretize into a 2D matrix (0 floor, 1 wall).", "Break down 4-cardinal neighbour lookups and map clamping."],
        ["BFS Mechanics", "Explain the FIFO queue and visited Set driving wave expansion.", "Demonstrate why BFS mathematically guarantees the shortest step path."],
        ["Path Backtracking", "Teach reverse backtracking from target to start via parent pointers.", "Explain why reversing the array yields the bot's immediate next step."],
        ["State Machine", "Walk through the 3 behavioral states: PATROL, CHASE, and ATTACK.", "Show how an 8-tile detection threshold triggers red combat alerts."],
        ["60 FPS Optimization", "Warn against calling full BFS every frame inside requestAnimationFrame.", "Teach the 500ms throttling pattern and waypoint caching."],
        ["Smartboard Demo", "Draw obstacles on the interactive board and trigger BFS waves.", "Invite a student to design a maze and watch the bot solve it."],
        ["Quick Quiz", "Conduct the 3-question knowledge check.", "Award bonus marks to active participants."],
        ["Summary & Next", "Wrap up the lesson and assign the 3-tier homework.", "Tease the upcoming Inventory & Drag-and-Drop system for Lesson 35."]
    ]
}

# -----------------------------------------------------------------------------
# 3. INTERACTIVE SIMULATOR SCRIPT FOR PRESENTATION
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
var miniGrid = [
  [0,0,0,0,0,0,0],
  [0,1,1,1,1,0,0],
  [0,0,0,0,1,0,0],
  [0,1,1,0,1,0,0],
  [0,0,1,0,0,0,0],
  [0,0,1,1,1,1,0],
  [0,0,0,0,0,0,0]
];
var startPos = {x: 0, y: 0};
var targetPos = {x: 6, y: 6};
var currentTool = 'wall';

function drawMiniGrid(pathCells) {
  var cvs = document.getElementById('miniGridCanvas');
  if (!cvs) return;
  var ctx = cvs.getContext('2d');
  var sz = cvs.width / 7;

  ctx.clearRect(0, 0, cvs.width, cvs.height);

  for (var r = 0; r < 7; r++) {
    for (var c = 0; c < 7; c++) {
      if (miniGrid[r][c] === 1) {
        ctx.fillStyle = '#475569';
      } else {
        ctx.fillStyle = '#0f172a';
      }
      ctx.fillRect(c * sz, r * sz, sz - 1, sz - 1);

      // Path highlight
      if (pathCells && pathCells[c + ',' + r]) {
        ctx.fillStyle = 'rgba(16, 185, 129, 0.4)';
        ctx.fillRect(c * sz, r * sz, sz - 1, sz - 1);
      }
    }
  }

  // Draw Start (Enemy Bot - Purple)
  ctx.fillStyle = '#a855f7';
  ctx.beginPath();
  ctx.arc(startPos.x * sz + sz/2, startPos.y * sz + sz/2, sz/3, 0, Math.PI * 2);
  ctx.fill();

  // Draw Target (Player - Green)
  ctx.fillStyle = '#10b981';
  ctx.beginPath();
  ctx.arc(targetPos.x * sz + sz/2, targetPos.y * sz + sz/2, sz/3, 0, Math.PI * 2);
  ctx.fill();
}

function setGridTool(tool) {
  currentTool = tool;
  var lbl = document.getElementById('demoModeLabel');
  if (tool === 'wall') {
    lbl.textContent = 'Devor Qurish';
    lbl.style.color = 'var(--green)';
  } else {
    for (var r = 0; r < 7; r++) {
      for (var c = 0; c < 7; c++) {
        miniGrid[r][c] = 0;
      }
    }
    drawMiniGrid(null);
    var tel = document.getElementById('demoTelemetry');
    if (tel) tel.textContent = 'Xarita tozalandi. Devor quring va "▶️ BFS Qidiruv"ni bosing.';
  }
}

function runBfsDemo() {
  var queue = [[startPos.x, startPos.y]];
  var visited = {};
  var parent = {};
  visited[startPos.x + ',' + startPos.y] = true;

  var found = false;
  var steps = 0;

  var dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]];

  while (queue.length > 0) {
    var curr = queue.shift();
    steps++;
    var cx = curr[0];
    var cy = curr[1];

    if (cx === targetPos.x && cy === targetPos.y) {
      found = true;
      break;
    }

    for (var i = 0; i < 4; i++) {
      var nx = cx + dirs[i][0];
      var ny = cy + dirs[i][1];
      var key = nx + ',' + ny;

      if (nx >= 0 && nx < 7 && ny >= 0 && ny < 7 && miniGrid[ny][nx] === 0 && !visited[key]) {
        visited[key] = true;
        parent[key] = cx + ',' + cy;
        queue.push([nx, ny]);
      }
    }
  }

  var tel = document.getElementById('demoTelemetry');
  if (found) {
    var pathMap = {};
    var currK = targetPos.x + ',' + targetPos.y;
    var length = 0;
    while (currK && currK !== (startPos.x + ',' + startPos.y)) {
      pathMap[currK] = true;
      currK = parent[currK];
      length++;
    }
    pathMap[startPos.x + ',' + startPos.y] = true;
    drawMiniGrid(pathMap);

    if (tel) {
      tel.innerHTML = '<span style="color:#10b981; font-weight:700;">✅ Yo‘l Topildi!</span><br>' +
        'Eng qisqa masofa: <strong>' + length + ' qadam</strong><br>' +
        'Tekshirilgan kataklar: ' + steps + ' ta<br>' +
        '<span style="color:#38bdf8;">Dushman yashil chiziq bo‘ylab o‘yinchiga yetib boradi.</span>';
    }
  } else {
    drawMiniGrid(null);
    if (tel) {
      tel.innerHTML = '<span style="color:#ef4444; font-weight:700;">❌ Yo‘l Yo‘q (Bloklangan)!</span><br>' +
        'O‘yinchi atrofini devorlar to‘liq o‘rab olgan. Tekshirildi: ' + steps + ' ta katak.';
    }
  }
}

window.addEventListener('DOMContentLoaded', function() {
  var cvs = document.getElementById('miniGridCanvas');
  if (cvs) {
    drawMiniGrid(null);
    cvs.addEventListener('click', function(e) {
      var rect = cvs.getBoundingClientRect();
      var sz = cvs.width / 7;
      var c = Math.floor((e.clientX - rect.left) / sz);
      var r = Math.floor((e.clientY - rect.top) / sz);
      if (c >= 0 && c < 7 && r >= 0 && r < 7) {
        if ((c === startPos.x && r === startPos.y) || (c === targetPos.x && r === targetPos.y)) return;
        miniGrid[r][c] = miniGrid[r][c] === 1 ? 0 : 1;
        drawMiniGrid(null);
      }
    });
  }
});
"""

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "34-dars: Dushman AI va Pathfinding: To'siqlarni Aylanib Quvish"
    title_ru = "Урок 34: ИИ Врагов и Pathfinding: Обход Препятствий"
    title_en = "Lesson 34: Enemy AI & Pathfinding: Obstacle Avoidance"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="7–8 КЛАСС" data-en="GRADES 7–8">7–8-SINF</span>',
                 tpl)

    titles_json = json.dumps({"uz": title_uz, "ru": title_ru, "en": title_en}, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', lambda m: f'var TITLES = {titles_json};', tpl)

    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', lambda m: f'var NOTES = {notes_json};', tpl)

    stage_regex = r'<div class="stage">[\s\S]*?</div><!-- /stage -->'
    new_stage = f'<div class="stage">\n{SLIDES_HTML}\n  </div><!-- /stage -->'
    tpl = re.sub(stage_regex, lambda m: new_stage, tpl)

    custom_script = f"<script>\n{SIMULATOR_JS}\n</script>\n</body>"
    tpl = tpl.replace("</body>", custom_script)

    out_path = os.path.join(DEST_DIR, "prezentatsiya.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

def build_worksheet():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "34-dars: Dushman AI va Pathfinding: To'siqlarni Aylanib Quvish"
    title_ru = "Урок 34: ИИ Врагов и Pathfinding: Обход Препятствий"
    title_en = "Lesson 34: Enemy AI & Pathfinding: Obstacle Avoidance"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<h1>.*?</h1>',
                 f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>',
                 tpl)

    sec1_html = """
    <p class="lead" style="font-size:12px; margin-bottom:8px;" data-ru="<strong>Миссия Урока:</strong> Запрограммировать искусственный интеллект вражеского дрона в Canvas 2D: преобразовать тайловую карту в граф проходимости, запустить поиск в ширину (BFS) по очереди FIFO, восстановить кратчайший маршрут вокруг стен и внедрить конечный автомат состояний (PATROL ➔ CHASE ➔ ATTACK)." data-en="<strong>Lesson Mission:</strong> Architect enemy drone AI navigation in Canvas 2D: convert tilemaps into walkable graphs, execute Breadth-First Search (BFS) via FIFO queues, reconstruct shortest paths around walls, and implement a 3-state finite state machine (PATROL ➔ CHASE ➔ ATTACK)."><strong>Dars Missiyasi:</strong> Canvas 2D-da dushman botining aqlli harakatini yaratish: taylli xaritani grafga aylantirish, FIFO navbati bilan BFS qidiruvini ishga tushirish, devorlarni aylanib o'tuvchi eng qisqa yo'lni tiklash va 3 bosqichli holat mashinasini (PATROL ➔ CHASE ➔ ATTACK) dasturlash.</p>
    <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="3 Фазы Алгоритма BFS:" data-en="3 Phases of the BFS Algorithm:">BFS Qidiruvining 3 Asosiy Bosqichi:</div>
      <div>1. <strong>Queue Exploration:</strong> <span data-ru="Стартовый узел помещается в очередь FIFO, соседи проверяются по 4 направлениям." data-en="Start node enqueues into FIFO; 4 cardinal neighbours are evaluated.">Boshlang'ich katak FIFO navbatiga qo'yilib, 4 tomonlama qo'shnilar tekshiriladi</span>.</div>
      <div>2. <strong>Visited Set:</strong> <span data-ru="Каждая клетка помечается в visited, исключая бесконечные циклы вокруг колонн." data-en="Cells are logged in a visited set, eliminating endless circular loops.">Kataklar visited to'plamiga saqlanib, cheksiz aylanib qolishlar bartaraf etiladi</span>.</div>
      <div>3. <strong>Parent Backtracking:</strong> <span data-ru="От игрока к врагу восстанавливается кратчайшая цепочка шагов." data-en="Optimal step-by-step waypoints backtrack from target to enemy.">O'yinchidan dushmanga qarab eng optimal qadamlar zanjiri qayta tiklanadi</span>.</div>
    </div>
    """

    sec2_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="JavaScript-реализация поиска в ширину (BFS) на сетке:" data-en="JavaScript BFS grid search implementation:">2D katakli grafda BFS qidiruv funksiyasi:</p>
    <pre style="background:var(--surface-2); padding:6px; font-size:11px; border-radius:4px; margin:0;"><code class="language-javascript">function findPathBFS(grid, start, target) {
  const queue = [[start.x, start.y]];
  const visited = new Set([`${start.x},${start.y}`]);
  const parent = {};

  while (queue.length > 0) {
    const [cx, cy] = queue.shift();
    if (cx === target.x && cy === target.y) return backtrack(parent, start, target);
    for (const [dx, dy] of [[0,-1], [1,0], [0,1], [-1,0]]) {
      const nx = cx + dx, ny = cy + dy, key = `${nx},${ny}`;
      if (grid[ny]?.[nx] === 0 && !visited.has(key)) {
        visited.add(key);
        parent[key] = `${cx},${cy}`;
        queue.push([nx, ny]);
      }
    }
  }
  return [];
}</code></pre>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Модуль ИИ" data-en="AI Module">AI Moduli</th>
            <th style="padding:4px 6px;" data-ru="Входные Данные" data-en="Input Data">Kiruvchi Ma'lumot</th>
            <th style="padding:4px 6px;" data-ru="Выходной Результат" data-en="Output Result">Natijaviy Harakat</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;">Tile Graph</td>
            <td style="padding:4px 6px;">Canvas 2D xaritasi</td>
            <td style="padding:4px 6px;">2D massiv [0, 1]</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ Bajarildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;">BFS Search</td>
            <td style="padding:4px 6px;">Start va Target katak</td>
            <td style="padding:4px 6px;">Parent zanjiri</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ Bajarildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;">Backtracking</td>
            <td style="padding:4px 6px;">Parent xaritasi</td>
            <td style="padding:4px 6px;">path[] qadamlar ro'yxati</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ Bajarildi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;">State Machine</td>
            <td style="padding:4px 6px;">Masofa (dist)</td>
            <td style="padding:4px 6px;">PATROL / CHASE / ATTACK</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ 100% Yashil</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    replacements = {
        "{{LESSON_NUM}}": "34",
        "{{LESSON_TITLE_UZ}}": "Dushman AI va Pathfinding: To'siqlarni Aylanib Quvish",
        "{{LESSON_TITLE_RU}}": "ИИ Врагов и Pathfinding: Обход Препятствий",
        "{{LESSON_TITLE_EN}}": "Enemy AI & Pathfinding: Obstacle Avoidance",
        "{{COHORT_LABEL_UZ}}": "7–8-sinf",
        "{{COHORT_LABEL_RU}}": "7–8 класс",
        "{{COHORT_LABEL_EN}}": "Grade 7–8",
        "{{TRACK_NAME_UZ}}": "Game Dev, Interaktiv Veb & FUT Creator Track",
        "{{TRACK_NAME_RU}}": "Game Dev, Интерактивный Веб & FUT Creator",
        "{{TRACK_NAME_EN}}": "Game Dev, Interactive Web & FUT Creator Track",
        "{{SECTION_1_CONTENT}}": sec1_html,
        "{{SECTION_2_CONTENT}}": sec2_html,
        "{{SECTION_3_CONTENT}}": sec3_html,
        "{{RUBRIC_T1_BALL}}": "4",
        "{{RUBRIC_T1_UZ}}": "1-Daraja: Baza (2D xaritada 4 tomonlama qo'shnilarni tekshirish)",
        "{{RUBRIC_T1_RU}}": "Уровень 1: База (Поиск соседей по 4 направлениям на сетке)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (4-cardinal neighbour lookup on 2D grid)",
        "{{RUBRIC_T2_BALL}}": "4",
        "{{RUBRIC_T2_UZ}}": "2-Daraja: Amaliyot (BFS algoritmi va orqaga tiklash zanjiri)",
        "{{RUBRIC_T2_RU}}": "Уровень 2: Практика (Алгоритм BFS и восстановление пути)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Full BFS algorithm & route backtracking)",
        "{{RUBRIC_T3_BALL}}": "2",
        "{{RUBRIC_T3_UZ}}": "3-Daraja: Challenge (3 holatli State Machine va 60 FPS kesh)",
        "{{RUBRIC_T3_RU}}": "Уровень 3: Челлендж (State Machine и троттлинг кэша пути)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (State Machine and 60 FPS path throttling)"
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

    title_uz = "34-dars: Dushman AI va Pathfinding: To'siqlarni Aylanib Quvish"
    title_ru = "Урок 34: ИИ Врагов и Pathfinding: Обход Препятствий"
    title_en = "Lesson 34: Enemy AI & Pathfinding: Obstacle Avoidance"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tasks_html = """
    <!-- TIER 1 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1-Daraja (Baza — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Поиск Валидных Соседей на Сетке" data-en="Valid Neighbour Discovery on 2D Grid">2D Xaritada Qo'shni Kataklarni Topish</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите функцию get_walkable_neighbours(grid, x, y), которая проверяет 4 стороны от текущей клетки и возвращает только те координаты, где нет стены (grid[ny][nx] === 0) и которые не выходят за границы карты." data-en="Write a function get_walkable_neighbours(grid, x, y) inspecting 4 cardinal directions and returning only walkable coordinates (grid[ny][nx] === 0) within grid boundaries.">Berilgan katakdan 4 tomonga (yuqoriga, o'ngga, pastga, chapga) tekshirib, devor bo'lmagan va xaritadan chiqib ketmagan kataklar ro'yxatini qaytaruvchi funksiya yozing.</p>
      <textarea id="hw_code_t1" class="code-editor" style="width:100%; min-height:90px; background:#0f172a; color:#f8fafc; font-family:monospace; font-size:11px; padding:8px; border-radius:4px; border:1px solid #334155;">// 1-Daraja yechimingizni shu yerga yozing
function getWalkableNeighbours(grid, x, y) {
  const dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]];
  const valid = [];
  // Kodni yozing
  return valid;
}
</textarea>
    </div>

    <!-- TIER 2 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">2-Daraja (Amaliyot — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Полный Алгоритм BFS с Бэктрекингом" data-en="Complete BFS Algorithm with Backtracking">BFS Qidiruv va Yo'lni Qayta Tiklash</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Создайте функцию find_path_bfs(grid, start, target), которая находит кратчайший путь между стартом и целью через очередь FIFO и возвращает массив координат пути [{x, y}, ...]." data-en="Create find_path_bfs(grid, start, target) finding the shortest walkable route between start and target via FIFO queue, returning an array of waypoint coordinates [{x, y}, ...].">Boshlang'ich va maqsad koordinatalari orasidagi eng qisqa yo'lni FIFO navbati orqali topib, qadamlar massivini qaytaruvchi to'liq BFS funksiyasini yozing.</p>
      <textarea id="hw_code_t2" class="code-editor" style="width:100%; min-height:100px; background:#0f172a; color:#f8fafc; font-family:monospace; font-size:11px; padding:8px; border-radius:4px; border:1px solid #334155;">// 2-Daraja yechimingizni shu yerga yozing
function findPathBFS(grid, start, target) {
  // BFS qidiruv kodi
}
</textarea>
    </div>

    <!-- TIER 3 (2 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);">3-Daraja (Kiber-Challenge — 2 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Конечный Автомат Состояний Врага" data-en="Enemy Finite State Machine">Dushman Holat Mashinasi (State Machine)</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Реализуйте класс EnemyAI с методами update(player, grid). Если дистанция > 8 — режим PATROL, если 1.5 < дистанция <= 8 — CHASE с пересчетом BFS раз в 500 мс, если дистанция <= 1.5 — ATTACK." data-en="Implement an EnemyAI class with an update(player, grid) method. State is PATROL when distance > 8, CHASE when 1.5 < distance <= 8 (recomputing BFS every 500ms), and ATTACK when distance <= 1.5.">EnemyAI klassini yarating: masofa > 8 bo'lsa PATROL, 1.5 < masofa <= 8 bo'lsa CHASE (yo'lni har 500 ms da yangilash), masofa <= 1.5 bo'lsa ATTACK holatini ishga tushirsin.</p>
      <textarea id="hw_code_t3" class="code-editor" style="width:100%; min-height:90px; background:#0f172a; color:#f8fafc; font-family:monospace; font-size:11px; padding:8px; border-radius:4px; border:1px solid #334155;">// 3-Daraja yechimingizni shu yerga yozing
class EnemyAI {
  // State machine kodi
}
</textarea>
    </div>
    """

    replacements = {
        "{{LESSON_NUM}}": "34",
        "{{LESSON_TITLE_UZ}}": "Dushman AI va Pathfinding: To'siqlarni Aylanib Quvish",
        "{{LESSON_TITLE_RU}}": "ИИ Врагов и Pathfinding: Обход Препятствий",
        "{{LESSON_TITLE_EN}}": "Enemy AI & Pathfinding: Obstacle Avoidance",
        "{{COHORT_LABEL_UZ}}": "7–8-sinf",
        "{{COHORT_LABEL_RU}}": "7–8 класс",
        "{{COHORT_LABEL_EN}}": "Grade 7–8",
        "{{RUBRIC_T1_BALL}}": "4",
        "{{RUBRIC_T1_UZ}}": "1-Daraja: Baza (4 tomonlama qo'shnilarni tekshirish)",
        "{{RUBRIC_T1_RU}}": "Уровень 1: База (Поиск соседей по 4 сторонам)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (4-cardinal neighbour lookups)",
        "{{RUBRIC_T2_BALL}}": "4",
        "{{RUBRIC_T2_UZ}}": "2-Daraja: Amaliyot (To'liq BFS qidiruv va yo'lni tiklash)",
        "{{RUBRIC_T2_RU}}": "Уровень 2: Практика (Полный BFS алгоритм и бэктрекинг)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Full BFS algorithm & backtracking)",
        "{{RUBRIC_T3_BALL}}": "2",
        "{{RUBRIC_T3_UZ}}": "3-Daraja: Challenge (3 holatli State Machine va 500ms kesh)",
        "{{RUBRIC_T3_RU}}": "Уровень 3: Челлендж (State Machine и троттлинг 500мс)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (3-state machine & 500ms throttle)",
        "{{TASKS_HTML}}": tasks_html,
        "{{LESSON_SLUG}}": "7-8-w12-l34-dushman-ai-va-pathfinding"
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    doc = """# 34-dars: Dushman AI va Pathfinding: To'siqlarni Aylanib Quvish (O'qituvchi Metodologiyasi)

## Darsning Pasporti
- **Sinf:** 7–8-sinf (Game Dev, Interaktiv Veb & FUT Creator Track)
- **Davomiyligi:** 40 daqiqa (Yakka Dars / Single Block)
- **Asosiy maqsad:** O'quvchilarga Canvas 2D o'yinlarida ko'r-ko'rona koordinatalarga intiluvchi sodda dushmanlar o'rniga to'siqlarni aylanib o'tuvchi fazoviy intellektga ega sun'iy intellekt (Pathfinding) yaratishni o'rgatish. 2D xaritani grafga aylantirish, BFS (Breadth-First Search) kenglik bo'yicha qidiruv, parent backtracking va o'yin qotib qolmasligi uchun 500 ms kesh optimizatsiyasini dasturlash.

---

## 40 Daqiqalik Aniq Vaqt Taqsimoti (Pacing)

| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Motivatsiya | 1 | Pac-Man va zamonaviy o'yinlardagi dushmanlar qanday qilib o'yinchini aylanib topishini tushuntirish. | Diqqat bilan tinglaydilar va dars maqsadini belgilaydilar. |
| **04:00–08:00** | 33-dars HW Tahlili | 2 | GTA 2D o'yinida dushmanlarning devorga botib, qaltirab qolishi xatosini tahlil qilish. | Blitz savolga javob beradilar, navbat FIFO mexanizmini yozadilar. |
| **08:00–14:00** | Xaritani Grafga Aylantirish | 3 | Canvas piksellarini 2D sonlar massiviga (0 yo'l, 1 devor) o'tkazish va 4 tomonlama qo'shnilarni ko'rsatish. | Graf matritsasi tuzilishini tushunadilar. |
| **14:00–20:00** | BFS Mexanikasi | 4 | FIFO navbati (queue.shift) va visited to'plami yordamida to'lqinsimon tarqalishni doskaga chizish. | Nega BFS eng qisqa yo'lni kafolatlashini anglaydilar. |
| **20:00–25:00** | Yo'lni Qayta Tiklash | 5 | O'yinchidan dushmanga qarab orqaga parent zanjiri bo'yicha qaytish va path.reverse() qilishni o'rgatish. | Yo'l tiklash kodini ko'rib chiqadilar. |
| **25:00–29:00** | Holat Mashinasi (FSM) | 6 | PATROL (sokin yurish), CHASE (quvish) va ATTACK (hujum) holatlarini tahlil qilish. | 8 katakli ko'rish radiusini o'rganadilar. |
| **29:00–33:00** | 60 FPS Optimizatsiyasi | 7 | Har kadrda BFS chaqirish o'yinni qotirib qo'yishini ko'rsatish. 500 ms lik kesh taymerini joriy etish. | O'yin optimizatsiyasi sirini yozib oladilar. |
| **33:00–37:00** | Smartboard Sinovi | 8 | Slayddagi simulyatorda devorlar chizib, BFS to'lqini qanday tarqalishini jonli ko'rsatish. | Ekranda dushman harakatini kuzatadilar. |
| **37:00–39:00** | Viktorina (Quiz) | 9 | 3 ta nazorat savoli bo'yicha tezkor blitz o'tkazish. | Faol javob beradilar va o'z bilimlarini tekshiradilar. |
| **39:00–40:00** | Xulosa va Uy Vazifasi | 10 | 10 ballik uy vazifasini tushuntirish va Inventar mavzusiga ko'prik! | Kundaliklariga vazifani yozib oladilar. |

---

## O'qituvchi Uchun Muhim Blitz Savollari
1. **"Nega BFS algoritmi doim eng qisqa yo'lni topishga kafolat beradi?"**
   - Javob: Chunki u to'lqin kabi har tomonlama teng tezlikda (avval 1 qadam, keyin 2 qadam, keyin 3 qadam) kengayadi. Nishonga birinchi yetib borgan to'lqin zanjiri eng qisqa yo'l bo'ladi.
2. **"Agar visited to'plamini qo'shishni unutib qoldirsak nima bo'ladi?"**
   - Javob: Algoritm ikkita qo'shni katak o'rtasida abadiy navbatga qo'shilib, cheksiz siklga (Infinite Loop) tushadi va brauzerni qotirib qo'yadi.

---

## 10 Ballik Baholash Rubrikasi
- **4 Ball (Baza):** 2D massivda to'siqlarni tekshirib, 4 tomonlama qo'shnilarni to'g'ri filtrlaydi.
- **4 Ball (Amaliy):** FIFO navbati bilan BFS algoritmini to'liq ishga tushirib, eng qisqa yo'lni orqaga tiklay oladi.
- **2 Ball (Challenge):** PATROL / CHASE holatlarini ajratadi va yo'lni har kadrda emas, faqat kerak paytda hisoblovchi 500 ms kesh kiritadi!
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
<title data-ru="Pathfinding & Enemy AI Studio" data-en="Pathfinding & Enemy AI Studio">Pathfinding & Enemy AI Studiyasi: 2D Aqlli Dushman</title>
<link rel="stylesheet" href="../../../../assets/brand.css">
<style>
:root {
  --bg-dark: #090d16;
  --surface-panel: #111827;
  --surface-border: #1f2937;
  --accent-blue: #3b82f6;
  --accent-green: #10b981;
  --accent-purple: #a855f7;
  --accent-red: #ef4444;
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
  background: rgba(168,85,247,0.15);
  color: var(--accent-purple);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-family: monospace;
}
.main-grid {
  flex: 1;
  display: grid;
  grid-template-columns: 1fr 340px;
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
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.arena-view {
  flex: 1;
  background: #050811;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}
canvas {
  background: #020617;
  box-shadow: 0 0 20px rgba(0,0,0,0.5);
  border: 1px solid #1e293b;
  border-radius: 6px;
  cursor: crosshair;
}
.sidebar-body {
  flex: 1;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  overflow-y: auto;
}
.btn {
  background: var(--accent-blue);
  color: #fff;
  border: none;
  padding: 8px 14px;
  border-radius: 6px;
  font-weight: 700;
  font-size: 11px;
  cursor: pointer;
}
.btn:hover { opacity: 0.9; }
.btn-purple {
  background: var(--accent-purple);
}
.btn-red {
  background: var(--accent-red);
}
.telemetry-card {
  background: #0b1120;
  border: 1px solid #1e293b;
  border-radius: 6px;
  padding: 10px;
  font-family: monospace;
  font-size: 11px;
  line-height: 1.6;
}
</style>
</head>
<body>

<header>
  <div class="brand-title">
    <span>Target International School</span>
    <span class="badge-tech">BFS PATHFINDER v1.2</span>
    <span data-ru="Лаборатория ИИ Врагов" data-en="Enemy AI Lab">Dushman AI va Pathfinding Studiyasi</span>
  </div>
  <div style="font-size:11px; color:#94a3b8; font-family:monospace;">
    <span data-ru="Алгоритм:" data-en="Algorithm:">Algoritm:</span> <strong style="color:var(--accent-purple);">Breadth-First Search (FIFO)</strong>
  </div>
  <div style="display:flex; gap:8px;">
    <button class="btn btn-purple" onclick="triggerBfsStep()" data-ru="▶️ Шаг Поиска" data-en="▶️ Single Step">▶️ 1 Qadam</button>
    <button class="btn" onclick="startContinuousChase()" data-ru="⚡ Авто-Погоня" data-en="⚡ Auto Chase">⚡ Jonli Quvish</button>
    <button class="btn btn-red" onclick="resetGrid()" data-ru="Сброс" data-en="Reset">Tozalash</button>
  </div>
</header>

<div class="main-grid">
  <!-- ARENA CANVAS -->
  <div class="panel">
    <div class="panel-header">
      <span data-ru="2D АРЕНА (КЛИКАЙТЕ ПО КЛЕТКАМ ДЛЯ ПОСТРОЙКИ СТЕН)" data-en="2D ARENA (CLICK CELLS TO BUILD WALLS)">2D LABIRINT MAYDONI (DEVOR QURISH UCHUN KATAKLARGA BOSING)</span>
      <span style="color:#64748b; font-size:10px;">Grid: 16x16 Tiles</span>
    </div>
    <div class="arena-view">
      <canvas id="arenaCanvas" width="480" height="480"></canvas>
    </div>
  </div>

  <!-- SIDEBAR CONTROLS & TELEMETRY -->
  <div class="panel">
    <div class="panel-header">
      <span data-ru="ТЕЛЕМЕТРИЯ И УПРАВЛЕНИЕ ИИ" data-en="AI TELEMETRY & CONTROLS">AI TELEMETRIYA VA BOSHQARUV</span>
      <span id="aiStateBadge" style="color:var(--accent-green); font-size:10px; font-weight:700;">State: CHASE</span>
    </div>
    <div class="sidebar-body">
      <div class="telemetry-card">
        <div style="color:var(--accent-purple); font-weight:700; margin-bottom:4px;" data-ru="Состояние Дроида (State Machine):" data-en="Drone State Machine:">Dushman Holati (FSM):</div>
        <div><span data-ru="Дистанция до цели:" data-en="Target distance:">Nishongacha masofa:</span> <strong id="telDist" style="color:#38bdf8;">0 katak</strong></div>
        <div><span data-ru="Текущий статус:" data-en="Current mode:">Joriy rejim:</span> <strong id="telMode" style="color:var(--accent-green);">CHASE (Quvish)</strong></div>
        <div><span data-ru="Длина маршрута:" data-en="Path length:">Eng qisqa yo'l:</span> <strong id="telPathLen" style="color:#eab308;">0 qadam</strong></div>
        <div><span data-ru="Исследовано клеток:" data-en="Explored nodes:">Tekshirilgan kataklar:</span> <strong id="telExplored" style="color:#94a3b8;">0</strong></div>
      </div>

      <div class="telemetry-card" style="background:#090d16;">
        <div style="color:var(--accent-blue); font-weight:700; margin-bottom:4px;" data-ru="Управление Элементами:" data-en="Element Controls:">Qahramonlar va Nishon:</div>
        <div style="font-size:10px; color:#cbd5e1; line-height:1.6;">
          <div>🟣 <strong>Siyohrang:</strong> Dushman Droidi (Bot)</div>
          <div>🟢 <strong>Yashil:</strong> O'yinchi (Player)</div>
          <div>⬛ <strong>Kulrang:</strong> Devorlar (To'siqlar)</div>
          <div>🟦 <strong>Moviy chiziq:</strong> BFS eng qisqa yo'li</div>
        </div>
      </div>

      <div style="font-size:11px; color:#64748b; line-height:1.5;">
        <span data-ru="💡 Подсказка: Кликните и потяните мышь по арене, чтобы нарисовать извилистый лабиринт. Дроид мгновенно найдет кратчайший путь в обход стен!" data-en="💡 Tip: Click and drag on the arena to draw intricate mazes. The drone instantly routes around barriers via BFS!">💡 Maslahat: Arena ustida sichqoncha bilan devorlar chizing. Dushman BFS to'lqini orqali devorlarni aylanib o'tuvchi yo'lni darhol topadi!</span>
      </div>
    </div>
  </div>
</div>

<script>
var COLS = 16;
var ROWS = 16;
var grid = [];
for (var r = 0; r < ROWS; r++) {
  grid[r] = [];
  for (var c = 0; c < COLS; c++) {
    grid[r][c] = 0;
  }
}

// Preset walls
for (var i = 3; i < 13; i++) {
  grid[5][i] = 1;
  grid[10][i] = 1;
}
grid[5][8] = 0; // Door 1
grid[10][8] = 0; // Door 2

var botPos = {x: 2, y: 2};
var playerPos = {x: 13, y: 13};
var isChasing = false;
var chaseTimer = null;

var cvs = document.getElementById('arenaCanvas');
var ctx = cvs.getContext('2d');
var TILE_SIZE = cvs.width / COLS;

var isMouseDown = false;
cvs.addEventListener('mousedown', function(e) {
  isMouseDown = true;
  toggleTile(e);
});
window.addEventListener('mouseup', function() { isMouseDown = false; });
cvs.addEventListener('mousemove', function(e) {
  if (isMouseDown) toggleTile(e);
});

function toggleTile(e) {
  var rect = cvs.getBoundingClientRect();
  var c = Math.floor((e.clientX - rect.left) / TILE_SIZE);
  var r = Math.floor((e.clientY - rect.top) / TILE_SIZE);
  if (c >= 0 && c < COLS && r >= 0 && r < ROWS) {
    if ((c === botPos.x && r === botPos.y) || (c === playerPos.x && r === playerPos.y)) return;
    grid[r][c] = 1;
    drawScene();
  }
}

function calculateBFS() {
  var queue = [[botPos.x, botPos.y]];
  var visited = {};
  var parent = {};
  var startKey = botPos.x + ',' + botPos.y;
  visited[startKey] = true;

  var found = false;
  var exploredCount = 0;
  var dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]];

  while (queue.length > 0) {
    var curr = queue.shift();
    exploredCount++;
    var cx = curr[0];
    var cy = curr[1];

    if (cx === playerPos.x && cy === playerPos.y) {
      found = true;
      break;
    }

    for (var i = 0; i < 4; i++) {
      var nx = cx + dirs[i][0];
      var ny = cy + dirs[i][1];
      var key = nx + ',' + ny;

      if (nx >= 0 && nx < COLS && ny >= 0 && ny < ROWS && grid[ny][nx] === 0 && !visited[key]) {
        visited[key] = true;
        parent[key] = cx + ',' + cy;
        queue.push([nx, ny]);
      }
    }
  }

  var path = [];
  if (found) {
    var currK = playerPos.x + ',' + playerPos.y;
    while (currK && currK !== startKey) {
      var parts = currK.split(',');
      path.push({x: parseInt(parts[0]), y: parseInt(parts[1])});
      currK = parent[currK];
    }
    path.reverse();
  }

  return {path: path, explored: exploredCount, found: found};
}

function drawScene(pathResult) {
  if (!pathResult) pathResult = calculateBFS();
  ctx.clearRect(0, 0, cvs.width, cvs.height);

  // 1. Draw Grid Tiles
  for (var r = 0; r < ROWS; r++) {
    for (var c = 0; c < COLS; c++) {
      if (grid[r][c] === 1) {
        ctx.fillStyle = '#334155';
      } else {
        ctx.fillStyle = '#0f172a';
      }
      ctx.fillRect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1);
    }
  }

  // 2. Draw Shortest Path
  if (pathResult && pathResult.path.length > 0) {
    ctx.strokeStyle = '#06b6d4';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(botPos.x * TILE_SIZE + TILE_SIZE/2, botPos.y * TILE_SIZE + TILE_SIZE/2);
    for (var i = 0; i < pathResult.path.length; i++) {
      var pt = pathResult.path[i];
      ctx.lineTo(pt.x * TILE_SIZE + TILE_SIZE/2, pt.y * TILE_SIZE + TILE_SIZE/2);
    }
    ctx.stroke();
  }

  // 3. Draw Bot (Purple)
  ctx.fillStyle = '#a855f7';
  ctx.beginPath();
  ctx.arc(botPos.x * TILE_SIZE + TILE_SIZE/2, botPos.y * TILE_SIZE + TILE_SIZE/2, TILE_SIZE/2.5, 0, Math.PI * 2);
  ctx.fill();

  // 4. Draw Player (Green)
  ctx.fillStyle = '#10b981';
  ctx.beginPath();
  ctx.arc(playerPos.x * TILE_SIZE + TILE_SIZE/2, playerPos.y * TILE_SIZE + TILE_SIZE/2, TILE_SIZE/2.5, 0, Math.PI * 2);
  ctx.fill();

  // Update Telemetry
  var dist = Math.abs(playerPos.x - botPos.x) + Math.abs(playerPos.y - botPos.y);
  document.getElementById('telDist').textContent = dist + ' katak (Manxetten)';
  document.getElementById('telPathLen').textContent = pathResult.path.length + ' qadam';
  document.getElementById('telExplored').textContent = pathResult.explored + ' ta katak';

  var modeEl = document.getElementById('telMode');
  var badgeEl = document.getElementById('aiStateBadge');
  if (dist <= 1) {
    modeEl.textContent = 'ATTACK (Zarba berish)';
    modeEl.style.color = 'var(--accent-red)';
    badgeEl.textContent = 'State: ATTACK';
    badgeEl.style.color = 'var(--accent-red)';
  } else if (dist <= 10) {
    modeEl.textContent = 'CHASE (Quvish)';
    modeEl.style.color = 'var(--accent-green)';
    badgeEl.textContent = 'State: CHASE';
    badgeEl.style.color = 'var(--accent-green)';
  } else {
    modeEl.textContent = 'PATROL (Patrul)';
    modeEl.style.color = '#94a3b8';
    badgeEl.textContent = 'State: PATROL';
    badgeEl.style.color = '#94a3b8';
  }
}

function triggerBfsStep() {
  var res = calculateBFS();
  if (res.path.length > 0) {
    botPos.x = res.path[0].x;
    botPos.y = res.path[0].y;
  }
  drawScene();
}

function startContinuousChase() {
  if (isChasing) {
    clearInterval(chaseTimer);
    isChasing = false;
    return;
  }
  isChasing = true;
  chaseTimer = setInterval(function() {
    triggerBfsStep();
    var dist = Math.abs(playerPos.x - botPos.x) + Math.abs(playerPos.y - botPos.y);
    if (dist <= 1) {
      clearInterval(chaseTimer);
      isChasing = false;
    }
  }, 300);
}

function resetGrid() {
  if (isChasing) clearInterval(chaseTimer);
  isChasing = false;
  for (var r = 0; r < ROWS; r++) {
    for (var c = 0; c < COLS; c++) {
      grid[r][c] = 0;
    }
  }
  botPos = {x: 1, y: 1};
  playerPos = {x: 14, y: 14};
  drawScene();
}

drawScene();
</script>

</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "simulator", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: simulator/index.html")

def main():
    print("📦 Building 7-8-sinf (Lesson 34: Enemy AI & Pathfinding: Obstacle Avoidance)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_simulator()
    print("🎉 Done! Generated Grade 7–8 Lesson 34.")

if __name__ == "__main__":
    main()
