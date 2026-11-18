#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_7_8_w11_l32.py — Builder for 7–8th Grade, Week 11, Lesson 32

Mavzu: O'yin Fizikasi va Otishma Mexanikasi: Trigonometriya, Traektoriya va Zarrachalar
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 7-8-sinf (Vibecoding & Game Dev Track)
Pedagogika: VIBECODING — Prompt arxitekturasi, bosqichma-bosqich so'rov berish,
            xatolarni fosh qilish (critic prompt), testlash va polish.
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
        <h3 data-ru="Vibecoding va Ballistika" data-en="Vibecoding & Ballistics">Vibecoding va Ballistika</h3>
        <p data-ru="От подсказок для ИИ к точной математике: как давать промпты для захвата угла курсора и полета пуль на 60 FPS." data-en="From AI prompting to exact math: crafting prompts for 360° cursor tracking and 60 FPS projectile flight.">AI ga to'g'ri prompt berish orqali kursor burchagini ushlash va 60 FPS da ravon uchuvchi o'qlar fizikasi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Shooting Engine</div>
        <h3 data-ru="Боевой Модуль" data-en="Combat Module">Jangovar Dvigatel</h3>
        <p data-ru="Каждый ученик создаст через Vibecoding модуль прицельной стрельбы с рикошетом, частицами и защитой от утечки памяти." data-en="Each student builds an aiming shooting engine via Vibecoding with sparks, shotgun spread, and memory safety.">Har bir o'quvchi Vibecoding orqali nishonga otish, devor to'qnashuvi, uchqunlar va xotira tozalash modulini quradi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="РАЗБОР ДОМАШНЕГО ЗАДАНИЯ И МОСТ" data-en="HOMEWORK REVIEW & BRIDGE">UY VAZIFASI TAHLILI VA KO'PRIK</span></div>
    <h2 data-ru="Ошибки Процедурных Миров и Мост к Баллистике" data-en="Procedural Generation Pitfalls & Bridge to Ballistics">O'tgan Dars Xatolari va Bugungi Yangi Mavzuga Ko'prik</h2>
    <div class="grid-2">
      <div>
        <div class="box" style="border-left:4px solid var(--red); margin-bottom:10px;">
          <h4 style="color:var(--red);" data-ru="Типичная Ошибка (Pitfall): Перепутанные Аргументы atan2" data-en="Common Pitfall: Swapped atan2 Arguments">Keng Tarqalgan Xato: atan2 Argumentlari Adashishi</h4>
          <p style="font-size:12px; margin-bottom:4px;" data-ru="Многие пишут Math.atan2(dx, dy) вместо Math.atan2(dy, dx)! Из-за этого пули летели под углом 90 градусов вбок." data-en="Writing Math.atan2(dx, dy) instead of Math.atan2(dy, dx)! This causes bullets to fly sideways at a 90-degree offset.">Ko'pchilik Math.atan2(dx, dy) deb yozadi! Doimo birinchi <strong>dy</strong> (vertikal), keyin <strong>dx</strong> (gorizontal) kelishi shart: <code>Math.atan2(dy, dx)</code>.</p>
        </div>
        <div class="box" style="border-left:4px solid var(--green);">
          <h4 style="color:var(--green);" data-ru="Золотой Стандарт (Golden Standard)" data-en="Golden Standard">Oltin Yechim Standarti</h4>
          <pre style="font-size:11px; margin:0;"><code>const dx = targetX - hero.x;
const dy = targetY - hero.y;
const angle = Math.atan2(dy, dx); // To'g'ri burchak (rad)</code></pre>
        </div>
      </div>
      <div>
        <div class="box" style="background:var(--surface-2); margin-bottom:10px;">
          <h4 style="color:var(--accent);" data-ru="30-Секундный Блиц-Вопрос" data-en="30-Second Blitz Question">30 Soniyalik Blitz Savol</h4>
          <p style="font-size:12px; margin-bottom:8px;" data-ru="Курсор находится ровно справа от героя на одной линии (dy = 0, dx > 0). Чему равен угол в радианах?" data-en="The cursor is directly to the right of the hero (dy = 0, dx > 0). What is the angle in radians?">Kursor qahramonning to'g'ri o'ng tomonida (dy = 0, dx &gt; 0). Burchak necha radian bo'ladi?</p>
          <div style="font-weight:700; color:var(--green); font-size:13px;" data-ru="Ответ: 0 радиан! cos(0)=1, sin(0)=0 (полет строго вправо)." data-en="Answer: 0 radians! cos(0)=1, sin(0)=0 (flies straight right).">Javob: Aynan 0 radian! cos(0)=1, sin(0)=0 (to'g'ri o'ngga uchadi).</div>
        </div>
        <div class="box" style="border-left:4px solid var(--purple);">
          <h4 style="color:var(--purple);" data-ru="Мост к Новой Теме" data-en="Bridge to Today's Theme">Bugungi Yangi Mavzuga Ko'prik</h4>
          <p style="font-size:12px; margin:0;" data-ru="Теперь, когда в нашем лабиринте есть стены и комнаты, герою нужно оружие! Сегодня мы создадим полноценную систему прицела и стрельбы с помощью Vibecoding." data-en="Now that our dungeon has procedural rooms, the hero needs weapons! Today we engineer a complete aiming combat engine via Vibecoding.">Labirintimiz bor, endi qahramonimizga qurol kerak! Bugun Vibecoding orqali nishonga olish va otishma fizikasini quramiz.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: AIMING ARCHITECTURE -->
  <section class="slide" data-phase="Nishonga Olish|Архитектура Прицеливания|Aiming Architecture" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="АРХИТЕКТУРА СИСТЕМЫ ПРИЦЕЛИВАНИЯ" data-en="AIMING ARCHITECTURE">OTISHMA ARXITEKTURASI</span></div>
    <h2 data-ru="Координаты, Курсор и Вектор Взгляда" data-en="Coordinates, Cursor & Line of Sight">Kursor Koordinatalari va Qahramon Nigohi</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Как игра узнает, куда целится игрок? Мы соединяем две точки в 2D пространстве Canvas:" data-en="How does the game know where the player is aiming? We connect two points in 2D Canvas space:">O'yin qayerga nishonga olinganini qanday biladi? 2D Canvas maydonidagi ikki nuqta birlashtiriladi:</p>
        <ul class="clean-list">
          <li data-ru="<strong>Точка 1 (Герой):</strong> Координаты центра стрелка (hero.x, hero.y)." data-en="<strong>Point 1 (Hero):</strong> Center coordinates of shooter (hero.x, hero.y)."><strong>1-Nuqta (Qahramon):</strong> Qahramon markazi (hero.x, hero.y).</li>
          <li data-ru="<strong>Точка 2 (Курсор):</strong> Событие mousemove или pointerdown (e.clientX, e.clientY)." data-en="<strong>Point 2 (Cursor):</strong> Mouse or touch coordinates (e.clientX, e.clientY)."><strong>2-Nuqta (Kursor):</strong> Sichqoncha yoki barmoq tekkan koordinata.</li>
          <li data-ru="<strong>Дельта (Смещение):</strong> dx = targetX - hero.x, dy = targetY - hero.y." data-en="<strong>Delta (Offset):</strong> dx = targetX - hero.x, dy = targetY - hero.y."><strong>Delta (Farq):</strong> dx = targetX - hero.x, dy = targetY - hero.y.</li>
        </ul>
      </div>
      <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); font-family:var(--font-mono); font-size:12px;">
        <div style="color:var(--accent); margin-bottom:8px;">// Kursor burchagini olish</div>
        <div>window.addEventListener('mousemove', (e) =&gt; {</div>
        <div style="padding-left:14px; color:#94a3b8;">const rect = canvas.getBoundingClientRect();</div>
        <div style="padding-left:14px; color:#94a3b8;">const mouseX = e.clientX - rect.left;</div>
        <div style="padding-left:14px; color:#94a3b8;">const mouseY = e.clientY - rect.top;</div>
        <div style="padding-left:14px; color:var(--yellow);">const dx = mouseX - hero.x;</div>
        <div style="padding-left:14px; color:var(--yellow);">const dy = mouseY - hero.y;</div>
        <div style="padding-left:14px; color:var(--green);">hero.angle = Math.atan2(dy, dx);</div>
        <div>});</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: MATH.ATAN2 DEEP DIVE -->
  <section class="slide" data-phase="Math.atan2|Функция Math.atan2|Math.atan2" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="ГЕОМЕТРИЯ КРУГА И РАДИАНЫ" data-en="CIRCLE GEOMETRY & RADIANS">TRIGONOMETRIYA VA RADIANLAR</span></div>
    <h2 data-ru="Магия Math.atan2: Круговой Охват 360 Градусов" data-en="The Magic of Math.atan2: Full 360-Degree Radians">Math.atan2 Sehri: 360 Darajali Doiraviy Radianlar</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="В отличие от старого Math.atan(y/x), функция Math.atan2(dy, dx) автоматически учитывает знаки X и Y:" data-en="Unlike legacy Math.atan(y/x), Math.atan2(dy, dx) natively distinguishes all 4 quadrants:">Oddiy atan(y/x) nolga bo'lish xatosiga uchraydi. Math.atan2(dy, dx) esa barcha 4 chorakni to'liq qamrab oladi:</p>
        <ul class="clean-list">
          <li data-ru="<strong>Диапазон:</strong> Возвращает угол в радианах от -PI (-3.14) до +PI (+3.14)." data-en="<strong>Range:</strong> Returns radians spanning from -PI (-3.14) to +PI (+3.14)."><strong>Diapazon:</strong> -PI (-3.14) dan +PI (+3.14) gacha radianlar.</li>
          <li data-ru="<strong>0 радиан:</strong> Смотрит строго вправо (восток)." data-en="<strong>0 radians:</strong> Directly facing East (right)."><strong>0 rad:</strong> To'g'ri o'ngga qarash (sharq).</li>
          <li data-ru="<strong>PI / 2 (1.57 rad):</strong> Смотрит строго вниз (юг в экранных координатах)." data-en="<strong>PI / 2 (1.57 rad):</strong> Facing straight Down (Canvas Y is inverted)."><strong>PI/2 rad:</strong> To'g'ri pastga qarash (Canvas da Y pastga qarab o'sadi).</li>
          <li data-ru="<strong>-PI / 2 (-1.57 rad):</strong> Смотрит строго вверх (север)." data-en="<strong>-PI / 2 (-1.57 rad):</strong> Facing straight Up (north)."><strong>-PI/2 rad:</strong> To'g'ri yuqoriga qarash (shimol).</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
        <div style="font-size:48px; margin-bottom:8px;">🎯 📐 ⭕</div>
        <h4 data-ru="Координатная Особенность Canvas" data-en="Canvas Coordinate Quirk">Canvas Koordinata Xususiyati</h4>
        <p style="font-size:12px; color:var(--ink-2); max-width:280px; margin:0;" data-ru="Внимание! На экранах компьютеров ось Y направлена ВНИЗ, а не вверх как в школьной тетради!" data-en="Note! On computer screens, Y points DOWNWARDS, opposite of standard school math notebooks!">Ekranda Y o'qi pastga qarab o'sadi! Shuning uchun dy musbat bo'lsa, kursor pastda joylashgan bo'ladi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: VELOCITY VECTORS (COS & SIN) -->
  <section class="slide" data-phase="Vektorlar|Векторы Скорости|Velocity Vectors" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="РАЗЛОЖЕНИЕ СКОРОСТИ НА ВЕКТОРЫ" data-en="VELOCITY DECOMPOSITION">TEZLIK VEKTORLARI (COS VA SIN)</span></div>
    <h2 data-ru="Как Запустить Пулю: vx = cos(a) * speed, vy = sin(a) * speed" data-en="Launching the Projectile: vx = cos(a) * speed, vy = sin(a) * speed">O'qni Uchirish: cos va sin Orqali Tezlik Vektorlari</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Чтобы пуля летела на постоянной скорости под любым углом, мы раскладываем скорость на горизонтальную и вертикальную составляющие:" data-en="To propel projectiles at constant speed regardless of angle, decompose velocity into X and Y components:">O'q istalgan burchakda bir xil doimiy tezlikda uchishi uchun tezlik ikki vektorga bo'linadi:</p>
        <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); font-family:var(--font-mono); font-size:12px; margin-bottom:10px;">
          <div style="color:var(--accent);">// O'q obyektini yaratish</div>
          <div>const speed = 12; // Piksel/freym</div>
          <div style="color:var(--green);">const vx = Math.cos(angle) * speed;</div>
          <div style="color:var(--green);">const vy = Math.sin(angle) * speed;</div>
          <div style="margin-top:6px; color:#94a3b8;">bullets.push({ x: hero.x, y: hero.y, vx, vy });</div>
        </div>
      </div>
      <div>
        <div class="box" style="margin-bottom:10px;">
          <h4 data-ru="Почему Нельзя Просто x += speed?" data-en="Why Not Simple x += speed?">Nega Oddiy x += speed Ishlamaydi?</h4>
          <p style="font-size:12px; margin:0;" data-ru="Без тригонометрии пули могли бы лететь только по 4 или 8 сторонам, а по диагонали летели бы в 1.41 раза быстрее (теорема Пифагора)!" data-en="Without trigonometry, bullets are locked to 4/8 axes and diagonal movement is 1.41x faster!">Trigonometriyalarsiz o'qlar faqat 4 tomonga ucha oladi va diagonallar 1.41 barobar tezroq bo'lib ketadi.</p>
        </div>
        <div class="box" style="border-left:4px solid var(--accent);">
          <h4 data-ru="Обновление в Игровом Цикле" data-en="Game Loop Update">O'yin Tsiklida Harakat</h4>
          <p style="font-size:12px; margin:0;" data-ru="Каждый кадр (60 раз в секунду): bullet.x += bullet.vx; bullet.y += bullet.vy;" data-en="Every single frame (60 FPS): bullet.x += bullet.vx; bullet.y += bullet.vy;">Har bir freymda (60 FPS): bullet.x += bullet.vx; bullet.y += bullet.vy;</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: MEMORY CLEANUP & REVERSE LOOP -->
  <section class="slide" data-phase="Xotirani Tozalash|Очистка Памяти|Memory Cleanup" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ЗАЩИТА ОТ УТЕЧЕК ПАМЯТИ" data-en="MEMORY LEAK GUARD">XOTIRA XAVFSIZLIGI VA TOZALASH</span></div>
    <h2 data-ru="Ловушка splice(): Почему Цикл Должен Идти с Конца?" data-en="The splice() Trap: Why Arrays Must Be Traversed Backwards">splice() Tuzog'i: Nega Teskari Sikl Ishlatiladi?</h2>
    <div class="grid-2">
      <div>
        <div class="box" style="border-left:4px solid var(--red); margin-bottom:10px;">
          <h4 style="color:var(--red);" data-ru="Катастрофа: Утечка Памяти (Memory Leak)" data-en="Disaster: Memory Leak">Katta Xato: Xotira Oqishi (Memory Leak)</h4>
          <p style="font-size:12px; margin:0;" data-ru="Если пули не удалять при улете за экран, массив bullets вырастет до 10 000+ элементов. Игра зависнет через 2 минуты!" data-en="If off-screen bullets aren't spliced, bullets array balloons past 10,000+ items, crashing the browser!">Ekrandan chiqqan o'qlar o'chirib tashlanmasa, massiv minglab oshib ketadi va o'yin qotib qoladi!</p>
        </div>
        <div class="box" style="border-left:4px solid var(--yellow);">
          <h4 style="color:var(--yellow);" data-ru="Ловушка Прямого Цикла (Index Shift)" data-en="Forward Loop Index Shift Bug">To'g'ri Sikl Tuzog'i (Indeks Surilishi)</h4>
          <p style="font-size:12px; margin:0;" data-ru="Если удалять через bullets.splice(i, 1) в обычном цикле от 0 до length, следующий элемент сдвигается на место i и пропускается!" data-en="Deleting via splice(i, 1) during forward loop skips adjacent items due to index recalculation!">Oddiy 0 dan length gacha siklda bitta o'q o'chirilsa, keyingi o'q tekshirilmay o'tib ketadi!</p>
        </div>
      </div>
      <div>
        <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); font-family:var(--font-mono); font-size:12px;">
          <div style="color:var(--green); margin-bottom:6px;">// Oltin Yechim: Teskari Sikl (Reverse Loop)</div>
          <div style="color:var(--accent);">for (let i = bullets.length - 1; i &gt;= 0; i--) {</div>
          <div style="padding-left:14px;">const b = bullets[i];</div>
          <div style="padding-left:14px;">b.x += b.vx; b.y += b.vy;</div>
          <div style="padding-left:14px; margin-top:4px; color:#94a3b8;">// Agar ekrandan chiqsa yoki devorga urilsa:</div>
          <div style="padding-left:14px; color:var(--red);">if (isOutOfBounds(b) || checkWallHit(b)) {</div>
          <div style="padding-left:28px; color:var(--yellow);">createSparks(b.x, b.y);</div>
          <div style="padding-left:28px; color:var(--green);">bullets.splice(i, 1); // Xavfsiz o'chirish!</div>
          <div style="padding-left:14px; color:var(--red);">}</div>
          <div style="color:var(--accent);">}</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: PARTICLE SPARKS & GAME JUICE -->
  <section class="slide" data-phase="Zarrachalar|Система Частиц|Particle Sparks" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ЭФФЕКТЫ СОЧНОСТИ: GAME JUICE" data-en="GAME JUICE & FX">ZARRACHALAR TIZIMI VA O'YIN SHIRASI</span></div>
    <h2 data-ru="Искры при Попадании: Физика Затухания и Трения" data-en="Sparks upon Impact: Drag & Alpha Fadeout">Devorga Urilishdagi Uchqunlar: Friktsiya va Shaffoflik</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);">1. Sachrash</div>
        <h4 data-ru="Случайный Взрыв" data-en="Random Scatter">Tasodifiy Sachrash</h4>
        <p style="font-size:12px;" data-ru="При ударе пули о стену создаем 8–12 частиц с произвольным углом (Math.random() * PI * 2)." data-en="On wall impact, instantiate 8–12 particles with random radians (Math.random() * PI * 2).">O'q urilganda har tomonga tasodifiy burchakda 8-12 ta mayda zarracha sachraydi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(245,158,11,0.15); color:var(--yellow);">2. Tormozlanish</div>
        <h4 data-ru="Трение Воздуха" data-en="Air Friction (0.92)">Friktsiya (Tormozlanish)</h4>
        <p style="font-size:12px;" data-ru="Каждый кадр: p.vx *= 0.92; p.vy *= 0.92; Искры плавно замедляются и останавливаются." data-en="Every frame: p.vx *= 0.92; p.vy *= 0.92; Sparks naturally decelerate.">Har freymda zarracha tezligi 0.92 ga ko'paytiriladi, natijada ular tez tormozlanadi.</p>
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

  <!-- SLIDE 10: 25-MIN VIBECODING ARENA -->
  <section class="slide" data-phase="Amaliy Arena|Практическая Арена|Hands-on Arena" data-time="55:00–70:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="VIBECODING АРЕНА (25 МИНУТ)" data-en="VIBECODING ARENA (25 MIN)">VIBECODING AMALIY ARENASI (25 DAQIQA)</span></div>
    <h2 data-ru="Vibecoding: 4 Шага Создания Баллистики с ИИ" data-en="Vibecoding: 4 Real Steps to Engineer Ballistics with AI">Vibecoding: AI ga 4 Bosqichda Aniq So'rov Berish va Sinash</h2>
    <div class="grid-2">
      <div>
        <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
          <button class="btn" id="arenaTimerBtn" onclick="toggleArenaTimer()" style="background:var(--accent); color:#fff; font-weight:700;" data-ru="⏱️ Запустить Таймер" data-en="⏱️ Start Timer">⏱️ Taymerni Boshlash</button>
          <span id="arenaTimerDisplay" style="font-family:var(--font-mono); font-size:24px; font-weight:700; color:var(--red);">25:00</span>
        </div>
        <p class="lede" style="font-size:13px; margin-bottom:8px;" data-ru="Не пишите код вручную — будьте AI-Архитекторами! Выполните 4 конкретных промпт-шага:" data-en="Don't code manually — act as AI Architects! Execute the 4 concrete prompting milestones:">Kodni qo'lda yozib o'tirmang — AI Arxitektor bo'ling! 4 ta aniq Vibecoding bosqichini bajaring:</p>
        <ul class="clean-list" style="font-size:12px;">
          <li data-ru="<strong>1-й Шаг (6 мин):</strong> Промпт контекста и прицела: даем ИИ структуру игры и просим функцию shoot() на Math.atan2." data-en="<strong>Step 1 (6 min):</strong> Context & Aiming Prompt: feed game context to AI and request shoot() via Math.atan2."><strong>1-Qadam (6 min):</strong> Kontekst va Otishma Prompti — AI ga o'yinimizni tushuntirib, 360° nishonga oluvchi <code>shoot()</code> funksiyasini so'rash.</li>
          <li data-ru="<strong>2-й Шаг (6 мин):</strong> Интеграция и первый тест: вставляем код и проверяем полет пуль во всех 4 направлениях." data-en="<strong>Step 2 (6 min):</strong> Integration & Test: inject code and verify bullets fly precisely to cursor in all 4 quadrants."><strong>2-Qadam (6 min):</strong> Integratsiya va Birinchi Sinov — AI kodini o'rnatib, barcha 4 chorakda otib ko'rish.</li>
          <li data-ru="<strong>3-й Шаг (7 мин):</strong> Промпт исправления утечки памяти (Critic): просим ИИ сделать обратный цикл splice() для исчезновения пуль." data-en="<strong>Step 3 (7 min):</strong> Critic Bug-Fix Prompt: ask AI for reverse loop splice() to prevent memory leaks and wall tunneling."><strong>3-Qadam (7 min):</strong> Xatolikni AI bilan Tuzatish (Critic Prompt) — O'qlar o'chmayotganini aytib, teskari <code>splice()</code> siklini talab qilish.</li>
          <li data-ru="<strong>4-й Шаг (6 мин):</strong> Промпт эффектов (Juice): просим вспышки искр (частицы с friction 0.92) и режим дробовика!" data-en="<strong>Step 4 (6 min):</strong> Juice & Weapon Polish: prompt AI for impact spark particles (friction 0.92) and 3-way shotgun spread! "><strong>4-Qadam (6 min):</strong> Vibe-Juice va Qurollar — Devorga urilganda uchqunlar (particles) va 3-talik Drobovik rejimini so'rash!</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="font-weight:700; color:var(--accent); margin-bottom:6px;" data-ru="Критерии Оценки (10 Баллов):" data-en="10 Points Rubric:">10 Ballik Baholash Rubrikasi:</div>
          <div style="font-size:11px; line-height:1.6;">
            <div>✅ <strong>4 Ball:</strong> AI ga to'g'ri arxitektura prompti berilgan va o'qlar kursor tomon to'g'ri uchadi.</div>
            <div>✅ <strong>4 Ball:</strong> Xotira oqishi (Memory Leak) tuzatilgan: teskari <code>splice()</code> bilan devorga urilgan o'qlar xotiradan tozalanadi.</div>
            <div>✅ <strong>2 Ball:</strong> Zarrachalar (uchqunlar) yoki Drobovik rejimi muvaffaqiyatli ulangan!</div>
          </div>
        </div>
        <div style="margin-top:10px; text-align:right;">
          <a href="simulator/index.html" target="_blank" class="btn" style="background:var(--purple); color:#fff; font-size:11px;" data-ru="Открыть Студию Баллистики" data-en="Launch Ballistics Studio">Katta Vibecoding Studiyasini Ochish ➔</a>
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
        <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);">2-Daraja (Loyiha)</div>
        <h4 data-ru="Очистка Памяти и Стены (4 Балла)" data-en="Memory Cleanup & Walls (4 Points)">Xotirani Tozalash (4 Ball)</h4>
        <p style="font-size:12px;" data-ru="Добавьте проверку коллизий с препятствиями и безопасное удаление через обратный цикл splice()." data-en="Add obstacle collision detection and safe reverse loop array splicing.">Devorga urilganda to'xtash va teskari for-loop yordamida o'qlarni xotiradan tozalash.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">3-Daraja (Kiber-Chaqiruv)</div>
        <h4 data-ru="Искры или Рикошет (2 Балла)" data-en="Sparks or Ricochet (2 Points)">Uchqunlar / Rikoshet (2 Ball)</h4>
        <p style="font-size:12px;" data-ru="Создайте эффект искр при ударе или заставьте пули отскакивать от стен!" data-en="Create impact spark particles or implement a wall bouncing ricochet mechanic!">Zarba joyida 10 ta uchqun sochish yoki o'qlarni devordan sakrab rikoshet qilishini yarating!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И МОСТ" data-en="SUMMARY & BRIDGE">XULOSA VA KEYINGI DARS</span></div>
    <h2 data-ru="Чему Мы Научились: Тригонометрия в Действии" data-en="What We Engineered: Trigonometry in Action">Otishma Fizikasi Xulosasi va Keyingi Bosqich</h2>
    <div class="grid-2">
      <div>
        <ul class="clean-list">
          <li data-ru="<strong>Math.atan2(dy, dx):</strong> Точный расчет угла между любыми двумя точками 2D пространства." data-en="<strong>Math.atan2(dy, dx):</strong> Exact radian computation between any 2 coordinates in 2D space."><strong>Math.atan2(dy, dx):</strong> Istalgan 2 nuqta orasidagi aniq burchak.</li>
          <li data-ru="<strong>cos & sin:</strong> Разложение постоянной скорости на оси X и Y." data-en="<strong>cos & sin:</strong> Velocity vector decomposition along X and Y axes."><strong>cos & sin:</strong> Tezlikni gorizontal va vertikal harakatga ajratish.</li>
          <li data-ru="<strong>Обратный цикл:</strong> Защита от зависания браузера и сдвига индексов при удалении." data-en="<strong>Reverse loop:</strong> Zero-leak memory safety via length-1 to 0 index traversing."><strong>Teskari sikl:</strong> Xotira to'lib qolishi va indeks surilishidan himoya.</li>
          <li data-ru="<strong>Частицы (Sparks):</strong> Физика сочности: случайный угол, трение 0.92 и альфа-затухание." data-en="<strong>Particles (Sparks):</strong> Game juice mechanics: random scatter, 0.92 friction, and alpha fadeout."><strong>Zarrachalar:</strong> O'yin shirasini beruvchi sochilish, friktsiya va so'nish.</li>
        </ul>
      </div>
      <div class="box" style="border-left:4px solid var(--accent); display:flex; flex-direction:column; justify-content:center;">
        <h4 data-ru="Следующий Урок: ИИ Врагов и Погоня" data-en="Next Lesson: Enemy AI & Pathfinding">Keyingi Dars: Dushman AI va Pathfinding</h4>
        <p style="font-size:12px; margin:0;" data-ru="На следующем уроке мы заставим монстров подземелья вычислять кратчайший путь к герою в обход стен (алгоритм A* и поиск в ширину BFS)!" data-en="Next lesson we program dungeon monsters to calculate shortest paths towards the player around solid walls (A* and BFS algorithms)!">Keyingi darsda labirint dushmanlari tosh devorlarni aylanib o'tib, qahramonni quvlashini dasturlaymiz (A* va BFS qidiruv algoritmlari)!</p>
      </div>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. IN-DECK SIMULATOR SCRIPT
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
var deckB_canvas, deckB_ctx;
var deckB_hero = { x: 230, y: 125, size: 14 };
var deckB_bullets = [];
var deckB_sparks = [];
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

    deckB_ctx.fillStyle = '#38bdf8';
    deckB_ctx.shadowColor = '#38bdf8';
    deckB_ctx.shadowBlur = 6;
    deckB_ctx.beginPath();
    deckB_ctx.arc(b.x, b.y, 3, 0, Math.PI * 2);
    deckB_ctx.fill();
    deckB_ctx.shadowBlur = 0;
  }

  // Update & Draw Sparks
  for (var s = deckB_sparks.length - 1; s >= 0; s--) {
    var sp = deckB_sparks[s];
    sp.x += sp.vx;
    sp.y += sp.vy;
    sp.vx *= 0.92;
    sp.vy *= 0.92;
    sp.alpha -= 0.03;

    if (sp.alpha <= 0) {
      deckB_sparks.splice(s, 1);
      continue;
    }

    deckB_ctx.fillStyle = 'rgba(245, 158, 11, ' + sp.alpha + ')';
    deckB_ctx.beginPath();
    deckB_ctx.arc(sp.x, sp.y, 2, 0, Math.PI * 2);
    deckB_ctx.fill();
  }

  // Draw Hero
  deckB_ctx.fillStyle = '#10b981';
  deckB_ctx.beginPath();
  deckB_ctx.arc(deckB_hero.x, deckB_hero.y, deckB_hero.size / 2, 0, Math.PI * 2);
  deckB_ctx.fill();

  // HUD
  var elB = document.getElementById('deckBulletCount');
  var elS = document.getElementById('deckSparkCount');
  if (elB) elB.textContent = deckB_bullets.length;
  if (elS) elS.textContent = deckB_sparks.length;
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
        alert('Vaqt tugadi! Endi partadoshingiz kodini audit qiling!');
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
  initDeckBallistics();
});
"""

# Teacher Notes Data
NOTES_DATA = {
    "uz": [
        ["Kirish va Maqsad", "80 daqiqalik juftlik dars rejasi. Bugun o'quvchilar Roguelike o'yiniga to'liq nishonga olish va otishma tizimini Vibecoding orqali integratsiya qilishadi.", "Doskaga Math.atan2 va cos/sin koordinata chizmasini chizing."],
        ["Uy Vazifasi Tahlili", "dy va dx tartibi adashishi keng tarqalgan xato. Math.atan2(dy, dx) tartibini eslatib o'ting.", "30 soniyalik blits savol bering: dy=0, dx>0 bo'lganda burchak 0 radian bo'ladi."],
        ["Nishonga Olish Arxitekturasi", "Kursor koordinatalari va delta masofa: ekranda sichqoncha voqealari (mousemove) va qahramon markazini hisoblashni tushuntiring.", "e.clientX - rect.left formulasi."],
        ["Trigonometriya: Math.atan2", "Radianlar aylanasi (-PI dan +PI gacha). Nega Canvas da Y o'qi pastga qaraganini vizual tarzda ko'rsating.", "Har bir chorak uchun burchak belgilarini tahlil qiling."],
        ["Tezlik Vektorlari: cos va sin", "Gipotenuza har doim speed (doimiy tezlik) ga teng bo'lishini tushuntiring.", "vx = Math.cos(angle) * speed va vy = Math.sin(angle) * speed."],
        ["Xotira Xavfsizligi va Tozalash", "Eng muhim muhandislik nuqtasi! splice() to'g'ri siklda indekslarni surib yuborishini va o'yin qotib qolishini ko'rsating.", "Oltin yechim: teskari for-loop (length-1 dan 0 gacha)."],
        ["Zarrachalar Tizimi / Game Juice", "O'q shunchaki g'oyib bo'lmasligi, balki 8-12 ta uchqun sochilib, friktsiya (0.92) bilan tormozlanib so'nishi o'yin hissiyotini beradi.", "Alpha shaffoflik so'nishi."],
        ["Smartboard Simulyatori", "Taqdimot ichidagi simulyatorda barmoq bilan otish va 360 salyutni sinatib ko'ring.", "O'quvchilarni doskaga chaqiring."],
        ["Kiber-Viktorina", "3 ta nazorat savoli bo'yicha tezkor viktorina o'tkazing.", "Har bir javobni tahlil qiling va qoidani mustahkamlang."],
        ["Vibecoding Amaliy Arenasi", "25 daqiqalik amaliyot: o'quvchilar qo'lda kod yozmaydi, AI ga aniq 4 bosqichli prompt beradi va test qiladi.", "Xotira oqishini bartaraf etish critic promptiga e'tibor qarating."],
        ["Partadosh Auditi", "Partadoshlar o'rin almashib, 4 ta mezon bo'yicha otishmani sinashadi.", "Do'stona yordam va kiber-tekshiruv."],
        ["Katta Ekran Showcasi", "Eng qiziqarli qurollar (drobovik, rikoshet) ni katta doskaga chiqarib ko'rsating.", "Mualliflarni olqishlang."],
        ["3 Darajali Uy Vazifasi", "10 ballik uy vazifasi shartlarini tushuntiring (4 + 4 + 2).", "Mustaqil dasturlash va kiber-chaqiruv."],
        ["Xulosa va Keyingi Dars", "Darsni sarhisob qiling va keyingi darsda dushman AI va A* qidiruv algoritmini o'rganamiz deb e'lon qiling.", "O'quvchilar savollariga javob bering."]
    ],
    "ru": [
        ["Введение и Цель", "План сдвоенного урока (80 минут). Сегодня ученики интегрируют баллистику в Roguelike через Vibecoding.", "Нарисуйте на доске формулы Math.atan2 и cos/sin."],
        ["Разбор Домашнего Задания", "Порядок dy и dx: типичная ошибка. Напомните порядок Math.atan2(dy, dx).", "30-секундный блиц: при dy=0, dx>0 угол равен 0 радиан."],
        ["Архитектура Прицеливания", "Координаты курсора и дельта-смещение: разберите захват mousemove и центр героя.", "Формула e.clientX - rect.left."],
        ["Тригонометрия: Math.atan2", "Круговой диапазон радианов (от -PI до +PI). Объясните инверсию оси Y на Canvas.", "Разберите знаки углов во всех 4 четвертях."],
        ["Векторы Скорости: cos и sin", "Гипотенуза всегда равна постоянной скорости speed.", "vx = Math.cos(angle) * speed и vy = Math.sin(angle) * speed."],
        ["Очистка Памяти и Безопасность", "Критическая точка! Покажите сдвиг индексов при прямом цикле splice() и утечку памяти.", "Золотой стандарт: обратный цикл (от length-1 до 0)."],
        ["Система Частиц / Game Juice", "Физика сочности: 8-12 искр, трение 0.92 и затухание прозрачности (alpha).", "Удаление угасших частиц из массива."],
        ["Интерактив на Смартборде", "Протестируйте стрельбу на интерактивной доске пальцем и запустите круговой салют.", "Вызовите учеников к доске."],
        ["Кибер-Квиз", "Быстрый квиз из 3 контрольных вопросов по физике снарядов.", "Разберите каждый ответ."],
        ["Арена Vibecoding (25 минут)", "Ученики формулируют 4 четких промпта для ИИ и тестируют код в реальном времени.", "Контролируйте critic-промпт защиты от утечки памяти."],
        ["Взаимный Аудит", "Ученики меняются местами и тестируют физику стрельбы одноклассника по 4 критериям.", "Взаимопомощь и поиск багов."],
        ["Шоукейс на Доске", "Продемонстрируйте лучшие виды оружия (дробовик, рикошет) на смартборде.", "Похвалите авторов."],
        ["3 Уровня Домашнего Задания", "Объясните 10-балльную систему оценивания (4 + 4 + 2).", "Самостоятельная работа и вызов."],
        ["Итоги и Мост", "Подведите итоги и анонсируйте следующий урок: ИИ врагов и поиск пути A*.", "Ответьте на вопросы."]
    ],
    "en": [
        ["Intro & Objectives", "80-minute double block pacing. Today students integrate a ballistics combat module via Vibecoding.", "Diagram Math.atan2 and cos/sin velocity vectors on the board."],
        ["Homework Review", "Swapped dy and dx: common pitfall. Emphasize Math.atan2(dy, dx) order.", "30-second blitz: when dy=0, dx>0 angle equals 0 radians."],
        ["Aiming Architecture", "Cursor coordinates and delta offset: explain mousemove capture and hero center.", "Formula e.clientX - rect.left."],
        ["Trigonometry: Math.atan2", "Full 360-degree radian range (-PI to +PI). Explain why Canvas Y points downwards.", "Analyze quadrant signs."],
        ["Velocity Vectors: cos & sin", "Hypotenuse always matches constant projectile speed.", "vx = Math.cos(angle) * speed and vy = Math.sin(angle) * speed."],
        ["Memory Safety & Cleanup", "Crucial milestone! Demonstrate array index shifting and memory leaks during forward loops.", "Golden standard: reverse loop (length-1 down to 0)."],
        ["Particle Sparks & Juice", "Juicy game feel: 8-12 scatter sparks, 0.92 drag, and alpha fadeout.", "Purging dead particles from memory."],
        ["Smartboard Interactive", "Test touch aiming directly on the smartboard and trigger 360 burst.", "Invite students to the board."],
        ["Cyber Quiz", "Fast 3-question assessment on projectile physics and array cleanup.", "Analyze each response."],
        ["Vibecoding Arena (25 min)", "Students act as AI Architects: issuing 4 structured prompts and verifying code live.", "Enforce memory leak critic prompt."],
        ["Peer Audit", "Students swap seats and audit peer ballistics across 4 checkpoints.", "Peer debugging and support."],
        ["Showcase", "Demonstrate outstanding weapons (shotgun spread, ricochet) on the big screen.", "Praise students."],
        ["Tiered Homework", "Explain 10-point rubric criteria (4 + 4 + 2).", "Independent challenge."],
        ["Summary & Bridge", "Summarize learnings and announce next lesson: Enemy AI & A* Pathfinding.", "Q&A session."]
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

    replacements = {
        "{{LESSON_NUM}}": "32",
        "{{TITLE_UZ}}": "O'yin Fizikasi va Otishma Mexanikasi: Trigonometriya, Traektoriya va Zarrachalar",
        "{{TITLE_RU}}": "Физика Игры и Механика Стрельбы: Тригонометрия, Траектории и Частицы",
        "{{TITLE_EN}}": "Game Physics & Ballistics: Trigonometry, Trajectories & Particles",
        "{{COHORT_LABEL_UZ}}": "7–8-SINF",
        "{{COHORT_LABEL_RU}}": "7–8 КЛАСС",
        "{{COHORT_LABEL_EN}}": "GRADES 7–8",
        "{{META_UZ}}": "11-Hafta · Juftlik Dars (80 daqiqa) · Vibecoding & Creative Coding Track",
        "{{META_RU}}": "11-я Неделя · Сдвоенный Урок (80 минут) · Направление Vibecoding",
        "{{META_EN}}": "Week 11 · Double Block (80 min) · Vibecoding & Creative Coding Track",
        "{{MISSION_UZ}}": "HTML5 Canvas o'yiniga to'liq nishonga olish va otishma mexanikasini kiritish: Math.atan2 orqali kursor burchagini topish, cos/sin vektorlari bilan o'qlarni uchirish, teskari sikl orqali xotira oqishini (Memory Leak) bartaraf etish va to'qnashuvda neon zarrachalar sochilishini Vibecoding orqali amalga oshirish.",
        "{{MISSION_RU}}": "Интегрировать в HTML5 Canvas полноценную систему баллистики: захват угла курсора через Math.atan2, полет пуль по векторам cos/sin, устранение утечки памяти через обратный цикл и вспышки частиц при попадании.",
        "{{MISSION_EN}}": "Engineer a complete Canvas ballistics engine: targeting cursor angle via Math.atan2, launching projectiles along cos/sin vectors, eliminating memory leaks via reverse loops, and sparking particle bursts upon wall impact.",
        "{{SEC1_TITLE_UZ}}": "Otishma Fizikasining 4 Asosiy Ustuni (Trigonometriya va Vektorlar)",
        "{{SEC1_TITLE_RU}}": "4 Математических Столпа Баллистики (Тригонометрия и Векторы)",
        "{{SEC1_TITLE_EN}}": "4 Mathematical Pillars of Ballistics (Trigonometry & Vectors)",
        "{{SEC1_CONTENT}}": """
    <div style="background:var(--panel); padding:8px; border-radius:4px; font-size:9pt; line-height:1.45;">
      <div style="font-weight:700; color:var(--accent-ink); margin-bottom:4px;" data-ru="Ключевые формулы баллистики в 2D пространстве:" data-en="Key 2D ballistics formulas:">2D fazoda asosiy otishma formulalari:</div>
      <div>1. <strong>Delta masofa:</strong> <code>dx = mouseX - hero.x</code>, <code>dy = mouseY - hero.y</code></div>
      <div>2. <strong>Burchak:</strong> <code>angle = Math.atan2(dy, dx)</code> (-PI dan +PI gacha radianlar)</div>
      <div>3. <strong>Harakat vektorlari:</strong> <code>vx = Math.cos(angle) * speed</code>, <code>vy = Math.sin(angle) * speed</code></div>
      <div>4. <strong>Xotirani tozalash:</strong> <code>for (let i = bullets.length - 1; i >= 0; i--) bullets.splice(i, 1);</code></div>
    </div>
        """,
        "{{SEC2_TITLE_UZ}}": "Vibecoding Prompt Shabloni: AI ga To'g'ri Buyruq Berish",
        "{{SEC2_TITLE_RU}}": "Шаблон Промпта Vibecoding: Правильная Постановка Задачи ИИ",
        "{{SEC2_TITLE_EN}}": "Vibecoding Prompt Template: Structured AI Request",
        "{{SEC2_CONTENT}}": """
    <p style="font-size:8.8pt; margin:4px 0;" data-ru="Эффективный AI-промпт состоит из 4 обязательных частей:" data-en="An effective AI prompt consists of 4 mandatory components:">Professional Vibecoding prompti 4 qismdan tashkil topadi:</p>
    <div style="background:var(--panel-2); border-left:3px solid var(--accent); padding:6px 8px; font-size:8.5pt; line-height:1.4;">
      <div>🎯 <strong>[Rol]:</strong> "Sen tajribali 2D HTML5 Canvas o'yin dasturchisisan."</div>
      <div>📦 <strong>[Kontekst]:</strong> "Menda hero {x, y} obyektli va requestAnimationFrame li o'yinim bor."</div>
      <div>⚙️ <strong>[Vazifa]:</strong> "Sichqoncha bosilgan tomonga Math.atan2 orqali 360° nishonga olib o'q otuvchi shoot() funksiyasini yoz."</div>
      <div>🛡️ <strong>[Cheklovlar]:</strong> "Ekrandan chiqqan o'qlarni orqadan oldinga (reverse loop) splice bilan tozala, xotira oqmasin."</div>
    </div>
        """,
        "{{SEC3_TITLE_UZ}}": "Amaliy Vibecoding Protokoli (Laboratoriya Rejasi)",
        "{{SEC3_TITLE_RU}}": "Практический Протокол Vibecoding (План Лабораторной)",
        "{{SEC3_TITLE_EN}}": "Hands-on Vibecoding Protocol (Lab Checklist)",
        "{{SEC3_CONTENT}}": """
    <div style="font-size:8.8pt; line-height:1.45;">
      <p style="margin:2px 0 6px;" data-ru="Выполните 4 практических шага в редакторе кода с вашим ИИ-ассистентом:" data-en="Execute the 4 practical milestones in your code editor with your AI assistant:">Kodni qo'lda yozmang — AI bilan 4 ta aniq Vibecoding qadamini bajaring:</p>
      <div style="border:1px solid var(--rule); border-radius:4px; padding:6px 8px; margin-bottom:6px; background:var(--panel);">
        <strong>[Qadam 1] Otishma Prompti:</strong> AI ga o'yin kontekstini bering va burchak bo'yicha uchuvchi o'q funksiyasini oling. <em>Tekshiruv:</em> 4 ta chorakda o'qlar to'g'ri kursor tomon uchayaptimi? [ &nbsp; ] Bajarildi
      </div>
      <div style="border:1px solid var(--rule); border-radius:4px; padding:6px 8px; margin-bottom:6px; background:var(--panel);">
        <strong>[Qadam 2] Xotira Oqishini Fosh Qilish (Critic):</strong> O'qlar o'chmasdan massiv kattalashayotganini AI ga ayting va teskari <code>for (let i = bullets.length - 1; i >= 0; i--)</code> so'rang. [ &nbsp; ] Bajarildi
      </div>
      <div style="border:1px solid var(--rule); border-radius:4px; padding:6px 8px; margin-bottom:6px; background:var(--panel);">
        <strong>[Qadam 3] Vibe-Juice (Zarrachalar):</strong> O'q tosh devorga urilganda 10 ta uchqun sochilishini va shaffoflik (alpha) so'nishini qo'shing. [ &nbsp; ] Bajarildi
      </div>
      <div style="border:1px solid var(--rule); border-radius:4px; background:var(--panel);">
        <strong>[Qadam 4] Qurol Turlari (Challenge):</strong> 3-talik yelpig'ich Drobovik (Shotgun) yoki 360° kiber-salьyut otish rejimini prompt orqali yarating. [ &nbsp; ] Bajarildi
      </div>
    </div>
        """,
        "{{SEC4_CONTENT}}": """
    <div style="font-size:8.6pt; line-height:1.4; margin-top:6px;">
      <div style="margin-bottom:6px;">
        <strong>1-Daraja: Baza (4 ball):</strong> Math.atan2 va cos/sin orqali yakka lazer uzuvchi toza kodni sharhlab bering.
      </div>
      <div style="margin-bottom:6px;">
        <strong>2-Daraja: Amaliyot (4 ball):</strong> Tosh devorlar bilan to'qnashuv va teskari siklda xotirani tozalash mexanizmini to'liq ishga tushiring.
      </div>
      <div style="margin-bottom:6px;">
        <strong>3-Daraja: Kiber-Chaqiruv (2 ball):</strong> Zarba joyida neon uchqunlar sochilishini yoki devordan rikoshet qilishini integratsiya qiling.
      </div>
      <div style="border-top:1px dashed var(--rule); padding-top:4px; font-weight:700; color:var(--accent-ink); display:flex; justify-content:space-between;" data-ru="Итоговый балл: _____ / 10 &nbsp; Подпись преподавателя: ____________" data-en="Total Score: _____ / 10 &nbsp; Teacher Signature: ____________">
        <span>To'plangan ball: _____ / 10</span>
        <span>O'qituvchi imzosi: ____________</span>
      </div>
    </div>
        """
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
        <span class="badge" style="background:var(--accent); color:#fff; font-weight:700; padding:2px 8px; border-radius:4px; font-size:11px;">1-Vazifa (4 Ball) — Baza</span>
        <span style="font-size:11px; color:var(--ink-2);" data-ru="Math.atan2 и расчет векторов" data-en="Math.atan2 & velocity vectors">Math.atan2 va Vektorlar</span>
      </div>
      <h3 style="font-size:13pt; margin-bottom:6px;" data-ru="Промпт для ИИ: Функция Стрельбы" data-en="AI Prompt: Shooting Function">Otishma Uchun AI Prompti va Hisob-Kitob</h3>
      <p style="font-size:12px; color:var(--ink-2); margin-bottom:8px;" data-ru="Напишите структурированный AI-промпт, который заставит ИИ написать функцию shoot(targetX, targetY) с правильным расчетом угла и скорости." data-en="Compose a structured prompt that instructs AI to generate shoot(targetX, targetY) with correct angle and velocities.">AI ga <code>shoot(targetX, targetY)</code> funksiyasini to'g'ri yozdirish uchun to'liq prompt matnini shakllantiring:</p>
      <textarea id="hwTask1" style="width:100%; height:90px; background:var(--surface-2); color:var(--ink); border:1px solid var(--hair); border-radius:4px; padding:8px; font-family:var(--font-mono); font-size:11px;"></textarea>
      <div style="margin-top:6px; display:flex; justify-content:space-between; align-items:center;">
        <button class="btn" onclick="saveAnswer('hwTask1')" style="font-size:11px; background:var(--surface-2); border:1px solid var(--hair);" data-ru="💾 Сохранить" data-en="💾 Save">💾 Saqlash</button>
        <button class="btn toggle-sol" onclick="toggleSolution('sol1')" style="font-size:11px; color:var(--accent); background:none; border:none; cursor:pointer;" data-ru="Показать эталонный ответ" data-en="Show Golden Answer">Oltin Yechimni Ko'rish</button>
      </div>
      <div id="sol1" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px;">
        <strong>Oltin Prompt:</strong> "Men 2D Canvas o'yinimda (Hero koordinatalari hero.x, hero.y) sichqoncha kursoriga qarab o'q uzmoqchiman. Math.atan2(targetY - hero.y, targetX - hero.x) orqali burchakni hisoblab, bullets massiviga vx = Math.cos(angle)*12 va vy = Math.sin(angle)*12 parametrli o'q qo'shuvchi shoot(tx, ty) funksiyasini yozib ber."
      </div>
    </div>

    <!-- TASK 2 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <span class="badge" style="background:var(--purple); color:#fff; font-weight:700; padding:2px 8px; border-radius:4px; font-size:11px;">2-Vazifa (4 Ball) — Amaliyot</span>
        <span style="font-size:11px; color:var(--ink-2);" data-ru="Устранение утечки памяти" data-en="Memory leak debugging">Xotira Oqishi va Teskari Sikl</span>
      </div>
      <h3 style="font-size:13pt; margin-bottom:6px;" data-ru="Critic-Промпт для ИИ: Исправление Ошибки Сдвига Индексов" data-en="Critic Prompt: Fixing Array Index Shift">Critic Prompt: Indekslar Surilishini Tuzatish</h3>
      <p style="font-size:12px; color:var(--ink-2); margin-bottom:8px;" data-ru="Опишите, как вы сформулируете сообщение ИИ об ошибке утечки памяти при прямом цикле for(i=0; i<len) и попросите обратный цикл." data-en="Formulate a bug-fixing prompt reporting the forward-loop index shift bug and requesting a reverse splice() traversal.">To'g'ri for-loop da <code>splice()</code> ishlatilganda o'qlar o'chmay qolishi xatosini AI ga tushuntirib, teskari sikl so'rash promptini yozing:</p>
      <textarea id="hwTask2" style="width:100%; height:90px; background:var(--surface-2); color:var(--ink); border:1px solid var(--hair); border-radius:4px; padding:8px; font-family:var(--font-mono); font-size:11px;"></textarea>
      <div style="margin-top:6px; display:flex; justify-content:space-between; align-items:center;">
        <button class="btn" onclick="saveAnswer('hwTask2')" style="font-size:11px; background:var(--surface-2); border:1px solid var(--hair);" data-ru="💾 Сохранить" data-en="💾 Save">💾 Saqlash</button>
        <button class="btn toggle-sol" onclick="toggleSolution('sol2')" style="font-size:11px; color:var(--accent); background:none; border:none; cursor:pointer;" data-ru="Показать эталонный ответ" data-en="Show Golden Answer">Oltin Yechimni Ko'rish</button>
      </div>
      <div id="sol2" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px;">
        <strong>Oltin Critic Prompt:</strong> "Diqqat: O'qlarni 0 dan length gacha oddiy siklda splice() bilan o'chirganda indekslar surilib, ba'zi o'qlar ekrandan chiqsa ham massivda qolib ketmoqda (Memory Leak). Menga bullets massivini oxiridan boshiga qarab (for let i = bullets.length - 1; i >= 0; i--) xavfsiz aylanuvchi va devorga urilgan o'qlarni splice(i, 1) bilan tozalovchi to'g'ri kodni ber."
      </div>
    </div>

    <!-- TASK 3 (2 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <span class="badge" style="background:var(--green); color:#fff; font-weight:700; padding:2px 8px; border-radius:4px; font-size:11px;">3-Vazifa (2 Ball) — Kiber-Chaqiruv</span>
        <span style="font-size:11px; color:var(--ink-2);" data-ru="Дробовик или Частицы" data-en="Shotgun or Particle Sparks">Drobovik yoki Uchqunlar Tizimi</span>
      </div>
      <h3 style="font-size:13pt; margin-bottom:6px;" data-ru="Промпт Сочности: Искры и Режимы Оружия" data-en="Game Juice Prompt: Sparks & Weapons">O'yin Shirasi (Vibe-Juice) Uchun Prompt</h3>
      <p style="font-size:12px; color:var(--ink-2); margin-bottom:8px;" data-ru="Напишите промпт для добавления 10 искр (с затуханием прозрачности и трением 0.92) или веерного выстрела дробовика (3 пули)." data-en="Write an enhancement prompt adding 10 impact spark particles (friction 0.92, alpha fadeout) or 3-way shotgun spread.">O'q devorga urilganda 10 ta rangli uchqun (friction 0.92, alpha fade) sochilishini yoki 3-talik Drobovikni so'rash prompti:</p>
      <textarea id="hwTask3" style="width:100%; height:90px; background:var(--surface-2); color:var(--ink); border:1px solid var(--hair); border-radius:4px; padding:8px; font-family:var(--font-mono); font-size:11px;"></textarea>
      <div style="margin-top:6px; display:flex; justify-content:space-between; align-items:center;">
        <button class="btn" onclick="saveAnswer('hwTask3')" style="font-size:11px; background:var(--surface-2); border:1px solid var(--hair);" data-ru="💾 Сохранить" data-en="💾 Save">💾 Saqlash</button>
        <button class="btn toggle-sol" onclick="toggleSolution('sol3')" style="font-size:11px; color:var(--accent); background:none; border:none; cursor:pointer;" data-ru="Показать эталонный ответ" data-en="Show Golden Answer">Oltin Yechimni Ko'rish</button>
      </div>
      <div id="sol3" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px;">
        <strong>Oltin Prompt:</strong> "O'yinimga zarba hissiyotini qo'sh: o'q tosh devorga urilganda xuddi shu nuqtada 10 ta neon uchqun sochilsin. Har bir uchqun tasodifiy burchakda uchsin, har freymda tezligi 0.92 koeffitsiyent bilan tormozlansin (friction) va alpha shaffofligi 1.0 dan 0 ga tushib, xotiradan splice() bilan o'chirilsin."
      </div>
    </div>
    """

    replacements = {
        "{{TITLE_UZ}}": "32-dars: O'yin Fizikasi va Otishma Mexanikasi: Trigonometriya, Traektoriya va Zarrachalar",
        "{{TITLE_RU}}": "Урок 32: Физика Игры и Механика Стрельбы: Тригонометрия, Траектории и Частицы",
        "{{TITLE_EN}}": "Lesson 32: Game Physics & Ballistics: Trigonometry, Trajectories & Particles",
        "{{COHORT_LABEL_UZ}}": "7–8-SINF",
        "{{HERO_TAG_UZ}}": "11-Hafta · Vibecoding & Creative Coding Track",
        "{{HERO_DESC_UZ}}": "HTML5 Canvas da Math.atan2 va tezlik vektorlari yordamida o'q otish, devor to'qnashuvlari va xotirani tozalash mexanizmini mustaqil Vibecoding orqali yaratish topshiriqlari.",
        "{{HERO_DESC_RU}}": "Задания для самостоятельного создания баллистики на HTML5 Canvas через Vibecoding: Math.atan2, векторы скорости, очистка памяти и искры при ударе.",
        "{{HERO_DESC_EN}}": "Independent Vibecoding assignments: engineering HTML5 Canvas ballistics, Math.atan2, velocity vectors, memory leak prevention, and impact sparks.",
        "{{RUBRIC_T1_UZ}}": "1-Bosqich: Baza (Math.atan2 va vektorlar prompti)",
        "{{RUBRIC_T1_RU}}": "1-й Уровень: База (Промпт Math.atan2 и векторов)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (Math.atan2 & vectors prompt)",
        "{{RUBRIC_T2_UZ}}": "2-Bosqich: Amaliyot (Xotira oqishini tuzatuvchi Critic prompt)",
        "{{RUBRIC_T2_RU}}": "2-й Уровень: Практика (Critic-промпт утечки памяти)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Memory leak bug-fix critic prompt)",
        "{{RUBRIC_T3_UZ}}": "3-Bosqich: Kiber-Chaqiruv (Zarrachalar yoki Drobovik rejimi)",
        "{{RUBRIC_T3_RU}}": "3-й Уровень: Вызов (Искры или режим дробовика)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (Sparks or shotgun mode prompt)",
        "{{TASKS_HTML}}": tasks_html,
        "{{LESSON_SLUG}}": "7-8-w11-l32-otishma-mexanikasi"
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    content = """# O'qituvchi Uchun Dars Qo'llanmasi (Teacher Reading Guide)

**Sinf:** 7–8-sinf · **Hafta:** 11-hafta · **Dars:** 32-dars  
**Mavzu:** O'yin Fizikasi va Otishma Mexanikasi: Trigonometriya, Traektoriya va Zarrachalar (Canvas Ballistics, Math.atan2 & Particle Sparks)  
**Format:** 80 daqiqalik Juftlik Dars (Double Block)  
**Uslub:** Vibecoding — AI bilan interaktiv dasturlash, prompt muhandisligi va kod auditi.

---

## 1. 80 Daqiqalik Darsning Daqiqama-Daqiqa Pacing Rejasi

### 1-Bosqich: Uy Vazifasi Tahlili va Nazariy Poydevor (40 daqiqa)
* **00:00–04:00 (Kirish):** Dars mavzusi va maqsadini e'lon qilish. Roguelike o'yinimizga bugun haqiqiy jangovar mexanika qo'shilishini tushuntirish.
* **04:00–12:00 (Uy Vazifasi Tahlili):** 
  - Keng tarqalgan xato (Pitfall): `Math.atan2(dx, dy)` emas, doim `Math.atan2(dy, dx)`! O'quvchilarga nega vertikal o'q (dy) birinchi kelishini doskada chizib ko'rsating.
  - 30 soniyalik blits savol: dy = 0, dx > 0 bo'lganda burchak necha radian? (0 rad).
* **12:00–24:00 (Nishonga Olish va Math.atan2):**
  - Ekranda sichqoncha koordinatalarini tutish (`e.clientX - rect.left`).
  - Radianlar aylanasi (-PI dan +PI gacha). Canvas da Y o'qi pastga qaragani uchun radianlar yo'nalishini ko'rsatish.
* **24:00–35:00 (Tezlik Vektorlari va Xotira Tozalash):**
  - `vx = cos(angle) * speed`, `vy = sin(angle) * speed`.
  - **Kritik nuqta (Memory Leak):** Agar o'qlar ekrandan chiqqanda o'chirilmasa, o'yin qotadi. Nega oddiy `for (i=0)` siklida `splice()` indekslarni buzib yuborishini, teskari sikl `for (let i = bullets.length - 1; i >= 0; i--)` esa xavfsiz ekanini tushuntiring.
* **35:00–40:00 (Zarrachalar — Game Juice):**
  - 8–12 ta uchqun sochish, havo qarshiligi (friction: 0.92) va shaffoflik (alpha) so'nishi.

### 2-Bosqich: Amaliyot, Kiber-Duel va Baholash (40 daqiqa)
* **40:00–48:00 (Smartboard Jonli Simulyatori):** Doskada o'quvchilar bilan interaktiv o'q otish, 360° salьyutni sinash.
* **48:00–55:00 (Kiber-Viktorina):** 3 ta savol bo'yicha tezkor musobaqa.
* **55:00–70:00 (Vibecoding Amaliy Arenasi — 15 daqiqa):**
  - O'quvchilar kompyuterlarini ochadi.
  - **Muhim Vibecoding qoidasi:** Kodni qo'lda yozmaslik, AI ga 4 bosqichli prompt berish!
  - 1-qadam: Boshlang'ich prompt orqali burchak va uchishni olish.
  - 2-qadam: Sinov va 360° nishonni tekshirish.
  - 3-qadam: Xotira oqishini AI ga tushuntirib, teskari siklni talab qilish (Critic prompt).
  - 4-qadam: Zarrachalar (sparks) yoki Drobovik rejimini qo'shish.
* **70:00–74:00 (Partadosh Auditi):** Partadoshlar o'rin almashib, 4 ta mezon bo'yicha bir-birining o'yinini test qiladi.
* **74:00–77:00 (Katta Ekran Showcasi):** Eng chiroyli otishma yoki qurol yaratgan 2 nafar o'quvchi ishini doskada ko'rsatish.
* **77:00–80:00 (Xulosa va Vazifa):** 10 ballik rubrika va ertangi darsga (Dushman AI va Pathfinding) ko'prik.

---

## 2. O'qituvchi Uchun Savol-Javob va Baholash Kaliti
* **Savol 1:** Math.atan2(dy, dx) nima qaytaradi?  
  *Javob:* Qahramondan kursorga yo'nalgan to'g'ri burchakni radianlarda (-3.14 dan +3.14 gacha) qaytaradi.
* **Savol 2:** Nega oddiy `bullets.push()` bilan birga `bullets.splice()` yozilmasa o'yin sekinlashadi?  
  *Javob:* Har bosilganda massivga yangi obyekt qo'shiladi. Ekrandan chiqqan o'qlar o'chirilmasa, 60 FPS sikli minglab o'qlarni hisoblashga majbur bo'ladi va xotira to'lib (Memory Leak) o'yin qotadi.
* **Savol 3:** Nega massivni orqadan oldinga tekshirish kerak?  
  *Javob:* Chunki 0-indeksdan boshlab o'chirilsa, qolgan elementlar bitta chapga siljiydi va keyingi o'q tekshirilmay o'tib ketadi.
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
  <title data-ru="Студия Баллистики и Vibecoding (Canvas Ballistics Lab)" data-en="Canvas Ballistics & Vibecoding Studio">Ballistika va Vibecoding Studiyasi</title>
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
    <span>🎯 Vibecoding Ballistics Studio: Math.atan2 & Particle Sparks</span>
    <span style="font-size:11px; background:rgba(56,189,248,0.15); color:var(--accent); padding:2px 8px; border-radius:12px;">7–8-Sinf</span>
  </div>
  <div class="hud">
    <div class="hud-badge">🚀 <span data-ru="Пули:" data-en="Bullets:">O'qlar:</span> <strong id="hudBullets" style="color:var(--accent); font-size:13px;">0</strong></div>
    <div class="hud-badge">💥 <span data-ru="Искры:" data-en="Sparks:">Uchqunlar:</span> <strong id="hudSparks" style="color:var(--yellow); font-size:13px;">0</strong></div>
    <div class="hud-badge">🎯 <span data-ru="Уничтожено:" data-en="Destroyed:">Nishonlar:</span> <strong id="hudKills" style="color:var(--green); font-size:13px;">0</strong></div>
    <div class="hud-badge" id="hudMemoryBadge" style="color:var(--green);">🛡️ <span data-ru="Память чиста" data-en="Memory Safe">Xotira Toza</span></div>
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
        <button class="step-btn active" onclick="switchPromptStep(1)" data-ru="1. Прицел" data-en="1. Aiming">1. Nishon</button>
        <button class="step-btn" onclick="switchPromptStep(2)" data-ru="2. Память" data-en="2. Memory">2. Xotira</button>
        <button class="step-btn" onclick="switchPromptStep(3)" data-ru="3. Искры" data-en="3. Sparks">3. Uchqun</button>
        <button class="step-btn" onclick="switchPromptStep(4)" data-ru="4. Оружие" data-en="4. Weapon">4. Qurol</button>
      </div>

      <div id="stepInfo">
        <div style="font-size:11px; color:var(--ink-2); line-height:1.4;" id="stepDesc">
          <strong>1-Qadam:</strong> AI ga o'yin kontekstini berib, kursor burchagini topish va o'q uzishni so'rash.
        </div>
        <div class="prompt-box" id="stepPromptText">Menda 2D Canvas o'yini bor (hero markazda). Sichqoncha bosilgan nuqtaga Math.atan2(dy, dx) orqali burchakni hisoblab, bullets massiviga vx = cos(angle)*12 va vy = sin(angle)*12 bilan o'q qo'shuvchi shoot() funksiyasini yozib ber.</div>
        <div style="display:flex; gap:6px; margin-top:6px;">
          <button class="btn btn-accent" onclick="copyPrompt()" style="flex:1;" data-ru="📋 Копировать Промпт" data-en="📋 Copy Prompt">📋 Nusxalash</button>
          <button class="btn btn-green" onclick="applyStepCode()" style="flex:1;" data-ru="⚡ Применить Код" data-en="⚡ Run in Lab">⚡ Kodni Qo'llash</button>
        </div>
      </div>
    </div>

    <div class="box-card">
      <h4 data-ru="Управление Оружием" data-en="Weapon Mode">Qurol Rejimi</h4>
      <div style="display:flex; gap:6px; margin-bottom:8px;">
        <button class="btn btn-gray" id="btnSingle" onclick="setWeapon('single')" style="flex:1; border:1px solid var(--accent);" data-ru="Одиночный" data-en="Single">Yakka</button>
        <button class="btn btn-gray" id="btnShotgun" onclick="setWeapon('shotgun')" style="flex:1;" data-ru="Дробовик" data-en="Shotgun">Drobovik</button>
        <button class="btn btn-gray" id="btnBurst" onclick="setWeapon('burst')" style="flex:1;" data-ru="360° Залп" data-en="360° Burst">360° Burst</button>
      </div>
      <div style="font-size:11px; display:flex; justify-content:space-between; margin-bottom:4px;">
        <span data-ru="Угол прицела:" data-en="Aim Angle:">Nishon burchagi:</span>
        <span id="txtAimAngle" style="font-family:var(--font-mono); color:var(--accent);">0.00 rad</span>
      </div>
      <button class="btn btn-gray" onclick="spawnTargets()" style="width:100%; margin-top:4px;" data-ru="🎯 Обновить Мишени" data-en="🎯 Refresh Targets">🎯 Yangi Nishonlar Qo'shish</button>
      <button class="btn btn-red" onclick="simulateMemoryLeak()" style="width:100%; margin-top:6px;" data-ru="⚠️ Симулировать Утечку Памяти" data-en="⚠️ Simulate Memory Leak">⚠️ Xotira Oqishini Sinash (Bug Demo)</button>
    </div>

    <div class="box-card" style="font-family:var(--font-mono); font-size:10.5px; line-height:1.4;">
      <div style="color:var(--accent); font-weight:700; margin-bottom:4px;">[Real-Vaqt Formulalar]</div>
      <div style="color:#94a3b8;">dx = targetX - hero.x;</div>
      <div style="color:#94a3b8;">dy = targetY - hero.y;</div>
      <div style="color:var(--yellow);">angle = Math.atan2(dy, dx);</div>
      <div style="color:var(--green);">vx = Math.cos(angle) * speed;</div>
      <div style="color:var(--green);">vy = Math.sin(angle) * speed;</div>
    </div>
  </div>
</main>

<script>
var canvas = document.getElementById('simCanvas');
var ctx = canvas.getContext('2d');

var hero = { x: 400, y: 260, size: 22 };
var bullets = [];
var sparks = [];
var targets = [
  { x: 160, y: 130, size: 20, hp: 3, maxHp: 3 },
  { x: 640, y: 130, size: 20, hp: 3, maxHp: 3 },
  { x: 200, y: 400, size: 20, hp: 3, maxHp: 3 },
  { x: 600, y: 400, size: 20, hp: 3, maxHp: 3 }
];
var walls = [
  { x: 100, y: 80, w: 25, h: 360 },
  { x: 675, y: 80, w: 25, h: 360 },
  { x: 260, y: 60, w: 280, h: 25 },
  { x: 260, y: 435, w: 280, h: 25 }
];

var weaponMode = 'single';
var bulletSpeed = 12;
var kills = 0;
var currentAimAngle = 0;
var currentStep = 1;
var isMemoryLeakActive = false;
var sparksEnabled = true;

var STEPS = {
  1: {
    desc: "<strong>1-Qadam (Arxitektura Prompti):</strong> AI ga o'yin kontekstini bering va burchak bo'yicha uchuvchi shoot() funksiyasini so'rang.",
    prompt: "Men 2D Canvas o'yinimda (hero markazda: hero.x, hero.y) sichqoncha kursoriga qarab 360° o'q uzmoqchiman. Math.atan2(targetY - hero.y, targetX - hero.x) yordamida burchakni hisobla, vx = Math.cos(angle)*12 va vy = Math.sin(angle)*12 bilan bullets massiviga obyekt qo'shuvchi shoot(tx, ty) funksiyasini yoz.",
    action: function() {
      weaponMode = 'single';
      isMemoryLeakActive = false;
      highlightButton('btnSingle');
      updateMemoryBadge();
    }
  },
  2: {
    desc: "<strong>2-Qadam (Critic Bug-Fix Prompt):</strong> Xotira oqishini bartaraf etish! Ekrandan chiqqan o'qlarni teskari for-loop da splice(i, 1) orqali tozalash.",
    prompt: "Diqqat: O'yinimda xotira oqishi (Memory Leak) yuz berdi: ekrandan chiqqan yoki tosh devorga urilgan o'qlar massivda qolib ketyapti. Menga bullets massivini orqadan oldinga qarab (for let i = bullets.length - 1; i >= 0; i--) aylanuvchi va bullets.splice(i, 1) bilan o'chiruvchi xavfsiz tozalash kodini yozib ber.",
    action: function() {
      isMemoryLeakActive = false;
      updateMemoryBadge();
    }
  },
  3: {
    desc: "<strong>3-Qadam (Vibe-Juice Prompt):</strong> Zarba effekti! O'q devorga yoki nishonga urilganda 10 ta neon uchqun (friction 0.92, alpha fade) sochilishini so'rash.",
    prompt: "Otishmaga kiber-zarba effekti qo'sh: o'q devorga yoki nishonga urilganda xuddi shu nuqtada 10-14 ta neon rangli uchqun (spark) sochilsin. Har bir uchqun tasodifiy burchakda uchsin, tezligi har freymda 0.92 koeffitsiyent bilan tormozlansin (friction) va alpha (shaffoflik) 1.0 dan 0 ga tushib yo'qolsin.",
    action: function() {
      sparksEnabled = true;
      for (var i = 0; i < 4; i++) {
        spawnSparks(hero.x + (Math.random()-0.5)*100, hero.y + (Math.random()-0.5)*100);
      }
    }
  },
  4: {
    desc: "<strong>4-Qadam (Kiber-Qurollar Prompti):</strong> Yelpig'ich drobovik (Shotgun) va 360° doiraviy salьyut otish rejimlarini kiritish.",
    prompt: "Otishma tizimiga 2 ta yangi qurol qo'sh: 1) Drobovik (Shotgun) — bitta o'q o'rniga 3 ta o'qni yelpig'ich qilib otsin (burchaklar: angle - 0.2, angle, angle + 0.2); 2) Kiber-Salьyut (360° Burst) — 16 ta o'qni to'liq doira bo'ylab bir vaqtda sochsin. Buni bitta shoot(mode) funksiyasiga jamlab ber.",
    action: function() {
      weaponMode = 'shotgun';
      highlightButton('btnShotgun');
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

function highlightButton(activeId) {
  ['btnSingle', 'btnShotgun', 'btnBurst'].forEach(function(id) {
    var b = document.getElementById(id);
    if (id === activeId) {
      b.style.borderColor = 'var(--accent)';
      b.style.color = 'var(--accent)';
    } else {
      b.style.borderColor = 'rgba(255,255,255,0.1)';
      b.style.color = '#fff';
    }
  });
}

function setWeapon(mode) {
  weaponMode = mode;
  if (mode === 'single') highlightButton('btnSingle');
  if (mode === 'shotgun') highlightButton('btnShotgun');
  if (mode === 'burst') highlightButton('btnBurst');
}

function simulateMemoryLeak() {
  isMemoryLeakActive = true;
  updateMemoryBadge();
  alert('Xotira oqishi faollashdi! Endi o‘qlar ekrandan chiqqanda o‘chirilmaydi. Xotira hisoblagichiga e‘tibor bering!');
}

function updateMemoryBadge() {
  var mb = document.getElementById('hudMemoryBadge');
  if (!mb) return;
  if (isMemoryLeakActive) {
    mb.innerHTML = '⚠️ <span data-ru="Утечка памяти!" data-en="Memory Leak!">Xotira Oqishi Xavfi!</span>';
    mb.style.color = 'var(--red)';
  } else {
    mb.innerHTML = '🛡️ <span data-ru="Память чиста" data-en="Memory Safe">Xotira Toza</span>';
    mb.style.color = 'var(--green)';
  }
}

function spawnTargets() {
  targets = [
    { x: 160, y: 130, size: 20, hp: 3, maxHp: 3 },
    { x: 640, y: 130, size: 20, hp: 3, maxHp: 3 },
    { x: 200, y: 400, size: 20, hp: 3, maxHp: 3 },
    { x: 600, y: 400, size: 20, hp: 3, maxHp: 3 }
  ];
}

function spawnSparks(x, y) {
  if (!sparksEnabled) return;
  for (var i = 0; i < 12; i++) {
    var angle = Math.random() * Math.PI * 2;
    var spd = Math.random() * 5 + 1.5;
    sparks.push({
      x: x, y: y,
      vx: Math.cos(angle) * spd,
      vy: Math.sin(angle) * spd,
      alpha: 1.0,
      color: Math.random() > 0.5 ? '#f59e0b' : '#38bdf8'
    });
  }
}

canvas.addEventListener('mousemove', function(e) {
  var rect = canvas.getBoundingClientRect();
  var scaleX = canvas.width / rect.width;
  var scaleY = canvas.height / rect.height;
  var tx = (e.clientX - rect.left) * scaleX;
  var ty = (e.clientY - rect.top) * scaleY;
  currentAimAngle = Math.atan2(ty - hero.y, tx - hero.x);
  document.getElementById('txtAimAngle').textContent = currentAimAngle.toFixed(2) + ' rad';
});

canvas.addEventListener('pointerdown', function(e) {
  var rect = canvas.getBoundingClientRect();
  var scaleX = canvas.width / rect.width;
  var scaleY = canvas.height / rect.height;
  var tx = (e.clientX - rect.left) * scaleX;
  var ty = (e.clientY - rect.top) * scaleY;
  fireWeapon(tx, ty);
});

function fireWeapon(tx, ty) {
  var angle = Math.atan2(ty - hero.y, tx - hero.x);
  if (weaponMode === 'single') {
    bullets.push({
      x: hero.x, y: hero.y,
      vx: Math.cos(angle) * bulletSpeed,
      vy: Math.sin(angle) * bulletSpeed,
      life: 80
    });
  } else if (weaponMode === 'shotgun') {
    [-0.2, 0, 0.2].forEach(function(spread) {
      bullets.push({
        x: hero.x, y: hero.y,
        vx: Math.cos(angle + spread) * bulletSpeed,
        vy: Math.sin(angle + spread) * bulletSpeed,
        life: 75
      });
    });
  } else if (weaponMode === 'burst') {
    for (var i = 0; i < 16; i++) {
      var a = (i / 16) * Math.PI * 2;
      bullets.push({
        x: hero.x, y: hero.y,
        vx: Math.cos(a) * bulletSpeed,
        vy: Math.sin(a) * bulletSpeed,
        life: 80
      });
    }
  }
}

function gameLoop() {
  ctx.fillStyle = '#020617';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Grid background
  ctx.strokeStyle = 'rgba(255,255,255,0.03)';
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

  // Draw Laser Guide Line
  ctx.strokeStyle = 'rgba(56, 189, 248, 0.2)';
  ctx.lineWidth = 1;
  ctx.setLineDash([4, 4]);
  ctx.beginPath();
  ctx.moveTo(hero.x, hero.y);
  ctx.lineTo(hero.x + Math.cos(currentAimAngle) * 800, hero.y + Math.sin(currentAimAngle) * 800);
  ctx.stroke();
  ctx.setLineDash([]);

  // Draw Hero
  ctx.fillStyle = '#10b981';
  ctx.beginPath();
  ctx.arc(hero.x, hero.y, hero.size / 2, 0, Math.PI * 2);
  ctx.fill();

  // Gun nozzle
  ctx.strokeStyle = '#38bdf8';
  ctx.lineWidth = 4;
  ctx.beginPath();
  ctx.moveTo(hero.x, hero.y);
  ctx.lineTo(hero.x + Math.cos(currentAimAngle) * (hero.size / 2 + 8), hero.y + Math.sin(currentAimAngle) * (hero.size / 2 + 8));
  ctx.stroke();

  // Draw Targets
  for (var t = 0; t < targets.length; t++) {
    var tg = targets[t];
    if (tg.hp <= 0) continue;
    ctx.fillStyle = '#ef4444';
    ctx.beginPath();
    ctx.arc(tg.x, tg.y, tg.size / 2, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = '#f87171';
    ctx.lineWidth = 2;
    ctx.stroke();

    // HP Bar
    ctx.fillStyle = '#334155';
    ctx.fillRect(tg.x - 14, tg.y - 18, 28, 4);
    ctx.fillStyle = '#10b981';
    ctx.fillRect(tg.x - 14, tg.y - 18, (tg.hp / tg.maxHp) * 28, 4);
  }

  // Update & Draw Bullets
  for (var i = bullets.length - 1; i >= 0; i--) {
    var b = bullets[i];
    b.x += b.vx;
    b.y += b.vy;
    b.life--;

    var hit = false;
    // Check walls
    for (var j = 0; j < walls.length; j++) {
      var wl2 = walls[j];
      if (b.x >= wl2.x && b.x <= wl2.x + wl2.w && b.y >= wl2.y && b.y <= wl2.y + wl2.h) {
        hit = true;
        break;
      }
    }

    // Check targets
    if (!hit) {
      for (var k = 0; k < targets.length; k++) {
        var trg = targets[k];
        if (trg.hp <= 0) continue;
        var dist = Math.hypot(b.x - trg.x, b.y - trg.y);
        if (dist < trg.size / 2 + 4) {
          trg.hp--;
          hit = true;
          if (trg.hp <= 0) kills++;
          break;
        }
      }
    }

    // Out of bounds check
    var oob = (b.x < 0 || b.x > canvas.width || b.y < 0 || b.y > canvas.height);

    if (hit) {
      spawnSparks(b.x, b.y);
      bullets.splice(i, 1);
      continue;
    }

    if (oob || b.life <= 0) {
      if (!isMemoryLeakActive) {
        bullets.splice(i, 1);
        continue;
      }
    }

    // Draw bullet
    ctx.fillStyle = '#38bdf8';
    ctx.shadowColor = '#38bdf8';
    ctx.shadowBlur = 8;
    ctx.beginPath();
    ctx.arc(b.x, b.y, 4, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;
  }

  // Update & Draw Sparks
  for (var s = sparks.length - 1; s >= 0; s--) {
    var sp = sparks[s];
    sp.x += sp.vx;
    sp.y += sp.vy;
    sp.vx *= 0.92;
    sp.vy *= 0.92;
    sp.alpha -= 0.03;

    if (sp.alpha <= 0) {
      sparks.splice(s, 1);
      continue;
    }

    ctx.fillStyle = sp.color;
    ctx.globalAlpha = Math.max(0, sp.alpha);
    ctx.beginPath();
    ctx.arc(sp.x, sp.y, 2.5, 0, Math.PI * 2);
    ctx.fill();
    ctx.globalAlpha = 1.0;
  }

  // Update HUD
  document.getElementById('hudBullets').textContent = bullets.length;
  document.getElementById('hudSparks').textContent = sparks.length;
  document.getElementById('hudKills').textContent = kills;

  if (bullets.length > 40 && isMemoryLeakActive) {
    document.getElementById('hudBullets').style.color = 'var(--red)';
  } else {
    document.getElementById('hudBullets').style.color = 'var(--accent)';
  }

  requestAnimationFrame(gameLoop);
}

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
    print(f"Building Lesson 32 (Grades 7–8, 80-min Double Block, Vibecoding & Ballistics)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_simulator()
    print("Lesson 32 build complete!")

if __name__ == "__main__":
    main()
