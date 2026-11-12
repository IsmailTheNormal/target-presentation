#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_9_w10_l30.py — 9-sinf (10-hafta 30-dars)
Mavzu: Real-Vaqt Texnologiyalari: WebSockets va LAN Kiber-Chat Engine
Track: Junior Vibecoders, Full-Stack & DevOps Track
Duration: 80 daqiqa (Double block / 2-hour class)
"""

import os
import sys
import json
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LESSON_DIR = os.path.join(REPO_ROOT, "classes", "9-sinf", "10-hafta", "30-dars-websockets-va-jonli-chat")
STUDIO_DIR = os.path.join(LESSON_DIR, "studio")
LAB_DIR = os.path.join(LESSON_DIR, "lab")
os.makedirs(STUDIO_DIR, exist_ok=True)
os.makedirs(LAB_DIR, exist_ok=True)

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
    TPL_PRES = f.read()

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
    TPL_VAR = f.read()

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
    TPL_VAZ = f.read()

def build_9_lesson():
    print("📦 Generating 9-sinf (30-dars: Real-Vaqt Texnologiyalari: WebSockets va LAN Kiber-Chat)...")

    title_uz = "30-dars: Real-Vaqt Texnologiyalari: WebSockets va LAN Kiber-Chat Engine"
    title_ru = "Урок 30: Технологии Реального Времени: WebSockets и LAN Кибер-Чат Движок"
    title_en = "Lesson 30: Real-Time Technologies: WebSockets & LAN Cyber Chat Engine"

    # ============================================================
    # 1. PREZENTATSIYA.HTML (14 Slides, 80 Minutes)
    # ============================================================
    tpl = TPL_PRES
    tpl = re.sub(r"<title[^>]*>.*?</title>", f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>', tpl)
    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>', '<span class="tag" data-ru="9 · ВАЙБКОДИНГ" data-en="9 · VIBECODING">9 · VIBECODING</span>', tpl, count=1)
    tpl = tpl.replace('<span id="totalSlides">6</span>', '<span id="totalSlides">14</span>')

    titles_dict = {"uz": title_uz, "ru": title_ru, "en": title_en}
    titles_json = json.dumps(titles_dict, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    slides = []

    # Slide 1: Titul
    slides.append("""  <!-- SLIDE 1: TITUL -->
  <section class="slide is-on" data-phase="Kirish|Введение|Introduction" data-time="00:00–04:00">
    <div class="eyebrow" data-ru="9-СИНФ · 10-Я НЕДЕЛЯ · УРОК 30" data-en="GRADE 9 · WEEK 10 · LESSON 30">9-SINF · 10-HAFTA · 30-DARS</div>
    <h1 data-ru="Технологии Реального Времени: WebSockets и LAN Кибер-Чат Движок" data-en="Real-Time Technologies: WebSockets & LAN Cyber Chat Engine">Real-Vaqt Texnologiyalari: WebSockets va LAN Kiber-Chat Engine</h1>
    <p class="lede" data-ru="Как работают Discord, Telegram и онлайн-игры под капотом: от медленного HTTP-опроса к постоянному полнодуплексному TCP-туннелю WebSockets с нулевой задержкой." data-en="How Discord, Telegram, and multiplayer games operate under the hood: transitioning from sluggish HTTP polling to permanent full-duplex WebSocket TCP tunnels with zero latency.">Discord, Telegram va multiplayer o'yinlar kapot ostida qanday ishlaydi: sekin HTTP polling so'rovlaridan doimiy full-duplex WebSocket TCP tunneliga va yashin tezligidagi real-vaqt aloqasiga o'tamiz.</p>
    <div class="grid c3" style="margin-top:24px;">
      <div class="card">
        <h3 data-ru="Формат занятия" data-en="Lesson Format">Format va Davomiylik</h3>
        <p data-ru="Спаренный блок: 2 x 40 минут = 80 минут глубокой сетевой инженерии" data-en="Double block: 2 x 40 min = 80 min intensive network engineering">Juftlik blok: 2 x 40 daqiqa = 80 daqiqalik chuqur tarmoq muhandisligi</p>
      </div>
      <div class="card">
        <h3 data-ru="Главная миссия" data-en="Core Mission">Amaliy Missiya</h3>
        <p data-ru="Запустить реальный чат-сервер и обмениваться сообщениями между компьютерами класса" data-en="Launch live real-time chat engine communicating across lab computers over LAN">Sinfdagi kompyuterlar o'rtasida jonli ishlovchi LAN Kiber-Chat va paket snifferini qurish</p>
      </div>
      <div class="card">
        <h3 data-ru="10-Балльная система" data-en="10-Point Rubric">Baholash Mezoni</h3>
        <p data-ru="4 балла: Клиент и 101 Handshake · 4 балла: Серверный Broadcast · 2 балла: Комнаты и Ping" data-en="4 pts: Client & 101 Handshake · 4 pts: Server Broadcast · 2 pts: Rooms & Latency Ping">4 ball: Klient & 101 Handshake · 4 ball: Broadcast tarqatish · 2 ball: Xonalar va Ping</p>
      </div>
    </div>
  </section>""")

    # Slide 2: Mandatory HW Review
    slides.append("""  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00">
    <div class="eyebrow" data-ru="РАЗБОР ДОМАШНЕГО ЗАДАНИЯ · МОСТ К НОВОЙ ТЕМЕ" data-en="HOMEWORK REVIEW · BRIDGE TO NEW TOPIC">UY VAZIFASI TAHLILI VA O'TGAN DARS KO'PRIGI</div>
    <h2 data-ru="29-Урок: Асинхронность и Ловушка HTTP-Опроса (Polling)" data-en="Lesson 29 Review: Async JS & The HTTP Polling Bottleneck">29-Dars Tahlili: Asinxron JS va HTTP Polling Qopqoni</h2>
    <p class="lede" data-ru="На прошлом уроке мы освоили Promise и async/await. Давайте разберем, почему попытка сделать чат через setInterval(fetch, 1000) убивает сервер:" data-en="Last lesson we mastered Promises and async/await. Let's inspect why building chat via setInterval(fetch, 1000) crashes servers:">29-darsda Promise va async/await asinxronligini o'rgandik. Keng tarqalgan xato — har soniyada `setInterval(fetch, 1000)` bilan serverdan xabar so'rash nega halokatga olib kelishini ko'ramiz:</p>
    
    <div class="grid c2" style="margin-top:16px;">
      <div class="card" style="border-left:4px solid var(--accent);">
        <span class="pill" style="background:var(--accent-soft); color:var(--accent-ink);" data-ru="Типичная Ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (HTTP Polling)</span>
        <h3 style="margin-top:8px;" data-ru="Бесконечный HTTP Polling цикл" data-en="Infinite HTTP Polling Loop">Cheksiz HTTP So'rovlar Bo'roni</h3>
        <pre><code style="font-size:12px;">// ❌ XATO: Har 1 soniyada serverga so'rov urish!
setInterval(async () => {
  const res = await fetch("/api/messages");
  const data = await res.json(); // 99% holatda bo'sh []!
}, 1000);</code></pre>
        <p style="font-size:12.5px; color:var(--ink-2); margin-top:6px;" data-ru="1000 учеников создают 3 600 000 HTTP-запросов в час. 99% из них возвращают пустоту, сжигая CPU и трафик." data-en="1,000 users generate 3.6 million HTTP requests per hour. 99% return empty arrays, scorching CPU and wasting bandwidth.">1000 ta foydalanuvchi soatiga 3 600 000 ta HTTP so'rov hosil qiladi. 99% so'rovlar bo'sh qaytib, serverni qotiradi.</p>
      </div>

      <div class="card" style="border-left:4px solid var(--green);">
        <span class="pill" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой Стандарт (Golden Solution)" data-en="Golden Standard">Oltin Yechim (WebSockets)</span>
        <h3 style="margin-top:8px;" data-ru="Постоянный сокетный туннель (ws://)" data-en="Persistent Socket Tunnel (ws://)">Doimiy Ochiq TCP Tunnel</h3>
        <pre><code style="font-size:12px;">// ✅ TOZA STANDART: Doimiy ochiq soket!
const socket = new WebSocket("ws://192.168.1.50:8080");

// Server o'zi yangi xabar kelganda itarib beradi (Push)
socket.onmessage = (event) => {
  const msg = JSON.parse(event.data);
  displayMessage(msg);
};</code></pre>
        <p style="font-size:12.5px; color:var(--ink-2); margin-top:6px;" data-ru="Никакого опроса! Соединение открыто один раз. Задержка падает с 1000 мс до 5 миллисекунд." data-en="Zero polling waste! The tunnel stays open once. Latency plummets from 1000 ms to sub-5 milliseconds.">Hech qanday keraksiz so'rov yo'q! Ulanish 1 marta ochiladi. Kechikish 1 soniyadan 5 millisekundga tushadi!</p>
      </div>
    </div>

    <div class="card" style="margin-top:14px; background:rgba(255,255,255,0.7); display:flex; align-items:center; justify-content:space-between; gap:16px;">
      <div>
        <span class="pill" style="background:#00214a; color:#fff;" data-ru="30-Секундный Блиц" data-en="30-Second Blitz">30 Soniyalik Blitz</span>
        <b style="margin-left:8px;" data-ru="Какой HTTP статус-код означает успешное переключение протокола на WebSocket?" data-en="Which HTTP status code confirms switching protocols to WebSocket?">Qaysi HTTP status kodi WebSocket protokoliga o'tishni tasdiqlaydi?</b>
      </div>
      <div style="font-size:13px; font-weight:700; color:var(--green);" data-ru="Ответ: 101 Switching Protocols" data-en="Answer: 101 Switching Protocols">Javob: 101 Switching Protocols!</div>
    </div>
  </section>""")

    # Slide 3: Real Muammo
    slides.append("""  <!-- SLIDE 3: PROBLEM -->
  <section class="slide" data-phase="Muammo|Проблема|Problem" data-time="12:00–18:00">
    <div class="eyebrow" data-ru="ПРОБЛЕМА · ПОЧЕМУ HTTP НЕ СПРАВЛЯЕТСЯ" data-en="PROBLEM · WHY HTTP FAILS REAL-TIME">AQLIY HUJUM · REAL MUAMMO</div>
    <h2 data-ru="Почему Обычный HTTP Убивает Онлайн-Игры и Чаты?" data-en="Why Does Standard HTTP Ruin Online Games and Live Chats?">Nega Oddiy HTTP Real-Vaqt O'yinlari va Chatlarini O'ldiradi?</h2>
    <p class="lede" data-ru="HTTP создавался для статических текстовых документов: клиент спрашивает, сервер отвечает и закрывает дверь. В реальном времени это приводит к 3 катастрофам:" data-en="HTTP was architected for static hypertexts: client asks, server replies, and shuts the door. In real-time apps, this triggers 3 systemic catastrophes:">HTTP statik veb-sahifalar uchun yaratilgan: klient so'raydi, server javob beradi va ulanishni yopadi. Jonli tizimlarda bu 3 ta katta muammoga olib keladi:</p>
    
    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <span class="pill" style="background:#fee2e2; color:#b91c1c;" data-ru="1. Фатальный Лаг" data-en="1. Latency Lag">1. Kechikish (Lag)</span>
        <h3 style="margin-top:10px;" data-ru="Задержка 1-2 секунды" data-en="1-2 Second Latency">1–2 Soniyalik Lag</h3>
        <p data-ru="В шутере CS2 или чате задержка в 1 секунду — это смерть. Вы видите врага там, где его уже давно нет." data-en="In competitive games or active chats, a 1-second lag is fatal. You perceive players where they stood in the past.">Online o'yinda yoki tezkor chatda 1 soniyalik kechikish halokatlidir. Xabarlar kech yetib keladi.</p>
      </div>

      <div class="card">
        <span class="pill" style="background:#fef3c7; color:#b45309;" data-ru="2. Мусорные Заголовки" data-en="2. Header Overhead">2. Gigabaytlab Ortiqcha Kod</span>
        <h3 style="margin-top:10px;" data-ru="1 КБ на каждое слово" data-en="1 KB per Single Byte">1 KB Sarlavha Yuklamasi</h3>
        <p data-ru="Каждый HTTP-запрос тащит куки, User-Agent и заголовки. Чтобы передать слово 'Ok' (2 байта), отправляется 1000 байт!" data-en="Every HTTP request transmits cookies and headers. Sending 2 bytes of text carries 1,000 bytes of overhead!">"Ha" degan 2 baytli xabarni yuborish uchun HTTP 1000 baytlik (1 KB) keraksiz sarlavha va cookie paketlarini tashiydi.</p>
      </div>

      <div class="card">
        <span class="pill" style="background:#ede9fe; color:#6d28d9;" data-ru="3. Серверный Коллапс" data-en="3. Server Crash">3. Serverning Qulashi</span>
        <h3 style="margin-top:10px;" data-ru="Проблема C10K" data-en="The C10K Crisis">C10K Falokati</h3>
        <p data-ru="Если 10 000 игроков ежесекундно шлют запросы, веб-сервер открывает 10 000 новых TCP-сокетов и зависает." data-en="If 10,000 gamers spam HTTP polls per second, the server exhausts available sockets and crashes under load.">10,000 ta foydalanuvchi har soniyada so'rov yuborsa, server protsessori 100% ga chiqib qulab tushadi.</p>
      </div>
    </div>
  </section>""")

    # Slide 4: WebSockets Konsept
    slides.append("""  <!-- SLIDE 4: WEBSOCKET CONCEPT -->
  <section class="slide" data-phase="Konsept|Концепт|Concept" data-time="18:00–24:00">
    <div class="eyebrow" data-ru="ПРОТОКОЛ НОВОГО ПОКОЛЕНИЯ" data-en="NEXT-GEN PROTOCOL">YANGI PARADIGMA · OCHIQ TCP TUNNELI</div>
    <h2 data-ru="WebSockets: Полнодуплексный Туннель Сквозь 101 Handshake" data-en="WebSockets: Full-Duplex Tunnel via 101 Handshake">WebSockets: 101 Handshake Orqali Doimiy Full-Duplex Tunnel</h2>
    <p class="lede" data-ru="WebSocket начинается как обычный HTTP-запрос, но вместо завершения 'договаривается' превратиться в непрерывный сокет:" data-en="A WebSocket connection initiates as a standard HTTP request, but seamlessly negotiates an upgrade into a raw TCP socket:">WebSocket odatiy HTTP so'rovi kabi boshlanadi, lekin ulanish yopilmasdan, server bilan doimiy ochiq tunnelga aylanadi:</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Процесс Рукопожатия (Handshake)" data-en="Handshake Protocol Flow">Handshake Qadamlari</h3>
        <ul style="margin-left:18px; line-height:1.9; font-size:13.5px; margin-top:10px;">
          <li data-ru="1. Клиент шлет запрос: Upgrade: websocket и Sec-WebSocket-Key." data-en="1. Client initiates: Upgrade: websocket and Sec-WebSocket-Key."><b style="color:var(--accent);">1. Client so'rovi:</b> `Upgrade: websocket` va maxfiy `Sec-WebSocket-Key` jo'natadi.</li>
          <li data-ru="2. Сервер отвечает: HTTP 101 Switching Protocols и подтверждает хеш." data-en="2. Server confirms: HTTP 101 Switching Protocols with hash accept."><b style="color:var(--green);">2. Server javobi:</b> `HTTP/1.1 101 Switching Protocols` bilan rozi bo'ladi.</li>
          <li data-ru="3. Туннель открыт: Соединение переходит в режим чистого TCP-потока." data-en="3. Tunnel unlocked: Stream enters raw bidirectional TCP frame mode."><b style="color:#d97706;">3. Tunnel ochildi:</b> Endi ulanish hech qachon yopilmaydi (Full-Duplex).</li>
          <li data-ru="4. Двусторонний Push: И сервер, и клиент могут слать данные в любой миг!" data-en="4. Bidirectional Push: Both server and client can push payloads anytime!"><b style="color:#2563eb;">4. Jonli Push:</b> Ikkala tomon ham istalgan soniyada bir-biriga xabar bera oladi!</li>
        </ul>
      </div>

      <div class="card" style="background:#0a0e17; color:#f1f5f9; border-color:#1e293b;">
        <span class="pill" style="background:#1e293b; color:#38bdf8;" data-ru="Сравнение Задержек" data-en="Latency Benchmark">Tezlik Taqqoslashi</span>
        <div style="font-family:'JetBrains Mono',monospace; font-size:16px; font-weight:700; color:#38bdf8; margin:16px 0 10px 0;">HTTP Polling: ~1200 ms vs WS: ~4 ms</div>
        <p style="font-size:12.5px; color:#94a3b8; line-height:1.6;" data-ru="В WebSockets нет накладных расходов на установку TCP/TLS при каждом сообщении. Данные летят в легковесных бинарных фреймах (от 2 байт накладных расходов!)." data-en="WebSockets bypass the overhead of repetitive TCP handshakes. Payloads travel inside lightweight frames carrying only 2 bytes of header overhead!">WebSockets har bir xabar uchun yangitdan TCP/TLS ochmaydi. Xabarlar atigi 2 baytlik engil freymlarda oqib o'tadi!</p>
        <div style="margin-top:14px; padding:8px 12px; background:rgba(56,189,248,0.1); border-radius:6px; font-size:11.5px; color:#7dd3fc;" data-ru="💡 Одно соединение держится часами и передает миллионы сообщений без перезагрузки!" data-en="💡 One socket stays alive for hours delivering millions of frames without reload!">
          💡 Bitta ulanish soatlab ochiq turadi va sahifani bir marta ham yangilamasdan millionlab xabarlarni tashiydi!
        </div>
      </div>
    </div>
  </section>""")

    # Slide 5: Packet Anatomy & DevTools
    slides.append("""  <!-- SLIDE 5: PACKET ANATOMY -->
  <section class="slide" data-phase="Paket Tahlili|Анатомия Пакетов|Packet Anatomy" data-time="24:00–30:00">
    <div class="eyebrow" data-ru="АНАТОМИЯ ФРЕЙМОВ И СНИФФИНГ" data-en="FRAME ANATOMY & SNIFFING">KIBER-DETEKTIVLIK · TARMOQ FREYMLARI</div>
    <h2 data-ru="Внутри WebSocket: Opcodes и Chrome DevTools" data-en="Inside WebSocket: Opcodes & Chrome DevTools">WebSocket Freymlari: Opcodes va Chrome DevTools Tahlili</h2>
    <p class="lede" data-ru="В панели Chrome DevTools -> Network -> WS можно сниффить каждый фрейм. Каждый пакет помечен специальным кодом операции (Opcode):" data-en="Inside Chrome DevTools -> Network -> WS you can inspect every frame live. Each packet is identified by an Opcode:">Chrome DevTools -> Network -> WS bo'limida har bir o'tgan paketni jonli ushlab ko'rish mumkin. Har bir freym o'zining maxsus <b>Opcode</b> turiga ega:</p>

    <div class="grid c2" style="margin-top:16px;">
      <!-- Diagram Card -->
      <div class="card">
        <h3 data-ru="Таблица Кодов Операций (Opcodes)" data-en="Opcode Standards Matrix">Asosiy Opcodes Turlari</h3>
        <table style="width:100%; border-collapse:collapse; font-size:12px; margin-top:10px;">
          <thead>
            <tr style="border-bottom:1px solid var(--rule); text-align:left;">
              <th style="padding:4px 6px;" data-ru="Opcode" data-en="Opcode">Opcode</th>
              <th style="padding:4px 6px;" data-ru="Тип Данных" data-en="Data Type">Turi</th>
              <th style="padding:4px 6px;" data-ru="Назначение" data-en="Purpose">Maqsadi</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px dashed var(--hair);">
              <td style="padding:4px 6px;" data-ru="0x1" data-en="0x1"><code>0x1</code></td>
              <td style="padding:4px 6px; color:var(--green); font-weight:700;" data-ru="Текст (UTF-8)" data-en="Text (UTF-8)">Text (UTF-8)</td>
              <td style="padding:4px 6px;" data-ru="JSON строки, чат-сообщения" data-en="JSON payloads, chat messages">JSON matnlari va xabarlar</td>
            </tr>
            <tr style="border-bottom:1px dashed var(--hair);">
              <td style="padding:4px 6px;" data-ru="0x2" data-en="0x2"><code>0x2</code></td>
              <td style="padding:4px 6px; color:#3b82f6; font-weight:700;" data-ru="Бинарный" data-en="Binary">Binary</td>
              <td style="padding:4px 6px;" data-ru="Аудио, картинки, Buffer" data-en="Audio, images, binary blobs">Ovoz, rasm, fayllar</td>
            </tr>
            <tr style="border-bottom:1px dashed var(--hair);">
              <td style="padding:4px 6px;" data-ru="0x8" data-en="0x8"><code>0x8</code></td>
              <td style="padding:4px 6px; color:#ef4444; font-weight:700;" data-ru="Закрытие Сокета" data-en="Connection Close">Connection Close</td>
              <td style="padding:4px 6px;" data-ru="Корректное закрытие сокета" data-en="Graceful socket teardown">Ulanishni xavfsiz yopish</td>
            </tr>
            <tr style="border-bottom:1px dashed var(--hair);">
              <td style="padding:4px 6px;" data-ru="0x9" data-en="0x9"><code>0x9</code></td>
              <td style="padding:4px 6px; color:#d97706; font-weight:700;" data-ru="Пинг (Heartbeat)" data-en="Ping (Heartbeat)">Ping</td>
              <td style="padding:4px 6px;" data-ru="Проверка живо ли соединение" data-en="Heartbeat liveness check">Aloqa tirikligini tekshirish</td>
            </tr>
            <tr>
              <td style="padding:4px 6px;" data-ru="0xA" data-en="0xA"><code>0xA</code></td>
              <td style="padding:4px 6px; color:#10b981; font-weight:700;" data-ru="Понг (Ответ)" data-en="Pong (ACK)">Pong</td>
              <td style="padding:4px 6px;" data-ru="Ответ на Ping (измерение пинга)" data-en="Ping acknowledgment">Pingga javob (Latency hisobi)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- JSON Protocol Card -->
      <div class="card">
        <h3 data-ru="Стандартный JSON Протокол Чата" data-en="Standard JSON Message Protocol">Kiber-Chat JSON Protokoli</h3>
        <p style="font-size:12px; color:var(--ink-2); margin-top:4px;" data-ru="Клиент и сервер общаются структурированными JSON-сообщениями:" data-en="Client and server exchange structured JSON payloads:">Tarmoqda xabarlar chalkashib ketmasligi uchun yagona JSON protokolidan foydalanamiz:</p>
        <pre><code style="font-size:11.5px;">{
  "type": "CHAT",
  "room": "general",
  "user": "Aziz",
  "text": "Salom hammaga!",
  "time": 1731512400
}</code></pre>
        <p style="font-size:11.5px; color:var(--ink-2); margin-top:4px;" data-ru="Поле 'type' указывает действие: CHAT, JOIN, LEAVE, TYPING или PING." data-en="The 'type' field dictates actions: CHAT, JOIN, LEAVE, TYPING, or PING."><code>type</code> maydoni harakatni belgilaydi: <code>CHAT</code>, <code>JOIN</code>, <code>TYPING</code> yoki <code>PING</code>.</p>
      </div>
    </div>
  </section>""")

    # Slide 6: Server Architecture (Node.js & ws)
    slides.append("""  <!-- SLIDE 6: SERVER ARCHITECTURE -->
  <section class="slide" data-phase="Server Arxitekturasi|Серверная Архитектура|Server Architecture" data-time="30:00–35:00">
    <div class="eyebrow" data-ru="СЕРВЕРНЫЙ ДВИЖОК" data-en="SERVER ENGINE">BACKEND VA TARMOQNI BOSHQARISH</div>
    <h2 data-ru="Как Работает WebSocket Сервер: Цикл Рассылки (Broadcast)" data-en="How WebSocket Servers Work: The Broadcast Loop">WebSocket Server Qanday Ishlaydi: Broadcast Tarqatish Tsikli</h2>
    <p class="lede" data-ru="Сервер хранит список всех активных сокетов. Когда один ученик шлет сообщение, сервер рассылает его всем остальным в цикле:" data-en="The server maintains an in-memory set of all active sockets. When one client sends data, the server broadcasts it to all peers:">Server unga ulangan barcha kompyuterlarning soketlarini xotirada saqlaydi. Bitta o'quvchi xabar yozganda, server uni hamma o'quvchilarga tarqatadi (Broadcast):</p>

    <div class="grid c2" style="margin-top:14px;">
      <div class="card">
        <span class="pill" style="background:#e0f2fe; color:#0369a1;" data-ru="Node.js WebSocket Сервер" data-en="Node.js WebSocket Server">Node.js Server Kodi</span>
        <pre><code style="font-size:11.5px;">const { WebSocketServer, WebSocket } = require('ws');
const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', (socket) => {
  console.log('⚡ Yangi o\\'quvchi ulandi!');

  socket.on('message', (raw) => {
    // 1. Kelgan xabarni hammaga tarqatish (Broadcast)
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(raw.toString());
      }
    });
  });
});</code></pre>
      </div>

      <div class="card">
        <h3 data-ru="3 Критических Правила Сервера" data-en="3 Critical Server Rules">Serverning 3 Ta Oltin Qoidasi</h3>
        <ol style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="Проверка readyState: Никогда не отправлять в закрытый сокет (иначе сервер упадет)!" data-en="Verify readyState: Never write to a closed socket (avoids crash)!"><b>readyState Tekshiruvi:</b> Faqat <code>client.readyState === WebSocket.OPEN</code> bo'lgan soketlarga yoziladi!</li>
          <li data-ru="Изоляция комнат: Сообщения из комнаты 'red-team' не должны лететь в 'blue-team'." data-en="Room Isolation: Messages inside 'red-team' must never leak into 'blue-team'."><b>Xonalarni Ajratish:</b> <code>#red-team</code> xabarlari <code>#blue-team</code> o'quvchilariga bormasligi kerak.</li>
          <li data-ru="Heartbeat / Очистка: Закрытые вкладки должны мгновенно удаляться из памяти." data-en="Heartbeat Cleanup: Closed browser tabs must be evicted from memory immediately."><b>Tozalash:</b> Darchani yopgan o'quvchi xotiradan o'chirilishi shart.</li>
        </ol>
      </div>
    </div>
  </section>""")

    # Slide 7: Client Lifecycle
    slides.append("""  <!-- SLIDE 7: CLIENT LIFECYCLE -->
  <section class="slide" data-phase="Mijoz Klienti|Клиентский Код|Client Lifecycle" data-time="35:00–40:00">
    <div class="eyebrow" data-ru="БРАУЗЕРНЫЙ КЛИЕНТ" data-en="BROWSER CLIENT">BRAUZERDA JONLI ULONISH</div>
    <h2 data-ru="Жизненный Цикл Клиента: onopen, onmessage, onclose" data-en="Client Lifecycle: onopen, onmessage, onclose">Klient Hayot Tsikli: onopen, onmessage va Avto-Qayta Ulanish</h2>
    <p class="lede" data-ru="Браузер имеет встроенный глобальный объект WebSocket. Вам не нужны библиотеки — все работает из коробки:" data-en="Modern browsers feature native WebSocket support natively without requiring external heavy libraries:">Brauzerda hech qanday tashqi kutubxonasiz ishlovchi rasmiy <code>WebSocket</code> API mavjud. U 4 ta asosiy hodisaga ega:</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <span class="pill" style="background:#fef3c7; color:#b45309;" data-ru="Чистый JavaScript Клиент" data-en="Pure JavaScript Client">Vanilla JS Klient</span>
        <pre><code style="font-size:11.5px;">const ws = new WebSocket("ws://192.168.1.50:8080");

ws.onopen = () => {
  console.log("🟢 Serverga ulandik!");
  ws.send(JSON.stringify({ type: "JOIN", user: "Ali" }));
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log("📩 Yangi xabar:", data);
};

ws.onclose = () => {
  console.warn("🔴 Aloqa uzildi! Qayta ulanish...");
  setTimeout(connect, 3000); // Auto-reconnect
};</code></pre>
      </div>

      <div class="card">
        <h3 data-ru="Стратегия Auto-Reconnect" data-en="Auto-Reconnect Strategy">Tarmoq Uzilganda Nima Bo'ladi?</h3>
        <p style="font-size:12.5px; color:var(--ink-2); line-height:1.6;" data-ru="Если Wi-Fi мигнул — сокет закроется (onclose). Профессиональный клиент не падает, а запускает таймер повторной попытки через Exponential Backoff:" data-en="If Wi-Fi flickers, the socket closes (onclose). Enterprise clients never panic; they gracefully retry with Exponential Backoff:">Agar Wi-Fi uzilib qolsa — soket yopiladi (<code>onclose</code>). Haqiqiy professional klient xatolik bermasdan, har 2-3 soniyada avtomatik qayta ulanishni amalga oshiradi.</p>
        <div style="margin-top:14px; padding:10px; background:rgba(16,185,129,0.1); border-left:3px solid var(--green); border-radius:4px; font-size:12px;">
          ✓ Natija: O'quvchi sahifani F5 qilib yangilashi shart emas — chat o'zi avtomatik tiklanadi!
        </div>
      </div>
    </div>
  </section>""")

    # Slide 8: In-Deck Interactive Simulator
    slides.append("""  <!-- SLIDE 8: IN-DECK INTERACTIVE SIMULATOR -->
  <section class="slide" data-phase="Jonli Sinov|Интерактив|Live Demo" data-time="40:00–48:00">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНЫЙ ТРЕНАЖЕР НА ЭКРАНЕ" data-en="INTERACTIVE SMARTBOARD LAB">JONLI WEBSOCKET SIMULYATORI</div>
    <h2 data-ru="Лаборатория Пакетов: Alice и Bob в Реальном Времени" data-en="Live Packet Lab: Alice & Bob in Real-Time">Smartboardda Jonli Paketlar Oqimi: Alice va Bob</h2>
    <p class="lede" data-ru="Нажимайте кнопки отправки и наблюдайте, как пакет летит через серверный хаб в режиме реального времени:" data-en="Dispatch test messages and inspect real-time WebSocket frame traversal across the simulated switch:">Ekranda xabar yuborish tugmasini bosing va paket server orqali boshqa klientga qanday yetib borishini jonli tomosha qiling:</p>

    <div class="grid c2" style="margin-top:14px; align-items:flex-start;">
      <!-- Interactive Terminal View -->
      <div class="card" style="padding:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span class="pill" style="background:var(--accent-soft); color:var(--accent-ink);" data-ru="Клиент 1 (Alice)" data-en="Client 1 (Alice)">Mijoz 1 (Alice)</span>
          <span id="deckWsStatus" style="font-size:11px; font-family:'JetBrains Mono',monospace; color:#34d399; font-weight:700;">● WS OPEN (101)</span>
        </div>
        
        <div id="deckChatBox" style="margin-top:12px; height:130px; overflow-y:auto; background:#0b1120; border:1px solid #1e293b; border-radius:8px; padding:10px; font-family:'JetBrains Mono',monospace; font-size:11px; color:#cbd5e1; display:flex; flex-direction:column; gap:4px;">
          <div style="color:#64748b;">// WebSocket ochiq: ws://127.0.0.1:8080/hub</div>
          <div><b style="color:#38bdf8;">Alice:</b> Salom Bob! LAN chat ishlayaptimi?</div>
          <div><b style="color:#34d399;">Bob:</b> Ha, 101 Handshake muvaffaqiyatli! Ping: 4ms</div>
        </div>

        <div style="margin-top:10px; display:flex; gap:6px;">
          <input type="text" id="deckMsgInput" value="Kiber-duelga tayyormisiz?" style="flex:1; padding:6px 10px; font-size:11px; background:#0f172a; border:1px solid #334155; border-radius:6px; color:#fff;" />
          <button class="btn" onclick="sendDeckWsMessage()" style="background:var(--accent); color:#fff; border-color:var(--accent); font-size:11px;" data-ru="⚡ Отправить (WS)" data-en="⚡ Send (WS)">⚡ Yuborish (WS)</button>
        </div>
      </div>

      <!-- Live Packet Inspector -->
      <div class="card">
        <h3 data-ru="Сниффер Пакетов (Frame Inspector)" data-en="Packet Sniffer (Frame Inspector)">Jonli Freymlar Tahlilchisi (Sniffer)</h3>
        <div style="margin-top:8px; display:flex; flex-direction:column; gap:6px;">
          <div style="font-size:11.5px; font-family:'JetBrains Mono',monospace; background:rgba(0,0,0,0.25); padding:8px; border-radius:6px; line-height:1.5;">
            <div>Status: <span style="color:var(--green); font-weight:700;">101 Switching Protocols</span></div>
            <div>Opcode: <span id="deckOpcode" style="color:var(--accent); font-weight:700;">0x1 (TEXT)</span></div>
            <div>Packets Dispatched: <span id="deckPktCount" style="color:#38bdf8; font-weight:700;">2</span></div>
            <div>Roundtrip Latency: <span id="deckLatency" style="color:var(--green); font-weight:700;">4 ms</span></div>
          </div>
          <div style="display:flex; gap:6px; margin-top:4px;">
            <button class="btn" onclick="sendDeckPing()" style="font-size:11px; padding:4px 8px;" data-ru="📡 Отправить Ping (0x9)" data-en="📡 Send Ping (0x9)">📡 Ping Yuborish (0x9)</button>
            <button class="btn" onclick="clearDeckChat()" style="font-size:11px; padding:4px 8px;" data-ru="🔄 Очистить" data-en="🔄 Clear">🔄 Tozalash</button>
          </div>
        </div>
      </div>
    </div>
  </section>""")

    # Slide 9: Interactive Quiz
    slides.append("""  <!-- SLIDE 9: QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Interactive Quiz" data-time="48:00–54:00">
    <div class="eyebrow" data-ru="ПРОВЕРКА ЗНАНИЙ (3 ВОПРОСА)" data-en="KNOWLEDGE CHECK (3 QUESTIONS)">INTERAKTIV QUIZ</div>
    <h2 data-ru="Блиц-Тест: WebSockets и Сетевые Протоколы" data-en="Fast Quiz: WebSockets & Network Protocols">Bilimni Sinash: WebSockets va Tarmoq Freymlari</h2>
    <div class="grid c3" style="margin-top:16px;">
      <!-- Q1 -->
      <div class="card quiz-card">
        <span class="pill" data-ru="Вопрос 1" data-en="Question 1">1-Savol</span>
        <h4 style="margin:10px 0;" data-ru="Какой HTTP статус подтверждает переход на WebSocket?" data-en="Which HTTP status confirms upgrading to WebSocket?">WebSocket ulanishini qaysi HTTP status tasdiqlaydi?</h4>
        <div style="display:flex; flex-direction:column; gap:6px; margin-top:8px;">
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="A) 200 OK" data-en="A) 200 OK">A) 200 OK</button>
          <button class="btn" onclick="checkDeckQuiz(this, true)" style="text-align:left; font-size:11.5px;" data-ru="B) 101 Switching Protocols" data-en="B) 101 Switching Protocols">B) 101 Switching Protocols</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="C) 404 Not Found" data-en="C) 404 Not Found">C) 404 Not Found</button>
        </div>
      </div>

      <!-- Q2 -->
      <div class="card quiz-card">
        <span class="pill" data-ru="Вопрос 2" data-en="Question 2">2-Savol</span>
        <h4 style="margin:10px 0;" data-ru="В чем главное преимущество WebSockets над Polling?" data-en="What is the key advantage of WebSockets over Polling?">WebSockets ning HTTP Polling dan asosiy ustunligi nima?</h4>
        <div style="display:flex; flex-direction:column; gap:6px; margin-top:8px;">
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="A) Он шифрует всё паролем" data-en="A) It encrypts with password">A) U parollarni shifrlaydi</button>
          <button class="btn" onclick="checkDeckQuiz(this, true)" style="text-align:left; font-size:11.5px;" data-ru="B) Постоянный дуплексный туннель без перезапросов" data-en="B) Persistent full-duplex tunnel with zero polling">B) Qayta so'rovsiz doimiy full-duplex tunnel</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="C) Работает без интернета" data-en="C) Works without internet">C) Internetsiz ham sayt ochadi</button>
        </div>
      </div>

      <!-- Q3 -->
      <div class="card quiz-card">
        <span class="pill" data-ru="Вопрос 3" data-en="Question 3">3-Savol</span>
        <h4 style="margin:10px 0;" data-ru="Какой Opcode используется для отправки JSON текста?" data-en="Which Opcode is used to transmit JSON text?">JSON xabarlari uchun qaysi Opcode ishlatiladi?</h4>
        <div style="display:flex; flex-direction:column; gap:6px; margin-top:8px;">
          <button class="btn" onclick="checkDeckQuiz(this, true)" style="text-align:left; font-size:11.5px;" data-ru="A) 0x1 (Text UTF-8)" data-en="A) 0x1 (Text UTF-8)">A) 0x1 (Text UTF-8)</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="B) 0x8 (Close)" data-en="B) 0x8 (Close)">B) 0x8 (Close)</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="C) 0x9 (Ping)" data-en="C) 0x9 (Ping)">C) 0x9 (Ping)</button>
        </div>
      </div>
    </div>
  </section>""")

    # Slide 10: 25-Min Practice Cyber Arena
    slides.append("""  <!-- SLIDE 10: ARENA LAB -->
  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="54:00–69:00">
    <div class="eyebrow" data-ru="БОЛЬШАЯ ПРАКТИЧЕСКАЯ АРЕНА (25 МИНУТ)" data-en="25-MINUTE CYBER ARENA">AMALIY ARENA</div>
    <h2 data-ru="Задание: Запусти LAN Чат и Поймай Пакеты Друга" data-en="Mission: Launch LAN Cyber Chat & Sniff Live Packets">Kiber-Missiya: LAN Chatni Ishga Tushir va Paketlarni Sniff Qil</h2>
    <p class="lede" data-ru="Откройте студию studio/index.html и выполните 3 практических шага за 25 минут:" data-en="Launch studio/index.html and accomplish 3 hands-on network milestones within 25 minutes:">Kompyuteringizda <b>studio/index.html</b> faylini oching va 25 daqiqada 3 ta tarmoq bosqichini bajaring:</p>
    
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Чек-лист Сетевого Инженера" data-en="Network Engineer Checklist">Muhandislik Bosqichlari</h3>
        <ol style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="Подключиться к сокет-хабу и отправить событие JOIN с вашим никнеймом" data-en="Connect to socket hub and dispatch JOIN event with your handle">Soket serveriga ulanish va o'z taxallusingiz bilan <code>JOIN</code> hodisasini uzatish</li>
          <li data-ru="Открыть Chrome DevTools -> Network -> WS и перехватить фрейм соседа" data-en="Open Chrome DevTools -> Network -> WS and intercept peer frames">Chrome DevTools -> Network -> WS orqali partadoshingizdan kelgan freymni ushlab olish</li>
          <li data-ru="Переключиться в комнату #red-team и протестировать изоляцию каналов" data-en="Switch into #red-team room and verify channel traffic isolation"><code>#red-team</code> xonasiga o'tib, xabarlar begonalarga ko'rinmasligini tekshirish!</li>
        </ol>
        <div style="margin-top:16px;">
          <a href="studio/index.html" target="_blank" class="btn" style="text-decoration:none; display:inline-flex; align-items:center; gap:8px; font-size:13px; font-weight:700; padding:10px 18px; background:var(--accent); color:#fff; border-color:var(--accent);" data-ru="🚀 Открыть Студию LAN Чата (studio/index.html)" data-en="🚀 Launch LAN Chat Studio (studio/index.html)">🚀 LAN Chat Studiyasini Ochish (studio/index.html)</a>
        </div>
      </div>

      <!-- Live 25-Min Timer Card -->
      <div class="card" style="text-align:center; padding:16px;">
        <span class="pill" data-ru="Таймер Лаборатории" data-en="Arena Timer">Arena Taymeri</span>
        <div id="deckTimerDisplay" style="font-family:'JetBrains Mono',monospace; font-size:44px; font-weight:800; color:var(--accent); margin:12px 0;">25:00</div>
        <div style="display:flex; justify-content:center; gap:8px;">
          <button class="btn" id="deckTimerBtn" onclick="toggleDeckTimer()" data-ru="▶ Старт (25 мин)" data-en="▶ Start (25m)">▶ Boshlash (25m)</button>
          <button class="btn" onclick="resetDeckTimer()" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta o'rnatish</button>
        </div>
        <div style="font-size:12px; color:var(--ink-2); margin-top:10px;" data-ru="Учитель проходит по рядам и помогает настроить сокеты" data-en="Teacher navigates floor assisting socket connections and sniffing">O'qituvchi sinf bo'ylab aylanib, xona filtri va paketlarni tekshirishda yordam beradi</div>
      </div>
    </div>
  </section>""")

    # Slide 11: Peer Review
    slides.append("""  <!-- SLIDE 11: PEER REVIEW -->
  <section class="slide" data-phase="Kiber-Audit|Код-Ревью|Peer Review" data-time="69:00–74:00">
    <div class="eyebrow" data-ru="ПАРНЫЙ СЕТЕВОЙ АУДИТ" data-en="PAIR NETWORK AUDIT">JUFTLIKDA PEER-REVIEW (KIBER-AUDIT)</div>
    <h2 data-ru="Обменяйтесь Экранами: Чек-лист из 4 Пунктов" data-en="Swap Screens: 4-Point Network Audit">Partadosh Bilan Almashing: 4 Bosqichli Tarmoq Auditi</h2>
    <p class="lede" data-ru="Инженерное правило: сетевой протокол считается надежным, только если напарник проверил безопасность и отсутствие утечек:" data-en="Engineering standard: network architecture is solid only when peer-reviewed against data leaks and edge cases:">Professional muhandislik qoidasi: sherigingiz tekshirmaguncha tarmoq kodi tayyor hisoblanmaydi. Partadoshingiz chatini sinang:</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Чек-лист Инспекции" data-en="Inspection Checklist">Tekshirish Mezonlari</h3>
        <ul style="margin-left:18px; line-height:2.0; font-size:13px; margin-top:8px;">
          <li data-ru="[ ] 101 Статус: Вкладка Network -> WS подтверждает успешный Handshake." data-en="[ ] 101 Status: Network -> WS confirms successful Handshake.">[ ] <b>101 Handshake:</b> Network -> WS darchasida 101 statusi qayd etilganmi?</li>
          <li data-ru="[ ] Broadcast без зависаний: Сообщения доходят до соседа мгновенно." data-en="[ ] Real-time Broadcast: Messages reach peer instantly without reload.">[ ] <b>Broadcast Tezligi:</b> Xabarlar partadoshingizga bir zumda yetib boryaptimi?</li>
          <li data-ru="[ ] Изоляция каналов: Чат из #red-team не просачивается в #general." data-en="[ ] Channel Isolation: Chats in #red-team do not leak into #general.">[ ] <b>Xonalar Maxfiyligi:</b> <code>#red-team</code> xabarlari begona xonalarga sizmayaptimi?</li>
          <li data-ru="[ ] Восстановление: При закрытии и повторном открытии сокет переподключается." data-en="[ ] Auto-Reconnect: Socket reconnects gracefully when connection toggles.">[ ] <b>Qayta Ulanish:</b> Aloqa uzilganda klient avtomatik qayta ulanadimi?</li>
        </ul>
      </div>

      <div class="card" style="display:flex; flex-direction:column; justify-content:center; text-align:center;">
        <div style="font-size:36px; margin-bottom:8px;">📡⚡💬</div>
        <h3 data-ru="Роль: Network Security Architect" data-en="Role: Network Security Architect">Siz Tarmoq Arxitektorsiz!</h3>
        <p style="font-size:12.5px; color:var(--ink-2); margin-top:6px;" data-ru="Если вы обнаружили, что сообщения из приватного канала утекают — помогите соседу поставить фильтр room!" data-en="If you discover private room messages leaking out — help your peer implement proper room filters!">Agar xabarlar boshqa xonalarga tarqalayotganini sezsangiz — partadoshingizga `msg.room === currentRoom` filtri qo'yishni o'rgating!</p>
      </div>
    </div>
  </section>""")

    # Slide 12: Showcase Demo
    slides.append("""  <!-- SLIDE 12: SHOWCASE DEMO -->
  <section class="slide" data-phase="Taqdimot|Демонстрация|Showcase Arena" data-time="74:00–77:00">
    <div class="eyebrow" data-ru="ДЕМОНСТРАЦИЯ ЧАТА НА ДОСКЕ" data-en="SMARTBOARD LIVE CHAT SHOWCASE">O'QUVCHILAR DEMOSI</div>
    <h2 data-ru="Презентация LAN Сети на Большом Экране" data-en="Smartboard LAN Network Showcase">Kiber-Showcase: Katta Ekranda Jonli Chat Demosi</h2>
    <p class="lede" data-ru="2 лучшие пары учеников подключаются к общему экрану и демонстрируют обмен пакетами между компьютерами:" data-en="Top 2 student pairs connect to the central screen and demonstrate real-time packet exchange live:">Eng tezkor 2 ta juftlik o'zlarining shaxsiy xonalarini va paketlar almashinuvini butun sinf oldida namoyish etadi:</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card" style="text-align:center; padding:20px;">
        <span class="pill" style="background:var(--accent-soft); color:var(--accent-ink);" data-ru="Демо 1" data-en="Demo 1">Demo 1</span>
        <h3 style="margin-top:10px;" data-ru="Мгновенный Broadcast" data-en="Instant Broadcast">Yashin Tezligidagi Broadcast</h3>
        <p style="font-size:12.5px; color:var(--ink-2);" data-ru="Показ доставки сообщения между двумя компьютерами за 3 миллисекунды." data-en="Demonstrate sub-3ms message delivery between two separate machines.">Ikki xil kompyuter o'rtasida 3 millisekundda xabar yetib borishini ko'rsatish.</p>
      </div>
      <div class="card" style="text-align:center; padding:20px;">
        <span class="pill" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Демо 2" data-en="Demo 2">Demo 2</span>
        <h3 style="margin-top:10px;" data-ru="Перехват Фреймов в DevTools" data-en="DevTools Frame Sniffing">DevTools Freymlar Sniffingi</h3>
        <p style="font-size:12.5px; color:var(--ink-2);" data-ru="Демонстрация зеленого входящего и белого исходящего фрейма в Chrome DevTools." data-en="Live demonstration of green incoming and white outgoing frames inside DevTools.">Chrome DevTools Network tabida yashil kiruvchi va oq chiquvchi freymlarni jonli namoyish etish.</p>
      </div>
    </div>
  </section>""")

    # Slide 13: 3-Tier Homework
    slides.append("""  <!-- SLIDE 13: HOMEWORK -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Tiered Homework" data-time="77:00–79:00">
    <div class="eyebrow" data-ru="ДОМАШНЕЕ ЗАДАНИЕ (10 БАЛЛОВ)" data-en="HOMEWORK ASSIGNMENT (10 POINTS)">MUSTAQIL AMALIYOT</div>
    <h2 data-ru="3 Уровня Домашнего Задания" data-en="3-Tiered Homework Assignment">10 Ballik Mezonli 3 Darajali Uy Vazifasi</h2>
    <p class="lede" data-ru="Задание выполняется в интерактивном приложении vazifa.html с автосохранением в браузере:" data-en="Complete your tasks inside the standalone vazifa.html app featuring local autosave:">Vazifa <b>vazifa.html</b> ilovasida bajariladi va brauzer xotirasida (LocalStorage) avtomatik saqlanadi:</p>

    <div class="grid c3" style="margin-top:20px;">
      <div class="card" style="border-top:3px solid var(--ink);">
        <span class="pill" data-ru="1-Уровень: База" data-en="Tier 1: Base">1-Bosqich: Baza</span>
        <div style="font-size:18px; font-weight:800; color:var(--accent); margin:6px 0;">4 BALL</div>
        <h3 data-ru="Клиент WebSocket" data-en="WebSocket Client">Toza WebSocket Klient</h3>
        <p data-ru="Создать подключение new WebSocket() с обработчиками onopen и onmessage." data-en="Construct new WebSocket() connection with onopen and onmessage listeners.">Brauzerda <code>new WebSocket()</code> ochuvchi va kelgan xabarlarni chiqaruvchi klient yozish.</p>
      </div>

      <div class="card" style="border-top:3px solid var(--accent);">
        <span class="pill" data-ru="2-Уровень: Проект" data-en="Tier 2: Engineering">2-Bosqich: Muhandislik</span>
        <div style="font-size:18px; font-weight:800; color:var(--accent); margin:6px 0;">4 BALL</div>
        <h3 data-ru="Роутер Комнат и Broadcast" data-en="Room Router & Broadcast">Xonalar Boyicha Broadcast</h3>
        <p data-ru="Написать серверную функцию рассылки с проверкой принадлежности к комнате." data-en="Author server broadcast router checking room recipient boundaries.">Xabarlarni faqat bitta xonadagi klientlarga tarqatuvchi server mantiqini yozish.</p>
      </div>

      <div class="card" style="border-top:3px solid var(--green);">
        <span class="pill" data-ru="3-Уровень: Вызов" data-en="Tier 3: Challenge">3-Bosqich: Kiber-Sinov</span>
        <div style="font-size:18px; font-weight:800; color:var(--green); margin:6px 0;">2 BALL</div>
        <h3 data-ru="Auto-Reconnect и Heartbeat" data-en="Auto-Reconnect & Heartbeat">Avto-Tiklanish & Ping</h3>
        <p data-ru="Реализовать повторное подключение при обрыве и замер времени пинга в миллисекундах." data-en="Implement exponential auto-reconnect on socket close and live ping tracker.">Aloqa uzilganda avtomatik qayta ulanish va real-vaqt ping o'lchagichini yaratish.</p>
      </div>
    </div>
  </section>""")

    # Slide 14: Summary & Bridge
    slides.append("""  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00">
    <div class="eyebrow" data-ru="ИТОГИ УРОКА И АНОНС 11 НЕДЕЛИ" data-en="LESSON SUMMARY & WEEK 11 TEASER">DARS XULOSASI VA KELGUSI QADAM</div>
    <h2 data-ru="WebSockets — Магистраль Интернета Реального Времени" data-en="WebSockets: Highway of the Real-Time Web">WebSockets — Zamonaviy Internetning Jonli Arteriyasi</h2>
    <p class="lede" data-ru="Сегодня мы навсегда попрощались с медленным HTTP Polling и перешли на молниеносные сокетные туннели!" data-en="Today we said farewell to sluggish HTTP polling and embraced lightning-speed full-duplex socket tunnels!">Bugun biz eskirgan HTTP Polling kechikishlaridan qutulib, barcha zamonaviy chatlar va multiplayer o'yinlar ishlatadigan toza WebSockets ga o'tdik!</p>

    <div class="grid c2" style="margin-top:20px;">
      <div class="card">
        <h3 data-ru="Что мы освоили сегодня" data-en="Today's Milestones">Bugungi Yutuqlarimiz</h3>
        <ul style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="Изучили 101 Switching Protocols и рукопожатие Upgrade: websocket." data-en="Mastered HTTP 101 Switching Protocols and Upgrade: websocket handshake.">101 Switching Protocols va `Upgrade: websocket` orqali doimiy tunnel ochishni o'rgandik.</li>
          <li data-ru="Освоили коды операций Opcodes (0x1 Text, 0x8 Close, 0x9 Ping) и сниффинг в DevTools." data-en="Understood Opcodes (0x1 Text, 0x8 Close, 0x9 Ping) and live DevTools frame sniffing.">Opcodes turlari (0x1 Text, 0x8 Close, 0x9 Ping) va DevTools orqali freymlarni tutishni o'zlashtirdik.</li>
          <li data-ru="Создали живой чат с комнатами и серверным широковещанием (Broadcast)." data-en="Engineered live room-based chat with server-side broadcast distribution.">Serverda Broadcast tarqatish va shaxsiy xonalar arxitekturasi qurdik.</li>
        </ul>
      </div>

      <div class="card" style="background:#00214a; color:#fff;">
        <span class="pill" style="background:var(--accent); color:#fff;" data-ru="Анонс 11 Недели" data-en="Week 11 Preview">Keyingi 11-Haftada</span>
        <h3 style="color:#fff; margin-top:8px;" data-ru="WebRTC и Peer-to-Peer Стриминг" data-en="WebRTC & Peer-to-Peer Streaming">WebRTC va Peer-to-Peer Oqimlari</h3>
        <p style="font-size:12.5px; color:#cbd5e1; margin-top:6px;" data-ru="Мы научим компьютеры обмениваться голосовыми и видеопотоками напрямую без участия центрального сервера!" data-en="We will connect browsers directly peer-to-peer exchanging live voice and video streams with zero middleman servers!">Biz kompyuterlarni markaziy serversiz, to'g'ridan-to'g'ri bir-biriga bog'lab (P2P), ovoz va video almashinuvchi <b>WebRTC</b> tizimini o'rganamiz!</p>
      </div>
    </div>
  </section>""")

    # Inject slides into presentation
    all_slides_html = "\n\n".join(slides)
    tpl = re.sub(r'<div class="stage">[\s\S]*?</div><!-- /stage -->', f'<div class="stage">\n{all_slides_html}\n</div><!-- /stage -->', tpl)

    # Teacher notes
    notes = {
        "uz": [
            ["Darsga Kirish", "9-sinflar bilan 30-darsga xush kelibsiz. Discord, Telegram va online o'yinlar qanday ishlashini e'lon qiling.", "Doskaga telefon va o'yin kontrolleri belgisini chizing."],
            ["Uy Vazifasi Tahlili", "29-darsdagi asinxronlikni eslang. setInterval orqali serverni bombardimon qilish xatosini ko'rsating.", "30 soniyalik blits savolni bering."],
            ["Muammo: Nega HTTP Sekin?", "HTTP request-response nega online o'yinlarda 1 soniyalik lag keltirib chiqarishini tushuntiring.", "Ortiqcha 1 KB sarlavhalar va C10K muammosini ayting."],
            ["WebSockets Konsepti", "101 Switching Protocols handshake jarayonini doskada chizing.", "Full-duplex ochiq tunnel qanday ishlashini tushuntiring."],
            ["Freymlar va DevTools", "Chrome DevTools -> Network -> WS orqali freymlarni sniffer qilishni ko'rsating.", "0x1 Text, 0x8 Close, 0x9 Ping opcodelarini tushuntiring."],
            ["Server Arxitekturasi", "Node.js ws kutubxonasi va wss.clients.forEach broadcast tsiklini tushuntiring.", "Xonalar (#red-team vs #blue-team) xavfsizligini ta'kidlang."],
            ["Brauzer Klienti", "new WebSocket() obyekti va onopen, onmessage, onclose hodisalarini ko'rsating.", "Tarmoq uzilganda auto-reconnect qoidasini tushuntiring."],
            ["Jonli Simulyator", "Smartboardda Alice va Bob terminallaridan paket jo'natib ko'rsating.", "O'quvchilarni ekranga chaqirib Ping tugmasini bostiring."],
            ["Interaktiv Kiber-Quiz", "3 ta savol bo'yicha blits o'tkazing va to'g'ri javoblarni ekranda belgilang.", "Natijalarni mustahkamlang."],
            ["25 Minutlik Kiber-Arena", "O'quvchilar studio/index.html da chatni ochadilar. 25 daqiqalik taymerni yoqing.", "Sinf bo'ylab aylanib har bir juftlikka partadoshining paketini tutishda yordam bering."],
            ["Juftlikda Peer-Review", "O'quvchilar partadoshining ekranini 4 ta qoida bo'yicha audit qiladilar.", "Xabarlar begona xonalarga sizmayotganini tekshirsinlar."],
            ["O'quvchilar Demosi", "2 ta juftlik doskaga chiqib o'zaro chat xabarlarini va freymlar snifferini ko'rsatadi.", "Tezkor va toza ishlarni olqishlang."],
            ["3 Darajali Uy Vazifasi", "vazifa.html ilovasidagi 10 ballik mezonni tushuntiring. Local auto-save borligini eslating.", "O'quvchilarga vazifa formatini tushuntiring."],
            ["Dars Xulosasi", "11-haftadagi WebRTC va Peer-to-Peer mavzusini anons qiling.", "Faol o'quvchilarni baholang."]
        ],
        "ru": [
            ["Введение в Урок", "Приветствие 9-го класса на 30-м уроке. Анонсируйте устройство Discord, Telegram и онлайн-игр.", "Нарисуйте схему смартфона и игрового сервера."],
            ["Разбор ДЗ", "Вспомните асинхронность 29-го урока. Покажите фатальную ошибку опроса сервера через setInterval.", "Задайте 30-секундный блиц-вопрос."],
            ["Проблема HTTP", "Почему модель HTTP запрос-ответ создает секундный лаг в играх и чатах.", "Объясните накладные расходы заголовков и проблему C10K."],
            ["Концепт WebSockets", "Нарисуйте рукопожатие 101 Switching Protocols на доске.", "Объясните полнодуплексный режим постоянного сокета."],
            ["Фреймы и DevTools", "Покажите вкладку Chrome DevTools -> Network -> WS для сниффинга фреймов.", "Разберите коды операций: 0x1 Text, 0x8 Close, 0x9 Ping."],
            ["Серверный Движок", "Объясните сервер на библиотеке ws и цикл рассылки wss.clients.forEach.", "Подчеркните изоляцию комнат #red-team и #blue-team."],
            ["Клиент Браузера", "Покажите нативный объект new WebSocket() и события onopen, onmessage, onclose.", "Объясните механизм авто-переподключения."],
            ["Живой Демо-Тренажер", "Отправляйте пакеты между Alice и Bob на смартборде.", "Вызовите учеников проверить замер пинга на экране."],
            ["Интерактивный Квиз", "Проведите блиц по 3 вопросам и закрепите статус 101 и опкоды.", "Нажимайте варианты ответов на экране."],
            ["Практическая Арена", "Ученики открывают studio/index.html. Запустите 25-минутный таймер.", "Помогайте парам учеников перехватывать фреймы соседа."],
            ["Парный Аудит", "Ученики меняются экранами и проверяют сокеты по 4 критериям.", "Проверьте отсутствие утечек между комнатами."],
            ["Демонстрация Работ", "2 пары выходят к доске и показывают обмен сообщениями и сниффер в DevTools.", "Похвалите лучшие сетевые решения."],
            ["Домашнее Задание 10 Баллов", "Разберите 10-балльную рубрику в vazifa.html и напомните об автосохранении.", "Покажите интерфейс приложения."],
            ["Итоги и Анонс 11 Недели", "Анонсируйте тему 11-й недели — WebRTC и одноранговые P2P сети.", "Выставите оценки за занятие."]
        ],
        "en": [
            ["Lesson Introduction", "Welcome 9th graders to Lesson 30. Introduce the real-time engineering behind Discord, Telegram, and multiplayer gaming.", "Illustrate client-server live socket on board."],
            ["Homework Review", "Revisit async patterns from Lesson 29. Expose the server-crashing pitfall of HTTP polling intervals.", "Prompt 30-second blitz question."],
            ["The HTTP Bottleneck", "Explain why HTTP request-response triggers fatal latency in competitive games and chats.", "Discuss 1KB header bloat and the C10K concurrency crisis."],
            ["WebSockets Concept", "Draw the 101 Switching Protocols handshake flow on the board.", "Explain full-duplex persistent TCP tunneling."],
            ["Frames & DevTools", "Demonstrate frame sniffing inside Chrome DevTools -> Network -> WS tab.", "Break down Opcodes: 0x1 Text, 0x8 Close, 0x9 Ping."],
            ["Server Architecture", "Explain Node.js ws server implementation and wss.clients.forEach broadcast loops.", "Highlight channel isolation for #red-team and #blue-team."],
            ["Browser Client", "Inspect native new WebSocket() and its onopen, onmessage, and onclose lifecycle.", "Explain exponential backoff auto-reconnect logic."],
            ["In-Deck Live Simulator", "Transmit live frames between Alice and Bob terminals on the smartboard.", "Invite students to test roundtrip ping latency."],
            ["Interactive Cyber Quiz", "Run rapid blitz check on 3 questions to solidify protocol principles.", "Click quiz choices on smartboard."],
            ["25-Min Cyber Arena", "Students launch studio/index.html. Start 25-min timer.", "Guide student pairs across the room intercepting peer frames."],
            ["Peer Review Quality Audit", "Students swap screens auditing socket code across 4 checkpoints.", "Verify robust channel scoping and graceful reconnects."],
            ["Student Showcase Arena", "2 student pairs take the smartboard demonstrating live chat and DevTools sniffing.", "Celebrate clean network engineering."],
            ["Tiered Homework Rubric", "Explain 10-point rubric in vazifa.html and highlight local autosave in browser.", "Preview homework web application."],
            ["Summary & Week 11 Teaser", "Tease Week 11 topic — WebRTC & Peer-to-Peer Voice/Video Streaming.", "Record student achievements."]
        ]
    }
    notes_json = json.dumps(notes, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    # In-Deck Simulator & Timer scripts
    demo_js = """
// ============================================================
// IN-DECK INTERACTIVE SIMULATOR (Slide 8: WebSockets)
// ============================================================
var deckPktCount = 2;

function sendDeckWsMessage() {
  var input = document.getElementById("deckMsgInput");
  var text = input ? input.value.trim() : "";
  if (!text) return;

  var box = document.getElementById("deckChatBox");
  deckPktCount++;
  var countEl = document.getElementById("deckPktCount");
  if (countEl) countEl.textContent = deckPktCount;

  var opEl = document.getElementById("deckOpcode");
  if (opEl) opEl.textContent = "0x1 (TEXT)";

  if (box) {
    var outDiv = document.createElement("div");
    outDiv.innerHTML = '<b style="color:#38bdf8;">Alice (⬆ WS):</b> ' + escapeHtml(text);
    box.appendChild(outDiv);

    setTimeout(function() {
      deckPktCount++;
      if (countEl) countEl.textContent = deckPktCount;
      var inDiv = document.createElement("div");
      inDiv.innerHTML = '<b style="color:#34d399;">Bob (⬇ WS):</b> [ACK] Qabul qilindi (' + Math.floor(Math.random() * 5 + 2) + 'ms)';
      box.appendChild(inDiv);
      box.scrollTop = box.scrollHeight;
    }, 180);

    box.scrollTop = box.scrollHeight;
  }
  if (input) input.value = "";
}

function sendDeckPing() {
  var box = document.getElementById("deckChatBox");
  var opEl = document.getElementById("deckOpcode");
  var latEl = document.getElementById("deckLatency");
  deckPktCount += 2;
  var countEl = document.getElementById("deckPktCount");
  if (countEl) countEl.textContent = deckPktCount;

  if (opEl) opEl.textContent = "0x9 (PING)";
  var ms = Math.floor(Math.random() * 4 + 2);
  if (latEl) latEl.textContent = ms + " ms";

  if (box) {
    var pDiv = document.createElement("div");
    pDiv.style.color = "#fbbf24";
    pDiv.textContent = "📡 Ping (0x9) -> Server -> Pong (0xA) ACK (" + ms + " ms)";
    box.appendChild(pDiv);
    box.scrollTop = box.scrollHeight;
  }
}

function clearDeckChat() {
  var box = document.getElementById("deckChatBox");
  if (box) {
    box.innerHTML = '<div style="color:#64748b;">// WebSocket toza: ws://127.0.0.1:8080/hub</div>';
  }
}

function escapeHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// 25-Min Arena Timer
var deckTimerSec = 25 * 60;
var deckTimerInterval = null;

function toggleDeckTimer() {
  var btn = document.getElementById("deckTimerBtn");
  if (deckTimerInterval) {
    clearInterval(deckTimerInterval);
    deckTimerInterval = null;
    if (btn) btn.textContent = "▶ Davom etish";
  } else {
    deckTimerInterval = setInterval(function() {
      if (deckTimerSec > 0) {
        deckTimerSec--;
        var m = Math.floor(deckTimerSec / 60);
        var s = deckTimerSec % 60;
        var disp = document.getElementById("deckTimerDisplay");
        if (disp) disp.textContent = (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s);
      } else {
        clearInterval(deckTimerInterval);
        deckTimerInterval = null;
        alert("⏰ 25-Minutlik Kiber-Arena vaqti yakunlandi! Kodni peer-review qilishga o'ting.");
      }
    }, 1000);
    if (btn) btn.textContent = "⏸ Pauza";
  }
}

function resetDeckTimer() {
  if (deckTimerInterval) {
    clearInterval(deckTimerInterval);
    deckTimerInterval = null;
  }
  deckTimerSec = 25 * 60;
  var disp = document.getElementById("deckTimerDisplay");
  if (disp) disp.textContent = "25:00";
  var btn = document.getElementById("deckTimerBtn");
  if (btn) btn.textContent = "▶ Boshlash (25m)";
}

function checkDeckQuiz(btn, isCorrect) {
  var parent = btn.parentElement;
  var btns = parent.querySelectorAll("button");
  btns.forEach(function(b) {
    b.disabled = true;
    b.style.opacity = "0.7";
  });
  btn.style.opacity = "1";
  if (isCorrect) {
    btn.style.background = "var(--green)";
    btn.style.color = "#fff";
    btn.style.borderColor = "var(--green)";
  } else {
    btn.style.background = "var(--accent)";
    btn.style.color = "#fff";
    btn.style.borderColor = "var(--accent)";
  }
}
"""
    tpl = tpl.replace("</script>\n</body>", f"{demo_js}\n</script>\n</body>")

    with open(os.path.join(LESSON_DIR, "prezentatsiya.html"), "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

    # ============================================================
    # 2. VARAQA.HTML (Printable A4 Worksheet)
    # ============================================================
    v_tpl = TPL_VAR
    v_tpl = v_tpl.replace("{{LESSON_NUM}}", "30")
    v_tpl = v_tpl.replace("{{TITLE_UZ}}", "Real-Vaqt Texnologiyalari: WebSockets va LAN Kiber-Chat")
    v_tpl = v_tpl.replace("{{TITLE_RU}}", "Технологии Реального Времени: WebSockets и LAN Кибер-Чат")
    v_tpl = v_tpl.replace("{{TITLE_EN}}", "Real-Time Technologies: WebSockets & LAN Cyber Chat")
    v_tpl = v_tpl.replace("{{SUBTITLE_UZ}}", "HTTP Polling qopqoni, 101 Switching Protocols, doimiy full-duplex TCP tunnel va Chrome DevTools paket snifferi")
    v_tpl = v_tpl.replace("{{SUBTITLE_RU}}", "Ловушка HTTP Polling, 101 Switching Protocols, полнодуплексный TCP туннель и сниффер пакетов в DevTools")
    v_tpl = v_tpl.replace("{{SUBTITLE_EN}}", "HTTP Polling bottleneck, 101 Switching Protocols, full-duplex TCP tunneling, and Chrome DevTools frame sniffing")

    v_tpl = v_tpl.replace("{{SEC1_TITLE_UZ}}", "1-Qism: HTTP Polling vs WebSockets Taqqoslash Matritsasi")
    v_tpl = v_tpl.replace("{{SEC1_TITLE_RU}}", "Часть 1: Сравнительная Матрица HTTP Polling и WebSockets")
    v_tpl = v_tpl.replace("{{SEC1_TITLE_EN}}", "Part 1: HTTP Polling vs WebSockets Architecture Matrix")
    v_sec1 = """    <p data-ru="Заполните фундаментальные различия между протоколами передачи данных в реальном времени:" data-en="Analyze the structural divergence between real-time networking protocols:">Real-vaqt rejimida ma'lumot uzatishning 2 xil modeli o'rtasidagi farqlarni tahlil qiling va jadvalni to'ldiring:</p>
    <div class="box" style="margin-top:6px;">
      <table style="width:100%; border-collapse:collapse; font-size:8.5pt;">
        <thead>
          <tr style="border-bottom:1px solid var(--rule); text-align:left;">
            <th style="padding:4px 6px;" data-ru="Критерий" data-en="Metric">Mezon</th>
            <th style="padding:4px 6px;" data-ru="HTTP Polling (Опрос)" data-en="HTTP Polling">HTTP Polling (Eski usul)</th>
            <th style="padding:4px 6px;" data-ru="WebSockets (ws://)" data-en="WebSockets (ws://)">WebSockets (Doimiy tunnel)</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;" data-ru="Модель связи" data-en="Connection Model"><b>Ulanish modeli</b></td>
            <td style="padding:4px 6px;" data-ru="Запрос-ответ (Request-Response)" data-en="Request-Response">So'rov-javob (har safar yangi TCP)</td>
            <td style="padding:4px 6px;" data-ru="Полнодуплексный двусторонний туннель" data-en="Full-Duplex persistent tunnel">Doimiy 1 ta ochiq TCP tunnel</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;" data-ru="Накладные расходы" data-en="Header Overhead"><b>Sarlavha hajmi</b></td>
            <td style="padding:4px 6px;" data-ru="~1000 байт на каждый запрос" data-en="~1,000 bytes per request">~1000 bayt (katta sarlavhalar)</td>
            <td style="padding:4px 6px;" data-ru="2-8 байт на каждый фрейм" data-en="2-8 bytes per frame">Atigi 2–6 bayt freym sarlavhasi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;" data-ru="Средний лаг" data-en="Average Latency"><b>Kechikish (Latency)</b></td>
            <td style="padding:4px 6px;" data-ru="1000 - 3000 мс (задержка опроса)" data-en="1,000 - 3,000 ms lag">1000–3000 ms (lag seziladi)</td>
            <td style="padding:4px 6px;" data-ru="2 - 10 мс (мгновенно)" data-en="2 - 10 ms (instant)">2–10 ms (bir zumda yetib boradi)</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;" data-ru="Инициатор отправки" data-en="Push Originator"><b>Serverdan Push</b></td>
            <td style="padding:4px 6px;" data-ru="Невозможно (только клиент)" data-en="Impossible (client only)">Mumkin emas (faqat mijoz so'raydi)</td>
            <td style="padding:4px 6px;" data-ru="Сервер может слать в любой момент" data-en="Server pushes anytime">Server istalgan soniyada uzata oladi</td>
          </tr>
        </tbody>
      </table>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC1_CONTENT}}", v_sec1)

    v_tpl = v_tpl.replace("{{SEC2_TITLE_UZ}}", "2-Qism: Kod Tahlili — Xavfsiz WebSocket Broadcast Serveri")
    v_tpl = v_tpl.replace("{{SEC2_TITLE_RU}}", "Часть 2: Анализ Кода — Безопасный WebSocket Broadcast Сервер")
    v_tpl = v_tpl.replace("{{SEC2_TITLE_EN}}", "Part 2: Code Analysis — Resilient WebSocket Broadcast Engine")
    v_sec2 = """    <div class="code-snippet">// ⚠️ Kodni to'g'rilang: Yopiq soketga yozib serverni qulatish xatosini bartaraf eting va xona filtrini qo'ying:
wss.on('connection', (socket) => {
  socket.on('message', (raw) => {
    const msg = JSON.parse(raw);
    wss.clients.forEach((client) => {
      // ❌ XATO: client.send(raw) — yopiq klient bo'lsa server crash bo'ladi!
      // ✅ TO'G'RI: Faqat ochiq va bir xil xonadagi mijozlarga jo'natish:
      if (client.readyState === ________________________ && client.room === ________________________) {
        client.send(JSON.stringify(msg));
      }
    });
  });
});</div>
    <p style="margin-top:4px;" data-ru="Запишите правильное условие проверки soket holati и xona mosligi:" data-en="Fill in safe readyState check and room boundary match:">Bo'sh joylarga to'g'ri `readyState` holati va xonani tekshirish shartini yozing:</p>
    <div class="write-line"></div>"""
    v_tpl = v_tpl.replace("{{SEC2_CONTENT}}", v_sec2)

    v_tpl = v_tpl.replace("{{SEC3_TITLE_UZ}}", "3-Qism: Amaliy Laboratoriya (Chrome DevTools WS Sniffer)")
    v_tpl = v_tpl.replace("{{SEC3_TITLE_RU}}", "Часть 3: Практическая Лаборатория (Сниффер WS в Chrome DevTools)")
    v_tpl = v_tpl.replace("{{SEC3_TITLE_EN}}", "Part 3: Hands-on Lab (Chrome DevTools WS Sniffer Table)")
    v_sec3 = """    <p data-ru="Откройте DevTools -> Network -> WS, перехватите 4 типа фреймов и заполните аудит:" data-en="Launch DevTools -> Network -> WS, intercept 4 frame types, and complete the packet log:"><b>studio/index.html</b> da xabar yuborib, Chrome DevTools Network oynasida freymlarni tahlil qiling:</p>
    <div class="box" style="margin-top:6px;">
      <table style="width:100%; border-collapse:collapse; font-size:8.5pt;">
        <thead>
          <tr style="border-bottom:1px solid var(--rule); text-align:left;">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Событие" data-en="Network Event">Harakat</th>
            <th style="padding:4px 6px;" data-ru="Направление" data-en="Direction">Yo'nalish</th>
            <th style="padding:4px 6px;" data-ru="Opcode / Тип" data-en="Opcode / Type">Opcode Turi</th>
            <th style="padding:4px 6px;" data-ru="Статус / Размер" data-en="Status / Size">Holat / Hajmi</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="Handshake рукопожатие" data-en="Handshake negotiation">HTTP Upgrade Handshake</td>
            <td style="padding:4px 6px;" data-ru="Клиент ➔ Сервер" data-en="Client ➔ Server">Mijoz ➔ Server</td>
            <td style="padding:4px 6px;" data-ru="HTTP 101 Switching Protocols" data-en="HTTP 101 Switching Protocols"><code>HTTP 101</code></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] OK" data-en="[ &nbsp; ] OK">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="Чат-сообщение JSON" data-en="JSON chat payload">JSON Chat Xabari</td>
            <td style="padding:4px 6px;" data-ru="Исходящий (⬆)" data-en="Outgoing (⬆)">Chiquvchi (⬆)</td>
            <td style="padding:4px 6px;" data-ru="0x1 (Text UTF-8)" data-en="0x1 (Text UTF-8)"><code>0x1 (Text)</code></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] OK" data-en="[ &nbsp; ] OK">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="Heartbeat Ping" data-en="Heartbeat Ping">Tarmoq Pingi (Heartbeat)</td>
            <td style="padding:4px 6px;" data-ru="Двусторонний" data-en="Bidirectional">Ikki tomonlama</td>
            <td style="padding:4px 6px;" data-ru="0x9 Ping / 0xA Pong" data-en="0x9 Ping / 0xA Pong"><code>0x9 / 0xA</code></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] OK" data-en="[ &nbsp; ] OK">[ &nbsp; ] OK</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="Закрытие вкладки" data-en="Tab Disconnect">Aloqani uzish (Disconnect)</td>
            <td style="padding:4px 6px;" data-ru="Клиент ➔ Сервер" data-en="Client ➔ Server">Mijoz ➔ Server</td>
            <td style="padding:4px 6px;" data-ru="0x8 (Close Frame)" data-en="0x8 (Close Frame)"><code>0x8 (Close)</code></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] OK" data-en="[ &nbsp; ] OK">[ &nbsp; ] OK</td>
          </tr>
        </tbody>
      </table>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC3_CONTENT}}", v_sec3)

    v_sec4 = """    <div class="box-grid" style="margin-top:6px;">
      <div class="box">
        <h4 data-ru="1-Уровень: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</h4>
        <p data-ru="Подключиться к WebSocket, обработать onopen и отправить JSON с типом JOIN." data-en="Establish WebSocket connection, handle onopen, and dispatch JSON JOIN event.">WebSocket ochish, onopen hodisasida o'z ismini yuborish va kelgan xabarlarni chiqarish.</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="2-Уровень: Проект (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Amaliyot (4 ball)</h4>
        <p data-ru="Реализовать фильтрацию по комнатам (#general, #red-team) в цикле рассылки." data-en="Implement channel filtering logic across broadcast loop boundaries.">Serverda xabarlarni faqat bitta xonadagi o'quvchilarga tarqatuvchi filtr yozish.</p>
        <div class="write-line"></div>
      </div>
    </div>
    <div class="box" style="margin-top:6px;">
      <h4 data-ru="3-Уровень: Кибер-Вызов (2 балла)" data-en="Tier 3: Cyber Challenge (2 pts)">3-Daraja: Kiber-Chaqiruv (2 ball)</h4>
      <p data-ru="Реализовать auto-reconnect при обрыве соединения и таймер замера пинга (ms)." data-en="Engineer resilient auto-reconnect backoff on socket close and live ping tracker.">Tarmoq uzilganda avtomatik qayta ulanuvchi (Auto-reconnect) va ping hisoblagich yozish.</p>
      <div class="write-line"></div>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC4_CONTENT}}", v_sec4)

    with open(os.path.join(LESSON_DIR, "varaqa.html"), "w", encoding="utf-8") as f:
        f.write(v_tpl)
    print("  ✓ Created: varaqa.html")

    # ============================================================
    # 3. VAZIFA.HTML (Interactive Homework App)
    # ============================================================
    vz_tpl = TPL_VAZ
    vz_tpl = vz_tpl.replace("{{TITLE_UZ}}", "30-dars: Real-Vaqt Texnologiyalari: WebSockets va LAN Kiber-Chat")
    vz_tpl = vz_tpl.replace("{{TITLE_RU}}", "Урок 30: Технологии Реального Времени: WebSockets и LAN Кибер-Чат")
    vz_tpl = vz_tpl.replace("{{TITLE_EN}}", "Lesson 30: Real-Time Technologies: WebSockets & LAN Cyber Chat")
    vz_tpl = vz_tpl.replace("{{LESSON_SLUG}}", "9-w10-l30-websockets-lan-chat")
    vz_tpl = vz_tpl.replace("{{COHORT_LABEL_UZ}}", "9-SINF · 10-HAFTA")
    vz_tpl = vz_tpl.replace("{{HERO_TAG_UZ}}", "TARMOQ MUHANDISLIGI & JONLI SOKETLAR")
    vz_tpl = vz_tpl.replace("{{HERO_DESC_UZ}}", "HTTP Polling qopqonidan qutulish, 101 Handshake, doimiy full-duplex TCP soketlar va real-vaqt xabarlar marshrutlash bo'yicha 3 darajali topshiriqlarni bajaring.")
    vz_tpl = vz_tpl.replace("{{HERO_DESC_RU}}", "Выполните 3 уровня задач по преодолению ловушки HTTP Polling, рукопожатию 101 Handshake, постоянным TCP сокетам и маршрутизации сообщений.")
    vz_tpl = vz_tpl.replace("{{HERO_DESC_EN}}", "Complete 3 challenge tiers overcoming HTTP polling bottlenecks, mastering 101 Handshakes, full-duplex TCP socket tunnels, and broadcast routing.")

    vz_tpl = vz_tpl.replace("{{RUBRIC_T1_UZ}}", "WebSocket klienti va xabarlarni qabul qilish (4 ball)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T1_RU}}", "Реализация WebSocket клиента и прием сообщений (4 балла)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T1_EN}}", "Authoring WebSocket client with onmessage handling (4 pts)")

    vz_tpl = vz_tpl.replace("{{RUBRIC_T2_UZ}}", "Xonalar (#red-team) bo'yicha xavfsiz broadcast tarqatish (4 ball)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T2_RU}}", "Широковещательная рассылка с фильтрацией комнат (4 балла)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T2_EN}}", "Room-scoped broadcast router with channel isolation (4 pts)")

    vz_tpl = vz_tpl.replace("{{RUBRIC_T3_UZ}}", "Avto-qayta ulanish (Auto-reconnect) va ping hisoblagich (2 ball)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T3_RU}}", "Авто-переподключение при обрыве и замер пинга (2 балла)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T3_EN}}", "Resilient exponential auto-reconnect and ping tracker (2 pts)")

    tasks_9 = """  <!-- TASK 1 -->
  <article class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="1-Уровень: База" data-en="Tier 1: Base">1-Bosqich: Baza</span>
      <span class="task-score">4 BALL</span>
    </div>
    <h3 data-ru="Создание Клиента createChatClient(url, user)" data-en="Authoring createChatClient(url, user)">createChatClient(url, user) Klientini Yozish</h3>
    <p data-ru="Напишите функцию createChatClient(url, user, onMessageCallback), которая открывает new WebSocket(url), отправляет JOIN пакет при подключении и парсит входящие JSON сообщения в onmessage:" data-en="Write a function createChatClient(url, user, onMessageCallback) opening new WebSocket(url), dispatching a JOIN packet on open, and parsing incoming JSON in onmessage:"><code>new WebSocket(url)</code> ochuvchi, <code>onopen</code> bo'lganda <code>{ type: "JOIN", user }</code> xabarini yuboruvchi va kelgan JSON xabarlarni qayta ishlovchi funksiya yozing:</p>
    <div class="code-box">// Kutilayotgan funksiya:
function createChatClient(url, user, onMessageCallback) {
  const ws = new WebSocket(url);
  // 1. ws.onopen: send JOIN JSON
  // 2. ws.onmessage: JSON.parse(e.data) va callback chaqirish
  // 3. send(text) metodi bilan ws obyektini qaytarish
}</div>
    <textarea class="answer-area" id="ans_task_1" rows="7" placeholder="JavaScript kodingizni bu yerga yozing..." data-placeholder-ru="Напишите ваш JavaScript код здесь..." data-placeholder-en="Write your JavaScript code here..." oninput="saveAnswers()"></textarea>
    <div style="margin-top:12px;">
      <button class="btn btn-outline teacher-solution-only" onclick="toggleSolution('sol_1')" data-ru="🔒 Эталон Решения (Учитель)" data-en="🔒 Solution (Teacher)">🔒 Etalon Yechim (O'qituvchi)</button>
      <div class="solution-box teacher-solution-only" id="sol_1" hidden>
        <h4 data-ru="✅ Эталонная Функция Клиента" data-en="✅ Reference Client Function">✅ Etalon Yechim</h4>
        <pre><code>export function createChatClient(url, user, onMessageCallback) {
  const ws = new WebSocket(url);
  ws.onopen = () => {
    ws.send(JSON.stringify({ type: "JOIN", user }));
  };
  ws.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data);
      if (onMessageCallback) onMessageCallback(data);
    } catch (e) {
      console.error("Invalid JSON frame:", e);
    }
  };
  return {
    send: (text, room = "general") => {
      if (ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify({ type: "CHAT", user, text, room }));
      }
    },
    close: () => ws.close()
  };
}</code></pre>
      </div>
    </div>
  </article>

  <!-- TASK 2 -->
  <article class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="2-Уровень: Проект" data-en="Tier 2: Engineering">2-Bosqich: Muhandislik</span>
      <span class="task-score">4 BALL</span>
    </div>
    <h3 data-ru="Серверный Broadcast Роутер с Комнатами" data-en="Server Broadcast Router with Channel Scoping">Xonalar Bo'yicha Xavfsiz Broadcast Tarqatish</h3>
    <p data-ru="Напишите функцию broadcastToRoom(clients, senderSocket, messageJson), которая отправляет сообщение только тем клиентам, у которых readyState === OPEN и client.room === messageJson.room. Отправителю обратно сообщение слать не нужно:" data-en="Write a function broadcastToRoom(clients, senderSocket, messageJson) dispatching payloads strictly to open sockets belonging to the target room. Exclude the original sender:">Xabarni faqat <code>readyState === WebSocket.OPEN</code> va <code>client.room === messageJson.room</code> bo'lgan mijozlarga tarqatuvchi, xabarni yuborgan klientning o'ziga qaytarib yubormaydigan <code>broadcastToRoom</code> funksiyasini yozing:</p>
    <div class="code-box">function broadcastToRoom(clients, senderSocket, messageJson) {
  const payload = JSON.stringify(messageJson);
  // clients.forEach loop:
  // Faqat ochiq va bir xil xonadagi mijozlarga yuborish!
}</div>
    <textarea class="answer-area" id="ans_task_2" rows="8" placeholder="Broadcast router kodini bu yerga yozing..." data-placeholder-ru="Напишите код роутера здесь..." data-placeholder-en="Write router code here..." oninput="saveAnswers()"></textarea>
    <div style="margin-top:12px;">
      <button class="btn btn-outline teacher-solution-only" onclick="toggleSolution('sol_2')" data-ru="🔒 Эталон Решения (Учитель)" data-en="🔒 Solution (Teacher)">🔒 Etalon Yechim (O'qituvchi)</button>
      <div class="solution-box teacher-solution-only" id="sol_2" hidden>
        <h4 data-ru="✅ Эталонный Broadcast Роутер" data-en="✅ Reference Broadcast Router">✅ Etalon Yechim</h4>
        <pre><code>export function broadcastToRoom(clients, senderSocket, messageJson) {
  const payload = JSON.stringify(messageJson);
  clients.forEach((client) => {
    const isOpen = client.readyState === 1; // WebSocket.OPEN
    const isSameRoom = client.room === messageJson.room;
    const isNotSender = client !== senderSocket;
    
    if (isOpen && isSameRoom && isNotSender) {
      client.send(payload);
    }
  });
}</code></pre>
      </div>
    </div>
  </article>

  <!-- TASK 3 -->
  <article class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="3-Уровень: Вызов" data-en="Tier 3: Challenge">3-Bosqich: Kiber-Sinov</span>
      <span class="task-score">2 BALL</span>
    </div>
    <h3 data-ru="Авто-Переподключение (Exponential Backoff)" data-en="Exponential Backoff Auto-Reconnect">Avtomatik Qayta Ulanish va Ping/Pong O'lchagich</h3>
    <p data-ru="Реализуйте класс ResilientSocket(url), который слушает ws.onclose и пробует переподключиться через задержку delay * 1.5, но не более 10 000 мс. Также добавьте метод measurePing(), вычисляющий время ответа:" data-en="Implement class ResilientSocket(url) listening to ws.onclose and reconnecting with exponential backoff delay * 1.5 (capped at 10,000ms). Add measurePing() tracking latency:">Soket yopilganda (<code>onclose</code>) har safar kechikishni 1.5 barobarga oshirib avtomatik qayta ulanuvchi (maksimal 10 soniya) va <code>measurePing()</code> metodi orqali millisekund kechikishini hisoblovchi <code>ResilientSocket</code> klassini yozing:</p>
    <div class="code-box">class ResilientSocket {
  constructor(url) {
    this.url = url;
    this.delay = 1000;
    this.connect();
  }
  // onclose triggers setTimeout with this.delay
}</div>
    <textarea class="answer-area" id="ans_task_3" rows="8" placeholder="ResilientSocket kodini bu yerga yozing..." data-placeholder-ru="Напишите код класса здесь..." data-placeholder-en="Write class code here..." oninput="saveAnswers()"></textarea>
    <div style="margin-top:12px;">
      <button class="btn btn-outline teacher-solution-only" onclick="toggleSolution('sol_3')" data-ru="🔒 Эталон Решения (Учитель)" data-en="🔒 Solution (Teacher)">🔒 Etalon Yechim (O'qituvchi)</button>
      <div class="solution-box teacher-solution-only" id="sol_3" hidden>
        <h4 data-ru="✅ Эталонный Resilient Класс" data-en="✅ Reference Resilient Class">✅ Etalon Yechim</h4>
        <pre><code>export class ResilientSocket {
  constructor(url) {
    this.url = url;
    this.delay = 1000;
    this.connect();
  }
  connect() {
    this.ws = new WebSocket(this.url);
    this.ws.onopen = () => {
      this.delay = 1000; // Reset delay upon success
    };
    this.ws.onclose = () => {
      setTimeout(() => this.connect(), this.delay);
      this.delay = Math.min(this.delay * 1.5, 10000);
    };
  }
  measurePing() {
    const start = performance.now();
    this.ws.send(JSON.stringify({ type: "PING", ts: start }));
  }
}</code></pre>
      </div>
    </div>
  </article>"""
    vz_tpl = vz_tpl.replace("{{TASKS_LIST}}", tasks_9)

    with open(os.path.join(LESSON_DIR, "vazifa.html"), "w", encoding="utf-8") as f:
        f.write(vz_tpl)
    print("  ✓ Created: vazifa.html")

    # ============================================================
    # 4. TEACHER_READING.MD (Guide & Rubric)
    # ============================================================
    tr_md = f"""# 9-sinf: 30-dars — Real-Vaqt Texnologiyalari: WebSockets va LAN Kiber-Chat Engine
**Target International School · Yunusobod Filiali**
**O'qituvchi:** Ismoiljon Usmonov · **Format:** 80 Daqiqa (Double Block / Juftlik dars)

---

## 🎯 Dars Maqsadi va Asosiy Mohiyati
Ushbu 80 daqiqalik juftlik darsda 9-sinf o'quvchilari eskirgan, serverni zo'riqtiruvchi HTTP Polling modeli bilan xayrlashadilar va butun dunyo bo'ylab barcha jonli chatlar (Telegram, Discord) hamda multiplayer o'yinlar ishlatadigan **WebSockets (Full-Duplex TCP soket)** texnologiyasiga o'tadilar.

Sinfdagi kompyuterlar o'rtasida real-vaqt rejimida xabarlar almashinuvi yo'lga qo'yiladi va Chrome DevTools orqali freymlar (Opcodes `0x1 Text`, `0x8 Close`, `0x9 Ping`) bevosita tutib ko'riladi.

---

## ⏱️ 80 Daqiqalik Vaqt Taqsimoti (2 Bosqichli Reja)

### 1-Bosqich: Nazariya, Protokol va Jonli Simulyator (40 Daqiqa)
* **00:00 – 04:00 (4 min) | Kirish & Missiya:** Dars mavzusi va 10 ballik baholash mezonini e'lon qilish.
* **04:00 – 12:00 (8 min) | 29-Dars Tahlili (HW Review):** Asinxron JS va `setInterval(fetch, 1000)` polling xatosi tahlili. 30 soniyalik blits savol (`101 Switching Protocols`).
* **12:00 – 18:00 (6 min) | Real Muammo:** Nega HTTP real-vaqtda qulaydi? 1 soniyalik lag, 1 KB sarlavha isrofi va C10K server falokati.
* **18:00 – 24:00 (6 min) | WebSockets Konsepti:** 101 Handshake mexanizmi va doimiy ochiq full-duplex TCP tunnel.
* **24:00 – 30:00 (6 min) | Paketlar Anatomiyasi & DevTools:** Chrome DevTools -> Network -> WS filtri va Opcodes (`0x1 Text`, `0x8 Close`, `0x9 Ping`).
* **30:00 – 35:00 (5 min) | Server Arxitekturasi:** Node.js `ws` serveri va `wss.clients.forEach` broadcast tsikli.
* **35:00 – 40:00 (5 min) | Klient Hayot Tsikli:** `new WebSocket()`, `onopen`, `onmessage`, `onclose` va auto-reconnect.

### 2-Bosqich: Jonli Tajriba, Kiber-Arena va Demos (40 Daqiqa)
* **40:00 – 48:00 (8 min) | Jonli Slayd Simulyatori:** Smartboardda Alice va Bob terminallari orqali paket uzatish va ping-pong kechikishini sinash.
* **48:00 – 54:00 (6 min) | Interaktiv Kiber-Quiz:** 3 ta savol bo'yicha blits o'tkazish.
* **54:00 – 69:00 (15 min) | Kiber-Arena (Amaliyot):** O'quvchilar `studio/index.html` da LAN chatini ochib, partadoshi bilan xabar almashadilar.
* **69:00 – 74:00 (5 min) | Juftlikda Peer-Review:** 4 ta mezon bo'yicha xonalar izolyatsiyasi va freymlar tekshiruvi.
* **74:00 – 77:00 (3 min) | O'quvchilar Demosi:** 2 ta juftlik doskaga chiqib o'zaro freymlar oqimini namoyish qiladi.
* **77:00 – 80:00 (3 min) | Xulosa & Uy Vazifasi:** 10 ballik `vazifa.html` ilovasini tushuntirish va 11-hafta WebRTC mavzusini anons qilish.

---

## 🏆 10 Ballik Rasmiy Baholash Mezoni
1. **1-Daraja: Baza (4 ball):** `new WebSocket()` ochish, `onopen` statusini ushlash va JSON xabar qabul qilish.
2. **2-Daraja: Amaliyot (4 ball):** Serverda `broadcastToRoom()` orqali faqat bitta xonadagi o'quvchilarga xabar tarqatish.
3. **3-Daraja: Kiber-Sinov (2 ball):** Aloqa uzilganda auto-reconnect mexanizmi va real-vaqt ping o'lchash.
"""
    with open(os.path.join(LESSON_DIR, "TEACHER_READING.md"), "w", encoding="utf-8") as f:
        f.write(tr_md)
    print("  ✓ Created: TEACHER_READING.md")

    # ============================================================
    # 5. STUDIO/INDEX.HTML & LAB/INDEX.HTML (LAN Cyber Chat & Sniffer)
    # ============================================================
    studio_html = """<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Target Cyber-Chat Hub & WebSocket Сниффер" data-en="Target Cyber-Chat Hub & WebSocket Sniffer">Target Cyber-Chat Hub & WebSocket Sniffer</title>
  <style>
    :root {
      --bg: #090d16;
      --panel: #0f172a;
      --panel-2: #1e293b;
      --ink: #f8fafc;
      --ink-2: #94a3b8;
      --accent: #e11d48;
      --green: #10b981;
      --blue: #38bdf8;
      --amber: #f59e0b;
      --rule: #334155;
    }
    :root[data-theme="light"] {
      --bg: #f8fafc;
      --panel: #ffffff;
      --panel-2: #f1f5f9;
      --ink: #0f172a;
      --ink-2: #64748b;
      --accent: #e11d48;
      --green: #059669;
      --blue: #0284c7;
      --amber: #d97706;
      --rule: #e2e8f0;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg);
      color: var(--ink);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }
    header {
      background: var(--panel);
      border-bottom: 1px solid var(--rule);
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 800;
      font-size: 14px;
    }
    .tag {
      background: var(--accent);
      color: #fff;
      font-size: 10px;
      padding: 2px 8px;
      border-radius: 4px;
      letter-spacing: 0.05em;
    }
    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .btn {
      font-family: inherit;
      font-size: 12px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid var(--rule);
      background: var(--panel-2);
      color: var(--ink);
      cursor: pointer;
      transition: all 0.15s;
    }
    .btn:hover {
      border-color: var(--accent);
    }
    .lang-btn.active {
      background: var(--accent);
      color: #fff;
      border-color: var(--accent);
    }
    main {
      flex: 1;
      display: grid;
      grid-template-columns: 240px 1fr 340px;
      gap: 1px;
      background: var(--rule);
    }
    @media (max-width: 900px) {
      main { grid-template-columns: 1fr; }
    }
    .sidebar-left, .chat-area, .sidebar-right {
      background: var(--bg);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    h2 {
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--ink-2);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .room-list {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .room-item {
      padding: 8px 12px;
      border-radius: 6px;
      background: var(--panel);
      border: 1px solid transparent;
      cursor: pointer;
      font-size: 13px;
      font-weight: 600;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .room-item.active {
      border-color: var(--accent);
      background: rgba(225, 29, 72, 0.1);
      color: var(--accent);
    }
    .chat-messages {
      flex: 1;
      background: var(--panel);
      border: 1px solid var(--rule);
      border-radius: 8px;
      padding: 14px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
      min-height: 380px;
    }
    .msg-card {
      background: var(--panel-2);
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 12.5px;
      line-height: 1.5;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .msg-head {
      display: flex;
      justify-content: space-between;
      font-size: 11px;
    }
    .msg-user {
      font-weight: 700;
      color: var(--blue);
    }
    .msg-time {
      color: var(--ink-2);
    }
    .chat-input-bar {
      display: flex;
      gap: 8px;
    }
    .chat-input {
      flex: 1;
      background: var(--panel);
      border: 1px solid var(--rule);
      border-radius: 6px;
      padding: 10px 14px;
      color: var(--ink);
      font-family: inherit;
      font-size: 13px;
    }
    .chat-input:focus {
      outline: none;
      border-color: var(--accent);
    }
    .telemetry {
      background: var(--panel);
      border: 1px solid var(--rule);
      border-radius: 8px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 12px;
      font-family: "JetBrains Mono", monospace;
    }
    .packet-log {
      flex: 1;
      font-family: "JetBrains Mono", monospace;
      font-size: 10.5px;
      background: #030712;
      border: 1px solid var(--rule);
      border-radius: 8px;
      padding: 10px;
      overflow-y: auto;
      color: #94a3b8;
      display: flex;
      flex-direction: column;
      gap: 4px;
      max-height: 300px;
    }
    .frame-in { color: #34d399; }
    .frame-out { color: #38bdf8; }
    .frame-ping { color: #f59e0b; }
  </style>
</head>
<body>

<header>
  <div class="brand">
    <span class="tag">TARGET VIBECODING</span>
    <span data-ru="Target Cyber-Chat Hub & WebSocket Сниффер" data-en="Target Cyber-Chat Hub & WebSocket Sniffer">Target Cyber-Chat Hub & WebSocket Sniffer</span>
  </div>
  <div class="header-actions">
    <button class="btn" onclick="toggleTheme()" aria-label="Theme">🌓</button>
    <div style="display:flex; gap:4px;">
      <button class="btn lang-btn active" data-lang="uz" onclick="setAppLang('uz')">UZ</button>
      <button class="btn lang-btn" data-lang="ru" onclick="setAppLang('ru')">RU</button>
      <button class="btn lang-btn" data-lang="en" onclick="setAppLang('en')">EN</button>
    </div>
  </div>
</header>

<main>
  <!-- Sidebar Left: Rooms & Status -->
  <div class="sidebar-left">
    <h2 data-ru="Каналы Чата" data-en="Chat Channels">Kiber-Xonalar</h2>
    <div class="room-list">
      <div class="room-item active" onclick="switchRoom('general')">
        <span># general</span>
        <span style="font-size:10px; color:var(--green);">● Online</span>
      </div>
      <div class="room-item" onclick="switchRoom('red-team')">
        <span># red-team</span>
        <span style="font-size:10px; color:var(--accent);">🔒 CTF</span>
      </div>
      <div class="room-item" onclick="switchRoom('devops')">
        <span># devops</span>
        <span style="font-size:10px; color:var(--blue);">⚡ Ops</span>
      </div>
    </div>

    <div style="margin-top:auto; font-size:11px; color:var(--ink-2); line-height:1.5;" data-ru="💡 Сообщения изолированы по комнатам. Канал #red-team не виден пользователям #general." data-en="💡 Messages are strictly isolated per room. #red-team traffic is hidden from #general.">
      💡 Xabarlar xonalar bo'yicha to'liq izolyatsiya qilingan. <code>#red-team</code> xabarlari begona xonalarga chiqmaydi.
    </div>
  </div>

  <!-- Center: Chat Window -->
  <div class="chat-area">
    <div style="display:flex; justify-content:space-between; align-items:center;">
      <h2 id="activeRoomTitle" data-ru="Канал: #general" data-en="Channel: #general">Xona: #general</h2>
      <div style="font-size:11.5px; font-family:'JetBrains Mono',monospace; color:var(--green);">● WS CONNECTED (101)</div>
    </div>

    <div class="chat-messages" id="chatMessages">
      <div class="msg-card">
        <div class="msg-head">
          <span class="msg-user">System (101 Handshake)</span>
          <span class="msg-time">00:00:00</span>
        </div>
        <div style="color:var(--green);">⚡ WebSocket tunnel ochiq: ws://127.0.0.1:8080/lan-chat. Xabarlar real-vaqt rejimida oqib keladi.</div>
      </div>
    </div>

    <div class="chat-input-bar">
      <input type="text" id="chatInput" class="chat-input" placeholder="Xabarni yozing va Enter bosing..." data-placeholder-ru="Введите сообщение и нажмите Enter..." data-placeholder-en="Type your message and hit Enter..." onkeydown="if(event.key==='Enter') sendChatMessage()" />
      <button class="btn" onclick="sendChatMessage()" style="background:var(--accent); color:#fff; border-color:var(--accent);" data-ru="Отправить" data-en="Send">Yuborish</button>
    </div>
  </div>

  <!-- Sidebar Right: Telemetry & Sniffer -->
  <div class="sidebar-right">
    <h2>
      <span data-ru="Сниффер Фреймов (DevTools)" data-en="Frame Sniffer (DevTools)">WS Freymlar Snifferi</span>
      <button class="btn" onclick="clearFrames()" data-ru="Очистить" data-en="Clear">Tozalash</button>
    </h2>

    <div class="telemetry">
      <div data-ru="Статус: " data-en="Status: ">Status: <span style="color:var(--green); font-weight:700;">101 Switching Protocols</span></div>
      <div data-ru="Активные Клиенты: " data-en="Active Clients: ">Active Clients: <span id="telClients" style="color:var(--blue); font-weight:700;">2</span></div>
      <div data-ru="Пакетов (Фреймов): " data-en="Dispatched Frames: ">Dispatched Frames: <span id="telFrames" style="color:var(--accent); font-weight:700;">1</span></div>
      <div data-ru="Пинг (RTT): " data-en="Ping (RTT): ">Ping (RTT): <span id="telPing" style="color:var(--green); font-weight:700;">3 ms</span></div>
    </div>

    <div style="display:flex; gap:6px;">
      <button class="btn" onclick="sendHeartbeatPing()" style="flex:1;" data-ru="📡 Отправить Ping (0x9)" data-en="📡 Send Ping (0x9)">📡 Ping Yuborish (0x9)</button>
      <button class="btn" onclick="simulatePeerMessage()" style="flex:1;" data-ru="🤖 Бот-Сосед" data-en="🤖 Peer Bot">🤖 Partadosh Xabari</button>
    </div>

    <h2 style="margin-top:4px;" data-ru="Лог Пакетов (Opcodes)" data-en="Live Packet Stream">Jonli Freymlar Oqimi</h2>
    <div class="packet-log" id="packetLog">
      <div class="frame-in">[00:00:00] ⬇ 101 Handshake OK: Sec-WebSocket-Accept verified</div>
    </div>
  </div>
</main>

<script>
var appLang = "uz";
var currentRoom = "general";
var frameCount = 1;

// LAN BroadcastChannel simulator (connects multiple browser tabs!)
var bc = null;
try {
  bc = new BroadcastChannel("target_cyber_chat_lan");
  bc.onmessage = function(ev) {
    if (ev.data && ev.data.room === currentRoom) {
      appendMessage(ev.data.user, ev.data.text, false);
      logFrame("⬇ INCOMING", "0x1 (TEXT)", JSON.stringify(ev.data), "frame-in");
    }
  };
} catch(e) {}

function setAppLang(l) {
  appLang = l;
  document.documentElement.lang = l;
  document.querySelectorAll(".lang-btn").forEach(function(b) {
    b.classList.toggle("active", b.getAttribute("data-lang") === l);
  });
  document.querySelectorAll("[data-" + l + "]").forEach(function(el) {
    if (el.children.length === 0 || el.tagName === "TITLE") {
      el.textContent = el.getAttribute("data-" + l);
    }
  });
  var inp = document.getElementById("chatInput");
  if (inp) {
    var ph = inp.getAttribute("data-placeholder-" + l);
    if (ph) inp.placeholder = ph;
  }
}

function toggleTheme() {
  var cur = document.documentElement.getAttribute("data-theme") || "dark";
  var next = (cur === "dark") ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", next);
}

function switchRoom(r) {
  currentRoom = r;
  document.querySelectorAll(".room-item").forEach(function(el) {
    el.classList.toggle("active", el.textContent.indexOf("# " + r) >= 0);
  });
  var title = document.getElementById("activeRoomTitle");
  if (title) title.textContent = "Xona: #" + r;
  var box = document.getElementById("chatMessages");
  if (box) {
    box.innerHTML = '<div class="msg-card" style="border-left:3px solid var(--accent);"><div class="msg-head"><span class="msg-user">Room Switcher</span><span class="msg-time">' + new Date().toLocaleTimeString() + '</span></div><div>Siz <b>#' + r + '</b> xonasiga otdingiz.</div></div>';
  }
  logFrame("⬆ OUTGOING", "0x1 (TEXT)", JSON.stringify({ type: "JOIN_ROOM", room: r }), "frame-out");
}

function sendChatMessage() {
  var inp = document.getElementById("chatInput");
  var text = inp ? inp.value.trim() : "";
  if (!text) return;

  var user = "Men (Client-1)";
  appendMessage(user, text, true);

  var payload = { type: "CHAT", room: currentRoom, user: user, text: text, ts: Date.now() };
  if (bc) bc.postMessage(payload);

  logFrame("⬆ OUTGOING", "0x1 (TEXT)", JSON.stringify(payload), "frame-out");
  if (inp) inp.value = "";
}

function appendMessage(user, text, isMe) {
  var box = document.getElementById("chatMessages");
  if (!box) return;
  var card = document.createElement("div");
  card.className = "msg-card";
  if (isMe) card.style.borderLeft = "3px solid var(--blue)";
  else card.style.borderLeft = "3px solid var(--green)";

  var time = new Date().toLocaleTimeString();
  card.innerHTML = '<div class="msg-head"><span class="msg-user" style="color:' + (isMe ? 'var(--blue)' : 'var(--green)') + ';">' + escapeHtml(user) + '</span><span class="msg-time">' + time + '</span></div><div>' + escapeHtml(text) + '</div>';
  box.appendChild(card);
  box.scrollTop = box.scrollHeight;
}

function logFrame(dir, opcode, dataStr, cls) {
  frameCount++;
  var fCountEl = document.getElementById("telFrames");
  if (fCountEl) fCountEl.textContent = frameCount;

  var log = document.getElementById("packetLog");
  if (!log) return;
  var div = document.createElement("div");
  div.className = cls;
  div.textContent = `[${new Date().toLocaleTimeString()}] ${dir} [${opcode}] -> ${dataStr}`;
  log.prepend(div);
}

function sendHeartbeatPing() {
  var start = performance.now();
  logFrame("⬆ PING", "0x9 (PING)", '{"opcode":"0x9","type":"HEARTBEAT"}', "frame-ping");
  setTimeout(function() {
    var lat = Math.floor(performance.now() - start);
    var pEl = document.getElementById("telPing");
    if (pEl) pEl.textContent = lat + " ms";
    logFrame("⬇ PONG", "0xA (PONG)", '{"opcode":"0xA","rtt_ms":' + lat + '}', "frame-in");
  }, 3);
}

function simulatePeerMessage() {
  var peers = ["Ali (Partadosh)", "Zilola (Red-Team)", "Sardor (Ops)"];
  var quotes = ["Salom! LAN chat juda tez ishlayapti!", "DevTools WS da paketni tutdim, lag 3ms!", "101 Handshake kodini tekshirdim, toza!"];
  var pUser = peers[Math.floor(Math.random() * peers.length)];
  var pText = quotes[Math.floor(Math.random() * quotes.length)];

  appendMessage(pUser, pText, false);
  logFrame("⬇ INCOMING", "0x1 (TEXT)", JSON.stringify({ type: "CHAT", room: currentRoom, user: pUser, text: pText }), "frame-in");
}

function clearFrames() {
  var log = document.getElementById("packetLog");
  if (log) log.innerHTML = '<div style="color:#64748b;">// Freymlar royxati tozalandi</div>';
}

function escapeHtml(s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
</script>
</body>
</html>
"""
    with open(os.path.join(STUDIO_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(studio_html)
    with open(os.path.join(LAB_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(studio_html)
    print("  ✓ Created: studio/index.html & lab/index.html")

    print(f"🎉 9-sinf (30-dars) generation finished in {LESSON_DIR}!")

if __name__ == "__main__":
    build_9_lesson()
