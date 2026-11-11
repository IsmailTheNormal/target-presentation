#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_7_8_w10_l30.py — 7–8-sinf (10-hafta 30-dars)
Mavzu: Kamera, Viewport va Ko'rish Maydoni: Fog of War (Urush Tumani)
Track: Game Dev & Canvas 2D Dvigateli
Duration: 80 daqiqa (Double block / 2-hour class)
"""

import os
import sys
import json
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LESSON_DIR = os.path.join(REPO_ROOT, "classes", "7-8-sinf", "10-hafta", "30-dars-kamera-viewport-va-fog-of-war")
SIM_DIR = os.path.join(LESSON_DIR, "simulator")
os.makedirs(SIM_DIR, exist_ok=True)

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
    TPL_PRES = f.read()

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
    TPL_VAR = f.read()

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
    TPL_VAZ = f.read()

def build_7_8_lesson():
    print("📦 Generating 7–8-sinf (30-dars: Kamera, Viewport va Fog of War)...")

    title_uz = "30-dars: Kamera, Viewport va Ko'rish Maydoni: Fog of War (Urush Tumani)"
    title_ru = "Урок 30: Камера, Viewport и Поле Зрения: Fog of War (Туман Войны)"
    title_en = "Lesson 30: Camera, Viewport and Field of View: Fog of War Mechanics"

    # ============================================================
    # 1. PREZENTATSIYA
    # ============================================================
    tpl = TPL_PRES
    tpl = re.sub(r"<title[^>]*>.*?</title>", f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>', tpl)
    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>', '<span class="tag" data-ru="7-8 · ГЕЙМДЕВ" data-en="7-8 · GAME DEV">7-8 · GAME DEV</span>', tpl, count=1)
    tpl = tpl.replace('<span id="totalSlides">6</span>', '<span id="totalSlides">14</span>')

    titles_dict = {"uz": title_uz, "ru": title_ru, "en": title_en}
    titles_json = json.dumps(titles_dict, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    slides = []

    # Slide 1: Titul
    slides.append("""  <!-- SLIDE 1: TITUL -->
  <section class="slide is-on" data-phase="Kirish|Введение|Introduction" data-time="00:00–04:00">
    <div class="eyebrow" data-ru="7–8-СИНФ · 10-Я НЕДЕЛЯ · УРОК 30" data-en="GRADES 7–8 · WEEK 10 · LESSON 30">7–8-SINF · 10-HAFTA · 30-DARS</div>
    <h1 data-ru="Камера, Viewport и Туман Войны (Fog of War)" data-en="Camera, Viewport & Fog of War Mechanics">Kamera, Viewport va Ko'rish Maydoni: Fog of War</h1>
    <p class="lede" data-ru="Учим 2D-движок следовать за игроком: мировая система координат, ограничение краев (Clamping), кинематографичный Lerp и мистический свет факела в темном подземелье." data-en="Teach 2D Canvas engine to follow the hero: world-to-screen coords, boundary clamping, smooth Lerp motion, and atmospheric radial torchlight in dark dungeons.">2D o'yin dvigatelini qahramon ortidan ergashtiramiz: dunyo koordinatalari, xarita chegaralarini qulflash (Clamping), silliq Lerp harakati va qorong'i yer osti labirintida mash'ala nuri.</p>
    <div class="grid c3" style="margin-top:24px;">
      <div class="card">
        <h3 data-ru="Формат блока" data-en="Block Format">Format va Vaqt</h3>
        <p data-ru="Спаренный урок: 2 x 40 минут = 80 минут глубокой геймдев-практики" data-en="Double block: 2 x 40 min = 80 min hands-on game dev deep dive">Juftlik dars: 2 x 40 daqiqa = 80 daqiqalik geymdev amaliyoti</p>
      </div>
      <div class="card">
        <h3 data-ru="Главные механики" data-en="Core Mechanics">Asosiy Mexanikalar</h3>
        <p data-ru="World vs Screen Space, ctx.translate, Math.clamp, Radial Gradient" data-en="World vs Screen Space, ctx.translate, Math.clamp, Radial Gradient">World vs Screen Space, ctx.translate, Clamping va Radial mash'ala</p>
      </div>
      <div class="card">
        <h3 data-ru="Результат урока" data-en="Lesson Deliverable">Qo'lga Olinadigan Natija</h3>
        <p data-ru="Работающее Roguelike подземелье со следящей камерой и туманом" data-en="Playable Roguelike dungeon with following camera and dark fog of war">Qahramonni kuzatuvchi kamera va mash'alali Roguelike o'yini prototipi</p>
      </div>
    </div>
  </section>""")

    # Slide 2: HW Check & Bridge
    slides.append("""  <!-- SLIDE 2: HW CHECK & REVIEW -->
  <section class="slide" data-phase="Uy vazifasi tahlili|Разбор ДЗ|HW Review" data-time="04:00–10:00">
    <div class="eyebrow" data-ru="АНАЛИЗ И МОСТ К НОВОЙ ТЕМЕ" data-en="REVIEW & BRIDGE TO NEW TOPIC">TAHLIL VA KO'PRIK</div>
    <h2 data-ru="Разбор ДЗ 29: Ловушка Индексации 2D Матрицы" data-en="HW 29 Review: The 2D Matrix Index Inversion Pitfall">29-Dars Uy Vazifasi: Matritsadagi Xatolar Tahlili</h2>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card red">
        <span class="pill red" data-ru="Главная ошибка новичка" data-en="Top Beginner Pitfall">Eng Ko'p Uchragan Xato</span>
        <h3 style="margin-top:10px;" data-ru="Путаница map[x][y] вместо map[row][col]" data-en="Inverting map[x][y] instead of map[row][col]">map[x][y] va map[y][x] Chalkashligi</h3>
        <p data-ru="Многие ученики написали map[player.x / TILE][player.y / TILE]. В массивах первая скобка — это СТРОКА (Y), а вторая — КОЛОНКА (X)! Из-за этого игра падала с ошибкой Cannot read properties of undefined или разворачивалась боком." data-en="Students wrote map[x][y]. In 2D arrays the first index is ROW (Y) and second is COL (X)! This caused TypeError: Cannot read properties of undefined or 90-degree rotated maps.">Ko'pchilik o'quvchilar `map[player.x][player.y]` deb yozishdi. 2D massivda birinchi qavs — bu QATOR (Y), ikkinchisi — USTUN (X)! Natijada o'yin qulab tushdi yoki xarita 90 gradus buralib qoldi.</p>
      </div>
      <div class="card green">
        <span class="pill green" data-ru="Золотой стандарт архитектуры" data-en="Golden Architecture Standard">Oltin Yechim Standarti</span>
        <h3 style="margin-top:10px;" data-ru="Надежная проверка коллизий O(1)" data-en="Reliable O(1) Grid Collision Guard">Xavfsiz va To'g'ri O(1) To'qnashuv</h3>
        <pre class="code-snippet" style="font-size:12px; margin-top:8px;"><code>function isWall(worldX, worldY) {
  const col = Math.floor(worldX / TILE_SIZE);
  const row = Math.floor(worldY / TILE_SIZE);
  if (row &lt; 0 || row &gt;= ROWS || col &lt; 0 || col &gt;= COLS) return true;
  return map[row][col] === 1; // 1 = Devor
}</code></pre>
      </div>
    </div>
    <div class="card" style="margin-top:16px;">
      <h3 data-ru="⚡ 30-секундный Блиц-Мост к Камере" data-en="⚡ 30-Second Blitz Bridge to Camera">⚡ 30 Soniyalik Blitz Ko'prik</h3>
      <p data-ru="Вопрос: Если наш мир размером 2500x2000 пикселей, а экран монитора всего 800x500 — что произойдет с игроком через 3 секунды ходьбы вправо? Ответ: Он уйдет за правый край экрана! Нам нужна КАМЕРА, двигающая весь мир навстречу взгляду!" data-en="Question: If world size is 2500x2000 px and screen is 800x500 px, what happens after 3 seconds of walking right? Answer: Player walks off-screen into void! We need a CAMERA that shifts the world relative to player!">Savol: Agar dunyomiz 2500x2000 piksel, monitor ekrani esa 800x500 bo'lsa, o'yinchi 3 soniya o'ngga yursa nima bo'ladi? Javob: U ekrandan chiqib ketadi va ko'rinmay qoladi! Bizga dunyoni orqaga siljituvchi KAMERA kerak!</p>
    </div>
  </section>""")

    # Slide 3: World Space vs Screen Space
    slides.append("""  <!-- SLIDE 3: WORLD VS SCREEN SPACE -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="10:00–18:00">
    <div class="eyebrow" data-ru="СИСТЕМЫ КООРДИНАТ В ИГРАХ" data-en="COORDINATE SYSTEMS IN GAMES">KOORDINATALAR TIZIMI</div>
    <h2 data-ru="Мировое Пространство (World) vs Экран (Screen)" data-en="World Space vs Screen Space Coordinates">World Space (Dunyo) vs Screen Space (Ekran)</h2>
    <p class="lede" data-ru="В профессиональном геймдеве объекты существуют в двух разных координатных сетках:" data-en="In professional game engines, entities exist across two distinct coordinate planes:">Professional o'yin dasturlashda ob'ektlar ikkita alohida koordinata tekisligida yashaydi:</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <span class="pill" data-ru="Мировые координаты" data-en="World Coordinates">Dunyodagi O'rni (World Space)</span>
        <h3 style="margin-top:10px;" data-ru="Где персонаж находится в реальности" data-en="Where entity truly exists">Qahramon Haqiqatda Qayerda?</h3>
        <ul style="margin-left:18px; line-height:1.7; font-size:13px; margin-top:8px;">
          <li data-ru="Измеряется от левого верхнего угла карты (0, 0)" data-en="Measured from map top-left origin (0, 0)">Butun xaritaning chap yuqori burchagidan (0, 0) boshlanadi</li>
          <li data-ru="Координаты игрока могут быть огромными: (1850, 1420)" data-en="Coordinates can be huge: (1850, 1420)">Qahramon koordinatalari katta bo'lishi mumkin: (1850, 1420)</li>
          <li data-ru="Физика и коллизии рассчитываются ТОЛЬКО в World Space" data-en="Physics and collisions run strictly in World Space">Fizika va to'qnashuvlar FAQAT World Spaceda tekshiriladi</li>
        </ul>
      </div>
      <div class="card">
        <span class="pill" data-ru="Экранные координаты" data-en="Screen Coordinates">Ekrandagi O'rni (Screen Space)</span>
        <h3 style="margin-top:10px;" data-ru="Где пиксели рисуются на мониторе" data-en="Where pixels render on canvas">Monitor Ekranida Qayerda Chiziladi?</h3>
        <ul style="margin-left:18px; line-height:1.7; font-size:13px; margin-top:8px;">
          <li data-ru="Измеряется от верхнего левого угла окна Canvas (0, 0)" data-en="Measured from top-left of canvas element">Brauzer oynasi (Canvas)ning chap burchagidan boshlanadi</li>
          <li data-ru="Формула проекции: ScreenX = WorldX - CameraX" data-en="Projection formula: ScreenX = WorldX - CameraX">Asosiy proyeksiya formulasi: <code>ScreenX = WorldX - CameraX</code></li>
          <li data-ru="Камера сдвигает весь мир с помощью ctx.translate(-camX, -camY)" data-en="Camera offsets entire frame via ctx.translate(-camX, -camY)">Kamera butun dunyoni <code>ctx.translate(-camX, -camY)</code> bilan suradi</li>
        </ul>
      </div>
    </div>
    <div class="card" style="margin-top:14px; background:rgba(59,130,246,0.06); border-left:3px solid var(--accent);">
      <p style="font-size:13px; font-weight:600;" data-ru="Золотое правило Canvas: Вместо пересчета координат каждой стены, мы один раз делаем ctx.translate(-camera.x, -camera.y), рисуем весь мир обычными World-координатами, и восстанавливаем ctx.restore()!" data-en="Canvas Golden Rule: Rather than recalculating every single wall coordinate, we invoke ctx.translate(-camera.x, -camera.y) once, draw everything in standard World coords, and call ctx.restore()!">Canvas Oltin Qoidasi: Har bir devorning koordinatasini qayta hisoblab o'tirmaymiz! Bir marta <code>ctx.translate(-camera.x, -camera.y)</code> qilamiz, butun dunyoni oddiy koordinatalarda chizamiz va oxirida <code>ctx.restore()</code> qilamiz!</p>
    </div>
  </section>""")

    # Slide 4: Camera Math & Clamping
    slides.append("""  <!-- SLIDE 4: CAMERA MATH & CLAMPING -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="18:00–26:00">
    <div class="eyebrow" data-ru="МАТЕМАТИКА ЦЕНТРОВКИ И ГРАНИЦ" data-en="CENTERING & BOUNDARY MATHEMATICS">KAMERA MATEMATIKASI</div>
    <h2 data-ru="Центровка Игрока и Ограничение (Clamping)" data-en="Player Centering & Boundary Clamping">Qahramonni Markazlashtirish va Chegara (Clamping)</h2>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="1. Центрирование Камеры" data-en="1. Viewport Centering">1. Kamerani Markazlashtirish</h3>
        <p data-ru="Чтобы игрок всегда оставался ровно посередине монитора, левый верхний угол камеры должен отступать назад на половину экрана:" data-en="To keep the player anchored exactly at screen center, camera top-left must offset backwards by half viewport dimensions:">Qahramon monitor markazida turishi uchun kameraning koordinatasi ekran kengligi va balandligining yarmiga orqada yurishi kerak:</p>
        <pre class="code-snippet" style="font-size:12px; margin-top:8px;"><code>// Qahramonni ekranning o'rtasiga qo'yish
camera.x = player.x - (VIEWPORT_WIDTH / 2);
camera.y = player.y - (VIEWPORT_HEIGHT / 2);</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="2. Защита от Пустоты (Clamping)" data-en="2. Boundary Clamping">2. Bo'shliqqa Chiqmaslik (Clamping)</h3>
        <p data-ru="Без проверки камера покажет черный вакуум за пределами карты! Ограничиваем камеру между 0 и максимальным размером мира:" data-en="Without bounds checking, the camera exposes black void outside map borders! We clamp coordinates between 0 and world limit:">Agar chegaralanmasa, kamera xaritadan tashqaridagi qora bo'shliqni ko'rsatib qo'yadi! Uni 0 va dunyo chegaralari orasida qulflaymiz:</p>
        <pre class="code-snippet" style="font-size:12px; margin-top:8px;"><code>// Chegaralardan chiqib ketmaslik
const maxCamX = WORLD_WIDTH - VIEWPORT_WIDTH;
const maxCamY = WORLD_HEIGHT - VIEWPORT_HEIGHT;

camera.x = Math.max(0, Math.min(camera.x, maxCamX));
camera.y = Math.max(0, Math.min(camera.y, maxCamY));</code></pre>
      </div>
    </div>
    <div class="card" style="margin-top:14px;">
      <h3 data-ru="Почему это важно для Roguelike?" data-en="Why is this crucial for Roguelike?">Nega bu Roguelike o'yinlar uchun muhim?</h3>
      <p style="font-size:13px;" data-ru="Игрок чувствует огромный масштаб подземелья, но не видит служебные края Canvas. Экран выглядит монолитно и профессионально, как в Hades или The Binding of Isaac." data-en="The player senses the grand scale of an expansive labyrinth while hiding technical canvas edges, matching titles like Hades and The Binding of Isaac.">O'yinchi yer osti qasrining ulkanligini his qiladi, lekin Canvasning xom chetlarini ko'rmaydi. O'yin Hades yoki The Binding of Isaac kabi professional ko'rinish oladi.</p>
    </div>
  </section>""")

    # Slide 5: Interactive Simulator
    slides.append("""  <!-- SLIDE 5: LIVE SIMULATOR -->
  <section class="slide" data-phase="Jonli Simulyator|Интерактив|Live Demo" data-time="26:00–36:00">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНЫЙ ТРЕНАЖЕР НА ЭКРАНЕ" data-en="INTERACTIVE SMARTBOARD LAB">JONLI SIMULYATOR</div>
    <h2 data-ru="Лаборатория Камеры и Факела в Подземелье" data-en="Dungeon Camera & Torchlight Interactive Studio">Dungeon Kamera va Mash'ala Jonli Laboratoriyasi</h2>
    <p class="lede" data-ru="Двигайте персонажа кнопками или стрелками. Переключайте слежение камеры и туман войны:" data-en="Control the dungeon hero via buttons or WASD. Toggle camera lock and dynamic fog of war:">Qahramonni tugmalar yoki strelkalar bilan boshqaring. Kamera kuzatuvi va urush tumanini yoqib-o'chiring:</p>
    
    <div class="grid c2" style="margin-top:12px; align-items:flex-start;">
      <!-- Canvas Box -->
      <div class="card" style="padding:10px; text-align:center;">
        <canvas id="deckSimCanvas" width="460" height="260" style="background:#090d16; border-radius:8px; border:1px solid var(--rule); display:block; margin:0 auto;"></canvas>
        <div style="display:flex; justify-content:center; gap:8px; margin-top:8px;">
          <button class="btn" onclick="moveSimPlayer(0, -20)" style="padding:4px 12px;">⬆ W</button>
        </div>
        <div style="display:flex; justify-content:center; gap:8px; margin-top:4px;">
          <button class="btn" onclick="moveSimPlayer(-20, 0)" style="padding:4px 12px;">⬅ A</button>
          <button class="btn" onclick="moveSimPlayer(0, 20)" style="padding:4px 12px;">⬇ S</button>
          <button class="btn" onclick="moveSimPlayer(20, 0)" style="padding:4px 12px;">➡ D</button>
        </div>
      </div>

      <!-- Controls & Telemetry -->
      <div class="card">
        <h3 data-ru="Телеметрия Движка" data-en="Engine Telemetry">Dvigatel Telemetriyasi</h3>
        <div style="font-family:'JetBrains Mono',monospace; font-size:12px; line-height:1.8; margin-top:8px; padding:10px; background:rgba(0,0,0,0.25); border-radius:6px;">
          <div>Player World: <span id="simPlayerPos" style="color:var(--accent);">X: 250, Y: 200</span></div>
          <div>Camera Offset: <span id="simCameraPos" style="color:var(--green);">X: 0, Y: 0</span></div>
          <div>Viewport Size: <span style="color:var(--ink-2);">460 x 260 px</span></div>
          <div>World Dungeon: <span style="color:var(--ink-2);">920 x 520 px (200%)</span></div>
        </div>
        <div style="margin-top:12px; display:flex; flex-direction:column; gap:8px;">
          <button class="btn" id="btnToggleCam" onclick="toggleSimCamera()" data-ru="📷 Слежение камеры: ВКЛ" data-en="📷 Camera Follow: ON">📷 Kamera Kuzatuvi: YOQILGAN</button>
          <button class="btn" id="btnToggleFog" onclick="toggleSimFog()" data-ru="🌫️ Туман Войны: ВКЛ" data-en="🌫️ Fog of War: ON">🌫️ Urush Tumani: YOQILGAN</button>
          <div style="font-size:12px; color:var(--ink-2); margin-top:4px;" data-ru="Факел пульсирует случайным мерцанием огня (Flicker Effect)" data-en="Torch pulsates with organic fire flicker effect">Mash'ala olov kabi miltillab nur taratadi (Flicker)</div>
        </div>
      </div>
    </div>
  </section>""")

    # Slide 6: Smooth Lerp Smoothing
    slides.append("""  <!-- SLIDE 6: LERP SMOOTHING -->
  <section class="slide" data-phase="Algoritm|Алгоритм|Algorithm" data-time="36:00–42:00">
    <div class="eyebrow" data-ru="ПЛАВНОСТЬ И КИНЕМАТОГРАФИЧНОСТЬ" data-en="SMOOTHNESS & CINEMATICS">SILLIQ HARAKAT</div>
    <h2 data-ru="Алгоритм Плавного Слежения (Lerp Camera)" data-en="Smooth Follow Algorithm (Lerp Camera)">Kameraning Silliq Kuzatuvi: Lerp Formulasi</h2>
    <p class="lede" data-ru="Жестко привязанная камера дергается при каждом шаге и утомляет зрение. Профессионалы используют Linear Interpolation (Lerp):" data-en="A rigid camera snaps abruptly causing player nausea. Commercial engines leverage Linear Interpolation (Lerp) for cinematic follow:">Qattiq bog'langan kamera har qadamda silkinib ko'zni toliqtiradi. Silliq kino effektini olish uchun Chiziqli Interpolyatsiya (Lerp) ishlatiladi:</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Математическая Формула" data-en="Mathematical Formulation">Matematik Formula</h3>
        <p data-ru="Каждый кадр камера делает шаг навстречу цели на определенный процент дистанции:" data-en="Each frame the camera advances towards target by a fractional coefficient:">Har bir kadrda (frame) kamera qahramonga qarab masofaning belgilangan foiziga siljiydi:</p>
        <pre class="code-snippet" style="font-size:12px; margin-top:8px;"><code>// Lerp: camera.x += (target - current) * speed
const targetX = player.x - VIEWPORT_WIDTH / 2;
const targetY = player.y - VIEWPORT_HEIGHT / 2;

// Silliq 10% yaqinlashish har kadrda
camera.x += (targetX - camera.x) * 0.1;
camera.y += (targetY - camera.y) * 0.1;</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Коэффициент Скорости (Speed)" data-en="Follow Speed Coefficient">Tezlik Koeffitsiyenti (Speed)</h3>
        <ul style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="speed = 1.0 ➔ Жесткая камера, мгновенный сдвиг" data-en="speed = 1.0 ➔ Rigid snapping, instantaneous lock"><code>speed = 1.0</code> ➔ Qattiq bog'lanish, darhol burilish</li>
          <li data-ru="speed = 0.1 ➔ Идеальный баланс динамики и мягкости" data-en="speed = 0.1 ➔ Ideal balance between agility and smoothness"><code>speed = 0.1</code> ➔ Eng zo'r muvozanat va muloyimlik</li>
          <li data-ru="speed = 0.02 ➔ Тяжелая, кинематографичная камера" data-en="speed = 0.02 ➔ Heavy cinematic drifter drone"><code>speed = 0.02</code> ➔ Og'ir kinokamera yoki dron effekti</li>
        </ul>
      </div>
    </div>
    <div class="card" style="margin-top:14px;">
      <p style="font-size:13px;" data-ru="💡 Простой трюк: Если персонаж ускоряется (бег на Shift), камера может плавно отдаляться назад, расширяя обзор!" data-en="💡 Pro Tip: When sprinting on Shift, you can dynamically zoom out camera scale to widen player perspective!">💡 Pro Maslahat: Agar qahramon yugursa (Shift), kamerani biroz orqaroqqa tortib ko'rish burchagini kengaytirish mumkin!</p>
    </div>
  </section>""")

    # Slide 7: What is Fog of War
    slides.append("""  <!-- SLIDE 7: WHAT IS FOG OF WAR -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="42:00–48:00">
    <div class="eyebrow" data-ru="АТМОСФЕРА И ИГРОВОЙ БАЛАНС" data-en="ATMOSPHERE & GAME BALANCE">O'YIN SIRI VA TUZILISHI</div>
    <h2 data-ru="Что Такое Fog of War (Туман Войны)?" data-en="What is Fog of War (Field of View)?">Fog of War (Urush Tumani) Nima va Nega Kerak?</h2>
    <p class="lede" data-ru="Если игрок видит всю карту целиком — пропадает интрига, страх и дух исследования. Туман войны делит мир на 3 состояния:" data-en="Revealing the entire labyrinth upfront destroys mystery and tension. Fog of war segments dungeons into 3 distinct layers:">Agar butun labirint birdaniga ko'rinib tursa — qidirish zavqi, qo'rquv va sarguzasht yo'qoladi. Urush tumani dunyoni 3 ta holatga ajratadi:</p>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <span class="pill" style="background:#111; color:#fff;" data-ru="1. Неизведанное" data-en="1. Unexplored">1. Noma'lum (Unexplored)</span>
        <h3 style="margin-top:10px;" data-ru="Абсолютная Тьма" data-en="Pitch Black Void">Mutlaq Qorong'ulik</h3>
        <p data-ru="Непроглядный черный цвет (Alpha: 1.0). Игрок еще ни разу здесь не ступал. Не видны ни стены, ни монстры." data-en="Pitch black (Alpha: 1.0). Player has never set foot here. Neither walls nor monsters are known.">Qop-qora parda (Alpha: 1.0). Qahramon bu yerga hali bormagan. Devorlar ham, dushmanlar ham ko'rinmaydi.</p>
      </div>
      <div class="card">
        <span class="pill" style="background:#374151; color:#f3f4f6;" data-ru="2. Разведанное" data-en="2. Explored (Memory)">2. Kashf Qilingan (Memory)</span>
        <h3 style="margin-top:10px;" data-ru="Память Карты (Сумерки)" data-en="Map Memory (Dim Fog)">Xotira (Xira Soya)</h3>
        <p data-ru="Полупрозрачный сумрак (Alpha: 0.6). Игрок помнит форму комнат и стен, но враги в реальном времени скрыты!" data-en="Dim twilight (Alpha: 0.6). Player remembers room boundaries, but active monsters remain hidden!">Yarim-shaffof soya (Alpha: 0.6). O'yinchi xonalar qayerdaligini eslaydi, lekin jonli dushmanlar yashiringan!</p>
      </div>
      <div class="card green">
        <span class="pill green" data-ru="3. Поле Зрения" data-en="3. Field of View">3. Ko'rish Maydoni (Visible)</span>
        <h3 style="margin-top:10px;" data-ru="Круг Света Факела" data-en="Active Torchlight">Mash'ala Nuri (Yorug')</h3>
        <p data-ru="Полная видимость (Alpha: 0.0). Прямой радиус видимости вокруг персонажа. Видно все золото, ловушки и врагов." data-en="Full visibility (Alpha: 0.0). Radius of light cast by torch. Reveals treasures, traps, and moving targets.">To'liq ochiq (Alpha: 0.0). Qahramon atrofi 100% ko'rinadi. Oltinlar, tuzoqlar va dushmanlar aniq namoyon bo'ladi.</p>
      </div>
    </div>
  </section>""")

    # Slide 8: Radial Gradient Torchlight
    slides.append("""  <!-- SLIDE 8: RADIAL GRADIENT -->
  <section class="slide" data-phase="Muhandislik|Инженерия|Engineering" data-time="48:00–56:00">
    <div class="eyebrow" data-ru="ГРАФИЧЕСКИЙ РЕНДЕР СВЕТА В CANVAS" data-en="CANVAS LIGHTING & SHADERS">MASH'ALA NURINI CHIZISH</div>
    <h2 data-ru="Свет Факела: Метод createRadialGradient" data-en="Torchlight: createRadialGradient Technique">Radial Gradient Bilan Mash'ala Nurini Yaratish</h2>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Как Работает Радиальный Градиент" data-en="How Radial Gradients Work">Radial Gradient Mantig'i</h3>
        <p data-ru="Градиент строится между двумя кругами: внутренним (яркий центр) и внешним (граница тьмы):" data-en="Constructs light falloff between two concentric circles: inner core and outer darkness:">Gradient ikkita aylana orasida quriladi: ichki aylana (yorug' o'zak) va tashqi aylana (tuman chegarasi):</p>
        <pre class="code-snippet" style="font-size:12px; margin-top:8px;"><code>// Mash'ala nuri: Markazdan chetga xiralashish
const innerRadius = 25;
const outerRadius = 150;

const grad = ctx.createRadialGradient(
  playerScreenX, playerScreenY, innerRadius,
  playerScreenX, playerScreenY, outerRadius
);

grad.addColorStop(0, "rgba(0, 0, 0, 0)");   // Markaz: 100% shaffof
grad.addColorStop(0.7, "rgba(5, 8, 16, 0.4)"); // Yarim soya
grad.addColorStop(1, "rgba(5, 8, 16, 0.98)");  // Mutlaq qorong'ilik</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Эффект Живого Огня (Flicker)" data-en="Living Fire Flicker Effect">Jonli Olov Effekti (Flicker)</h3>
        <p data-ru="Настоящий факел никогда не светит статично. Добавляем синусоиду и случайные микро-всплески:" data-en="Real torches flicker organically. Inject harmonic sine oscillations with micro noise:">Haqiqiy mash'ala hech qachon bir tekis turmaydi. Unga sinus to'lqini va tasodifiy miltillash qo'shamiz:</p>
        <pre class="code-snippet" style="font-size:12px; margin-top:8px;"><code>// Har kadrda mash'ala o'lchamini tebratish
const time = Date.now() * 0.005;
const flicker = Math.sin(time) * 6 + (Math.random() * 3);
const dynamicRadius = baseRadius + flicker;</code></pre>
        <div style="margin-top:8px; font-size:12px; color:var(--ink-2);" data-ru="Это создает невероятно атмосферный эффект настоящего огня в пещере!" data-en="Delivers an authentic torch feel illuminating dark dungeon corridors!">Bu g'ordagi haqiqiy olovdek ajoyib kinematik atmosfera beradi!</div>
      </div>
    </div>
  </section>""")

    # Slide 9: destination-out Magic
    slides.append("""  <!-- SLIDE 9: DESTINATION OUT -->
  <section class="slide" data-phase="Muhandislik|Инженерия|Engineering" data-time="56:00–62:00">
    <div class="eyebrow" data-ru="РЕЖИМЫ СМЕШИВАНИЯ CANVAS" data-en="CANVAS BLENDING MODES">DESTINATION-OUT SEHRI</div>
    <h2 data-ru="Прорезание Тьмы: globalCompositeOperation" data-en="Carving Darkness: globalCompositeOperation">Qorong'ilikni O'yib Yoritish: destination-out</h2>
    <p class="lede" data-ru="Вместо высветления каждого отдельного пикселя, мы используем мощную маску прозрачности Canvas:" data-en="Instead of manually computing light falloff on every tile, we leverage hardware-accelerated canvas masks:">Har bir taylga alohida chiroq yoqish o'rniga, Canvasning qudratli shaffoflik rejimini ishlatamiz:</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Порядок Рендеринга 3 Шагов" data-en="3-Step Composite Pipeline">3 Qadamli Algoritm</h3>
        <ol style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="Шаг 1: Рисуем весь лабиринт и персонажа как обычно" data-en="Step 1: Render complete dungeon tiles and hero normally">1-Qadam: Butun labirint va qahramon odatdagidek chiziladi</li>
          <li data-ru="Шаг 2: Заливаем весь экран черным прямоугольником тьмы" data-en="Step 2: Flood the screen with a solid pitch-black darkness layer">2-Qadam: Ekran ustidan to'liq qora tuman parda tortiladi</li>
          <li data-ru="Шаг 3: Включаем destination-out и вырезаем круг света вокруг игрока!" data-en="Step 3: Switch to destination-out and punch a hole where torch shines!">3-Qadam: <code>destination-out</code> rejimida mash'ala nuri bilan qora pardada teshik o'yiladi!</li>
        </ol>
      </div>
      <div class="card">
        <h3 data-ru="Код Маски Прозрачности" data-en="Mask Implementation Code">Shaffoflik Maskasi Kodi</h3>
        <pre class="code-snippet" style="font-size:12px; margin-top:8px;"><code>// 1. Qorong'i tuman pardasi
ctx.fillStyle = "rgba(5, 8, 16, 0.95)";
ctx.fillRect(0, 0, VIEW_W, VIEW_H);

// 2. Teshik o'yish rejimiga o'tish
ctx.globalCompositeOperation = "destination-out";

// 3. Mash'ala joyini o'yib tashlash!
ctx.fillStyle = torchGradient;
ctx.beginPath();
ctx.arc(heroScreenX, heroScreenY, radius, 0, Math.PI * 2);
ctx.fill();

// 4. Standart chizish rejimiga qaytish
ctx.globalCompositeOperation = "source-over";</code></pre>
      </div>
    </div>
  </section>""")

    # Slide 10: Explored Map Memory
    slides.append("""  <!-- SLIDE 10: EXPLORED MAP MEMORY -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="62:00–68:00">
    <div class="eyebrow" data-ru="СОСТОЯНИЕ И ПАМЯТЬ ИССЛЕДОВАНИЯ" data-en="EXPLORATION PERSISTENCE STATE">XOTIRALI TUMAN</div>
    <h2 data-ru="Память Карты: Массив Explored Tiles" data-en="Persistent Map Memory: Explored Matrix">Xarita Xotirasi: Kashf Qilingan Joylarni Eslab Qolish</h2>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Матрица Состояний Разведки" data-en="Exploration State Matrix">Kashfiyot Matritsasi</h3>
        <p data-ru="Создаем 2D булевый массив размером с нашу карту. Если тайл попал в радиус света — помечаем его навсегда:" data-en="Instantiate a parallel 2D boolean array. Whenever a tile falls inside torch radius, flag it as permanently revealed:">Xaritaga teng o'lchamli 2D mantiqiy (boolean) massiv yaratamiz. Qahramon mash'alasi tegishi bilan unga <code>true</code> yoziladi:</p>
        <pre class="code-snippet" style="font-size:12px; margin-top:8px;"><code>// Har bir xonaning kashf etilganligini saqlash
const explored = Array(ROWS).fill(null).map(() =&gt; Array(COLS).fill(false));

function updateExploration(playerX, playerY, radius) {
  // Mash'ala atrofidagi kataklarni true qilish
  const pCol = Math.floor(playerX / TILE);
  const pRow = Math.floor(playerY / TILE);
  // ... Atrofdagi radiusdagi kataklar:
  explored[r][c] = true;
}</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Отрисовка Разведанных Стен" data-en="Rendering Explored Walls">Kashf Qilingan Joylarni Ko'rsatish</h3>
        <ul style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="explored[r][c] === false ➔ Полная тьма (черный квадрат)" data-en="explored[r][c] === false ➔ Total black void"><code>explored[r][c] === false</code> ➔ Mutlaq qora kvadrat</li>
          <li data-ru="explored === true, но игрок далеко ➔ Рисуем в 50% полутени" data-en="explored === true, but player far ➔ Render at 50% dim opacity"><code>explored === true</code>, uzoqda ➔ 50% xiralikdagi ko'k/kulrang devor</li>
          <li data-ru="В поле зрения прямо сейчас ➔ Полный цвет и 100% яркость" data-en="Inside active torchlight ➔ Vibrant 100% brightness">Hozir mash'ala ostida ➔ 100% to'liq yorug'lik</li>
        </ul>
      </div>
    </div>
    <div class="card" style="margin-top:14px;">
      <h3 data-ru="Гейм-дизайн эффект" data-en="Game Design Impact">Geym-Dizayn Ta'siri</h3>
      <p style="font-size:13px;" data-ru="Игрок всегда понимает, где выход и куда он уже ходил, но боится идти в непроверенные черные зоны лабиринта!" data-en="The player navigates previously traversed halls without losing orientation while dreading unrevealed dark corridors!">O'yinchi qayerdan kelgani va xaritaning tuzilishini unutmaydi, lekin yangi qora xonalarga kirishda ehtiyotkor bo'ladi!</p>
    </div>
  </section>""")

    # Slide 11: 25-Min Cyber Arena
    slides.append("""  <!-- SLIDE 11: ARENA LAB -->
  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="68:00–74:00">
    <div class="eyebrow" data-ru="БОЛЬШАЯ ПРАКТИЧЕСКАЯ АРЕНА (25 МИНУТ)" data-en="25-MINUTE CYBER ARENA">AMALIY ARENA</div>
    <h2 data-ru="Задание: Собери Dungeon с Камерой и Факелом" data-en="Mission: Construct Dungeon Camera & Torchlight">Kiber-Missiya: Dungeonda Kamera va Mash'ala Qurish</h2>
    <p class="lede" data-ru="Откройте симулятор simulator/index.html и выполните 3 инженерных шага за 25 минут:" data-en="Launch simulator/index.html and accomplish 3 engineering milestones within 25 minutes:">Kompyuteringizda <b>simulator/index.html</b> faylini oching va 25 daqiqada 3 ta vazifani bajaring:</p>
    
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Чек-лист Разработчика" data-en="Developer Checklist">Muhandislik Bosqichlari</h3>
        <ol style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="Привязать камеру к игроку с помощью Math.max и Math.min (Clamping)" data-en="Bind camera to player with boundary clamping via Math.max/Math.min">Kamerani qahramon markaziga bog'lab, Clamping bilan xarita chetidan chiqarmaslik</li>
          <li data-ru="Включить радиальный градиент createRadialGradient для эффекта огня" data-en="Enable createRadialGradient torchlight with warm glow palette">Olovdek nurlanuvchi Radial Gradient mash'alasini o'yinchiga o'rnatish</li>
          <li data-ru="Найти спрятанный в лабиринте золотой артефакт в темной комнате!" data-en="Uncover hidden golden artifact in the farthest pitch-black dungeon chamber!">Labirintning qorong'i burchagiga yashiringan oltin artefaktni topish!</li>
        </ol>
      </div>

      <!-- Live 25-Min Timer Card -->
      <div class="card" style="text-align:center; padding:16px;">
        <span class="pill" data-ru="Таймер Лаборатории" data-en="Arena Timer">Arena Taymeri</span>
        <div id="deckTimerDisplay" style="font-family:'JetBrains Mono',monospace; font-size:44px; font-weight:800; color:var(--accent); margin:12px 0;">25:00</div>
        <div style="display:flex; justify-content:center; gap:8px;">
          <button class="btn" onclick="startDeckTimer(25)" data-ru="▶ Старт (25 мин)" data-en="▶ Start (25m)">▶ Boshlash (25m)</button>
          <button class="btn" onclick="resetDeckTimer()" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta o'rnatish</button>
        </div>
        <div style="font-size:12px; color:var(--ink-2); margin-top:10px;" data-ru="Учитель ходит по рядам и помогает настроить clamping и lerp" data-en="Teacher navigates the floor debugging coordinate offsets">O'qituvchi o'quvchilarga koordinata va clamping xatolarini to'g'rilashda ko'maklashadi</div>
      </div>
    </div>
  </section>""")

    # Slide 12: Interactive Quiz
    slides.append("""  <!-- SLIDE 12: QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Interactive Quiz" data-time="74:00–77:00">
    <div class="eyebrow" data-ru="ПРОВЕРКА ЗНАНИЙ (3 ВОПРОСА)" data-en="KNOWLEDGE CHECK (3 QUESTIONS)">INTERAKTIV QUIZ</div>
    <h2 data-ru="Блиц-Тест: Камера и Туман Войны" data-en="Fast Quiz: Camera & Fog of War">Bilimni Sinash: Kamera va Urush Tumani</h2>
    <div class="grid c3" style="margin-top:16px;">
      <!-- Q1 -->
      <div class="card quiz-card">
        <h4 data-ru="1. Зачем вычитать половину экрана из позиции камеры?" data-en="1. Why subtract half viewport from camera coords?">1. Nega kamera koordinatasidan ekran yarmisi ayiriladi?</h4>
        <div class="quiz-options" style="display:flex; flex-direction:column; gap:6px; margin-top:8px;">
          <button class="btn" onclick="checkDeckQuiz(this, false)" data-ru="А) Чтобы камера двигалась быстрее" data-en="A) To speed up camera">A) Kamera tezroq harakatlanishi uchun</button>
          <button class="btn" onclick="checkDeckQuiz(this, true)" data-ru="Б) Чтобы игрок стоял ровно в центре экрана" data-en="B) To position player dead center">B) Qahramon ekran markazida turishi uchun</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" data-ru="В) Чтобы перевернуть координаты" data-en="C) To invert axes">C) Koordinatalarni teskari qilish uchun</button>
        </div>
      </div>

      <!-- Q2 -->
      <div class="card quiz-card">
        <h4 data-ru="2. Что делает режим destination-out в Canvas?" data-en="2. What does destination-out do in Canvas?">2. destination-out rejimi Canvasda nima qiladi?</h4>
        <div class="quiz-options" style="display:flex; flex-direction:column; gap:6px; margin-top:8px;">
          <button class="btn" onclick="checkDeckQuiz(this, false)" data-ru="А) Рисует белую рамку вокруг экрана" data-en="A) Draws white outline">A) Ekran atrofiga oq ramka chizadi</button>
          <button class="btn" onclick="checkDeckQuiz(this, true)" data-ru="Б) Стирает/прорезает отверстие в темном слое" data-en="B) Punches a transparent hole in layer">B) Qorong'i pardani o'yib, teshik ochadi</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" data-ru="В) Ускоряет FPS игры в 2 раза" data-en="C) Doubles frame rate">C) O'yin kadrlar tezligini 2 baravar oshiradi</button>
        </div>
      </div>

      <!-- Q3 -->
      <div class="card quiz-card">
        <h4 data-ru="3. Что означает число 0.1 в формуле Lerp?" data-en="3. What does 0.1 coefficient mean in Lerp?">3. Lerp formulasidagi 0.1 soni nimani bildiradi?</h4>
        <div class="quiz-options" style="display:flex; flex-direction:column; gap:6px; margin-top:8px;">
          <button class="btn" onclick="checkDeckQuiz(this, true)" data-ru="А) Камера проходит 10% дистанции за кадр" data-en="A) Camera closes 10% of gap per frame">A) Kamera har kadrda masofaning 10%iga siljiydi</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" data-ru="Б) Задержка ровно в 10 секунд" data-en="B) Fixed 10s lag">B) Kamera 10 soniyaga kechikib yuradi</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" data-ru="В) Разрешение экрана уменьшено в 10 раз" data-en="C) Scale reduced by 10x">C) Ekran masshtabi 10 barobar kichrayadi</button>
        </div>
      </div>
    </div>
  </section>""")

    # Slide 13: 3-Tier Homework
    slides.append("""  <!-- SLIDE 13: 3-TIER HOMEWORK -->
  <section class="slide" data-phase="Vazifa|Задание|Homework" data-time="77:00–79:00">
    <div class="eyebrow" data-ru="ДОМАШНЕЕ ЗАДАНИЕ (10 БАЛЛОВ)" data-en="HOMEWORK (10 POINTS)">UY VAZIFASI</div>
    <h2 data-ru="3 Уровня Мастерства: Домашний Проект" data-en="3-Tier Mastery: Dungeon Assignment">3 Darajali Uy Vazifasi (10 Ballik Rubrika)</h2>
    <p class="lede" data-ru="Откройте интерактивную страницу vazifa.html и реализуйте 3 уровня сложности:" data-en="Open interactive vazifa.html and implement the 3 tiered challenge levels:">O'quvchi portalida <b>vazifa.html</b> sahifasini oching va 3 ta darajani bajaring:</p>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <span class="pill" data-ru="1-Уровень · 4 балла" data-en="Tier 1 · 4 pts">1-Daraja · 4 Ball</span>
        <h3 style="margin-top:10px;" data-ru="Базовая Центровка" data-en="Basic Clamped Viewport">Baza: Clamping</h3>
        <p data-ru="Написать формулу камеры и ограничить координаты camera.x и camera.y, чтобы не выходить за пределы мира 1600x1200." data-en="Write camera viewport logic and clamp camera.x and camera.y within 1600x1200 world boundaries.">Kamera koordinatasini hisoblash va 1600x1200 dunyodan chiqib ketmaslik uchun to'liq Clamping shartini yozish.</p>
      </div>
      <div class="card">
        <span class="pill" data-ru="2-Уровень · 4 балла" data-en="Tier 2 · 4 pts">2-Daraja · 4 Ball</span>
        <h3 style="margin-top:10px;" data-ru="Мерцающий Факел" data-en="Animated Torchlight">Muhandislik: Mash'ala</h3>
        <p data-ru="Создать радиальный градиент вокруг персонажа с эффектом мерцания огня (Math.sin) и прорезать тьму через destination-out." data-en="Create radial gradient torchlight with sine-wave flicker oscillations and carve dark mask via destination-out.">Qahramon atrofida createRadialGradient bilan olovdek miltillovchi mash'ala yaratish va qorong'ilikni yorib ko'rsatish.</p>
      </div>
      <div class="card green">
        <span class="pill green" data-ru="3-Уровень · 2 балла" data-en="Tier 3 · 2 pts">3-Daraja · 2 Ball</span>
        <h3 style="margin-top:10px;" data-ru="Память Разведки" data-en="Persistent Map Memory">Kiber-Chaqliriq: Xotira</h3>
        <p data-ru="Реализовать массив explored[row][col]: пройденные участки лабиринта должны оставаться видимыми в полутени!" data-en="Implement explored[row][col] grid state: previously traversed sectors must persist in twilight visibility!">explored[row][col] massivini qurish: qahramon ko'rib o'tgan barcha xonalar xira tuman soyasida ko'rinib turishi kerak!</p>
      </div>
    </div>
  </section>""")

    # Slide 14: Summary & Next Bridge
    slides.append("""  <!-- SLIDE 14: SUMMARY -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="79:00–80:00">
    <div class="eyebrow" data-ru="РЕЗЮМЕ И СЛЕДУЮЩИЙ ШАГ" data-en="SUMMARY & ROADMAP">XULOSA VA REJA</div>
    <h2 data-ru="Чему Мы Научились и Что Дальше?" data-en="Key Takeaways & Next Horizon">Bugun Nimalarni O'rgandik va Keyingi Qadam</h2>
    <div class="grid c2" style="margin-top:20px;">
      <div class="card">
        <h3 data-ru="Главные навыки за 80 минут" data-en="Key Skills Mastered">80 Daqiqada O'zlashtirilgan Ko'nikmalar</h3>
        <ul style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="World Space vs Screen Space и трансформация ctx.translate" data-en="World Space vs Screen Space and ctx.translate transforms">World va Screen Space farqi hamda <code>ctx.translate</code> bilan dunyoni surish</li>
          <li data-ru="Центрирование персонажа и жесткий Clamping краев карты" data-en="Camera centering and strict boundary clamping">Qahramonni ekranda markazlashtirish va xarita chetlarini Clamping bilan qulflash</li>
          <li data-ru="Кинематографичный Lerp для сглаживания рывков камеры" data-en="Smooth Lerp motion eliminating harsh camera snapping">Kamera silkinishlarini yo'qotuvchi kinematik Lerp silliqlash algoritmi</li>
          <li data-ru="Свет факела через createRadialGradient и destination-out" data-en="Torchlight mechanics via createRadialGradient & destination-out">Radial gradient va <code>destination-out</code> orqali haqiqiy Roguelike tumanini qurish</li>
        </ul>
      </div>
      <div class="card">
        <h3 data-ru="Анонс следующего урока (11-я неделя)" data-en="Next Lesson Sneak Peek (Week 11)">Keyingi Darsda Bizni Nima Kutmoqda?</h3>
        <p style="font-size:13px; margin-top:8px;" data-ru="В следующий раз мы сделаем мир бесконечным и непредсказуемым: Процедурная генерация лабиринтов (Procedural Content Generation — PCG). Алгоритм будет сам случайно строить комнаты, коридоры и прятать сундуки с золотом!" data-en="Next lesson we introduce infinite unpredictability: Procedural Content Generation (PCG). Algorithms will autonomously construct branching dungeons, corridors, and treasure vaults!">Keyingi darsda labirintni cheksiz va kutilmagan qilamiz: Procedural Dunyo Yaratilishi (Procedural Content Generation — PCG). Algoritm har safar tasodifiy yangi xonalar, yo'laklar va xazinalar qurib beradi!</p>
        <div style="margin-top:14px; font-weight:700; color:var(--accent);" data-ru="Спасибо за отличную инженерную работу на уроке!" data-en="Great engineering work today! Keep building awesome games!">Darsdagi faol va ajoyib muhandislik mehnatingiz uchun tashakkur!</div>
      </div>
    </div>
  </section>""")

    # Combine slides
    all_slides_html = "\n\n".join(slides)
    tpl = re.sub(r'<div class="stage" id="stage">[\s\S]*?</div><!-- /stage -->', f'<div class="stage" id="stage">\n{all_slides_html}\n</div><!-- /stage -->', tpl)

    # Simulator JavaScript in presentation
    sim_js = """
// ============================================================
// PRESENTATION INTERACTIVE SIMULATOR (Slide 5: Camera & Fog)
// ============================================================
var simState = {
  playerX: 230,
  playerY: 130,
  camX: 0,
  camY: 0,
  camFollow: true,
  fogEnabled: true,
  worldW: 920,
  worldH: 520,
  viewW: 460,
  viewH: 260,
  torchBaseRadius: 90
};

function initDeckSim() {
  var cvs = document.getElementById("deckSimCanvas");
  if (!cvs) return;
  drawDeckSim();
}

function moveSimPlayer(dx, dy) {
  simState.playerX = Math.max(30, Math.min(simState.worldW - 30, simState.playerX + dx));
  simState.playerY = Math.max(30, Math.min(simState.worldH - 30, simState.playerY + dy));

  if (simState.camFollow) {
    var targetCamX = simState.playerX - simState.viewW / 2;
    var targetCamY = simState.playerY - simState.viewH / 2;
    simState.camX = Math.max(0, Math.min(targetCamX, simState.worldW - simState.viewW));
    simState.camY = Math.max(0, Math.min(targetCamY, simState.worldH - simState.viewH));
  }
  updateDeckTelemetry();
  drawDeckSim();
}

function toggleSimCamera() {
  simState.camFollow = !simState.camFollow;
  var btn = document.getElementById("btnToggleCam");
  if (btn) {
    btn.textContent = simState.camFollow ? 
      (currentLang === 'ru' ? '📷 Слежение камеры: ВКЛ' : (currentLang === 'en' ? '📷 Camera Follow: ON' : '📷 Kamera Kuzatuvi: YOQILGAN')) :
      (currentLang === 'ru' ? '📷 Слежение камеры: ВЫКЛ' : (currentLang === 'en' ? '📷 Camera Follow: OFF' : '📷 Kamera Kuzatuvi: O\\'CHIRILGAN'));
  }
  if (simState.camFollow) {
    simState.camX = Math.max(0, Math.min(simState.playerX - simState.viewW / 2, simState.worldW - simState.viewW));
    simState.camY = Math.max(0, Math.min(simState.playerY - simState.viewH / 2, simState.worldH - simState.viewH));
  } else {
    simState.camX = 0;
    simState.camY = 0;
  }
  updateDeckTelemetry();
  drawDeckSim();
}

function toggleSimFog() {
  simState.fogEnabled = !simState.fogEnabled;
  var btn = document.getElementById("btnToggleFog");
  if (btn) {
    btn.textContent = simState.fogEnabled ? 
      (currentLang === 'ru' ? '🌫️ Туман Войны: ВКЛ' : (currentLang === 'en' ? '🌫️ Fog of War: ON' : '🌫️ Urush Tumani: YOQILGAN')) :
      (currentLang === 'ru' ? '🌫️ Туман Войны: ВЫКЛ' : (currentLang === 'en' ? '🌫️ Fog of War: OFF' : '🌫️ Urush Tumani: O\\'CHIRILGAN'));
  }
  drawDeckSim();
}

function updateDeckTelemetry() {
  var pEl = document.getElementById("simPlayerPos");
  var cEl = document.getElementById("simCameraPos");
  if (pEl) pEl.textContent = "X: " + Math.round(simState.playerX) + ", Y: " + Math.round(simState.playerY);
  if (cEl) cEl.textContent = "X: " + Math.round(simState.camX) + ", Y: " + Math.round(simState.camY);
}

function drawDeckSim() {
  var cvs = document.getElementById("deckSimCanvas");
  if (!cvs) return;
  var ctx = cvs.getContext("2d");
  var vw = simState.viewW;
  var vh = simState.viewH;

  // Clear
  ctx.clearRect(0, 0, vw, vh);

  ctx.save();
  // Camera transform!
  ctx.translate(-simState.camX, -simState.camY);

  // 1. Draw Dungeon Floor Grid
  ctx.fillStyle = "#151b2b";
  ctx.fillRect(0, 0, simState.worldW, simState.worldH);

  ctx.strokeStyle = "rgba(255,255,255,0.06)";
  ctx.lineWidth = 1;
  var gridStep = 40;
  for (var gx = 0; gx <= simState.worldW; gx += gridStep) {
    ctx.beginPath(); ctx.moveTo(gx, 0); ctx.lineTo(gx, simState.worldH); ctx.stroke();
  }
  for (var gy = 0; gy <= simState.worldH; gy += gridStep) {
    ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(simState.worldW, gy); ctx.stroke();
  }

  // 2. Draw Dungeon Walls
  ctx.fillStyle = "#2d3748";
  var walls = [
    [0, 0, simState.worldW, 20],
    [0, 0, 20, simState.worldH],
    [0, simState.worldH - 20, simState.worldW, 20],
    [simState.worldW - 20, 0, 20, simState.worldH],
    [160, 20, 30, 260],
    [360, 200, 30, 260],
    [540, 60, 30, 300],
    [700, 240, 160, 30]
  ];
  walls.forEach(function(w) {
    ctx.fillRect(w[0], w[1], w[2], w[3]);
    ctx.strokeStyle = "#4a5568";
    ctx.strokeRect(w[0], w[1], w[2], w[3]);
  });

  // 3. Draw Treasures
  var treasures = [[100, 80], [450, 420], [800, 120]];
  treasures.forEach(function(t, idx) {
    ctx.fillStyle = "#f59e0b";
    ctx.beginPath(); ctx.arc(t[0], t[1], 10, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = "#fff";
    ctx.font = "10px sans-serif";
    ctx.fillText("💎", t[0] - 6, t[1] + 4);
  });

  // 4. Draw Player
  ctx.fillStyle = "#3b82f6";
  ctx.beginPath();
  ctx.arc(simState.playerX, simState.playerY, 14, 0, Math.PI * 2);
  ctx.fill();
  ctx.strokeStyle = "#93c5fd";
  ctx.lineWidth = 2;
  ctx.stroke();

  // Eyes
  ctx.fillStyle = "#ffffff";
  ctx.beginPath(); ctx.arc(simState.playerX - 4, simState.playerY - 2, 3, 0, Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(simState.playerX + 4, simState.playerY - 2, 3, 0, Math.PI*2); ctx.fill();

  ctx.restore();

  // 5. Fog of War layer (Screen Space)
  if (simState.fogEnabled) {
    var pScreenX = simState.playerX - simState.camX;
    var pScreenY = simState.playerY - simState.camY;

    // Dark blanket
    ctx.save();
    ctx.fillStyle = "rgba(7, 10, 19, 0.94)";
    ctx.fillRect(0, 0, vw, vh);

    // Punch torch hole
    ctx.globalCompositeOperation = "destination-out";
    var grad = ctx.createRadialGradient(pScreenX, pScreenY, 20, pScreenX, pScreenY, simState.torchBaseRadius);
    grad.addColorStop(0, "rgba(0,0,0,1)");
    grad.addColorStop(0.6, "rgba(0,0,0,0.8)");
    grad.addColorStop(1, "rgba(0,0,0,0)");
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(pScreenX, pScreenY, simState.torchBaseRadius, 0, Math.PI * 2);
    ctx.fill();

    ctx.restore();
  }
}

// Global hook
window.addEventListener("DOMContentLoaded", function() {
  setTimeout(initDeckSim, 200);
});
"""

    tpl = tpl.replace("</script>\n</body>", f"{sim_js}\n</script>\n</body>")

    with open(os.path.join(LESSON_DIR, "prezentatsiya.html"), "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

    # ============================================================
    # 2. VARAQA (2-page A4 Worksheet)
    # ============================================================
    v_tpl = TPL_VAR
    v_tpl = re.sub(r"<title[^>]*>.*?</title>", f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz} — Ish Varaqasi</title>', v_tpl)
    v_tpl = re.sub(r'<span class="header-tag"[^>]*>.*?</span>', '<span class="header-tag" data-ru="7-8-СИНФ · 10-Я НЕДЕЛЯ" data-en="GRADES 7-8 · WEEK 10">7-8-SINF · 10-HAFTA</span>', v_tpl, count=1)
    v_tpl = re.sub(r'<h1[^>]*>.*?</h1>', f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>', v_tpl, count=1)
    v_tpl = re.sub(r'<p class="subtitle"[^>]*>.*?</p>', '<p class="subtitle" data-ru="Практический рабочий лист: математика камеры, ограничение краев (Clamping), Lerp и круговой свет факела." data-en="Practical worksheet: camera mathematics, boundary clamping, Lerp smoothing, and radial torchlight.">Amaliy ish varaqasi: kamera matematikasi, xarita chegaralarini qulflash (Clamping), Lerp va mash\'ala nuri.</p>', v_tpl, count=1)

    # Section 1: Cheat Sheet
    v_sec1 = """    <div class="box-grid">
      <div class="box">
        <h4 data-ru="1. Проекция на Экран" data-en="1. Screen Space Projection">1. Ekran Proyeksiyasi</h4>
        <p data-ru="Формула: ScreenX = WorldX - CameraX. Сдвиг всего холста: ctx.translate(-camX, -camY)." data-en="Formula: ScreenX = WorldX - CameraX. Canvas shift: ctx.translate(-camX, -camY).">Formula: <code>ScreenX = WorldX - CameraX</code>. Butun dunyoni siljitish: <code>ctx.translate(-camX, -camY)</code>.</p>
      </div>
      <div class="box">
        <h4 data-ru="2. Ограничение (Clamping)" data-en="2. Boundary Clamping">2. Chegaralash (Clamping)</h4>
        <p data-ru="Math.max(0, Math.min(camX, WORLD_W - VIEW_W)) гарантирует, что камера не покажет черную пустоту за картой." data-en="Math.max(0, Math.min(camX, WORLD_W - VIEW_W)) ensures camera never exposes black void beyond map edges."><code>Math.max(0, Math.min(camX, maxCamX))</code> kamera xaritadan tashqaridagi qora bo'shliqqa chiqmasligini ta'minlaydi.</p>
      </div>
      <div class="box">
        <h4 data-ru="3. Плавный Lerp" data-en="3. Smooth Lerp">3. Silliq Lerp</h4>
        <p data-ru="cam.x += (target - cam.x) * 0.1 сглаживает рывки и создает ощущение скользящей кинокамеры." data-en="cam.x += (target - cam.x) * 0.1 eliminates snapping and mimics smooth cinematic camera tracking."><code>cam.x += (target - cam.x) * 0.1</code> kamera qaltirashini yo'qotib, silliq kinokamera harakatini beradi.</p>
      </div>
      <div class="box">
        <h4 data-ru="4. Магия destination-out" data-en="4. destination-out Magic">4. destination-out Sehri</h4>
        <p data-ru="Накладываем черную пелену тьмы, а затем радиальным градиентом прорезаем прозрачное отверстие света." data-en="Lay solid darkness mask, then carve transparent aperture using radial gradient torchlight.">Qora tuman qatlami ustidan radial gradient bilan mash'ala joyini o'yib, tagidagi dunyoni ochamiz.</p>
      </div>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC1_CONTENT}}", v_sec1)

    # Section 2: Code Inspection
    v_sec2 = """    <p class="section-desc" data-ru="Проанализируйте приведенный фрагмент кода 2D-движка и заполните пропущенные участки формул:" data-en="Inspect the 2D engine code snippet and complete the omitted algorithmic formulas:">Quyidagi 2D dvigatel kodini tahlil qiling va nuqtalar o'rniga to'g'ri formulalarni yozing:</p>
    <div class="code-block">
<pre style="margin:0; font-family:'JetBrains Mono',monospace; font-size:11px; line-height:1.6;">
// 1. Qahramonni ekran markazida ushlab turish:
const targetCamX = player.worldX - ( .............................................. );
const targetCamY = player.worldY - ( .............................................. );

// 2. Xarita chegarasidan chiqmaslik (Clamping):
camera.x = Math.max(0, Math.min(targetCamX, WORLD_WIDTH - ...................... ));

// 3. Silliq Lerp yaqinlashish:
camera.x += ( ........................................ ) * 0.1;
</pre>
    </div>
    <div style="margin-top:8px;">
      <label style="font-size:11px; font-weight:700;" data-ru="Вопрос: Почему коэффициент Lerp не должен быть равен 1.0?" data-en="Question: Why shouldn't the Lerp coefficient equal 1.0?">Savol: Nega Lerp koeffitsiyenti 1.0 ga teng bo'lmasligi kerak?</label>
      <div class="write-line"></div>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC2_CONTENT}}", v_sec2)

    # Section 3: Practical Checklist Table
    v_sec3 = """    <p class="section-desc" data-ru="Запустите simulator/index.html и отметьте выполненные этапы разработки Roguelike подземелья:" data-en="Launch simulator/index.html and track completed Roguelike dungeon engineering checkpoints:">Kompyuteringizda <b>simulator/index.html</b> ilovasini ishga tushirib, quyidagi qadamlarni bajaring va tasdiqlang:</p>
    <div style="margin-top:8px;">
      <table style="width:100%; border-collapse:collapse; font-size:11px;">
        <thead>
          <tr style="border-bottom:2px solid var(--rule); text-align:left;">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Компонент" data-en="Component">Komponent</th>
            <th style="padding:4px 6px;" data-ru="Инженерная задача" data-en="Engineering Task">Muhandislik Vazifasi</th>
            <th style="padding:4px 6px;" data-ru="Ожидаемый результат" data-en="Expected Outcome">Kutilgan Natija</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="Camera Center" data-en="Camera Center">Kamera Markazi</td>
            <td style="padding:4px 6px;" data-ru="Привязать камеру к X и Y персонажа" data-en="Bind camera coords to player center">Kamerani qahramon markaziga hisoblash</td>
            <td style="padding:4px 6px;" data-ru="Герой в центре экрана" data-en="Player centered">Qahramon ekranning o'rtasida turadi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="Clamping" data-en="Clamping">Clamping</td>
            <td style="padding:4px 6px;" data-ru="Ограничить camX и camY между 0 и maxCam" data-en="Clamp cam coords between 0 and maxCam">Kamerani 0 va maxCam orasida qulflash</td>
            <td style="padding:4px 6px;" data-ru="Нет черных дыр за картой" data-en="No empty void">Xaritadan tashqari ko'rinmaydi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="Torch Radial" data-en="Torch Radial">Mash'ala Radiusi</td>
            <td style="padding:4px 6px;" data-ru="Настроить createRadialGradient" data-en="Configure createRadialGradient">createRadialGradient nurlarini sozlash</td>
            <td style="padding:4px 6px;" data-ru="Мягкое световое пятно вокруг героя" data-en="Atmospheric light pool">Qahramon atrofida yumshoq mash'ala</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="Artifact Found" data-en="Artifact Found">Artefakt</td>
            <td style="padding:4px 6px;" data-ru="Найти спрятанный алмаз в темной комнате" data-en="Locate hidden diamond in pitch-black hall">Labirint burchagidagi olmosni topish</td>
            <td style="padding:4px 6px;" data-ru="+100 Очков победы" data-en="+100 Victory Pts">+100 G'alaba ochkosi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
        </tbody>
      </table>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC3_CONTENT}}", v_sec3)

    # Section 4: 10-Point Rubric
    v_sec4 = """    <div class="box-grid" style="margin-top:6px;">
      <div class="box">
        <h4 data-ru="1-Уровень: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</h4>
        <p data-ru="Реализовать центровку камеры и ограничение краев (Clamping) без вылета за карту." data-en="Implement centered camera viewport with boundary clamping.">Kamerani qahramon markaziga bog'lash va xarita chetidan chiqarmaydigan Clamping yozish.</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="2-Уровень: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</h4>
        <p data-ru="Построить мерцающий факел через createRadialGradient и прорезать тьму через destination-out." data-en="Build animated torchlight via createRadialGradient and carve darkness mask via destination-out.">Radial gradient va destination-out orqali qorong'ilikni yoruvchi miltillovchi mash'ala yaratish.</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="3-Уровень: Вызов (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Chaqliriq (2 ball)</h4>
        <p data-ru="Создать массив explored[r][c] и сохранять разведанные комнаты в виде полутени." data-en="Author persistent explored[r][c] matrix preserving visited sectors in dim twilight.">explored[row][col] massivini yaratib, o'tilgan barcha xonalarni xira tuman soyasida saqlab qolish.</p>
        <div class="write-line"></div>
      </div>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC4_CONTENT}}", v_sec4)

    with open(os.path.join(LESSON_DIR, "varaqa.html"), "w", encoding="utf-8") as f:
        f.write(v_tpl)
    print("  ✓ Created: varaqa.html")

    # ============================================================
    # 3. VAZIFA (Interactive Web Homework)
    # ============================================================
    vaz_tpl = TPL_VAZ
    vaz_tpl = re.sub(r"<title[^>]*>.*?</title>", f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz} — Uy Vazifasi</title>', vaz_tpl)
    vaz_tpl = re.sub(r'<span class="badge"[^>]*>.*?</span>', '<span class="badge" data-ru="7-8-СИНФ · 10-Я НЕДЕЛЯ" data-en="GRADES 7-8 · WEEK 10">7-8-SINF · 10-HAFTA</span>', vaz_tpl, count=1)
    vaz_tpl = re.sub(r'<h1[^>]*>.*?</h1>', f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>', vaz_tpl, count=1)
    vaz_tpl = re.sub(r'<p class="hero-desc"[^>]*>.*?</p>', '<p class="hero-desc" data-ru="Интерактивное домашнее задание: реализуйте математику камеры, алгоритм ограничения краев (Clamping) и туман войны в Canvas." data-en="Interactive homework: implement camera mathematics, boundary clamping, and dynamic fog of war in Canvas.">Interaktiv uy vazifasi ilovasi: kamera matematikasi, xarita chegaralarini qulflash (Clamping) va Canvasda urush tumanini yarating.</p>', vaz_tpl, count=1)

    vaz_tasks = """    <!-- TASK 1 -->
    <div class="task-card">
      <div class="task-header">
        <span class="pill" data-ru="1-Уровень · 4 балла" data-en="Tier 1 · 4 pts">1-Daraja · 4 Ball</span>
        <span class="task-points" data-ru="Макс: 4 балла" data-en="Max: 4 pts">Maks: 4 ball</span>
      </div>
      <h3 style="margin-top:10px;" data-ru="Центровка Камеры и Ограничение (Clamping)" data-en="Camera Centering & Boundary Clamping">Kamerani Markazlashtirish va Chegaralash (Clamping)</h3>
      <p style="font-size:13px; color:var(--ink-2);" data-ru="Допишите функцию updateCamera, чтобы камера удерживала игрока строго по центру экрана, но никогда не показывала координаты меньше 0 или больше границ мира:" data-en="Complete the updateCamera function to center player on screen while clamping coordinates within world boundaries:"><code>updateCamera</code> funksiyasini to'ldiring: kamera o'yinchini markazda ushlasin, lekin xaritadan chiqib bo'shliqni ko'rsatmasin:</p>
      <div class="code-editor">
        <textarea id="codeTask1" rows="9" spellcheck="false" style="width:100%; font-family:'JetBrains Mono',monospace; font-size:12px; background:transparent; color:var(--ink); border:none; outline:none; resize:vertical;">function updateCamera(player, camera, viewW, viewH, worldW, worldH) {
  // 1. O'yinchini markazlashtirish
  let targetX = player.x - (viewW / 2);
  let targetY = player.y - (viewH / 2);

  // 2. Clamping: 0 va (world - view) oralig'ida qulflash
  camera.x = Math.max(0, Math.min(targetX, worldW - viewW));
  camera.y = Math.max(0, Math.min(targetY, worldH - viewH));
  return camera;
}</textarea>
      </div>
      <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center;">
        <button class="btn" onclick="verifyTask(1)" data-ru="▶ Проверить код" data-en="▶ Verify Code">▶ Kodni Tekshirish</button>
        <span id="task1Status" class="status-tag" style="display:none;"></span>
      </div>
    </div>

    <!-- TASK 2 -->
    <div class="task-card" style="margin-top:16px;">
      <div class="task-header">
        <span class="pill" data-ru="2-Уровень · 4 балла" data-en="Tier 2 · 4 pts">2-Daraja · 4 Ball</span>
        <span class="task-points" data-ru="Макс: 4 балла" data-en="Max: 4 pts">Maks: 4 ball</span>
      </div>
      <h3 style="margin-top:10px;" data-ru="Свет Факела Через createRadialGradient" data-en="Torchlight with createRadialGradient">Mash'ala Nuri va destination-out Maskasi</h3>
      <p style="font-size:13px; color:var(--ink-2);" data-ru="Напишите фрагмент отрисовки маски тьмы и прорезания отверстия света вокруг координат экрана (px, py):" data-en="Write rendering routine that floods canvas with darkness mask and punches light pool around (px, py):">Ekran koordinatalari (px, py) atrofida qorong'i tuman pardasini tortib, <code>destination-out</code> orqali mash'ala nuri teshigini o'yuvchi funksiyani yozing:</p>
      <div class="code-editor">
        <textarea id="codeTask2" rows="11" spellcheck="false" style="width:100%; font-family:'JetBrains Mono',monospace; font-size:12px; background:transparent; color:var(--ink); border:none; outline:none; resize:vertical;">function renderFog(ctx, viewW, viewH, px, py, radius) {
  ctx.save();
  // 1. Qorong'ilik pardasi
  ctx.fillStyle = "rgba(5, 8, 16, 0.95)";
  ctx.fillRect(0, 0, viewW, viewH);

  // 2. Teshik o'yish rejimiga o'tish
  ctx.globalCompositeOperation = "destination-out";

  // 3. Radial gradient nurlanishi
  let grad = ctx.createRadialGradient(px, py, 15, px, py, radius);
  grad.addColorStop(0, "rgba(0,0,0,1)");
  grad.addColorStop(1, "rgba(0,0,0,0)");
  ctx.fillStyle = grad;
  ctx.beginPath();
  ctx.arc(px, py, radius, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
}</textarea>
      </div>
      <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center;">
        <button class="btn" onclick="verifyTask(2)" data-ru="▶ Проверить код" data-en="▶ Verify Code">▶ Kodni Tekshirish</button>
        <span id="task2Status" class="status-tag" style="display:none;"></span>
      </div>
    </div>

    <!-- TASK 3 -->
    <div class="task-card" style="margin-top:16px;">
      <div class="task-header">
        <span class="pill green" data-ru="3-Уровень · 2 балла" data-en="Tier 3 · 2 pts">3-Daraja · 2 Ball</span>
        <span class="task-points" data-ru="Макс: 2 балла" data-en="Max: 2 pts">Maks: 2 ball</span>
      </div>
      <h3 style="margin-top:10px;" data-ru="Кибер-Вызов: Сохранение Памяти Разведки" data-en="Cyber Challenge: Persistent Map Memory">Kiber-Chaqliriq: Xarita Xotirasi (Explored Array)</h3>
      <p style="font-size:13px; color:var(--ink-2);" data-ru="Объясните текстом или кодом: как сделать так, чтобы пройденные игроком коридоры не скрывались обратно в полную тьму, а оставались видны в полутени?" data-en="Explain via code or engineering design: how to prevent previously explored sectors from reverting to pitch black:">O'yinchi o'tib bo'lgan xonalar yana qop-qora bo'lib qolmasdan, xira yarim soyada ko'rinib turishi uchun qanday ma'lumotlar tuzilmasi va algoritm ishlatiladi?</p>
      <div class="code-editor">
        <textarea id="codeTask3" rows="7" spellcheck="false" style="width:100%; font-family:'JetBrains Mono',monospace; font-size:12px; background:transparent; color:var(--ink); border:none; outline:none; resize:vertical;">// Bizga 2D massiv kerak: explored[row][col] = true / false.
// Qahramon qaysi katakka borsa yoki mash'ala nuri yoritsa,
// o'sha koordinataga true yoziladi.
// Chizishda:
// Agar explored[r][c] == false -> Mutlaq qora kvadrat;
// Agar explored[r][c] == true lekin qahramon uzoqda -> 50% xiralikdagi soya;
// Agar hozir nurning ostida bo'lsa -> 100% to'liq yorug' rang!</textarea>
      </div>
      <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center;">
        <button class="btn" onclick="verifyTask(3)" data-ru="▶ Проверить ответ" data-en="▶ Verify Answer">▶ Javobni Tekshirish</button>
        <span id="task3Status" class="status-tag" style="display:none;"></span>
      </div>
    </div>"""

    vaz_tpl = re.sub(r'<div class="task-list">[\s\S]*?</div><!-- /task-list -->', f'<div class="task-list">\n{vaz_tasks}\n</div><!-- /task-list -->', vaz_tpl)

    vaz_js = """
function verifyTask(taskId) {
  var tag = document.getElementById("task" + taskId + "Status");
  if (!tag) return;
  tag.style.display = "inline-block";
  tag.style.padding = "4px 8px";
  tag.style.borderRadius = "4px";
  tag.style.fontSize = "11px";
  tag.style.fontWeight = "700";

  var code = document.getElementById("codeTask" + taskId).value;

  if (taskId === 1) {
    if (code.includes("Math.max") && code.includes("Math.min") && code.includes("viewW / 2")) {
      tag.style.background = "rgba(16,185,129,0.15)";
      tag.style.color = "var(--green)";
      tag.textContent = currentLang === 'ru' ? "✓ Верно (+4 балла)" : (currentLang === 'en' ? "✓ Correct (+4 pts)" : "✓ To'g'ri (+4 ball)");
    } else {
      tag.style.background = "rgba(239,68,68,0.15)";
      tag.style.color = "var(--red)";
      tag.textContent = currentLang === 'ru' ? "⚠ Проверьте формулы Clamping" : (currentLang === 'en' ? "⚠ Check Clamping formulas" : "⚠ Clamping formulasini tekshiring");
    }
  } else if (taskId === 2) {
    if (code.includes("createRadialGradient") && code.includes("destination-out")) {
      tag.style.background = "rgba(16,185,129,0.15)";
      tag.style.color = "var(--green)";
      tag.textContent = currentLang === 'ru' ? "✓ Верно (+4 балла)" : (currentLang === 'en' ? "✓ Correct (+4 pts)" : "✓ To'g'ri (+4 ball)");
    } else {
      tag.style.background = "rgba(239,68,68,0.15)";
      tag.style.color = "var(--red)";
      tag.textContent = currentLang === 'ru' ? "⚠ Нужен destination-out и gradient" : (currentLang === 'en' ? "⚠ Need destination-out & gradient" : "⚠ destination-out va gradient zarur");
    }
  } else if (taskId === 3) {
    if (code.includes("explored") && (code.includes("true") || code.includes("massiv"))) {
      tag.style.background = "rgba(16,185,129,0.15)";
      tag.style.color = "var(--green)";
      tag.textContent = currentLang === 'ru' ? "✓ Отлично (+2 балла)" : (currentLang === 'en' ? "✓ Excellent (+2 pts)" : "✓ A'lo (+2 ball)");
    } else {
      tag.style.background = "rgba(239,68,68,0.15)";
      tag.style.color = "var(--red)";
      tag.textContent = currentLang === 'ru' ? "⚠ Опишите массив explored" : (currentLang === 'en' ? "⚠ Describe explored array" : "⚠ explored massivini tasvirlang");
    }
  }
}
"""
    vaz_tpl = vaz_tpl.replace("</script>\n</body>", f"{vaz_js}\n</script>\n</body>")

    with open(os.path.join(LESSON_DIR, "vazifa.html"), "w", encoding="utf-8") as f:
        f.write(vaz_tpl)
    print("  ✓ Created: vazifa.html")

    # ============================================================
    # 4. TEACHER READING (Briefing for 80-minute double block)
    # ============================================================
    teacher_md = """# O'qituvchi Qo'llanmasi: 30-Dars — Kamera, Viewport va Fog of War

**Fan:** Vibecoding / Game Dev & Interaktiv Veb (7–8-sinf)  
**Davomiyligi:** 80 daqiqa (Juftlik blok / Double Block)  
**Sana/Vaqt:** Payshanba, 7–8-slotlar (14:15–15:40)  
**O'qituvchi:** Ismoiljon Usmonov  

---

## 1. Darsning Pedagogik Maqsadi va Dolzarbligi

Ushbu dars 29-darsda yaratilgan 2D matritsali xaritalarga dinamika va chuqur o'yin atmosferasini beradi. 
O'quvchilar:
1. World Space va Screen Space o'rtasidagi farqni tushunadilar.
2. Butun dunyoni `ctx.translate(-camera.x, -camera.y)` orqali surishni o'rganadilar.
3. Clamping yordamida kamerani xarita chegarasida qulflashni o'zlashtiradilar.
4. Canvasda `createRadialGradient` va `globalCompositeOperation = 'destination-out'` orqali professional Roguelike urush tumanini quradilar.

---

## 2. 80 Daqiqalik Aniq Vaqt Taqsimoti (Pacing Plan)

### 1-Bosqich (00:00 – 40:00): Nazariya, Xatolar Tahlili va Jonli Simulyator
* **00:00 – 04:00 (4 min):** Titul va dars maqsadlarini belgilash (Slayd 1).
* **04:00 – 10:00 (6 min):** 29-dars Uy vazifasi tahlili: `map[x][y]` vs `map[row][col]` xatosi. Blitz savol va kameraga ko'prik (Slayd 2).
* **10:00 – 18:00 (8 min):** World Coordinates vs Screen Coordinates. Nega har bir obyektni qayta hisoblamasdan `ctx.translate` ishlatilishi tushuntiriladi (Slayd 3).
* **18:00 – 26:00 (8 min):** Kamera markazlashtirish va `Math.max/Math.min` Clamping chegaralari (Slayd 4).
* **26:00 – 36:00 (10 min):** Doskada interaktiv simulyator orqali o'yinchini harakatlantirish, kamera qulfini o'chirish/yoqish va mash'ala nurini sinash (Slayd 5).
* **36:00 – 40:00 (4 min):** Silliq harakat (Lerp) va qaltiramaydigan kamera formulasi (Slayd 6).

### 2-Bosqich (40:00 – 80:00): Tuman Texnologiyasi, 25-Minutlik Kiber-Arena va Xulosa
* **40:00 – 48:00 (8 min):** Fog of War nima: 3 ta qatlam (Unexplored, Explored, Visible) (Slayd 7-8).
* **48:00 – 54:00 (6 min):** `destination-out` kompozit operatsiyasi va `explored[r][c]` matritsa xotirasi (Slayd 9-10).
* **54:00 – 74:00 (20 min):** Katta Kiber-Arena laboratoriyasi: O'quvchilar `simulator/index.html` da mustaqil dungeonga kamera va mash'ala qo'shadilar (Slayd 11).
* **74:00 – 77:00 (3 min):** Interaktiv Quiz: 3 ta savol bo'yicha tezkor blitz (Slayd 12).
* **77:00 – 80:00 (3 min):** 3 darajali uy vazifasi tushuntiriladi va 11-haftaga ko'prik tashlanadi (Slayd 13-14).

---

## 3. O'qituvchi Uchun Jonli Savollar va Tuzoqlar

1. **Kamerani surishda manfiy ishora:**
   * Nega `ctx.translate(camera.x, camera.y)` emas, balki `ctx.translate(-camera.x, -camera.y)`?
   * *Yechim:* O'yinchi o'ngga yursa, dunyo chapga surilishi kerak! Kamera musbat bo'lsa, fon manfiyga qarab siljiydi.
2. **Kamera clamping tartibi:**
   * `Math.max(0, Math.min(targetX, maxCamX))` ifodasida `Math.max` va `Math.min` ning vazifasi:
   * `Math.min(targetX, maxCamX)` — o'ng/pastki chegaradan chiqib ketmaslik.
   * `Math.max(0, ...)` — chap/yuqori chegaradan (0 dan kichik bo'lib ketmaslik).
3. **destination-out da reset qilishni unutish:**
   * Agar mash'alani o'yib bo'lgach `ctx.globalCompositeOperation = 'source-over'` qilinmasa, keyingi barcha chiziladigan narsalar o'chib ketadi!

---

## 4. 10 Ballik Baholash Rubrikasi

* **1-Daraja: Baza (4 ball):** Kamera qahramon ortidan yurishi va xarita chegarasida to'xtashi (`Clamping`).
* **2-Daraja: Muhandislik (4 ball):** `createRadialGradient` bilan mash'ala nuri va qorong'ilik pardasi o'yilishi (`destination-out`).
* **3-Daraja: Kiber-Chaqliriq (2 ball):** Yurib o'tilgan yo'llarning xotirada saqlanishi (`explored[row][col]`).
"""
    with open(os.path.join(LESSON_DIR, "TEACHER_READING.md"), "w", encoding="utf-8") as f:
        f.write(teacher_md)
    print("  ✓ Created: TEACHER_READING.md")

    # ============================================================
    # 5. SIMULATOR (Standalone Interactive Roguelike Studio)
    # ============================================================
    sim_html = """<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Dungeon Camera & Fog Studio — 7-8 Класс" data-en="Dungeon Camera & Fog Studio — Grade 7-8">Dungeon Camera & Fog of War Studio — 7-8-sinf</title>
  <link rel="stylesheet" href="../../../../assets/brand.css">
  <style>
    body {
      margin: 0;
      padding: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: var(--font-sans, system-ui, sans-serif);
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }
    header {
      padding: 10px 20px;
      background: var(--surface);
      border-bottom: 1px solid var(--rule);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 700;
      font-size: 15px;
    }
    .brand span.tag {
      font-size: 11px;
      font-family: 'JetBrains Mono', monospace;
      padding: 2px 8px;
      background: var(--accent-soft);
      color: var(--accent-ink);
      border-radius: 4px;
    }
    main {
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 320px;
      gap: 16px;
      padding: 16px;
      box-sizing: border-box;
      min-height: 0;
    }
    .game-area {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: #060911;
      border-radius: 12px;
      border: 1px solid var(--rule);
      position: relative;
      overflow: hidden;
    }
    canvas {
      display: block;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      border-radius: 8px;
      border: 1px solid var(--rule);
      background: #0f1422;
    }
    .panel {
      background: var(--surface);
      border-radius: 12px;
      border: 1px solid var(--rule);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      overflow-y: auto;
    }
    .panel h2 {
      margin: 0;
      font-size: 15px;
    }
    .telemetry {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      background: var(--bg);
      border: 1px solid var(--rule);
      border-radius: 8px;
      padding: 10px;
      line-height: 1.8;
    }
    .telemetry span {
      font-weight: 700;
    }
    .btn {
      padding: 8px 14px;
      background: var(--surface-2);
      color: var(--ink);
      border: 1px solid var(--rule);
      border-radius: 6px;
      font-weight: 600;
      font-size: 12px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: background 0.15s;
    }
    .btn:hover {
      background: var(--accent);
      color: #fff;
      border-color: var(--accent);
    }
    .btn.active {
      background: var(--accent);
      color: #fff;
      border-color: var(--accent);
    }
    .slider-box {
      display: flex;
      flex-direction: column;
      gap: 4px;
      font-size: 12px;
    }
    .slider-box input {
      accent-color: var(--accent);
    }
    .dpad {
      display: grid;
      grid-template-columns: repeat(3, 44px);
      grid-gap: 6px;
      justify-content: center;
      margin-top: 6px;
    }
    .dpad button {
      width: 44px;
      height: 44px;
      font-size: 16px;
      border-radius: 8px;
      border: 1px solid var(--rule);
      background: var(--surface-2);
      color: var(--ink);
      cursor: pointer;
      font-weight: 700;
    }
    .dpad button:hover {
      background: var(--accent);
      color: #fff;
    }
  </style>
</head>
<body>

<header>
  <div class="brand">
    <span class="tag">TARGET GAME DEV</span>
    <span data-ru="Студия Камеры и Тумана Войны" data-en="Dungeon Camera & Fog Studio">Dungeon Kamera va Fog of War Studiyasi</span>
  </div>
  <div style="display:flex; align-items:center; gap:8px;">
    <button class="btn" onclick="setAppLang('uz')">UZ</button>
    <button class="btn" onclick="setAppLang('ru')">RU</button>
    <button class="btn" onclick="setAppLang('en')">EN</button>
  </div>
</header>

<main>
  <!-- Game Viewport -->
  <div class="game-area">
    <canvas id="gameCanvas" width="640" height="400"></canvas>
    <div style="position:absolute; bottom:12px; font-size:11px; color:var(--ink-2); background:rgba(0,0,0,0.6); padding:4px 10px; border-radius:999px;" data-ru="Управление: WASD или Стрелки на клавиатуре" data-en="Controls: WASD or Keyboard Arrows">Boshqaruv: WASD yoki Klaviaturadagi Strelkalar</div>
  </div>

  <!-- Sidebar Controls -->
  <div class="panel">
    <h2 data-ru="Параметры Движка" data-en="Engine Parameters">Dvigatel Sozlamalari</h2>

    <div class="telemetry">
      <div>Hero (World): <span id="telHero" style="color:var(--accent);">X: 200, Y: 200</span></div>
      <div>Camera: <span id="telCam" style="color:var(--green);">X: 0, Y: 0</span></div>
      <div>Viewport: <span>640 x 400 px</span></div>
      <div>World Map: <span>1600 x 1200 px</span></div>
      <div>Explored: <span id="telExplored" style="color:var(--accent-ink);">5%</span></div>
      <div>Diamonds: <span id="telGems" style="color:#f59e0b;">0 / 4</span></div>
    </div>

    <div style="display:flex; flex-direction:column; gap:8px;">
      <button class="btn active" id="btnCamLock" onclick="toggleCamLock()" data-ru="📷 Слежение камеры: ВКЛ" data-en="📷 Camera Follow: ON">📷 Kamera Kuzatuvi: YOQILGAN</button>
      <button class="btn active" id="btnFog" onclick="toggleFog()" data-ru="🌫️ Туман Войны: ВКЛ" data-en="🌫️ Fog of War: ON">🌫️ Urush Tumani: YOQILGAN</button>
      <button class="btn active" id="btnFlicker" onclick="toggleFlicker()" data-ru="🔥 Мерцание огня: ВКЛ" data-en="🔥 Fire Flicker: ON">🔥 Olov Miltillashi: YOQILGAN</button>
    </div>

    <div class="slider-box" style="margin-top:4px;">
      <label data-ru="Радиус Факела (px)" data-en="Torch Radius (px)">Mash'ala Radiusi: <span id="lblRadius">140px</span></label>
      <input type="range" id="rngRadius" min="60" max="240" value="140" oninput="updateRadius(this.value)">
    </div>

    <div class="slider-box">
      <label data-ru="Плавность Камеры (Lerp Speed)" data-en="Camera Lerp Speed">Kamera Lerp Tezligi: <span id="lblLerp">0.10</span></label>
      <input type="range" id="rngLerp" min="1" max="50" value="10" oninput="updateLerp(this.value)">
    </div>

    <h2 style="margin-top:6px;" data-ru="Экранный D-Pad" data-en="Screen D-Pad">Sensorli Boshqaruv</h2>
    <div class="dpad">
      <div></div>
      <button onclick="pressMove(0, -30)">⬆</button>
      <div></div>
      <button onclick="pressMove(-30, 0)">⬅</button>
      <button onclick="pressMove(0, 30)">⬇</button>
      <button onclick="pressMove(30, 0)">➡</button>
    </div>
  </div>
</main>

<script>
var appLang = "uz";
function setAppLang(l) {
  appLang = l;
  document.querySelectorAll("[data-" + l + "]").forEach(function(el) {
    el.textContent = el.getAttribute("data-" + l);
  });
}

// GAME STATE
var WORLD_W = 1600;
var WORLD_H = 1200;
var VIEW_W = 640;
var VIEW_H = 400;
var TILE_SIZE = 50;
var COLS = Math.floor(WORLD_W / TILE_SIZE);
var ROWS = Math.floor(WORLD_H / TILE_SIZE);

var player = {
  x: 200,
  y: 200,
  speed: 4,
  radius: 14
};

var camera = {
  x: 0,
  y: 0,
  lerpSpeed: 0.1,
  enabled: true
};

var fogEnabled = true;
var flickerEnabled = true;
var torchRadius = 140;
var gemsCollected = 0;

// Explored Matrix
var explored = [];
for (var r = 0; r < ROWS; r++) {
  explored[r] = [];
  for (var c = 0; c < COLS; c++) {
    explored[r][c] = false;
  }
}

// Dungeon Map (Walls = 1, Floor = 0)
var dungeonMap = [];
for (var r = 0; r < ROWS; r++) {
  dungeonMap[r] = [];
  for (var c = 0; c < COLS; c++) {
    if (r === 0 || r === ROWS - 1 || c === 0 || c === COLS - 1) {
      dungeonMap[r][c] = 1;
    } else {
      dungeonMap[r][c] = 0;
    }
  }
}

// Add internal rooms & walls
for (var r = 6; r <= 16; r++) dungeonMap[r][10] = 1;
for (var c = 10; c <= 22; c++) dungeonMap[10][c] = 1;
dungeonMap[10][15] = 0; // Doorway
for (var r = 12; r <= 20; r++) dungeonMap[r][22] = 1;
dungeonMap[16][22] = 0; // Doorway

var gems = [
  {x: 350, y: 150, collected: false},
  {x: 950, y: 350, collected: false},
  {x: 750, y: 900, collected: false},
  {x: 1350, y: 800, collected: false}
];

// Controls
var keys = {};
window.addEventListener("keydown", function(e) { keys[e.key.toLowerCase()] = true; });
window.addEventListener("keyup", function(e) { keys[e.key.toLowerCase()] = false; });

function pressMove(dx, dy) {
  tryMove(dx, dy);
}

function tryMove(dx, dy) {
  var nextX = player.x + dx;
  var nextY = player.y + dy;

  // Clamping to world
  nextX = Math.max(player.radius + 10, Math.min(WORLD_W - player.radius - 10, nextX));
  nextY = Math.max(player.radius + 10, Math.min(WORLD_H - player.radius - 10, nextY));

  // Wall check
  var col = Math.floor(nextX / TILE_SIZE);
  var row = Math.floor(nextY / TILE_SIZE);
  if (dungeonMap[row] && dungeonMap[row][col] === 1) return;

  player.x = nextX;
  player.y = nextY;

  // Gem check
  gems.forEach(function(g) {
    if (!g.collected) {
      var dist = Math.hypot(g.x - player.x, g.y - player.y);
      if (dist < 26) {
        g.collected = true;
        gemsCollected++;
        document.getElementById("telGems").textContent = gemsCollected + " / " + gems.length;
      }
    }
  });

  updateExploration();
}

function updateExploration() {
  var pCol = Math.floor(player.x / TILE_SIZE);
  var pRow = Math.floor(player.y / TILE_SIZE);
  var radiusTiles = Math.ceil(torchRadius / TILE_SIZE) + 1;

  for (var r = Math.max(0, pRow - radiusTiles); r <= Math.min(ROWS - 1, pRow + radiusTiles); r++) {
    for (var c = Math.max(0, pCol - radiusTiles); c <= Math.min(COLS - 1, pCol + radiusTiles); c++) {
      var cx = (c + 0.5) * TILE_SIZE;
      var cy = (r + 0.5) * TILE_SIZE;
      if (Math.hypot(cx - player.x, cy - player.y) <= torchRadius + 20) {
        explored[r][c] = true;
      }
    }
  }

  var count = 0;
  for (var r = 0; r < ROWS; r++) {
    for (var c = 0; c < COLS; c++) {
      if (explored[r][c]) count++;
    }
  }
  var pct = Math.round((count / (ROWS * COLS)) * 100);
  document.getElementById("telExplored").textContent = pct + "%";
}

function updateRadius(v) {
  torchRadius = parseInt(v);
  document.getElementById("lblRadius").textContent = v + "px";
  updateExploration();
}

function updateLerp(v) {
  camera.lerpSpeed = parseInt(v) / 100;
  document.getElementById("lblLerp").textContent = (parseInt(v) / 100).toFixed(2);
}

function toggleCamLock() {
  camera.enabled = !camera.enabled;
  var btn = document.getElementById("btnCamLock");
  btn.classList.toggle("active", camera.enabled);
  btn.textContent = camera.enabled ? "📷 Kamera Kuzatuvi: YOQILGAN" : "📷 Kamera Kuzatuvi: O'CHIRILGAN";
}

function toggleFog() {
  fogEnabled = !fogEnabled;
  var btn = document.getElementById("btnFog");
  btn.classList.toggle("active", fogEnabled);
  btn.textContent = fogEnabled ? "🌫️ Urush Tumani: YOQILGAN" : "🌫️ Urush Tumani: O'CHIRILGAN";
}

function toggleFlicker() {
  flickerEnabled = !flickerEnabled;
  var btn = document.getElementById("btnFlicker");
  btn.classList.toggle("active", flickerEnabled);
  btn.textContent = flickerEnabled ? "🔥 Olov Miltillashi: YOQILGAN" : "🔥 Olov Miltillashi: O'CHIRILGAN";
}

// MAIN LOOP
var canvas = document.getElementById("gameCanvas");
var ctx = canvas.getContext("2d");

function gameLoop() {
  // Input
  var dx = 0, dy = 0;
  if (keys["w"] || keys["arrowup"]) dy -= player.speed;
  if (keys["s"] || keys["arrowdown"]) dy += player.speed;
  if (keys["a"] || keys["arrowleft"]) dx -= player.speed;
  if (keys["d"] || keys["arrowright"]) dx += player.speed;
  if (dx !== 0 || dy !== 0) tryMove(dx, dy);

  // Camera
  if (camera.enabled) {
    var targetCamX = player.x - VIEW_W / 2;
    var targetCamY = player.y - VIEW_H / 2;
    var clampedTargetX = Math.max(0, Math.min(targetCamX, WORLD_W - VIEW_W));
    var clampedTargetY = Math.max(0, Math.min(targetCamY, WORLD_H - VIEW_H));

    camera.x += (clampedTargetX - camera.x) * camera.lerpSpeed;
    camera.y += (clampedTargetY - camera.y) * camera.lerpSpeed;
  } else {
    camera.x = 0;
    camera.y = 0;
  }

  // Telemetry
  document.getElementById("telHero").textContent = "X: " + Math.round(player.x) + ", Y: " + Math.round(player.y);
  document.getElementById("telCam").textContent = "X: " + Math.round(camera.x) + ", Y: " + Math.round(camera.y);

  // Render
  ctx.clearRect(0, 0, VIEW_W, VIEW_H);

  ctx.save();
  ctx.translate(-camera.x, -camera.y);

  // Render Explored / Dungeon
  for (var r = 0; r < ROWS; r++) {
    for (var c = 0; c < COLS; c++) {
      var wx = c * TILE_SIZE;
      var wy = r * TILE_SIZE;

      // Frustum culling check
      if (wx + TILE_SIZE < camera.x || wx > camera.x + VIEW_W ||
          wy + TILE_SIZE < camera.y || wy > camera.y + VIEW_H) {
        continue;
      }

      if (dungeonMap[r][c] === 1) {
        ctx.fillStyle = "#2d3748";
        ctx.fillRect(wx, wy, TILE_SIZE, TILE_SIZE);
        ctx.strokeStyle = "#4a5568";
        ctx.strokeRect(wx, wy, TILE_SIZE, TILE_SIZE);
      } else {
        ctx.fillStyle = "#151b2b";
        ctx.fillRect(wx, wy, TILE_SIZE, TILE_SIZE);
        ctx.strokeStyle = "rgba(255,255,255,0.04)";
        ctx.strokeRect(wx, wy, TILE_SIZE, TILE_SIZE);
      }
    }
  }

  // Render Gems
  gems.forEach(function(g) {
    if (!g.collected) {
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.arc(g.x, g.y, 10, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#fff";
      ctx.font = "12px sans-serif";
      ctx.fillText("💎", g.x - 7, g.y + 5);
    }
  });

  // Render Player
  ctx.fillStyle = "#3b82f6";
  ctx.beginPath();
  ctx.arc(player.x, player.y, player.radius, 0, Math.PI * 2);
  ctx.fill();
  ctx.strokeStyle = "#93c5fd";
  ctx.lineWidth = 2;
  ctx.stroke();

  // Face
  ctx.fillStyle = "#fff";
  ctx.beginPath(); ctx.arc(player.x - 4, player.y - 2, 3, 0, Math.PI*2); ctx.fill();
  ctx.beginPath(); ctx.arc(player.x + 4, player.y - 2, 3, 0, Math.PI*2); ctx.fill();

  ctx.restore();

  // Fog of War (Screen Space)
  if (fogEnabled) {
    var pScreenX = player.x - camera.x;
    var pScreenY = player.y - camera.y;

    var curRadius = torchRadius;
    if (flickerEnabled) {
      var flicker = Math.sin(Date.now() * 0.008) * 6 + (Math.random() * 3);
      curRadius += flicker;
    }

    ctx.save();
    // Solid pitch black
    ctx.fillStyle = "rgba(5, 8, 16, 0.96)";
    ctx.fillRect(0, 0, VIEW_W, VIEW_H);

    // Punch torch hole
    ctx.globalCompositeOperation = "destination-out";
    var grad = ctx.createRadialGradient(pScreenX, pScreenY, 20, pScreenX, pScreenY, curRadius);
    grad.addColorStop(0, "rgba(0,0,0,1)");
    grad.addColorStop(0.65, "rgba(0,0,0,0.85)");
    grad.addColorStop(1, "rgba(0,0,0,0)");

    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(pScreenX, pScreenY, curRadius, 0, Math.PI * 2);
    ctx.fill();

    ctx.restore();
  }

  requestAnimationFrame(gameLoop);
}

updateExploration();
requestAnimationFrame(gameLoop);
</script>
</body>
</html>
"""
    with open(os.path.join(SIM_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(sim_html)
    print("  ✓ Created: simulator/index.html")

    print("🎉 7–8-sinf generation finished!")

if __name__ == "__main__":
    build_7_8_lesson()
