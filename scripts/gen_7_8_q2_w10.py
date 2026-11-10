#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator for 7-8-sinf 10-hafta 29-dars:
Matritsalar va Xaritalar (Tilemaps): 2D Labirint va Platformalar
"""

import os
import json
import html

FOLDER = "classes/7-8-sinf/10-hafta/29-dars-tilemaps-va-2d-labirint"
os.makedirs(FOLDER, exist_ok=True)
os.makedirs(os.path.join(FOLDER, "simulator"), exist_ok=True)

# Load CSS from 28-dars
with open("classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/prezentatsiya.html", "r", encoding="utf-8") as f:
    t28 = f.read()

css_chunk = t28[t28.find("<style>"):t28.find("</style>") + 8]

SLIDES = [
    # 1. Kirish
    {
        "phase": "KIRISH|ВВЕДЕНИЕ|INTRO",
        "eyebrow": {"uz": "7–8-SINF · 10-HAFTA · 29-DARS", "ru": "7–8 КЛАСС · 10-Я НЕДЕЛЯ · УРОК 29", "en": "GRADE 7–8 · WEEK 10 · LESSON 29"},
        "title": {"uz": "Matritsalar va Xaritalar (Tilemaps): 2D Labirint va Platformalar", "ru": "Матрицы и Карты (Tilemaps): 2D Лабиринт и Платформы", "en": "Matrices & Tilemaps: 2D Maze & Platformers"},
        "lede": {"uz": "2-Chorakda o'z shaxsiy Roguelike yer osti qasrimizni quramiz: massivlar orqali dunyo yaratish san'ati!", "ru": "Во 2-й четверти создаем собственный Roguelike лабиринт: искусство создания миров через массивы!", "en": "In Quarter 2, we engineer a full Roguelike dungeon: the art of building game worlds via arrays!"},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="Матрица сетки" data-en="Grid Matrix">2D Massivlar</div>
    <h3 data-ru="Цифровая карта" data-en="Digital Map">Sonlar Matritsasi</h3>
    <p data-ru="Каждая клетка карты — число в двумерном массиве: 0 — тропа, 1 — кирпичная стена, 2 — золотая монета." data-en="Every cell is an integer in a 2D array: 0 for path, 1 for brick wall, 2 for gold coin.">Har bir katak — 2D massivdagi bitta son: 0 — yo'l, 1 — tosh devor, 2 — oltin tanga, 3 — portal.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Скорость O(1)" data-en="O(1) Speed">Panjara Fizikasi</div>
    <h3 data-ru="Коллизии без лагов" data-en="Lag-free Collisions">Tezyurar To'qnashuv</h3>
    <p data-ru="Вместо проверки 1000 препятствий проверяем одну ячейку map[row][col]. Скорость 60 FPS!" data-en="Instead of checking 1000 obstacles, inspect a single cell map[row][col]. Solid 60 FPS!">1000 ta devorni tekshirish o'rniga faqat o'yinchi borayotgan bitta katak tekshiriladi.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Результат урока" data-en="Lesson Deliverable">Dars natijasi</div>
    <h3 data-ru="Живой 2D Лабиринт" data-en="Living 2D Maze">Ishlovchi 2D Labirint</h3>
    <p data-ru="Полноценный движок карты на Canvas 2D: игрок свободно бегает по лабиринту и собирает сокровища." data-en="A complete Canvas 2D tilemap engine: the hero navigates corridors and gathers dungeon treasures.">Canvas 2D da sonlar o'zgarishi bilan xaritasi yangilanadigan va devorga urilmaydigan o'yin.</p>
  </div>
</div>
""",
        "note": ["2-Chorak geym-dev rejasini ochish", "O'quvchilarga 2-chorak davomida to'liq Roguelike o'yinini yaratishimizni (tuman, dushman sun'iy intellekti, o'qlar va inventar) e'lon qiling.", "Ushbu buyuk loyihaning poydevori aynan bugungi darsdagi Tilemap ekanini uqtiring."]
    },

    # 2. Muammo
    {
        "phase": "MUAMMO|ПРОБЛЕМА|PROBLEM",
        "eyebrow": {"uz": "AQLIY HUJUM · MUAMMO", "ru": "МОЗГОВОЙ ШТУРМ · ПРОБЛЕМА", "en": "BRAINSTORMING · PROBLEM"},
        "title": {"uz": "Nega O'yin Dunyosini Bitta Katta Rasm Qilib Chizib Bo'lmaydi?", "ru": "Почему Нельзя Нарисовать Мир Одной Большой Картинкой?", "en": "Why Not Draw the Game World as One Giant Picture?"},
        "lede": {"uz": "10,000 x 10,000 pikselli ulkan rasmni xotiraga yuklasangiz, telefon va noutbuklar qotib qoladi (RAM crash).", "ru": "Загрузка гигантской картинки 10,000x10,000 пикселей вызовет краш оперативной памяти (RAM).", "en": "Loading a single massive 10,000x10,000 pixel image will crash available RAM immediately."},
        "body": """
<div class="compare-grid">
  <div class="compare-card bad">
    <div class="badge-bad" data-ru="Огромная картинка (Плохо)" data-en="Giant Image (Bad)">Bitta ulkan rasm (Yomon)</div>
    <h4 data-ru="Файл весит 400 МБ, RAM переполнен" data-en="400 MB file size, memory overload">Fayl hajmi 400 MB, xotira to'lib ketadi</h4>
    <p data-ru="Нельзя изменить карту на лету. Персонаж не знает, где на картинке нарисована стена, а где пол." data-en="Cannot modify map dynamically. The game has no clue which pixels are walls vs walkable floor.">Xaritani dinamik o'zgartirib bo'lmaydi. Kompyuter rasmning qaysi piksellari devor ekanini tushunmaydi.</p>
  </div>
  <div class="compare-card good">
    <div class="badge-good" data-ru="Tilemap сетка (Гениально)" data-en="Tilemap Grid (Smart)">Tilemap panjarasi (Aqlli)</div>
    <h4 data-ru="Матрица весит 2 КБ, супер-быстро" data-en="Matrix weighs 2 KB, blazing fast">Matritsa bor-yo'g'i 2 KB, yashin tezligida</h4>
    <p data-ru="Один спрайт стены (32x32 px) повторяется 1000 раз по сетке. Карта меняется за 1 миллисекунду!" data-en="A single 32x32 wall sprite is stamped 1000 times by matrix index. Instant map updates!">Bitta 32x32 devor tayli matritsa orqali ming marta qayta ishlatiladi. Xarita bir zumda yangilanadi!</p>
  </div>
</div>
""",
        "note": ["Xotirani tejash muammosi", "O'yin yaratuvchilari doim resurslarni tejashga majbur. Minecraft yoki Zelda o'yinlari aynan tile (blok) tizimida qurilgan.", "400 MB li rasm o'rniga 2 KB li massiv qanday qilib butun dunyoni saqlashini ta'kidlang."]
    },

    # 3. Konsept
    {
        "phase": "KONSEPT|КОНЦЕПТ|CONCEPT",
        "eyebrow": {"uz": "ARXITEKTURA · ASOS", "ru": "АРХИТЕКТУРА · ОСНОВА", "en": "ARCHITECTURE · CORE"},
        "title": {"uz": "Tilemap Anatomiyasi: Kataklar, Tayllar va Lug'at", "ru": "Анатомия Tilemap: Ячейки, Тайлы и Словарь", "en": "Tilemap Anatomy: Cells, Tiles and Lookup"},
        "lede": {"uz": "Har bir katak — raqam. Har bir raqam esa o'yin lug'atidagi (Tileset) bitta grafik blokni bildiradi.", "ru": "Каждая ячейка — число. Число ссылается на графический блок в словаре тайлов (Tileset).", "en": "Every cell is an integer. That number maps directly to a graphical block in the tileset dictionary."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="Индекс 0" data-en="Index 0">0: Bo'sh Yo'l (Floor)</div>
    <h3 data-ru="Проходимая зона" data-en="Walkable Zone">Qadam bosiladigan yer</h3>
    <p data-ru="Коридор или комната, по которой игрок и враги могут свободно перемещаться." data-en="Corridor or chamber where player and monsters roam freely.">Qahramon hech qanday to'siqsiz yugura oladigan tekis pol.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Индекс 1" data-en="Index 1">1: Tosh Devor (Wall)</div>
    <h3 data-ru="Твердое препятствие" data-en="Solid Obstacle">O'tib bo'lmas to'siq</h3>
    <p data-ru="Блокирует движение. Игрок не может зайти в ячейку, где записана единица." data-en="Blocks motion completely. Hero cannot enter any cell with value 1.">Qahramonning harakatini to'xtatuvchi mustahkam tosh devor.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Индекс 2 & 3" data-en="Index 2 & 3">2 & 3: Xazina va Chiqish</div>
    <h3 data-ru="Интерактивные цели" data-en="Interactive Targets">Oltin va Portal</h3>
    <p data-ru="2 — золотая монетка (дает +50 очков), 3 — портал выхода на следующий уровень." data-en="2 is a golden coin (+50 pts), 3 is the magic portal to the next level.">2 — ochko beruvchi oltin tanga, 3 — keyingi bosqichga o'tish eshigi.</p>
  </div>
</div>
""",
        "note": ["Lug'at analogiyasi", "Xaritaning raqamlari qanday qilib rasmga aylanishini doskaga yozing: 0=qora pol, 1=kulrang g'isht, 2=sariq doira.", "Kompyuter faqat sonlarni ko'radi, Canvas esa ularni rasmga aylantiradi."]
    },

    # 4. Sxema
    {
        "phase": "ARXITEKTURA|АРХИТЕКТУРА|ARCHITECTURE",
        "eyebrow": {"uz": "INLINE SVG · TIZIM SXEMASI", "ru": "INLINE SVG · СХЕМА СИСТЕМЫ", "en": "INLINE SVG · SYSTEM SCHEMA"},
        "title": {"uz": "2D Massivdan Ekrandagi Canvas Piksellarigacha", "ru": "От 2D Массива до Пикселей на Canvas", "en": "From 2D Array to Pixels on Canvas"},
        "lede": {"uz": "Matritsaning qatori (row) Y o'qiga, ustuni (col) esa X o'qiga ko'paytiriladi: col * TILE_SIZE.", "ru": "Строка (row) умножается на Y, а колонка (col) — на X: col * TILE_SIZE.", "en": "Matrix row maps to Y and column to X: col * TILE_SIZE."},
        "body": """
<div style="background:var(--panel-2); border:1px solid var(--rule); border-radius:12px; padding:18px; margin-bottom:12px; text-align:center;">
  <svg viewBox="0 0 520 220" style="max-width:100%; height:auto;">
    <!-- Array representation -->
    <rect x="20" y="20" width="220" height="180" fill="var(--sheet)" stroke="var(--rule)" stroke-width="1.5" rx="8" />
    <text x="35" y="45" fill="var(--accent-ink)" font-family="JetBrains Mono" font-size="12" font-weight="700">const map = [</text>
    <text x="50" y="75" fill="var(--ink)" font-family="JetBrains Mono" font-size="13">[1, 1, 1, 1, 1],</text>
    <text x="50" y="105" fill="var(--ink)" font-family="JetBrains Mono" font-size="13">[1, 0, 2, 0, 1],</text>
    <text x="50" y="135" fill="var(--ink)" font-family="JetBrains Mono" font-size="13">[1, 0, 1, 3, 1],</text>
    <text x="50" y="165" fill="var(--ink)" font-family="JetBrains Mono" font-size="13">[1, 1, 1, 1, 1]</text>
    <text x="35" y="190" fill="var(--accent-ink)" font-family="JetBrains Mono" font-size="12" font-weight="700">];</text>

    <!-- Arrow -->
    <path d="M 255 110 L 295 110" stroke="var(--accent)" stroke-width="3" marker-end="url(#arrow)" />
    <text x="250" y="95" fill="var(--accent)" font-family="JetBrains Mono" font-size="10" font-weight="700">Render</text>

    <!-- Canvas rendered grid -->
    <g transform="translate(310, 30)">
      <!-- Row 0: all walls -->
      <rect x="0" y="0" width="32" height="32" fill="#4A5568" stroke="#2D3748" />
      <rect x="34" y="0" width="32" height="32" fill="#4A5568" stroke="#2D3748" />
      <rect x="68" y="0" width="32" height="32" fill="#4A5568" stroke="#2D3748" />
      <rect x="102" y="0" width="32" height="32" fill="#4A5568" stroke="#2D3748" />
      <rect x="136" y="0" width="32" height="32" fill="#4A5568" stroke="#2D3748" />

      <!-- Row 1: Wall, Floor, Coin, Floor, Wall -->
      <rect x="0" y="34" width="32" height="32" fill="#4A5568" stroke="#2D3748" />
      <rect x="34" y="34" width="32" height="32" fill="#1A202C" stroke="#2D3748" />
      <rect x="68" y="34" width="32" height="32" fill="#1A202C" stroke="#2D3748" />
      <circle cx="84" cy="50" r="8" fill="#ECC94B" />
      <rect x="102" y="34" width="32" height="32" fill="#1A202C" stroke="#2D3748" />
      <rect x="136" y="34" width="32" height="32" fill="#4A5568" stroke="#2D3748" />

      <!-- Row 2: Wall, Floor, Wall, Portal, Wall -->
      <rect x="0" y="68" width="32" height="32" fill="#4A5568" stroke="#2D3748" />
      <rect x="34" y="68" width="32" height="32" fill="#1A202C" stroke="#2D3748" />
      <rect x="68" y="68" width="32" height="32" fill="#4A5568" stroke="#2D3748" />
      <rect x="102" y="68" width="32" height="32" fill="#1A202C" stroke="#2D3748" />
      <rect x="108" y="74" width="20" height="20" fill="#9F7AEA" rx="4" />
      <rect x="136" y="68" width="32" height="32" fill="#4A5568" stroke="#2D3748" />

      <!-- Row 3: all walls -->
      <rect x="0" y="102" width="32" height="32" fill="#4A5568" stroke="#2D3748" />
      <rect x="34" y="102" width="32" height="32" fill="#4A5568" stroke="#2D3748" />
      <rect x="68" y="102" width="32" height="32" fill="#4A5568" stroke="#2D3748" />
      <rect x="102" y="102" width="32" height="32" fill="#4A5568" stroke="#2D3748" />
      <rect x="136" y="102" width="32" height="32" fill="#4A5568" stroke="#2D3748" />
    </g>
  </svg>
</div>
""",
        "note": ["Vizual transformatsiya", "Chapdagi JavaScript massivi o'ngdagi ko'rinishga qanday aylanishini tushuntiring.", "Har bir 1 soni kulrang tosh devorga, 2 soni oltin tangaga, 3 esa binafsha eshikka aylanmoqda."]
    },

    # 5. Mexanizm (Nested Loops)
    {
        "phase": "MEXANIZM|МЕХАНИЗМ|MECHANISM",
        "eyebrow": {"uz": "ALGORITM · RENDER", "ru": "АЛГОРИТМ · РЕНДЕР", "en": "ALGORITHM · RENDER"},
        "title": {"uz": "Ichma-ich Sikllar: Matritsani Chizuvchi Dvigatel", "ru": "Вложенные Циклы: Движок Отрисовки Матрицы", "en": "Nested Loops: The Matrix Rendering Engine"},
        "lede": {"uz": "Xaritani ekranga chiqarish uchun ikkita sikl kerak: qatorlar bo'ylab (row) va ustunlar bo'ylab (col).", "ru": "Чтобы вывести карту, нужны два цикла: по строкам (row) и по колонкам (col).", "en": "Two nested loops render the grid: one for rows and an inner one for columns."},
        "body": """
<div class="code-snippet">
<span style="color:#E67E22;">const</span> TILE_SIZE = <span style="color:#00D68F;">32</span>;<br><br>
<span style="color:#0066FF;">function</span> <span style="color:#FFB703;">drawMap</span>(ctx, map) {{<br>
&nbsp;&nbsp;<span style="color:#0066FF;">for</span> (<span style="color:#E67E22;">let</span> row = <span style="color:#00D68F;">0</span>; row &lt; map.length; row++) {{<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0066FF;">for</span> (<span style="color:#E67E22;">let</span> col = <span style="color:#00D68F;">0</span>; col &lt; map[row].length; col++) {{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#E67E22;">const</span> tile = map[row][col];<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#0066FF;">if</span> (tile === <span style="color:#00D68F;">1</span>) {{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ctx.fillStyle = <span style="color:#FFD166;">"#4A5568"</span>; &nbsp;<span style="color:var(--ink-3);">// Tosh devor</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ctx.fillRect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE);<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}} <span style="color:#0066FF;">else if</span> (tile === <span style="color:#00D68F;">2</span>) {{<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ctx.fillStyle = <span style="color:#FFD166;">"#ECC94B"</span>; &nbsp;<span style="color:var(--ink-3);">// Oltin tanga</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ctx.fillRect(col * TILE_SIZE + <span style="color:#00D68F;">10</span>, row * TILE_SIZE + <span style="color:#00D68F;">10</span>, <span style="color:#00D68F;">12</span>, <span style="color:#00D68F;">12</span>);<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}}<br>
&nbsp;&nbsp;&nbsp;&nbsp;}}<br>
&nbsp;&nbsp;}}<br>
}}
</div>
""",
        "note": ["Ichma-ich sikl kodi", "O'quvchilarga nima uchun col * TILE_SIZE X koordinatasi, row * TILE_SIZE esa Y koordinatasi ekanini ko'rsating.", "row pastga qarab sanaladi (Y), col esa o'ngga qarab sanaladi (X)."]
    },

    # 6. Taqqoslash (Collision)
    {
        "phase": "TAQQOSLASH|СРАВНЕНИЕ|COMPARISON",
        "eyebrow": {"uz": "FIZIKA OPTIMIZATSIYASI", "ru": "ОПТИМИЗАЦИЯ ФИЗИКИ", "en": "PHYSICS OPTIMIZATION"},
        "title": {"uz": "Piksellar AABB To'qnashuvi vs Panjara To'qnashuvi (O(1))", "ru": "Пиксельные Коллизии AABB vs Коллизии по Сетке (O(1))", "en": "Pixel AABB Collisions vs Grid Collisions (O(1))"},
        "lede": {"uz": "1-Chorakda o'rgangan to'rtburchaklar to'qnashuvi (AABB) 1000 ta devorda o'yinni qotirib qo'yadi. Tilemap esa 1 ta amal bilan yechadi!", "ru": "Проверка AABB по 1000 стенам вызовет лаги. Tilemap решает коллизию всего за 1 операцию!", "en": "Checking AABB across 1000 walls causes severe lag. Tilemaps resolve collisions in a single O(1) step!"},
        "body": """
<div class="compare-grid">
  <div class="compare-card bad">
    <div class="badge-bad" data-ru="Цикл по всем стенам: O(N)" data-en="Loop Over All Walls: O(N)">Har bir devorni tekshirish: O(N)</div>
    <h4 data-ru="1000 стен = 1000 проверок в каждом кадре" data-en="1000 walls = 1000 checks per frame">1000 devor = har kadrda 1000 ta if</h4>
    <p data-ru="Игра начинает тормозить и греть процессор. Игрок застревает в углах." data-en="Game drops frames and burns CPU. The character gets caught on corners.">Dushmanlar va o'qlar ko'payishi bilan kompyuter qotishni (FPS pasayishi) boshlaydi.</p>
  </div>
  <div class="compare-card good">
    <div class="badge-good" data-ru="Проверка одной ячейки: O(1)" data-en="Single Cell Lookup: O(1)">Bitta katakni tekshirish: O(1)</div>
    <h4 data-ru="map[nextRow][nextCol] === 1" data-en="map[nextRow][nextCol] === 1">map[nextRow][nextCol] === 1</h4>
    <p data-ru="Игрок делает шаг? Просто делим его X и Y на TILE_SIZE и мгновенно узнаем, свободна ли клетка!" data-en="Player moving? Simply divide X and Y by TILE_SIZE to know if the target cell is free!">O'yinchi qadam bosayotgan joy devormi? Koordinatani 32 ga bo'lamiz va darhol bilamiz!</p>
  </div>
</div>
""",
        "note": ["Algoritmik tezlik", "O(N) va O(1) farqini oddiy so'zlar bilan tushuntiring: 1000 ta kitobni bittalab varaqlab izlash (O(N)) yoki kitob mundarijasidan sahifani darhol ochish (O(1)).", "Tilemap bu o'yin xaritasining mundarijasidir."]
    },

    # 7. Xavfsizlik (Edge cases)
    {
        "phase": "XAVFSIZLIK|БЕЗОПАСНОСТЬ|SAFETY",
        "eyebrow": {"uz": "CHEGARA XATOLARI", "ru": "ОШИБКИ ГРАНИЦ", "en": "BOUNDARY ERRORS"},
        "title": {"uz": "Klassik Xatolik: 'Cannot read properties of undefined'", "ru": "Классическая Ошибка: 'Cannot read properties of undefined'", "en": "Classic Crash: 'Cannot read properties of undefined'"},
        "lede": {"uz": "Agar o'yinchi xaritadan tashqariga (masalan, row = -1) chiqishga urinsa, JavaScript darhol qulaydi.", "ru": "Если игрок попытается шагнуть за пределы карты (row = -1), JS выбросит фатальную ошибку.", "en": "If the player steps out of map bounds (e.g. row = -1), JavaScript throws a fatal runtime crash."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge-bad" data-ru="Краш игры" data-en="Game Crash">Xavfli Kod (Himoyasiz)</div>
    <div class="code-snippet">
      <span style="color:#0066FF;">function</span> canMove(row, col) {{<br>
      &nbsp;&nbsp;<span style="color:#FF1100;">return map[row][col] !== 1;</span><br>
      }}
    </div>
    <p data-ru="Если row = -1, map[-1] вернет undefined. undefined[col] выбросит ошибку и остановит игру!" data-en="If row = -1, map[-1] is undefined. Reading undefined[col] crashes the entire game loop!">Agar row = -1 bo'lsa, map[-1] undefined beradi va dastur butunlay to'xtab qoladi!</p>
  </div>
  <div class="card" style="border-left:4px solid var(--ok);">
    <div class="badge-good" data-ru="Безопасный код" data-en="Safe Code">Xavfsiz Qalqon (Guarded)</div>
    <div class="code-snippet">
      <span style="color:#0066FF;">function</span> isWalkable(row, col) {{<br>
      &nbsp;&nbsp;<span style="color:#0066FF;">if</span> (row &lt; <span style="color:#00D68F;">0</span> || row &gt;= map.length) <span style="color:#0066FF;">return false</span>;<br>
      &nbsp;&nbsp;<span style="color:#0066FF;">if</span> (col &lt; <span style="color:#00D68F;">0</span> || col &gt;= map[<span style="color:#00D68F;">0</span>].length) <span style="color:#0066FF;">return false</span>;<br>
      &nbsp;&nbsp;<span style="color:#0066FF;">return</span> map[row][col] !== <span style="color:#00D68F;">1</span>;<br>
      }}
    </div>
    <p data-ru="Сначала проверяем границы сетки, и только затем лезем внутрь массива. 100% стабильность!" data-en="Bounds-check rows and cols before indexing into the array. 100% crash-proof!">Avval massiv chegaralarini tekshiramiz, keyin katakka murojaat qilamiz. Crash xavfi nol!</p>
  </div>
</div>
""",
        "note": ["Muhandislik xavfsizligi", "Katta dasturchilar ham yo'l qo'yadigan eng mashhur xato: massiv chegaralarini tekshirmaslik.", "Har doim avval chegarani tekshiruvchi qo'riqchi (Guard Clause) qo'yishni o'rgating."]
    },

    # 8. Real hayotiy keys
    {
        "phase": "AMALIYOT|ПРАКТИКА|PRACTICE",
        "eyebrow": {"uz": "SANOAT STANDARTI · GAMEDEV", "ru": "ИНДУСТРИАЛЬНЫЙ СТАНДАРТ", "en": "INDUSTRY STANDARD · GAMEDEV"},
        "title": {"uz": "Retro O'yinlardan 'Terraria' va 'Hades'gacha", "ru": "От Ретро-Игр до 'Terraria' и 'Hades'", "en": "From Retro Classics to 'Terraria' and 'Hades'"},
        "lede": {"uz": "Dunyoning eng mashhur o'yinlari aynan Tilemap poydevorida qurilgan. Massiv sonlarini o'zgartirib yangi olamlar yasashadi.", "ru": "Мировые бестселлеры построены на Tilemap. Меняя числа в массиве, они создают бесконечные миры.", "en": "Top games worldwide are built on Tilemaps. By modifying array values, infinite worlds are generated."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="1985 год" data-en="Year 1985">Super Mario Bros</div>
    <h3 data-ru="NES 8-битная эпоха" data-en="NES 8-bit Era">Nintendo 8-bit afsonasi</h3>
    <p data-ru="Картридж имел всего 40 КБ памяти! Только благодаря тайлам Марио смог прыгать по 32 уровням." data-en="Cartridge had only 40 KB ROM! Only tilemaps allowed 32 full worlds to fit.">Kassetada atigi 40 KB xotira bo'lgan! Faqat tayllar yordamida 32 ta dunyo sig'dirilgan.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="2011 год" data-en="Year 2011">Terraria</div>
    <h3 data-ru="Песочница на миллионы блоков" data-en="Sandbox of Millions">Millionlab Blokli Qumloq</h3>
    <p data-ru="Каждый блок грязи, камня или лавы — это элемент гигантского 2D массива. Можно копать и строить!" data-en="Every block of dirt, stone, or lava is a 2D array cell. Dig and construct dynamically!">Tuproq yoki toshni qaziganda, dastur faqat massivdagi 1 sonini 0 ga almashtirib qo'yadi!</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="2020 год" data-en="Year 2020">Hades & Roguelike</div>
    <h3 data-ru="Случайные комнаты" data-en="Procedural Rooms">Tasodifiy Labirintlar</h3>
    <p data-ru="Каждый запуск генерирует новую матрицу комнат. Игрок никогда не знает, что ждет за поворотом." data-en="Every run generates a new room matrix. The dungeon is always fresh and unpredictable.">Har safar o'lganda yangi sonlar matritsasi generatsiya qilinadi — bu Roguelike janri siri!</p>
  </div>
</div>
""",
        "note": ["Haqiqiy o'yinlar bilan ilhomlantirish", "O'quvchilar o'zlari o'ynaydigan Terraria, Celeste yoki Mario o'yinlarini eslashsin.", "Ular o'ynaydigan o'yinlar ortida ham aynan bugun biz yozayotgan oddiy sonlar matritsasi yotadi."]
    },

    # 9. Viktorina (Quiz & Fix)
    {
        "phase": "TEST|ТЕСТ|QUIZ",
        "eyebrow": {"uz": "KIBER-TEST · BILIMNI TEKSHIRISH", "ru": "КИБЕР-ТЕСТ · ПРОВЕРКА ЗНАНИЙ", "en": "CYBER-QUIZ · KNOWLEDGE CHECK"},
        "title": {"uz": "Viktorina: O'yinchi Pikselini Matritsa Katagiga Qanday Aylantiramiz?", "ru": "Викторина: Как Перевести Пиксели Игрока в Клетку Матрицы?", "en": "Quiz: How Do We Convert Player Pixels into Matrix Coordinates?"},
        "lede": {"uz": "O'yinchi piksel koordinatasi: player.x = 75, player.y = 100. TILE_SIZE = 32. O'yinchi qaysi katakda turibdi?", "ru": "Координаты игрока: x = 75, y = 100. TILE_SIZE = 32. В какой ячейке матрицы находится герой?", "en": "Player coords: x = 75, y = 100. TILE_SIZE = 32. Which matrix row and column contains the player?"},
        "body": """
<div class="quiz-box">
  <div class="quiz-option" onclick="checkQuiz(this, false)">
    <span>A)</span> <span data-ru="col = player.x * 32, row = player.y * 32 (Умножение)" data-en="col = player.x * 32, row = player.y * 32 (Multiply)">col = player.x * 32, row = player.y * 32 (Ko'paytirish)</span>
  </div>
  <div class="quiz-option" onclick="checkQuiz(this, true)">
    <span>B)</span> <span data-ru="col = Math.floor(player.x / 32), row = Math.floor(player.y / 32) (Деление с округлением)" data-en="col = Math.floor(player.x / 32), row = Math.floor(player.y / 32) (Floor division)">col = Math.floor(player.x / 32), row = Math.floor(player.y / 32) (Bo'lish va pastga yaxlitlash)</span>
  </div>
  <div class="quiz-option" onclick="checkQuiz(this, false)">
    <span>C)</span> <span data-ru="col = player.x + 32, row = player.y + 32 (Сложение)" data-en="col = player.x + 32, row = player.y + 32 (Addition)">col = player.x + 32, row = player.y + 32 (Qo'shish)</span>
  </div>
  <div class="quiz-option" onclick="checkQuiz(this, false)">
    <span>D)</span> <span data-ru="col = player.x % 32, row = player.y % 32 (Остаток)" data-en="col = player.x % 32, row = player.y % 32 (Modulo)">col = player.x % 32, row = player.y % 32 (Qoldiq)</span>
  </div>
</div>
<div style="margin-top:14px; text-align:center;">
  <button class="dock-btn" onclick="toggleTestFix()" style="padding:8px 16px; font-weight:700;" data-ru="Показать решение (Fix)" data-en="Reveal Solution (Fix)">💡 Yechimni Ko'rish (Fix)</button>
</div>
<div id="testFixBox" style="display:none; margin-top:12px; background:var(--panel-2); border:1px solid var(--ok); border-radius:8px; padding:12px;">
  <b style="color:var(--ok);" data-ru="Правильный ответ: B!" data-en="Correct Answer: B!">To'g'ri javob: B!</b>
  <p style="margin:4px 0 0;" data-ru="Потому что 75 / 32 = 2.34 -> Math.floor округляет до 2 (col = 2). А 100 / 32 = 3.12 -> округляет до 3 (row = 3). Игрок находится в ячейке map[3][2]!" data-en="75 / 32 = 2.34 -> Math.floor rounds down to 2 (col = 2). 100 / 32 = 3.12 -> rounds down to 3 (row = 3). Hero is at map[3][2]!">Chunki 75 / 32 = 2.34 -> Math.floor uni 2 ga yaxlitlaydi (col = 2). 100 / 32 = 3.12 -> uni 3 ga yaxlitlaydi (row = 3). Demak, qahramon map[3][2] katagida joylashgan!</p>
</div>
""",
        "note": ["Matematik formula", "Math.floor nima uchun kerakligini ko'rsating: piksellar kasr son bo'ladi (2.34), lekin massiv indekslari faqat butun son (0, 1, 2) bo'lishi shart.", "Bu formula har qanday 2D o'yinda o'yinchi turgan katakni aniqlashning oltin standartidir."]
    },

    # 10. Amaliy topshiriq
    {
        "phase": "AMALIYOT|ПРАКТИКА|PRACTICE",
        "eyebrow": {"uz": "GEYM-DEV MISSIYA · 15 DAQIQA", "ru": "ГЕЙМ-ДЕВ МИССИЯ · 15 МИНУТ", "en": "GAMEDEV MISSION · 15 MINUTES"},
        "title": {"uz": "Laboratoriya: O'z Roguelike Labirintingizni Yarating", "ru": "Лаборатория: Создайте Свой Roguelike Лабиринт", "en": "Lab: Engineer Your Own Roguelike Dungeon"},
        "lede": {"uz": "VS Code yoki brauzerda 10x10 lik 2D massiv tuzamiz va Canvas-da labirintni renderlaymiz!", "ru": "Создаем массив 10x10 в VS Code и отрисовываем лабиринт на Canvas!", "en": "Build a 10x10 array in VS Code and render the labyrinth onto Canvas!"},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="Шаг 1" data-en="Step 1">1-Qadam: Matritsa</div>
    <h3 data-ru="Создание 2D массива" data-en="Create 2D Array">10x10 xarita tuzish</h3>
    <p data-ru="Задайте массив «map»: по краям 1 (стены), внутри 0 (путь) и портал 3 в углу." data-en="Define initial 'map' array: borders are 1 (walls), interior is 0 (paths), portal 3 at corner.">Chetlari 1 (devor), ichkarisi 0 (yo'l) va chiqishda 3 (portal) bo'lgan massiv e'lon qiling.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Шаг 2" data-en="Step 2">2-Qadam: Dvigatel</div>
    <h3 data-ru="Отрисовка в цикле" data-en="Render Loops">drawMap() funksiyasi</h3>
    <p data-ru="С помощью вложенных циклов проверьте каждое число и отрисуйте прямоугольник в col*32, row*32." data-en="Use nested loops to check each tile and fillRect at col*32, row*32 accordingly.">Ichma-ich for siklida devorlar (kulrang), yo'l (qora) va tangalarni (sariq) chizing.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Шаг 3" data-en="Step 3">3-Qadam: O'yinchi</div>
    <h3 data-ru="Управление WASD" data-en="WASD Controls">To'qnashuv bilan yurish</h3>
    <p data-ru="При нажатии клавиш: если map[nextRow][nextCol] !== 1, переместите персонажа вперёд!" data-en="When key pressed: if map[nextRow][nextCol] !== 1, allow player to step forward!">Devorga urilmaydigan va tangalarni yig'ganda ularni 0 ga aylantiruvchi harakatni qo'shing.</p>
  </div>
</div>
""",
        "note": ["Amaliyotni tashkil etish", "O'quvchilar simulator/index.html ni ochishlari yoki VS Code da o'z fayllarini yozishlari mumkin.", "Tangani yeganda nima bo'lishini tushuntiring: map[row][col] = 0 ga aylanadi va ball oshadi!"]
    },

    # 11. Baholash mezoni
    {
        "phase": "BAHOLASH|ОЦЕНКА|GRADING",
        "eyebrow": {"uz": "10 BALLIK MEZON", "ru": "10-БАЛЛЬНАЯ ШКАЛА", "en": "10-POINT RUBRIC"},
        "title": {"uz": "Bugungi Darsni Baholash Mezonlari", "ru": "Критерии Оценки за Сегодняшний Урок", "en": "Today's Lesson Evaluation Rubric"},
        "lede": {"uz": "Geym-dizayn va algoritmik aniqlik 10 ballik muhandislik shkalasida baholanadi.", "ru": "Гейм-дизайн и алгоритмическая точность оцениваются по 10-балльной шкале.", "en": "Game design architecture and algorithmic precision evaluated on a 10-point scale."},
        "body": """
<div class="rubric-grid" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px;">
  <div class="card" style="text-align:center;">
    <div style="font-family:'JetBrains Mono'; font-size:20px; font-weight:800; color:var(--accent);">3 Ball</div>
    <b data-ru="2D Матрица карты" data-en="2D Map Matrix">To'g'ri 2D Massiv</b>
    <p style="font-size:12px; margin-top:4px;" data-ru="Матрица 10x10 объявлена без синтаксических ошибок." data-en="10x10 matrix declared cleanly without syntax errors.">10x10 massiv xatosiz e'lon qilingan, chetlari yopiq.</p>
  </div>
  <div class="card" style="text-align:center;">
    <div style="font-family:'JetBrains Mono'; font-size:20px; font-weight:800; color:var(--accent);">3 Ball</div>
    <b data-ru="Рендер на Canvas" data-en="Canvas Rendering">Ichma-ich Sikl Render</b>
    <p style="font-size:12px; margin-top:4px;" data-ru="Отрисовка всех тайлов через col*32 и row*32." data-en="All tiles rendered properly via col*32 and row*32.">Barcha tayllar ekranga to'g'ri piksellarda chizilgan.</p>
  </div>
  <div class="card" style="text-align:center;">
    <div style="font-family:'JetBrains Mono'; font-size:20px; font-weight:800; color:var(--accent);">2 Ball</div>
    <b data-ru="Коллизии по сетке" data-en="Grid Collisions">Devor To'qnashuvi</b>
    <p style="font-size:12px; margin-top:4px;" data-ru="Игрок останавливается перед стеной map[][]==1." data-en="Hero stops in front of solid wall map[][]==1.">Qahramon 1 bo'lgan devor ichiga kirib ketmaydi.</p>
  </div>
  <div class="card" style="text-align:center;">
    <div style="font-family:'JetBrains Mono'; font-size:20px; font-weight:800; color:var(--accent);">2 Ball</div>
    <b data-ru="Сбор монет" data-en="Coin Collection">Xazina Yig'ish</b>
    <p style="font-size:12px; margin-top:4px;" data-ru="Монета 2 исчезает с карты (становится 0) при касании." data-en="Coin 2 clears to 0 upon hero touch (+score).">Tanga ustiga kelganda u 0 bo'ladi va ochko yoziladi.</p>
  </div>
</div>
""",
        "note": ["Baholash reglamenti", "Har bir talaba o'z ishini noutbukda o'qituvchiga ko'rsatadi.", "Kodi toza bo'lgan va devorlari buzilmagan o'quvchilarga to'liq 10 ball qo'yiladi."]
    },

    # 12. Xulosa
    {
        "phase": "XULOSA|ИТОГ|SUMMARY",
        "eyebrow": {"uz": "UY VAZIFASI · AMALIYOT", "ru": "ДОМАШНЕЕ ЗАДАНИЕ · ПРАКТИКА", "en": "HOMEWORK · PRACTICE"},
        "title": {"uz": "Xulosa va Mustaqil Geym-Dev Vazifasi", "ru": "Итог и Домашнее Задание", "en": "Summary & Homework Mission"},
        "lede": {"uz": "Bugun siz professional 2D o'yinlarning xaritasi qanday ishlashini o'rgandingiz! Keyingi darsda labirint ustiga 'Urush Tumani' (Fog of War) yopamiz.", "ru": "Вы освоили тайловые карты профессиональных игр! На следующем уроке наложим 'Туман Войны' (Fog of War).", "en": "You mastered pro 2D game tilemaps! Next lesson we overlay the atmospheric 'Fog of War'."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="Итог" data-en="Summary">Dars xulosasi</div>
    <h3 data-ru="Tilemap освоен" data-en="Tilemaps Mastered">Tilemap o'zlashtirildi</h3>
    <p data-ru="2D массивы экономят оперативную память и дают мгновенные коллизии со скоростью O(1)." data-en="2D arrays conserve RAM and provide instant collision detection at O(1) speed.">2D massivlar xotirani tejaydi va O(1) tezlikda to'qnashuvni hisoblashga imkon beradi.</p>
  </div>
  <div class="card" style="border-left:4px solid var(--accent);">
    <div class="badge-good" data-ru="Домашнее задание" data-en="Homework Mission">Mustaqil Topshiriq</div>
    <h3 data-ru="Портал 'vazifa.html'" data-en="Portal 'vazifa.html'">'vazifa.html' topshiriqlari</h3>
    <p data-ru="Выполните 4 инженерных задания в портале: формулы координат, обход границ и динамическая смена карты." data-en="Complete 4 engineering tasks in portal: coordinate formulas, boundary guards, dynamic map switching.">Portalda 4 ta kiber-topshiriqni yeching: koordinata matematikasi, chegaralar qalqoni va xarita o'zgarishi.</p>
  </div>
</div>
""",
        "note": ["Keyingi darsga anons", "Keyingi darsda 'Urush Tumani' effekti bo'ladi: qahramon atrofida mash'ala nuri yonadi, qolgan joylar qorong'i bo'ladi.", "Bu bolalarda ulkan qiziqish uyg'otadi!"]
    }
]

SLIDE_TIMES = [
    '00-03|00-03|00-03', '03-07|03-07|03-07', '07-11|07-11|07-11', '11-15|11-15|11-15',
    '15-18|15-18|15-18', '18-21|18-21|18-21', '21-24|21-24|21-24', '24-27|24-27|24-27',
    '27-31|27-31|27-31', '31-36|31-36|31-36', '36-38|36-38|36-38', '38-40|38-40|38-40'
]

slides_html = ""
notes_dict = {"uz": [], "ru": [], "en": []}

for idx, s in enumerate(SLIDES):
    s_time = SLIDE_TIMES[idx]
    slides_html += f"""
<section class="slide{' active' if idx==0 else ''}" data-phase="{s['phase']}" data-time="{s_time}" data-slide-index="{idx}">
  <div class="slide-header">
    <span class="slide-eyebrow" data-ru="{s['eyebrow']['ru']}" data-en="{s['eyebrow']['en']}">{s['eyebrow']['uz']}</span>
    <h2 data-ru="{s['title']['ru']}" data-en="{s['title']['en']}">{s['title']['uz']}</h2>
    <p class="lede" data-ru="{s['lede']['ru']}" data-en="{s['lede']['en']}">{s['lede']['uz']}</p>
  </div>
  <div class="slide-body">
    {s['body']}
  </div>
</section>
"""
    notes_dict["uz"].append([s["note"][0], s["note"][1], s["note"][2]])
    notes_dict["ru"].append([s["note"][0], s["note"][1], s["note"][2]])
    notes_dict["en"].append([s["note"][0], s["note"][1], s["note"][2]])

def get_floating_elements():
    return """
<a href="../../../../index.html" class="floating-brand" title="Bosh sahifa / Home" data-title-ru="Главная страница / Home" data-title-en="Home Page">
  <img src="{LOGO_DATA_URI}" alt="Target Logo" class="logo-img">
  <span class="tag">7-8 · VIBECODING</span>
</a>

<div class="floating-dock">
  <button class="dock-btn lang-btn" data-lang="uz" onclick="setLang('uz')" title="O'zbek tili" data-title-ru="Узбекский язык" data-title-en="Uzbek language">UZ</button>
  <button class="dock-btn lang-btn" data-lang="ru" onclick="setLang('ru')" title="Rus tili" data-title-ru="Русский язык" data-title-en="Russian language">RU</button>
  <button class="dock-btn lang-btn" data-lang="en" onclick="setLang('en')" title="Ingliz tili" data-title-ru="Английский язык" data-title-en="English language">EN</button>
  <button class="dock-btn" onclick="toggleTheme()" title="Mavzuni almashtirish" data-title-ru="Переключить тему" data-title-en="Toggle Theme">🌓</button>
  <button class="dock-btn" onclick="toggleNotes()" title="O'qituvchi izohlari (N)" data-title-ru="Заметки преподавателя (N)" data-title-en="Teacher Notes (N)">📝</button>
  <button class="dock-btn" onclick="toggleHelp()" title="Klavishlar yordami (?)" data-title-ru="Справка клавиш (?)" data-title-en="Keyboard Help (?)">⌨️</button>
</div>

<div class="floating-counter">
  <span class="curr" id="slide-curr">01</span> / <span id="slide-total">12</span>
</div>

<div class="floating-phase" id="slide-phase" data-phase="KIRISH|ВВЕДЕНИЕ|INTRO">
  KIRISH
</div>
"""

def get_modals():
    return """
<div class="notes-modal" id="notesModal" onclick="if(event.target===this)toggleNotes()">
  <div class="modal-box">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
      <h3 style="margin:0;" data-ru="Заметки преподавателя" data-en="Teacher Notes">O'qituvchi izohlari</h3>
      <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:var(--ink-2); cursor:pointer;" onclick="toggleNotes()">[ESC]</span>
    </div>
    <div class="notes-body" id="notesContent">...</div>
  </div>
</div>

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

def get_js():
    notes_json = json.dumps(notes_dict, ensure_ascii=False, indent=2)
    return f"""
<script>
var currentSlide = 0;
var currentLang = "uz";
var slides = document.querySelectorAll(".slide");
var totalSlides = slides.length;
var NOTES = {notes_json};

function updateSlideView() {{
  slides.forEach(function(s, idx) {{ s.classList.toggle("active", idx === currentSlide); }});
  var currStr = (currentSlide + 1 < 10 ? "0" : "") + (currentSlide + 1);
  var totalStr = (totalSlides < 10 ? "0" : "") + totalSlides;
  document.getElementById("slide-curr").textContent = currStr;
  document.getElementById("slide-total").textContent = totalStr;

  var act = slides[currentSlide];
  var phaseData = act.getAttribute("data-phase") || "DARS|УРОК|LESSON";
  var parts = phaseData.split("|");
  var pText = parts[0];
  if (currentLang === "ru" && parts[1]) pText = parts[1];
  if (currentLang === "en" && parts[2]) pText = parts[2];
  document.getElementById("slide-phase").textContent = pText;

  var notesArr = NOTES[currentLang] || NOTES["uz"] || [];
  var note = notesArr[currentSlide] || ["", "", ""];
  var sayLabel = currentLang === "ru" ? "Сказать" : (currentLang === "en" ? "Say" : "Aytish");
  var doLabel = currentLang === "ru" ? "Действие" : (currentLang === "en" ? "Action" : "Qilish");
  document.getElementById("notesContent").innerHTML = "<h4>" + note[0] + "</h4><p><b>" + sayLabel + ":</b> " + note[1] + "</p><p><b>" + doLabel + ":</b> " + note[2] + "</p>";
}}

function nextSlide() {{ if (currentSlide < totalSlides - 1) {{ currentSlide++; updateSlideView(); }} }}
function prevSlide() {{ if (currentSlide > 0) {{ currentSlide--; updateSlideView(); }} }}

function setLang(lang) {{
  currentLang = lang;
  try {{ localStorage.setItem("target_lang", lang); }} catch(e) {{}}
  document.documentElement.lang = lang;

  document.querySelectorAll(".dock-btn.lang-btn").forEach(function(b) {{
    b.classList.toggle("active", b.getAttribute("data-lang") === lang);
  }});

  document.querySelectorAll("[data-ru], [data-en]").forEach(function(el) {{
    if (!el.getAttribute("data-uz-orig")) el.setAttribute("data-uz-orig", el.innerHTML);
    if (lang === "uz") el.innerHTML = el.getAttribute("data-uz-orig");
    else if (lang === "ru" && el.getAttribute("data-ru")) el.innerHTML = el.getAttribute("data-ru");
    else if (lang === "en" && el.getAttribute("data-en")) el.innerHTML = el.getAttribute("data-en");
  }});

  updateSlideView();
}}

function toggleTheme() {{
  var cur = document.documentElement.getAttribute("data-theme") || "dark";
  var next = cur === "dark" ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", next);
  try {{ localStorage.setItem("target_theme", next); }} catch(e) {{}}
}}

function toggleNotes() {{ document.getElementById("notesModal").classList.toggle("active"); }}
function toggleHelp() {{ document.getElementById("helpModal").classList.toggle("active"); }}

function checkQuiz(el, isCorrect) {{
  var box = el.parentElement;
  box.querySelectorAll(".quiz-option").forEach(function(opt) {{ opt.classList.remove("correct", "wrong"); }});
  if (isCorrect) el.classList.add("correct");
  else el.classList.add("wrong");
}}

function toggleTestFix() {{
  var box = document.getElementById("testFixBox");
  if (box) box.style.display = (box.style.display === "block") ? "none" : "block";
}}

document.addEventListener("keydown", function(e) {{
  if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
  if (e.key === "ArrowRight" || e.key === " ") {{ e.preventDefault(); nextSlide(); }}
  else if (e.key === "ArrowLeft") {{ e.preventDefault(); prevSlide(); }}
  else if (e.key === "l" || e.key === "L") {{
    var order = ["uz", "ru", "en"];
    setLang(order[(order.indexOf(currentLang) + 1) % 3]);
  }} else if (e.key === "t" || e.key === "T") {{ toggleTheme(); }}
  else if (e.key === "n" || e.key === "N") {{ toggleNotes(); }}
  else if (e.key === "?" || e.key === "/") {{ toggleHelp(); }}
  else if (e.key === "Escape") {{
    document.querySelectorAll(".notes-modal.active").forEach(function(m){{ m.classList.remove("active"); }});
  }}
}});

// Touch / Swipe Navigation for Mobile & Tablets & Smartboards
var touchStartX = 0, touchStartY = 0, touchStartTime = 0;
document.addEventListener("touchstart", function(e) {{
  if (e.touches && e.touches.length === 1) {{
    touchStartX = e.touches[0].clientX;
    touchStartY = e.touches[0].clientY;
    touchStartTime = Date.now();
  }}
}}, {{ passive: true }});

document.addEventListener("touchend", function(e) {{
  if (e.changedTouches && e.changedTouches.length === 1) {{
    var dx = e.changedTouches[0].clientX - touchStartX;
    var dy = e.changedTouches[0].clientY - touchStartY;
    var dt = Date.now() - touchStartTime;
    if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy) * 1.3 && dt < 800) {{
      var target = e.target;
      if (target.closest("input, textarea, select, button, .quiz-box, .code-snippet, .notes-modal")) return;
      if (dx < 0) {{
        nextSlide();
      }} else {{
        prevSlide();
      }}
    }}
  }}
}}, {{ passive: true }});

window.addEventListener("DOMContentLoaded", function() {{
  var savedTheme = "dark";
  try {{ savedTheme = localStorage.getItem("target_theme") || "dark"; }} catch(e) {{}}
  document.documentElement.setAttribute("data-theme", savedTheme);

  var savedLang = "uz";
  try {{ savedLang = localStorage.getItem("target_lang") || "uz"; }} catch(e) {{}}
  setLang(savedLang);
}});
</script>
"""

full_pres = f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Урок 29: Матрицы и Карты (Tilemaps) — 2D Лабиринт" data-en="Lesson 29: Matrices & Tilemaps — 2D Labyrinth">29-dars: Matritsalar va Xaritalar (Tilemaps) — 2D Labirint va Platformalar</title>
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
  {css_chunk}
</head>
<body>

{get_floating_elements()}

<div class="stage">
{slides_html}
</div>

{get_modals()}
{get_js()}

</body>
</html>
"""

with open(os.path.join(FOLDER, "prezentatsiya.html"), "w", encoding="utf-8") as f:
    f.write(full_pres)

print("✅ Prezentatsiya generated for 7-8-sinf 29-dars")

# -------------------------------------------------------------
# 2. VARAQA (2-page printable A4 worksheet)
# -------------------------------------------------------------
with open("classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/varaqa.html", "r", encoding="utf-8") as f:
    t_var = f.read()

varaqa_css = t_var[t_var.find("<style>"):t_var.find("</style>") + 8]

full_varaqa = f"""<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="Урок 29: Матрицы и Tilemaps — Рабочий лист" data-en="Lesson 29: Matrices & Tilemaps — Worksheet">29-dars: Matritsalar va Xaritalar (Tilemaps) — Amaliy Ish Varaqasi</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
{varaqa_css}
</head>
<body>

<div class="noprint">
  <div class="noprint-left">
    <a href="/index.html" style="color:var(--ink); text-decoration:none; font-weight:700;">← PORTAL</a>
    <span>|</span>
    <span data-ru="7–8 Класс · Урок 29" data-en="Grade 7–8 · Lesson 29">7–8-sinf · 29-dars</span>
  </div>
  <div class="noprint-right">
    <button class="lg active" onclick="setLang('uz')">UZ</button>
    <button class="lg" onclick="setLang('ru')">RU</button>
    <button class="lg" onclick="setLang('en')">EN</button>
    <button id="printBtn" onclick="window.print()" data-ru="Распечатать (A4)" data-en="Print (A4)">🖨️ Chop etish (A4)</button>
  </div>
</div>

<!-- PAGE 1 -->
<div class="sheet">
  <div>
    <div class="brandrule"></div>
    <header>
      <div>
        <h1 data-ru="Tilemaps: Матрицы и 2D Лабиринт" data-en="Tilemaps: Matrices and 2D Maze">Matritsalar va Xaritalar (Tilemaps): 2D Labirint</h1>
        <div class="header-meta" data-ru="2-я четверть · 10-я неделя · 29-й урок · 7–8 класс" data-en="Quarter 2 · Week 10 · Lesson 29 · Grade 7–8">2-Chorak · 10-hafta · 29-dars · 7–8-sinf Game Dev Track</div>
      </div>
      <div class="header-fields">
        <div class="field-line">
          <span data-ru="Ученик:" data-en="Student:">O'quvchi:</span>
          <div class="line" style="min-width:140px;"></div>
        </div>
        <div class="field-line">
          <span data-ru="Класс:" data-en="Class:">Sinf:</span>
          <div class="line" style="min-width:60px;"></div>
        </div>
        <div class="field-line">
          <span data-ru="Дата:" data-en="Date:">Sana:</span>
          <div class="line" style="min-width:80px;"></div>
        </div>
        <div class="field-line">
          <span data-ru="Балл:" data-en="Score:">Ball:</span>
          <div class="line" style="min-width:50px;"></div>
        </div>
      </div>
    </header>

    <div class="mission-box">
      <h3 data-ru="Кибер-Миссия Урока" data-en="Lesson Cyber Mission">Kiber-Missiya</h3>
      <p data-ru="Построить систему тайловых карт (Tilemaps) на JavaScript и Canvas 2D. Освоить двумерные массивы, формулу преобразования экранных пикселей в индексы сетки и реализовать проверку коллизий за время O(1)." data-en="Engineer a Canvas 2D tilemap system in JavaScript. Master 2D arrays, screen-to-grid index projection formulas, and execute instant O(1) collision lookups.">JavaScript va Canvas 2D da Tilemap tizimini qurish. 2D massivlar orqali xaritani saqlash, piksellarni panjara indeksiga aylantirish va $O(1)$ tezlikdagi devor to'qnashuvini dasturlash.</p>
    </div>

    <div class="sec-title">
      <span class="num">01</span>
      <span data-ru="Тайловый словарь: Сопоставьте числовой индекс и тип ячейки" data-en="Tile Dictionary: Match Numerical Index to Tile Type">Tayllar lug'ati: Sonli indeks va katak turini juftlang</span>
    </div>
    <div class="box-grid">
      <div class="box">
        <h4 data-ru="Числовые Индексы Массива" data-en="Array Numeric Indices">Massivdagi Sonlar</h4>
        <p><b>0</b> — <span data-ru="Пустой проходимый пол" data-en="Empty walkable floor">Bo'sh yo'l (Floor)</span></p>
        <p><b>1</b> — <span data-ru="Непроходимая каменная стена" data-en="Solid brick wall">Tosh devor (Wall)</span></p>
        <p><b>2</b> — <span data-ru="Золотая монетка (+50 очков)" data-en="Gold coin (+50 pts)">Oltin tanga (Coin)</span></p>
        <p><b>3</b> — <span data-ru="Портал перехода на уровень 2" data-en="Next level portal">Chiqish portali (Exit)</span></p>
      </div>
      <div class="box">
        <h4 data-ru="Действие Физического Движка" data-en="Physics Engine Behavior">Fizik Dvigatel Harakati</h4>
        <p data-ru="[ &nbsp; ] Герой свободно бегает, препятствий нет" data-en="[ &nbsp; ] Hero moves freely, no barrier">[ &nbsp; ] Qahramon erkin yuguradi, to'siq yo'q</p>
        <p data-ru="[ &nbsp; ] Harakat to'xtatiladi: canMove = false" data-en="[ &nbsp; ] Motion blocked: canMove = false">[ &nbsp; ] Harakat to'xtatiladi: canMove = false</p>
        <p data-ru="[ &nbsp; ] Katak 0 bo'ladi, hisobga +50 qo'shiladi" data-en="[ &nbsp; ] Cell clears to 0, score increases">[ &nbsp; ] Katak 0 bo'ladi, hisobga +50 qo'shiladi</p>
        <p data-ru="[ &nbsp; ] G'alaba ekrani: 'Next Level!'" data-en="[ &nbsp; ] Victory trigger: 'Next Level!'">[ &nbsp; ] G'alaba ekrani: 'Next Level!'</p>
      </div>
    </div>

    <div class="sec-title">
      <span class="num">02</span>
      <span data-ru="Математика Координат: Преобразование пикселей в сетку" data-en="Coordinate Math: Pixels to Grid Index Conversion">Koordinata Matematikasi: Piksellarni panjaraga o'tkazish</span>
    </div>
    <div class="code-snippet">
      const TILE_SIZE = 32;<br>
      // O'yinchi pozitsiyasi: x = 165px, y = 98px<br>
      const col = Math.floor(player.x / TILE_SIZE); // col = Math.floor(165 / 32)<br>
      const row = Math.floor(player.y / TILE_SIZE); // row = Math.floor(98 / 32)
    </div>
    <p style="font-size:8.4pt; color:var(--ink-2); margin:4px 0;" data-ru="Вопрос: Вычислите значения col и row для x=165, y=98. В какой ячейке матрицы map[row][col] находится игрок?" data-en="Question: Calculate col and row values for x=165, y=98. Which cell map[row][col] holds the player?">Savol: x=165 va y=98 uchun col va row qiymatlarini hisoblang. O'yinchi map[row][col] ning aynan qaysi katagida?</p>
    <div class="write-line"></div>
    <div class="write-line"></div>
  </div>

  <div class="sheet-footer">
    <span>TARGET INTERNATIONAL SCHOOL · VIBECODING 7–8</span>
    <span data-ru="Страница 1 из 2" data-en="Page 1 of 2">1-bet / 2</span>
  </div>
</div>

<!-- PAGE 2 -->
<div class="sheet">
  <div>
    <div class="brandrule"></div>
    <header>
      <div>
        <h1 data-ru="Практическая Лаборатория и Рубрика" data-en="Practical Lab & Rubric">Amaliy Dvigatel va Baholash</h1>
        <div class="header-meta" data-ru="Алгоритмы проверки коллизий и сбор наград" data-en="Collision verification algorithms and reward collection">To'qnashuv algoritmlari va mukofotlarni yig'ish</div>
      </div>
      <div class="header-fields">
        <div class="field-line">
          <span data-ru="Подпись учителя:" data-en="Teacher Signature:">O'qituvchi imzosi:</span>
          <div class="line" style="min-width:120px;"></div>
        </div>
      </div>
    </header>

    <div class="sec-title">
      <span class="num">03</span>
      <span data-ru="4 Инженерных Задания на Компьютере" data-en="4 Hands-on Engineering Tasks">Kompyuterda 4 ta Muhandislik Topshirig'i</span>
    </div>

    <div class="box" style="margin-bottom:6px;">
      <h4 data-ru="1-Topshiriq: 2D Massiv E'lon Qilish (3 Ball)" data-en="Task 1: Declare 2D Array (3 Points)">1-Topshiriq: 2D Massiv E'lon Qilish (3 Ball)</h4>
      <p data-ru="5x5 o'lchamli tosh devorlar bilan o'ralgan kichik labirint massivini JavaScript sintaksisida yozing:" data-en="Write a 5x5 dungeon array surrounded by solid stone walls in JS syntax:">5x5 o'lchamli tosh devorlar bilan o'ralgan kichik labirint massivini JavaScript sintaksisida yozing:</p>
      <div class="write-line"></div>
    </div>

    <div class="box" style="margin-bottom:6px;">
      <h4 data-ru="2-Topshiriq: Вложенные Циклы Отрисовки (3 Ball)" data-en="Task 2: Nested Render Loops (3 Points)">2-Topshiriq: Ichma-ich Sikl bilan Chizish (3 Ball)</h4>
      <p data-ru="Canvas-da har bir katakni to'g'ri koordinatada (col*32, row*32) chizish uchun qaysi ikkita for sikli kerak?" data-en="Which two nested for loops are required to paint each tile at (col*32, row*32)?">Canvas-da har bir katakni to'g'ri koordinatada (col*32, row*32) chizish uchun qaysi ikkita for sikli kerak?</p>
      <div class="write-line"></div>
    </div>

    <div class="box" style="margin-bottom:6px;">
      <h4 data-ru="3-Topshiriq: O(1) Скорость Проверки Стен (2 Ball)" data-en="Task 3: O(1) Wall Collision Check (2 Points)">3-Topshiriq: O(1) Tezlikdagi Devor Qalqoni (2 Ball)</h4>
      <p data-ru="Nega 1000 ta devor bo'lsa ham, map[row][col] tekshiruvi kompyuterni qotirmasdan bir zumda ishlaydi?" data-en="Why does map[row][col] check run instantly without lag even with 1000 obstacles?">Nega 1000 ta devor bo'lsa ham, map[row][col] tekshiruvi kompyuterni qotirmasdan bir zumda ishlaydi?</p>
      <div class="write-line"></div>
    </div>

    <div class="box" style="margin-bottom:8px;">
      <h4 data-ru="4-Topshiriq: Tanga Yeyilganda Massivni Yangilash (2 Ball)" data-en="Task 4: Clear Coin on Collection (2 Points)">4-Topshiriq: Tanga Yeyilganda Massivni Yangilash (2 Ball)</h4>
      <p data-ru="O'yinchi 2 soni turgan katakka kelganda, tanga o'chib ketishi uchun massiv qaysi kod bilan yangilanadi?" data-en="When the hero steps into cell with value 2, how is the array updated to erase it?">O'yinchi 2 soni turgan katakka kelganda, tanga o'chib ketishi uchun massiv qaysi kod bilan yangilanadi?</p>
      <div class="write-line"></div>
    </div>

    <div class="sec-title">
      <span class="num">04</span>
      <span data-ru="10-Балльная Шкала Оценки" data-en="10-Point Evaluation Rubric">10 Ballik Rasmiy Baholash Mezoni</span>
    </div>
    <div class="rubric-grid">
      <div class="rubric-card">
        <b>3 Ball</b>
        <span data-ru="2D Массив: Корректная матрица" data-en="2D Array: Valid matrix syntax">2D Massiv: To'g'ri e'lon qilingan</span>
      </div>
      <div class="rubric-card">
        <b>3 Ball</b>
        <span data-ru="Рендер: Вложенные циклы Canvas" data-en="Render: Nested Canvas loops">Render: Ichma-ich sikl ishlaydi</span>
      </div>
      <div class="rubric-card">
        <b>2 Ball</b>
        <span data-ru="Коллизии: Защита от стен O(1)" data-en="Collisions: O(1) wall guard">To'qnashuv: Devor ichiga kirmaydi</span>
      </div>
      <div class="rubric-card">
        <b>2 Ball</b>
        <span data-ru="Интерактив: Сбор монеты (tile=0)" data-en="Interactive: Coin pickup (tile=0)">Oltin tanga: Yig'ilganda o'chadi</span>
      </div>
    </div>
  </div>

  <div class="sheet-footer">
    <span>TARGET INTERNATIONAL SCHOOL · VIBECODING 7–8</span>
    <span data-ru="Страница 2 из 2" data-en="Page 2 of 2">2-bet / 2</span>
  </div>
</div>

<script>
function setLang(lang) {{
  document.querySelectorAll(".noprint button.lg").forEach(function(b) {{
    b.classList.toggle("active", b.textContent.toLowerCase() === lang);
  }});
  document.querySelectorAll("[data-ru], [data-en]").forEach(function(el) {{
    if (!el.getAttribute("data-uz-orig")) el.setAttribute("data-uz-orig", el.innerHTML);
    if (lang === "uz") el.innerHTML = el.getAttribute("data-uz-orig");
    else if (lang === "ru" && el.getAttribute("data-ru")) el.innerHTML = el.getAttribute("data-ru");
    else if (lang === "en" && el.getAttribute("data-en")) el.innerHTML = el.getAttribute("data-en");
  }});
}}
</script>
</body>
</html>
"""

with open(os.path.join(FOLDER, "varaqa.html"), "w", encoding="utf-8") as f:
    f.write(full_varaqa)

print("✅ Varaqa generated for 7-8-sinf 29-dars")

# -------------------------------------------------------------
# 3. VAZIFA (Interactive standalone homework app)
# -------------------------------------------------------------
with open("classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/vazifa.html", "r", encoding="utf-8") as f:
    t_vaz = f.read()

vazifa_css = t_vaz[t_vaz.find("<style>"):t_vaz.find("</style>") + 8]

full_vazifa = f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="Tilemaps и 2D Лабиринт — Домашнее Задание" data-en="Tilemaps & 2D Maze — Homework">Tilemaps va 2D Labirint: Massivlar — Mustaqil Uy Vazifasi</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap">
{vazifa_css}
</head>
<body>

<header class="top-nav">
  <div class="nav-brand">
    <a href="../../../../index.html" class="logo-link" title="Bosh sahifa / Home" data-title-ru="Главная страница / Home" data-title-en="Home Page">
      <img src="{LOGO_DATA_URI}" alt="Target Logo" class="brand-logo">
    </a>
    <span class="cohort-badge">7-8 · UY VAZIFASI</span>
  </div>
  <div class="nav-controls">
    <button class="nav-btn lang-btn" data-lang="uz" onclick="setLang('uz')">UZ</button>
    <button class="nav-btn lang-btn" data-lang="ru" onclick="setLang('ru')">RU</button>
    <button class="nav-btn lang-btn" data-lang="en" onclick="setLang('en')">EN</button>
    <button class="nav-btn" onclick="toggleTheme()" title="Mavzuni almashtirish" data-title-ru="Сменить тему" data-title-en="Toggle Theme">🌓</button>
    <button class="nav-btn primary" onclick="window.print()" data-ru="🖨️ Распечатать (A4)" data-en="🖨️ Print (A4)">🖨️ Chop etish (A4)</button>
  </div>
</header>

<main class="page-container">
  <section class="assignment-hero">
    <div class="hero-eyebrow" data-ru="7–8 КЛАСС · 10-Я НЕДЕЛЯ · УРОК 29" data-en="GRADE 7–8 · WEEK 10 · LESSON 29">7–8-SINF · 10-HAFTA · 29-DARS</div>
    <h1 class="hero-title" data-ru="Matritsalar va Xaritalar (Tilemaps) — Mustaqil Amaliy Vazifa" data-en="Tilemaps & 2D Mazes — Homework Assignment">Matritsalar va Xaritalar (Tilemaps) — Mustaqil Amaliy Vazifa</h1>
    <p class="hero-subtitle" data-ru="2D массивы, вложенные циклы рендеринга, расчет индексов сетки и физика коллизий O(1)." data-en="2D arrays, nested render loops, grid index calculation, and O(1) collision physics.">2D massivlar, ichma-ich render sikllari, panjara indeksi formulasi va $O(1)$ to'qnashuv fizikasi.</p>
  </section>

  <section class="student-card">
    <div class="card-grid">
      <div class="field-group">
        <label data-ru="Имя и Фамилия ученика" data-en="Student Full Name">O'quvchi F.I.Sh.</label>
        <input type="text" id="studentName" placeholder="Ism va familiyangizni yozing..." data-placeholder-ru="Введите имя и фамилию..." data-placeholder-en="Enter full name..." oninput="saveStudentData()">
      </div>
      <div class="field-group">
        <label data-ru="Класс" data-en="Class">Sinf</label>
        <select id="studentClass" onchange="saveStudentData()">
          <option value="7A">7A</option>
          <option value="7B">7B</option>
          <option value="8A">8A</option>
          <option value="8B">8B</option>
        </select>
      </div>
      <div class="field-group">
        <label data-ru="Дата сдачи" data-en="Submission Date">Topshirish sanasi</label>
        <input type="date" id="studentDate" oninput="saveStudentData()">
      </div>
    </div>
  </section>

  <!-- TASK 1 -->
  <article class="task-card">
    <div class="task-header">
      <div>
        <span class="task-num">Topshiriq 1</span>
        <h2 class="task-title" data-ru="1. Расчет Ячейки Игрока по Координатам Пикселей" data-en="1. Calculating Player Cell from Pixel Coordinates">1. Piksellarni Matritsa Indeksiga Aylantirish</h2>
      </div>
      <div class="task-score">2.5 Ball</div>
    </div>
    <p class="task-desc" data-ru="В игре с тайлами 32x32 пикселя координаты персонажа: player.x = 210, player.y = 145. Напишите формулы и вычислите точные значения row и col ячейки матрицы map[row][col]." data-en="In a 32x32 tile game, character position is: player.x = 210, player.y = 145. Write the formula and compute exact row and col indices for map[row][col].">Tayl o'lchami 32 piksel bo'lgan o'yinda qahramon koordinatasi: player.x = 210, player.y = 145. Formulani yozing va qahramon turgan aniq row va col indekslarini hisoblab bering.</p>
    <textarea class="task-textarea" id="task1_ans" placeholder="Formulani va hisob-kitobni yozing..." data-placeholder-ru="Напишите формулу и расчет..." data-placeholder-en="Write formula and calculations..." oninput="autoSave()"></textarea>
    <div style="margin-top:10px;">
      <button class="nav-btn" onclick="toggleFix('fix1')" data-ru="💡 Показать решение (Fix)" data-en="💡 Reveal Solution (Fix)">💡 Yechimni ko'rish (Fix)</button>
      <div id="fix1" class="fix-box" style="display:none; margin-top:8px; padding:10px; background:var(--panel-2); border-left:3px solid var(--ok); border-radius:4px;">
        <b style="color:var(--ok);" data-ru="Эталонное решение:" data-en="Reference Solution:">Etalon Yechim:</b>
        <p style="margin:4px 0 0;" data-ru="Формулы: col = Math.floor(player.x / TILE_SIZE); row = Math.floor(player.y / TILE_SIZE);<br>Расчет: col = Math.floor(210 / 32) = Math.floor(6.5625) = 6;<br>row = Math.floor(145 / 32) = Math.floor(4.5312) = 4.<br>Игрок находится в ячейке map[4][6]!" data-en="Formulas: col = Math.floor(player.x / 32); row = Math.floor(player.y / 32);<br>col = Math.floor(210 / 32) = 6;<br>row = Math.floor(145 / 32) = 4.<br>Player is at map[4][6]!">Formulalar: col = Math.floor(player.x / 32); row = Math.floor(player.y / 32);<br>Hisob: col = Math.floor(210 / 32) = 6;<br>row = Math.floor(145 / 32) = 4.<br>Qahramon map[4][6] katagida joylashgan!</p>
      </div>
    </div>
  </article>

  <!-- TASK 2 -->
  <article class="task-card">
    <div class="task-header">
      <div>
        <span class="task-num">Topshiriq 2</span>
        <h2 class="task-title" data-ru="2. Скорость Проверки Коллизий: O(1) против O(N)" data-en="2. Collision Speed: O(1) vs O(N)">2. To'qnashuv Tezligi: O(1) va O(N) ning Asosiy Farqi</h2>
      </div>
      <div class="task-score">2.5 Ball</div>
    </div>
    <p class="task-desc" data-ru="Почему проверка прямоугольников (AABB) по 2000 препятствиям тормозит игру, а проверка по сетке map[row][col] выполняется мгновенно за O(1)? Объясните технический принцип." data-en="Why does AABB collision checking across 2000 obstacles cause lag, while grid lookup map[row][col] executes instantly in O(1)? Explain the technical mechanism.">Nima uchun 2000 ta to'siqni AABB to'rtburchaklar bilan tekshirish o'yinni qotirib qo'yadi, lekin Tilemap panjarasida map[row][col] tekshiruvi O(1) vaqtda bir zumda bajariladi?</p>
    <textarea class="task-textarea" id="task2_ans" placeholder="Texnik sababini tushuntiring..." data-placeholder-ru="Объясните техническую причину..." data-placeholder-en="Explain the technical reason..." oninput="autoSave()"></textarea>
    <div style="margin-top:10px;">
      <button class="nav-btn" onclick="toggleFix('fix2')" data-ru="💡 Показать решение (Fix)" data-en="💡 Reveal Solution (Fix)">💡 Yechimni ko'rish (Fix)</button>
      <div id="fix2" class="fix-box" style="display:none; margin-top:8px; padding:10px; background:var(--panel-2); border-left:3px solid var(--ok); border-radius:4px;">
        <b style="color:var(--ok);" data-ru="Эталонное решение:" data-en="Reference Solution:">Etalon Yechim:</b>
        <p style="margin:4px 0 0;" data-ru="В AABB нужно в каждом кадре (60 раз в секунду!) в цикле перебирать все 2000 препятствий. В Tilemap мы не перебираем препятствия: по координатам игрока мы мгновенно вычисляем индекс одной конкретной ячейки и читаем ее за 1 операцию по прямому адресу памяти." data-en="In AABB, the engine loops through all 2000 obstacles every frame (60 FPS). In a Tilemap, no iteration is needed: hero coordinates directly compute the memory offset of the exact target cell in a single step O(1).">AABB usulida dvigatel har bir kadrda (sekundiga 60 marta) 2000 ta devorni for siklida tekshirishi kerak. Tilemapda esa sikl umuman aylanmaydi: o'yinchining kelgusi qadami formuladan to'g'ridan-to'g'ri massiv manziliga (O(1)) boradi va bitta operatsiyada yechiladi.</p>
      </div>
    </div>
  </article>

  <!-- TASK 3 -->
  <article class="task-card">
    <div class="task-header">
      <div>
        <span class="task-num">Topshiriq 3</span>
        <h2 class="task-title" data-ru="3. Предотвращение Краша: Проверка Границ Сетки (Guard Clause)" data-en="3. Preventing Crashes: Boundary Guard Clause">3. Xatolikdan Qalqon: Massiv Chegaralarini Tekshirish</h2>
      </div>
      <div class="task-score">2.5 Ball</div>
    </div>
    <p class="task-desc" data-ru="Напишите функцию canMove(map, row, col), которая возвращает false, если игрок пытается шагнуть за пределы карты (меньше нуля или больше длины массива), и true, только если клетка свободна (tile !== 1)." data-en="Write canMove(map, row, col) that returns false if player tries to step out of bounds, and true only when target cell is walkable (tile !== 1).">O'yinchi xaritadan tashqariga chiqib ketganda 'Cannot read properties of undefined' xatoligi chiqmasligi uchun to'liq xavfsiz canMove(map, row, col) funksiyasi kodini yozing.</p>
    <textarea class="task-textarea" id="task3_ans" placeholder="JavaScript funksiyasini yozing..." data-placeholder-ru="Напишите функцию JavaScript..." data-placeholder-en="Write the JavaScript function..." oninput="autoSave()"></textarea>
    <div style="margin-top:10px;">
      <button class="nav-btn" onclick="toggleFix('fix3')" data-ru="💡 Показать решение (Fix)" data-en="💡 Reveal Solution (Fix)">💡 Yechimni ko'rish (Fix)</button>
      <div id="fix3" class="fix-box" style="display:none; margin-top:8px; padding:10px; background:var(--panel-2); border-left:3px solid var(--ok); border-radius:4px;">
        <b style="color:var(--ok);" data-ru="Эталонное решение:" data-en="Reference Solution:">Etalon Yechim:</b>
        <p style="margin:4px 0 0;" data-ru="function canMove(map, row, col) {{<br>&nbsp;&nbsp;if (row &lt; 0 || row &gt;= map.length) return false;<br>&nbsp;&nbsp;if (col &lt; 0 || col &gt;= map[0].length) return false;<br>&nbsp;&nbsp;return map[row][col] !== 1;<br>}}" data-en="function canMove(map, row, col) {{<br>&nbsp;&nbsp;if (row &lt; 0 || row &gt;= map.length) return false;<br>&nbsp;&nbsp;if (col &lt; 0 || col &gt;= map[0].length) return false;<br>&nbsp;&nbsp;return map[row][col] !== 1;<br>}}">function canMove(map, row, col) {{<br>&nbsp;&nbsp;if (row &lt; 0 || row &gt;= map.length) return false;<br>&nbsp;&nbsp;if (col &lt; 0 || col &gt;= map[0].length) return false;<br>&nbsp;&nbsp;return map[row][col] !== 1;<br>}}</p>
      </div>
    </div>
  </article>

  <!-- TASK 4 -->
  <article class="task-card">
    <div class="task-header">
      <div>
        <span class="task-num">Topshiriq 4</span>
        <h2 class="task-title" data-ru="4. Динамическое Разрушение Стен (Механика Terraria / Bomberman)" data-en="4. Dynamic Wall Destruction (Terraria / Bomberman Mechanics)">4. Dinamik Devorni Buzish: Massivni Jonli O'zgartirish</h2>
      </div>
      <div class="task-score">2.5 Ball</div>
    </div>
    <p class="task-desc" data-ru="Как в коде реализовать разрушение стены? Например, персонаж ударил ки Kirka или бросил бомбу в клетку [row][col]. Какая строка кода превратит стену в проходимую тропу и перерисует экран?" data-en="How is dynamic wall destruction coded? For instance, the hero strikes a wall with a pickaxe at [row][col]. What code statement converts the wall into a path and re-renders?">O'yinda devor buzilganda (masalan, bomba portlaganda yoki o'yinchi toshni qaziganda) ushbu devor bo'sh yo'lga aylanishi uchun massiv qaysi kod bilan yangilanadi va ekranda qanday aks etadi?</p>
    <textarea class="task-textarea" id="task4_ans" placeholder="Kod va mantiqni yozing..." data-placeholder-ru="Напишите код и логику..." data-placeholder-en="Write code and logic..." oninput="autoSave()"></textarea>
    <div style="margin-top:10px;">
      <button class="nav-btn" onclick="toggleFix('fix4')" data-ru="💡 Показать решение (Fix)" data-en="💡 Reveal Solution (Fix)">💡 Yechimni ko'rish (Fix)</button>
      <div id="fix4" class="fix-box" style="display:none; margin-top:8px; padding:10px; background:var(--panel-2); border-left:3px solid var(--ok); border-radius:4px;">
        <b style="color:var(--ok);" data-ru="Эталонное решение:" data-en="Reference Solution:">Etalon Yechim:</b>
        <p style="margin:4px 0 0;" data-ru="Достаточно выполнить: map[row][col] = 0; В следующем кадре функция drawMap() прочитает ноль и нарисует пол вместо кирпича. Персонаж сразу сможет пройти через бывшую стену!" data-en="Simply execute: map[row][col] = 0; In the next animation frame, drawMap() sees 0 and renders empty floor. The hero can walk right through!">Shunchaki: map[row][col] = 0; buyrug'ini berish kifoya. Keyingi kadrda drawMap() funksiyasi ushbu katakda 0 ni ko'radi va devor o'rniga qora pol chizadi. Qahramon esa to'siqsiz o'tib ketadi!</p>
      </div>
    </div>
  </article>

  <!-- RUBRIC -->
  <section class="rubric-section" style="margin-top:20px; background:var(--panel); border:1px solid var(--rule); border-radius:12px; padding:18px;">
    <h3 style="margin:0 0 12px; font-family:'Manrope',sans-serif;" data-ru="Критерии Оценки за Домашнюю Работу (10 Баллов)" data-en="Homework Evaluation Rubric (10 Points)">Uy Vazifasi Baholash Mezonlari (10 Ball)</h3>
    <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px;">
      <div class="card" style="padding:10px; text-align:center; background:var(--panel-2); border-radius:8px;">
        <b style="color:var(--accent);">2.5 Ball</b>
        <p style="font-size:12px; margin:4px 0 0;" data-ru="1-Задание: Точный расчет row и col" data-en="Task 1: Precise row and col calculation">1-Topshiriq: row va col aniq hisoblangan</p>
      </div>
      <div class="card" style="padding:10px; text-align:center; background:var(--panel-2); border-radius:8px;">
        <b style="color:var(--accent);">2.5 Ball</b>
        <p style="font-size:12px; margin:4px 0 0;" data-ru="2-Задание: Анализ сложности O(1) vs O(N)" data-en="Task 2: Complexity analysis O(1) vs O(N)">2-Topshiriq: O(1) va O(N) tezligi asoslangan</p>
      </div>
      <div class="card" style="padding:10px; text-align:center; background:var(--panel-2); border-radius:8px;">
        <b style="color:var(--accent);">2.5 Ball</b>
        <p style="font-size:12px; margin:4px 0 0;" data-ru="3-Задание: Защита от выхода за границы" data-en="Task 3: Boundary Guard Clause">3-Topshiriq: Chegaralar tekshiruvi yozilgan</p>
      </div>
      <div class="card" style="padding:10px; text-align:center; background:var(--panel-2); border-radius:8px;">
        <b style="color:var(--accent);">2.5 Ball</b>
        <p style="font-size:12px; margin:4px 0 0;" data-ru="4-Задание: Мутация map[row][col]=0" data-en="Task 4: Dynamic array mutation">4-Topshiriq: Dinamik xarita yangilanishi ko'rsatilgan</p>
      </div>
    </div>
  </section>
</main>

<script>
function autoSave() {{
  ['task1_ans', 'task2_ans', 'task3_ans', 'task4_ans'].forEach(function(id) {{
    var val = document.getElementById(id).value;
    localStorage.setItem("vc_hw_29_78_" + id, val);
  }});
}}

function saveStudentData() {{
  localStorage.setItem("vc_student_name_78", document.getElementById("studentName").value);
  localStorage.setItem("vc_student_class_78", document.getElementById("studentClass").value);
  localStorage.setItem("vc_student_date_78", document.getElementById("studentDate").value);
}}

function loadStudentData() {{
  if (localStorage.getItem("vc_student_name_78")) document.getElementById("studentName").value = localStorage.getItem("vc_student_name_78");
  if (localStorage.getItem("vc_student_class_78")) document.getElementById("studentClass").value = localStorage.getItem("vc_student_class_78");
  if (localStorage.getItem("vc_student_date_78")) document.getElementById("studentDate").value = localStorage.getItem("vc_student_date_78");
  ['task1_ans', 'task2_ans', 'task3_ans', 'task4_ans'].forEach(function(id) {{
    var saved = localStorage.getItem("vc_hw_29_78_" + id);
    if (saved) document.getElementById(id).value = saved;
  }});
}}

function toggleFix(id) {{
  var el = document.getElementById(id);
  el.style.display = (el.style.display === "block") ? "none" : "block";
}}

function setLang(lang) {{
  document.querySelectorAll(".lang-btn").forEach(function(b) {{
    b.classList.toggle("active", b.getAttribute("data-lang") === lang);
  }});
  document.querySelectorAll("[data-ru], [data-en]").forEach(function(el) {{
    if (!el.getAttribute("data-uz-orig")) el.setAttribute("data-uz-orig", el.innerHTML);
    if (lang === "uz") el.innerHTML = el.getAttribute("data-uz-orig");
    else if (lang === "ru" && el.getAttribute("data-ru")) el.innerHTML = el.getAttribute("data-ru");
    else if (lang === "en" && el.getAttribute("data-en")) el.innerHTML = el.getAttribute("data-en");
  }});
}}

function toggleTheme() {{
  var cur = document.documentElement.getAttribute("data-theme") || "dark";
  var next = cur === "dark" ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", next);
}}

window.addEventListener("DOMContentLoaded", function() {{
  loadStudentData();
}});
</script>
</body>
</html>
"""

with open(os.path.join(FOLDER, "vazifa.html"), "w", encoding="utf-8") as f:
    f.write(full_vazifa)

print("✅ Vazifa generated for 7-8-sinf 29-dars")

# -------------------------------------------------------------
# 4. TEACHER_READING.md (Teacher's Guide)
# -------------------------------------------------------------
teacher_guide = """# 29-Dars: O'qituvchi Uchun Metodik Qo'llanma va Yechimlar Kaliti
**Target International School // 7–8-Sinf // 10-Hafta (2-Chorak 1-Darsi: 40 daqiqa)**
**Mavzu:** Matritsalar va Xaritalar (Tilemaps): 2D Labirint va Platformalar
**Kohorta:** `7-8-sinf` (Game Dev, Interactive Web & Physics Track)

---

## 1. Asosiy Pedagogik Maqsad
Bugungi dars bilan 7–8-sinflar **2-Chorak: Roguelike O'yin Dvigateli** katta amaliy modulini boshlaydilar:
1. **2D Massivlar:** Xarita geometriyasini raqamli matritsa ko'rinishida saqlash (0 = yo'l, 1 = devor, 2 = tanga, 3 = portal).
2. **Ichma-ich Sikllar:** `for(row)` va `for(col)` orqali butun xaritani Canvas-ga $O(N)$ tezlikda chizish.
3. **Piksellarni Indeksga Aylantirish:** `Math.floor(x / TILE_SIZE)` formulasi yordamida o'yinchi turgan katakni aniqlash.
4. **O(1) To'qnashuv Qalqoni:** Barcha devorlarni aylanib chiqmasdan, faqatgina borilayotgan bitta katakni `map[nextRow][nextCol] === 1` orqali tekshirish.

---

## 2. 40 Daqiqalik Dars Reglamenti

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 03:00** | Kirish & 2-Chorak Rejasi | 2-Chorakda to'liq Roguelike o'yini yaratilishini e'lon qilish. | Noutbuklarni ochish, dars mavzusini qayd etish. |
| **03:00 – 08:00** | Aqliy Hujum (Xotira va RAM) | Nega 400 MB rasm o'rniga 2 KB massiv ishlatilishini savol-javob qilish. | O'z fikrlarini bildirish, farqlarni aniqlash. |
| **08:00 – 18:00** | Nazariya va Arxitektura | 12 slaydli prezentatsiyani namoyish etish, ichma-ich sikl va O(1) to'qnashuvni tushuntirish. | Bloklar va formulalarni daftarga qayd qilish. |
| **18:00 – 23:00** | Jonli Kiber-Test (Quiz & Fix) | Slayd 9 dagi matematik formulani sinf bilan hisoblash. | Hisob-kitob qilish, to'g'ri variantni tanlash. |
| **23:00 – 36:00** | Amaliy Dvigatel Laboratoriyasi | O'quvchilar shaxsiy 10x10 massiv labirintini tuzadilar va WASD bilan o'yinchini yurgizadilar. | Kod yozish, labirintdan chiqish, tangalarni yig'ish. |
| **36:00 – 40:00** | Xulosa & Baholash | 10 ballik mezon asosida eng yaxshi labirintlarga baho qo'yish, `vazifa.html` ni berish. | Ishlarni ko'rsatish, vazifani saqlab olish. |

---

## 3. Viktorina va Topshiriqlar Yechimi (Teacher Fixes)

### Viktorina (Slayd 9):
* **Savol:** Qaysi formula o'yinchi piksellarini matritsa indekslariga aylantiradi?
* **To'g'ri javob:** **B) col = Math.floor(player.x / 32), row = Math.floor(player.y / 32)**
* **Izoh:** 75 / 32 = 2.34 -> yaxlitlasak 2 (col=2). 100 / 32 = 3.12 -> yaxlitlasak 3 (row=3).

### Uy Vazifasi Yechimlari:
1. **Piksellar hisobi:** x=210 uchun col=Math.floor(210/32)=6. y=145 uchun row=Math.floor(145/32)=4. Katak: `map[4][6]`.
2. **O(1) vs O(N):** AABB 2000 ta devorni for tsiklida aylanib chiqadi (og'ir). Tilemap to'g'ridan-to'g'ri katak manziliga murojaat qiladi (bitta amal).
3. **Chegaralar himoyasi:** `row < 0 || row >= map.length || col < 0 || col >= map[0].length` shartlari qo'yiladi.
4. **Devor buzilishi:** `map[row][col] = 0;` qilib yangilanadi va keyingi kadrda devor yo'qoladi.

---

## 4. Baholash Mezoni (10 Ball)
* **3 Ball:** 10x10 lik 2D massiv sintaksis xatosiz e'lon qilingan.
* **3 Ball:** Ichma-ich `for` sikllari orqali Canvas-da barcha tayllar to'g'ri chizilgan.
* **2 Ball:** Panjara to'qnashuvi (`map[nextRow][nextCol] !== 1`) qahramonni devorga urilishdan saqlaydi.
* **2 Ball:** Oltin tangalar yig'ilganda `map[row][col] = 0` bo'lib yangilanadi va ball qo'shiladi.
"""

with open(os.path.join(FOLDER, "TEACHER_READING.md"), "w", encoding="utf-8") as f:
    f.write(teacher_guide)

print("✅ TEACHER_READING.md generated for 7-8-sinf 29-dars")

# -------------------------------------------------------------
# 5. SIMULATOR (Interactive Canvas 2D Tilemap Dungeon Lab)
# -------------------------------------------------------------
simulator_html = """<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>2D Tilemap Labirint Studiyasi — Roguelike Engine</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&family=JetBrains+Mono:wght@500;700&display=swap">
<style>
:root {
  --bg: #061530; --panel: #0E2249; --panel-2: #16305A;
  --ink: #E9EFF8; --accent: #FF1100; --ok: #00D68F; --rule: #22406B;
}
body {
  margin: 0; padding: 20px; background: var(--bg); color: var(--ink);
  font-family: 'Manrope', sans-serif; display: flex; flex-direction: column; align-items: center;
}
.header { text-align: center; margin-bottom: 16px; }
.header h1 { margin: 0 0 6px; font-size: 22px; }
.header p { margin: 0; color: #8496B0; font-size: 14px; }
.lab-container {
  display: flex; gap: 20px; background: var(--panel); border: 1px solid var(--rule);
  border-radius: 16px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}
canvas {
  background: #031024; border: 2px solid var(--rule); border-radius: 8px; cursor: pointer;
}
.controls { width: 300px; display: flex; flex-direction: column; gap: 12px; }
.metric-box {
  background: var(--panel-2); border-radius: 8px; padding: 10px;
  font-family: 'JetBrains Mono', monospace; text-align: center;
}
.metric-val { font-size: 20px; font-weight: 700; color: var(--ok); }
.code-display {
  background: #031024; border-radius: 8px; padding: 12px; font-family: 'JetBrains Mono', monospace;
  font-size: 11px; color: #A2B4CE; border-left: 3px solid var(--accent); max-height: 180px; overflow-y: auto;
}
.btn-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
button {
  background: var(--panel-2); border: 1px solid var(--rule); color: var(--ink);
  padding: 8px 10px; border-radius: 6px; font-family: 'Manrope', sans-serif;
  font-size: 11px; font-weight: 700; cursor: pointer; transition: 0.2s;
}
button:hover { background: var(--accent); color: #fff; border-color: var(--accent); }
.arrows-dpad {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; width: 140px; margin: 0 auto;
}
</style>
</head>
<body>

<div class="header">
  <h1 data-ru="Движок 2D Лабиринта Tilemap" data-en="2D Tilemap Labyrinth Engine">2D Tilemap Labirint Dvigateli</h1>
  <p data-ru="Управляйте WASD или стрелками | Редактируйте карту кликом мыши!" data-en="Control with WASD or arrows | Edit map by clicking tiles!">WASD yoki strelkalar bilan yuring | Xaritani sichqoncha bilan tahrirlang (Katakka bosing)!</p>
</div>

<div class="lab-container">
  <canvas id="gameCanvas" width="384" height="384"></canvas>
  <div class="controls">
    <div class="metric-box">
      <div>OCHKO / BALL</div>
      <div class="metric-val" id="score">0 Ball</div>
    </div>
    <div class="metric-box">
      <div>O'YINCHI KOORDINATASI</div>
      <div class="metric-val" id="playerPos" style="color:#FFB703;">row: 1, col: 1</div>
    </div>
    <div class="code-display" id="matrixView"></div>
    <div class="btn-grid">
      <button onclick="resetGame()" data-ru="Начать заново" data-en="Restart">Qayta Boshlash</button>
      <button onclick="clearWalls()" data-ru="Удалить стены" data-en="Clear Walls">Devorlarni O'chirish</button>
    </div>
    <div style="text-align:center; font-size:11px; color:#8496B0;">Boshqaruv tugmalari:</div>
    <div class="arrows-dpad">
      <div></div><button onclick="tryMove(0, -1)">▲</button><div></div>
      <button onclick="tryMove(-1, 0)">◄</button><button onclick="resetGame()">●</button><button onclick="tryMove(1, 0)">►</button>
      <div></div><button onclick="tryMove(0, 1)">▼</button><div></div>
    </div>
  </div>
</div>

<script>
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const TILE_SIZE = 32;
const ROWS = 12;
const COLS = 12;

let score = 0;
let player = { col: 1, row: 1 };

let map = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1, 0, 2, 0, 0, 0, 2, 1],
  [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 2, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
  [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
  [1, 0, 0, 1, 0, 0, 2, 0, 0, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1],
  [1, 2, 1, 0, 1, 1, 0, 0, 0, 1, 3, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
];

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      const tile = map[r][c];
      const x = c * TILE_SIZE;
      const y = r * TILE_SIZE;

      if (tile === 1) {
        ctx.fillStyle = "#4A5568";
        ctx.fillRect(x, y, TILE_SIZE, TILE_SIZE);
        ctx.strokeStyle = "#2D3748";
        ctx.strokeRect(x, y, TILE_SIZE, TILE_SIZE);
      } else {
        ctx.fillStyle = "#1A202C";
        ctx.fillRect(x, y, TILE_SIZE, TILE_SIZE);
        ctx.strokeStyle = "#222D3D";
        ctx.strokeRect(x, y, TILE_SIZE, TILE_SIZE);

        if (tile === 2) {
          ctx.fillStyle = "#ECC94B";
          ctx.beginPath();
          ctx.arc(x + 16, y + 16, 7, 0, Math.PI * 2);
          ctx.fill();
        } else if (tile === 3) {
          ctx.fillStyle = "#9F7AEA";
          ctx.fillRect(x + 6, y + 6, 20, 20);
        }
      }
    }
  }

  // Draw Player
  ctx.fillStyle = "#FF1100";
  ctx.beginPath();
  ctx.arc(player.col * TILE_SIZE + 16, player.row * TILE_SIZE + 16, 11, 0, Math.PI * 2);
  ctx.fill();
  ctx.strokeStyle = "#FFF";
  ctx.lineWidth = 2;
  ctx.stroke();

  document.getElementById("score").textContent = score + " Ball";
  document.getElementById("playerPos").textContent = "row: " + player.row + ", col: " + player.col;

  // Update live matrix snippet
  let snippet = "const map = [<br>";
  for (let r = 0; r < ROWS; r++) {
    snippet += "&nbsp;&nbsp;[" + map[r].join(", ") + "],<br>";
  }
  snippet += "];";
  document.getElementById("matrixView").innerHTML = snippet;
}

function tryMove(dc, dr) {
  const newCol = player.col + dc;
  const newRow = player.row + dr;

  if (newRow >= 0 && newRow < ROWS && newCol >= 0 && newCol < COLS) {
    const tile = map[newRow][newCol];
    if (tile !== 1) {
      player.col = newCol;
      player.row = newRow;

      if (tile === 2) {
        score += 50;
        map[newRow][newCol] = 0; // Tanga yo'qoladi
      } else if (tile === 3) {
        alert("🎉 G'alaba! Labirintdan omon chiqdingiz! Ballingiz: " + score);
      }
      draw();
    }
  }
}

canvas.addEventListener("click", (e) => {
  const rect = canvas.getBoundingClientRect();
  const clickX = e.clientX - rect.left;
  const clickY = e.clientY - rect.top;
  const c = Math.floor(clickX / TILE_SIZE);
  const r = Math.floor(clickY / TILE_SIZE);

  if (r > 0 && r < ROWS - 1 && c > 0 && c < COLS - 1) {
    if (map[r][c] === 1) map[r][c] = 0;
    else if (map[r][c] === 0) map[r][c] = 1;
    draw();
  }
});

window.addEventListener("keydown", (e) => {
  if (e.key === "ArrowUp" || e.key === "w" || e.key === "W") { e.preventDefault(); tryMove(0, -1); }
  else if (e.key === "ArrowDown" || e.key === "s" || e.key === "S") { e.preventDefault(); tryMove(0, 1); }
  else if (e.key === "ArrowLeft" || e.key === "a" || e.key === "A") { e.preventDefault(); tryMove(-1, 0); }
  else if (e.key === "ArrowRight" || e.key === "d" || e.key === "D") { e.preventDefault(); tryMove(1, 0); }
});

function resetGame() {
  player = { col: 1, row: 1 };
  score = 0;
  draw();
}

function clearWalls() {
  for (let r = 1; r < ROWS - 1; r++) {
    for (let c = 1; c < COLS - 1; c++) {
      if (map[r][c] === 1) map[r][c] = 0;
    }
  }
  draw();
}

draw();
</script>
</body>
</html>
"""

with open(os.path.join(FOLDER, "simulator", "index.html"), "w", encoding="utf-8") as f:
    f.write(simulator_html)

print("✅ Simulator generated for 7-8-sinf 29-dars")
