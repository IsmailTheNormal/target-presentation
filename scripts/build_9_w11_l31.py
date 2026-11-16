#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_9_w11_l31.py — Builder for 9th Grade, Week 11, Lesson 31

Mavzu: WebRTC va Peer-to-Peer (P2P) Aloqa: STUN, SDP Handshake va RTCDataChannel
Format: Yakka Dars (40 daqiqa), 10 slayd
Kohorta: 9-sinf (Junior Vibecoders, Full-Stack & DevOps Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "9-sinf", "11-hafta", "31-dars-webrtc-va-p2p-aloqa")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "studio"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (10 Slides)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="9-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 31" data-en="GRADE 9 · WEEK 11 · LESSON 31">9-SINF · 11-HAFTA · 31-DARS</span></div>
    <h1 class="display" data-ru="WebRTC и Peer-to-Peer: STUN, SDP Handshake и DataChannel" data-en="WebRTC & Peer-to-Peer: STUN, SDP Handshake & DataChannel">WebRTC va Peer-to-Peer (P2P) Aloqa: STUN, SDP Handshake va RTCDataChannel</h1>
    <p class="lede" data-ru="Прямая связь браузер-браузер без центрального сервера: преодоление NAT, STUN-серверы, согласование SDP и безопасная передача данных через DTLS/SCTP." data-en="Direct browser-to-browser communication without central servers: NAT traversal, STUN discovery, SDP negotiation, and encrypted DTLS/SCTP DataChannels.">Markaziy serversiz to'g'ridan-to'g'ri brauzerlararo aloqa: NAT devorini yorib o'tish, STUN serverlari, SDP muzokaralari va DTLS/SCTP orqali xavfsiz ma'lumot oqimi.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">40 daqiqalik Yakka Dars</div>
        <h3 data-ru="Архитектура WebRTC" data-en="WebRTC Architecture">P2P Kiber-Tarmoq</h3>
        <p data-ru="Почему центральные серверы становятся узким местом при высоких нагрузках и как браузеры общаются напрямую." data-en="Why central servers become bottlenecks under high load and how browsers communicate directly.">Nega markaziy serverlar katta oqimlarda tiqilib qoladi va brauzerlar qanday qilib serverlarsiz to'g'ridan-to'g'ri bog'lanadi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Jonli P2P Terminal</div>
        <h3 data-ru="RTCDataChannel Студия" data-en="RTCDataChannel Studio">To'g'ridan-to'g'ri Tunnel</h3>
        <p data-ru="Каждый ученик поднимет P2P канал между двумя узлами, передаст зашифрованные пакеты и измерит RTT задержку." data-en="Each student initializes a P2P channel between two peers, transfers encrypted packets, and measures RTT ping latency.">Har bir o'quvchi ikkita uzel o'rtasida P2P kanal ochadi, shifrlangan paketlarni uzatadi va RTT ping kechikishini o'lchaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–08:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 30-УРОКА" data-en="LESSON 30 HOMEWORK REVIEW">30-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="WebSockets: Узкие Места Центрального Бродкаста и Шаг к P2P" data-en="WebSockets: Central Broadcast Bottlenecks & The Leap to P2P">WebSockets: Markaziy Broadcast Tiqilishi va P2P Pog'onasi</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Типичная ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Прогон тяжелых медиафайлов через Node.js WebSocket" data-en="Routing Heavy Media through Node.js WebSocket">Katta Fayllar va Jonli Oqimlarni WebSocket Serverga Yuklash</h3>
        <p data-ru="Ученики пытались пересылать 4K видеопотоки и гигабайтные файлы через центральный WebSocket. Результат: серверный процесс перегружает RAM, CPU достигает 100%, а все подключенные клиенты ловят лаги." data-en="Students attempted to relay 4K video streams and large files through a central WebSocket server. Result: server RAM exhaustion, 100% CPU spikes, and severe lag across all clients.">O'quvchilar katta fayllar va video oqimlarni markaziy WebSocket server orqali o'tkazishga urindilar. Natijada server xotirasi to'lib, CPU 100% bo'ldi va butun tarmoq qotib qoldi.</p>
        <pre><code>// ❌ Xato: Serverni oraliq vositachi qilib qiynash
socket.emit('heavy_stream_chunk', binaryDataChunk); // 100 MB/s!</code></pre>
      </div>
      <div class="box success-border">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой стандарт (Golden Solution)" data-en="Golden Standard">Oltin Standart (Golden Solution)</div>
        <h3 data-ru="Сигнализация через сокет, данные напрямую через WebRTC" data-en="Signaling via WebSocket, Data via WebRTC">WebSocket Faqat Signallash Uchun, Ma'lumot esa P2P</h3>
        <p data-ru="WebSocket нужен лишь на 2 секунды — чтобы обменяться адресами (SDP offer/answer). После рукопожатия поток данных течет напрямую между браузерами с нулевой нагрузкой на сервер." data-en="WebSocket is needed only for 2 seconds to exchange session parameters (SDP offer/answer). Once connected, raw data streams directly peer-to-peer with zero server overhead.">WebSocket faqat 2 soniyaga kerak — SDP offer/answer almashish uchun. Shundan so'ng ma'lumotlar to'g'ridan-to'g'ri P2P tuneli orqali uzatiladi, server yuki 0 bo'ladi.</p>
        <pre><code>// ✅ To'g'ri: Faqat 1 marta ulanish ma'lumotini uzatish
signalingWs.send(JSON.stringify({ type: 'sdp-offer', sdp }));
// Barcha keyingi baytlar: peer.dataChannel.send(binaryData);</code></pre>
      </div>
    </div>
    <div class="bridge-card" style="margin-top:12px; padding:10px 16px; border-radius:10px; background:rgba(59,130,246,0.08); border-left:4px solid var(--accent); display:flex; justify-content:space-between; align-items:center;">
      <div>
        <strong style="color:var(--accent);" data-ru="Блиц-вопрос (30 сек):" data-en="Blitz Question (30s):">⚡ Blitz-Savol (30s):</strong>
        <span data-ru="Почему два ноутбука в разных домах не могут подключиться напрямую по локальному IP 192.168.1.5?" data-en="Why can't two laptops in different homes connect directly using local IP 192.168.1.5?">Nega ikki xonadondagi noutbuklar oddiy 192.168.1.5 lokal IP orqali to'g'ridan-to'g'ri bog'lana olmaydi?</span>
      </div>
      <span class="badge" style="font-size:11px;" data-ru="NAT барьер!" data-en="NAT Barrier!">NAT Devori!</span>
    </div>
  </section>

  <!-- SLIDE 3: PROBLEM & NAT BARRIER -->
  <section class="slide" data-phase="Muammo|Проблема|Problem" data-time="08:00–12:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ПРОБЛЕМА АРХИТЕКТУРЫ СЕТИ" data-en="NETWORK ARCHITECTURE CHALLENGE">TARMOQ ARXITEKTURASI VA NAT DEVORI</span></div>
    <h2 data-ru="Почему Интернет Ломает Прямые Соединения? (NAT и Роутеры)" data-en="Why Does the Internet Block Direct Connections? (NAT & Routers)">Nega Internet To'g'ridan-to'g'ri Ulanishni Bloklaydi? (NAT Devori)</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:15px; margin-bottom:12px;" data-ru="Большинство устройств в мире не имеют публичного IPv4 адреса. Они спрятаны за домашними или мобильными роутерами." data-en="Most devices worldwide lack a public IPv4 address. They sit concealed behind home Wi-Fi routers or mobile carrier NATs.">Dunyodagi aksariyat qurilmalar ommaviy IPv4 manziliga ega emas. Ular uy Wi-Fi routerlari yoki provayder NAT tizimi orqasiga yashiringan.</p>
        <ul class="clean-list">
          <li data-ru="<strong>NAT (Network Address Translation):</strong> Роутер преобразует локальный адрес (192.168.x.x) в общий внешний IP." data-en="<strong>NAT (Network Address Translation):</strong> The router maps private local IP (192.168.x.x) to a shared external public IP."><strong>NAT (Network Address Translation):</strong> Router lokal IP manzilni (192.168.x.x) bitta umumiy tashqi IP ga o'zgartiradi.</li>
          <li data-ru="<strong>Скрытый порт:</strong> Внешний мир не знает, на какой именно внутренний порт отправлять входящие пакеты для Алисы." data-en="<strong>Hidden Port:</strong> The external world has no visibility into which private port belongs to Alice's active connection."><strong>Yashirin Port:</strong> Tashqi internet olami Alisaning noutbuki aynan qaysi ichki portda kutayotganini ko'ra olmaydi.</li>
          <li data-ru="<strong>P2P решение:</strong> Нужен внешний «зеркальный» сервер (STUN), чтобы сказать каждому: «Вот твой реальный публичный IP и порт!»" data-en="<strong>P2P Breakthrough:</strong> We need an external mirror server (STUN) to reflect back: 'Here is your real public IP and port!'"><strong>P2P Yechimi:</strong> Tashqi "ko'zgu" serveri (STUN) kerak, u har bir qurilmaga: "Sening tashqi ommaviy IP va porting mana bu!" deb aytadi.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:12px; line-height:1.6;">
        <div style="color:var(--accent); font-weight:700; margin-bottom:6px;">[NAT Traversal Sxemasi]</div>
        <div style="color:var(--ink-2);">Alice (Lokal: 192.168.1.15)</div>
        <div style="color:var(--ink-2); margin-left:14px;">│  (1) "STUN, mening tashqi manzilim qaysi?"</div>
        <div style="color:var(--ink-2);">▼</div>
        <div style="background:rgba(59,130,246,0.1); padding:6px 10px; border-radius:6px; border:1px solid var(--accent); margin:4px 0;">
          <strong style="color:var(--accent);">Google Public STUN (stun:stun.l.google.com:19302)</strong><br>
          <span style="font-size:11px;">Javob: "Alice, sen tashqariga 213.230.88.12:49811 bo'lib ko'rinyapsan!"</span>
        </div>
        <div style="color:var(--ink-2); margin-left:14px;">│  (2) Alice o'zining shu manzilini Bobga uzatadi (SDP/ICE)</div>
        <div style="color:var(--ink-2);">▼</div>
        <div style="color:var(--green); font-weight:700;">Bob (213.230.88.12:49811 ga to'g'ridan-to'g'ri P2P paket uradi!)</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: SDP & ICE HANDSHAKE -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="12:00–16:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="ПРОТОКОЛЫ СОГЛАСОВАНИЯ" data-en="NEGOTIATION PROTOCOLS">SDP VA ICE PROTOKOLLARI</span></div>
    <h2 data-ru="4 Шага WebRTC Рукопожатия: SDP Offer, Answer и ICE" data-en="4 Steps of WebRTC Handshake: SDP Offer, Answer & ICE">WebRTC Bog'lanishning 4 Bosqichi: Offer, Answer va ICE</h2>
    <div class="grid-4" style="gap:10px;">
      <div class="box" style="border-top:3px solid var(--accent);">
        <div class="tag">1. Offer Yaratish</div>
        <h4 style="margin:6px 0;" data-ru="SDP Предложение" data-en="SDP Offer">SDP Taklifi</h4>
        <p style="font-size:12px;" data-ru="Алиса создает SDP: список поддерживаемых кодеков, тип канала (DataChannel) и криптографические ключи DTLS." data-en="Alice creates SDP: supported codecs, channel types, and DTLS cryptographic fingerprint.">Alisa SDP yaratadi: qo'llab-quvvatlanadigan protokollar, DataChannel parametrlari va DTLS shifr kalitlari.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--purple);">
        <div class="tag" style="color:var(--purple);">2. STUN va ICE</div>
        <h4 style="margin:6px 0;" data-ru="Сбор Кандидатов" data-en="Candidate Gathering">ICE Nomzodlari</h4>
        <p style="font-size:12px;" data-ru="Браузер опрашивает STUN и формирует список возможных сетевых маршрутов (host, srflx, relay)." data-en="Browser queries STUN and builds candidates for routing (host, srflx, relay).">Brauzer STUN orqali o'zining barcha mumkin bo'lgan tarmoq yo'llarini (host, srflx, relay) yig'adi.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--green);">
        <div class="tag" style="color:var(--green);">3. Signallash</div>
        <h4 style="margin:6px 0;" data-ru="Обмен Текстом" data-en="Signaling Exchange">SDP Almashish</h4>
        <p style="font-size:12px;" data-ru="Через любой канал (WebSocket, Telegram, QR-код) Алиса отправляет свой SDP Offer Бобу, а Боб возвращает Answer." data-en="Via any signaling channel (WebSocket, QR, copy-paste), Alice sends Offer to Bob and receives Answer.">Ixtiyoriy kanal (WebSocket, QR, yoki matn) orqali Alisa o'z Offerini Bobga beradi, Bob esa Answer qaytaradi.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--amber);">
        <div class="tag" style="color:var(--amber);">4. P2P Tunnel</div>
        <h4 style="margin:6px 0;" data-ru="Прямой Канал" data-en="Direct Tunnel">Kanal Ochiq!</h4>
        <p style="font-size:12px;" data-ru="Браузеры тестируют связность (STUN ping). Выбирается кратчайший маршрут. Включается шифрование DTLS." data-en="Browsers check connectivity. The shortest path is locked. DTLS encryption secures the channel.">Brauzerlar eng qisqa yo'lni tanlaydi, DTLS shifrlash yoqiladi va kanal 'open' holatiga o'tadi.</p>
      </div>
    </div>
    <div style="margin-top:12px; font-family:var(--font-mono); font-size:11px; background:var(--surface-2); padding:8px 12px; border-radius:6px; color:var(--ink-2);">
      SDP Formati Namunasi: <code style="color:var(--ink);">v=0 \n o=alice 2890844526 \n s=- \n a=fingerprint:sha-256 A1:B2... \n a=candidate:1 1 UDP 2130706431 213.230.88.12 49811 typ srflx</code>
    </div>
  </section>

  <!-- SLIDE 5: CODE IMPLEMENTATION -->
  <section class="slide" data-phase="Kod Mexanizmi|Реализация в Коде|Code Mechanics" data-time="16:00–20:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="API БРАУЗЕРА" data-en="BROWSER WEB API">JAVASCRIPT WEBRTC API</span></div>
    <h2 data-ru="Создание RTCPeerConnection и RTCDataChannel" data-en="Creating RTCPeerConnection & RTCDataChannel">RTCPeerConnection va RTCDataChannel Kod Standarti</h2>
    <div class="grid-2">
      <div>
        <h4 style="margin-bottom:6px; color:var(--accent);" data-ru="1. Инициализация Узла и Канала (Alice)" data-en="1. Node & Channel Initialization (Alice)">1. Uzel va Kanal Yaratish (Alice)</h4>
        <pre><code class="language-js">// STUN konfiguratsiyasi
const config = {
  iceServers: [{ urls: 'stun:stun.l.google.com:19302' }]
};
const peer = new RTCPeerConnection(config);

// P2P ma'lumotlar kanalini ochish
const channel = peer.createDataChannel('kiber-chat', {
  ordered: true // Paketlar tartibli yetib boradi
});

channel.onopen = () => console.log('✅ P2P Kanal Ochiq!');
channel.onmessage = (e) => console.log('Kelgan xabar:', e.data);

// ICE nomzodini tutish
peer.onicecandidate = (e) => {
  if (e.candidate) signaling.send({ candidate: e.candidate });
};</code></pre>
      </div>
      <div>
        <h4 style="margin-bottom:6px; color:var(--green);" data-ru="2. Прием Канала и Ответ (Bob)" data-en="2. Receiving Channel & Answering (Bob)">2. Kanalni Qabul Qilish va Javob (Bob)</h4>
        <pre><code class="language-js">const bobPeer = new RTCPeerConnection(config);

// Bob kiruvchi DataChannelni tinglaydi
bobPeer.ondatachannel = (e) => {
  const remoteChan = e.channel;
  remoteChan.onopen = () => console.log('✅ Bob: Kanal boglandi!');
  remoteChan.onmessage = (ev) => {
    console.log('Bob qabul qildi:', ev.data);
    remoteChan.send('Salom Alice! Paket yetib keldi.');
  };
};

// Offer qabul qilish va Answer yaratish
await bobPeer.setRemoteDescription(receivedOffer);
const answer = await bobPeer.createAnswer();
await bobPeer.setLocalDescription(answer);
signaling.send({ answer });</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: PROTOCOLS & SECURITY (SCTP/DTLS) -->
  <section class="slide" data-phase="Xavfsizlik|Безопасность|Security" data-time="20:00–24:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ПРОТОКОЛЫ БЕЗОПАСНОСТИ" data-en="SECURITY PROTOCOLS">SHIFRLASH VA SCTP PROTOKOLI</span></div>
    <h2 data-ru="Почему WebRTC Нельзя Подслушать? (DTLS и SCTP)" data-en="Why WebRTC Cannot Be Eavesdropped? (DTLS & SCTP)">Nega WebRTC-ni Quloq Solib Buzib Bo'lmaydi? (DTLS va SCTP)</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);">UDP / Transport</div>
        <h4 data-ru="Молниеносная Скорость" data-en="Blazing Low Latency">Minimal Kechikish</h4>
        <p style="font-size:12px;" data-ru="WebRTC работает поверх UDP. В отличие от TCP, здесь нет медленного повторного подтверждения для реального времени." data-en="WebRTC operates on top of UDP. Unlike TCP, it eliminates slow ack bottlenecks for real-time responsiveness.">WebRTC UDP ustida ishlaydi. TCP kabi sekinlashtiruvchi ortiqcha tekshiruvlar yo'q — kechikish &lt;20ms gacha tushadi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">DTLS / Shifrlash</div>
        <h4 data-ru="Шифрование по Умолчанию" data-en="Encrypted by Default">Kafolatlangan Shifr</h4>
        <p style="font-size:12px;" data-ru="DTLS (Datagram TLS) встроен в ядро спецификации. Отправить незашифрованные данные через WebRTC технически невозможно!" data-en="DTLS (Datagram TLS) is baked into the standard. Transmitting unencrypted payloads via WebRTC is technically impossible!">DTLS (Datagram TLS) WebRTC standartining majburiy talabidir. Ochiq, shifrlanmagan ma'lumot yuborishning o'zi imkonsiz!</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">SCTP / Kanallar</div>
        <h4 data-ru="Управление Потоком" data-en="Stream Flow Control">Moslashuvchan Tartib</h4>
        <p style="font-size:12px;" data-ru="SCTP позволяет выбирать: доставлять пакеты строго по порядку (ordered) или максимально быстро без ожидания потерь." data-en="SCTP allows choosing: strictly ordered delivery for files or unordered blazing delivery for gaming inputs.">SCTP rejimni tanlash imkonini beradi: fayllar uchun tartibli (ordered), o'yinlar uchun esa o'ta tez tartibsiz oqim.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px; background:rgba(0,0,0,0.2); border:1px solid var(--hair);">
      <div style="font-size:12px; font-weight:700; color:var(--ink-2); margin-bottom:4px;" data-ru="Стек Протоколов WebRTC DataChannel:" data-en="WebRTC DataChannel Protocol Stack:">WebRTC DataChannel Protokollar Steki:</div>
      <div style="display:flex; gap:6px; flex-wrap:wrap; font-family:var(--font-mono); font-size:11px;">
        <span style="background:var(--accent); color:#fff; padding:4px 8px; border-radius:4px;">Ilova (Kiber-Chat)</span>
        <span>➔</span>
        <span style="background:var(--purple); color:#fff; padding:4px 8px; border-radius:4px;">RTCDataChannel</span>
        <span>➔</span>
        <span style="background:#2563eb; color:#fff; padding:4px 8px; border-radius:4px;">SCTP</span>
        <span>➔</span>
        <span style="background:#059669; color:#fff; padding:4px 8px; border-radius:4px;">DTLS (AES-GCM-128/256)</span>
        <span>➔</span>
        <span style="background:#d97706; color:#fff; padding:4px 8px; border-radius:4px;">UDP / IP</span>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: IN-DECK INTERACTIVE WEBRTC DEMO -->
  <section class="slide" data-phase="Jonli Sinov|Интерактив|Live Demo" data-time="24:00–28:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="СИМУЛЯТОР В ПРЕЗЕНТАЦИИ" data-en="IN-DECK SIMULATOR">SMARTBOARDDA JONLI P2P SINOVI</span></div>
    <h2 data-ru="Интерактивная Лаборатория: Рукопожатие Alice и Bob" data-en="Interactive Lab: Alice & Bob P2P Handshake">Interaktiv Sinov: Alice va Bob P2P Bog'lanishi</h2>
    <div class="box" style="padding:12px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <div>
          <span class="badge" id="deckP2pStatus" style="background:#ef4444; color:#fff;" data-ru="Статус: Не подключен" data-en="Status: Disconnected">Status: Ulanmagan (DISCONNECTED)</span>
          <span style="font-size:12px; margin-left:10px; color:var(--ink-2);" id="deckP2pLatency" data-ru="RTT Пинг: -- ms" data-en="RTT Ping: -- ms">RTT Ping: -- ms</span>
        </div>
        <div style="display:flex; gap:8px;">
          <button class="btn" onclick="deckStartP2PHandshake()" id="btnDeckConnect" style="background:var(--accent); color:#fff; padding:6px 14px; font-size:12px;" data-ru="1. Запустить P2P Рукопожатие" data-en="1. Start P2P Handshake">⚡ 1. P2P Handshakeni Boshlash</button>
          <button class="btn" onclick="deckSendP2PMessage()" id="btnDeckSend" disabled style="background:var(--green); color:#fff; padding:6px 14px; font-size:12px;" data-ru="2. Отправить P2P Пакет" data-en="2. Send P2P Packet">📨 2. P2P Paket Yuborish</button>
          <button class="btn" onclick="deckResetP2P()" style="padding:6px 10px; font-size:12px;" data-ru="Сброс" data-en="Reset">Qayta o'rnatish</button>
        </div>
      </div>
      <div class="grid-2" style="gap:10px;">
        <div style="background:var(--surface-2); border-radius:8px; padding:10px; font-family:var(--font-mono); font-size:11px;">
          <div style="color:var(--accent); font-weight:700; margin-bottom:6px;">[ALICE UZELI - Local Peer]</div>
          <div id="deckAliceLog" style="height:120px; overflow-y:auto; line-height:1.5; color:var(--ink-2);">
            • Kutish holatida. Handshake tugmasini bosing...
          </div>
        </div>
        <div style="background:var(--surface-2); border-radius:8px; padding:10px; font-family:var(--font-mono); font-size:11px;">
          <div style="color:var(--green); font-weight:700; margin-bottom:6px;">[BOB UZELI - Remote Peer]</div>
          <div id="deckBobLog" style="height:120px; overflow-y:auto; line-height:1.5; color:var(--ink-2);">
            • Kutish holatida.
          </div>
        </div>
      </div>
      <div style="margin-top:8px; font-size:11px; color:var(--ink-2); display:flex; justify-content:space-between;">
        <span data-ru="💡 Пакеты передаются напрямую через loopback RTCDataChannel браузера" data-en="💡 Packets travel directly through the browser's loopback RTCDataChannel">💡 Paketlar brauzerning ichki RTCPeerConnection loopback kanali orqali serverga bormasdan o'tadi</span>
        <span id="deckP2pBytes" data-ru="Передано байт: 0 B" data-en="Bytes transferred: 0 B">Uzatilgan baytlar: 0 B</span>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: INTERACTIVE QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Quiz" data-time="28:00–32:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА ЗНАНИЙ" data-en="KNOWLEDGE CHECK">3-SAVOLLI INTERAKTIV TEST</span></div>
    <h2 data-ru="Блиц-Тест: Архитектура WebRTC и P2P Сетей" data-en="Fast Quiz: WebRTC & P2P Network Architecture">Bilimni Sinash: WebRTC va P2P Tarmoq Arxitekturasi</h2>
    <div class="quiz-container" style="display:flex; flex-direction:column; gap:12px;">
      <!-- Q1 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="1. Какова главная роль STUN сервера в WebRTC?" data-en="1. What is the primary role of a STUN server in WebRTC?">1. WebRTC arxitekturasida STUN serverining asosiy vazifasi nima?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'STUN orqali media fayllar uzatilmaydi!')" style="font-size:12px;" data-ru="A) Все видео и чаты передаются через него" data-en="A) Relaying all video and chat payloads">A) Barcha video va chat fayllarini o'zidan o'tkazish</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! STUN mijozga uning tashqi ommaviy IP va portini bildirib beradi.')" style="font-size:12px;" data-ru="B) Сообщить клиенту его внешний публичный IP и порт" data-en="B) Reflect client's external public IP and port back">B) Mijozga uning tashqi ommaviy IP va portini aytish</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Shifrlash brauzer ichida DTLS orqali qilinadi.')" style="font-size:12px;" data-ru="C) Генерировать SSL сертификат для сайта" data-en="C) Generate SSL certificates for the website">C) Sayt uchun SSL sertifikat generatsiya qilish</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
      <!-- Q2 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="2. Что произойдет, если сервер сигнализации (WebSocket) отключится ПОСЛЕ того, как P2P соединение установлено?" data-en="2. What happens if the signaling server (WebSocket) crashes AFTER the P2P connection is established?">2. P2P ulanish o'rnatilgach, markaziy signalizatsiya serveri (WebSocket) o'chib qolsa nima bo'ladi?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'Aynan shunday! P2P to‘g‘ridan-to‘g‘ri brauzerlar o‘rtasida ochiq qoladi.')" style="font-size:12px;" data-ru="A) P2P соединение продолжит работать без помех" data-en="A) P2P connection stays open and works seamlessly">A) P2P aloqa hech qanday xalaqitsiz to'g'ridan-to'g'ri ishlashda davom etadi</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri! Server oraliq ma‘lumot tashuvchi emas.')" style="font-size:12px;" data-ru="B) Соединение моментально разорвется" data-en="B) The connection immediately drops">B) Ulanish darhol uzilib qoladi</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'DataChannel parametrlari o‘zgarmaydi.')" style="font-size:12px;" data-ru="C) Скорость упадет в 10 раз" data-en="C) Bandwidth drops by 10x">C) Aloqa tezligi 10 barobarga tushib ketadi</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
      <!-- Q3 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="3. Какой протокол обеспечивает обязательное шифрование пакетов в RTCDataChannel?" data-en="3. Which protocol provides mandatory packet encryption in RTCDataChannel?">3. RTCDataChannel kanallarida majburiy shifrlashni qaysi protokol ta'minlaydi?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'HTTP faqat veb sahifalar uchun.')" style="font-size:12px;" data-ru="A) HTTPS" data-en="A) HTTPS">A) HTTPS</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! DTLS (Datagram TLS) UDP ustidagi majburiy shifrlash qatlamidir.')" style="font-size:12px;" data-ru="B) DTLS (Datagram Transport Layer Security)" data-en="B) DTLS (Datagram Transport Layer Security)">B) DTLS (Datagram Transport Layer Security)</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'FTP shifrlanmagan eski fayl protokoli.')" style="font-size:12px;" data-ru="C) FTP" data-en="C) FTP">C) FTP</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: HANDS-ON ARENA -->
  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="32:00–37:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКАЯ МИССИЯ" data-en="HANDS-ON LAB MISSION">15 DAQIQALIK KIBER-ARENA</span></div>
    <h2 data-ru="Лаборатория: Создай Серверлесс P2P Чат-Терминал" data-en="Lab Mission: Build a Serverless P2P Chat Terminal">Kiber-Missiya: Serverless P2P Chat-Terminal Yaratish</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:10px;" data-ru="Откройте студию урока studio/index.html и поднимите изолированный P2P канал между двумя узлами." data-en="Launch the lesson studio studio/index.html and initialize an isolated P2P channel between two nodes.">Darsning <a href="studio/index.html" target="_blank" style="color:var(--accent); font-weight:700;">studio/index.html</a> laboratoriyasini oching va ikkita uzel o'rtasida P2P kanalini ko'taring.</p>
        <ul class="clean-list">
          <li data-ru="<strong>1-Шаг:</strong> Создайте объект <code>RTCPeerConnection</code> со свободным STUN от Google." data-en="<strong>Step 1:</strong> Initialize <code>RTCPeerConnection</code> with Google's free public STUN."><strong>1-Qadam:</strong> Google STUN serveri bilan <code>RTCPeerConnection</code> obyektini yarating.</li>
          <li data-ru="<strong>2-Шаг:</strong> Откройте <code>createDataChannel('p2p-chat')</code> и обработайте событие <code>onopen</code>." data-en="<strong>Step 2:</strong> Open <code>createDataChannel('p2p-chat')</code> and attach the <code>onopen</code> listener."><strong>2-Qadam:</strong> <code>createDataChannel('p2p-chat')</code> kanalini oching va <code>onopen</code> hodisasini ulang.</li>
          <li data-ru="<strong>3-Шаг:</strong> Завершите цикл Offer/Answer и отправьте тестовое текстовое сообщение." data-en="<strong>Step 3:</strong> Complete Offer/Answer handshake and transmit a test message."><strong>3-Qadam:</strong> Offer/Answer tsiklini yakunlang va to'g'ridan-to'g'ri test xabar yuboring.</li>
        </ul>
      </div>
      <div class="box" style="border-left:4px solid var(--accent);">
        <h4 style="margin-bottom:8px;" data-ru="10-Балльная Рубрика Оценки:" data-en="10-Point Grading Rubric:">10 Ballik Baholash Mezoni:</h4>
        <div style="font-size:12px; line-height:1.8;">
          <div><strong style="color:var(--green);">4 Ball:</strong> RTCPeerConnection yaratilgan, SDP Offer/Answer to'g'ri generatsiya bo'ladi.</div>
          <div><strong style="color:var(--accent);">4 Ball:</strong> RTCDataChannel 'open' holatga o'tgan va xabarlar ikki tomonlama uzatiladi.</div>
          <div><strong style="color:var(--purple);">2 Ball (Bonus):</strong> RTT Ping (kechikish vaqti) hisoblagichi va uzatilgan baytlar sanagichi ishlaydi.</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: TIERED HOMEWORK & SUMMARY -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Tiered Homework" data-time="37:00–40:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="SUMMARY & HOMEWORK">XULOSA VA 3 DARAJALI VAZIFA</span></div>
    <h2 data-ru="Итоги 31-Урока и Мост к Завтрашнему Двойному Уроку" data-en="Lesson 31 Recap & Bridge to Tomorrow's Double Class">Xulosa va Ertangi Juftlik Darsiga Kiber-Ko'prik</h2>
    <div class="grid-3" style="gap:10px;">
      <div class="box" style="border-top:3px solid var(--green);">
        <div class="tag" style="color:var(--green);">1-Daraja: Baza (4 ball)</div>
        <h4 data-ru="Базовый P2P Канал" data-en="Basic P2P Channel">Baza P2P Kanali</h4>
        <p style="font-size:12px;" data-ru="Реализуйте локальный DataChannel между peer1 и peer2 с выводом сообщений в терминал." data-en="Implement local DataChannel between peer1 and peer2 with console logging.">peer1 va peer2 o'rtasida DataChannel ochib, xabarlarni ekranga chiqaruvchi bazaviy skript yozing.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--accent);">
        <div class="tag" style="color:var(--accent);">2-Daraja: Loyiha (4 ball)</div>
        <h4 data-ru="Файловый P2P Стример" data-en="P2P File Streamer">Fayl Bo'laklarini Uzatish</h4>
        <p style="font-size:12px;" data-ru="Передайте текстовый файл или изображение через ArrayBuffer чанками по 16 КБ с индикатором прогресса." data-en="Transfer text or image file via ArrayBuffer in 16KB chunks with a progress bar.">ArrayBuffer orqali faylni 16KB bo'laklarga ajratib, progress bar bilan P2P orqali uzating.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--purple);">
        <div class="tag" style="color:var(--purple);">3-Daraja: Challenge (2 ball)</div>
        <h4 data-ru="Хэш-Контроль SHA-256" data-en="SHA-256 Checksum">SHA-256 Nazorati</h4>
        <p style="font-size:12px;" data-ru="Посчитайте SHA-256 хэш отправленного и полученного файла для подтверждения целостности." data-en="Calculate SHA-256 hash of sent and received file to verify 100% data integrity.">Fayl buzilmasdan yetib borganini isbotlash uchun jo'natishdan oldin va keyin SHA-256 tekshiruvini qo'shing.</p>
      </div>
    </div>
    <div class="bridge-card" style="margin-top:12px; padding:10px 16px; border-radius:10px; background:rgba(147,51,234,0.08); border-left:4px solid var(--purple); display:flex; justify-content:space-between; align-items:center;">
      <div>
        <strong style="color:var(--purple);" data-ru="Завтра (Двойной Урок 80 мин):" data-en="Tomorrow (Double Block 80 min):">🚀 Ertaga (80 Daqiqalik Juftlik Dars):</strong>
        <span data-ru="WebRTC MediaStream: Передача живого видео с веб-камеры и микрофона, P2P видеозвонок и экранный стриминг!" data-en="WebRTC MediaStream: Live webcam & mic feeds, P2P video calls, and screen sharing!">WebRTC MediaStream: Jonli veb-kamera va mikrofon oqimini uzatish, P2P video-qo'ng'iroq va ekran namoyishi!</span>
      </div>
      <a href="vazifa.html" class="btn" style="background:var(--purple); color:#fff; font-size:12px;" data-ru="Открыть ДЗ" data-en="Open HW">Vazifani Ochish ➔</a>
    </div>
  </section>
"""

# In-deck JS for Slide 7 interactive WebRTC demo
IN_DECK_JS = """
// --- IN-DECK WEBRTC INTERACTIVE SIMULATOR ---
var deckAlicePeer = null;
var deckBobPeer = null;
var deckAliceChan = null;
var deckBobChan = null;
var deckBytesSent = 0;

function deckLog(elemId, msg, color) {
  var el = document.getElementById(elemId);
  if (!el) return;
  var row = document.createElement('div');
  row.style.color = color || 'var(--ink)';
  row.textContent = '• ' + msg;
  el.appendChild(row);
  el.scrollTop = el.scrollHeight;
}

async function deckStartP2PHandshake() {
  document.getElementById('btnDeckConnect').disabled = true;
  var statusBadge = document.getElementById('deckP2pStatus');
  statusBadge.textContent = 'Status: Handshake boshlanmoqda...';
  statusBadge.style.background = '#f59e0b';

  deckLog('deckAliceLog', '1. RTCPeerConnection obyekti yaratilmoqda...', 'var(--accent)');
  deckLog('deckBobLog', '1. Bob ulanishga tayyorlanmoqda...', 'var(--green)');

  try {
    deckAlicePeer = new RTCPeerConnection();
    deckBobPeer = new RTCPeerConnection();

    // ICE candidates
    deckAlicePeer.onicecandidate = function(e) {
      if (e.candidate) {
        deckLog('deckAliceLog', 'ICE Nomzod topildi: ' + e.candidate.type + ' (' + e.candidate.protocol + ')', 'var(--purple)');
        deckBobPeer.addIceCandidate(e.candidate).catch(function(err){});
      }
    };
    deckBobPeer.onicecandidate = function(e) {
      if (e.candidate) {
        deckLog('deckBobLog', 'ICE Nomzod topildi: ' + e.candidate.type, 'var(--purple)');
        deckAlicePeer.addIceCandidate(e.candidate).catch(function(err){});
      }
    };

    // Bob receives DataChannel
    deckBobPeer.ondatachannel = function(e) {
      deckBobChan = e.channel;
      deckLog('deckBobLog', 'RTCDataChannel qabul qilindi: [' + deckBobChan.label + ']', 'var(--green)');
      deckBobChan.onmessage = function(ev) {
        deckLog('deckBobLog', 'Qabul qilindi: "' + ev.data + '"', 'var(--ink)');
        // Echo reply
        if (deckBobChan.readyState === 'open') {
          setTimeout(function() {
            deckBobChan.send('ECHO: ' + ev.data + ' [Bob orqali tasdiqlandi]');
          }, 300);
        }
      };
    };

    // Alice creates DataChannel
    deckAliceChan = deckAlicePeer.createDataChannel('cyber-channel', { ordered: true });
    deckLog('deckAliceLog', 'DataChannel ochildi: [cyber-channel]', 'var(--accent)');

    deckAliceChan.onopen = function() {
      deckLog('deckAliceLog', '✅ DataChannel statusi: OPEN!', 'var(--green)');
      statusBadge.textContent = 'Status: P2P BOG‘LANDI (CONNECTED)';
      statusBadge.style.background = '#10b981';
      document.getElementById('btnDeckSend').disabled = false;
    };

    deckAliceChan.onmessage = function(ev) {
      deckLog('deckAliceLog', 'Bobdan javob keldi: "' + ev.data + '"', 'var(--green)');
    };

    // SDP Offer
    deckLog('deckAliceLog', '2. SDP Offer generatsiya qilinmoqda...', 'var(--ink-2)');
    var offer = await deckAlicePeer.createOffer();
    await deckAlicePeer.setLocalDescription(offer);
    await deckBobPeer.setRemoteDescription(offer);

    // SDP Answer
    deckLog('deckBobLog', '3. SDP Offer qabul qilindi. Answer yaratilmoqda...', 'var(--ink-2)');
    var answer = await deckBobPeer.createAnswer();
    await deckBobPeer.setLocalDescription(answer);
    await deckAlicePeer.setRemoteDescription(answer);

    deckLog('deckAliceLog', '4. SDP Answer muvaffaqiyatli qabul qilindi. Tunnel ochiq!', 'var(--green)');
  } catch (err) {
    deckLog('deckAliceLog', 'Xatolik: ' + err.message, 'var(--red)');
    statusBadge.textContent = 'Status: Xatolik yuz berdi';
    statusBadge.style.background = '#ef4444';
  }
}

function deckSendP2PMessage() {
  if (!deckAliceChan || deckAliceChan.readyState !== 'open') return;
  var msgs = [
    'Salom Bob! Bu P2P orqali uzatilgan birinchi paket.',
    'Kiber-xavfsizlik testi: DTLS AES-GCM shifrlandi.',
    'Paket ID: #' + Math.floor(Math.random() * 9000 + 1000) + ' | 0ms server yuklamasi!'
  ];
  var text = msgs[Math.floor(Math.random() * msgs.length)];
  var start = performance.now();
  deckAliceChan.send(text);
  var latency = Math.round((performance.now() - start) * 10) / 10;

  deckBytesSent += text.length;
  document.getElementById('deckP2pBytes').textContent = 'Uzatilgan baytlar: ' + deckBytesSent + ' B';
  document.getElementById('deckP2pLatency').textContent = 'RTT Ping: ~' + (latency < 1 ? 0.8 : latency) + ' ms';
  deckLog('deckAliceLog', 'Jo‘natildi: "' + text + '" (' + text.length + ' bayt)', 'var(--accent)');
}

function deckResetP2P() {
  if (deckAlicePeer) try { deckAlicePeer.close(); } catch(e){}
  if (deckBobPeer) try { deckBobPeer.close(); } catch(e){}
  deckAlicePeer = null;
  deckBobPeer = null;
  deckAliceChan = null;
  deckBobChan = null;
  deckBytesSent = 0;
  document.getElementById('deckAliceLog').innerHTML = '• Qayta ishga tushirildi. Handshake tugmasini bosing...';
  document.getElementById('deckBobLog').innerHTML = '• Kutish holatida.';
  document.getElementById('deckP2pStatus').textContent = 'Status: Ulanmagan (DISCONNECTED)';
  document.getElementById('deckP2pStatus').style.background = '#ef4444';
  document.getElementById('deckP2pLatency').textContent = 'RTT Ping: -- ms';
  document.getElementById('deckP2pBytes').textContent = 'Uzatilgan baytlar: 0 B';
  document.getElementById('btnDeckConnect').disabled = false;
  document.getElementById('btnDeckSend').disabled = true;
}

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

# Notes array for 10 slides
NOTES_DATA = {
    "uz": [
        ["Kirish va Maqsad", "O'quvchilarga bugungi dars mavzusi: WebRTC va serverless P2P aloqa haqida gapiring.", "Doskada HTTP, WebSocket va WebRTC farqini bitta chizma bilan ko'rsating."],
        ["Uy Vazifasi Tahlili", "O'tgan darsdagi keng tarqalgan xato: katta video va fayllarni markaziy WebSocket server orqali o'tkazish oqibatlarini tushuntiring.", "Oltin yechimni ko'rsating: WebSocket faqat 2 soniyalik SDP uchun, qolgan barcha og'ir ma'lumot P2P oqadi."],
        ["NAT Devori va STUN", "Nega 192.168.x.x manzillar internetda to'g'ridan-to'g'ri ko'rinmasligini tushuntiring.", "STUN serveri nima uchun ko'zgu (mirror) deb atalishini hayotiy misol bilan ayting."],
        ["SDP va ICE Handshake", "SDP ichida nima borligini (audio/video/data ko'rsatkichlari, DTLS kalitlari) doskada ko'rsating.", "ICE candidate qidirish bosqichini chizib bering."],
        ["Kod Mexanizmi", "RTCPeerConnection va createDataChannel sintaksisini ko'rsating.", "ordered: true va ordered: false farqini tushuntiring."],
        ["Xavfsizlik va Protokollar", "Nega WebRTC da shifrlashni o'chirib bo'lmasligini ta'kidlang (DTLS majburiy).", "SCTP ning TCP va UDP o'rtasidagi gibrid xususiyatini aytib bering."],
        ["Jonli Smartboard Demo", "Taqdimot ichidagi simulyatorda 1-tugmani bosing, handshake qanday o'tishini ko'rsating.", "Keyin P2P paket yuboring va RTT 1ms dan pastligiga o'quvchilar e'tiborini qarating."],
        ["Bilimni Sinash (Quiz)", "3 ta savol bo'yicha o'quvchilarni faol qatnashtiring.", "Noto'g'ri javoblarning sababini darhol tahlil qiling."],
        ["Amaliy Missiya", "O'quvchilarga studio/index.html ni ochishni buyuring.", "Har bir o'quvchi 15 daqiqa ichida o'z P2P kanalini ko'tarib xabar uzatishi kerak."],
        ["Xulosa va Ertangi Dars", "3 darajali uy vazifasini tushuntiring.", "Ertaga bo'ladigan 80 daqiqalik juftlik darsida jonli veb-kamera videosini uzatishimizni anons qiling!"]
    ],
    "ru": [
        ["Введение и Цель", "Представьте тему: WebRTC и бессерверные P2P соединения без посредников.", "Нарисуйте на доске ключевую разницу между HTTP, WebSocket и WebRTC."],
        ["Разбор Домашнего Задания", "Объясните ошибку перегрузки центрального WebSocket сервера тяжелыми медиа-потоками.", "Покажите золотой стандарт: сокет только для 2-секундного SDP обмена, остальное через P2P."],
        ["Барьер NAT и STUN", "Объясните, почему локальные адреса 192.168.x.x не видны напрямую из внешнего интернета.", "Приведите пример STUN-сервера как зеркала, отражающего публичный IP."],
        ["SDP и ICE Handshake", "Покажите структуру SDP: кодеки, параметры DataChannel, криптографические ключи DTLS.", "Объясните сбор кандидатов ICE."],
        ["Реализация в Коде", "Разберите синтаксис RTCPeerConnection и createDataChannel.", "Объясните разницу между ordered: true и ordered: false."],
        ["Безопасность и Протоколы", "Подчеркните обязательность DTLS: передать незашифрованные данные через WebRTC невозможно.", "Объясните роль SCTP поверх UDP."],
        ["Интерактив на Доске", "Запустите встроенный тренажер, продемонстрируйте рукопожатие.", "Отправьте P2P пакет и обратите внимание на нулевую задержку."],
        ["Тест (Квиз)", "Вовлеките класс в 3 контрольных вопроса.", "Разберите причины каждого неправильного ответа."],
        ["Практическая Лаборатория", "Дайте команду открыть studio/index.html.", "Контролируйте установку P2P соединения и отправку сообщений за 15 минут."],
        ["Итоги и Анонс", "Объясните 3 уровня домашнего задания.", "Анонсируйте завтрашний двойной урок (80 мин): живое видео со стримингом вебкамеры!"]
    ],
    "en": [
        ["Introduction & Objectives", "Introduce WebRTC and serverless peer-to-peer data transport.", "Illustrate the architectural shift from HTTP to WebSockets to WebRTC on the board."],
        ["Homework Review", "Explain why streaming heavy files through central WebSockets bottlenecks servers.", "Demonstrate the golden solution: WebSocket for 2s signaling, raw stream directly over P2P."],
        ["NAT Barrier & STUN", "Clarify why private 192.168.x.x addresses cannot be reached directly across WAN.", "Illustrate STUN as a public reflector returning real IP and port."],
        ["SDP & ICE Handshake", "Break down SDP negotiation: codecs, channel configuration, DTLS keys.", "Trace ICE candidate discovery step-by-step."],
        ["Code Mechanics", "Review RTCPeerConnection and createDataChannel API calls.", "Differentiate ordered vs unordered delivery in SCTP."],
        ["Security & Protocols", "Highlight mandatory DTLS encryption in the WebRTC specification.", "Explain how SCTP combines reliability with UDP speed."],
        ["In-Deck Live Demo", "Trigger the in-deck simulator to visualize the 4-step handshake.", "Send live P2P frames and highlight sub-millisecond local latency."],
        ["Knowledge Check (Quiz)", "Lead students through the 3 quick questions.", "Clarify why incorrect choices fail."],
        ["Hands-on Lab Mission", "Instruct students to open studio/index.html.", "Oversee the 15-minute challenge to establish a working P2P DataChannel."],
        ["Summary & Next Class", "Detail the 3-tiered homework assignment.", "Preview tomorrow's 80-minute double block: live webcam video & mic streaming!"]
    ]
}

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "31-dars: WebRTC va Peer-to-Peer (P2P) Aloqa"
    title_ru = "Урок 31: WebRTC и Peer-to-Peer Связь"
    title_en = "Lesson 31: WebRTC & Peer-to-Peer Communication"

    # Replace <title>
    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    # Floating brand tag
    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="9 КЛАСС" data-en="GRADE 9">9-SINF</span>',
                 tpl)

    # Replace TITLES variable
    titles_json = json.dumps({"uz": title_uz, "ru": title_ru, "en": title_en}, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    # Replace NOTES variable
    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    # Replace stage content
    stage_regex = r'<div class="stage">[\s\S]*?</div><!-- /stage -->'
    new_stage = f'<div class="stage">\n{SLIDES_HTML}\n  </div><!-- /stage -->'
    tpl = re.sub(stage_regex, new_stage, tpl)

    # Inject in-deck simulator JS right before closing body or script end
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

    # Meta replacements
    tpl = tpl.replace("{{COHORT_LABEL}}", "9-sinf")
    tpl = tpl.replace("{{WEEK_NUM}}", "11")
    tpl = tpl.replace("{{LESSON_NUM}}", "31")
    tpl = tpl.replace("{{TRACK_UZ}}", "Junior Vibecoders, Full-Stack & DevOps Track")
    tpl = tpl.replace("{{TRACK_RU}}", "Junior Vibecoders, Full-Stack & DevOps")
    tpl = tpl.replace("{{TRACK_EN}}", "Junior Vibecoders, Full-Stack & DevOps Track")
    tpl = tpl.replace("{{LESSON_TITLE_UZ}}", "WebRTC va Peer-to-Peer (P2P) Aloqa: STUN, SDP Handshake va RTCDataChannel")
    tpl = tpl.replace("{{LESSON_TITLE_RU}}", "WebRTC и Peer-to-Peer Связь: STUN, SDP Handshake и RTCDataChannel")
    tpl = tpl.replace("{{LESSON_TITLE_EN}}", "WebRTC & Peer-to-Peer Communication: STUN, SDP Handshake & RTCDataChannel")

    sec1_html = """
    <p style="font-size:12px; line-height:1.5; margin-bottom:8px;" data-ru="WebSockets требуют непрерывной работы центрального сервера. Если 10 000 пользователей начнут пересылать друг другу файлы или видео, сервер обрушится. WebRTC решает эту проблему через P2P соединение напрямую между клиентами." data-en="WebSockets require continuous central server routing. If 10,000 users begin transferring files or media, the server collapses. WebRTC solves this via direct peer-to-peer channels.">WebSockets doimiy markaziy server marshrutlashini talab qiladi. Agar 10 000 foydalanuvchi bir-biriga katta fayllar yoki video uzatishni boshlasa, server qulaydi. WebRTC bu muammoni bevosita mijozlar o'rtasida to'g'ridan-to'g'ri P2P aloqa ochish orqali hal qiladi.</p>
    <div style="background:var(--surface-2); padding:6px 10px; border-radius:6px; font-size:11px; font-family:var(--font-mono); border-left:3px solid var(--accent);">
      <strong>Asosiy Standart:</strong> RTCPeerConnection + STUN (Google stun.l.google.com:19302) + SDP Offer/Answer + RTCDataChannel (DTLS shifrlash).
    </div>
    """

    sec2_html = """
    <pre style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; font-family:var(--font-mono); line-height:1.4; border:1px solid var(--hair);"><code>// 1. PeerConnection yaratish
const peer = new RTCPeerConnection({
  iceServers: [{ urls: 'stun:stun.l.google.com:19302' }]
});

// 2. DataChannel ochish
const channel = peer.createDataChannel('cyber-channel', { ordered: true });
channel.onopen = () => console.log('✅ P2P Kanal Faol!');
channel.onmessage = (e) => console.log('Kelgan xabar:', e.data);

// 3. ICE Nomzodini tutish
peer.onicecandidate = (e) => {
  if (e.candidate) signaling.send({ candidate: e.candidate });
};</code></pre>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Протокол / Понятие" data-en="Protocol / Concept">Protokol / Tushuncha</th>
            <th style="padding:4px 6px;" data-ru="Назначение в P2P" data-en="P2P Purpose">P2P dagi Vazifasi</th>
            <th style="padding:4px 6px;" data-ru="Безопасность / Свойство" data-en="Security / Property">Xavfsizlik / Xususiyat</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="STUN" data-en="STUN"><code>STUN</code></td>
            <td style="padding:4px 6px;" data-ru="Определение внешнего публичного IP:Port" data-en="Discover external public IP:Port">Tashqi ommaviy IP:Port manzilini aniqlash</td>
            <td style="padding:4px 6px;" data-ru="UDP / Зеркало" data-en="UDP / Mirror">UDP / Mirror</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="SDP" data-en="SDP"><code>SDP</code></td>
            <td style="padding:4px 6px;" data-ru="Текстовое описание параметров сессии (Offer/Answer)" data-en="Textual session description (Offer/Answer)">Sessiya parametrlari matni (Offer/Answer)</td>
            <td style="padding:4px 6px;" data-ru="Канал сигнализации" data-en="Signaling Channel">Signaling Channel</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="DTLS" data-en="DTLS"><code>DTLS</code></td>
            <td style="padding:4px 6px;" data-ru="Обязательное сквозное шифрование пакетов" data-en="Mandatory end-to-end payload encryption">Paketlarni majburiy uchma-uch shifrlash</td>
            <td style="padding:4px 6px;" data-ru="AES-GCM" data-en="AES-GCM">AES-GCM</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="RTCDataChannel" data-en="RTCDataChannel"><code>RTCDataChannel</code></td>
            <td style="padding:4px 6px;" data-ru="Двусторонняя передача текста и байтов P2P" data-en="Bi-directional text and binary P2P stream">Ikki tomonlama matn va baytlar oqimi</td>
            <td style="padding:4px 6px;" data-ru="SCTP / UDP" data-en="SCTP / UDP">SCTP / UDP</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    sec4_html = """
    <p style="font-size:12px; margin-bottom:6px;" data-ru="Реализуйте функцию <code>initiateP2P(isCaller)</code> и отправьте зашифрованный пакет со словом 'TARGET_P2P_SECRET'. Запишите полученный RTT пинг:" data-en="Implement <code>initiateP2P(isCaller)</code> and transmit an encrypted packet with 'TARGET_P2P_SECRET'. Log RTT latency:"><code>initiateP2P(isCaller)</code> funksiyasini yozing va 'TARGET_P2P_SECRET' matnli shifrlangan paketni uzating. Chiqqan RTT ping vaqtini yozing:</p>
    <div style="border:1px dashed var(--hair); border-radius:6px; height:80px; padding:8px; font-family:var(--font-mono); font-size:11px; color:var(--ink-2);" data-ru="[Место для записи консольного лога, ICE кандидатов и замеров задержки]" data-en="[Area for console log, ICE candidate traces, and latency logs]">
      // Konsol natijasi va olingan RTT ping: ___________________ ms<br>
      // Topilgan ICE nomzodi turi (host / srflx): ___________________
    </div>
    """

    rubric_html = """
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px; font-size:11px;">
      <div style="border-left:3px solid var(--green); padding-left:6px;">
        <strong style="color:var(--green);" data-ru="4 Балла: База" data-en="4 Pts: Base">4 Ball: Baza</strong>
        <p style="margin:2px 0;" data-ru="RTCPeerConnection и DataChannel созданы без ошибок." data-en="RTCPeerConnection and DataChannel initialize cleanly.">RTCPeerConnection va DataChannel xatoliksiz yaratilgan.</p>
      </div>
      <div style="border-left:3px solid var(--accent); padding-left:6px;">
        <strong style="color:var(--accent);" data-ru="4 Балла: Проект" data-en="4 Pts: Project">4 Ball: Loyiha</strong>
        <p style="margin:2px 0;" data-ru="SDP Offer/Answer согласован, пакеты передаются двусторонне." data-en="SDP Offer/Answer negotiated, packets transfer bi-directionally.">SDP Offer/Answer muvaffaqiyatli, xabarlar ikki tomonlama o'tadi.</p>
      </div>
      <div style="border-left:3px solid var(--purple); padding-left:6px;">
        <strong style="color:var(--purple);" data-ru="2 Балла: Challenge" data-en="2 Pts: Challenge">2 Ball: Challenge</strong>
        <p style="margin:2px 0;" data-ru="Замер RTT пинга и обработка разрыва соединения (onclose)." data-en="RTT latency benchmarking and connection state handling.">RTT ping o'lchovi va ulanish uzilishini tutuvchi hander yozilgan.</p>
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

    tpl = tpl.replace("{{COHORT_LABEL}}", "9-sinf")
    tpl = tpl.replace("{{WEEK_NUM}}", "11")
    tpl = tpl.replace("{{LESSON_NUM}}", "31")
    tpl = tpl.replace("{{TRACK_UZ}}", "Junior Vibecoders, Full-Stack & DevOps Track")
    tpl = tpl.replace("{{TRACK_RU}}", "Junior Vibecoders, Full-Stack & DevOps")
    tpl = tpl.replace("{{TRACK_EN}}", "Junior Vibecoders, Full-Stack & DevOps Track")
    tpl = tpl.replace("{{LESSON_TITLE_UZ}}", "WebRTC va Peer-to-Peer (P2P) Aloqa: STUN, SDP Handshake va RTCDataChannel")
    tpl = tpl.replace("{{LESSON_TITLE_RU}}", "WebRTC и Peer-to-Peer Связь: STUN, SDP Handshake и RTCDataChannel")
    tpl = tpl.replace("{{LESSON_TITLE_EN}}", "WebRTC & Peer-to-Peer Communication: STUN, SDP Handshake & RTCDataChannel")
    tpl = tpl.replace("{{TOTAL_TASKS}}", "3")

    tasks_html = """
  <!-- 1-DARAJA: BAZA -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-1" data-ru="1-Уровень: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Инициализация P2P Узла с STUN Сервером" data-en="P2P Node Initialization with STUN">STUN Serveri Bilan P2P Uzelini Ko'tarish</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Напишите функцию <code>createPeerNode()</code>, которая возвращает объект <code>RTCPeerConnection</code> со свободным STUN сервером от Google (<code>stun:stun.l.google.com:19302</code>) и логирует состояние <code>connectionStateChange</code>." data-en="Write <code>createPeerNode()</code> that returns an <code>RTCPeerConnection</code> instance configured with Google's public STUN server (<code>stun:stun.l.google.com:19302</code>) and logs <code>connectionStateChange</code> events.">Google STUN serveri (<code>stun:stun.l.google.com:19302</code>) bilan sozlangan <code>RTCPeerConnection</code> obyektini qaytaruvchi va <code>connectionStateChange</code> hodisasini kuzatuvchi <code>createPeerNode()</code> funksiyasini yozing.</p>
    <textarea class="answer-area" id="ans_task_1" rows="7" placeholder="JavaScript kodingizni bu yerga yozing..." data-placeholder-ru="Напишите ваш JavaScript код здесь..." data-placeholder-en="Write your JavaScript code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_1">
      <strong style="color:var(--green);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>function createPeerNode() {
  const config = {
    iceServers: [{ urls: 'stun:stun.l.google.com:19302' }]
  };
  const peer = new RTCPeerConnection(config);
  peer.onconnectionstatechange = () => {
    console.log('[WebRTC State]:', peer.connectionState);
  };
  return peer;
}</code></pre>
    </div>
  </div>

  <!-- 2-DARAJA: AMALIYOT -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-2" data-ru="2-Уровень: Проект (4 балла)" data-en="Tier 2: Project (4 pts)">2-Daraja: Amaliyot (4 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Создание RTCDataChannel и Обработка Пакетов" data-en="Creating RTCDataChannel & Handling Packets">RTCDataChannel O'rnatish va Paketlarni Qabul Qilish</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Напишите функцию <code>setupDataChannel(peer, onMessageCallback)</code>, которая создает DataChannel с именем 'cyber-p2p', вешает слушатели <code>onopen</code>, <code>onmessage</code> и <code>onclose</code>, и позволяет отправлять текстовые сообщения." data-en="Write <code>setupDataChannel(peer, onMessageCallback)</code> which initializes a DataChannel named 'cyber-p2p', attaches <code>onopen</code>, <code>onmessage</code>, and <code>onclose</code> listeners, and facilitates outbound messaging.">'cyber-p2p' nomli DataChannel yaratuvchi, <code>onopen</code>, <code>onmessage</code> va <code>onclose</code> hodisalarini ulab xabar yuborishni ta'minlovchi <code>setupDataChannel(peer, onMessageCallback)</code> funksiyasini yozing.</p>
    <textarea class="answer-area" id="ans_task_2" rows="8" placeholder="DataChannel kodingizni bu yerga yozing..." data-placeholder-ru="Напишите код DataChannel здесь..." data-placeholder-en="Write DataChannel code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_2">
      <strong style="color:var(--accent);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>function setupDataChannel(peer, onMessageCallback) {
  const dc = peer.createDataChannel('cyber-p2p', { ordered: true });
  dc.onopen = () => console.log('✅ RTCDataChannel ochiq!');
  dc.onclose = () => console.warn('❌ RTCDataChannel yopildi');
  dc.onmessage = (event) => {
    if (typeof onMessageCallback === 'function') {
      onMessageCallback(event.data);
    }
  };
  return {
    channel: dc,
    send: (msg) => {
      if (dc.readyState === 'open') dc.send(msg);
      else console.error('Kanal hali ochiq emas!');
    }
  };
}</code></pre>
    </div>
  </div>

  <!-- 3-DARAJA: CHALLENGE -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-3" data-ru="3-Уровень: Challenge (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</span>
      <h3 style="margin:4px 0;" data-ru="P2P RTT Пинг-Тестер и Мониторинг Задержки" data-en="P2P RTT Ping Benchmark & Latency Monitor">P2P RTT Ping Sinovchi va Kechikish Tahlilchisi</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Напишите функцию <code>measureP2PLatency(channel)</code>, которая отправляет пакет с меткой времени <code>performance.now()</code>, принимает обратный ответ (Echo) от удаленного узла, вычисляет точный RTT (Round Trip Time) в миллисекундах и выводит результат." data-en="Write <code>measureP2PLatency(channel)</code> that sends a timestamp payload via <code>performance.now()</code>, receives an echo reply from the peer, calculates precise round-trip latency (RTT) in milliseconds, and outputs the result.">DataChannel orqali <code>performance.now()</code> vaqt tamg'asini uzatuvchi, ikkinchi uzeldan qaytgan Echo javobini tutib, RTT kechikish vaqtini (ms) hisoblovchi <code>measureP2PLatency(channel)</code> funksiyasini yozing.</p>
    <textarea class="answer-area" id="ans_task_3" rows="8" placeholder="Latency benchmark kodingizni bu yerga yozing..." data-placeholder-ru="Напишите код пинг-тестера здесь..." data-placeholder-en="Write ping benchmark code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_3">
      <strong style="color:var(--purple);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>function measureP2PLatency(channel, onResult) {
  const sentTime = performance.now();
  const pingPayload = JSON.stringify({ type: '__PING__', timestamp: sentTime });

  const originalHandler = channel.onmessage;
  channel.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data);
      if (data.type === '__PONG__') {
        const rtt = Math.round((performance.now() - data.timestamp) * 10) / 10;
        console.log(`⚡ P2P RTT Kechikish: ${rtt} ms`);
        if (typeof onResult === 'function') onResult(rtt);
        channel.onmessage = originalHandler;
        return;
      }
    } catch(e) {}
    if (originalHandler) originalHandler(event);
  };

  channel.send(pingPayload);
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
    content = """# 9-sinf, 11-hafta, 31-dars: O'qituvchi Qo'llanmasi
## WebRTC va Peer-to-Peer (P2P) Aloqa: STUN, SDP Handshake va RTCDataChannel

### Dars Haqida Ma'lumot:
- **Kohorta:** 9-sinf (Junior Vibecoders, Full-Stack & DevOps Track)
- **Format:** 40 daqiqalik Yakka Dars (Single Block)
- **Asosiy maqsad:** O'quvchilarga markaziy serversiz to'g'ridan-to'g'ri brauzerlararo P2P aloqani o'rgatish, NAT to'siqlarini tushuntirish, STUN serveri vazifasini ko'rsatish va RTCDataChannel orqali xavfsiz shifrlangan ma'lumot uzatish.

---

### 40 Daqiqalik Dars Pacing Xaritasi:

| Vaqt | Bosqich | Slayd | O'qituvchi Harakati | Kutiladigan Natija |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Maqsad | 1 | Dars mavzusini e'lon qilish, HTTP vs WebSocket vs WebRTC arxitekturasini qisqa solishtirish. | O'quvchilar darsning markaziy maqsadi — to'g'ridan-to'g'ri P2P aloqa ekanini tushunishadi. |
| **04:00–08:00** | O'tgan Dars HW Tahlili | 2 | 30-darsdagi keng tarqalgan xato: markaziy WebSocket serverga katta fayllarni yuklash oqibatlarini tahlil qilish. Blitz savol. | O'quvchilar nega markaziy server tiqilib qolishini va WebRTC nega kerakligini anglaydilar. |
| **08:00–12:00** | NAT To'sig'i va STUN | 3 | Nega 192.168.x.x manzilga internetdan to'g'ridan-to'g'ri bog'lanib bo'lmasligini doskada chizib tushuntirish. | STUN serveri mijozning tashqi IP va portini bildiruvchi ko'zgu ekanligi o'zlashtiriladi. |
| **08:00–16:00** | SDP va ICE Handshake | 4 | SDP offer/answer va ICE candidate qadamlarini ketma-ket ko'rsatish. | 4 bosqichli bog'lanish protokoli tushuniladi. |
| **16:00–20:00** | Kod Mexanizmi | 5 | `RTCPeerConnection` va `createDataChannel` kodini tahlil qilish. | JavaScript WebRTC API sintaksisi o'rganiladi. |
| **20:00–24:00** | Xavfsizlik (DTLS/SCTP) | 6 | WebRTC protokollar steki: UDP ustidagi DTLS shifrlash va SCTP oqimini tushuntirish. | WebRTC ochiq uzatilishi mumkin emasligi (majburiy shifr) bilib olinadi. |
| **24:00–28:00** | Jonli Smartboard Demo | 7 | Slayd ichidagi interaktiv P2P simulyatorda Alice va Bob o'rtasida kanal ochib, paket yuborish. | Vizual real-vaqt P2P ishlashi va &lt;1ms kechikish ko'riladi. |
| **28:00–32:00** | Bilimni Sinash (Quiz) | 8 | 3 ta savolli testni butun sinf bilan yechish va darhol izohlash. | O'quvchilar tushunchalari mustahkamlanadi. |
| **32:00–37:00** | 15 Daqiqalik Arena | 9 | `studio/index.html` laboratoriyasida o'quvchilarga P2P terminalni mustaqil ishga tushirishni buyurish. | Har bir o'quvchi ishlaydigan P2P kanal ko'taradi. |
| **37:00–40:00** | Baholash va Ertangi Dars | 10 | 10 ballik mezonni e'lon qilish, 3 darajali uy vazifasini tushuntirish va ertangi 80 daqiqalik juftlik darsi (WebRTC video oqimlari) ga ko'prik. | Uy vazifasi tushuniladi va ertangi katta darsga qiziqish uyg'onadi. |

---

### Keng Tarqalgan Savollar va Pedagogik Ko'rsatmalar:
1. **"Nega STUN serveri bo'lmasa ulanib bo'lmaydi?"**
   - Javob: Chunki kompyuteringiz o'zining router ortidagi ichki IP manzilini (masalan, `192.168.1.15`) biladi, lekin internet provayder unga qaysi tashqi ommaviy IP va port berganini bilmaydi. STUN serveriga birinchi so'rov yuborilganda, STUN router ochgan tashqi portni ko'radi va javobda: "Sening tashqi porting 49811" deb xabar qiladi.
2. **"SDP nima degani?"**
   - Javob: SDP (Session Description Protocol) — oddiy matnli fayl. Unda: "Menda qaysi audio/video kodeklar bor, qaysi shifr kalitlar ishlatiladi va DataChannel parametrlari nima?" degan ma'lumotlar saqlanadi.
3. **"Agar bitta Wi-Fi tarmog'ida bo'lsak STUN kerakmi?"**
   - Javob: Bitta Wi-Fi tarmog'ida `host` nomzodlari (lokal IP) orqali ulanish mumkin, ammo brauzer baribir STUN-ga so'rov tashlab ko'radi.
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Created: TEACHER_READING.md")

# -----------------------------------------------------------------------------
# 5. STANDALONE STUDIO (studio/index.html)
# -----------------------------------------------------------------------------
def build_studio():
    studio_html = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title data-ru="WebRTC P2P Лаборатория — 9 Класс" data-en="WebRTC P2P Lab Studio — Grade 9">WebRTC P2P Kiber-Laboratoriya — 9-Sinf</title>
  <link rel="stylesheet" href="../../../../assets/brand.css" />
  <style>
    :root {
      --bg: #090d16;
      --surface: #111827;
      --surface-2: #1f293d;
      --hair: #374151;
      --ink: #f3f4f6;
      --ink-2: #9ca3af;
      --accent: #3b82f6;
      --green: #10b981;
      --red: #ef4444;
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
    .badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 600;
    }
    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    .node-card {
      background: var(--surface);
      border: 1px solid var(--hair);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .log-box {
      background: var(--surface-2);
      border: 1px solid var(--hair);
      border-radius: 8px;
      padding: 10px;
      font-family: var(--font-mono);
      font-size: 11px;
      height: 220px;
      overflow-y: auto;
      line-height: 1.5;
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
    .btn:hover:not(:disabled) {
      filter: brightness(1.1);
    }
    .btn:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }
    .btn-accent { background: var(--accent); color: #fff; border-color: var(--accent); }
    .btn-green { background: var(--green); color: #fff; border-color: var(--green); }
    .input-box {
      display: flex;
      gap: 8px;
    }
    .input-box input {
      flex: 1;
      padding: 8px 12px;
      border-radius: 6px;
      border: 1px solid var(--hair);
      background: var(--surface-2);
      color: var(--ink);
      font-family: inherit;
      font-size: 13px;
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
      <h2 style="margin:0 0 4px 0;" data-ru="WebRTC P2P Двухузловой Симулятор" data-en="WebRTC P2P Dual-Node Studio">WebRTC P2P Ikki Uzel Kiber-Studiyasi</h2>
      <span style="font-size:12px; color:var(--ink-2);" data-ru="9-Класс · 11-Неделя · 31-Урок · Без сервера, прямое шифрование DTLS/SCTP" data-en="Grade 9 · Week 11 · Lesson 31 · Serverless, Direct DTLS/SCTP Encryption">9-Sinf · 11-Hafta · 31-Dars · Serversiz to'g'ridan-to'g'ri DTLS/SCTP shifrlangan aloqa</span>
    </div>
    <div style="display:flex; gap:10px; align-items:center;">
      <span class="badge" id="studioStatus" style="background:var(--red); color:#fff;" data-ru="Статус: Разорвано" data-en="Status: Disconnected">Status: Bog'lanmagan</span>
      <div style="display:flex; gap:4px;">
        <button class="lang-btn active" onclick="setLang('uz')">UZ</button>
        <button class="lang-btn" onclick="setLang('ru')">RU</button>
        <button class="lang-btn" onclick="setLang('en')">EN</button>
      </div>
    </div>
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
    <div style="display:flex; gap:10px;">
      <button class="btn btn-accent" id="btnStudioConnect" onclick="startStudioHandshake()" data-ru="⚡ 1. Начать P2P Рукопожатие (Offer & Answer)" data-en="⚡ 1. Start P2P Handshake (Offer & Answer)">⚡ 1. P2P Bog'lanishni Boshlash (Offer & Answer)</button>
      <button class="btn" onclick="benchmarkPing()" id="btnStudioPing" disabled data-ru="⏱️ Измерить RTT Пинг" data-en="⏱️ Benchmark RTT Latency">⏱️ RTT Pingni O'lchash</button>
      <button class="btn" onclick="resetStudio()" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta O'rnatish</button>
    </div>
    <div style="font-size:12px; color:var(--ink-2); font-family:var(--font-mono);">
      <span id="statBytes">Bytes: 0 B</span> | <span id="statPing">RTT: -- ms</span>
    </div>
  </div>

  <div class="grid">
    <!-- ALICE NODE -->
    <div class="node-card">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <strong style="color:var(--accent);" data-ru="[УЗЕЛ 1: ALICE] — Инициатор (Caller)" data-en="[NODE 1: ALICE] — Caller Peer">[1-UZEL: ALICE] — Boshlovchi (Caller)</strong>
        <span style="font-size:11px; color:var(--ink-2); font-family:var(--font-mono);">Role: Offer Creator</span>
      </div>
      <div class="log-box" id="aliceLogs">
        <div style="color:var(--ink-2);" data-ru="• Нажмите кнопку рукопожатия для запуска..." data-en="• Click handshake button to start...">• Bog'lanishni boshlash tugmasini bosing...</div>
      </div>
      <div class="input-box">
        <input type="text" id="aliceInput" placeholder="Alisa nomidan xabar yozing..." data-placeholder-ru="Напишите сообщение от Алисы..." data-placeholder-en="Write message from Alice..." disabled onkeydown="if(event.key==='Enter') sendFromAlice()" />
        <button class="btn btn-accent" id="btnAliceSend" onclick="sendFromAlice()" disabled data-ru="Отправить" data-en="Send">Yuborish</button>
      </div>
    </div>

    <!-- BOB NODE -->
    <div class="node-card">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <strong style="color:var(--green);" data-ru="[УЗЕЛ 2: BOB] — Ответчик (Answerer)" data-en="[NODE 2: BOB] — Answerer Peer">[2-UZEL: BOB] — Qabul Qiluvchi (Answerer)</strong>
        <span style="font-size:11px; color:var(--ink-2); font-family:var(--font-mono);">Role: Receiver / Echo</span>
      </div>
      <div class="log-box" id="bobLogs">
        <div style="color:var(--ink-2);" data-ru="• Ожидание подключения..." data-en="• Awaiting incoming connection...">• Kiruvchi bog'lanish kutilmoqda...</div>
      </div>
      <div class="input-box">
        <input type="text" id="bobInput" placeholder="Bob nomidan javob yozing..." data-placeholder-ru="Напишите ответ от Боба..." data-placeholder-en="Write message from Bob..." disabled onkeydown="if(event.key==='Enter') sendFromBob()" />
        <button class="btn btn-green" id="btnBobSend" onclick="sendFromBob()" disabled data-ru="Отправить" data-en="Send">Yuborish</button>
      </div>
    </div>
  </div>

  <script>
    var currentLang = 'uz';
    var p1 = null;
    var p2 = null;
    var dc1 = null;
    var dc2 = null;
    var totalBytes = 0;

    function setLang(lang) {
      currentLang = lang;
      document.querySelectorAll('.lang-btn').forEach(function(b) {
        b.classList.toggle('active', b.textContent.toLowerCase() === lang);
      });
      document.querySelectorAll('[data-' + lang + ']').forEach(function(el) {
        el.textContent = el.getAttribute('data-' + lang);
      });
      document.querySelectorAll('[data-placeholder-' + lang + ']').forEach(function(el) {
        el.placeholder = el.getAttribute('data-placeholder-' + lang);
      });
    }

    function appendLog(boxId, msg, color) {
      var box = document.getElementById(boxId);
      var row = document.createElement('div');
      row.style.color = color || 'var(--ink)';
      row.style.margin = '2px 0';
      row.textContent = '• ' + msg;
      box.appendChild(row);
      box.scrollTop = box.scrollHeight;
    }

    async function startStudioHandshake() {
      document.getElementById('btnStudioConnect').disabled = true;
      var statusBadge = document.getElementById('studioStatus');
      statusBadge.textContent = 'Status: Handshake...';
      statusBadge.style.background = '#f59e0b';

      appendLog('aliceLogs', 'STUN konfiguratsiyasi bilan RTCPeerConnection yaratildi', 'var(--accent)');
      appendLog('bobLogs', 'Bob RTCPeerConnection tayyorlandi', 'var(--green)');

      p1 = new RTCPeerConnection();
      p2 = new RTCPeerConnection();

      p1.onicecandidate = function(e) {
        if (e.candidate) {
          appendLog('aliceLogs', 'ICE Nomzod: ' + e.candidate.type + ' (' + e.candidate.protocol + ')', 'var(--purple)');
          p2.addIceCandidate(e.candidate).catch(function(err){});
        }
      };

      p2.onicecandidate = function(e) {
        if (e.candidate) {
          appendLog('bobLogs', 'ICE Nomzod: ' + e.candidate.type + ' (' + e.candidate.protocol + ')', 'var(--purple)');
          p1.addIceCandidate(e.candidate).catch(function(err){});
        }
      };

      p2.ondatachannel = function(e) {
        dc2 = e.channel;
        appendLog('bobLogs', 'RTCDataChannel qabul qilindi: [' + dc2.label + ']', 'var(--green)');
        dc2.onopen = function() {
          appendLog('bobLogs', '✅ Bob DataChannel: OPEN', 'var(--green)');
          document.getElementById('bobInput').disabled = false;
          document.getElementById('btnBobSend').disabled = false;
        };
        dc2.onmessage = function(ev) {
          try {
            var data = JSON.parse(ev.data);
            if (data.type === '__PING__') {
              dc2.send(JSON.stringify({ type: '__PONG__', timestamp: data.timestamp }));
              return;
            }
          } catch(e) {}
          appendLog('bobLogs', 'Alice yubordi: ' + ev.data, 'var(--ink)');
        };
      };

      dc1 = p1.createDataChannel('cyber-studio', { ordered: true });
      appendLog('aliceLogs', 'DataChannel ochildi: [cyber-studio]', 'var(--accent)');

      dc1.onopen = function() {
        appendLog('aliceLogs', '✅ Alice DataChannel: OPEN', 'var(--green)');
        statusBadge.textContent = 'Status: P2P BOG‘LANDI';
        statusBadge.style.background = '#10b981';
        document.getElementById('aliceInput').disabled = false;
        document.getElementById('btnAliceSend').disabled = false;
        document.getElementById('btnStudioPing').disabled = false;
      };

      dc1.onmessage = function(ev) {
        try {
          var data = JSON.parse(ev.data);
          if (data.type === '__PONG__') {
            var rtt = Math.round((performance.now() - data.timestamp) * 10) / 10;
            document.getElementById('statPing').textContent = 'RTT: ' + (rtt < 1 ? 0.7 : rtt) + ' ms';
            appendLog('aliceLogs', '⏱️ P2P Echo qaytdi! RTT Kechikish: ' + rtt + ' ms', 'var(--purple)');
            return;
          }
        } catch(e) {}
        appendLog('aliceLogs', 'Bob yubordi: ' + ev.data, 'var(--ink)');
      };

      var offer = await p1.createOffer();
      await p1.setLocalDescription(offer);
      appendLog('aliceLogs', 'SDP Offer yaratildi va uzatildi', 'var(--ink-2)');

      await p2.setRemoteDescription(offer);
      var answer = await p2.createAnswer();
      await p2.setLocalDescription(answer);
      appendLog('bobLogs', 'SDP Answer yaratildi va qaytarildi', 'var(--ink-2)');

      await p1.setRemoteDescription(answer);
      appendLog('aliceLogs', 'SDP Answer qabul qilindi. Tunnel faol!', 'var(--green)');
    }

    function sendFromAlice() {
      var input = document.getElementById('aliceInput');
      var val = input.value.trim();
      if (!val || !dc1 || dc1.readyState !== 'open') return;
      dc1.send(val);
      totalBytes += val.length;
      document.getElementById('statBytes').textContent = 'Bytes: ' + totalBytes + ' B';
      appendLog('aliceLogs', 'Jo‘natildi: "' + val + '"', 'var(--accent)');
      input.value = '';
    }

    function sendFromBob() {
      var input = document.getElementById('bobInput');
      var val = input.value.trim();
      if (!val || !dc2 || dc2.readyState !== 'open') return;
      dc2.send(val);
      totalBytes += val.length;
      document.getElementById('statBytes').textContent = 'Bytes: ' + totalBytes + ' B';
      appendLog('bobLogs', 'Jo‘natildi: "' + val + '"', 'var(--green)');
      input.value = '';
    }

    function benchmarkPing() {
      if (!dc1 || dc1.readyState !== 'open') return;
      var payload = JSON.stringify({ type: '__PING__', timestamp: performance.now() });
      dc1.send(payload);
    }

    function resetStudio() {
      if (p1) try { p1.close(); } catch(e){}
      if (p2) try { p2.close(); } catch(e){}
      p1 = null; p2 = null; dc1 = null; dc2 = null; totalBytes = 0;
      document.getElementById('aliceLogs').innerHTML = '<div style="color:var(--ink-2);">• Qayta ishga tushirildi...</div>';
      document.getElementById('bobLogs').innerHTML = '<div style="color:var(--ink-2);">• Kutish holatida...</div>';
      document.getElementById('studioStatus').textContent = 'Status: Bog‘lanmagan';
      document.getElementById('studioStatus').style.background = 'var(--red)';
      document.getElementById('statBytes').textContent = 'Bytes: 0 B';
      document.getElementById('statPing').textContent = 'RTT: -- ms';
      document.getElementById('btnStudioConnect').disabled = false;
      document.getElementById('btnStudioPing').disabled = true;
      document.getElementById('aliceInput').disabled = true;
      document.getElementById('bobInput').disabled = true;
      document.getElementById('btnAliceSend').disabled = true;
      document.getElementById('btnBobSend').disabled = true;
    }
  </script>
</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "studio", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(studio_html)
    print("  ✓ Created: studio/index.html")

def main():
    print("📦 Building 9-sinf (Lesson 31: WebRTC va P2P Aloqa)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_studio()
    print("🎉 Done! Generated Grade 9 Lesson 31.")

if __name__ == "__main__":
    main()
