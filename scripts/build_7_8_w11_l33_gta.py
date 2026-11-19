#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_7_8_w11_l33_gta.py — Builder for 7–8th Grade, Week 11, Lesson 33

Mavzu: GTA 2D: Cyber City — Kiber-Shahar Ochiq Dunyo O'yin Loyihasi
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 7-8-sinf (Game Dev & Canvas 2D Track)
Pedagogika: VIBECODING VA OCHIQ DUNYO O'YIN ARXITEKTURASI.
             Qorong'i yer osti zindonlari emas, balki o'quvchilar sevadigan
             zamonaviy GTA 2D shahar simulyatori:
             1) WASD piyoda va 360° sichqoncha nishoni
             2) 'F' tugmasi bilan mashinaga o'tirish va drift fizikasi
             3) Lazer blaster, orqaga tepish (recoil) va uchqunlar
             4) Qidiruv yulduzlari (⭐⭐⭐) va politsiya ta'qibi
             5) Kiber-kuryer yetkazib berish missiyasi va kesh ($$$)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "7-8-sinf", "11-hafta", "33-dars-gta-cyber-city-2d")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "simulator"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides — High-Energy GTA 2D Game Architecture)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="7–8-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 33" data-en="GRADES 7–8 · WEEK 11 · LESSON 33">7–8-SINF · 11-HAFTA · 33-DARS</span></div>
    <h1 class="display" data-ru="GTA 2D: Cyber City — Создание Игры с Открытым Миром" data-en="GTA 2D: Cyber City — Open World 2D Game Architecture">GTA 2D: Cyber City — Kiber-Shahar Ochiq Dunyo O'yini</h1>
    <p class="lede" data-ru="Никаких скучных подземелий! Сегодня мы создаем топовую 2D GTA с открытым неоновым городом: угон спорткаров на клавишу 'F', физика заноса и дрифта, лазерные перестрелки, полицейские сирены и курьерские миссии через Vibecoding!" data-en="No boring dungeons! Today we engineer a top-tier 2D GTA in an open cyber city: car hijacking with 'F', drift physics, 360° laser blasters, police sirens, and delivery missions via Vibecoding!">Zerikarli yer osti zindonlari emas! Bugun biz Vibecoding yordamida haqiqiy 2D GTA o'yinini quramiz: 'F' tugmasi bilan sportkarga o'tirish, drift va shina izlari fizikasi, 360° lazer blaster, politsiya ta'qibi va kiber-kuryer missiyalari!</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="5 Столпов GTA 2D" data-en="5 Pillars of GTA 2D">GTA 2D ning 5 Asosiy Ustuni</h3>
        <p data-ru="Пешеход, угон авто, баллистика выстрела, полицейский ИИ с сиренами и доставка посылок за кэш." data-en="Pedestrian mode, vehicle hijacking, bullet ballistics, police AI sirens, and cash delivery missions.">Piyoda rejimi, mashina haydash, o'qlar ballistikasi, sirenali politsiya AI va kuryerlik missiyasi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">GTA 2D Cyber City</div>
        <h3 data-ru="Полноценная 2D Игра" data-en="Full Playable 2D Game">To'liq Ishlaydigan O'yin</h3>
        <p data-ru="Каждый запустит собственный открытый город прямо в браузере и протестирует погоню с друзьями!" data-en="Everyone launches their own open city in the browser and tests police chases with peers!">Har bir o'quvchi o'zining ochiq kiber-shaharini brauzerda ishga tushirib, politsiya poygasini sinaydi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW & BRIDGE -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="РАЗБОР ДОМАШНЕГО ЗАДАНИЯ И МОСТ" data-en="HOMEWORK REVIEW & BRIDGE">UY VAZIFASI TAHLILI VA KO'PRIK</span></div>
    <h2 data-ru="Разбор ДЗ 32-урока: Ошибки Баллистики и Мост к GTA 2D" data-en="Lesson 32 HW Review: Ballistics Pitfalls & Bridge to GTA">32-Dars Uy Vazifasi: Otishma Xatolari va GTA 2D Ko'prigi</h2>
    <div class="grid-2">
      <div class="card" style="border-left:4px solid var(--danger);">
        <div class="tag" style="background:var(--danger); color:#fff;" data-ru="Частая ошибка" data-en="Common Pitfall">Keng Tarqalgan Xato</div>
        <h3 data-ru="Утечка Памяти в Массиве Пуль" data-en="Memory Leak in Projectile Array">O'qlar Massivida Xotira Oqishi (Memory Leak)</h3>
        <p data-ru="Ученики создавали массив <code>bullets.push()</code> при каждом клике, но забывали удалять улетевшие за экран пули. Через 1 минуту стрельбы игра начинала лагать из-за 10,000+ объектов в памяти!" data-en="Students pushed bullets on every click but forgot to slice/filter off-screen projectiles. After 1 minute of shooting, the game lagged processing 10,000+ dead objects!">O'quvchilar har bir klikda <code>bullets.push()</code> qilishgan, lekin ekrandan chiqib ketgan o'qlarni massivdan o'chirishmagan. Natijada xotirada 10,000+ ob'ekt to'planib, o'yin qotishni boshlagan!</p>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <div class="tag" style="background:var(--accent); color:#fff;" data-ru="Золотой Стандарт" data-en="Golden Standard">Oltin Yechim (Filter & Splice)</div>
        <h3 data-ru="Чистая Очистка Кадра" data-en="Clean Frame Garbage Cleanup">Toza Filtrlash Algoritmi</h3>
        <pre><code>// O'qlarni yangilash va o'chirish:
bullets.forEach(b =&gt; { b.x += b.vx; b.y += b.vy; b.life--; });
bullets = bullets.filter(b =&gt; b.life &gt; 0 &amp;&amp; !b.hit);</code></pre>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Каждая пуля имеет таймер жизни или удаляется при ударе в здание." data-en="Each projectile has a life timer and purges immediately upon hitting buildings.">Har bir o'q masofa tugashi yoki binoga urilishi bilan bir zumda xotiradan tozalanadi.</p>
      </div>
    </div>
    <div class="card mt" style="background:var(--surface-2); padding:10px 16px;">
      <div class="badge" style="background:var(--accent); color:#fff; font-size:11px;" data-ru="Блиц-Вопрос (30 сек)" data-en="Blitz Question (30s)">30 Soniyalik Blitz</div>
      <p style="margin:4px 0; font-size:13px;" data-ru="Почему в GTA угол машины нельзя менять мгновенно, как у пешехода?" data-en="Why can't car steering snap instantly like pedestrian rotation in GTA?">Nega GTA o'yinida mashinaning burilish burchagini piyodadek bir zumda burib bo'lmaydi? Chunki mashina inersiya va shinalarning asfaltga ishqalanishi (friction & turning radius) bilan buriladi!</p>
    </div>
  </section>

  <!-- SLIDE 3: OPEN WORLD CITY ANATOMY -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="12:00–20:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="АРХИТЕКТУРА GTA 2D" data-en="GTA 2D ARCHITECTURE">OCHIQ DUNYO ARXITEKTURASI</span></div>
    <h2 data-ru="Анатомия GTA 2D: 5 Независимых Систем Кибер-Города" data-en="GTA 2D Anatomy: 5 Independent City Systems">Kiber-Shahar Anatomiyasi: 5 Ta Mustaqil Tizim</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" data-ru="1. Слой Карты" data-en="1. City Map">1. Shahar Xaritasi</div>
        <h3 data-ru="Асфальт и Здания" data-en="Roads & Buildings">Asfalt va Binolar</h3>
        <p data-ru="Черный асфальт, двойная разделительная полоса, пешеходные переходы и неоновые небоскребы с коллизией." data-en="Dark asphalt, road markings, crosswalks, and neon skyscrapers with solid bounding box collisions.">Qora asfalt, oq-sariq chiziqlar, piyodalar yo'lagi va qattiq chegarali (AABB) neon binolar.</p>
      </div>
      <div class="card">
        <div class="tag" data-ru="2. Транспорт" data-en="2. Vehicle Switch">2. Avtomobil Tizimi</div>
        <h3 data-ru="Сел / Вышел на 'F'" data-en="Enter / Exit 'F'">'F' Bilan O'tirish</h3>
        <p data-ru="Когда игрок рядом с машиной, нажимает клавишу 'F'. Спрайт прячется внутрь, физика переключается на авто!" data-en="Standing near a car, player presses 'F'. Pedestrian hides, controls switch to vehicle dynamics!">Mashinaga yaqinlashib 'F' bosilganda, o'yinchi mashina ichiga o'tiradi va boshqaruv avtomobil fizikasiga o'tadi.</p>
      </div>
      <div class="card">
        <div class="tag" data-ru="3. Полиция" data-en="3. Police AI">3. Qidiruv Yulduzlari</div>
        <h3 data-ru="Звезды Розыска ⭐" data-en="Wanted Stars ⭐">Wanted Stars ⭐</h3>
        <p data-ru="Каждый выстрел или таран повышает розыск. На 2+ звездах выезжают копы с мигалками и звуком сирен!" data-en="Firing or crashing increases wanted stars. At 2+ stars, police cruisers spawn with sirens and chase!">O't ochish yoki avto-falokat yulduzni oshiradi. 2+ yulduzda miltillovchi politsiya quva boshlaydi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: PLAYER ON FOOT & 360 AIM -->
  <section class="slide" data-phase="Piyoda Mantig'i|Логика Пешехода|Pedestrian Mode" data-time="20:00–28:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="ШАГ 1: ПЕШЕХОД И ПРИЦЕЛ" data-en="STEP 1: PEDESTRIAN & AIM">1-BOSQICH: PIYODA HARAKATI</span></div>
    <h2 data-ru="Управление Персонажем: Вектор Скорости и Вращение за Мышью" data-en="Player On Foot: WASD Movement & Mouse Angle">Piyoda Rejimi: WASD Harakati va Sichqoncha Nishoni</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Вращение через Тригонометрию" data-en="Trigonometric Rotation">360° Sichqonchaga Qarash</h3>
        <pre><code>// Qahramon doimo kursorga qaraydi:
const dx = mouse.x - player.x;
const dy = mouse.y - player.y;
player.angle = Math.atan2(dy, dx);

// Canvasda burib chizish:
ctx.save();
ctx.translate(player.x, player.y);
ctx.rotate(player.angle);
drawMercenary(ctx);
ctx.restore();</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Плавное Движение на WASD" data-en="Smooth WASD Vector">Vektorli Harakat va Devorlar</h3>
        <p data-ru="Пешеход перемещается со скоростью 3.5 px/кадр. Перед каждым шагом проверяем AABB-коллизию с углами зданий: если следующий шаг врезается в стену — скорость обнуляется!" data-en="Player moves at 3.5 px/frame. Before moving, check AABB collisions with building bounds: if colliding, movement halts!">Qahramon har kadrda 3.5 piksel tezlikda yuradi. Har bir harakatdan oldin shahar binolari chegarasi tekshiriladi: devorga urilsa, harakat darhol to'xtatiladi!</p>
        <div class="box mt" style="background:var(--surface-2); padding:8px 12px; font-size:12px;">
          <strong>🎯 Muhim Eslatma:</strong> Diagonal yurishda tezlik oshib ketmasligi uchun vektor normallashtiriladi: <code>speed / 1.414</code>.
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: CAR PHYSICS & DRIFT -->
  <section class="slide" data-phase="Avto Fizikasi|Физика Авто|Car Physics" data-time="28:00–36:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="ШАГ 2: ФИЗИКА ДРИФТА" data-en="STEP 2: CAR DRIFT PHYSICS">2-BOSQICH: SPORTKAR FIZIKASI</span></div>
    <h2 data-ru="Физика Дрифта: Газ, Тормоз, Инерция и Следы Шин" data-en="Car Dynamics: Accel, Steering, Drift & Skidmarks">Avtomobil Fizikasi: Tezlanish, Rul va Asfaltda Drift</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Уравнение Движения Авто" data-en="Vehicle Equation of Motion">Avtomobil Harakat Tenglamasi</h3>
        <pre><code>// W - gaz, S - tormoz / orqaga:
if (keys['KeyW']) car.speed += car.accel;
if (keys['KeyS']) car.speed -= car.brake;

// Rul faqat mashina yurganda buriladi:
if (Math.abs(car.speed) &gt; 0.2) {
  if (keys['KeyA']) car.angle -= car.turnSpeed;
  if (keys['KeyD']) car.angle += car.turnSpeed;
}

// Ishqalanish (Inersiya):
car.speed *= 0.985;
car.x += Math.cos(car.angle) * car.speed;
car.y += Math.sin(car.angle) * car.speed;</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Следы Заноса на Асфальте" data-en="Tire Skidmarks Generator">Asfaltdagi Qora Shina Izlari</h3>
        <p data-ru="Когда игрок резко поворачивает на высокой скорости (speed &gt; 4), колеса срываются в занос. Мы рисуем полупрозрачные черные полосы под задними колесами:" data-en="When steering sharply at high speed (speed &gt; 4), tires lose traction. We render semi-transparent black tyre marks under wheels:">Mashina yuqori tezlikda (speed &gt; 4) keskin burilganda, g'ildiraklar sirpanadi. Orqa g'ildiraklar ostida asfaltdagi qora drift izlarini hosil qilamiz:</p>
        <pre><code>if (Math.abs(car.speed) &gt; 4 &amp;&amp; turning) {
  skidmarks.push({ x: car.x, y: car.y, a: car.angle, alpha: 0.6 });
}</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: ENTER / EXIT CAR LOGIC -->
  <section class="slide" data-phase="Avto Almashish|Посадка в Авто|Hijack Logic" data-time="36:00–44:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ШАГ 3: УГОН НА КЛАВИШУ 'F'" data-en="STEP 3: HIJACK KEY 'F'">3-BOSQICH: 'F' TUGMASI BILAN O'TIRISH</span></div>
    <h2 data-ru="Логика Переключения Состояний: Пешеход ↔ Водитель" data-en="State Machine: Pedestrian ↔ Driver via 'F' Key">Holat Mashinasi: Piyoda ↔ Haydovchi Rejimi</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Детекция Дистанции До Авто" data-en="Proximity Distance Check">Mashinaga Yaqinlikni Tekshirish</h3>
        <pre><code>window.addEventListener('keydown', (e) =&gt; {
  if (e.code === 'KeyF') {
    if (!player.inCar) {
      // Mashinagacha masofa:
      const dist = Math.hypot(player.x - car.x, player.y - car.y);
      if (dist &lt; 50) {
        player.inCar = true;
        playSFX('doorClose');
      }
    } else {
      // Mashinadan tushish:
      player.inCar = false;
      player.x = car.x + Math.sin(car.angle) * 30;
      player.y = car.y - Math.cos(car.angle) * 30;
      playSFX('doorOpen');
    }
  }
});</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Что Происходит При Посадке?" data-en="What Happens When Hijacking?">Mashinaga O'tirganda Nima Bo'ladi?</h3>
        <ul style="font-size:13px; line-height:1.7;">
          <li data-ru="<strong>Спрайт игрока скрывается:</strong> рисуется только машина." data-en="<strong>Player sprite hidden:</strong> only car rendered."><strong>Piyoda spriti yashiriladi:</strong> faqat sportkar chiziladi.</li>
          <li data-ru="<strong>Камера привязывается к авто:</strong> плавный следящий зум." data-en="<strong>Camera locks onto car:</strong> smooth tracking."><strong>Kamera mashinani markazga oladi:</strong> silliq kuzatuv.</li>
          <li data-ru="<strong>Включаются фары:</strong> два конуса яркого света на дорогу." data-en="<strong>Headlights turn on:</strong> twin yellow light cones."><strong>Farlar yoqiladi:</strong> yo'lni yorituvchi ikkita sariq nur.</li>
          <li data-ru="<strong>Скорость увеличивается в 2.5 раза:</strong> от 3 px до 8 px!" data-en="<strong>Speed doubles:</strong> from 3px up to 8px!"><strong>Tezlik 2.5 barobar oshadi:</strong> 3 px dan 8 px gacha!</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: WEAPONS & RECOIL -->
  <section class="slide" data-phase="Qurol va Otishma|Оружие и Стрельба|Shooting" data-time="44:00–50:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ШАГ 4: ЛАЗЕРНЫЙ БЛАСТЕР" data-en="STEP 4: LASER BLASTER">4-BOSQICH: 360° QUROLLAR VA O'Q UCHISHI</span></div>
    <h2 data-ru="Баллистика Выстрела: Вспышка, Звук и Отдача" data-en="Weapon Ballistics: Muzzle Flash, SFX & Recoil">Blaster Ballistikasi: O't Oflashi, Orqaga Tepish va Ovoz</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" data-ru="Вспышка" data-en="Muzzle Flash">1. Muzzle Flash</div>
        <h3 data-ru="Яркая Вспышка Ствола" data-en="Barrel Flash">Stvol Uchi Olovi</h3>
        <p data-ru="При выстреле на 2 кадра рисуется яркий неоновый круг света у дула бластера." data-en="Bright glowing neon spark drawn at weapon muzzle for 2 frames.">O'q uzilgan paytda qurol stvoli uchida 2 kadr davomida yorqin neon chaqnash chiziladi.</p>
      </div>
      <div class="card">
        <div class="tag" data-ru="Отдача" data-en="Recoil">2. Orqaga Tepish (Recoil)</div>
        <h3 data-ru="Физическая Отдача" data-en="Physical Pushback">Qahramonni Surish</h3>
        <p data-ru="Выстрел толкает персонажа назад по вектору: <code>player.x -= cos(angle)*2</code>." data-en="Recoil pushes player backward along shooting vector.">Har bir o'q uzilganda qahramon qarama-qarshi tomonga biroz orqaga suriladi.</p>
      </div>
      <div class="card">
        <div class="tag" data-ru="Искры" data-en="Sparks">3. Uchqunlar (Sparks)</div>
        <h3 data-ru="Удар в Препятствие" data-en="Impact Particles">Devorga Urilish</h3>
        <p data-ru="При попадании в здание пуля взрывается 6 яркими разлетающимися искрами!" data-en="Bullet spawns 6 vibrant ricochet sparks upon hitting buildings!">O'q bino devoriga urilganda 6 ta har tomonga sochilib so'nuvchi uchqun hosil qiladi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: IN-DECK INTERACTIVE GAMEPLAY -->
  <section class="slide" data-phase="Jonli O'yin|Интерактив|Live Game" data-time="50:00–60:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ЖИВОЙ ТЕСТ-ДРАЙВ В СЛАЙДЕ" data-en="LIVE IN-DECK SIMULATOR">JONLI TEST-DRAYV</span></div>
    <h2 data-ru="GTA 2D Cyber City: Управляй, Дрифтуй, Стреляй и Уходи от Копов!" data-en="GTA 2D Cyber City: Drive, Drift, Shoot & Evade Police!">GTA 2D: Hayda, Drift Qil, O't Och va Politsiyadan Qoch!</h2>
    <div style="display:flex; justify-content:center; align-items:center; gap:16px;">
      <div style="position:relative; width:640px; height:360px; background:#0f1319; border-radius:12px; overflow:hidden; border:2px solid var(--accent); box-shadow:0 12px 36px rgba(0,0,0,0.4);">
        <canvas id="gtaDeckCanvas" width="640" height="360" style="display:block;"></canvas>
        <div id="deckPromptF" style="position:absolute; bottom:12px; left:12px; background:rgba(0,0,0,0.8); color:#00f2fe; padding:4px 10px; border-radius:6px; font-size:11px; font-weight:700; display:none;">[F] Mashinaga o'tirish / Enter Vehicle</div>
        <div style="position:absolute; top:10px; left:12px; font-size:12px; font-weight:800; color:#ffdd00; text-shadow:0 0 8px rgba(255,221,0,0.6);" id="deckStatsHUD">⭐ WANTED: 0 · 💵 CASH: $0</div>
      </div>
      <div style="width:260px; font-size:11px; display:flex; flex-direction:column; gap:8px;">
        <div class="card" style="padding:10px;">
          <h4 style="margin:0 0 6px; font-size:12px; color:var(--accent);" data-ru="🎮 Управление" data-en="🎮 Controls">🎮 Boshqaruv</h4>
          <div>• <strong>WASD / Strelkalar:</strong> Piyoda & Mashina</div>
          <div>• <strong>F:</strong> Mashinaga o'tirish / tushish</div>
          <div>• <strong>Sichqoncha:</strong> 360° nishon olish</div>
          <div>• <strong>Chap Klik:</strong> Lazer otish</div>
          <div>• <strong>Sariq Neon:</strong> Paket yetkazish ($500)</div>
        </div>
        <button id="gtaDeckResetBtn" style="padding:8px 12px; background:var(--accent); color:#fff; border:none; border-radius:6px; font-weight:700; cursor:pointer;" data-ru="Перезапустить Симулятор" data-en="Reset Simulator">🔄 O'yinni Qayta Boshlash</button>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: WANTED STARS & POLICE AI -->
  <section class="slide" data-phase="Politsiya AI|ИИ Полиции|Police AI" data-time="60:00–66:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ШАГ 5: ПОЛИЦИЯ И ЗВЕЗДЫ" data-en="STEP 5: POLICE & WANTED">5-BOSQICH: QIDIRUV VA POLITSIYA AI</span></div>
    <h2 data-ru="Система Розыска: Звезды, Мигалки и Алгоритм Преследования" data-en="Wanted Level Engine: Stars, Flashing Sirens & Pursuit AI">Qidiruv Tizimi: Yulduzlar, Sirenalar va Ta'qib AI</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Как Работает ИИ Копов?" data-en="How Police Pursuit AI Works">Politsiya Mashinasi Qanday Quvadi?</h3>
        <pre><code>// Politsiya o'yinchiga qarab buriladi va gaz bosadi:
const dx = player.x - cop.x;
const dy = player.y - cop.y;
const targetAngle = Math.atan2(dy, dx);

// Sekinlik bilan burilish (inertial steering):
cop.angle += (targetAngle - cop.angle) * 0.05;
cop.x += Math.cos(cop.angle) * cop.speed;
cop.y += Math.sin(cop.angle) * cop.speed;

// Miltillovchi sirena chiroqlari:
cop.sirenTimer++;
cop.light = (cop.sirenTimer % 20 &lt; 10) ? '#ff0033' : '#0066ff';</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Шкала Преступлений" data-en="Crime Escalation Meter">Qidiruv Yulduzlari Bosqichlari</h3>
        <ul style="font-size:13px; line-height:1.7;">
          <li data-ru="<strong>⭐ 1 Звезда:</strong> Звук выстрела — патруль предупрежден." data-en="<strong>⭐ 1 Star:</strong> Gunshot detected — police on alert."><strong>⭐ 1 Yulduz:</strong> O'q ovozi eshitildi — patrul xabardor qilindi.</li>
          <li data-ru="<strong>⭐⭐ 2 Звезды:</strong> 1 патрульная машина преследует с сиреной." data-en="<strong>⭐⭐ 2 Stars:</strong> 1 cruiser in active high-speed pursuit."><strong>⭐⭐ 2 Yulduz:</strong> 1 ta politsiya mashinasi sirenani yoqib quvadi.</li>
          <li data-ru="<strong>⭐⭐⭐ 3 Звезды:</strong> 2 полицейские машины и заграждения!" data-en="<strong>⭐⭐⭐ 3 Stars:</strong> Multiple pursuit cars and barricades!"><strong>⭐⭐⭐ 3 Yulduz:</strong> 2 ta politsiya mashinasi o'rab oladi!</li>
          <li data-ru="<strong>Как Сбросить Розыск?</strong> Заезд в неоновый гараж сбрасывает все звезды." data-en="<strong>How to Lose Stars?</strong> Entering Neon Garage resets heat."><strong>Qanday Qutilish Mumkin?</strong> Neon garajga kirish yulduzlarni o'chiradi.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: WEB AUDIO SYNTHESIS -->
  <section class="slide" data-phase="Audio Sintezi|Аудио Синтез|Web Audio" data-time="66:00–70:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ШАГ 6: ЗВУКОВОЙ ДВИЖОК" data-en="STEP 6: AUDIO ENGINE">6-BOSQICH: WEB AUDIO SINTEZI</span></div>
    <h2 data-ru="Синтез Звука Без Файлов: Рёв Мотора, Свист Шин и Сирена" data-en="Zero-Asset Audio Synthesis: Engine Rev, Tire Screech & Siren">Faylsiz Ovoz Sintezi: Dvigatel, Shina va Politsiya Sirenasi</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" data-ru="Двигатель" data-en="Engine">1. Dvigatel Guvillashi</div>
        <h3 data-ru="Низкая Пилообразная Волна" data-en="Sawtooth Oscillator">Sawtooth Osilator</h3>
        <p data-ru="Звук мотора меняет частоту от скорости: <code>osc.frequency.value = 60 + speed * 25</code>." data-en="Engine frequency shifts dynamically with car speed: 60Hz to 260Hz.">Mashina tezlashgan sari dvigatel ovozi 60Hz dan 260Hz gacha ko'tariladi.</p>
      </div>
      <div class="card">
        <div class="tag" data-ru="Свист Шин" data-en="Tire Screech">2. Shina G'iyqillashi</div>
        <h3 data-ru="Белый Шум и Фильтр" data-en="White Noise & Filter">Noise Generator</h3>
        <p data-ru="При заносе на высокой частоте генерируется высокочастотный скрежет резины об асфальт." data-en="Tire drift triggers high-pitch bandpass noise resembling rubber friction.">Drift paytida asfaltdagi rezina ishqalanishining yuqori chastotali ovozi.</p>
      </div>
      <div class="card">
        <div class="tag" data-ru="Сирена" data-en="Police Siren">3. Politsiya Sirenasi</div>
        <h3 data-ru="LFO Модуляция Частоты" data-en="LFO Warble Siren">Modulyatsiyali Siren</h3>
        <p data-ru="Плавное колебание частоты между 600Hz и 900Hz каждые 0.5 секунды." data-en="Frequency smoothly warbles between 600Hz and 900Hz every 0.5s.">Chastota har yarim soniyada 600Hz va 900Hz oralig'ida to'lqinlanadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: VIBECODING PROMPT BLUEPRINT -->
  <section class="slide" data-phase="Vibecoding Metodi|Метод Vibecoding|Prompt Engineering" data-time="70:00–74:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="МЕТОДИКА VIBECODING" data-en="VIBECODING METHOD">AI PROMPT ARXITEKTURASI</span></div>
    <h2 data-ru="Как Собрать GTA 2D за 4 Промпта в AI: Пошаговая Инструкция" data-en="How to Build GTA 2D via 4 Prompts: Step-by-Step Blueprint">AI Yordamida GTA 2D ni 4 Qadamda Yaratish Yo'riqnomasi</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:var(--accent); color:#fff;" data-ru="1-й и 2-й Промпты" data-en="Prompts 1 & 2">1-va 2-Promptlar</div>
        <h4 style="margin:4px 0 6px; font-size:12px;" data-ru="Карта + Пешеход + Физика Авто" data-en="Map + Pedestrian + Car Physics">Xarita + Piyoda + Mashina Fizikasi</h4>
        <pre><code>"HTML5 Canvas 2D da Top-Down shahar xaritasini
yarat. WASD bilan yuguruvchi piyoda va sichqoncha
yo'nalishiga buriluvchi ko'rish burchagi bo'lsin.
Ko'chada sportkar tursin. O'yinchi yaqinlashib
'F' tugmasini bossa, mashinaga o'tirsin. Mashina
inersiya, tezlanish va drift izlari bilan yursin!"</code></pre>
      </div>
      <div class="card">
        <div class="tag" style="background:var(--accent); color:#fff;" data-ru="3-й и 4-й Промпты" data-en="Prompts 3 & 4">3-va 4-Promptlar</div>
        <h4 style="margin:4px 0 6px; font-size:12px;" data-ru="Стрельба + Полиция + Миссии" data-en="Shooting + Police + Missions">Otishma + Politsiya + Missiyalar</h4>
        <pre><code>"Sichqoncha chap tugmasi bilan 360° blasterdan
o't ochish va o'qlarni bino to'siqlariga urilishini
qo'sh. O'q uzilganda 'Wanted Stars' (⭐) oshsin va
miltillovchi qizil-ko'k sirenaga ega politsiya
mashinasi o'yinchini quvsin! Xaritada kiber-paket
yetkazish nuqtasi ($500) bo'lsin!"</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: PEER PLAYTESTING & DUEL -->
  <section class="slide" data-phase="Playtesting|Тестирование|Playtesting" data-time="74:00–77:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ПАРНОЕ ТЕСТИРОВАНИЕ И БАТТЛ" data-en="PEER PLAYTESTING">JUFTLIKDA PLAYTESTING</span></div>
    <h2 data-ru="Критерии Playtesting: Проверь Игру Соседа по Парте!" data-en="Playtesting Checklist: Audit Your Peer's City!">Playtesting Sinovi: Partadoshing O'yinini Tekshir!</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" data-ru="Тест 1" data-en="Test 1">1. Rul va Drift Silliqligi</div>
        <h3 data-ru="Ощущение Скорости" data-en="Speed Feeling">Boshqaruv Sezgisi</h3>
        <p data-ru="Машина управляется плавно? Оставляет ли четкие черные следы при резком входе в поворот?" data-en="Does the car handle smoothly? Are skidmarks rendered during sharp turns?">Mashina silliq yuradimi? Keskin burilganda asfaltdagi drift izlari ko'rinyaptimi?</p>
      </div>
      <div class="card">
        <div class="tag" data-ru="Тест 2" data-en="Test 2">2. 'F' Tugmasi Barqarorligi</div>
        <h3 data-ru="Без Застреваний" data-en="Zero Glitches">Qotib Qolmaslik</h3>
        <p data-ru="При выходе из машины игрок появляется рядом с дверью, а не застревает внутри текстур здания?" data-en="Does player exit beside the door without clipping into walls?">Mashinadan tushganda o'yinchi bino ichiga tushib qotib qolmayaptimi?</p>
      </div>
      <div class="card">
        <div class="tag" data-ru="Тест 3" data-en="Test 3">3. Politsiya Ta'qibi</div>
        <h3 data-ru="Баланс Сложности" data-en="Difficulty Balance">Adolatli Qochish</h3>
        <p data-ru="Полиция действительно догоняет и мигает сиренами? Реально ли оторваться на полной скорости?" data-en="Do cops pursue with flashing sirens? Can you evade them at top speed?">Politsiya chindan quvyaptimi va yuqori tezlikda burilib ulardan qochsa bo'ladimi?</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: GOLDEN RULES & CONCLUSION -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="77:00–79:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И ЗОЛОТЫЕ ПРАВИЛА" data-en="GOLDEN RULES & SUMMARY">XULOSA VA OLTIN QOIDALAR</span></div>
    <h2 data-ru="4 Закона Архитектуры Открытого Мира 2D" data-en="4 Laws of 2D Open World Architecture">Ochiq Dunyo 2D O'yinining 4 Oltin Qoidasi</h2>
    <div class="grid-2">
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3 data-ru="1. Разделение Состояний (State Machine)" data-en="1. State Decoupling">1. Holatlar Ajratilishi (State Machine)</h3>
        <p data-ru="Пешеход и авто — это два разных режима управления. Никогда не смешивайте их код в одной куче: флаг <code>player.inCar</code> четко переключает ветку физики." data-en="Pedestrian and vehicle are separate states. Decouple them cleanly via player.inCar flag.">Piyoda va mashina — ikki xil rejim. Ularni bitta aralash kodda emas, <code>player.inCar</code> holat bayrog'i orqali toza ajrating.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3 data-ru="2. Очистка Мертвых Объектов" data-en="2. Garbage Cleanup">2. Xotirani Tozalash (Garbage Collection)</h3>
        <p data-ru="Следы шин, искры пуль и дым должны исчезать со временем (alpha -= 0.01), иначе игра зависнет через 2 минуты активного заезда!" data-en="Tire marks, sparks, and smoke must fade out and purge, preventing memory leaks.">Shina izlari, o'q uchqunlari vaqt o'tishi bilan o'chirilishi shart, aks holda brauzer xotirasi to'ladi.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3 data-ru="3. Инерция — Залог Кайфа от Вождения" data-en="3. Inertia Delivers Driving Feel">3. Inersiya — Haqiqiy Haydash Zavqi</h3>
        <p data-ru="Мгновенная остановка машины убивает ощущение веса. Трение 0.985 и радиус разворота дают реалистичный вес и дрифт." data-en="Instant stops feel fake. Friction 0.985 and turning radius provide realistic weight.">Mashinaning bir zumda to'xtashi sun'iy ko'rinadi. 0.985 ishqalanish koeffitsienti haqiqiy vazn hissini beradi.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3 data-ru="4. Динамическая Полиция" data-en="4. Dynamic Pursuit Response">4. Jonli Politsiya Reaksiyasi</h3>
        <p data-ru="Город оживает только тогда, когда мир реагирует на действия игрока: преступление = полиция, доставка = награда." data-en="The city breathes when the world reacts: crime sparks police, delivery earns rewards.">Shahar faqat harakatga javob berilsagina tiriladi: noqonuniy o't ochish = politsiya ta'qibi, yetkazib berish = mukofot.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: 3-TIER HOMEWORK & RUBRIC -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Homework" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ДОМАШНЕЕ ЗАДАНИЕ · 10 БАЛЛОВ" data-en="HOMEWORK · 10 POINTS">3 DARAJALI UY VAZIFASI</span></div>
    <h2 data-ru="Проект GTA 2D: Добавь Свою Уникальную Механику!" data-en="GTA 2D Project: Implement Your Custom Feature!">GTA 2D Loyihasi: O'z Unikal Mexanikangni Qo'sh!</h2>
    <div class="grid-3">
      <div class="card" style="border-top:4px solid var(--accent);">
        <div class="tag" data-ru="Уровень 1: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</div>
        <h3 data-ru="Чистый Город и Авто" data-en="City & Car">Shahar va Sportkar</h3>
        <p data-ru="Запустить город, настроить ходьбу на WASD, посадку в авто на 'F' и корректную физику заноса без застревания в стенах." data-en="Launch open city, configure WASD walking, 'F' hijacking, and drift physics without wall clipping.">Shaharni ishga tushirish, WASD harakati, 'F' bilan mashinaga o'tirish va devorga qotib qolmaslik.</p>
      </div>
      <div class="card" style="border-top:4px solid var(--accent);">
        <div class="tag" data-ru="Уровень 2: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</div>
        <h3 data-ru="Погоня и Курьер" data-en="Chase & Courier">Politsiya va Kuryerlik</h3>
        <p data-ru="Добавить систему розыска: стрельба привлекает копов с сиренами, а доставка неоновых пакетов приносит +$500 кэша." data-en="Add wanted system: firing attracts sirens, neon package deliveries grant +$500 cash.">Qidiruv yulduzlari: o't ochish politsiyani chaqiradi, kiber-paket yetkazish +$500 keltiradi.</p>
      </div>
      <div class="card" style="border-top:4px solid var(--danger);">
        <div class="tag" style="background:var(--danger); color:#fff;" data-ru="Уровень 3: Кибер-Вызов (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Challenge (2 ball)</div>
        <h3 data-ru="Покраска Pay'n'Spray" data-en="Pay'n'Spray Garage">Neon Garaj (Pay'n'Spray)</h3>
        <p data-ru="Создать неоновый гараж, куда можно заехать на машине: звезды розыска сбрасываются до 0, а кузов перекрашивается в новый цвет!" data-en="Build a neon garage: driving inside resets wanted stars to 0 and repaints car body to a fresh neon hue!">Xaritada garaj yasash: unga kirganda yulduzlar 0 bo'lib o'chadi va mashina yangi rangda bo'yaladi!</p>
      </div>
    </div>
    <div class="card mt" style="background:var(--surface-2); padding:10px 16px;">
      <p style="margin:0; font-size:12px; color:var(--ink-2);" data-ru="Сдача работы: загрузить проект на GitHub / Vercel или прислать ссылку на интерактивный файл." data-en="Submission: Push project to GitHub / Vercel or deliver interactive HTML file.">Topshirish: Kodni GitHub / Vercel ga joylash yoki interaktiv fayl havolasini taqdim etish.</p>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. TEACHER NOTES DATA (14 Slides x [Title, Say, Do] triplets across uz, ru, en)
# -----------------------------------------------------------------------------
NOTES_DATA = {
    "0": {
        "uz": ["Titul va Darsga Kirish", "Bugun zerikarli nazariya emas, hamma sevadigan GTA 2D ochiq dunyo o'yinini quramiz! Piyoda yurish, 'F' bilan mashinaga o'tirish, drift va politsiya quvishi.", "Ekranda GTA 2D sarlavhasini oching va o'quvchilarda yuqori motivatsiya uyg'oting."],
        "ru": ["Титул и Введение", "Сегодня никакой скучной теории — мы создаем всеми любимую GTA 2D! Пешеход, угон авто на 'F', дрифт и погоня полиции.", "Откройте титульный слайд и вовлеките ребят в атмосферу открытого мира."],
        "en": ["Title & Intro", "No boring theory today — we are building GTA 2D! Pedestrian mode, hijacking with 'F', drift, and police pursuit.", "Show the title slide and ignite student enthusiasm for open world game dev."]
    },
    "1": {
        "uz": ["32-Dars Uy Vazifasi Tahlili", "O'tgan darsdagi eng katta xato: o'qlar otilgach xotiradan o'chirilmagan va o'yin qotgan. Bugun toza filter algoritmini mustahkamlaymiz.", "Doskada bullets.filter() tozalash kodini ko'rsating va blitz savolni bering."],
        "ru": ["Разбор ДЗ 32-урока", "Главная ошибка прошлого урока — пули не удалялись из памяти и игра лагала. Сегодня закрепим очистку через filter().", "Покажите код очистки снарядов и проведите 30-секундный блиц-опрос."],
        "en": ["Lesson 32 HW Review", "Major pitfall from last lesson: bullets weren't deleted from memory causing lag. Today we reinforce memory filter().", "Display projectile cleanup code and conduct the 30-second blitz."]
    },
    "2": {
        "uz": ["GTA 2D ning 5 Asosiy Ustuni", "Ochiq dunyo o'yini 5 ta mustaqil tizimdan iborat: xarita, avto, politsiya, qurollar va missiyalar.", "Slayddagi 5 ta kartani birma-bir tushuntiring."],
        "ru": ["5 Столпов GTA 2D", "Игра с открытым миром состоит из 5 независимых систем: карта, авто, полиция, стрельба и миссии.", "Последовательно разберите 5 ключевых модулей."],
        "en": ["5 Pillars of GTA 2D", "An open world game consists of 5 modular systems: map, vehicles, police AI, weapons, and missions.", "Explain the 5 modular pillars to students."]
    },
    "3": {
        "uz": ["Piyoda Harakati va 360° Nishon", "Math.atan2 yordamida qahramon doimo sichqoncha kursoriga qaraydi. WASD esa shahar ko'chalarida yugurtiradi.", "Kursorni aylantirib, o'quvchilarga qahramon qanday burilishi kerakligini tushuntiring."],
        "ru": ["Пешеход и Прицел 360°", "С помощью Math.atan2 персонаж всегда смотрит на курсор мыши. WASD перемещает по улицам города.", "Покажите механику вращения тела игрока за курсором."],
        "en": ["Pedestrian & 360 Aim", "Using Math.atan2, the player constantly faces the cursor. WASD moves along city streets.", "Demonstrate mouse rotation mechanics on the board."]
    },
    "4": {
        "uz": ["Sportkar Fizikasi va Drift", "Mashinada inersiya va tormoz bor. Tez burilganda asfaltdagi qora drift izlarini hosil qilamiz.", "Mashina nima uchun piyodadek bir zumda to'xtamasligini, inersiya muhimligini ta'kidlang."],
        "ru": ["Физика Авто и Дрифт", "У машины есть инерция и торможение. При резком повороте колеса оставляют черные следы заноса.", "Объясните, почему коэффициент трения 0.985 создает реалистичный вес авто."],
        "en": ["Car Physics & Drift", "Vehicles have momentum and braking. Sharp turns leave black skidmarks on asphalt.", "Highlight why friction 0.985 provides convincing vehicular weight."]
    },
    "5": {
        "uz": ["'F' Tugmasi Bilan Mashinaga O'tirish", "Mashinagacha masofa Math.hypot bilan tekshiriladi. 50 pikseldan yaqin bo'lsa 'F' bosilganda o'tiriladi.", "State Machine almashishini ko'rsating: piyoda yashiriladi, mashina harakatga keladi."],
        "ru": ["Посадка на Клавишу 'F'", "Дистанция до машины проверяется через Math.hypot. Если ближе 50px — по нажатию 'F' игрок садится за руль.", "Покажите смену состояний: спрайт пешехода скрыт, активна физика машины."],
        "en": ["Hijacking on 'F' Key", "Proximity is checked via Math.hypot. If closer than 50px, pressing 'F' enters the vehicle.", "Explain state switching: pedestrian hidden, car dynamics activated."]
    },
    "6": {
        "uz": ["360° Qurollar va O'q Uchishi", "Lazer otilganda stvol uchida chaqnash, orqaga tepish (recoil) va devorga urilganda uchqunlar chiqadi.", "O'qlar o'chirilishi shartligini yana bir bor eslating."],
        "ru": ["Стрельба и Отдача", "При выстреле видна вспышка ствола, отдача назад и искры при попадании в стены.", "Напомните о важности очистки массива пуль при попадании."],
        "en": ["Shooting & Recoil", "Firing produces muzzle flash, backward recoil push, and ricochet impact sparks.", "Remind students to clean up impact projectiles immediately."]
    },
    "7": {
        "uz": ["Jonli O'yin: GTA 2D Test-Drayv", "Hozir taqdimot ichidagi simulyatorda mashinaga minib ko'ramiz! Drift qiling, o't oching va politsiyadan qoching.", "Barcha o'quvchilarga klaviatura va sichqoncha bilan simulyatorni sinashga ruxsat bering."],
        "ru": ["Живой Тест-Драйв GTA 2D", "Прямо сейчас тестируем симулятор внутри слайда! Садитесь за руль, дрифтуйте, стреляйте и уходите от погони.", "Дайте ребятам протестировать симулятор прямо в слайде."],
        "en": ["Live GTA 2D Test Drive", "Right now let's test drive the in-deck simulator! Hijack the car, drift, shoot, and evade police.", "Allow students to test drive directly inside the slide."]
    },
    "8": {
        "uz": ["Qidiruv Yulduzlari va Politsiya AI", "O't ochsangiz yoki mashinani ursangiz yulduzlar ko'payadi va sirenali politsiya mashinasi quva boshlaydi.", "Politsiya AI qanday qilib o'yinchi koordinatasiga qarab burilishini tushuntiring."],
        "ru": ["Звезды Розыска и Копы", "Выстрелы повышают уровень розыска. Копы включают красно-синие мигалки и преследуют игрока.", "Объясните алгоритм преследования: полиция плавно поворачивает за машиной."],
        "en": ["Wanted Stars & Police AI", "Shooting raises wanted stars. Police flash red-blue sirens and chase the player.", "Explain pursuit algorithms: cops steer toward player coordinates."]
    },
    "9": {
        "uz": ["Faylsiz Web Audio Sintezi", "Hech qanday og'ir mp3 faylsiz brauzerning o'zida motor g'uvillashi, shina chiyillashi va politsiya sirenasi yasaladi.", "Web Audio API osilatorlarining chastotasini ko'rsatib bering."],
        "ru": ["Синтез Web Audio", "Без тяжелых mp3 файлов синтезируем рёв мотора, визг шин и сирену прямо в браузере.", "Продемонстрируйте изменение частоты осциллятора при ускорении."],
        "en": ["Web Audio Synthesis", "Zero external mp3 files: engine revs, tire squeals, and sirens synthesized in code.", "Demonstrate frequency modulation as speed shifts."]
    },
    "10": {
        "uz": ["AI Vibecoding Yo'riqnomasi", "Cursor yoki ChatGPT ga bitta uzun xabar emas, 4 ta ketma-ket aniq prompt bering.", "Promptlarni o'quvchilar bilan birga o'qib chiqing va tushuntiring."],
        "ru": ["Инструкция Vibecoding", "В Cursor или ChatGPT отправляем не один длинный запрос, а 4 четких последовательных промпта.", "Разберите 4 шага промптов вместе с классом."],
        "en": ["Vibecoding Blueprint", "In Cursor/ChatGPT, send 4 progressive prompts rather than one huge wall of text.", "Walk through the 4 prompt stages with students."]
    },
    "11": {
        "uz": ["Juftlikda Playtesting", "Partadoshingiz o'yinini ochib, rul qanday ishlashini, mashinadan tushishni va politsiyani tekshiring.", "O'quvchilarni bir-birining o'yinini sinashga undab, xatolarni toping."],
        "ru": ["Парный Playtesting", "Откройте игру соседа и проверьте физику авто, выход на 'F' и баланс погони полиции.", "Поощряйте взаимное тестирование и поиск багов."],
        "en": ["Peer Playtesting", "Audit your partner's game: test car steering, 'F' exit, and police chase balance.", "Encourage peer playtesting and bug hunting."]
    },
    "12": {
        "uz": ["Ochiq Dunyoning 4 Oltin Qoidasi", "Holatlarni toza ajrating, xotirani tozalang, inersiyani saqlang va shahar harakatga javob bersin.", "4 qoidani yakuniy xulosa qilib mustahkamlang."],
        "ru": ["4 Закона Открытого Мира", "Разделяйте состояния, чистите память, сохраняйте инерцию и оживляйте мир реакциями.", "Обобщите главные инженерные выводы урока."],
        "en": ["4 Open World Laws", "Decouple states, clean memory, preserve inertia, and make the world reactive.", "Summarize the key architectural takeaways."]
    },
    "13": {
        "uz": ["3 Darajali Uy Vazifasi", "Baza (4b): shahar va avto. Muhandislik (4b): politsiya va kuryer. Challenge (2b): Neon garajda yulduzlarni o'chirish.", "10 ballik rubrikani tushuntiring va savollarga javob bering."],
        "ru": ["3 Уровня Домашнего Задания", "База (4б): город и авто. Инженерия (4б): копы и курьер. Челлендж (2б): перекраска в гараже Pay'n'Spray.", "Разъясните 10-балльную шкалу и ответьте на вопросы."],
        "en": ["3-Tiered Homework", "Base (4 pts): city & car. Engineering (4 pts): cops & courier. Challenge (2 pts): Pay'n'Spray garage.", "Explain the 10-point rubric and take questions."]
    }
}

# -----------------------------------------------------------------------------
# 3. INTERACTIVE SIMULATOR SCRIPT (Deck + Standalone)
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
// =============================================================================
// GTA 2D CYBER CITY ENGINE — CANVAS SIMULATOR
// =============================================================================
(function() {
  const canvas = document.getElementById('gtaDeckCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const promptF = document.getElementById('deckPromptF');
  const hud = document.getElementById('deckStatsHUD');
  const resetBtn = document.getElementById('gtaDeckResetBtn');

  let W = canvas.width;
  let H = canvas.height;

  // Sound Engine (Web Audio)
  let audioCtx = null;
  function getAudio() {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    if (audioCtx.state === 'suspended') audioCtx.resume();
    return audioCtx;
  }
  function playLaser() {
    try {
      const a = getAudio();
      const osc = a.createOscillator();
      const gain = a.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(800, a.currentTime);
      osc.frequency.exponentialRampToValueAtTime(100, a.currentTime + 0.12);
      gain.gain.setValueAtTime(0.15, a.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, a.currentTime + 0.12);
      osc.connect(gain);
      gain.connect(a.destination);
      osc.start();
      osc.stop(a.currentTime + 0.13);
    } catch(e) {}
  }
  function playCoin() {
    try {
      const a = getAudio();
      const osc = a.createOscillator();
      const gain = a.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(600, a.currentTime);
      osc.frequency.setValueAtTime(900, a.currentTime + 0.08);
      gain.gain.setValueAtTime(0.2, a.currentTime);
      gain.gain.linearRampToValueAtTime(0.01, a.currentTime + 0.25);
      osc.connect(gain);
      gain.connect(a.destination);
      osc.start();
      osc.stop(a.currentTime + 0.26);
    } catch(e) {}
  }

  // City Map Bounds & Buildings
  const buildings = [
    { x: 40, y: 30, w: 160, h: 90, color: '#161d2b', label: 'TARGET LABS' },
    { x: 260, y: 30, w: 160, h: 90, color: '#1c1b29', label: 'CYBER TOWER' },
    { x: 480, y: 30, w: 120, h: 90, color: '#152222', label: 'NEON CLUB' },
    { x: 40, y: 220, w: 160, h: 100, color: '#181b28', label: 'TECH HUB' },
    { x: 260, y: 220, w: 160, h: 100, color: '#1a1f26', label: 'AUTO DOCK' },
    { x: 480, y: 220, w: 120, h: 100, color: '#1f1624', label: 'SAFEHOUSE' },
  ];

  // Game State
  let player = { x: 120, y: 160, speed: 3.2, angle: 0, inCar: false, radius: 10 };
  let car = { x: 200, y: 160, angle: 0, speed: 0, accel: 0.18, brake: 0.15, maxSpeed: 6.5, turnSpeed: 0.065, w: 42, h: 22 };
  let cop = { x: 550, y: 160, angle: Math.PI, speed: 3.8, active: false, sirenTimer: 0, light: '#ff0033' };
  let targetPkg = { x: 540, y: 270, radius: 14, collected: false, pulse: 0 };
  let bullets = [];
  let sparks = [];
  let skidmarks = [];
  let mouse = { x: 0, y: 0 };
  let keys = {};
  let wanted = 0;
  let cash = 0;

  // Input Listeners
  window.addEventListener('keydown', (e) => {
    keys[e.code] = true;
    if (e.code === 'KeyF') {
      if (!player.inCar) {
        const d = Math.hypot(player.x - car.x, player.y - car.y);
        if (d < 50) {
          player.inCar = true;
        }
      } else {
        player.inCar = false;
        player.x = car.x + Math.sin(car.angle) * 25;
        player.y = car.y - Math.cos(car.angle) * 25;
      }
    }
  });
  window.addEventListener('keyup', (e) => { keys[e.code] = false; });

  canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.y;
  });

  canvas.addEventListener('mousedown', (e) => {
    if (e.button === 0 && !player.inCar) {
      // Shoot bullet
      const bSpeed = 9;
      bullets.push({
        x: player.x + Math.cos(player.angle) * 16,
        y: player.y + Math.sin(player.angle) * 16,
        vx: Math.cos(player.angle) * bSpeed,
        vy: Math.sin(player.angle) * bSpeed,
        life: 45
      });
      playLaser();
      wanted = Math.min(3, wanted + 1);
      cop.active = true;
    }
  });

  if (resetBtn) {
    resetBtn.addEventListener('click', resetGame);
  }

  function resetGame() {
    player.x = 120;
    player.y = 160;
    player.inCar = false;
    car.x = 200;
    car.y = 160;
    car.speed = 0;
    car.angle = 0;
    cop.x = 550;
    cop.y = 160;
    cop.active = false;
    wanted = 0;
    cash = 0;
    bullets = [];
    sparks = [];
    skidmarks = [];
  }

  function update() {
    // 1. Player On Foot Movement
    if (!player.inCar) {
      let dx = 0, dy = 0;
      if (keys['KeyW'] || keys['ArrowUp']) dy -= 1;
      if (keys['KeyS'] || keys['ArrowDown']) dy += 1;
      if (keys['KeyA'] || keys['ArrowLeft']) dx -= 1;
      if (keys['KeyD'] || keys['ArrowRight']) dx += 1;

      if (dx !== 0 && dy !== 0) {
        dx *= 0.7071;
        dy *= 0.7071;
      }

      let nx = player.x + dx * player.speed;
      let ny = player.y + dy * player.speed;

      // Building Collisions
      if (!checkBuildingCollide(nx, ny, player.radius)) {
        player.x = Math.max(12, Math.min(W - 12, nx));
        player.y = Math.max(12, Math.min(H - 12, ny));
      }

      // Rotate towards mouse
      player.angle = Math.atan2(mouse.y - player.y, mouse.x - player.x);

      // Proximity to car prompt
      const distToCar = Math.hypot(player.x - car.x, player.y - car.y);
      if (distToCar < 45 && promptF) {
        promptF.style.display = 'block';
      } else if (promptF) {
        promptF.style.display = 'none';
      }
    } else {
      if (promptF) promptF.style.display = 'none';

      // 2. Car Driving Physics
      let turning = false;
      if (keys['KeyW'] || keys['ArrowUp']) car.speed = Math.min(car.maxSpeed, car.speed + car.accel);
      if (keys['KeyS'] || keys['ArrowDown']) car.speed = Math.max(-2.5, car.speed - car.brake);

      if (Math.abs(car.speed) > 0.3) {
        if (keys['KeyA'] || keys['ArrowLeft']) { car.angle -= car.turnSpeed; turning = true; }
        if (keys['KeyD'] || keys['ArrowRight']) { car.angle += car.turnSpeed; turning = true; }
      }

      car.speed *= 0.985; // friction
      let ncx = car.x + Math.cos(car.angle) * car.speed;
      let ncy = car.y + Math.sin(car.angle) * car.speed;

      if (!checkBuildingCollide(ncx, ncy, 18)) {
        car.x = Math.max(20, Math.min(W - 20, ncx));
        car.y = Math.max(20, Math.min(H - 20, ncy));
      } else {
        car.speed = -car.speed * 0.4; // bounce
      }

      // Player follows car
      player.x = car.x;
      player.y = car.y;

      // Skidmarks on drift
      if (Math.abs(car.speed) > 3.8 && turning) {
        skidmarks.push({ x: car.x, y: car.y, a: car.angle, life: 120 });
      }
    }

    // 3. Bullets update
    bullets.forEach(b => {
      b.x += b.vx;
      b.y += b.vy;
      b.life--;

      // Hit buildings
      if (checkBuildingCollide(b.x, b.y, 3)) {
        b.life = 0;
        for (let i = 0; i < 5; i++) {
          sparks.push({
            x: b.x, y: b.y,
            vx: (Math.random() - 0.5) * 4,
            vy: (Math.random() - 0.5) * 4,
            life: 15,
            color: '#00f2fe'
          });
        }
      }
    });
    bullets = bullets.filter(b => b.life > 0);

    // 4. Sparks update
    sparks.forEach(s => {
      s.x += s.vx;
      s.y += s.vy;
      s.life--;
    });
    sparks = sparks.filter(s => s.life > 0);

    // 5. Skidmarks life
    skidmarks.forEach(s => s.life--);
    skidmarks = skidmarks.filter(s => s.life > 0);

    // 6. Delivery package collection
    targetPkg.pulse += 0.08;
    const px = player.inCar ? car.x : player.x;
    const py = player.inCar ? car.y : player.y;
    if (Math.hypot(px - targetPkg.x, py - targetPkg.y) < targetPkg.radius + 15) {
      cash += 500;
      playCoin();
      // Move package to new building alley
      const spots = [{x: 100, y: 160}, {x: 350, y: 160}, {x: 540, y: 160}, {x: 210, y: 280}];
      const next = spots[Math.floor(Math.random() * spots.length)];
      targetPkg.x = next.x;
      targetPkg.y = next.y;
    }

    // 7. Police Pursuit AI
    if (wanted > 0 && cop.active) {
      cop.sirenTimer++;
      cop.light = (cop.sirenTimer % 18 < 9) ? '#ff0033' : '#0066ff';

      const targetX = player.inCar ? car.x : player.x;
      const targetY = player.inCar ? car.y : player.y;
      const tAngle = Math.atan2(targetY - cop.y, targetX - cop.x);

      cop.angle += (tAngle - cop.angle) * 0.055;
      cop.x += Math.cos(cop.angle) * cop.speed;
      cop.y += Math.sin(cop.angle) * cop.speed;
    }

    // Update HUD
    if (hud) {
      hud.textContent = `⭐ WANTED: ${wanted} · 💵 CASH: $${cash}`;
    }
  }

  function checkBuildingCollide(x, y, r) {
    for (let b of buildings) {
      if (x + r > b.x && x - r < b.x + b.w && y + r > b.y && y - r < b.y + b.h) {
        return true;
      }
    }
    return false;
  }

  function render() {
    ctx.clearRect(0, 0, W, H);

    // Roads & Crossings Background
    ctx.fillStyle = '#10131a';
    ctx.fillRect(0, 0, W, H);

    // Street Crossings & Center Dotted Lines
    ctx.strokeStyle = '#222938';
    ctx.lineWidth = 44;
    // Main avenue (horizontal)
    ctx.beginPath();
    ctx.moveTo(0, 160);
    ctx.lineTo(W, 160);
    ctx.stroke();

    // Vertical alleys
    ctx.lineWidth = 36;
    ctx.beginPath();
    ctx.moveTo(230, 0); ctx.lineTo(230, H);
    ctx.moveTo(450, 0); ctx.lineTo(450, H);
    ctx.stroke();

    // Road Divider Dashes
    ctx.strokeStyle = '#ffcc00';
    ctx.lineWidth = 2;
    ctx.setLineDash([12, 10]);
    ctx.beginPath();
    ctx.moveTo(0, 160);
    ctx.lineTo(W, 160);
    ctx.stroke();
    ctx.setLineDash([]);

    // Skidmarks
    skidmarks.forEach(s => {
      ctx.save();
      ctx.translate(s.x, s.y);
      ctx.rotate(s.a);
      ctx.fillStyle = `rgba(0,0,0,${s.life / 160})`;
      ctx.fillRect(-12, -7, 10, 3);
      ctx.fillRect(-12, 4, 10, 3);
      ctx.restore();
    });

    // Draw Buildings
    buildings.forEach(b => {
      ctx.fillStyle = b.color;
      ctx.strokeStyle = '#2d3748';
      ctx.lineWidth = 2;
      ctx.fillRect(b.x, b.y, b.w, b.h);
      ctx.strokeRect(b.x, b.y, b.w, b.h);

      // Neon Sign
      ctx.fillStyle = '#00f2fe';
      ctx.font = '800 9px monospace';
      ctx.fillText(b.label, b.x + 8, b.y + 16);

      // Roof Helipad / Details
      ctx.strokeStyle = 'rgba(255,255,255,0.08)';
      ctx.strokeRect(b.x + 10, b.y + 24, b.w - 20, b.h - 34);
    });

    // Draw Package (Delivery Objective)
    ctx.save();
    const pulseR = targetPkg.radius + Math.sin(targetPkg.pulse) * 3;
    ctx.strokeStyle = '#ffdd00';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(targetPkg.x, targetPkg.y, pulseR, 0, Math.PI * 2);
    ctx.stroke();
    ctx.fillStyle = '#ffdd00';
    ctx.font = 'bold 8px sans-serif';
    ctx.fillText('📦 DELIVERY', targetPkg.x - 24, targetPkg.y - pulseR - 4);
    ctx.restore();

    // Draw Sports Car
    ctx.save();
    ctx.translate(car.x, car.y);
    ctx.rotate(car.angle);

    // Car Shadow
    ctx.fillStyle = 'rgba(0,0,0,0.5)';
    ctx.fillRect(-22, -11, 44, 22);

    // Car Body (Neon Cyan Supercar)
    ctx.fillStyle = '#00f2fe';
    ctx.fillRect(-20, -10, 40, 20);

    // Roof / Windshield
    ctx.fillStyle = '#091524';
    ctx.fillRect(-8, -8, 20, 16);
    ctx.fillStyle = '#1a334d';
    ctx.fillRect(-3, -7, 12, 14);

    // Headlights Cones
    ctx.fillStyle = 'rgba(255, 235, 120, 0.18)';
    ctx.beginPath();
    ctx.moveTo(20, -6);
    ctx.lineTo(80, -28);
    ctx.lineTo(80, -2);
    ctx.closePath();
    ctx.fill();

    ctx.beginPath();
    ctx.moveTo(20, 6);
    ctx.lineTo(80, 2);
    ctx.lineTo(80, 28);
    ctx.closePath();
    ctx.fill();

    ctx.restore();

    // Draw Police Cruiser (if active)
    if (cop.active) {
      ctx.save();
      ctx.translate(cop.x, cop.y);
      ctx.rotate(cop.angle);

      // Cruiser body
      ctx.fillStyle = '#0d1117';
      ctx.fillRect(-20, -10, 40, 20);
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(-4, -10, 12, 20); // white doors

      // Flashing Siren Roof Bar
      ctx.fillStyle = cop.light;
      ctx.shadowColor = cop.light;
      ctx.shadowBlur = 12;
      ctx.fillRect(-2, -6, 6, 12);
      ctx.shadowBlur = 0;

      ctx.restore();
    }

    // Draw Player On Foot (if not inside car)
    if (!player.inCar) {
      ctx.save();
      ctx.translate(player.x, player.y);
      ctx.rotate(player.angle);

      // Body
      ctx.fillStyle = '#22c55e'; // green agent
      ctx.beginPath();
      ctx.arc(0, 0, 8, 0, Math.PI * 2);
      ctx.fill();

      // Hands holding weapon
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(5, -4, 10, 3);

      // Flashlight cone
      ctx.fillStyle = 'rgba(0, 242, 254, 0.09)';
      ctx.beginPath();
      ctx.moveTo(6, 0);
      ctx.lineTo(70, -20);
      ctx.lineTo(70, 20);
      ctx.closePath();
      ctx.fill();

      ctx.restore();
    }

    // Draw Bullets
    ctx.fillStyle = '#ffdd00';
    bullets.forEach(b => {
      ctx.beginPath();
      ctx.arc(b.x, b.y, 2.5, 0, Math.PI * 2);
      ctx.fill();
    });

    // Draw Sparks
    sparks.forEach(s => {
      ctx.fillStyle = s.color;
      ctx.fillRect(s.x, s.y, 2, 2);
    });

    // Minimap Radar (Bottom-Right Corner)
    const mapW = 80, mapH = 50;
    const mapX = W - mapW - 10, mapY = H - mapH - 10;
    ctx.fillStyle = 'rgba(10, 15, 25, 0.85)';
    ctx.strokeStyle = 'var(--accent, #00f2fe)';
    ctx.lineWidth = 1;
    ctx.fillRect(mapX, mapY, mapW, mapH);
    ctx.strokeRect(mapX, mapY, mapW, mapH);

    // Minimap Buildings
    ctx.fillStyle = '#253245';
    buildings.forEach(b => {
      ctx.fillRect(mapX + (b.x / W) * mapW, mapY + (b.y / H) * mapH, (b.w / W) * mapW, (b.h / H) * mapH);
    });

    // Minimap Player (Green Dot)
    ctx.fillStyle = '#22c55e';
    ctx.fillRect(mapX + (player.x / W) * mapW - 1.5, mapY + (player.y / H) * mapH - 1.5, 3, 3);

    // Minimap Car (Cyan Dot)
    ctx.fillStyle = '#00f2fe';
    ctx.fillRect(mapX + (car.x / W) * mapW - 2, mapY + (car.y / H) * mapH - 2, 4, 4);

    // Minimap Objective (Yellow)
    ctx.fillStyle = '#ffdd00';
    ctx.fillRect(mapX + (targetPkg.x / W) * mapW - 2, mapY + (targetPkg.y / H) * mapH - 2, 4, 4);
  }

  function loop() {
    update();
    render();
    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);
})();
"""

# -----------------------------------------------------------------------------
# 4. BUILD FUNCTIONS
# -----------------------------------------------------------------------------
def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "33-dars: GTA 2D: Cyber City — Kiber-Shahar Ochiq Dunyo O'yini"
    title_ru = "Урок 33: GTA 2D: Cyber City — Создание Игры с Открытым Миром"
    title_en = "Lesson 33: GTA 2D: Cyber City — Open World 2D Game Architecture"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="7–8 КЛАСС" data-en="GRADES 7–8">7–8-SINF</span>',
                 tpl)

    titles_json = json.dumps({"uz": title_uz, "ru": title_ru, "en": title_en}, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    canonical_notes = {
        "uz": [NOTES_DATA[str(i)]["uz"] for i in range(14)],
        "ru": [NOTES_DATA[str(i)]["ru"] for i in range(14)],
        "en": [NOTES_DATA[str(i)]["en"] for i in range(14)]
    }
    notes_json = json.dumps(canonical_notes, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\n\};\n\nfunction updateSlide',
                 f'var NOTES = {notes_json};\n\nfunction updateSlide', tpl)

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

    title_uz = "33-dars: GTA 2D: Cyber City — Ish Varaqasi"
    title_ru = "Урок 33: GTA 2D: Cyber City — Рабочий Лист"
    title_en = "Lesson 33: GTA 2D: Cyber City — Worksheet"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<h1>.*?</h1>',
                 f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>',
                 tpl)

    sec1_html = """
    <p class="lead" style="font-size:12px; margin-bottom:8px;" data-ru="<strong>Миссия Урока:</strong> Спроектировать и собрать открытый 2D кибер-город в стиле GTA: угон спорткара на клавишу 'F', физика заноса, лазерные перестрелки на 360 градусов и полицейский розыск." data-en="<strong>Lesson Mission:</strong> Architect an open 2D cyber city in GTA style: vehicle hijacking on 'F', drift dynamics, 360° laser blasters, and police pursuit mechanics."><strong>Dars Missiyasi:</strong> GTA uslubidagi 2D ochiq kiber-shaharni loyihalash: 'F' tugmasi bilan sportkarga o'tirish, shina drift izlari fizikasi, 360° lazer blaster va politsiya ta'qib tizimini qurish.</p>
    <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="5 Ключевых Механик GTA 2D:" data-en="5 Core Mechanics of GTA 2D:">GTA 2D O'yinining 5 Asosiy Mexanikasi:</div>
      <div>1. <strong>Piyoda va 360° Nishon:</strong> <span data-ru="WASD перемещение + Math.atan2 вращение за курсором" data-en="WASD movement + Math.atan2 mouse look">WASD bilan yugurish va kursor yo'nalishiga burilish</span>.</div>
      <div>2. <strong>'F' Bilan Mashinaga O'tirish:</strong> <span data-ru="Проверка дистанции через Math.hypot и смена режима на car.speed" data-en="Proximity check via Math.hypot, switching state to car.speed">Math.hypot orqali yaqinlikni tekshirib haydovchiga aylanish</span>.</div>
      <div>3. <strong>Drift va Asfalt Izlari:</strong> <span data-ru="Коэффициент трения 0.985 и массив следов шин skidmarks" data-en="Friction 0.985 and tire skidmarks array">0.985 ishqalanish va burilganda asfaltdagi qora izlar</span>.</div>
      <div>4. <strong>Qidiruv Yulduzlari (⭐⭐):</strong> <span data-ru="Стрельба активирует погоню патрульных машин с сиренами" data-en="Gunfire alerts patrol cruisers with flashing sirens">O't ochish sirenali politsiya ta'qibini faollashtiradi</span>.</div>
      <div>5. <strong>Kiber-Kuryer Missiyasi:</strong> <span data-ru="Доставка неоновых пакетов в безопасные точки приносит +$500" data-en="Delivering neon packages to waypoints awards +$500 cash">Xaritadagi sariq neon paketlarni yetkazib berish ($500 kesh)</span>.</div>
    </div>
    """
    tpl = re.sub(r'<!-- SEC1_START -->[\s\S]*?<!-- SEC1_END -->', sec1_html, tpl)

    code_html = """
    <div style="font-size:10px; background:var(--surface-2); border:1px solid var(--border); border-radius:6px; padding:8px; font-family:monospace;">
      <div style="color:var(--accent); font-weight:700; margin-bottom:4px;">// Mashinaga o'tirish va drift fizikasi:</div>
      <div>if (keys['KeyF'] &amp;&amp; Math.hypot(p.x - c.x, p.y - c.y) &lt; 50) { p.inCar = !p.inCar; }</div>
      <div>if (p.inCar) {</div>
      <div>&nbsp;&nbsp;if (keys['KeyW']) c.speed += 0.18;</div>
      <div>&nbsp;&nbsp;if (keys['KeyA']) c.angle -= 0.065;</div>
      <div>&nbsp;&nbsp;c.speed *= 0.985; // Ishqalanish</div>
      <div>&nbsp;&nbsp;c.x += Math.cos(c.angle) * c.speed;</div>
      <div>&nbsp;&nbsp;c.y += Math.sin(c.angle) * c.speed;</div>
      <div>}</div>
    </div>
    """
    tpl = re.sub(r'<!-- SEC2_START -->[\s\S]*?<!-- SEC2_END -->', code_html, tpl)

    task1_html = """
    <div style="font-size:11px; line-height:1.5;">
      <p style="margin:2px 0 4px; font-weight:700;" data-ru="Задание 1: Разбор Физики Инерции" data-en="Task 1: Inertia Physics Analysis">1-Vazifa: Inersiya va Ishqalanish Tahlili</p>
      <p style="margin:2px 0 4px; font-size:8.5pt;" data-ru="Почему мы умножаем скорость машины на 0.985 в каждом кадре вместо мгновенной остановки при отпускании газа?" data-en="Why do we multiply car speed by 0.985 each frame instead of setting speed to 0 immediately?">Nega gaz qo'yib yuborilganda mashina tezligini darhol 0 qilmasdan, har kadrda 0.985 ga ko'paytiramiz?</p>
      <div style="border-bottom:1px dashed var(--border); height:22px; margin:4px 0;"></div>
      <div style="border-bottom:1px dashed var(--border); height:22px; margin:4px 0;"></div>
    </div>
    """
    tpl = re.sub(r'<!-- TASK1_START -->[\s\S]*?<!-- TASK1_END -->', task1_html, tpl)

    task2_html = """
    <div style="font-size:11px; line-height:1.5;">
      <p style="margin:2px 0 4px; font-weight:700;" data-ru="Задание 2: Архитектура Полицейского ИИ" data-en="Task 2: Police AI Logic">2-Vazifa: Politsiya Quvishi Mantig'i</p>
      <p style="margin:2px 0 4px; font-size:8.5pt;" data-ru="Напишите формулу, по которой полицейская машина вычисляет угол поворота targetAngle к координатам игрока:" data-en="Write down the formula the police cruiser uses to calculate targetAngle towards player coordinates:">Politsiya mashinasi o'yinchining (x, y) koordinatalari tomon burilish burchagini qaysi formula orqali hisoblaydi?</p>
      <div style="border-bottom:1px dashed var(--border); height:22px; margin:4px 0;"></div>
      <div style="border-bottom:1px dashed var(--border); height:22px; margin:4px 0;"></div>
    </div>
    """
    tpl = re.sub(r'<!-- TASK2_START -->[\s\S]*?<!-- TASK2_END -->', task2_html, tpl)

    task3_html = """
    <div style="font-size:11px; line-height:1.5;">
      <p style="margin:2px 0 4px; font-weight:700;" data-ru="Задание 3: Промпт для ИИ (Vibecoding)" data-en="Task 3: Vibecoding Prompt">3-Vazifa: AI ga Beriladigan Oltin Prompt</p>
      <p style="margin:2px 0 4px; font-size:8.5pt;" data-ru="Сформулируйте промпт для добавления неонового гаража Pay'n'Spray, который перекрашивает авто и сбрасывает звезды розыска:" data-en="Formulate the prompt to add a Pay'n'Spray neon garage that repaints car and resets wanted stars:">Mashinani yangi rangga bo'yovchi va qidiruv yulduzlarini 0 qiluvchi Neon Garaj qo'shish uchun AI ga beriladigan promptni yozing:</p>
      <div style="border-bottom:1px dashed var(--border); height:22px; margin:4px 0;"></div>
      <div style="border-bottom:1px dashed var(--border); height:22px; margin:4px 0;"></div>
    </div>
    """
    tpl = re.sub(r'<!-- TASK3_START -->[\s\S]*?<!-- TASK3_END -->', task3_html, tpl)

    # 10-Point Rubric
    rubric_html = """
    <table class="rubric-table" style="width:100%; border-collapse:collapse; font-size:10px; margin-top:6px;">
      <thead>
        <tr style="background:var(--surface-2);">
          <th style="padding:4px 6px; border:1px solid var(--border);" data-ru="Критерий Оценки" data-en="Criteria">Baholash Mezoni</th>
          <th style="padding:4px 6px; border:1px solid var(--border); width:70px;" data-ru="Баллы" data-en="Max Pts">Maksimal Ball</th>
          <th style="padding:4px 6px; border:1px solid var(--border);" data-ru="Самопроверка" data-en="Check">O'quvchi Belgisi</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:4px 6px; border:1px solid var(--border);" data-ru="1. Город и ходьба: WASD перемещение + поворот за мышью" data-en="1. City & on-foot movement: WASD + mouse aim">1. Shahar va piyoda harakati: WASD + sichqoncha nishoni</td>
          <td style="padding:4px 6px; border:1px solid var(--border); text-align:center; font-weight:700;">2 ball</td>
          <td style="padding:4px 6px; border:1px solid var(--border); text-align:center;">[ &nbsp; ]</td>
        </tr>
        <tr>
          <td style="padding:4px 6px; border:1px solid var(--border);" data-ru="2. Угон на 'F' и физика авто: газ, тормоз, инерция 0.985" data-en="2. 'F' hijacking & car dynamics: accel, brake, friction">2. 'F' bilan mashinaga o'tirish va inersiyali haydash</td>
          <td style="padding:4px 6px; border:1px solid var(--border); text-align:center; font-weight:700;">2 ball</td>
          <td style="padding:4px 6px; border:1px solid var(--border); text-align:center;">[ &nbsp; ]</td>
        </tr>
        <tr>
          <td style="padding:4px 6px; border:1px solid var(--border);" data-ru="3. Дрифт: генерация следов шин на асфальте" data-en="3. Drift: generating tire skidmarks on turns">3. Drift: keskin burilishda shina izlarining chizilishi</td>
          <td style="padding:4px 6px; border:1px solid var(--border); text-align:center; font-weight:700;">2 ball</td>
          <td style="padding:4px 6px; border:1px solid var(--border); text-align:center;">[ &nbsp; ]</td>
        </tr>
        <tr>
          <td style="padding:4px 6px; border:1px solid var(--border);" data-ru="4. Стрельба и полиция: лазерные пули + погоня с сиренами" data-en="4. Weapons & police: laser bullets + pursuit sirens">4. Qurollar va politsiya: lazer otish va sirenali ta'qib</td>
          <td style="padding:4px 6px; border:1px solid var(--border); text-align:center; font-weight:700;">2 ball</td>
          <td style="padding:4px 6px; border:1px solid var(--border); text-align:center;">[ &nbsp; ]</td>
        </tr>
        <tr>
          <td style="padding:4px 6px; border:1px solid var(--border);" data-ru="5. Доставка и кэш: сбор пакетов (+$500) и радар мини-карты" data-en="5. Courier & cash: package pickups and minimap radar">5. Kiber-kuryer va minimap: paket yetkazish va GPS radar</td>
          <td style="padding:4px 6px; border:1px solid var(--border); text-align:center; font-weight:700;">2 ball</td>
          <td style="padding:4px 6px; border:1px solid var(--border); text-align:center;">[ &nbsp; ]</td>
        </tr>
      </tbody>
    </table>
    """
    tpl = re.sub(r'<!-- RUBRIC_START -->[\s\S]*?<!-- RUBRIC_END -->', rubric_html, tpl)

    out_path = os.path.join(DEST_DIR, "varaqa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: varaqa.html")


def build_homework():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "33-dars: GTA 2D: Cyber City — Mustaqil Uy Vazifasi"
    title_ru = "Урок 33: GTA 2D: Cyber City — Домашнее Задание"
    title_en = "Lesson 33: GTA 2D: Cyber City — Interactive Homework"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<h1[^>]*>.*?</h1>',
                 f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>',
                 tpl)

    hw_tasks = """
    <!-- TASK 1 -->
    <div class="card mb">
      <div class="tag" data-ru="Задание 1: Базовая физика авто" data-en="Task 1: Car Drift Dynamics">1-Topshiriq: Sportkar Harakati va Inersiya (4 ball)</div>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите блок кода физики движения машины с инерцией (0.985) и ограничением максимальной скорости:" data-en="Write car driving physics code with friction (0.985) and top speed clamping:">Mashinaning gaz bosilgandagi tezlanishi, inersiya (0.985) va burilish kodini yozing:</p>
      <textarea id="hw_code_1" class="code-editor" style="width:100%; height:110px; background:var(--surface-2); color:var(--ink); font-family:monospace; padding:8px; border-radius:6px; border:1px solid var(--border);">// Mashina harakat fizikasi:
if (keys['KeyW']) car.speed += car.accel;
if (keys['KeyS']) car.speed -= car.brake;
if (Math.abs(car.speed) > 0.2) {
  if (keys['KeyA']) car.angle -= car.turnSpeed;
  if (keys['KeyD']) car.angle += car.turnSpeed;
}
car.speed *= 0.985;
car.x += Math.cos(car.angle) * car.speed;
car.y += Math.sin(car.angle) * car.speed;</textarea>
    </div>

    <!-- TASK 2 -->
    <div class="card mb">
      <div class="tag" data-ru="Задание 2: Посадка в авто на 'F'" data-en="Task 2: Hijacking 'F' Key">2-Topshiriq: 'F' Bilan Mashinaga O'tirish Mantig'i (4 ball)</div>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Реализуйте проверку дистанции Math.hypot и переключение флага player.inCar при нажатии клавиши 'F':" data-en="Implement distance proximity check via Math.hypot and toggle player.inCar flag upon pressing 'F':">O'yinchi mashina yonida 'F' bosganda minish va qayta bosganda tushish kodini yozing:</p>
      <textarea id="hw_code_2" class="code-editor" style="width:100%; height:100px; background:var(--surface-2); color:var(--ink); font-family:monospace; padding:8px; border-radius:6px; border:1px solid var(--border);">window.addEventListener('keydown', (e) => {
  if (e.code === 'KeyF') {
    if (!player.inCar) {
      const dist = Math.hypot(player.x - car.x, player.y - car.y);
      if (dist < 50) player.inCar = true;
    } else {
      player.inCar = false;
      player.x = car.x + 30;
      player.y = car.y;
    }
  }
});</textarea>
    </div>

    <!-- TASK 3 -->
    <div class="card mb">
      <div class="tag" style="background:var(--danger); color:#fff;" data-ru="Задание 3: Кибер-Челлендж" data-en="Task 3: Cyber Challenge">3-Topshiriq: Politsiya Yulduzlari va Qochish (2 ball)</div>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Как запрограммировать полицию, чтобы она включала сирены и начинала погоню только после стрельбы игрока?" data-en="How to program police AI so they activate sirens and pursuit only after gunfire?">O'yinchi o't ochganda qidiruv yulduzi (wanted) oshishi va politsiya quva boshlashi mantig'ini yozing:</p>
      <textarea id="hw_code_3" class="code-editor" style="width:100%; height:90px; background:var(--surface-2); color:var(--ink); font-family:monospace; padding:8px; border-radius:6px; border:1px solid var(--border);">function onPlayerShoot() {
  wanted = Math.min(3, wanted + 1);
  cop.active = true;
  playSirenSound();
}</textarea>
    </div>
    """
    tpl = re.sub(r'<!-- HW_CONTENT_START -->[\s\S]*?<!-- HW_CONTENT_END -->', hw_tasks, tpl)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")


def build_teacher_reading():
    content = """# 7–8-sinf · 11-hafta · 33-dars: GTA 2D: Cyber City
## O'qituvchi Uchun Dars O'tish Qo'llanmasi (80 daqiqalik Juftlik Dars)

**O'qituvchi:** Ismoiljon Usmonov  
**Fan:** Vibecoding / Game Dev  
**Mavzu:** GTA 2D: Cyber City — Kiber-Shahar Ochiq Dunyo O'yin Loyihasi  
**Dars turi:** Juftlik blok (Double Block — 80 daqiqa)

---

### 1. Darsning Pedagogik Maqsadi va Falsafasi
Bugungi darsda qorong'i yer osti zindonlari yoki quruq formulalar o'rniga, o'quvchilar hayrat bilan o'ynaydigan **GTA 2D ochiq kiber-shahar o'yini** noldan yig'iladi. 
O'quvchilar mustaqil ravishda:
1. WASD piyoda harakati va sichqoncha bilan 360° nishonga olish;
2. 'F' tugmasi bilan sportkarga o'tirish va asfaltdagi drift fizikasi;
3. 360° lazer blaster, o'qlar ballistikasi va orqaga tepish;
4. Qidiruv yulduzlari (⭐⭐⭐) va miltillovchi sirenali politsiya ta'qibi;
5. Kiber-kuryer yetkazib berish missiyalari va naqd pul ($$$) hisobini birlashtiradilar.

---

### 2. Dars Vaqti Taqsimoti (80 Daqiqalik Aniq Pacing)

| Bosqich | Vaqt | Faoliyat Mazmuni |
|:---:|:---:|---|
| **1-Bosqich** | 00:00–04:00 | **Titul va Darsga Kirish:** GTA 2D o'yin loyihasi konsepsiyasini e'lon qilish. |
| **2-Bosqich** | 04:00–12:00 | **Uy Vazifasi Tahlili:** 32-dars otishma kodidagi xotira oqishi (bullets memory leak) xatosi va toza filter(). |
| **3-Bosqich** | 12:00–20:00 | **Kiber-Shahar Arxitekturasi:** GTA 2D ning 5 asosiy yadrosi (Xarita, Avto, Politsiya, Qurollar, Missiyalar). |
| **4-Bosqich** | 20:00–28:00 | **Piyoda Harakati:** Math.atan2 bilan burilish va WASD vektorli siljish. |
| **5-Bosqich** | 28:00–36:00 | **Sportkar Fizikasi:** Tezlanish, inersiya (0.985) va asfaltdagi qora drift izlari. |
| **6-Bosqich** | 36:00–44:00 | **'F' Tugmasi Mantig'i:** Masofani tekshirib (Math.hypot < 50) mashinaga o'tirish / tushish. |
| **7-Bosqich** | 44:00–50:00 | **360° Qurollar:** Stvol chaqnashi, orqaga tepish va devorga urilganda uchqunlar. |
| **8-Bosqich** | 50:00–60:00 | **Jonli Test-Drayv:** Taqdimot ichidagi interaktiv GTA 2D simulyatorida poyga o'tkazish. |
| **9-Bosqich** | 60:00–66:00 | **Politsiya AI:** Qidiruv yulduzlari, miltillovchi qizil-ko'k sirena va ta'qib burchagi. |
| **10-Bosqich** | 66:00–70:00 | **Web Audio Sintezi:** Dvigatel guvillashi, shinalar g'iyqillashi va politsiya sirenasi. |
| **11-Bosqich** | 70:00–74:00 | **Vibecoding Prompt Arxitekturasi:** AI ga 4 bosqichli buyruqlar berish metodikasi. |
| **12-Bosqich** | 74:00–77:00 | **Juftlikda Playtesting:** Partadoshining o'yinini tekshirish va xatolarni topish. |
| **13-Bosqich** | 77:00–79:00 | **Xulosa va Oltin Qoidalar:** Ochiq dunyo arxitekturasining 4 ta oltin qoidasi. |
| **14-Bosqich** | 79:00–80:00 | **3 Darajali Uy Vazifasi:** 10 ballik rubrika va Pay'n'Spray neon garaj topshirig'i. |

---

### 3. Keng Tarqalgan Xatolar (Pitfalls) va Oltin Yechimlar
* **Tuzoq 1: Mashinadan tushganda bino ichiga tushib qolish:**
  * *Yechim:* O'yinchini mashinaning yon tomoniga chiqarishda devor chegarasi tekshiriladi: `checkBuildingCollide(player.x, player.y)`.
* **Tuzoq 2: Mashina burilganda joyida aylanib qolishi:**
  * *Yechim:* Mashina faqat tezlik mavjud bo'lganda burilishi kerak: `if (Math.abs(car.speed) > 0.2) { car.angle += turn; }`.
* **Tuzoq 3: Politsiyaning juda tez yetib olib o'yinni buzishi:**
  * *Yechim:* Politsiya tezligi (3.8 px) sportkar maksimal tezligidan (6.5 px) biroz sekinroq qilinadi, shunda o'yinchi drift qilib qochishi mumkin bo'ladi!
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Created: TEACHER_READING.md")


def build_standalone_simulator():
    html = f"""<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title data-ru="GTA 2D: Cyber City — Симулятор Открытого Мира" data-en="GTA 2D: Cyber City — Open World Simulator">GTA 2D: Cyber City — Ochiq Dunyo Simulyatori</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #090c10;
      color: #e6edf3;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      overflow: hidden;
    }}
    #gameContainer {{
      position: relative;
      border: 2px solid #00f2fe;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 16px 48px rgba(0, 242, 254, 0.2);
    }}
    canvas {{ display: block; background: #10131a; }}
    .hud-bar {{
      position: absolute;
      top: 12px;
      left: 14px;
      right: 14px;
      display: flex;
      justify-content: space-between;
      pointer-events: none;
      font-weight: 800;
      font-size: 14px;
      text-shadow: 0 2px 4px rgba(0,0,0,0.8);
    }}
    .hud-wanted {{ color: #ffcc00; }}
    .hud-cash {{ color: #22c55e; }}
    .prompt-box {{
      position: absolute;
      bottom: 16px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(0, 0, 0, 0.85);
      border: 1px solid #00f2fe;
      color: #00f2fe;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      display: none;
      pointer-events: none;
    }}
    .instructions {{
      margin-top: 12px;
      font-size: 12px;
      color: #8b949e;
      display: flex;
      gap: 20px;
    }}
    .instructions span {{ color: #e6edf3; font-weight: 600; }}
  </style>
</head>
<body>
  <div id="gameContainer">
    <canvas id="gtaDeckCanvas" width="800" height="500"></canvas>
    <div class="hud-bar">
      <div id="deckStatsHUD" class="hud-wanted">⭐ WANTED: 0 · 💵 CASH: $0</div>
      <div style="color:#00f2fe;">TARGET CITY 2D</div>
    </div>
    <div id="deckPromptF" class="prompt-box">[F] Mashinaga o'tirish / Enter Vehicle</div>
  </div>
  <div class="instructions">
    <div><span>WASD / Strelkalar:</span> Harakat</div>
    <div><span>F:</span> Mashinaga o'tirish / tushish</div>
    <div><span>Sichqoncha:</span> 360° Nishon</div>
    <div><span>Chap Klik:</span> Lazer Otish</div>
    <div><span>Sariq Neon:</span> Kuryer Missiyasi ($500)</div>
  </div>

  <script>
    {SIMULATOR_JS}
  </script>
</body>
</html>"""
    out_path = os.path.join(DEST_DIR, "simulator", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: simulator/index.html")


def main():
    print("🚀 Building 7–8th Grade Week 11 Lesson 33: GTA 2D: Cyber City...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_standalone_simulator()
    print("✅ All GTA 2D Lesson 33 files successfully compiled!")


if __name__ == "__main__":
    main()
