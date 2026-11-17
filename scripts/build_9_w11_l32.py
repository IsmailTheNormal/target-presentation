#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_9_w11_l32.py — Builder for 9th Grade, Week 11, Lesson 32

Mavzu: WebRTC MediaStream va Jonli P2P Mesh: Video, Audio va Ekran Ulashish (Screen Sharing & Encrypted P2P Video Calls)
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 9-sinf (Junior Vibecoders, Full-Stack & DevOps Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "9-sinf", "11-hafta", "32-dars-webrtc-mediastream-va-video-chat")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "studio"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="9-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 32" data-en="GRADE 9 · WEEK 11 · LESSON 32">9-SINF · 11-HAFTA · 32-DARS</span></div>
    <h1 class="display" data-ru="WebRTC MediaStream: Видео, Аудио и Стриминг Экрана P2P" data-en="WebRTC MediaStream: Live Video, Audio & Screen Sharing P2P">WebRTC MediaStream: Jonli Video, Audio va Ekran Ulashish P2P</h1>
    <p class="lede" data-ru="Прямая трансляция веб-камеры, захват микрофона через getUserMedia, шаринг экрана (getDisplayMedia) и аппаратное шифрование SRTP без промежуточных серверов." data-en="Direct peer-to-peer webcam streaming, microphone capture via getUserMedia, screen sharing (getDisplayMedia), and hardware-accelerated SRTP encryption without server intermediaries.">Veb-kamera va mikrofondan jonli oqim olish (getUserMedia), ekranni ulashish (getDisplayMedia) va hech qanday serverlarsiz to'g'ridan-to'g'ri SRTP orqali shifrlangan P2P video-qo'ng'iroq tizimi.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Стриминг Реального Времени" data-en="Real-Time Media Pipeline">MediaStream Quvuri</h3>
        <p data-ru="Как современные приложения (Discord, Zoom, Google Meet) передают 60 FPS видео напрямую между клиентами." data-en="How modern tools (Discord, Zoom, Google Meet) transmit 60 FPS video streams directly between peers.">Qanday qilib Discord, Zoom va Google Meet 60 FPS video oqimini to'g'ridan-to'g'ri brauzerlararo uzatadi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Jonli Video Chat</div>
        <h3 data-ru="P2P Видеотерминал" data-en="P2P Video Studio">Shifrlangan Video-Qo'ng'iroq</h3>
        <p data-ru="Каждый ученик поднимет живую видеосвязь с веб-камеры, наложит холст-фильтры и протестирует шаринг экрана." data-en="Each student initializes live webcam video, applies real-time Canvas filters, and tests screen sharing.">Har bir o'quvchi jonli video-aloqani ko'taradi, Canvas filtrlarini qo'llaydi va ekran ulashishni sinaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 31-УРОКА" data-en="LESSON 31 HOMEWORK REVIEW">31-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="WebRTC DataChannel: Ловушка Передачи Видео через Base64 Текст" data-en="WebRTC DataChannel: The Base64 Video String Trap">WebRTC DataChannel: Videoni Base64 Matn Qilib Uzatish Xatosi</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Типичная ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Кодирование кадров видео в Base64 и отправка в DataChannel" data-en="Encoding Video Frames into Base64 via DataChannel">Kadrni toDataURL('base64') Qilib DataChannel Orqali Yuborish</h3>
        <p data-ru="Ученики пытались захватывать холст в строку Base64 и слать через send(text). Результат: браузер зависает от сборщика мусора (GC), нагрузка на сеть вырастает на 33% из-за оверхеда Base64, а FPS падает до 5 кадров в секунду!" data-en="Students converted canvas frames into Base64 strings and spammed dataChannel.send(). Result: brutal garbage collection freezes, a 33% bandwidth penalty, and framerates tanking to 5 FPS!">O'quvchilar har bir kadrni Base64 matniga aylantirib DataChannel orqali yuborishga urindilar. Natijada xotira to'lib brauzer qotib qoldi, hajm 33% ga oshib ketdi va tezlik 5 FPS gacha tushib ketdi!</p>
        <pre><code>// ❌ Xato: Videoni matn qilib jo'natish
channel.send(canvas.toDataURL()); // 33% ortiqcha bayt va qotish!</code></pre>
      </div>
      <div class="box success-border">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой стандарт (Golden Solution)" data-en="Golden Standard">Oltin Standart (Golden Solution)</div>
        <h3 data-ru="Нативные медиатреки через RTCPeerConnection.addTrack()" data-en="Native MediaTracks via RTCPeerConnection.addTrack()">addTrack() Orqali Apparat Darajasida Video Uzatish</h3>
        <p data-ru="Видео передается нативно через видеокодеки (VP8, VP9, H.264) и протокол SRTP. Браузер использует аппаратное ускорение видеокарты (GPU), потребляя минимум CPU при стабильных 60 FPS." data-en="Video is streamed natively using hardware-accelerated video codecs (VP8/H.264) via SRTP. GPU offloading maintains silky 60 FPS with minimal CPU strain.">Video bevosita videokarta (GPU) apparat tezlatgichi va SRTP protokoli orqali uzatiladi. Hech qanday matnli o'zgartirishsiz 60 FPS silliq harakat ta'minlanadi.</p>
        <pre><code>// ✅ To'g'ri: Apparat kodekli toza MediaStream
stream.getTracks().forEach(track =&gt; peer.addTrack(track, stream));
peer.ontrack = (e) =&gt; remoteVideo.srcObject = e.streams[0];</code></pre>
      </div>
    </div>
    <div class="bridge-card" style="margin-top:12px; padding:10px 16px; border-radius:10px; background:rgba(59,130,246,0.08); border-left:4px solid var(--accent); display:flex; justify-content:space-between; align-items:center;">
      <div>
        <strong style="color:var(--accent);" data-ru="Блиц-вопрос (30 сек):" data-en="Blitz Question (30s):">⚡ Blitz-Savol (30s):</strong>
        <span data-ru="Почему потоковое видео в реальном времени использует UDP/SRTP, а не надежный TCP?" data-en="Why does real-time streaming rely on UDP/SRTP instead of reliable TCP?">Nega jonli video-qo'ng'iroqlarda sekinlashtiruvchi TCP emas, tezkor UDP/SRTP ishlatiladi?</span>
      </div>
      <span class="badge" style="font-size:11px;" data-ru="TCP зависает при потере!" data-en="TCP freezes on drop!">TCP kadr yo'qolsa qotib qoladi!</span>
    </div>
  </section>

  <!-- SLIDE 3: VIDEO PIPELINE & CONSTRAINTS -->
  <section class="slide" data-phase="Media Oqimi|Медиа Поток|Media Pipeline" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ЗАХВАТ УСТРОЙСТВ" data-en="HARDWARE CAPTURE">KAMERA VA MIKROFON QUVURI</span></div>
    <h2 data-ru="Как Браузер Захватывает Камеру? (navigator.mediaDevices)" data-en="How Browsers Access Cameras: navigator.mediaDevices">Brauzer Kameraga Qanday Ulanadi? (navigator.mediaDevices)</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:15px; margin-bottom:12px;" data-ru="<strong>MediaStream API:</strong> интерфейс браузера для безопасного доступа к оборудованию пользователя с явным подтверждением разрешений." data-en="<strong>MediaStream API:</strong> secure browser interface to access user video and audio hardware with explicit user permission."><strong>MediaStream API:</strong> foydalanuvchining kamera va mikrofoni bilan xavfsiz ishlash imkonini beruvchi rasmiy brauzer texnologiyasi.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Xavfsizlik (HTTPS Majburiy):</strong> Kamera va mikrofonga faqat HTTPS yoki localhost orqali ruxsat beriladi!" data-en="<strong>HTTPS Only:</strong> Camera and microphone access is strictly forbidden on insecure HTTP!"><strong>HTTPS Majburiy:</strong> Kamera va mikrofonga faqat shifrlangan HTTPS yoki localhost orqali ulanish mumkin.</li>
          <li data-ru="<strong>MediaStreamTracks:</strong> Oqim treklar to'plamidir: alohida VideoTrack va alohida AudioTrack." data-en="<strong>MediaStreamTracks:</strong> Streams encapsulate distinct audio and video track objects."><strong>Treklar:</strong> MediaStream ichida alohida Video trek va Audio trek mustaqil boshqariladi.</li>
          <li data-ru="<strong>O'chirish (Mute/Disable):</strong> <code>track.enabled = false</code> qilib kamerani yoki mikrofonni darhol o'chirish mumkin." data-en="<strong>Mute Toggle:</strong> <code>track.enabled = false</code> instantly mutes feeds without tearing down connections."><strong>Mute Qilish:</strong> <code>track.enabled = false</code> orqali aloqani uzmasdan kamerani o'chirib qo'yish mumkin.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:12px; line-height:1.6;">
        <div style="color:var(--accent); font-weight:700; margin-bottom:6px;">[Kamera Sozlamalari (Constraints)]</div>
        <pre><code class="language-js">const constraints = {
  video: {
    width: { ideal: 1280, max: 1920 },
    height: { ideal: 720, max: 1080 },
    frameRate: { ideal: 30, max: 60 }
  },
  audio: {
    echoCancellation: true, // Echo aks-sado himoyasi
    noiseSuppression: true  // Shovqinni tozalash
  }
};
const stream = await navigator.mediaDevices.getUserMedia(constraints);
myVideoElement.srcObject = stream;</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: ADDTRACK & ONTRACK LIFECYCLE -->
  <section class="slide" data-phase="Treklar Hayoti|Жизненный Цикл|Track Lifecycle" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="ПЕРЕДАЧА ПОТОКОВ" data-en="TRACK TRANSMISSION">TREKLARNI P2P GA ULASH</span></div>
    <h2 data-ru="Связывание Потоков: RTCPeerConnection.addTrack() и ontrack" data-en="Binding Media: RTCPeerConnection.addTrack() & ontrack">Treklarni P2P ga Ulash: addTrack() va ontrack Hodisasi</h2>
    <div class="grid-2">
      <div>
        <h4 style="margin-bottom:6px; color:var(--accent);" data-ru="1. Отправка Треков (Alice)" data-en="1. Adding Tracks (Alice)">1. Treklarni Ulanishga Qo'shish (Alice)</h4>
        <pre><code class="language-js">// Kameradan oqim olindi
const localStream = await navigator.mediaDevices
  .getUserMedia({ video: true, audio: true });

// Har bir trekni peer ulanishiga kiritamiz
localStream.getTracks().forEach(track => {
  peerConnection.addTrack(track, localStream);
});

// Shundan so'ng createOffer() chaqirilganda,
// SDP ichiga video/audio kodeklari avtomatik yoziladi!</code></pre>
      </div>
      <div>
        <h4 style="margin-bottom:6px; color:var(--green);" data-ru="2. Прием Треков (Bob)" data-en="2. Receiving Remote Stream (Bob)">2. Masofaviy Oqimni Qabul Qilish (Bob)</h4>
        <pre><code class="language-js">const remoteVideo = document.getElementById('remoteVideo');

// Masofadan kadrlar kelganda ishga tushadi
peerConnection.ontrack = (event) => {
  console.log('✅ Yangi media trek keldi:', event.track.kind);
  // Birinchi kelgan streamni videoga ulaymiz
  if (remoteVideo.srcObject !== event.streams[0]) {
    remoteVideo.srcObject = event.streams[0];
  }
};</code></pre>
      </div>
    </div>
    <div style="margin-top:12px; background:var(--surface-2); padding:8px 12px; border-radius:6px; font-size:12px; color:var(--ink-2); display:flex; justify-content:space-between; align-items:center;">
      <span data-ru="💡 SDP автоматически согласует лучший кодек (например, H.264 или VP9) в зависимости от возможностей устройств" data-en="💡 SDP automatically negotiates the optimal codec (e.g. H.264 or VP9) matching device hardware">💡 SDP avtomatik ravishda ikkala kompyuter videokartasi qo'llab-quvvatlaydigan eng yaxshi video kodekni (VP8, VP9, H.264) tanlaydi</span>
      <span class="badge" style="background:var(--accent); color:#fff;" data-ru="Аппаратный Стандарт" data-en="Hardware Standard">Apparat Standarti</span>
    </div>
  </section>

  <!-- SLIDE 5: SRTP ENCRYPTION -->
  <section class="slide" data-phase="Kiberxavfsizlik|Безопасность|Security" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="ШИФРОВАНИЕ МЕДИАПОТОКА" data-en="STREAM ENCRYPTION">MEDIA OQIMLARINI SHIFRLASH</span></div>
    <h2 data-ru="Почему Видеозвонок Нельзя Перехватить? (SRTP и DTLS)" data-en="Why P2P Video Calls Cannot Be Intercepted: SRTP & DTLS">Nega Video-Qo'ng'iroqni O'g'irlab Bo'lmaydi? (SRTP va DTLS)</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);">RTP / Asos</div>
        <h4 data-ru="Real-Time Protocol" data-en="Real-Time Protocol">RTP Standarti</h4>
        <p style="font-size:12px;" data-ru="Базовый протокол передачи аудио и видео в реальном времени. Сам по себе не зашифрован." data-en="Base real-time audio/video transmission standard. Lacks built-in encryption on its own.">Internetda audio va video uzatuvchi asosiy standart. O'z holicha shifrlanmagan bo'ladi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">SRTP / Himoya</div>
        <h4 data-ru="Secure RTP (AES-128)" data-en="Secure RTP (AES-128)">Kafolatlangan SRTP</h4>
        <p style="font-size:12px;" data-ru="Каждый аудио-пакет и кадр видео шифруются алгоритмом AES-128-GCM на лету до отправки в сеть." data-en="Every audio sample and video frame is encrypted with AES-128-GCM before hitting the wire.">Har bir audio bo'lagi va video kadri tarmoqqa chiqishidan oldin apparat darajasida AES-128 bilan shifrlandi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">DTLS / Kalitlar</div>
        <h4 data-ru="Обмен Ключами" data-en="Key Exchange">DTLS Handshake</h4>
        <p style="font-size:12px;" data-ru="Ключи шифрования SRTP генерируются в браузере и передаются через защищенный канал DTLS." data-en="SRTP keys are negotiated dynamically inside the browser over the encrypted DTLS channel.">Shifrlash kalitlari brauzer ichida avtomatik yaratiladi — provayder ham, admin ham videoni ko'ra olmaydi.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px; background:rgba(0,0,0,0.2); border:1px solid var(--hair);">
      <div style="font-size:12px; font-weight:700; color:var(--ink-2); margin-bottom:4px;" data-ru="Стек Протоколов WebRTC MediaStream:" data-en="WebRTC MediaStream Protocol Stack:">WebRTC MediaStream Protokollar Steki:</div>
      <div style="display:flex; gap:6px; flex-wrap:wrap; font-family:var(--font-mono); font-size:11px;">
        <span style="background:var(--accent); color:#fff; padding:4px 8px; border-radius:4px;">Webcam / Mic</span>
        <span>➔</span>
        <span style="background:var(--purple); color:#fff; padding:4px 8px; border-radius:4px;">VP8 / Opus Codecs</span>
        <span>➔</span>
        <span style="background:#059669; color:#fff; padding:4px 8px; border-radius:4px;">SRTP (AES-128 Shifr)</span>
        <span>➔</span>
        <span style="background:#d97706; color:#fff; padding:4px 8px; border-radius:4px;">UDP (Tarmoq)</span>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: SCREEN SHARING -->
  <section class="slide" data-phase="Ekran Ulashish|Шаринг Экрана|Screen Sharing" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ДЕМОНСТРАЦИЯ ЭКРАНА" data-en="SCREEN SHARING">EKRAN ULASHISH API</span></div>
    <h2 data-ru="Стриминг Экрана: getDisplayMedia() и Замена Трека" data-en="Screen Capture: getDisplayMedia() & Track Replacement">Ekran Namoyishi: getDisplayMedia() va Treklarni Almashtirish</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="<strong>getDisplayMedia():</strong> позволяет пользователю выбрать конкретную вкладку, окно приложения или весь рабочий стол для трансляции." data-en="<strong>getDisplayMedia():</strong> allows the user to broadcast a specific browser tab, application window, or full desktop."><strong>getDisplayMedia():</strong> foydalanuvchiga butun ish stolini, ma'lum dastur oynasini yoki bitta brauzer tabini jonli translyatsiya qilish imkonini beradi.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Без переподключения:</strong> Для переключения камеры на экран не требуется заново устанавливать соединение!" data-en="<strong>Zero Reconnection:</strong> Switching between webcam and screen sharing does not drop the P2P call!"><strong>Qayta bog'lanish shart emas:</strong> Kamerani ekranga almashtirish uchun ulanishni uzish kerak emas!</li>
          <li data-ru="<strong>sender.replaceTrack():</strong> Отправляет новый видеотрек на лету сквозь существующий туннель." data-en="<strong>sender.replaceTrack():</strong> Swaps the active video track on the fly without renegotiation."><strong>sender.replaceTrack():</strong> Mavjud ulanish ichidagi kamerani bir zumda ekran tasviriga almashtirib yuboradi.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:12px; line-height:1.6;">
        <div style="color:var(--accent); font-weight:700; margin-bottom:6px;">[Ekranni Almashtirish Kodi]</div>
        <pre><code class="language-js">async function shareScreen() {
  const screenStream = await navigator.mediaDevices
    .getDisplayMedia({ video: true });
  const screenTrack = screenStream.getVideoTracks()[0];

  // RTCRtpSender orqali treknialmashtirish
  const sender = peerConnection.getSenders()
    .find(s => s.track.kind === 'video');
  await sender.replaceTrack(screenTrack);

  // Ekran ulashish to'xtatilganda kameraga qaytish
  screenTrack.onended = () => sender.replaceTrack(camTrack);
}</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: REAL-TIME CANVAS VIDEO FILTERS -->
  <section class="slide" data-phase="Kiber-Filtrlar|Видео Фильтры|Video Filters" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ОБРАБОТКА КАДРОВ НА ХОДУ" data-en="REAL-TIME CANVAS FX">CANVAS VIDEO FILTRLARI</span></div>
    <h2 data-ru="Матричные Фильтры Видео: Обработка Кадров в Реальном Времени" data-en="Matrix Video Filters: Real-Time Frame Processing on Canvas">Jonli Kadrlar Tahlili: Canvas Orqali Matritsali Filtrlar</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">Kiber-Yashil</div>
        <h4 data-ru="Эффект Матрицы" data-en="Matrix Effect">Matrix Yashil</h4>
        <p style="font-size:12px;" data-ru="Обнуляем красный и синий каналы, оставляя только чистый зеленый оттенок терминала." data-en="Zero out red and blue pixel channels, leaving only phosphor terminal green.">Pikselning qizil va ko'k rangini 0 qilib, faqat kiber-xakerlik yashil kanalini qoldirish.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">Grayscale</div>
        <h4 data-ru="Черно-Белый" data-en="Grayscale">Monoxrom (Oq-Qora)</h4>
        <p style="font-size:12px;" data-ru="Вычисляем яркость: <code>Y = 0.299R + 0.587G + 0.114B</code> для каждого пикселя видео." data-en="Compute luminance: <code>Y = 0.299R + 0.587G + 0.114B</code> across all frame pixels.">Inson ko'zi idroki formulasiga ko'ra yorqinlikni hisoblab oq-qora tasvir hosil qilish.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);">Invert / Negativ</div>
        <h4 data-ru="Инверсия Цветов" data-en="Color Inversion">Kiber-Rentgen</h4>
        <p style="font-size:12px;" data-ru="Инвертируем каждый цвет: <code>255 - R</code>, <code>255 - G</code>, <code>255 - B</code> для эффекта тепловизора." data-en="Invert colors: <code>255 - R</code>, <code>255 - G</code>, <code>255 - B</code> for thermal camera styling.">Har bir pikselni 255 dan ayirib termal ko'rish kamerasining tasvirini yasash.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px; background:rgba(0,0,0,0.2); border:1px solid var(--hair); font-family:var(--font-mono); font-size:11px;">
      <code>canvasCtx.drawImage(video, 0, 0); const imgData = canvasCtx.getImageData(0,0,w,h); // 60 FPS piksel filtri!</code>
    </div>
  </section>

  <!-- SLIDE 8: IN-DECK INTERACTIVE SIMULATOR -->
  <section class="slide" data-phase="Jonli Sinov|Интерактив|Live Demo" data-time="40:00–48:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="СИМУЛЯТОР В ПРЕЗЕНТАЦИИ" data-en="IN-DECK SIMULATOR">SMARTBOARDDA JONLI VIDEO OQIMI</span></div>
    <h2 data-ru="Интерактивный Видеотерминал: Фильтры и P2P Трансляция" data-en="Interactive Video Terminal: Real-Time Filters & P2P Stream">Jonli Sinov: Kamera Oqimi va Kiber-Filtrlar Studiyasi</h2>
    <div class="box" style="padding:12px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <div style="display:flex; gap:8px;">
          <button class="btn" onclick="deckStartDemoVideo()" id="btnDeckStartCam" style="background:var(--accent); color:#fff; padding:6px 14px; font-size:12px;" data-ru="📹 1. Запустить Камеру" data-en="📹 1. Start Camera">📹 1. Test Kamerasini Yoqish</button>
          <button class="btn" onclick="deckSetFilter('matrix')" style="padding:6px 10px; font-size:12px;" data-ru="🟢 Матрица" data-en="🟢 Matrix">🟢 Matrix</button>
          <button class="btn" onclick="deckSetFilter('grayscale')" style="padding:6px 10px; font-size:12px;" data-ru="⚪ Ч/Б" data-en="⚪ Grayscale">⚪ Oq-Qora</button>
          <button class="btn" onclick="deckSetFilter('invert')" style="padding:6px 10px; font-size:12px;" data-ru="🔴 Инверсия" data-en="🔴 Invert">🔴 Invert</button>
          <button class="btn" onclick="deckSetFilter('normal')" style="padding:6px 10px; font-size:12px;" data-ru="Обычный" data-en="Normal">Oddiy</button>
        </div>
        <div style="font-family:var(--font-mono); font-size:12px; color:var(--ink-2);">
          Bitrate: <strong style="color:var(--green);" id="deckBitrate">1.4 Mbps</strong> | 30 FPS | SRTP AES-128
        </div>
      </div>
      <div class="grid-2" style="gap:10px;">
        <div style="background:#000; border-radius:8px; padding:6px; display:flex; flex-direction:column; align-items:center; justify-content:center; height:180px; border:1px solid var(--hair);">
          <canvas id="deckLocalVideoCanvas" width="220" height="150" style="background:#0a0f1d; border-radius:4px;"></canvas>
          <span style="font-size:10px; color:var(--accent); margin-top:4px; font-family:var(--font-mono);">[ALICE - Mahalliy Kamera Oqimi]</span>
        </div>
        <div style="background:#000; border-radius:8px; padding:6px; display:flex; flex-direction:column; align-items:center; justify-content:center; height:180px; border:1px solid var(--hair);">
          <canvas id="deckRemoteVideoCanvas" width="220" height="150" style="background:#0a0f1d; border-radius:4px;"></canvas>
          <span style="font-size:10px; color:var(--green); margin-top:4px; font-family:var(--font-mono);">[BOB - P2P Orqali Qabul Qilingan Video]</span>
        </div>
      </div>
      <div style="margin-top:8px; font-size:11px; color:var(--ink-2); display:flex; justify-content:space-between;">
        <span data-ru="💡 Видео передается напрямую между узлами через MediaStreamTrack без сервера" data-en="💡 Video streams directly between peers via MediaStreamTrack without server routing">💡 Video to'g'ridan-to'g'ri brauzerlararo uzatiladi, markaziy server yuklamasi 0%</span>
        <span id="deckStreamStatus" style="color:var(--green);" data-ru="Статус: Канал открыт" data-en="Status: Channel Open">Status: P2P Video Ochiq</span>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: INTERACTIVE QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Quiz" data-time="48:00–54:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА ЗНАНИЙ" data-en="KNOWLEDGE CHECK">3-SAVOLLI INTERAKTIV TEST</span></div>
    <h2 data-ru="Блиц-Тест: WebRTC MediaStream и Видеопротоколы" data-en="Fast Quiz: WebRTC MediaStream & Video Protocols">Bilimni Sinash: WebRTC MediaStream va Jonli Video Oqimlari</h2>
    <div class="quiz-container" style="display:flex; flex-direction:column; gap:12px;">
      <!-- Q1 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="1. Какой метод используется для захвата камеры и микрофона в JavaScript?" data-en="1. Which JavaScript method captures webcam and microphone streams?">1. JavaScript-da veb-kamera va mikrofon oqimini olish uchun qaysi metod chaqiriladi?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Bu metod faqat geolokatsiya koordinatalari uchun.')" style="font-size:12px;" data-ru="A) navigator.geolocation.getCurrentPosition()" data-en="A) navigator.geolocation.getCurrentPosition()">A) navigator.geolocation.getCurrentPosition()</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! navigator.mediaDevices.getUserMedia() audio va videoni xavfsiz olib beradi.')" style="font-size:12px;" data-ru="B) navigator.mediaDevices.getUserMedia()" data-en="B) navigator.mediaDevices.getUserMedia()">B) navigator.mediaDevices.getUserMedia()</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'document.camera metodi mavjud emas.')" style="font-size:12px;" data-ru="C) document.camera.open()" data-en="C) document.camera.open()">C) document.camera.open()</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
      <!-- Q2 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="2. Какой протокол обеспечивает сквозное шифрование видео в WebRTC?" data-en="2. Which protocol provides end-to-end video encryption in WebRTC?">2. WebRTC-da video va audio kadrlarni uchma-uch shifrlashni qaysi protokol ta'minlaydi?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'HTTP video oqimlarini apparat darajasida shifrlamaydi.')" style="font-size:12px;" data-ru="A) HTTP / 1.1" data-en="A) HTTP / 1.1">A) HTTP / 1.1</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'Aynan shunday! SRTP (Secure Real-time Transport Protocol) AES-128 bilan har bir kadrni shifrlandi.')" style="font-size:12px;" data-ru="B) SRTP (Secure Real-time Transport Protocol)" data-en="B) SRTP (Secure Real-time Transport Protocol)">B) SRTP (Secure Real-time Transport Protocol)</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'FTP faqat fayl ko‘chirish uchun eski protokol.')" style="font-size:12px;" data-ru="C) FTP" data-en="C) FTP">C) FTP</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
      <!-- Q3 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="3. Как заменить видеотрек с веб-камеры на трансляцию экрана без разрыва соединения?" data-en="3. How to switch from webcam to screen sharing without dropping the P2P connection?">3. Ulanishni uzmasdan veb-kamerani ekran namoyishiga almashtirish qaysi metod orqali qilinadi?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! sender.replaceTrack(screenTrack) oqimni uzmasdan treknialmashtiradi.')" style="font-size:12px;" data-ru="A) sender.replaceTrack(screenTrack)" data-en="A) sender.replaceTrack(screenTrack)">A) sender.replaceTrack(screenTrack)</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Ulanishni yopish shart emas.')" style="font-size:12px;" data-ru="B) peer.close() и создать заново" data-en="B) peer.close() and re-initialize">B) peer.close() qilib noldan ochish</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Brauzerni yangilash aloqani to‘xtatadi.')" style="font-size:12px;" data-ru="C) Перезагрузить страницу" data-en="C) Reload the web page">C) Sahifani qayta yuklash</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: 25-MINUTE HANDS-ON ARENA -->
  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="54:00–69:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="БОЛЬШАЯ ПРАКТИЧЕСКАЯ АРЕНА" data-en="PRACTICE ARENA">25 DAQIQALIK KIBER-ARENA</span></div>
    <h2 data-ru="Миссия: Создай Зашифрованный P2P Видеочат с Фильтрами" data-en="Mission: Build Encrypted P2P Video Chat with Canvas FX">Kiber-Missiya: Shifrlangan P2P Video-Chat va Kiber-Filtrlar</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:10px;" data-ru="Откройте студию studio/index.html и поднимите двустороннюю видеосвязь с экраном шаринга." data-en="Launch studio/index.html and initialize a bi-directional video call with screen capture.">Darsning <a href="studio/index.html" target="_blank" style="color:var(--accent); font-weight:700;">studio/index.html</a> laboratoriyasini oching va to'liq P2P video-qo'ng'iroqni ko'taring.</p>
        <ul class="clean-list">
          <li data-ru="<strong>1-Шаг:</strong> Получите видеопоток через <code>getUserMedia()</code> и отобразите в локальном элементе." data-en="<strong>Step 1:</strong> Acquire local feed via <code>getUserMedia()</code> and bind to video element."><strong>1-Qadam:</strong> <code>getUserMedia()</code> orqali kamera oqimini olib ekranga chiqaring.</li>
          <li data-ru="<strong>2-Шаг:</strong> Добавьте треки в <code>RTCPeerConnection</code> и свяжите <code>ontrack</code> на удаленном узле." data-en="<strong>Step 2:</strong> Add tracks to <code>RTCPeerConnection</code> and attach <code>ontrack</code> on remote peer."><strong>2-Qadam:</strong> Treklarni <code>addTrack()</code> bilan ulanishga bering va masofaviy videoga ulang.</li>
          <li data-ru="<strong>3-Шаг:</strong> Реализуйте кнопку переключения экрана (<code>getDisplayMedia</code>) и Matrix-фильтр!" data-en="<strong>Step 3:</strong> Implement screen share toggle (<code>getDisplayMedia</code>) and Matrix filter!"><strong>3-Qadam:</strong> Ekranni ulashish (<code>getDisplayMedia</code>) va Matrix kiber-filtrini qo'shing!</li>
        </ul>
      </div>
      <div class="box" style="border-left:4px solid var(--accent);">
        <h4 style="margin-bottom:8px;" data-ru="10-Балльная Рубрика Оценки:" data-en="10-Point Grading Rubric:">10 Ballik Baholash Mezoni:</h4>
        <div style="font-size:12px; line-height:1.8;">
          <div><strong style="color:var(--green);">4 Ball:</strong> Kamera va mikrofon xatoliksiz ulanadi, lokal video ko'rinadi.</div>
          <div><strong style="color:var(--accent);">4 Ball:</strong> P2P ulanish orqali ikkinchi kompyuterga video uzatiladi va audio yangraydi.</div>
          <div><strong style="color:var(--purple);">2 Ball (Bonus):</strong> replaceTrack bilan ekran ulashish va Canvas kiber-filtrlari ishlaydi!</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: PEER REVIEW -->
  <section class="slide" data-phase="Kiber-Audit|Код-Ревью|Peer Review" data-time="69:00–74:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМНЫЙ КОНТРОЛЬ" data-en="PEER REVIEW">PARTADOSH BILAN KIBER-AUDIT</span></div>
    <h2 data-ru="Обменяйтесь Экранами: Тестирование Видеосвязи из 4 Пунктов" data-en="Swap Screens: 4-Point P2P Video Call Audit">Partadosh Bilan Almashing: 4 Bosqichli Video-Qo'ng'iroq Auditi</h2>
    <div class="grid-4" style="gap:10px;">
      <div class="box" style="border-top:3px solid var(--green);">
        <div class="tag" style="color:var(--green);">1. Video Oqimi</div>
        <h4 data-ru="Качество Кадров" data-en="Frame Quality">30 FPS Video</h4>
        <p style="font-size:12px;" data-ru="Идет ли видеопоток плавно, без артефактов и задержки менее 100 мс?" data-en="Is the video stream playing smoothly at &lt;100ms latency?">Video oqimi silliq kelyaptimi, kechikish 100ms dan pastmi?</p>
      </div>
      <div class="box" style="border-top:3px solid var(--accent);">
        <div class="tag" style="color:var(--accent);">2. Mikrofon</div>
        <h4 data-ru="Чистый Звук" data-en="Clear Audio">Audio Sifati</h4>
        <p style="font-size:12px;" data-ru="Слышен ли голос собеседника без эха и треска при включенном микрофоне?" data-en="Is audio clearly audible without echo or crackling?">Suhbatdosh ovozi aks-sadosiz toza va ravon eshitilyaptimi?</p>
      </div>
      <div class="box" style="border-top:3px solid var(--purple);">
        <div class="tag" style="color:var(--purple);">3. Ekran Ulashish</div>
        <h4 data-ru="Screen Share" data-en="Screen Share">Ekran Namoyishi</h4>
        <p style="font-size:12px;" data-ru="Переключается ли видеопоток на рабочий стол при нажатии кнопки шаринга?" data-en="Does the video seamlessly swap to desktop upon toggle?">Tugma bosilganda kamera o'rniga ekran tasviri uzatilyaptimi?</p>
      </div>
      <div class="box" style="border-top:3px solid var(--amber);">
        <div class="tag" style="color:var(--amber);">4. Filtrlar</div>
        <h4 data-ru="Canvas Фильтры" data-en="Canvas Filters">Kiber-Filtrlar</h4>
        <p style="font-size:12px;" data-ru="Работает ли матричный зеленый или монохромный фильтр в реальном времени?" data-en="Do real-time Matrix green or grayscale filters function?">Matrix yoki oq-qora kiber-filtrlar real-vaqtda kadrga urilyaptimi?</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: SHOWCASE ARENA -->
  <section class="slide" data-phase="Taqdimot|Демонстрация|Showcase Arena" data-time="74:00–77:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="БОЛЬШОЙ ЭКРАН" data-en="BIG SCREEN SHOWCASE">SMARTBOARDDA JONLI P2P QO'NG'IROQ</span></div>
    <h2 data-ru="Презентация Видеосвязи на Большом Экране" data-en="Live Smartboard Video Call Showcase">Smartboardda Jonli Video-Qo'ng'iroq Demosi</h2>
    <div class="grid-2">
      <div class="box">
        <h3 data-ru="Живой Тест: Парта 1 ➔ Парта 5" data-en="Live Test: Desk 1 ➔ Desk 5">Jonli Sinov: 1-Parta ➔ 5-Parta</h3>
        <p style="font-size:13px;" data-ru="Два ученика соединяются через школьный Wi-Fi без сторонних программ (только чистый WebRTC код браузера)." data-en="Two students connect across the school Wi-Fi with zero third-party software (pure browser WebRTC).">Ikkita o'quvchi maktab Wi-Fi tarmog'i orqali hech qanday Zoom yoki Telegramsiz, faqat o'z kodlari orqali bog'lanadilar.</p>
        <div style="background:var(--surface-2); padding:10px; border-radius:8px; font-size:12px; line-height:1.6;">
          📡 <strong>Protokol:</strong> WebRTC MediaStream + SRTP AES-128<br>
          ⚡ <strong>Kechikish:</strong> ~8 ms (LAN to'g'ridan-to'g'ri bog'lanish)<br>
          💻 <strong>Server Xarajati:</strong> $0.00 (Zero server overhead)
        </div>
      </div>
      <div class="box" style="display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
        <div style="font-size:48px; margin-bottom:10px;">📹 ⚡ 🚀</div>
        <h4 style="margin:4px 0; color:var(--green);" data-ru="Чистая Сетевая Инженерия" data-en="Pure Network Engineering">Haqiqiy Tarmoq Muhandisligi</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Никакого стороннего API — чистые веб-стандарты W3C!" data-en="No proprietary black boxes — pure W3C standards!">Hech qanday tayyor platformalarsiz — sof W3C xalqaro standartlari!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: TIERED HOMEWORK -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Tiered Homework" data-time="77:00–79:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="SUMMARY & HOMEWORK">10 BALLIK 3 DARAJALI UY VAZIFASI</span></div>
    <h2 data-ru="3 Уровня Домашнего Задания: P2P Видеотерминал" data-en="3-Tiered Homework Mission: P2P Video Terminal">3 Darajali Uy Vazifasi: Shaxsiy P2P Video-Xizmat</h2>
    <div class="grid-3" style="gap:10px;">
      <div class="box" style="border-top:3px solid var(--green);">
        <div class="tag" style="color:var(--green);">1-Daraja: Baza (4 ball)</div>
        <h4 data-ru="Камера и Микрофон" data-en="Camera & Mic">Baza Kamera Oqimi</h4>
        <p style="font-size:12px;" data-ru="Реализуйте захват веб-камеры и микрофона с кнопками Mute Audio и Video Off." data-en="Implement webcam and microphone capture with Mute Audio and Video Off toggles.">Kamera va mikrofondan oqim olib, Audio Mute va Video Off tugmalariga ega boshqaruv panelini yozing.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--accent);">
        <div class="tag" style="color:var(--accent);">2-Daraja: Loyiha (4 ball)</div>
        <h4 data-ru="P2P Видеозвонок" data-en="P2P Video Call">P2P Video Aloqa</h4>
        <p style="font-size:12px;" data-ru="Соедините два узла через addTrack() и ontrack, отобразив оба видеопотока." data-en="Establish a two-node video call via addTrack() and ontrack, displaying both feeds.">Ikkita uzel o'rtasida addTrack() va ontrack orqali to'liq ishchi P2P video aloqani ko'taring.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--purple);">
        <div class="tag" style="color:var(--purple);">3-Daraja: Challenge (2 ball)</div>
        <h4 data-ru="Шаринг Экрана" data-en="Screen Sharing">Ekran Namoyishi</h4>
        <p style="font-size:12px;" data-ru="Добавьте кнопку Share Screen через getDisplayMedia() и replaceTrack()." data-en="Add Share Screen button using getDisplayMedia() and replaceTrack().">Aloqani uzmasdan kamerani ekran namoyishiga almashtiruvchi replaceTrack() funksiyasini qo'shing.</p>
      </div>
    </div>
    <div style="margin-top:12px; text-align:right;">
      <a href="vazifa.html" class="btn" style="background:var(--purple); color:#fff; font-size:12px;" data-ru="Открыть ДЗ" data-en="Open HW">Vazifalar Ilovasini Ochish ➔</a>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ УРОКА" data-en="LESSON SUMMARY">XULOSA VA KEYINGI DARS</span></div>
    <h2 data-ru="WebRTC — Будущее Децентрализованных Медиасетей" data-en="WebRTC: Future of Decentralized Media Networks">WebRTC — Markazlashmagan Media Tarmoqlarning Kelajagi</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="За эти два урока мы прошли путь от текстовых P2P каналов до полноценного зашифрованного видеотерминала." data-en="Across these two lessons we advanced from textual data channels to full encrypted video communication.">Ushbu darslar davomida biz oddiy matnli ma'lumot uzatishdan to'liq shifrlangan professional video-qo'ng'iroq tizimigacha bo'lgan yo'lni bosib o'tdik.</p>
        <ul class="clean-list">
          <li data-ru="<strong>getUserMedia:</strong> Ученики освоили безопасное управление аппаратными ресурсами устройства." data-en="<strong>getUserMedia:</strong> Students mastered secure client-side hardware orchestration."><strong>getUserMedia:</strong> Kompyuter kamera va mikrofonini xavfsiz boshqarish o'zlashtirildi.</li>
          <li data-ru="<strong>Шифрование SRTP:</strong> Каждый видеокадр аппаратно защищен сквозным шифрованием AES-128." data-en="<strong>SRTP Encryption:</strong> Every frame is encrypted end-to-end at the hardware level."><strong>SRTP Shifrlash:</strong> Har bir video kadr apparat darajasida AES-128 bilan himoyalandi.</li>
          <li data-ru="<strong>replaceTrack:</strong> Освоена бесшовная замена видеопотоков на лету без переподключения." data-en="<strong>replaceTrack:</strong> Hot-swapping streams without renegotiation executed."><strong>replaceTrack:</strong> Aloqani uzmasdan oqimlarni bir zumda almashtirish amaliyoti qilindi.</li>
        </ul>
      </div>
      <div class="box" style="border-left:4px solid var(--purple); background:rgba(147,51,234,0.08);">
        <strong style="color:var(--purple); font-size:14px;" data-ru="Следующая Тема:" data-en="Next Topic:">🚀 Keyingi Dars Ko'prigi:</strong>
        <p style="font-size:12px; margin-top:6px; line-height:1.5;" data-ru="<strong>SPA (Single Page Application) и Client-Side Routing:</strong> Как строить веб-приложения без перезагрузки страниц с помощью History API и динамических роутов!" data-en="<strong>SPA & Client-Side Routing:</strong> Building fluid single-page applications without full page reloads using the History API!"><strong>SPA va Client-Side Routing:</strong> Sahifani qayta yuklamasdan ishlovchi tezkor SPA ilovalari va History API marshrutlash mexanizmi!</p>
      </div>
    </div>
  </section>
"""

# In-deck JS for Slide 8 live video/canvas filter simulator
IN_DECK_JS = """
// --- IN-DECK VIDEO STREAM & CANVAS FILTER SIMULATOR ---
var deckFilterMode = 'normal';
var deckCamRunning = false;
var deckSimFrame = 0;
var deckCamTimer = null;

function deckDrawFrame() {
  var localC = document.getElementById('deckLocalVideoCanvas');
  var remoteC = document.getElementById('deckRemoteVideoCanvas');
  if (!localC || !remoteC) return;
  var lCtx = localC.getContext('2d');
  var rCtx = remoteC.getContext('2d');

  deckSimFrame++;

  // Draw simulated synthetic camera frame
  lCtx.fillStyle = '#0f172a';
  lCtx.fillRect(0, 0, localC.width, localC.height);

  // Animated hacker face silhouette
  lCtx.fillStyle = '#3b82f6';
  lCtx.beginPath();
  lCtx.arc(110, 75, 38, 0, Math.PI * 2);
  lCtx.fill();

  // Eyes & Tech HUD
  lCtx.fillStyle = '#60a5fa';
  var blink = Math.sin(deckSimFrame * 0.1) > 0.95;
  if (!blink) {
    lCtx.fillRect(95, 65, 8, 8);
    lCtx.fillRect(117, 65, 8, 8);
  }
  lCtx.strokeStyle = '#38bdf8';
  lCtx.lineWidth = 1.5;
  lCtx.strokeRect(40, 20, 140, 110);
  lCtx.fillStyle = '#38bdf8';
  lCtx.font = '9px monospace';
  lCtx.fillText('TARGET_CAM_01 [30 FPS]', 44, 32);

  // Remote frame processing (Canvas Video Filter)
  var imgData = lCtx.getImageData(0, 0, localC.width, localC.height);
  var data = imgData.data;

  for (var i = 0; i < data.length; i += 4) {
    var r = data[i];
    var g = data[i+1];
    var b = data[i+2];

    if (deckFilterMode === 'matrix') {
      data[i] = 0; // Red off
      data[i+1] = Math.min(255, (r + g + b) * 1.2); // Bright green
      data[i+2] = 0; // Blue off
    } else if (deckFilterMode === 'grayscale') {
      var gray = 0.299 * r + 0.587 * g + 0.114 * b;
      data[i] = gray;
      data[i+1] = gray;
      data[i+2] = gray;
    } else if (deckFilterMode === 'invert') {
      data[i] = 255 - r;
      data[i+1] = 255 - g;
      data[i+2] = 255 - b;
    }
  }

  rCtx.putImageData(imgData, 0, 0);

  // Bitrate fluctuation
  if (deckSimFrame % 15 === 0) {
    var mbps = Math.round((1.2 + Math.random() * 0.4) * 10) / 10;
    var el = document.getElementById('deckBitrate');
    if (el) el.textContent = mbps + ' Mbps';
  }
}

function deckStartDemoVideo() {
  var btn = document.getElementById('btnDeckStartCam');
  var status = document.getElementById('deckStreamStatus');
  if (deckCamRunning) {
    clearInterval(deckCamTimer);
    deckCamTimer = null;
    deckCamRunning = false;
    btn.textContent = '📹 1. Test Kamerasini Yoqish';
    btn.style.background = 'var(--accent)';
    status.textContent = 'Status: To‘xtatildi';
  } else {
    deckCamRunning = true;
    deckCamTimer = setInterval(deckDrawFrame, 33); // ~30 FPS
    btn.textContent = '⏸️ Kamerani To‘xtatish';
    btn.style.background = 'var(--red)';
    status.textContent = 'Status: Jonli P2P Video Oqimi';
  }
}

function deckSetFilter(filterName) {
  deckFilterMode = filterName;
}

setTimeout(deckDrawFrame, 400);

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
        ["Kirish va Maqsad", "O'quvchilarga bugungi dars mavzusi: WebRTC MediaStream va P2P video-qo'ng'iroq haqida so'zlang.", "Doskaga kamera oqimi qanday qilib serverlarsiz to'g'ridan-to'g'ri o'tishini chizing."],
        ["Uy Vazifasi Tahlili", "31-darsdagi videoni Base64 matn qilib jo'natish xatosi (33% o'sish va qotish) ni tushuntiring.", "Oltin yechim: apparat videokodeklari (VP8/H.264) va SRTP ekanini ko'rsating."],
        ["Kamera va getUserMedia", "navigator.mediaDevices.getUserMedia va uning parametrlarini (width, height, echoCancellation) tushuntiring.", "HTTPS xavfsizlik talabini alohida ta'kidlang."],
        ["Treklarni Bog'lash", "addTrack() va ontrack hayot tsiklini ko'rsating.", "Har bir trek qanday qilib SDP ichiga yozilishini ayting."],
        ["SRTP Shifrlash", "RTP va SRTP farqini tushuntiring. AES-128 shifrlash qanday ishlashini ayting.", "Uchinchi shaxslar videoni o'g'irlay olmasligini ko'rsating."],
        ["Ekran Namoyishi", "getDisplayMedia orqali butun ekranni ulashish sintaksisini o'rgating.", "replaceTrack yordamida aloqani uzmasdan almashtirishni ko'rsating."],
        ["Canvas Video Filtrlari", "Video kadrlarini Canvas orqali Matrix yashil, oq-qora va invert qilib o'zgartirish formulasini tushuntiring.", "60 FPS pikselli manipulyatsiyani aytib bering."],
        ["Smartboard Simulyatori", "Taqdimot ichidagi simulyatorda kamerani yoqing va filtrlarni almashtirib ko'rsating.", "Bitrate va FPS ko'rsatkichlariga bolalar e'tiborini qarating."],
        ["Bilimni Sinash (Quiz)", "3 ta savol bo'yicha interaktiv viktorina o'tkazing.", "Har bir javobni tahlil qiling."],
        ["25 Daqiqalik Arena", "O'quvchilarga studio/index.html ni ochishni buyuring.", "Har bir o'quvchi o'z P2P video-chatini ko'tarishini nazorat qiling."],
        ["Partadosh Auditi", "O'rin almashib, 4 ta mezon bo'yicha loyihani tekshirishsin.", "Boshqalarning loyihasidagi video va ovoz sifatini baholang."],
        ["Katta Ekran Showcasi", "Ikkita kompyuter o'rtasida katta ekranda jonli P2P video-qo'ng'iroqni ko'rsating.", "O'quvchilarni olqishlang."],
        ["3 Darajali Uy Vazifasi", "10 ballik uy vazifasi shartlarini tushuntiring.", "3-darajadagi ekran ulashish vazifasiga e'tibor qarating."],
        ["Xulosa va Keyingi Dars", "Darsni sarhisob qiling va keyingi darsda SPA hamda client-side routingni o'rganishimizni e'lon qiling.", "O'quvchilar savollariga javob bering va vazifa ilovasini topshirish muddatini eslating."]
    ],
    "ru": [
        ["Введение и Цель", "Представьте тему: WebRTC MediaStream и прямые P2P видеозвонки без серверов.", "Нарисуйте на доске архитектуру захвата веб-камеры и передачи по сети."],
        ["Разбор Домашнего Задания", "Объясните ошибку отправки кадров строками Base64 через DataChannel (фризы и 33% оверхед).", "Покажите золотой стандарт: нативные треки через SRTP и видеокарту."],
        ["Камера и getUserMedia", "Разберите синтаксис getUserMedia и параметры constraints (разрешение, частота кадров).", "Подчеркните обязательность HTTPS соединения."],
        ["Связывание Треков", "Объясните функции addTrack() и событие ontrack.", "Покажите, как треки автоматически согласуются в SDP."],
        ["Шифрование SRTP", "Объясните разницу между RTP и защищенным SRTP на базе AES-128.", "Подчеркните приватность звонков: перехват исключен."],
        ["Шаринг Экрана", "Покажите метод getDisplayMedia() для захвата рабочего стола.", "Объясните replaceTrack() без разрыва соединения."],
        ["Видеофильтры на Холсте", "Покажите алгоритмы фильтров Matrix, Grayscale и Invert прямо на пикселях видео.", "Объясните обработку кадров на 60 FPS."],
        ["Интерактив на Доске", "Запустите встроенный в слайд симулятор видеосвязи.", "Продемонстрируйте переключение фильтров и битрейт."],
        ["Тест (Квиз)", "Проведите опрос по 3 контрольным вопросам.", "Разберите причины ошибок."],
        ["Практическая Арена (25 мин)", "Дайте команду открыть studio/index.html.", "Курируйте подъем видеосвязи каждым учеником."],
        ["Взаимный Аудит", "Организуйте обмен местами за партами по чек-листу из 4 пунктов.", "Проверьте звук, видео и шаринг экрана."],
        ["Шоукейс на Доске", "Выведите демонстрационный видеозвонок между двумя партами на смартборд.", "Похвалите авторов."],
        ["Домашнее Задание", "Объясните 3 уровня 10-балльного домашнего задания.", "Обратите внимание на вызов 3-го уровня."],
        ["Итоги и Анонс", "Подведите итоги урока и анонсируйте следующую тему: SPA и клиентская маршрутизация.", "Ответьте на вопросы учеников и напомните дедлайн сдачи практического ДЗ."]
    ],
    "en": [
        ["Intro & Objectives", "Introduce WebRTC MediaStream and direct P2P video conferencing.", "Diagram camera capture and peer-to-peer transmission on the board."],
        ["Homework Review", "Explain why streaming Base64-encoded canvas frames destroys framerates and balloons payloads by 33%.", "Present the golden solution: native hardware-accelerated MediaTracks via SRTP."],
        ["Hardware & getUserMedia", "Break down getUserMedia API options and media constraints.", "Highlight mandatory HTTPS enforcement."],
        ["Binding Media Tracks", "Walk through addTrack() and ontrack event listeners.", "Show how SDP automatically advertises codec capabilities."],
        ["SRTP Stream Encryption", "Contrast clear RTP with AES-128 encrypted SRTP.", "Reinforce that eavesdropping is mathematically infeasible."],
        ["Screen Sharing", "Demonstrate desktop broadcasting via getDisplayMedia().", "Explain hot-swapping video tracks seamlessly with replaceTrack()."],
        ["Real-Time Canvas FX", "Show how Matrix green, grayscale, and invert filters manipulate raw pixel arrays.", "Discuss 60 FPS performance optimizations."],
        ["In-Deck Live Demo", "Trigger the in-deck dual-node video simulator.", "Tweak filter presets and review real-time bandwidth metrics."],
        ["Knowledge Check (Quiz)", "Lead the class through the 3 quick questions.", "Discuss each answer with the class."],
        ["Hands-on Arena (25 min)", "Instruct students to open studio/index.html.", "Oversee the 25-minute P2P video call implementation challenge."],
        ["Peer Review", "Facilitate seat swapping to review code using the 4-point audit rubric.", "Test microphone clarity, frame stability, and screen sharing."],
        ["Showcase Arena", "Host a live desk-to-desk video call on the main Smartboard.", "Celebrate student achievements."],
        ["Tiered Homework", "Explain the 3-tiered 10-point homework assignment.", "Highlight Tier 3 screen sharing objectives."],
        ["Summary & Next Class", "Summarize core networking takeaways and preview SPA client-side routing.", "Answer student questions and remind them of the homework lab deadline."]
    ]
}

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "32-dars: WebRTC MediaStream va Jonli Video Chat"
    title_ru = "Урок 32: WebRTC MediaStream и Видеочат"
    title_en = "Lesson 32: WebRTC MediaStream & Live Video Chat"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="9 КЛАСС" data-en="GRADE 9">9-SINF</span>',
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

    tpl = tpl.replace("{{COHORT_LABEL}}", "9-sinf")
    tpl = tpl.replace("{{WEEK_NUM}}", "11")
    tpl = tpl.replace("{{LESSON_NUM}}", "32")
    tpl = tpl.replace("{{TRACK_UZ}}", "Junior Vibecoders, Full-Stack & DevOps Track")
    tpl = tpl.replace("{{TRACK_RU}}", "Junior Vibecoders, Full-Stack & DevOps")
    tpl = tpl.replace("{{TRACK_EN}}", "Junior Vibecoders, Full-Stack & DevOps Track")
    tpl = tpl.replace("{{LESSON_TITLE_UZ}}", "WebRTC MediaStream va Jonli P2P Mesh: Video, Audio va Ekran Ulashish")
    tpl = tpl.replace("{{LESSON_TITLE_RU}}", "WebRTC MediaStream: Видео, Аудио и Стриминг Экрана P2P")
    tpl = tpl.replace("{{LESSON_TITLE_EN}}", "WebRTC MediaStream: Live Video, Audio & Screen Sharing P2P")

    sec1_html = """
    <p style="font-size:12px; line-height:1.5; margin-bottom:8px;" data-ru="В отличие от передачи текстовых сообщений, видеопотоки требуют передачи 30–60 кадров в секунду. WebRTC передает медиа напрямую через аппаратные кодеки (VP8, H.264) и защищенный протокол SRTP, снижая задержку до минимума (&lt;100 мс)." data-en="Unlike text messages, video feeds demand 30–60 frames per second. WebRTC transmits media natively using hardware codecs (VP8, H.264) and SRTP encryption, slashing real-time latency below 100ms.">Matnli xabarlardan farqli o'laroq, video oqimlari soniyasiga 30–60 ta kadrni uzatishni talab qiladi. WebRTC videoni apparat kodeklari (VP8, H.264) va SRTP shifrlangan protokoli orqali to'g'ridan-to'g'ri jo'natib, kechikishni 100ms dan pastga tushiradi.</p>
    <div style="background:var(--surface-2); padding:6px 10px; border-radius:6px; font-size:11px; font-family:var(--font-mono); border-left:3px solid var(--accent);">
      <strong>Asosiy Standart:</strong> getUserMedia() + RTCPeerConnection.addTrack() + ontrack hodisasi + SRTP AES-128 Shifr + getDisplayMedia() ekran ulashish.
    </div>
    """

    sec2_html = """
    <pre style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; font-family:var(--font-mono); line-height:1.4; border:1px solid var(--hair);"><code>// Kamera va Mikrofondan Oqim Olish
const stream = await navigator.mediaDevices.getUserMedia({
  video: { width: 1280, height: 720 },
  audio: true
});

// P2P ga Treklarni Qo'shish
stream.getTracks().forEach(track => {
  peerConnection.addTrack(track, stream);
});

// Masofaviy Videoni Qabul Qilish
peerConnection.ontrack = (event) => {
  remoteVideo.srcObject = event.streams[0];
};</code></pre>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="API / Протокол" data-en="API / Protocol">API / Protokol</th>
            <th style="padding:4px 6px;" data-ru="Назначение в Медиа" data-en="Media Purpose">Media Tizimidagi Vazifasi</th>
            <th style="padding:4px 6px;" data-ru="Аппаратное Свойство" data-en="Hardware Property">Apparat Xususiyati</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="getUserMedia()" data-en="getUserMedia()"><code>getUserMedia()</code></td>
            <td style="padding:4px 6px;" data-ru="Захват камеры и микрофона" data-en="Capture camera & mic">Kamera va mikrofondan oqim olish</td>
            <td style="padding:4px 6px;" data-ru="HTTPS Обязательно" data-en="HTTPS Enforced">HTTPS Majburiy</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="getDisplayMedia()" data-en="getDisplayMedia()"><code>getDisplayMedia()</code></td>
            <td style="padding:4px 6px;" data-ru="Захват экрана или окна" data-en="Desktop / Window Capture">Ekranni jonli translyatsiya qilish</td>
            <td style="padding:4px 6px;" data-ru="Screen Permission" data-en="Screen Permission">Ekran Ruxsati</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="SRTP" data-en="SRTP"><code>SRTP</code></td>
            <td style="padding:4px 6px;" data-ru="Сквозное шифрование видеокадров" data-en="End-to-end frame encryption">Har bir video kadrni AES-128 bilan shifrlash</td>
            <td style="padding:4px 6px;" data-ru="AES-GCM-128" data-en="AES-GCM-128">AES-GCM-128</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="replaceTrack()" data-en="replaceTrack()"><code>replaceTrack()</code></td>
            <td style="padding:4px 6px;" data-ru="Смена камеры на экран без реконнекта" data-en="Hot-swap camera to screen">Ulanishni uzmasdan oqimni almashtirish</td>
            <td style="padding:4px 6px;" data-ru="Zero Downtime" data-en="Zero Downtime">0ms Uzilish</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    sec4_html = """
    <p style="font-size:12px; margin-bottom:6px;" data-ru="Запустите студию видеосвязи. Поднимите видеопоток с веб-камеры, примените фильтр Matrix и запишите показатели битрейта и разрешения:" data-en="Run the video studio. Start webcam video feed, apply Matrix filter, and record bitrate & resolution:">Video-chat studiyasini ishga tushiring. Kamerani yoqing, Matrix filtrini qo'llang va video ko'rsatkichlarini yozing:</p>
    <div style="border:1px dashed var(--hair); border-radius:6px; height:80px; padding:8px; font-family:var(--font-mono); font-size:11px; color:var(--ink-2);" data-ru="[Показатели битрейта, разрешения камеры и статус сквозного шифрования]" data-en="[Bitrate metrics, camera resolution, and encryption status]">
      // Video o'lchami (Resolution): ________ x ________ px<br>
      // O'lchangan bitreyt tezligi: ________ Mbps | Kadrlar soni: ________ FPS<br>
      // Shifrlash protokoli: SRTP (AES-128) - [  ] Tasdiqlandi
    </div>
    """

    rubric_html = """
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px; font-size:11px;">
      <div style="border-left:3px solid var(--green); padding-left:6px;">
        <strong style="color:var(--green);" data-ru="4 Балла: База" data-en="4 Pts: Base">4 Ball: Baza</strong>
        <p style="margin:2px 0;" data-ru="Камера и микрофон захвачены, локальное видео воспроизводится без сбоев." data-en="Camera and mic acquired cleanly, local video plays smoothly.">Kamera va mikrofondan oqim olindi, lokal video ishlaydi.</p>
      </div>
      <div style="border-left:3px solid var(--accent); padding-left:6px;">
        <strong style="color:var(--accent);" data-ru="4 Балла: Проект" data-en="4 Pts: Project">4 Ball: Loyiha</strong>
        <p style="margin:2px 0;" data-ru="Видео передается на удаленный узел через addTrack() и ontrack по P2P." data-en="Video streams to remote peer via addTrack() & ontrack bi-directionally.">Video masofaviy uzelga addTrack va ontrack orqali uzatiladi.</p>
      </div>
      <div style="border-left:3px solid var(--purple); padding-left:6px;">
        <strong style="color:var(--purple);" data-ru="2 Балла: Challenge" data-en="2 Pts: Challenge">2 Ball: Challenge</strong>
        <p style="margin:2px 0;" data-ru="Замена видеотрека на рабочий стол (getDisplayMedia) и холст-фильтры." data-en="Hot-swapping screen share via getDisplayMedia and Canvas filters.">getDisplayMedia ekran ulashish va Canvas Matrix filtrlari ishlaydi.</p>
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
    tpl = tpl.replace("{{LESSON_NUM}}", "32")
    tpl = tpl.replace("{{TRACK_UZ}}", "Junior Vibecoders, Full-Stack & DevOps Track")
    tpl = tpl.replace("{{TRACK_RU}}", "Junior Vibecoders, Full-Stack & DevOps")
    tpl = tpl.replace("{{TRACK_EN}}", "Junior Vibecoders, Full-Stack & DevOps Track")
    tpl = tpl.replace("{{LESSON_TITLE_UZ}}", "WebRTC MediaStream va Jonli P2P Mesh: Video, Audio va Ekran Ulashish")
    tpl = tpl.replace("{{LESSON_TITLE_RU}}", "WebRTC MediaStream: Видео, Аудио и Стриминг Экрана P2P")
    tpl = tpl.replace("{{LESSON_TITLE_EN}}", "WebRTC MediaStream: Live Video, Audio & Screen Sharing P2P")
    tpl = tpl.replace("{{TOTAL_TASKS}}", "3")

    tasks_html = """
  <!-- 1-DARAJA: BAZA -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-1" data-ru="1-Уровень: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Инициализация Видеопотока и Mute Управление" data-en="Video Feed Init & Mute Controls">Kamera Oqimini Olish va Mute Boshqaruvi</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Напишите функцию <code>initLocalStream(videoElement)</code>, которая запрашивает камеру и микрофон в разрешении 1280x720, связывает поток с элементом <code>&lt;video&gt;</code> и предоставляет функцию <code>toggleMute()</code> для отключения микрофона." data-en="Write <code>initLocalStream(videoElement)</code> that requests 1280x720 video and audio, binds to a <code>&lt;video&gt;</code> tag, and exports <code>toggleMute()</code> to disable audio track.">1280x720 o'lchamdagi kamera va mikrofonni olib, uni <code>&lt;video&gt;</code> tegiga ulovchi hamda mikrofoni o'chirib-yoquvchi <code>toggleMute()</code> funksiyasini taqdim etuvchi <code>initLocalStream(videoElement)</code> funksiyasini yozing.</p>
    <textarea class="answer-area" id="ans_task_1" rows="7" placeholder="JavaScript kodingizni bu yerga yozing..." data-placeholder-ru="Напишите ваш код здесь..." data-placeholder-en="Write your code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_1">
      <strong style="color:var(--green);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>async function initLocalStream(videoElement) {
  const stream = await navigator.mediaDevices.getUserMedia({
    video: { width: 1280, height: 720 },
    audio: true
  });
  videoElement.srcObject = stream;
  videoElement.play();

  return {
    stream,
    toggleMute: () => {
      const audioTrack = stream.getAudioTracks()[0];
      if (audioTrack) {
        audioTrack.enabled = !audioTrack.enabled;
        console.log('Mikrofon holati:', audioTrack.enabled ? 'ON' : 'MUTED');
      }
    }
  };
}</code></pre>
    </div>
  </div>

  <!-- 2-DARAJA: AMALIYOT -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-2" data-ru="2-Уровень: Проект (4 балла)" data-en="Tier 2: Project (4 pts)">2-Daraja: Amaliyot (4 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Связывание Треков addTrack() и ontrack" data-en="Binding Media Tracks: addTrack() & ontrack">P2P Media Bog'lanishi: addTrack() va ontrack</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Напишите функцию <code>connectMediaPeer(peer, localStream, remoteVideoElement)</code>, которая добавляет все локальные треки в peer соединение и при получении события <code>ontrack</code> связывает удаленный поток с элементом <code>remoteVideoElement</code>." data-en="Implement <code>connectMediaPeer(peer, localStream, remoteVideoElement)</code> to bind local tracks to peer connection and assign incoming remote stream on <code>ontrack</code> event.">Lokal stream ichidagi barcha treklarni <code>peer.addTrack()</code> bilan qo'shuvchi va masofadan kelgan oqimni <code>peer.ontrack</code> orqali <code>remoteVideoElement</code> ga ulovchi <code>connectMediaPeer()</code> funksiyasini yozing.</p>
    <textarea class="answer-area" id="ans_task_2" rows="8" placeholder="addTrack kodingizni bu yerga yozing..." data-placeholder-ru="Напишите код связывания здесь..." data-placeholder-en="Write track binding code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_2">
      <strong style="color:var(--accent);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>function connectMediaPeer(peer, localStream, remoteVideoElement) {
  localStream.getTracks().forEach(track => {
    peer.addTrack(track, localStream);
  });

  peer.ontrack = (event) => {
    console.log('Masofaviy trek qabul qilindi:', event.track.kind);
    if (remoteVideoElement.srcObject !== event.streams[0]) {
      remoteVideoElement.srcObject = event.streams[0];
    }
  };
}</code></pre>
    </div>
  </div>

  <!-- 3-DARAJA: CHALLENGE -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-3" data-ru="3-Уровень: Challenge (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Бесшовный Шаринг Экрана: replaceTrack()" data-en="Seamless Screen Sharing: replaceTrack()">Ulanishni Uzmasdan Ekranni Ulashish: replaceTrack()</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Напишите функцию <code>enableScreenShare(peer, originalCamTrack)</code>, которая вызывает <code>getDisplayMedia()</code>, заменяет видеотрек в существующем RTCRtpSender без повторного рукопожатия, а при остановке шаринга возвращает исходную камеру." data-en="Write <code>enableScreenShare(peer, originalCamTrack)</code> which calls <code>getDisplayMedia()</code>, replaces active video track in RTCRtpSender without SDP renegotiation, and reverts to webcam upon stop."><code>getDisplayMedia()</code> orqali ekranni oluvchi, RTCRtpSender orqali ulanishni uzmasdan kamerani ekranga almashtiruvchi va ekran to'xtatilganda yana avtomatik kameraga qaytuvchi <code>enableScreenShare()</code> funksiyasini yozing.</p>
    <textarea class="answer-area" id="ans_task_3" rows="8" placeholder="replaceTrack kodingizni bu yerga yozing..." data-placeholder-ru="Напишите код замены трека здесь..." data-placeholder-en="Write track replacement code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_3">
      <strong style="color:var(--purple);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>async function enableScreenShare(peer, originalCamTrack) {
  const screenStream = await navigator.mediaDevices.getDisplayMedia({ video: true });
  const screenTrack = screenStream.getVideoTracks()[0];

  const sender = peer.getSenders().find(s => s.track && s.track.kind === 'video');
  if (sender) {
    await sender.replaceTrack(screenTrack);
    console.log('✅ Ekran translyatsiyasi faol!');

    screenTrack.onended = async () => {
      console.log('Ekran ulashish tugadi, kameraga qaytilmoqda...');
      await sender.replaceTrack(originalCamTrack);
    };
  }
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
    content = """# 9-sinf, 11-hafta, 32-dars: O'qituvchi Qo'llanmasi
## WebRTC MediaStream va Jonli P2P Mesh: Video, Audio va Ekran Ulashish

### Dars Haqida Ma'lumot:
- **Kohorta:** 9-sinf (Junior Vibecoders, Full-Stack & DevOps Track)
- **Format:** 80 daqiqalik Juftlik Dars (Double Block, 2 bosqichli)
- **Asosiy maqsad:** O'quvchilarga WebRTC MediaStream arxitekturasini o'rgatish, `getUserMedia()` va `getDisplayMedia()` orqali apparat resurslarini boshqarish, videoni SRTP shifrlash bilan uzatish, `replaceTrack()` yordamida aloqani uzmasdan ekran ulashish va Canvas matritsali kiber-filtrlarni kodlash.

---

### 80 Daqiqalik Dars Pacing Xaritasi:

#### 1-BOSQICH (40 daqiqa): Nazariya, Xatolar Tahlili va Jonli Test
| Vaqt | Bosqich | Slayd | O'qituvchi Harakati | Kutiladigan Natija |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Maqsad | 1 | Dars mavzusini e'lon qilish, Discord va Google Meet qanday ishlashini aytish. | O'quvchilarda qiziqish uyg'onadi. |
| **04:00–12:00** | O'tgan Dars HW Tahlili | 2 | 31-darsdagi videoni Base64 matn qilib jo'natish xatosi (33% o'sish va qotish) ni tushuntirish. Blitz savol. | Nega naqd media treklari kerakligi o'zlashtiriladi. |
| **12:00–18:00** | Kamera va getUserMedia | 3 | `getUserMedia` va uning sozlamalari (resolution, echo cancellation) ni tahlil qilish. | HTTPS talabi va media obyekti tushuniladi. |
| **18:00–24:00** | addTrack va ontrack | 4 | Treklar hayot tsikli va SDP kelishuvi. | MediaStream treklarining ulanishi o'rganiladi. |
| **24:00–30:00** | SRTP Shifrlash | 5 | RTP vs SRTP AES-128 va DTLS kalitlar almashishi. | Kiberxavfsizlik va maxfiylik kafolati anglanadi. |
| **30:00–35:00** | Ekran Ulashish | 6 | `getDisplayMedia` va `replaceTrack` orqali uzilishsiz almashtirish. | Ekranni translyatsiya qilish o'rganiladi. |
| **35:00–40:00** | Canvas Kiber-Filtrlari | 7 | Matrix yashil, oq-qora va invert filtrlari formulasini ko'rsatish. | 60 FPS kadrlar bilan ishlash tushuniladi. |

#### 2-BOSQICH (40 daqiqa): Amaliy Kiber-Arena va Taqdimot
| Vaqt | Bosqich | Slayd | O'qituvchi Harakati | Kutiladigan Natija |
|---|---|:---:|---|---|
| **40:00–48:00** | Smartboard Sinovi | 8 | Slayd ichidagi simulyatorda kamerani yoqib, Matrix filtrini ko'rsatish. | Vizual tajriba ortadi. |
| **48:00–54:00** | 3-Savolli Quiz | 9 | Butun sinf bilan interaktiv test o'tkazish. | Bilimlar mustahkamlanadi. |
| **54:00–69:00** | 25 Daqiqalik Arena | 10 | Bolalarga `studio/index.html` da P2P video-chatni ko'tarishni topshirish. | Har bir o'quvchi video-chatni ishga tushiradi. |
| **69:00–74:00** | Partadosh Auditi | 11 | O'rin almashib, 4 ta mezon bo'yicha video va ovozni tekshirish. | Sifat nazorati va kiber-audit. |
| **74:00–77:00** | Katta Ekran Showcasi | 12 | 2 ta parta o'rtasida katta ekranda jonli P2P video-qo'ng'iroqni ko'rsatish. | O'quvchilarda g'urur va ishonch. |
| **77:00–79:00** | Uy Vazifasi | 13 | 10 ballik 3 darajali vazifani tushuntirish. | Vazifa tushuniladi. |
| **79:00–80:00** | Xulosa va Keyingi Dars | 14 | Darsni sarhisob qilish va SPA / Client-side routing mavzusiga ko'prik. | 80 daqiqa to'liq yakunlanadi. |

---

### Keng Tarqalgan Savollar va Maslahatlar:
1. **"Nega brauzer kameraga ruxsat bermayapti?"**
   - Javob: Brauzer xavfsizlik nuqtai nazaridan faqat `localhost` yoki `https://` protokoli orqali ishlovchi saytlarga kamera va mikrofondan foydalanishga ruxsat beradi.
2. **"replaceTrack() chaqirilganda nega qayta offer/answer qilish shart emas?"**
   - Javob: Chunki P2P kanal va kodeklar muzokaralari allaqachon o'rnatilgan. `replaceTrack()` faqat jo'natilayotgan apparat oqimining manbasini almashtiradi (kamera o'rniga ekran treki), kanalning o'zi uzilmaydi!
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
  <title data-ru="WebRTC Видеостудия — 9 Класс" data-en="WebRTC Video Studio — Grade 9">WebRTC Video Kiber-Studiyasi — 9-Sinf</title>
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
      --amber: #f59e0b;
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
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    .video-card {
      background: var(--surface);
      border: 1px solid var(--hair);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .video-screen {
      width: 100%;
      height: 260px;
      background: #000;
      border-radius: 8px;
      border: 1px solid var(--hair);
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
      overflow: hidden;
    }
    canvas {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }
    .hud-overlay {
      position: absolute;
      top: 10px;
      left: 10px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--accent);
      background: rgba(0,0,0,0.6);
      padding: 2px 6px;
      border-radius: 4px;
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
      <h2 style="margin:0 0 4px 0;" data-ru="WebRTC P2P Видеотерминал" data-en="WebRTC P2P Video Terminal">WebRTC P2P Video Kiber-Studiyasi</h2>
      <span style="font-size:12px; color:var(--ink-2);" data-ru="9-Класс · 11-Неделя · 32-Урок · MediaStream, SRTP шифрование и Canvas фильтры" data-en="Grade 9 · Week 11 · Lesson 32 · MediaStream, SRTP Encryption & Canvas Filters">9-Sinf · 11-Hafta · 32-Dars · MediaStream, SRTP shifrlash va Canvas filtrlari</span>
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
    <button class="btn btn-green" id="btnToggleCam" onclick="toggleLocalCam()" data-ru="📹 Включить Камеру" data-en="📹 Start Camera">📹 Kamerani Yoqish</button>
    <button class="btn btn-accent" id="btnShareScreen" onclick="toggleScreenShare()" data-ru="🖥️ Поделиться Экраном" data-en="🖥️ Share Screen">🖥️ Ekranni Ulashish</button>
    <button class="btn" onclick="cycleFilter()" data-ru="🎨 Сменить Фильтр" data-en="🎨 Cycle Filter">🎨 Filtrni Almashtirish</button>
    <span style="font-size:12px; color:var(--ink-2); margin-left:auto; font-family:var(--font-mono);">
      Filtr: <strong id="lblFilter" style="color:var(--green);">NORMAL</strong> | SRTP: <strong style="color:var(--accent);">AES-GCM-128</strong>
    </span>
  </div>

  <div class="grid">
    <!-- LOCAL NODE -->
    <div class="video-card">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <strong style="color:var(--accent);" data-ru="[УЗЕЛ 1: ЛОКАЛЬНАЯ КАМЕРА]" data-en="[NODE 1: LOCAL FEED]">[1-UZEL: MAHALLIY KAMERA]</strong>
        <span style="font-size:11px; color:var(--ink-2); font-family:var(--font-mono);">Role: Broadcaster</span>
      </div>
      <div class="video-screen">
        <canvas id="localCanvas" width="320" height="240"></canvas>
        <div class="hud-overlay" id="localHud">FPS: 30 | 720p</div>
      </div>
      <div style="display:flex; gap:8px;">
        <button class="btn" onclick="toggleMute()" id="btnMute" style="flex:1;" data-ru="🎙️ Выкл Звук" data-en="🎙️ Mute Mic">🎙️ Mikrofonni O'chirish</button>
        <button class="btn" onclick="toggleVideo()" id="btnVideoOff" style="flex:1;" data-ru="🚫 Выкл Видео" data-en="🚫 Video Off">🚫 Kamerani O'chirish</button>
      </div>
    </div>

    <!-- REMOTE NODE -->
    <div class="video-card">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <strong style="color:var(--green);" data-ru="[УЗЕЛ 2: МАСОФАВИЙ ПРИЕМ (P2P)]" data-en="[NODE 2: REMOTE P2P FEED]">[2-UZEL: MASOFAVIY P2P QABUL]</strong>
        <span style="font-size:11px; color:var(--ink-2); font-family:var(--font-mono);">Transport: SRTP / UDP</span>
      </div>
      <div class="video-screen">
        <canvas id="remoteCanvas" width="320" height="240"></canvas>
        <div class="hud-overlay" style="color:var(--green);">P2P SECURE | LAN ~8ms</div>
      </div>
      <div style="background:var(--surface-2); padding:10px; border-radius:8px; font-size:12px; line-height:1.6; color:var(--ink-2);">
        <strong style="color:var(--green);" data-ru="Статус P2P Связи:" data-en="P2P Stream Status:">P2P Aloqa Holati:</strong><br>
        <span data-ru="Поток воспроизводится напрямую без промежуточного сервера. Задержка минимальна (&lt;100 мс)." data-en="Media stream renders directly peer-to-peer with zero server hops. Sub-100ms latency.">Oqim to'g'ridan-to'g'ri P2P tunnel orqali uzatilmoqda. Kechikish &lt;100ms.</span>
      </div>
    </div>
  </div>

  <script>
    var currentLang = 'uz';
    var isCamOn = false;
    var isScreenOn = false;
    var isMuted = false;
    var isVideoOff = false;
    var filterIndex = 0;
    var filters = ['normal', 'matrix', 'grayscale', 'invert'];
    var frameCount = 0;
    var animTimer = null;

    var lCanvas = document.getElementById('localCanvas');
    var rCanvas = document.getElementById('remoteCanvas');
    var lCtx = lCanvas.getContext('2d');
    var rCtx = rCanvas.getContext('2d');

    function setLang(lang) {
      currentLang = lang;
      document.querySelectorAll('.lang-btn').forEach(function(b) {
        b.classList.toggle('active', b.textContent.toLowerCase() === lang);
      });
      document.querySelectorAll('[data-' + lang + ']').forEach(function(el) {
        el.textContent = el.getAttribute('data-' + lang);
      });
    }

    function renderFrame() {
      frameCount++;

      lCtx.fillStyle = '#030712';
      lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);

      if (isVideoOff) {
        lCtx.fillStyle = '#ef4444';
        lCtx.font = '14px monospace';
        lCtx.fillText('KAMERA O‘CHIRILGAN', 80, 120);
      } else if (isScreenOn) {
        // Simulated screen sharing
        lCtx.fillStyle = '#1e1b4b';
        lCtx.fillRect(20, 20, 280, 200);
        lCtx.strokeStyle = '#6366f1';
        lCtx.strokeRect(20, 20, 280, 200);
        lCtx.fillStyle = '#a5b4fc';
        lCtx.font = '12px monospace';
        lCtx.fillText('🖥️ ISH STOLI NAMOYISHI', 40, 50);
        lCtx.fillText('code app.js --webrtc-stream', 40, 90);
        lCtx.fillText('Status: Active 60 FPS', 40, 120);
      } else {
        // Simulated webcam user silhouette
        lCtx.fillStyle = '#3b82f6';
        lCtx.beginPath();
        lCtx.arc(160, 110, 50, 0, Math.PI * 2);
        lCtx.fill();

        // Eyes
        lCtx.fillStyle = '#93c5fd';
        var blink = Math.sin(frameCount * 0.08) > 0.94;
        if (!blink) {
          lCtx.fillRect(140, 100, 10, 10);
          lCtx.fillRect(170, 100, 10, 10);
        }

        lCtx.strokeStyle = '#38bdf8';
        lCtx.lineWidth = 2;
        lCtx.strokeRect(50, 30, 220, 170);
        lCtx.fillStyle = '#38bdf8';
        lCtx.font = '10px monospace';
        lCtx.fillText('CYBER_WEBCAM_01', 56, 46);
      }

      // Process filters for remote peer
      var imgData = lCtx.getImageData(0, 0, lCanvas.width, lCanvas.height);
      var d = imgData.data;
      var curFilter = filters[filterIndex];

      for (var i = 0; i < d.length; i += 4) {
        var r = d[i], g = d[i+1], b = d[i+2];
        if (curFilter === 'matrix') {
          d[i] = 0;
          d[i+1] = Math.min(255, (r + g + b) * 1.3);
          d[i+2] = 0;
        } else if (curFilter === 'grayscale') {
          var gray = 0.299 * r + 0.587 * g + 0.114 * b;
          d[i] = gray; d[i+1] = gray; d[i+2] = gray;
        } else if (curFilter === 'invert') {
          d[i] = 255 - r; d[i+1] = 255 - g; d[i+2] = 255 - b;
        }
      }

      rCtx.putImageData(imgData, 0, 0);
    }

    function toggleLocalCam() {
      var btn = document.getElementById('btnToggleCam');
      if (isCamOn) {
        clearInterval(animTimer);
        animTimer = null;
        isCamOn = false;
        btn.textContent = '📹 Kamerani Yoqish';
        btn.style.background = 'var(--green)';
        lCtx.clearRect(0, 0, lCanvas.width, lCanvas.height);
        rCtx.clearRect(0, 0, rCanvas.width, rCanvas.height);
      } else {
        isCamOn = true;
        animTimer = setInterval(renderFrame, 33);
        btn.textContent = '⏸️ Kamerani To‘xtatish';
        btn.style.background = 'var(--red)';
      }
    }

    function toggleScreenShare() {
      if (!isCamOn) return;
      isScreenOn = !isScreenOn;
      var btn = document.getElementById('btnShareScreen');
      if (isScreenOn) {
        btn.textContent = '📹 Kameraga Qaytish';
        btn.style.background = 'var(--purple)';
      } else {
        btn.textContent = '🖥️ Ekranni Ulashish';
        btn.style.background = 'var(--accent)';
      }
    }

    function toggleMute() {
      isMuted = !isMuted;
      var btn = document.getElementById('btnMute');
      btn.textContent = isMuted ? '🎙️ Ovozni Yoqish' : '🎙️ Mikrofonni O‘chirish';
      btn.style.background = isMuted ? 'var(--red)' : 'var(--surface-2)';
    }

    function toggleVideo() {
      isVideoOff = !isVideoOff;
      var btn = document.getElementById('btnVideoOff');
      btn.textContent = isVideoOff ? '📹 Videoni Yoqish' : '🚫 Kamerani O‘chirish';
      btn.style.background = isVideoOff ? 'var(--red)' : 'var(--surface-2)';
    }

    function cycleFilter() {
      filterIndex = (filterIndex + 1) % filters.length;
      document.getElementById('lblFilter').textContent = filters[filterIndex].toUpperCase();
    }

    renderFrame();
  </script>
</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "studio", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(studio_html)
    print("  ✓ Created: studio/index.html")

def main():
    print("📦 Building 9-sinf (Lesson 32: WebRTC MediaStream va Video Chat)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_studio()
    print("🎉 Done! Generated Grade 9 Lesson 32.")

if __name__ == "__main__":
    main()
