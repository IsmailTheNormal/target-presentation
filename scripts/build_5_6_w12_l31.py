#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_5_6_w12_l31.py — Builder for 5–6th Grade, Week 12, Lesson 31

Mavzu: Xabarlar va Hodisalar (Broadcast Messages): Qahramonlar Muloqoti va Sehrli Kalit
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 5-6-sinf (Junior Creators & Kiber-Gigiyena Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "5-6-sinf", "12-hafta", "31-dars-broadcast-xabarlar-va-sehrli-kalit")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "playground"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides — Scratch Events & Broadcast Messaging)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide is-on" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="5–6-КЛАСС · 12-Я НЕДЕЛЯ · УРОК 31" data-en="GRADES 5–6 · WEEK 12 · LESSON 31">5–6-SINF · 12-HAFTA · 31-DARS</span></div>
    <h1 class="display" data-ru="События и Сообщения (Broadcast): Диалог Героев и Волшебный Ключ" data-en="Events & Broadcast Messaging: Sprite Dialogue & The Magic Key">Xabarlar va Hodisalar: Qahramonlar Muloqoti va Sehrli Kalit</h1>
    <p class="lede" data-ru="Связываем персонажей игры в единую команду: как передавать радиосигналы между спрайтами (Broadcast), открывать запертые ворота при подборе золотого ключа и управлять победой через глобальные сообщения 'GameOver' и 'Victory'!" data-en="Connecting sprites into a synchronized game team: broadcasting radio signals between sprites, unlocking castle gates when picking up the magic key, and orchestrating scenes via 'GameOver' and 'Victory' events!">O'yin qahramonlarini yagona jamoaga aylantiramiz: spraytlar o'rtasida radiosignallar (Broadcast) yuborish, sehrli kalit olinganda darvozani ochish va 'GameOver' hamda 'Victory' xabarlari orqali butun o'yinni boshqarish!</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Радиоволны Спрайтов" data-en="Sprite Radio">Xabar Tarqatish (Broadcast)</h3>
        <p data-ru="Один спрайт кричит в рупор 'Ключ найден!', а замок и дракон мгновенно реагируют." data-en="One sprite broadcasts 'Key Found!' and the castle gate and dragon react immediately.">Bitta sprayt 'Kalit olindi!' deb xabar beradi, qulflangan darvoza va ajdarho esa darhol eshitib harakatga tushadi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Magic Castle Quest</div>
        <h3 data-ru="Квест с Воротами" data-en="Castle Gate Quest">Sehrli Qasr Sarguzashti</h3>
        <p data-ru="Интерактивный квест: поиск золотого ключа, открытие потайной двери и переход на экран победы." data-en="Playable adventure quest: finding the golden key, unlocking hidden gates, and triggering the victory scene.">O'ynaladigan sarguzasht: oltin kalitni topish, sehrli darvozani ochish va g'alaba sahnasiga o'tish.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Tahlil|Разбор|Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 30-УРОКА" data-en="LESSON 30 HOMEWORK REVIEW">30-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Разбор Ошибок: Бесконечное Добавление Очков и Сброс Жизней" data-en="Reviewing Pitfalls: Infinite Coin Glitch & HP Reset">O'tgan Dars Tahlili: Cheksiz Tangalar va Jonlar Nollanmasligi</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Типичная Ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Тангага теgib turganda ball cheksiz oshaveradi" data-en="Coin Touching Infinite Score Bug">Tangaga tekkanda ball to'xtovsiz oshib ketishi</h3>
        <p data-ru="Если в условии 'если касается игрока' забыть спрятать монету ('спрятаться') или подождать ('ждать 0.1 сек'), цикл добавляет +10 очков 60 раз в секунду!" data-en="If you omit 'hide' or 'wait 0.1s' inside 'touching player', the loop adds +10 points 60 times every second!">Agar 'agar qahramonga tegsa' blokida tangani yashirmasangiz ('hide') yoki kutish bermasangiz, sikl har soniyada 60 marta +10 ball qo'shib, hisobni buzib yuboradi!</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#ef4444;">// XATO: Tanga yo'qolmaydi, ball 10000 ga chiqib ketadi</span>
agar &lt;qahramonga tegsa&gt; u holda
  o'zgaruvchi [Ballar] ni (10) ga o'zgartir
<span style="color:#64748b;">// Yechim: tangani darhol 'yashirish' shart!</span>
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Золотой Стандарт" data-en="Golden Standard">Oltin Standart (Best Practice)</div>
        <h3 data-ru="Сбор Монеты + Скрытие + Звук" data-en="Clean Coin Pickup Logic">Olingan Tangani Yashirish va Ovoz</h3>
        <p data-ru="Правильный алгоритм: при касании сразу проигрывается звук 'Coin', переменная увеличивается на 10 и спрайт монеты прячется командой 'спрятаться'." data-en="Ideal pattern: immediately play 'Coin' chime, bump Score by 10, and invoke 'hide' so the coin disappears.">Mukammal algoritm: tekkanda darhol 'Coin' ovozi chalinadi, ball 10 ga oshiriladi va tanga 'yashirinish' buyrug'i bilan ko'rinmas bo'ladi.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#22c55e;">// TO'G'RI: Toza yig'ish mantig'i</span>
agar &lt;qahramonga tegsa&gt; u holda
  [Coin v] ovozini chal
  o'zgaruvchi [Ballar] ni (10) ga o'zgartir
  <span style="color:#22c55e;">yashirinish (hide)</span>
        </div>
      </div>
    </div>
    <div class="grid-2" style="margin-top:14px;">
      <div class="box">
        <span class="badge" data-ru="Блиц-вопрос (30 сек)" data-en="Blitz Question (30s)">Blitz Savol</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="Как сделать так, чтобы при старте новой игры спрятанная монета снова появилась?" data-en="How do you make sure the hidden coin reappears whenever a new game starts?">Yangi o'yin boshlanganda (yashil bayroqcha bosilganda) yashiringan tanga yana ko'rinishi uchun nima qilish kerak?</p>
      </div>
      <div class="box">
        <span class="badge" data-ru="Мост к теме" data-en="Bridge to Today">Bugungi Mavzuga Ko'prik</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="А что если ключ находится в одном углу, а ворота — в другом? Как ворота узнают, что игрок взял ключ? Через СООБЩЕНИЯ (Broadcast)!" data-en="What if the key is on one side and the gate is far away? How does the gate know the key was taken? Via BROADCAST MESSAGES!">Agar kalit ekranning bir chetida, ulkan darvoza esa narigi chetida bo'lsa, darvoza qahramon kalitni olganini qayerdan biladi? XABARLAR (Broadcast) orqali!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: WHAT IS BROADCAST -->
  <section class="slide" data-phase="Konsept|Концепт|Concept" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ПОНЯТИЕ BROADCAST · РАДИОВОЛНЫ SCRATCH" data-en="BROADCAST CONCEPT · SCRATCH RADIO SIGNALS">BROADCAST NIMA? · SPRAYTLAR RADIOMULOQOTI</span></div>
    <h2 data-ru="Что такое Broadcast: Рация для Персонажей" data-en="What is Broadcast: Walkie-Talkie for Sprites">Broadcast Nima? Spraytlar Uchun Maxfiy Ratsiya</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Проблема" data-en="The Problem">Mustaqil Qahramonlar</div>
        <h3 data-ru="Спрайты живут отдельно" data-en="Sprites Live Separately">Har Biri O'z Olamida</h3>
        <p data-ru="Каждый персонаж видит только свои блоки. Кот не знает, что делает Рыцарь, а Замок не знает, взял ли игрок Ключ." data-en="Each sprite only executes its own scripts. The Cat cannot directly inspect the Knight's coordinates.">Har bir sprayt faqat o'z skriptini biladi. Darvoza qahramonning qayerda yurganini yoki kalit olinganini to'g'ridan-to'g'ri ko'ra olmaydi.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Решение" data-en="The Solution">Xabar Yuborish</div>
        <h3 data-ru="Глобальный Радиосигнал" data-en="Global Radio Wave">Umumiy Efirga Xabar</h3>
        <p data-ru="Блок 'передать [сообщение]' кричит в громкоговоритель на всю игру. Все персонажи, настроенные на эту волну, мгновенно просыпаются!" data-en="The 'broadcast [message]' block shouts across the whole scene. All listening sprites trigger their scripts.">'xabarni tarqatish' bloki butun o'yinga signal tarqatadi. Shu xabarni kutib turgan barcha spraytlar bir vaqtda ishga tushadi!</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(234,179,8,0.15); color:var(--warning);" data-ru="Результат" data-en="The Result">Sinxron Harakat</div>
        <h3 data-ru="Командная Работа" data-en="Team Synchronization">Jamoaviy O'yin</h3>
        <p data-ru="Kalit olinganda darvoza ochiladi, ajdarho qochadi, musiqa o'zgaradi va ekranda yangi xona paydo bo'ladi!" data-en="When key is touched: gate opens, dragon roars, music shifts, and next room unlocks!">Kalit olinganda darvoza ochiladi, fon musiqasi tantanali bo'ladi va ekranda yangi xona ochiladi!</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px;">
      <strong data-ru="Аналогия из реальной жизни:" data-en="Real-world Analogy:">Maktabdagi oddiy misol:</strong>
      <p style="font-size:12px; margin-top:4px;" data-ru="Когда звенит школьный звонок, директору не нужно заходить в каждый класс и говорить «Перемена!». Звук звонка — это один сигнал BROADCAST, который слышат все!" data-en="When the school bell rings, the principal doesn't visit every room saying 'Recess!'. The bell sound is a single BROADCAST heard by all classes!">Qo'ng'iroq chalinganda har bir xonaga kirib chiqish shart emas. Qo'ng'iroq — bu barcha sinflar bir vaqtda eshitadigan va tanaffusga chiqadigan BROADCAST signalidir!</p>
    </div>
  </section>

  <!-- SLIDE 4: THE TWO CORE BLOCKS -->
  <section class="slide" data-phase="Standart|Стандарт|Standard" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="БЛОКИ СОБЫТИЙ · ЖЕЛТЫЙ РАЗДЕЛ" data-en="EVENT BLOCKS · YELLOW CATEGORY">HODISALAR BLOKLARI · SARIQ BO'LIM</span></div>
    <h2 data-ru="Два Главных Блока: 'Передать' и 'Когда я получу'" data-en="Two Core Blocks: 'Broadcast' & 'When I Receive'">Ikkita Asosiy Blok: "Xabar Tarqatish" va "Xabar Olganda..."</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Отправитель (Sender)" data-en="Sender Sprite">Yuboruvchi Sprayt (Sender)</div>
        <h3 data-ru="Блок: 'передать [xabar]'" data-en="Block: 'broadcast [xabar]'">[xabarni tarqatish] bloki</h3>
        <p data-ru="Используется тем персонажем, который совершил действие (например, Ключ, которого коснулись):" data-en="Used by the trigger sprite (e.g. the Golden Key when touched by hero):">Biror muhim hodisa sodir bo'lganda (masalan, qahramon kalitga tekkanida) signalni havoga tarqatadi:</p>
        <div class="code-block" style="margin-top:10px; font-size:12px;">
<span style="color:#eab308;">// Kalit spraytida:</span>
agar &lt;qahramonga tegsa&gt; u holda
  [Chime v] ovozini chal
  <span style="color:#3b82f6; font-weight:700;">[DarvozaOchildi v] xabarini tarqatish</span>
  yashirinish
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Получатель (Receiver)" data-en="Receiver Sprite">Qabul Qiluvchi Sprayt (Receiver)</div>
        <h3 data-ru="Блок: 'когда я получу [xabar]'" data-en="Block: 'when I receive [xabar]'">[men ... xabarini olganda] shlyuzi</h3>
        <p data-ru="Этот блок стоит в начале скрипта тех персонажей, которые должны среагировать (например, Ворота):" data-en="Placed at the top of scripts for reacting sprites (e.g. Castle Gate):">Ushbu blok buyruq kutib turgan boshqa spraytlar boshiga qo'yiladi (masalan, Darvoza):</p>
        <div class="code-block" style="margin-top:10px; font-size:12px;">
<span style="color:#eab308;">// Qulflangan Darvoza spraytida:</span>
<span style="color:#22c55e; font-weight:700;">men [DarvozaOchildi v] xabarini olganda</span>
  keyingi libosga (ochiq eshik) o't
  1 soniya kut
  yashirinish <span style="color:#64748b;">// Yo'l ochildi!</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: QUEST ARCHITECTURE -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="АРХИТЕКТУРА КВЕСТА · СХЕМА СВЯЗЕЙ" data-en="QUEST ARCHITECTURE · SIGNAL FLOW">KVEST ARXITEKTURASI · SIGNALLAR OQIMI</span></div>
    <h2 data-ru="Схема Игры: Как Сигналы Связывают Спрайты" data-en="Signal Flow: Connecting Game Sprites Together">Signallar Oqimi: 4 Spraytning Yagona Zanjiri</h2>
    <div class="card" style="padding:16px;">
      <div class="code-block" style="font-size:12px; line-height:1.7;">
[ Qahramon (Player) ] ──(Tegish)──► [ Oltin Kalit (Key) ]
                                            │
                                            ▼ (Signal Tarqatadi)
                             BROADCAST: "DARVOZA_OCHILDI"
                                            │
                 ┌──────────────────────────┴──────────────────────────┐
                 ▼                                                     ▼
      [ Sehrli Darvoza (Gate) ]                             [ Fon Musiqasi (Audio) ]
      - Ochiq eshik libosiga o'tadi                         - G'alaba ohangini chaladi
      - 1 soniyadan so'ng g'oyib bo'ladi                    - Qorong'i tuman yo'qoladi
      </div>
      <p style="font-size:12px; margin-top:10px; color:var(--ink-secondary);" data-ru="Обратите внимание: один сигнал 'DARVOZA_OCHILDI' одновременно активирует ДВА спрайта! Это главная сила Broadcast." data-en="Notice: a single 'DARVOZA_OCHILDI' broadcast triggers TWO independent sprites simultaneously! This is the core superpower of Broadcast.">E'tibor bering: bitta "DARVOZA_OCHILDI" xabari bir vaqtning o'zida IKKITA spraytni (Darvoza va Musiqani) harakatga keltirdi!</p>
    </div>
  </section>

  <!-- SLIDE 6: THE INFINITE BROADCAST LOOP PITFALL -->
  <section class="slide" data-phase="Tuzoq|Ловушка|Pitfall" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ОПАСНАЯ ЛОВУШКА · БЕСКОНЕЧНЫЙ ЦИКЛ" data-en="CRITICAL TRAP · INFINITE BROADCAST LOOP">XAVFLI TUZOQ · CHEKSIZ XABARLAR SIKLI</span></div>
    <h2 data-ru="Осторожно: Бесконечный Спам Сообщениями (Игра Зависает!)" data-en="Watch Out: Infinite Broadcast Spam (Game Freezes!)">Ehtiyot Bo'ling: Cheksiz Xabar Qopqoni va O'yin Qotishi</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Опасный Код" data-en="Broken Code">Qotib Qoluvchi Skript</div>
        <h3 data-ru="Broadcast внутри цикла 'всегда'" data-en="Broadcast Inside Forever Loop">'doim takrorlash' ichidagi Broadcast</h3>
        <p data-ru="Если поместить 'передать сообщение' внутри вечного цикла без задержки, игра будет посылать 60 сигналов в секунду! Скрипт получателя будет перезапускаться с 1-й строки и зависнет." data-en="If you drop a broadcast into a forever loop with no wait delay, it fires 60 times/sec! The receiving script resets constantly and stutters.">Agar 'xabar tarqatish' blokini kutishsiz 'doim takrorlash' ichiga qo'ysangiz, soniyasiga 60 marta signal yuboriladi! Qabul qiluvchi sprayt har soniya qayta boshlanib, qotib qoladi.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#ef4444;">// XATO: 1 soniyada 60 marta baqirish!</span>
doim takrorlash
  <span style="color:#ef4444;">[Signal v] xabarini tarqatish</span>
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Безопасное Решение" data-en="Safe Pattern">Xavfsiz Qoida: Bir Martalik Signal</div>
        <h3 data-ru="Спрятать или остановить" data-en="Hide or Stop This Script">Xabar Yuborib To'xtatish</h3>
        <p data-ru="Сигнал должен отправляться ровно 1 раз! После отправки спрайт либо прячется ('спрятаться'), либо останавливает этот скрипт ('стоп этот скрипт')." data-en="A broadcast must fire exactly ONCE! Follow it up with 'hide' or 'stop this script' to prevent spam.">Xabar roppa-rosa 1 marta yuborilishi shart! Yuborilgach, sprayt yo 'yashirinish' qilishi yoki 'ushbu skriptni to'xtatish' buyrug'ini berishi kerak.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#22c55e;">// TO'G'RI: 1 marta yuboriladi va to'xtaydi</span>
agar &lt;qahramonga tegsa&gt; u holda
  [Signal v] xabarini tarqatish
  <span style="color:#22c55e;">yashirinish</span>
  <span style="color:#22c55e;">ushbu skriptni to'xtatish</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: BROADCAST AND WAIT -->
  <section class="slide" data-phase="Muhandislik|Инженерия|Engineering" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ДИАЛОГ ГЕРОЕВ · ОЧЕРЕДЬ РЕПЛИК" data-en="SPRITE DIALOGUE · SEQUENTIAL CHAT">QAHRAMONLAR DIALOGI · NAVBATMA-NAVBAT GAPLASHISH</span></div>
    <h2 data-ru="Диалог: 'Передать и ждать' (Broadcast and Wait)" data-en="Ordered Dialogue: 'Broadcast and Wait'">Tartibli Suhbat: "Xabarni Tarqatish va Kutish"</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Проблема одновременного крика" data-en="Simultaneous Speaking Chaos">Bir Vaqtda Gapirish Chalkashligi</h3>
        <p data-ru="Если два персонажа просто скажут 'Привет!', их облачка текста перекроют друг друга. Чтобы получился связный диалог, первый должен подождать ответа второго!" data-en="If two sprites trigger speech blocks at once, bubbles overlap. For natural conversation, speaker 1 must await speaker 2's line!">Agar ikkala qahramon bir vaqtda "Salom!" desa, pufakchalar bir-birini to'sib qo'yadi. Jonli suhbat hosil bo'lishi uchun 1-qahramon 2-qahramonning javobini kutishi kerak!</p>
        <div class="box" style="margin-top:12px;">
          <strong data-ru="Блок 'передать и ждать':" data-en="'Broadcast and wait' block:">[xabarni tarqatish va kutish]:</strong>
          <p style="font-size:12px; margin-top:4px;" data-ru="Персонаж отправляет сигнал и замирает, пока ВСЕ получатели не закончат свои действия. Только потом он продолжает свой скрипт." data-en="Sprite dispatches message and pauses until all receivers finish their routines. Only then does it proceed.">Sprayt xabarni yuboradi va barcha qabul qiluvchilar o'z harakatini tugatmaguncha kutib turadi. So'ng o'z skriptini davom ettiradi.</p>
        </div>
      </div>
      <div class="card">
        <div class="code-block" style="font-size:11px; line-height:1.6;">
<span style="color:#eab308;">// 1-Sprayt (Sehrgar Bobo):</span>
[Salom yosh ritsar! v] 2 soniya ayt
<span style="color:#3b82f6; font-weight:700;">[RitsargaSavol v] xabarini tarqatish va kutish</span>
[Barakalla, yo'l ochildi! v] 2 soniya ayt

<span style="color:#22c55e;">// 2-Sprayt (Ritsar):</span>
<span style="color:#22c55e;">men [RitsargaSavol v] xabarini olganda</span>
  [Men sehrli kalitni topdim! v] 2 soniya ayt
  <span style="color:#64748b;">// Ritsar gapirib bo'lgach, Bobo davom etadi!</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: GAME STATES (START, GAMEOVER, VICTORY) -->
  <section class="slide" data-phase="Boshqaruv|Состояния|States" data-time="40:00–45:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="СОСТОЯНИЯ ИГРЫ · ГЛОБАЛЬНЫЙ КОНТРОЛЬ" data-en="GAME STATES · GLOBAL ORCHESTRATION">O'YIN HOLATLARI · GLOBAL BOSHQARUV</span></div>
    <h2 data-ru="Три Главных Сигнала Любой Игры: Start, GameOver, Win" data-en="Three Master Game Signals: Start, GameOver, Win">Har Qanday O'yinning 3 Ta Bosh Signali</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="1. Старт Игры" data-en="1. Start Game">Boshlash Signali</div>
        <h3 data-ru="Сигнал 'START'" data-en="'START' Event">'OyinBoshlandi'</h3>
        <p data-ru="Все спрайты выходят на исходные позиции: жизни = 3, очки = 0, монеты показываются, ворота закрываются." data-en="All sprites reset: HP = 3, Score = 0, coins appear, gates lock shut.">Barcha spraytlar boshlang'ich nuqtaga qaytadi: Jonlar = 3, Ballar = 0, kalit ko'rinadi, darvoza qulflanadi.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="2. Поражение" data-en="2. Defeat">Mag'lubiyat</div>
        <h3 data-ru="Сигнал 'GAME OVER'" data-en="'GAME OVER' Event">'GameOver'</h3>
        <p data-ru="Когда Jonlar = 0, посылается сигнал: фон становится черным, монстры замирают, появляется надпись 'Yutqazdingiz'." data-en="When HP = 0: scene dims, enemies freeze, 'Game Over' banner emerges.">Jonlar 0 bo'lganda yuboriladi: fon qorayadi, dushmanlar qotib qoladi, 'Yutqazdingiz' yozuvi chiqadi.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="3. Победа" data-en="3. Victory">Buyuk G'alaba</div>
        <h3 data-ru="Сигнал 'VICTORY'" data-en="'VICTORY' Event">'Galaba'</h3>
        <p data-ru="Герой прошел сквозь ворота: гремят фейерверки, играет победная музыка, начисляется золотой кубок!" data-en="Hero passes gate: fireworks launch, victory fanfare plays, trophy awards.">Qahramon darvozadan o'tganda: mushaklar otiladi, bayramona musiqa chalinadi, oltin kubok taqdim etiladi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: INTERACTIVE BLITZ QUIZ -->
  <section class="slide" data-phase="Viktorina|Викторина|Quiz" data-time="45:00–50:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="БЛИЦ-ПРОВЕРКА ЗНАНИЙ · 4 ВОПРОСА" data-en="KNOWLEDGE CHECK · 4 BLITZ QUESTIONS">BLITZ KIBER-TEST · 4 TA TEZKOR SAVOL</span></div>
    <h2 data-ru="Интерактивный Квиз: Проверь Свою Радиосвязь" data-en="Interactive Quiz: Test Your Radio Logic">Interaktiv Quiz: Radiomuloqotni Sinash</h2>
    <div class="grid-2">
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:var(--accent); color:#fff;">1</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Сколько спрайтов одновременно могут поймать ОДНО сообщение?" data-en="How many sprites can receive ONE broadcast simultaneously?">Bitta xabarni bir vaqtda nechta sprayt qabul qila oladi?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) Только один | B) Ровно два | C) Сколько угодно (хоть 100)" data-en="A) Only one | B) Exactly two | C) As many as listening (even 100)">A) Faqat bitta | B) Faqat ikkita | C) Nechta xohlasa (hatto 100 ta ham)</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: C (Все спрайты с блоком 'когда я получу')" data-en="Answer: C (All sprites having matching 'when I receive')">Javob: C (Shu xabar blokiga ega barcha spraytlar bir vaqtda)</div>
      </div>
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:#a855f7; color:#fff;">2</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Что произойдет, если отправить Broadcast внутри бесконечного цикла?" data-en="What happens if you broadcast repeatedly in a forever loop?">Cheksiz sikl ichida xabar tarqatilsa nima bo'ladi?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) Игра ускорится | B) Игра зависнет и скрипты будут сбиваться | C) Ничего" data-en="A) Speed up | B) Game freezes & scripts stutter | C) Nothing">A) Tezlashadi | B) O'yin qotadi va skriptlar chalg'iydi | C) Hech narsa</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: B (Скрипты получателей будут постоянно перезапускаться)" data-en="Answer: B (Receiving scripts constantly reset)">Javob: B (Qabul qiluvchi spraytlar doim boshidan qayta boshlanib qotadi)</div>
      </div>
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:var(--warning); color:#fff;">3</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Чем отличается 'передать и ждать' от обычного 'передать'?" data-en="What makes 'broadcast and wait' special?">'xabarni tarqatish va kutish' ning oddiysidan farqi nima?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) Ждет ответа получателя | B) Ничем | C) Удаляет сообщение" data-en="A) Waits for receiver | B) None | C) Deletes message">A) Qabul qiluvchi tugatishini kutadi | B) Farqi yo'q | C) Xabarni o'chiradi</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: A (Ждет завершения всех действий получателей)" data-en="Answer: A (Waits until all receiver actions complete)">Javob: A (Barcha qabul qiluvchilar harakatini tugatishini kutadi)</div>
      </div>
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:var(--danger); color:#fff;">4</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Какой блок лучше использовать для старта уровня после подбора ключа?" data-en="Which block triggers next level after finding key?">Kalit olinganda yangi xonani ochish uchun qaysi xabar kerak?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) Xabar: 'DarvozaOchilsin' | B) Sichqoncha bosilganda | C) Bo'sh joy" data-en="A) Broadcast 'OpenGate' | B) When clicked | C) Empty">A) Xabar: 'DarvozaOchilsin' | B) Sichqoncha bosilganda | C) Probel</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: A (Понятное имя сообщения связывает логику)" data-en="Answer: A (Meaningful broadcast name links game logic)">Javob: A (Aniq nomlangan xabar o'yin mantiqini birlashtiradi)</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: BACKDROP AND SOUND INTEGRATION -->
  <section class="slide" data-phase="Dizayn|Дизайн|Design" data-time="50:00–55:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="АТМОСФЕРА ИГРЫ · СМЕНА ФОНА И ЗВУКИ" data-en="ATMOSPHERE · BACKDROPS & AUDIO">O'YIN ATMOSFERASI · SAHNA FONI VA MUSIQA</span></div>
    <h2 data-ru="Смена Фона по Сигналу: Переход в Замок" data-en="Backdrop Switching via Events: Entering Castle">Xabar Bo'yicha Fon O'zgarishi: Qasrga Kirish</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Сцена тоже слушает сообщения!" data-en="Stage Listens to Broadcasts Too!">Sahna (Stage) ham xabarlarni eshitadi!</h3>
        <p data-ru="Не только спрайты, но и сам задний фон (Сцена) может иметь блок 'когда я получу [xabar]'. По сигналу 'DarvozaOchilsin' фон сменится с Леса на Тронный Зал!" data-en="Not only sprites, but the Stage backdrop itself executes 'when I receive [xabar]'. Switch from Forest to Castle Throne Room!">Faqat spraytlar emas, balki orqa fon (Sahna) ham xabarlarni tinglay oladi. 'DarvozaOchildi' signali bilan o'rmon foni qasr zali foniga o'zgaradi!</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#eab308;">// Sahna (Backdrop) skriptida:</span>
<span style="color:#22c55e;">men [YangiXona v] xabarini olganda</span>
  fonni [Qasr_Ichkari v] ga o'zgartir
  [Fanfare v] g'alaba kuyini chal
        </div>
      </div>
      <div class="card">
        <h3 data-ru="Два правила чистого кода" data-en="Two Rules for Clean Broadcasts">Toza Dasturlashning 2 Qoidasi</h3>
        <ul style="font-size:12px; line-height:1.7; margin-top:8px;">
          <li data-ru="🏷️ <strong>Понятные имена:</strong> Не называйте сообщения 'message1', 'xabar2'. Называйте 'OpenGate', 'DragonAttack', 'GameOver'." data-en="🏷️ <strong>Clear Names:</strong> Avoid 'message1'. Use descriptive names like 'OpenGate', 'DragonAttack', 'GameOver'.">🏷️ <strong>Aniq nomlar:</strong> 'message1' deb nomlamang! 'DarvozaOchildi', 'AjdarhoUygondi' deb yozing.</li>
          <li data-ru="🧹 <strong>Сброс при старте:</strong> При нажатии на зеленый флажок ВСЕГДА возвращайте начальный фон и показывайте спрятанный ключ." data-en="🧹 <strong>Green Flag Reset:</strong> Always restore starting backdrop and show hidden key on green flag.">🧹 <strong>Boshlang'ich holat:</strong> Yashil bayroqcha bosilganda orqa fonni 1-sahifaga qaytarishni unutmang.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: HANDS-ON MISSION BRIEF -->
  <section class="slide" data-phase="Amaliyot|Практика|Practice" data-time="55:00–65:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКАЯ МИССИЯ · СЕКРЕТНЫЙ КВЕСТ" data-en="PRACTICE MISSION · CASTLE QUEST">AMALIY MISSIYA · SEHRLI KALIT KVESTI</span></div>
    <h2 data-ru="Миссия: Собери Ключ, Открой Ворота и Победи Дракона" data-en="Mission: Find Key, Open Gate & Defeat Dragon">Missiya: Kalitni Top, Darvozani Och va G'alaba Qozon</h2>
    <div class="hero-split">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Сценарий Квеста" data-en="Quest Steps">4 Bosqichli Algoritm</div>
        <ul style="font-size:12px; line-height:1.7; margin-top:8px;">
          <li data-ru="1. <strong>Рыцарь</strong> ходит стрелками (WASD) по темному лабиринту." data-en="1. <strong>Knight</strong> navigates dark maze with arrows (WASD).">1. <strong>Ritsar</strong> strelkalar bilan yer osti yo'lidan yuradi.</li>
          <li data-ru="2. Находит <strong>Золотой Ключ</strong> ➔ ключ исчезает и шлет 'OpenGate'." data-en="2. Touches <strong>Golden Key</strong> ➔ key hides and sends 'OpenGate'.">2. <strong>Oltin Kalit</strong>ga tegadi ➔ kalit yo'qolib 'DarvozaOchildi' deb signal beradi.</li>
          <li data-ru="3. <strong>Ворота</strong> ловят сигнал, открываются и исчезают." data-en="3. <strong>Gate</strong> catches broadcast, animates, and clears the path.">3. <strong>Darvoza</strong> signalni tutib, ochiladi va yo'l bo'shaydi.</li>
          <li data-ru="4. Рыцарь доходит до <strong>Сундука</strong> ➔ звучит фанфара Победы!" data-en="4. Knight reaches <strong>Treasure Chest</strong> ➔ Victory Fanfare plays!">4. Ritsar <strong>Xazina Sandig'i</strong>ga yetadi ➔ G'alaba qozonadi!</li>
        </ul>
      </div>
      <div class="card" style="display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:rgba(15,23,42,0.6);">
        <div style="font-size:42px; margin-bottom:10px;">🗝️ 🏰 🛡️ 🏆</div>
        <h3 data-ru="Запуск Игровой Студии" data-en="Open Game Studio">Sehrli Qasr Studiyasi</h3>
        <p style="font-size:13px; max-width:320px; color:var(--ink-secondary);" data-ru="Откройте playground/index.html для визуального тестирования сигналов Broadcast." data-en="Launch playground/index.html to play and inspect broadcast signals live.">Broadcast signallarini o'yinda sinash uchun maydonchani oching.</p>
        <a href="playground/index.html" target="_blank" style="display:inline-block; margin-top:14px; padding:10px 20px; border-radius:10px; background:var(--accent); color:#fff; text-decoration:none; font-weight:700; font-size:13px;" data-ru="🚀 Открыть Игру" data-en="🚀 Launch Playground">🚀 Maydonchani Ochish</a>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: PEER-REVIEW & PLAYTEST -->
  <section class="slide" data-phase="Taqdimot|Тестирование|Playtest" data-time="65:00–72:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ТЕСТИРОВАНИЕ В ПАРАХ · ВЗАИМНАЯ ПРОВЕРКА" data-en="PEER PLAYTEST · RECIPROCAL REVIEW">JUFTLIKDA PLAYTEST · O'ZARO SINOV</span></div>
    <h2 data-ru="Тест-Драйв: Сыграй в Игру Соседа по Парте" data-en="Playtest: Swap and Play Your Teammate's Game">Playtest: Partadoshingizning O'yinini O'ynab Ko'ring</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Чек-лист Тестера" data-en="Tester Checklist">Kiber-Tekshiruv (Checklist)</div>
        <ul style="font-size:12px; line-height:1.7; margin-top:8px;">
          <li data-ru="[ ] Исчезает ли Ключ при касании игроком?" data-en="[ ] Does the Key disappear upon touching the player?">[ ] Qahramon tekkanda Kalit darhol g'oyib bo'ldimi?</li>
          <li data-ru="[ ] Открываются ли Ворота ТОЛЬКО после взятия ключа?" data-en="[ ] Does the Gate open ONLY after obtaining the key?">[ ] Darvoza FAQAT kalit olingandagina ochilmoqdami?</li>
          <li data-ru="[ ] При нажатии на зеленый флажок игра сбрасывается?" data-en="[ ] Does the game reset completely on green flag click?">[ ] Yashil bayroqcha bosilganda barcha narsa o'z joyiga qaytdimi?</li>
          <li data-ru="[ ] Звучит ли победный звук при касании сундука?" data-en="[ ] Does victory fanfare trigger upon reaching chest?">[ ] Xazinaga yetganda g'alaba ovozi yangradimi?</li>
        </ul>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Награды Урока" data-en="Lesson Awards">Kiber-Yulduzlar</div>
        <p style="font-size:13px;" data-ru="2 ученика, создавшие самый захватывающий квест с дополнительными сообщениями (например, летающий дракон), покажут свою игру на смартборде!" data-en="2 creators with the most thrilling quests and custom broadcasts (e.g. flying dragon alert) will showcase on the smartboard!">Qo'shimcha qiziqarli xabarlar (masalan, uyg'ongan ajdarho) qo'shgan 2 nafar o'quvchi o'z o'yinini katta doskaga chiqaradi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: ADVANCED SIGNALS (CHAINS) -->
  <section class="slide" data-phase="Kengaytirish|Сложные Цепочки|Chains" data-time="72:00–76:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ПРОДВИНУТЫЙ УРОВЕНЬ · ЦЕПОЧКИ СООБЩЕНИЙ" data-en="ADVANCED CONCEPT · SIGNAL CHAINS">MURAKKAB ZANJIR · KASKAD SIGNALLAR</span></div>
    <h2 data-ru="Цепочки Сообщений: Сигнал Рождает Новый Сигнал" data-en="Signal Chains: One Broadcast Spawns Another">Xabarlar Zanjiri: Bitta Signal Ikkinchisini Qo'zg'atadi</h2>
    <div class="card">
      <div class="code-block" style="font-size:12px; line-height:1.7;">
[ Kalit ] ──► broadcast "DarvozaOchildi"
                     │
                     ▼
             [ Darvoza ] ──(Ochilgach)──► broadcast "AjdahoUygondi"
                                                 │
                                                 ▼
                                         [ Ajdaho ] ──► Olov purkaydi!
      </div>
      <p style="font-size:12px; margin-top:8px; color:var(--ink-secondary);" data-ru="Так создаются настоящие сюжетные игры! Одно событие запускает следующее, превращая Scratch-проект в интерактивный мультфильм-блокбастер." data-en="This is how true narrative games are forged! Cascading events orchestrate thrilling interactive blockbusters.">Haqiqiy sarguzashtli o'yinlar shunday quriladi! Bitta voqea ikkinchisini boshlab, o'yinni qiziqarli filmga aylantiradi.</p>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & 3-TIER HOMEWORK -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="76:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ УРОКА И ДОМАШНЕЕ ЗАДАНИЕ · 10 БАЛЛОВ" data-en="SUMMARY & 3-TIER HOMEWORK · 10 POINTS">XULOSA VA 3 DARAJALI UY VAZIFASI · 10 BALL</span></div>
    <h2 data-ru="Итоги Урока и Домашнее Задание" data-en="Lesson Summary & Homework">Xulosa va 3 Darajali Uy Vazifasi</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Уровень 1: База (4 балла)" data-en="Tier 1: Core (4 pts)">1-Daraja: Baza (4 ball)</div>
        <h3 data-ru="Ключ и Ворота" data-en="Key & Gate">Kalit va Darvoza</h3>
        <p data-ru="Создать 2 спрайта. При касании Ключа отправляется 'OpenGate', и Ворота прячутся." data-en="Create 2 sprites. Touching Key broadcasts 'OpenGate' and hides Gate.">2 ta sprayt yasash. Qahramon Kalitga tekkanda 'OpenGate' yuborilib, Darvoza g'oyib bo'lishi kerak.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Уровень 2: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</div>
        <h3 data-ru="Смена Фона и Музыка" data-en="Scene & Sound">Sahna va Ovozlar</h3>
        <p data-ru="Добавить Сцену, которая ловит 'OpenGate', меняет фон на Тронный Зал и включает победную музыку." data-en="Add Stage catching 'OpenGate', switching backdrop to Castle and playing music.">Sahnaga 'OpenGate' kelganda orqa fon qasr ichkarisiga o'zgarishi va bayramona musiqa chalinishi kerak.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Уровень 3: Челлендж (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</div>
        <h3 data-ru="Сигнал GameOver" data-en="GameOver Event">Xavf va GameOver</h3>
        <p data-ru="Добавить ловушку с лавой. При касании лавы отправляется 'GameOver', и все персонажи замирают." data-en="Add lava trap. Touching lava broadcasts 'GameOver' halting all game scripts.">Lava tuzog'ini qo'shish. Qahramon lavaga tushsa, 'GameOver' xabari bilan barcha o'yin to'xtashi kerak.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px; text-align:center;">
      <p style="font-size:13px;" data-ru="💡 Домашнее задание с автопроверкой доступно в файле vazifa.html с сохранением прогресса в LocalStorage." data-en="💡 Interactive homework with instant feedback is ready in vazifa.html with LocalStorage persistence.">💡 Interaktiv uy vazifasi <a href="vazifa.html" style="color:var(--accent); font-weight:700;">vazifa.html</a> faylida joylashgan bo'lib, avtomatik testlar va saqlash tizimiga ega.</p>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. TEACHER NOTES JSON (Triplets: [title, say, do])
# -----------------------------------------------------------------------------
NOTES_DATA = {
  "uz": [
    ["Kirish va Maqsad", "Bugun qahramonlarimiz bir-biri bilan qanday gaplashishini, ya'ni Broadcast xabarlar tizimini o'rganamiz. Sehrli kalit orqali darvoza ochilishini quramiz.", "Doskaga mavzuni yozing va slaydni oching."],
    ["Uy Vazifasi Tahlili", "O'tgan 30-darsda ko'pchilik o'quvchilarda tangaga tekkanda ball cheksiz oshaverdi. Buning sababi — tangani yashirish unutilgan edi. Golden standardni ko'rsatamiz.", "O'quvchilardan blitz savolga javob oling."],
    ["Broadcast Tushunchasi", "Broadcast — bu butun sinfga yangraydigan maktab qo'ng'irog'i kabi radiosignal. Barcha spraytlar shu signalni eshitib birdaniga harakat qiladi.", "Maktab qo'ng'irog'i metaforasi orqali tushuntiring."],
    ["Ikkita Asosiy Blok", "Sariq rangli Hodisalar bo'limidagi 'xabar tarqatish' va 'men xabarni olganda' bloklarini ko'rsating. Biri yuboruvchi, ikkinchisi qabul qiluvchi.", "Doskada ikkala blokni chizib, ularning vazifasini ayting."],
    ["Signallar Sxemasi", "Kalit olinganda bitta signal bilan ikkita ish: Darvoza ochiladi va Fon musiqasi yangraydi. Bu tizimning go'zalligi.", "Sxemadagi strelkalar yo'nalishini tushuntiring."],
    ["Cheksiz Xabar Tuzog'i", "Xabarni 'doim takrorlash' ichiga qo'yish taqiqlanadi! Aks holda kompyuter qotib qoladi. Xabar faqat 1 marta yuborilib, skript to'xtashi kerak.", "Xato va to'g'ri kod farqini ko'rsating."],
    ["Xabar Tarqatish va Kutish", "Agar qahramonlar navbat bilan gaplashishi kerak bo'lsa, 'xabarni tarqatish va kutish' ishlatiladi. Bu chalkashlikning oldini oladi.", "Dialog misolini tahlil qiling."],
    ["3 Ta Asosiy Holat", "Har qanday o'yinda 3 ta bosh signal bo'ladi: StartGame, GameOver va Victory. Bular butun o'yin holatini boshqaradi.", "3 ta signalni o'quvchilar bilan birga sanang."],
    ["Interaktiv Quiz", "4 ta tezkor savol bilan o'quvchilar tushunchasini mustahkamlaymiz. O'quvchilarni faol javob berishga undaymiz.", "Savollarni birma-bir ochib, to'g'ri javoblarni e'lon qiling."],
    ["Sahna va Fon", "Sahna (Backdrop) ham xabarlarni eshita oladi. Darvoza ochilganda fon qasr ichkarisiga o'zgarishini ko'rsating.", "Sahnaning skript maydonini tushuntiring."],
    ["Amaliy Missiya", "Endi o'quvchilar o'z kompyuterida Ritsar, Kalit, Darvoza va Xazina qutisini yaratib, xabarlar bilan bog'lashadi.", "O'quvchilarni amaliy ishga yo'naltiring."],
    ["Juftlikda Playtest", "O'quvchilar partadoshining o'yinini o'ynab, kalit olinganda darvoza ochilishini sinab ko'rishadi.", "Sinf bo'ylab yurib, loyihalarni baholang."],
    ["Xabarlar Zanjiri", "Bitta signal ikkinchi signalni uyg'otishi mumkin: Kalit -> Darvoza -> Ajdarho. Bu sarguzashtli o'yinlarning asosi.", "Murakkab zanjir mantig'ini tushuntiring."],
    ["Xulosa va Uy Vazifasi", "Bugun jamoaviy xabarlar tizimini o'rgandik. 3 darajali uy vazifasi vazifa.html da berilgan, ballarni e'lon qiling.", "Darsni ijobiy xulosalar bilan yakunlang."]
  ],
  "ru": [
    ["Введение и Цель", "Сегодня мы изучаем систему сообщений (Broadcast) в Scratch: как спрайты общаются между собой и открывают ворота с помощью волшебного ключа.", "Запишите тему на доске и откройте первый слайд."],
    ["Разбор Домашнего Задания", "На 30-м уроке частой ошибкой было бесконечное начисление очков при касании монеты из-за отсутствия блока 'спрятаться'. Разбираем золотой стандарт.", "Примите ответы на блиц-вопрос."],
    ["Понятие Broadcast", "Broadcast — это как школьный звонок, который слышат сразу все классы. Один спрайт кричит, а остальные одновременно реагируют.", "Объясните метафору радиосигнала."],
    ["Два Главных Блока", "В желтом разделе Событий изучаем 'передать сообщение' и 'когда я получу'. Один отправляет, второй принимает.", "Изобразите блоки на доске."],
    ["Схема Сигналов", "Один сигнал подбора ключа активирует сразу два спрайта: ворота открываются, музыка начинает играть.", "Поясните стрелки на архитектурной схеме."],
    ["Ловушка Спама", "Запрещено вставлять Broadcast внутрь вечного цикла! Игра зависнет. Сигнал должен посылаться ровно один раз.", "Подчеркните важность блока 'спрятаться'."],
    ["Передать и Ждать", "Для последовательных диалогов используется блок 'передать и ждать', чтобы реплики не накладывались друг на друга.", "Разберите пример диалога рыцаря и мага."],
    ["Три Состояния Игры", "В любой игре есть три главных события: StartGame, GameOver и Victory, управляющие сменой сцен.", "Назовите эти три состояния вместе с классом."],
    ["Интерактивный Квиз", "Закрепляем понимание радиосигналов через 4 быстрых блиц-вопроса.", "Обсудите ответы и похвалите активных."],
    ["Смена Фона и Сцена", "Сцена тоже умеет слушать сообщения. При сигнале ворота открываются, и фон меняется на Замок.", "Покажите скрипты сцены."],
    ["Практическая Миссия", "Ученики создают квест: Рыцарь, Ключ, Ворота и Сундук победы, связывая их сигналами.", "Контролируйте ход самостоятельной работы."],
    ["Парный Тест-Драйв", "Соседи по парте меняются местами и тестируют квесты друг друга по чек-листу.", "Оцените лучшие работы в классе."],
    ["Цепочки Сигналов", "Один сигнал может порождать следующий: Ключ -> Ворота -> Пробуждение Дракона. Так строятся сюжетные квесты.", "Поясните каскадные события."],
    ["Итоги и Задание", "Мы освоили командную работу спрайтов. 3-уровневое домашнее задание доступно в vazifa.html.", "Напомните критерии оценки на 10 баллов."]
  ],
  "en": [
    ["Intro & Mission", "Today we discover Scratch Broadcast messaging: how sprites communicate like radio stations and unlock castle gates using a magic key.", "Write topic on board and project slide 1."],
    ["Homework Review", "The major bug in lesson 30 was infinite score runaway when touching coins due to missing 'hide'. Reviewing the golden standard.", "Collect quick answers to blitz question."],
    ["Broadcast Concept", "Broadcast acts like a school bell heard across every room. One sprite triggers, and all listening sprites act simultaneously.", "Explain the radio broadcast analogy."],
    ["Two Core Blocks", "In the yellow Events category, explore 'broadcast [msg]' and 'when I receive [msg]'. One transmits, the other listens.", "Sketch both blocks on the board."],
    ["Signal Architecture", "Touching the key triggers two sprites at once: the Gate swings open and triumphant audio plays.", "Walk through signal flow arrows."],
    ["Broadcast Loop Trap", "Never place broadcasts inside unthrottled forever loops! The game freezes. Fire broadcasts strictly once.", "Highlight the difference between spam and clean code."],
    ["Broadcast and Wait", "For sequential dialogue, use 'broadcast and wait' so speech bubbles never overlap awkwardly.", "Inspect the wizard and knight dialogue."],
    ["Three Game States", "Every complete arcade game manages three core states: StartGame, GameOver, and Victory.", "Recite the three states with the room."],
    ["Interactive Quiz", "Reinforce messaging concepts via 4 rapid-fire quiz questions.", "Reveal correct answers and celebrate accuracy."],
    ["Stage & Backdrops", "The Stage listens to broadcasts too! Switch backgrounds from dark forest to throne room upon entry.", "Explain stage event blocks."],
    ["Hands-on Quest", "Students build their playable quest: Knight, Key, Gate, and Treasure Chest connected by broadcasts.", "Guide students as they code."],
    ["Peer Playtesting", "Teammates swap laptops and playtest each other's quests against the rubric checklist.", "Highlight stand-out mechanics."],
    ["Cascading Chains", "One broadcast triggers another: Key -> Gate -> Dragon Awakens! That is narrative game design.", "Explain cascading event chains."],
    ["Summary & Homework", "We mastered sprite synchronization. The 3-tier homework is ready in vazifa.html for 10 total points.", "Summarize key lessons and conclude."]
  ]
}

def build_presentation():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Taqdimot shabloni — Target Maktabi</title>", "<title>5-6-sinf: Broadcast Xabarlar va Sehrli Kalit</title>")
    tpl = re.sub(r'name="total-slides"\s+content="\d+"', 'name="total-slides" content="14"', tpl)
    tpl = re.sub(r'id="totalSlides">0</span>', 'id="totalSlides">14</span>', tpl)

    stage_regex = r'<div class="stage">[\s\S]*?</div><!-- /stage -->'
    new_stage = f'<div class="stage">\n{SLIDES_HTML}\n</div><!-- /stage -->'
    tpl = re.sub(stage_regex, lambda m: new_stage, tpl)

    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    notes_regex = r'var NOTES\s*=\s*\{[\s\S]*?\};'
    tpl = re.sub(notes_regex, lambda m: f'var NOTES = {notes_json};', tpl)

    out_path = os.path.join(DEST_DIR, "prezentatsiya.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

def build_worksheet():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Amaliy Ish Varaqasi — Target Maktabi</title>", "<title>Ish Varaqasi: Broadcast Xabarlar va Sehrli Kalit — 5-6-sinf</title>")
    tpl = tpl.replace("1-AMALIY ISH VARAQASI", "31-AMALIY ISH VARAQASI")
    tpl = tpl.replace("Mavzu: Kirish va Vibecoding asoslari", "Mavzu: Xabarlar va Hodisalar (Broadcast Messages): Qahramonlar Muloqoti va Sehrli Kalit")

    worksheet_body = """
  <div class="mission-box">
    <div class="mission-title" data-ru="МИССИЯ УРОКА: РАДИОСВЯЗЬ СПРАЙТОВ В SCRATCH" data-en="LESSON MISSION: SCRATCH BROADCAST NETWORKING">DARSNING KIBER-MISSIYASI: SPRAYTLAR RADIOMULOQOTI</div>
    <p style="font-size:12px; margin-top:4px;" data-ru="Понять принцип работы сообщений Broadcast, научить персонажей слушать радиосигналы, связать подбор Ключа с открытием Ворот и настроить победный экран игры." data-en="Master Scratch Broadcast messaging, train sprites to react to radio triggers, link the Magic Key pickup to Gate opening, and orchestrate the victory finale.">Scratch-da Broadcast xabarlarining ishlash prinsipini o'rganish, spraytlarni radiosignallarni tinglashga o'rgatish, sehrli Kalit olinganda Darvozani ochish va g'alaba sahnasini boshqarish.</p>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">1</span>
      <h3 data-ru="Сравнение Блоков Сообщений (2 балла)" data-en="Comparing Broadcast Blocks (2 pts)">Xabar Bloklarini Taqqoslash (2 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Соедините блок Scratch с его правильным назначением:" data-en="Match each Scratch block with its correct behavior:">Scratch blokini uning to'g'ri vazifasi bilan tutashtiring:</p>
    <table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:11px;">
      <thead>
        <tr style="background:var(--card-bg, #f1f5f9);">
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Блок Scratch" data-en="Block">Scratch Bloki</th>
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Роль (Отправитель / Получатель)" data-en="Role">Roli</th>
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Что делает в игре?" data-en="Action">O'yinda nima qiladi?</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<code>[передать сообщение]</code>" data-en="<code>[broadcast message]</code>"><code>[xabarni tarqatish]</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="Отправитель" data-en="Sender">Yuboruvchi</td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Посылает сигнал всем спрайтам" data-en="Broadcasts signal to all">________________________</td>
        </tr>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<code>[когда я получу ...]</code>" data-en="<code>[when I receive ...]</code>"><code>[men ... xabarini olganda]</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="Получатель" data-en="Receiver">Qabul qiluvchi</td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Запускает скрипт при получении" data-en="Executes script upon receive">________________________</td>
        </tr>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<code>[передать и ждать]</code>" data-en="<code>[broadcast and wait]</code>"><code>[xabarni tarqatish va kutish]</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="Диалог / Очередь" data-en="Dialogue queue">Navbat bilan suhbat</td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Ждет завершения всех действий" data-en="Awaits receiver completion">________________________</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">2</span>
      <h3 data-ru="Поиск Ошибки в Логике Квеста (3 балла)" data-en="Quest Logic Debugging (3 pts)">Kvest Mantig'idagi Xatoni Topish (3 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Ученик написал скрипт для Ключа, но при касании игра зависла. Найдите ошибку в коде:" data-en="A student coded the Key script, but upon collision the game freezes. Spot the bug:">O'quvchi Kalit uchun skript yozdi, ammo unga tekkanda o'yin qotib qoldi. Xatoni toping:</p>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:10px; margin-top:8px; font-family:monospace; font-size:11px;">
      yashil bayroqcha bosilganda<br>
      doim takrorlash<br>
      &nbsp;&nbsp;agar &lt;qahramonga tegsa&gt; u holda<br>
      &nbsp;&nbsp;&nbsp;&nbsp;[DarvozaOchilsin v] xabarini tarqatish<br>
      <span style="color:#ef4444;">// Nega o'yin qotib qoldi? Nima unutilgan?</span>
    </div>
    <div style="margin-top:6px; font-size:12px; line-height:1.6;">
      Xato sababi: ____________________________________________________________________<br>
      Tuzatish: ____________________________________________________________________
    </div>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">3</span>
      <h3 data-ru="Схема Сюжетного Квеста: 3 Сообщения (3 балла)" data-en="Quest Architecture: 3 Custom Signals (3 pts)">Kiber-Kvest Sxemasi: 3 Ta Maxsus Xabar (3 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Придумайте и запишите 3 понятных имени сообщений для вашей собственной приключенческой игры:" data-en="Design and write 3 meaningful broadcast names for your own adventure game:">O'zingiz yaratayotgan sarguzasht o'yini uchun 3 ta aniq nomlangan xabar yozing:</p>
    <div style="margin-top:6px; font-size:12px; line-height:1.8;">
      1. Xabar nomi: <code>____________________</code> ➔ Vazifasi: ____________________________________<br>
      2. Xabar nomi: <code>____________________</code> ➔ Vazifasi: ____________________________________<br>
      3. Xabar nomi: <code>____________________</code> ➔ Vazifasi: ____________________________________
    </div>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">4</span>
      <h3 data-ru="Критерии Оценки и Рефлексия (2 балла)" data-en="Evaluation Rubric & Reflection (2 pts)">Baholash Mezoni va Xulosa (2 ball)</h3>
    </div>
    <div style="display:flex; justify-content:space-between; font-size:11px; margin-top:6px;">
      <span>[ ] 1-Daraja: Kalit & Darvoza (4 ball)</span>
      <span>[ ] 2-Daraja: Sahna & Ovozlar (4 ball)</span>
      <span>[ ] 3-Daraja: GameOver Signali (2 ball)</span>
    </div>
  </div>
"""
    tpl = re.sub(r'<!-- PAGE 1:[\s\S]*?(?=\n<script>)', lambda m: f'<div class="sheet">\n{worksheet_body}\n</div>', tpl)

    out_path = os.path.join(DEST_DIR, "varaqa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: varaqa.html")

def build_homework():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Vazifa Shabloni — Target Maktabi</title>", "<title>Uy Vazifasi: Broadcast Xabarlar va Sehrli Kalit — 5-6-sinf</title>")
    tpl = tpl.replace("1-AMALIY VAZIFA", "31-AMALIY VAZIFA")
    tpl = tpl.replace("Mavzu: Kirish va Vibecoding Asoslari", "Mavzu: Xabarlar va Hodisalar (Broadcast Messages): Qahramonlar Muloqoti va Sehrli Kalit")

    hw_body = """
  <div class="hw-card">
    <div class="hw-header">
      <span class="badge" style="background:var(--accent); color:#fff;" data-ru="Уровень 1: База (4 балла)" data-en="Tier 1: Core (4 pts)">1-Daraja: Baza (4 ball)</span>
      <h3 data-ru="Связка 'Ключ' и 'Ворота' через Broadcast" data-en="Key & Gate Broadcast Binding">Kalit va Darvoza Bog'lanishi</h3>
    </div>
    <p style="font-size:13px;" data-ru="Заполните пропуски в коде: когда игрок касается ключа, отправить сообщение 'OpenGate' и спрятать ключ:" data-en="Fill in the blanks: when touching key, broadcast 'OpenGate' and hide the key sprite:">Qahramon kalitga tekkanda 'OpenGate' xabarini tarqatish va kalitni yashirish kodini to'ldiring:</p>
    <div class="code-area">
      <textarea id="codeTier1" rows="7" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="Введите код Scratch..." data-placeholder-en="Write Scratch block pseudo-code...">
agar <qahramonga tegsa> u holda
    [OpenGate] xabarini tarqatish
    yashirinish
    ushbu skriptni to'xtatish
</textarea>
    </div>
    <button onclick="testTier1()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--accent); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить код" data-en="Check Code">Tekshirish</button>
    <span id="resTier1" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <div class="hw-card" style="margin-top:16px;">
    <div class="hw-header">
      <span class="badge" style="background:var(--success); color:#fff;" data-ru="Уровень 2: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</span>
      <h3 data-ru="Реакция Ворот на Сообщение" data-en="Gate Reaction Handler">Darvozaning Xabarga Javobi</h3>
    </div>
    <p style="font-size:13px;" data-ru="Напишите скрипт для спрайта Ворот: при получении сообщения 'OpenGate' ворота открываются (меняют костюм) и исчезают:" data-en="Write Gate script: when receiving 'OpenGate', switch costume and hide to let hero pass:">Darvoza sprayti uchun skript: 'OpenGate' xabarini olganda ochiq eshik libosiga o'tib, g'oyib bo'lishini yozing:</p>
    <div class="code-area">
      <textarea id="codeTier2" rows="6" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="men [OpenGate] xabarini olganda..." data-placeholder-en="when I receive [OpenGate]...">
men [OpenGate] xabarini olganda
    libosni [ochiq_darvoza] ga o'zgartir
    (1) soniya kut
    yashirinish
</textarea>
    </div>
    <button onclick="testTier2()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--success); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить реакцию" data-en="Verify Gate">Tekshirish</button>
    <span id="resTier2" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <div class="hw-card" style="margin-top:16px;">
    <div class="hw-header">
      <span class="badge" style="background:var(--danger); color:#fff;" data-ru="Уровень 3: Челлендж (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</span>
      <h3 data-ru="Глобальная Остановка Игры (GameOver)" data-en="Global GameOver Broadcast Handler">GameOver va Hamma Skriptlarni To'xtatish</h3>
    </div>
    <p style="font-size:13px;" data-ru="Напишите обработчик для Сцены: при получении сообщения 'GameOver' сменить фон на темный и остановить все скрипты:" data-en="Code Stage handler: on 'GameOver', switch backdrop to dark and halt all scripts:">Sahna uchun skript: 'GameOver' xabarini olganda fonni qora qilib, barcha skriptlarni to'xtatish kodini yozing:</p>
    <div class="code-area">
      <textarea id="codeTier3" rows="6" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="men [GameOver] xabarini olganda..." data-placeholder-en="when I receive [GameOver]...">
men [GameOver] xabarini olganda
    fonni [Qorong'i_Zindon] ga o'zgartir
    [hammasini to'xtatish]
</textarea>
    </div>
    <button onclick="testTier3()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--danger); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить остановку" data-en="Verify GameOver">Tekshirish</button>
    <span id="resTier3" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <script>
    function testTier1() {
      var txt = document.getElementById('codeTier1').value;
      var res = document.getElementById('resTier1');
      if (txt.includes('OpenGate') && (txt.includes('tarqatish') || txt.includes('broadcast')) && txt.includes('yashirinish')) {
        res.textContent = "✅ Barakalla! Kalit xabarni to'g'ri tarqatdi va yashirindi (+4 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: [OpenGate] xabari va 'yashirinish' buyrug'ini tekshiring!";
        res.style.color = "var(--danger)";
      }
    }

    function testTier2() {
      var txt = document.getElementById('codeTier2').value;
      var res = document.getElementById('resTier2');
      if (txt.includes('OpenGate') && txt.includes('olganda') && txt.includes('yashirinish')) {
        res.textContent = "✅ Ajoyib! Darvoza xabarni eshitib yo'lni ochdi (+4 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: [OpenGate] xabarini olganda va 'yashirinish' blokidan foydalaning!";
        res.style.color = "var(--danger)";
      }
    }

    function testTier3() {
      var txt = document.getElementById('codeTier3').value;
      var res = document.getElementById('resTier3');
      if (txt.includes('GameOver') && (txt.includes("to'xtatish") || txt.includes("stop"))) {
        res.textContent = "✅ Mukammal! Butun o'yinni to'xtatuvchi global signal to'g'ri ulandi (+2 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: [GameOver] xabari va hammasini to'xtatish blokini yozing!";
        res.style.color = "var(--danger)";
      }
    }
  </script>
"""
    tpl = re.sub(r'<main class="container">[\s\S]*?</main>', lambda m: f'<main class="container">\n{hw_body}\n</main>', tpl)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    doc = """# O'qituvchi Qo'llanmasi (Teacher Reading)
## 5–6-sinf · 12-hafta · 31-dars
### Mavzu: Xabarlar va Hodisalar (Broadcast Messages): Qahramonlar Muloqoti va Sehrli Kalit
**Dars formati:** Juftlik Dars (Double Block — 80 daqiqa / 2-soatlik dars)

---

### 1. Darsning Pedagogik Maqsadi va Metodikasi
O'tgan 30-darsda o'quvchilar bitta sprayt ichida o'zgaruvchilarni (tangalar, jonlar, taymer) boshqarishni o'rgandilar.
Bugungi 31-darsning asosiy maqsadi — bir nechta mustaqil spraytlarni yagona tizimga birlashtirishdir.
Scratch-dagi **Broadcast Messages** (Xabarlar) mexanizmi event-driven arxitekturaning (Publish-Subscribe Pattern) bolalar uchun eng sodda va kuchli namunasidir.

---

### 2. Darsning 80 Daqiqalik Aniq Xronometraji

#### 1-BOSQICH (40 daqiqa) — Tushuntirish, Sxema va Viktorina
- **00:00–04:00 (4 min):** Kirish, dars mavzusi va maqsadlarini e'lon qilish.
- **04:00–12:00 (8 min):** 30-dars uy vazifasi tahlili: tangaga tekkanda ball to'xtovsiz oshib ketishi xatosi, 'yashirinish'ning zarurligi va 30 sek blitz savol.
- **12:00–18:00 (6 min):** Broadcast nima? Maktab qo'ng'irog'i metaforasi: bitta signal butun o'yinga eshittiriladi.
- **18:00–24:00 (6 min):** Ikkita sariq blok: `[xabarni tarqatish]` (Sender) va `[men xabarni olganda]` (Receiver).
- **24:00–30:00 (6 min):** Signallar arxitekturasi: Kalit olinganda Darvoza ochilishi va sahna musiqasining yangrashi.
- **30:00–35:00 (5 min):** Katta xato: Xabarni `doim takrorlash` ichiga qo'yish o'yinni qotirishi (Spam qopqoni).
- **35:00–40:00 (5 min):** Dialoglar: `[xabarni tarqatish va kutish]` bloki.

#### 2-BOSQICH (40 daqiqa) — Amaliyot, Playtest va Baholash
- **40:00–45:00 (5 min):** 3 ta bosh signal: `StartGame`, `GameOver` va `Victory`.
- **45:00–50:00 (5 min):** Interaktiv Quiz: 4 ta tezkor savol bilan tushunchalarni mustahkamlash.
- **50:00–55:00 (5 min):** Sahna (Backdrop) ning xabarlarga javob qaytarishi.
- **55:00–65:00 (10 min):** Amaliy kiber-kvest: Ritsar, Kalit, Darvoza va Xazina qutisini kodlash.
- **65:00–72:00 (7 min):** Juftlikda Playtest: partadoshining o'yinini sinab ko'rish.
- **72:00–76:00 (4 min):** 2 nafar o'quvchining Smartboardda jonli demosi.
- **76:00–80:00 (4 min):** Dars xulosasi va 3 darajali uy vazifasi (vazifa.html).

---

### 3. O'qituvchi Uchun Chuqur Texnik Savollar va Javoblar

1. **Savol:** Bitta xabar yuborilganda uni bir vaqtda nechta sprayt eshita oladi?
   - **Javob:** Cheksiz miqdorda! Shu xabarni kutuvchi (`men [xabar] olganda`) barcha spraytlar bir soniyada bir vaqtda ishga tushadi.
2. **Savol:** Nega xabar yuborilgandan so'ng kalitni darhol yashirish (`yashirinish`) kerak?
   - **Javob:** Agar yashirilmasa, qahramon kalit ustida turgan har bir soniyada yangidan xabar tarqalaveradi va bu o'yinni qotirib qo'yadi.
3. **Savol:** Sahna (Backdrop) qanday qilib xabarni eshitadi?
   - **Javob:** Sahna ham xuddi spraytlar kabi o'z skript maydoniga ega va unda ham `men [xabar] olganda` blokini qo'yib, fonni o'zgartirish mumkin.
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("  ✓ Created: TEACHER_READING.md")

def build_playground():
    html = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Песочница Scratch: Волшебный Ключ и Broadcast" data-en="Scratch Playground: Magic Key & Broadcast">Sehrli Qasr va Broadcast Maydonchasi</title>
  <style>
    :root {
      --bg: #0b0f19;
      --panel: #111827;
      --card: #1f2937;
      --border: #374151;
      --ink: #f9fafb;
      --ink-dim: #9ca3af;
      --accent: #3b82f6;
      --success: #22c55e;
      --danger: #ef4444;
      --warning: #eab308;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace;
      background: var(--bg);
      color: var(--ink);
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    header {
      background: var(--panel);
      border-bottom: 1px solid var(--border);
      padding: 10px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .badge-sub {
      background: rgba(59,130,246,0.2);
      color: var(--accent);
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 700;
    }
    .main-grid {
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 320px;
      overflow: hidden;
    }
    .canvas-box {
      position: relative;
      background: #000;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    canvas {
      border: 2px solid #334155;
      border-radius: 8px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      background: #1e1b4b;
    }
    .side-panel {
      background: var(--panel);
      border-left: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      padding: 14px;
    }
    .log-box {
      flex: 1;
      background: #090d16;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 10px;
      font-family: monospace;
      font-size: 11px;
      overflow-y: auto;
      line-height: 1.6;
      margin-top: 10px;
    }
    .btn {
      background: #374151;
      color: #fff;
      border: none;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 11px;
      cursor: pointer;
      font-weight: 700;
    }
    .btn.op { background: var(--accent); }
    .btn:hover { opacity: 0.9; }
    .signal-chip {
      display: inline-block;
      padding: 2px 6px;
      border-radius: 4px;
      background: rgba(234, 179, 8, 0.2);
      color: #facc15;
      font-weight: 700;
    }
  </style>
</head>
<body>

<header>
  <div style="display:flex; align-items:center; gap:12px;">
    <strong data-ru="Квест: Волшебный Ключ" data-en="Quest: Magic Key">Sehrli Qasr Kvesti</strong>
    <span class="badge-sub" data-ru="Симуляция Broadcast Сообщений" data-en="Broadcast Signal Simulator">Broadcast Radiomuloqot</span>
  </div>
  <div style="display:flex; gap:10px;">
    <button onclick="toggleLang()" class="btn" id="langBtn" data-ru="UZ / RU / EN" data-en="UZ / RU / EN">UZ / RU / EN</button>
    <button onclick="resetGame()" class="btn" data-ru="Перезапуск" data-en="Restart">Qayta boshlash</button>
  </div>
</header>

<div class="main-grid">
  <div class="canvas-box">
    <canvas id="gameCanvas" width="560" height="380"></canvas>
    <div style="margin-top:8px; font-size:11px; color:#94a3b8;" data-ru="Управление: Стрелки клавиатуры или W, A, S, D" data-en="Controls: Arrow keys or W, A, S, D">Boshqaruv: Klaviatura strelkalari yoki W, A, S, D</div>
  </div>

  <div class="side-panel">
    <h3 style="font-size:13px;" data-ru="Радиоэфир Broadcast" data-en="Broadcast Radio Feed">Broadcast Radiokanali</h3>
    <p style="font-size:11px; color:var(--ink-dim); margin-top:4px;" data-ru="Здесь отображаются сообщения, которыми спрайты обмениваются в реальном времени:" data-en="Real-time broadcast events exchanged between sprites:">Spraytlar almashayotgan xabarlar jonli radiotasmada ko'rinadi:</p>
    
    <div class="log-box" id="logBox">
      <div style="color:#64748b;">[Tizim]: O'yin boshlandi. Kalitni toping!</div>
    </div>

    <div style="margin-top:12px; padding:10px; background:#1e293b; border-radius:6px; font-size:11px;">
      <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
        <span data-ru="Статус Ворот:" data-en="Gate Status:">Darvoza holati:</span>
        <strong id="gateStatus" style="color:#ef4444;" data-ru="Заперто" data-en="Locked">Qulflangan 🔒</strong>
      </div>
      <div style="display:flex; justify-content:space-between;">
        <span data-ru="Ключ:" data-en="Key:">Kalit:</span>
        <strong id="keyStatus" style="color:#eab308;" data-ru="В комнате" data-en="In maze">Labirintda 🗝️</strong>
      </div>
    </div>
  </div>
</div>

<script>
var curLang = 'uz';
var canvas = document.getElementById('gameCanvas');
var ctx = canvas.getContext('2d');

var player = { x: 50, y: 190, r: 14, speed: 4 };
var key = { x: 140, y: 80, r: 12, collected: false };
var gate = { x: 380, y: 140, w: 20, h: 100, open: false };
var chest = { x: 480, y: 190, w: 28, h: 28, opened: false };
var victory = false;

var keys = {};
window.addEventListener('keydown', function(e) { keys[e.key] = true; });
window.addEventListener('keyup', function(e) { keys[e.key] = false; });

function toggleLang() {
  if (curLang === 'uz') curLang = 'ru';
  else if (curLang === 'ru') curLang = 'en';
  else curLang = 'uz';
  document.getElementById('langBtn').textContent = curLang.toUpperCase();
  applyLang();
}

function applyLang() {
  var els = document.querySelectorAll('[data-ru]');
  els.forEach(function(el) {
    if (curLang === 'ru') el.textContent = el.getAttribute('data-ru');
    else if (curLang === 'en') el.textContent = el.getAttribute('data-en');
  });
}

function logMsg(msg) {
  var box = document.getElementById('logBox');
  var d = document.createElement('div');
  d.innerHTML = msg;
  box.appendChild(d);
  box.scrollTop = box.scrollHeight;
}

function update() {
  if (victory) return;

  var nextX = player.x;
  var nextY = player.y;

  if (keys['ArrowUp'] || keys['w'] || keys['W']) nextY -= player.speed;
  if (keys['ArrowDown'] || keys['s'] || keys['S']) nextY += player.speed;
  if (keys['ArrowLeft'] || keys['a'] || keys['A']) nextX -= player.speed;
  if (keys['ArrowRight'] || keys['d'] || keys['D']) nextX += player.speed;

  // Collision with Gate
  if (!gate.open && nextX + player.r > gate.x && nextX - player.r < gate.x + gate.w && nextY > gate.y && nextY < gate.y + gate.h) {
    // blocked by gate
  } else {
    player.x = Math.max(player.r, Math.min(canvas.width - player.r, nextX));
    player.y = Math.max(player.r, Math.min(canvas.height - player.r, nextY));
  }

  // Key Pickup Collision
  if (!key.collected) {
    var distKey = Math.hypot(player.x - key.x, player.y - key.y);
    if (distKey < player.r + key.r) {
      key.collected = true;
      logMsg('<span class="signal-chip">BROADCAST: "DarvozaOchildi"</span> ➔ Kalit yubordi!');
      document.getElementById('keyStatus').textContent = "Olingan ✅";
      document.getElementById('keyStatus').style.color = "var(--success)";

      setTimeout(function() {
        gate.open = true;
        logMsg('<span style="color:#22c55e;">[Darvoza]:</span> Xabar qabul qilindi. Darvoza ochildi!');
        document.getElementById('gateStatus').textContent = "Ochiq 🔓";
        document.getElementById('gateStatus').style.color = "var(--success)";
      }, 400);
    }
  }

  // Chest Victory Collision
  if (gate.open && !chest.opened) {
    if (player.x + player.r > chest.x && player.x - player.r < chest.x + chest.w && player.y + player.r > chest.y && player.y - player.r < chest.y + chest.h) {
      chest.opened = true;
      victory = true;
      logMsg('<span class="signal-chip" style="background:rgba(34,197,94,0.3); color:#4ade80;">BROADCAST: "VICTORY"</span> ➔ G\'alaba!');
      logMsg('<span style="color:#4ade80; font-weight:700;">🏆 TABRIKLAYMIZ! Qasr kvesti yakunlandi!</span>');
    }
  }
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Background Castle Grid
  ctx.strokeStyle = '#2e1065';
  ctx.lineWidth = 1;
  for (var x = 0; x < canvas.width; x += 40) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
  }
  for (var y = 0; y < canvas.height; y += 40) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
  }

  // Draw Key
  if (!key.collected) {
    ctx.font = '24px sans-serif';
    ctx.fillText('🗝️', key.x - 12, key.y + 8);
  }

  // Draw Gate
  if (!gate.open) {
    ctx.fillStyle = '#ef4444';
    ctx.fillRect(gate.x, gate.y, gate.w, gate.h);
    ctx.fillStyle = '#fff';
    ctx.font = '14px sans-serif';
    ctx.fillText('🔒', gate.x + 2, gate.y + 55);
  } else {
    ctx.strokeStyle = '#22c55e';
    ctx.setLineDash([4, 4]);
    ctx.strokeRect(gate.x, gate.y, gate.w, gate.h);
    ctx.setLineDash([]);
  }

  // Draw Chest
  ctx.font = '28px sans-serif';
  ctx.fillText(chest.opened ? '🏆' : '📦', chest.x, chest.y + 24);

  // Draw Player (Knight)
  ctx.font = '28px sans-serif';
  ctx.fillText('🛡️', player.x - 14, player.y + 10);

  // Draw Victory Message
  if (victory) {
    ctx.fillStyle = 'rgba(0,0,0,0.7)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#facc15';
    ctx.font = 'bold 28px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText("G'ALABA! BROADCAST ISHLADI!", canvas.width / 2, canvas.height / 2);
    ctx.textAlign = 'start';
  }
}

function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}

function resetGame() {
  player.x = 50; player.y = 190;
  key.collected = false;
  gate.open = false;
  chest.opened = false;
  victory = false;
  document.getElementById('logBox').innerHTML = '<div style="color:#64748b;">[Qayta boshlandi] Kalitni toping!</div>';
  document.getElementById('gateStatus').textContent = "Qulflangan 🔒";
  document.getElementById('gateStatus').style.color = "#ef4444";
  document.getElementById('keyStatus').textContent = "Labirintda 🗝️";
  document.getElementById('keyStatus').style.color = "#eab308";
}

loop();
</script>

</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "playground", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: playground/index.html")

def main():
    print("📦 Building 5-6-sinf (Lesson 31: Events & Broadcast Messaging)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_playground()
    print("🎉 Done! Generated Grade 5–6 Lesson 31.")

if __name__ == "__main__":
    main()
