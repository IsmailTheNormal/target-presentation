#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_5_6_w11_l29.py — Builder for 5–6th Grade, Week 11, Lesson 29

Mavzu: Aqlli Shartlar: Agar... U Holda (If... Then) va Sezgirlik Bloklari
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 5-6-sinf (Junior Creators & Scratch Track)
Pedagogika: VIZUAL MANTIQ VA AMALIYAT — Scratch "Agar... u holda" (If... then)
             va "Tegdimi?" (Sensing) bloklari. Sehrli labirint o'yini: qora devorga
             tekkanda orqaga otilish, qizil tuzoqdan qochish va marraga yetish.
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "5-6-sinf", "11-hafta", "29-dars-aqlli-shartlar-va-sezgirlik")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "playground"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides — Fun, Visual Scratch Logic)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="5–6-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 29" data-en="GRADES 5–6 · WEEK 11 · LESSON 29">5–6-SINF · 11-HAFTA · 29-DARS</span></div>
    <h1 class="display" data-ru="Умные Условия: «Если… То» и Блоки Сенсоров в Scratch" data-en="Smart Conditions: «If… Then» & Sensing Blocks in Scratch">Aqlli Shartlar: Agar... U Holda va Sezgirlik</h1>
    <p class="lede" data-ru="Учим нашего персонажа думать и чувствовать мир: блоки «Если... то», проверка касания цвета и препятствий, а также создание игры «Волшебный Лабиринт»!" data-en="Teaching our character to reason and sense the world: «If... then» logic, color sensing, and engineering the Magic Maze game in Scratch!">Qahramonimizga fikrlash va sezish qobiliyatini beramiz: Scratch "Agar... u holda" shartlari, rang va to'siqlarga tegish datchiklari hamda "Sehrli Labirint" o'yini!</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Сенсоры и Логика" data-en="Sensors & Logic">Mantiq va Sezgirlik</h3>
        <p data-ru="Персонаж больше не ходит вслепую — он чувствует стены лабиринта и реагирует на опасность!" data-en="The character no longer moves blindly — it senses walls and reacts to danger!">Qahramon endi ko'r-ko'rona yurmaydi — u labirint devorlarini sezadi va xavfdan qochadi!</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Magic Maze Game</div>
        <h3 data-ru="Игра «Волшебный Лабиринт»" data-en="Magic Maze Game">Sehrli Labirint O'yini</h3>
        <p data-ru="Каждый соберет лабиринт, где кот отскакивает от черных стен и собирает кристаллы." data-en="Everyone builds a maze where the cat bounces off walls and collects gems.">Har bir o'quvchi qora devorga tekkanda orqaga otiluvchi va kristallarni teruvchi o'yin yasaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW & BRIDGE -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="РАЗБОР ДОМАШНЕГО ЗАДАНИЯ И МОСТ" data-en="HOMEWORK REVIEW & BRIDGE">UY VAZIFASI TAHLILI VA KO'PRIK</span></div>
    <h2 data-ru="Итоги Game Jam и Мост к Умным Условиям" data-en="Game Jam Recap & Bridge to Smart Logic">28-Dars Game Jam Tahlili va Yangi Mavzuga Ko'prik</h2>
    <div class="grid-2">
      <div>
        <div class="box" style="border-left:4px solid var(--accent); margin-bottom:12px;">
          <h4 data-ru="Частая ошибка: Кот проваливался сквозь стены" data-en="Common Pitfall: Cat Clipping Through Walls">Katta Xato: Qahramon Devordan O'tib Ketishi</h4>
          <p style="font-size:12px;" data-ru="Многие ученики сделали управление стрелками, но кот проходил сквозь любые препятствия как призрак!" data-en="Many students added arrow movement, but the cat clipped through walls like a ghost!">Ko'pchilik o'quvchilar strelkalar bilan harakat qilishni qo'shdi, lekin mushuk tosh devorlardan arvohdek o'tib ketdi!</p>
        </div>
        <div class="box" style="border-left:4px solid var(--green);">
          <h4 data-ru="Золотой Стандарт (Блок «Касается»)" data-en="Golden Standard (Touching Block)">Oltin Yechim: Sezgirlik Bloki</h4>
          <p style="font-size:12px; margin:4px 0; font-family:var(--font-mono); color:var(--green);" data-ru="«Если касается цвета [Черный], то идти (-10) шагов»" data-en="«If touching color [Black], then move (-10) steps»">"agar [Qora rang]ga tegdimi? bo'lsa: (-10) qadam yur"</p>
          <p style="font-size:11px; color:var(--ink-2); margin:0;" data-ru="При столкновении со стеной герой отскакивает назад и не проходит сквозь неё." data-en="Hero bounces backward upon hitting a wall, preventing clipping.">Devorga tekkanda mushuk orqaga tisariladi va devor ichiga kirib ketmaydi.</p>
        </div>
      </div>
      <div>
        <div class="box" style="margin-bottom:12px; background:var(--panel-2);">
          <div class="tag" style="background:var(--accent-soft); color:var(--accent);" data-ru="Блиц-Вопрос" data-en="Blitz Question">30 Soniyalik Blitz Savol</div>
          <p style="font-size:13px; font-weight:600; margin:6px 0;" data-ru="Как заставить робота открывать дверь ТОЛЬКО когда у него есть золотой ключ?" data-en="How to make a robot open a door ONLY when it has the golden key?">Qanday qilib robotga "Faqat oltin kalit bo'lsagina eshikni och" deb buyruq beramiz?</p>
          <p style="font-size:12px; color:var(--green); font-weight:700;" data-ru="👉 Ответ: Через блок «Если [ключ есть], то [открыть дверь]»!" data-en="👉 Answer: Via the block «If [has key], then [open door]»!">👉 Javob: Scratch'dagi "Agar [kalit bor] bo'lsa, [eshikni och]" bloki orqali!</p>
        </div>
        <div class="box" style="border-left:4px solid var(--purple);">
          <h4 data-ru="Мост к сегодняшней теме" data-en="Bridge to Today's Lesson">Bugungi Mavzuga Ko'prik</h4>
          <p style="font-size:12px;" data-ru="Сегодня мы научим наших персонажей думать: принимать решения, объезжать ловушки и находить выход из лабиринта!" data-en="Today we teach our sprites to think: make decisions, avoid traps, and escape mazes!">Bugun barcha qahramonlarimizga "aql" beramiz: to'siqlarni sezish, tuzoqlardan qochish va sehrli labirint qurishni o'rganamiz!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: WHAT IS AN IF CONDITION -->
  <section class="slide" data-phase="Shartlar Nima|Что Такое Условия|If-Then Concept" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ОСНОВА ВСЕГО ПРОГРАММИРОВАНИЯ" data-en="FOUNDATION OF ALL CODING">KOMPYUTER QANDAY FIKRLAYDI?</span></div>
    <h2 data-ru="Блок «Если… То»: Как Компьютер Принимает Решения?" data-en="The «If… Then» Block: How Computers Make Decisions">«Agar... U Holda» Bloki Qanday Ishlaydi?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="В реальной жизни мы постоянно используем условия:" data-en="In real life, we use conditional rules every single day:">Haqiqiy hayotda ham biz har doim shartlar asosida yashaymiz:</p>
        <ul class="clean-list">
          <li data-ru="<strong>☔ Дождь:</strong> «ЕСЛИ на улице дождь, ТО берем зонтик»." data-en="<strong>☔ Rain:</strong> «IF it rains outside, THEN take an umbrella»." data-uz="<strong>☔ Yomg'ir:</strong> «AGAR ko'chada yomg'ir yog'sa, U HOLDA soyabon olamiz»."><strong>☔ Yomg'ir:</strong> «AGAR ko'chada yomg'ir yog'sa, U HOLDA soyabon olamiz».</li>
          <li data-ru="<strong>🚦 Светофор:</strong> «ЕСЛИ горит красный, ТО стоим на месте»." data-en="<strong>🚦 Traffic Light:</strong> «IF red light is on, THEN stop and wait»." data-uz="<strong>🚦 Svetofor:</strong> «AGAR qizil chiroq yonsa, U HOLDA to'xtaymiz»."><strong>🚦 Svetofor:</strong> «AGAR qizil chiroq yonsa, U HOLDA to'xtaymiz».</li>
          <li data-ru="<strong>🎮 Игра:</strong> «ЕСЛИ жизней 0, ТО игра окончена (Game Over)»." data-en="<strong>🎮 Game:</strong> «IF health reaches 0, THEN Game Over»." data-uz="<strong>🎮 O'yin:</strong> «AGAR jonlar 0 bo'lsa, U HOLDA Game Over bo'ladi»."><strong>🎮 O'yin:</strong> «AGAR jonlar 0 bo'lsa, U HOLDA Game Over bo'ladi».</li>
        </ul>
      </div>
      <div>
        <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); padding:16px;">
          <div style="color:var(--yellow); font-family:var(--font-mono); font-size:13px; font-weight:700; margin-bottom:8px;">Scratch "Boshqaruv" (Control) Bloki:</div>
          <div style="background:#f59e0b; color:#000; padding:10px 14px; border-radius:6px; font-weight:700; font-family:system-ui; font-size:13px;">
            agar &lt; shart &gt; bo'lsa:
            <div style="background:#fff; margin:6px 0 6px 14px; padding:6px 10px; border-radius:4px; color:#000; font-size:12px;">
              // Shart to'g'ri bo'lsa bajariladigan ish
            </div>
            tamom
          </div>
          <p style="font-size:11px; color:#94a3b8; margin-top:8px;" data-ru="Внутрь шестиугольника вставляется вопрос, на который можно ответить только ДА или НЕТ." data-en="Inside the hexagon sits a question with only YES or NO answers.">Oltiburchak shaklidagi uyachaga faqat "HA" yoki "YO'Q" deb javob beriladigan savol qo'yiladi!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: SENSING BLOCKS (TOUCHING) -->
  <section class="slide" data-phase="Sezgirlik Bloklari|Блоки Сенсоров|Sensing Blocks" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="ГЛАЗА И УШИ ПЕРСОНАЖА" data-en="EYES & EARS OF SPRITES">SEZGIRLIK (SENSING) BLOKLARI</span></div>
    <h2 data-ru="Голубые Блоки Сенсоров: Что Умеет Чувствовать Кот?" data-en="Cyan Sensing Blocks: What Can the Cat Sense?">Moviy Sezgirlik Bloklari Qanday Ishlaydi?</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid #38bdf8;">
        <div style="font-size:28px; margin-bottom:6px;">🎨</div>
        <h4 data-ru="Касается Цвета?" data-en="Touching Color?">&lt; [Rang]ga tegdimi? &gt;</h4>
        <p style="font-size:12px;" data-ru="Проверяет, коснулся ли спрайт определенного цвета на экране (например, черной стены или красной лавы)." data-en="Detects if sprite touches a specific color on screen (e.g. black wall or red lava).">Sprayt ekrandagi biror rangga (masalan qora devorga yoki qizil olovga) tekkanini aniqlaydi.</p>
      </div>
      <div class="box" style="border-top:4px solid #38bdf8;">
        <div style="font-size:28px; margin-bottom:6px;">👾</div>
        <h4 data-ru="Касается Спрайта?" data-en="Touching Sprite?">&lt; [Sprayt]ga tegdimi? &gt;</h4>
        <p style="font-size:12px;" data-ru="Проверяет, коснулся ли герой другого персонажа: кристаллов, врагов или портала победы!" data-en="Checks if hero collided with crystals, enemies, or the victory portal!">Qahramon boshqa spraytga (masalan yulduzga, dushmanga yoki eshikka) tekkanini biladi!</p>
      </div>
      <div class="box" style="border-top:4px solid #38bdf8;">
        <div style="font-size:28px; margin-bottom:6px;">⌨️</div>
        <h4 data-ru="Клавиша Нажата?" data-en="Key Pressed?">&lt; [Tugma] bosildimi? &gt;</h4>
        <p style="font-size:12px;" data-ru="Проверяет, нажата ли прямо сейчас клавиша пробел или стрелка на клавиатуре игрока." data-en="Checks if spacebar or an arrow key is actively pressed on the keyboard.">Klaviaturadagi 'Probel' yoki strelka tugmasi ayni damda bosib turilganini tekshiradi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: WALL COLLISION LOGIC -->
  <section class="slide" data-phase="Devorga Urilish|Отскок от Стен|Wall Collision" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="СЕКРЕТ НЕПРОБИВАЕМЫХ СТЕН" data-en="SOLID WALL SECRET">DEVORGA URILISH SIRI</span></div>
    <h2 data-ru="Как Сделать Стены Твердыми? Секрет Отскока" data-en="How to Make Walls Solid? The Bounce Secret">Qanday Qilib Devorlarni Qattiq Qilamiz?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Компьютер не знает, что стена твердая, пока мы не объясним это блоками:" data-en="The computer does not know walls are solid until we instruct it with blocks:">Kompyuter devor tosh ekanini o'zi bilmaydi. Biz unga qoida o'rgatishimiz kerak:</p>
        <ul class="clean-list">
          <li data-ru="<strong>1-Шаг:</strong> Герой делает шаг вперед: «идти (5) шагов»." data-en="<strong>Step 1:</strong> Hero takes a step forward: «move (5) steps»." data-uz="<strong>1-Qadam:</strong> Qahramon oldinga qadam bosadi: «(5) qadam yur»."><strong>1-Qadam:</strong> Qahramon oldinga qadam bosadi: «(5) qadam yur».</li>
          <li data-ru="<strong>2-Шаг:</strong> Проверяем: «ЕСЛИ коснулся стены...»" data-en="<strong>Step 2:</strong> Check condition: «IF touching wall...»" data-uz="<strong>2-Qadam:</strong> Shart tekshiriladi: «AGAR qora rangga tegsa...»"><strong>2-Qadam:</strong> Shart tekshiriladi: «AGAR qora rangga tegsa...»</li>
          <li data-ru="<strong>3-Шаг:</strong> Отталкиваем назад: «идти (-5) шагов»!" data-en="<strong>Step 3:</strong> Push back immediately: «move (-5) steps»!" data-uz="<strong>3-Qadam:</strong> Darhol orqaga suramiz: «(-5) qadam yur»!"><strong>3-Qadam:</strong> Darhol orqaga suramiz: «(-5) qadam yur»!</li>
        </ul>
      </div>
      <div>
        <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); padding:16px;">
          <div style="color:var(--green); font-family:var(--font-mono); font-size:12px; margin-bottom:6px;">// Qattiq Devor Skripti:</div>
          <div style="background:#3b82f6; color:#fff; padding:6px 10px; border-radius:4px; font-weight:700; font-size:12px;">(5) qadam yur</div>
          <div style="background:#f59e0b; color:#000; padding:8px 10px; border-radius:4px; font-weight:700; margin-top:4px; font-size:12px;">
            agar &lt; [Qora rang]ga tegdimi? &gt; bo'lsa:
            <div style="background:#3b82f6; color:#fff; padding:6px 10px; border-radius:4px; margin-top:4px;">(-5) qadam yur</div>
          </div>
          <p style="font-size:11px; color:#cbd5e1; margin-top:8px;" data-ru="Результат: Кот мгновенно отскакивает назад, и человеческий глаз видит, что стена непробиваема!" data-en="Result: The cat snaps back instantly, making walls appear completely solid to human eyes!">Natija: Qahramon ko'z ochib yumguncha orqaga tisariladi va inson ko'ziga devor qattiqdek ko'rinadi!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: MAGIC MAZE RULES -->
  <section class="slide" data-phase="Labirint Qoidalari|Правила Лабиринта|Maze Rules" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="СТРОИМ ИГРУ СЕГОДНЯ" data-en="BUILDING OUR GAME TODAY">BUGUNGI O'YINIMIZ</span></div>
    <h2 data-ru="Игра «Волшебный Лабиринт»: 3 Главных Правила" data-en="«Magic Maze» Game: 3 Golden Rules">«Sehrli Labirint» O'yinining 3 Ta Qoidasi</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid #000;">
        <div style="font-size:32px; margin-bottom:6px;">🧱</div>
        <h4 data-ru="1. Черные Стены" data-en="1. Black Walls">1. Qora Tosh Devorlar</h4>
        <p style="font-size:12px;" data-ru="Стены нарисованы черным цветом на фоне. Если кот касается их, он отскакивает назад и издает звук 'Бум!'." data-en="Walls are drawn in solid black. Touching them pushes the cat back with a 'Boing!' sound.">Devorlar qora rangda chiziladi. Qahramon tekkanda orqaga tisariladi va 'Bum!' tovushi chiqadi.</p>
      </div>
      <div class="box" style="border-top:4px solid #ef4444;">
        <div style="font-size:32px; margin-bottom:6px;">🔥</div>
        <h4 data-ru="2. Красные Ловушки" data-en="2. Red Traps">2. Qizil Olov Tuzoqlar</h4>
        <p style="font-size:12px;" data-ru="Опасные зоны! Если кот касается красного цвета, он телепортируется обратно на старт лабиринта!" data-en="Hazard zones! Touching red lava teleports the player right back to the maze start!"><span style="color:#ef4444; font-weight:700;">Xavfli zona!</span> Qizil rangga tegsa, qahramon darhol boshlang'ich nuqtaga (Startga) qaytariladi!</p>
      </div>
      <div class="box" style="border-top:4px solid #10b981;">
        <div style="font-size:32px; margin-bottom:6px;">💎</div>
        <h4 data-ru="3. Зеленый Кристалл" data-en="3. Green Gem">3. Yashil G'alaba Olmosi</h4>
        <p style="font-size:12px;" data-ru="Финиш лабиринта! Если кот касается зеленого кристалла, играет музыка победы и кот кричит 'УРА!'." data-en="Maze finish line! Touching the green gem triggers victory fanfare and 'Hooray!' cheer.">Marraga qo'yilgan olmos! Unga tekkanda g'alaba kuyi yangraydi va "G'ALABA!" yozuvi chiqadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: SOUNDS AND ANIMATION -->
  <section class="slide" data-phase="Ovoz va Effektlar|Звуки и Эффекты|Sounds & Effects" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ОЖИВЛЯЕМ ИГРУ" data-en="MAKING GAMES JUICY">OVOZ VA EMOTSIYALAR</span></div>
    <h2 data-ru="Звуки и Реакции: Пусть Кот Разговаривает!" data-en="Sounds & Reactions: Let the Cat Speak!">Qahramonni Gapirtiramiz va Tovush Qo'shamiz!</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Игра без звуков скучна. Добавим эмоции через блок «Говорить» и звуки Scratch:" data-en="Games without sound feel empty. Add emotions via «Say» blocks and sound FX:">Tovushsiz o'yin zerikarli bo'ladi. Har bir hodisaga o'z ovozini ulaymiz:</p>
        <ul class="clean-list">
          <li data-ru="<strong>При ударе о стену:</strong> Кот говорит «Ой!» на 0.5 секунды и играет звук 'Boing'." data-en="<strong>Hitting wall:</strong> Cat says «Ouch!» for 0.5s and plays 'Boing' sound."><strong>Devorga urilganda:</strong> Mushuk 0.5 soniyaga «Voy!» deb baqiradi va 'Boing' tovushi yangraydi.</li>
          <li data-ru="<strong>При попадании в лаву:</strong> Звук 'Oops!' и возврат на старт." data-en="<strong>Touching lava:</strong> 'Oops!' sound and instant respawn at start."><strong>Olovga tushganda:</strong> 'Oops!' ovozi chiqib, startga qaytadi.</li>
          <li data-ru="<strong>На финише:</strong> Торжественный звук 'Win' и танец радости!" data-en="<strong>At finish:</strong> Victory fanfare 'Win' and celebratory dance!"><strong>Marrada:</strong> Bayramona 'Cheer' ovozi va g'alaba raqsi!</li>
        </ul>
      </div>
      <div>
        <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); padding:16px;">
          <div style="font-size:32px; margin-bottom:6px;">🐱 💬 🎵</div>
          <h4 data-ru="Секрет Геймдева: Обратная Связь" data-en="Game Feel Secret: Feedback">Geym-Dizayn Qoidasi: Feedback</h4>
          <p style="font-size:12px; color:#cbd5e1;" data-ru="Когда игра реагирует звуками на каждое действие игрока, играть становится в 10 раз веселее!" data-en="When a game responds with sound and text to every action, it feels 10 times more fun!">O'yin o'yinchining har bir harakatiga ovoz va gap bilan javob qaytarsa, undan zavqlanish 10 barobar oshadi!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: IN-DECK INTERACTIVE MAZE GAME -->
  <section class="slide" data-phase="Smartboard Labirinti|Игра на Доске|Playable Maze" data-time="40:00–48:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ЖИВАЯ ИГРА НА СМАРТБОРДЕ" data-en="SMARTBOARD LIVE GAME">SMARTBOARDDA JONLI LABIRINT</span></div>
    <h2 data-ru="Попробуй Пройти Волшебный Лабиринт Прямо Сейчас!" data-en="Try Escaping the Magic Maze Right on the Display!">Doskada Sehrli Labirintni O'ynab Ko'ring!</h2>
    <p class="lede" style="font-size:13px; margin-bottom:8px;" data-ru="Управляйте котом стрелками клавиатуры. Не касайтесь черных стен (⬛) и красных ловушек (🟥)! Соберите кристалл (💎)!" data-en="Control the cat with arrow keys. Avoid black walls (⬛) and red traps (🟥)! Reach the green gem (💎)!">Strelkalar bilan qahramonni boshqaring. Qora devorlar (⬛) va qizil tuzoqlardan (🟥) saqlaning! Yashil kristallga (💎) yetib boring!</p>
    
    <div style="background:#090d16; border:1px solid rgba(255,255,255,0.15); border-radius:8px; padding:10px; display:flex; flex-direction:column; align-items:center;">
      <div style="display:flex; justify-content:space-between; width:100%; max-width:580px; margin-bottom:6px; font-family:var(--font-mono); font-size:12px;">
        <span style="color:#38bdf8; font-weight:700;">🐱 Qahramon: Mushukcha</span>
        <span id="deck-maze-status" style="color:#fbbf24; font-weight:700;">Harakatlaning!</span>
        <button id="deck-btn-reset-maze" class="btn" style="padding:2px 8px; font-size:11px; background:#334155; color:#fff;" data-ru="🔄 Старт Заново" data-en="🔄 Reset">🔄 Boshiga Qaytish</button>
      </div>
      <canvas id="deck-maze-canvas" width="580" height="250" style="border:2px solid #334155; border-radius:6px; background:#f8fafc; touch-action:none;"></canvas>
      <div style="font-size:11px; color:#94a3b8; margin-top:6px;">
        ⌨️ <b>Strelkalar / WASD</b>: Harakat | ⬛ <b>Qora Devor</b>: Orqaga tisariladi | 🟥 <b>Qizil Olov</b>: Boshiga qaytaradi | 💎 <b>Olmos</b>: G'alaba!
      </div>
    </div>
  </section>

  <!-- SLIDE 9: QUICK QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Quiz" data-time="48:00–55:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА СМЕКАЛКИ" data-en="LOGIC CHECK">TEZKOR MANTIQ SAVOLLARI</span></div>
    <h2 data-ru="3 Вопроса: Насколько Хорошо Ты Знаешь Условия?" data-en="3 Questions: How Well Do You Know Conditions?">Aqlli Shartlar Bo'yicha 3 Ta Tezkor Savol</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:#dbeafe; color:#1e40af;">1-Savol</div>
        <h4 data-ru="Какого цвета блок «Если... то» в Scratch?" data-en="What color is «If... then» in Scratch?">Scratch'da «Agar... u holda» bloki qaysi rangda?</h4>
        <div class="interactive-opt" onclick="this.classList.toggle('selected');" style="margin-top:8px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">A) Moviy ko'k (Harakat)</div>
        <div class="interactive-opt correct-opt" onclick="this.classList.toggle('selected');" style="margin-top:4px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">B) Sariq-olovrang (Boshqaruv)</div>
      </div>
      <div class="box">
        <div class="tag" style="background:#fef3c7; color:#92400e;">2-Savol</div>
        <h4 data-ru="Как заставить кота отскочить от черной стены?" data-en="How to make cat bounce off black walls?">Qora devorga tekkanda nima buyruq beramiz?</h4>
        <div class="interactive-opt correct-opt" onclick="this.classList.toggle('selected');" style="margin-top:8px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">A) (-10) qadam yur (orqaga tisarilish)</div>
        <div class="interactive-opt" onclick="this.classList.toggle('selected');" style="margin-top:4px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">B) 100 qadam oldinga yugur</div>
      </div>
      <div class="box">
        <div class="tag" style="background:#fee2e2; color:#991b1b;">3-Savol</div>
        <h4 data-ru="Где находятся блоки «Касается цвета»?" data-en="Where are «Touching color» blocks?">«Rangga tegdimi?» bloklari qaysi bo'limda?</h4>
        <div class="interactive-opt correct-opt" onclick="this.classList.toggle('selected');" style="margin-top:8px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">A) Moviy Sezgirlik (Sensing) bo'limida</div>
        <div class="interactive-opt" onclick="this.classList.toggle('selected');" style="margin-top:4px; padding:6px; background:var(--panel-2); border-radius:4px; font-size:11px; cursor:pointer;">B) Qizil Ovozlar bo'limida</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: HANDS-ON WORKSHOP ARENA -->
  <section class="slide" data-phase="Amaliy Dars|Практическая Арена|Hands-on Workshop" data-time="55:00–70:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="СОЗДАЕМ СВОЙ ЛАБИРИНТ В SCRATCH" data-en="BUILDING YOUR SCRATCH MAZE">AMALIYOT: O'Z LABIRINTINGNI YARAT!</span></div>
    <h2 data-ru="4 Шага Создания Игры «Волшебный Лабиринт»" data-en="4 Steps to Build Your Magic Maze Game">4 Bosqichda Scratch'da O'yinimizni Yig'amiz!</h2>
    <div class="grid-2">
      <div>
        <div class="box" style="margin-bottom:8px; border-left:4px solid #3b82f6;">
          <div style="font-weight:700; font-size:11px; color:#2563eb;">1-BOSQICH: Labirint Sahnasini Chizamiz</div>
          <p style="font-size:11px; margin:4px 0; color:var(--ink-2);" data-ru="Нарисуйте фон: черные стены лабиринта, зеленый квадрат финиша и красную полоску лавы." data-en="Draw the backdrop: black maze walls, green finish zone, and a red lava strip.">Fon muharririda qora devorlar bilan labirint chizing, burchakka qizil olov va marraga yashil kvadrat qo'ying.</p>
        </div>
        <div class="box" style="border-left:4px solid #f59e0b;">
          <div style="font-weight:700; font-size:11px; color:#d97706;">2-BOSQICH: Strelkalar Bilan Harakat</div>
          <p style="font-size:11px; margin:4px 0; color:var(--ink-2);" data-ru="Соберите блоки движения для 4 стрелок (Вверх, Вниз, Влево, Вправо)." data-en="Assemble movement blocks for all 4 arrow keys (Up, Down, Left, Right).">Qahramon uchun 4 ta strelka bloklarini yig'ing (Yuqori, Past, Chap, O'ng).</p>
        </div>
      </div>
      <div>
        <div class="box" style="margin-bottom:8px; border-left:4px solid #ef4444;">
          <div style="font-weight:700; font-size:11px; color:#dc2626;">3-BOSQICH: Qora Devor va Qizil Olov Shartlari</div>
          <p style="font-size:11px; margin:4px 0; color:var(--ink-2);" data-ru="Добавьте: «Если касается черного, то шаг (-5)» и «Если касается красного, то перейти на X: -200, Y: 140»." data-en="Add: «If touching black, move (-5)» and «If touching red, go to X: -200, Y: 140».">Qo'shing: «Agar qora rangga tegsa: (-5) qadam yur» va «Agar qizil rangga tegsa: startga qayt».</p>
        </div>
        <div class="box" style="border-left:4px solid #10b981;">
          <div style="font-weight:700; font-size:11px; color:#059669;">4-BOSQICH: Marra va G'alaba Kuyi</div>
          <p style="font-size:11px; margin:4px 0; color:var(--ink-2);" data-ru="«Если касается зеленого, то сказать УРА! и играть победный звук»." data-en="«If touching green, say HOORAY! and play victory sound».">«Agar yashil rangga tegsa: 'G'ALABA!' deb ayt va chiptune g'alaba kuyini chal».</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: PEER REVIEW PLAYTEST -->
  <section class="slide" data-phase="Partadosh Sinovi|Тест Соседа|Peer Playtest" data-time="70:00–74:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРЯЕМ ЛАБИРИНТ ДРУГА" data-en="TESTING FRIEND'S MAZE">PARTADOSH SINOVI</span></div>
    <h2 data-ru="Поменяйтесь Местами: Пройди Лабиринт Соседа!" data-en="Swap Seats: Escape Your Classmate's Maze!">O'rin Almashib Sinfdosh O'yinini Tekshiramiz!</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Поменяйтесь местами с соседом по парте! Сыграйте в его лабиринт и проверьте 3 вещи:" data-en="Swap seats with your neighbor! Play their maze and verify 3 items:">Partadoshingiz bilan o'rin almashing va uning o'yinini 3 ta sinovdan o'tkazing:</p>
        <ul class="clean-list">
          <li data-ru="<strong>1. Стены:</strong> Кот не проходит сквозь черные стены?" data-en="<strong>1. Walls:</strong> Does the sprite bounce off black walls properly?"><strong>1. Devorlar:</strong> Qahramon qora devordan o'tib ketmayaptimi?</li>
          <li data-ru="<strong>2. Ловушка:</strong> Возвращает ли красная лава на старт?" data-en="<strong>2. Lava:</strong> Does the red lava trap respawn player at start?"><strong>2. Olov tuzog'i:</strong> Qizil rangga tekkanda startga qaytaryaptimi?</li>
          <li data-ru="<strong>3. Финиш:</strong> Играет ли музыка при победе?" data-en="<strong>3. Victory:</strong> Does the victory sound play upon touching green?"><strong>3. Marra:</strong> Yashil olmosga yetganda g'alaba tovushi yangrayaptimi?</li>
        </ul>
      </div>
      <div>
        <div class="box" style="background:#090d16; border:1px solid rgba(255,255,255,0.1); padding:16px;">
          <div style="color:var(--accent); font-weight:700; font-size:12px; margin-bottom:6px;">💡 Maslahat:</div>
          <p style="font-size:12px; color:#cbd5e1; margin:0;" data-ru="Если кот застрял внутри стены, уменьшите размер спрайта до 50% в панели свойств!" data-en="If the sprite gets stuck inside corridors, reduce sprite size to 50% in properties!">Agar qahramon yo'lakka sig'may devorga tiqilib qolsa, uning o'lchamini (Size) 50% ga kichraytiring!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: BIG SCREEN SHOWCASE -->
  <section class="slide" data-phase="Katta Ekran|Шоукейс|Showcase" data-time="74:00–77:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ЛУЧШИЕ ЛАБИРИНТЫ КЛАССА" data-en="CLASSROOM SHOWCASE">KATTA EKRAN SHOWCASE</span></div>
    <h2 data-ru="Шоукейс: Проходим Самые Сложные Лабиринты!" data-en="Showcase: Conquering the Hardest Mazes!">Katta Doskada Eng Qiyin Labirintlarni O'ynaymiz!</h2>
    <div class="grid-2">
      <div>
        <div class="box" style="margin-bottom:12px;">
          <div class="tag" style="background:#dcfce7; color:#166534;" data-ru="Турнир Лабиринтов" data-en="Maze Tournament">2 Ta Eng Qiziqarli Labirint</div>
          <p style="font-size:13px; font-weight:600; margin:6px 0;" data-ru="Два ученика с самыми красивыми и хитрыми лабиринтиками выходят к смартборду!" data-en="Two students with the most creative mazes demonstrate their games on the Smartboard!">Eng qiziqarli labirint chizgan 2 nafar o'quvchi doskaga chiqib o'z o'yinini butun sinfga ko'rsatadi!</p>
        </div>
        <ul class="clean-list">
          <li data-ru="У кого самый необычный рисунок коридоров?" data-en="Who created the most inventive maze layout?">Kimning labirint chizmasi eng g'aroyib va chiroyli?</li>
          <li data-ru="Сможет ли учитель пройти ваш лабиринт с первой попытки?" data-en="Can the teacher escape your maze on the first attempt?">O'qituvchi sizning labirintingizdan birinchi urinishda chiqa oladimi?</li>
        </ul>
      </div>
      <div>
        <div class="box" style="text-align:center; padding:24px; background:var(--panel);">
          <div style="font-size:48px; margin-bottom:12px;">🏆</div>
          <h3 data-ru="Мастер Логики Scratch" data-en="Master of Scratch Logic">"Sehrli Labirint Ustasi"</h3>
          <p style="font-size:12px; color:var(--ink-2);" data-ru="Ученик, чей лабиринт работает без единой ошибки и радует класс звуками, получает 10 баллов!" data-en="The student whose maze runs flawlessly with rich sounds wins 10 points!">Devorlari xatolarsiz ishlovchi va qiziqarli tovushlarga ega o'yin muallifi 10 ball oladi!</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: 3-TIER HOMEWORK -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Homework" data-time="77:00–79:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ДОМАШНЕЕ ЗАДАНИЕ (10 БАЛЛОВ)" data-en="HOMEWORK CHALLENGE (10 POINTS)">UYGA KIBER-VAZIFA</span></div>
    <h2 data-ru="3 Уровня: От Простого Лабиринта к Супер-Игре" data-en="3 Tiers: From Core Maze to Epic Game">3 Darajali Labirint Vazifasi (10 Ball)</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid #3b82f6;">
        <div class="tag" style="background:#e0f2fe; color:#0369a1;">1-Daraja: Baza (4 ball)</div>
        <h4 data-ru="Стены и Финиш" data-en="Walls & Finish">Devor va Marra</h4>
        <p style="font-size:12px;" data-ru="Создайте лабиринт: кот слушается стрелок, отскакивает от черных стен и побеждает на зеленом финише." data-en="Build basic maze: arrow controls, bounce off black walls, win upon green finish.">Strelkalar bilan boshqariladigan, qora devordan qaytuvchi va yashil marraga yetganda g'alaba beruvchi o'yin.</p>
      </div>
      <div class="box" style="border-top:4px solid #10b981;">
        <div class="tag" style="background:#dcfce7; color:#15803d;">2-Daraja: Muhandis (4 ball)</div>
        <h4 data-ru="Красная Лава и Звуки" data-en="Red Lava & Sounds">Qizil Olov va Tovushlar</h4>
        <p style="font-size:12px;" data-ru="Добавьте красные ловушки (возврат на старт) и звуки при ударе о стену ('Ой!') и на финише." data-en="Add red lava traps (respawn at start) and sound FX on wall bumps and victory.">Qizil olov tuzoqlari (startga qaytarish) va devorga tekkanda 'Voy!' tovushini qo'shing.</p>
      </div>
      <div class="box" style="border-top:4px solid #8b5cf6;">
        <div class="tag" style="background:#f3e8ff; color:#6b21a8;">3-Daraja: Chempion (2 ball)</div>
        <h4 data-ru="Движущееся Препятствие" data-en="Moving Hazard">Harakatlanuvchi To'siq</h4>
        <p style="font-size:12px;" data-ru="Добавьте вращающийся или двигающийся туда-сюда красный шип с помощью цикла «Повторять всегда»!" data-en="Add a patrolling moving spike obstacle using a «Forever» loop!"><span style="color:#8b5cf6; font-weight:700;">Chempionlik:</span> Labirint ichida u yoqdan-bu yoqqa harakatlanuvchi tikanli to'siq qo'shing!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И ВПЕРЕД" data-en="SUMMARY & WHAT'S NEXT">XULOSA VA KEYINGI BOSQICH</span></div>
    <h2 data-ru="Чему Мы Научились и Что Будет в 30-м Уроке?" data-en="What We Mastered & What's Next in Lesson 30?">Mantiq Zabt Etildi: Bugun Nimalarni O'rgandik?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Сегодня мы сделали огромный шаг в настоящую логику программирования:" data-en="Today we took a massive leap into authentic computer science logic:">Bugun dasturlashning eng asosiy poydevori — mantiqiy shartlarni o'rgandik:</p>
        <ul class="clean-list">
          <li data-ru="Поняли, как работает мозг компьютера через блок «Если… то»." data-en="Understood how computer brains reason via «If… then» blocks.">Kompyuter qanday fikrlashini: «Agar... u holda» blokini o'zlashtirdik.</li>
          <li data-ru="Подключили сенсоры касания цвета и научили кота чувствовать мир." data-en="Connected color sensing blocks to help sprites feel their environment.">Ranglarni sezish datchiklarini ulab, qahramonni devorlarga urilmaslikka o'rgatdik.</li>
          <li data-ru="Создали собственную игру «Волшебный Лабиринт» со звуками и ловушками." data-en="Engineered our own Magic Maze game with sounds and lava hazards.">Tovushlar va tuzoqlarga ega o'z shaxsiy "Sehrli Labirint" o'yinimizni qurdik!</li>
        </ul>
      </div>
      <div>
        <div class="box" style="border-left:4px solid var(--accent); background:var(--panel);">
          <div class="tag" style="background:var(--accent-soft); color:var(--accent);" data-ru="Анонс следующего урока" data-en="Next Lesson Teaser">Keyingi 30-Dars Ko'prigi</div>
          <h3 data-ru="Магия Переменных: Очки и Монеты!" data-en="Variables Magic: Coins & High Scores!">O'zgaruvchilar Sehri: Tangalar va Jonlar (HP)!</h3>
          <p style="font-size:12px; color:var(--ink-2);" data-ru="Как компьютер считает собранные монеты и потраченные жизни? В следующем уроке мы познакомимся с великой Магией Переменных (Variables)!" data-en="How does a game track collected coins and remaining health? Next lesson we unlock the great magic of Variables!">O'yinda yig'ilgan tangalar va yo'qotilgan jonlarni kompyuter qayerda saqlaydi? Keyingi darsda o'yinlarning xotirasi — **O'zgaruvchilar (Variables)** bilan tanishamiz!</p>
        </div>
      </div>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. IN-DECK INTERACTIVE MAZE JS
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
(function() {
  const canvas = document.getElementById('deck-maze-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let cat = { x: 40, y: 40, r: 12 };
  let statusEl = document.getElementById('deck-maze-status');

  // Maze layout (walls in black, lava in red, gem in green)
  const walls = [
    { x: 0, y: 0, w: 580, h: 10 },
    { x: 0, y: 240, w: 580, h: 10 },
    { x: 0, y: 0, w: 10, h: 250 },
    { x: 570, y: 0, w: 10, h: 250 },
    // Inner obstacles
    { x: 100, y: 10, w: 16, h: 160 },
    { x: 200, y: 80, w: 16, h: 160 },
    { x: 300, y: 10, w: 16, h: 160 },
    { x: 400, y: 80, w: 16, h: 160 }
  ];

  const lava = [
    { x: 220, y: 210, w: 76, h: 30 },
    { x: 420, y: 10, w: 146, h: 24 }
  ];

  const gem = { x: 520, y: 200, r: 16 };
  let gameWon = false;

  function reset() {
    cat = { x: 40, y: 40, r: 12 };
    gameWon = false;
    if (statusEl) {
      statusEl.innerText = "Harakatlaning!";
      statusEl.style.color = "#fbbf24";
    }
    render();
  }

  function checkCollision(nx, ny) {
    // Check walls
    for (const w of walls) {
      if (nx + cat.r > w.x && nx - cat.r < w.x + w.w &&
          ny + cat.r > w.y && ny - cat.r < w.y + w.h) {
        return "wall";
      }
    }
    // Check lava
    for (const l of lava) {
      if (nx + cat.r > l.x && nx - cat.r < l.x + l.w &&
          ny + cat.r > l.y && ny - cat.r < l.y + l.h) {
        return "lava";
      }
    }
    // Check gem
    const dx = nx - gem.x;
    const dy = ny - gem.y;
    if (Math.sqrt(dx*dx + dy*dy) < cat.r + gem.r) {
      return "gem";
    }
    return "ok";
  }

  function render() {
    ctx.fillStyle = '#f8fafc';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw walls (Black)
    ctx.fillStyle = '#0f172a';
    for (const w of walls) {
      ctx.fillRect(w.x, w.y, w.w, w.h);
    }

    // Draw lava (Red)
    ctx.fillStyle = '#ef4444';
    for (const l of lava) {
      ctx.fillRect(l.x, l.y, l.w, l.h);
    }

    // Draw Gem (Green diamond)
    ctx.fillStyle = '#10b981';
    ctx.beginPath();
    ctx.arc(gem.x, gem.y, gem.r, 0, Math.PI * 2);
    ctx.fill();
    ctx.font = '16px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('💎', gem.x, gem.y);

    // Draw Cat
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath();
    ctx.arc(cat.x, cat.y, cat.r, 0, Math.PI * 2);
    ctx.fill();
    ctx.font = '16px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('🐱', cat.x, cat.y);

    if (gameWon) {
      ctx.fillStyle = 'rgba(15, 23, 42, 0.88)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = '#4ade80';
      ctx.font = 'bold 22px system-ui';
      ctx.textAlign = 'center';
      ctx.fillText("🎉 G'ALABA! SEHRLI OLMOSTI OLDINGIZ! 🎉", canvas.width/2, canvas.height/2 - 10);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '13px system-ui';
      ctx.fillText("Qora devorlar va qizil tuzoqlardan omon o'tdingiz!", canvas.width/2, canvas.height/2 + 18);
    }
  }

  window.addEventListener('keydown', (e) => {
    if (gameWon) return;
    let dx = 0, dy = 0;
    const speed = 8;
    if (e.key === 'ArrowUp' || e.key === 'w') dy = -speed;
    else if (e.key === 'ArrowDown' || e.key === 's') dy = speed;
    else if (e.key === 'ArrowLeft' || e.key === 'a') dx = -speed;
    else if (e.key === 'ArrowRight' || e.key === 'd') dx = speed;
    else return;

    const res = checkCollision(cat.x + dx, cat.y + dy);
    if (res === "ok") {
      cat.x += dx;
      cat.y += dy;
    } else if (res === "wall") {
      // Bounce back
      if (statusEl) {
        statusEl.innerText = "💥 Devorga urildi! (-5 qadam)";
        statusEl.style.color = "#ef4444";
      }
    } else if (res === "lava") {
      cat.x = 40;
      cat.y = 40;
      if (statusEl) {
        statusEl.innerText = "🔥 Olovga tushdi! Startga qaytarildi!";
        statusEl.style.color = "#ef4444";
      }
    } else if (res === "gem") {
      cat.x = gem.x;
      cat.y = gem.y;
      gameWon = true;
      if (statusEl) {
        statusEl.innerText = "🎉 G'ALABA!";
        statusEl.style.color = "#10b981";
      }
    }
    render();
  });

  const btnReset = document.getElementById('deck-btn-reset-maze');
  if (btnReset) btnReset.addEventListener('click', reset);

  reset();
})();
"""

# -----------------------------------------------------------------------------
# 3. TEACHER NOTES DATA (14 Slides Trilingual Triplets)
# -----------------------------------------------------------------------------
triplets_uz = [
    ["Kirish va Maqsad", "O'quvchilarga bugungi missiya: qahramonga 'aql' berish — Agar... u holda shartlari va Sehrli Labirint o'yinini qurish ekanini ayting.", "Doskaga 'Agar... u holda' blokining oltiburchak shaklini chizing."],
    ["Uy Vazifasi Tahlili", "28-darsdagi Game Jam xatolarini eslang: qahramon devorlardan arvohdek o'tib ketganini ayting.", "Yechim: 'qora rangga tegsa (-10) qadam yur' orqaga tisarilish kodi ekanini ko'rsating."],
    ["Shartlar Tushunchasi", "Hayotiy misollar keltiring: yomg'ir yog'sa soyabon olamiz, svetofor qizil bo'lsa to'xtaymiz.", "O'quvchilardan o'z hayotlaridagi shartli qoidalarni so'rang."],
    ["Sezgirlik Bloklari", "Moviy Sezgirlik bo'limidagi 3 ta asosiy blokni ko'rsating: rangga tegdimi, spraytga tegdimi, tugma bosildimi.", "Oltiburchak datchik faqat 'HA' yoki 'YO'Q' deb javob berishini tushuntiring."],
    ["Qattiq Devor Qoidasi", "Kompyuterga devorni qattiq qilish siri: oldinga 5 qadam bosish va devorga tegsa darhol 5 qadam orqaga surish.", "Bu ko'z ochib yumguncha bo'lgani uchun devor qattiqdek ko'rinishini ayting."],
    ["Sehrli Labirint Qoidalari", "O'yinning 3 qoidasi: qora devor (orqaga tisarilish), qizil olov (startga qaytish) va yashil olmos (g'alaba).", "Doskada mini-labirint chizmasini ko'rsating."],
    ["Ovoz va Emotsiyalar", "Har bir to'qnashuvga tovush qo'shish: devorga urilganda 'Voy!', marraga yetganda 'Ura!' deyish.", "Geym-dizaynda audio feedback o'yinni 10 barobar qiziq qilishini ayting."],
    ["Smartboard Jonli O'yini", "8-slaydni oching: o'quvchilarni doskaga chaqirib qora devor va qizil olovdan qochirib olmosga yetkazing.", "Butun sinf bilan qahramonni boshqarishni tomosha qiling."],
    ["Tezkor Viktorina", "3 ta tezkor savol orqali shartlar va sezgirlik bloklarini mustahkamlang.", "To'g'ri javob bergan o'quvchilarni rag'batlantiring."],
    ["Amaliy Dars Arenasi", "O'quvchilar Scratch dasturini ochib, 4 bosqichda o'z labirintlarini yig'adilar.", "Zaldan aylanib qora devordan o'tib ketayotganlarga orqaga tisarilish kodini eslatib turing."],
    ["Partadosh Sinovi", "Partadoshlar o'rin almashib, bir-birining labirintidan o'tishga harakat qilsin.", "Katta qahramon yo'lakka sig'masa, o'lchamini 50% qilishni o'rgating."],
    ["Katta Ekran Showcasi", "Eng qiziqarli labirint yaratgan 2 nafar o'quvchini doskaga chaqirib namoyish qildiring.", "Sinfdoshlar ularning labirintini o'ynab ko'rsin."],
    ["Uyga Kiber-Vazifa", "10 ballik mezonni tushuntiring: baza labirint, qizil olov va ovozlar, harakatlanuvchi to'siq.", "Vazifa ilovasida LocalStorage avto-saqlanishini eslatib o'ting."],
    ["Xulosa va Keyingi Dars", "Bugun qahramonimizga fikrlash va sezishni o'rgatganimizni xulosa qiling.", "Keyingi 30-darsda o'yinlarning xotirasi — O'zgaruvchilar (Variables) va ballar hisobini anons qiling."]
]

triplets_ru = [
    ["Введение и Цель", "Расскажите ученикам о миссии: научить персонажа думать через условия 'Если... то' и построить игру 'Волшебный Лабиринт'.", "Нарисуйте на доске шестиугольный блок условия Scratch."],
    ["Разбор ДЗ", "Вспомните частую ошибку 28-го урока: кот проваливался сквозь стены как призрак.", "Покажите золотой стандарт: блок 'отскока' назад при касании черного цвета."],
    ["Понятие Условий", "Приведите примеры из жизни: зонт при дожде, остановка на красный свет.", "Спросите у ребят их примеры повседневных условий."],
    ["Блоки Сенсоров", "Покажите 3 блока из голубого раздела Сенсоры: касание цвета, касание спрайта, клавиша нажата.", "Объясните логику ответов ДА / НЕТ."],
    ["Секрет Твердых Стен", "Объясните механику: шаг вперед на 5, и если коснулся стены — мгновенный шаг назад на (-5).", "Человеческий глаз видит непреодолимую твердую стену."],
    ["Правила Лабиринта", "3 правила игры: черные стены (отскок), красная лава (старт) и зеленый кристалл (победа).", "Продемонстрируйте схему уровней на доске."],
    ["Звуки и Эмоции", "Добавьте озвучку: звук 'Ой!' при ударе и победная музыка на финише.", "Подчеркните важность звукового отклика для удовольствия от игры."],
    ["Игра на Смартборде", "Откройте 8-й слайд: вызовите учеников к доске пройти лабиринт стрелками клавиатуры.", "Уворачивайтесь от лавы и заберите кристалл."],
    ["Быстрый Квиз", "Закрепите понятия условий через 3 интерактивных вопроса на слайде.", "Похвалите класс за активные правильные ответы."],
    ["Практическая Арена", "Ученики открывают Scratch и за 4 шага строят свой собственный лабиринт.", "Проходите по рядам и помогайте настраивать касания цветов."],
    ["Тест Соседа", "Ученики меняются местами и пробуют пройти лабиринт соседа по парте.", "Если кот застревает, уменьшите размер спрайта до 50%."],
    ["Шоукейс на Доске", "Вызовите двух авторов самых хитрых лабиринтов на смартборд.", "Проведите турнир на прохождение перед всем классом."],
    ["Домашнее Задание", "Объясните 10-балльную рубрику: базовый лабиринт, лава со звуками, движущееся препятствие.", "Напомните про автосохранение ответов в приложении vazifa.html."],
    ["Итоги и Анонс", "Подведите итог: сегодня персонаж обрел разум и научился чувствовать мир.", "Анонсируйте 30-й урок: переменные, монеты и подсчет жизней (HP)."]
]

triplets_en = [
    ["Intro & Mission", "Introduce the mission: empowering sprites with reasoning via «If... then» logic and engineering the Magic Maze game.", "Draw the hexagonal Scratch condition block on the board."],
    ["Homework Review", "Review lesson 28 pitfall: sprites clipping through walls like ghosts without collisions.", "Demonstrate the bounce-back code standard on color collision."],
    ["Concept of Conditions", "Provide real-world analogies: umbrellas on rainy days, stopping on red lights.", "Ask students for daily if-then rules."],
    ["Sensing Blocks", "Introduce 3 core cyan sensing blocks: touching color, touching sprite, key pressed.", "Explain Boolean YES/NO evaluation."],
    ["Solid Wall Mechanics", "Explain collision resolution: take 5 steps forward, and if touching wall, step (-5) backwards instantly.", "Visual trick creates the illusion of impenetrable solid rock."],
    ["Magic Maze Rules", "3 core rules: black walls (bounce), red lava (teleport to start), green gem (victory fanfare).", "Diagram the maze corridors on the display."],
    ["Sound & Emotional Juice", "Add audio reactions: 'Ouch!' upon wall impact and celebratory cheer at finish.", "Highlight how responsive audio feedback makes games 10x more fun."],
    ["Smartboard Live Play", "Open slide 8: invite students to navigate the interactive maze directly on screen.", "Dodge red lava and grab the emerald diamond!"],
    ["Quick Quiz", "Reinforce conditional logic via 3 interactive questions.", "Reward quick and accurate answers."],
    ["Workshop Arena", "Students launch Scratch and engineer their custom maze game across 4 structured steps.", "Walk the room and help fine-tune color picker tolerances."],
    ["Peer Playtest", "Students swap seats to playtest classmate mazes.", "Advise shrinking sprite size to 50% if corridors feel too narrow."],
    ["Big Screen Showcase", "Invite 2 students with coolest maze layouts to demonstrate gameplay on the display.", "Cheer on maze escapes with the entire class."],
    ["Homework Challenge", "Explain 10-point rubric: base maze, lava traps & audio, and a patrolling moving hazard.", "Remind them of LocalStorage auto-save in vazifa.html."],
    ["Summary & Bridge", "Summarize achievements: our sprite now perceives and reasons about obstacles.", "Tease lesson 30: Variables, coins, and health points (HP)."]
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

    title_uz = "29-dars: Aqlli Shartlar: Agar... U Holda va Sezgirlik Bloklari"
    title_ru = "Урок 29: Умные Условия: «Если… То» и Блоки Сенсоров в Scratch"
    title_en = "Lesson 29: Smart Conditions: «If… Then» & Sensing Blocks in Scratch"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="5–6 КЛАСС" data-en="GRADES 5–6">5–6-SINF</span>',
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

    title_uz = "29-dars: Aqlli Shartlar va Sezgirlik Bloklari — Ish Varaqasi"
    title_ru = "Урок 29: Умные Условия и Сенсоры в Scratch — Рабочий лист"
    title_en = "Lesson 29: Smart Conditions & Sensing Blocks — Worksheet"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<h1>.*?</h1>',
                 f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>',
                 tpl)

    sec1_html = """
    <p class="lead" style="font-size:12px; margin-bottom:8px;" data-ru="<strong>Миссия Урока:</strong> Научить персонажа Scratch думать и чувствовать мир через блоки «Если... то» и сенсоры касания, а также создать игру «Волшебный Лабиринт»." data-en="<strong>Lesson Mission:</strong> Empower Scratch sprites to reason and sense obstacles via «If... then» logic and color sensors, creating the playable Magic Maze game."><strong>Dars Missiyasi:</strong> Qahramonimizga fikrlash va sezish qobiliyatini berish: Scratch "Agar... u holda" shartlari, rang va to'siqlarga tegish datchiklari hamda "Sehrli Labirint" o'yinini yaratish.</p>
    <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="3 Главных Правила Игры «Волшебный Лабиринт»:" data-en="3 Rules of the Magic Maze Game:">Sehrli Labirint O'yinining 3 Qoidasi:</div>
      <div>1. <strong>Qora Tosh Devor:</strong> <span data-ru="При касании черного цвета спрайт отскакивает назад: идти (-5) шагов" data-en="Touching black color pushes sprite backward: move (-5) steps">Qora rangga tekkanda orqaga tisariladi: (-5) qadam yur</span>.</div>
      <div>2. <strong>Qizil Olov Tuzog'i:</strong> <span data-ru="При касании красного цвета спрайт возвращается на старт лабиринта" data-en="Touching red lava teleports sprite back to maze starting point">Qizil rangga tekkanda boshlang'ich nuqtaga (Startga) qaytariladi</span>.</div>
      <div>3. <strong>Yashil Olmos (Marra):</strong> <span data-ru="При касании зеленого кристалла звучит победный звук и слово УРА!" data-en="Touching green gem triggers victory sound and 'Hooray!' cheer">Yashil olmosga yetganda g'alaba kuyi yangraydi va g'alaba beriladi</span>.</div>
    </div>
    """

    sec2_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="Скрипт проверки касания черной стены:" data-en="Black wall collision detection script:">Qora devorga tegishni tekshirish kodi:</p>
    <pre style="background:var(--surface-2); padding:6px; font-size:11px; border-radius:4px; margin:0;"><code class="language-scratch">// Strelkalar bilan harakatlanganda devorni tekshiramiz:
agar &lt; [Qora rang]ga tegdimi? &gt; bo'lsa:
    (-5) qadam yur
    ovozni chal [Boing]
    ayt [Voy!] 0.5 soniya</code></pre>
    """

    sec3_html = """
    <div style="font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="Паспорт Игры «Волшебный Лабиринт»:" data-en="Magic Maze Game Profile:">Sehrli Labirint O'yini Pasporti:</div>
      <div>🐱 <strong>Qahramon:</strong> Mushukcha (o'lchami 50%)</div>
      <div>🎯 <strong>Maqsadi:</strong> Qora devorlar va olovdan saqlanib, yashil olmosga yetib borish.</div>
      <div>🧱 <strong>To'siqlar:</strong> Qora devorlar (-5 qadam), Qizil olov (Startga qaytish).</div>
    </div>
    """

    sec4_html = """
    <div style="display:flex; flex-direction:column; gap:8px; font-size:11px;">
      <div style="border:1px solid var(--rule); border-radius:4px; padding:6px;">
        <div style="font-weight:700; color:var(--accent-ink);" data-ru="Задание 1: Свое Условие из Жизни" data-en="Task 1: Real Life If-Then Rule">1-Topshiriq: O'z Hayotingizdagi Bitta Shartni Yozing</div>
        <p style="margin:2px 0 4px; font-size:8.5pt;" data-ru="«ЕСЛИ ..., ТО ...» shaklida bitta hayotiy qoidani yozing (masalan, yomg'ir yoki dars):" data-en="Write one real-life «IF ..., THEN ...» rule:">«AGAR ..., U HOLDA ...» shaklida bitta hayotiy qoidangizni yozing:</p>
        <div style="border-bottom:1px dashed #cbd5e1; height:20px;"></div>
      </div>
      <div style="border:1px solid var(--rule); border-radius:4px; padding:6px;">
        <div style="font-weight:700; color:var(--accent-ink);" data-ru="Задание 2: Блоки для Финиша" data-en="Task 2: Finish Line Blocks">2-Topshiriq: Marraga Yetganda Nima Sodir Bo'ladi?</div>
        <p style="margin:2px 0 4px; font-size:8.5pt;" data-ru="Какие блоки должен выполнить Scratch при касании героем зеленого кристалла?" data-en="Which blocks should Scratch execute upon reaching the green gem?">Qahramon yashil olmosga tekkanda Scratch qaysi bloklarni bajarishi kerak?</p>
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
          <td style="padding:4px; border:1px solid var(--rule); font-weight:600;" data-ru="Стены лабиринта" data-en="Maze Walls">Qora devorlar va harakat</td>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:700; color:var(--green);" data-ru="4 балла" data-en="4 pts">4 ball</td>
          <td style="padding:4px; border:1px solid var(--rule);" data-ru="Кот слушается стрелок и отскакивает от черных стен." data-en="Cat moves on arrows and bounces off black walls.">Qahramon strelkalar bilan yuradi va qora devordan qaytadi.</td>
        </tr>
        <tr>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:600;" data-ru="Красная лава и финиш" data-en="Red Lava & Finish">Qizil olov va yashil marra</td>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:700; color:var(--green);" data-ru="4 балла" data-en="4 pts">4 ball</td>
          <td style="padding:4px; border:1px solid var(--rule);" data-ru="Лава возвращает на старт, кристалл дает победу." data-en="Lava teleports to start, gem triggers victory.">Qizil olov startga qaytaradi, yashil olmos g'alaba beradi.</td>
        </tr>
        <tr>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:600;" data-ru="Звуки и эффекты" data-en="Audio & Polish">Tovushlar va so'zlar</td>
          <td style="padding:4px; border:1px solid var(--rule); font-weight:700; color:var(--green);" data-ru="2 балла" data-en="2 pts">2 ball</td>
          <td style="padding:4px; border:1px solid var(--rule);" data-ru="Звук 'Ой!' при ударе и победная музыка на финише." data-en="Sound on bump and victory fanfare.">Devorga tekkanda 'Voy!' tovushi va marrada g'alaba kuyi.</td>
        </tr>
      </tbody>
    </table>
    """

    replacements = {
        "{{LESSON_NUM}}": "29",
        "{{TITLE_UZ}}": "Aqlli Shartlar: Agar... U Holda va Sezgirlik Bloklari",
        "{{TITLE_RU}}": "Умные Условия: «Если… То» и Блоки Сенсоров в Scratch",
        "{{TITLE_EN}}": "Smart Conditions: «If… Then» & Sensing Blocks in Scratch",
        "{{COHORT_LABEL_UZ}}": "5–6-SINF",
        "{{COHORT_LABEL_RU}}": "5–6 КЛАСС",
        "{{COHORT_LABEL_EN}}": "GRADES 5–6",
        "{{META_UZ}}": "11-Hafta · Juftlik Dars (80 daqiqa) · Junior Creators & Scratch Track",
        "{{META_RU}}": "11-я Неделя · Сдвоенный Урок (80 минут) · Направление Scratch и Junior Creators",
        "{{META_EN}}": "Week 11 · Double Block (80 min) · Junior Creators & Scratch Track",
        "{{MISSION_UZ}}": "Qahramonimizga fikrlash va sezish qobiliyatini berish: Scratch 'Agar... u holda' shartlari, rang va to'siqlarga tegish datchiklari hamda 'Sehrli Labirint' o'yinini yaratish.",
        "{{MISSION_RU}}": "Научить персонажа Scratch думать и чувствовать мир через блоки «Если... то» и сенсоры касания, а также создать игру «Волшебный Лабиринт».",
        "{{MISSION_EN}}": "Empower Scratch sprites to reason and sense obstacles via «If... then» logic and color sensors, creating the playable Magic Maze game.",
        "{{SEC1_TITLE_UZ}}": "Sehrli Labirint O'yinining 3 Qoidasi",
        "{{SEC1_TITLE_RU}}": "3 Правила Игры «Волшебный Лабиринт»",
        "{{SEC1_TITLE_EN}}": "3 Rules of the Magic Maze Game",
        "{{SEC1_CONTENT}}": sec1_html,
        "{{SEC2_TITLE_UZ}}": "Qora Devorga Tegishni Tekshirish Kodi",
        "{{SEC2_TITLE_RU}}": "Скрипт Проверки Касания Черной Стены",
        "{{SEC2_TITLE_EN}}": "Black Wall Collision Detection Script",
        "{{SEC2_CONTENT}}": sec2_html,
        "{{SEC3_TITLE_UZ}}": "Sehrli Labirint O'yini Pasporti va Topshiriqlar",
        "{{SEC3_TITLE_RU}}": "Паспорт Игры «Волшебный Лабиринт» и Задания",
        "{{SEC3_TITLE_EN}}": "Magic Maze Game Profile & Tasks",
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
      <h4 data-ru="Задание 1: Условие для Черной Стены" data-en="Task 1: Black Wall Bounce Condition">1-Topshiriq: Qora Devor Sharti</h4>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Опишите, какие блоки нужно соединить в Scratch, чтобы персонаж отскакивал назад при ударе о черную стену:" data-en="Describe which Scratch blocks must connect to make the sprite bounce back from black walls:">Scratch'da qahramon qora devorga tekkanda orqaga tisarilishi uchun qaysi bloklarni birlashtirish kerakligini yozing:</p>
      <textarea id="hw-t1" class="hw-input" style="width:100%; height:75px; font-family:var(--font-mono); font-size:12px;" placeholder="Bloklar ketma-ketligi..." data-placeholder-ru="Последовательность блоков..." data-placeholder-en="Sequence of blocks..."></textarea>
      <button class="btn" style="margin-top:6px; padding:4px 10px; font-size:11px;" onclick="document.getElementById('sol-t1').style.display='block';" data-ru="💡 Показать Решение" data-en="💡 View Solution">💡 Yechimni Ko'rish</button>
      <div id="sol-t1" style="display:none; margin-top:6px; padding:8px; background:var(--panel-2); border-radius:4px; font-size:11px; font-family:var(--font-mono); color:var(--green);">
        // Oltin Yechim:<br>
        1. "agar &lt; [Qora rang]ga tegdimi? &gt; bo'lsa:"<br>
        2. ichiga: "(-5) qadam yur"<br>
        3. va ovoz: "ovozni chal [Boing]"
      </div>
    </div>
    """

    task2 = """
    <div style="margin-bottom:12px;">
      <h4 data-ru="Задание 2: Ловушка Красной Лавы" data-en="Task 2: Red Lava Hazard">2-Topshiriq: Qizil Olov Tuzog'i</h4>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Какая команда возвращает кота в самое начало лабиринта при касании красного цвета?" data-en="Which block command teleports the cat back to the start upon touching red lava?">Qahramon qizil olovga tekkanda uni labirint boshiga (Start koordinatalariga) qanday qaytaramiz?</p>
      <textarea id="hw-t2" class="hw-input" style="width:100%; height:65px; font-family:var(--font-mono); font-size:12px;" placeholder="Javobingizni yozing..." data-placeholder-ru="Напишите ваш ответ..." data-placeholder-en="Write your answer..."></textarea>
      <button class="btn" style="margin-top:6px; padding:4px 10px; font-size:11px;" onclick="document.getElementById('sol-t2').style.display='block';" data-ru="💡 Показать Решение" data-en="💡 View Solution">💡 Yechimni Ko'rish</button>
      <div id="sol-t2" style="display:none; margin-top:6px; padding:8px; background:var(--panel-2); border-radius:4px; font-size:11px; font-family:var(--font-mono); color:var(--green);">
        // To'g'ri Javob:<br>
        "agar &lt; [Qizil rang]ga tegdimi? &gt; bo'lsa: X: -200, Y: 140 ga o't" (Start nuqtasi koordinatalari).
      </div>
    </div>
    """

    task3 = """
    <div style="margin-bottom:12px;">
      <h4 data-ru="Задание 3: Финиш и Победный Звук" data-en="Task 3: Victory Gem & Sound">3-Topshiriq: Yashil Olmos va G'alaba Kuyi</h4>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Как запрограммировать радость персонажа при победе на зеленом кристалле?" data-en="How to program the sprite's celebration upon reaching the green gem?">Qahramon yashil olmosga yetganda nima deb qichqirishi va qanday ovoz chiqarishini yozing:</p>
      <textarea id="hw-t3" class="hw-input" style="width:100%; height:65px; font-family:var(--font-mono); font-size:12px;" placeholder="G'alaba bloklari..." data-placeholder-ru="Блоки победы..." data-placeholder-en="Victory blocks..."></textarea>
      <button class="btn" style="margin-top:6px; padding:4px 10px; font-size:11px;" onclick="document.getElementById('sol-t3').style.display='block';" data-ru="💡 Показать Решение" data-en="💡 View Solution">💡 Yechimni Ko'rish</button>
      <div id="sol-t3" style="display:none; margin-top:6px; padding:8px; background:var(--panel-2); border-radius:4px; font-size:11px; font-family:var(--font-mono); color:var(--green);">
        // G'alaba Bloki:<br>
        "agar &lt; [Yashil rang]ga tegdimi? &gt; bo'lsa: 'G'ALABA!' deb ayt 2 soniya va ovozni chal [Cheer] oxirigacha".
      </div>
    </div>
    """

    task4 = """
    <div style="margin-bottom:12px;">
      <h4 data-ru="Задание 4: Движущаяся Ловушка (Супер-Уровень)" data-en="Task 4: Moving Hazard Challenge">4-Topshiriq: Harakatlanuvchi Tikanli To'siq</h4>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Как заставить опасный шип двигаться вверх и вниз внутри лабиринта?" data-en="How to make a hazard spike patrol up and down inside the maze?">Labirint ichida qizil tikan u yoqdan-bu yoqqa tinimsiz harakatlanishi uchun qaysi sikl blokidan foydalanamiz?</p>
      <textarea id="hw-t4" class="hw-input" style="width:100%; height:65px; font-family:var(--font-mono); font-size:12px;" placeholder="Tikan harakati kodi..." data-placeholder-ru="Код движения шипа..." data-placeholder-en="Spike movement code..."></textarea>
      <button class="btn" style="margin-top:6px; padding:4px 10px; font-size:11px;" onclick="document.getElementById('sol-t4').style.display='block';" data-ru="💡 Показать Решение" data-en="💡 View Solution">💡 Yechimni Ko'rish</button>
      <div id="sol-t4" style="display:none; margin-top:6px; padding:8px; background:var(--panel-2); border-radius:4px; font-size:11px; font-family:var(--font-mono); color:var(--green);">
        // Super Yechim:<br>
        "doim takrorla (Forever) bloki ichiga: 1 soniyada X: 50, Y: 100 ga suz, keyin 1 soniyada X: 50, Y: -100 ga suz".
      </div>
    </div>
    """

    tasks_html = task1 + task2 + task3 + task4

    replacements = {
        "{{TITLE_UZ}}": "29-dars: Aqlli Shartlar: Agar... U Holda va Sezgirlik Bloklari",
        "{{TITLE_RU}}": "Урок 29: Умные Условия: «Если… То» и Блоки Сенсоров в Scratch",
        "{{TITLE_EN}}": "Lesson 29: Smart Conditions: «If… Then» & Sensing Blocks in Scratch",
        "{{COHORT_LABEL_UZ}}": "5–6-SINF",
        "{{HERO_TAG_UZ}}": "11-Hafta · Junior Creators & Scratch Track",
        "{{HERO_DESC_UZ}}": "Uyingizda mustaqil ravishda Scratch shartlari (Agar... u holda), qora devorlar bilan to'qnashuv va qizil tuzoqlar ustida mashq qiling.",
        "{{HERO_DESC_RU}}": "Попрактикуйтесь дома с условиями Scratch («Если... то»), столкновениями со стенами и ловушками лавы.",
        "{{HERO_DESC_EN}}": "Practice Scratch conditional logic («If... then»), solid wall collisions, and lava traps at home.",
        "{{RUBRIC_T1_UZ}}": "1-Bosqich: Baza (Qora devordan orqaga qaytish)",
        "{{RUBRIC_T1_RU}}": "1-й Уровень: База (Отскок от черной стены)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (Bounce back from black walls)",
        "{{RUBRIC_T2_UZ}}": "2-Bosqich: Muhandis (Qizil olov va g'alaba olmosi)",
        "{{RUBRIC_T2_RU}}": "2-й Уровень: Практика (Красная лава и победный кристалл)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Red lava hazard and victory gem)",
        "{{RUBRIC_T3_UZ}}": "3-Bosqich: Kiber-Chaqiruv (Harakatlanuvchi tikanli to'siq)",
        "{{RUBRIC_T3_RU}}": "3-й Уровень: Вызов (Движущийся шип-препятствие)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (Patrolling moving hazard spike)",
        "{{TASKS_HTML}}": tasks_html,
        "{{LESSON_SLUG}}": "5-6-w11-l29-aqlli-shartlar-va-sezgirlik"
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")


def build_teacher_guide():
    guide_md = """# O'qituvchi Qo'llanmasi: 29-Dars — Aqlli Shartlar: Agar... U Holda va Sezgirlik Bloklari

**Sinf:** 5–6-sinf · **Format:** 80 daqiqalik Juftlik Dars · **Yo'nalish:** Junior Creators & Scratch

---

## 🎯 Asosiy Pedagogik Maqsad
Bugun 5–6-sinf o'quvchilari dasturlashning eng muhim fundamenti — **Shartlar ("Agar... u holda" / If... then)** va **Sezgirlik (Sensing / "Tegdimi?")** bloklarini o'rganadilar!

O'quvchilar ko'r-ko'rona harakat qiluvchi qahramondan devorlarni sezadigan, qizil tuzoqdan qochadigan va yashil marraga yetganda g'alaba qozonadigan **"Sehrli Labirint"** o'yinini yaratadilar.

---

## ⏱️ 80 Daqiqalik Dars Vaqti Taqsimoti

| Vaqt | Bosqich | O'qituvchi Harakati va Faoliyat |
|---|---|---|
| **00:00–08:00** | **HW Review & Ko'prik** | 28-dars Game Jam tahlili: qahramon devordan arvohdek o'tib ketganini eslash. Blitz savol: "Robotga faqat kaliti bo'lsa eshikni och deb qanday aytamiz? Albatta 'Agar' bloki bilan!" |
| **08:00–20:00** | **Yangi Mavzu Tushunchasi** | Hayotiy shartlar (yomg'ir, svetofor). Moviy sezgirlik datchiklari. Qattiq devor siri: oldinga 5 qadam, tekkanda darhol -5 qadam orqaga tisarilish. |
| **20:00–30:00** | **Smartboardda Jonli O'yin** | 8-slaydni ochish: o'quvchilarni doskaga chaqirib 'Sehrli Labirint'ni strelkalar bilan o'ynatish. Qora devorga urilish va qizil olovdan qochish. |
| **30:00–35:00** | **Tezkor Mantiq Viktorinasi** | 3 ta tezkor savol orqali tushunchalarni mustahkamlash. |
| **35:00–65:00** | **30 Minutlik Katta Scratch Ustaxonasi** | O'quvchilar Scratch dasturida (yoki playgroundda) o'z labirintlarini chizib, qora devor, qizil tuzoq va yashil marra bloklarini yig'adilar. |
| **65:00–74:00** | **Partadosh Sinovi (Playtest)** | Partadoshlar o'rin almashib, bir-birining labirintidan o'tishga harakat qilishadi. Qahramon tiqilsa, o'lchamini 50% qilish o'rgatiladi. |
| **74:00–77:00** | **Katta Ekran Showcasi** | Eng chiroyli labirint chizgan 2 nafar o'quvchi o'z o'yinini katta doskada namoyish qiladi. |
| **77:00–80:00** | **Uy Vazifasi va Yakun** | 10 ballik uy vazifasi tushuntiriladi. Keyingi 30-dars (O'zgaruvchilar va tangalar) e'lon qilinadi. |
"""

    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(guide_md)
    print("  ✓ Created: TEACHER_READING.md")


def build_standalone_playground():
    playground_html = f"""<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Sehrli Labirint — Игровая Площадка Scratch" data-en="Magic Maze — Scratch Playground">Sehrli Labirint — Scratch Maydonchasi</title>
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
      background: #f8fafc;
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
    <span style="color:#38bdf8;" data-ru="🐱 Персонаж: Кот" data-en="🐱 Sprite: Cat">🐱 Qahramon: Mushukcha</span>
    <span id="deck-maze-status" style="color:#fbbf24;" data-ru="Двигайтесь к кристаллу!" data-en="Navigate to the gem!">Harakatlaning!</span>
    <button id="deck-btn-reset-maze" style="padding:2px 8px; font-size:11px; background:#334155; color:#fff; border:none; border-radius:4px; cursor:pointer;" data-ru="🔄 Старт Заново" data-en="🔄 Reset">🔄 Boshiga Qaytish</button>
  </div>
  <canvas id="deck-maze-canvas" width="580" height="250"></canvas>
  <div class="controls" data-ru="⌨️ Стрелки/WASD: Движение | ⬛ Черная стена: Отскок | 🟥 Лава: Старт | 💎 Кристалл: Победа" data-en="⌨️ Arrows/WASD: Move | ⬛ Black Wall: Bounce | 🟥 Lava: Start | 💎 Gem: Win">
    ⌨️ <b>Strelkalar / WASD</b>: Harakat | ⬛ <b>Qora Devor</b>: Orqaga qaytish | 🟥 <b>Qizil Olov</b>: Startga qaytarish | 💎 <b>Olmos</b>: G'alaba!
  </div>

  <script>
{SIMULATOR_JS}
  </script>
</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "playground", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(playground_html)
    print("  ✓ Created: playground/index.html")


if __name__ == "__main__":
    print("🚀 Building 5–6th Grade Week 11 Lesson 29: Aqlli Shartlar va Sezgirlik...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_guide()
    build_standalone_playground()
    print("✅ All Lesson 29 files successfully compiled!")
