#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_5_6_w11_l27.py — Builder for 5–6th Grade, Week 11, Lesson 27

Mavzu: Takrorlanishlar Sehri: Cheksiz Harakat va Sikllar (Forever & Repeat Loops)
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 5-6-sinf (Junior Creators & Kiber-Gigiyena Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "5-6-sinf", "11-hafta", "27-dars-takrorlanishlar-va-sikllar")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "playground"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="5–6-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 27" data-en="GRADE 5–6 · WEEK 11 · LESSON 27">5–6-SINF · 11-HAFTA · 27-DARS</span></div>
    <h1 class="display" data-ru="Магия Повторений: Бесконечное Движение и Циклы в Scratch" data-en="Magic of Loops: Endless Motion & Repeat Blocks in Scratch">Takrorlanishlar Sehri: Cheksiz Harakat va Sikllar (Loops)</h1>
    <p class="lede" data-ru="Как заставить персонажа летать по экрану вечно: блоки «повторять всегда» (forever), «повторить 10 раз», отскок от краев и создание космической орбиты." data-en="How to make sprites fly indefinitely: 'forever' and 'repeat 10' blocks, screen boundary bouncing, and creating a cosmic spaceship orbit.">Qahramonni ekranda to'xtovsiz harakatlantirish siri: "doimiy takrorlash" (forever), "10 marta takrorlash", devordan qaytish va koinot uchar likopchasining orbitasini yaratish.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Блочные Циклы" data-en="Scratch Loops">Scratch Sikllari</h3>
        <p data-ru="Зачем писать 100 одинаковых блоков, если можно обернуть движение в один вечный цикл." data-en="Why stack 100 identical blocks when you can wrap movement in a single endless loop.">Nega 100 ta bir xil blok qo'yish kerak emas? Birgina sikl bloki butun animatsiyani cheksiz aylantiradi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Uchar Likopcha</div>
        <h3 data-ru="Космическая Орбита" data-en="Cosmic Orbit">Koinot Sayohati</h3>
        <p data-ru="Каждый ученик создаст летающую тарелку или комету, непрерывно парящую по экрану с вращением и отскоком." data-en="Each student programs a flying UFO or comet endlessly orbiting space with rotation and bounce guards.">Har bir o'quvchi yulduzlar aro to'xtovsiz aylanib yuruvchi va devordan qaytuvchi uchar likopcha yasaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 26-УРОКА" data-en="LESSON 26 HOMEWORK REVIEW">26-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Анимация Костюмов: Ловушка Сверхскоростного Мигания" data-en="Costume Animation: The Hyper-Speed Blinking Trap">Kostyumlar Animatsiyasi: Super-Tez Miltillash Xatosi</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Типичная ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Смена костюмов без паузы (блока «ждать»)" data-en="Switching Costumes Without 'Wait' Blocks">"Kutish" Blokisiz Kostyumni Almashtirish</h3>
        <p data-ru="Ученики ставили блок «следующий костюм» прямо в цикл. Компьютер переключает костюмы 60 раз в секунду — кот не идет, а превращается в размытое мерцающее пятно!" data-en="Students placed 'next costume' directly in a loop without pausing. The CPU cycles 60 times per second — the sprite flickers violently instead of walking smoothly!">O'quvchilar sikl ichiga "kutish" blokini qo'ymasdan faqat "keyingi kostyum" qo'yishdi. Kompyuter soniyasiga 60 marta almashtirgani uchun mushuk yurmaydi, balki ko'zga ko'rinmas darajada tez miltillab qoladi!</p>
        <pre><code>// ❌ Xato: Miltillovchi tushunarsiz tezlik
takrorla (cheksiz) {
  keyingi_kostyum(); // 0 soniya kutish!
}</code></pre>
      </div>
      <div class="box success-border">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой стандарт (Golden Solution)" data-en="Golden Standard">Oltin Standart (Golden Solution)</div>
        <h3 data-ru="Шаг + Следующий Костюм + Пауза 0.1 секунды" data-en="Step + Next Costume + 0.1s Wait">Qadam + Keyingi Kostyum + 0.1 Soniyalik Tanaffus</h3>
        <p data-ru="Человеческий глаз воспринимает плавную походку, когда между сменой кадров есть микропауза в 0.1 или 0.15 секунды. Тогда шаги выглядят как в настоящем мультфильме!" data-en="The human brain perceives smooth fluid motion when frames transition with a 0.1s to 0.15s micro-pause, mimicking real cartoon cinema!">Inson ko'zi harakatni ravon ko'rishi uchun har bir kadr oralig'ida 0.1 yoki 0.15 soniya kutish kerak. Shunda harakat xuddi haqiqiy Disney multfilmidagidek silliq bo'ladi!</p>
        <pre><code>// ✅ To'g'ri: Multfilmdek ravon animatsiya
takrorla (cheksiz) {
  10 qadam yur;
  keyingi_kostyum();
  0.1 soniya kut; // Silliq harakat!
}</code></pre>
      </div>
    </div>
    <div class="bridge-card" style="margin-top:12px; padding:10px 16px; border-radius:10px; background:rgba(59,130,246,0.08); border-left:4px solid var(--accent); display:flex; justify-content:space-between; align-items:center;">
      <div>
        <strong style="color:var(--accent);" data-ru="Блиц-вопрос (30 сек):" data-en="Blitz Question (30s):">⚡ Blitz-Savol (30s):</strong>
        <span data-ru="Что произойдет, если коту дать команду «идти 10 шагов» 100 раз без цикла?" data-en="What happens if we give the cat 'move 10 steps' 100 times without loops?">Agar mushukka siklsiz 100 marta ketma-ket "10 qadam yur" deb yozib chiqsak nima bo'ladi?</span>
      </div>
      <span class="badge" style="font-size:11px;" data-ru="Код станет бесконечным!" data-en="Code explodes!">Dastur qog'ozdek cho'zilib ketadi!</span>
    </div>
  </section>

  <!-- SLIDE 3: WHY LOOPS? -->
  <section class="slide" data-phase="Konsept|Концепт|Concept" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ЗАЧЕМ НУЖНЫ ЦИКЛЫ?" data-en="WHY DO WE NEED LOOPS?">SIKLLAR NIMA UCHUN KERAK?</span></div>
    <h2 data-ru="Сила Циклов: Избавляемся от Одинакового Труда" data-en="The Power of Loops: Eliminating Repetitive Labor">Sikllar Kuchi: Bir Xil Mehnatdan Qutulish</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:15px; margin-bottom:12px;" data-ru="<strong>Цикл (Loop):</strong> команда, которая заставляет компьютер повторять нужные действия снова и снова автоматически." data-en="<strong>Loop:</strong> an instruction that commands the computer to repeat specified actions automatically."><strong>Sikl (Loop):</strong> kompyuterga bir xil buyruqlarni avtomatik tarzda qayta-qayta bajarishni buyuruvchi sehrli blok.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Один блок вместо десятков:</strong> Вместо 50 отдельных блоков движения используется один компактный цикл." data-en="<strong>One Block Replaces Many:</strong> A single loop replaces 50 separate step commands."><strong>O'rniga bitta blok:</strong> 50 ta alohida blok o'rniga bitta ixcham sikl bloki kifoya.</li>
          <li data-ru="<strong>Бесконечная жизнь:</strong> Чтобы враги, ракеты и кометы летели непрерывно, нужен цикл «всегда» (forever)." data-en="<strong>Endless Life:</strong> Heroes, enemies, and obstacles stay active continuously via forever loops."><strong>Doimiy Harakat:</strong> O'yindagi dushmanlar, avtomobillar va yulduzlar to'xtamasdan oqishi uchun forever sikli kerak.</li>
          <li data-ru="<strong>Точный контроль:</strong> Прыгнуть ровно 10 раз или летать по экрану всю игру — количество задаем сами." data-en="<strong>Smart Control:</strong> Repeat 10 times for jumping, or repeat forever for planet rotation."><strong>Aniqlik:</strong> Qahramon 10 marta o'q otsin yoki butun umr koinotda aylansin — sonini o'zimiz belgilaymiz.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-size:12px; line-height:1.6;">
        <div style="font-weight:700; color:var(--accent); margin-bottom:8px;" data-ru="Сравнение в Scratch:" data-en="Scratch Comparison:">Scratch-da Taqqoslash:</div>
        <div style="background:rgba(239,68,68,0.1); border-left:3px solid var(--red); padding:8px 12px; border-radius:6px; margin-bottom:10px;">
          <strong style="color:var(--red);">❌ Siklsiz:</strong> 10 qadam yur ➔ 10 qadam yur ➔ 10 qadam yur ➔ ... (50 ta blok, 2 metr cho'zilgan kod!)
        </div>
        <div style="background:rgba(16,185,129,0.1); border-left:3px solid var(--green); padding:8px 12px; border-radius:6px;">
          <strong style="color:var(--green);">✅ Sikl Bilan:</strong> [ 10 marta takrorlash: 10 qadam yur ] — atigi 1 ta toza sariq blok!
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: TWO TYPES OF LOOPS -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="ДВА ГЛАВНЫХ ЦИКЛА SCRATCH" data-en="TWO MAIN SCRATCH LOOPS">IKKITA ASOSIY SIKL TURI</span></div>
    <h2 data-ru="«Повторять Всегда» против «Повторить N Раз»" data-en="'Forever' vs 'Repeat N Times' Blocks">"Doimiy Takrorlash" va "N Marta Takrorlash" Farqi</h2>
    <div class="grid-2">
      <div class="box" style="border-top:3px solid var(--accent);">
        <div class="tag" style="color:var(--accent);">1. Cheksiz Sikl (Forever)</div>
        <h3 data-ru="Блок «Повторять Всегда»" data-en="'Repeat Forever' Block">"Doimiy Takrorlash" Bloki</h3>
        <p style="font-size:13px;" data-ru="Этот блок не имеет снизу выступа для присоединения других блоков. Почему? Потому что выполнение НИКОГДА не закончится, пока игрок не нажмет красный знак СТОП!" data-en="This block lacks a bottom connector notch. Why? Because it runs endlessly until the red STOP button is clicked!">Bu blokning pastki qismida ulanish tishi yo'q. Nega? Chunki u HECH QACHON to'xtamaydi — faqat qizil "STOP" tugmasi bosilgandagina to'xtaydi!</p>
        <div style="background:var(--surface-2); padding:8px 12px; border-radius:6px; font-family:var(--font-mono); font-size:12px; color:var(--accent);">
          Qayerda ishlatiladi: Koinot fonidagi yulduzlar harakati, dushman samolyotining uchishi, fon musiqasi.
        </div>
      </div>
      <div class="box" style="border-top:3px solid var(--purple);">
        <div class="tag" style="color:var(--purple);">2. Sanovchi Sikl (Repeat N)</div>
        <h3 data-ru="Блок «Повторить 10 Раз»" data-en="'Repeat 10 Times' Block">"10 Marta Takrorlash" Bloki</h3>
        <p style="font-size:13px;" data-ru="Внутрь блока можно вписать любое число: 5, 10, 100. Когда действие повторится нужное количество раз, цикл завершится и программа пойдет дальше." data-en="Type any count: 5, 10, 100. Once the count is fulfilled, the loop terminates and passes control downwards.">Ichiga xohlagan sonni yozish mumkin: 5, 10, 20. Sanab bo'lingach, sikl to'xtaydi va keyingi bloklarga navbat beradi.</p>
        <div style="background:var(--surface-2); padding:8px 12px; border-radius:6px; font-family:var(--font-mono); font-size:12px; color:var(--purple);">
          Qayerda ishlatiladi: Qahramon 10 marta yuqoriga sakrab tushishi, 5 marta ko'z qisishi, 3 ta o'q uzishi.
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: BOUNCE ON EDGE -->
  <section class="slide" data-phase="Mexanizm|Механизм|Mechanism" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="ЗАЩИТА ОТ ВЫЛЕТА ЗА ЭКРАН" data-en="SCREEN BOUNDARY BOUNCE">CHEKKAGA YETGANDA QAYTISH</span></div>
    <h2 data-ru="Блок «Если Касается Края, Оттолкнуться» и Стиль Вращения" data-en="'If on Edge, Bounce' & Rotation Style Rules">"Agar Chekkaga Yetsa, Qaytish" va Aylanish Uslubi</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Если не поставить этот блок, ваш персонаж улетит за пределы экрана и навсегда пропадет из вида!" data-en="Without this guard block, sprites drift off-screen and disappear forever!">Agar bu blokni qo'ymasangiz, qahramoningiz ekrandan chiqib ketadi va ko'rinmay qoladi!</p>
        <ul class="clean-list">
          <li data-ru="<strong>Отскок (Bounce):</strong> При касании координаты X = 240 или Y = 180 спрей поворачивается в обратную сторону." data-en="<strong>Bounce:</strong> Touching coordinate boundaries instantly inverts motion direction."><strong>Qaytish (Bounce):</strong> Qahramon X=240 yoki Y=180 chegarasiga yetganda, orqaga buriladi.</li>
          <li data-ru="<strong>Проблема переворота:</strong> При обычном отскоке кот может перевернуться вниз головой." data-en="<strong>Upside Down Trap:</strong> Bouncing can flip characters upside-down without rotation styles!"><strong>Teskari bo'lib qolish xatosi:</strong> Qahramon qaytganda boshi bilan pastga aylanib qolishi mumkin.</li>
          <li data-ru="<strong>Решение — стиль «влево-вправо»:</strong> Блок <code>стиль вращения [влево-вправо]</code> удерживает спрей строго вертикально!" data-en="<strong>Left-Right Fix:</strong> <code>set rotation style [left-right]</code> ensures sprites only face left or right cleanly."><strong>Yechim — Chap-O'ng Uslubi:</strong> <code>aylanish uslubini [chap-o'ng] qilib o'rnatish</code> bloki mushukning tik yurishini kafolatlaydi!</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:12px; line-height:1.6;">
        <div style="color:var(--accent); font-weight:700; margin-bottom:8px;">[Oltin Scratch Skripti]</div>
        <div style="color:var(--green);">qachonki [yashil bayroqcha] bosilganda</div>
        <div style="color:var(--ink-2); margin-left:14px;">aylanish uslubini [chap-o'ng] ga sozla;</div>
        <div style="color:var(--purple); margin-left:14px;">doimiy takrorlash {</div>
        <div style="color:var(--ink); margin-left:28px;">10 qadam yur;</div>
        <div style="color:var(--ink); margin-left:28px;">keyingi kostyum;</div>
        <div style="color:var(--amber); margin-left:28px;">agar chekkaga yetsa, qaytish;</div>
        <div style="color:var(--ink-2); margin-left:28px;">0.1 soniya kut;</div>
        <div style="color:var(--purple); margin-left:14px;">}</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: SMOOTH ROTATION & ORBIT -->
  <section class="slide" data-phase="Kosmik Mexanika|Космическая Механика|Cosmic Mechanics" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ОРБИТА И ВРАЩЕНИЕ" data-en="ORBIT & ROTATION">BURILISH VA ORBITADA UCHISH</span></div>
    <h2 data-ru="Как Заставить Тарелку Летать по Кругу? (Поворот на N Градусов)" data-en="How to Orbit in Circles? (Turn N Degrees)">Qanday Qilib Aylanma Orbitada Uchiladi? (Burilish Burchagi)</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">To'g'ri Chiziq</div>
        <h4 data-ru="Только Вперед" data-en="Straight Motion">Faqat To'g'riga</h4>
        <p style="font-size:12px;" data-ru="Шаг вперед без поворота. Персонаж бегает от стенки к стенке по прямой линии." data-en="Moving forward without rotation results in straight line ping-pong motion.">Burilishsiz qadam qo'yish. Qahramon faqat bitta to'g'ri chiziq bo'ylab u devordan bu devorga borib qaytadi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">Dumaloq Orbita</div>
        <h4 data-ru="Шаг + Поворот 5°" data-en="Step + Turn 5°">Qadam + 5° Burilish</h4>
        <p style="font-size:12px;" data-ru="Каждый шаг поворачиваем на 5 или 10 градусов. Получается идеальная круговая орбита планеты или НЛО!" data-en="Turning 5 to 10 degrees each step naturally forms an exquisite orbital curve!">Har qadamda 5 yoki 10 gradus burilsa, qahramon doira bo'ylab uchar likopchadek silliq aylanishni boshlaydi!</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(245,158,11,0.15); color:var(--amber);">Spiralli Girdob</div>
        <h4 data-ru="Переменная Скорость" data-en="Varying Speed">Kengayuvchi Spirala</h4>
        <p style="font-size:12px;" data-ru="Если постепенно увеличивать шаги, тарелка начнет раскручиваться из центра наружу, как галактика." data-en="Gradually increasing speed causes the sprite to spiral outward like a galaxy.">Har qadamda tezlikni oshirib borsak, uchar likopcha galaktika kabi markazdan kengayib uchadi.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px; background:rgba(0,0,0,0.2); border:1px solid var(--hair);">
      <strong style="color:var(--accent); font-size:12px;" data-ru="Космическая формула полета UFO:" data-en="Cosmic UFO Flight Formula:">Kosmik Uchar Likopcha Formulasi:</strong>
      <div style="font-family:var(--font-mono); font-size:12px; margin-top:4px;">
        <code>doimiy takrorlash { 6 qadam yur; 4 gradus o'ngga buril; agar chekkaga yetsa, qaytish; }</code>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: COSTUME + SOUND INSIDE LOOP -->
  <section class="slide" data-phase="Kombinatsiya|Комбинация|Combination" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ЖИВОЙ МИР ВНУТРИ ЦИКЛА" data-en="ANIMATED SPRITES">SIKL ICHIDA HARAKAT VA OVOZ</span></div>
    <h2 data-ru="Сборка Мега-Блока: Движение, Костюм и Космический Звук" data-en="Building the Mega-Block: Motion, Costumes & Cosmic Audio">Mega-Blok: Harakat, Kostyum va Kosmik Audio Birgalikda</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Внутрь одного цикла можно помещать сразу 4 разные команды! Они будут выполняться по очереди сверху вниз, создавая эффект живой игры." data-en="You can stack 4 distinct action blocks within a single loop, executing sequentially top-to-bottom!">Bitta sikl ichiga bir vaqtning o'zida 4 ta turli buyruq qo'yish mumkin! Ular ketma-ket bajarilib, jonli o'yin hissini uyg'otadi.</p>
        <ol class="clean-list" style="font-size:12px;">
          <li data-ru="<strong>1. Движение:</strong> Спрей смещается на несколько шагов вперед." data-en="<strong>1. Motion:</strong> Moves sprite forward by a set step count."><strong>1. Harakat:</strong> Qahramon oldinga bir necha qadam siljiydi.</li>
          <li data-ru="<strong>2. Анимация:</strong> Сменяется кадр костюма (сопла двигателя светятся)." data-en="<strong>2. Animation:</strong> Cycles costume frame (rocket thruster glows)."><strong>2. Animatsiya:</strong> Raketa olovi miltillab yangi kostyumga o'tadi.</li>
          <li data-ru="<strong>3. Проверка границы:</strong> Если врезался в край космоса — плавно отскакивает." data-en="<strong>3. Border Guard:</strong> Bounces off cosmic screen boundaries."><strong>3. Chegara:</strong> Kosmos chekkasiga yetganda silliq qaytadi.</li>
          <li data-ru="<strong>4. Звуковой импульс:</strong> Каждые 10 шагов проигрывается лазерный звук." data-en="<strong>4. Audio Pulse:</strong> Plays laser or thruster sound effect."><strong>4. Ovoz:</strong> Dvigatel shovqini yoki lazer ovozi yangraydi.</li>
        </ol>
      </div>
      <div class="box" style="background:var(--surface-2); display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
        <div style="font-size:42px; margin-bottom:8px;">🛸 ✨ 🪐</div>
        <h4 style="margin:4px 0; color:var(--green);" data-ru="Результат: Живой Космос" data-en="Outcome: Living Cosmos">Natija: Jonli Kosmik Sahnasi</h4>
        <p style="font-size:12px; color:var(--ink-2); max-width:280px;" data-ru="Спрей больше не ждет нажатия клавиш. Он живет своей жизнью в бесконечном цикле!" data-en="The sprite no longer waits for key clicks. It lives autonomously in an infinite loop!">Qahramon tugma bosilishini kutib o'tirmaydi. U cheksiz sikl ichida mustaqil ravishda koinotni kezadi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: IN-DECK INTERACTIVE SIMULATOR -->
  <section class="slide" data-phase="Jonli Sinov|Интерактив|Live Demo" data-time="40:00–48:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="СИМУЛЯТОР В ПРЕЗЕНТАЦИИ" data-en="IN-DECK SIMULATOR">SMARTBOARDDA JONLI SIKL SINOVI</span></div>
    <h2 data-ru="Интерактивная Лаборатория: Управление Циклом НЛО" data-en="Interactive Studio: UFO Loop Controller">Jonli Sinov: Uchar Likopcha Siklini Boshqarish</h2>
    <div class="box" style="padding:12px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <div style="display:flex; gap:8px; align-items:center;">
          <button class="btn" onclick="deckToggleLoop()" id="btnDeckLoop" style="background:var(--green); color:#fff; padding:6px 14px; font-size:12px;" data-ru="▶️ Запустить Цикл" data-en="▶️ Start Loop">▶️ Siklni Ishga Tushirish</button>
          <button class="btn" onclick="deckToggleBounce()" id="btnDeckBounce" style="background:var(--accent); color:#fff; padding:6px 12px; font-size:12px;" data-ru="🛡️ Отскок: ВКЛ" data-en="🛡️ Bounce: ON">🛡️ Qaytish: YOQILGAN</button>
          <button class="btn" onclick="deckResetUFO()" style="padding:6px 10px; font-size:12px;" data-ru="Сброс" data-en="Reset">Qayta O'rnatish</button>
        </div>
        <div style="display:flex; gap:12px; font-family:var(--font-mono); font-size:12px; color:var(--ink-2);">
          <span>Qadamlar: <strong style="color:var(--green);" id="deckStepCount">0</strong></span>
          <span>Burilish: <strong style="color:var(--amber);" id="deckTurnAngle">4°</strong></span>
        </div>
      </div>
      <div style="display:flex; justify-content:center;">
        <canvas id="deckUfoCanvas" width="400" height="240" style="background:#050814; border-radius:8px; border:1px solid var(--hair);"></canvas>
      </div>
      <div style="margin-top:8px; font-size:11px; color:var(--ink-2); display:flex; justify-content:space-between;">
        <span data-ru="💡 Изменяйте угол поворота и наблюдайте, как меняется космическая орбита" data-en="💡 Tweak rotation angles and observe how orbital curves transition">💡 Burilish burchagini o'zgartiring va uchar likopchaning kosmik orbitasini kuzating</span>
        <span id="deckLoopStatus" style="color:var(--green);" data-ru="Статус: Готов" data-en="Status: Ready">Status: Tayyor</span>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: INTERACTIVE QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Quiz" data-time="48:00–54:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА ЗНАНИЙ" data-en="KNOWLEDGE CHECK">3-SAVOLLI INTERAKTIV TEST</span></div>
    <h2 data-ru="Блиц-Тест: Циклы и Поведение Спрайтов" data-en="Fast Quiz: Loops & Sprite Behaviors">Bilimni Sinash: Scratch Sikllari va Qahramon Mantig'i</h2>
    <div class="quiz-container" style="display:flex; flex-direction:column; gap:12px;">
      <!-- Q1 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="1. Чем блок «повторять всегда» (forever) отличается от других блоков в Scratch?" data-en="1. How does the 'repeat forever' block differ from other Scratch blocks?">1. "Doimiy takrorlash" (forever) bloki Scratch-dagi boshqa bloklardan nimasi bilan farq qiladi?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Rangi sariq bo‘lishi boshqa bloklarda ham bor.')" style="font-size:12px;" data-ru="A) Он всегда только синего цвета" data-en="A) It is always blue">A) U har doim ko'k rangda bo'ladi</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! U cheksiz ishlagani uchun tagiga boshqa blok ulab bo‘lmaydi.')" style="font-size:12px;" data-ru="B) У него нет нижнего паза, он работает бесконечно" data-en="B) It has no bottom connector notch as it runs endlessly">B) Uning pastki qismida ulanish tishi yo'q, chunki u hech qachon tugamaydi</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Matn yozish mumkin emas.')" style="font-size:12px;" data-ru="C) В него нельзя класть другие блоки" data-en="C) You cannot nest blocks inside it">C) Uning ichiga boshqa bloklarni qo'yib bo'lmaydi</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
      <!-- Q2 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="2. Зачем между сменой костюмов в цикле ставить блок «ждать 0.1 секунды»?" data-en="2. Why add a 'wait 0.1 seconds' block between costume swaps in a loop?">2. Nega sikl ichida kostyumlarni almashtirganda "0.1 soniya kutish" bloki qo'yiladi?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Ranglar kutish blokiga bog‘liq emas.')" style="font-size:12px;" data-ru="A) Чтобы изменить цвет костюма" data-en="A) To change costume colors">A) Kostyum rangini o'zgartirish uchun</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'Aynan shunday! Bo‘lmasa kadrlar ko‘zga ko‘rinmas darajada tez miltillab ketadi.')" style="font-size:12px;" data-ru="B) Чтобы анимация была плавной, а не бешено мигала" data-en="B) To make animation smooth rather than violently flickering">B) Animatsiya miltillab ketmasdan multfilmdek silliq ko'rinishi uchun</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Musiqa ovoz bloklaridan qo‘yiladi.')" style="font-size:12px;" data-ru="C) Чтобы включилась музыка" data-en="C) To trigger background music">C) Musiqa yangrashi uchun</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
      <!-- Q3 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="3. Какой блок не дает коту перевернуться вверх тормашками при отскоке от края?" data-en="3. Which block prevents the cat from flipping upside-down when bouncing?">3. Qaysi buyruq mushuk devordan qaytganda boshi bilan teskari aylanib qolmasligini ta'minlaydi?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! Chap-O‘ng uslubi qahramonni faqat to‘g‘ri vertikal ushlaydi.')" style="font-size:12px;" data-ru="A) Стиль вращения [влево-вправо]" data-en="A) Set rotation style [left-right]">A) Aylanish uslubini [chap-o'ng] ga sozlash</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Bu faqat o‘lchamni o‘zgartiradi.')" style="font-size:12px;" data-ru="B) Изменить размер на 10" data-en="B) Change size by 10">B) O'lchamni 10 ga o'zgartirish</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Bu orqa fonni o‘zgartiradi.')" style="font-size:12px;" data-ru="C) Следующий фон" data-en="C) Next backdrop">C) Keyingi fon</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: 25-MINUTE HANDS-ON ARENA -->
  <section class="slide" data-phase="Kiber-Arena|Практика|Hands-on Lab" data-time="54:00–69:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="БОЛЬШАЯ ПРАКТИЧЕСКАЯ АРЕНА" data-en="PRACTICE ARENA">25 DAQIQALIK AMALIY ARENA</span></div>
    <h2 data-ru="Миссия: Собери Летающую Тарелку или Комету в Космосе" data-en="Mission: Build an Orbiting UFO or Cosmic Comet">Kiber-Missiya: Koinotda Uchar Likopcha yoki Kometani Uchirish</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:10px;" data-ru="Откройте Scratch 3.0 или нашу песочницу playground/index.html и соберите космическую анимацию." data-en="Launch Scratch 3.0 or our playground/index.html and assemble the cosmic orbital project.">Scratch 3.0 dasturini yoki <a href="playground/index.html" target="_blank" style="color:var(--accent); font-weight:700;">playground/index.html</a> laboratoriyamizni oching va koinot animatsiyasini quring.</p>
        <ul class="clean-list">
          <li data-ru="<strong>1-Шаг:</strong> Добавьте космический фон (Stars) и выберите спрей (UFO, Rocket или Star)." data-en="<strong>Step 1:</strong> Select 'Stars' space backdrop and choose a sprite (UFO, Rocket, Star)."><strong>1-Qadam:</strong> Qora koinot fonini tanlang va uchar likopcha (yoki raketa) spraytini qo'ying.</li>
          <li data-ru="<strong>2-Шаг:</strong> Соберите вечный цикл: <code>идти 8 шагов</code> + <code>повернуть на 4 градуса</code>." data-en="<strong>Step 2:</strong> Assemble forever loop: <code>move 8 steps</code> + <code>turn 4 degrees</code>."><strong>2-Qadam:</strong> Doimiy takrorlash siklini tuzing: <code>8 qadam yur</code> + <code>4 gradus o'ngga buril</code>.</li>
          <li data-ru="<strong>3-Шаг:</strong> Добавьте блок «если на краю, оттолкнуться» и смену костюма пламени двигателя!" data-en="<strong>Step 3:</strong> Add 'if on edge, bounce' and engine thruster costume animation!"><strong>3-Qadam:</strong> "Agar chekkaga yetsa, qaytish" blokini qo'ying va dvigatel olovining animatsiyasini ulang!</li>
        </ul>
      </div>
      <div class="box" style="border-left:4px solid var(--accent);">
        <h4 style="margin-bottom:8px;" data-ru="10-Балльная Рубрика Оценки:" data-en="10-Point Grading Rubric:">10 Ballik Baholash Mezoni:</h4>
        <div style="font-size:12px; line-height:1.8;">
          <div><strong style="color:var(--green);">4 Ball:</strong> Doimiy takrorlash sikli ishlaydi, qahramon to'xtovsiz harakatlanadi.</div>
          <div><strong style="color:var(--accent);">4 Ball:</strong> Chekkaga yetganda silliq qaytadi, aylanish uslubi to'g'ri sozlangan.</div>
          <div><strong style="color:var(--purple);">2 Ball (Bonus):</strong> Sikl ichida aylanma orbita va raketa olovi animatsiyasi bor!</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: PEER REVIEW -->
  <section class="slide" data-phase="Kiber-Audit|Код-Ревью|Peer Review" data-time="69:00–74:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМНЫЙ КОНТРОЛЬ" data-en="PEER REVIEW">PARTADOSH BILAN KIBER-AUDIT</span></div>
    <h2 data-ru="Обменяйтесь Местами: Проверьте Проект Друга" data-en="Swap Seats: Test Your Classmate's Project">Partadosh Bilan Almashing: 4 Bosqichli Kiber-Audit</h2>
    <div class="grid-4" style="gap:10px;">
      <div class="box" style="border-top:3px solid var(--green);">
        <div class="tag" style="color:var(--green);">1. Bayroqcha</div>
        <h4 data-ru="Старт с 1 Клика" data-en="1-Click Start">Yashil Bayroqcha</h4>
        <p style="font-size:12px;" data-ru="Нажмите зеленый флаг. Персонаж начинает движение сразу и сам?" data-en="Click green flag. Does sprite start smoothly on its own?">Yashil bayroqcha bosilganda qahramon darhol harakatga tushyaptimi?</p>
      </div>
      <div class="box" style="border-top:3px solid var(--accent);">
        <div class="tag" style="color:var(--accent);">2. Sikl Holati</div>
        <h4 data-ru="Не Зависает Ли?" data-en="Loop Persistence">To'xtab Qolmaslik</h4>
        <p style="font-size:12px;" data-ru="Движется ли тарелка непрерывно 30 секунд без сбоев и остановок?" data-en="Does the UFO orbit continuously for 30 seconds without freezing?">Qahramon kamida 30 soniya to'xtamasdan uzluksiz aylanyaptimi?</p>
      </div>
      <div class="box" style="border-top:3px solid var(--purple);">
        <div class="tag" style="color:var(--purple);">3. Chegara Himoyasi</div>
        <h4 data-ru="Не Улетает Ли?" data-en="Screen Guard">Ekrandan Chiqmaslik</h4>
        <p style="font-size:12px;" data-ru="При приближении к краю космоса спрей отталкивается или пропадает?" data-en="Does the sprite bounce off borders or vanish outside the screen?">Chekkaga yetganda chiroyli qaytyaptimi yoki ekrandan yo'qolib ketyaptimi?</p>
      </div>
      <div class="box" style="border-top:3px solid var(--amber);">
        <div class="tag" style="color:var(--amber);">4. Chiroy va Orbita</div>
        <h4 data-ru="Костюмы и Огонь" data-en="Visual Polish">Kostyum va Olov</h4>
        <p style="font-size:12px;" data-ru="Меняются ли костюмы пламени и вращается ли тарелка красиво?" data-en="Do thrusters pulse and does the UFO look awesome in motion?">Dvigatel olovi miltillab, dumaloq orbita chiroyli chiqqanmi?</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: SHOWCASE ARENA -->
  <section class="slide" data-phase="Taqdimot|Демонстрация|Showcase Arena" data-time="74:00–77:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="БОЛЬШОЙ ЭКРАН" data-en="BIG SCREEN SHOWCASE">SMARTBOARDDA O'QUVCHILAR DEMOSI</span></div>
    <h2 data-ru="Парад Космических Анимаций на Большом Экране" data-en="Space Animation Parade on Smartboard">Katta Ekranda Jonli Kosmik Paradi</h2>
    <div class="grid-2">
      <div class="box">
        <h3 data-ru="3 Лучших Проекта Класса" data-en="Top 3 Class Projects">Sinfning Eng Zo'r 3 Ta Loyihasi</h3>
        <p style="font-size:13px;" data-ru="Учитель выводит на смартборд проекты учеников с самыми плавными орбитами и эффектами." data-en="Teacher features the smoothest orbital animations and visual effects on the main Smartboard.">O'qituvchi doskaga eng chiroyli orbitali va miltillovchi koinot loyihalarini chiqaradi.</p>
        <div style="background:var(--surface-2); padding:10px; border-radius:8px; font-size:12px; line-height:1.6;">
          ⭐ <strong>Eng Silliq Orbita:</strong> Qahramon mukammal ellips yoki doira bo'ylab uchadi.<br>
          ⭐ <strong>Eng Chiroyli Animatsiya:</strong> Dvigatel alangalari silliq miltillaydi.<br>
          ⭐ <strong>Super-Tezlik:</strong> Chekkadan to'qnashmasdan chaqqon qaytadi.
        </div>
      </div>
      <div class="box" style="display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
        <div style="font-size:48px; margin-bottom:10px;">🏆 🚀 🥇</div>
        <h4 style="margin:4px 0; color:var(--amber);" data-ru="Звездный Инженер Недели" data-en="Star Space Engineer">Haftaning Yulduz Muhandisi</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Проект попадает в зал славы Target International School!" data-en="Featured in Target International School student Hall of Fame!">Loyiha maktabimizning o'quvchilar ko'rgazmasiga qo'yiladi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: TIERED HOMEWORK -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Tiered Homework" data-time="77:00–79:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="SUMMARY & HOMEWORK">10 BALLIK 3 DARAJALI UY VAZIFASI</span></div>
    <h2 data-ru="3 Уровня Домашнего Задания: Космический Патруль" data-en="3-Tiered Homework Mission: Cosmic Patrol">3 Darajali Uy Vazifasi: Kosmik Patrul</h2>
    <div class="grid-3" style="gap:10px;">
      <div class="box" style="border-top:3px solid var(--green);">
        <div class="tag" style="color:var(--green);">1-Daraja: Baza (4 ball)</div>
        <h4 data-ru="Вечный Патруль" data-en="Endless Patrol">Doimiy Patrul</h4>
        <p style="font-size:12px;" data-ru="Создайте спрей, который бесконечно бегает слева направо с отскоком от краев и сменяет костюм." data-en="Create a sprite moving endlessly left-to-right bouncing off edges with costume changes.">Chapdan o'ngga to'xtovsiz yugurib, devordan qaytuvchi va kostyumini almashtiruvchi mushuk loyihasini quring.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--accent);">
        <div class="tag" style="color:var(--accent);">2-Daraja: Loyiha (4 ball)</div>
        <h4 data-ru="Круговая Орбита" data-en="Circular Orbit">Koinot Orbitasi</h4>
        <p style="font-size:12px;" data-ru="Запрограммируйте летающую тарелку на плавную круговую орбиту с помощью поворота на 5 градусов." data-en="Program a flying UFO into a smooth circular orbit via 5-degree increments.">5 gradus burilish orqali dumaloq orbita bo'ylab uchuvchi va dumi miltillovchi uchar likopcha yarating.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--purple);">
        <div class="tag" style="color:var(--purple);">3-Daraja: Challenge (2 ball)</div>
        <h4 data-ru="Две Планеты" data-en="Two Planets">Ikki Sayyora Tizimi</h4>
        <p style="font-size:12px;" data-ru="Добавьте второй спрей (Землю или Луну), который вращается вокруг первого с другой скоростью!" data-en="Add a secondary sprite orbiting around the central body at a distinct rotational speed!">Birinchi sayyora atrofida boshqa tezlikda aylanuvchi ikkinchi yo'ldosh (Oy) spraytini qo'shing!</p>
      </div>
    </div>
    <div style="margin-top:12px; text-align:right;">
      <a href="vazifa.html" class="btn" style="background:var(--purple); color:#fff; font-size:12px;" data-ru="Открыть ДЗ" data-en="Open HW">Vazifalar Ilovasini Ochish ➔</a>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ УРОКА" data-en="LESSON SUMMARY">XULOSA VA KEYINGI DARS</span></div>
    <h2 data-ru="Циклы — Двигатель Всех Компьютерных Игр" data-en="Loops: The Engine of All Video Games">Sikllar — Barcha Kompyuter O'yinlarining Yuragi</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Сегодня мы научились управлять бесконечным движением без лишних строк кода." data-en="Today we mastered infinite motion without writing hundreds of redundant blocks.">Bugun biz bir nechta keraksiz bloklar o'rniga bitta aqlli sikl bilan cheksiz harakat yaratishni o'rgandik.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Forever (Doimiy):</strong> О'yindagi barcha harakatlanuvchi jismlar uchun asosiy dvigatel." data-en="<strong>Forever Loop:</strong> The core game loop powering all active entities."><strong>Forever (Doimiy):</strong> O'yindagi hamma jonli qahramonlarning asosiy dvigateli.</li>
          <li data-ru="<strong>Bounce (Qaytish):</strong> Qahramonni ekrandan chiqib ketishdan asrovchi kiber-qalqon." data-en="<strong>Bounce Guard:</strong> Prevents sprites from flying outside screen boundaries."><strong>Bounce (Qaytish):</strong> Qahramonni ekrandan chiqib ketishdan asrovchi himoya.</li>
          <li data-ru="<strong>Wait (Kutish):</strong> Animatsiyani miltillashdan asrab, Disney darajasidagi silliqlik beruvchi vosita." data-en="<strong>Micro-Pause:</strong> Delivers Disney-grade smooth animation fluidity."><strong>Wait (Kutish):</strong> Animatsiyani Disney darajasida silliq qiluvchi vosita.</li>
        </ul>
      </div>
      <div class="box" style="border-left:4px solid var(--purple); background:rgba(147,51,234,0.08);">
        <strong style="color:var(--purple); font-size:14px;" data-ru="Следующий Урок:" data-en="Next Lesson:">🚀 Keyingi Dars Ko'prigi:</strong>
        <p style="font-size:12px; margin-top:6px; line-height:1.5;" data-ru="<strong>Умные Условия: «Если... То» (If... Then)!</strong> Как заставить персонажа реагировать на препятствия, собирать кристаллы и останавливаться перед красным светом!" data-en="<strong>Smart Conditions: 'If... Then'!</strong> Teaching sprites to detect obstacles, collect crystals, and brake at red lights!"><strong>Aqlli Shartlar: "Agar... U Holda" (If... Then)!</strong> Qahramon to'siqlarni qanday payqaydi, kristallarni qanday yig'adi va qizil chiroqda qanday to'xtaydi!</p>
      </div>
    </div>
  </section>
"""

# In-deck JS for Slide 8 interactive UFO canvas
IN_DECK_JS = """
// --- IN-DECK UFO LOOP SIMULATOR ---
var deckUfoX = 200;
var deckUfoY = 120;
var deckUfoAngle = 0;
var deckUfoSpeed = 4;
var deckUfoTurn = 4;
var deckUfoBounce = true;
var deckUfoLoopRunning = false;
var deckUfoSteps = 0;
var deckUfoTimer = null;

function deckDrawUfo() {
  var canvas = document.getElementById('deckUfoCanvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Background stars
  ctx.fillStyle = 'rgba(255,255,255,0.4)';
  var starSeed = [ [30, 40], [80, 180], [150, 70], [220, 200], [310, 50], [350, 160], [120, 220], [270, 90] ];
  starSeed.forEach(function(pt) {
    ctx.fillRect(pt[0], pt[1], 2, 2);
  });

  // Central Planet
  ctx.fillStyle = '#6366f1';
  ctx.beginPath();
  ctx.arc(200, 120, 24, 0, Math.PI * 2);
  ctx.fill();
  ctx.strokeStyle = '#818cf8';
  ctx.lineWidth = 3;
  ctx.stroke();

  // Draw UFO
  ctx.save();
  ctx.translate(deckUfoX, deckUfoY);
  ctx.rotate((deckUfoAngle * Math.PI) / 180);

  // Thruster flame
  if (deckUfoLoopRunning) {
    ctx.fillStyle = Math.random() < 0.5 ? '#f59e0b' : '#ef4444';
    ctx.beginPath();
    ctx.moveTo(-12, 0);
    ctx.lineTo(-24, -4);
    ctx.lineTo(-24, 4);
    ctx.closePath();
    ctx.fill();
  }

  // UFO Dome
  ctx.fillStyle = '#38bdf8';
  ctx.beginPath();
  ctx.arc(0, -3, 8, Math.PI, 0);
  ctx.fill();

  // UFO Saucer Body
  ctx.fillStyle = '#10b981';
  ctx.beginPath();
  ctx.ellipse(0, 2, 18, 6, 0, 0, Math.PI * 2);
  ctx.fill();
  ctx.strokeStyle = '#059669';
  ctx.lineWidth = 1.5;
  ctx.stroke();

  // Lights
  ctx.fillStyle = '#fbbf24';
  ctx.fillRect(-10, 1, 3, 2);
  ctx.fillRect(-2, 1, 3, 2);
  ctx.fillRect(6, 1, 3, 2);

  ctx.restore();
}

function deckStepUfo() {
  deckUfoAngle = (deckUfoAngle + deckUfoTurn) % 360;
  var rad = (deckUfoAngle * Math.PI) / 180;
  var nx = deckUfoX + Math.cos(rad) * deckUfoSpeed;
  var ny = deckUfoY + Math.sin(rad) * deckUfoSpeed;

  var canvas = document.getElementById('deckUfoCanvas');
  if (canvas) {
    if (deckUfoBounce) {
      if (nx < 20 || nx > canvas.width - 20) {
        deckUfoAngle = 180 - deckUfoAngle;
        nx = Math.max(20, Math.min(canvas.width - 20, nx));
      }
      if (ny < 20 || ny > canvas.height - 20) {
        deckUfoAngle = -deckUfoAngle;
        ny = Math.max(20, Math.min(canvas.height - 20, ny));
      }
    } else {
      if (nx < 0) nx = canvas.width;
      if (nx > canvas.width) nx = 0;
      if (ny < 0) ny = canvas.height;
      if (ny > canvas.height) ny = 0;
    }
  }

  deckUfoX = nx;
  deckUfoY = ny;
  deckUfoSteps++;
  var stepsEl = document.getElementById('deckStepCount');
  if (stepsEl) stepsEl.textContent = deckUfoSteps;
  deckDrawUfo();
}

function deckToggleLoop() {
  var btn = document.getElementById('btnDeckLoop');
  var status = document.getElementById('deckLoopStatus');
  if (deckUfoLoopRunning) {
    clearInterval(deckUfoTimer);
    deckUfoTimer = null;
    deckUfoLoopRunning = false;
    btn.textContent = '▶️ Siklni Boshlash';
    btn.style.background = 'var(--green)';
    status.textContent = 'Status: To‘xtatildi';
    status.style.color = 'var(--ink-2)';
  } else {
    deckUfoLoopRunning = true;
    deckUfoTimer = setInterval(deckStepUfo, 30);
    btn.textContent = '⏸️ Siklni To‘xtatish';
    btn.style.background = 'var(--red)';
    status.textContent = 'Status: Cheksiz Harakatda';
    status.style.color = 'var(--green)';
  }
}

function deckToggleBounce() {
  deckUfoBounce = !deckUfoBounce;
  var btn = document.getElementById('btnDeckBounce');
  if (deckUfoBounce) {
    btn.textContent = '🛡️ Qaytish: YOQILGAN';
    btn.style.background = 'var(--accent)';
  } else {
    btn.textContent = '🛡️ Qaytish: O‘CHIRILGAN';
    btn.style.background = '#64748b';
  }
}

function deckResetUFO() {
  if (deckUfoTimer) {
    clearInterval(deckUfoTimer);
    deckUfoTimer = null;
  }
  deckUfoLoopRunning = false;
  deckUfoX = 200;
  deckUfoY = 120;
  deckUfoAngle = 0;
  deckUfoSteps = 0;
  var btn = document.getElementById('btnDeckLoop');
  if (btn) {
    btn.textContent = '▶️ Siklni Boshlash';
    btn.style.background = 'var(--green)';
  }
  var status = document.getElementById('deckLoopStatus');
  if (status) {
    status.textContent = 'Status: Tayyor';
    status.style.color = 'var(--green)';
  }
  var stepsEl = document.getElementById('deckStepCount');
  if (stepsEl) stepsEl.textContent = '0';
  deckDrawUfo();
}

setTimeout(deckDrawUfo, 400);

function checkQuiz(btn, isCorrect, feedbackText) {
  var parent = btn.closest('.box');
  var allBtns = parent.querySelectorAll('.quiz-btn');
  allBtns.forEach(function(b) {
    b.disabled = true;
    b.style.opacity = '0.6';
  });
  btn.style.opacity = '1';
  var fb = parent.querySelector('.quiz-feedback');
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

# Notes array for 14 slides
NOTES_DATA = {
    "uz": [
        ["Kirish va Maqsad", "O'quvchilarga bugungi dars mavzusi: Scratch sikllari va cheksiz harakat haqida so'zlab bering.", "Doskaga bir xil bloklarni 100 marta terish o'rniga bitta sikl qo'yish afzalligini ko'rsating."],
        ["Uy Vazifasi Tahlili", "26-darsdagi miltillash xatosini tushuntiring. Nega 0.1 soniya kutish shart ekanini ayting.", "Oltin yechimni ko'rsatib, Disney animatsiyasi kabi silliq yurish siri aynan shu ekanini ta'kidlang."],
        ["Sikllar Nega Kerak?", "Hayotiy misol: quyoshning har kuni chiqishi, soat milining aylanishi — bularning hammasi tabiiy sikllar.", "Scratch-da o'yinlar aynan shu sikllar tufayli to'xtab qolmasligini ayting."],
        ["Ikki Xil Sikl", "Forever va Repeat 10 bloklarining shaklidagi farqni ko'rsating.", "Nega Forever tagiga boshqa blok ulab bo'lmasligini bolalardan so'rang."],
        ["Chekkaga Yetganda Qaytish", "Qahramon ekrandan chiqib ketmasligi uchun 'agar chekkaga yetsa, qaytish' blokini ko'rsating.", "Boshi bilan pastga aylanib qolmaslik uchun [chap-o'ng] aylanish uslubini o'rgating."],
        ["Kosmik Orbita", "Qadam tashlash va 5 gradus burilish qanday qilib dumaloq aylanma orbitani hosil qilishini tushuntiring.", "Uchar likopcha orbitasini doskada chizib bering."],
        ["Animatsiya va Ovoz", "Sikl ichiga harakat, kadr almashishi va kosmik audio qo'yish tartibini ko'rsating.", "Bloklar yuqoridan pastga navbatma-navbat bajarilishini ta'kidlang."],
        ["Smartboard Simulyatori", "Taqdimot ichidagi simulyatorda siklni yoqing.", "Qaytish tugmasini o'chirib/yoqib, uchar likopchaning traektoriyasini ko'rsating."],
        ["Bilimni Sinash (Quiz)", "3 ta savol bo'yicha tezkor blitz o'tkazing.", "Har bir to'g'ri va noto'g'ri javobni quvnoq ohangda tahlil qiling."],
        ["25 Daqiqalik Arena", "O'quvchilarga Scratch 3.0 yoki playground/index.html ni ochishni buyuring.", "Har bir o'quvchi o'z uchar likopchasini koinotda uchirishini nazorat qiling."],
        ["Partadosh Bilan Audit", "O'quvchilar partadoshi bilan o'rnini almashtirib, loyihani 4 ta mezon bo'yicha tekshirishsin.", "Boshqalarning loyihasidan o'rganishni rag'batlantiring."],
        ["Katta Ekran Showcasi", "Eng chiroyli 3 ta koinot loyihasini doskada butun sinfga ko'rsating.", "O'quvchilarni olqishlang."],
        ["3 Darajali Uy Vazifasi", "10 ballik uy vazifasi shartlarini tushuntiring.", "2-darajadagi koinot orbitasi loyihasiga e'tibor qarating."],
        ["Xulosa va Keyingi Dars", "Darsni yakunlang va keyingi darsda 'Agar... U Holda' shartli bloklarini o'rganishimizni e'lon qiling!", "Doskaga keyingi dars shart bloklarini chizib, o'quvchilarni rag'batlantiring."]
    ],
    "ru": [
        ["Введение и Цель", "Представьте тему: циклы в Scratch и создание бесконечного движения.", "Покажите на доске замену сотен однотипных блоков одним компактным циклом."],
        ["Разбор Домашнего Задания", "Объясните ошибку сверхбыстрого мигания костюмов из-за отсутствия паузы в 0.1 сек.", "Покажите золотой стандарт плавной мультипликационной походки."],
        ["Зачем Нужны Циклы?", "Приведите жизненные примеры циклов: восход солнца, тиканье часов, дыхание.", "Объясните, что без циклов любая игра мгновенно замирает."],
        ["Два Типа Циклов", "Покажите визуальную разницу между блоками «повторять всегда» и «повторить 10 раз».", "Спросите у ребят, почему у блока «всегда» нет нижнего паза."],
        ["Отскок от Краев", "Покажите блок «если касается края, оттолкнуться».", "Объясните стиль вращения [влево-вправо], чтобы кот не переворачивался вверх тормашками."],
        ["Космическая Орбита", "Покажите, как шаг вперед и поворот на 5 градусов образуют идеальную круговую траекторию.", "Нарисуйте орбиту НЛО на доске."],
        ["Анимация и Звук", "Соберите комплексный блок: движение + следующий костюм + отскок + звук.", "Подчеркните последовательное выполнение команд."],
        ["Интерактив на Доске", "Запустите встроенный в слайд симулятор полета тарелки.", "Продемонстрируйте включение и выключение отскока от границ."],
        ["Тест (Квиз)", "Проведите веселое тестирование из 3 вопросов.", "Разберите ошибки вместе с классом."],
        ["Практическая Арена (25 мин)", "Дайте команду открыть Scratch 3.0 или playground/index.html.", "Курируйте создание летающей тарелки каждым учеником."],
        ["Взаимный Аудит", "Организуйте обмен местами за партами по чек-листу из 4 пунктов.", "Поощряйте взаимопомощь и поиск багов."],
        ["Шоукейс на Доске", "Выведите 3 лучших космических проекта на интерактивную доску.", "Похвалите авторов."],
        ["Домашнее Задание", "Объясните 3 уровня 10-балльного домашнего задания.", "Обратите внимание на круговую орбиту 2-го уровня."],
        ["Итоги и Анонс", "Подведите итоги урока и анонсируйте следующую тему: умные условия «Если... То»!", "Выставите итоговые оценки за космические проекты на доске."]
    ],
    "en": [
        ["Intro & Objectives", "Introduce Scratch loops and continuous sprite animation.", "Contrast stacking 100 identical blocks with a single clean loop."],
        ["Homework Review", "Explain hyper-speed blinking caused by omitting a 0.1s delay between costume changes.", "Present the golden solution for fluid cartoon motion."],
        ["Why Do We Need Loops?", "Relate loops to real-life cycles: ticking clocks, planetary rotations, heartbeats.", "Explain that loops form the heart of every active video game."],
        ["Two Types of Loops", "Contrast 'forever' vs 'repeat 10' blocks visually.", "Prompt students on why the forever block lacks a bottom connector notch."],
        ["Boundary Bounce", "Introduce 'if on edge, bounce' to prevent off-screen sprite loss.", "Demonstrate setting rotation style to [left-right] to avoid upside-down flipping."],
        ["Cosmic Orbit", "Show how combining steps forward with slight degree turns crafts smooth orbital motion.", "Sketch orbital curves on the board."],
        ["Animation & Audio", "Assemble a 4-action loop: motion + next costume + bounce guard + thruster audio.", "Reinforce sequential top-to-bottom block execution."],
        ["In-Deck Live Demo", "Activate the in-deck UFO simulator on the Smartboard.", "Toggle boundary bounce on and off to observe trajectory shifts."],
        ["Knowledge Check (Quiz)", "Lead students through the 3 quick questions.", "Discuss each answer cheerfully."],
        ["Hands-on Arena (25 min)", "Instruct students to open Scratch 3.0 or playground/index.html.", "Guide each student in programming their space animation."],
        ["Peer Review", "Facilitate seat swapping to review code using the 4-point audit rubric.", "Encourage positive constructive feedback."],
        ["Showcase Arena", "Project the 3 most impressive cosmic projects onto the main Smartboard.", "Celebrate student achievements."],
        ["Tiered Homework", "Explain the 3-tiered 10-point homework assignment.", "Highlight Tier 2's circular orbit requirement."],
        ["Summary & Next Class", "Summarize core concepts and preview smart 'If... Then' condition blocks!", "Display final mission scores on the Smartboard."]
    ]
}

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "27-dars: Takrorlanishlar Sehri: Cheksiz Harakat va Sikllar"
    title_ru = "Урок 27: Магия Повторений: Бесконечное Движение и Циклы"
    title_en = "Lesson 27: Magic of Loops: Endless Motion & Repeat Blocks"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="5–6 КЛАСС" data-en="GRADE 5–6">5–6-SINF</span>',
                 tpl)

    titles_json = json.dumps({"uz": title_uz, "ru": title_ru, "en": title_en}, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    stage_regex = r'<div class="stage">[\s\S]*?</div><!-- /stage -->'
    new_stage = f'<div class="stage">\n{SLIDES_HTML}\n  </div><!-- /stage -->'
    tpl = re.sub(stage_regex, new_stage, tpl)

    tpl = tpl.replace("</script>\n</body>", f"\n{IN_DECK_JS}\n</script>\n</body>")

    out_path = os.path.join(DEST_DIR, "prezentatsiya.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

# -----------------------------------------------------------------------------
# 2. WORKSHEET (varaqa.html)
# -----------------------------------------------------------------------------
def build_worksheet():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("{{COHORT_LABEL}}", "5–6-sinf")
    tpl = tpl.replace("{{WEEK_NUM}}", "11")
    tpl = tpl.replace("{{LESSON_NUM}}", "27")
    tpl = tpl.replace("{{TRACK_UZ}}", "Junior Creators & Kiber-Gigiyena Track")
    tpl = tpl.replace("{{TRACK_RU}}", "Junior Creators & Кибер-Гигиена")
    tpl = tpl.replace("{{TRACK_EN}}", "Junior Creators & Cyber Hygiene Track")
    tpl = tpl.replace("{{LESSON_TITLE_UZ}}", "Takrorlanishlar Sehri: Cheksiz Harakat va Sikllar (Loops)")
    tpl = tpl.replace("{{LESSON_TITLE_RU}}", "Магия Повторений: Бесконечное Движение и Циклы в Scratch")
    tpl = tpl.replace("{{LESSON_TITLE_EN}}", "Magic of Loops: Endless Motion & Repeat Blocks in Scratch")

    sec1_html = """
    <p style="font-size:12px; line-height:1.5; margin-bottom:8px;" data-ru="В компьютерных играх персонажи и враги двигаются непрерывно. Вместо сотен одинаковых команд программисты используют циклы. В Scratch есть бесконечный цикл «повторять всегда» и счетный цикл «повторить 10 раз»." data-en="In video games, characters and enemies move continuously. Instead of hundreds of duplicate commands, engineers use loops. Scratch provides the infinite 'forever' loop and the counted 'repeat 10' block.">Kompyuter o'yinlarida qahramonlar va dushmanlar to'xtovsiz harakatlanadi. Yuzlab bir xil buyruqlarni qo'lda terish o'rniga dasturchilar sikllardan foydalanadilar. Scratch-da cheksiz "doimiy takrorlash" (forever) va sanovchi "10 marta takrorlash" bloklari mavjud.</p>
    <div style="background:var(--surface-2); padding:6px 10px; border-radius:6px; font-size:11px; font-family:var(--font-mono); border-left:3px solid var(--accent);">
      <strong>Asosiy Standart:</strong> Doimiy Takrorlash (Forever) + Qadam (Move) + Chekkadan Qaytish (Bounce) + Aylanish Uslubi (Left-Right) + 0.1s Kutish (Wait).
    </div>
    """

    sec2_html = """
    <pre style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; font-family:var(--font-mono); line-height:1.4; border:1px solid var(--hair);"><code>// Kosmik Orbita Skripti
qachonki [yashil bayroqcha] bosilganda:
  aylanish uslubini [chap-o'ng] ga sozla;
  doimiy takrorlash {
    8 qadam yur;
    keyingi kostyum;
    agar chekkaga yetsa, qaytish;
    0.1 soniya kut;
  }</code></pre>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Scratch Блоки" data-en="Scratch Block">Scratch Bloki</th>
            <th style="padding:4px 6px;" data-ru="Категория" data-en="Category">Kategoriyasi</th>
            <th style="padding:4px 6px;" data-ru="Что Делает в Проекте" data-en="Action">Vazifasi</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="повторять всегда" data-en="forever"><code>doimiy takrorlash</code></td>
            <td style="padding:4px 6px;" data-ru="Управление (Control)" data-en="Control">Boshqaruv (Control)</td>
            <td style="padding:4px 6px;" data-ru="Бесконечно выполняет вложенные блоки" data-en="Executes nested blocks endlessly">Ichidagi bloklarni to'xtovsiz aylantiradi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="повторить 10 раз" data-en="repeat 10"><code>10 marta takrorlash</code></td>
            <td style="padding:4px 6px;" data-ru="Управление (Control)" data-en="Control">Boshqaruv (Control)</td>
            <td style="padding:4px 6px;" data-ru="Выполняет действие ровно N раз и завершается" data-en="Runs exactly N times and stops">Amalni N marta bajarib, to'xtaydi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="если касается края, оттолкнуться" data-en="if on edge, bounce"><code>agar chekkaga yetsa, qaytish</code></td>
            <td style="padding:4px 6px;" data-ru="Движение (Motion)" data-en="Motion">Harakat (Motion)</td>
            <td style="padding:4px 6px;" data-ru="Не дает спрею вылететь за границы экрана" data-en="Keeps sprite inside boundary">Qahramonni ekrandan chiqib ketishdan asraydi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="стиль вращения [влево-вправо]" data-en="set rotation style [left-right]"><code>aylanish uslubi [chap-o'ng]</code></td>
            <td style="padding:4px 6px;" data-ru="Движение (Motion)" data-en="Motion">Harakat (Motion)</td>
            <td style="padding:4px 6px;" data-ru="Предотвращает переворот вверх тормашками" data-en="Prevents upside-down flipping">Boshi pastga teskari aylanib qolishini oldini oladi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    sec4_html = """
    <p style="font-size:12px; margin-bottom:6px;" data-ru="Соберите космическую орбиту в симуляторе. Запишите, при каком угле поворота тарелка делает идеальный ровный круг:" data-en="Assemble an orbit in the simulator. Record the rotation angle producing a perfect circle:">Simulyatorda kosmik orbitani quring. Uchar likopcha chiroyli doira yasashi uchun burilish burchagi necha gradus bo'lishi kerakligini yozing:</p>
    <div style="border:1px dashed var(--hair); border-radius:6px; height:80px; padding:8px; font-family:var(--font-mono); font-size:11px; color:var(--ink-2);" data-ru="[Угол поворота, количество шагов и имя космического корабля]" data-en="[Rotation angle, step count, and spaceship name]">
      // Uchar likopcha burilish burchagi: ____________ gradus<br>
      // 1 soniyada bosib o'tilgan qadamlar soni: ____________ ta<br>
      // Qaytish bloki bo'lmasa qahramon qayerga ketib qoladi? ____________
    </div>
    """

    rubric_html = """
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px; font-size:11px;">
      <div style="border-left:3px solid var(--green); padding-left:6px;">
        <strong style="color:var(--green);" data-ru="4 Балла: База" data-en="4 Pts: Base">4 Ball: Baza</strong>
        <p style="margin:2px 0;" data-ru="Блок «повторять всегда» заставляет спрей непрерывно ходить." data-en="Forever loop keeps sprite moving continuously.">Doimiy takrorlash bloki qahramonni to'xtovsiz harakatlantiradi.</p>
      </div>
      <div style="border-left:3px solid var(--accent); padding-left:6px;">
        <strong style="color:var(--accent);" data-ru="4 Балла: Проект" data-en="4 Pts: Project">4 Ball: Loyiha</strong>
        <p style="margin:2px 0;" data-ru="Отскок от краев работает, персонаж не переворачивается вверх тормашками." data-en="Edge bounce works cleanly without upside-down flipping.">Chekkadan qaytish va [chap-o'ng] aylanish uslubi to'g'ri sozlangan.</p>
      </div>
      <div style="border-left:3px solid var(--purple); padding-left:6px;">
        <strong style="color:var(--purple);" data-ru="2 Балла: Challenge" data-en="2 Pts: Challenge">2 Ball: Challenge</strong>
        <p style="margin:2px 0;" data-ru="Плавная круговая космическая орбита и анимация двигателей спрея." data-en="Smooth circular cosmic orbit with engine thruster animation.">Dumaloq orbita va dvigatel alangasi animatsiyasi yaratilgan.</p>
      </div>
    </div>
    """

    tpl = tpl.replace("{{SEC1_CONTENT}}", sec1_html)
    tpl = tpl.replace("{{SEC2_CONTENT}}", sec2_html)
    tpl = tpl.replace("{{SEC3_CONTENT}}", sec3_html)
    tpl = tpl.replace("{{SEC4_CONTENT}}", sec4_html)
    tpl = tpl.replace("{{RUBRIC_CONTENT}}", rubric_html)

    out_path = os.path.join(DEST_DIR, "varaqa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: varaqa.html")

# -----------------------------------------------------------------------------
# 3. INTERACTIVE HOMEWORK (vazifa.html)
# -----------------------------------------------------------------------------
def build_homework():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("{{COHORT_LABEL}}", "5–6-sinf")
    tpl = tpl.replace("{{WEEK_NUM}}", "11")
    tpl = tpl.replace("{{LESSON_NUM}}", "27")
    tpl = tpl.replace("{{TRACK_UZ}}", "Junior Creators & Kiber-Gigiyena Track")
    tpl = tpl.replace("{{TRACK_RU}}", "Junior Creators & Кибер-Гигиена")
    tpl = tpl.replace("{{TRACK_EN}}", "Junior Creators & Cyber Hygiene Track")
    tpl = tpl.replace("{{LESSON_TITLE_UZ}}", "Takrorlanishlar Sehri: Cheksiz Harakat va Sikllar (Loops)")
    tpl = tpl.replace("{{LESSON_TITLE_RU}}", "Магия Повторений: Бесконечное Движение и Циклы в Scratch")
    tpl = tpl.replace("{{LESSON_TITLE_EN}}", "Magic of Loops: Endless Motion & Repeat Blocks in Scratch")
    tpl = tpl.replace("{{TOTAL_TASKS}}", "3")

    tasks_html = """
  <!-- 1-DARAJA: BAZA -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-1" data-ru="1-Уровень: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Вечный Патруль: Ходьба с Отскоком" data-en="Endless Patrol: Walk with Bounce">Doimiy Patrul: Chekkadan Qaytuvchi Mushuk</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Напишите алгоритм для Scratch, который заставляет кота бесконечно шагать по 10 шагов, отталкиваться от края экрана и менять костюм каждые 0.1 секунды без переворачивания вверх ногами." data-en="Describe the Scratch algorithm making the cat walk endlessly by 10 steps, bounce off edges cleanly, and alternate costumes every 0.1s without flipping upside-down.">Mushukni to'xtamasdan 10 qadamdan yurgizuvchi, ekrandan chiqib ketmasdan qaytaruvchi va boshi bilan teskari aylanmasligi uchun [chap-o'ng] uslubini qo'llovchi Scratch bloklari tartibini yozing.</p>
    <textarea class="answer-area" id="ans_task_1" rows="7" placeholder="Scratch bloklari ketma-ketligini yozing..." data-placeholder-ru="Напишите последовательность блоков здесь..." data-placeholder-en="Write block sequence here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_1">
      <strong style="color:var(--green);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>1. qachonki [yashil bayroqcha] bosilganda
2. aylanish uslubini [chap-o'ng] ga sozla
3. doimiy takrorlash {
     10 qadam yur
     keyingi kostyum
     agar chekkaga yetsa, qaytish
     0.1 soniya kut
   }</code></pre>
    </div>
  </div>

  <!-- 2-DARAJA: AMALIYOT -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-2" data-ru="2-Уровень: Проект (4 балла)" data-en="Tier 2: Project (4 pts)">2-Daraja: Amaliyot (4 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Космическая Орбита Летающей Тарелки" data-en="Cosmic Orbit of the Flying UFO">Uchar Likopchaning Aylanma Orbitasi</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Опишите, как с помощью шагов и поворота на определенный угол заставить летающую тарелку летать по плавной круговой орбите вокруг центра экрана." data-en="Describe how combining forward motion with slight rotational degree shifts commands a UFO into an orbital path around center screen.">Qanday qilib oldinga qadam tashlash va ma'lum burchakka burilish orqali uchar likopchani koinot markazi bo'ylab doira shaklida uchirish mumkinligini tushuntiring va bloklarini yozing.</p>
    <textarea class="answer-area" id="ans_task_2" rows="8" placeholder="Orbita bloklarini bu yerga yozing..." data-placeholder-ru="Напишите код орбиты здесь..." data-placeholder-en="Write orbit code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_2">
      <strong style="color:var(--accent);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>qachonki [yashil bayroqcha] bosilganda:
  x: 0, y: 100 nuqtasiga o't
  doimiy takrorlash {
    6 qadam yur
    5 gradus o'ngga buril
    agar chekkaga yetsa, qaytish
    0.05 soniya kut
  }</code></pre>
    </div>
  </div>

  <!-- 3-DARAJA: CHALLENGE -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-3" data-ru="3-Уровень: Challenge (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Двойная Орбита: Планета и Спутник" data-en="Dual Orbit: Planet & Satellite">Ikki Sayyora Tizimi: Sayyora va Yo'ldosh</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Как запрограммировать два независимых спрея (например, Солнце в центре и Земля на орбите), чтобы один стоял на месте и вращался вокруг своей оси, а второй быстро наматывал круги вокруг него?" data-en="How to program two independent sprites (Sun and Earth) such that the Sun spins in-place while Earth orbits around it continuously?">Qanday qilib ikkita mustaqil sprayt (markazda Quyosh va atrofida Yer) yasash mumkin: Quyosh o'z o'qi atrofida aylanadi, Yer esa uning atrofida cheksiz yuguradi?</p>
    <textarea class="answer-area" id="ans_task_3" rows="8" placeholder="Ikki sprayt kodini bu yerga yozing..." data-placeholder-ru="Напишите код для двух спреев здесь..." data-placeholder-en="Write dual-sprite code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_3">
      <strong style="color:var(--purple);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>// 1-Sprayt (Quyosh):
qachonki [yashil bayroqcha] bosilganda:
  x: 0, y: 0 ga o't
  doimiy takrorlash {
    2 gradus o'ngga buril
  }

// 2-Sprayt (Yer):
qachonki [yashil bayroqcha] bosilganda:
  x: 0, y: 120 ga o't
  doimiy takrorlash {
    8 qadam yur
    6 gradus o'ngga buril
  }</code></pre>
    </div>
  </div>
    """

    tpl = tpl.replace("{{TASKS_CONTENT}}", tasks_html)
    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

# -----------------------------------------------------------------------------
# 4. TEACHER READING GUIDE (TEACHER_READING.md)
# -----------------------------------------------------------------------------
def build_teacher_reading():
    content = """# 5–6-sinf, 11-hafta, 27-dars: O'qituvchi Qo'llanmasi
## Takrorlanishlar Sehri: Cheksiz Harakat va Sikllar (Loops)

### Dars Haqida Ma'lumot:
- **Kohorta:** 5–6-sinf (Junior Creators & Kiber-Gigiyena Track)
- **Format:** 80 daqiqalik Juftlik Dars (Double Block, 2 bosqichli)
- **Asosiy maqsad:** O'quvchilarga Scratch-da sikllar (forever, repeat N) tushunchasini o'rgatish, to'xtovsiz harakatlantirish, "agar chekkaga yetsa, qaytish" xavfsizlik bloki va [chap-o'ng] aylanish uslubi orqali qahramonning silliq yurishini ta'minlash.

---

### 80 Daqiqalik Dars Pacing Xaritasi:

#### 1-BOSQICH (40 daqiqa): Nazariya, Xatolar Tahlili va Jonli Test
| Vaqt | Bosqich | Slayd | O'qituvchi Harakati | Kutiladigan Natija |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Maqsad | 1 | Dars mavzusini e'lon qilish, uchar likopchaning cheksiz parvozi maqsadi. | Bolalarda qiziqish uyg'onadi. |
| **04:00–12:00** | O'tgan Dars HW Tahlili | 2 | 26-darsdagi miltillash xatosini ko'rsatish: 0.1s kutishsiz kostyumlar chalkashib ketishi. Blitz savol. | Nega kutish bloki kerakligi o'zlashtiriladi. |
| **12:00–18:00** | Sikllar Falsafasi | 3 | Nega 50 ta blok o'rniga 1 ta sikl kerakligini hayotiy misol bilan aytish. | Kodni qisqartirish tushuniladi. |
| **18:00–24:00** | Forever vs Repeat 10 | 4 | Doimiy takrorlash va sanovchi sikllar farqini tushuntirish. | Sikl turlari ajratiladi. |
| **24:00–30:00** | Chekkadan Qaytish | 5 | "Agar chekkaga yetsa, qaytish" va [chap-o'ng] uslubini doskada ko'rsatish. | Qahramon ekrandan yo'qolmaydi. |
| **30:00–35:00** | Kosmik Orbita | 6 | Qadam + gradusga burilish orqali dumaloq orbita yasash formulasini aytish. | Doiraviy harakat mantig'i o'rganiladi. |
| **35:00–40:00** | Animatsiya va Ovoz | 7 | Sikl ichiga kadrlar va audio qo'shish tartibi. | Mega-blok tushunchasi shakllanadi. |

#### 2-BOSQICH (40 daqiqa): Amaliy Kiber-Arena va Taqdimot
| Vaqt | Bosqich | Slayd | O'qituvchi Harakati | Kutiladigan Natija |
|---|---|:---:|---|---|
| **40:00–48:00** | Smartboard Sinovi | 8 | Slayd ichidagi simulyatorda uchar likopchani harakatlantirib ko'rsatish. | Vizual tajriba ortadi. |
| **48:00–54:00** | 3-Savolli Quiz | 9 | Butun sinf bilan 3 ta savol bo'yicha interaktiv test o'tkazish. | Bilimlar mustahkamlanadi. |
| **54:00–69:00** | 25 Daqiqalik Arena | 10 | Bolalarga `playground/index.html` da uchar likopcha orbitasini qurishni topshirish. | Har bir o'quvchi ishchi animatsiya yaratadi. |
| **69:00–74:00** | Partadosh Auditi | 11 | O'rin almashib, 4 ta mezon bo'yicha loyihani sinash. | Do'stona ko'rik va tahlil. |
| **74:00–77:00** | Katta Ekran Showcasi | 12 | Eng chiroyli 3 ta loyihani doskaga chiqarish. | O'quvchilarda g'urur va ishonch. |
| **77:00–79:00** | Uy Vazifasi | 13 | 10 ballik 3 darajali vazifani tushuntirish. | Vazifa tushuniladi. |
| **79:00–80:00** | Xulosa va Keyingi Dars | 14 | Darsni sarhisob qilish va 'Agar... U Holda' mavzusiga ko'prik. | 80 daqiqa to'liq yakunlanadi. |

---

### Keng Tarqalgan Savollar va Maslahatlar:
1. **"Nega uchar likopcha aylanmay to'g'riga uchib ketyapti?"**
   - Javob: Chunki siz sikl ichiga "o'ngga 5 gradus burilish" blokini qo'ymagansiz! Har qadamda ozgina burilmasa, u faqat to'g'ri chiziq bo'ylab borib qaytadi.
2. **"Nega uchar likopcha ekranning pastiga tushib qotib qoldi?"**
   - Javob: Siz "agar chekkaga yetsa, qaytish" blokini qo'yishni unutdingiz. U ekrandan tashqariga chiqib ketgan. Qaytish blokini qo'shing!
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Created: TEACHER_READING.md")

# -----------------------------------------------------------------------------
# 5. STANDALONE PLAYGROUND (playground/index.html)
# -----------------------------------------------------------------------------
def build_playground():
    play_html = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title data-ru="Scratch Космическая Орбита — 5–6 Класс" data-en="Scratch Cosmic Orbit Studio — Grade 5–6">Scratch Kosmik Orbita Maydonchasi — 5–6-Sinf</title>
  <link rel="stylesheet" href="../../../../assets/brand.css" />
  <style>
    :root {
      --bg: #070a14;
      --surface: #101626;
      --surface-2: #1b2438;
      --hair: #2e3b52;
      --ink: #f8fafc;
      --ink-2: #94a3b8;
      --accent: #3b82f6;
      --green: #10b981;
      --red: #ef4444;
      --amber: #f59e0b;
      --purple: #8b5cf6;
      --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
    }
    body {
      margin: 0;
      padding: 20px;
      background: var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    .header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--hair);
    }
    .btn {
      padding: 8px 16px;
      border-radius: 6px;
      border: 1px solid var(--hair);
      background: var(--surface-2);
      color: var(--ink);
      cursor: pointer;
      font-weight: 600;
      font-size: 13px;
      transition: all 0.15s ease;
    }
    .btn:hover { filter: brightness(1.1); }
    .btn-green { background: var(--green); color: #fff; border-color: var(--green); }
    .btn-accent { background: var(--accent); color: #fff; border-color: var(--accent); }
    .grid {
      display: grid;
      grid-template-columns: 480px 1fr;
      gap: 20px;
    }
    canvas {
      background: #030712;
      border-radius: 12px;
      border: 2px solid var(--hair);
    }
    .control-card {
      background: var(--surface);
      border: 1px solid var(--hair);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .param-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .param-group label {
      font-size: 12px;
      color: var(--ink-2);
      font-weight: 600;
    }
    .param-group input[type=range] {
      width: 100%;
    }
    .lang-btn {
      padding: 4px 10px;
      border-radius: 6px;
      background: transparent;
      border: 1px solid var(--hair);
      color: var(--ink-2);
      font-size: 12px;
      cursor: pointer;
    }
    .lang-btn.active {
      background: var(--accent);
      color: #fff;
      border-color: var(--accent);
    }
  </style>
</head>
<body>

  <div class="header-bar">
    <div>
      <h2 style="margin:0 0 4px 0;" data-ru="Scratch Космическая Орбита: Симулятор Циклов" data-en="Scratch Cosmic Orbit: Loop Simulator">Scratch Kosmik Orbita: Sikllar Simulyatori</h2>
      <span style="font-size:12px; color:var(--ink-2);" data-ru="5–6-Класс · 11-Неделя · 27-Урок · Блоки «повторять всегда», шаг, отскок и орбита" data-en="Grade 5–6 · Week 11 · Lesson 27 · Forever loops, steps, bouncing & orbital physics">5–6-Sinf · 11-Hafta · 27-Dars · Doimiy takrorlash, qadam, qaytish va dumaloq orbita</span>
    </div>
    <div style="display:flex; gap:10px; align-items:center;">
      <div style="display:flex; gap:4px;">
        <button class="lang-btn active" onclick="setLang('uz')">UZ</button>
        <button class="lang-btn" onclick="setLang('ru')">RU</button>
        <button class="lang-btn" onclick="setLang('en')">EN</button>
      </div>
    </div>
  </div>

  <div style="margin-bottom:16px; display:flex; gap:10px; align-items:center;">
    <button class="btn btn-green" id="btnPlayLoop" onclick="togglePlayLoop()" data-ru="▶️ Запустить Сикл (Зеленый Флаг)" data-en="▶️ Start Loop (Green Flag)">▶️ Siklni Boshlash (Yashil Bayroq)</button>
    <button class="btn btn-accent" id="btnPlayBounce" onclick="togglePlayBounce()" data-ru="🛡️ Отскок от Края: ВКЛ" data-en="🛡️ Boundary Bounce: ON">🛡️ Chekkadan Qaytish: YOQILGAN</button>
    <button class="btn" onclick="resetPlayground()" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta O'rnatish</button>
    <span style="font-size:12px; color:var(--ink-2); margin-left:auto; font-family:var(--font-mono);">
      Qadamlar: <strong style="color:var(--green);" id="playSteps">0</strong> | Tezlik: <strong style="color:var(--amber);" id="playSpeedVal">5 px</strong>
    </span>
  </div>

  <div class="grid">
    <canvas id="playCanvas" width="480" height="360"></canvas>

    <div class="control-card">
      <h3 style="margin:0;" data-ru="Параметры Цикла в Scratch" data-en="Scratch Loop Parameters">Scratch Sikl Parametrlari</h3>

      <div class="param-group">
        <label data-ru="Скорость Движения (Шагов за Кадр):" data-en="Motion Speed (Steps per Frame):">Harakat Tezligi (Qadamlar Soni):</label>
        <input type="range" id="rngSpeed" min="1" max="15" value="5" oninput="updateParams()" />
      </div>

      <div class="param-group">
        <label data-ru="Угол Поворота (Градусов):" data-en="Turn Angle (Degrees):">Burilish Burchagi (Graduslar):</label>
        <input type="range" id="rngTurn" min="0" max="15" value="4" oninput="updateParams()" />
        <span style="font-size:11px; color:var(--ink-2); font-family:var(--font-mono);" id="lblTurn">Burilish: 4° (Aylanma Orbita)</span>
      </div>

      <div class="param-group">
        <label data-ru="Второй Спутник (Луна):" data-en="Second Satellite (Moon):">Ikkinchi Yo'ldosh (Oy):</label>
        <button class="btn" id="btnToggleMoon" onclick="toggleMoon()" data-ru="🌙 Добавить Спутник" data-en="🌙 Add Satellite">🌙 Ikkinchi Yo'ldoshni Qo'shish</button>
      </div>

      <div style="margin-top:auto; background:var(--surface-2); padding:10px; border-radius:8px; font-size:12px; line-height:1.6; color:var(--ink-2);">
        <strong style="color:var(--accent);" data-ru="Совет по Анимации:" data-en="Animation Tip:">💡 O'qituvchi Maslahati:</strong><br>
        <span data-ru="Если угол поворота равен 0°, тарелка летит по прямой линии как мячик для пинг-понга. Если угол 4° или 5°, получается идеальная круговая орбита вокруг планеты!" data-en="If turn angle is 0°, the UFO flies strictly straight. If turn is 4° or 5°, it crafts a marvelous orbit around the planet!">Agar burilish 0° bo'lsa, likopcha ping-pong to'pidek to'g'ri chiziqda yuradi. Agar burilish 4° yoki 5° bo'lsa, sayyora atrofida ajoyib dumaloq orbita hosil bo'ladi!</span>
      </div>
    </div>
  </div>

  <script>
    var currentLang = 'uz';
    var canvas = document.getElementById('playCanvas');
    var ctx = canvas.getContext('2d');

    var ufoX = 240;
    var ufoY = 180;
    var ufoAngle = 0;
    var ufoSpeed = 5;
    var ufoTurn = 4;
    var ufoBounce = true;
    var hasMoon = false;
    var moonAngle = 0;
    var loopRunning = false;
    var steps = 0;
    var timer = null;

    function setLang(lang) {
      currentLang = lang;
      document.querySelectorAll('.lang-btn').forEach(function(b) {
        b.classList.toggle('active', b.textContent.toLowerCase() === lang);
      });
      document.querySelectorAll('[data-' + lang + ']').forEach(function(el) {
        el.textContent = el.getAttribute('data-' + lang);
      });
    }

    function updateParams() {
      ufoSpeed = parseInt(document.getElementById('rngSpeed').value, 10);
      ufoTurn = parseInt(document.getElementById('rngTurn').value, 10);
      document.getElementById('playSpeedVal').textContent = ufoSpeed + ' px';
      document.getElementById('lblTurn').textContent = 'Burilish: ' + ufoTurn + '° ' + (ufoTurn === 0 ? '(To‘g‘ri Chiziq)' : '(Aylanma Orbita)');
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Starfield
      ctx.fillStyle = 'rgba(255,255,255,0.3)';
      var stars = [ [40,50],[120,80],[200,40],[320,70],[420,120],[80,240],[180,300],[300,260],[390,310],[440,210] ];
      stars.forEach(function(s) { ctx.fillRect(s[0], s[1], 2, 2); });

      // Central Planet
      ctx.fillStyle = '#4f46e5';
      ctx.beginPath();
      ctx.arc(240, 180, 32, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#818cf8';
      ctx.lineWidth = 4;
      ctx.stroke();

      // Second satellite (Moon)
      if (hasMoon) {
        moonAngle = (moonAngle + 3) % 360;
        var mRad = (moonAngle * Math.PI) / 180;
        var mx = 240 + Math.cos(mRad) * 75;
        var my = 180 + Math.sin(mRad) * 75;
        ctx.fillStyle = '#cbd5e1';
        ctx.beginPath();
        ctx.arc(mx, my, 8, 0, Math.PI * 2);
        ctx.fill();
      }

      // UFO
      ctx.save();
      ctx.translate(ufoX, ufoY);
      ctx.rotate((ufoAngle * Math.PI) / 180);

      // Thruster
      if (loopRunning) {
        ctx.fillStyle = Math.random() < 0.5 ? '#f59e0b' : '#ef4444';
        ctx.beginPath();
        ctx.moveTo(-16, 0);
        ctx.lineTo(-30, -5);
        ctx.lineTo(-30, 5);
        ctx.closePath();
        ctx.fill();
      }

      // Dome
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath();
      ctx.arc(0, -4, 10, Math.PI, 0);
      ctx.fill();

      // Body
      ctx.fillStyle = '#10b981';
      ctx.beginPath();
      ctx.ellipse(0, 3, 24, 8, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#047857';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Lights
      ctx.fillStyle = '#fde047';
      ctx.fillRect(-14, 2, 4, 3);
      ctx.fillRect(-3, 2, 4, 3);
      ctx.fillRect(8, 2, 4, 3);

      ctx.restore();
    }

    function step() {
      ufoAngle = (ufoAngle + ufoTurn) % 360;
      var rad = (ufoAngle * Math.PI) / 180;
      var nx = ufoX + Math.cos(rad) * ufoSpeed;
      var ny = ufoY + Math.sin(rad) * ufoSpeed;

      if (ufoBounce) {
        if (nx < 25 || nx > canvas.width - 25) {
          ufoAngle = 180 - ufoAngle;
          nx = Math.max(25, Math.min(canvas.width - 25, nx));
        }
        if (ny < 25 || ny > canvas.height - 25) {
          ufoAngle = -ufoAngle;
          ny = Math.max(25, Math.min(canvas.height - 25, ny));
        }
      } else {
        if (nx < 0) nx = canvas.width;
        if (nx > canvas.width) nx = 0;
        if (ny < 0) ny = canvas.height;
        if (ny > canvas.height) ny = 0;
      }

      ufoX = nx;
      ufoY = ny;
      steps++;
      document.getElementById('playSteps').textContent = steps;
      draw();
    }

    function togglePlayLoop() {
      var btn = document.getElementById('btnPlayLoop');
      if (loopRunning) {
        clearInterval(timer);
        timer = null;
        loopRunning = false;
        btn.textContent = '▶️ Siklni Boshlash (Yashil Bayroq)';
        btn.style.background = 'var(--green)';
      } else {
        loopRunning = true;
        timer = setInterval(step, 30);
        btn.textContent = '⏸️ Siklni To‘xtatish';
        btn.style.background = 'var(--red)';
      }
    }

    function togglePlayBounce() {
      ufoBounce = !ufoBounce;
      var btn = document.getElementById('btnPlayBounce');
      if (ufoBounce) {
        btn.textContent = '🛡️ Chekkadan Qaytish: YOQILGAN';
        btn.style.background = 'var(--accent)';
      } else {
        btn.textContent = '🛡️ Chekkadan Qaytish: O‘CHIRILGAN';
        btn.style.background = '#64748b';
      }
    }

    function toggleMoon() {
      hasMoon = !hasMoon;
      var btn = document.getElementById('btnToggleMoon');
      btn.textContent = hasMoon ? '🌙 Oyni O‘chirish' : '🌙 Ikkinchi Yo‘ldoshni Qo‘shish';
      draw();
    }

    function resetPlayground() {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
      loopRunning = false;
      ufoX = 240;
      ufoY = 180;
      ufoAngle = 0;
      steps = 0;
      document.getElementById('btnPlayLoop').textContent = '▶️ Siklni Boshlash (Yashil Bayroq)';
      document.getElementById('btnPlayLoop').style.background = 'var(--green)';
      document.getElementById('playSteps').textContent = '0';
      draw();
    }

    draw();
  </script>
</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "playground", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(play_html)
    print("  ✓ Created: playground/index.html")

def main():
    print("📦 Building 5–6-sinf (Lesson 27: Takrorlanishlar va Sikllar)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_playground()
    print("🎉 Done! Generated Grade 5–6 Lesson 27.")

if __name__ == "__main__":
    main()
