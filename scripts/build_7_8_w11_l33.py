#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_7_8_w11_l33.py — Builder for 7–8th Grade, Week 11, Lesson 33

Loyiha: Shadow Dungeon 2D: Kiber-Qasr O'yin Loyihasi (To'liq O'ynaladigan Roguelike O'yini)
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 7-8-sinf (Vibecoding & Game Dev Track)
Pedagogika: ANIQ LOYIHA SINTEZI & VIBECODING — O'quvchilar 10-11-haftalarda o'rgangan
             barcha geym-dizayn elementlarini (Labirint, Mash'ala nuri, Kiber-blaster,
             Xazina qutilari va G'alaba portali) bitta yaxlit "Shadow Dungeon" o'yiniga
             birlashtiradilar. Quruq nazariya yo'q, faqat amaliy o'yin yaratish!
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "7-8-sinf", "11-hafta", "33-dars-shadow-dungeon-kiber-qasr")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "simulator"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides — Concrete Project: Shadow Dungeon 2D)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="7–8-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 33" data-en="GRADES 7–8 · WEEK 11 · LESSON 33">7–8-SINF · 11-HAFTA · 33-DARS</span></div>
    <h1 class="display" data-ru="Shadow Dungeon 2D: Создаем Свою Игру Roguelike в Кибер-Замке" data-en="Shadow Dungeon 2D: Engineering a Complete Roguelike Game">Shadow Dungeon: O'z Kiber-Qasringni Qur!</h1>
    <p class="lede" data-ru="Объединяем все изученные механики в одну полноценную захватывающую игру: лабиринт подземелья, свет факела, лазерный бластер, золотые сундуки и портал победы через Vibecoding!" data-en="Uniting all learned mechanics into one complete thrilling game: dungeon maze, torch light, laser blaster, gold chests, and victory portal via Vibecoding!">O'tgan darslarda o'rgangan barcha qismlarni (Labirint, qorong'u mash'ala nuri, lazer blastersi va xazina qutilari) bitta yaxlit, to'liq o'ynaladigan "Shadow Dungeon" o'yiniga jamlaymiz!</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Конкретный Игровой Проект" data-en="Concrete Game Project">Aniq O'yin Loyihasi</h3>
        <p data-ru="Никакой сухой теории: строим готовую игру Shadow Dungeon 2D, в которую можно сразу играть с друзьями." data-en="Zero abstract theory: build a complete playable Shadow Dungeon 2D game to play with friends.">Ortiqcha nazariyasiz: partadoshingiz bilan darhol musobaqalashish mumkin bo'lgan to'liq Shadow Dungeon 2D o'yinini quramiz.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Playable Game Project</div>
        <h3 data-ru="Готовая Игра в Браузере" data-en="Complete Browser Game">To'liq O'yin Dvigateli</h3>
        <p data-ru="Каждый ученик создаст свой замок с сундуками, факелом и порталом выхода." data-en="Every student completes their own castle with chests, torchlight, and exit portal.">Har bir o'quvchi o'zining sirli qasri, mash'alasi, 3 ta xazinasi va chiqish portaliga ega bo'ladi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW & BRIDGE -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="РАЗБОР ДОМАШНЕГО ЗАДАНИЯ И МОСТ" data-en="HOMEWORK REVIEW & BRIDGE">UY VAZIFASI TAHLILI VA KO'PRIK</span></div>
    <h2 data-ru="Ошибки Стрельбы и Мост к Единому Проекту" data-en="Shooting Pitfalls & Bridge to Unified Project">32-Dars Otishma Tahlili va Bugungi Katta Loyihaga Ko'prik</h2>
    <div class="grid-2">
      <div>
        <div class="box" style="border-left:4px solid var(--accent); margin-bottom:12px;">
          <h4 data-ru="Главная ловушка: Бесконечные пули" data-en="Major Pitfall: Infinite Bullets Lag">Eng Katta Xato: Cheksiz O'qlar va O'yin Qotishi</h4>
          <p style="font-size:12px;" data-ru="Ученики создавали массив пуль, но забывали удалять снаряды за пределами экрана. Браузер зависал от 10,000 пуль!" data-en="Students added bullets but forgot cleanup. 10,000 off-screen bullets lagged the browser!">O'quvchilar ekrandan chiqib ketgan o'qlarni massivdan o'chirishni unutishgan. Natijada yuzlab o'qlar to'planib o'yin qotgan!</p>
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
          <p style="font-size:13px; font-weight:600; margin:6px 0;" data-ru="Сетка есть, факел есть, бластер стреляет. Чего не хватает для НАСТОЯЩЕЙ игры?" data-en="We have a grid, torch, and blaster. What is missing for a REAL game?">Kataklar bor, mash'ala bor, blaster otyapti. Haqiqiy o'yin bo'lishi uchun nima yetishmayapti?</p>
          <p style="font-size:12px; color:var(--green); font-weight:700;" data-ru="👉 Ответ: Цели! Сундуков с золотом и портала победы!" data-en="👉 Answer: An objective! Gold chests and a victory portal!">👉 Javob: Aniq Maqsad! Xazina qutilari, kalitlar va g'alaba portali!</p>
        </div>
        <div class="box" style="border-left:4px solid var(--purple);">
          <h4 data-ru="Мост к сегодняшней теме" data-en="Bridge to Today's Project">Bugungi Loyihaga Ko'prik</h4>
          <p style="font-size:12px;" data-ru="Сегодня мы соберем все части головоломки воедино и создадим полноценную игру Shadow Dungeon 2D!" data-en="Today we assemble all pieces of the puzzle into one complete playable Shadow Dungeon 2D game!">Bugun barcha qismlarni bitta qutiga solib, do'stlaringiz bilan o'ynaydigan haqiqiy 'Shadow Dungeon' o'yinini yaratasiz!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: 4 PILLARS OF SHADOW DUNGEON -->
  <section class="slide" data-phase="O'yin Arxitekturasi|Архитектура Игры|Game Architecture" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="4 СТОЛПА ИГРЫ SHADOW DUNGEON" data-en="4 PILLARS OF SHADOW DUNGEON">O'YIN LOYIHASI ARXITEKTURASI</span></div>
    <h2 data-ru="4 Столпа Игры: Что Делает Shadow Dungeon Захватывающей?" data-en="4 Core Pillars: What Makes Shadow Dungeon Addictive?">Shadow Dungeon O'yinining 4 Ta Asosiy Ustuni</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Каждая великая игра состоит из 4 базовых игровых систем:" data-en="Every great game consists of 4 foundational gameplay systems:">Har bir qiziqarli o'yin 4 ta asosiy mustahkam ustundan tashkil topadi:</p>
        <ul class="clean-list">
          <li data-ru="<strong>1. Лабиринт (Карта):</strong> Каменные стены и коридоры замка." data-en="<strong>1. The Maze (Map):</strong> Solid stone walls and dungeon corridors."><strong>1. Tosh Qasr (Labirint):</strong> 20x13 katakli qadimiy qasr koridorlari.</li>
          <li data-ru="<strong>2. Факел (Атмосфера):</strong> Видимость только вокруг героя в радиусе 140px." data-en="<strong>2. The Torch (Mood):</strong> Smooth radial lighting within 140px around hero."><strong>2. Mash'ala (Atmosfera):</strong> Qahramon atrofidagi 140px radial yorug'lik.</li>
          <li data-ru="<strong>3. Бластер (Действие):</strong> Стрельба во все стороны с искрами от стен." data-en="<strong>3. The Blaster (Action):</strong> 360-degree aiming and spark bursts upon impact."><strong>3. Kiber-Blaster (Otishma):</strong> Kursor tomon otish va devorga uchqunlar.</li>
          <li data-ru="<strong>4. Цель (Победа):</strong> 3 сундука с сокровищами и портал выхода!" data-en="<strong>4. The Goal (Victory):</strong> 3 hidden gold chests and an active exit portal!"><strong>4. O'yin Maqsadi (G'alaba):</strong> 3 ta xazina qutisi va chiqish portali!</li>
        </ul>
      </div>
      <div>
        <div class="box" style="text-align:center; padding:16px; background:var(--panel);">
          <div style="font-size:44px; margin-bottom:8px;">🏰 🔦 ⚡ 📦</div>
          <h3 data-ru="Формула Захватывающего Roguelike" data-en="Addictive Roguelike Formula">To'liq O'yin Sintezi</h3>
          <p style="font-size:12px; color:var(--ink-2);" data-ru="Когда все 4 системы работают вместе, простая веб-страница превращается в настоящую коммерческую инди-игру!" data-en="When all 4 systems interact harmoniously, a simple webpage becomes an authentic indie game!">Barcha 4 tizim bir-biriga ulanganda oddiy sahifa haqiqiy zavqli mustaqil o'yinga aylanadi!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: PILLAR 1 - THE MAZE -->
  <section class="slide" data-phase="1-Ustun: Qasr|1-Столп: Замок|Pillar 1: Maze" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="1-Й СТОЛП: КАРТА И ЛАБИРИНТ" data-en="PILLAR 1: DUNGEON MAZE">1-USTUN: TOSH LABIRINT</span></div>
    <h2 data-ru="1-й Столп: Сетка Лабиринта и Столкновения со Стенами" data-en="Pillar 1: Maze Grid & Solid Wall Collisions">1-Ustun: Qorong'u Labirint va Tosh Devorlar</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Игровое поле делится на сетку 20 на 13 квадратных блоков (тайлов):" data-en="The game arena is partitioned into a 20 by 13 tile grid:">O'yin maydoni 20x13 katakli shaxmat doskasiga o'xshaydi:</p>
        <ul class="clean-list">
          <li data-ru="<strong>🟩 Пол (0):</strong> Свободные коридоры замка, где герой ходит на стрелки или WASD." data-en="<strong>🟩 Floor (0):</strong> Open dungeon corridors navigated via arrows or WASD."><strong>🟩 Bo'sh pol:</strong> Qahramon strelkalar yoki WASD bilan erkin yuradi.</li>
          <li data-ru="<strong>⬛ Стены (1):</strong> Непробиваемые каменные блоки — герой не может пройти сквозь них." data-en="<strong>⬛ Walls (1):</strong> Solid stone blocks — hero cannot clip through them."><strong>⬛ Tosh devorlar:</strong> O'tib bo'lmaydigan qattiq to'siqlar.</li>
          <li data-ru="<strong>Плавное скольжение:</strong> Если нажать влево у стены, герой скользит вдоль нее." data-en="<strong>Smooth Sliding:</strong> If hero presses diagonally, it slides along obstacles."><strong>Silliq sirg'anish:</strong> Devorga urilganda qotib qolmasdan yonlab sirg'aladi.</li>
        </ul>
      </div>
      <div>
        <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); padding:14px; font-family:var(--font-mono); font-size:12px;">
          <div style="color:var(--accent); font-weight:700; margin-bottom:6px;">// To'siqlar tekshiruvi (Collision Check)</div>
          <div style="color:#cbd5e1; line-height:1.5;">
            const nextX = hero.x + dx;<br>
            const nextY = hero.y + dy;<br>
            <span style="color:var(--green);">// Agar oldinda bo'sh pol bo'lsa, qadam bosamiz:</span><br>
            if (isWalkable(nextX, nextY)) {<br>
            &nbsp;&nbsp;hero.x = nextX;<br>
            &nbsp;&nbsp;hero.y = nextY;<br>
            }
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: PILLAR 2 - THE TORCH -->
  <section class="slide" data-phase="2-Ustun: Mash'ala|2-Столп: Факел|Pillar 2: Torch" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="2-Й СТОЛП: СВЕТ И АТМОСФЕРА" data-en="PILLAR 2: TORCHLIGHT">2-USTUN: MASH'ALA NURI</span></div>
    <h2 data-ru="2-й Столп: Свет Факела и Тайна Подземелья" data-en="Pillar 2: Dynamic Torchlight & Dungeon Atmosphere">2-Ustun: Qorong'ilik va Mash'ala Nuri</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Почему полностью освещенная комната скучна? Потому что в ней нет тайны!" data-en="Why is a fully lit room boring? Because there is no mystery!">Nega butun ekran yorug' bo'lsa o'yin zerikarli? Chunki kutilmagan sirlar bo'lmaydi!</p>
        <ul class="clean-list">
          <li data-ru="<strong>Радиальный свет:</strong> Вокруг героя горит факел радиусом 140 пикселей." data-en="<strong>Radial Light:</strong> A warm torch radius of 140px illuminates hero's surroundings."><strong>Radial yorug'lik:</strong> Qahramon atrofida 140px radiusli mash'ala yonadi.</li>
          <li data-ru="<strong>Мягкие края:</strong> Свет плавно затухает от золотистого к полной тьме." data-en="<strong>Soft Feathering:</strong> Light smoothly falls off from warm amber to pitch black."><strong>Silliq chekkalar:</strong> Markazda yorug', chetida esa sirli qorong'ilik.</li>
          <li data-ru="<strong>Эффект неожиданности:</strong> Сундук или выход нельзя увидеть, пока не подойдешь близко!" data-en="<strong>Suspense:</strong> Chests and exits remain hidden until you explore nearby!"><strong>Kutilmagan kashfiyot:</strong> Quti yoki portalga yaqinlashmaguncha uni ko'rib bo'lmaydi!</li>
        </ul>
      </div>
      <div>
        <div class="box" style="border-left:4px solid var(--amber); background:var(--panel);">
          <h4 data-ru="Как работает магия холста (Canvas Context):" data-en="Canvas Flashlight Magic:">Canvas Mash'ala Texnologiyasi:</h4>
          <p style="font-size:12px; color:var(--ink-2); line-height:1.5;" data-ru="1. Заливаем холст черной тьмой.<br>2. Создаем радиальный градиент вокруг героя.<br>3. Прорезаем свет через destination-out!" data-en="1. Fill canvas with dark shadow.<br>2. Create radial gradient around hero.<br>3. Carve light cutout via destination-out!">
            1. Butun ekranni to'q qora rang bilan bo'yaymiz.<br>
            2. Qahramon turgan joyda <code>createRadialGradient</code> yaratamiz.<br>
            3. <code>globalCompositeOperation = 'destination-out'</code> bilan qorong'ulikni teshik ochib yoritamiz!
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: PILLAR 3 - BLASTER & PARTICLES -->
  <section class="slide" data-phase="3-Ustun: Blaster|3-Столп: Бластер|Pillar 3: Blaster" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="3-Й СТОЛП: ДИНАМИКА И ВЫСТРЕЛЫ" data-en="PILLAR 3: BLASTER ACTION">3-USTUN: KIBER-BLASTER</span></div>
    <h2 data-ru="3-й Столп: Стрельба во Все Стороны и Искры от Стен" data-en="Pillar 3: 360° Blaster Shooting & Spark Particles">3-Ustun: Kiber-Blaster va Rangli Uchqunlar</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Игрок целится мышкой и выпускает лазерные снаряды по клику:" data-en="Player aims with mouse crosshair and unleashes laser bolts on click:">O'yinchi kursor bilan nishonga oladi va sichqoncha bilan lazer otadi:</p>
        <ul class="clean-list">
          <li data-ru="<strong>Прицеливание 360°:</strong> Пуля летит ровно туда, куда указывает курсор мыши." data-en="<strong>360° Aiming:</strong> The projectile travels precisely towards mouse cursor."><strong>360° Erkin nishon:</strong> O'q sichqoncha turgan aniq yo'nalishga uchadi.</li>
          <li data-ru="<strong>Взрыв искр:</strong> При ударе о каменную стену пуля взрывается 6–8 искрами!" data-en="<strong>Spark Bursts:</strong> Hitting stone obstacles creates 6–8 fiery sparks!"><strong>Uchqunlar portlashi:</strong> Devorga urilganda 6–8 ta yorqin zarracha sochiladi!</li>
          <li data-ru="<strong>Отдача:</strong> Легкий толчок героя при выстреле делает стрельбу сочной!" data-en="<strong>Gun Recoil:</strong> Subtle recoil kickback gives weapon punchy game-feel!"><strong>Qurol zarbasi:</strong> Otganda qahramonning biroz siljishi o'yinni yoqimli qiladi!</li>
        </ul>
      </div>
      <div>
        <div class="box" style="border-left:4px solid var(--accent); background:var(--panel);">
          <div style="font-size:36px; margin-bottom:6px;">💥 ⚡ ✨</div>
          <h4 data-ru="Игровой Сок (Game Juice)" data-en="Game Juice Polish">O'yin Zavqi (Game Juice)</h4>
          <p style="font-size:12px; color:var(--ink-2);" data-ru="Без искр игра ощущается плоской. Добавив частицы и вспышки, мы делаем стрельбу захватывающей!" data-en="Without particles, combat feels dull. Sparks and flashes transform basic shooting into addictive action!">Uchqunlarsiz otishma zerikarli ko'rinadi. Rangli zarrachalar va yorug'lik o'yinni haqiqiy arkadaga aylantiradi!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: PILLAR 4 - OBJECTIVES & PORTAL -->
  <section class="slide" data-phase="4-Ustun: G'alaba|4-Столп: Победа|Pillar 4: Victory" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="4-Й СТОЛП: ЦЕЛЬ И ФИНИШ" data-en="PILLAR 4: MISSION GOAL">4-USTUN: O'YIN MAQSADI</span></div>
    <h2 data-ru="4-й Столп: 3 Золотых Сундука и Портал Победы" data-en="Pillar 4: 3 Gold Chests & The Victory Exit Portal">4-Ustun: 3 Ta Oltin Quti va Chiqish Portali</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid #f59e0b;">
        <div style="font-size:32px; margin-bottom:6px;">📦</div>
        <h4 data-ru="3 Сундука" data-en="3 Gold Chests">1. Xazina Qutilari</h4>
        <p style="font-size:12px;" data-ru="3 сундука спрятаны в дальних углах замка. Подойди к ним вплотную, чтобы забрать золотой ключ!" data-en="3 chests hidden in far corners. Step onto them to pick up the golden keys!">Qasrning chekka burchaklariga 3 ta oltin quti yashiringan. Ularga yaqinlashib oching!</p>
      </div>
      <div class="box" style="border-top:4px solid #3b82f6;">
        <div style="font-size:32px; margin-bottom:6px;">🔑</div>
        <h4 data-ru="Счетчик Ключей" data-en="Key Counter">2. Kalitlar Hisobi</h4>
        <p style="font-size:12px;" data-ru="В верхнем углу горит HUD: 'Ключи: 0/3'. Портал выхода заперт, пока вы не найдете все три ключа!" data-en="Top HUD displays: 'Keys: 0/3'. The exit portal remains sealed until all 3 keys are collected!">Ekranning yuqorisida 'Kalitlar: 0/3' hisobi turadi. 3 ta kalit topilmaguncha portal ochilmaydi!</p>
      </div>
      <div class="box" style="border-top:4px solid #10b981;">
        <div style="font-size:32px; margin-bottom:6px;">🌀</div>
        <h4 data-ru="Портал Победы" data-en="Victory Portal">3. Chiqish Portali</h4>
        <p style="font-size:12px;" data-ru="Как только собраны 3 ключа, портал вспыхивает изумрудным светом! Доберись до него и выиграй игру!" data-en="Once 3 keys are found, portal flashes emerald green! Step inside to win the game!">3 ta kalit to'planishi bilan portal yashil bo'lib ochiladi! Unga kirgan o'yinchi g'alaba qozonadi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: IN-DECK INTERACTIVE GAME -->
  <section class="slide" data-phase="Jonli O'yin|Игра на Доске|Playable Game" data-time="40:00–48:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ЖИВАЯ ИГРА НА СМАРТБОРДЕ" data-en="SMARTBOARD LIVE GAMEPLAY">SMARTBOARDDA JONLI O'YIN</span></div>
    <h2 data-ru="Сыграйте в Shadow Dungeon Прямо Сейчас!" data-en="Play Shadow Dungeon 2D Right on the Screen!">Doskada 'Shadow Dungeon 2D' O'yinini O'ynab Ko'ring!</h2>
    <p class="lede" style="font-size:13px; margin-bottom:8px;" data-ru="Двигайте героя стрелками или WASD. Стреляйте кликом мыши. Найдите 3 сундука (📦) и дойдите до портала (🌀)!" data-en="Move hero with arrows or WASD. Shoot via mouse click. Collect 3 chests (📦) and enter the portal (🌀)!">Strelkalar bilan qahramonni boshqaring. Sichqoncha bilan o'q uzing. 3 ta qutini (📦) toping va portalga (🌀) kiring!</p>
    
    <div style="background:#090d16; border:1px solid rgba(255,255,255,0.15); border-radius:8px; padding:10px; display:flex; flex-direction:column; align-items:center;">
      <div style="display:flex; justify-content:space-between; width:100%; max-width:620px; margin-bottom:6px; font-family:var(--font-mono); font-size:12px;">
        <span style="color:#f59e0b; font-weight:700;">📦 Xazinalar: <span id="deck-keys">0</span>/3</span>
        <span style="color:#38bdf8; font-weight:700;">❤️ Jon: <span id="deck-hp">3</span></span>
        <button id="deck-btn-restart" class="btn" style="padding:2px 8px; font-size:11px; background:#334155; color:#fff;" data-ru="🔄 Перезапуск" data-en="🔄 Restart">🔄 Qayta Boshlash</button>
      </div>
      <canvas id="deck-shadow-canvas" width="620" height="260" style="border:2px solid #334155; border-radius:6px; cursor:crosshair; background:#020617; touch-action:none;"></canvas>
      <div style="font-size:11px; color:#94a3b8; margin-top:6px;">
        ⌨️ <b>Strelkalar / WASD</b>: Harakat | 🖱️ <b>Klik</b>: Lazer Otish | 📦 <b>Xazinalar</b>: Kalitlar | 🌀 <b>Portal</b>: Chiqish
      </div>
    </div>
  </section>

  <!-- SLIDE 9: GAMER QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Quiz" data-time="48:00–55:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА ИНТУИЦИИ ГЕЙМДЕВА" data-en="GAMEDEV INTUITION CHECK">GEYM-DIZAYNERLAR SAVOLLARI</span></div>
    <h2 data-ru="3 Вопроса: Как Устроен Твой Shadow Dungeon?" data-en="3 Questions: How Does Shadow Dungeon Work?">Shadow Dungeon Bo'yicha 3 Ta Tezkor Savol</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:#dbeafe; color:#1e40af;">1-Savol</div>
        <h4 data-ru="Зачем нужен факел тьмы?" data-en="Why add dark torchlight?">Nega qorong'u mash'ala o'yinni qiziqarli qiladi?</h4>
        <div class="interactive-opt" onclick="this.classList.toggle('selected');" style="margin-top:8px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">A) Chunki o'yinchining ko'zi og'rimasligi uchun</div>
        <div class="interactive-opt correct-opt" onclick="this.classList.toggle('selected');" style="margin-top:4px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">B) Chunki kutilmagan qutilar va xavflar sirli qoladi</div>
      </div>
      <div class="box">
        <div class="tag" style="background:#fef3c7; color:#92400e;">2-Savol</div>
        <h4 data-ru="Что происходит с пулей при ударе о стену?" data-en="What happens when a bullet hits a wall?">O'q tosh devorga tekkanda nima sodir bo'lishi kerak?</h4>
        <div class="interactive-opt correct-opt" onclick="this.classList.toggle('selected');" style="margin-top:8px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">A) O'q o'chiriladi va rangli uchqunlar sochiladi</div>
        <div class="interactive-opt" onclick="this.classList.toggle('selected');" style="margin-top:4px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">B) O'q devorni teshib narigi tomonga o'tib ketadi</div>
      </div>
      <div class="box">
        <div class="tag" style="background:#fee2e2; color:#991b1b;">3-Savol</div>
        <h4 data-ru="Как открывается портал победы?" data-en="How does the victory portal open?">Chiqish portali qachon faollashadi?</h4>
        <div class="interactive-opt correct-opt" onclick="this.classList.toggle('selected');" style="margin-top:8px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">A) Qasr bo'ylab yashiringan 3 ta xazina qutisi ochilganda</div>
        <div class="interactive-opt" onclick="this.classList.toggle('selected');" style="margin-top:4px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">B) O'yin boshlanishi bilan ochiq turadi</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: VIBECODING PROMPTING LAB -->
  <section class="slide" data-phase="Amaliy Arena|Практическая Арена|Hands-on Arena" data-time="55:00–70:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ПОШАГОВЫЙ VIBECODING В ДЕЛЕ" data-en="STEP-BY-STEP VIBECODING">VIBECODING: 4 BOSQICHDA O'YIN YIG'ISH</span></div>
    <h2 data-ru="Vibecoding: 4 Точных Промпта для Сборки Shadow Dungeon" data-en="Vibecoding: 4 Precision Prompts to Build Shadow Dungeon">AI ga 4 Bosqichda Aniq So'rov Berib O'yinni Yaratamiz!</h2>
    <div class="grid-2">
      <div>
        <div class="box" style="margin-bottom:8px; border-left:4px solid #3b82f6;">
          <div style="font-weight:700; font-size:11px; color:#2563eb;">1-BOSQICH: Qasr Labirinti va Qahramon (Baza)</div>
          <p style="font-size:11px; margin:4px 0; color:var(--ink-2); font-style:italic;" data-ru="«Создай Canvas-игру 620x260 со стенами лабиринта 20x13. Добавь синего героя, который ходит на стрелки/WASD и упирается в стены без застревания.»" data-en="«Create a 620x260 Canvas game with a 20x13 maze grid. Add a blue hero moving via arrows/WASD with solid obstacle collisions.»">"Mening Canvas loyihamga 20x13 o'lchamli tosh qasr labirinti va strelkalar/WASD bilan yuruvchi qahramonni bog'la. Qahramon devorlardan o'tib ketmasin."</p>
        </div>
        <div class="box" style="border-left:4px solid #f59e0b;">
          <div style="font-weight:700; font-size:11px; color:#d97706;">2-BOSQICH: Mash'ala Yorug'ligi (Torchlight)</div>
          <p style="font-size:11px; margin:4px 0; color:var(--ink-2); font-style:italic;" data-ru="«Добавь эффект тьмы: весь экран черный, но вокруг героя светит радиальный факел радиусом 140px с золотистым градиентом через destination-out.»" data-en="«Add darkness: screen is black, but a 140px warm torch radius illuminates around hero via destination-out radial gradient.»">"Qahramon atrofiga 140px radial mash'ala yorug'ligini qo'sh. U faqat o'yinchi atrofini ko'rsatsin, qolgan joylar qorong'i bo'lsin."</p>
        </div>
      </div>
      <div>
        <div class="box" style="margin-bottom:8px; border-left:4px solid #ef4444;">
          <div style="font-weight:700; font-size:11px; color:#dc2626;">3-BOSQICH: Kiber-Blaster va Uchqunlar</div>
          <p style="font-size:11px; margin:4px 0; color:var(--ink-2); font-style:italic;" data-ru="«При клике мышкой выпускай лазерный снаряд в сторону курсора. При ударе о стену удаляй пулю и создавай 6 цветных искр.»" data-en="«On mouse click, fire a laser projectile towards cursor. On wall hit, remove bullet and spawn 6 colorful spark particles.»">"Sichqoncha bosilganda kursor tomon lazer o'qi otilsin. O'q devorga tekkanda o'chsin va 6 ta yorqin zarracha uchqun sochilsin."</p>
        </div>
        <div class="box" style="border-left:4px solid #10b981;">
          <div style="font-weight:700; font-size:11px; color:#059669;">4-BOSQICH: 3 Ta Xazina va Chiqish Portali</div>
          <p style="font-size:11px; margin:4px 0; color:var(--ink-2); font-style:italic;" data-ru="«Размести на карте 3 золотых сундука. При их сборе открывай зеленый портал выхода. При входе в портал показывай экран ПОБЕДА!»" data-en="«Scatter 3 gold chests. Collecting them unlocks an emerald exit portal. Entering portal displays VICTORY screen!»">"Labirint burchaklariga 3 ta oltin quti qo'sh. 3 ta quti ochilganda yashil Chiqish Portali yonsin va unga kirganda G'ALABA ekrani chiqsin!"</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: PEER REVIEW PLAYTEST -->
  <section class="slide" data-phase="Partadosh Auditi|Взаимный Аудит|Peer Review" data-time="70:00–74:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ТЕСТИРОВАНИЕ ИГРЫ ДРУГА" data-en="PEER PLAYTESTING">PARTADOSH DUELOSI</span></div>
    <h2 data-ru="Баттл Замков: Найди Все Сундуки в Игре Друга!" data-en="Castle Battle: Find All Chests in Peer's Game!">Partadosh Duelosy: Do'stingning Qasridan Omon Chiq!</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Поменяйтесь местами с соседом по парте! Сыграйте в его Shadow Dungeon и проверьте 4 вещи:" data-en="Swap seats with your classmate! Play their Shadow Dungeon and check 4 things:">Partadoshingiz bilan joyingizni almashtiring! Uning o'yinini o'ynab, 4 ta mezon bo'yicha baholang:</p>
        <ul class="clean-list">
          <li data-ru="<strong>1. Управление:</strong> Легко ли управлять героем? Не застревает ли он в углах?" data-en="<strong>1. Controls:</strong> Are controls responsive? Does hero glide around corners?"><strong>1. Boshqaruv:</strong> Qahramon devorlarga tiqilmay silliq yuryaptimi?</li>
          <li data-ru="<strong>2. Факел:</strong> Видны ли коридоры? Достаточно ли света?" data-en="<strong>2. Torchlight:</strong> Is torch visibility comfortable and atmospheric?"><strong>2. Mash'ala:</strong> Yorug'lik yetarlimi, atmosfera qiziqarlimi?</li>
          <li data-ru="<strong>3. Стрельба:</strong> Летят ли искры при попадании в стену?" data-en="<strong>3. Blaster:</strong> Do spark particles burst upon obstacle impact?"><strong>3. Blaster:</strong> Devorga tekkanda chiroyli uchqunlar sochilyaptimi?</li>
          <li data-ru="<strong>4. Финал:</strong> Открывается ли портал после сбора 3 сундуков?" data-en="<strong>4. Win State:</strong> Does the emerald portal unlock after 3 chests?"><strong>4. G'alaba:</strong> 3 ta qutidan keyin portal ochilib g'alaba beryaptimi?</li>
        </ul>
      </div>
      <div>
        <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); margin-bottom:12px;">
          <div style="color:var(--accent); font-weight:700; font-size:12px; margin-bottom:6px;">🛠️ Agar xato topsangiz (Bag ovlash):</div>
          <p style="font-size:12px; color:#cbd5e1; margin:0;" data-ru="Сразу отправьте ИИ уточняющий запрос (Critic prompt):" data-en="Immediately send AI this critic bug-fix prompt:">AI ga darhol quyidagi tuzatish so'rovini (Critic prompt) bering:</p>
          <p style="margin-top:6px; font-size:11px; color:var(--yellow); font-family:var(--font-mono);" data-ru="«Сундуки должны исчезать после касания, а счетчик ключей на экране должен увеличиваться на +1.»" data-en="«Chests must disappear upon hero touch, and the HUD key counter must increment +1.»">"Qutilarga tegilganda ular yo'qolib ekrandagi kalitlar hisobi +1 ga oshsin va 3 ta bo'lganda portal yonsin!"</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: BIG SCREEN SHOWCASE -->
  <section class="slide" data-phase="Katta Ekran|Шоукейс|Showcase" data-time="74:00–77:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ШОУКЕЙС НА БОЛЬШОМ ЭКРАНЕ" data-en="BIG SCREEN SHOWCASE">KATTA EKRAN SHOWCASE</span></div>
    <h2 data-ru="Шоукейс: Прохождение Замков на Большом Смартборде!" data-en="Showcase: Conquering Castles on the Big Display!">Katta Doskada Eng Zo'r 'Shadow Dungeon' Namoyishi!</h2>
    <div class="grid-2">
      <div>
        <div class="box" style="margin-bottom:12px;">
          <div class="tag" style="background:#dcfce7; color:#166534;" data-ru="Лучшие Проекты" data-en="Top Projects">2 Ta Eng Zo'r O'yin</div>
          <p style="font-size:13px; font-weight:600; margin:6px 0;" data-ru="Два ученика с самым сочным геймплеем и атмосферой выходят к доске!" data-en="Two students with the juiciest gameplay and mood showcase on the big screen!">Eng chiroyli mash'ala va silliq otishma yaratgan 2 nafar o'quvchi doskaga chiqib o'z qasrini namoyish qiladi!</p>
        </div>
        <ul class="clean-list">
          <li data-ru="У кого самая крутая анимация искр при стрельбе?" data-en="Who engineered the coolest spark particle effects?">Kimning lazer blastersi eng chiroyli uchqunlarga ega?</li>
          <li data-ru="Кто спрятал сундуки в самых хитрых уголках замка?" data-en="Who hid the chests in the most challenging secret spots?">Kim qutilarni eng sirli va qiziqarli burchaklarga yashirdi?</li>
          <li data-ru="Сможет ли учитель найти выход из вашего замка за 60 секунд?" data-en="Can the teacher find the exit portal in under 60 seconds?">O'qituvchi sizning qasringizdan 60 soniyada chiqib keta oladimi?</li>
        </ul>
      </div>
      <div>
        <div class="box" style="text-align:center; padding:24px; background:var(--panel);">
          <div style="font-size:48px; margin-bottom:12px;">🏆</div>
          <h3 data-ru="Звание Лучшего Инди-Разработчика" data-en="Master Indie Game Dev">"Kiber-Qasr Me'mori" G'olibi</h3>
          <p style="font-size:12px; color:var(--ink-2);" data-ru="Ученик, создавший самую сбалансированную и красивую игру, получает 10 баллов и аплодисменты класса!" data-en="The student with the most polished and balanced dungeon wins 10 points!">Eng qiziqarli va silliq o'yin yaratgan o'quvchi eng yuqori 10 ballni qo'lga kiritadi!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: 3-TIER HOMEWORK -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Homework" data-time="77:00–79:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ДОМАШНЕЕ ЗАДАНИЕ (10 БАЛЛОВ)" data-en="HOMEWORK CHALLENGE (10 POINTS)">UYGA KIBER-VAZIFA</span></div>
    <h2 data-ru="3 Уровня: От Базового Замка к Эпической Игре" data-en="3 Tiers: From Core Dungeon to Epic Game">3 Darajali Shadow Dungeon Vazifasi (10 Ball)</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid #3b82f6;">
        <div class="tag" style="background:#e0f2fe; color:#0369a1;">1-Daraja: Baza (4 ball)</div>
        <h4 data-ru="Лабиринт и Факел" data-en="Maze & Torchlight">Labirint va Mash'ala</h4>
        <p style="font-size:12px;" data-ru="Объедините сетку замка, движение героя на стрелки и круг света фонарика." data-en="Unite dungeon maze grid, hero arrow controls, and radial torchlight.">Qasr xaritasi, strelkalar bilan harakat va qahramon atrofidagi mash'ala nurini to'liq bog'lang.</p>
      </div>
      <div class="box" style="border-top:4px solid #10b981;">
        <div class="tag" style="background:#dcfce7; color:#15803d;">2-Daraja: Muhandis (4 ball)</div>
        <h4 data-ru="Бластер и 3 Сундука" data-en="Blaster & 3 Chests">Blaster va 3 Ta Xazina</h4>
        <p style="font-size:12px;" data-ru="Добавьте стрельбу искрами и 3 золотых сундука, открывающих портал выхода." data-en="Add mouse blaster with sparks and 3 chests unlocking the emerald portal.">Sichqoncha bilan lazer otish, uchqunlar va 3 ta qutini ochganda portal yonishini qo'shing.</p>
      </div>
      <div class="box" style="border-top:4px solid #8b5cf6;">
        <div class="tag" style="background:#f3e8ff; color:#6b21a8;">3-Daraja: Chempion (2 ball)</div>
        <h4 data-ru="Спец-Механика" data-en="Custom Mechanic">Shaxsiy Super-Imkoniyat</h4>
        <p style="font-size:12px;" data-ru="Добавьте звук победы, ускорение на пробел (Dash) или ядовитые шипы на полу!" data-en="Add victory audio, spacebar dash sprint, or floor spike hazards!">G'alaba audio ovozi, 'Space' bilan yugurish (Sprint) yoki sekinlashtiruvchi tikanlar qo'shing!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И СЛЕДУЮЩИЙ ШАГ" data-en="SUMMARY & WHAT'S NEXT">XULOSA VA KEYINGI BOSQICH</span></div>
    <h2 data-ru="Мы Создали Настоящую Игру! Что Дальше?" data-en="We Engineered a Real Game! What's Next?">Shadow Dungeon Tayyor: Bugun Nimalarga Erishdik?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Сегодня мы доказали, что умеем собирать полноценные игровые миры:" data-en="Today we proved we can engineer complete, cohesive game worlds:">Bugun alohida kichik kodlardan haqiqiy to'liq o'yin yaratishni o'rgandik:</p>
        <ul class="clean-list">
          <li data-ru="Объединили 4 игровых системы: карту, свет, стрельбу и финал!" data-en="United 4 core systems: map, lighting, shooting, and win condition!">4 ta asosiy tizimni jamladik: xarita, mash'ala, otishma va g'alaba portali!</li>
          <li data-ru="Научились давать ИИ точные пошаговые промпты без путаницы." data-en="Mastered giving AI precise, step-by-step modular prompts.">AI ga chalkashmasdan bosqichma-bosqich aniq so'rov berishni o'rgandik.</li>
          <li data-ru="Каждый уходит с урока с готовой игрой в своем портфолио!" data-en="Everyone leaves today with an authentic, playable portfolio game!">Har biringiz o'z portfoliangiz uchun to'liq ishlaydigan o'yinga ega bo'ldingiz!</li>
        </ul>
      </div>
      <div>
        <div class="box" style="border-left:4px solid var(--accent); background:var(--panel);">
          <div class="tag" style="background:var(--accent-soft); color:var(--accent);" data-ru="Анонс следующего уровня" data-en="Next Level Teaser">Keyingi 12-Hafta Ko'prigi</div>
          <h3 data-ru="В Лабиринте Просыпаются Монстры!" data-en="Monsters Awaken in the Dungeon!">Labirintda Yirtqich Dushmanlar Uyg'onadi!</h3>
          <p style="font-size:12px; color:var(--ink-2);" data-ru="Замок готов, факел горит, сундуки спрятаны. Но кого мы будем встречать в темных коридорах? В следующем модуле мы добавим в лабиринт умных монстров, которые охотятся на игрока!" data-en="The castle is built, torch burns bright, chests are hidden. But who awaits in the dark? Next module, we unleash cunning monsters that hunt the player!">Qasrimiz tayyor, mash'ala yonmoqda, xazinalar yashirilgan. Endi qorong'u yo'laklarda kimni uchratamiz? Keyingi bosqichda labirintga bizni ovlovchi yirtqich kiber-monstrlarni kiritamiz!</p>
        </div>
      </div>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. IN-DECK INTERACTIVE GAME JS (Playable Shadow Dungeon 2D)
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
(function() {
  const canvas = document.getElementById('deck-shadow-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  const COLS = 20;
  const ROWS = 9;
  const TILE = 28;

  let grid = [];
  function initGrid() {
    grid = [];
    for (let r = 0; r < ROWS; r++) {
      grid[r] = [];
      for (let c = 0; c < COLS; c++) {
        if (r === 0 || r === ROWS - 1 || c === 0 || c === COLS - 1) grid[r][c] = 1;
        else grid[r][c] = 0;
      }
    }
    // Maze walls
    for (let r = 2; r <= 6; r++) grid[r][5] = 1;
    for (let r = 2; r <= 6; r++) grid[r][11] = 1;
    grid[4][5] = 0; // doorway
    grid[4][11] = 0; // doorway
  }

  let hero = { x: 2, y: 4, hp: 3 };
  let chests = [
    { x: 2, y: 1, collected: false },
    { x: 8, y: 7, collected: false },
    { x: 17, y: 1, collected: false }
  ];
  let portal = { x: 18, y: 7, active: false };
  let bullets = [];
  let particles = [];
  let keysFound = 0;
  let gameWon = false;

  function resetGame() {
    initGrid();
    hero = { x: 2, y: 4, hp: 3 };
    chests = [
      { x: 2, y: 1, collected: false },
      { x: 8, y: 7, collected: false },
      { x: 17, y: 1, collected: false }
    ];
    portal = { x: 18, y: 7, active: false };
    bullets = [];
    particles = [];
    keysFound = 0;
    gameWon = false;
    updateHUD();
  }

  function updateHUD() {
    const kEl = document.getElementById('deck-keys');
    const hEl = document.getElementById('deck-hp');
    if (kEl) kEl.innerText = keysFound;
    if (hEl) hEl.innerText = hero.hp;
  }

  function shootBullet(targetX, targetY) {
    const startX = hero.x * TILE + 20 + TILE/2;
    const startY = hero.y * TILE + 4 + TILE/2;
    const dx = targetX - startX;
    const dy = targetY - startY;
    const angle = Math.atan2(dy, dx);
    bullets.push({
      x: startX,
      y: startY,
      vx: Math.cos(angle) * 7,
      vy: Math.sin(angle) * 7,
      dead: false
    });
  }

  function spawnSparks(x, y) {
    for (let i = 0; i < 7; i++) {
      const angle = Math.random() * Math.PI * 2;
      const speed = 1 + Math.random() * 3;
      particles.push({
        x: x, y: y,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed,
        life: 1.0,
        color: ['#fbbf24', '#f87171', '#38bdf8'][Math.floor(Math.random() * 3)]
      });
    }
  }

  function update() {
    // Bullets
    for (const b of bullets) {
      b.x += b.vx;
      b.y += b.vy;
      const c = Math.floor((b.x - 20) / TILE);
      const r = Math.floor((b.y - 4) / TILE);
      if (c < 0 || c >= COLS || r < 0 || r >= ROWS || grid[r][c] === 1) {
        b.dead = true;
        spawnSparks(b.x, b.y);
      }
    }
    bullets = bullets.filter(b => !b.dead);

    // Particles
    for (const p of particles) {
      p.x += p.vx;
      p.y += p.vy;
      p.life -= 0.04;
    }
    particles = particles.filter(p => p.life > 0);

    // Chest collision
    for (const ch of chests) {
      if (!ch.collected && ch.x === hero.x && ch.y === hero.y) {
        ch.collected = true;
        keysFound++;
        spawnSparks(hero.x * TILE + 20 + TILE/2, hero.y * TILE + 4 + TILE/2);
        if (keysFound === 3) portal.active = true;
        updateHUD();
      }
    }

    // Portal collision
    if (portal.active && portal.x === hero.x && portal.y === hero.y) {
      gameWon = true;
    }
  }

  function render() {
    update();

    ctx.fillStyle = '#020617';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw Map
    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        const x = c * TILE + 20;
        const y = r * TILE + 4;
        if (grid[r][c] === 1) {
          ctx.fillStyle = '#1e293b';
          ctx.fillRect(x, y, TILE - 2, TILE - 2);
          ctx.strokeStyle = '#334155';
          ctx.strokeRect(x, y, TILE - 2, TILE - 2);
        } else {
          ctx.fillStyle = '#090d16';
          ctx.fillRect(x, y, TILE - 2, TILE - 2);
        }
      }
    }

    // Draw Chests
    for (const ch of chests) {
      if (!ch.collected) {
        const cx = ch.x * TILE + 20 + TILE/2;
        const cy = ch.y * TILE + 4 + TILE/2;
        ctx.font = '16px sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('📦', cx, cy);
      }
    }

    // Draw Portal
    const ptx = portal.x * TILE + 20 + TILE/2;
    const pty = portal.y * TILE + 4 + TILE/2;
    ctx.font = '18px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(portal.active ? '🌀' : '🔒', ptx, pty);

    // Draw Bullets
    for (const b of bullets) {
      ctx.fillStyle = '#38bdf8';
      ctx.shadowColor = '#38bdf8';
      ctx.shadowBlur = 8;
      ctx.beginPath();
      ctx.arc(b.x, b.y, 4, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    // Draw Particles
    for (const p of particles) {
      ctx.fillStyle = p.color;
      ctx.globalAlpha = p.life;
      ctx.beginPath();
      ctx.arc(p.x, p.y, 2, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1.0;

    // Draw Hero
    const hx = hero.x * TILE + 20 + TILE/2;
    const hy = hero.y * TILE + 4 + TILE/2;
    ctx.fillStyle = '#3b82f6';
    ctx.beginPath();
    ctx.arc(hx, hy, TILE/2 - 2, 0, Math.PI * 2);
    ctx.fill();
    ctx.font = '14px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('🦸', hx, hy);

    // TORCHLIGHT MASK
    ctx.save();
    ctx.fillStyle = 'rgba(2, 6, 23, 0.88)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.globalCompositeOperation = 'destination-out';
    const grad = ctx.createRadialGradient(hx, hy, 20, hx, hy, 140);
    grad.addColorStop(0, 'rgba(0,0,0,1)');
    grad.addColorStop(0.7, 'rgba(0,0,0,0.85)');
    grad.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(hx, hy, 140, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();

    // VICTORY OVERLAY
    if (gameWon) {
      ctx.fillStyle = 'rgba(15, 23, 42, 0.92)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = '#4ade80';
      ctx.font = 'bold 22px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText("🎉 G'ALABA! QASRDAN OMON CHIQDINGIZ! 🎉", canvas.width/2, canvas.height/2 - 10);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '13px system-ui';
      ctx.fillText("3 ta oltin xazina to'liq yig'ildi va portal zabt etildi!", canvas.width/2, canvas.height/2 + 18);
    }

    requestAnimationFrame(render);
  }

  // Controls
  window.addEventListener('keydown', (e) => {
    let dx = 0, dy = 0;
    if (e.key === 'ArrowUp' || e.key === 'w') dy = -1;
    else if (e.key === 'ArrowDown' || e.key === 's') dy = 1;
    else if (e.key === 'ArrowLeft' || e.key === 'a') dx = -1;
    else if (e.key === 'ArrowRight' || e.key === 'd') dx = 1;
    else return;

    const nx = hero.x + dx;
    const ny = hero.y + dy;
    if (nx >= 0 && nx < COLS && ny >= 0 && ny < ROWS && grid[ny][nx] === 0) {
      hero.x = nx;
      hero.y = ny;
    }
  });

  canvas.addEventListener('click', (e) => {
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    shootBullet(x, y);
  });

  const btnReset = document.getElementById('deck-btn-restart');
  if (btnReset) btnReset.addEventListener('click', resetGame);

  resetGame();
  render();
})();
"""

# -----------------------------------------------------------------------------
# 3. TEACHER NOTES DATA (14 Slides Trilingual Triplets)
# -----------------------------------------------------------------------------
triplets_uz = [
    ["Kirish va Maqsad", "O'quvchilarga bugungi missiya: to'liq o'ynaladigan 'Shadow Dungeon 2D' kiber-qasr o'yinini yaratish ekanini ayting.", "Doskaga o'yinning 4 ta ustuni: Labirint, Mash'ala, Blaster, Portallarni chizing."],
    ["Uy Vazifasi Tahlili", "32-dars otishmasini eslang: o'qlarni massivdan tozalash va tosh devorga urilganda zarrachalar sochilishini ko'rsating.", "Oltin yechim: memory cleanup va game feel ekanini ta'kidlang."],
    ["O'yinning 4 Ustuni", "Haqiqiy o'yin qanday tuziladi: xarita, mash'ala, qurol va g'alaba shartini tushuntiring.", "O'quvchilarga savol bering: 'Nega maqsadsiz o'yin tez zeriktiradi?'"],
    ["1-Ustun: Labirint", "20x13 katakli qasr va devorlar bilan to'qnashuv mantig'ini ko'rsating.", "Qahramon tosh devordan o'tib ketmasligi shart ekanini ayting."],
    ["2-Ustun: Mash'ala", "Qorong'ulik nega o'yinni qiziq qiladi: radial gradient va destination-out sirlarini tushuntiring.", "Quti va portallar qorong'ida yashirinishi sarguzasht bag'ishlaydi."],
    ["3-Ustun: Blaster", "360 daraja sichqoncha bilan otish va devorga urilganda zarrachalar otilishini ko'rsating.", "Qurolning orqaga siljishi (recoil) o'yinga 'sharbat' bag'ishlaydi."],
    ["4-Ustun: Xazina va Portal", "3 ta quti yig'ilgandan keyingina portal ochilishini tushuntiring.", "HUD displeyida 'Kalitlar: 0/3' hisobini ko'rsating."],
    ["Smartboard Jonli O'yini", "8-slaydni oching: o'quvchilarni doskaga chaqirib 'Shadow Dungeon'ni o'ynating.", "Strelkalar bilan yuring, o'q uzing, 3 ta qutini topib portalga kiring!"],
    ["Geymerlar Viktorinasi", "3 ta tezkor savol orqali tushunchalarni mustahkamlang.", "To'g'ri javob bergan o'quvchilarni rag'batlantiring."],
    ["Vibecoding Arenasi", "O'quvchilarga 4 ta tayyor prompt kartasini ko'rsating va kompyuterlarida ishga tushirishlarini ayting.", "Zaldan aylanib o'yinini yig'ayotgan o'quvchilarga yordam bering."],
    ["Partadosh Duelosy", "Partadoshlar bir-birining qasrini o'ynab, kalitlarni qidirsin.", "Baglar aniqlansa, Critic prompt orqali tuzatishni o'rgating."],
    ["Katta Ekran Showcasi", "Eng chiroyli qasr yaratgan 2 nafar o'quvchini doskaga chaqirib namoyish qildiring.", "Butun sinf bilan birgalikda o'ynang."],
    ["Uyga Kiber-Vazifa", "10 ballik mezonni tushuntiring: labirint va mash'ala, blaster va 3 ta quti, maxsus qobiliyat.", "Vazifa ilovasida LocalStorage saqlanishini eslatib o'ting."],
    ["Xulosa va Keyingi Dars", "Bugun to'liq indie o'yin qurildi: har bir o'quvchi o'z portfolioga ega bo'ldi.", "Keyingi modulda labirintga yirtqich dushmanlar kirishini anons qiling."]
]

triplets_ru = [
    ["Введение и Цель", "Расскажите ученикам о миссии: собрать полноценную играбельную инди-игру 'Shadow Dungeon 2D'.", "Нарисуйте на доске 4 столпа игры: Лабиринт, Факел, Бластер, Портал."],
    ["Разбор ДЗ", "Вспомните 32-й урок: очистка массива пуль от утечки памяти и визуализация искр при ударе.", "Покажите золотой стандарт фильтрации и сочный геймплей."],
    ["4 Столпа Игры", "Объясните архитектуру: карта, факел, стрельба и цель победы.", "Спросите класс: 'Почему игра без цели быстро надоедает?'"],
    ["1-й Столп: Лабиринт", "Продемонстрируйте сетку 20x13 и механику столкновений со стенами подземелья.", "Герой должен плавно скользить вдоль препятствий."],
    ["2-й Столп: Факел", "Объясните атмосферу тьмы: радиальный градиент и вырезание света через destination-out.", "Сундуки скрыты во тьме, пока игрок не подойдет близко."],
    ["3-й Столп: Бластер", "Покажите механику стрельбы на 360 градусов и вспышки частиц от каменных стен.", "Отдача оружия добавляет сочности выстрелам."],
    ["4-й Столп: Портал", "Объясните условие победы: собрать 3 сундука, чтобы открыть изумрудный портал.", "Покажите счетчик ключей в верхнем углу."],
    ["Игра на Смартборде", "Откройте 8-й слайд: вызовите учеников к доске сыграть в готовую игру прямо на экране.", "Стреляйте кликом мыши, соберите 3 сундука и войдите в портал."],
    ["Геймерский Квиз", "Закрепите понятия через 3 интерактивных вопроса на слайде.", "Похвалите учеников за правильные ответы."],
    ["Vibecoding Арена", "Покажите 4 пошаговых промпта и запустите 30 минут работы за ПК.", "Проходите по рядам и помогайте интегрировать механики."],
    ["Взаимный Дуэльный Тест", "Ученики меняются местами и пробуют пройти замок соседа.", "Обучите отправлять Critic-промпты при обнаружении багов."],
    ["Шоукейс на Доске", "Вызовите двух авторов лучших замков на большой экран смартборда.", "Проведите живой турнир на скорость прохождения."],
    ["Домашнее Задание", "Объясните 10-балльную рубрику: лабиринт с факелом, бластер с сундуками, суперспособность.", "Напомните про автосохранение в приложении vazifa.html."],
    ["Итоги и Анонс", "Подведите итог: каждый создал готовую Roguelike-игру для портфолио.", "Анонсируйте появление монстров в подземелье на следующем модуле."]
]

triplets_en = [
    ["Intro & Mission", "Introduce the mission: engineering a complete, playable 'Shadow Dungeon 2D' indie game.", "Diagram the 4 pillars on the board: Maze, Torch, Blaster, Portal."],
    ["Homework Review", "Review lesson 32: bullet memory cleanup and spark particle bursts upon impact.", "Highlight golden code patterns and punchy game feel."],
    ["4 Game Pillars", "Break down game architecture: map, torchlight, shooting action, and victory goal.", "Ask the class: 'Why does an aimless game get boring so fast?'"],
    ["Pillar 1: Maze", "Demonstrate 20x13 tile grid collisions and smooth obstacle sliding.", "Ensure hero does not clip through stone obstacles."],
    ["Pillar 2: Torch", "Explain darkness and mystery: radial gradient torchlight via destination-out mask.", "Chests stay shrouded until explored up close."],
    ["Pillar 3: Blaster", "Demonstrate 360-degree mouse aiming and radial spark bursts against walls.", "Weapon recoil delivers authentic arcade crunch."],
    ["Pillar 4: Portal", "Explain win state: collecting all 3 chests unseals the emerald exit portal.", "Showcase the HUD key counter."],
    ["Smartboard Live Play", "Open slide 8: invite students to play Shadow Dungeon 2D directly on screen.", "Move with arrows, shoot lasers, collect 3 chests, and escape!"],
    ["Gamer Quiz", "Reinforce game dev intuition through 3 interactive questions.", "Reward quick and accurate answers."],
    ["Vibecoding Arena", "Display 4 structured prompt cards and launch 30 minutes of hands-on PC coding.", "Guide students through assembling the 4 game pillars."],
    ["Peer Duel Playtest", "Students swap seats to test if peer dungeons are fun, fair, and bug-free.", "Guide students on submitting Critic fix prompts."],
    ["Big Screen Showcase", "Invite 2 students with coolest dungeons to showcase gameplay on the big display.", "Cheer on evasive speedruns with the whole class."],
    ["Homework Challenge", "Explain the 10-point rubric: maze & torch, blaster & chests, and custom mechanic.", "Remind them of LocalStorage auto-save in vazifa.html."],
    ["Summary & Bridge", "Summarize the milestone: everyone built a complete indie game for their portfolio.", "Tease the arrival of predatory monsters in the next module."]
]

NOTES_DATA = {
  "uz": triplets_uz,
  "ru": triplets_ru,
  "en": triplets_en
}

# -----------------------------------------------------------------------------
# 4. BUILD FUNCTIONS
# -----------------------------------------------------------------------------
def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "33-dars: Shadow Dungeon: O'z Kiber-Qasringni Qur! (Roguelike Game Project)"
    title_ru = "Урок 33: Shadow Dungeon: Создаем Свою Игру Roguelike"
    title_en = "Lesson 33: Shadow Dungeon: Engineering a Complete Roguelike Game"

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

    title_uz = "33-dars: Shadow Dungeon: Kiber-Qasr O'yin Loyihasi (GDD)"
    title_ru = "Урок 33: Shadow Dungeon: Проект Игры в Кибер-Замке (GDD)"
    title_en = "Lesson 33: Shadow Dungeon: Game Design Document & Project"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<h1>.*?</h1>',
                 f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>',
                 tpl)

    sec1_html = """
    <p class="lead" style="font-size:12px; margin-bottom:8px;" data-ru="<strong>Миссия Урока:</strong> Собрать 4 игровые системы в один целостный инди-проект 'Shadow Dungeon 2D': лабиринт, факел тьмы, лазерный бластер и победный портал с золотыми сундуками." data-en="<strong>Lesson Mission:</strong> Assemble 4 game systems into one complete indie title 'Shadow Dungeon 2D': maze grid, torchlight, laser blaster, and a victory portal unlocked via 3 gold chests."><strong>Dars Missiyasi:</strong> 4 ta o'yin tizimini bitta yaxlit "Shadow Dungeon 2D" loyihasiga jamlash: labirint xaritasi, mash'ala nuri, lazer blastersi va 3 ta oltin quti orqali ochiluvchi g'alaba portali.</p>
    <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="4 Столпа Игры Shadow Dungeon:" data-en="4 Pillars of Shadow Dungeon:">Shadow Dungeon O'yinining 4 Asosiy Ustuni:</div>
      <div>1. <strong>Tosh Qasr:</strong> <span data-ru="Сетка 20x13 с каменными стенами и свободными коридорами" data-en="20x13 tile grid with impassable walls and open corridors">20x13 katakli labirint va tosh devorlar bilan to'qnashuv</span>.</div>
      <div>2. <strong>Mash'ala Nuri:</strong> <span data-ru="Радиальный свет факела 140px вокруг героя в темноте" data-en="140px radial torchlight illuminating around hero in the dark">Qahramon atrofidagi 140px sirli radial yorug'lik doirasi</span>.</div>
      <div>3. <strong>Kiber-Blaster:</strong> <span data-ru="Стрельба на 360 градусов и вспышки искр от препятствий" data-en="360-degree mouse aiming and spark particles upon wall hit">Sichqoncha bilan nishonga olish va devorga tekkanda uchqunlar</span>.</div>
      <div>4. <strong>Xazina va Portal:</strong> <span data-ru="Сбор 3 сундуков открывает изумрудный портал победы" data-en="3 collected gold chests unlock the emerald victory portal">3 ta oltin qutini ochgandan keyin ochiluvchi chiqish portali</span>.</div>
    </div>
    """

    sec2_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="Архитектура проверки открытия портала:" data-en="Victory portal unlock logic:">G'alaba portali ochilish mantig'i:</p>
    <pre style="background:var(--surface-2); padding:6px; font-size:11px; border-radius:4px; margin:0;"><code class="language-javascript">// Agar qahramon qutiga tegsa, kalit qo'shiladi:
if (!chest.collected && hero.x === chest.x && hero.y === chest.y) {
  chest.collected = true;
  keysFound++;
  if (keysFound === 3) {
    portal.active = true; // Yashil portal yonadi!
  }
}</code></pre>
    """

    sec3_html = """
    <div style="font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="Паспорт Игрового Проекта:" data-en="Game Project Profile:">O'yin Loyihasi Pasporti:</div>
      <div>🏰 <strong>Nomi:</strong> Shadow Dungeon 2D (Kiber-Qasr)</div>
      <div>🎯 <strong>Maqsadi:</strong> 3 ta xazinani ochib, portalga yetib borish va omon chiqish.</div>
      <div>⚡ <strong>Vositalar:</strong> HTML5 Canvas, JavaScript, Math.atan2, Vibecoding.</div>
    </div>
    """

    sec4_html = """
    <div style="display:flex; flex-direction:column; gap:8px; font-size:11px;">
      <div style="border:1px solid var(--rule); border-radius:4px; padding:6px;">
        <div style="font-weight:700; color:var(--accent-ink);" data-ru="Задание 1: Название и Атмосфера Замка" data-en="Task 1: Castle Name & Theme">1-Topshiriq: O'z Qasringiz Nomi va Xususiyatini Yozing</div>
        <p style="margin:2px 0 4px; font-size:8.5pt;" data-ru="Придумайте название для своей версии игры и радиус факела:" data-en="Write title for your game version and torch radius:">O'z o'yiningiz uchun nom va mash'ala rangini yozing (masalan: Neon Dungeon, Oltin nur):</p>
        <div style="border-bottom:1px dashed #cbd5e1; height:20px;"></div>
      </div>
      <div style="border:1px solid var(--rule); border-radius:4px; padding:6px;">
        <div style="font-weight:700; color:var(--accent-ink);" data-ru="Задание 2: Vibecoding промпт для сбора сундуков" data-en="Task 2: Chest Collecting Prompt">2-Topshiriq: Qutilar va Portal Uchun AI Prompti</div>
        <p style="margin:2px 0 4px; font-size:8.5pt;" data-ru="Напишите точный промпт для AI, чтобы сундуки открывали портал:" data-en="Write precision prompt so 3 chests unlock the victory portal:">AI ga 3 ta quti yig'ilganda portal ochilib g'alaba berishi uchun so'rov matnini yozing:</p>
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
          <td style="padding:4px; border:1px solid var(--rule); font-weight:600;" data-ru="Лабиринт и факел" data-en="Maze & Torchlight">Labirint va mash'ala</td>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:700; color:var(--green);" data-ru="4 балла" data-en="4 pts">4 ball</td>
          <td style="padding:4px; border:1px solid var(--rule);" data-ru="Сетка замка, движение на стрелки и круг света факела." data-en="Maze grid, arrow controls, and radial torchlight.">Qasr xaritasi, strelkalar bilan harakat va mash'ala nuri.</td>
        </tr>
        <tr>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:600;" data-ru="Бластер и 3 сундука" data-en="Blaster & 3 Chests">Blaster va 3 ta quti</td>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:700; color:var(--green);" data-ru="4 балла" data-en="4 pts">4 ball</td>
          <td style="padding:4px; border:1px solid var(--rule);" data-ru="Стрельба искрами и 3 сундука, открывающих портал." data-en="Blaster with sparks and 3 chests opening portal.">Lazer otish, uchqunlar va 3 ta qutini ochish.</td>
        </tr>
        <tr>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:600;" data-ru="Спец-механика" data-en="Custom Mechanic">Shaxsiy super-imkoniyat</td>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:700; color:var(--green);" data-ru="2 балла" data-en="2 pts">2 ball</td>
          <td style="padding:4px; border:1px solid var(--rule);" data-ru="Звук победы, рывок на пробел или ловушки на полу." data-en="Victory audio, spacebar dash, or floor hazards.">G'alaba audio ovozi, 'Space' sprinti yoki tikanlar.</td>
        </tr>
      </tbody>
    </table>
    """

    replacements = {
        "{{LESSON_NUM}}": "33",
        "{{TITLE_UZ}}": "Shadow Dungeon 2D: Kiber-Qasr O'yin Loyihasi",
        "{{TITLE_RU}}": "Shadow Dungeon 2D: Проект Игры в Кибер-Замке",
        "{{TITLE_EN}}": "Shadow Dungeon 2D: Castle Roguelike Game Project",
        "{{COHORT_LABEL_UZ}}": "7–8-SINF",
        "{{COHORT_LABEL_RU}}": "7–8 КЛАСС",
        "{{COHORT_LABEL_EN}}": "GRADES 7–8",
        "{{META_UZ}}": "11-Hafta · Juftlik Dars (80 daqiqa) · Game Dev & Vibecoding Track",
        "{{META_RU}}": "11-я Неделя · Сдвоенный Урок (80 минут) · Направление Game Dev & Vibecoding",
        "{{META_EN}}": "Week 11 · Double Block (80 min) · Game Dev & Vibecoding Track",
        "{{MISSION_UZ}}": "O'tgan darslarda o'rganilgan barcha mexanikalarni (Labirint, mash'ala nuri, lazer blastersi va xazina qutilari) yagona, to'liq o'ynaladigan 'Shadow Dungeon 2D' kiber-qasr o'yiniga jamlash.",
        "{{MISSION_RU}}": "Объединить все изученные механики (лабиринт, факел тьмы, лазерный бластер и сундуки) в одну целостную играбельную игру 'Shadow Dungeon 2D'.",
        "{{MISSION_EN}}": "Unite all learned mechanics (maze grid, torchlight, laser blaster, and chests) into one complete playable 'Shadow Dungeon 2D' title.",
        "{{SEC1_TITLE_UZ}}": "Shadow Dungeon O'yinining 4 Asosiy Ustuni",
        "{{SEC1_TITLE_RU}}": "4 Столпа Игры Shadow Dungeon",
        "{{SEC1_TITLE_EN}}": "4 Pillars of Shadow Dungeon",
        "{{SEC1_CONTENT}}": sec1_html,
        "{{SEC2_TITLE_UZ}}": "G'alaba Portali Ochilish Mantig'i",
        "{{SEC2_TITLE_RU}}": "Логика Открытия Портала Победы",
        "{{SEC2_TITLE_EN}}": "Victory Portal Unlock Architecture",
        "{{SEC2_CONTENT}}": sec2_html,
        "{{SEC3_TITLE_UZ}}": "O'yin Loyihasi Pasporti va Topshiriqlar",
        "{{SEC3_TITLE_RU}}": "Паспорт Игрового Проекта и Задания",
        "{{SEC3_TITLE_EN}}": "Game Project Profile & Tasks",
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
      <h4 data-ru="Задание 1: Промпт для Факела Тьмы" data-en="Task 1: Prompt for Darkness Torchlight">1-Topshiriq: Mash'ala Yorug'ligi Prompti</h4>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите точный промпт для ИИ, чтобы добавить в игру радиальный свет факела вокруг героя через destination-out:" data-en="Write a precision prompt for AI to add radial torchlight around hero via destination-out:">AI ga qahramon atrofida 140px radial mash'ala yorug'ligi yaratish va qolgan joylarni qorong'i qilish so'rovini yozing:</p>
      <textarea id="hw-t1" class="hw-input" style="width:100%; height:75px; font-family:var(--font-mono); font-size:12px;" placeholder="AI ga yoziladigan prompt..." data-placeholder-ru="Промпт для отправки в ИИ..." data-placeholder-en="Prompt to send to AI..."></textarea>
      <button class="btn" style="margin-top:6px; padding:4px 10px; font-size:11px;" onclick="document.getElementById('sol-t1').style.display='block';" data-ru="💡 Показать Решение" data-en="💡 View Solution">💡 Yechimni Ko'rish</button>
      <div id="sol-t1" style="display:none; margin-top:6px; padding:8px; background:var(--panel-2); border-radius:4px; font-size:11px; font-family:var(--font-mono); color:var(--green);">
        // Oltin Prompt:<br>
        "Butun ekranni qora rang bilan qopla. Qahramon koordinatasida 140px radial gradient yarat va globalCompositeOperation = 'destination-out' orqali qorong'ulikni teshik ochib qahramon atrofini yorit."
      </div>
    </div>
    """

    task2 = """
    <div style="margin-bottom:12px;">
      <h4 data-ru="Задание 2: Стрельба Мышкой с Отдачей" data-en="Task 2: Mouse Blaster with Sparks">2-Topshiriq: Kiber-Blaster va Uchqunlar So'rovi</h4>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите промпт для стрельбы кликом мыши с удалением пуль при ударе о стену и вспышкой искр:" data-en="Write prompt for mouse shooting with wall collision and spark particles:">Sichqoncha bosilganda lazer otilishi va devorga tekkanda 6 ta uchqun sochilib o'q o'chishi uchun prompt yozing:</p>
      <textarea id="hw-t2" class="hw-input" style="width:100%; height:65px; font-family:var(--font-mono); font-size:12px;" placeholder="Javobingizni yozing..." data-placeholder-ru="Напишите ваш ответ..." data-placeholder-en="Write your answer..."></textarea>
      <button class="btn" style="margin-top:6px; padding:4px 10px; font-size:11px;" onclick="document.getElementById('sol-t2').style.display='block';" data-ru="💡 Показать Решение" data-en="💡 View Solution">💡 Yechimni Ko'rish</button>
      <div id="sol-t2" style="display:none; margin-top:6px; padding:8px; background:var(--panel-2); border-radius:4px; font-size:11px; font-family:var(--font-mono); color:var(--green);">
        // Oltin Prompt:<br>
        "Canvas'ga 'click' hodisasini qo'sh. Kursor tomon Math.atan2 bilan o'q uz. O'q tosh devorga tekkanda uni bullets massividan o'chir va o'rniga 6 ta rangli uchqun (particle) yarat."
      </div>
    </div>
    """

    task3 = """
    <div style="margin-bottom:12px;">
      <h4 data-ru="Задание 3: Логика 3 Сундуков и Портала" data-en="Task 3: 3 Chests & Exit Portal Logic">3-Topshiriq: 3 Ta Quti va Chiqish Portali</h4>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Как на JavaScript проверить сбор 3 сундуков и активировать портал выхода? Опишите логику:" data-en="How to verify collecting 3 chests and trigger the exit portal in JavaScript? Describe the logic:">3 ta xazina qutisi to'liq ochilganini tekshirish va portalni faollashtirish kod mantig'ini yozing:</p>
      <textarea id="hw-t3" class="hw-input" style="width:100%; height:65px; font-family:var(--font-mono); font-size:12px;" placeholder="Audio so'rovi yoki javob..." data-placeholder-ru="Запрос на аудио или ответ..." data-placeholder-en="Audio prompt or answer..."></textarea>
      <button class="btn" style="margin-top:6px; padding:4px 10px; font-size:11px;" onclick="document.getElementById('sol-t3').style.display='block';" data-ru="💡 Показать Решение" data-en="💡 View Solution">💡 Yechimni Ko'rish</button>
      <div id="sol-t3" style="display:none; margin-top:6px; padding:8px; background:var(--panel-2); border-radius:4px; font-size:11px; font-family:var(--font-mono); color:var(--green);">
        // To'g'ri Javob:<br>
        O'zgaruvchi keysFound = 0; Har safar qutiga tegilganda keysFound++; Agar keysFound === 3 bo'lsa, portal.active = true; va portal yashil zangori rangda porlaydi!
      </div>
    </div>
    """

    task4 = """
    <div style="margin-bottom:12px;">
      <h4 data-ru="Задание 4: Уникальная Игровая Фича" data-en="Task 4: Custom Game Polish Feature">4-Topshiriq: O'yiningiz Uchun Maxsus Qo'shimcha</h4>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Придумайте и опишите одну свою уникальную игровую деталь (звук победы, спринт на пробел, зелье лечения):" data-en="Invent and describe your unique game feature (victory audio, spacebar sprint, health potion):">O'z o'yiningiz uchun bitta qiziqarli yangilik (g'alaba audio ovozi, 'Space' bilan yugurish, jon dorisi) g'oyasini va AI promptini yozing:</p>
      <textarea id="hw-t4" class="hw-input" style="width:100%; height:65px; font-family:var(--font-mono); font-size:12px;" placeholder="Super-qobiliyat prompti..." data-placeholder-ru="Промпт суперспособности..." data-placeholder-en="Super-power prompt..."></textarea>
      <button class="btn" style="margin-top:6px; padding:4px 10px; font-size:11px;" onclick="document.getElementById('sol-t4').style.display='block';" data-ru="💡 Показать Решение" data-en="💡 View Solution">💡 Yechimni Ko'rish</button>
      <div id="sol-t4" style="display:none; margin-top:6px; padding:8px; background:var(--panel-2); border-radius:4px; font-size:11px; font-family:var(--font-mono); color:var(--green);">
        // Misol Prompt:<br>
        "'Space' klavishi bosilganda qahramon 1 soniyaga tezligini 2 barobar oshirsin (Dash) va orqasidan ko'k iz qoldirsin!"
      </div>
    </div>
    """

    tasks_html = task1 + task2 + task3 + task4

    replacements = {
        "{{TITLE_UZ}}": "33-dars: Shadow Dungeon 2D: Kiber-Qasr O'yin Loyihasi",
        "{{TITLE_RU}}": "Урок 33: Shadow Dungeon 2D: Проект Игры в Кибер-Замке",
        "{{TITLE_EN}}": "Lesson 33: Shadow Dungeon 2D: Castle Roguelike Game Project",
        "{{COHORT_LABEL_UZ}}": "7–8-SINF",
        "{{HERO_TAG_UZ}}": "11-Hafta · Game Dev & Vibecoding Track",
        "{{HERO_DESC_UZ}}": "Uyingizda mustaqil ravishda Shadow Dungeon 2D o'yini uchun mash'ala nuri, kiber-blaster, xazina qutilari va portalni AI yordamida dasturlang.",
        "{{HERO_DESC_RU}}": "Самостоятельно соберите игру Shadow Dungeon 2D: свет факела, лазерный бластер, сундуки и портал через Vibecoding.",
        "{{HERO_DESC_EN}}": "Assemble the Shadow Dungeon 2D game at home: torchlight, laser blaster, chests, and portal via Vibecoding prompts.",
        "{{RUBRIC_T1_UZ}}": "1-Bosqich: Baza (Labirint xaritasi va mash'ala nuri)",
        "{{RUBRIC_T1_RU}}": "1-й Уровень: База (Сетка лабиринта и свет факела)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (Maze grid & torchlight illumination)",
        "{{RUBRIC_T2_UZ}}": "2-Bosqich: Muhandis (Kiber-blaster va 3 ta xazina)",
        "{{RUBRIC_T2_RU}}": "2-й Уровень: Практика (Бластер с искрами и 3 сундука)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Spark blaster & 3 chests with portal)",
        "{{RUBRIC_T3_UZ}}": "3-Bosqich: Kiber-Chaqiruv (Shaxsiy super-imkoniyat va ovoz)",
        "{{RUBRIC_T3_RU}}": "3-й Уровень: Вызов (Уникальная фича, спринт или аудио)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (Custom polish feature, sprint, or audio)",
        "{{TASKS_HTML}}": tasks_html,
        "{{LESSON_SLUG}}": "7-8-w11-l33-shadow-dungeon-kiber-qasr"
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")


def build_teacher_guide():
    guide_md = """# O'qituvchi Qo'llanmasi: 33-Dars — Shadow Dungeon: O'z Kiber-Qasringni Qur!

**Sinf:** 7–8-sinf · **Format:** 80 daqiqalik Juftlik Dars · **Yo'nalish:** Vibecoding & Game Dev

---

## 🎯 Asosiy Pedagogik Konseptsiya (QAT'IY QOIDA)
🛑 **Quruq matematika va nazariya taqiqlanadi!**
Bugun o'quvchilar 10–11-haftalar davomida o'rgangan barcha qismlarini (Tilemaps, Mash'ala, Otishma) bitta haqiqiy, do'stlari bilan o'ynaydigan **"Shadow Dungeon 2D"** o'yiniga birlashtiradilar!

Dars formati: **Mini Game Jam & O'yin Sintezi**.
Har bir o'quvchi dars oxirida o'zining to'liq o'ynaladigan qasri va g'alaba portaliga ega bo'lishi shart!

---

## ⏱️ 80 Daqiqalik Dars Vaqti Taqsimoti

| Vaqt | Bosqich | O'qituvchi Harakati va Faoliyat |
|---|---|---|
| **00:00–08:00** | **HW Review & Ko'prik** | 32-dars otishmasini eslash: o'qlarni tozalash (Memory cleanup). Blitz savol: "Hamma narsa bor, o'yin bo'lishi uchun nima yetishmayapti? Albatta maqsad — 3 ta xazina va chiqish portali!" |
| **08:00–20:00** | **O'yinning 4 Ustuni Tahlili** | Qasr labirinti, Mash'ala qorong'uligi, Kiber-blaster uchqunlari va Oltin qutilar/Portal mexanikasini doskada tushuntirish. |
| **20:00–30:00** | **Smartboardda Jonli O'yin** | 8-slaydni ochish: o'quvchilarni doskaga chaqirib 'Shadow Dungeon' o'yinini o'ynatish. Strelkalar bilan yurish, o'q uzish, 3 ta qutini topib portalga kirish! |
| **30:00–35:00** | **Geymerlar Viktorinasi** | 3 ta tezkor savol orqali tushunchalarni mustahkamlash. |
| **35:00–65:00** | **30 Minutlik Katta Game Jam Arena** | O'quvchilar kompyuterlarida o'tirib, 4 ta tayyor prompt kartasi orqali o'z o'yinlariga barcha qismlarni jamlaydilar. |
| **65:00–74:00** | **Partadosh Duelosy (Playtest)** | Partadoshlar joyini almashtirib, bir-birining qasridan omon chiqishga harakat qilishadi. Xatolar critic prompt orqali tuzatiladi. |
| **74:00–77:00** | **Katta Ekran Showcasi** | 2 ta eng chiroyli atmosfera yaratgan o'quvchi o'z o'yinini katta doskada namoyish qiladi. |
| **77:00–80:00** | **Uy Vazifasi va Yakun** | 10 ballik uy vazifasi tushuntiriladi. Keyingi modul anons qilinadi. |
"""

    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(guide_md)
    print("  ✓ Created: TEACHER_READING.md")


def build_standalone_game():
    with open(os.path.join(DEST_DIR, "prezentatsiya.html"), "r", encoding="utf-8") as f:
        html = f.read()

    # Create full screen playable game in simulator/index.html
    game_html = f"""<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Shadow Dungeon 2D — Игра в Кибер-Замке" data-en="Shadow Dungeon 2D — Cyber Castle Game">Shadow Dungeon 2D — Kiber-Qasr O'yini</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #020617;
      color: #f8fafc;
      font-family: system-ui, -apple-system, sans-serif;
      height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}
    .hud {{
      display: flex;
      gap: 20px;
      margin-bottom: 12px;
      font-size: 14px;
      font-weight: 700;
      background: #0f172a;
      padding: 8px 16px;
      border-radius: 8px;
      border: 1px solid rgba(255,255,255,0.1);
    }}
    canvas {{
      border: 2px solid #334155;
      border-radius: 8px;
      cursor: crosshair;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}
    .controls {{
      margin-top: 12px;
      font-size: 12px;
      color: #94a3b8;
    }}
  </style>
</head>
<body>
  <div class="hud">
    <span style="color:#f59e0b;" data-ru="📦 Ключи: <span id='deck-keys'>0</span>/3" data-en="📦 Keys: <span id='deck-keys'>0</span>/3">📦 Xazinalar: <span id="deck-keys">0</span>/3</span>
    <span style="color:#38bdf8;" data-ru="❤️ Жизни: <span id='deck-hp'>3</span>" data-en="❤️ HP: <span id='deck-hp'>3</span>">❤️ Jon: <span id="deck-hp">3</span></span>
    <button id="deck-btn-restart" style="padding:2px 8px; font-size:11px; background:#334155; color:#fff; border:none; border-radius:4px; cursor:pointer;" data-ru="🔄 Перезапуск" data-en="🔄 Restart">🔄 Qayta Boshlash</button>
  </div>
  <canvas id="deck-shadow-canvas" width="620" height="260"></canvas>
  <div class="controls" data-ru="⌨️ Стрелки/WASD: Движение | 🖱️ Клик: Лазер | 📦 Сундуки: Ключи | 🌀 Портал: Выход" data-en="⌨️ Arrows/WASD: Move | 🖱️ Click: Shoot | 📦 Chests: Keys | 🌀 Portal: Exit">
    ⌨️ <b>Strelkalar / WASD</b>: Harakat | 🖱️ <b>Klik</b>: Lazer | 📦 <b>Xazinalar</b>: Kalitlar | 🌀 <b>Portal</b>: Chiqish
  </div>

  <script>
{SIMULATOR_JS}
  </script>
</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "simulator", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(game_html)
    print("  ✓ Created: simulator/index.html")


if __name__ == "__main__":
    print("🚀 Building 7–8th Grade Week 11 Lesson 33: Shadow Dungeon 2D (Concrete Game Project)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_guide()
    build_standalone_game()
    print("✅ All Shadow Dungeon 2D project files successfully compiled!")
