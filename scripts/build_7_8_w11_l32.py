#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_7_8_w11_l32.py — Builder for 7–8th Grade, Week 11, Lesson 32

Mavzu: O'yin Fizikasi va Otishma Mexanikasi: Trigonometriya, Traektoriya va Zarrachalar
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 7-8-sinf (Game Dev & Creative Coding Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "7-8-sinf", "11-hafta", "32-dars-otishma-mexanikasi-va-trigonometriya")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "simulator"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides for 80-min Double Block)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="7–8-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 32" data-en="GRADES 7–8 · WEEK 11 · LESSON 32">7–8-SINF · 11-HAFTA · 32-DARS</span></div>
    <h1 class="display" data-ru="Физика Игры и Механика Стрельбы: Тригонометрия, Траектории и Частицы" data-en="Game Physics & Ballistics: Trigonometry, Trajectories & Particles">O'yin Fizikasi va Otishma Mexanikasi: Trigonometriya va Traektoriya</h1>
    <p class="lede" data-ru="Как заставить пули лететь точно в курсор: формула Math.atan2, разложение скорости на векторы cos/sin, очистка памяти от улетевших снарядов и система искрящихся частиц при попадании." data-en="How to launch projectiles towards the crosshair: Math.atan2 targeting, velocity vector decomposition via cos/sin, memory cleanup for dead bullets, and particle spark systems.">O'qlarni sichqoncha nishoniga qarab to'g'ri uchirish siri: Math.atan2 formulasi, tezlikni cos/sin vektorlariga ajratish, xotirani tozalash va to'qnashuvdagi uchqunlar tizimi.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Баллистика и Векторы" data-en="Ballistics & Vectors">Ballistika va Vektorlar</h3>
        <p data-ru="От угла поворота курсора к плавным физическим траекториям полета снарядов на 60 FPS." data-en="Translating raw cursor angles into fluid 60 FPS physical projectile trajectories.">Kursor burchagidan 60 FPS chastotada ravon uchuvchi lazer o'qlari fizikasi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Shooting Engine</div>
        <h3 data-ru="Боевой Модуль" data-en="Combat Module">Jangovar Dvigatel</h3>
        <p data-ru="Каждый ученик встроит в свой Roguelike модуль прицельной стрельбы с рикошетом и искрами." data-en="Each student integrates a complete aiming and shooting engine with wall impacts and spark FX.">Har bir o'quvchi o'z o'yiniga nishonga olib otish, devorga urilish va uchqunlar modulini qo'shadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 31-УРОКА" data-en="LESSON 31 HOMEWORK REVIEW">31-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Процедурный Мир: Ловушка Выхода за Границы и Изолированных Комнат" data-en="Procedural Worlds: Array Out-of-Bounds & Isolated Dungeon Traps">Procedural Dunyo: Massivdan Chiqib Ketish va Qamalgan Xonalar</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Типичная ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h4 data-ru="Случайный блуждатель (Random Walker) пробил внешнюю стену" data-en="Random Walker carved through perimeter boundary walls">Random Walker xarita devorlarini teshib yuborishi</h4>
        <p style="font-size:12px;" data-ru="Ученики не ограничили координаты конкопателя: x += dx; y += dy без проверки границ. В результате код попытался прочитать grid[-1][5] и выбросил Uncaught TypeError: Cannot set properties of undefined." data-en="Students omitted boundary clamping: x += dx; y += dy without guards. Walker accessed grid[-1][5], triggering 'Cannot set properties of undefined' crashes.">Konchi koordinatalari chegaralanmagani sababli u 0 dan kichik yoki xaritadan katta indekslarga o'tib ketgan va grid[-1][5] chaqirilib brauzer qulagan.</p>
        <pre><code class="language-js">// ❌ Xato: Chegaralar tekshiruvi yo'q
x += dx; y += dy;
grid[y][x] = 0; // x=-1 bo'lganda TypeError!</code></pre>
      </div>
      <div class="box" style="border:1px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой стандарт (Golden Solution)" data-en="Golden Standard">Oltin Standart Yechim</div>
        <h4 data-ru="Math.max / Math.min (Clamping) + Буфер 1 тайла стен" data-en="Math.max / Math.min Clamping + 1-Tile Wall Margin">Clamping Chegarasi + 1 Qavatli Tosh Devor</h4>
        <p style="font-size:12px;" data-ru="Координаты жестко зажимаются в диапазоне [1, COLS-2] и [1, ROWS-2]. Периметр всегда остается непробиваемой каменной стеной (тайл 1)." data-en="Coordinates are strictly clamped between [1, COLS-2] and [1, ROWS-2]. The outer perimeter remains an impenetrable barrier (tile 1).">Konchi koordinatalari [1, COLS-2] oralig'ida qat'iy cheklanadi. Tashqi devorlar doim 100% buzilmas tosh bo'lib qoladi.</p>
        <pre><code class="language-js">// ✅ To'g'ri: Clamping bilan chegaralash
nx = Math.max(1, Math.min(COLS - 2, x + dx));
ny = Math.max(1, Math.min(ROWS - 2, y + dy));
grid[ny][nx] = 0;</code></pre>
      </div>
    </div>
    <div class="box" style="margin-top:12px; background:var(--surface-2);">
      <div style="font-size:12px; font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="⚡ Блиц-Вопрос и Мост к Теме:" data-en="⚡ Blitz Question & Lesson Bridge:">⚡ Blitz Savol va Bugungi Mavzuga Ko'prik:</div>
      <p style="font-size:12px; margin:0;" data-ru="<strong>Вопрос:</strong> Если пуля летит в направлении курсора, как определить угол ее полета на 2D-плоскости? <em>(Ответ: Функция Math.atan2(dy, dx))</em>.<br><strong>Мост:</strong> Сегодня мы научим нашего героя целиться в любую точку экрана и запускать лазерные снаряды с помощью тригонометрии!" data-en="<strong>Question:</strong> When shooting towards the cursor on a 2D plane, how do we determine the flight angle? <em>(Answer: The Math.atan2(dy, dx) function)</em>.<br><strong>Bridge:</strong> Today we equip our dungeon explorer with a trigonometric aiming and shooting engine featuring realistic ballistics and impact sparks!"><strong>Savol:</strong> O'q sichqoncha kursoriga qarab uchishi uchun 2D tekislikda uning uchish burchagini qanday topamiz? <em>(Javob: Math.atan2(dy, dx) funksiyasi orqali)</em>.<br><strong>Ko'prik:</strong> Bugun biz labirint qahramonimizga sichqoncha yoki sensorli ekranga qarab o't ochuvchi va devorlarga urilganda uchqun sochuvchi ballistika fizikasini o'rgatamiz!</p>
    </div>
  </section>

  <!-- SLIDE 3: AIMING ARCHITECTURE -->
  <section class="slide" data-phase="Nishonga Olish|Архитектура Прицеливания|Aiming Architecture" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="АРХИТЕКТУРА СТРЕЛЬБЫ" data-en="SHOOTING ARCHITECTURE">OTISHMA ARXITEKTURASI</span></div>
    <h2 data-ru="От Курсора Мыши к Снаряду: 4 Шага Баллистики" data-en="From Mouse Cursor to Bullet: 4 Steps of Ballistics">Sichqoncha Kursoridan O'qqacha: 4 Bosqich</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="В играх пуля не появляется случайно. Это математический процесс, преобразующий координаты экрана в вектор движения." data-en="Bullets never spawn haphazardly in games. They follow a mathematical pipeline turning cursor screen coordinates into velocity vectors.">O'yinlarda o'q tasodifan uchmaydi. Bu kursor koordinatalarini aniq harakat vektoriga aylantiruvchi matematik zanjirdir.</p>
        <ul class="clean-list">
          <li data-ru="<strong>1. Захват Цели (Targeting):</strong> Получение координат мыши (mouseX, mouseY) при событии mousemove." data-en="<strong>1. Targeting:</strong> Capturing mouse coordinates (mouseX, mouseY) on canvas movement events."><strong>1. Nishonni aniqlash:</strong> Sichqoncha yoki barmoq bosilgan nuqta (targetX, targetY).</li>
          <li data-ru="<strong>2. Расчет Дельты (Delta X & Y):</strong> Разность dx = targetX - heroX и dy = targetY - heroY." data-en="<strong>2. Delta Calculation:</strong> Distance offsets dx = targetX - heroX and dy = targetY - heroY."><strong>2. Masofa farqi:</strong> dx = targetX - heroX va dy = targetY - heroY hisoblanadi.</li>
          <li data-ru="<strong>3. Угол через Артангенс:</strong> Вычисление точного угла angle = Math.atan2(dy, dx)." data-en="<strong>3. Arctangent Angle:</strong> Computing the precise angle via angle = Math.atan2(dy, dx)."><strong>3. Burchakni topish:</strong> angle = Math.atan2(dy, dx) orqali burchak topiladi.</li>
          <li data-ru="<strong>4. Разложение на Векторы:</strong> vx = cos(angle) * speed и vy = sin(angle) * speed." data-en="<strong>4. Vector Split:</strong> vx = cos(angle) * speed and vy = sin(angle) * speed."><strong>4. Tezlik vektorlari:</strong> vx = Math.cos(angle) * spd va vy = Math.sin(angle) * spd.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; gap:8px;">
        <div style="font-size:32px;">🎯 ➔ 📐 ➔ 🚀 ➔ 💥</div>
        <div style="font-weight:700; color:var(--accent); font-size:13px;" data-ru="Пайплайн Выстрела" data-en="Ballistics Pipeline">Otishma Zanjiri</div>
        <div style="font-size:11px; color:var(--ink-2); line-height:1.5;" data-ru="Клик мыши ➔ Расчет dx/dy ➔ Math.atan2 ➔ Векторы cos/sin ➔ Полет на 60 FPS" data-en="Mouse Click ➔ dx/dy delta ➔ Math.atan2 ➔ cos/sin vectors ➔ 60 FPS Projectile Update">Kursor bosilishi ➔ dx/dy ➔ Math.atan2 ➔ cos/sin vektorlari ➔ 60 FPS ravon parvoz!</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: MATH.ATAN2 -->
  <section class="slide" data-phase="Math.atan2|Функция Math.atan2|Math.atan2" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="МАТЕМАТИКА ПРИЦЕЛИВАНИЯ" data-en="TARGETING MATHEMATICS">MATH.ATAN2 SEHRI</span></div>
    <h2 data-ru="Почему Math.atan2(dy, dx), а не Обычный atan(dy/dx)?" data-en="Why Math.atan2(dy, dx) Instead of Regular atan(dy/dx)?">Nega Oddiy atan Emas, Aynan Math.atan2(dy, dx)?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Классическая формула atan(dy/dx) ломается при делении на ноль (когда dx=0) и не различает квадранты (лево/право, верх/низ)." data-en="Standard atan(dy/dx) breaks on zero divisions (dx=0) and confuses quadrants. Math.atan2 handles full 360-degree rotations safely.">Oddiy atan(dy/dx) da dx=0 bo'lsa nolga bo'lish xatosi chiqadi va burchak adashadi. Math.atan2 esa barcha 360 darajani aniq hisoblaydi.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Все 4 квадранта (Full Circle):</strong> Возвращает угол в радианах от -PI до +PI (-180° до +180°)." data-en="<strong>All 4 Quadrants:</strong> Returns radians between -PI and +PI (-180° to +180°)."><strong>Barcha 4 chorak:</strong> Burchakni -PI dan +PI gacha (-180° dan +180° gacha) aniq beradi.</li>
          <li data-ru="<strong>Порядок аргументов:</strong> Сначала DY, затем DX! Запомнить: <code>Math.atan2(y, x)</code>." data-en="<strong>Argument Order:</strong> DY comes first, then DX! Memorize: <code>Math.atan2(y, x)</code>."><strong>Argumentlar tartibi:</strong> Avval Y, keyin X beriladi: <code>Math.atan2(dy, dx)</code>.</li>
          <li data-ru="<strong>Ноль деления исключен:</strong> При dx=0 функция безопасно возвращает PI/2 (90°)." data-en="<strong>Zero Division Safe:</strong> When dx=0, safely yields PI/2 (90°) without errors."><strong>Nolga bo'linmaydi:</strong> dx=0 bo'lsa, xatosiz 90 daraja (PI/2) qiymatini qaytaradi.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:12px; line-height:1.6;">
        <div style="color:var(--accent); font-weight:700; margin-bottom:6px;">[Burchakni Hisoblash Kodi]</div>
        <pre><code class="language-js">function getAimAngle(hero, target) {
  const dx = target.x - hero.x;
  const dy = target.y - hero.y;
  
  // Radiandagi burchak (-3.14 .. +3.14)
  const angle = Math.atan2(dy, dx);
  return angle;
}</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: VELOCITY VECTORS -->
  <section class="slide" data-phase="Vektorlar|Векторы Скорости|Velocity Vectors" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="РАЗЛОЖЕНИЕ НА ВЕКТОРЫ" data-en="VECTOR DECOMPOSITION">TEZLIK VEKTORLARI</span></div>
    <h2 data-ru="Траектория Полета: Math.cos и Math.sin" data-en="Flight Trajectory: Math.cos & Math.sin">Uchish Traektoriyasi: Math.cos va Math.sin</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Каждый кадр пуля должна смещаться по оси X и Y так, чтобы ее итоговая скорость оставалась постоянной, независимо от направления." data-en="Each frame, the bullet increments along X and Y so that total linear speed remains constant in every direction.">O'q qaysi tomonga otilmasin, uning umumiy tezligi doim bir xil (masalan: 10 px/kadr) bo'lishi shart!</p>
        <ul class="clean-list">
          <li data-ru="<strong>Горизонтальная скорость:</strong> <code>vx = Math.cos(angle) * speed</code>" data-en="<strong>Horizontal Velocity:</strong> <code>vx = Math.cos(angle) * speed</code>"><strong>Gorizontal tezlik:</strong> <code>vx = Math.cos(angle) * speed</code></li>
          <li data-ru="<strong>Вертикальная скорость:</strong> <code>vy = Math.sin(angle) * speed</code>" data-en="<strong>Vertical Velocity:</strong> <code>vy = Math.sin(angle) * speed</code>"><strong>Vertikal tezlik:</strong> <code>vy = Math.sin(angle) * speed</code></li>
          <li data-ru="<strong>Теорема Пифагора:</strong> <code>vx² + vy² = speed²</code> (Скорость всегда стабильна!)." data-en="<strong>Pythagorean Invariance:</strong> <code>vx² + vy² = speed²</code> (Uniform velocity)."><strong>Pifagor qoidasi:</strong> <code>vx² + vy² = speed²</code> (Tezlik o'zgarmas saqlanadi).</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:12px; line-height:1.6;">
        <div style="color:var(--green); font-weight:700; margin-bottom:6px;">[O'q Yaratish Funksiyasi]</div>
        <pre><code class="language-js">function shootBullet(hero, target) {
  const angle = Math.atan2(target.y - hero.y, target.x - hero.x);
  const speed = 12; // px per frame
  
  bullets.push({
    x: hero.x,
    y: hero.y,
    vx: Math.cos(angle) * speed,
    vy: Math.sin(angle) * speed,
    life: 60 // 60 kadr umr
  });
}</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: MEMORY CLEANUP -->
  <section class="slide" data-phase="Xotirani Tozalash|Очистка Памяти|Memory Cleanup" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="УПРАВЛЕНИЕ ПАМЯТЬЮ" data-en="MEMORY MANAGEMENT">XOTIRANI TOZALASH</span></div>
    <h2 data-ru="Ловушка Утечки Памяти: Почему Нельзя Забывать Снаряды?" data-en="Memory Leak Trap: Why Dead Bullets Must Be Purged?">Xotira Oqishi (Memory Leak): O'qlarni O'chirish Shart!</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Если игрок сделает 500 выстрелов, а пули улетят за пределы экрана и останутся в массиве, браузер начнет лагать и сбросит FPS до нуля." data-en="If a player fires 500 shots and off-screen bullets linger in memory arrays, the browser will lag and collapse frame rates to zero.">Agar o'yinchi 500 marta o'q uzsa va ekrandan chiqib ketgan o'qlar massivdan o'chirilmasa, o'yin qotib qoladi (Memory Leak).</p>
        <ul class="clean-list">
          <li data-ru="<strong>Удаление с конца (Reverse Loop):</strong> Итерируемся с i = bullets.length - 1 до 0." data-en="<strong>Reverse Iteration:</strong> Loop from i = bullets.length - 1 down to 0 to safely splice."><strong>Orqadan aylanish:</strong> O'chirishda massiv indekslari surilmasligi uchun teskari sikl ishlatiladi.</li>
          <li data-ru="<strong>Удар о Стену:</strong> Если тайл стены равен 1, о'q zudlik bilan yo'q qilinadi." data-en="<strong>Wall Collision:</strong> If bullet hits tile 1, it splices and spawns sparks."><strong>Devorga urilish:</strong> Agar o'q tosh devorga tegsa, zudlik bilan o'chiriladi.</li>
          <li data-ru="<strong>Выход за Экран:</strong> x &lt; 0 || x &gt; width bo'lsa o'chirish." data-en="<strong>Out-of-Bounds:</strong> If bullet exits viewport bounds, purge immediately."><strong>Ekranni tark etish:</strong> Ko'rinish chegarasidan chiqsa massivdan chiqariladi.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:11px; line-height:1.6;">
        <div style="color:var(--red); font-weight:700; margin-bottom:6px;">[Xavfsiz O'chirish Sikli]</div>
        <pre><code class="language-js">for (let i = bullets.length - 1; i >= 0; i--) {
  const b = bullets[i];
  b.x += b.vx;
  b.y += b.vy;
  b.life--;

  // Devor to'qnashuvi yoki vaqt tugashi
  if (b.life <= 0 || isWall(b.x, b.y)) {
    createSparks(b.x, b.y); // Uchqunlar
    bullets.splice(i, 1);   // Xotiradan tozalash
  }
}</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: PARTICLE SPARKS -->
  <section class="slide" data-phase="Zarrachalar|Система Частиц|Particle Sparks" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ВИЗУАЛЬНЫЕ ЭФФЕКТЫ" data-en="VISUAL EFFECTS">ZARRACHALAR TIZIMI</span></div>
    <h2 data-ru="Эффект Попадания: Генерация Искр и Плавное Затухание" data-en="Impact Effects: Particle Sparks & Alpha Fading">Zarba Uchqunlari: Zarrachalar Tizimi va So'nish</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);">1. Tarqalish</div>
        <h4 data-ru="Случайный Вектор" data-en="Random Scatter">Tasodifiy Burchak</h4>
        <p style="font-size:12px;" data-ru="При ударе о стену создается 10–15 частиц со случайным углом от 0 до 2*PI и разной скоростью." data-en="Impact spawns 10-15 particles radiating in random directions with varied speeds.">O'q urilganda 10-15 ta kichik zarracha tasodifiy burchaklar bo'ylab sochilib ketadi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(245,158,11,0.15); color:var(--yellow);">2. Sekinlashuv</div>
        <h4 data-ru="Трение (Friction)" data-en="Friction Decel">Ishqalanish Kuchi</h4>
        <p style="font-size:12px;" data-ru="Каждый кадр скорость частицы умножается на 0.92, создавая эффект сопротивления воздуха." data-en="Each frame, particle velocity is multiplied by 0.92 to simulate air drag.">Zarracha tezligi har kadrda 0.92 ga ko'paytirilib, havoda sekinlashadi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">3. So'nish</div>
        <h4 data-ru="Прозрачность (Alpha)" data-en="Alpha Fadeout">Shaffoflik So'nishi</h4>
        <p style="font-size:12px;" data-ru="Альфа-канал частицы падает с 1.0 до 0. Когда alpha &lt;= 0, частица удаляется из памяти." data-en="Particle alpha fades from 1.0 down to 0, purging from arrays when invisible.">Zarracha shaffofligi (alpha) pasayib boradi va 0 bo'lganda o'chiriladi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: IN-DECK INTERACTIVE SIMULATOR -->
  <section class="slide" data-phase="Smartboard Simulyatori|Интерактив на Доске|In-Deck Simulator" data-time="40:00–48:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="СИМУЛЯТОР НА СМАРТБОРДЕ" data-en="SMARTBOARD BALLISTICS">JONLI OTISHMA ARENASI</span></div>
    <h2 data-ru="Протестируйте Баллистику Прямо на Доске!" data-en="Test Ballistics & Projectiles Right on the Board!">Taqdimot Ichidagi Ballistika Dvigatelini Sinab Ko'ring!</h2>
    <div style="display:grid; grid-template-columns: 1fr 280px; gap:14px; align-items:start;">
      <div style="background:#020617; border-radius:8px; border:2px solid var(--accent); position:relative; overflow:hidden; height:250px;" id="deckBallisticsWrapper">
        <canvas id="deckBallisticsCanvas" width="460" height="250" style="display:block; width:100%; height:100%; cursor:crosshair;"></canvas>
      </div>
      <div class="box" style="display:flex; flex-direction:column; gap:8px;">
        <div style="display:flex; justify-content:space-between; font-weight:700; font-size:12px;">
          <span>🚀 O'qlar: <strong id="deckBulletCount" style="color:var(--accent);">0</strong></span>
          <span>💥 Zarrachalar: <strong id="deckSparkCount" style="color:var(--yellow);">0</strong></span>
        </div>
        <div style="font-size:11px; color:var(--ink-2); line-height:1.4;">
          <strong>Boshqaruv:</strong> Maydonga bosing yoki barmog'ingiz bilan teging — qahramon o'sha nuqtaga qarab lazer uzadi!
        </div>
        <button class="btn" onclick="deckTriggerBurst()" style="font-size:11px; background:var(--green); color:#fff; font-weight:700;" data-ru="💥 360° Салют Снарядов" data-en="💥 360° Projectile Burst">💥 360° Salьyut O'qlari</button>
        <button class="btn" onclick="deckClearArena()" style="font-size:11px; background:var(--surface-2); border:1px solid var(--hair);" data-ru="🔄 Очистить Поле" data-en="🔄 Clear Canvas">🔄 Maydonni Tozalash</button>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: INTERACTIVE QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Quiz" data-time="48:00–55:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА ЗНАНИЙ" data-en="KNOWLEDGE CHECK">KIBER-VIKTORINA</span></div>
    <h2 data-ru="3 Вопроса по Тригонометрии и Физике Снарядов" data-en="3 Questions on Trigonometry & Projectiles">Otishma Fizikasi Bo'yicha 3 Ta Tezkor Savol</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:var(--accent); color:#fff;">1-Savol</div>
        <p style="font-size:12px; margin-bottom:10px;" data-ru="Какая функция вычисляет точный угол между героем и курсором в радианах?" data-en="Which function calculates the exact radian angle between hero and cursor?">Qahramon va kursor orasidagi burchakni qaysi funksiya topadi?</p>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! Math.atan2(dy, dx) barcha 4 chorak burchaklarini hisoblaydi.')" style="font-size:11px;" data-ru="A) Math.atan2(dy, dx)" data-en="A) Math.atan2(dy, dx)">A) Math.atan2(dy, dx)</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri. Math.sin faqat vertikal proeksiyani beradi.')" style="font-size:11px;" data-ru="B) Math.sin(dy / dx)" data-en="B) Math.sin(dy / dx)">B) Math.sin(dy / dx)</button>
        </div>
      </div>
      <div class="box">
        <div class="tag" style="background:var(--purple); color:#fff;">2-Savol</div>
        <p style="font-size:12px; margin-bottom:10px;" data-ru="Как рассчитать смещение пули по оси X при известном угле angle и скорости speed?" data-en="How to compute horizontal velocity vx given angle and speed?">Burchak va tezlik ma'lum bo'lsa, X o'qi bo'yicha tezlik qanday topiladi?</p>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! X o‘qi uchun Math.cos, Y o‘qi uchun Math.sin ishlatiladi.')" style="font-size:11px;" data-ru="A) vx = Math.cos(angle) * speed" data-en="A) vx = Math.cos(angle) * speed">A) vx = Math.cos(angle) * speed</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri. Tan burchak nisbati, vektor emas.')" style="font-size:11px;" data-ru="B) vx = Math.tan(angle) * speed" data-en="B) vx = Math.tan(angle) * speed">B) vx = Math.tan(angle) * speed</button>
        </div>
      </div>
      <div class="box">
        <div class="tag" style="background:var(--green); color:#fff;">3-Savol</div>
        <p style="font-size:12px; margin-bottom:10px;" data-ru="Почему удаление снарядов из массива bullets нужно делать с конца (от length-1 к 0)?" data-en="Why must array splicing be conducted in reverse (from length-1 down to 0)?">Nega o'qlarni massivdan o'chirish teskari tartibda bajarilishi shart?</p>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! Boshidan o‘chirilganda indekslar surilib, ba‘zi o‘qlar o‘chmay qoladi.')" style="font-size:11px;" data-ru="A) Чтобы не сбивались индексы массива" data-en="A) Prevents index shifting bugs">A) Indekslar surilib ketmasligi uchun</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri. Teskari sikl kompyuterni sekinlashtirmaydi.')" style="font-size:11px;" data-ru="B) Чтобы замедлить полет пуль" data-en="B) To slow down bullet speed">B) O'qlar sekinroq uchishi uchun</button>
        </div>
      </div>
    </div>
    <div id="quizFeedback" style="margin-top:10px; font-weight:700; font-size:12px; min-height:18px;"></div>
  </section>

  <!-- SLIDE 10: 25-MIN ARENA -->
  <section class="slide" data-phase="Amaliy Arena|Практическая Арена|Hands-on Arena" data-time="55:00–70:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКАЯ АРЕНА (25 МИНУТ)" data-en="HANDS-ON ARENA (25 MIN)">AMALIY ARENA (25 DAQIQA)</span></div>
    <h2 data-ru="Интеграция Баллистики в Свой Roguelike" data-en="Integrating Ballistics into Your Roguelike">O'z O'yiningizga Otishma Tizimini Bog'lang</h2>
    <div class="grid-2">
      <div>
        <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
          <button class="btn" id="arenaTimerBtn" onclick="toggleArenaTimer()" style="background:var(--accent); color:#fff; font-weight:700;" data-ru="⏱️ Запустить Таймер" data-en="⏱️ Start Timer">⏱️ Taymerni Boshlash</button>
          <span id="arenaTimerDisplay" style="font-family:var(--font-mono); font-size:24px; font-weight:700; color:var(--red);">25:00</span>
        </div>
        <p class="lede" style="font-size:13px; margin-bottom:8px;" data-ru="Откройте свой код Roguelike и реализуйте 3 обязательных баллистических этапа:" data-en="Open your Roguelike codebase and implement the 3 core ballistics milestones:">O'z kodingizni oching va 3 ta asosiy otishma bosqichini qo'shing:</p>
        <ul class="clean-list" style="font-size:12px;">
          <li data-ru="<strong>1-й Шаг (7 мин):</strong> Слушатель клика мыши и расчет угла через Math.atan2." data-en="<strong>Step 1 (7 min):</strong> Mouse click listener and Math.atan2 angle calculation."><strong>1-Qadam (7 min):</strong> Sichqoncha bosilganda Math.atan2 orqali burchakni hisoblash.</li>
          <li data-ru="<strong>2-й Шаг (8 мин):</strong> Массив пуль, разложение на cos/sin и полет на 60 FPS." data-en="<strong>Step 2 (8 min):</strong> Bullets array, cos/sin velocity split, and 60 FPS flight."><strong>2-Qadam (8 min):</strong> O'qlar massivi, cos/sin orqali harakat va chizish.</li>
          <li data-ru="<strong>3-й Шаг (10 мин):</strong> Проверка удара о тайлы стен и генерация искр (частиц)!" data-en="<strong>Step 3 (10 min):</strong> Tilemap wall collision checks and particle spark explosion FX!"><strong>3-Qadam (10 min):</strong> Devorga urilganda o'qni o'chirish va portlash uchqunlarini sochish!</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="font-weight:700; color:var(--accent); margin-bottom:6px;" data-ru="Критерии Оценки (10 Баллов):" data-en="10 Points Rubric:">10 Ballik Mezon:</div>
          <div style="font-size:11px; line-height:1.6;">
            <div>✅ <strong>4 Ball:</strong> O'qlar kursor yo'nalishiga qarab to'g'ri burchakda uchadi.</div>
            <div>✅ <strong>4 Ball:</strong> Devorga urilganda o'qlar to'xtaydi va xotiradan tozalanadi.</div>
            <div>✅ <strong>2 Ball:</strong> Zarrachalar (uchqunlar) sochilib, chiroyli so'nadi!</div>
          </div>
        </div>
        <div style="margin-top:10px; text-align:right;">
          <a href="simulator/index.html" target="_blank" class="btn" style="background:var(--purple); color:#fff; font-size:11px;" data-ru="Открыть Студию Баллистики" data-en="Launch Ballistics Studio">Katta Studiyani Ochish ➔</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: PEER REVIEW -->
  <section class="slide" data-phase="Partadosh Auditi|Взаимный Аудит|Peer Review" data-time="70:00–74:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМНЫЙ АУДИТ ФИЗИКИ" data-en="PEER PHYSICS AUDIT">PARTADOSH AUDITI</span></div>
    <h2 data-ru="Тестируем Стрельбу Друга: 4 Контрольные Точки" data-en="Audit Your Peer's Shooting Engine: 4 Checkpoints">Do'stingizning Otishma Dvigatelini 4 Mezon Bo'yicha Sinang</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Поменяйтесь местами за партами и проведите стресс-тест баллистики одноклассника:" data-en="Swap seats and stress-test your peer's ballistics implementation:">O'rin almashib, partadoshingizning otishma fizikasini sinovdan o'tkazing:</p>
        <ul class="clean-list">
          <li data-ru="<strong>1. Точность 360°:</strong> Летит ли пуля ровно в перекрестие во всех 4 направлениях?" data-en="<strong>1. 360° Precision:</strong> Does bullet hit precisely where cursor points in all 4 quadrants?"><strong>1. Aniqlik:</strong> O'q barcha 4 chorakda aynan kursor tomon uchayaptimi?</li>
          <li data-ru="<strong>2. Защита от Утечки Памяти:</strong> Очищается ли массив при улете за экран?" data-en="<strong>2. Memory Leak Guard:</strong> Does bullets array length stay under 20 when shooting?"><strong>2. Xotira:</strong> Ko'p o'q uzilganda o'yin qotib qolmayaptimi (massiv o'chyaptimi)?</li>
          <li data-ru="<strong>3. Коллизии Стен:</strong> Не пролетают ли пули сквозь каменные стены насквозь?" data-en="<strong>3. Wall Collisions:</strong> Do projectiles stop upon hitting solid dungeon tiles?"><strong>3. To'qnashuv:</strong> O'q tosh devorlarni teshib o'tib ketmayaptimi?</li>
          <li data-ru="<strong>4. Эстетика Частиц:</strong> Разлетаются ли искры с затуханием прозрачности?" data-en="<strong>4. Spark Aesthetics:</strong> Do sparks scatter and fade away gracefully?"><strong>4. Zarrachalar:</strong> Portlash uchqunlari chiroyli so'nyaptimi?</li>
        </ul>
      </div>
      <div class="box" style="border:1px dashed var(--accent); background:rgba(59,130,246,0.05); display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
        <div style="font-size:40px; margin-bottom:8px;">🎯 🔫 ✨</div>
        <h4 data-ru="Взаимопомощь" data-en="Peer Support">Do'stona Yordam</h4>
        <p style="font-size:12px; color:var(--ink-2); max-width:240px; margin:0;" data-ru="Если пули летят в противоположную сторону, проверьте порядок: dy = targetY - heroY!" data-en="If bullets fly in reverse, check coordinate subtraction: dy = targetY - heroY!">Agar o'q teskari uchsa, ayirish tartibini tekshiring: target - hero bo'lishi kerak!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: SHOWCASE -->
  <section class="slide" data-phase="Katta Ekran|Шоукейс|Showcase" data-time="74:00–77:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ДЕМОНСТРАЦИЯ НА ДОСКЕ" data-en="SMARTBOARD SHOWCASE">KATTA EKRAN SHOWCASI</span></div>
    <h2 data-ru="Шоукейс: Лазерный Бой в Подземелье на Смартборде!" data-en="Showcase: Live Laser Combat on the Big Screen!">Katta Doskada Jonli Kiber-Otishma Showcasi!</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid var(--accent);">
        <h4 data-ru="1. Скорострельный Дробовик" data-en="1. Shotgun Spread">1. Drobovik Sochmasi</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Выстрел веером из 5 снарядов с разбросом угла +-15 градусов." data-en="Firing 5 projectiles in a conical spread of +-15 degrees.">Bitta bosishda +-15 daraja burchak bilan 5 ta o'q sochish.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--purple);">
        <h4 data-ru="2. Рикошетные Пули" data-en="2. Wall Ricochet">2. Rikoshet O'qlari</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Снаряд отскакивает от стены (vx = -vx), сохраняя энергию еще на 2 удара." data-en="Bullet bounces off walls with inverted velocities (vx = -vx).">Devorga urilganda vx = -vx bilan qaytib chiroyli sakrovchi lazer.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--green);">
        <h4 data-ru="3. Плазменный Взрыв" data-en="3. Plasma Burst">3. Plazma Portlashi</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Снаряд взрывается с 40 частицами и звуковым хлопком Web Audio API." data-en="Massive 40-particle explosion with Web Audio synthetic sound FX.">Zarba paytida 40 ta zarracha va sintezlangan portlash ovozi.</p>
      </div>
    </div>
    <div class="box" style="margin-top:12px; background:rgba(16,185,129,0.08); border:1px solid var(--green); text-align:center;">
      <span style="font-weight:700; color:var(--green); font-size:13px;" data-ru="🎉 Браво! Ваша игра теперь превратилась в полноценный боевик!" data-en="🎉 Bravo! Your roguelike has officially leveled up into an action combat game!">🎉 Qoyilmaqom! Roguelike o'yiningiz endi haqiqiy jangovar kiber-jang maydoniga aylandi!</span>
    </div>
  </section>

  <!-- SLIDE 13: TIERED HOMEWORK -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Homework" data-time="77:00–79:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ДОМАШНЕЕ ЗАДАНИЕ (10 БАЛЛОВ)" data-en="HOMEWORK (10 POINTS)">UY VAZIFASI (10 BALL)</span></div>
    <h2 data-ru="3 Уровня: От Базового Выстрела до Рикошета Снарядов" data-en="3 Challenge Tiers: From Base Shooting to Wall Ricochets">3 Darajali Ballistika Vazifasi</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid var(--accent);">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1-Daraja (Baza)</div>
        <h4 data-ru="Одиночный Выстрел (4 Балла)" data-en="Single Shot (4 Points)">Yakka O'q Uzish (4 Ball)</h4>
        <p style="font-size:12px;" data-ru="Реализуйте функцию shootBullet() с расчетом угла через Math.atan2 и полетом по cos/sin." data-en="Implement shootBullet() calculating angle via Math.atan2 and velocity via cos/sin.">Math.atan2 orqali burchakni topib, cos/sin vektorlarida uchuvchi yakka o'q funksiyasini yozing.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--purple);">
        <div class="tag" style="background:rgba(147,51,234,0.15); color:var(--purple);">2-Daraja (Amaliy)</div>
        <h4 data-ru="Стена и Искры (4 Балла)" data-en="Walls & Sparks (4 Points)">Devor va Uchqunlar (4 Ball)</h4>
        <p style="font-size:12px;" data-ru="Добавьте удаление пули при столкновении со стеной тайлмапа и создание 12 искрящихся частиц." data-en="Integrate wall collision detection, bullet deletion, and 12 glowing particle sparks.">O'q devorga tekkanda o'chishi va o'sha yerda 12 ta zarrachalar sochilishini bog'lang.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">3-Daraja (Challenge)</div>
        <h4 data-ru="Рикошет или Дробовик (2 Балла)" data-en="Ricochet or Spread (2 Points)">Rikoshet yoki Drobovik (2 Ball)</h4>
        <p style="font-size:12px;" data-ru="Сделайте рикошет от горизонтальных/вертикальных стен или веерный выстрел 3 пулями одновременно!" data-en="Program wall ricochets (inverting vx/vy) or a triple shotgun conical spread!">Devorga urilganda vx=-vx qilib qaytuvchi rikoshet yoki birdaniga 3 ta o'q sochuvchi drobovik kodi!</p>
      </div>
    </div>
    <div style="margin-top:12px; text-align:right;">
      <a href="vazifa.html" class="btn" style="background:var(--purple); color:#fff; font-size:12px;" data-ru="Открыть ДЗ" data-en="Open HW">Vazifalar Ilovasini Ochish ➔</a>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ УРОКА" data-en="LESSON SUMMARY">XULOSA VA KEYINGI DARS</span></div>
    <h2 data-ru="Баллистика Освоена: Впереди Искусственный Интеллект Врагов" data-en="Ballistics Mastered: Ahead Lies Enemy AI & Pathfinding">Ballistika Egallandi: Oldinda — Dushman AI va Ta'qib</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Сегодня мы превратили математическую тригонометрию в осязаемую физику видеоигры с частицами и баллистикой." data-en="Today we brought trigonometry to life as high-octane video game physics with projectiles and sparks.">Bugun biz trigonometriya fanini jonli video-o'yin fizikasiga aylantirdik: o'qlar, nishonga olish va zarrachalar!</p>
        <ul class="clean-list">
          <li data-ru="<strong>Math.atan2:</strong> Универсальный инструмент прицеливания во всех 360 градусах." data-en="<strong>Math.atan2:</strong> Universal targeting engine covering full 360-degree rads."><strong>Math.atan2:</strong> 360 darajali fazoda nishon burchagini topish standarti.</li>
          <li data-ru="<strong>Векторы cos/sin:</strong> Разделение общей скорости на гладкие шаги по осям." data-en="<strong>cos/sin Vectors:</strong> Splitting linear velocity into clean X/Y frame deltas."><strong>Vektorlar:</strong> Harakatni X va Y o'qlari bo'yicha teng taqsimlash.</li>
          <li data-ru="<strong>Чистка Памяти:</strong> Залог стабильных 60 FPS без лагов и утечек." data-en="<strong>Memory Management:</strong> Essential foundation for stable 60 FPS without leaks."><strong>Xotirani tozalash:</strong> O'yin doim 60 FPS da ravon ishlashining garovi.</li>
        </ul>
      </div>
      <div class="box" style="border-left:4px solid var(--purple); background:rgba(147,51,234,0.08);">
        <strong style="color:var(--purple); font-size:14px;" data-ru="Следующая Тема:" data-en="Next Topic:">🚀 Keyingi Dars Ko'prigi:</strong>
        <p style="font-size:12px; margin-top:6px; line-height:1.5;" data-ru="<strong>Dushman AI va Pathfinding (A* / BFS):</strong> Как научить монстров в лабиринте обходить препятствия и преследовать игрока по кратчайшему пути!" data-en="<strong>Enemy AI & Pathfinding (A* / BFS):</strong> Teaching dungeon monsters to navigate around walls and chase the player using shortest-path graph algorithms!"><strong>Dushman AI va Pathfinding:</strong> Labirintdagi dushmanlarni devorlarni aylanib o'tishga va qahramonni eng qisqa yo'l bilan quvishga o'rgatamiz!</p>
      </div>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. IN-DECK INTERACTIVE SIMULATOR SCRIPT (Slide 8)
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
// Slide 8: In-Deck Canvas Ballistics Simulator
var deckB_canvas = null;
var deckB_ctx = null;
var deckB_bullets = [];
var deckB_sparks = [];
var deckB_hero = { x: 230, y: 125, size: 16 };
var deckB_walls = [
  { x: 60, y: 40, w: 20, h: 170 },
  { x: 380, y: 40, w: 20, h: 170 },
  { x: 180, y: 30, w: 100, h: 20 },
  { x: 180, y: 200, w: 100, h: 20 }
];
var deckB_loopTimer = null;

function initDeckBallistics() {
  deckB_canvas = document.getElementById('deckBallisticsCanvas');
  if (!deckB_canvas) return;
  deckB_ctx = deckB_canvas.getContext('2d');

  deckB_canvas.addEventListener('pointerdown', function(e) {
    var rect = deckB_canvas.getBoundingClientRect();
    var scaleX = deckB_canvas.width / rect.width;
    var scaleY = deckB_canvas.height / rect.height;
    var tx = (e.clientX - rect.left) * scaleX;
    var ty = (e.clientY - rect.top) * scaleY;
    deckFireBullet(tx, ty);
  });

  if (!deckB_loopTimer) {
    deckB_loopTimer = setInterval(deckUpdateBallistics, 1000 / 60);
  }
}

function deckFireBullet(tx, ty) {
  var angle = Math.atan2(ty - deckB_hero.y, tx - deckB_hero.x);
  var spd = 8;
  deckB_bullets.push({
    x: deckB_hero.x,
    y: deckB_hero.y,
    vx: Math.cos(angle) * spd,
    vy: Math.sin(angle) * spd,
    life: 75
  });
}

function deckTriggerBurst() {
  for (var i = 0; i < 16; i++) {
    var angle = (i / 16) * Math.PI * 2;
    var spd = 7;
    deckB_bullets.push({
      x: deckB_hero.x,
      y: deckB_hero.y,
      vx: Math.cos(angle) * spd,
      vy: Math.sin(angle) * spd,
      life: 80
    });
  }
}

function deckClearArena() {
  deckB_bullets = [];
  deckB_sparks = [];
}

function deckSpawnSparks(x, y) {
  for (var i = 0; i < 10; i++) {
    var angle = Math.random() * Math.PI * 2;
    var spd = Math.random() * 4 + 1;
    deckB_sparks.push({
      x: x,
      y: y,
      vx: Math.cos(angle) * spd,
      vy: Math.sin(angle) * spd,
      alpha: 1.0
    });
  }
}

function deckUpdateBallistics() {
  if (!deckB_ctx) return;
  deckB_ctx.fillStyle = '#020617';
  deckB_ctx.fillRect(0, 0, deckB_canvas.width, deckB_canvas.height);

  // Draw Walls
  deckB_ctx.fillStyle = '#1e293b';
  deckB_ctx.strokeStyle = '#334155';
  deckB_ctx.lineWidth = 1;
  for (var w = 0; w < deckB_walls.length; w++) {
    var wl = deckB_walls[w];
    deckB_ctx.fillRect(wl.x, wl.y, wl.w, wl.h);
    deckB_ctx.strokeRect(wl.x, wl.y, wl.w, wl.h);
  }

  // Update & Draw Bullets (Reverse Loop)
  for (var i = deckB_bullets.length - 1; i >= 0; i--) {
    var b = deckB_bullets[i];
    b.x += b.vx;
    b.y += b.vy;
    b.life--;

    var hit = false;
    // Check wall collisions (AABB)
    for (var j = 0; j < deckB_walls.length; j++) {
      var wall = deckB_walls[j];
      if (b.x >= wall.x && b.x <= wall.x + wall.w && b.y >= wall.y && b.y <= wall.y + wall.h) {
        hit = true;
        break;
      }
    }

    if (hit || b.life <= 0 || b.x < 0 || b.x > deckB_canvas.width || b.y < 0 || b.y > deckB_canvas.height) {
      if (hit) deckSpawnSparks(b.x, b.y);
      deckB_bullets.splice(i, 1);
      continue;
    }

    // Draw bullet
    deckB_ctx.fillStyle = '#38bdf8';
    deckB_ctx.beginPath();
    deckB_ctx.arc(b.x, b.y, 3, 0, Math.PI * 2);
    deckB_ctx.fill();

    // Glow tail
    deckB_ctx.strokeStyle = 'rgba(56,189,248,0.4)';
    deckB_ctx.lineWidth = 2;
    deckB_ctx.beginPath();
    deckB_ctx.moveTo(b.x, b.y);
    deckB_ctx.lineTo(b.x - b.vx * 2, b.y - b.vy * 2);
    deckB_ctx.stroke();
  }

  // Update & Draw Sparks
  for (var s = deckB_sparks.length - 1; s >= 0; s--) {
    var spk = deckB_sparks[s];
    spk.x += spk.vx;
    spk.y += spk.vy;
    spk.vx *= 0.92;
    spk.vy *= 0.92;
    spk.alpha -= 0.03;

    if (spk.alpha <= 0) {
      deckB_sparks.splice(s, 1);
      continue;
    }

    deckB_ctx.fillStyle = 'rgba(245, 158, 11, ' + spk.alpha + ')';
    deckB_ctx.fillRect(spk.x - 1, spk.y - 1, 3, 3);
  }

  // Draw Hero
  deckB_ctx.fillStyle = '#10b981';
  deckB_ctx.beginPath();
  deckB_ctx.arc(deckB_hero.x, deckB_hero.y, deckB_hero.size, 0, Math.PI * 2);
  deckB_ctx.fill();
  deckB_ctx.font = '16px sans-serif';
  deckB_ctx.fillText('🧙', deckB_hero.x - 8, deckB_hero.y + 6);

  // Update Counters
  var bEl = document.getElementById('deckBulletCount');
  var sEl = document.getElementById('deckSparkCount');
  if (bEl) bEl.textContent = deckB_bullets.length;
  if (sEl) sEl.textContent = deckB_sparks.length;
}

setTimeout(initDeckBallistics, 500);

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

# Notes array for 14 slides (Strictly triplets [title, say, do])
NOTES_DATA = {
    "uz": [
        ["Kirish va Maqsad", "O'quvchilarga bugungi mavzu: O'yin fizikasi va otishma mexanikasi haqida so'zlang.", "Doskaga qahramon va nishon burchagini chizing."],
        ["Uy Vazifasi Tahlili", "31-darsdagi Random Walker devorlarni teshib tashlash xatosini va clamping yechimini tushuntiring.", "Oltin yechim: Math.max va Math.min bilan chegaralash ekanini ko'rsating."],
        ["Otishma Arxitekturasi", "Sichqoncha bosilishidan o'q parvozigacha bo'lgan 4 bosqichni tushuntiring.", "dx va dy hisoblash formulalarini ko'rsating."],
        ["Math.atan2 Sehri", "Nega oddiy atan emas, Math.atan2(dy, dx) ishlatilishini ayting.", "Nolga bo'lish xavfi yo'qligi va 4 ta chorak burchaklarini tushuntiring."],
        ["Tezlik Vektorlari", "cos va sin yordamida umumiy tezlikni X va Y o'qlariga taqsimlash formulasini ko'rsating.", "Pifagor teoremasi orqali tezlik doimiyligini tushuntiring."],
        ["Xotirani Tozalash", "Ekranni tark etgan yoki devorga urilgan o'qlarni splice qilish zarurligini ayting.", "Nega teskari sikl (length-1 dan 0 gacha) ishlatilishini tushuntiring."],
        ["Zarrachalar Tizimi", "Zarba paytida uchqunlar qanday sochilib, alpha shaffofligi bilan so'nishini ko'rsating.", "Ishqalanish koeffitsienti 0.92 ni tushuntiring."],
        ["Smartboard Simulyatori", "Taqdimot ichidagi ballistika simulyatorida sichqoncha bilan o't ochib bering.", "Devorga urilganda o'q yo'qolib, uchqunlar chiqishini ko'rsating."],
        ["Bilimni Sinash (Quiz)", "3 ta viktorina savolini sinf bilan birga tahlil qiling.", "Har bir to'g'ri va noto'g'ri javob sababini ayting."],
        ["25 Daqiqalik Arena", "O'quvchilarga simulator/index.html ni ochishni buyuring.", "O'z o'yinlariga otishma mexanikasini kiritishlarini nazorat qiling."],
        ["Partadosh Auditi", "O'rin almashib, 4 ta mezon bo'yicha partadosh o'yinini sinashsin.", "Devorlar o'qlarni to'xtatayotganini tekshiring."],
        ["Katta Ekran Showcasi", "Eng yaxshi 3 ta otishma tizimini katta doskaga chiqarib namoyish qiling.", "Mualliflarni olqishlang."],
        ["3 Darajali Uy Vazifasi", "10 ballik uy vazifasi shartlarini tushuntiring.", "3-darajadagi rikoshet yoki drobovik vazifasini ta'kidlang."],
        ["Xulosa va Keyingi Dars", "Darsni sarhisob qiling va keyingi darsda Dushman AI va Pathfinding algoritmlarini o'rganishimizni e'lon qiling.", "O'quvchilar savollariga javob bering va vazifa topshirilish muddatini eslating."]
    ],
    "ru": [
        ["Введение и Цель", "Представьте тему: физика снарядов, механика прицеливания и тригонометрия на Canvas.", "Нарисуйте на доске треугольник скоростей и угол прицеливания."],
        ["Разбор Домашнего Задания", "Разберите ошибку выхода Random Walker за пределы сетки из 31-урока.", "Покажите золотой стандарт: принудительный clamping координат."],
        ["Архитектура Стрельбы", "Разберите 4 шага выстрела: захват координат, расчет dx/dy, угол atan2 и векторы cos/sin.", "Покажите связь клика мыши с физикой пули."],
        ["Магия Math.atan2", "Объясните, почему atan2(dy, dx) превосходит классический atan(dy/dx).", "Подчеркните отсутствие деления на ноль и работу во всех 360 градусах."],
        ["Векторы Скорости", "Покажите разложение линейной скорости на проекции vx = cos * speed и vy = sin * speed.", "Продемонстрируйте постоянство скорости по теореме Пифагора."],
        ["Очистка Памяти", "Объясните катастрофу утечки памяти (Memory Leak) при накоплении снарядов в массиве.", "Покажите обратный цикл удаления с конца."],
        ["Система Частиц", "Покажите создание искр при ударе о стену с затуханием прозрачности alpha.", "Объясните эффект воздушного сопротивления (умножение на 0.92)."],
        ["Интерактив на Доске", "Запустите встроенный симулятор баллистики на смартборде.", "Продемонстрируйте прицельный огонь и 360-градусный залп."],
        ["Тест (Квиз)", "Проведите веселое тестирование из 3 вопросов.", "Обсудите правильные формулы со всем классом."],
        ["Практическая Арена (25 мин)", "Дайте команду открыть simulator/index.html.", "Курируйте внедрение механики стрельбы каждым учеником."],
        ["Взаимный Аудит", "Организуйте обмен местами за партами по чек-листу из 4 пунктов.", "Проверьте стабильность FPS при непрерывной стрельбе."],
        ["Шоукейс на Доске", "Выведите лучшие боевые системы на смартборд и сыграйте перед классом.", "Похвалите авторов аплодисментами."],
        ["Домашнее Задание", "Объясните 3 уровня 10-балльного домашнего задания.", "Обратите внимание на вызов 3-го уровня с рикошетом пуль."],
        ["Итоги и Анонс", "Подведите итоги урока и анонсируйте следующую тему: ИИ врагов и поиск путей (A* / BFS).", "Ответьте на вопросы учеников и напомните дедлайн сдачи практического ДЗ."]
    ],
    "en": [
        ["Intro & Objectives", "Introduce 2D ballistics, mouse targeting, and trigonometric velocity vectors.", "Diagram the right-angle triangle showing dx, dy, and aiming radians."],
        ["Homework Review", "Analyze the perimeter wall penetration bug in Lesson 31's procedural walker.", "Demonstrate the golden solution: boundary clamping with Math.max/min."],
        ["Shooting Pipeline", "Break down the 4 steps: mouse coordinates, delta offsets, Math.atan2, and velocity split.", "Connect raw user input to continuous physics loops."],
        ["Magic of Math.atan2", "Explain why Math.atan2(dy, dx) prevents zero-division crashes and handles full 360 degrees.", "Highlight argument ordering: dy comes before dx."],
        ["Velocity Vectors", "Demonstrate decomposing linear velocity via vx = cos * speed and vy = sin * speed.", "Prove constant projectile velocity using Pythagorean theorem."],
        ["Memory Management", "Explain memory leaks caused by lingering off-screen projectiles in unmanaged arrays.", "Demonstrate reverse-order array splicing."],
        ["Particle Spark Systems", "Show how wall impacts generate radial particle bursts with alpha fadeouts.", "Explain air friction damping via 0.92 velocity scaling."],
        ["In-Deck Live Demo", "Activate the interactive Canvas ballistics engine directly on the Smartboard.", "Test precision targeting and fire the 360-degree projectile burst."],
        ["Knowledge Check (Quiz)", "Lead the class through the 3 quick questions.", "Discuss each answer with the class."],
        ["Hands-on Arena (25 min)", "Instruct students to open simulator/index.html.", "Supervise students integrating the shooting engine into their roguelike."],
        ["Peer Code Audit", "Facilitate seat swapping to review shooting code using the 4-point rubric.", "Ensure projectiles cannot tunnel through solid walls."],
        ["Showcase Arena", "Project the 3 top shooting prototypes onto the main Smartboard.", "Celebrate student achievements."],
        ["Tiered Homework", "Explain the 3-tiered 10-point homework assignment.", "Highlight Tier 3's ricochet and shotgun challenges."],
        ["Summary & Next Class", "Summarize core takeaways and preview Enemy AI and Pathfinding (A* search).", "Answer student questions and remind them of the homework lab deadline."]
    ]
}

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "32-dars: O'yin Fizikasi va Otishma Mexanikasi: Trigonometriya, Traektoriya va Zarrachalar"
    title_ru = "Урок 32: Физика Игры и Механика Стрельбы: Тригонометрия, Траектории и Частицы"
    title_en = "Lesson 32: Game Physics & Ballistics: Trigonometry, Trajectories & Particles"

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

    title_uz = "32-dars: O'yin Fizikasi va Otishma Mexanikasi: Trigonometriya, Traektoriya va Zarrachalar"
    title_ru = "Урок 32: Физика Игры и Механика Стрельбы: Тригонометрия, Траектории и Частицы"
    title_en = "Lesson 32: Game Physics & Ballistics: Trigonometry, Trajectories & Particles"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<h1>.*?</h1>',
                 f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>',
                 tpl)

    sec1_html = """
    <p class="lead" style="font-size:12px; margin-bottom:8px;" data-ru="<strong>Миссия Урока:</strong> Запрограммировать физический движок баллистики на HTML5 Canvas: захват угла курсора через Math.atan2, разложение скорости на векторы cos/sin, очистку памяти от улетевших пуль и вспышки искр при ударе о стены." data-en="<strong>Lesson Mission:</strong> Engineer a 2D Canvas ballistics engine: targeting cursor radians via Math.atan2, vector velocity decomposition via cos/sin, off-screen memory purging, and particle spark impacts upon wall collision."><strong>Dars Missiyasi:</strong> HTML5 Canvas da to'liq otishma fizikasini yaratish: Math.atan2 yordamida nishon burchagini topish, cos/sin orqali tezlik vektorlarini uzatish, xotirani tozalash va devorga urilganda uchqunlar portlashini kodlash.</p>
    <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="4 Математических Столпа Баллистики:" data-en="4 Mathematical Pillars of Ballistics:">Otishma Fizikasining 4 Asosiy Ustuni:</div>
      <div>1. <strong>Delta masofa:</strong> <span data-ru="dx = mouseX - heroX, dy = mouseY - heroY" data-en="dx = mouseX - heroX, dy = mouseY - heroY">dx = mouseX - heroX, dy = mouseY - heroY</span>.</div>
      <div>2. <strong>Burchak:</strong> <span data-ru="angle = Math.atan2(dy, dx) (в радианах от -PI до +PI)" data-en="angle = Math.atan2(dy, dx) (radians between -PI and +PI)">angle = Math.atan2(dy, dx) (-PI dan +PI gacha)</span>.</div>
      <div>3. <strong>Vektorlar:</strong> <span data-ru="vx = Math.cos(angle) * speed, vy = Math.sin(angle) * speed" data-en="vx = Math.cos(angle) * speed, vy = Math.sin(angle) * speed">vx = Math.cos(angle) * speed, vy = Math.sin(angle) * speed</span>.</div>
      <div>4. <strong>Tozalash:</strong> <span data-ru="bullets.splice(i, 1) при ударе о стену или выходе за экран" data-en="bullets.splice(i, 1) upon wall hit or out-of-bounds">Devorga urilganda bullets.splice(i, 1) orqali tozalash</span>.</div>
    </div>
    """

    sec2_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="Код расчета скорости и добавления снаряда в массив:" data-en="Code snippet calculating velocity and pushing projectile into array:">O'q tezligini hisoblash va massivga qo'shish kodi:</p>
    <pre style="background:var(--surface-2); padding:6px; font-size:11px; border-radius:4px; margin:0;"><code class="language-js">function shoot(targetX, targetY) {
  const angle = Math.atan2(targetY - hero.y, targetX - hero.x);
  const speed = 10;
  bullets.push({
    x: hero.x, y: hero.y,
    vx: Math.cos(angle) * speed,
    vy: Math.sin(angle) * speed,
    life: 60
  });
}</code></pre>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Функция / Формула" data-en="Function / Formula">Funksiya / Formula</th>
            <th style="padding:4px 6px;" data-ru="Назначение" data-en="Purpose">Maqsadi</th>
            <th style="padding:4px 6px;" data-ru="Возвращаемое Значение" data-en="Output">Qaytuvchi Natija</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="Math.atan2(dy, dx)" data-en="Math.atan2(dy, dx)"><code>Math.atan2(dy, dx)</code></td>
            <td style="padding:4px 6px;" data-ru="Расчет угла между точками" data-en="Calculates angle between points">Ikki nuqta orasidagi burchak</td>
            <td style="padding:4px 6px;" data-ru="Радианы (-PI .. +PI)" data-en="Radians (-PI .. +PI)">Radianlar (-3.14 .. +3.14)</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Освоено" data-en="[ &nbsp; ] Done">[ &nbsp; ] Bajarildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="Math.cos(angle) * spd" data-en="Math.cos(angle) * spd)"><code>Math.cos(angle) * spd</code></td>
            <td style="padding:4px 6px;" data-ru="Горизонтальная скорость (X)" data-en="Horizontal speed component">Gorizontal tezlik (vx)</td>
            <td style="padding:4px 6px;" data-ru="Смещение по X за кадр" data-en="Delta X per frame">X o'qi bo'yicha siljish</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Освоено" data-en="[ &nbsp; ] Done">[ &nbsp; ] Bajarildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="Math.sin(angle) * spd" data-en="Math.sin(angle) * spd)"><code>Math.sin(angle) * spd</code></td>
            <td style="padding:4px 6px;" data-ru="Вертикальная скорость (Y)" data-en="Vertical speed component">Vertikal tezlik (vy)</td>
            <td style="padding:4px 6px;" data-ru="Смещение по Y за кадр" data-en="Delta Y per frame">Y o'qi bo'yicha siljish</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Освоено" data-en="[ &nbsp; ] Done">[ &nbsp; ] Bajarildi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="bullets.splice(i, 1)" data-en="bullets.splice(i, 1)"><code>bullets.splice(i, 1)</code></td>
            <td style="padding:4px 6px;" data-ru="Удаление снаряда из массива" data-en="Purging projectile from array">O'qni massivdan o'chirish</td>
            <td style="padding:4px 6px;" data-ru="Освобождение памяти" data-en="Memory reclaimed">Xotirani tozalash</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Освоено" data-en="[ &nbsp; ] Done">[ &nbsp; ] Bajarildi</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    sec4_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="Спроектируйте жизненный цикл снаряда от выстрела до искр:" data-en="Draft the projectile lifecycle from firing to particle sparks:">O'qning hayot tsikli rejasini to'ldiring:</p>
    <div style="border:1px dashed var(--hair); padding:8px; border-radius:4px; font-family:var(--font-mono); font-size:11px; line-height:1.6;">
      <div>1. [TUGMA BOSILDI] ➔ dx = tx - hx; dy = ty - hy ➔ angle = Math.atan2(dy, dx)</div>
      <div>2. [PARVOZ] ➔ x += vx; y += vy; life--; (60 FPS da har kadr chiziladi)</div>
      <div>3. [DEVOR BILAN TO'QNASHUV] ➔ if (isWall(x, y)) {</div>
      <div>&nbsp;&nbsp;&nbsp;&nbsp;createSparks(x, y); // 12 ta zarracha sochiladi</div>
      <div>&nbsp;&nbsp;&nbsp;&nbsp;bullets.splice(i, 1); // o'q xotiradan tozalanadi</div>
      <div>&nbsp;&nbsp;&nbsp;}</div>
    </div>
    """

    sec5_html = """
    <div style="font-size:11px; line-height:1.6;">
      <div>[ &nbsp; ] <strong>4 Ball (Baza):</strong> O'qlar kursor yo'nalishiga qarab to'g'ri burchakda uzluksiz uchadi.</div>
      <div>[ &nbsp; ] <strong>4 Ball (Amaliy):</strong> Devorga urilganda o'qlar to'xtaydi va massivdan xatosiz tozalanadi.</div>
      <div>[ &nbsp; ] <strong>2 Ball (Challenge):</strong> Zarrachalar (uchqunlar) sochilib, chiroyli so'nishi (yoki rikoshet) ishlaydi!</div>
      <div style="margin-top:6px; border-top:1px solid var(--hair); padding-top:4px; font-weight:700; color:var(--accent);" data-ru="Итоговый балл: _____ / 10 &nbsp; Подпись учителя: ____________" data-en="Total Score: _____ / 10 &nbsp; Teacher Signature: ____________">Jami to'plangan ball: _____ / 10 &nbsp; O'qituvchi imzosi: ____________</div>
    </div>
    """

    tpl = tpl.replace("{{SECTION_1}}", sec1_html)
    tpl = tpl.replace("{{SECTION_2}}", sec2_html)
    tpl = tpl.replace("{{SECTION_3}}", sec3_html)
    tpl = tpl.replace("{{SECTION_4}}", sec4_html)
    tpl = tpl.replace("{{SECTION_5}}", sec5_html)

    out_path = os.path.join(DEST_DIR, "varaqa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: varaqa.html")

def build_homework():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "32-dars: O'yin Fizikasi va Otishma Mexanikasi: Trigonometriya, Traektoriya va Zarrachalar"
    title_ru = "Урок 32: Физика Игры и Механика Стрельбы: Тригонометрия, Траектории и Частицы"
    title_en = "Lesson 32: Game Physics & Ballistics: Trigonometry, Trajectories & Particles"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tasks_html = """
    <!-- TIER 1 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1-Daraja (Baza — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Функция Выстрела: Math.atan2, cos и sin" data-en="Shooting Function: Math.atan2, cos & sin">Otishma Funksiyasi: Math.atan2, cos va sin</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите функцию shootBullet(hero, targetX, targetY, speed), которая вычисляет угол через Math.atan2, рассчитывает vx и vy через cos/sin и возвращает объект снаряда." data-en="Write shootBullet(hero, targetX, targetY, speed) calculating angle via Math.atan2, decomposing velocity via cos/sin, and returning the projectile object."><code>shootBullet(hero, targetX, targetY, speed)</code> funksiyasini yozing: burchakni Math.atan2 bilan topib, vx va vy tezliklarini cos/sin orqali hisoblab yangi o'q obyektini qaytaring.</p>
      <textarea class="answer-area" id="ans_task_1" rows="6" placeholder="JavaScript funksiyangizni bu yerga yozing..." data-placeholder-ru="Напишите функцию здесь..." data-placeholder-en="Write your function here..." oninput="saveAnswers()"></textarea>
      <div class="solution-box" id="sol_task_1" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px; font-family:var(--font-mono);">
        <strong>Namunaviy Yechim:</strong><br>
        <code>function shootBullet(hero, targetX, targetY, speed = 10) {</code><br>
        <code>&nbsp;&nbsp;const angle = Math.atan2(targetY - hero.y, targetX - hero.x);</code><br>
        <code>&nbsp;&nbsp;return { x: hero.x, y: hero.y, vx: Math.cos(angle) * speed, vy: Math.sin(angle) * speed, life: 60 };</code><br>
        <code>}</code>
      </div>
    </div>

    <!-- TIER 2 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(147,51,234,0.15); color:var(--purple);">2-Daraja (Amaliy — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Очистка Памяти и Столкновение со Стенами" data-en="Memory Purging & Wall Collision">Xotirani Tozalash va Devor To'qnashuvi</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите цикл обновления массива bullets: смещение координат, проверка столкновения со стеной тайлмапа isWall(b.x, b.y) и корректное удаление снаряда через splice в обратном цикле." data-en="Implement the bullets update loop: incrementing coordinates, checking tilemap wall collisions via isWall(b.x, b.y), and safely splicing dead projectiles in reverse order.">O'qlar massivini yangilovchi siklni yozing: koordinatalarni oshirish, devorga urilishni tekshirish va teskari siklda <code>bullets.splice(i, 1)</code> bilan tozalash.</p>
      <textarea class="answer-area" id="ans_task_2" rows="7" placeholder="Yangilash siklini bu yerga yozing..." data-placeholder-ru="Напишите цикл здесь..." data-placeholder-en="Write loop code here..." oninput="saveAnswers()"></textarea>
      <div class="solution-box" id="sol_task_2" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px; font-family:var(--font-mono);">
        <strong>Namunaviy Yechim:</strong><br>
        <code>for (let i = bullets.length - 1; i >= 0; i--) {</code><br>
        <code>&nbsp;&nbsp;const b = bullets[i];</code><br>
        <code>&nbsp;&nbsp;b.x += b.vx; b.y += b.vy; b.life--;</code><br>
        <code>&nbsp;&nbsp;if (b.life <= 0 || isWall(b.x, b.y) || b.x < 0 || b.x > width || b.y < 0 || b.y > height) {</code><br>
        <code>&nbsp;&nbsp;&nbsp;&nbsp;createSparks(b.x, b.y);</code><br>
        <code>&nbsp;&nbsp;&nbsp;&nbsp;bullets.splice(i, 1);</code><br>
        <code>&nbsp;&nbsp;}</code><br>
        <code>}</code>
      </div>
    </div>

    <!-- TIER 3 (2 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">3-Daraja (Challenge — 2 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Рикошет от Стен или Дробовик (Shotgun)" data-en="Wall Ricochet or Shotgun Cone">Kiber-Challenge: Rikoshet yoki Drobovik</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Как реализовать рикошет от горизонтальной стены (инверсия vy = -vy) или залп из 3 пуль веером с отклонением угла [-0.2, 0, +0.2] радиан?" data-en="How to code a wall ricochet (inverting vy = -vy upon horizontal impact) or a 3-bullet conical shotgun burst with angle offsets [-0.2, 0, +0.2] rads?">Gorizontal devorga urilganda vy = -vy qilib sakrovchi rikoshet yoki birdaniga 3 ta o'qni burchak siljishi [-0.2, 0, +0.2] bilan sochuvchi drobovik algoritmini tushuntiring.</p>
      <textarea class="answer-area" id="ans_task_3" rows="6" placeholder="Challenge yechimingizni bu yerga yozing..." data-placeholder-ru="Напишите решение здесь..." data-placeholder-en="Write challenge code here..." oninput="saveAnswers()"></textarea>
      <div class="solution-box" id="sol_task_3" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px; font-family:var(--font-mono);">
        <strong>Namunaviy Yechim:</strong><br>
        <code>// Drobovik: 3 ta o'q uzish</code><br>
        <code>[-0.2, 0, 0.2].forEach(offset => {</code><br>
        <code>&nbsp;&nbsp;const a = baseAngle + offset;</code><br>
        <code>&nbsp;&nbsp;bullets.push({ x: hero.x, y: hero.y, vx: Math.cos(a)*speed, vy: Math.sin(a)*speed, life: 50 });</code><br>
        <code>});</code>
      </div>
    </div>
    """

    tpl = tpl.replace("{{TASKS}}", tasks_html)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    doc = """# 32-dars: O'yin Fizikasi va Otishma Mexanikasi: Trigonometriya, Traektoriya va Zarrachalar (O'qituvchi Metodologiyasi)

## Darsning Pasporti
- **Sinf:** 7–8-sinf (Game Dev & Creative Coding Track)
- **Davomiyligi:** 80 daqiqa (Juftlik Dars / Double Block)
- **Asosiy maqsad:** 2D Canvas o'yinlarida otishma fizikasi va ballistika mexanikasini o'rgatish. Math.atan2 orqali burchakni hisoblash, tezlikni cos/sin vektorlariga ajratish, o'qlar massivini xavfsiz boshqarish (Memory leakning oldini olish) va devorga urilganda uchqunlar (particle sparks) tizimini dasturlash.

---

## 80 Daqiqalik Aniq Vaqt Taqsimoti (Pacing)

### 1-Qism: Nazariya, Xatolar Tahlili va Jonli Test (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Motivatsiya | 1 | Ballistika va otishma fizikasining video o'yinlardagi rolini tushuntirish. | Diqqat bilan tinglaydilar va maqsadni belgilaydilar. |
| **04:00–12:00** | 31-dars HW Tahlili | 2 | Random Walker devorlarni teshib o'tishi va clamping xatolarini tahlil qilish. | Blitz savolga javob beradilar, clamping qoidasini yozib oladilar. |
| **12:00–18:00** | Otishma Arxitekturasi | 3 | Kursor bosilishidan to'qnashuvgacha bo'lgan 4 bosqichni chizib ko'rsatish. | Otishma zanjirini tushunadilar. |
| **18:00–24:00** | Math.atan2 Sehri | 4 | Nega atan emas, Math.atan2(dy, dx) ishlatilishini asoslash. Argumentlar tartibini ta'kidlash. | Radiandagi burchak tushunchasini o'rganadilar. |
| **24:00–30:00** | Tezlik Vektorlari | 5 | cos va sin proeksiyalarini Pifagor teoremasi orqali isbotlash. | vx va vy formulalarini yozib oladilar. |
| **30:00–35:00** | Xotirani Tozalash | 6 | Memory leak muammosi va nega teskari tartibda (length-1 dan 0 gacha) splice qilish zarurligini tushuntirish. | Xavfsiz tozalash siklini o'zlashtiradilar. |
| **35:00–40:00** | Zarrachalar Tizimi | 7 | Uchqunlar sochilishi, 0.92 ishqalanish kuchi va alpha so'nishi mexanikasini ko'rsatish. | Vizual effektlar fizikasini o'rganadilar. |

### 2-Qism: Smartboard Sinovi, Katta Arena va Showcase (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **40:00–48:00** | Smartboard Simulyatori | 8 | Slayddagi simulyatorda bolalar bilan doskaga bosib lazer uzish va 360° salyutni ko'rsatish. | Doskada lazer uzib, zarrachalar sochilishini kuzatadilar. |
| **48:00–55:00** | Viktorina (Quiz) | 9 | 3 ta nazorat savoli bo'yicha viktorina o'tkazish. | Faol javob beradilar va o'z bilimlarini tekshiradilar. |
| **55:00–70:00** | 25 Daqiqalik Arena | 10 | 25:00 taymerni yoqish, partalar bo'ylab yurib ko'maklashish. | simulator/index.html da o'z Roguelike o'yinlariga otishma tizimini ulaydilar. |
| **70:00–74:00** | Partadosh Auditi | 11 | O'rin almashishni e'lon qilish, 4 mezonli sinovni nazorat qilish. | Bir-birining tizimiga to'xtovsiz o'q uzib, xotira tozalanishini tekshiradilar. |
| **74:00–77:00** | Katta Ekran Showcasi | 12 | Eng zo'r otishma tizimini katta doskaga chiqarib sinash (drobovik / rikoshet). | Sinfdoshlari natijasini olqishlaydilar. |
| **77:00–80:00** | Uy Vazifasi va Yakun | 13–14 | 10 ballik uy vazifasini tushuntirish va Dushman AI (A* qidiruv) mavzusiga ko'prik! | Kundaliklariga vazifani belgilaydilar. |

---

## O'qituvchi Uchun Muhim Blitz Savollari
1. **"Nega Math.atan2(dx, dy) deb yozsak xato bo'ladi?"**
   - Javob: Chunki funksiya birinchi argument sifatida Y o'qidagi siljishni (dy), ikkinchi bo'lib X o'qidagi siljishni (dx) kutadi. Agar adashtirsak, o'qlar 90 daraja noto'g'ri tomonga uchadi!
2. **"O'qlarni boshidan (i=0 dan) splice qilsak nega ba'zi o'qlar o'chmay qoladi?"**
   - Javob: Chunki splice qilinganda massivdagi qolgan elementlar bitta chapga suriladi. Natijada keyingi elementning indeksi o'tib ketilib, tekshirilmay qoladi (indeks sakrashi xatosi).

---

## 10 Ballik Baholash Rubrikasi
- **4 Ball (Baza):** O'qlar kursor bosilgan tomonga Math.atan2 va cos/sin orqali to'g'ri uchadi.
- **4 Ball (Amaliy):** Devorga urilganda o'q to'xtaydi va teskari sikl orqali massivdan xatosiz o'chiriladi.
- **2 Ball (Challenge):** Zarrachalar (uchqunlar) portlashi yoki rikoshet/drobovik mexanikasi ishlaydi!
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
  <title data-ru="Студия Баллистики и Оружия (Canvas Ballistics)" data-en="Canvas Ballistics & Shooting Studio">Ballistika va Otishma Fizikasi Studiyasi</title>
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
      font-size: 16px;
      color: var(--accent);
    }
    .hud {
      display: flex;
      gap: 14px;
      align-items: center;
      font-weight: 700;
      font-size: 13px;
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
      grid-template-columns: 1fr 320px;
      gap: 14px;
      padding: 14px;
      overflow: hidden;
    }
    .stage-wrapper {
      background: #020617;
      border: 2px solid var(--accent);
      border-radius: 10px;
      position: relative;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    #simCanvas {
      display: block;
      width: 100%;
      height: 100%;
      cursor: crosshair;
    }
    .sidebar {
      background: var(--surface);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 10px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      overflow-y: auto;
    }
    .box-card {
      background: var(--surface-2);
      padding: 12px;
      border-radius: 8px;
    }
    .box-card h4 {
      font-size: 12px;
      color: var(--accent);
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .btn {
      background: var(--accent);
      color: #000;
      border: none;
      border-radius: 6px;
      padding: 8px 14px;
      font-weight: 700;
      cursor: pointer;
      font-size: 12px;
      transition: all 0.2s;
    }
    .btn:hover { opacity: 0.9; transform: scale(1.02); }
    .btn-green { background: var(--green); color: #fff; }
    .btn-red { background: var(--red); color: #fff; }
    .btn-gray { background: #334155; color: #fff; }
  </style>
</head>
<body>

<header>
  <div class="brand">
    <span>🎯 Canvas Ballistics Engine: Math.atan2 & Particle Sparks</span>
    <span style="font-size:11px; background:rgba(56,189,248,0.15); color:var(--accent); padding:2px 8px; border-radius:12px;">7–8-Sinf</span>
  </div>
  <div class="hud">
    <div class="hud-badge">🚀 <span data-ru="Пули:" data-en="Bullets:">O'qlar:</span> <strong id="hudBullets" style="color:var(--accent); font-size:14px;">0</strong></div>
    <div class="hud-badge">💥 <span data-ru="Искры:" data-en="Sparks:">Uchqunlar:</span> <strong id="hudSparks" style="color:var(--yellow); font-size:14px;">0</strong></div>
    <div class="hud-badge">🎯 <span data-ru="Уничтожено:" data-en="Destroyed:">Nishonlar:</span> <strong id="hudKills" style="color:var(--green); font-size:14px;">0</strong></div>
  </div>
</header>

<main>
  <div class="stage-wrapper">
    <canvas id="simCanvas" width="800" height="500"></canvas>
  </div>

  <div class="sidebar">
    <div class="box-card">
      <h4 data-ru="Режим Стрельбы" data-en="Weapon Mode">Qurol Rejimi</h4>
      <div style="display:flex; flex-direction:column; gap:6px;">
        <label style="display:flex; gap:8px; align-items:center; font-size:12px; cursor:pointer;">
          <input type="radio" name="weapon" value="single" checked onchange="setWeapon(this.value)">
          <span data-ru="Одиночный Лазер (Single)" data-en="Single Laser">Yakka Lazer (Single)</span>
        </label>
        <label style="display:flex; gap:8px; align-items:center; font-size:12px; cursor:pointer;">
          <input type="radio" name="weapon" value="shotgun" onchange="setWeapon(this.value)">
          <span data-ru="Дробовик (3 Пули Веером)" data-en="Shotgun (3-Way Spread)">Drobovik (3 ta o'q sochmasi)</span>
        </label>
        <label style="display:flex; gap:8px; align-items:center; font-size:12px; cursor:pointer;">
          <input type="radio" name="weapon" value="burst" onchange="setWeapon(this.value)">
          <span data-ru="Круговой Залп (360° Burst)" data-en="360° Circular Burst">360° Doiraviy Salьyut</span>
        </label>
      </div>
    </div>

    <div class="box-card">
      <h4 data-ru="Параметры Физики" data-en="Physics Tuning">Fizika Sozlamalari</h4>
      <div style="font-size:12px; display:flex; flex-direction:column; gap:8px;">
        <label style="display:flex; justify-content:space-between;">
          <span data-ru="Скорость Пули:" data-en="Bullet Speed:">O'q Tezligi:</span>
          <input type="range" id="rangeSpeed" min="5" max="20" value="12" style="width:100px;" oninput="updateSpeed(this.value)">
        </label>
        <label style="display:flex; justify-content:space-between;">
          <span data-ru="Угол Прицела:" data-en="Aim Rads:">Burchak:</span>
          <span id="txtAimAngle" style="font-family:var(--font-mono); color:var(--accent);">0.00 rad</span>
        </label>
      </div>
      <button class="btn btn-green" onclick="spawnTarget()" style="width:100%; margin-top:8px;" data-ru="🎯 Добавить Мишень" data-en="🎯 Spawn Target">🎯 Yangi Nishon Qo'shish</button>
      <button class="btn btn-gray" onclick="clearProjectiles()" style="width:100%; margin-top:6px;" data-ru="🔄 Очистить Осколки" data-en="🔄 Clear Sparks">🔄 Maydonni Tozalash</button>
    </div>

    <div class="box-card" style="font-family:var(--font-mono); font-size:11px; line-height:1.5;">
      <div style="color:var(--accent); font-weight:700; margin-bottom:4px;">[Real-Vaqt Formulalar]</div>
      <div style="color:#94a3b8;">dx = targetX - heroX</div>
      <div style="color:#94a3b8;">dy = targetY - heroY</div>
      <div style="color:var(--yellow);">angle = Math.atan2(dy, dx)</div>
      <div style="color:var(--green);">vx = Math.cos(angle) * speed</div>
      <div style="color:var(--green);">vy = Math.sin(angle) * speed</div>
    </div>
  </div>
</main>

<script>
var canvas = document.getElementById('simCanvas');
var ctx = canvas.getContext('2d');

var hero = { x: 400, y: 250, size: 20 };
var bullets = [];
var sparks = [];
var targets = [
  { x: 150, y: 120, size: 18, hp: 3 },
  { x: 650, y: 120, size: 18, hp: 3 },
  { x: 200, y: 380, size: 18, hp: 3 },
  { x: 600, y: 380, size: 18, hp: 3 }
];
var walls = [
  { x: 100, y: 80, w: 25, h: 340 },
  { x: 680, y: 80, w: 25, h: 340 },
  { x: 260, y: 60, w: 280, h: 25 },
  { x: 260, y: 415, w: 280, h: 25 }
];

var weaponMode = 'single';
var bulletSpeed = 12;
var kills = 0;
var currentAimAngle = 0;

function setWeapon(mode) { weaponMode = mode; }
function updateSpeed(val) { bulletSpeed = parseInt(val) || 12; }
function clearProjectiles() { bullets = []; sparks = []; }

function spawnTarget() {
  targets.push({
    x: Math.floor(Math.random() * 500) + 150,
    y: Math.floor(Math.random() * 300) + 100,
    size: 18,
    hp: 3
  });
}

canvas.addEventListener('mousemove', function(e) {
  var rect = canvas.getBoundingClientRect();
  var scaleX = canvas.width / rect.width;
  var scaleY = canvas.height / rect.height;
  var mx = (e.clientX - rect.left) * scaleX;
  var my = (e.clientY - rect.top) * scaleY;
  currentAimAngle = Math.atan2(my - hero.y, mx - hero.x);
  document.getElementById('txtAimAngle').textContent = currentAimAngle.toFixed(2) + ' rad';
});

canvas.addEventListener('pointerdown', function(e) {
  var rect = canvas.getBoundingClientRect();
  var scaleX = canvas.width / rect.width;
  var scaleY = canvas.height / rect.height;
  var tx = (e.clientX - rect.left) * scaleX;
  var ty = (e.clientY - rect.top) * scaleY;

  var baseAngle = Math.atan2(ty - hero.y, tx - hero.x);

  if (weaponMode === 'single') {
    fireBullet(baseAngle, bulletSpeed);
  } else if (weaponMode === 'shotgun') {
    [-0.18, 0, 0.18].forEach(function(offset) {
      fireBullet(baseAngle + offset, bulletSpeed);
    });
  } else if (weaponMode === 'burst') {
    for (var i = 0; i < 20; i++) {
      fireBullet((i / 20) * Math.PI * 2, bulletSpeed);
    }
  }
});

function fireBullet(angle, spd) {
  bullets.push({
    x: hero.x,
    y: hero.y,
    vx: Math.cos(angle) * spd,
    vy: Math.sin(angle) * spd,
    life: 90
  });
}

function spawnSparks(x, y, color) {
  for (var i = 0; i < 14; i++) {
    var a = Math.random() * Math.PI * 2;
    var s = Math.random() * 5 + 1;
    sparks.push({
      x: x,
      y: y,
      vx: Math.cos(a) * s,
      vy: Math.sin(a) * s,
      alpha: 1.0,
      color: color || '#f59e0b'
    });
  }
}

function loop() {
  ctx.fillStyle = '#020617';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Background Grid
  ctx.strokeStyle = 'rgba(255,255,255,0.04)';
  ctx.lineWidth = 1;
  for (var x = 0; x < canvas.width; x += 40) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
  }
  for (var y = 0; y < canvas.height; y += 40) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
  }

  // Draw Walls
  ctx.fillStyle = '#1e293b';
  ctx.strokeStyle = '#334155';
  ctx.lineWidth = 2;
  for (var w = 0; w < walls.length; w++) {
    var wl = walls[w];
    ctx.fillRect(wl.x, wl.y, wl.w, wl.h);
    ctx.strokeRect(wl.x, wl.y, wl.w, wl.h);
  }

  // Draw Targets
  for (var t = targets.length - 1; t >= 0; t--) {
    var tgt = targets[t];
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.arc(tgt.x, tgt.y, tgt.size, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#fee2e2';
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.fillStyle = '#fff';
    ctx.font = '11px sans-serif';
    ctx.fillText('HP:' + tgt.hp, tgt.x - 12, tgt.y + 4);
  }

  // Update & Draw Bullets (Reverse Loop)
  for (var bIdx = bullets.length - 1; bIdx >= 0; bIdx--) {
    var b = bullets[bIdx];
    b.x += b.vx;
    b.y += b.vy;
    b.life--;

    var hit = false;
    // Check wall hits (AABB)
    for (var wIdx = 0; wIdx < walls.length; wIdx++) {
      var wall = walls[wIdx];
      if (b.x >= wall.x && b.x <= wall.x + wall.w && b.y >= wall.y && b.y <= wall.y + wall.h) {
        hit = true;
        spawnSparks(b.x, b.y, '#f59e0b');
        break;
      }
    }

    // Check target hits
    if (!hit) {
      for (var tgIdx = targets.length - 1; tgIdx >= 0; tgIdx--) {
        var trg = targets[tgIdx];
        var d = Math.hypot(b.x - trg.x, b.y - trg.y);
        if (d < b.size + trg.size || d < trg.size + 4) {
          hit = true;
          trg.hp--;
          spawnSparks(b.x, b.y, '#ef4444');
          if (trg.hp <= 0) {
            targets.splice(tgIdx, 1);
            kills++;
            document.getElementById('hudKills').textContent = kills;
          }
          break;
        }
      }
    }

    if (hit || b.life <= 0 || b.x < 0 || b.x > canvas.width || b.y < 0 || b.y > canvas.height) {
      bullets.splice(bIdx, 1);
      continue;
    }

    // Draw Laser Bullet
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath();
    ctx.arc(b.x, b.y, 4, 0, Math.PI * 2);
    ctx.fill();

    // Laser Trail
    ctx.strokeStyle = 'rgba(56,189,248,0.5)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(b.x, b.y);
    ctx.lineTo(b.x - b.vx * 2, b.y - b.vy * 2);
    ctx.stroke();
  }

  // Update & Draw Sparks
  for (var sIdx = sparks.length - 1; sIdx >= 0; sIdx--) {
    var spk = sparks[sIdx];
    spk.x += spk.vx;
    spk.y += spk.vy;
    spk.vx *= 0.92;
    spk.vy *= 0.92;
    spk.alpha -= 0.025;

    if (spk.alpha <= 0) {
      sparks.splice(sIdx, 1);
      continue;
    }

    ctx.fillStyle = spk.color.replace(')', ', ' + spk.alpha + ')').replace('rgb', 'rgba');
    ctx.fillRect(spk.x - 1, spk.y - 1, 3, 3);
  }

  // Draw Hero with Aiming Pointer
  ctx.fillStyle = '#10b981';
  ctx.beginPath();
  ctx.arc(hero.x, hero.y, hero.size, 0, Math.PI * 2);
  ctx.fill();
  ctx.strokeStyle = '#a7f3d0';
  ctx.lineWidth = 2;
  ctx.stroke();

  // Sight laser line
  ctx.strokeStyle = 'rgba(16,185,129,0.3)';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(hero.x, hero.y);
  ctx.lineTo(hero.x + Math.cos(currentAimAngle) * 60, hero.y + Math.sin(currentAimAngle) * 60);
  ctx.stroke();

  ctx.font = '18px sans-serif';
  ctx.fillText('🧙', hero.x - 9, hero.y + 7);

  // Update HUD
  document.getElementById('hudBullets').textContent = bullets.length;
  document.getElementById('hudSparks').textContent = sparks.length;

  requestAnimationFrame(loop);
}

requestAnimationFrame(loop);
</script>

</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "simulator", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: simulator/index.html")

def main():
    print("📦 Building 7-8-sinf (Lesson 32: Ballistics & Shooting Engine)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_simulator()
    print("🎉 Done! Generated Grade 7–8 Lesson 32.")

if __name__ == "__main__":
    main()
