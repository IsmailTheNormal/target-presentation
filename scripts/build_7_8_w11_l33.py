#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_7_8_w11_l33.py — Builder for 7–8th Grade, Week 11, Lesson 33

Mavzu: Dushman AI va Pathfinding: To'siqlarni Aylanib Quvish Algoritmi
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 7-8-sinf (Vibecoding & Game Dev Track)
Pedagogika: SOF AMALIY GEYM-DIZAYN & VIBECODING — Murakkab matematik formulalar yo'q!
             O'quvchilar o'yinlariga aqlli dushman (Zombi, Kiber-O'rgimchak, Boss) qo'shadilar,
             AI ga bosqichma-bosqich prompt beradilar, to'siqlarni aylanib o'tishni sozlaydilar,
             do'stlari bilan duel o'ynab test qiladilar.
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
# 1. SLIDES HTML (14 Slides for 80-min Double Block — Practical Game Dev Focus)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="7–8-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 33" data-en="GRADES 7–8 · WEEK 11 · LESSON 33">7–8-SINF · 11-HAFTA · 33-DARS</span></div>
    <h1 class="display" data-ru="Оживляем Врагов: Умные Монстры в Нашем Roguelike Подземелье" data-en="Bringing Enemies to Life: Smart Monster AI for Our Roguelike">O'yiningga Aqlli Yirtqich Dushman Qo'shamiz!</h1>
    <p class="lede" data-ru="Как заставить монстров подземелья видеть героя, обходить каменные стены и преследовать игрока по лабиринту: создаем живой искусственный интеллект для игры с помощью Vibecoding!" data-en="How to make dungeon monsters spot the hero, navigate around stone walls, and pursue the player: engineering living game AI with Vibecoding!">Labirint dushmanlarini tosh devorlarni aylanib o'tib, qahramonni eng qisqa yo'l bilan quvlashga o'rgatamiz: devorga tiqilib qolmaydigan, ko'rish nuri va 3 xil kayfiyatga ega aqlli dushman AI loyihasi!</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Практический Геймдев" data-en="Hands-on Game Dev">Amaliy Geym-Dizayn</h3>
        <p data-ru="Никаких скучных формул: строим реального монстра, который видит через фонарик, не застревает в углах и атакует игрока." data-en="Zero boring math: build a living monster with flashlight vision that dodges walls and hunts the hero.">Ortiqcha nazariyasiz: ko'rish chirog'i bor, tosh burchaklarga tiqilmaydigan va o'yinchiga hujum qiluvchi jonli dushman yaratamiz.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Monster AI Engine</div>
        <h3 data-ru="Рабочий Модуль Врага" data-en="Working Monster Module">Tayyor Dushman Dvigateli</h3>
        <p data-ru="Каждый ученик добавит в свою игру хищника с 3 режимами: Спокойный патруль, Тревога и Яростная погоня." data-en="Every student adds a predator with 3 modes to their game: Patrol, Alert, and Frenzied Chase.">Har bir o'quvchi o'z o'yiniga 3 xil rejimli dushmanni kiritadi: Sokin patrul, Shubhali tovush va Quturgan ta'qib.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="РАЗБОР ДОМАШНЕГО ЗАДАНИЯ И МОСТ" data-en="HOMEWORK REVIEW & BRIDGE">UY VAZIFASI TAHLILI VA KO'PRIK</span></div>
    <h2 data-ru="Ошибки Стрельбы и Мост к Новой Миссии" data-en="Shooting Pitfalls & Bridge to the New Mission">32-Dars Otishma Tahlili va Yangi Dushmanga Ko'prik</h2>
    <div class="grid-2">
      <div>
        <div class="box" style="border-left:4px solid var(--accent); margin-bottom:12px;">
          <h4 data-ru="Главная ловушка: Бесконечные пули" data-en="Major Pitfall: Infinite Zombie Bullets">Eng Katta Xato: Cheksiz O'qlar va O'yin Qotishi</h4>
          <p style="font-size:12px;" data-ru="Ученики создавали массив пуль, но забывали удалять улетевшие за экран снаряды. Через 2 минуты игра зависала от 10,000 пуль!" data-en="Students added bullets but forgot cleanup. After 2 minutes of gameplay, 10,000 off-screen bullets lagged the browser!">O'quvchilar ekrandan chiqib ketgan o'qlarni massivdan o'chirishni unutishgan. Natijada 2 daqiqadan so'ng 10,000 ta o'q to'planib o'yin qotgan!</p>
        </div>
        <div class="box" style="border-left:4px solid var(--green);">
          <h4 data-ru="Золотой Стандарт (Очистка памяти)" data-en="Golden Standard (Memory Cleanup)">Oltin Yechim: Tozalash Filtri</h4>
          <pre style="font-size:11px; margin:4px 0;"><code>bullets = bullets.filter(b => !b.dead);</code></pre>
          <p style="font-size:11px; color:var(--ink-2); margin:0;" data-ru="При ударе о стену летят яркие искры, а отработавшая пуля удаляется." data-en="Sparks burst upon wall impact and dead bullets get removed.">Devorga tekkanda chiroyli uchqunlar sochiladi va o'q darhol yo'qotiladi.</p>
        </div>
      </div>
      <div>
        <div class="box" style="margin-bottom:12px; background:var(--panel-2);">
          <div class="tag" style="background:var(--accent-soft); color:var(--accent);" data-ru="Блиц-Вопрос" data-en="Blitz Question">30 Soniyalik Blitz Savol</div>
          <p style="font-size:13px; font-weight:600; margin:6px 0;" data-ru="Мы научились метко стрелять во все стороны. Но по кому стрелять в пустом лабиринте?" data-en="We mastered 360-degree shooting. But whom do we shoot in an empty dungeon?">O'q uzishni o'rgandik, lekin bo'sh labirintda kimga qarata o't ochamiz?</p>
          <p style="font-size:12px; color:var(--green); font-weight:700;" data-ru="👉 Ответ: Нам нужен живой, хитрый враг, который охотится на нас!" data-en="👉 Answer: We need a clever predator that hunts us down!">👉 Javob: Albatta bizni labirint bo'ylab qidirib keluvchi yirtqich dushmanga!</p>
        </div>
        <div class="box" style="border-left:4px solid var(--purple);">
          <h4 data-ru="Мост к сегодняшней теме" data-en="Bridge to Today's Mission">Bugungi Mavzuga Ko'prik</h4>
          <p style="font-size:12px;" data-ru="Сегодня мы вдохнем жизнь в монстров: научим их видеть через стены, обходить тупики и устраивать засады!" data-en="Today we breathe life into monsters: giving them eyes, obstacle avoidance, and stealth pursuit!">Bugun dushmanlarni tiriltiramiz: devorlarni aylanib o'tish, chiroq nuri bilan payqash va bizni quvish mexanikasini quramiz!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: THE GAMEPLAY PROBLEM -->
  <section class="slide" data-phase="Muammo|Проблема|Problem" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ГЕЙМ-ДИЗАЙН КРИЗИС" data-en="GAMEDEV CRISIS">KATTA GEYM-DIZAYN MUAMMOSI</span></div>
    <h2 data-ru="Почему Глупый Враг Застревает в Стенах?" data-en="Why Dumb Enemies Freeze at Obstacles">Nega Oddiy Dushman Labirintda Qotib Qoladi?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="В простых играх враг просто бежит по прямой линии на координаты героя:" data-en="In naive games, enemies simply charge along a direct straight line towards the hero:">Oddiy o'yinlarda dushman shunchaki to'g'ri chiziq bo'ylab qahramon tomon yuguradi:</p>
        <ul class="clean-list">
          <li data-ru="<strong>Прямой бег:</strong> Если герой справа — бежать вправо. Если внизу — бежать вниз." data-en="<strong>Direct Run:</strong> If player is right, run right. If below, run down."><strong>To'g'ri yugurish:</strong> Qahramon o'ngda bo'lsa o'ngga, pastda bo'lsa pastga yuguradi.</li>
          <li data-ru="<strong>Ловушка:</strong> Посреди комнаты стоит каменная стена или колонна." data-en="<strong>The Trap:</strong> A solid stone wall or column stands in between."><strong>Qopqon:</strong> Yo'l o'rtasida bitta tosh devor yoki ustun paydo bo'ldi.</li>
          <li data-ru="<strong>Коллапс:</strong> Враг утыкается лбом в стену и беспомощно дрожит на месте!" data-en="<strong>Disaster:</strong> The monster bangs its head against the wall and vibrates helplessly!"><strong>Kulgili holat:</strong> Dushman devorga kallasini urib, qimirlamay titrab turadi!</li>
        </ul>
      </div>
      <div>
        <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); margin-bottom:12px;">
          <div style="color:var(--accent); font-weight:700; font-size:12px; margin-bottom:6px;" data-ru="❌ Глупый ИИ (Dumb AI):" data-en="❌ Dumb Enemy AI:">❌ Qotib qoluvchi dushman:</div>
          <div style="font-family:var(--font-mono); font-size:11px; color:#94a3b8; line-height:1.5;">
            hero = [X: 10, Y: 5]<br>
            monster = [X: 2, Y: 5]<br>
            <span style="color:var(--yellow);">// O'rtada tosh devor bor! [X: 5, Y: 5]</span><br>
            <span style="color:var(--accent);">monster.x += speed; // Devorga urildi va qotib qoldi!</span>
          </div>
        </div>
        <div class="box" style="border-left:4px solid var(--green);">
          <h4 data-ru="Решение Настоящего Геймдева" data-en="Real Game Dev Solution">Geym-Dizaynerning Yechimi</h4>
          <p style="font-size:12px;" data-ru="Умный монстр должен 'видеть' лабиринт: если прямо стена, он должен повернуть налево или направо и обойти препятствие!" data-en="A smart monster must read the maze: if a wall blocks the path, flank left or right and circle around!">Aqlli dushman labirintni his qilishi kerak: oldida tosh bo'lsa, chapga yoki o'ngga aylanib o'tib, yo'lini davom ettirishi shart!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: THE TILE GRID -->
  <section class="slide" data-phase="Labirint Kataklari|Сетка Лабиринта|Grid Map" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="КАРТА КАК ШАХМАТНАЯ ДОСКА" data-en="GRID AS CHESSBOARD">DUSHMANNING KO'ZLARI</span></div>
    <h2 data-ru="Глаза Монстра: Карта как Шахматная Доска" data-en="Monster's Eyes: The Maze as a Chessboard Grid">Dushmanning Ko'zlari: Maydon Kataklari va Devorlar</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Чтобы монстр мог думать, игра делит весь экран на понятные квадратные клетки (Тайлы):" data-en="To help monsters reason, the game splits the entire screen into clear square tiles:">Dushman yo'lni tushunishi uchun butun ekran shaxmat doskasiga o'xshash kataklarga bo'linadi:</p>
        <ul class="clean-list">
          <li data-ru="<strong>🟩 Зеленая клетка (0):</strong> Свободный пол подземелья — монстр может спокойно шагать." data-en="<strong>🟩 Green Tile (0):</strong> Open dungeon floor — monster walks freely."><strong>🟩 Bo'sh kataklar:</strong> Xavfsiz pol, dushman erkin qadam tashlay oladi.</li>
          <li data-ru="<strong>⬛ Серая клетка (1):</strong> Каменная стена — заходить строго запрещено!" data-en="<strong>⬛ Grey Tile (1):</strong> Solid stone wall — strictly forbidden to step into!"><strong>⬛ Tosh devorlar:</strong> Qizil to'siq, bu katakka kirish taqiqlangan!</li>
          <li data-ru="<strong>4 Направления:</strong> Вверх, Вниз, Влево, Вправо — только по свободным клеткам." data-en="<strong>4 Directions:</strong> Up, Down, Left, Right — only onto free tiles."><strong>4 Tomonga harakat:</strong> Yuqoriga, Pastga, Chapga, O'ngga.</li>
        </ul>
      </div>
      <div>
        <div class="box" style="text-align:center; padding:16px; background:var(--panel);">
          <div style="font-size:12px; font-weight:700; color:var(--ink-2); margin-bottom:8px;" data-ru="Сетка подземелья (Grid Matrix)" data-en="Dungeon Grid Matrix">Labirint Kataklari Sxemasi</div>
          <div style="display:inline-grid; grid-template-columns:repeat(5, 36px); gap:4px; font-family:var(--font-mono); font-size:11px; font-weight:700;">
            <div style="background:#e2eaf4; padding:8px; border-radius:4px;">🟩</div>
            <div style="background:#e2eaf4; padding:8px; border-radius:4px;">🟩</div>
            <div style="background:#334155; color:#fff; padding:8px; border-radius:4px;">⬛</div>
            <div style="background:#e2eaf4; padding:8px; border-radius:4px;">🟩</div>
            <div style="background:#dcfce7; padding:8px; border-radius:4px;">🦸</div>

            <div style="background:#fee2e2; padding:8px; border-radius:4px;">🧟</div>
            <div style="background:#e2eaf4; padding:8px; border-radius:4px;">🟩</div>
            <div style="background:#334155; color:#fff; padding:8px; border-radius:4px;">⬛</div>
            <div style="background:#e2eaf4; padding:8px; border-radius:4px;">🟩</div>
            <div style="background:#e2eaf4; padding:8px; border-radius:4px;">🟩</div>

            <div style="background:#e2eaf4; padding:8px; border-radius:4px;">🟩</div>
            <div style="background:#e2eaf4; padding:8px; border-radius:4px;">🟩</div>
            <div style="background:#e2eaf4; padding:8px; border-radius:4px;">🟩</div>
            <div style="background:#e2eaf4; padding:8px; border-radius:4px;">🟩</div>
            <div style="background:#e2eaf4; padding:8px; border-radius:4px;">🟩</div>
          </div>
          <p style="font-size:11px; color:var(--ink-3); margin-top:10px;" data-ru="Зомби (🧟) видит стену (⬛) и огибает ее снизу через свободные клетки к герою (🦸)!" data-en="Zombie (🧟) spots the wall (⬛) and loops under it through open tiles towards the hero (🦸)!">Zombi (🧟) tosh devor (⬛) borligini ko'rib, uni pastdan aylanib qahramon (🦸) tomon yuguradi!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: WATER FLOW METHOD -->
  <section class="slide" data-phase="Suv Oqimi|Принцип Воды|Water Flow" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="ИНТУИТИВНЫЙ ПОИСК ПУТИ" data-en="INTUITIVE PATHFINDING">HARAKAT MANTIG'I</span></div>
    <h2 data-ru="Принцип Течения Воды: Как Обходить Препятствия" data-en="The Flowing Water Principle: Circling Around Walls">Suv Oqimi Usuli: Devorlarni Qanday Aylanib O'tish Kerak?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Представьте, что вы вылили воду на наклонный стол с камнем. Что сделает вода?" data-en="Imagine pouring water onto a sloped table with a stone obstacle. What happens?">Tasavvur qiling, tosh ustiga chelakdan suv quydingiz. Suv toshni teshib o'tmaydi, balki ikki chetidan aylanib pastga oqadi:</p>
        <ul class="clean-list">
          <li data-ru="<strong>Волна поиска:</strong> Монстр мысленно пускает волну по коридорам." data-en="<strong>Search Wave:</strong> The monster mentally sends a ripple through corridors."><strong>To'lqinsimon qidiruv:</strong> Dushman xuddi suv kabi har bir bo'sh koridorga oqadi.</li>
          <li data-ru="<strong>Выбор лучшего поворота:</strong> Из двух свободных путей выбирается тот, который ближе к герою." data-en="<strong>Smart Turn:</strong> Out of two open corridors, it picks the one closer to the player."><strong>Eng optimal burilish:</strong> Qaysi yo'l qahramonga yaqinroq bo'lsa, o'sha burilish tanlanadi.</li>
          <li data-ru="<strong>Никаких застреваний:</strong> Даже в лабиринте монстр найдет выход за секунду!" data-en="<strong>Zero Freezing:</strong> Even in complex mazes, the monster finds the exit in seconds!"><strong>Qotish yo'q:</strong> Eng chigal berk ko'chalardan ham 1 soniyada chiqib keladi!</li>
        </ul>
      </div>
      <div>
        <div class="box" style="border-left:4px solid var(--accent); margin-bottom:12px;">
          <h4 data-ru="Секрет Vibecoding для ИИ:" data-en="Vibecoding Secret for AI:">AI ga Beriladigan Asosiy Qoida:</h4>
          <p style="font-size:12px; font-style:italic;" data-ru="«Если перед монстром стена, проверь соседние клетки сверху, снизу, слева и справа. Выбери свободную клетку, которая ближе всего к герою, и шагай туда!»" data-en="«If a wall is directly in front, check neighbors up, down, left, right. Pick the open tile closest to the hero and step there!»">"Agar dushmanning oldida devor bo'lsa, to'xtab qolma! Yon tomondagi bo'sh kataklarni tekshir, qahramonga eng yaqin bo'sh katakka qadam tashla!"</p>
        </div>
        <div class="box" style="background:var(--green-soft); border-left:4px solid var(--green);">
          <span style="font-weight:700; color:var(--green); font-size:12px;" data-ru="🎯 Итог: Монстр движется плавно, как живой охотник в кино!" data-en="🎯 Result: The monster flows smoothly like a real predator in movies!">🎯 Natija: Dushman xuddi kinolardagi yirtqich kabi silliq va aqlli quvlaydi!</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: 3 ENEMY STATES (FSM) -->
  <section class="slide" data-phase="3 Holat|3 Состояния Врага|3 States" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ПСИХОЛОГИЯ И ХАРАКТЕР МОНСТРА" data-en="MONSTER PSYCHOLOGY">DUSHMAN PSIXOLOGIYASI</span></div>
    <h2 data-ru="3 Состояния Хищника: Патруль ➔ Тревога ➔ Погоня" data-en="3 Predator States: Patrol ➔ Alert ➔ Chase">Dushman Xarakteri: 1. Sokin ➔ 2. Shubhali ➔ 3. Quturgan</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid #3b82f6;">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:#2563eb;" data-ru="Режим 1" data-en="Mode 1">1. SOkin Patrul</div>
        <h4 data-ru="💤 Спокойный Патруль" data-en="💤 Peaceful Patrol">💤 Sokin Patrul</h4>
        <p style="font-size:12px;" data-ru="Монстр еще не знает о герое. Медленно ходит по коридору туда-обратно. Скорость 1x. Фонарик синий." data-en="Monster unaware of hero. Slowly patrols between waypoints. 1x speed. Blue vision light.">Dushman bizni ko'rmagan. Koridorda sokin aylanadi. Tezligi oddiy (1x), ko'rish chirog'i ko'k rangda.</p>
      </div>
      <div class="box" style="border-top:4px solid #f59e0b;">
        <div class="tag" style="background:rgba(245,158,11,0.15); color:#d97706;" data-ru="Режим 2" data-en="Mode 2">2. Shubhali Qidiruv</div>
        <h4 data-ru="❓ Что это за звук?!" data-en="❓ What's That Noise?!">❓ Shubhali Tovush</h4>
        <p style="font-size:12px;" data-ru="Игрок выстрелил или пробежал рядом! Монстр останавливается, фонарик желтеет, и он идет проверить шум!" data-en="Hero shot a gun or ran nearby! Monster halts, light turns yellow, investigates the noise point!">O'yinchi o'q uzdi yoki yugurdi! Dushman to'xtab, chirog'i sariq bo'ladi va shovqin chiqqan tomonga qarab yuradi!</p>
      </div>
      <div class="box" style="border-top:4px solid #ef4444;">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:#dc2626;" data-ru="Режим 3" data-en="Mode 3">3. Quturgan Ta'qib</div>
        <h4 data-ru="🔥 Я тебя вижу!" data-en="🔥 Spotted You!">🔥 Quturgan Ta'qib!</h4>
        <p style="font-size:12px;" data-ru="Герой попал в луч света! Сирена, фонарик вспыхивает красным, скорость возрастает до 1.8x — спасайся кто может!" data-en="Hero stepped into the light! Red alert siren, 1.8x frenzy sprint — run for your life!">Qahramon ko'rish nuriga tushdi! Qizil signal yonadi, tezligi 1.8x ga oshadi va labirint bo'ylab quvlaydi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: MONSTER ROSTER -->
  <section class="slide" data-phase="Monstr Turlari|Виды Монстров|Monster Types" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ВЫБИРАЕМ МОНСТРА ДЛЯ ИГРЫ" data-en="SELECTING YOUR MONSTER">MONSTERLAR ROSTERI</span></div>
    <h2 data-ru="3 Вида Монстров: Кого Ты Добавишь в Игру?" data-en="3 Monster Archetypes: Which One Will You Build?">3 Ta Dushman Turi: O'yiningga Qaysi Birini Tanlaysan?</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div style="font-size:32px; margin-bottom:8px;">🧟</div>
        <h3 data-ru="Танк-Зомби" data-en="Zombie Tank">Zombi (Klassik)</h3>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Медленный, но живучий (3 жизни). Неумолимо идет за игроком, обходя все стены до конца комнаты." data-en="Slow but durable (3 HP). Relentlessly pursues the player, skirting all walls.">Sekin yuradi (0.8x tezlik), lekin joni ko'p (3 HP). Barcha devorlarni charchamay aylanib keladi.</p>
        <div class="tag" style="background:#e0f2fe; color:#0369a1;">Tavsiya: Boshlang'ich</div>
      </div>
      <div class="box">
        <div style="font-size:32px; margin-bottom:8px;">🕷️</div>
        <h3 data-ru="Кибер-Паук" data-en="Cyber Spider">Kiber-O'rgimchak</h3>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Очень быстрый спринтер (2x скорость)! Умирает от одного выстрела, но срезает углы молниеносно!" data-en="Lightning sprinter (2x speed)! Dies in one shot, but cuts corners with ruthless agility!">Juda tezkor (2x tezlik). Bitta o'qdan o'ladi, lekin burchaklardan yashindek aylanib yetib oladi!</p>
        <div class="tag" style="background:#fef3c7; color:#b45309;">Tavsiya: Chaqliriq</div>
      </div>
      <div class="box">
        <div style="font-size:32px; margin-bottom:8px;">👹</div>
        <h3 data-ru="Огненный Босс" data-en="Dungeon Boss">Kiber-Boss</h3>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Гигантский монстр (5 жизней). Огромный фонарь обзора и способность стрелять огненными шарами!" data-en="Giant monster (5 HP). Massive vision cone and spits fireball projectiles at the hero!">Katta kiber-yirtqich (5 HP). Katta ko'rish nuri bor va qahramonni ko'rsa o't sharlarini otadi!</p>
        <div class="tag" style="background:#fee2e2; color:#b91c1c;">Tavsiya: Professional</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: IN-DECK INTERACTIVE SIMULATOR -->
  <section class="slide" data-phase="Smartboard Sinovi|Интерактив на Доске|In-Deck Simulator" data-time="40:00–48:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ЖИВОЙ ТЕСТ НА СМАРТБОРДЕ" data-en="SMARTBOARD LIVE ARENA">SMARTBOARDDA JONLI SINOV</span></div>
    <h2 data-ru="Попробуй Убежать от Монстра Прямо на Доске!" data-en="Try Escaping the Monster Right on the Smartboard!">Doskada Labirint Chiz va Dushmandan Qochib Ko'r!</h2>
    <p class="lede" style="font-size:13px; margin-bottom:8px;" data-ru="Нажимайте на клетки, чтобы ставить каменные стены (⬛). Двигайте героя стрелками и смотрите, как монстр огибает препятствия!" data-en="Click tiles to place stone walls (⬛). Move hero with arrow keys and watch the monster loop around walls!">Kataklarni bosing — tosh devorlar (⬛) paydo bo'ladi. Strelkalar bilan qahramonni (🦸) boshqaring va dushman qanday aylanib kelayotganini ko'ring!</p>
    
    <div style="background:#090d16; border:1px solid rgba(255,255,255,0.15); border-radius:8px; padding:10px; display:flex; flex-direction:column; align-items:center;">
      <div style="display:flex; gap:12px; margin-bottom:8px; align-items:center;">
        <span style="color:#fff; font-size:12px; font-weight:700;">Dushman Rejimi:</span>
        <button id="deck-btn-smart" class="btn" style="padding:4px 12px; font-size:11px; background:var(--green); color:#fff;" data-ru="🟢 Умный (Обходит Стены)" data-en="🟢 Smart (Dodges Walls)">🟢 Aqlli (Devorni Aylanadi)</button>
        <button id="deck-btn-naive" class="btn" style="padding:4px 12px; font-size:11px; background:#475569; color:#fff;" data-ru="🔴 Простой (Застревает)" data-en="🔴 Naive (Gets Stuck)">🔴 Sodda (Tiqilib Qoladi)</button>
        <button id="deck-btn-reset" class="btn" style="padding:4px 12px; font-size:11px; background:#334155; color:#fff;" data-ru="🧹 Сброс Стен" data-en="🧹 Clear Walls">🧹 Tozalash</button>
      </div>
      <canvas id="deck-pathfinding-canvas" width="600" height="260" style="border:2px solid #334155; border-radius:6px; cursor:crosshair; background:#0f172a; touch-action:none;"></canvas>
      <div style="font-size:11px; color:#94a3b8; margin-top:6px;">
        🖱️ <b>Sichqoncha bilan devor chizing</b> | ⌨️ <b>Strelkalar: Qahramonni qochiring</b> | 🧟 <b>Dushman: Qizil kvadrat</b>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: QUICK GAMER QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Quiz" data-time="48:00–55:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА ИНТУИЦИИ ГЕЙМДЕВА" data-en="GAMEDEV INTUITION CHECK">TEZKOR GEYMER SAVOLLARI</span></div>
    <h2 data-ru="3 Вопроса: Сможешь ли Ты Перехитрить Монстра?" data-en="3 Questions: Can You Outsmart the Monster?">Dushman AI Bo'yicha 3 Ta Tezkor Savol</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:#dbeafe; color:#1e40af;">1-Savol</div>
        <h4 data-ru="Почему простой враг дрожит у стены?" data-en="Why does a simple enemy shake at walls?">Nega oddiy dushman devorga kallasini urib qotadi?</h4>
        <div class="interactive-opt" onclick="this.classList.toggle('selected');" style="margin-top:8px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">A) Chunki u uxlab qoladi</div>
        <div class="interactive-opt correct-opt" onclick="this.classList.toggle('selected');" style="margin-top:4px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">B) Chunki u faqat to'g'ri chiziqda yugurishni biladi, burilishni bilmaydi</div>
      </div>
      <div class="box">
        <div class="tag" style="background:#fef3c7; color:#92400e;">2-Savol</div>
        <h4 data-ru="Какой цвет фонарика включает режим бега?" data-en="Which light color triggers sprint mode?">Qaysi rangli ko'rish nuri dushmanning eng tez yugurishini bildiradi?</h4>
        <div class="interactive-opt" onclick="this.classList.toggle('selected');" style="margin-top:8px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">A) Moviy ko'k chiroq</div>
        <div class="interactive-opt correct-opt" onclick="this.classList.toggle('selected');" style="margin-top:4px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">B) Qizil ogohlantirish chirog'i (Alert!)</div>
      </div>
      <div class="box">
        <div class="tag" style="background:#fee2e2; color:#991b1b;">3-Savol</div>
        <h4 data-ru="Зачем делить экран на клетки (сетку)?" data-en="Why divide the screen into a tile grid?">Nima uchun o'yin maydoni kataklarga (Grid) bo'linadi?</h4>
        <div class="interactive-opt correct-opt" onclick="this.classList.toggle('selected');" style="margin-top:8px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">A) Dushman qaysi yo'l bo'sh va qayerda tosh borligini adashmasdan hisoblashi uchun</div>
        <div class="interactive-opt" onclick="this.classList.toggle('selected');" style="margin-top:4px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">B) Shunchaki chiroyli ko'rinishi uchun</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: VIBECODING PROMPTING LAB -->
  <section class="slide" data-phase="Amaliy Arena|Практическая Арена|Hands-on Arena" data-time="55:00–70:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ПОШАГОВЫЙ VIBECODING В ДЕЛЕ" data-en="STEP-BY-STEP VIBECODING">VIBECODING: 4 BOSQICHDA MONSTR YARATISH</span></div>
    <h2 data-ru="Vibecoding: 4 Точных Промпта для Создания ИИ Монстра" data-en="Vibecoding: 4 Precision Prompts to Engineer Monster AI">AI ga 4 Bosqichda Aniq So'rov Berib O'yinni Yaratamiz!</h2>
    <div class="grid-2">
      <div>
        <div class="box" style="margin-bottom:8px; border-left:4px solid #3b82f6;">
          <div style="font-weight:700; font-size:11px; color:#2563eb;">1-BOSQICH: Dushman Ob'ekti (Baza)</div>
          <p style="font-size:11px; margin:4px 0; color:var(--ink-2); font-style:italic;" data-ru="«Добавь в мою Canvas-игру объект зомби: координаты x, y, скорость: 2, hp: 3. В каждом кадре он делает 1 шаг к координатам героя.»" data-en="«Add a zombie object to my Canvas game: x, y, speed: 2, hp: 3. Each frame it takes 1 step towards hero coordinates.»">"Mening Canvas o'yinimga zombi ob'ekti qo'sh: x, y koordinatasi, speed: 2, hp: 3 bo'lsin. Har frame'da u qahramon koordinatasi tomon 1 qadam tashlasin."</p>
        </div>
        <div class="box" style="border-left:4px solid #10b981;">
          <div style="font-weight:700; font-size:11px; color:#059669;">2-BOSQICH: Devorlarni Aylanib O'tish Mantig'i</div>
          <p style="font-size:11px; margin:4px 0; color:var(--ink-2); font-style:italic;" data-ru="«Монстр не должен застревать у каменных стен. Если впереди стена, поверни на свободную соседнюю клетку и обойди препятствие.»" data-en="«The monster must not get stuck at walls. If the next tile is blocked, pivot to an open adjacent tile and loop around the obstacle.»">"Dushman tosh devorga urilib qotib qolmasin. Agar oldidagi katak tosh bo'lsa, yon tomondagi bo'sh katakka burilib, toshni aylanib o'tsin."</p>
        </div>
      </div>
      <div>
        <div class="box" style="margin-bottom:8px; border-left:4px solid #f59e0b;">
          <div style="font-weight:700; font-size:11px; color:#d97706;">3-BOSQICH: Ko'rish Nuri (Sight Cone)</div>
          <p style="font-size:11px; margin:4px 0; color:var(--ink-2); font-style:italic;" data-ru="«Нарисуй перед монстром конус света фонарика на 90 градусов. Если герой попадает в этот луч, монстр краснеет и бежит со скоростью 1.5x!»" data-en="«Draw a 90-degree flashlight cone in front of the monster. If the hero steps into this light, the monster turns red and sprints at 1.5x speed!»">"Dushmanning oldida 90 darajali ko'rish chirog'ini chiz. Agar qahramon shu nur ichiga kirsa, dushman qizil rangga kirsin va 1.5x tezlikda quvsin!"</p>
        </div>
        <div class="box" style="border-left:4px solid #ef4444;">
          <div style="font-weight:700; font-size:11px; color:#dc2626;">4-BOSQICH: Hujum va O'yinchining Joni (-1 HP)</div>
          <p style="font-size:11px; margin:4px 0; color:var(--ink-2); font-style:italic;" data-ru="«Если монстр касается героя, отними у игрока 1 жизнь (HP), моргни экраном красным на 0.2 секунды и оттолкни монстра чуть назад.»" data-en="«If the monster touches the hero, deduct 1 HP, flash the screen red for 0.2 seconds, and knock the monster slightly back.»">"Agar dushman qahramonga tegsa, o'yinchidan -1 Jon ayirilsin, ekran 0.2 soniya qizil yonib-o'chsin va dushman biroz orqaga surilsin."</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: PEER REVIEW PLAYTEST -->
  <section class="slide" data-phase="Partadosh Auditi|Взаимный Аудит|Peer Review" data-time="70:00–74:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ТЕСТИРОВАНИЕ ИГРЫ ДРУГА" data-en="PEER PLAYTESTING">PARTADOSH DUELOSI</span></div>
    <h2 data-ru="Баттл Лабиринтов: Выживи в Игре Своего Соседа!" data-en="Maze Battle: Survive in Your Friend's Dungeon!">Partadosh Duelosy: Do'stingning Labirintida Omon Qol!</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Поменяйтесь местами с соседом по парте! Сыграйте в его игру и проверьте монстра по 4 пунктам:" data-en="Swap seats with your classmate! Playtest their game and test the monster against 4 checkpoints:">Partadoshingiz bilan joyingizni almashtiring! Do'stingizning o'yinini o'ynab, uning dushmanini 4 ta sinovdan o'tkazing:</p>
        <ul class="clean-list">
          <li data-ru="<strong>1. Тест тупика:</strong> Заманите монстра в угол. Сможет ли он выбраться?" data-en="<strong>1. Dead-end test:</strong> Lure monster into a corner. Can it escape?"><strong>1. Burchak sinovi:</strong> Dushmanni burchakka qamang — u aylanib chiqa oladimi?</li>
          <li data-ru="<strong>2. Прятки:</strong> Спрячьтесь за каменную колонну. Потеряет ли он вас из виду?" data-en="<strong>2. Stealth test:</strong> Hide behind a stone pillar. Does it lose sight?"><strong>2. Yashirinish sinovi:</strong> Tosh ustun orqasiga berkinib ko'ring.</li>
          <li data-ru="<strong>3. Атака:</strong> При касании отнимается ли ровно 1 жизнь?" data-en="<strong>3. Damage test:</strong> Does hero lose exactly 1 HP on touch?"><strong>3. Hujum sinovi:</strong> Dushman yetib olganda jon kamayadimi?</li>
          <li data-ru="<strong>4. Скорость:</strong> Не слишком ли он быстрый или медленный?" data-en="<strong>4. Balance test:</strong> Is the speed fun and balanced?"><strong>4. Balans sinovi:</strong> O'yin zavqlimi yoki dushmandan qochish imkonsizmi?</li>
        </ul>
      </div>
      <div>
        <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); margin-bottom:12px;">
          <div style="color:var(--accent); font-weight:700; font-size:12px; margin-bottom:6px;">🛠️ Agar dushman devorga tiqilib qolsa:</div>
          <p style="font-size:12px; color:#cbd5e1; margin:0;" data-ru="Сразу отправьте ИИ уточняющий запрос (Critic prompt):" data-en="Immediately send AI this critic bug-fix prompt:">AI ga darhol quyidagi tuzatish so'rovini (Critic prompt) bering:</p>
          <p style="margin-top:6px; font-size:11px; color:var(--yellow); font-family:var(--font-mono);" data-ru="«Монстр не должен заходить в текстуру стены и вибрировать. Усиль логику поворота на свободную соседнюю клетку.»" data-en="«The monster must not clip into walls or vibrate. Enforce turning to open neighbor tiles.»">"Dushman tosh devor ichiga kirmasin va devor oldida qotib qolmasin. Eng yaqin bo'sh katakka burilish mantig'ini kuchaytir."</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: BIG SCREEN SHOWCASE -->
  <section class="slide" data-phase="Katta Ekran|Шоукейс|Showcase" data-time="74:00–77:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ШОУКЕЙС НА БОЛЬШОМ ЭКРАНЕ" data-en="BIG SCREEN SHOWCASE">KATTA EKRAN SHOWCASE</span></div>
    <h2 data-ru="Шоукейс: Охота Монстров на Большом Смартборде!" data-en="Showcase: Monster Hunt on the Big Screen!">Katta Doskada Eng Aqlli Dushmanlar Namoyishi!</h2>
    <div class="grid-2">
      <div>
        <div class="box" style="margin-bottom:12px;">
          <div class="tag" style="background:#dcfce7; color:#166534;" data-ru="Лучшие Работы" data-en="Top Projects">2 Ta Eng Qiziqarli O'yin</div>
          <p style="font-size:13px; font-weight:600; margin:6px 0;" data-ru="Два ученика с самыми интересными монстрами выходят к доске и показывают свой геймплей!" data-en="Two students with coolest monsters come to the Smartboard to showcase gameplay!">Eng qiziqarli dushman yasagan 2 nafar o'quvchi doskaga chiqib, o'z labirintini butun sinfga ko'rsatadi!</p>
        </div>
        <ul class="clean-list">
          <li data-ru="У кого монстр самый хитрый и не застревает?" data-en="Whose monster is the smartest and never gets stuck?">Kimning dushmani eng chaqqon va devorga tiqilmaydi?</li>
          <li data-ru="У кого круче всего выглядит конус света фонарика?" data-en="Who has the coolest visual vision flashlight cone?">Kimning ko'rish chirog'i eng chiroyli animatsiyaga ega?</li>
          <li data-ru="Сможет ли учитель пройти ваш лабиринт живым?" data-en="Can the teacher survive your dungeon maze?">O'qituvchi sizning dushmaningizdan qochib omon qola oladimi?</li>
        </ul>
      </div>
      <div>
        <div class="box" style="text-align:center; padding:24px; background:var(--panel);">
          <div style="font-size:48px; margin-bottom:12px;">🏆</div>
          <h3 data-ru="Звание Лучшего ИИ Охотника" data-en="Master of Game AI Badge">"Kiber-Ovchi 2026" G'olibi</h3>
          <p style="font-size:12px; color:var(--ink-2);" data-ru="Ученик, чей монстр показал самое плавное преследование и честный геймплей, получает 10 баллов!" data-en="The student whose monster demonstrated smartest pursuit and balanced fun wins 10 points!">Eng silliq quvuvchi va qiziqarli o'yin muvozanatini yaratgan o'quvchi eng yuqori 10 ballni oladi!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: 3-TIER HOMEWORK -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Homework" data-time="77:00–79:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ДОМАШНЕЕ ЗАДАНИЕ (10 БАЛЛОВ)" data-en="HOMEWORK CHALLENGE (10 POINTS)">UYGA KIBER-VAZIFA</span></div>
    <h2 data-ru="3 Уровня: От Простого Монстра к Супер-Боссу" data-en="3 Tiers: From Basic Hunter to Epic Boss">3 Darajali Dushman AI Vazifasi (10 Ball)</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid #3b82f6;">
        <div class="tag" style="background:#e0f2fe; color:#0369a1;">1-Daraja: Baza (4 ball)</div>
        <h4 data-ru="Обход Стен" data-en="Wall Dodging">Devorni Aylanib O'tish</h4>
        <p style="font-size:12px;" data-ru="Заставьте монстра в вашей игре преследовать героя и не застревать на Т-образных стенах." data-en="Make your monster pursue the hero smoothly without freezing on obstacles.">Dushmaningiz qahramonni quvsin va yo'lda tosh devor uchrasa, to'xtab qolmasdan aylanib o'tsin.</p>
      </div>
      <div class="box" style="border-top:4px solid #10b981;">
        <div class="tag" style="background:#dcfce7; color:#15803d;">2-Daraja: Muhandis (4 ball)</div>
        <h4 data-ru="Фонарь Обзора (3 Цвета)" data-en="Flashlight Cone (3 Colors)">Ko'rish Nuri va 3 Holat</h4>
        <p style="font-size:12px;" data-ru="Добавьте луч света: синий (патруль), желтый (услышал звук), красный (яростная погоня 1.5x)." data-en="Add vision flashlight: blue (patrol), yellow (suspicious noise), red (frenzy pursuit 1.5x).">Dushmanga ko'rish nuri qo'shing: Ko'k (sokin), Sariq (tovush eshitdi), Qizil (quturgan tezkor ta'qib).</p>
      </div>
      <div class="box" style="border-top:4px solid #8b5cf6;">
        <div class="tag" style="background:#f3e8ff; color:#6b21a8;">3-Daraja: Chempion (2 ball)</div>
        <h4 data-ru="Супер-Способность" data-en="Boss Special Power">Maxsus Super-Kuch</h4>
        <p style="font-size:12px;" data-ru="Дайте монстру супер-силу: огненный выстрел, рывок вперед или призыв маленьких паучков!" data-en="Give monster a unique skill: fireball shot, quick leap, or spawning mini spider minions!">Dushmanga bitta super-qobiliyat bering: olovli o'q otish, oldinga sakrash yoki o'rgimchak bolalarini chaqirish!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И СЛЕДУЮЩИЙ ШАГ" data-en="SUMMARY & WHAT'S NEXT">XULOSA VA KEYINGI BOSQICH</span></div>
    <h2 data-ru="Чему Мы Научились и Что Будет Дальше?" data-en="What We Built & The Next Mission">O'yinimizga Jon Kirdi: Bugun Nimalar Qurdik?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Сегодня мы превратили пустую комнату в настоящую захватывающую игру:" data-en="Today we converted an empty room into a thrilling, living game world:">Bugun oddiy zerikarli bo'sh xonani haqiqiy hayajonli o'yinga aylantirdik:</p>
        <ul class="clean-list">
          <li data-ru="Враги больше не глупые картинки — они видят лабиринт и думают!" data-en="Monsters aren't dumb pictures anymore — they see the maze and think!">Dushmanlar endi shunchaki rasm emas — ular labirintni his qiladi va aylanib o'tadi!</li>
          <li data-ru="Фонарик обзора добавляет механику скрытности (Stealth): можно прятаться!" data-en="Flashlight vision adds stealth mechanics: players can hide behind pillars!">Ko'rish nuri tufayli o'yinda yashirinish (Stealth) paydo bo'ldi: devor ortiga berkinish mumkin!</li>
          <li data-ru="Vibecoding позволяет создавать сложнейшие механики за считанные минуты." data-en="Vibecoding enables building complex game mechanics in mere minutes.">Vibecoding yordamida har biringiz o'yin dasturchisiga aylandingiz!</li>
        </ul>
      </div>
      <div>
        <div class="box" style="border-left:4px solid var(--accent); background:var(--panel);">
          <div class="tag" style="background:var(--accent-soft); color:var(--accent);" data-ru="Анонс следующего урока" data-en="Next Lesson Teaser">Keyingi 34-Dars Ko'prigi</div>
          <h3 data-ru="Сундуки, Золото и Инвентарь!" data-en="Chests, Loot & Inventory!">Xazinalar, O'lja va Inventar Tizimi!</h3>
          <p style="font-size:12px; color:var(--ink-2);" data-ru="Монстры научились охотиться на нас. Но чем нам защищаться? В следующем уроке мы раскидаем по лабиринту золотые сундуки, мечи и аптечки!" data-en="Monsters now hunt us down. But how do we fight back? Next lesson we scatter gold chests, magic swords, and health potions across the dungeon!">Dushmanlar bizni ovlashni o'rgandi. Endi o'zimizni qanday himoya qilamiz? Keyingi darsda labirintga sehrli qutilar, qilichlar, qalqonlar va dori vositalari (Loot & Inventory) tizimini kiritamiz!</p>
        </div>
      </div>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. IN-DECK SIMULATOR JAVASCRIPT (Smartboard A* Live Canvas)
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
(function() {
  const canvas = document.getElementById('deck-pathfinding-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const COLS = 20;
  const ROWS = 9;
  const TILE = 28; // fits 560x252 within 600x260

  let grid = [];
  for (let r = 0; r < ROWS; r++) {
    grid[r] = [];
    for (let c = 0; c < COLS; c++) {
      grid[r][c] = 0; // 0 = empty, 1 = wall
    }
  }

  // Pre-seed some fun obstacles
  for (let r = 2; r <= 6; r++) grid[r][6] = 1;
  for (let r = 2; r <= 6; r++) grid[r][13] = 1;

  let player = { col: 17, row: 4 };
  let monster = { col: 2, row: 4 };
  let isSmart = true;
  let path = [];

  function manhattan(a, b) {
    return Math.abs(a.col - b.col) + Math.abs(a.row - b.row);
  }

  function getSmartPath(start, goal) {
    const openSet = [{ col: start.col, row: start.row, g: 0, f: manhattan(start, goal), parent: null }];
    const closed = new Set();

    while (openSet.length > 0) {
      openSet.sort((a, b) => a.f - b.f);
      const cur = openSet.shift();

      if (cur.col === goal.col && cur.row === goal.row) {
        let curr = cur;
        const res = [];
        while (curr.parent) {
          res.unshift({ col: curr.col, row: curr.row });
          curr = curr.parent;
        }
        return res;
      }

      const key = `${cur.col},${cur.row}`;
      closed.add(key);

      const dirs = [[0,-1],[0,1],[-1,0],[1,0]];
      for (const [dc, dr] of dirs) {
        const nc = cur.col + dc;
        const nr = cur.row + dr;
        if (nc < 0 || nc >= COLS || nr < 0 || nr >= ROWS) continue;
        if (grid[nr][nc] === 1) continue;
        if (closed.has(`${nc},${nr}`)) continue;

        const g = cur.g + 1;
        const f = g + manhattan({col:nc, row:nr}, goal);
        const existing = openSet.find(n => n.col === nc && n.row === nr);
        if (!existing) {
          openSet.push({ col: nc, row: nr, g, f, parent: cur });
        } else if (g < existing.g) {
          existing.g = g;
          existing.f = f;
          existing.parent = cur;
        }
      }
    }
    return [];
  }

  function render() {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw tiles
    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        const x = c * TILE + 20;
        const y = r * TILE + 4;
        if (grid[r][c] === 1) {
          ctx.fillStyle = '#334155';
          ctx.fillRect(x, y, TILE - 2, TILE - 2);
          ctx.strokeStyle = '#475569';
          ctx.strokeRect(x, y, TILE - 2, TILE - 2);
        } else {
          ctx.fillStyle = '#1e293b';
          ctx.fillRect(x, y, TILE - 2, TILE - 2);
        }
      }
    }

    // Calculate path
    if (isSmart) {
      path = getSmartPath(monster, player);
      ctx.strokeStyle = 'rgba(74, 222, 128, 0.6)';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(monster.col * TILE + 20 + TILE/2, monster.row * TILE + 4 + TILE/2);
      for (const p of path) {
        ctx.lineTo(p.col * TILE + 20 + TILE/2, p.row * TILE + 4 + TILE/2);
      }
      ctx.stroke();
    } else {
      ctx.strokeStyle = 'rgba(239, 68, 68, 0.5)';
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(monster.col * TILE + 20 + TILE/2, monster.row * TILE + 4 + TILE/2);
      ctx.lineTo(player.col * TILE + 20 + TILE/2, player.row * TILE + 4 + TILE/2);
      ctx.stroke();
      ctx.setLineDash([]);
    }

    // Draw Player
    const px = player.col * TILE + 20;
    const py = player.row * TILE + 4;
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath();
    ctx.arc(px + TILE/2, py + TILE/2, TILE/2 - 3, 0, Math.PI * 2);
    ctx.fill();
    ctx.font = '14px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('🦸', px + TILE/2, py + TILE/2);

    // Draw Monster
    const mx = monster.col * TILE + 20;
    const my = monster.row * TILE + 4;
    ctx.fillStyle = isSmart ? '#22c55e' : '#ef4444';
    ctx.beginPath();
    ctx.arc(mx + TILE/2, my + TILE/2, TILE/2 - 3, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillText('🧟', mx + TILE/2, my + TILE/2);
  }

  // Monster movement ticker
  setInterval(() => {
    if (isSmart && path.length > 0) {
      const next = path[0];
      monster.col = next.col;
      monster.row = next.row;
    } else if (!isSmart) {
      const dc = Math.sign(player.col - monster.col);
      const dr = Math.sign(player.row - monster.row);
      const nc = monster.col + dc;
      const nr = monster.row + dr;
      if (grid[monster.row][nc] === 0) monster.col = nc;
      if (grid[nr][monster.col] === 0) monster.row = nr;
    }
    render();
  }, 500);

  // Mouse / Touch drawing of walls
  function toggleWall(e) {
    const rect = canvas.getBoundingClientRect();
    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    const clientY = e.touches ? e.touches[0].clientY : e.clientY;
    const x = clientX - rect.left - 20;
    const y = clientY - rect.top - 4;
    const c = Math.floor(x / TILE);
    const r = Math.floor(y / TILE);
    if (c >= 0 && c < COLS && r >= 0 && r < ROWS) {
      if ((c === player.col && r === player.row) || (c === monster.col && r === monster.row)) return;
      grid[r][c] = grid[r][c] === 1 ? 0 : 1;
      render();
    }
  }

  canvas.addEventListener('click', toggleWall);

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    let dc = 0, dr = 0;
    if (e.key === 'ArrowUp' || e.key === 'w') dr = -1;
    else if (e.key === 'ArrowDown' || e.key === 's') dr = 1;
    else if (e.key === 'ArrowLeft' || e.key === 'a') dc = -1;
    else if (e.key === 'ArrowRight' || e.key === 'd') dc = 1;
    else return;

    const nc = player.col + dc;
    const nr = player.row + dr;
    if (nc >= 0 && nc < COLS && nr >= 0 && nr < ROWS && grid[nr][nc] === 0) {
      player.col = nc;
      player.row = nr;
      render();
    }
  });

  const btnSmart = document.getElementById('deck-btn-smart');
  const btnNaive = document.getElementById('deck-btn-naive');
  const btnReset = document.getElementById('deck-btn-reset');

  if (btnSmart) btnSmart.addEventListener('click', () => { isSmart = true; btnSmart.style.background = 'var(--green)'; if (btnNaive) btnNaive.style.background = '#475569'; render(); });
  if (btnNaive) btnNaive.addEventListener('click', () => { isSmart = false; btnNaive.style.background = '#ef4444'; if (btnSmart) btnSmart.style.background = '#475569'; render(); });
  if (btnReset) btnReset.addEventListener('click', () => {
    for (let r = 0; r < ROWS; r++) for (let c = 0; c < COLS; c++) grid[r][c] = 0;
    monster = { col: 2, row: 4 };
    player = { col: 17, row: 4 };
    render();
  });

  render();
})();
"""

# -----------------------------------------------------------------------------
# 3. TEACHER NOTES DATA (14 Slides Trilingual)
# -----------------------------------------------------------------------------
NOTES_DATA = {
  "uz": [
    [
      "Kirish va Maqsad",
      "O'quvchilarga bugungi missiya: labirintda qahramonni quvuvchi aqlli dushman yaratish haqida so'zlang.",
      "Doskaga qahramon va yirtqich dushman rasmini chizib ko'rsating."
    ],
    [
      "Uy Vazifasi Tahlili",
      "32-dars otishmasini eslang: cheksiz o'qlar xotirani to'ldirib o'yinni qotirishi xatosini tushuntiring.",
      "O'qlar o'chirilishi va devorga urilganda uchqunlar chiqishini ko'rsating."
    ],
    [
      "Geym-Dizayn Muammosi",
      "Sodda dushman nega tosh devorga kallasini urib qotib qolishini ko'rsating.",
      "O'quvchilarga savol bering: 'O'yin qiziq bo'lishi uchun dushman nima qilishi kerak?'"
    ],
    [
      "Maydon Kataklari",
      "O'yin ekrani shaxmat doskasiga o'xshash kataklar (bo'sh pol va tosh devor) ekanini tushuntiring.",
      "Doskada 5x3 katakli mini-xarita chizib ko'rsating."
    ],
    [
      "Suv Oqimi Usuli",
      "Tosh ustiga suv quyilsa suv toshni teshib o'tmaydi, balki ikki chetidan oqadi deb tushuntiring.",
      "Dushman ham xuddi shunday toshni aylanib qahramon tomon borishini ayting."
    ],
    [
      "Dushmanning 3 Kayfiyati",
      "3 xil rejimni tushuntiring: 1. Sokin patrul (ko'k), 2. Shubhali tovush (sariq), 3. Quturgan ta'qib (qizil).",
      "Chiroq ranglari o'zgarishi o'yinni hayajonli qilishini ta'kidlang."
    ],
    [
      "Monstrlar Rosteri",
      "Zombi (sekin, joni ko'p), O'rgimchak (tezkor) va Boss xususiyatlarini solishtiring.",
      "O'quvchilardan qaysi monstrni yasashlarini so'rang."
    ],
    [
      "Smartboardda Jonli Sinov",
      "8-slaydni oching: o'quvchilarni doskaga chaqirib tosh devorlar chizdiring.",
      "Strelkalar bilan qahramonni qochiring, dushman devorlarni aylanib kelayotganini ko'rsating."
    ],
    [
      "Geymerlar Viktorinasi",
      "3 ta qiziqarli savol orqali tushunchalarni mustahkamlang.",
      "To'g'ri javob bergan o'quvchilarni rag'batlantiring."
    ],
    [
      "Vibecoding Arenasi",
      "O'quvchilarga 4 ta tayyor prompt kartasini ko'rsating va kompyuterlarida ishga tushirishlarini ayting.",
      "Zaldan aylanib dushmanini o'yinga kiritgan o'quvchilarni tekshiring."
    ],
    [
      "Partadosh Duelosy",
      "Partadoshlar joyini almashtirib, bir-birining dushmanidan omon qolishga harakat qilsin.",
      "Dushman devorga tiqilib qolsa, Critic prompt berishni o'rgating."
    ],
    [
      "Katta Ekran Showcasi",
      "Eng qiziqarli dushman yasagan 2 nafar o'quvchini doskaga chaqirib namoyish qildiring.",
      "Butun sinf bilan birgalikda dushmanning quvishini tomosha qiling."
    ],
    [
      "Uyga Kiber-Vazifa",
      "10 ballik rubrikani tushuntiring: devorni aylanadi, ko'rish nuri bor, super-qobiliyat qo'shiladi.",
      "Vazifa ilovasida LocalStorage avto-saqlanishini eslatib o'ting."
    ],
    [
      "Xulosa va Keyingi Dars",
      "Bugun o'yinimizga jon kirdi: endi xonada xavfli va aqlli yirtqich borligini xulosa qiling.",
      "Keyingi 34-darsda xazinalar, sehrli qutilar va inventar tizimi (Loot) bo'lishini e'lon qiling."
    ]
  ],
  "ru": [
    [
      "Введение и Цель",
      "Расскажите ученикам о миссии: оживить хищного монстра, который преследует героя в лабиринте.",
      "Нарисуйте на доске схему подземелья и крадущегося монстра."
    ],
    [
      "Разбор ДЗ",
      "Вспомните 32-й урок: бесконечные пули и зависание браузера от утечки памяти.",
      "Покажите золотой стандарт фильтрации пуль и вспышки искр."
    ],
    [
      "Проблема Глупого ИИ",
      "Объясните, почему простой бег по прямой приводит к вибрации у стены.",
      "Спросите класс: 'Что должен сделать умный монстр, встретив стену?'"
    ],
    [
      "Сетка Тайлов",
      "Объясните сетку подземелья: проходимый пол и непроходимые каменные блоки.",
      "Продемонстрируйте на доске координаты клеток."
    ],
    [
      "Принцип Воды",
      "Объясните аналогию с водой: поток огибает камень с двух сторон, не пробивая его насквозь.",
      "Подчеркните плавность такого обхода препятствий."
    ],
    [
      "3 Режима Хищника",
      "Разберите 3 состояния: 1. Патруль (синий свет), 2. Тревога (желтый свет), 3. Погоня (красный свет).",
      "Объясните, как меняется скорость монстра."
    ],
    [
      "Ростер Монстров",
      "Сравните Зомби-танка, Кибер-Паука и Огненного Босса.",
      "Помогите ученикам выбрать архетип для своего проекта."
    ],
    [
      "Тест на Смартборде",
      "Откройте 8-й слайд: вызовите учеников к доске рисовать стены и убегать от зомби.",
      "Переключайте режимы Smart и Naive для демонстрации."
    ],
    [
      "Геймерский Квиз",
      "Закрепите понятия через 3 интерактивных вопроса на слайде.",
      "Похвалите учеников за правильные ответы."
    ],
    [
      "Vibecoding Арена",
      "Покажите 4 пошаговых промпта и запустите 30 минут самостоятельной работы за ПК.",
      "Проходите по рядам и помогайте настраивать код."
    ],
    [
      "Взаимный Дуэльный Тест",
      "Ученики меняются местами и пробуют выжить в лабиринте соседа.",
      "Обучите отправлять Critic-промпты при застревании врага."
    ],
    [
      "Шоукейс на Доске",
      "Вызовите 2 авторов самых хитрых монстров на смартборд.",
      "Проведите живой классный турнир на выживание."
    ],
    [
      "Домашнее Задание",
      "Объясните 10-балльную рубрику: обход стен, фонарик обзора и спецспособность.",
      "Напомните про автосохранение в приложении vazifa.html."
    ],
    [
      "Итоги и Анонс",
      "Подведите итог: комната ожила, в ней появился умный хищник.",
      "Анонсируйте 34-й урок: сундуки с золотом, мечи и инвентарь (Loot)."
    ]
  ],
  "en": [
    [
      "Intro & Mission",
      "Introduce the mission: engineering a living predator that stalks the hero in the dungeon.",
      "Sketch the hero and pursuing monster layout on the board."
    ],
    [
      "Homework Review",
      "Review lesson 32: memory leaks caused by infinite bullets and lag prevention.",
      "Showcase the golden filter standard and particle sparks."
    ],
    [
      "Dumb AI Pitfall",
      "Demonstrate why naive direct chasing slams into walls and vibrates endlessly.",
      "Ask the class: 'What should a smart predator do when facing a wall?'"
    ],
    [
      "Grid Tiles",
      "Explain how the canvas is divided into walkable floor tiles and impassable stone walls.",
      "Show tile coordinates on the board."
    ],
    [
      "Flowing Water Logic",
      "Use the water analogy: water loops around rocks smoothly without tunneling through.",
      "Highlight smooth corner rounding in games."
    ],
    [
      "3 Predator States",
      "Break down 3 states: 1. Patrol (blue light), 2. Suspicious alert (yellow), 3. Frenzy chase (red).",
      "Explain how speed and aggression scale."
    ],
    [
      "Monster Roster",
      "Compare Zombie Tank, Agile Cyber-Spider, and Dungeon Boss.",
      "Help students pick an archetype for their game."
    ],
    [
      "Smartboard Live Arena",
      "Open slide 8: invite students to draw walls and evade the monster live on screen.",
      "Toggle Smart vs Naive AI modes for clear contrast."
    ],
    [
      "Gamer Quiz",
      "Reinforce pathfinding intuition through 3 interactive questions.",
      "Reward quick and accurate answers."
    ],
    [
      "Vibecoding Arena",
      "Display 4 structured prompt cards and launch 30 minutes of hands-on PC coding.",
      "Walk the floor and assist with AI generation."
    ],
    [
      "Peer Duel Playtest",
      "Students swap seats to test if peer monsters escape dead ends or freeze.",
      "Guide students on submitting Critic fix prompts."
    ],
    [
      "Big Screen Showcase",
      "Invite 2 students with best monster projects to demonstrate gameplay on the display.",
      "Cheer on evasive gameplay with the whole class."
    ],
    [
      "Homework Challenge",
      "Explain the 10-point rubric: wall dodging, vision cone, and custom boss skill.",
      "Remind them of LocalStorage auto-save in vazifa.html."
    ],
    [
      "Summary & Bridge",
      "Summarize the achievement: our game world now has a living, cunning adversary.",
      "Tease lesson 34: gold chests, weapons, and inventory system (Loot)."
    ]
  ]
}

# -----------------------------------------------------------------------------
# 4. BUILD FUNCTIONS
# -----------------------------------------------------------------------------
def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "33-dars: O'yiningga Aqlli Yirtqich Dushman Qo'shamiz! (Monster AI Lab)"
    title_ru = "Урок 33: Оживляем Врагов: Умные Монстры в Roguelike"
    title_en = "Lesson 33: Engineering Smart Monster AI for Your Roguelike"

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

    title_uz = "33-dars: O'yiningga Aqlli Yirtqich Dushman Qo'shamiz! (Monster AI Lab)"
    title_ru = "Урок 33: Оживляем Врагов: Умные Монстры в Roguelike"
    title_en = "Lesson 33: Engineering Smart Monster AI for Your Roguelike"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<h1>.*?</h1>',
                 f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>',
                 tpl)

    sec1_html = """
    <p class="lead" style="font-size:12px; margin-bottom:8px;" data-ru="<strong>Миссия Урока:</strong> Оживить врагов в подземелье Roguelike: научить монстров обходить каменные стены по свободным клеткам, реагировать на звуки выстрелов и преследовать героя с фонариком обзора." data-en="<strong>Lesson Mission:</strong> Bring dungeon monsters to life in Roguelike: empower enemies to skirt stone walls via open floor tiles, react to gunshots, and stalk the player via vision lights."><strong>Dars Missiyasi:</strong> Roguelike labirintida tosh devorlarni aylanib o'tib, qahramonni quvuvchi aqlli dushman AI tizimini yaratish: devorga qotib qolmaslik, ko'rish chirog'i va 3 xil kayfiyat (Patrul, Shubhali tovush, Quturgan ta'qib).</p>
    <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="4 Правила Умного Монстра:" data-en="4 Rules of Smart Monster AI:">Aqlli Dushmanning 4 Ta Asosiy Qoidasi:</div>
      <div>1. <strong>Maydon Kataklari:</strong> <span data-ru="Экран делится на проходимый пол (0) и каменные стены (1)" data-en="Screen is partitioned into walkable floor (0) and solid stone (1)">Ekran bo'sh pol (yurish mumkin) va tosh devorlar (to'siq) to'plamiga bo'linadi</span>.</div>
      <div>2. <strong>Suv Oqimi Usuli:</strong> <span data-ru="Враг не пробивает стену, а огибает ее с двух сторон" data-en="Enemy does not tunnel through walls; it circles around them">Dushman oldida tosh bo'lsa to'xtamaydi, balki yon tomondagi bo'sh katak orqali aylanib o'tadi</span>.</div>
      <div>3. <strong>Ko'rish Chirog'i:</strong> <span data-ru="Конус обзора: синий патруль, желтая тревога, красный спринт" data-en="Vision flashlight: blue patrol, yellow alert, red frenzy chase">Chiroq rangi: ko'k (sokin patrul), sariq (shubhali shovqin), qizil (quturgan ta'qib)</span>.</div>
      <div>4. <strong>Hujum va Xavf:</strong> <span data-ru="При касании героя отнимается ровно 1 жизнь (-1 HP) и звучит сигнал" data-en="Touching hero deducts exactly 1 HP and triggers alarm audio">Dushman yetib olganda o'yinchidan -1 Jon kamayadi va signal yangraydi</span>.</div>
    </div>
    """

    sec2_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="Архитектура проверки свободных соседних клеток:" data-en="Neighbor tile collision avoidance architecture:">To'siqlarni aylanib o'tish tekshiruvi mantig'i:</p>
    <pre style="background:var(--surface-2); padding:6px; font-size:11px; border-radius:4px; margin:0;"><code class="language-javascript">// Agar oldinda tosh devor bo'lsa, 4 ta qo'shni katakni tekshiramiz
const dirs = [[0,-1], [0,1], [-1,0], [1,0]]; // Yuqori, Past, Chap, O'ng
let bestTile = null, minDistance = 9999;
for (const [dx, dy] of dirs) {
  const nextX = enemy.col + dx, nextY = enemy.row + dy;
  if (grid[nextY][nextX] === 0) { // Bo'sh pol!
    const dist = Math.abs(hero.col - nextX) + Math.abs(hero.row - nextY);
    if (dist < minDistance) { minDistance = dist; bestTile = {x: nextX, y: nextY}; }
  }
}
if (bestTile) { enemy.col = bestTile.x; enemy.row = bestTile.y; }</code></pre>
    """

    sec3_html = """
    <div style="font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="3 Архетипа Монстров для Игры:" data-en="3 Monster Archetypes for Your Game:">3 Ta Dushman Turi va Xususiyatlari:</div>
      <div>🧟 <strong>Zombi (Klassik):</strong> Tezligi 0.8x, Joni 3 HP. Barcha devorlarni charchamay aylanib keladi. Boshlang'ich daraja.</div>
      <div>🕷️ <strong>Kiber-O'rgimchak:</strong> Tezligi 2.0x, Joni 1 HP. Juda chaqqon, burchaklarni kesib o'tadi. O'ta xavfli!</div>
      <div>👹 <strong>Kiber-Boss:</strong> Tezligi 1.0x, Joni 5 HP. Katta chirog'i bor va qahramonni ko'rsa olov sharlarini otadi!</div>
    </div>
    """

    sec4_html = """
    <div style="display:flex; flex-direction:column; gap:8px; font-size:11px;">
      <div style="border:1px solid var(--rule); border-radius:4px; padding:6px;">
        <div style="font-weight:700; color:var(--accent-ink);" data-ru="Задание 1: Паспорт Монстра" data-en="Task 1: Monster Profile">1-Topshiriq: O'z Dushmaningiz Pasportini To'ldiring</div>
        <p style="margin:2px 0 4px; font-size:8.5pt;" data-ru="Выберите имя, тип, скорость и спец-способность монстра:" data-en="Select name, type, speed, and special power:">Dushmaningiz turi (Zombi/O'rgimchak/Boss), joni (HP), tezligi va ko'rish masofasini yozing:</p>
        <div style="border-bottom:1px dashed #cbd5e1; height:20px;"></div>
      </div>
      <div style="border:1px solid var(--rule); border-radius:4px; padding:6px;">
        <div style="font-weight:700; color:var(--accent-ink);" data-ru="Задание 2: Vibecoding промпт для обхода стен" data-en="Task 2: Wall-Dodging Prompt">2-Topshiriq: Devorni Aylanib O'tish Promptini Yozing</div>
        <p style="margin:2px 0 4px; font-size:8.5pt;" data-ru="Напишите точный промпт для AI, чтобы монстр не застревал:" data-en="Write precision prompt so monster loops around walls:">AI ga dushman devorga urilganda to'xtab qolmasdan bo'sh katakni topishi uchun qanday so'rov berasiz?</p>
        <div style="border-bottom:1px dashed #cbd5e1; height:28px;"></div>
      </div>
    </div>
    """

    sec5_html = """
    <table style="width:100%; border-collapse:collapse; font-size:8pt; text-align:left;">
      <thead>
        <tr style="background:var(--panel-2);">
          <th style="padding:4px; border:1px solid var(--rule);" data-ru="Критерий" data-en="Criteria">Mezon</th>
          <th style="padding:4px; border:1px solid var(--rule); width:60px;" data-ru="Баллы" data-en="Points">Ball</th>
          <th style="padding:4px; border:1px solid var(--rule);" data-ru="Описание" data-en="Description">Izoh</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:600;" data-ru="Обход препятствий" data-en="Wall Dodging">Devorni aylanib o'tish</td>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:700; color:var(--green);" data-ru="4 балла" data-en="4 pts">4 ball</td>
          <td style="padding:4px; border:1px solid var(--rule);" data-ru="Враг обходит каменные стены и не застревает." data-en="Enemy dodges stone obstacles smoothly.">Dushman tosh devorlarga tiqilmaydi va qahramonni quvlaydi.</td>
        </tr>
        <tr>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:600;" data-ru="3 Режима и луч обзора" data-en="3 Modes & Vision Cone">Ko'rish nuri va 3 rejim</td>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:700; color:var(--green);" data-ru="4 балла" data-en="4 pts">4 ball</td>
          <td style="padding:4px; border:1px solid var(--rule);" data-ru="Синий патруль, желтая тревога, красный спринт." data-en="Blue patrol, yellow alert, red frenzy sprint.">Chiroq rangi o'zgaradi: ko'k patrul, sariq shovqin, qizil ta'qib.</td>
        </tr>
        <tr>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:600;" data-ru="Супер-способность" data-en="Special Ability">Maxsus super-kuch</td>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:700; color:var(--green);" data-ru="2 балла" data-en="2 pts">2 ball</td>
          <td style="padding:4px; border:1px solid var(--rule);" data-ru="Огненные шары, рывок или призыв миньонов." data-en="Fireballs, dash leap, or minion spawning.">Olovli o'q otish, oldinga sakrash yoki chaqqon hujum.</td>
        </tr>
      </tbody>
    </table>
    """

    replacements = {
        "{{LESSON_NUM}}": "33",
        "{{TITLE_UZ}}": "O'yiningga Aqlli Yirtqich Dushman Qo'shamiz! (Monster AI Lab)",
        "{{TITLE_RU}}": "Оживляем Врагов: Умные Монстры в Roguelike",
        "{{TITLE_EN}}": "Engineering Smart Monster AI for Your Roguelike",
        "{{COHORT_LABEL_UZ}}": "7–8-SINF",
        "{{COHORT_LABEL_RU}}": "7–8 КЛАСС",
        "{{COHORT_LABEL_EN}}": "GRADES 7–8",
        "{{META_UZ}}": "11-Hafta · Juftlik Dars (80 daqiqa) · Game Dev & Vibecoding Track",
        "{{META_RU}}": "11-я Неделя · Сдвоенный Урок (80 минут) · Направление Game Dev & Vibecoding",
        "{{META_EN}}": "Week 11 · Double Block (80 min) · Game Dev & Vibecoding Track",
        "{{MISSION_UZ}}": "Roguelike labirintida tosh devorlarni aylanib o'tib, qahramonni quvuvchi aqlli dushman AI tizimini yaratish: devorga qotib qolmaslik, ko'rish chirog'i va 3 xil kayfiyat (Patrul, Shubhali tovush, Quturgan ta'qib).",
        "{{MISSION_RU}}": "Оживить врагов в подземелье Roguelike: научить монстров обходить каменные стены по свободным клеткам, реагировать на звуки выстрелов и преследовать героя с фонариком обзора.",
        "{{MISSION_EN}}": "Bring dungeon monsters to life in Roguelike: empower enemies to skirt stone walls via open floor tiles, react to gunshots, and stalk the player via vision lights.",
        "{{SEC1_TITLE_UZ}}": "Aqlli Dushmanning 4 Ta Asosiy Qoidasi",
        "{{SEC1_TITLE_RU}}": "4 Правила Умного Монстра",
        "{{SEC1_TITLE_EN}}": "4 Rules of Smart Monster AI",
        "{{SEC1_CONTENT}}": sec1_html,
        "{{SEC2_TITLE_UZ}}": "To'siqlarni Aylanib O'tish Mantig'i (Suv Oqimi)",
        "{{SEC2_TITLE_RU}}": "Логика Обхода Препятствий (Принцип Воды)",
        "{{SEC2_TITLE_EN}}": "Obstacle Avoidance Logic (Flowing Water)",
        "{{SEC2_CONTENT}}": sec2_html,
        "{{SEC3_TITLE_UZ}}": "3 Ta Dushman Turi va Topshiriqlar",
        "{{SEC3_TITLE_RU}}": "3 Архетипа Монстров и Задания",
        "{{SEC3_TITLE_EN}}": "3 Monster Archetypes & Tasks",
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

    task1 = """
    <div style="margin-bottom:12px;">
      <h4 data-ru="Задание 1: Промпт для 3 Режимов Монстра" data-en="Task 1: Prompt for 3 Monster States">1-Topshiriq: Dushmanga 3 Ta Rejim Berish So'rovi</h4>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите полный текст промпта для ИИ, чтобы запрограммировать 3 состояния монстра (Патруль, Тревога, Погоня):" data-en="Write a full prompt to ask AI for 3 monster states (Patrol, Alert, Chase):">AI ga dushmaningiz uchun 3 xil kayfiyat (Sokin patrul, Shubhali qidiruv, Quturgan ta'qib) kodini yozib berishi uchun to'liq so'rov matnini yozing:</p>
      <textarea id="hw-t1" class="hw-input" style="width:100%; height:75px; font-family:var(--font-mono); font-size:12px;" placeholder="AI ga yoziladigan prompt..." data-placeholder-ru="Промпт для отправки в ИИ..." data-placeholder-en="Prompt to send to AI..."></textarea>
      <button class="btn" style="margin-top:6px; padding:4px 10px; font-size:11px;" onclick="document.getElementById('sol-t1').style.display='block';" data-ru="💡 Показать Решение" data-en="💡 View Solution">💡 Yechimni Ko'rish</button>
      <div id="sol-t1" style="display:none; margin-top:6px; padding:8px; background:var(--panel-2); border-radius:4px; font-size:11px; font-family:var(--font-mono); color:var(--green);">
        // Oltin Prompt:<br>
        "Mening Canvas dushmanimga 3 ta state qo'sh: PATROL (1x tezlik, moviy chiroq), ALERT (shovqin chiqqanda sariq chiroq bilan to'xtash) va CHASE (o'yinchini ko'rganda qizil chiroq bilan 1.8x tezlikda quvish)."
      </div>
    </div>
    """

    task2 = """
    <div style="margin-bottom:12px;">
      <h4 data-ru="Задание 2: Логика Обхода Стен" data-en="Task 2: Obstacle Avoidance Logic">2-Topshiriq: Devorni Aylanib O'tish Mantig'i</h4>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Если перед монстром каменная стена, какие соседние клетки он должен проверить, чтобы не застрять?" data-en="If a wall blocks the monster, which neighbor tiles must it check to navigate around?">Agar dushman oldida tosh devor tursa, u to'xtab qolmasligi uchun qaysi kataklarni tekshirishi kerak?</p>
      <textarea id="hw-t2" class="hw-input" style="width:100%; height:65px; font-family:var(--font-mono); font-size:12px;" placeholder="Javobingizni yozing..." data-placeholder-ru="Напишите ваш ответ..." data-placeholder-en="Write your answer..."></textarea>
      <button class="btn" style="margin-top:6px; padding:4px 10px; font-size:11px;" onclick="document.getElementById('sol-t2').style.display='block';" data-ru="💡 Показать Решение" data-en="💡 View Solution">💡 Yechimni Ko'rish</button>
      <div id="sol-t2" style="display:none; margin-top:6px; padding:8px; background:var(--panel-2); border-radius:4px; font-size:11px; font-family:var(--font-mono); color:var(--green);">
        // To'g'ri Javob:<br>
        Dushman 4 ta qo'shni katakni (Yuqori, Past, Chap, O'ng) tekshiradi. To'siqsiz (bo'sh pol) bo'lgan va qahramonga masofasi eng yaqin bo'lgan katakni tanlab o'sha tomonga buriladi.
      </div>
    </div>
    """

    task3 = """
    <div style="margin-bottom:12px;">
      <h4 data-ru="Задание 3: Конус Зрения и Сигнал Тревоги" data-en="Task 3: Vision Cone & Alarm Audio">3-Topshiriq: Ko'rish Chirog'i va Signal Tovushi</h4>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Qahramon dushmanning nuri ichiga tushganda Web Audio API yordamida qanday ogohlantirish tovushi chalish mumkin?" data-en="How can Web Audio API play an alert sound when hero enters monster's flashlight?">Qahramon dushmanning nuri ichiga tushganda Web Audio API yordamida qanday ogohlantirish tovushi chalish mumkin?</p>
      <textarea id="hw-t3" class="hw-input" style="width:100%; height:65px; font-family:var(--font-mono); font-size:12px;" placeholder="Audio so'rovi yoki javob..." data-placeholder-ru="Запрос на аудио или ответ..." data-placeholder-en="Audio prompt or answer..."></textarea>
      <button class="btn" style="margin-top:6px; padding:4px 10px; font-size:11px;" onclick="document.getElementById('sol-t3').style.display='block';" data-ru="💡 Показать Решение" data-en="💡 View Solution">💡 Yechimni Ko'rish</button>
      <div id="sol-t3" style="display:none; margin-top:6px; padding:8px; background:var(--panel-2); border-radius:4px; font-size:11px; font-family:var(--font-mono); color:var(--green);">
        // Audio Prompt:<br>
        "Qahramon ko'rish nuriga tushganda AudioContext orqali 600Hz dan 900Hz ga ko'tariluvchi 0.15 soniyalik qisqa ogohlantirish beep signalini chal."
      </div>
    </div>
    """

    task4 = """
    <div style="margin-bottom:12px;">
      <h4 data-ru="Задание 4: Уникальная Супер-Способность Босса" data-en="Task 4: Custom Boss Super-Power">4-Topshiriq: Dushmanga Shaxsiy Super-Qobiliyat</h4>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="O'zingiz xohlagan bitta super-qobiliyat (olov otish, sakrash, kichik bolalarini chaqirish) g'oyasini va AI ga so'rovini yozing:" data-en="Describe your custom monster skill (fireballs, jump dash, summoning minions) and prompt:">O'zingiz xohlagan bitta super-qobiliyat (olov otish, sakrash, kichik bolalarini chaqirish) g'oyasini va AI ga so'rovini yozing:</p>
      <textarea id="hw-t4" class="hw-input" style="width:100%; height:65px; font-family:var(--font-mono); font-size:12px;" placeholder="Super-qobiliyat prompti..." data-placeholder-ru="Промпт суперспособности..." data-placeholder-en="Super-power prompt..."></textarea>
      <button class="btn" style="margin-top:6px; padding:4px 10px; font-size:11px;" onclick="document.getElementById('sol-t4').style.display='block';" data-ru="💡 Показать Решение" data-en="💡 View Solution">💡 Yechimni Ko'rish</button>
      <div id="sol-t4" style="display:none; margin-top:6px; padding:8px; background:var(--panel-2); border-radius:4px; font-size:11px; font-family:var(--font-mono); color:var(--green);">
        // Misol Prompt:<br>
        "Har 5 soniyada dushman 1 soniya to'xtab qichqirsin va qahramon tomonga 3 ta kichik olov shari otsin!"
      </div>
    </div>
    """

    tasks_html = task1 + task2 + task3 + task4

    replacements = {
        "{{TITLE_UZ}}": "33-dars: O'yiningga Aqlli Yirtqich Dushman Qo'shamiz! (Monster AI Lab)",
        "{{TITLE_RU}}": "Урок 33: Оживляем Врагов: Умные Монстры в Roguelike",
        "{{TITLE_EN}}": "Lesson 33: Engineering Smart Monster AI for Your Roguelike",
        "{{COHORT_LABEL_UZ}}": "7–8-SINF",
        "{{HERO_TAG_UZ}}": "11-Hafta · Game Dev & Vibecoding Track",
        "{{HERO_DESC_UZ}}": "Uyingizda mustaqil ravishda o'yin dushmani uchun devorlarni aylanib o'tish, ko'rish nuri va super-kuchlarni AI yordamida dasturlang.",
        "{{HERO_DESC_RU}}": "Самостоятельно запрограммируйте обход стен, фонарик обзора и супер-способности монстра через Vibecoding.",
        "{{HERO_DESC_EN}}": "Practice engineering obstacle navigation, flashlight vision cones, and special boss skills via Vibecoding prompts.",
        "{{RUBRIC_T1_UZ}}": "1-Bosqich: Baza (Devorni aylanib o'tish va quvish)",
        "{{RUBRIC_T1_RU}}": "1-й Уровень: База (Обход препятствий и погоня)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (Obstacle avoidance and chasing)",
        "{{RUBRIC_T2_UZ}}": "2-Bosqich: Muhandis (3 xil holat va ko'rish nuri)",
        "{{RUBRIC_T2_RU}}": "2-й Уровень: Практика (3 состояния и фонарик обзора)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (3 predator states & flashlight cone)",
        "{{RUBRIC_T3_UZ}}": "3-Bosqich: Kiber-Chaqiruv (Shaxsiy super-qobiliyat va ovoz)",
        "{{RUBRIC_T3_RU}}": "3-й Уровень: Вызов (Уникальная суперспособность и аудио)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (Custom boss skill & Web Audio alert)",
        "{{TASKS_HTML}}": tasks_html,
        "{{LESSON_SLUG}}": "7-8-w11-l33-dushman-ai-va-pathfinding"
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")


def build_teacher_guide():
    guide_md = """# O'qituvchi Qo'llanmasi: 33-Dars — O'yiningga Aqlli Yirtqich Dushman Qo'shamiz!

**Sinf:** 7–8-sinf · **Format:** 80 daqiqalik Juftlik Dars · **Yo'nalish:** Vibecoding & Game Dev

---

## 🎯 Asosiy Pedagogik Konseptsiya (QAT'IY QOIDA)
🛑 **O'quvchilarga quruq matematika va universitet algoritmlarini tushuntirish TAQIQLANADI!**
Hech qanday $f(n) = g(n) + h(n)$ formulalari yoki navbat massivlari bilan boshlarini qotirmang.
Ular 7–8-sinf o'quvchilari! Ularning maqsadi — **o'z o'yinlariga devorga tiqilmaydigan, o'yinchini quvuvchi aqlli monstr yasash!**

Darsning barcha nazariyasi qiziqarli geym-dizayn misollari bilan tushuntiriladi:
- "Suv toshni teshib o'tmaydi, balki ikki yonidan aylanib o'tadi — dushman ham shunday bo'lishi kerak!"
- "Dushmanning 3 ta kayfiyati: Sokin patrul (ko'k chiroq) -> Shubhali tovush (sariq chiroq) -> Quturgan ta'qib (qizil chiroq)!"

---

## ⏱️ 80 Daqiqalik Dars Vaqti Taqsimoti

| Vaqt | Bosqich | O'qituvchi Harakati va Faoliyat |
|---|---|---|
| **00:00–08:00** | **HW Review & Ko'prik** | 32-dars otishmasini eslash: cheksiz o'qlar xotirani to'ldirib o'yinni qotirishi. Blitz savol: "Endi kimga o't ochamiz? Albatta labirintdagi dushmanga!" |
| **08:00–20:00** | **Geym-Dizayn Tushunchalari** | Sodda dushman nega devorga kallasini urib qotib qolishini kulgili qilib ko'rsatish. Kataklar to'ri va suv oqimi usuli. 3 xil kayfiyat va ko'rish chirog'i. |
| **20:00–30:00** | **Smartboard Interaktiv Sinovi** | 8-slaydni ochish: doskaga o'quvchilarni chaqirib tosh devorlar chizdirish va qahramon bilan dushmandan qochish sinovi. |
| **30:00–35:00** | **Geymer Viktorinasi** | 3 ta tezkor savol orqali tushunchalarni mustahkamlash. |
| **35:00–65:00** | **30 Minutlik Katta Vibecoding Arena** | O'quvchilar kompyuterlarida o'tirib, 4 ta tayyor prompt kartasi orqali o'z o'yinlariga dushmanni kiritishadi. O'qituvchi zaldan aylanib tiqilib qolganlarga yordam beradi. |
| **65:00–74:00** | **Partadosh Duelosy (Playtest)** | Partadoshlar joyini almashtirib, bir-birining dushmanidan omon qolishga harakat qilishadi. Baglar (devorga tiqilish) aniqlanib tuzatiladi. |
| **74:00–77:00** | **Katta Ekran Showcasi** | 2 ta eng chiroyli va qiziqarli dushman yaratgan o'quvchi o'yinini katta doskada namoyish qiladi. |
| **77:00–80:00** | **Uy Vazifasi va Yakun** | 10 ballik uy vazifasi tushuntiriladi. Keyingi dars xazinalar va qurollar (Loot & Inventory) anons qilinadi. |
"""

    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(guide_md)
    print("  ✓ Created: TEACHER_READING.md")


if __name__ == "__main__":
    print("🚀 Building 7–8th Grade Week 11 Lesson 33 (Practical Game Dev Track)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_guide()
    print("✅ All Lesson 33 files successfully compiled!")
