#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_5_6_w12_l30.py — Builder for 5–6th Grade, Week 12, Lesson 30

Mavzu: O'zgaruvchilar Sehri: Tangalar, Jonlar (HP) va Vaqt Hisobi
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 5-6-sinf (Junior Creators & Kiber-Gigiyena Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "5-6-sinf", "12-hafta", "30-dars-ozgaruvchilar-tangalar-va-jonlar")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "playground"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides — Scratch Variables, Score & HP Logic)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="5–6-КЛАСС · 12-Я НЕДЕЛЯ · УРОК 30" data-en="GRADES 5–6 · WEEK 12 · LESSON 30">5–6-SINF · 12-HAFTA · 30-DARS</span></div>
    <h1 class="display" data-ru="Магия Переменных: Монеты, Жизни (HP) и Таймер в Scratch" data-en="The Magic of Variables: Coins, Lives (HP) & Timers in Scratch">O'zgaruvchilar Sehri: Tangalar, Jonlar (HP) va Vaqt</h1>
    <p class="lede" data-ru="Превращаем анимацию в настоящую игру: что такое переменная и как хранить в ней данные, сбор золотых монет (+10 очков), потеря жизней от ловушек (-1 HP) и победный таймер обратного отсчета!" data-en="Turning animations into real playable arcade games: understanding variables as memory boxes, collecting gold coins (+10 Score), losing lives on traps (-1 HP), and countdown timers!">Multfilmni haqiqiy arkada o'yiniga aylantiramiz: o'zgaruvchi nima va ma'lumotni qanday saqlash, oltin tangalarni yig'ish (+10 ball), tuzoqlardan jonlarni yo'qotish (-1 HP) va vaqt hisobi!</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Память Игры" data-en="Game Memory">Sehrli Quti (O'zgaruvchi)</h3>
        <p data-ru="Переменная — это коробка с названием, где игра хранит очки, жизни и секунды." data-en="A variable is a labeled memory box where the game stores score, hearts, and seconds.">O'zgaruvchi — bu kompyuter xotirasidagi sehrli quticha, unda ochko, jonlar va soniyalar saqlanadi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Coin & HP Arcade</div>
        <h3 data-ru="Полная Игра" data-en="Full Mini-Game">Tangalar va Jonlar O'yini</h3>
        <p data-ru="Каждый ученик создаст полноценную игру с интерфейсом жизней (❤️❤️❤️) и экраном Game Over." data-en="Each student codes a complete game featuring heart indicators (❤️❤️❤️) and Game Over screens.">Har bir o'quvchi yurakchalar (❤️❤️❤️), tangalar va Game Over xabariga ega haqiqiy o'yin yaratadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 29-УРОКА" data-en="LESSON 29 HOMEWORK REVIEW">29-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Волшебный Лабиринт: Ошибка Застревания в Черной Стене" data-en="Magic Maze: Getting Trapped Inside Black Walls">Sehrli Labirint: Qora Devor Ichiga Kirib Qotib Qolish Xatosi</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Типичная ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h4 data-ru="Забыли шаг назад при касании черного цвета" data-en="Forgot step-back upon touching black wall color">Devorga tekkanda orqaga siljishni unutib qo'yish</h4>
        <p style="font-size:12px;" data-ru="Ученики написали блок: «Если касается цвета [Черный], то сказать Ой!». Кот касался стены, говорил «Ой», но продолжал идти вперед и намертво застревал внутри стены лабиринта!" data-en="Students programmed: «If touching color [Black], say Ouch!». Cat touched the wall, said 'Ouch', but kept moving forward and got permanently embedded in the wall!">O'quvchilar: "Agar qora rangga tegsa, Voy deb gapirsin" blokini qo'yishdi. Mushuk devorga tekkanda "Voy" dedi, ammo oldinga yurishda davom etib devor ichiga kirib qotib qoldi!</p>
        <div style="background:#1e1014; padding:6px; border-radius:4px; font-family:monospace; font-size:11px; color:#f87171;" data-ru="❌ Ошибка: Нет отталкивания назад" data-en="❌ Error: Missing reverse pushback">❌ Xato: Orqaga qaytaruvchi blok yo'q</div>
      </div>
      <div class="box" style="border:1px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой стандарт (Golden Solution)" data-en="Golden Standard">Oltin Standart Yechim</div>
        <h4 data-ru="Шаг -10 шагов (Мгновенный Отскок Назад)" data-en="-10 Steps Instant Rebound">-10 Qadam Orqaga Sakrash (Oltin Qoida)</h4>
        <p style="font-size:12px;" data-ru="Как только персонаж коснулся черного контура стены, мы СРАЗУ делаем `идти -10 шагов`. Персонаж отскакивает назад и никогда не проваливается сквозь препятствия!" data-en="The exact moment our sprite touches the black contour, we INSTANTLY execute `move -10 steps`. The sprite bounces back and never clips through walls!">Qahramon qora devorga tekkan lahzada DARHOL `yurish -10 qadam` blokini beramiz. Mushuk devordan orqaga qaytib, hech qachon to'siq ichiga kirib ketmaydi!</p>
        <div style="background:#0e231b; padding:6px; border-radius:4px; font-family:monospace; font-size:11px; color:#34d399;" data-ru="✅ Решение: [если касается цвета (Черный) то: идти -10 шагов]" data-en="✅ Solution: [if touching color (Black) then: move -10 steps]">✅ Yechim: [agar (qora) rangiga tegsa: -10 qadam yurish]</div>
      </div>
    </div>
    <div class="grid-2" style="margin-top:10px;">
      <div class="box">
        <div class="tag" data-ru="30-секундный Блиц" data-en="30-Sec Blitz">30 Soniyalik Blitz</div>
        <p style="font-size:11px;" data-ru="Каким блоком проверить, что персонаж дошел до финишного кристалла?" data-en="Which block checks if sprite reached the goal crystal?">Qahramon marradagi olmosga yetib borganini qaysi blok bilan tekshiramiz?</p>
        <div style="font-size:11px; color:var(--accent); font-weight:700;" data-ru="Ответ: «Касается [Кристалл]?» из оранжево-голубого блока Сенсоров." data-en="Answer: «Touching [Crystal]?» sensing block.">Javob: Sezgirlik (Sensing) bo'limidagi "[Olmos] ga tegdimi?" bloki!</div>
      </div>
      <div class="box">
        <div class="tag" data-ru="Мост к теме 30" data-en="Bridge to Lesson 30">Bugungi Mavzuga Ko'prik</div>
        <p style="font-size:11px;" data-ru="В лабиринте мы просто доходили до выхода. Но где счет? Где жизни? Сегодня мы добавим золотые монеты и жизни ❤️❤️❤️!" data-en="In our maze we simply reached the exit. But where is the score? Where are player hearts? Today we add coins and lives ❤️❤️❤️!">Labirintda shunchaki yurdik. Lekin o'yinda nechta tanga yig'dik? Nechta jonimiz qoldi? Bugun o'yinimizga hisob va jonlar qo'shamiz!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: WHAT IS A VARIABLE -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ОСНОВЫ ПРОГРАММИРОВАНИЯ" data-en="CODING FUNDAMENTALS">DASTURLASH ASOSLARI</span></div>
    <h2 data-ru="Что такое Переменная? Волшебная Коробка Памяти" data-en="What is a Variable? The Magic Memory Box">O'zgaruvchi Nima? Kompyuterning Sehrli Qutichasi</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag" style="background:rgba(245,158,11,0.15); color:var(--yellow);">1. Qutining Nomi</div>
        <h4 data-ru="Имя Переменной (Label)" data-en="Variable Name (Label)">Nomlash (Masalan: "Tangalar")</h4>
        <p style="font-size:11px;" data-ru="Каждая коробка имеет понятное имя: `Очки`, `Жизни`, `Таймер`. Компьютер по этому имени находит нужные данные." data-en="Every box has a distinct name: `Score`, `Lives`, `Timer`. The game engine references this label to read or write data.">Har bir qutiga tushunarli nom qo'yiladi: `Ballar`, `Jonlar`, `Vaqt`. Kompyuter o'sha nom orqali ma'lumotni topadi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">2. Quti Ichidagi Qiymat</div>
        <h4 data-ru="Значение (Value)" data-en="Stored Value (Value)">Qiymat (Masalan: son 0)</h4>
        <p style="font-size:11px;" data-ru="Внутри коробки лежит число. В начале игры там лежит `0`. Когда кот берет монету, число меняется на `10`." data-en="A number lives inside the box. At game start it holds `0`. Once a coin is grabbed, it updates to `10`.">Qutining ichida son yotadi. O'yin boshida u `0` bo'ladi. Mushuk tanga olganda son `10` ga aylanadi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">3. O'zgarish Qobiliyati</div>
        <h4 data-ru="Она Изменяется!" data-en="It Can Change!">Qiymat O'zgarishi Mumkin</h4>
        <p style="font-size:11px;" data-ru="Именно поэтому она называется «Переменная»! Число внутри может расти (+1) или уменьшаться (-1)." data-en="That is why it is called a 'Variable'! The internal value can increment (+1) or decrement (-1).">Shuning uchun ham u "O'zgaruvchi" deb ataladi! Uning ichidagi son o'sishi (+1) yoki kamayishi (-1) mumkin.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: SCRATCH VARIABLE BLOCKS -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="БЛОКИ SCRATCH" data-en="SCRATCH BLOCKS">TO'Q SARIQ BLOKLAR</span></div>
    <h2 data-ru="3 Главных Блока Переменных в Scratch" data-en="3 Core Variable Blocks in Scratch">Scratch-dagi 3 Asosiy O'zgaruvchi Bloki</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag" style="background:rgba(245,158,11,0.15); color:var(--yellow);">1. Boshlang'ich Qiymat</div>
        <h4 data-ru="«Задать [Очки] значение 0»" data-en="«Set [Score] to 0»">«[Ballar] ni 0 ga sozlash»</h4>
        <p style="font-size:11px;" data-ru="Ставится сразу под зеленым флажком! Очищает старые результаты перед началом новой игры." data-en="Placed immediately beneath the Green Flag! Clears previous playthrough records before restarting.">Yashil bayroqcha bosilganda qo'yiladi! Yangi o'yin boshlanganda eski ballarni tozalab, nolga tenglaydi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">2. Qo'shish (Tangalar)</div>
        <h4 data-ru="«Изменить [Очки] на 1»" data-en="«Change [Score] by 1»">«[Ballar] ni 1 ga o'zgartirish»</h4>
        <p style="font-size:11px;" data-ru="Прибавляет число к текущему значению. Было 5 очков &rarr; стало 6!" data-en="Increments the current tally. Had 5 coins &rarr; now you hold 6!">Mavjud songa qo'shadi. 5 ta tangangiz bor edi &rarr; endi 6 ta bo'ladi!</p>
      </div>
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);">3. Kamaytirish (Jonlar)</div>
        <h4 data-ru="«Изменить [Жизни] на -1»" data-en="«Change [Lives] by -1»">«[Jonlar] ni -1 ga o'zgartirish»</h4>
        <p style="font-size:11px;" data-ru="Минус отнимает жизнь! Было 3 жизни &rarr; кот наступил на шипы &rarr; осталось 2 жизни." data-en="Negative numbers deduct lives! Had 3 hearts &rarr; cat touched spikes &rarr; 2 hearts remain.">Minus belgisi jonni kamaytiradi! 3 ta jon bor edi &rarr; tikanlarga tekkanda 2 ta qoladi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: COIN COLLECTION LOGIC -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="АЛГОРИТМ МОНЕТКИ" data-en="COIN ALGORITHM">TANGANING ALGORITMI</span></div>
    <h2 data-ru="Как Работает Золотая Монета: Сбор и Исчезновение" data-en="How Gold Coins Work: Collect & Disappear Logic">Oltin Tanga Qanday Ishlaydi: Olish va Yo'qolish</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" data-ru="Алгоритм Монеты" data-en="Coin Algorithm">Tanganing 4 Qadami</div>
        <ol style="font-size:12px; line-height:1.7; margin-top:6px;">
          <li data-ru="Флажок нажат: монета появляется `показаться`." data-en="Flag clicked: coin reveals itself `show`.">Yashil bayroqcha bosilganda: tanga ko'rinadi (`ko'rsatish`).</li>
          <li data-ru="В цикле `повторять всегда` проверяет касание кота." data-en="In a `forever` loop, continuously detects cat touch.">Doimiy siklda (`forever`) mushuk tegishini poylaydi.</li>
          <li data-ru="Если коснулся кота: `изменить [Очки] на 10`." data-en="If touching cat: `change [Score] by 10`.">Mushuk tegsa: `[Ballar] ni 10 ga oshirish`.</li>
          <li data-ru="Издать звук 'Coin' и сразу `спрятаться`!" data-en="Play 'Coin' chime and immediately `hide`!">Chiroyli 'Coin' ovozini chiqarish va darhol `yashirinish`!</li>
        </ol>
      </div>
      <div class="box" style="border:1px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Скрипт Монетки" data-en="Coin Scratch Script">Scratch Bloklari Ko'rinishi</div>
        <div style="background:#0f172a; padding:10px; border-radius:6px; font-family:monospace; font-size:11px; line-height:1.6; color:#cbd5e1;">
          <span style="color:#f59e0b;">qachonki [bayroqcha] bosilganda:</span><br>
          &nbsp;&nbsp;<span style="color:#a855f7;">ko'rsatish</span><br>
          &nbsp;&nbsp;<span style="color:#eab308;">doim takrorlash:</span><br>
          &nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#eab308;">agar &lt;[Mushuk]ga tegdimi?&gt; u holda:</span><br>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#f59e0b;">[Ballar] ni (10) ga o'zgartirish</span><br>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ec4899;">ovoz [Coin] chalish</span><br>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a855f7;">yashirinish</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: HEALTH POINTS (HP) & LIVES -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ЖИЗНИ ПЕРСОНАЖА" data-en="PLAYER HEALTH">JONLAR VA XAVF (HP)</span></div>
    <h2 data-ru="Система Жизней (HP): Опасные Шипы и Лава" data-en="Health Points (HP) Engine: Spikes & Lava Traps">Jonlar Tizimi (HP): Tikanlar va Xavfli Qizil Lava</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Потеря Жизней" data-en="Losing Health">Jon Yo'qotish Qoidasi</div>
        <p style="font-size:12px; line-height:1.6;" data-ru="В начале игры: `Задать [Жизни] значение 3`.<br>Если кот наступает на красные шипы:<br>1. `Изменить [Жизни] на -1`<br>2. Кот кричит «Ай!» и мигает красным<br>3. `Ждать 1 секунду` (защита от мгновенного сгорания всех жизней за 1 миллисекунду!)" data-en="At game launch: `Set [Lives] to 3`.<br>When cat steps onto red spikes:<br>1. `Change [Lives] by -1`<br>2. Cat says 'Ouch!' and flashes red<br>3. `Wait 1 second` (cooldown guard preventing losing all 3 hearts in 1 millisecond!)">O'yin boshida: `[Jonlar] ni 3 ga sozlash`.<br>Mushuk qizil tikanga tegsa:<br>1. `[Jonlar] ni -1 ga o'zgartirish`<br>2. Mushuk "Voy!" deb qizil rangda miltillaydi<br>3. `1 soniya kutish` (1 millisekundda barcha 3 ta jon tugab ketmasligi uchun himoya!)</p>
      </div>
      <div class="box" style="border:1px solid var(--red);">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Проверка Проигрыша" data-en="Game Over Condition">Game Over Sharti</div>
        <div style="background:#0f172a; padding:10px; border-radius:6px; font-family:monospace; font-size:11px; line-height:1.6; color:#cbd5e1;">
          <span style="color:#eab308;">agar &lt;[Jonlar] = 0&gt; u holda:</span><br>
          &nbsp;&nbsp;<span style="color:#a855f7;">fonni [Game Over] ga almashtirish</span><br>
          &nbsp;&nbsp;<span style="color:#ec4899;">ovoz [Lose] chalish</span><br>
          &nbsp;&nbsp;<span style="color:#eab308;">barchasini to'xtatish (Stop all)</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: TIMER LOGIC -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ОБРАТНЫЙ ОТСЧЕТ" data-en="COUNTDOWN TIMER">TAYMER VA VAQT</span></div>
    <h2 data-ru="Секундомер и Таймер: Успей Собрать за 30 Секунд!" data-en="Countdown Timer: Collect Everything in 30 Seconds!">Vaqt Hisobi: 30 Soniyada Yig'ishga Ulug'ur!</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Механика Таймера" data-en="Timer Mechanics">Taymer Qanday Ishlaydi?</div>
        <p style="font-size:12px; line-height:1.6;" data-ru="Создаем переменную `Время`.<br>1. В начале: `Задать [Время] значение 30`.<br>2. В цикле: `Ждать 1 секунду`.<br>3. `Изменить [Время] на -1`.<br>4. Когда Время станет `0`, игра останавливается!" data-en="Create a variable called `Timer`.<br>1. Start: `Set [Timer] to 30`.<br>2. Loop: `Wait 1 seconds`.<br>3. `Change [Timer] by -1`.<br>4. When Timer hits `0`, game terminates!">`Vaqt` nomli yangi o'zgaruvchi ochamiz.<br>1. Boshida: `[Vaqt] ni 30 ga sozlash`.<br>2. Sikl ichida: `1 soniya kutish`.<br>3. `[Vaqt] ni -1 ga o'zgartirish`.<br>4. Vaqt `0` bo'lib qolsa, o'yin to'xtaydi!</p>
      </div>
      <div class="box" style="border:1px solid var(--accent);">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Скрипт Таймера" data-en="Timer Scratch Script">Scratch Taymer Skripti</div>
        <div style="background:#0f172a; padding:10px; border-radius:6px; font-family:monospace; font-size:11px; line-height:1.6; color:#cbd5e1;">
          <span style="color:#f59e0b;">qachonki [bayroqcha] bosilganda:</span><br>
          &nbsp;&nbsp;<span style="color:#f59e0b;">[Vaqt] ni (30) ga sozlash</span><br>
          &nbsp;&nbsp;<span style="color:#eab308;">toki &lt;[Vaqt] = 0&gt; bo'lguncha takrorlash:</span><br>
          &nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#eab308;">kutish (1) soniya</span><br>
          &nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#f59e0b;">[Vaqt] ni (-1) ga o'zgartirish</span><br>
          &nbsp;&nbsp;<span style="color:#eab308;">barchasini to'xtatish (Stop all)</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: SMARTBOARD INTERACTIVE DEMO -->
  <section class="slide" data-phase="Jonli Sinov|Живой Тест|Live Test" data-time="40:00–48:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ИНТЕРАКТИВНЫЙ ТРЕНАЖЕР" data-en="INTERACTIVE SIMULATOR">SMARTBOARD BOSHQARUVI</span></div>
    <h2 data-ru="Живой Тест: Кот Собирает Золотые Монеты и Теряет HP" data-en="Live Simulation: Cat Collecting Coins & Losing HP">Jonli O'yin Sinovi: Mushuk Tangalarni Yig'adi va HP Yo'qotadi</h2>
    <div style="background:var(--surface); border:1px solid var(--hair); border-radius:8px; padding:12px; margin-top:8px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <div style="font-size:12px; font-weight:700;">
          <span>💰 <span data-ru="Монеты:" data-en="Score:">Tangalar:</span> <strong id="demoScore" style="color:var(--yellow);">0</strong></span>
          <span style="margin-left:14px;">❤️ <span data-ru="Жизни:" data-en="Lives:">Jonlar:</span> <strong id="demoHp" style="color:var(--red);">3</strong></span>
          <span style="margin-left:14px;">⏱️ <span data-ru="Таймер:" data-en="Timer:">Vaqt:</span> <strong id="demoTime" style="color:var(--accent);">20s</strong></span>
        </div>
        <div style="display:flex; gap:6px;">
          <button onclick="addDemoCoin()" class="btn" style="background:var(--yellow); color:#000; padding:4px 8px; font-size:11px;" data-ru="+10 Монет" data-en="+10 Coins">+10 Tanga</button>
          <button onclick="hitDemoTrap()" class="btn" style="background:var(--red); color:#fff; padding:4px 8px; font-size:11px;" data-ru="-1 Жизнь (Шип)" data-en="-1 Life (Spike)">-1 Jon (Tikan)</button>
          <button onclick="resetDemoGame()" style="background:#334155; color:#fff; border:none; padding:4px 8px; border-radius:4px; font-size:11px; cursor:pointer;" data-ru="Сброс" data-en="Reset">Qayta o'rnatish</button>
        </div>
      </div>
      <div id="demoGameBanner" style="background:#0f172a; padding:12px; border-radius:6px; border:1px solid #334155; text-align:center; min-height:80px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
        <div id="demoCatMood" style="font-size:32px;">🐱</div>
        <div id="demoMsg" style="font-size:12px; font-weight:700; color:#38bdf8; margin-top:4px;" data-ru="Нажимайте кнопки сверху для сбора монет или проверки шипов!" data-en="Click buttons above to collect coins or trigger spike traps!">Yuqoridagi tugmalarni bosib tanga oling yoki tikanga teging!</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: QUICK QUIZ -->
  <section class="slide" data-phase="Viktorina|Викторина|Quiz" data-time="48:00–55:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ЭКСПРЕСС-ТЕСТ" data-en="RAPID QUIZ">TEZKOR TEST</span></div>
    <h2 data-ru="3 Вопроса по Переменным в Scratch" data-en="3 Questions on Scratch Variables">O'zgaruvchilar Bo'yicha 3 Savol</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag">Savol 1</div>
        <h4 data-ru="Зачем перед стартом игры ставить «Задать [Очки] значение 0»?" data-en="Why set [Score] to 0 when green flag clicked?">Nega o'yin boshida «[Ballar] ni 0 ga sozlash» qo'yiladi?</h4>
        <div style="font-size:11px; margin-top:6px; line-height:1.5;">
          <div>A) Mushuk tezroq yugurishi uchun</div>
          <div style="color:var(--green); font-weight:700;">B) Yangi o'yinda o'tgan safargi eski ballarni tozalash uchun</div>
          <div>C) Tangalarni ko'paytirish uchun</div>
        </div>
      </div>
      <div class="box">
        <div class="tag">Savol 2</div>
        <h4 data-ru="Каким блоком отнять одну жизнь при касании шипов?" data-en="Which block deducts 1 life upon touching spikes?">Tikanga tekkanda bitta jonni qaysi blok bilan kamaytiramiz?</h4>
        <div style="font-size:11px; margin-top:6px; line-height:1.5;">
          <div>A) «[Jonlar] ni 1 ga o'zgartirish»</div>
          <div style="color:var(--green); font-weight:700;">B) «[Jonlar] ni -1 ga o'zgartirish»</div>
          <div>C) «Jonlarni o'chirish»</div>
        </div>
      </div>
      <div class="box">
        <div class="tag">Savol 3</div>
        <h4 data-ru="Что произойдет, если в таймере забыть блок «Ждать 1 секунду»?" data-en="What happens if you omit «Wait 1 second» in timer?">Taymerda «1 soniya kutish» blokini qo'yish esdan chiqsa nima bo'ladi?</h4>
        <div style="font-size:11px; margin-top:6px; line-height:1.5;">
          <div>A) Hech narsa bo'lmaydi</div>
          <div style="color:var(--green); font-weight:700;">B) 30 soniya bir ko'z ochib yumguncha (0.01 soniyada) tugab qoladi!</div>
          <div>C) O'yin sekinlashadi</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: BIG LAB ARENA -->
  <section class="slide" data-phase="Amaliyot|Практика|Practice" data-time="55:00–70:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="БОЛЬШАЯ ЛАБОРАТОРИЯ · 25 МИНУТ" data-en="GRAND LAB · 25 MINUTES">KATTA LABORATORIYA · 25 DAQIQA</span></div>
    <h2 data-ru="Практика: Создаем Игру «Охотник за Золотом»" data-en="Hands-on Lab: Build the 'Gold Hunter' Game">Katta Amaliyot: «Oltin Ovchisi» Kiber-O'yinini Yaratamiz!</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Техническое Задание (PRD)" data-en="Technical Task (PRD)">O'yin Qoidalari (PRD)</div>
        <ol style="font-size:12px; line-height:1.7; margin-top:6px;">
          <li data-ru="Создать 2 переменные: `Монеты` и `Жизни`." data-en="Create 2 variables: `Score` and `Lives`.">2 ta o'zgaruvchi oching: `Tangalar` va `Jonlar`.</li>
          <li data-ru="Разместить на поле 4 монетки. Каждая дает +10 очков и исчезает." data-en="Place 4 coins across the stage. Each grants +10 Score and hides.">Maydonga 4 ta tanga qo'ying. Har biri +10 ball berib, yo'qoladi.</li>
          <li data-ru="Добавить 2 красных шипа: при касании `Жизни -1`." data-en="Add 2 red spikes: touching deducts `Lives by -1`.">2 ta qizil tikan qo'ying: tekkanda `Jonlar -1` bo'ladi.</li>
          <li data-ru="Если Монеты = 40 &rarr; ПОБЕДА! Если Жизни = 0 &rarr; GAME OVER!" data-en="If Score = 40 &rarr; VICTORY! If Lives = 0 &rarr; GAME OVER!">Tangalar = 40 bo'lsa &rarr; G'ALABA! Jonlar = 0 bo'lsa &rarr; GAME OVER!</li>
        </ol>
      </div>
      <div class="box" style="border:1px solid var(--accent);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Критерии Успеха (100%)" data-en="Success Criteria (100%)">Muvaffaqiyat Mezoni (100%)</div>
        <ul style="font-size:12px; line-height:1.7; margin-top:6px;">
          <li data-ru="✅ Флажок сбрасывает счет: Монеты=0, Жизни=3." data-en="✅ Flag resets stats: Score=0, Lives=3.">✅ Bayroqcha bosilganda: Tangalar=0, Jonlar=3 bo'lishi.</li>
          <li data-ru="✅ Монетки исчезают и больше не дают повторных очков." data-en="✅ Coins vanish and do not award double points.">✅ Tangalar olgandan keyin qayta ochko bermasligi (`yashirinish`).</li>
          <li data-ru="✅ Кот отскакивает от шипов назад и мигает красным." data-en="✅ Cat rebounds from spikes and flashes red.">✅ Mushuk tikanga tekkanda orqaga qaytishi va qizil bo'lishi.</li>
          <li data-ru="✅ Экран Game Over останавливает весь проект." data-en="✅ Game Over screen stops all project scripts.">✅ Game Over chiqqanda o'yin to'liq to'xtashi (`stop all`).</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: PEER-REVIEW -->
  <section class="slide" data-phase="Ko'rik|Ревью|Review" data-time="70:00–74:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМНЫЙ АУДИТ" data-en="PEER REVIEW">JUFTLIKDA O'ZARO TEKSHIRUV</span></div>
    <h2 data-ru="Чек-лист Партнера: Проверь Игру Друга!" data-en="Peer Audit Checklist: Test Your Friend's Game!">Do'stingning O'yinini Tekshir: 3 Ta Asosiy Sinov</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag">1. Tanga Sinovi</div>
        <h4 data-ru="Исчезает ли монетка?" data-en="Does the coin disappear?">Tanga yo'qolyaptimi?</h4>
        <p style="font-size:11px;" data-ru="Возьмите монету. Прибавилось ли ровно 10 очков? Нельзя ли взять одну монету 5 раз подряд?" data-en="Collect the coin. Does it grant exactly 10 points? Can you exploit it multiple times?">Tangani oling. Roppa-rosa 10 ochko berdimi? Bitta tanga ustida turib 5 marta ball olish mumkin emasmi?</p>
      </div>
      <div class="box">
        <div class="tag">2. Tikan Sinovi</div>
        <h4 data-ru="Есть ли задержка урона?" data-en="Is there damage cooldown?">1 soniya kutish bormi?</h4>
        <p style="font-size:11px;" data-ru="Наступите на шипы. Отнялась ли 1 жизнь? Если сразу сгорело все 3 жизни — друг забыл блок «Ждать 1 секунду»!" data-en="Step onto spikes. Did you lose only 1 heart? If all 3 burned instantly, your friend forgot «Wait 1 second»!">Tikanga teging. 1 ta jon ketdimi? Agar barcha 3 ta jon birdaniga tugasa — do'stingiz 1 soniya kutishni unutgan!</p>
      </div>
      <div class="box">
        <div class="tag">3. Qayta Boshlash</div>
        <h4 data-ru="Сброс на флажок" data-en="Green flag reset">Bayroqcha bosilganda tozalanish</h4>
        <p style="font-size:11px;" data-ru="Нажмите флажок. Появились ли монетки заново? Сбросились ли жизни обратно на 3?" data-en="Hit the green flag. Did coins reappear? Did hearts reset back to 3?">Bayroqchani bosing. Tangalar yana paydo bo'ldimi? Jonlar yana 3 bo'ldimi?</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: SHOWCASE -->
  <section class="slide" data-phase="Namoyish|Шоукейс|Showcase" data-time="74:00–76:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ПАРАД ПРОЕКТОВ" data-en="PROJECT SHOWCASE">KATTA EKRAN NAMOYISHI</span></div>
    <h2 data-ru="Шоукейс: Самый Крутой Аркадный Лабиринт!" data-en="Showcase: Best Arcade Maze Game!">Sinfning Eng Zo'r Arkada O'yini Namoyishi!</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);" data-ru="Гордость Разработчика" data-en="Developer Pride">Katta Doskada O'ynash</div>
        <p style="font-size:12px;" data-ru="2 самых активных ученика выводят свою игру на большой экран смартборда. Весь класс наблюдает за прохождением лабиринта и подсчетом золотых монет!" data-en="2 top creators showcase their games on the interactive smartboard. The whole room cheers as they collect coins and dodge traps live!">2 nafar chaqqon o'quvchi o'z o'yinini katta doskaga chiqaradi. Butun sinf ularning tangalar yig'ishini va qizil tuzoqlardan chaqqon qochishini tomosha qiladi!</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Награды Урока" data-en="Lesson Awards">Kiber-Yulduzlar</div>
        <ul style="font-size:12px; line-height:1.7;">
          <li data-ru="🏆 <strong>Самый быстрый сборщик:</strong> Игрок, собравший 40 очков за 15 секунд!" data-en="🏆 <strong>Speed Collector:</strong> Player scoring 40 points in under 15 seconds!">🏆 <strong>Eng tezkor yig'uvchi:</strong> 15 soniyada 40 ball to'plagan o'yinchi!</li>
          <li data-ru="🎨 <strong>Лучший дизайн:</strong> Вращающиеся монеты со звуковыми эффектами!" data-en="🎨 <strong>Best Visual Design:</strong> Spinning coins with arcade sound effects!">🎨 <strong>Eng chiroyli dizayn:</strong> Tangalari aylanuvchi va ovoz chiqaruvchi o'yin!</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: RUBRIC -->
  <section class="slide" data-phase="Baholash|Оценка|Rubric" data-time="76:00–78:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="КРИТЕРИИ ОЦЕНИВАНИЯ" data-en="GRADING RUBRIC">10 BALLIK BAHOLASH MEZONI</span></div>
    <h2 data-ru="Рубрика Оценки 30-Урока (10 Баллов)" data-en="Lesson 30 Grading Rubric (10 Points)">30-Dars Bo'yicha 10 Ballik Baholash Rubrikasi</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">4 Ball (Baza)</div>
        <h4 data-ru="Переменные и Сброс" data-en="Variables & Reset">O'zgaruvchi va Boshlang'ich Qiymat</h4>
        <p style="font-size:11px;" data-ru="Созданы переменные Очки и Жизни. При нажатии флажка они сбрасываются на 0 и 3." data-en="Score and Lives variables created. Green flag resets them properly to 0 and 3.">Ballar va Jonlar o'zgaruvchilari ochilgan. Bayroqcha bosilganda 0 va 3 ga to'g'ri sozlanadi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">4 Ball (Amaliyot)</div>
        <h4 data-ru="Сбор Монет и Урон от Шипов" data-en="Coin Collect & Damage">Tangalar Yig'ish va Jon Yo'qotish</h4>
        <p style="font-size:11px;" data-ru="Монеты дают +10 и исчезают. Шипы отнимают -1 HP с задержкой 1 секунда." data-en="Coins grant +10 and hide. Spikes deduct -1 HP with a 1-second cooldown.">Tangalar +10 berib yashirinadi. Tikanlar 1 soniya kutish bilan -1 jon oladi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);">2 Ball (Challenge)</div>
        <h4 data-ru="Таймер и Экран Победы" data-en="Timer & Victory Screen">Taymer va G'alaba Ekrani</h4>
        <p style="font-size:11px;" data-ru="Добавлен обратный отсчет 30 секунд и надпись победы при сборе всех 4 монет!" data-en="Configured a 30s countdown timer and celebration screen upon winning!">{30} soniyalik taymer qo'shilgan va barcha tangalar yig'ilganda G'ALABA ekrani chiqadi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & HOMEWORK -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="78:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="SUMMARY & HOMEWORK">XULOSA VA UY VAZIFASI</span></div>
    <h2 data-ru="Главные Выводы и Домашнее Задание" data-en="Key Takeaways & Homework Assignment">Bugungi Dars Xulosalari va Uy Vazifasi</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Домашнее Задание" data-en="Homework Assignment">Uy Vazifasi (vazifa.html)</div>
        <p style="font-size:12px; line-height:1.6;" data-ru="<strong>1-Уровень (4 б):</strong> Создать переменные `Монеты` и `Жизни`, сбросить на старте.<br><strong>2-Уровень (4 б):</strong> Сделать 3 монеты и 1 опасный шип с потерей жизней.<br><strong>3-Уровень (2 б):</strong> Добавить таймер обратного отсчета на 20 секунд." data-en="<strong>Tier 1 (4 pts):</strong> Create `Score` and `Lives` variables with green flag resets.<br><strong>Tier 2 (4 pts):</strong> Program 3 coins and 1 spike hazard with health loss.<br><strong>Tier 3 (2 pts):</strong> Add a 20-second countdown timer."><strong>1-Daraja (4 b):</strong> `Tangalar` va `Jonlar` o'zgaruvchilarini ochib, bayroqcha bilan sozlash.<br><strong>2-Daraja (4 b):</strong> 3 ta tanga va 1 ta tikanni jon yo'qotish bilan dasturlash.<br><strong>3-Daraja (2 b):</strong> 20 soniyalik teskari hisoblovchi taymerni qo'shish.</p>
      </div>
      <div class="box" style="border:1px solid var(--accent);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Анонс 31-Урока" data-en="Next Lesson 31">Keyingi Dars (31-Dars)</div>
        <h4 data-ru="Сообщения и События (Broadcast): Диалоги Героев" data-en="Broadcast Messages: Hero Conversations">Xabarlar va Hodisalar (Broadcast): Qahramonlar Muloqoti</h4>
        <p style="font-size:12px;" data-ru="В следующий раз мы научим персонажей общаться между собой: кот находит ключ, отправляет радио-сообщение (Broadcast), и запертая дверь замка открывается!" data-en="Next time our characters learn to speak to one another: the cat finds a key, sends a broadcast signal, and the castle gate opens!">Keyingi darsimizda qahramonlar bir-biriga xabar yuborishni o'rganadi: mushuk kalitni olganda radio-xabar yuboradi va sehrli qasr darvozasi ochiladi!</p>
      </div>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. NOTES DATA (14 Slides Notes)
# -----------------------------------------------------------------------------
NOTES_DATA = {
    "uz": [
        ["Kirish va Maqsad", "O'quvchilarga bugungi mavzu: O'zgaruvchilar, tangalar yig'ish va jonlar tizimi ekanini e'lon qiling.", "Doskaga quti va uning ichidagi son rasmini chizing."],
        ["Uy Vazifasi Tahlili", "29-darsdagi devor ichiga kirib qotib qolish xatosini tushuntiring.", "Oltin yechim: devorga tekkanda -10 qadam orqaga otilish ekanini ko'rsating."],
        ["O'zgaruvchi Tushunchasi", "O'zgaruvchi nima uchun xotira qutisi ekanini sodda qilib tushuntiring.", "Qutining nomi va qiymati o'rtasidagi farqni so'rang."],
        ["Scratch Bloklari", "To'q sariq O'zgaruvchilar bo'limidagi 3 ta blokni ko'rsating.", "Set to 0 va change by 1 bloklari farqini tushuntiring."],
        ["Tanga Algoritmi", "Tanga olinganda nega yashirinishi shartligini ko'rsating.", "Agar yashirinmasa, doimiy tekkanda ochko cheksiz ko'payib ketishini ayting."],
        ["Jonlar Tizimi (HP)", "Tikanlarga tekkanda nega 1 soniya kutish shartligini tushuntiring.", "Agar kutish bo'lmasa, 1 millisekundda barcha 3 ta jon tugashini ko'rsating."],
        ["Taymer Mexanikasi", "30 soniyalik teskari hisoblovchi taymer algoritmini tahlil qiling.", "1 soniya kutish va -1 qilish blokini doskaga yozing."],
        ["Smartboard Sinovi", "Doskadagi simulyatorda tanga yig'ish va tikanga tegishni ko'rsating.", "O'quvchini doskaga chiqarib sinab ko'rishni buyuring."],
        ["Tezkor Viktorina", "3 ta qiziqarli savol orqali butun sinfni jonlantiring.", "To'g'ri javob berganlarga rag'bat stikerlari bering."],
        ["Katta Kiber-Arena", "25 daqiqalik amaliyotni boshlang.", "O'quvchilar playground/index.html da o'z o'yinlarini qurishlarini nazorat qiling."],
        ["O'zaro Tekshiruv", "Partadoshlar bir-birining o'yinida tanga va jonlar to'g'ri ishlashini tekshiradilar.", "Juftliklarni almashtirib sinov o'tkazing."],
        ["Katta Ekran Showcasi", "Eng zo'r arkada o'yinini katta doskaga chiqarib butun sinfga namoyish qiling.", "O'quvchini olqishlang."],
        ["Baholash Rubrikasi", "10 ballik mezonni eslatib o'ting: 4 ball baza, 4 ball amaliyot, 2 ball challenge.", "Barcha o'quvchilar baholarini belgilang."],
        ["Xulosa va Keyingi Dars", "Darsni yakunlang va uy vazifasini bering.", "Keyingi Broadcast va eshik ochish mavzusiga qiziqish uyg'oting."]
    ],
    "ru": [
        ["Введение и Цель", "Объявите тему: переменные в Scratch, сбор монет и система жизней (HP).", "Нарисуйте на доске коробку памяти с числом внутри."],
        ["Разбор ДЗ 29", "Разберите ошибку застревания в стене в игре Лабиринт.", "Напомните золотое правило: отскок на -10 шагов назад."],
        ["Понятие Переменной", "Объясните concept переменной как волшебной коробки для очков и жизней.", "Покажите разницу между именем и значением."],
        ["Блоки Scratch", "Разберите 3 блока оранжевой категории Переменные.", "Объясните сброс в 0 на старте и изменение на 1."],
        ["Алгоритм Монеты", "Объясните, почему монетка должна сразу исчезать (hide).", "Предупредите об ошибке бесконечного начисления очков."],
        ["Система Жизней", "Объясните задержку в 1 секунду при касании шипов.", "Покажите, как избежать мгновенной потери всех жизней."],
        ["Механика Таймера", "Разберите обратный отсчет от 30 до 0 секунд.", "Напишите на доске цикл с ожиданием 1 секунды."],
        ["Смартборд Тест", "Запустите интерактивный тренажер на смартборде.", "Пригласите ученика протестировать сбор монет и урон."],
        ["Экспресс-Тест", "Проведите веселый опрос по 3 вопросам слайда.", "Поощрите правильные ответы значками активности."],
        ["Большая Лаборатория", "Запустите 25-минутную практику в playground/index.html.", "Помогайте ученикам настраивать переменные очков и HP."],
        ["Взаимный Аудит", "Организуйте проверку игр между соседями по парте.", "Проконтролируйте проверку исчезновения монеток."],
        ["Шоукейс Проектов", "Выведите лучшую аркадную игру на смартборд.", "Похвалите авторов перед всем классом."],
        ["Критерии Оценки", "Напомните 10-балльную рубрику: база, практика, челлендж.", "Выставьте оценки за урок в журнал."],
        ["Итоги Урока", "Подведите итоги и выдайте домашнее задание.", "Анонсируйте тему Broadcast сообщений на следующий урок."]
    ],
    "en": [
        ["Intro & Objectives", "Announce today's topic: Scratch variables, coin collecting, and player HP.", "Draw a labeled memory box with a stored number on the board."],
        ["Lesson 29 Review", "Analyze the wall-clipping pitfall from the Magic Maze homework.", "Reinforce the golden rule: immediate -10 steps rebound."],
        ["Variable Concept", "Explain variables as named memory containers for score, HP, and time.", "Differentiate variable names from stored integer values."],
        ["Scratch Blocks", "Review the 3 essential orange variable blocks in Scratch.", "Contrast setting initial values versus incrementing tallies."],
        ["Coin Logic", "Explain why collectibles must hide immediately upon touch.", "Demonstrate the runaway score multiplier bug when hiding is omitted."],
        ["Health Points Engine", "Explain the 1-second cooldown guard when colliding with spikes.", "Show how cooldowns protect all 3 hearts from instant depletion."],
        ["Timer Mechanics", "Break down the countdown loop from 30 down to 0 seconds.", "Diagram the wait 1 second and decrement cycle on the board."],
        ["Smartboard Demo", "Run the live coin collection simulator on the smartboard.", "Invite a student to trigger the coin grab and spike hazard live."],
        ["Quick Quiz", "Conduct the 3-question knowledge check.", "Award participation stars to engaged students."],
        ["Grand Cyber Arena", "Commence the 25-minute build lab in playground/index.html.", "Assist students as they configure their score and heart engines."],
        ["Peer Audit", "Facilitate peer game testing between seatmates.", "Ensure students verify that collected coins vanish reliably."],
        ["Showcase", "Spotlight top arcade projects on the main screen.", "Celebrate game creators with classroom applause."],
        ["Grading Rubric", "Summarize the 10-point evaluation criteria.", "Log student achievement marks into records."],
        ["Summary & Next", "Wrap up the lesson and assign the homework.", "Tease the upcoming Broadcast messages module for Lesson 31."]
    ]
}

# -----------------------------------------------------------------------------
# 3. INTERACTIVE PLAYGROUND SCRIPT FOR PRESENTATION
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
var demoScore = 0;
var demoHp = 3;
var demoTime = 20;
var demoTimerId = null;

function addDemoCoin() {
  demoScore += 10;
  document.getElementById('demoScore').textContent = demoScore;
  document.getElementById('demoCatMood').textContent = '😺';
  document.getElementById('demoMsg').innerHTML = '<span style="color:#10b981; font-weight:700;">+10 Tanga olindi! 🎉</span>';
  if (demoScore >= 40) {
    document.getElementById('demoCatMood').textContent = '😻';
    document.getElementById('demoMsg').innerHTML = '<span style="color:#10b981; font-weight:700;">🏆 G‘ALABA! Barcha tangalar yig‘ildi!</span>';
  }
}

function hitDemoTrap() {
  if (demoHp <= 0) return;
  demoHp -= 1;
  document.getElementById('demoHp').textContent = demoHp;
  document.getElementById('demoCatMood').textContent = '😿';
  document.getElementById('demoMsg').innerHTML = '<span style="color:#ef4444; font-weight:700;">Voy! Tikanga tegildi (-1 Jon)!</span>';
  if (demoHp === 0) {
    document.getElementById('demoCatMood').textContent = '💀';
    document.getElementById('demoMsg').innerHTML = '<span style="color:#ef4444; font-weight:700;">GAME OVER! Jonlar tugadi.</span>';
  }
}

function resetDemoGame() {
  demoScore = 0;
  demoHp = 3;
  demoTime = 20;
  document.getElementById('demoScore').textContent = '0';
  document.getElementById('demoHp').textContent = '3';
  document.getElementById('demoTime').textContent = '20s';
  document.getElementById('demoCatMood').textContent = '🐱';
  document.getElementById('demoMsg').textContent = 'Yuqoridagi tugmalarni bosib tanga oling yoki tikanga teging!';
}
"""

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "30-dars: O'zgaruvchilar Sehri: Tangalar, Jonlar (HP) va Vaqt"
    title_ru = "Урок 30: Магия Переменных: Монеты, Жизни (HP) и Таймер"
    title_en = "Lesson 30: The Magic of Variables: Coins, Lives (HP) & Timers"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="5–6 КЛАСС" data-en="GRADES 5–6">5–6-SINF</span>',
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

    title_uz = "30-dars: O'zgaruvchilar Sehri: Tangalar, Jonlar (HP) va Vaqt"
    title_ru = "Урок 30: Магия Переменных: Монеты, Жизни (HP) и Таймер"
    title_en = "Lesson 30: The Magic of Variables: Coins, Lives (HP) & Timers"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<h1>.*?</h1>',
                 f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>',
                 tpl)

    sec1_html = """
    <p class="lead" style="font-size:12px; margin-bottom:8px;" data-ru="<strong>Миссия Урока:</strong> Превратить анимацию в настоящую аркаду: создать переменные «Очки» и «Жизни», запрограммировать сбор золотых монет (+10 очков с исчезновением), урон от шипов (-1 HP с задержкой 1 секунда) и условия победы или проигрыша (Game Over)." data-en="<strong>Lesson Mission:</strong> Transform animations into playable arcade games: create «Score» and «Lives» variables, program coin collection (+10 Score with hide effect), spike hazards (-1 HP with a 1-second cooldown), and Victory/Game Over conditions."><strong>Dars Missiyasi:</strong> Oddiy animatsiyani haqiqiy o'yinga aylantirish: «Ballar» va «Jonlar» o'zgaruvchilarini ochish, tangalarni yig'ish (+10 ball va yashirinish), tikanlarga tekkanda jon yo'qotish (-1 HP va 1 soniya kutish) hamda G'alaba yoki Game Over holatlarini yaratish.</p>
    <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="3 Правила Переменных в Scratch:" data-en="3 Rules of Scratch Variables:">Scratch O'zgaruvchilarining 3 Oltin Qoidasi:</div>
      <div>1. <strong>Boshlang'ich Sozlash:</strong> <span data-ru="Всегда сбрасывать переменные при нажатии флажка: Очки = 0, Жизни = 3." data-en="Always reset variables on green flag: Score = 0, Lives = 3.">Bayroqcha bosilganda o'zgaruvchilarni tozalash: Ballar = 0, Jonlar = 3</span>.</div>
      <div>2. <strong>Yashirish (Hide):</strong> <span data-ru="Собранная монетка обязана спрятаться, чтобы не начислять очки бесконечно." data-en="Collected coin must hide immediately to avoid infinite score glitch.">Olingan tanga qayta ochko bermasligi uchun darhol yashirinishi shart</span>.</div>
      <div>3. <strong>Vaqtinchalik Himoya:</strong> <span data-ru="После удара о шип ставить «Ждать 1 секунду», чтобы не сгорели все жизни сразу." data-en="After taking damage, wait 1 second to avoid instant health depletion.">Tikanga tekkanda 1 soniya kutish qo'yib, barcha jonlar birdan ketishini oldini olish</span>.</div>
    </div>
    """

    sec2_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="Блоки сбора монеты и урона от шипов в Scratch:" data-en="Coin collection and spike damage blocks in Scratch:">Tangani yig'ish va tikandan jon yo'qotish bloklari:</p>
    <pre style="background:var(--surface-2); padding:6px; font-size:11px; border-radius:4px; margin:0;"><code class="language-yaml"># Tanga skripti
qachonki [bayroqcha] bosilganda:
  ko'rsatish
  doim takrorlash:
    agar <[Mushuk]ga tegdimi?> u holda:
      [Ballar] ni (10) ga o'zgartirish
      yashirinish</code></pre>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Элемент Игры" data-en="Game Element">O'yin Qismi</th>
            <th style="padding:4px 6px;" data-ru="Переменная" data-en="Variable">O'zgaruvchi</th>
            <th style="padding:4px 6px;" data-ru="Действие" data-en="Action">Harakat</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;">Start Reset</td>
            <td style="padding:4px 6px;">Ballar &amp; Jonlar</td>
            <td style="padding:4px 6px;">Ballar=0, Jonlar=3</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ Bajarildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;">Tangalar</td>
            <td style="padding:4px 6px;">Ballar</td>
            <td style="padding:4px 6px;">+10 ochko &amp; yashirinish</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ Bajarildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;">Tikanlar</td>
            <td style="padding:4px 6px;">Jonlar</td>
            <td style="padding:4px 6px;">-1 HP &amp; 1s kutish</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ Bajarildi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;">Yakuniy Shart</td>
            <td style="padding:4px 6px;">Game Over</td>
            <td style="padding:4px 6px;">Jonlar = 0 &rarr; Stop all</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ 100% Yashil</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    replacements = {
        "{{LESSON_NUM}}": "30",
        "{{LESSON_TITLE_UZ}}": "O'zgaruvchilar Sehri: Tangalar, Jonlar (HP) va Vaqt",
        "{{LESSON_TITLE_RU}}": "Магия Переменных: Монеты, Жизни (HP) и Таймер",
        "{{LESSON_TITLE_EN}}": "The Magic of Variables: Coins, Lives (HP) & Timers",
        "{{COHORT_LABEL_UZ}}": "5–6-sinf",
        "{{COHORT_LABEL_RU}}": "5–6 класс",
        "{{COHORT_LABEL_EN}}": "Grade 5–6",
        "{{TRACK_NAME_UZ}}": "Junior Creators & Kiber-Gigiyena Track",
        "{{TRACK_NAME_RU}}": "Junior Creators & Кибер-Гигиена",
        "{{TRACK_NAME_EN}}": "Junior Creators & Cyber Hygiene Track",
        "{{SECTION_1_CONTENT}}": sec1_html,
        "{{SECTION_2_CONTENT}}": sec2_html,
        "{{SECTION_3_CONTENT}}": sec3_html,
        "{{RUBRIC_T1_BALL}}": "4",
        "{{RUBRIC_T1_UZ}}": "1-Daraja: Baza (Ballar va Jonlar o'zgaruvchilarini to'g'ri ochish)",
        "{{RUBRIC_T1_RU}}": "Уровень 1: База (Создание переменных Очки и Жизни)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (Creating Score and Lives variables)",
        "{{RUBRIC_T2_BALL}}": "4",
        "{{RUBRIC_T2_UZ}}": "2-Daraja: Amaliyot (Tanganing yashirinishi va tikandan jon yo'qotish)",
        "{{RUBRIC_T2_RU}}": "Уровень 2: Практика (Исчезновение монет и урон от шипов)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Coin collection hiding and spike hazards)",
        "{{RUBRIC_T3_BALL}}": "2",
        "{{RUBRIC_T3_UZ}}": "3-Daraja: Challenge (30 soniyalik taymer va g'alaba ekrani)",
        "{{RUBRIC_T3_RU}}": "Уровень 3: Челлендж (Таймер на 30 секунд и экран победы)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (30s countdown timer & victory screen)"
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

    title_uz = "30-dars: O'zgaruvchilar Sehri: Tangalar, Jonlar (HP) va Vaqt"
    title_ru = "Урок 30: Магия Переменных: Монеты, Жизни (HP) и Таймер"
    title_en = "Lesson 30: The Magic of Variables: Coins, Lives (HP) & Timers"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tasks_html = """
    <!-- TIER 1 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1-Daraja (Baza — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Создание Переменных в Scratch" data-en="Creating Variables in Scratch">Scratch-da O'zgaruvchilar Ochish</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Создайте две переменные `Монеты` и `Жизни`. Напишите скрипт под зеленым флажком, который задает Монеты = 0 и Жизни = 3." data-en="Create two variables `Score` and `Lives`. Program a green flag script setting Score = 0 and Lives = 3.">Scratch-da `Tangalar` va `Jonlar` nomli 2 ta o'zgaruvchi oching va yashil bayroqcha bosilganda ularni 0 hamda 3 ga tenglashtiruvchi bloklarni yozing.</p>
      <textarea id="hw_code_t1" class="code-editor" style="width:100%; min-height:80px; background:#0f172a; color:#f8fafc; font-family:monospace; font-size:11px; padding:8px; border-radius:4px; border:1px solid #334155;"># 1-Daraja javobingizni yozing:
qachonki [bayroqcha] bosilganda:
  [Tangalar] ni (0) ga sozlash
  [Jonlar] ni (3) ga sozlash
</textarea>
    </div>

    <!-- TIER 2 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">2-Daraja (Amaliyot — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Сбор Монеты и Потеря Жизни" data-en="Coin Collection & Health Loss">Tanga Yig'ish va Tikandan Jon Yo'qotish</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите алгоритм для спрайта Монетки (касается кота &rarr; +10 очков и спрятаться) и спрайта Шипа (касается кота &rarr; -1 жизнь и ждать 1 секунду)." data-en="Write the script for the Coin sprite (+10 Score and hide upon touch) and the Spike hazard (-1 HP and wait 1s cooldown).">Tanga sprayti uchun (+10 ball va yashirinish) hamda Tikan sprayti uchun (-1 jon va 1 soniya kutish) bloklar ketma-ketligini tuzing.</p>
      <textarea id="hw_code_t2" class="code-editor" style="width:100%; min-height:100px; background:#0f172a; color:#f8fafc; font-family:monospace; font-size:11px; padding:8px; border-radius:4px; border:1px solid #334155;"># 2-Daraja javobingizni yozing:
agar <[Mushuk]ga tegdimi?> u holda:
  [Tangalar] ni (10) ga o'zgartirish
  yashirinish
</textarea>
    </div>

    <!-- TIER 3 (2 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);">3-Daraja (Kiber-Challenge — 2 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Таймер Обратного Отсчета" data-en="Countdown Timer Logic">Teskari Hisoblovchi Taymer</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите скрипт для таймера: задать Время = 20, в цикле ждать 1 секунду, изменять Время на -1. Когда Время = 0 &rarr; остановить все скрипты!" data-en="Write a countdown timer script: set Timer = 20, loop with wait 1s and decrement by -1, and stop all scripts when Timer = 0.">Vaqt = 20 soniyadan boshlanib, har 1 soniyada 1 ga kamayuvchi va 0 bo'lganda o'yinni to'xtatuvchi to'liq taymer skriptini yozing.</p>
      <textarea id="hw_code_t3" class="code-editor" style="width:100%; min-height:90px; background:#0f172a; color:#f8fafc; font-family:monospace; font-size:11px; padding:8px; border-radius:4px; border:1px solid #334155;"># 3-Daraja javobingizni yozing:
[Vaqt] ni (20) ga sozlash
takrorlash toki <[Vaqt] = 0>:
  kutish (1) soniya
  [Vaqt] ni (-1) ga o'zgartirish
barchasini to'xtatish
</textarea>
    </div>
    """

    replacements = {
        "{{LESSON_NUM}}": "30",
        "{{LESSON_TITLE_UZ}}": "O'zgaruvchilar Sehri: Tangalar, Jonlar (HP) va Vaqt",
        "{{LESSON_TITLE_RU}}": "Магия Переменных: Монеты, Жизни (HP) и Таймер",
        "{{LESSON_TITLE_EN}}": "The Magic of Variables: Coins, Lives (HP) & Timers",
        "{{COHORT_LABEL_UZ}}": "5–6-sinf",
        "{{COHORT_LABEL_RU}}": "5–6 класс",
        "{{COHORT_LABEL_EN}}": "Grade 5–6",
        "{{RUBRIC_T1_BALL}}": "4",
        "{{RUBRIC_T1_UZ}}": "1-Daraja: Baza (Tangalar va Jonlar o'zgaruvchilarini ochish)",
        "{{RUBRIC_T1_RU}}": "Уровень 1: База (Создание переменных Монеты и Жизни)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (Creating Score and Lives variables)",
        "{{RUBRIC_T2_BALL}}": "4",
        "{{RUBRIC_T2_UZ}}": "2-Daraja: Amaliyot (Tanga yig'ish va tikandan jon yo'qotish)",
        "{{RUBRIC_T2_RU}}": "Уровень 2: Практика (Сбор монет и урон от шипов)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Coin collection and spike damage)",
        "{{RUBRIC_T3_BALL}}": "2",
        "{{RUBRIC_T3_UZ}}": "3-Daraja: Challenge (20 soniyalik teskari taymer)",
        "{{RUBRIC_T3_RU}}": "Уровень 3: Челлендж (Таймер обратного отсчета на 20 сек)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (20s countdown timer)",
        "{{TASKS_HTML}}": tasks_html,
        "{{LESSON_SLUG}}": "5-6-w12-l30-ozgaruvchilar-tangalar-va-jonlar"
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    doc = """# 30-dars: O'zgaruvchilar Sehri: Tangalar, Jonlar (HP) va Vaqt Hisobi (O'qituvchi Metodologiyasi)

## Darsning Pasporti
- **Sinf:** 5–6-sinf (Junior Creators & Kiber-Gigiyena Track)
- **Davomiyligi:** 80 daqiqa (Juftlik Dars / Double Block)
- **Asosiy maqsad:** O'quvchilarga Scratch dasturlash muhitida o'yin mantig'ining poydevori bo'lgan "O'zgaruvchilar" (Variables) tushunchasini o'rgatish. Tangalar yig'ish (+10 ochko), olingan tangani yashirish, tikanlarga tekkanda jonlarni yo'qotish (-1 HP va 1s kutish) hamda 30 soniyalik teskari hisoblovchi taymer bilan to'liq mini-arkada o'yinini yaratish.

---

## 80 Daqiqalik Aniq Vaqt Taqsimoti (Pacing)

### 1-Qism: Nazariya, Xatolar Tahlili va Jonli Test (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Motivatsiya | 1 | Nega o'zgaruvchisiz o'yin zerikarli ekani va bugun haqiqiy ballar tizimi qurilishini e'lon qilish. | Diqqat bilan tinglaydilar va maqsadni tushunadilar. |
| **04:00–12:00** | 29-dars HW Tahlili | 2 | Sehrli Labirintda qora devorga tekkanda orqaga -10 qadam otilishni unutib, devorga botib qolish xatosini ko'rsatish. | Blitz savolga javob beradilar, -10 qadam qoidasini yozadilar. |
| **12:00–18:00** | O'zgaruvchi Nima? | 3 | O'zgaruvchini nomlangan "sehrli quti" sifatida tushuntirish (nomi va ichidagi son). | Nom va qiymat farqini anglaydilar. |
| **18:00–24:00** | Scratch Bloklari | 4 | To'q sariq bo'limdagi "set to 0" va "change by 1" bloklari farqini doskada ko'rsatish. | Bloklarni daftarlariga chizadilar. |
| **24:00–30:00** | Tanga Algoritmi | 5 | Nega tanga olinganda yashirinishi shartligini tushuntirish (cheksiz ochko xatosidan himoya). | Tanganing 4 qadamini o'rganadilar. |
| **30:00–35:00** | Jonlar (HP) Tizimi | 6 | Tikanga tekkanda nega 1 soniya kutish shartligini ko'rsatish (barcha jonlar bir zumda tugamasligi uchun). | HP algoritmini tahlil qiladilar. |
| **35:00–40:00** | Taymer Mexanikasi | 7 | 30 soniyadan teskari hisoblovchi taymer bloklarini doskaga yozish. | Vaqt hisobi qanday ishlashini tushunadilar. |

### 2-Qism: Smartboard Sinovi, Katta Arena va Showcase (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **40:00–48:00** | Smartboard Simulyatori | 8 | Slayddagi interaktiv tangalar va jonlar simulyatorini ishga tushirish. | O'quvchi doskaga chiqib tanga yig'ishni sinab ko'radi. |
| **48:00–55:00** | Viktorina (Quiz) | 9 | 3 ta qiziqarli savol bo'yicha sinf bilan tezkor viktorina o'tkazish. | Faol qo'l ko'tarib javob beradilar. |
| **55:00–70:00** | 25 Daqiqalik Arena | 10 | 25:00 taymerni yoqish, partalar bo'ylab yurib Scratchda ko'maklashish. | playground/index.html da o'z arkada o'yinlarini yaratadilar. |
| **70:00–74:00** | Partadosh Auditi | 11 | O'rin almashish: partadoshining o'yinida tangalar va jonlar to'g'ri ishlashini tekshirish. | Bir-birining o'yinida xatolarni qidiradilar. |
| **74:00–76:00** | Katta Ekran Showcasi | 12 | Eng yaxshi arkada o'yinini katta ekranga chiqarib o'ynab ko'rsatish. | Sinfdoshlarining natijasini olqishlaydilar. |
| **76:00–78:00** | Baholash Rubrikasi | 13 | 10 ballik rubrika bo'yicha baholarni e'lon qilish. | Kundaliklariga ballarni qayd etadilar. |
| **78:00–80:00** | Uy Vazifasi va Yakun | 14 | 10 ballik uy vazifasini tushuntirish va keyingi Broadcast mavzusiga ko'prik! | Darsni yakunlaydilar. |

---

## O'qituvchi Uchun Muhim Blitz Savollari
1. **"Nega tanga mushukka tekkanda darhol 'yashirinish' (hide) bloki berilishi shart?"**
   - Javob: Chunki mushuk tanga ustida tursa, sikl har millisekundda ochko qo'shib, soniyada 1000 ball berib yuboradi! Yashirinish orqali tanga faqat bir marta ochko beradi.
2. **"Tikanga tekkanda nega '1 soniya kutish' bloki qo'yiladi?"**
   - Javob: Chunki o'yin soniyasiga 60 marta takrorlanadi. Agar kutish qo'yilmasa, o'yinchi tikanga tekkan 0.05 soniyadayoq barcha 3 ta jonidan ayrilib mag'lub bo'ladi.

---

## 10 Ballik Baholash Rubrikasi
- **4 Ball (Baza):** Ballar va Jonlar o'zgaruvchilarini yaratadi va bayroqcha bilan 0 hamda 3 ga sozlaydi.
- **4 Ball (Amaliyot):** Tangalar +10 ochko berib yashirinadi, tikanlar esa -1 jon olib qahramonni qaytaradi.
- **2 Ball (Challenge):** 30 soniyalik teskari taymerni to'g'ri bog'laydi va g'alaba ekranini chiqaradi!
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("  ✓ Created: TEACHER_READING.md")

def build_playground():
    html = """<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title data-ru="Scratch: Монеты и Жизни — Игровая Площадка" data-en="Scratch: Coins & Lives — Game Playground">Scratch: Tangalar va Jonlar — Arkada Maydonchasi</title>
<link rel="stylesheet" href="../../../../assets/brand.css">
<style>
:root {
  --bg-dark: #090d16;
  --surface-panel: #111827;
  --surface-border: #1f2937;
  --accent-yellow: #f59e0b;
  --accent-red: #ef4444;
  --accent-blue: #3b82f6;
  --accent-green: #10b981;
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
  background: rgba(245,158,11,0.15);
  color: var(--accent-yellow);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-family: monospace;
}
.main-grid {
  flex: 1;
  display: grid;
  grid-template-columns: 1fr 320px;
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
  background: #020617;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}
canvas {
  background: #0f172a;
  border: 2px solid #334155;
  border-radius: 6px;
  box-shadow: 0 0 20px rgba(0,0,0,0.6);
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
  background: var(--accent-yellow);
  color: #000;
  border: none;
  padding: 8px 14px;
  border-radius: 6px;
  font-weight: 700;
  font-size: 12px;
  cursor: pointer;
}
.btn:hover { opacity: 0.9; }
.hud-card {
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
    <span class="badge-tech">SCRATCH 3.0 ARCADE</span>
    <span data-ru="Студия Монет и Жизней" data-en="Coins & Lives Arcade">Tangalar va Jonlar Maydonchasi</span>
  </div>
  <div style="font-size:12px; font-weight:700;">
    <span>💰 <span data-ru="Монеты:" data-en="Score:">Tangalar:</span> <strong id="hudScore" style="color:var(--accent-yellow);">0</strong></span>
    <span style="margin-left:14px;">❤️ <span data-ru="Жизни:" data-en="Lives:">Jonlar:</span> <strong id="hudLives" style="color:var(--accent-red);">3</strong></span>
    <span style="margin-left:14px;">⏱️ <span data-ru="Таймер:" data-en="Timer:">Vaqt:</span> <strong id="hudTime" style="color:var(--accent-blue);">30s</strong></span>
  </div>
  <div>
    <button class="btn" onclick="resetGame()" data-ru="🔄 Начать Заново" data-en="🔄 Reset Game">🔄 Yangi O'yin</button>
  </div>
</header>

<div class="main-grid">
  <!-- CANVAS STAGE -->
  <div class="panel">
    <div class="panel-header">
      <span data-ru="ИГРОВАЯ СЦЕНА (УПРАВЛЕНИЕ: СТРЕЛКИ НА КЛАВИАТУРЕ)" data-en="GAME STAGE (CONTROLS: ARROW KEYS)">ARKADA SAHNASI (BOSHQARUV: KLAVIATURA STRELKALARI)</span>
      <span id="gameStatusBadge" style="color:var(--accent-green); font-size:10px;">Status: O'yin Davom Etmoqda</span>
    </div>
    <div class="arena-view">
      <canvas id="gameCanvas" width="480" height="360"></canvas>
    </div>
  </div>

  <!-- SIDEBAR INSTRUCTIONS -->
  <div class="panel">
    <div class="panel-header">
      <span data-ru="МИССИЯ И ПОДСКАЗКИ" data-en="MISSION & TIPS">O'YIN QOIDALARI</span>
      <span style="color:#64748b; font-size:10px;">Scratch Variables</span>
    </div>
    <div class="sidebar-body">
      <div class="hud-card">
        <div style="color:var(--accent-yellow); font-weight:700; margin-bottom:4px;" data-ru="🎯 Твоя Задача:" data-en="🎯 Your Objective:">🎯 Sening Vazifang:</div>
        <div style="font-size:11px; color:#cbd5e1;" data-ru="1. Собери все 5 золотых монет (+10 очков каждая).<br>2. Остерегайся красных огненных ловушек (-1 HP)!<br>3. Успей до того, как таймер покажет 0 секунд." data-en="1. Grab all 5 golden coins (+10 points each).<br>2. Avoid blazing red hazard traps (-1 HP)!<br>3. Beat the countdown before timer reaches 0.">1. Barcha 5 ta oltin tangani yig' (+10 ball har biri).<br>2. Qizil olovli tuzoqlardan qoch (-1 jon ketadi)!<br>3. Taymer 0 bo'lmasidan oldin ulgur.</div>
      </div>

      <div class="hud-card" style="background:#090d16;">
        <div style="color:var(--accent-blue); font-weight:700; margin-bottom:4px;" data-ru="Scratch Код Монеты:" data-en="Scratch Coin Code:">Scratch Tanga Kodi:</div>
        <pre style="margin:0; font-size:10px; color:#38bdf8;">agar &lt;Mushukka tegdimi?&gt; u holda:
  [Tangalar] ni 10 ga oshirish
  yashirinish (hide)</pre>
      </div>

      <div style="font-size:11px; color:#64748b; line-height:1.5;">
        <span data-ru="💡 Подсказка: Используйте стрелки [Вверх], [Вниз], [Влево], [Вправо] для перемещения котенка по игровому полю!" data-en="💡 Tip: Use arrow keys [Up], [Down], [Left], [Right] to pilot the kitten across the screen!">💡 Maslahat: Mushukchani ekranda harakatlantirish uchun klaviaturadagi yo'nalish tugmalaridan (strelkalar) foydalaning!</span>
      </div>
    </div>
  </div>
</div>

<script>
var cvs = document.getElementById('gameCanvas');
var ctx = cvs.getContext('2d');

var score = 0;
var lives = 3;
var timeLeft = 30;
var timerInterval = null;
var isGameOver = false;

var player = {x: 50, y: 180, size: 24, speed: 4};
var keys = {};

var coins = [
  {x: 140, y: 80, radius: 10, collected: false},
  {x: 240, y: 180, radius: 10, collected: false},
  {x: 340, y: 80, radius: 10, collected: false},
  {x: 180, y: 280, radius: 10, collected: false},
  {x: 400, y: 280, radius: 10, collected: false}
];

var hazards = [
  {x: 180, y: 120, width: 30, height: 30},
  {x: 290, y: 230, width: 30, height: 30}
];

var damageCooldown = false;

window.addEventListener('keydown', function(e) {
  if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].indexOf(e.key) !== -1) {
    e.preventDefault();
  }
  keys[e.key] = true;
});
window.addEventListener('keyup', function(e) {
  keys[e.key] = false;
});

function startTimer() {
  if (timerInterval) clearInterval(timerInterval);
  timerInterval = setInterval(function() {
    if (isGameOver) return;
    timeLeft--;
    document.getElementById('hudTime').textContent = timeLeft + 's';
    if (timeLeft <= 0) {
      endGame(false, 'Vaqt tugadi! Mag‘lubiyat.');
    }
  }, 1000);
}

function endGame(won, msg) {
  isGameOver = true;
  clearInterval(timerInterval);
  var badge = document.getElementById('gameStatusBadge');
  if (won) {
    badge.textContent = 'G‘ALABA! 🏆';
    badge.style.color = 'var(--accent-green)';
  } else {
    badge.textContent = 'GAME OVER! 💀';
    badge.style.color = 'var(--accent-red)';
  }
}

function update() {
  if (isGameOver) return;

  if (keys['ArrowUp'] && player.y > player.size) player.y -= player.speed;
  if (keys['ArrowDown'] && player.y < cvs.height - player.size) player.y += player.speed;
  if (keys['ArrowLeft'] && player.x > player.size) player.x -= player.speed;
  if (keys['ArrowRight'] && player.x < cvs.width - player.size) player.x += player.speed;

  // Check coins
  var allCollected = true;
  for (var i = 0; i < coins.length; i++) {
    var c = coins[i];
    if (!c.collected) {
      allCollected = false;
      var dist = Math.hypot(player.x - c.x, player.y - c.y);
      if (dist < player.size + c.radius) {
        c.collected = true;
        score += 10;
        document.getElementById('hudScore').textContent = score;
      }
    }
  }

  if (allCollected) {
    endGame(true, 'G‘alaba! Barcha tangalar yig‘ildi!');
  }

  // Check hazards
  if (!damageCooldown) {
    for (var j = 0; j < hazards.length; j++) {
      var h = hazards[j];
      if (player.x + player.size/2 > h.x && player.x - player.size/2 < h.x + h.width &&
          player.y + player.size/2 > h.y && player.y - player.size/2 < h.y + h.height) {
        lives--;
        document.getElementById('hudLives').textContent = lives;
        damageCooldown = true;
        setTimeout(function() { damageCooldown = false; }, 1000);

        if (lives <= 0) {
          endGame(false, 'Barcha jonlar tugadi!');
        }
      }
    }
  }
}

function draw() {
  ctx.clearRect(0, 0, cvs.width, cvs.height);

  // Draw Hazards (Red Spikes)
  for (var j = 0; j < hazards.length; j++) {
    var h = hazards[j];
    ctx.fillStyle = '#ef4444';
    ctx.fillRect(h.x, h.y, h.width, h.height);
    ctx.fillStyle = '#fff';
    ctx.font = '10px sans-serif';
    ctx.fillText('⚠️', h.x + 8, h.y + 18);
  }

  // Draw Coins (Gold Circles)
  for (var i = 0; i < coins.length; i++) {
    var c = coins[i];
    if (!c.collected) {
      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(c.x, c.y, c.radius, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#fef08a';
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.fillStyle = '#000';
      ctx.font = 'bold 9px sans-serif';
      ctx.fillText('$', c.x - 3, c.y + 3);
    }
  }

  // Draw Player (Cat)
  ctx.save();
  ctx.translate(player.x, player.y);
  ctx.fillStyle = damageCooldown ? '#f87171' : '#38bdf8';
  ctx.beginPath();
  ctx.arc(0, 0, player.size/2, 0, Math.PI * 2);
  ctx.fill();

  // Cat Face
  ctx.fillStyle = '#000';
  ctx.font = '14px sans-serif';
  ctx.fillText('🐱', -7, 5);
  ctx.restore();

  // Game Over / Win Overlay
  if (isGameOver) {
    ctx.fillStyle = 'rgba(0,0,0,0.7)';
    ctx.fillRect(0, 0, cvs.width, cvs.height);
    ctx.fillStyle = lives > 0 ? '#10b981' : '#ef4444';
    ctx.font = 'bold 22px sans-serif';
    ctx.textAlign = 'center';
    var text = lives > 0 ? '🏆 G‘ALABA! 50 BALL!' : '💀 GAME OVER!';
    ctx.fillText(text, cvs.width/2, cvs.height/2);
    ctx.font = '12px sans-serif';
    ctx.fillStyle = '#cbd5e1';
    ctx.fillText('Yangi o‘yin uchun "🔄 Yangi O‘yin" tugmasini bosing', cvs.width/2, cvs.height/2 + 30);
  }
}

function gameLoop() {
  update();
  draw();
  requestAnimationFrame(gameLoop);
}

function resetGame() {
  score = 0;
  lives = 3;
  timeLeft = 30;
  isGameOver = false;
  damageCooldown = false;
  player.x = 50;
  player.y = 180;
  for (var i = 0; i < coins.length; i++) {
    coins[i].collected = false;
  }
  document.getElementById('hudScore').textContent = '0';
  document.getElementById('hudLives').textContent = '3';
  document.getElementById('hudTime').textContent = '30s';
  var badge = document.getElementById('gameStatusBadge');
  badge.textContent = 'Status: O‘yin Davom Etmoqda';
  badge.style.color = 'var(--accent-green)';
  startTimer();
}

resetGame();
gameLoop();
</script>

</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "playground", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: playground/index.html")

def main():
    print("📦 Building 5-6-sinf (Lesson 30: Variables, Coins & HP)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_playground()
    print("🎉 Done! Generated Grade 5–6 Lesson 30.")

if __name__ == "__main__":
    main()
