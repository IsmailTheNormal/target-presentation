#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_7_8_w11_l33.py — Builder for 7–8th Grade, Week 11, Lesson 33

Mavzu: Dushman AI va Pathfinding: A* (A-Star) va BFS To'siqlarni Aylanib Quvish Algoritmi
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 7-8-sinf (Vibecoding & Game Dev Track)
Pedagogika: VIBECODING — Prompt arxitekturasi, bosqichma-bosqich so'rov berish,
            to'siqqa tiqilish xatosini fosh qilish (critic prompt), BFS vs A*, va sight cone.
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "7-8-sinf", "11-hafta", "33-dars-dushman-ai-va-pathfinding")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "simulator"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides for 80-min Double Block)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="7–8-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 33" data-en="GRADES 7–8 · WEEK 11 · LESSON 33">7–8-SINF · 11-HAFTA · 33-DARS</span></div>
    <h1 class="display" data-ru="ИИ Врагов и Pathfinding: Алгоритмы A* и BFS для Обхода Препятствий" data-en="Enemy AI & Pathfinding: A* and BFS Obstacle Navigation">Dushman AI va Pathfinding: A* va BFS Algoritmlari</h1>
    <p class="lede" data-ru="Как заставить монстров подземелья находить кратчайший путь к герою в обход каменных стен: алгоритм поиска в ширину (BFS), эвристика A* (Манхэттенское расстояние) и конусы видимости через Vibecoding." data-en="How to program dungeon monsters to navigate around stone walls towards the hero: Breadth-First Search (BFS), A* heuristics (Manhattan distance), and vision cones via Vibecoding.">Labirint dushmanlarini tosh devorlarni aylanib o'tib, qahramonni eng qisqa yo'l bilan quvlashga o'rgatamiz: BFS algoritmi, A* evristikasi (Manhattan masofasi) va ko'rish nuri fizikasini Vibecoding orqali yaratish.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Умный Интеллект Врагов" data-en="Intelligent Enemy AI">Aqlli Dushman AI</h3>
        <p data-ru="От глупых врагов, застревающих в углах, к умным хищникам, просчитывающим кратчайший маршрут по сетке тайлов." data-en="Moving from dumb wall-stuck enemies to smart predators calculating shortest tile paths.">Burchakda tiqilib qoluvchi sodda dushmandan kataklar bo'ylab eng optimal yo'lni hisoblovchi aqlli yirtqich AI ga o'tish.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">A* Pathfinding Lab</div>
        <h3 data-ru="Боевой Модуль Навигации" data-en="Navigation Module">Navigatsiya Dvigateli</h3>
        <p data-ru="Каждый ученик встроит в свой Roguelike алгоритм A* с визуализацией пути и переключением состояний PATROL / CHASE." data-en="Each student integrates an A* pathfinding engine with route visualizer and PATROL / CHASE states.">Har bir o'quvchi o'z o'yiniga A* algoritmi, yashil yo'l chizig'i va PATROL / CHASE holatlarini qo'shadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="РАЗБОР ДОМАШНЕГО ЗАДАНИЯ И МОСТ" data-en="HOMEWORK REVIEW & BRIDGE">UY VAZIFASI TAHLILI VA KO'PRIK</span></div>
    <h2 data-ru="Ошибки Баллистики и Мост к Интеллекту Врагов" data-en="Ballistics Pitfalls & Bridge to Enemy Pathfinding">32-Dars Xatolari va Bugungi Yangi Dushman AI ga Ko'prik</h2>
    <div class="grid-2">
      <div>
        <div class="box" style="border-left:4px solid var(--red); margin-bottom:10px;">
          <h4 style="color:var(--red);" data-ru="Типичная Ошибка (Pitfall): Утечка Памяти при Стрельбе" data-en="Common Pitfall: Bullet Memory Leak">Keng Tarqalgan Xato: O'qlarning Xotiradan O'chmasligi</h4>
          <p style="font-size:12px; margin-bottom:4px;" data-ru="Многие удаляли пули прямым циклом for(i=0..len), из-за чего часть пуль пропускалась и игра зависала через 50 выстрелов." data-en="Using a forward loop for(i=0..len) skipped items on splice(), leaking hundreds of off-screen bullets.">To'g'ri for-loop da <code>splice()</code> ishlatilganda indekslar surilib, ba'zi o'qlar xotirada qolib ketgan edi. Faqat <strong>teskari sikl</strong> (<code>length-1 dan 0 gacha</code>) xavfsiz tozalaydi!</p>
        </div>
        <div class="box" style="border-left:4px solid var(--green);">
          <h4 style="color:var(--green);" data-ru="Золотой Стандарт (Golden Standard)" data-en="Golden Standard">Oltin Yechim Standarti</h4>
          <pre style="font-size:11px; margin:0;"><code>for (let i = bullets.length - 1; i &gt;= 0; i--) {
  if (isOutOfBounds(bullets[i]) || hitWall(bullets[i])) {
    bullets.splice(i, 1); // Indeks buzilmaydi!
  }
}</code></pre>
        </div>
      </div>
      <div>
        <div class="box" style="background:var(--surface-2); margin-bottom:10px;">
          <h4 style="color:var(--accent);" data-ru="30-Секундный Блиц-Вопрос" data-en="30-Second Blitz Question">30 Soniyalik Blitz Savol</h4>
          <p style="font-size:12px; margin-bottom:8px;" data-ru="Если враг просто делает enemy.x += (hero.x - enemy.x), что произойдет, когда между ними встанет каменная стена?" data-en="If enemy simply steps via enemy.x += dx, what happens when a solid stone wall stands between them?">Agar dushman to'g'ridan-to'g'ri qahramon tomon borsa (`x += dx`), o'rtada tosh devor tursa nima bo'ladi?</p>
          <div style="font-weight:700; color:var(--red); font-size:13px;" data-ru="Ответ: Он навсегда уткнется в стену и застрянет как сломанный робот!" data-en="Answer: It gets permanently stuck in the wall and vibrates helplessly!">Javob: U devorga urilib, abadiy qotib qoladi va qahramonga yetib borolmaydi!</div>
        </div>
        <div class="box" style="border-left:4px solid var(--purple);">
          <h4 style="color:var(--purple);" data-ru="Мост к Новой Теме" data-en="Bridge to Today's Theme">Bugungi Yangi Mavzuga Ko'prik</h4>
          <p style="font-size:12px; margin:0;" data-ru="Герой уже умеет стрелять, но неподвижные мишени — это скучно! Сегодня мы оживим монстров и научим их обходить любые лабиринты с помощью графов и алгоритма A*!" data-en="Our hero can shoot, but dummy targets are boring! Today we bring monsters alive, teaching them to navigate around labyrinth walls via A*!">Endi qahramonimiz qurolga ega. Bugun dushmanlarni aqlli qilib, labirint devorlarini aylanib o'tishni o'rgatamiz!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: DIRECT CHASE TRAP -->
  <section class="slide" data-phase="To'g'ridan-to'g'ri Ta'qib|Прямое Преследование|Direct Chase" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="АРХИТЕКТУРА ИИ: ЛОВУШКА ПРЯМОГО ХОДА" data-en="AI ARCHITECTURE: DIRECT CHASE TRAP">SODDA DUSHMANNING TUZOG'I</span></div>
    <h2 data-ru="Почему Наивный ИИ Не Работает в Подземельях?" data-en="Why Naive AI Fails Miserably in Dungeons">Nega Oddiy Dushman Labirintda Qotib Qoladi?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Большинство начинающих разработчиков пишут наивный код прямого следования:" data-en="Most beginner game devs write naive direct chasing code:">Ko'pchilik boshlang'ich dasturchilar dushmanga to'g'ri yo'nalish kodini yozadi:</p>
        <ul class="clean-list">
          <li data-ru="<strong>Шаг 1:</strong> Если hero.x &gt; enemy.x, делаем enemy.x += speed." data-en="<strong>Step 1:</strong> If hero.x &gt; enemy.x, step enemy.x += speed."><strong>1-Qadam:</strong> Agar hero.x &gt; enemy.x bo'lsa, o'ngga yur.</li>
          <li data-ru="<strong>Шаг 2:</strong> Если hero.y &gt; enemy.y, делаем enemy.y += speed." data-en="<strong>Step 2:</strong> If hero.y &gt; enemy.y, step enemy.y += speed."><strong>2-Qadam:</strong> Agar hero.y &gt; enemy.y bo'lsa, pastga yur.</li>
          <li data-ru="<strong>Катастрофа:</strong> Появляется Т-образная стена. Дushman упирается в препятствие и дрожит на месте!" data-en="<strong>Disaster:</strong> A T-shaped wall appears. The enemy slams into it and vibrates endlessly!"><strong>Xatolik:</strong> O'rtada bitta devor paydo bo'lishi bilan dushman qotib qoladi!</li>
        </ul>
      </div>
      <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); font-family:var(--font-mono); font-size:12px;">
        <div style="color:var(--red); margin-bottom:8px;">// Sodda xato yondashuv (Dumb AI)</div>
        <div>function naiveChase(enemy, hero) {</div>
        <div style="padding-left:14px; color:#94a3b8;">const dx = hero.x - enemy.x;</div>
        <div style="padding-left:14px; color:#94a3b8;">const dy = hero.y - enemy.y;</div>
        <div style="padding-left:14px; color:var(--yellow);">// Agar oldinda devor bo'lsa nima bo'ladi?</div>
        <div style="padding-left:14px; color:var(--red);">enemy.x += Math.sign(dx) * enemy.speed;</div>
        <div style="padding-left:14px; color:var(--red);">enemy.y += Math.sign(dy) * enemy.speed;</div>
        <div style="padding-left:14px; color:#94a3b8;">// QOTIB QOLADI! Devor orqasini ko'rolmaydi.</div>
        <div>}</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: GRID GRAPH REPRESENTATION -->
  <section class="slide" data-phase="Labirint Kataklari|Сетка и Графы|Grid Graph" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="ТЕОРИЯ ГРАФОВ В ИГРАХ" data-en="GRAPH THEORY IN GAMES">LABIRINT KATAKLARI VA GRAFLAR</span></div>
    <h2 data-ru="Превращаем Карту в Граф: Сетка 20x13 Тайлов" data-en="Converting Tilemaps into Graphs: 20x13 Grid Nodes">Xaritani Grafga Aylantirish: 20x13 Katakli Grid</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Чтобы компьютер мог найти дорогу, мы превращаем экран в шахматную доску узлов (Nodes):" data-en="To enable algorithmic navigation, we discretize the canvas into a graph grid:">Dushman yo'lni topishi uchun ekran kataklar to'riga (Grid Graph) bo'linadi:</p>
        <ul class="clean-list">
          <li data-ru="<strong>Узел (Node):</strong> Каждая клетка имеет координаты (col, row)." data-en="<strong>Node:</strong> Each tile has integer coordinates (col, row)."><strong>Tugun (Katak):</strong> Har bir katak (col, row) butun sonli manzilga ega.</li>
          <li data-ru="<strong>0 (Проходимо):</strong> Пол подземелья, по которому можно идти." data-en="<strong>0 (Walkable):</strong> Open floor tile where monsters can walk freely."><strong>0 (O'tish mumkin):</strong> Bo'sh pol, qadam tashlash mumkin.</li>
          <li data-ru="<strong>1 (Препятствие):</strong> Каменная стена, куда заходить запрещено." data-en="<strong>1 (Blocked):</strong> Impassable solid stone obstacle."><strong>1 (Tosh devor):</strong> To'siq, bu katakka kirish taqiqlangan.</li>
          <li data-ru="<strong>Соседи (Neighbors):</strong> Из текущей клетки можно шагнуть в 4 стороны: Вверх, Вниз, Влево, Вправо." data-en="<strong>Neighbors:</strong> 4 orthogonal moves available: Up, Down, Left, Right."><strong>4 Qo'shni:</strong> Yuqoriga, Pastga, Chapga, O'ngga.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
        <div style="font-size:44px; margin-bottom:8px;">🗺️ 🧭 🧱</div>
        <h4 data-ru="Формула Координат Тайла" data-en="Tile Coordinate Formula">Pikseldan Katakka O'tish</h4>
        <pre style="font-size:11px; margin:0; text-align:left;"><code>const col = Math.floor(pixelX / TILE_SIZE);
const row = Math.floor(pixelY / TILE_SIZE);</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: BREADTH-FIRST SEARCH (BFS) -->
  <section class="slide" data-phase="BFS Qidiruv|Поиск в Ширину BFS|BFS Pathfinding" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="БАЗОВЫЙ АЛГОРИТМ НАВИГАЦИИ" data-en="CORE NAVIGATION ALGORITHM">BFS: KENGAYTIRILGAN QIDIRUV</span></div>
    <h2 data-ru="BFS (Breadth-First Search): Волна Поиска во Все Стороны" data-en="BFS (Breadth-First Search): Expanding Wave Search">BFS: To'lqinsimon Qidiruv va Eng Qisqa Yo'l</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="BFS распространяется как круги на воде от брошенного камня:" data-en="BFS expands like water ripples from where a stone was tossed:">BFS xuddi suvga tosh otgandek har tomonga bir tekis to'lqin bo'lib tarqaladi:</p>
        <ul class="clean-list">
          <li data-ru="<strong>Очередь (Queue):</strong> Структура данных FIFO (First-In, First-Out)." data-en="<strong>Queue:</strong> First-In, First-Out (FIFO) data structure."><strong>Navbat (Queue):</strong> Birinchi kirgan birinchi chiqadi (FIFO).</li>
          <li data-ru="<strong>Visited (Посещено):</strong> Множество клеток, чтобы не ходить по кругу." data-en="<strong>Visited:</strong> Hash set recording checked tiles to prevent endless loops."><strong>Visited to'plami:</strong> Bir xil katakka qayta kirmaslik kafolati.</li>
          <li data-ru="<strong>Гарантия:</strong> Всегда находит кратчайший путь в невзвешенной сетке!" data-en="<strong>Guarantee:</strong> Guaranteed to find shortest route in unweighted grids!"><strong>Kafolat:</strong> Har doim eng qisqa qadamlar sonini topadi!</li>
          <li data-ru="<strong>Минус:</strong> Ищет во все стороны вслепую, тратя процессор." data-en="<strong>Drawback:</strong> Explores all directions blindly, wasting CPU cycles."><strong>Kamchiligi:</strong> Keraksiz tomonga ham ko'r-ko'rona tarqaladi.</li>
        </ul>
      </div>
      <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); font-family:var(--font-mono); font-size:11px;">
        <div style="color:var(--accent);">// BFS ning asosiy sikli</div>
        <div>const queue = [startNode];</div>
        <div>const visited = new Set();</div>
        <div style="color:var(--yellow);">while (queue.length &gt; 0) {</div>
        <div style="padding-left:14px;">const current = queue.shift();</div>
        <div style="padding-left:14px; color:var(--green);">if (current == target) break; // Topildi!</div>
        <div style="padding-left:14px;">for (const neighbor of getWalkableNeighbors(current)) {</div>
        <div style="padding-left:28px;">if (!visited.has(neighbor)) {</div>
        <div style="padding-left:42px;">visited.add(neighbor);</div>
        <div style="padding-left:42px;">queue.push(neighbor);</div>
        <div style="padding-left:28px;">}</div>
        <div style="padding-left:14px;">}</div>
        <div style="color:var(--yellow);">}</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: A* (A-STAR) & MANHATTAN HEURISTIC -->
  <section class="slide" data-phase="A* Evristikasi|Эвристика A*|A* Algorithm" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ЗОЛОТОЙ СТАНДАРТ ГЕЙМДЕВА" data-en="GOLD STANDARD OF GAMEDEV">A* (A-STAR) EVRISTIKASI</span></div>
    <h2 data-ru="A* (A-Star): Умный Поиск с Формулой f = g + h" data-en="A* (A-Star): Guided Search with f = g + h">A* Algoritmi: Aqlli Qidiruv va f = g + h</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="В отличие от слепого BFS, алгоритм A* знает, в какой стороне находится цель, благодаря эвристике:" data-en="Unlike blind BFS, A* is directed towards the target via heuristic score:">BFS ko'r-ko'rona qidirsa, A* maqsad qaysi tomondaligini bilib, faqat to'g'ri tomonga intiladi:</p>
        <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); font-family:var(--font-mono); font-size:12px; margin-bottom:8px;">
          <div style="color:var(--accent); font-weight:700;">f(n) = g(n) + h(n)</div>
          <div style="color:#94a3b8; font-size:11px;">g(n): Boshlang'ich nuqtadan yurilgan qadamlar soni</div>
          <div style="color:var(--yellow); font-size:11px;">h(n): Qahramongacha qolgan taxminiy masofa (Heuristic)</div>
          <div style="color:var(--green); font-size:11px;">f(n): Umumiy baho (eng kichik f(n) birinchi tekshiriladi)</div>
        </div>
      </div>
      <div>
        <div class="box" style="border-left:4px solid var(--accent); margin-bottom:10px;">
          <h4 data-ru="Манхэттенское Расстояние (Manhattan Distance)" data-en="Manhattan Distance Formula">Manhattan Masofasi Formulasi</h4>
          <pre style="font-size:11px; margin:4px 0;"><code>function manhattan(a, b) {
  return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
}</code></pre>
          <p style="font-size:11px; color:var(--ink-2); margin:0;" data-ru="Названо в честь сетки улиц Манхэттена, где нельзя летать сквозь небоскребы по диагонали." data-en="Named after Manhattan street grids where cabs navigate along orthogonal blocks.">Nyu-York ko'chalaridek: binolarni teshib o'tib bo'lmaydi, faqat to'g'ri burchakli bloklar bo'ylab hisoblanadi.</p>
        </div>
        <div class="box" style="border-left:4px solid var(--green);">
          <span style="font-weight:700; color:var(--green); font-size:12px;" data-ru="⚡ Результат: A* работает в 5–10 раз быстрее BFS!" data-en="⚡ Result: A* searches 5–10x fewer nodes than BFS!">⚡ Natija: A* butun xaritani emas, faqat maqsad tomon kataklarni tekshiradi va 5-10 barobar tezroq ishlaydi!</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: ENEMY STATE MACHINE & SIGHT CONE -->
  <section class="slide" data-phase="Dushman Holatlari|Состояния Врага (FSM)|Enemy States" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ПАТРОЛИРОВАНИЕ И ТРЕВОГА" data-en="PATROL, ALERT & CHASE">DUSHMAN HOLATLARI VA KO'RISH NURI</span></div>
    <h2 data-ru="Конечный Автомат (FSM): Патруль ➔ Тревога ➔ Погоня" data-en="Finite State Machine: PATROL ➔ ALERT ➔ CHASE">Dushman Holatlari: PATROL ➔ ALERT ➔ CHASE</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1. PATROL</div>
        <h4 data-ru="Патрулирование" data-en="Patrol Mode">Sokin Patrul</h4>
        <p style="font-size:12px;" data-ru="Монстр медленно ходит между 2 точками (A и B). Скорость 1x. Конус обзора синий." data-en="Enemy wanders between predefined waypoints at 1x speed. Blue vision cone.">Dushman belgilangan 2 ta nuqta orasida sokin aylanadi. Tezligi 1x, ko'rish nuri ko'k rangda.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(245,158,11,0.15); color:var(--yellow);">2. ALERT</div>
        <h4 data-ru="Подозрение (!)" data-en="Alert State (!)">Shubha va Xavf (!)</h4>
        <p style="font-size:12px;" data-ru="Услышал выстрел или заметил краешком глаза. Над головой загорается желтый знак '?'." data-en="Detects gun sound or peripheral movement. Yellow '?' mark flashes.">O'q ovozini eshitdi yoki qahramon qisman ko'rindi. Boshida sariq '?' belgisi yonadi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);">3. CHASE</div>
        <h4 data-ru="Яростная Погоня" data-en="Full Chase">Qizil Ta'qib!</h4>
        <p style="font-size:12px;" data-ru="Включается алгоритм A*. Скорость 1.8x. Монстр бежит по кратчайшему пути к герою!" data-en="A* pathfinding triggers. Speed jumps to 1.8x. Monster sprints to player!">A* algoritmi ishga tushadi! Tezlik 1.8x ga oshadi, dushman eng qisqa yo'l bilan quvlaydi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: IN-DECK INTERACTIVE SIMULATOR -->
  <section class="slide" data-phase="Smartboard Simulyatori|Интерактив на Доске|In-Deck Simulator" data-time="40:00–48:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="СИМУЛЯТОР НА СМАРТБОРДЕ" data-en="SMARTBOARD PATHFINDING">SMARTBOARD PATHFINDING ARENASI</span></div>
    <h2 data-ru="Протестируйте Алгоритм A* Прямо на Доске!" data-en="Test A* Pathfinding Right on the Smartboard!">Doskada Jonli A* Yo'l Topish Dvigatelini Sinang!</h2>
    <div style="display:grid; grid-template-columns: 1fr 280px; gap:14px; align-items:start;">
      <div style="background:#020617; border-radius:8px; border:2px solid var(--accent); position:relative; overflow:hidden; height:260px;" id="deckPathWrapper">
        <canvas id="deckPathCanvas" width="460" height="260" style="display:block; width:100%; height:100%; cursor:pointer;"></canvas>
      </div>
      <div class="box" style="display:flex; flex-direction:column; gap:8px;">
        <div style="display:flex; justify-content:space-between; font-weight:700; font-size:12px;">
          <span>👣 Yo'l Uzunligi: <strong id="deckPathSteps" style="color:var(--green);">0</strong></span>
          <span>🔍 Tekshirildi: <strong id="deckExploredNodes" style="color:var(--accent);">0</strong></span>
        </div>
        <div style="font-size:11px; color:var(--ink-2); line-height:1.4;">
          <strong>Boshqaruv:</strong> Maydonga bosing — devor qo'shing yoki o'chiring. Qahramon va dushman o'rtasidagi yashil A* yo'lini kuzating!
        </div>
        <button class="btn" onclick="deckToggleAlgo()" id="btnDeckAlgo" style="font-size:11px; background:var(--accent); color:#000; font-weight:700;" data-ru="Режим: A* (Умный Поиск)" data-en="Mode: A* (Smart Heuristic)">Rejim: A* (Evristik)</button>
        <button class="btn" onclick="deckResetGrid()" style="font-size:11px; background:var(--surface-2); border:1px solid var(--hair);" data-ru="🔄 Сбросить Стены" data-en="🔄 Reset Walls">🔄 Devorlarni Tiklash</button>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: INTERACTIVE QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Quiz" data-time="48:00–55:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА ЗНАНИЙ" data-en="KNOWLEDGE CHECK">KIBER-VIKTORINA</span></div>
    <h2 data-ru="3 Вопроса по Алгоритмам A* и BFS" data-en="3 Questions on A* & BFS Pathfinding">Pathfinding Bo'yicha 3 Ta Nazorat Savoli</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:var(--accent); color:#000;">1-Savol</div>
        <p style="font-size:12px; margin-bottom:10px;" data-ru="Какая структура данных лежит в основе алгоритма BFS?" data-en="Which data structure powers the BFS algorithm?">BFS algoritmining asosi qaysi ma'lumotlar tuzilmasiga tayanadi?</p>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! BFS birinchi kirgan birinchi chiqadigan Queue (Navbat) dan foydalanadi.')" style="font-size:11px;" data-ru="A) Очередь (Queue / FIFO)" data-en="A) Queue (FIFO)">A) Navbat (Queue / FIFO)</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri. Stack DFS (Depth-First) da ishlatiladi.')" style="font-size:11px;" data-ru="B) Стек (Stack / LIFO)" data-en="B) Stack (LIFO)">B) Stek (Stack / LIFO)</button>
        </div>
      </div>
      <div class="box">
        <div class="tag" style="background:var(--purple); color:#fff;">2-Savol</div>
        <p style="font-size:12px; margin-bottom:10px;" data-ru="Что означает буква h в формуле A*: f(n) = g(n) + h(n)?" data-en="What does 'h' represent in the A* formula f = g + h?">A* dagi f(n) = g(n) + h(n) formulasida 'h' harfi nimani anglatadi?</p>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! h(n) — maqsadgacha bo‘lgan evristik (taxminiy) masofa.')" style="font-size:11px;" data-ru="A) Эвристика (расстояние до цели)" data-en="A) Heuristic distance to target">A) Evristika (maqsadgacha masofa)</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri. Harakat tezligi alohida parametr.')" style="font-size:11px;" data-ru="B) Высота препятствия (Height)" data-en="B) Obstacle height">B) To'siq balandligi</button>
        </div>
      </div>
      <div class="box">
        <div class="tag" style="background:var(--green); color:#fff;">3-Savol</div>
        <p style="font-size:12px; margin-bottom:10px;" data-ru="Почему Манхэттенское расстояние идеально подходит для сетки без диагоналей?" data-en="Why is Manhattan distance ideal for orthogonal 4-way tile grids?">Nega 4 tomonlama katakli o'yinlarda Manhattan masofasi eng yaxshi evristika?</p>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! Kataklar bo‘ylab faqat gorizontal va vertikal yuriladi (|dx| + |dy|).')" style="font-size:11px;" data-ru="A) Движение идет строго по осям X и Y" data-en="A) Movement is strictly along X & Y">A) Harakat faqat X va Y o'qlari bo'ylab</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri. Diagonallar uchun Evklid masofasi kerak bo‘ladi.')" style="font-size:11px;" data-ru="B) Потому что оно считает корни" data-en="B) Because it uses square roots">B) Ildiz hisoblagani uchun</button>
        </div>
      </div>
    </div>
    <div id="quizFeedback" style="margin-top:10px; font-weight:700; font-size:12px; min-height:18px;"></div>
  </section>

  <!-- SLIDE 10: 25-MIN VIBECODING ARENA -->
  <section class="slide" data-phase="Amaliy Arena|Практическая Арена|Hands-on Arena" data-time="55:00–70:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="VIBECODING АРЕНА (25 МИНУТ)" data-en="VIBECODING ARENA (25 MIN)">VIBECODING AMALIY ARENASI (25 DAQIQA)</span></div>
    <h2 data-ru="Vibecoding: 4 Шага Создания ИИ Монстров с ИИ" data-en="Vibecoding: 4 Real Steps to Engineer Monster AI with AI">Vibecoding: Dushman AI ga 4 Bosqichda Aniq So'rov Berish</h2>
    <div class="grid-2">
      <div>
        <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
          <button class="btn" id="arenaTimerBtn" onclick="toggleArenaTimer()" style="background:var(--accent); color:#000; font-weight:700;" data-ru="⏱️ Запустить Таймер" data-en="⏱️ Start Timer">⏱️ Taymerni Boshlash</button>
          <span id="arenaTimerDisplay" style="font-family:var(--font-mono); font-size:24px; font-weight:700; color:var(--red);">25:00</span>
        </div>
        <p class="lede" style="font-size:13px; margin-bottom:8px;" data-ru="Не пишите алгоритмы графов вручную — будьте AI-Архитекторами! Выполните 4 конкретных промпт-шага:" data-en="Don't code graph algorithms from scratch — act as AI Architects! Execute the 4 prompting milestones:">Graf algoritmlarini qo'lda yozib o'tirmang — AI Arxitektor bo'ling! 4 ta aniq Vibecoding bosqichini bajaring:</p>
        <ul class="clean-list" style="font-size:12px;">
          <li data-ru="<strong>1-й Шаг (6 мин):</strong> Промпт прямого хода: демонстрируем ИИ застревание в стене и формулируем потребность в сетке." data-en="<strong>Step 1 (6 min):</strong> Direct chase prompt: observe wall collision failure and specify grid requirement."><strong>1-Qadam (6 min):</strong> Devorga tiqilish xatosini fosh qilish — AI ga oddiy ta'qib kodi tosh devorga urilib qolganini ko'rsatish.</li>
          <li data-ru="<strong>2-й Шаг (6 мин):</strong> Промпт BFS поиска по сетке: просим алгоритм обхода тайлов с очередью Queue и массивом visited." data-en="<strong>Step 2 (6 min):</strong> Grid BFS prompt: request a tile-based queue pathfinder navigating around obstacle nodes."><strong>2-Qadam (6 min):</strong> Kataklar bo'yicha BFS prompti — AI dan Queue va visited to'plami bilan devorlarni aylanib o'tishni so'rash.</li>
          <li data-ru="<strong>3-й Шаг (7 мин):</strong> Промпт оптимизации A*: внедряем эвристику Манхэттена (|dx| + |dy|), сокращая проверяемые узлы в 5 раз!" data-en="<strong>Step 3 (7 min):</strong> A* optimization prompt: inject Manhattan heuristics (|dx| + |dy|), cutting explored nodes 5x! "><strong>3-Qadam (7 min):</strong> A* Evristika Prompti (Critic) — Ko'r-ko'rona qidiruv o'rniga Manhattan masofasi bilan maqsadga to'g'ri intilishni kiritish.</li>
          <li data-ru="<strong>4-й Шаг (6 мин):</strong> Промпт сочности: конус зрения (Sight Cone), восклицательный знак (!) над головой монстра и ускорение!" data-en="<strong>Step 4 (6 min):</strong> Vibe-Juice Polish: vision raycast, alert icon (!), and berserk speed boost upon sighting!"><strong>4-Qadam (6 min):</strong> Vibe-Juice va Ko'rish Nuri — Dushman ko'rish maydoni (Sight Cone), boshida '!' belgisi va qizil ta'qib tezlanishi.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="font-weight:700; color:var(--accent); margin-bottom:6px;" data-ru="Критерии Оценки (10 Баллов):" data-en="10 Points Rubric:">10 Ballik Baholash Rubrikasi:</div>
          <div style="font-size:11px; line-height:1.6;">
            <div>✅ <strong>4 Ball:</strong> Xarita kataklarga (Grid) bo'lingan va BFS/A* devorlarni xatosiz aylanib o'tadi.</div>
            <div>✅ <strong>4 Ball:</strong> A* algoritmi eng qisqa yo'lni topadi va qahramon harakatlanganda yo'l qayta hisoblanadi.</div>
            <div>✅ <strong>2 Ball:</strong> Dushmanning ko'rish maydoni yoki PATROL / CHASE holatlari chiroyli ulangan!</div>
          </div>
        </div>
        <div style="margin-top:10px; text-align:right;">
          <a href="simulator/index.html" target="_blank" class="btn" style="background:var(--purple); color:#fff; font-size:11px;" data-ru="Открыть Студию Pathfinding" data-en="Launch Pathfinding Studio">Katta Pathfinding Studiyasini Ochish ➔</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: PEER REVIEW -->
  <section class="slide" data-phase="Partadosh Auditi|Взаимный Аудит|Peer Review" data-time="70:00–74:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМНЫЙ АУДИТ НАВИГАЦИИ" data-en="PEER PATHFINDING AUDIT">PARTADOSH AUDITI</span></div>
    <h2 data-ru="Тестируем Интеллект Врага Друга: 4 Контрольные Точки" data-en="Audit Your Peer's Enemy AI: 4 Checkpoints">Do'stingizning Dushman AI Tizimini 4 Mezon Bo'yicha Sinang</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Поменяйтесь местами за партами и устройте стресс-тест интеллекту монстра:" data-en="Swap seats and stress-test your peer's pathfinding implementation:">O'rin almashib, partadoshingizning dushman AI fizikasini sinovdan o'tkazing:</p>
        <ul class="clean-list">
          <li data-ru="<strong>1. Стресс-тест Т-образной стены:</strong> Сможет ли монстр обойти глухой тупик, не застряв?" data-en="<strong>1. T-Wall Stress Test:</strong> Can the monster navigate around a blind dead-end without jamming?"><strong>1. T-devor testi:</strong> Dushman berk ko'chaga kirib qolmasdan devorni aylanib o'tyaptimi?</li>
          <li data-ru="<strong>2. Длина Пути (Optimal):</strong> Выбирает ли алгоритм действительно кратчайший обход?" data-en="<strong>2. Path Optimality:</strong> Does the pathfinder pick the strictly shortest bypass route?"><strong>2. Optimal masofa:</strong> Qidiruv chindan ham eng qisqa yo'lni topayaptimi?</li>
          <li data-ru="<strong>3. Производительность:</strong> Не падает ли FPS игры при непрерывном поиске пути?" data-en="<strong>3. Frame Budget:</strong> Does 60 FPS hold without lag during continuous recalculation?"><strong>3. Unumdorlik:</strong> Dushman quvlaganda o'yin FPS ko'rsatkichi 60 da silliq ishlayaptimi?</li>
          <li data-ru="<strong>4. Реакция на Потерю:</strong> Переходит ли враг обратно в PATROL, если герой убежал далеко?" data-en="<strong>4. Disengage State:</strong> Does the monster switch back to PATROL when losing line of sight?"><strong>4. Holat o'zgarishi:</strong> Qahramon yashiringanda dushman yana sokin patrulga qaytyaptimi?</li>
        </ul>
      </div>
      <div class="box" style="border:1px dashed var(--accent); background:rgba(59,130,246,0.05); display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
        <div style="font-size:40px; margin-bottom:8px;">🧟 🧱 🏃</div>
        <h4 data-ru="Взаимопомощь" data-en="Peer Support">Do'stona Maslahat</h4>
        <p style="font-size:12px; color:var(--ink-2); max-width:240px; margin:0;" data-ru="Если враг проходит сквозь стену по диагонали, запретите диагональные переходы в getNeighbors()!" data-en="If enemy clips diagonally through wall corners, disable diagonal moves in getNeighbors()!">Agar dushman devor burchagini kesib o'tayotgan bo'lsa, getNeighbors ichida diagonal harakatlarni o'chirib qo'ying!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: SHOWCASE -->
  <section class="slide" data-phase="Katta Ekran|Шоукейс|Showcase" data-time="74:00–77:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ДЕМОНСТРАЦИЯ НА ДОСКЕ" data-en="SMARTBOARD SHOWCASE">KATTA EKRAN SHOWCASI</span></div>
    <h2 data-ru="Шоукейс: Охота Монстров в Подземелье на Смартборде!" data-en="Showcase: Monster Hunt on the Big Screen!">Katta Doskada Jonli Dushman AI Showcasi!</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid var(--accent);">
        <h4 data-ru="1. Скрытный Ассасин" data-en="1. Stealth Assassin">1. Kiber-Qotil (Stealth)</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Держится в тени стен и атакует только со спины, когда герой отвернулся." data-en="Hugs wall shadows and only pounces when player faces away.">Faqat devor soyasida yuradi va qahramon orqasini o'girganda hujum qiladi.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--purple);">
        <h4 data-ru="2. Стая Волков (Flocking)" data-en="2. Pack Hunters">2. Bo'rilar Galasi (Flocking)</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="3 монстра обходят героя с трех разных сторон, окружая в кольцо!" data-en="3 enemies coordinate to flank the player from different angles.">3 ta dushman bir-birini itarib yubormasdan, qahramonni 3 tomondan o'rab oladi.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--green);">
        <h4 data-ru="3. Слепой Громила" data-en="3. Blind Heavy Brute">3. Ko'r G'o'l (Sound Chase)</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Ничего не видит, но бежит на звук каждого выстрела игрока через A*!" data-en="Blind monster that charges towards gunshot coordinates via A* sound triggers.">Ko'zi ko'rmaydi, lekin qahramon o'q uzganda xuddi shu nuqtaga A* bilan yuguradi!</p>
      </div>
    </div>
    <div class="box" style="margin-top:12px; background:rgba(16,185,129,0.08); border:1px solid var(--green); text-align:center;">
      <span style="font-weight:700; color:var(--green); font-size:13px;" data-ru="🎉 Невероятно! Ваше подземелье теперь наполнено умными и опасными противниками!" data-en="🎉 Incredible! Your dungeon is now teeming with cunning, intelligent predators!">🎉 Aqlbovar qilmas natija! Roguelike o'yiningiz endi aqlli va xavfli dushmanlar bilan to'ldi!</span>
    </div>
  </section>

  <!-- SLIDE 13: TIERED HOMEWORK -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Homework" data-time="77:00–79:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ДОМАШНЕЕ ЗАДАНИЕ (10 БАЛЛОВ)" data-en="HOMEWORK (10 POINTS)">UY VAZIFASI (10 BALL)</span></div>
    <h2 data-ru="3 Уровня: От Базового BFS до Стаи Окружающих Врагов" data-en="3 Challenge Tiers: From Base BFS to Coordinated Flanking">3 Darajali Dushman AI Vazifasi</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid var(--accent);">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1-Daraja (Baza)</div>
        <h4 data-ru="Сетка и BFS (4 Балла)" data-en="Grid & BFS (4 Points)">Grid va BFS (4 Ball)</h4>
        <p style="font-size:12px;" data-ru="Создайте структуру графа сетки и функцию bfs(start, target) для обхода стен." data-en="Implement grid graph conversion and a working bfs(start, target) navigation function.">Xaritani 2D kataklarga ajratib, devorlarni aylanib o'tuvchi asosiy BFS qidiruvini yozing.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--purple);">
        <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);">2-Daraja (Loyiha)</div>
        <h4 data-ru="Алгоритм A* и Путь (4 Балла)" data-en="A* & Route Tracking (4 Points)">A* Evristikasi (4 Ball)</h4>
        <p style="font-size:12px;" data-ru="Внедрите эвристику Манхэттена и заставьте монстра двигаться шаг за шагом по точкам пути." data-en="Integrate Manhattan heuristic and step-by-step path traversal for moving enemy.">Manhattan masofasi bilan A* ni ishga tushiring va dushmanni yashil yo'l bo'ylab qadamma-qadam yurgizing.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">3-Daraja (Kiber-Chaqiruv)</div>
        <h4 data-ru="Конус Зрения / FSM (2 Балла)" data-en="Vision Cone / FSM (2 Points)">Ko'rish Nuri / FSM (2 Ball)</h4>
        <p style="font-size:12px;" data-ru="Реализуйте переключение состояний PATROL ➔ CHASE и конус видимости с лучом Raycast!" data-en="Program PATROL ➔ CHASE state transitions and vision cone Raycasting! ">PATROL dan CHASE ga o'tuvchi ko'rish nuri (Raycast) yoki 2 ta dushmanning o'rab olishini qo'shing!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И МОСТ" data-en="SUMMARY & BRIDGE">XULOSA VA KEYINGI BOSQICH</span></div>
    <h2 data-ru="Чему Мы Научились: Алгоритмы ИИ в Действии" data-en="What We Engineered: AI Pathfinding in Action">Dushman AI Xulosasi va Keyingi Bosqich</h2>
    <div class="grid-2">
      <div>
        <ul class="clean-list">
          <li data-ru="<strong>Сетка Графов:</strong> Преобразование пиксельного холста в дискретные узлы (Nodes)." data-en="<strong>Grid Graph:</strong> Transforming raw pixel coordinates into discrete searchable nodes."><strong>Grid Grafi:</strong> Piksellarni kataklarga (col, row) bo'lib xarita yasash.</li>
          <li data-ru="<strong>BFS:</strong> Гарантированный поиск кратчайшего пути через очередь (FIFO Queue)." data-en="<strong>BFS:</strong> Guaranteed shortest path via breadth wave expansion."><strong>BFS:</strong> Navbat (Queue) orqali eng qisqa yo'lni topish kafolati.</li>
          <li data-ru="<strong>A* (A-Star):</strong> Интеллектуальный поиск с эвристикой Манхэттена f = g + h." data-en="<strong>A* (A-Star):</strong> Guided pathfinding optimizing evaluated nodes via Manhattan heuristic."><strong>A*:</strong> Manhattan evristikasi ($f = g + h$) bilan 5-10x tezroq qidirish.</li>
          <li data-ru="<strong>Конечный Автомат (FSM):</strong> Поведение монстров: PATROL, ALERT va CHASE." data-en="<strong>State Machine (FSM):</strong> Dynamic predator behaviors: PATROL, ALERT, and CHASE."><strong>FSM Holatlar:</strong> Dushmanning jonli xatti-harakati (Patrul, Shubha, Ta'qib).</li>
        </ul>
      </div>
      <div class="box" style="border-left:4px solid var(--accent); display:flex; flex-direction:column; justify-content:center;">
        <h4 data-ru="Следующий Модуль: Инвентарь и Предметы" data-en="Next Module: Inventory & Loot System">Keyingi Dars: Inventar va Buyumlar Tizimi</h4>
        <p style="font-size:12px;" data-ru="На следующем уроке мы добавим механику сундуков с лутом, Drag-and-Drop экипировку оружия и расчет характеристик (+10 к урону)!" data-en="Next lesson we engineer chest loot mechanics, Drag-and-Drop weapon equipping, and stat calculations (+10 Attack)!">Keyingi darsda labirint xazinalaridan tushuvchi buyumlar, Drag-and-Drop inventar paneli va qahramon kuchini oshirish tizimini quramiz!</p>
      </div>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. IN-DECK SIMULATOR SCRIPT (Interactive A* Pathfinding)
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
var deckP_canvas, deckP_ctx;
var deckP_cols = 16, deckP_rows = 9;
var deckP_tileW = 28, deckP_tileH = 28;
var deckP_grid = [];
var deckP_hero = { c: 13, r: 4 };
var deckP_enemy = { c: 2, r: 4 };
var deckP_useAStar = true;
var deckP_path = [];
var deckP_explored = 0;

function initDeckPathfinding() {
  deckP_canvas = document.getElementById('deckPathCanvas');
  if (!deckP_canvas) return;
  deckP_ctx = deckP_canvas.getContext('2d');
  deckResetGrid();

  deckP_canvas.addEventListener('pointerdown', function(e) {
    var rect = deckP_canvas.getBoundingClientRect();
    var scaleX = deckP_canvas.width / rect.width;
    var scaleY = deckP_canvas.height / rect.height;
    var tx = (e.clientX - rect.left) * scaleX;
    var ty = (e.clientY - rect.top) * scaleY;
    var c = Math.floor(tx / deckP_tileW);
    var r = Math.floor(ty / deckP_tileH);
    if (c >= 0 && c < deckP_cols && r >= 0 && r < deckP_rows) {
      if ((c === deckP_hero.c && r === deckP_hero.r) || (c === deckP_enemy.c && r === deckP_enemy.r)) {
        return;
      }
      deckP_grid[r][c] = deckP_grid[r][c] === 1 ? 0 : 1;
      recalculateDeckPath();
      drawDeckPath();
    }
  });
}

function deckResetGrid() {
  deckP_grid = [];
  for (var r = 0; r < deckP_rows; r++) {
    var row = [];
    for (var c = 0; c < deckP_cols; c++) {
      row.push(0);
    }
    deckP_grid.push(row);
  }
  // Default obstacle wall in middle
  for (var r = 2; r < 7; r++) {
    deckP_grid[r][8] = 1;
  }
  recalculateDeckPath();
  drawDeckPath();
}

function deckToggleAlgo() {
  deckP_useAStar = !deckP_useAStar;
  var btn = document.getElementById('btnDeckAlgo');
  if (btn) {
    if (deckP_useAStar) {
      btn.textContent = 'Rejim: A* (Evristik)';
      btn.style.background = 'var(--accent)';
      btn.style.color = '#000';
    } else {
      btn.textContent = 'Rejim: BFS (Oddiy)';
      btn.style.background = 'var(--purple)';
      btn.style.color = '#fff';
    }
  }
  recalculateDeckPath();
  drawDeckPath();
}

function recalculateDeckPath() {
  var start = { c: deckP_enemy.c, r: deckP_enemy.r };
  var target = { c: deckP_hero.c, r: deckP_hero.r };

  var openSet = [{ c: start.c, r: start.r, g: 0, h: 0, f: 0, parent: null }];
  var closedSet = new Set();
  deckP_path = [];
  deckP_explored = 0;

  while (openSet.length > 0) {
    var currentIdx = 0;
    if (deckP_useAStar) {
      for (var i = 1; i < openSet.length; i++) {
        if (openSet[i].f < openSet[currentIdx].f) currentIdx = i;
      }
    }
    var current = openSet.splice(currentIdx, 1)[0];
    deckP_explored++;

    var key = current.c + ',' + current.r;
    closedSet.add(key);

    if (current.c === target.c && current.r === target.r) {
      var curr = current;
      while (curr) {
        deckP_path.push({ c: curr.c, r: curr.r });
        curr = curr.parent;
      }
      deckP_path.reverse();
      break;
    }

    var neighbors = [
      { c: current.c + 1, r: current.r },
      { c: current.c - 1, r: current.r },
      { c: current.c, r: current.r + 1 },
      { c: current.c, r: current.r - 1 }
    ];

    for (var n = 0; n < neighbors.length; n++) {
      var nb = neighbors[n];
      if (nb.c < 0 || nb.c >= deckP_cols || nb.r < 0 || nb.r >= deckP_rows) continue;
      if (deckP_grid[nb.r][nb.c] === 1) continue;
      var nKey = nb.c + ',' + nb.r;
      if (closedSet.has(nKey)) continue;

      var g = current.g + 1;
      var h = Math.abs(nb.c - target.c) + Math.abs(nb.r - target.r);
      var f = g + (deckP_useAStar ? h : 0);

      var existing = openSet.find(function(item) { return item.c === nb.c && item.r === nb.r; });
      if (!existing) {
        openSet.push({ c: nb.c, r: nb.r, g: g, h: h, f: f, parent: current });
      } else if (g < existing.g) {
        existing.g = g;
        existing.f = f;
        existing.parent = current;
      }
    }
  }

  var elSteps = document.getElementById('deckPathSteps');
  var elExplored = document.getElementById('deckExploredNodes');
  if (elSteps) elSteps.textContent = deckP_path.length > 0 ? (deckP_path.length - 1) : 'Yo‘l yo‘q';
  if (elExplored) elExplored.textContent = deckP_explored;
}

function drawDeckPath() {
  if (!deckP_ctx) return;
  deckP_ctx.fillStyle = '#020617';
  deckP_ctx.fillRect(0, 0, deckP_canvas.width, deckP_canvas.height);

  // Draw Grid & Walls
  for (var r = 0; r < deckP_rows; r++) {
    for (var c = 0; c < deckP_cols; c++) {
      var x = c * deckP_tileW;
      var y = r * deckP_tileH;
      if (deckP_grid[r][c] === 1) {
        deckP_ctx.fillStyle = '#334155';
        deckP_ctx.fillRect(x + 1, y + 1, deckP_tileW - 2, deckP_tileH - 2);
      } else {
        deckP_ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
        deckP_ctx.strokeRect(x, y, deckP_tileW, deckP_tileH);
      }
    }
  }

  // Draw Path Line
  if (deckP_path.length > 1) {
    deckP_ctx.strokeStyle = '#10b981';
    deckP_ctx.lineWidth = 4;
    deckP_ctx.beginPath();
    for (var p = 0; p < deckP_path.length; p++) {
      var px = deckP_path[p].c * deckP_tileW + deckP_tileW / 2;
      var py = deckP_path[p].r * deckP_tileH + deckP_tileH / 2;
      if (p === 0) deckP_ctx.moveTo(px, py);
      else deckP_ctx.lineTo(px, py);
    }
    deckP_ctx.stroke();
  }

  // Draw Enemy (Start)
  var ex = deckP_enemy.c * deckP_tileW + deckP_tileW / 2;
  var ey = deckP_enemy.r * deckP_tileH + deckP_tileH / 2;
  deckP_ctx.fillStyle = '#ef4444';
  deckP_ctx.beginPath();
  deckP_ctx.arc(ex, ey, 10, 0, Math.PI * 2);
  deckP_ctx.fill();

  // Draw Hero (Target)
  var hx = deckP_hero.c * deckP_tileW + deckP_tileW / 2;
  var hy = deckP_hero.r * deckP_tileH + deckP_tileH / 2;
  deckP_ctx.fillStyle = '#38bdf8';
  deckP_ctx.beginPath();
  deckP_ctx.arc(hx, hy, 10, 0, Math.PI * 2);
  deckP_ctx.fill();
}

// 25-Min Arena Timer
var arenaTimeLeft = 25 * 60;
var arenaTimerInterval = null;
function toggleArenaTimer() {
  var btn = document.getElementById('arenaTimerBtn');
  var disp = document.getElementById('arenaTimerDisplay');
  if (arenaTimerInterval) {
    clearInterval(arenaTimerInterval);
    arenaTimerInterval = null;
    if (btn) btn.textContent = '⏱️ Davom Ettirish';
  } else {
    arenaTimerInterval = setInterval(function() {
      if (arenaTimeLeft <= 0) {
        clearInterval(arenaTimerInterval);
        arenaTimerInterval = null;
        if (disp) disp.textContent = '00:00';
        alert('Vaqt tugadi! Endi partadoshingiz dushman AI kodini audit qiling!');
        return;
      }
      arenaTimeLeft--;
      var m = Math.floor(arenaTimeLeft / 60);
      var s = arenaTimeLeft % 60;
      if (disp) disp.textContent = (m < 10 ? '0' + m : m) + ':' + (s < 10 ? '0' + s : s);
    }, 1000);
    if (btn) btn.textContent = '⏸️ To‘xtatish';
  }
}

// Interactive Quiz Handler
function checkQuiz(btn, isCorrect, feedback) {
  var parent = btn.parentElement;
  var btns = parent.querySelectorAll('button');
  btns.forEach(function(b) {
    b.disabled = true;
    b.style.opacity = '0.6';
  });
  if (isCorrect) {
    btn.style.background = 'var(--green)';
    btn.style.color = '#fff';
    btn.style.opacity = '1';
  } else {
    btn.style.background = 'var(--red)';
    btn.style.color = '#fff';
    btn.style.opacity = '1';
  }
  var fb = document.getElementById('quizFeedback');
  if (fb) {
    fb.textContent = feedback;
    fb.style.color = isCorrect ? 'var(--green)' : 'var(--red)';
  }
}

document.addEventListener('DOMContentLoaded', function() {
  initDeckPathfinding();
});
"""

# Teacher Notes Data
NOTES_DATA = {
    "uz": [
        ["Kirish va Maqsad", "80 daqiqalik juftlik dars rejasi. Bugun o'quvchilar Roguelike o'yinidagi dushmanlarga devorlarni aylanib o'tuvchi A* va BFS algoritmini Vibecoding orqali o'rgatishadi.", "Doskaga 2D kataklar va to'siq chizmasini chizing."],
        ["Uy Vazifasi Tahlili", "32-darsdagi splice teskari sikli xatosini tushuntiring. 30 soniyalik blits savol bering: devor o'rtada turganda dushman nega qotib qoladi?", "To'g'ri chiziqli ta'qibning cheklovini fosh qiling."],
        ["Sodda Ta'qibning Tuzog'i", "Nega enemy.x += dx kodi Т-shaklidagi devorda qotib qolishini ko'rsating.", "Kompyuterga butun xarita xaritasi va graf tugunlari kerakligini asoslang."],
        ["Xaritani Grafga Aylantirish", "Canvas ekranini 20x13 lik matritsaga bo'lish. 0 - erkin yo'l, 1 - tosh devor.", "Pikseldan katakka o'tish formulasini tushuntiring."],
        ["BFS: Kengaytirilgan Qidiruv", "Suv to'lqini kabi tarqaluvchi BFS algoritmi. Queue (FIFO) va visited to'plami roli.", "Nega BFS eng qisqa yo'lni topishi, lekin hamma tomonga ko'r-ko'rona tarqalishini ko'rsating."],
        ["A* Evristikasi (f = g + h)", "A* ning afzalligi: Manhattan masofasi orqali faqat maqsad tomon intilish.", "f(n) = g(n) + h(n) formulasini doskada hisoblab ko'rsating."],
        ["Dushman Holatlari (FSM)", "PATROL (sokin aylanib yurish), ALERT (shubha '?' belgisi) va CHASE (qizil tezkor ta'qib).", "Dushmanning ko'rish nuri (Sight Cone) mexanizmi."],
        ["Smartboard Simulyatori", "Doskadagi simulyatorda o'quvchilar bilan devorlar qurib, A* va BFS qidiruvini solishtirib ko'ring.", "Tekshirilgan kataklar soni farqini ko'rsating."],
        ["Kiber-Viktorina", "3 ta nazorat savoli bo'yicha viktorina o'tkazing.", "Har bir savolga professional tushuntirish bering."],
        ["Vibecoding Amaliy Arenasi", "25 daqiqalik amaliyot: o'quvchilar qo'lda kod yozmaydi, AI ga aniq 4 bosqichli prompt beradi va test qiladi.", "Devorga tiqilish xatosini tuzatuvchi A* promptiga e'tibor qarating."],
        ["Partadosh Auditi", "Partadoshlar o'rin almashib, dushman AI sini 4 ta mezon bo'yicha test qilishadi.", "Do'stona yordam va kiber-tekshiruv."],
        ["Katta Ekran Showcasi", "Eng aqlli dushman yoki yashirin stealth dushmanni katta doskada ko'rsating.", "Mualliflarni olqishlang."],
        ["3 Darajali Uy Vazifasi", "10 ballik uy vazifasi shartlarini tushuntiring (4 + 4 + 2).", "Mustaqil dasturlash va kiber-chaqiruv."],
        ["Xulosa va Keyingi Dars", "Darsni sarhisob qiling va keyingi darsda labirint xazinalari va Drag-and-Drop inventar tizimini o'rganamiz deb e'lon qiling.", "O'quvchilar savollariga javob bering."]
    ],
    "ru": [
        ["Введение и Цель", "План сдвоенного урока (80 минут). Сегодня ученики обучат монстров обходить препятствия через A* и BFS в Roguelike.", "Нарисуйте на доске сетку тайлов и стену."],
        ["Разбор Домашнего Задания", "Разберите ошибку обратного цикла splice() из 32-го урока. 30-секундный блиц: почему наивный враг застревает в стене?", "Покажите ограничения прямолинейного хода."],
        ["Ловушка Прямого Хода", "Объясните, почему enemy.x += dx беспомощно дрожит в Т-образной стене.", "Обоснуйте необходимость дискретной сетки узлов."],
        ["Сетка и Графы", "Разбиение холста на матрицу тайлов 20x13. 0 - пол, 1 - каменная стена.", "Формула перевода пикселей в индекс клетки."],
        ["Поиск в Ширину BFS", "Волновой алгоритм BFS, очередь FIFO и множество visited.", "Объясните гарантию кратчайшего пути и слепое сканирование во все стороны."],
        ["Эвристика A* (f = g + h)", "Преимущество A*: направленный поиск к цели через Манхэттенское расстояние.", "Разберите расчет формулы f(n) = g(n) + h(n) на доске."],
        ["Конечный Автомат (FSM)", "Состояния PATROL (патруль), ALERT (тревога '?') и CHASE (погоня).", "Механика конуса зрения и обнаружения."],
        ["Интерактив на Смартборде", "Постройте стены на смартборде вместе с учениками и сравните BFS и A*.", "Покажите разницу в проверенных узлах."],
        ["Кибер-Квиз", "Быстрый квиз из 3 контрольных вопросов по графам и навигации.", "Разберите каждый ответ."],
        ["Арена Vibecoding (25 минут)", "Ученики формулируют 4 четких промпта для ИИ и тестируют код в реальном времени.", "Контролируйте critic-промпт обхода препятствий."],
        ["Взаимный Аудит", "Ученики меняются местами и тестируют навигацию одноклассника по 4 критериям.", "Взаимопомощь и поиск багов."],
        ["Шоукейс на Доске", "Продемонстрируйте лучших врагов (стелс, стая волков) на смартборде.", "Похвалите авторов."],
        ["3 Уровня Домашнего Задания", "Объясните 10-балльную систему оценивания (4 + 4 + 2).", "Самостоятельная работа и вызов."],
        ["Итоги и Мост", "Подведите итоги и анонсируйте следующий урок: система инвентаря и Drag-and-Drop лута.", "Ответьте на вопросы."]
    ],
    "en": [
        ["Intro & Objectives", "80-minute double block pacing. Today students engineer monster pathfinding using A* and BFS in Roguelike.", "Diagram tile grid and obstacle traversal on board."],
        ["Homework Review", "Review reverse loop splice from Lesson 32. 30-second blitz: why does naive enemy jam into walls?", "Demonstrate naive chasing limitations."],
        ["Direct Chase Trap", "Explain why naive dx stepping vibrates helplessly against T-shaped barriers.", "Justify graph representation and node abstraction."],
        ["Grid Graph Conversion", "Discretizing 2D canvas into 20x13 node matrix. 0 - walkable floor, 1 - impassable stone.", "Pixel-to-tile coordinate conversion formula."],
        ["Breadth-First Search (BFS)", "Wave-expansion algorithm, FIFO Queue and visited set.", "Explain shortest path guarantee versus blind omnidirectional expansion."],
        ["A* Heuristic (f = g + h)", "The power of A*: guided search using Manhattan distance.", "Walk through f(n) = g(n) + h(n) calculation on the board."],
        ["Finite State Machine (FSM)", "PATROL (waypoint wandering), ALERT ('?' warning) and CHASE (aggressive pursuit).", "Sight cone raycast detection mechanics."],
        ["Smartboard Interactive", "Build wall labyrinths with students and compare BFS vs A* exploration live.", "Highlight explored node count differences."],
        ["Cyber Quiz", "Fast 3-question assessment on graph search and pathfinding heuristics.", "Review each explanation."],
        ["Vibecoding Arena (25 min)", "Students issue 4 structured AI prompts and verify pathfinding live.", "Enforce wall avoidance critic prompt."],
        ["Peer Audit", "Students swap seats and audit peer monster navigation across 4 checkpoints.", "Peer debugging and support."],
        ["Showcase", "Demonstrate stealth and flocking enemy behaviors on the big screen.", "Praise students."],
        ["Tiered Homework", "Explain 10-point rubric criteria (4 + 4 + 2).", "Independent challenge."],
        ["Summary & Bridge", "Summarize learnings and announce next lesson: Loot drops & Drag-and-Drop Inventory System.", "Q&A session."]
    ]
}

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "33-dars: Dushman AI va Pathfinding: A* va BFS Algoritmlari"
    title_ru = "Урок 33: ИИ Врагов и Pathfinding: Алгоритмы A* и BFS"
    title_en = "Lesson 33: Enemy AI & Pathfinding: A* and BFS Algorithms"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="7–8 КЛАСС" data-en="GRADES 7–8">7–8-SINF</span>',
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

    sec1_html = """
    <div style="background:var(--panel); padding:8px; border-radius:4px; font-size:9pt; line-height:1.45;">
      <div style="font-weight:700; color:var(--accent-ink); margin-bottom:4px;" data-ru="Ключевые формулы и понятия поиска пути:" data-en="Key pathfinding formulas and concepts:">Pathfinding qidiruvining asosiy formulalari:</div>
      <div>1. <strong>Katak koordinatasi:</strong> <code>col = Math.floor(x / TILE_SIZE)</code>, <code>row = Math.floor(y / TILE_SIZE)</code></div>
      <div>2. <strong>A* formulasi:</strong> <code>f(n) = g(n) + h(n)</code> (g - qadamlar, h - evristika)</div>
      <div>3. <strong>Manhattan masofasi:</strong> <code>h = Math.abs(a.x - b.x) + Math.abs(a.y - b.y)</code></div>
      <div>4. <strong>FSM holatlari:</strong> <code>PATROL</code> (1x tezlik), <code>ALERT</code> (shubha), <code>CHASE</code> (1.8x A* ta'qib)</div>
    </div>
    """

    sec2_html = """
    <p style="font-size:8.8pt; margin:4px 0;" data-ru="Эффективный AI-промпт для навигации состоит из 4 частей:" data-en="Effective pathfinding AI prompt structure:">Dushman AI uchun Vibecoding prompti 4 qismdan tuziladi:</p>
    <div style="background:var(--panel-2); border-left:3px solid var(--accent); padding:6px 8px; font-size:8.5pt; line-height:1.4;">
      <div>🎯 <strong>[Rol]:</strong> "Sen 2D o'yin fizikasi va graf algoritmlari bo'yicha AI mutaxassisisan."</div>
      <div>📦 <strong>[Kontekst]:</strong> "Menda 20x13 katakli labirint matritsasi bor (0 - pol, 1 - tosh devor)."</div>
      <div>⚙️ <strong>[Vazifa]:</strong> "Dushman qahramon tomon eng qisqa yo'l bilan borishi uchun A* algoritmini yoz."</div>
      <div>🛡️ <strong>[Cheklovlar]:</strong> "Manhattan evristikasini ishlat, devorlarni aylanib o'tsin, diagonallar yopilsin."</div>
    </div>
    """

    sec3_html = """
    <div style="font-size:8.8pt; line-height:1.45;">
      <p style="margin:2px 0 6px;" data-ru="Выполните 4 практических шага в редакторе кода с вашим ИИ-ассистентом:" data-en="Execute the 4 practical milestones in your code editor with your AI assistant:">Kodni qo'lda yozmang — AI bilan 4 ta aniq Vibecoding qadamini bajaring:</p>
      <div style="border:1px solid var(--rule); border-radius:4px; padding:6px 8px; margin-bottom:6px; background:var(--panel);">
        <strong>[Qadam 1] Xatoni Ko'rish:</strong> Dushmanga to'g'ri chiziqli ta'qib berib, devorga tiqilishini tekshiring. [ &nbsp; ] Bajarildi
      </div>
      <div style="border:1px solid var(--rule); border-radius:4px; padding:6px 8px; margin-bottom:6px; background:var(--panel);">
        <strong>[Qadam 2] Grid va BFS Prompti:</strong> Matritsa ustida navbat (Queue) orqali devorlarni aylanib o'tishni oling. [ &nbsp; ] Bajarildi
      </div>
      <div style="border:1px solid var(--rule); border-radius:4px; padding:6px 8px; margin-bottom:6px; background:var(--panel);">
        <strong>[Qadam 3] A* Evristikasi (Critic):</strong> Manhattan masofasi bilan qidiruvni 5 barobar tezlashtiring. [ &nbsp; ] Bajarildi
      </div>
      <div style="border:1px solid var(--rule); border-radius:4px; background:var(--panel);">
        <strong>[Qadam 4] Vibe-Juice:</strong> Ko'rish nuri (Sight Cone) va dushmanning '!' belgisini integratsiya qiling. [ &nbsp; ] Bajarildi
      </div>
    </div>
    """

    sec4_html = """
    <div style="font-size:8.6pt; line-height:1.4; margin-top:6px;">
      <div style="margin-bottom:6px;">
        <strong>1-Daraja: Baza (4 ball):</strong> Grid matritsasi va to'siqlarni aylanib o'tuvchi toza BFS kodini tahlil qiling.
      </div>
      <div style="margin-bottom:6px;">
        <strong>2-Daraja: Amaliyot (4 ball):</strong> Manhattan evristikali A* algoritmini o'yinga ulab, dushmanning harakatini ta'minlang.
      </div>
      <div style="margin-bottom:6px;">
        <strong>3-Daraja: Kiber-Chaqiruv (2 ball):</strong> Dushmanning ko'rish maydoni nurini yoki PATROL ➔ CHASE o'tishini sozlang.
      </div>
      <div style="border-top:1px dashed var(--rule); padding-top:4px; font-weight:700; color:var(--accent-ink); display:flex; justify-content:space-between;" data-ru="Итоговый балл: _____ / 10 &nbsp; Подпись преподавателя: ____________" data-en="Total Score: _____ / 10 &nbsp; Teacher Signature: ____________">
        <span>To'plangan ball: _____ / 10</span>
        <span>O'qituvchi imzosi: ____________</span>
      </div>
    </div>
    """

    replacements = {
        "{{LESSON_NUM}}": "33",
        "{{TITLE_UZ}}": "Dushman AI va Pathfinding: A* va BFS Algoritmlari",
        "{{TITLE_RU}}": "ИИ Врагов и Pathfinding: Алгоритмы A* и BFS",
        "{{TITLE_EN}}": "Enemy AI & Pathfinding: A* and BFS Algorithms",
        "{{COHORT_LABEL_UZ}}": "7–8-SINF",
        "{{COHORT_LABEL_RU}}": "7–8 КЛАСС",
        "{{COHORT_LABEL_EN}}": "GRADES 7–8",
        "{{META_UZ}}": "11-Hafta · Juftlik Dars (80 daqiqa) · Vibecoding & Creative Coding Track",
        "{{META_RU}}": "11-я Неделя · Сдвоенный Урок (80 минут) · Направление Vibecoding",
        "{{META_EN}}": "Week 11 · Double Block (80 min) · Vibecoding & Creative Coding Track",
        "{{MISSION_UZ}}": "Labirint dushmanlarini tosh devorlarni aylanib o'tib, qahramonni eng qisqa yo'l bilan quvlashga o'rgatish: 2D kataklar to'ri (Grid Graph), navbat asosidagi BFS algoritmi, Manhattan evristikali A* tezlatgichi va ko'rish nuri orqali PATROL dan CHASE ga o'tish mexanikasini Vibecoding yordamida yaratish.",
        "{{MISSION_RU}}": "Обучить монстров подземелья находить кратчайший маршрут к герою в обход стен через дискретную сетку узлов, очередь BFS, эвристику Манхэттена A* и конусы видимости.",
        "{{MISSION_EN}}": "Engineer intelligent dungeon enemy pathfinding: grid graph conversion, queue-based BFS obstacle avoidance, Manhattan-guided A* search, and vision raycasting for PATROL to CHASE transitions.",
        "{{SEC1_TITLE_UZ}}": "Pathfinding Nazariyasi: Kataklar va A* Formulalari",
        "{{SEC1_TITLE_RU}}": "Теория Pathfinding: Сетка и Формула A*",
        "{{SEC1_TITLE_EN}}": "Pathfinding Theory: Grid & A* Formulas",
        "{{SEC1_CONTENT}}": sec1_html,
        "{{SEC2_TITLE_UZ}}": "Vibecoding Prompt Shabloni: AI ga To'g'ri Buyruq Berish",
        "{{SEC2_TITLE_RU}}": "Шаблон Промпта Vibecoding: Правильная Постановка Задачи ИИ",
        "{{SEC2_TITLE_EN}}": "Vibecoding Prompt Template: Structured AI Request",
        "{{SEC2_CONTENT}}": sec2_html,
        "{{SEC3_TITLE_UZ}}": "Amaliy Vibecoding Protokoli (Laboratoriya Rejasi)",
        "{{SEC3_TITLE_RU}}": "Практический Протокол Vibecoding (План Лабораторной)",
        "{{SEC3_TITLE_EN}}": "Hands-on Vibecoding Protocol (Lab Checklist)",
        "{{SEC3_CONTENT}}": sec3_html,
        "{{SEC4_CONTENT}}": sec4_html
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

    tasks_html = """
    <!-- TASK 1 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <span class="badge" style="background:var(--accent); color:#000; font-weight:700; padding:2px 8px; border-radius:4px; font-size:11px;">1-Vazifa (4 Ball) — Baza</span>
        <span style="font-size:11px; color:var(--ink-2);" data-ru="Сетка и алгоритм BFS" data-en="Grid & BFS algorithm">Grid va BFS Qidiruvi</span>
      </div>
      <h3 style="margin-bottom:6px; font-size:13pt;" data-ru="Промпт для ИИ: Функция Поиска BFS" data-en="AI Prompt: BFS Pathfinding Function">Katakli Matritsa va BFS Qidiruv Prompti</h3>
      <p style="font-size:12px; color:var(--ink-2); margin-bottom:8px;" data-ru="Напишите структурированный AI-промпт, который заставит ИИ написать функцию bfs(grid, start, target) для поиска кратчайшего пути обхода стен с использованием очереди Queue." data-en="Write a structured AI prompt requesting a BFS pathfinding function navigating around obstacle tiles via a FIFO queue.">AI ga 2D matritsada tosh devorlarni aylanib o'tib, eng qisqa yo'lni topuvchi <code>bfs(grid, start, target)</code> funksiyasini yozdirish uchun to'liq prompt matnini shakllantiring:</p>
      <textarea id="hwTask1" style="width:100%; height:90px; background:var(--surface-2); color:var(--ink); border:1px solid var(--hair); border-radius:4px; padding:8px; font-family:var(--font-mono); font-size:11px;"></textarea>
      <div style="margin-top:6px; display:flex; justify-content:space-between; align-items:center;">
        <button class="btn" onclick="saveAnswer('hwTask1')" style="font-size:11px; background:var(--surface-2); border:1px solid var(--hair);" data-ru="💾 Сохранить" data-en="💾 Save">💾 Saqlash</button>
        <button class="btn toggle-sol" onclick="toggleSolution('sol1')" style="font-size:11px; color:var(--accent); background:none; border:none; cursor:pointer;" data-ru="Показать эталонный ответ" data-en="Show Golden Answer">Oltin Yechimni Ko'rish</button>
      </div>
      <div id="sol1" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px;">
        <strong>Oltin Prompt:</strong> "Men 2D HTML5 Canvas roguelike o'yinimda dushman AI sini dasturlayapman. Menda 20x13 lik grid mavjud (0 - bo'sh joy, 1 - tosh devor). Dushman devorlarni aylanib qahramonga borishi uchun BFS algoritmini yozib ber. Navbat (Queue) va visited to'plamidan foydalan, qadamlar ketma-ketligini [{c, r}, ...] massivida qaytar."
      </div>
    </div>

    <!-- TASK 2 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <span class="badge" style="background:var(--purple); color:#fff; font-weight:700; padding:2px 8px; border-radius:4px; font-size:11px;">2-Vazifa (4 Ball) — Amaliyot</span>
        <span style="font-size:11px; color:var(--ink-2);" data-ru="Эвристика A* (Манхэттен)" data-en="A* Manhattan Heuristics">A* Evristikasi va Optimizatsiya</span>
      </div>
      <h3 style="margin-bottom:6px; font-size:13pt;" data-ru="Critic-Промпт: Ускорение Поиска через A*" data-en="Critic Prompt: A* Acceleration">Critic Prompt: BFS dan A* ga O'tish</h3>
      <p style="font-size:12px; color:var(--ink-2); margin-bottom:8px;" data-ru="Сформулируйте промпт к ИИ, объясняющий, что обычный BFS проверяет слишком много лишних клеток, и требующий внедрить эвристику Манхэттена f = g + h." data-en="Formulate a prompt explaining that standard BFS checks too many nodes blindly, and requesting A* Manhattan distance optimization.">Oddiy BFS butun xaritani ko'r-ko'rona tekshirib, protsessorni yuklayotganini AI ga aytib, Manhattan masofasi ($f = g + h$) bilan 5 barobar tez ishlovchi $A^*$ algoritmini talab qilish promptini yozing:</p>
      <textarea id="hwTask2" style="width:100%; height:90px; background:var(--surface-2); color:var(--ink); border:1px solid var(--hair); border-radius:4px; padding:8px; font-family:var(--font-mono); font-size:11px;"></textarea>
      <div style="margin-top:6px; display:flex; justify-content:space-between; align-items:center;">
        <button class="btn" onclick="saveAnswer('hwTask2')" style="font-size:11px; background:var(--surface-2); border:1px solid var(--hair);" data-ru="💾 Сохранить" data-en="💾 Save">💾 Saqlash</button>
        <button class="btn toggle-sol" onclick="toggleSolution('sol2')" style="font-size:11px; color:var(--accent); background:none; border:none; cursor:pointer;" data-ru="Показать эталонный ответ" data-en="Show Golden Answer">Oltin Yechimni Ko'rish</button>
      </div>
      <div id="sol2" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px;">
        <strong>Oltin Critic Prompt:</strong> "Diqqat: Hozirgi BFS algoritmi orqaga va chetga qarab 200 dan ortiq ortiqcha kataklarni tekshiryapti. Unga A* (A-Star) evristikasini qo'sh: f(n) = g(n) + h(n), bu yerda h(n) Manhattan masofasi (|col - targetCol| + |row - targetRow|) bo'lsin. Har bir qadamda eng kichik f(n) ga ega tugunni birinchi ko'rib, maqsad tomon yo'naltirilgan tezkor kod ber."
      </div>
    </div>

    <!-- TASK 3 (2 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <span class="badge" style="background:var(--green); color:#fff; font-weight:700; padding:2px 8px; border-radius:4px; font-size:11px;">3-Vazifa (2 Ball) — Kiber-Chaqiruv</span>
        <span style="font-size:11px; color:var(--ink-2);" data-ru="Конус Зрения или FSM" data-en="Vision Cone or FSM">Ko'rish Nuri yoki Holatlar (FSM)</span>
      </div>
      <h3 style="margin-bottom:6px; font-size:13pt;" data-ru="Промпт Сочности: Конус Видимости и Тревога" data-en="Game Juice Prompt: Vision Ray & Alert">O'yin Shirasi: Ko'rish Nuri va Ogohlantirish</h3>
      <p style="font-size:12px; color:var(--ink-2); margin-bottom:8px;" data-ru="Напишите промпт для добавления конуса видимости (Sight Cone) и восклицательного знака (!) над головой монстра при обнаружении игрока." data-en="Compose an enhancement prompt adding vision raycasting cones and a floating alert icon (!) when the enemy acquires sight.">Dushmanga 90 darajali ko'rish nuri (Sight Cone) va qahramon ko'ringanda boshining ustida qizil '!' ogohlantirish belgisi yonib, 1.8x tezlanish qo'shish promptini yozing:</p>
      <textarea id="hwTask3" style="width:100%; height:90px; background:var(--surface-2); color:var(--ink); border:1px solid var(--hair); border-radius:4px; padding:8px; font-family:var(--font-mono); font-size:11px;"></textarea>
      <div style="margin-top:6px; display:flex; justify-content:space-between; align-items:center;">
        <button class="btn" onclick="saveAnswer('hwTask3')" style="font-size:11px; background:var(--surface-2); border:1px solid var(--hair);" data-ru="💾 Сохранить" data-en="💾 Save">💾 Saqlash</button>
        <button class="btn toggle-sol" onclick="toggleSolution('sol3')" style="font-size:11px; color:var(--accent); background:none; border:none; cursor:pointer;" data-ru="Показать эталонный ответ" data-en="Show Golden Answer">Oltin Yechimni Ko'rish</button>
      </div>
      <div id="sol3" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px;">
        <strong>Oltin Prompt:</strong> "Dushmanga o'yin shirasini (juice) qo'sh: dushman qahramonni ko'rmaguncha 2 nuqta orasida sokin yursin (PATROL). Agar qahramon dushmanning 90 darajali ko'rish nuriga (Sight Cone) kirsa, dushman boshida qizil '!' belgisi yonsin, tovush effekti chalinib, tezligi 1.8x ga oshsin va A* orqali yugurib quvlasin."
      </div>
    </div>
    """

    replacements = {
        "{{TITLE_UZ}}": "33-dars: Dushman AI va Pathfinding: A* va BFS Algoritmlari",
        "{{TITLE_RU}}": "Урок 33: ИИ Врагов и Pathfinding: Алгоритмы A* и BFS",
        "{{TITLE_EN}}": "Lesson 33: Enemy AI & Pathfinding: A* and BFS Algorithms",
        "{{COHORT_LABEL_UZ}}": "7–8-SINF",
        "{{HERO_TAG_UZ}}": "11-Hafta · Vibecoding & Creative Coding Track",
        "{{HERO_DESC_UZ}}": "HTML5 Canvas da dushman AI siga A* va BFS algoritmlari yordamida to'siqlarni aylanib o'tishni va ko'rish nuri orqali qahramonni quvlashni o'rgatuvchi mustaqil topshiriqlar.",
        "{{HERO_DESC_RU}}": "Самостоятельные задания по созданию ИИ монстров с обходом стен через A* и BFS, эвристику Манхэттена и конусы видимости на HTML5 Canvas.",
        "{{HERO_DESC_EN}}": "Independent assignments: programming enemy AI pathfinding, obstacle avoidance via A* and BFS, Manhattan heuristics, and vision cones on Canvas.",
        "{{RUBRIC_T1_UZ}}": "1-Bosqich: Baza (Grid va BFS qidiruvi)",
        "{{RUBRIC_T1_RU}}": "1-й Уровень: База (Сетка и алгоритм BFS)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (Grid representation & BFS pathfinding)",
        "{{RUBRIC_T2_UZ}}": "2-Bosqich: Amaliyot (A* evristikasi va tezkor yo'l)",
        "{{RUBRIC_T2_RU}}": "2-й Уровень: Практика (Эвристика Манхэттена A*)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Manhattan-guided A* search)",
        "{{RUBRIC_T3_UZ}}": "3-Bosqich: Kiber-Chaqiruv (Ko'rish nuri va FSM holatlari)",
        "{{RUBRIC_T3_RU}}": "3-й Уровень: Вызов (Конус видимости и состояния FSM)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (Vision cone & FSM state transitions)",
        "{{TASKS_HTML}}": tasks_html,
        "{{LESSON_SLUG}}": "7-8-w11-l33-dushman-ai-va-pathfinding"
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    content = """# O'qituvchi Uchun Dars Qo'llanmasi (Teacher Reading Guide)

**Sinf:** 7–8-sinf · **Hafta:** 11-hafta · **Dars:** 33-dars  
**Mavzu:** Dushman AI va Pathfinding: A* (A-Star) va BFS To'siqlarni Aylanib Quvish Algoritmi  
**Format:** 80 daqiqalik Juftlik Dars (Double Block)  
**Uslub:** Vibecoding — AI bilan interaktiv graf algoritmlari, prompt muhandisligi va vizual pathfinding.

---

## 1. 80 Daqiqalik Darsning Daqiqama-Daqiqa Pacing Rejasi

### 1-Bosqich: Uy Vazifasi Tahlili va Nazariy Poydevor (40 daqiqa)
* **00:00–04:00 (Kirish):** Dars mavzusi va maqsadini e'lon qilish. O'quvchilarga o'tgan darsdagi o'q otish modulidan so'ng, endi labirint dushmanlarini haqiqiy xavfli yirtqichga aylantirishimizni aytish.
* **04:00–12:00 (Uy Vazifasi Tahlili):** 
  - 32-darsdagi splice teskari sikli xatosini tahlil qilish.
  - 30 soniyalik blits savol: tosh devor turganda dushman nega qotib qoladi?
* **12:00–24:00 (Sodda Ta'qib vs Grid Matritsasi):**
  - Nega `enemy.x += dx` to'g'ri chiziqli harakat devor oldida abadiy tiqilib qolishini doskada chizib ko'rsating.
  - Canvas ni 20x13 lik kataklarga bo'lish: 0 - pol, 1 - tosh devor.
* **24:00–35:00 (BFS va A* Evristikasi):**
  - BFS (Breadth-First Search) qanday qilib Queue (navbat) orqali to'lqinsimon tarqalishini tushuntiring.
  - A* ning sehri: $f(n) = g(n) + h(n)$ formulasida $h(n)$ (Manhattan masofasi) orqali qidiruvni faqat qahramon tomonga yo'naltirish.
* **35:00–40:00 (Dushman Holatlari — FSM va Sight Cone):**
  - PATROL ➔ ALERT ('?' belgisi) ➔ CHASE (1.8x A* ta'qib) zanjiri.

### 2-Bosqich: Amaliyot, Kiber-Duel va Baholash (40 daqiqa)
* **40:00–48:00 (Smartboard Jonli Simulyatori):** Doskada devorlar chizib, A* va BFS qidiruvini solishtirish.
* **48:00–55:00 (Kiber-Viktorina):** 3 ta nazorat savoli bo'yicha tezkor musobaqa.
* **55:00–70:00 (Vibecoding Amaliy Arenasi — 15 daqiqa):**
  - O'quvchilar AI ga 4 ta promptni bosqichma-bosqich berishadi:
    1. Devorga tiqilish xatosini tahlil qilish.
    2. Grid va BFS funksiyasini yozdirish.
    3. Manhattan evristikali A* optimallashtirish promptini yuborish.
    4. Ko'rish nuri (Sight Cone) va '!' ogohlantirish belgisini qo'shish.
* **70:00–74:00 (Partadosh Auditi):** Partadoshlar o'rin almashib, 4 ta mezon bo'yicha bir-birining dushman AI sini sinashadi.
* **74:00–77:00 (Katta Ekran Showcasi):** Eng yaxshi dushman xulq-atvorini katta doskada ko'rsatish.
* **77:00–80:00 (Xulosa va Vazifa):** 10 ballik rubrika va keyingi darsga (Inventar va Buyumlar tizimi) ko'prik.

---

## 2. O'qituvchi Uchun Savol-Javob va Baholash Kaliti
* **Savol 1:** Nega BFS eng qisqa yo'lni topadi?  
  *Javob:* Chunki u qadamlarni bir tekis to'lqin qilib kengaytiradi va maqsadga birinchi yetib borgan qadam eng kam qadamli yo'l bo'ladi.
* **Savol 2:** A* nega BFS dan 5-10 barobar tezroq ishlaydi?  
  *Javob:* Chunki A* Manhattan masofasi orqali orqa va chetdagi keraksiz kataklarni tekshirmaydi, faqat maqsad tomon kataklarni ochadi.
* **Savol 3:** Manhattan masofasi qanday hisoblanadi?  
  *Javob:* `|x1 - x2| + |y1 - y2|` (gorizontal va vertikal delta qadamlar yig'indisi).
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Created: TEACHER_READING.md")

def build_simulator():
    html = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Студия ИИ Врагов и Pathfinding (A* & BFS Lab)" data-en="Enemy AI & Pathfinding Studio (A* & BFS Lab)">Dushman AI va Pathfinding Studiyasi</title>
  <style>
    :root {
      --bg: #090d16;
      --surface: #131b2e;
      --surface-2: #1e293b;
      --ink: #f8fafc;
      --ink-2: #94a3b8;
      --accent: #38bdf8;
      --green: #10b981;
      --red: #ef4444;
      --yellow: #f59e0b;
      --purple: #a855f7;
      --font: system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace, Consolas, monospace;
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
      font-size: 15px;
      color: var(--accent);
    }
    .hud {
      display: flex;
      gap: 12px;
      align-items: center;
      font-weight: 700;
      font-size: 12px;
    }
    .hud-badge {
      background: var(--surface-2);
      padding: 5px 10px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    main {
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 380px;
      gap: 14px;
      padding: 14px;
      overflow: hidden;
    }
    .stage-wrapper {
      background: #020617;
      border-radius: 8px;
      border: 1px solid rgba(255,255,255,0.1);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }
    canvas {
      display: block;
      width: 100%;
      height: 100%;
      cursor: crosshair;
    }
    .sidebar {
      background: var(--surface);
      border-radius: 8px;
      border: 1px solid rgba(255,255,255,0.08);
      display: flex;
      flex-direction: column;
      gap: 10px;
      padding: 12px;
      overflow-y: auto;
    }
    .box-card {
      background: var(--surface-2);
      border-radius: 6px;
      padding: 10px;
      border: 1px solid rgba(255,255,255,0.05);
    }
    .box-card h4 {
      font-size: 13px;
      margin-bottom: 6px;
      color: var(--accent);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .step-tabs {
      display: flex;
      gap: 4px;
      margin-bottom: 8px;
    }
    .step-btn {
      flex: 1;
      padding: 5px;
      font-size: 10px;
      font-weight: 700;
      border-radius: 4px;
      border: 1px solid rgba(255,255,255,0.1);
      background: var(--surface);
      color: var(--ink-2);
      cursor: pointer;
      text-align: center;
    }
    .step-btn.active {
      background: var(--accent);
      color: #000;
      border-color: var(--accent);
    }
    .prompt-box {
      background: #060913;
      border: 1px solid #334155;
      border-radius: 4px;
      padding: 8px;
      font-family: var(--font-mono);
      font-size: 11px;
      line-height: 1.4;
      color: #38bdf8;
      max-height: 130px;
      overflow-y: auto;
      margin: 6px 0;
      white-space: pre-wrap;
    }
    .btn {
      padding: 6px 12px;
      border-radius: 4px;
      border: none;
      font-weight: 700;
      font-size: 11px;
      cursor: pointer;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }
    .btn:hover { opacity: 0.9; }
    .btn-accent { background: var(--accent); color: #000; }
    .btn-green { background: var(--green); color: #fff; }
    .btn-purple { background: var(--purple); color: #fff; }
    .btn-red { background: var(--red); color: #fff; }
    .btn-gray { background: #334155; color: #fff; }
  </style>
</head>
<body>

<header>
  <div class="brand">
    <span>🧠 Vibecoding Enemy AI Studio: A* & BFS Pathfinding</span>
    <span style="font-size:11px; background:rgba(56,189,248,0.15); color:var(--accent); padding:2px 8px; border-radius:12px;">7–8-Sinf</span>
  </div>
  <div class="hud">
    <div class="hud-badge">👣 <span data-ru="Длина пути:" data-en="Path Steps:">Yo'l:</span> <strong id="hudSteps" style="color:var(--green); font-size:13px;">0</strong></div>
    <div class="hud-badge">🔍 <span data-ru="Узлов проверено:" data-en="Explored Nodes:">Kataklar:</span> <strong id="hudExplored" style="color:var(--accent); font-size:13px;">0</strong></div>
    <div class="hud-badge">⚡ <span data-ru="Режим:" data-en="Mode:">Holat:</span> <strong id="hudState" style="color:var(--yellow); font-size:13px;">CHASE</strong></div>
  </div>
</header>

<main>
  <div class="stage-wrapper">
    <canvas id="simCanvas" width="800" height="520"></canvas>
  </div>

  <div class="sidebar">
    <div class="box-card">
      <h4 data-ru="Пошаговый Протокол Vibecoding" data-en="Step-by-Step Vibecoding Protocol">Vibecoding 4 Bosqichli Prompt Laboratoriyasi</h4>
      <div class="step-tabs">
        <button class="step-btn active" onclick="switchPromptStep(1)" data-ru="1. Ловушка" data-en="1. Trap">1. Tuzoq</button>
        <button class="step-btn" onclick="switchPromptStep(2)" data-ru="2. BFS" data-en="2. BFS">2. BFS</button>
        <button class="step-btn" onclick="switchPromptStep(3)" data-ru="3. A*" data-en="3. A*">3. A*</button>
        <button class="step-btn" onclick="switchPromptStep(4)" data-ru="4. Конус" data-en="4. Cone">4. Nur</button>
      </div>

      <div id="stepInfo">
        <div style="font-size:11px; color:var(--ink-2); line-height:1.4;" id="stepDesc">
          <strong>1-Qadam:</strong> Devorga tiqilish xatosini fosh qilish — AI ga oddiy ta'qib kodi tosh devorga urilib qolganini ko'rsatish.
        </div>
        <div class="prompt-box" id="stepPromptText">Menda Canvas o'yinim bor. Dushman qahramon tomon x += dx bilan boryapti, lekin o'rtada tosh devor tursa devorga tiqilib titrab qolyapti. Menga labirint devorlarini hisobga oluvchi grid qidiruv tizimi kerak.</div>
        <div style="display:flex; gap:6px; margin-top:6px;">
          <button class="btn btn-accent" onclick="copyPrompt()" style="flex:1;" data-ru="📋 Копировать Промпт" data-en="📋 Copy Prompt">📋 Nusxalash</button>
          <button class="btn btn-green" onclick="applyStepCode()" style="flex:1;" data-ru="⚡ Применить Код" data-en="⚡ Run in Lab">⚡ Kodni Qo'llash</button>
        </div>
      </div>
    </div>

    <div class="box-card">
      <h4 data-ru="Управление Алгоритмом" data-en="Algorithm Control">Algoritm Boshqaruvi</h4>
      <div style="display:flex; gap:6px; margin-bottom:8px;">
        <button class="btn btn-gray" id="btnAlgoAStar" onclick="setAlgorithm('astar')" style="flex:1; border:1px solid var(--accent);" data-ru="A* (Эвристика)" data-en="A* (Heuristic)">A* (Evristik)</button>
        <button class="btn btn-gray" id="btnAlgoBFS" onclick="setAlgorithm('bfs')" style="flex:1;" data-ru="BFS (Волна)" data-en="BFS (Wave)">BFS (To'lqin)</button>
        <button class="btn btn-gray" id="btnAlgoNaive" onclick="setAlgorithm('naive')" style="flex:1;" data-ru="Наивный (Bug)" data-en="Naive (Bug)">Naive (Tiqilish)</button>
      </div>
      <button class="btn btn-gray" onclick="resetWalls()" style="width:100%; margin-top:4px;" data-ru="🔄 Сбросить Стены" data-en="🔄 Reset Walls">🔄 Devorlarni Boshlang'ich Holatga Qaytarish</button>
      <button class="btn btn-purple" onclick="toggleSightCone()" style="width:100%; margin-top:6px;" data-ru="👁️ Переключить Конус Зрения" data-en="👁️ Toggle Vision Cone">👁️ Ko'rish Nuri (Sight Cone)</button>
    </div>

    <div class="box-card" style="font-family:var(--font-mono); font-size:10.5px; line-height:1.4;">
      <div style="color:var(--accent); font-weight:700; margin-bottom:4px;">[Real-Vaqt Formulalar]</div>
      <div style="color:#94a3b8;">col = Math.floor(x / TILE);</div>
      <div style="color:#94a3b8;">row = Math.floor(y / TILE);</div>
      <div style="color:var(--yellow);">h = |col - targetC| + |row - targetR|</div>
      <div style="color:var(--green);">f(n) = g(n) + h(n)</div>
    </div>
  </div>
</main>

<script>
var canvas = document.getElementById('simCanvas');
var ctx = canvas.getContext('2d');

var cols = 20, rows = 13;
var tileW = 40, tileH = 40;
var grid = [];

var hero = { c: 17, r: 6, x: 17 * 40 + 20, y: 6 * 40 + 20, size: 20 };
var enemy = { c: 2, r: 6, x: 2 * 40 + 20, y: 6 * 40 + 20, size: 20, speed: 2, angle: 0 };
var algorithm = 'astar';
var path = [];
var exploredCount = 0;
var sightConeActive = true;
var currentStep = 1;

var STEPS = {
  1: {
    desc: "<strong>1-Qadam:</strong> Devorga tiqilish xatosini fosh qilish — oddiy to'g'ri chiziqli ta'qib kodi devorga urilib qoladi.",
    prompt: "Menda Canvas o'yinim bor. Dushman qahramon tomon x += dx bilan boryapti, lekin o'rtada tosh devor tursa devorga tiqilib titrab qolyapti. Menga labirint devorlarini hisobga oluvchi grid qidiruv tizimi kerak.",
    action: function() { setAlgorithm('naive'); }
  },
  2: {
    desc: "<strong>2-Qadam:</strong> Grid va BFS qidiruvi — kataklar bo'yicha navbat (Queue) va visited to'plami bilan devorlarni aylanib o'tish.",
    prompt: "Men 2D roguelike o'yinimda dushman AI sini dasturlayapman. Menda 20x13 lik grid mavjud (0 - bo'sh joy, 1 - tosh devor). Dushman devorlarni aylanib qahramonga borishi uchun BFS algoritmini yozib ber. Navbat (Queue) va visited to'plamidan foydalan.",
    action: function() { setAlgorithm('bfs'); }
  },
  3: {
    desc: "<strong>3-Qadam:</strong> A* Manhattan Evristikasi — ortiqcha kataklarni tekshirmasdan, qidiruvni 5 barobar tezlashtirish.",
    prompt: "Hozirgi BFS algoritmi butun xaritani ko'r-ko'rona tekshiryapti. Unga A* (A-Star) evristikasini qo'sh: f(n) = g(n) + h(n), bu yerda h(n) Manhattan masofasi bo'lsin. Qidiruvni faqat qahramon tomon yo'naltiruvchi optimal kod ber.",
    action: function() { setAlgorithm('astar'); }
  },
  4: {
    desc: "<strong>4-Qadam:</strong> Vibe-Juice va Ko'rish Nuri — 90 darajali Sight Cone va dushmanning '!' ogohlantirish belgisini qo'shish.",
    prompt: "Dushmanga kiber-hissiyot (vibe-juice) qo'sh: dushman boshining ustida qizil '!' ogohlantirish belgisi yonsin, 90 darajali ko'rish nuri (Sight Cone) qahramonga tekkanda dushman tezligi 1.8x ga oshib, A* bilan quvlasin.",
    action: function() {
      sightConeActive = true;
      setAlgorithm('astar');
    }
  }
};

function switchPromptStep(step) {
  currentStep = step;
  var btns = document.querySelectorAll('.step-btn');
  btns.forEach(function(b, idx) {
    if (idx + 1 === step) b.classList.add('active');
    else b.classList.remove('active');
  });
  document.getElementById('stepDesc').innerHTML = STEPS[step].desc;
  document.getElementById('stepPromptText').textContent = STEPS[step].prompt;
}

function copyPrompt() {
  var text = STEPS[currentStep].prompt;
  navigator.clipboard.writeText(text).then(function() {
    alert('Prompt nusxalandi! Endi uni AI (Cursor / Claude / Copilot) ga yuboring!');
  });
}

function applyStepCode() {
  STEPS[currentStep].action();
  alert(currentStep + '-Qadam kodi simulyatorga muvaffaqiyatli tatbiq etildi!');
}

function resetWalls() {
  grid = [];
  for (var r = 0; r < rows; r++) {
    var row = [];
    for (var c = 0; c < cols; c++) {
      row.push(0);
    }
    grid.push(row);
  }
  // Create challenging labyrinth walls
  for (var r = 2; r <= 10; r++) grid[r][10] = 1;
  for (var c = 5; c <= 9; c++) grid[3][c] = 1;
  for (var c = 11; c <= 15; c++) grid[9][c] = 1;
  recomputePath();
}

function setAlgorithm(algo) {
  algorithm = algo;
  ['btnAlgoAStar', 'btnAlgoBFS', 'btnAlgoNaive'].forEach(function(id) {
    var b = document.getElementById(id);
    if ((algo === 'astar' && id === 'btnAlgoAStar') ||
        (algo === 'bfs' && id === 'btnAlgoBFS') ||
        (algo === 'naive' && id === 'btnAlgoNaive')) {
      b.style.borderColor = 'var(--accent)';
      b.style.color = 'var(--accent)';
    } else {
      b.style.borderColor = 'rgba(255,255,255,0.1)';
      b.style.color = '#fff';
    }
  });
  recomputePath();
}

function toggleSightCone() {
  sightConeActive = !sightConeActive;
}

function recomputePath() {
  enemy.c = Math.floor(enemy.x / tileW);
  enemy.r = Math.floor(enemy.y / tileH);
  hero.c = Math.floor(hero.x / tileW);
  hero.r = Math.floor(hero.y / tileH);

  if (algorithm === 'naive') {
    path = [{ c: hero.c, r: hero.r }];
    exploredCount = 1;
    document.getElementById('hudSteps').textContent = 'Direct';
    document.getElementById('hudExplored').textContent = '1';
    return;
  }

  var start = { c: enemy.c, r: enemy.r };
  var target = { c: hero.c, r: hero.r };

  var openSet = [{ c: start.c, r: start.r, g: 0, h: 0, f: 0, parent: null }];
  var closedSet = new Set();
  path = [];
  exploredCount = 0;

  while (openSet.length > 0) {
    var currentIdx = 0;
    if (algorithm === 'astar') {
      for (var i = 1; i < openSet.length; i++) {
        if (openSet[i].f < openSet[currentIdx].f) currentIdx = i;
      }
    }
    var current = openSet.splice(currentIdx, 1)[0];
    exploredCount++;

    var key = current.c + ',' + current.r;
    closedSet.add(key);

    if (current.c === target.c && current.r === target.r) {
      var curr = current;
      while (curr) {
        path.push({ c: curr.c, r: curr.r });
        curr = curr.parent;
      }
      path.reverse();
      break;
    }

    var neighbors = [
      { c: current.c + 1, r: current.r },
      { c: current.c - 1, r: current.r },
      { c: current.c, r: current.r + 1 },
      { c: current.c, r: current.r - 1 }
    ];

    for (var n = 0; n < neighbors.length; n++) {
      var nb = neighbors[n];
      if (nb.c < 0 || nb.c >= cols || nb.r < 0 || nb.r >= rows) continue;
      if (grid[nb.r][nb.c] === 1) continue;
      var nKey = nb.c + ',' + nb.r;
      if (closedSet.has(nKey)) continue;

      var g = current.g + 1;
      var h = Math.abs(nb.c - target.c) + Math.abs(nb.r - target.r);
      var f = g + (algorithm === 'astar' ? h : 0);

      var existing = openSet.find(function(item) { return item.c === nb.c && item.r === nb.r; });
      if (!existing) {
        openSet.push({ c: nb.c, r: nb.r, g: g, h: h, f: f, parent: current });
      } else if (g < existing.g) {
        existing.g = g;
        existing.f = f;
        existing.parent = current;
      }
    }
  }

  document.getElementById('hudSteps').textContent = path.length > 0 ? (path.length - 1) : 'To‘siq!';
  document.getElementById('hudExplored').textContent = exploredCount;
}

canvas.addEventListener('pointerdown', function(e) {
  var rect = canvas.getBoundingClientRect();
  var scaleX = canvas.width / rect.width;
  var scaleY = canvas.height / rect.height;
  var tx = (e.clientX - rect.left) * scaleX;
  var ty = (e.clientY - rect.top) * scaleY;
  var c = Math.floor(tx / tileW);
  var r = Math.floor(ty / tileH);
  if (c >= 0 && c < cols && r >= 0 && r < rows) {
    if ((c === hero.c && r === hero.r) || (c === enemy.c && r === enemy.r)) return;
    grid[r][c] = grid[r][c] === 1 ? 0 : 1;
    recomputePath();
  }
});

canvas.addEventListener('mousemove', function(e) {
  if (e.buttons === 1) return;
  var rect = canvas.getBoundingClientRect();
  var scaleX = canvas.width / rect.width;
  var scaleY = canvas.height / rect.height;
  var tx = (e.clientX - rect.left) * scaleX;
  var ty = (e.clientY - rect.top) * scaleY;
  var c = Math.floor(tx / tileW);
  var r = Math.floor(ty / tileH);
  if (c >= 0 && c < cols && r >= 0 && r < rows) {
    if (grid[r][c] === 0) {
      hero.x = tx;
      hero.y = ty;
      hero.c = c;
      hero.r = r;
      recomputePath();
    }
  }
});

function gameLoop() {
  ctx.fillStyle = '#020617';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Draw Grid & Walls
  for (var r = 0; r < rows; r++) {
    for (var c = 0; c < cols; c++) {
      var x = c * tileW;
      var y = r * tileH;
      if (grid[r][c] === 1) {
        ctx.fillStyle = '#1e293b';
        ctx.strokeStyle = '#334155';
        ctx.lineWidth = 2;
        ctx.fillRect(x + 1, y + 1, tileW - 2, tileH - 2);
        ctx.strokeRect(x + 1, y + 1, tileW - 2, tileH - 2);
      } else {
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.03)';
        ctx.strokeRect(x, y, tileW, tileH);
      }
    }
  }

  // Draw Path Line
  if (path.length > 1 && algorithm !== 'naive') {
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 3;
    ctx.beginPath();
    for (var p = 0; p < path.length; p++) {
      var px = path[p].c * tileW + tileW / 2;
      var py = path[p].r * tileH + tileH / 2;
      if (p === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();
  }

  // Move Enemy along path
  if (algorithm === 'naive') {
    var dx = hero.x - enemy.x;
    var dy = hero.y - enemy.y;
    var dist = Math.hypot(dx, dy);
    if (dist > 10) {
      var nextX = enemy.x + (dx / dist) * enemy.speed;
      var nextY = enemy.y + (dy / dist) * enemy.speed;
      var nC = Math.floor(nextX / tileW);
      var nR = Math.floor(nextY / tileH);
      if (grid[nR] && grid[nR][nC] === 1) {
        // Stuck in wall! Vibrate bug
        enemy.x += (Math.random() - 0.5) * 3;
        enemy.y += (Math.random() - 0.5) * 3;
      } else {
        enemy.x = nextX;
        enemy.y = nextY;
      }
    }
  } else if (path.length > 1) {
    var targetTile = path[1];
    var tX = targetTile.c * tileW + tileW / 2;
    var tY = targetTile.r * tileH + tileH / 2;
    var edx = tX - enemy.x;
    var edy = tY - enemy.y;
    var eDist = Math.hypot(edx, edy);
    if (eDist > 2) {
      enemy.x += (edx / eDist) * enemy.speed;
      enemy.y += (edy / eDist) * enemy.speed;
      enemy.angle = Math.atan2(edy, edx);
    } else {
      recomputePath();
    }
  }

  // Draw Sight Cone
  if (sightConeActive) {
    ctx.fillStyle = 'rgba(239, 68, 68, 0.15)';
    ctx.beginPath();
    ctx.moveTo(enemy.x, enemy.y);
    ctx.arc(enemy.x, enemy.y, 160, enemy.angle - 0.5, enemy.angle + 0.5);
    ctx.closePath();
    ctx.fill();
  }

  // Draw Enemy Alert Icon
  ctx.fillStyle = '#ef4444';
  ctx.font = 'bold 16px monospace';
  ctx.fillText('!', enemy.x - 4, enemy.y - 18);

  // Draw Enemy
  ctx.fillStyle = '#ef4444';
  ctx.beginPath();
  ctx.arc(enemy.x, enemy.y, enemy.size / 2, 0, Math.PI * 2);
  ctx.fill();

  // Draw Hero
  ctx.fillStyle = '#38bdf8';
  ctx.beginPath();
  ctx.arc(hero.x, hero.y, hero.size / 2, 0, Math.PI * 2);
  ctx.fill();

  requestAnimationFrame(gameLoop);
}

resetWalls();
requestAnimationFrame(gameLoop);
</script>
</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "simulator", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: simulator/index.html")

def main():
    print("Building Lesson 33 (Grades 7–8, 80-min Double Block, Enemy AI & Pathfinding)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_simulator()
    print("Lesson 33 build complete!")

if __name__ == "__main__":
    main()
