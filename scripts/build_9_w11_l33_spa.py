#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_9_w11_l33_spa.py — Builder for 9th Grade, Week 11, Lesson 33

Mavzu: SPA (Single Page Application) Asoslari va Client-Side Routing
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 9-sinf (Full-Stack & DevOps Track)
Pedagogika: VIBECODING VA SAHIFANI QAYTA YUKLAMASDAN BOSHQARISH.
             1) MPA vs SPA farqlari, FOUC (oq ekran miltillashi) muammosi
             2) HTML5 History API: pushState, replaceState va popstate
             3) Link Interception: e.preventDefault() va markaziy navigatsiya
             4) Routes Map va dinamik komponentlar inyeksiyasi
             5) Jonli Cyber-OS SPA Studiyasi (Dashboard, Live Traffic Chart, Terminal, Settings)
             6) Server Fallback (Vercel rewrites / Nginx try_files) sir-asrorlari
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "9-sinf", "11-hafta", "33-dars-spa-va-client-side-routing")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "studio"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides — High-Energy SPA Architecture)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="9-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 33" data-en="GRADE 9 · WEEK 11 · LESSON 33">9-SINF · 11-HAFTA · 33-DARS</span></div>
    <h1 class="display" data-ru="Основы SPA и Клиентский Роутинг: Веб Без Перезагрузок" data-en="SPA Architecture & Client-Side Routing: Zero-Reload Web">SPA Asoslari va Client-Side Routing: Qayta Yuklamasdan Boshqarish</h1>
    <p class="lede" data-ru="Создаем быстрые приложения без белого экрана и перезагрузок: внутренняя механика HTML5 History API, перехват кликов по ссылкам, роутер на чистом JavaScript и сборка кибер-панели управления Cyber-OS через Vibecoding!" data-en="Engineering lightning-fast web apps without blank page flickers: under-the-hood HTML5 History API, link interception, Vanilla JS router, and building a Cyber-OS dashboard via Vibecoding!">Oq ekran miltillashi va sahifa qayta yuklanishisiz ishlovchi tezyurar veb-ilovalar: HTML5 History API ichki mexanikasi, havolalarni tutib qolish, toza JavaScript routeri va Vibecoding orqali Cyber-OS boshqaruv panelini qurish!</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Архитектура SPA" data-en="SPA Architecture">SPA Arxitekturasi</h3>
        <p data-ru="History API: pushState, popstate, перехват ссылок через e.preventDefault() и смена видов за 0 мс." data-en="History API: pushState, popstate, link interception with e.preventDefault(), and 0 ms view switches.">History API: pushState, popstate, e.preventDefault() orqali havolalarni tutish va 0 ms da sahifa yangilash.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Cyber-OS Dashboard</div>
        <h3 data-ru="Рабочий SPA Проект" data-en="Playable SPA App">Ishlaydigan SPA Loyihasi</h3>
        <p data-ru="Собственная панель с графиком трафика, терминалом и роутингом, работающая без единого обновления страницы." data-en="Personal dashboard with live traffic chart, terminal, and client-side routing with zero reloads.">Sahifani qayta yuklamasdan ishlovchi jonli trafik grafigi, terminal va sozlamalarga ega shaxsiy SPA ilovasi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW & BRIDGE -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="РАЗБОР ДОМАШНЕГО ЗАДАНИЯ И МОСТ" data-en="HOMEWORK REVIEW & BRIDGE">UY VAZIFASI TAHLILI VA KO'PRIK</span></div>
    <h2 data-ru="Разбор ДЗ 32-урока: Утечки Камеры и Мост к SPA" data-en="Lesson 32 HW Review: Media Leaks & Bridge to SPA">32-Dars Uy Vazifasi: Kamera Oqishi va SPA Ko'prigi</h2>
    <div class="grid-2">
      <div class="card" style="border-left:4px solid var(--danger);">
        <div class="tag" style="background:var(--danger); color:#fff;" data-ru="Частая ошибка" data-en="Common Pitfall">Keng Tarqalgan Xato</div>
        <h3 data-ru="Зеленый Индикатор Камеры Не Гаснет" data-en="Camera Light Remains ON">Kamera Chirog'i O'chmay Qolishi (Hardware Leak)</h3>
        <p data-ru="Ученики закрывали видео-звонок через <code>peerConnection.close()</code>, но зеленый светодиод веб-камеры продолжал гореть! Браузер держал аппаратную блокировку камеры, потому что треки не были остановлены." data-en="Students ended video calls via peerConnection.close(), but webcam LED remained on! The browser held a hardware lock because tracks weren't halted.">O'quvchilar qo'ng'iroqni <code>peerConnection.close()</code> bilan yopishgan, lekin noutbuk kamerasi yonib qolavergan! Sababi — MediaStream treklari to'xtatilmagan.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <div class="tag" style="background:var(--accent); color:#fff;" data-ru="Золотой Стандарт" data-en="Golden Standard">Oltin Yechim (Track Cleanup)</div>
        <h3 data-ru="Полная Остановка Треков" data-en="Halting Media Tracks">Apparat Treklarni To'xtatish</h3>
        <pre><code>// Kamera va mikrofondan xavfsiz chiqish:
function stopMedia(stream) {
  if (stream) {
    stream.getTracks().forEach(track =&gt; track.stop());
  }
}</code></pre>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Функция track.stop() освобождает веб-камеру для ОС." data-en="track.stop() properly releases camera hardware back to the OS."><code>track.stop()</code> operatsion tizim darajasida kamerani boshqa ilovalar uchun bo'shatadi.</p>
      </div>
    </div>
    <div class="card mt" style="background:var(--surface-2); padding:10px 16px;">
      <div class="badge" style="background:var(--accent); color:#fff; font-size:11px;" data-ru="Блиц-Вопрос (30 сек)" data-en="Blitz Question (30s)">30 Soniyalik Blitz</div>
      <p style="margin:4px 0; font-size:13px;" data-ru="Почему в YouTube или Telegram Web при переходе на другое видео экран не моргает белым светом?" data-en="Why doesn't YouTube or Telegram Web blink white when clicking another video or chat?">Nega YouTube yoki Telegram Web da boshqa sahifaga o'tganda ekran oqarib miltillamaydi? Chunki bu <strong>SPA (Single Page Application)</strong> — brauzer butun sahifani qayta yuklamaydi, faqat o'zgargan kontentni JavaScript orqali almashtiradi!</p>
    </div>
  </section>

  <!-- SLIDE 3: MPA VS SPA ARCHITECTURE -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="12:00–20:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="АРХИТЕКТУРНЫЙ СДВИГ" data-en="ARCHITECTURAL SHIFT">ARXITEKTURA INQILOBI</span></div>
    <h2 data-ru="MPA против SPA: Почему Классический Веб Устарел?" data-en="MPA vs SPA: Why Traditional Web Architecture Shifted">MPA vs SPA: Nega Klassik Veb Tarixga Aylanmoqda?</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:var(--danger); color:#fff;" data-ru="Классика (MPA)" data-en="Traditional MPA">Klassik Ko'p Sahifali (MPA)</div>
        <h3 data-ru="Перезагрузка Каждой Страницы" data-en="Full Page Reload Every Click">Har Bir Klikda Qayta Yuklash</h3>
        <ul style="font-size:12.5px; line-height:1.6;">
          <li data-ru="Каждый клик посылает GET-запрос на сервер за новым HTML." data-en="Every link click sends a GET request for a brand-new HTML document.">Har bir havolani bosganda serverdan yangi HTML so'raladi.</li>
          <li data-ru="Браузер очищает экран (белая вспышка FOUC) и парсит CSS заново." data-en="Browser clears screen (white flash FOUC) and re-parses stylesheets.">Brauzer ekranni tozalaydi (oq miltillash) va CSS/JS ni boshidan o'qiydi.</li>
          <li data-ru="Музыка, видео или сокет-соединение мгновенно разрываются!" data-en="Active music playback, video, or WebSocket streams get disconnected!">Ijro etilayotgan musiqa, video yoki WebSocket aloqasi uzilib qoladi!</li>
        </ul>
      </div>
      <div class="card" style="border:2px solid var(--accent);">
        <div class="tag" style="background:var(--accent); color:#fff;" data-ru="Современный Веб (SPA)" data-en="Modern Web (SPA)">Zamonaviy Bitta Sahifali (SPA)</div>
        <h3 data-ru="Один HTML + Мгновенные Роуты" data-en="Single HTML + Instant Routes">Yagona HTML + 0 ms O'tishlar</h3>
        <ul style="font-size:12.5px; line-height:1.6;">
          <li data-ru="HTML загружается ровно 1 раз при входе на сайт." data-en="Single HTML shell loads once upon initial site visit.">HTML faqat 1 marta — saytga birinchi kirganda yuklanadi.</li>
          <li data-ru="Клики перехватываются JS, обновляется только блок &lt;main&gt;." data-en="Clicks intercepted by JS, updating solely the active view container.">Havolalar JS bilan tutib qolinadi, faqat &lt;main&gt; qismi yangilanadi.</li>
          <li data-ru="Музыка играет непрерывно, WebSocket и WebRTC не обрываются!" data-en="Audio, WebSockets, and WebRTC remain active without interruption!">Fon musiqasi, WebSocket va WebRTC aloqasi uzilishsiz ishlayveradi!</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: HTML5 HISTORY API CORE -->
  <section class="slide" data-phase="History API|History API|History API" data-time="20:00–28:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="ДВИГАТЕЛЬ РОУТИНГА" data-en="ROUTING ENGINE">HTML5 HISTORY API</span></div>
    <h2 data-ru="Сердце SPA: pushState, replaceState и popstate" data-en="Core SPA Engine: pushState, replaceState & popstate">SPA Yuragi: pushState, replaceState va popstate</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Изменяем URL Без Перезагрузки" data-en="Mutating URL Without Reload">URL ni Qayta Yuklamasdan O'zgartirish</h3>
        <pre><code>// 1. Yangi URL va tarix yozuvi:
window.history.pushState(
  { view: 'analytics' }, 
  'Analytics', 
  '/analytics'
);

// 2. Tarixni yangilamasdan almashtirish:
window.history.replaceState({ tab: 1 }, '', '/tab1');

// 3. Orqaga / Oldinga tugmalarini tutish:
window.addEventListener('popstate', (event) =&gt; {
  console.log('Foydalanuvchi orqaga qaytdi:', window.location.pathname);
  renderView(window.location.pathname);
});</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="3 Аргумента pushState" data-en="3 Arguments of pushState">pushState ning 3 Parametri</h3>
        <div style="font-size:13px; line-height:1.7;">
          <div>1. <code>state</code> — <span data-ru="Объект данных, сохраняемый в истории браузера" data-en="Data object serialized into browser history entry">Tarix yozuviga biriktiriladigan ixtiyoriy JS obyekti</span>.</div>
          <div>2. <code>title</code> — <span data-ru="Заголовок страницы (исторически игнорируется браузерами)" data-en="Page title (largely unused by modern browsers)">Sarlavha (hozirgi brauzerlar ko'pincha e'tiborsiz qoldiradi)</span>.</div>
          <div>3. <code>url</code> — <span data-ru="Новый видимый адрес в строке браузера!" data-en="New path displayed in the browser address bar!">Brauzer manzil qatorida ko'rinuvchi yangi URL yo'li!</span></div>
        </div>
        <div class="box mt" style="background:var(--surface-2); padding:10px 14px; font-size:12px; border-left:3px solid var(--accent);">
          <strong>⚡ Oltin Qoida:</strong> <code>pushState</code> manzil qatoridagi URL ni o'zgartiradi, lekin sahifani qayta yuklamaydi. Sahifani yangilash mas'uliyati 100% sizning JS kodingizga yuklanadi!
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: HASH VS PATH ROUTING -->
  <section class="slide" data-phase="Marshrutlash Turlari|Виды Роутинга|Routing Types" data-time="28:00–36:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="АРХИТЕКТУРНЫЙ ВЫБОР" data-en="ARCHITECTURAL CHOICE">MARSHRUTLASH TURLARI</span></div>
    <h2 data-ru="Hash Роутинг (#) против Path Роутинга (/)" data-en="Hash Routing (#) vs Path Routing (/)">Hash Routing (#) va Path Routing (/) Taqqoslovi</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" data-ru="Hash Роутер" data-en="Hash Router">1. Hash Routing (#/terminal)</div>
        <h3 data-ru="Событие hashchange" data-en="hashchange Event">URL Hash Belgisi Bilan</h3>
        <p data-ru="Адрес выглядит как <code>site.com/#/settings</code>. Символ # никогда не отправляется на сервер!" data-en="Address looks like site.com/#/settings. Hash fragment is never sent to the server!">URL manzilda <code>#/settings</code> shaklida bo'ladi. # belgisi serverga yuborilmaydi, faqat brauzer ichida qoladi.</p>
        <ul style="font-size:12px; line-height:1.6;">
          <li data-ru="Плюс: работает везде, не требует настройки веб-сервера." data-en="Pro: Zero server setup required, works anywhere."><strong>Afzalligi:</strong> Hech qanday server sozlamasini talab qilmaydi.</li>
          <li data-ru="Минус: некрасивые ссылки, хуже для SEO." data-en="Con: Cluttered URLs, suboptimal for SEO."><strong>Kamchiligi:</strong> URL manzillar ko'rinishi unchalik chiroyli emas.</li>
        </ul>
      </div>
      <div class="card" style="border:2px solid var(--accent);">
        <div class="tag" style="background:var(--accent); color:#fff;" data-ru="Стандарт Индустрии" data-en="Industry Standard">2. Path Routing (/terminal)</div>
        <h3 data-ru="Чистый History API" data-en="Pure History API">Toza URL Manzillari</h3>
        <p data-ru="Адрес выглядит естественно: <code>site.com/settings</code>. Стандарт для современных сервисов (Next.js, Vite)." data-en="Clean natural URLs: site.com/settings. Used by modern frameworks and production web apps.">URL toza va chiroyli: <code>target.uz/settings</code>. Barcha professional platformalar shu standartda ishlaydi.</p>
        <ul style="font-size:12px; line-height:1.6;">
          <li data-ru="Плюс: красивые URL, идеально для индексации поисковиками." data-en="Pro: Beautiful URLs, pristine SEO semantics."><strong>Afzalligi:</strong> Toza, xalqaro standart va SEO uchun mukammal.</li>
          <li data-ru="Минус: требует серверного редиректа на index.html при F5." data-en="Con: Demands server-side fallback rule for direct visits."><strong>Talabi:</strong> F5 bosilganda server barcha so'rovlarni index.html ga yo'naltirishi shart!</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: LINK INTERCEPTION -->
  <section class="slide" data-phase="Havolalarni Tutish|Перехват Ссылок|Link Interception" data-time="36:00–44:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ТЕХНИКА ПЕРЕХВАТА" data-en="INTERCEPTION PATTERN">LINK INTERCEPTION</span></div>
    <h2 data-ru="Перехват Ссылок: Отменяем Перезагрузку Браузера" data-en="Link Interception: Bypassing Native Page Reloads">Havolalarni Tutib Qolish: e.preventDefault() San'ati</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Глобальный Делегат Кликов" data-en="Global Click Delegator">Markaziy Klik Delegati</h3>
        <pre><code>// Butun hujjat bo'yicha havolalarni tutib qolamiz:
document.addEventListener('click', (e) =&gt; {
  const link = e.target.closest('a[data-link]');
  if (!link) return;

  // Brauzerning sahifani yangilashini to'xtatamiz:
  e.preventDefault();

  const href = link.getAttribute('href');
  navigateTo(href);
});

function navigateTo(url) {
  window.history.pushState(null, '', url);
  router(); // Yangi sahifa komponentini chizish!
}</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Как Это Работает Под Капотом?" data-en="Under-The-Hood Mechanics">Mexanizm Qanday Ishlaydi?</h3>
        <ul style="font-size:13px; line-height:1.7;">
          <li data-ru="<code>closest('a[data-link]')</code>: faqat SPA ichki havolalarini filtrlaydi." data-en="closest('a[data-link]'): isolates internal SPA navigations."><strong>Atribut filtri:</strong> Faqat <code>data-link</code> qo'yilgan ichki havolalar ushlanadi.</li>
          <li data-ru="<code>e.preventDefault()</code>: brauzerning serverga GET so'rov yuborishini bekor qiladi." data-en="e.preventDefault(): aborts native browser page reload."><strong>Yangilashni to'xtatish:</strong> Brauzer serverdan yangi fayl so'ramaydi.</li>
          <li data-ru="<strong>Tashqi havolalar daxlsiz:</strong> Google yoki Telegram havolalari odatdagidek ochilaveradi." data-en="External links intact: third-party URLs navigate normally."><strong>Tashqi havolalar xavfsiz:</strong> Begona saytlarga havolalar erkin ishlaydi.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: ROUTES MAP & RENDERING -->
  <section class="slide" data-phase="Router Mantig'i|Логика Роутера|Router Engine" data-time="44:00–50:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ТАБЛИЦА МАРШРУТОВ" data-en="ROUTES TABLE">ROUTES MAP</span></div>
    <h2 data-ru="Таблица Маршрутов и Динамический Рендеринг Видов" data-en="Routes Map & Dynamic Component Rendering">Marshrutlar Jadvali va Dinamik Komponentlar</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Карта Роутов" data-en="Routes Registry">Marshrutlar Obyekti</h3>
        <pre><code>const routes = {
  '/': ViewDashboard,
  '/traffic': ViewTraffic,
  '/terminal': ViewTerminal,
  '/settings': ViewSettings
};

function router() {
  const path = window.location.pathname;
  const viewRenderer = routes[path] || ViewNotFound;

  // Asosiy konteynerni yangilaymiz:
  const app = document.getElementById('app');
  app.innerHTML = viewRenderer();

  updateActiveNavLink(path);
}</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Смена Активного Класса" data-en="Updating Active Navlink">Aktiv Menyu Tugmasi</h3>
        <p data-ru="Пользователь должен четко видеть, на какой странице находится. Мы находим активный пункт меню и подсвечиваем его:" data-en="Users need clear visual feedback of the active page. We query navigation links and assign the active class:">Foydalanuvchi qaysi bo'limda turganini ko'rishi uchun menyudagi aktiv havolaga <code>active</code> klassi qo'yiladi:</p>
        <pre><code>function updateActiveNavLink(path) {
  document.querySelectorAll('.nav-item').forEach(el =&gt; {
    const isCurrent = el.getAttribute('href') === path;
    el.classList.toggle('active', isCurrent);
  });
}</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: IN-DECK INTERACTIVE SPA DASHBOARD -->
  <section class="slide" data-phase="Jonli SPA|Интерактив|Live SPA" data-time="50:00–60:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ЖИВОЙ ТЕСТ SPA ВНУТРИ СЛАЙДА" data-en="LIVE IN-DECK SPA LAB">JONLI SPA STUDIYASI</span></div>
    <h2 data-ru="Cyber-OS SPA: Мгновенное Переключение Без Перезагрузок!" data-en="Cyber-OS SPA: Zero-Reload Instant Navigation Engine!">Cyber-OS SPA: Qayta Yuklamasdan Bir Zumda Boshqarish!</h2>
    <div style="display:flex; justify-content:center; align-items:center; gap:16px;">
      <div style="width:680px; height:370px; background:#0b0f17; border-radius:12px; border:2px solid var(--accent); overflow:hidden; display:flex; flex-direction:column; box-shadow:0 16px 40px rgba(0,0,0,0.5);">
        <!-- Top Browser URL Mock -->
        <div style="background:#131b28; padding:8px 14px; border-bottom:1px solid #1f2b3e; display:flex; align-items:center; gap:10px; font-size:11px;">
          <button id="spaBtnBack" data-ru="◀ Назад" data-en="◀ Back" style="background:#1c2738; border:none; color:#94a3b8; padding:3px 8px; border-radius:4px; cursor:pointer;">◀ Back</button>
          <button id="spaBtnFwd" data-ru="▶ Вперед" data-en="▶ Fwd" style="background:#1c2738; border:none; color:#94a3b8; padding:3px 8px; border-radius:4px; cursor:pointer;">▶ Fwd</button>
          <div style="flex:1; background:#070a0f; padding:4px 10px; border-radius:6px; color:#00f2fe; font-family:monospace;" id="spaUrlBar">https://target-os.local/dashboard</div>
          <span style="color:#22c55e; font-size:10px; font-weight:700;">● ZERO-RELOAD</span>
        </div>
        <!-- Body: Sidebar + Main Content -->
        <div style="display:flex; flex:1; overflow:hidden;">
          <!-- Sidebar Nav -->
          <div style="width:160px; background:#0e1420; border-right:1px solid #1f2b3e; padding:12px 8px; display:flex; flex-direction:column; gap:6px;">
            <div style="font-size:10px; font-weight:800; color:#64748b; padding:0 8px; margin-bottom:6px;">CYBER-OS</div>
            <button class="spa-nav-btn active" data-path="/dashboard" data-ru="📊 Главная Панель" data-en="📊 Dashboard" style="text-align:left; padding:8px 10px; background:rgba(0,242,254,0.15); color:#00f2fe; border:none; border-radius:6px; font-size:11px; cursor:pointer; font-weight:700;">📊 Asosiy Panel</button>
            <button class="spa-nav-btn" data-path="/traffic" data-ru="📈 Живой Трафик" data-en="📈 Live Traffic" style="text-align:left; padding:8px 10px; background:transparent; color:#94a3b8; border:none; border-radius:6px; font-size:11px; cursor:pointer; font-weight:600;">📈 Jonli Trafik</button>
            <button class="spa-nav-btn" data-path="/terminal" data-ru="⚡ Терминал" data-en="⚡ Terminal" style="text-align:left; padding:8px 10px; background:transparent; color:#94a3b8; border:none; border-radius:6px; font-size:11px; cursor:pointer; font-weight:600;">⚡ Terminal</button>
            <button class="spa-nav-btn" data-path="/settings" data-ru="⚙️ Настройки" data-en="⚙️ Settings" style="text-align:left; padding:8px 10px; background:transparent; color:#94a3b8; border:none; border-radius:6px; font-size:11px; cursor:pointer; font-weight:600;">⚙️ Sozlamalar</button>
          </div>
          <!-- Dynamic App View Container -->
          <div id="spaAppContainer" style="flex:1; padding:16px; overflow-y:auto; color:#e2e8f0; font-size:12px;">
            <!-- Injected via JavaScript -->
          </div>
        </div>
      </div>
      <div style="width:220px; font-size:11px; display:flex; flex-direction:column; gap:8px;">
        <div class="card" style="padding:10px;">
          <h4 style="margin:0 0 6px; font-size:12px; color:var(--accent);" data-ru="🎮 Что Тестируем?" data-en="🎮 What to Test?">🎮 Nimani Sinaymiz?</h4>
          <div>• Tugmalarni bosing: manzil satri o'zgaradi, lekin sahifa yangilanmaydi.</div>
          <div>• <strong>◀ Back / ▶ Fwd:</strong> Tarix bo'yicha orqaga-oldinga yuring.</div>
          <div>• <strong>Trafik</strong> sahifasida jonli Canvas to'lqinini kuzating!</div>
        </div>
        <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:10px; color:var(--ink-2);">
          <strong>History Stack:</strong> Har bir o'tish pushState orqali brauzer xotirasiga yoziladi.
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: DYNAMIC ROUTES & 404 -->
  <section class="slide" data-phase="Dinamik URL|Динамические URL|Dynamic Routes" data-time="60:00–66:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРОДВИНУТЫЙ РОУТИНГ" data-en="ADVANCED ROUTING">DINAMIK URL LAR</span></div>
    <h2 data-ru="Динамические Параметры (/user/:id) и Страница 404" data-en="Dynamic Parameters (/user/:id) & 404 Wildcard">Dinamik Parametrlar (/user/:id) va Wildcard 404</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Регулярные Выражения в Роутере" data-en="Regex Matching in Router">Regex Bilan Parametrlarni Ajratish</h3>
        <pre><code>// /user/:id kabi yo'llarni aniqlash:
function matchRoute(routePath, currentPath) {
  const paramNames = [];
  const regexPath = routePath.replace(/:(\\w+)/g, (_, key) =&gt; {
    paramNames.push(key);
    return '([^\\/]+)';
  });

  const match = currentPath.match(new RegExp(`^${regexPath}$`));
  if (!match) return null;

  // Parametrlarni obyektga yig'amiz:
  const params = {};
  paramNames.forEach((name, i) =&gt; params[name] = match[i + 1]);
  return params;
}</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Обработка Страницы 404" data-en="Handling 404 Fallback">404: Mavjud Bo'lmagan Sahifa</h3>
        <p data-ru="Если пользователь ввел несуществующий URL, роутер не должен падать с ошибкой в консоли! Он рендерит красивый компонент 404:" data-en="If a user navigates to an undefined path, router shouldn't throw unhandled errors! It renders a clean 404 component:">Agar foydalanuvchi noto'g'ri URL yozsa, ro'yxatdan topilmagan sahifa o'rniga chiroyli 404 komponenti ko'rsatiladi:</p>
        <pre><code>function ViewNotFound() {
  return `
    &lt;div class="error-box"&gt;
      &lt;h1&gt;404: SAHIFA TOPILMADI&lt;/h1&gt;
      &lt;p&gt;Kiber-manzil mavjud emas.&lt;/p&gt;
      &lt;a href="/" data-link&gt;Bosh Sahifaga Qaytish&lt;/a&gt;
    &lt;/div&gt;
  `;
}</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: PRODUCTION FALLBACK CONFIG -->
  <section class="slide" data-phase="Server Sozlash|Конфигурация Сервера|Server Fallback" data-time="66:00–70:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="PRODUCTION СЕКРЕТ" data-en="PRODUCTION PITFALL">SERVER FALLBACK SIRI</span></div>
    <h2 data-ru="Ловушка F5: Настройка Vercel и Nginx для SPA" data-en="The F5 Trap: Configuring Vercel & Nginx for SPA">F5 Tuzog'i: Vercel va Nginx ni SPA ga Moslash</h2>
    <div class="grid-2">
      <div class="card" style="border-left:4px solid var(--danger);">
        <h3 data-ru="В Чем Заключается Ловушка F5?" data-en="What is the F5 Reload Trap?">Nega F5 Bosilganda 404 Chiqadi?</h3>
        <p data-ru="Вы перешли на <code>site.com/traffic</code> через JS — всё работает. Но если нажать F5, браузер обращается к физическому серверу: <em>'Дай мне файл /traffic/index.html'</em>. А такого файла на диске нет! Сервер выдает стандартную 404 Not Found!" data-en="Navigating to /traffic via JS works great. But pressing F5 makes the browser query the web server for a physical file /traffic. Since it doesn't exist, server returns 404 Not Found!">Siz JS orqali <code>/traffic</code> ga o'tdingiz — barchasi ishlayapti. Ammo F5 bossangiz, brauzer to'g'ridan-to'g'ri serverdan <code>/traffic</code> faylini so'raydi. Diskda bunday papka bo'lmagani uchun server 404 xatosini beradi!</p>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3 data-ru="Решение: SPA Rewrite Rule" data-en="Fix: SPA Rewrite Rule">Yechim: Barcha So'rovlarni index.html ga Yo'naltirish</h3>
        <div style="font-size:11px; margin-bottom:6px; font-weight:700;">1. vercel.json:</div>
        <pre><code>{
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}</code></pre>
        <div style="font-size:11px; margin:6px 0; font-weight:700;">2. Nginx config:</div>
        <pre><code>location / {
  try_files $uri $uri/ /index.html;
}</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: VIBECODING BLUEPRINT -->
  <section class="slide" data-phase="Vibecoding Metodi|Метод Vibecoding|Prompt Engineering" data-time="70:00–74:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="МЕТОДИКА VIBECODING" data-en="VIBECODING METHOD">AI PROMPT ARXITEKTURASI</span></div>
    <h2 data-ru="Сборка SPA на Vanilla JS за 4 Промпта в AI" data-en="Building a Vanilla JS SPA via 4 AI Prompts">Vanilla JS SPA ni 4 Qadamda AI Bilan Yaratish</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:var(--accent); color:#fff;" data-ru="1-й и 2-й Промпты" data-en="Prompts 1 & 2">1-va 2-Promptlar</div>
        <h4 style="margin:4px 0 6px; font-size:12px;" data-ru="Скелет Роутера + Перехват Ссылок" data-en="Router Shell + Link Interception">Router Skeleti + Havolalarni Tutish</h4>
        <pre><code>"Toza Vanilla JS da SPA router tizimini yarat.
1) window.history.pushState va popstate hodisasini
bog'la. 2) Barcha a[data-link] havolalarni bosganda
e.preventDefault() bilan sahifa yangilanishini to'xtatib,
URL ni manzil satrida o'zgartiruvchi navigateTo() yoz!"</code></pre>
      </div>
      <div class="card">
        <div class="tag" style="background:var(--accent); color:#fff;" data-ru="3-й и 4-й Промпты" data-en="Prompts 3 & 4">3-va 4-Promptlar</div>
        <h4 style="margin:4px 0 6px; font-size:12px;" data-ru="Виды + Активное Меню + Анимация" data-en="Views + Active Navigation + Transition">Komponentlar + Aktiv Menyu + Animatsiya</h4>
        <pre><code>"Routes xaritasini tuz: /dashboard, /traffic,
/terminal va /settings. Har bir sahifa uchun HTML
qaytarsin. Navigatsiya menyusida hozirgi sahifaga
'active' klassini qo'sh. Sahifalar almashganda
silliq fade-in CSS animatsiyasi bo'lsin!"</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: PEER CODE REVIEW & PLAYTEST -->
  <section class="slide" data-phase="Playtesting|Тестирование|Playtesting" data-time="74:00–77:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ПАРНЫЙ АУДИТ КОДА" data-en="PEER CODE REVIEW">JUFTLIKDA KOD AUDITI</span></div>
    <h2 data-ru="Критерии Приемки SPA: Проверь Проект Партнера!" data-en="SPA Acceptance Criteria: Audit Your Peer's App!">SPA Qabul Qilish Mezonlari: Partadoshing Loyihasini Tekshir!</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" data-ru="Тест 1" data-en="Test 1">1. Zero-Reload Tekshiruvi</div>
        <h3 data-ru="Без Белого Экрана" data-en="Zero White Flash">Nol Miltillash</h3>
        <p data-ru="При кликах по боковому меню вкладка браузера не крутит спиннер загрузки? Экран не моргает?" data-en="Does clicking sidebar links avoid browser tab reload spinners and white flickers?">Menyuni bosganda brauzer vkladkasidagi aylanuvchi spinner chiqmayaptimi? Oq ekran yo'qmi?</p>
      </div>
      <div class="card">
        <div class="tag" data-ru="Тест 2" data-en="Test 2">2. Back / Forward Tugmalari</div>
        <h3 data-ru="История Браузера" data-en="Browser History">Tarixga Qaytish</h3>
        <p data-ru="Браузерная кнопка 'Назад' возвращает на предыдущий вид и обновляет активный пункт меню?" data-en="Does clicking browser 'Back' restore previous view and update active nav link?">Brauzerdagi "Orqaga" tugmasi avvalgi sahifani to'g'ri tiklayaptimi va menyuni bo'yayaptimi?</p>
      </div>
      <div class="card">
        <div class="tag" data-ru="Тест 3" data-en="Test 3">3. 404 Fallback Himoyasi</div>
        <h3 data-ru="Без Ошибок в Консоли" data-en="Zero Console Errors">Toza Konsol</h3>
        <p data-ru="Если вбить несуществующий путь (напр. /random), открывается ли красивый вид 404?" data-en="Does navigating to undefined paths render a graceful 404 view without errors?">Mavjud bo'lmagan yo'l kiritilganda konsolda qizil xatolarsiz chiroyli 404 ekrani chiqadimi?</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: GOLDEN RULES & CONCLUSION -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="77:00–79:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И ЗОЛОТЫЕ ПРАВИЛА" data-en="GOLDEN RULES & SUMMARY">XULOSA VA OLTIN QOIDALAR</span></div>
    <h2 data-ru="4 Столпа Архитектуры Single Page Application" data-en="4 Pillars of Single Page Architecture">SPA Arxitekturasining 4 Oltin Qoidasi</h2>
    <div class="grid-2">
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3 data-ru="1. Браузер Не Должен Перезагружаться" data-en="1. Prevent Default Navigation">1. Sahifani Qayta Yuklash Taqiqlanadi</h3>
        <p data-ru="Все внутренние ссылки перехватываются через e.preventDefault(). Перезагрузка убивает WebSocket и сбрасывает состояние." data-en="All internal links must be caught by e.preventDefault(). Reloads destroy active WebSockets and state.">Barcha ichki havolalar e.preventDefault() bilan ushlanadi. Qayta yuklash WebSocket va WebRTC ni uzib qo'yadi.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3 data-ru="2. URL Всегда Соответствует Экрану" data-en="2. URL Must Match UI">2. URL Doimo Ekranga Mos Bo'lsin</h3>
        <p data-ru="Никогда не меняйте вид без вызова pushState. Пользователь должен иметь возможность поделиться ссылкой или нажать Назад." data-en="Never swap views without calling pushState. Users must be able to share direct links or navigate back.">Hech qachon pushState chaqirmasdan sahifani o'zgartirmang. Foydalanuvchi havolani ulasha olishi kerak.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3 data-ru="3. Очистка Слушателей (No Memory Leaks)" data-en="3. Clean Component Listeners">3. Xotirani Tozalash (Cleanup)</h3>
        <p data-ru="При уходе со страницы удаляйте интервалы (clearInterval) и слушатели, иначе через 5 переходов память заполнится!" data-en="Clear intervals and event listeners when switching views, preventing memory leaks over time.">Boshqa sahifaga o'tganda taymerlar (clearInterval) va tinglovchilar tozalanishi shart.</p>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <h3 data-ru="4. Всегда Настраивайте Fallback на Сервере" data-en="4. Always Setup Server Fallback">4. Serverda Doimo Fallback Bo'lsin</h3>
        <p data-ru="В Vercel (rewrites) или Nginx (try_files) всегда направляйте все запросы на index.html для предотвращения ошибки 404 при F5." data-en="Configure Vercel rewrites or Nginx try_files to point all queries to index.html, preventing F5 404s.">F5 bosilganda 404 xatosi chiqmasligi uchun serverdagi barcha so'rovlar index.html ga yo'naltirilgan bo'lishi shart.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: 3-TIER HOMEWORK & RUBRIC -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Homework" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ДОМАШНЕЕ ЗАДАНИЕ · 10 БАЛЛОВ" data-en="HOMEWORK · 10 POINTS">3 DARAJALI UY VAZIFASI</span></div>
    <h2 data-ru="Проект Cyber-OS: Создай Собственную SPA Панель!" data-en="Cyber-OS Project: Engineer Your Custom SPA Dashboard!">Cyber-OS Loyihasi: O'z Shaxsiy SPA Panelini Yarat!</h2>
    <div class="grid-3">
      <div class="card" style="border-top:4px solid var(--accent);">
        <div class="tag" data-ru="Уровень 1: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</div>
        <h3 data-ru="Роутер на 3 Страницы" data-en="3-Route SPA">3 Sahifali SPA Router</h3>
        <p data-ru="Реализовать History API pushState и popstate с 3 видами (Главная, О проекте, Контакты) без единой перезагрузки страницы." data-en="Implement History API pushState and popstate across 3 distinct views without a single page reload.">History API pushState va popstate bilan 3 ta sahifani sahifani qayta yuklamasdan boshqarish.</p>
      </div>
      <div class="card" style="border-top:4px solid var(--accent);">
        <div class="tag" data-ru="Уровень 2: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</div>
        <h3 data-ru="Перехват Ссылок + Меню" data-en="Link Interception + Nav">Havolalar va Aktiv Menyu</h3>
        <p data-ru="Добавить глобальный перехватчик кликов на a[data-link], подсветку активного пункта меню и страницу 404 Not Found." data-en="Add global a[data-link] click interceptor, active navigation highlighting, and a 404 view.">a[data-link] havolalarni tutib qolish, aktiv menyu indikatori va 404 Not Found sahifasini qurish.</p>
      </div>
      <div class="card" style="border-top:4px solid var(--danger);">
        <div class="tag" style="background:var(--danger); color:#fff;" data-ru="Уровень 3: Кибер-Вызов (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Challenge (2 ball)</div>
        <h3 data-ru="Анимация и Vercel SPA" data-en="Transitions & Deploy">Silliq Fade va Vercel</h3>
        <p data-ru="Добавить плавную CSS анимацию смены экранов (fade-in 0.2s) и выложить проект на Vercel с правильным vercel.json rewrites!" data-en="Add smooth CSS view transitions (fade-in 0.2s) and deploy to Vercel with proper vercel.json rewrites!">Silliq fade-in animatsiyasini qo'shish va to'g'ri vercel.json konfiguratsiyasi bilan Vercel ga deploy qilish!</p>
      </div>
    </div>
    <div class="card mt" style="background:var(--surface-2); padding:10px 16px;">
      <p style="margin:0; font-size:12px; color:var(--ink-2);" data-ru="Сдача работы: прислать ссылку на репозиторий GitHub или живой Vercel деплой." data-en="Submission: Send GitHub repository link or live Vercel production deployment.">Topshirish: GitHub repozitoriy kodi yoki jonli Vercel havolasini topshirish.</p>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. TEACHER NOTES DATA (14 Slides x [Title, Say, Do] triplets across uz, ru, en)
# -----------------------------------------------------------------------------
TRIPLETS_UZ = [
    [
        "Titul va Darsga Kirish",
        "Bugun zamonaviy veb-ishlanmalarning asosi bo'lgan SPA (Single Page Application) arxitekturasini o'rganamiz. Nega Gmail, YouTube yoki Telegram Web bir marta ham oqarib qayta yuklanmaydi?",
        "Ekranda Cyber-OS sarlavhasini oching va o'quvchilarda yuqori qiziqish uyg'oting."
    ],
    [
        "32-Dars Uy Vazifasi Tahlili",
        "O'tgan darsdagi eng katta xato: video-chat yopilganda kamera treklari to'xtatilmagan va noutbukning yashil chirog'i yonib qolavergan. track.stop() chaqirish shart!",
        "Doskada track.stop() tozalash kodini ko'rsating va 30 soniyalik blitz savol bering."
    ],
    [
        "MPA va SPA Taqqoslovi",
        "Klassik saytlar har bir klikda serverdan yangi HTML oladi va oq ekran bo'ladi. SPA da esa bitta HTML yuklanadi va JS orqali kontent bir zumda yangilanadi.",
        "Doskada ikkala arxitektura o'rtasidagi so'rovlar oqimini solishtirib bering."
    ],
    [
        "HTML5 History API Mexanikasi",
        "pushState URL manzilni o'zgartiradi, lekin sahifani qayta yuklamaydi. popstate esa brauzerning 'Orqaga' tugmasini ushlaydi.",
        "Konsolda pushState chaqirib, manzil satri qanday o'zgarishini jonli ko'rsating."
    ],
    [
        "Hash va Path Routing",
        "Hash routing # belgisi bilan ishlaydi va server sozlamasini talab qilmaydi. Path routing esa toza va zamonaviy, lekin serverda qayta yo'naltirish talab qiladi.",
        "Ikkala usulning afzallik va kamchiliklarini tushuntiring."
    ],
    [
        "Link Interception San'ati",
        "Foydalanuvchi havolani bosganda e.preventDefault() bilan brauzerning serverga so'rov yuborishini to'xtatamiz va navigateTo() chaqiramiz.",
        "Markaziy klik tinglovchisi kodini tahlil qiling."
    ],
    [
        "Marshrutlar Xaritasi va Dinamik View",
        "routes obyekti URL yo'lini mos funksiya bilan bog'laydi. Sahifa o'zgarganda menyudagi aktiv tugma ham yashil rangga bo'yaladi.",
        "O'quvchilarga yangi sahifa qo'shish qanchalik osonligini ko'rsating."
    ],
    [
        "Jonli Test: Cyber-OS SPA Studiyasi",
        "Hozir slayddagi simulyatorda tugmalarni bosing. Sahifa biror marta ham qayta yuklanmasdan grafik, terminal va sozlamalar ochilishini sinang!",
        "O'quvchilarga simulyatorda Back va Forward tugmalarini bosib ko'rishga ruxsat bering."
    ],
    [
        "Dinamik Parametrlar va 404",
        "Regex yordamida /user/:id kabi yo'llardan ID ni ajratib olamiz. Noma'lum yo'llar uchun esa 404 komponentini ko'rsatamiz.",
        "Regex kodini va 404 sahifasini ko'rsatib bering."
    ],
    [
        "F5 Tuzog'i va Server Fallback",
        "Katta xato: SPA da F5 bosilganda server 404 beradi. Chunki fayl diskda yo'q. Vercel da rewrites, Nginx da try_files qoidasi qo'yiladi.",
        "vercel.json faylini qanday yozish kerakligini ko'rsating."
    ],
    [
        "Vibecoding Prompt Arxitekturasi",
        "Cursor yoki ChatGPT ga bitta uzun xat yozmang. 4 ta ketma-ket prompt orqali router, havolalar, komponentlar va animatsiyani qurdiring.",
        "Slayddagi 4 ta promptni birma-bir o'qib tushuntiring."
    ],
    [
        "Juftlikda Kod Auditi (Review)",
        "Partadoshingiz noutbukiga qarab, Back tugmasi to'g'ri ishlashini va F5 bosilganda xato bo'lmasligini tekshiring.",
        "O'quvchilar o'rtasida o'zaro sifat nazorati va playtesting o'tkazing."
    ],
    [
        "SPA ning 4 Oltin Qoidasi",
        "Qayta yuklamaslik, URL ni doimo ekranga moslash, xotirani tozalash va serverda fallback sozlash.",
        "Darsning asosiy xulosalarini jamlang."
    ],
    [
        "3 Darajali Uy Vazifasi",
        "Baza (4b): 3 sahifali router. Muhandislik (4b): link interception va 404. Challenge (2b): fade animatsiyasi va Vercel deploy.",
        "10 ballik mezonni tushuntiring va savollarga javob bering."
    ]
]

TRIPLETS_RU = [
    [
        "Титул и Введение",
        "Сегодня мы изучаем фундамент современного веба — архитектуру SPA. Почему Gmail, YouTube и Telegram Web никогда не моргают белым экраном?",
        "Откройте титульный слайд Cyber-OS и создайте живой интерес у школьников."
    ],
    [
        "Разбор ДЗ 32-урока",
        "Главная ошибка прошлого урока: при закрытии звонка треки камеры не останавливались и зеленый индикатор продолжал гореть. Нужен track.stop()!",
        "Покажите код очистки аппаратных ресурсов и проведите 30-секундный блиц."
    ],
    [
        "Сравнение MPA и SPA",
        "Классические сайты запрашивают полный HTML на каждый клик. В SPA загружается один HTML, а виды сменяются через JS за 0 миллисекунд.",
        "Сравните сетевые потоки традиционного и современного веба."
    ],
    [
        "Механика HTML5 History API",
        "pushState меняет видимый URL в адресной строке без перезагрузки, а popstate перехватывает клики по кнопке 'Назад'.",
        "В консоли вызовите pushState и покажите изменение адресной строки вживую."
    ],
    [
        "Hash и Path Роутинг",
        "Hash роутинг работает через знак # и не требует настройки сервера. Path роутинг чистый и современный, но требует редиректа на сервере.",
        "Объясните плюсы и минусы обоих подходов к маршрутизации."
    ],
    [
        "Искусство Перехвата Ссылок",
        "Через e.preventDefault() отменяем стандартный сетевой запрос браузера и передаем управление внутренней функции navigateTo().",
        "Разберите центральный делегат кликов по ссылкам."
    ],
    [
        "Таблица Роутов и Рендеринг",
        "Объект routes сопоставляет URL путь с нужным компонентом. При смене экрана активная кнопка меню подсвечивается.",
        "Покажите, как легко расширять маршруты новыми страницами."
    ],
    [
        "Живой Тест: Студия Cyber-OS SPA",
        "Кликайте по кнопкам внутри слайда: наблюдайте моментальную смену графика трафика, терминала и настроек без единой перезагрузки!",
        "Дайте ребятам покликать кнопки симулятора прямо в презентации."
    ],
    [
        "Динамические Роуты и 404",
        "С помощью регулярных выражений извлекаем параметры вида /user/:id. А для несуществующих путей рендерим заглушку 404.",
        "Продемонстрируйте парсинг параметров из адресной строки."
    ],
    [
        "Ловушка F5 и Серверный Fallback",
        "При нажатии F5 в SPA веб-сервер выдает 404, если не настроен fallback. В Vercel пишем rewrites, в Nginx — try_files.",
        "Покажите правильный конфигурационный файл vercel.json."
    ],
    [
        "Методика Vibecoding в AI",
        "Не отправляйте длинные запросы. Через 4 последовательных промпта соберите роутер, перехват, компоненты и анимацию.",
        "Разберите 4 шага промптов вместе с классом."
    ],
    [
        "Парный Аудит Кода",
        "Проверьте проект соседа по парте: работает ли кнопка Назад, не ломается ли сайт при F5 и чиста ли консоль.",
        "Организуйте взаимопроверку кода и поиск багов."
    ],
    [
        "4 Закона Архитектуры SPA",
        "Без перезагрузок, соответствие URL экрану, очистка интервалов и серверный fallback.",
        "Сформулируйте итоговые инженерные законы урока."
    ],
    [
        "3 Уровня Домашнего Задания",
        "База (4б): роутер на 3 вида. Инженерия (4б): перехват ссылок и 404. Челлендж (2б): плавный fade и Vercel деплой.",
        "Разъясните критерии оценки на 10 баллов."
    ]
]

TRIPLETS_EN = [
    [
        "Title & Intro",
        "Today we master the cornerstone of modern web architecture: Single Page Applications. Why do Gmail, YouTube, and Telegram Web never reload?",
        "Open the Cyber-OS title slide and spark student engagement."
    ],
    [
        "Lesson 32 HW Review",
        "Major pitfall from last lesson: camera tracks weren't halted upon call exit, keeping hardware active. track.stop() is required!",
        "Present the hardware cleanup snippet and run the 30s blitz."
    ],
    [
        "MPA vs SPA Architecture",
        "Traditional sites fetch full HTML on every click, causing white flickers. SPAs load one shell and swap views instantly via JS.",
        "Contrast traditional round-trips against fluid client-side rendering."
    ],
    [
        "HTML5 History API Core",
        "pushState modifies browser URL without reloading, while popstate captures navigation back/forward events.",
        "Execute pushState in browser DevTools to demonstrate dynamic URL shifts."
    ],
    [
        "Hash vs Path Routing",
        "Hash routing uses the # symbol and needs zero server config. Path routing provides clean URLs but demands server fallbacks.",
        "Explain pros and cons of both routing strategies."
    ],
    [
        "Link Interception Technique",
        "Using e.preventDefault(), we intercept browser link clicks and route navigation to our custom navigateTo() function.",
        "Break down global click delegation architecture."
    ],
    [
        "Routes Map & View Rendering",
        "The routes registry maps URL paths to component functions. When paths change, navigation links receive active highlights.",
        "Demonstrate how simple it is to add new view endpoints."
    ],
    [
        "Live In-Deck Cyber-OS Lab",
        "Click the sidebar items right inside the slide: observe instant traffic charts, terminal views, and settings with zero reload!",
        "Allow students to test drive the simulator directly in the deck."
    ],
    [
        "Dynamic Routes & 404 Fallback",
        "Using regular expressions, extract route parameters like /user/:id. Render a fallback view for unmapped paths.",
        "Walk through route parameter parsing and 404 templates."
    ],
    [
        "The F5 Reload Trap & Server Fallback",
        "Pressing F5 in an SPA triggers server 404 if direct paths lack files. Use Vercel rewrites or Nginx try_files rules.",
        "Explain production vercel.json rewrite configurations."
    ],
    [
        "Vibecoding Prompt Blueprint",
        "Don't dump monolithic prompts. Guide AI through 4 incremental prompts: router shell, interception, views, and animations.",
        "Walk through the 4 prompt stages with the class."
    ],
    [
        "Peer Code Review",
        "Audit your partner's repository: test browser Back buttons, verify zero reload flickers, and audit console health.",
        "Coordinate peer review and code auditing."
    ],
    [
        "4 Open SPA Principles",
        "Zero reload, URL parity, listener cleanup, and mandatory server fallback.",
        "Summarize core engineering takeaways."
    ],
    [
        "3-Tiered Homework",
        "Base (4 pts): 3-view router. Engineering (4 pts): link interception & 404. Challenge (2 pts): fade transition & Vercel deploy.",
        "Clarify the 10-point rubric and address questions."
    ]
]

NOTES_DATA = {
    "uz": TRIPLETS_UZ,
    "ru": TRIPLETS_RU,
    "en": TRIPLETS_EN
}

# -----------------------------------------------------------------------------
# 3. INTERACTIVE SIMULATOR SCRIPT (Deck + Standalone)
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
// =============================================================================
// CYBER-OS SPA ENGINE & ROUTER SIMULATOR
// =============================================================================
(function() {
  const container = document.getElementById('spaAppContainer');
  const urlBar = document.getElementById('spaUrlBar');
  const btnBack = document.getElementById('spaBtnBack');
  const btnFwd = document.getElementById('spaBtnFwd');
  if (!container || !urlBar) return;

  // Internal Navigation History Stack for In-Deck Mock
  const historyStack = ['/dashboard'];
  let historyIndex = 0;

  // View Components
  function ViewDashboard() {
    return `
      <div style="animation: fadeIn 0.25s ease;">
        <h3 data-ru="📊 Состояние кибер-системы: Панель управления" data-en="📊 Cyber System State: Control Dashboard" style="margin:0 0 10px; color:#00f2fe; font-size:14px;">📊 Kiber-Tizim Holati: Boshqaruv Paneli</h3>
        <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; margin-bottom:12px;">
          <div style="background:#131d2e; padding:10px; border-radius:8px; border:1px solid #1f2f47;">
            <div class="t" data-ru="НАГРУЗКА CPU" data-en="CPU LOAD" style="font-size:10px; color:#94a3b8;">CPU YUKLAMASI</div>
            <div style="font-size:18px; font-weight:800; color:#22c55e;">24.8%</div>
            <div class="t" data-ru="4 ядра активны" data-en="4 Cores Active" style="font-size:9px; color:#64748b;">4 Cores Active</div>
          </div>
          <div style="background:#131d2e; padding:10px; border-radius:8px; border:1px solid #1f2f47;">
            <div class="t" data-ru="ПАМЯТЬ (RAM)" data-en="MEMORY (RAM)" style="font-size:10px; color:#94a3b8;">XOTIRA (RAM)</div>
            <div style="font-size:18px; font-weight:800; color:#00f2fe;">4.2 GB</div>
            <div class="t" data-ru="16 GB всего" data-en="16 GB Total" style="font-size:9px; color:#64748b;">16 GB Umumiy</div>
          </div>
          <div style="background:#131d2e; padding:10px; border-radius:8px; border:1px solid #1f2f47;">
            <div class="t" data-ru="P2P УЗЛЫ" data-en="P2P NODES" style="font-size:10px; color:#94a3b8;">P2P ULANISHLAR</div>
            <div class="t" data-ru="12 Узлов" data-en="12 Nodes" style="font-size:18px; font-weight:800; color:#eab308;">12 Tugun</div>
            <div class="t" data-ru="Сеть WebRTC Mesh" data-en="WebRTC Mesh Net" style="font-size:9px; color:#64748b;">WebRTC Mesh</div>
          </div>
        </div>
        <div style="background:#0e1624; padding:10px; border-radius:8px; border:1px solid #1b263b;">
          <div class="t" data-ru="🚀 Преимущество архитектуры SPA:" data-en="🚀 Advantage of SPA Engine:" style="font-weight:700; color:#38bdf8; margin-bottom:6px;">🚀 SPA Mexanizmi Afzalligi:</div>
          <p data-ru="При переходе на эту страницу браузер не запрашивал новый HTML у сервера. Через History API URL обновился мгновенно, а компонент перерисовался за 0.1 миллисекунды!" data-en="When navigating here, the browser did not request new HTML from the server. Using the History API, the URL updated instantly and only this container re-rendered in 0.1ms!" style="margin:0; font-size:11px; color:#94a3b8; line-height:1.5;">Ushbu sahifaga o'tganda brauzer serverdan yangi HTML so'ramadi. JavaScript History API orqali URL o'zgartirildi va faqat shu konteyner 0.1 millisekundda yangilandi!</p>
        </div>
      </div>
    `;
  }

  function ViewTraffic() {
    setTimeout(initTrafficCanvas, 20);
    return `
      <div style="animation: fadeIn 0.25s ease;">
        <h3 data-ru="📈 Сетевой трафик в реальном времени (Live WebRTC Mesh)" data-en="📈 Real-Time Network Traffic (Live WebRTC Mesh)" style="margin:0 0 10px; color:#00f2fe; font-size:14px;">📈 Real-Vaqt Tarmoq Trafiki (Live WebRTC Mesh)</h3>
        <div style="background:#0e1624; border-radius:8px; border:1px solid #1f2f47; padding:10px; margin-bottom:10px;">
          <canvas id="spaTrafficCanvas" width="460" height="150" style="width:100%; height:150px; display:block;"></canvas>
        </div>
        <div style="display:flex; justify-content:space-between; font-size:11px; color:#94a3b8;">
          <div><span class="t" data-ru="Входящий:" data-en="Inbound:">Kiruvchi:</span> <span style="color:#22c55e; font-weight:700;">842 KB/s</span></div>
          <div><span class="t" data-ru="Исходящий:" data-en="Outbound:">Chiquvchi:</span> <span style="color:#38bdf8; font-weight:700;">310 KB/s</span></div>
          <div><span class="t" data-ru="Потеря пакетов:" data-en="Packet Loss:">Paketlar Yo'qolishi:</span> <span style="color:#eab308; font-weight:700;">0.00%</span></div>
        </div>
      </div>
    `;
  }

  function ViewTerminal() {
    return `
      <div style="animation: fadeIn 0.25s ease;">
        <h3 data-ru="⚡ Кибер-терминал: Командный центр" data-en="⚡ Cyber-Terminal: Command Center" style="margin:0 0 10px; color:#00f2fe; font-size:14px;">⚡ Kiber-Terminal: Buyruqlar Markazi</h3>
        <div style="background:#070a0f; border:1px solid #1f2f47; border-radius:8px; padding:12px; font-family:monospace; font-size:11px; height:180px; overflow-y:auto; line-height:1.6;" id="spaTerminalOutput">
          <div class="t" data-ru="[system] Маршрутизатор Cyber-OS v3.2 инициализирован." data-en="[system] Cyber-OS v3.2 Client-Side Router initialized." style="color:#22c55e;">[system] Cyber-OS v3.2 Client-Side Router initialized.</div>
          <div class="t" data-ru="[webrtc] Канал данных DataChannel установлен с узлом #48." data-en="[webrtc] DataChannel established with Peer #48." style="color:#38bdf8;">[webrtc] DataChannel established with Peer #48.</div>
          <div class="t" data-ru="[router] Переход на /terminal выполнен без перезагрузки." data-en="[router] Navigated to /terminal without full reload." style="color:#eab308;">[router] Navigated to /terminal without full reload.</div>
          <div class="t" data-ru="&gt; ввод команд: help, status, ping, clear" data-en="&gt; available commands: help, status, ping, clear" style="color:#94a3b8; margin-top:8px;">&gt; buyruq kiritish: help, status, ping, clear</div>
        </div>
        <div style="display:flex; gap:8px; margin-top:10px;">
          <input type="text" id="spaTerminalInput" placeholder="Buyruq yozing..." data-placeholder-ru="Введите команду..." data-placeholder-en="Type a command..." style="flex:1; background:#0e1624; border:1px solid #1f2f47; color:#00f2fe; padding:6px 10px; border-radius:6px; font-family:monospace; font-size:11px;" />
          <button id="spaTerminalSend" class="t" data-ru="Запуск" data-en="Run" style="background:var(--accent, #00f2fe); color:#000; font-weight:700; border:none; padding:6px 14px; border-radius:6px; cursor:pointer;">Run</button>
        </div>
      </div>
    `;
  }

  function ViewSettings() {
    return `
      <div style="animation: fadeIn 0.25s ease;">
        <h3 data-ru="⚙️ Настройки системы (LocalStorage State)" data-en="⚙️ System Settings (LocalStorage State)" style="margin:0 0 10px; color:#00f2fe; font-size:14px;">⚙️ Tizim Sozlamalari (LocalStorage State)</h3>
        <div style="display:flex; flex-direction:column; gap:10px;">
          <label style="display:flex; align-items:center; justify-content:space-between; background:#131d2e; padding:10px; border-radius:8px;">
            <span class="t" data-ru="Неоновый кибер-режим" data-en="Neon Cyber Mode">Neon Cyber Rejimi</span>
            <input type="checkbox" checked style="accent-color:#00f2fe;" />
          </label>
          <label style="display:flex; align-items:center; justify-content:space-between; background:#131d2e; padding:10px; border-radius:8px;">
            <span class="t" data-ru="Плавный переход видов (0.2s Fade)" data-en="Smooth View Transition (0.2s Fade)">Silliq View Transition (0.2s Fade)</span>
            <input type="checkbox" checked style="accent-color:#00f2fe;" />
          </label>
          <label style="display:flex; align-items:center; justify-content:space-between; background:#131d2e; padding:10px; border-radius:8px;">
            <span class="t" data-ru="Аппаратное видео-ускорение" data-en="Hardware Video Acceleration">Hardware Video Tezlatgichi</span>
            <input type="checkbox" checked style="accent-color:#00f2fe;" />
          </label>
        </div>
      </div>
    `;
  }

  const routes = {
    '/dashboard': ViewDashboard,
    '/traffic': ViewTraffic,
    '/terminal': ViewTerminal,
    '/settings': ViewSettings
  };

  function render(path) {
    window.__currentSpaPath = path;
    const viewFn = routes[path] || ViewDashboard;
    container.innerHTML = viewFn();
    urlBar.textContent = 'https://target-os.local' + path;

    // Immediately translate newly injected view components to current lang
    const curLang = document.documentElement.getAttribute('data-lang') || 'uz';
    if (curLang !== 'uz') {
      container.querySelectorAll('[data-ru][data-en]').forEach(el => {
        const val = el.getAttribute('data-' + curLang);
        if (val) el.innerHTML = val;
      });
      container.querySelectorAll('[data-placeholder-ru][data-placeholder-en]').forEach(el => {
        const val = el.getAttribute('data-placeholder-' + curLang);
        if (val) el.placeholder = val;
      });
    }

    // Update active nav button
    document.querySelectorAll('.spa-nav-btn').forEach(btn => {
      const match = btn.getAttribute('data-path') === path;
      btn.style.background = match ? 'rgba(0,242,254,0.15)' : 'transparent';
      btn.style.color = match ? '#00f2fe' : '#94a3b8';
      btn.style.fontWeight = match ? '700' : '600';
    });

    document.querySelectorAll('.nav-link').forEach(link => {
      const match = link.getAttribute('href') === path || link.getAttribute('data-path') === path;
      link.classList.toggle('active', match);
    });

    // Hook terminal input if view is terminal
    if (path === '/terminal') {
      setTimeout(bindTerminal, 30);
    }
  }

  window.__renderSpa = render;

  function navigate(path, push = true) {
    if (push) {
      // Truncate forward history if navigating new path
      historyStack.splice(historyIndex + 1);
      historyStack.push(path);
      historyIndex = historyStack.length - 1;
    }
    render(path);
  }

  // Nav click handlers (deck buttons or studio nav links)
  document.querySelectorAll('.spa-nav-btn, .nav-link').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const path = btn.getAttribute('data-path') || btn.getAttribute('href');
      if (path) navigate(path, true);
    });
  });

  // Back / Fwd Handlers
  if (btnBack) {
    btnBack.addEventListener('click', () => {
      if (historyIndex > 0) {
        historyIndex--;
        navigate(historyStack[historyIndex], false);
      }
    });
  }
  if (btnFwd) {
    btnFwd.addEventListener('click', () => {
      if (historyIndex < historyStack.length - 1) {
        historyIndex++;
        navigate(historyStack[historyIndex], false);
      }
    });
  }

  // Live Canvas Wave
  let animId = null;
  function initTrafficCanvas() {
    const cvs = document.getElementById('spaTrafficCanvas');
    if (!cvs) return;
    const ctx = cvs.getContext('2d');
    let offset = 0;

    if (animId) cancelAnimationFrame(animId);

    function draw() {
      if (!document.getElementById('spaTrafficCanvas')) return;
      ctx.clearRect(0, 0, cvs.width, cvs.height);
      ctx.strokeStyle = '#00f2fe';
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = 0; x < cvs.width; x++) {
        const y = cvs.height / 2 + Math.sin((x + offset) * 0.05) * 30 + Math.cos((x + offset * 0.5) * 0.03) * 15;
        if (x === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();
      offset += 2;
      animId = requestAnimationFrame(draw);
    }
    draw();
  }

  function bindTerminal() {
    const input = document.getElementById('spaTerminalInput');
    const send = document.getElementById('spaTerminalSend');
    const out = document.getElementById('spaTerminalOutput');
    if (!input || !send || !out) return;

    function exec() {
      const cmd = input.value.trim().toLowerCase();
      if (!cmd) return;
      const row = document.createElement('div');
      row.style.color = '#00f2fe';
      row.textContent = '> ' + cmd;
      out.appendChild(row);

      const resp = document.createElement('div');
      if (cmd === 'help') resp.textContent = 'Buyruqlar: status, ping, clear, router';
      else if (cmd === 'status') resp.textContent = 'SPA Router: ONLINE · Active View: /terminal · Zero Reloads: 100%';
      else if (cmd === 'ping') resp.textContent = 'P2P latency to target server: 8.2ms';
      else if (cmd === 'clear') { out.innerHTML = ''; input.value = ''; return; }
      else resp.textContent = "Noma'lum buyruq: " + cmd + '. "help" yozing.';

      resp.style.color = '#94a3b8';
      out.appendChild(resp);
      out.scrollTop = out.scrollHeight;
      input.value = '';
    }

    send.addEventListener('click', exec);
    input.addEventListener('keydown', (e) => { if (e.key === 'Enter') exec(); });
  }

  // Initial render
  render('/dashboard');
})();
"""

# -----------------------------------------------------------------------------
# 4. BUILD FUNCTIONS
# -----------------------------------------------------------------------------
def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "33-dars: SPA Asoslari va Client-Side Routing"
    title_ru = "Урок 33: Основы SPA и Клиентский Роутинг в JavaScript"
    title_en = "Lesson 33: SPA Architecture & Client-Side Routing"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="9-КЛАСС" data-en="GRADE 9">9-SINF</span>',
                 tpl)

    titles_json = json.dumps({"uz": title_uz, "ru": title_ru, "en": title_en}, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\n\};\n\nfunction updateSlide',
                 f'var NOTES = {notes_json};\n\nfunction updateSlide', tpl)

    stage_regex = r'<div class="stage">[\s\S]*?</div><!-- /stage -->'
    new_stage = f'<div class="stage">\n{SLIDES_HTML}\n  </div><!-- /stage -->'
    tpl = re.sub(stage_regex, lambda _: new_stage, tpl)

    custom_script = f"<script>\n{SIMULATOR_JS}\n</script>\n<script src=\"../../../../assets/i18n-inspector.js\" defer></script>\n</body>"
    tpl = tpl.replace("</body>", custom_script)

    out_path = os.path.join(DEST_DIR, "prezentatsiya.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")


def build_worksheet():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    sec1_html = """
    <p style="font-size:12px; margin-bottom:8px;" data-ru="Традиционные сайты (MPA) перезагружают весь HTML-документ при каждом клике, разрывая соединения WebSocket и WebRTC. Архитектура SPA (Single Page Application) загружает один каркас index.html, а дальнейшая смена экранов выполняется на клиенте за 0.1 мс." data-en="Traditional multi-page sites (MPA) reload the full HTML page on every navigation, severing real-time WebSocket and WebRTC connections. SPA architecture loads a single index.html shell, swapping views entirely client-side in under 0.1ms.">An'anaviy veb-saytlar (MPA) har bir havola bosilganda butun HTML hujjatni serverdan qayta yuklaydi va barcha WebSockets/WebRTC ulanishlarini uzib yuboradi. SPA (Single Page Application) arxitekturasi esa bitta bosh sahifani (index.html) yuklab, qolgan barcha ko'rinishlarni mijoz brauzerining o'zida 0.1 ms da yangilaydi.</p>
    <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="4 Столпа Архитектуры SPA:" data-en="4 Pillars of SPA Architecture:">SPA Arxitekturasining 4 Asosiy Ustuni:</div>
      <div>1. <strong>History API (pushState):</strong> <span data-ru="Изменение URL без запроса нового документа с сервера" data-en="Mutating URL bar without requesting new HTML documents">Brauzerda URL manzilini sahifani qayta yuklamasdan o'zgartirish</span>.</div>
      <div>2. <strong>Link Interception:</strong> <span data-ru="Перехват click по a[data-link] через e.preventDefault()" data-en="Intercepting a[data-link] clicks via e.preventDefault()">e.preventDefault() bilan havolalarning yangilanishini to'xtatish</span>.</div>
      <div>3. <strong>popstate Handler:</strong> <span data-ru="Синхронизация видов при нажатии кнопок Назад/Вперед" data-en="Synchronizing UI when user clicks Back/Forward browser buttons">Brauzerning Orqaga/Oldinga tugmalari bosilganda sahifani tiklash</span>.</div>
      <div>4. <strong>Server Fallback (Rewrite):</strong> <span data-ru="Редирект всех путей на index.html для предотвращения 404 при F5" data-en="Rerouting all requests to index.html preventing 404 errors on F5">F5 bosilganda xato chiqmasligi uchun barcha yo'llarni index.html ga burish</span>.</div>
    </div>
    """

    sec2_html = """
    <div style="font-size:10px; background:var(--surface-2); border:1px solid var(--border); border-radius:6px; padding:8px; font-family:monospace; line-height:1.4;">
      <div style="color:var(--accent); font-weight:700; margin-bottom:4px;">// Vanilla JS SPA Router yadrosi:</div>
      <div>function navigateTo(url) {</div>
      <div>&nbsp;&nbsp;window.history.pushState(null, '', url);</div>
      <div>&nbsp;&nbsp;router();</div>
      <div>}</div>
      <div>document.addEventListener('click', e =&gt; {</div>
      <div>&nbsp;&nbsp;const a = e.target.closest('a[data-link]');</div>
      <div>&nbsp;&nbsp;if (a) { e.preventDefault(); navigateTo(a.href); }</div>
      <div>});</div>
      <div>window.addEventListener('popstate', router);</div>
    </div>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:10px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Компонент / Механизм" data-en="Component / Mechanism">Komponent / Mexanizm</th>
            <th style="padding:4px 6px;" data-ru="Назначение в SPA" data-en="Purpose in SPA">SPA Tizimidagi Vazifasi</th>
            <th style="padding:4px 6px;" data-ru="Поведение Браузера" data-en="Browser Behavior">Brauzer Xulqi</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="pushState(state, '', url)" data-en="pushState(state, '', url)"><code>pushState(state, '', url)</code></td>
            <td style="padding:4px 6px;" data-ru="Добавление записи в историю перехода" data-en="Add history stack record">Tarixga yangi manzil qo'shish</td>
            <td style="padding:4px 6px;" data-ru="Без перезагрузки" data-en="Zero Reload">Qayta yuklanmaydi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Проверено" data-en="[ &nbsp; ] Verified">[ &nbsp; ] Tekshirildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="e.preventDefault()" data-en="e.preventDefault()"><code>e.preventDefault()</code></td>
            <td style="padding:4px 6px;" data-ru="Отмена стандартного HTTP перехода" data-en="Block default HTTP request">Brauzerning standart GET so'rovini to'xtatish</td>
            <td style="padding:4px 6px;" data-ru="Остается на странице" data-en="Stays on page">Sahifada qoladi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Проверено" data-en="[ &nbsp; ] Verified">[ &nbsp; ] Tekshirildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="window.onpopstate" data-en="window.onpopstate"><code>window.onpopstate</code></td>
            <td style="padding:4px 6px;" data-ru="Событие нажатия кнопок Назад / Вперед" data-en="Browser Back / Forward trigger">Orqaga/Oldinga tugmasi bosilishini tutish</td>
            <td style="padding:4px 6px;" data-ru="Синхронизация вида" data-en="View Sync">Ko'rinishni yangilaydi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Проверено" data-en="[ &nbsp; ] Verified">[ &nbsp; ] Tekshirildi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="vercel.json rewrites" data-en="vercel.json rewrites"><code>vercel.json rewrites</code></td>
            <td style="padding:4px 6px;" data-ru="Перенаправление всех путей на /index.html" data-en="Rerouting all routes to /index.html">Barcha so'rovlarni index.html ga yo'naltirish</td>
            <td style="padding:4px 6px;" data-ru="Предотвращение 404" data-en="Prevents 404">404 chiqmaydi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Проверено" data-en="[ &nbsp; ] Verified">[ &nbsp; ] Tekshirildi</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    sec4_html = """
    <div style="font-size:11px; line-height:1.5;">
      <p style="margin:2px 0 4px; font-weight:700;" data-ru="Задание 1: Разбор pushState против location.href (4 балла)" data-en="Task 1: pushState vs location.href (4 Pts)">1-Vazifa: pushState va location.href Farqi (4 ball)</p>
      <p style="margin:2px 0 4px; font-size:8.5pt;" data-ru="Почему присваивание window.location.href='/about' вызывает перезагрузку, а window.history.pushState(null,'','/about') — нет?" data-en="Why does window.location.href='/about' trigger full page reload while pushState does not?">Nega window.location.href='/about' sahifani to'liq yangilab yuboradi, pushState esa manzilni o'zgartirib sahifani yangilamaydi?</p>
      <div style="border-bottom:1px dashed var(--border); height:20px; margin:3px 0;"></div>
      <div style="border-bottom:1px dashed var(--border); height:20px; margin:3px 0;"></div>

      <p style="margin:6px 0 4px; font-weight:700;" data-ru="Задание 2: Логика Обработки 404 и Маршрутизация (4 балла)" data-en="Task 2: 404 Fallback Routing (4 Pts)">2-Vazifa: 404 Marshrutlash Mantig'i (4 ball)</p>
      <p style="margin:2px 0 4px; font-size:8.5pt;" data-ru="Напишите строку в функции router(), которая безопасно выбирает компонент 404, если запрошенный путь отсутствует в объекте routes:" data-en="Write down the code line in router() that selects the 404 view if current path does not exist in routes object:">Agar joriy yo'l routes obyektida mavjud bo'lmasa, 404 komponentini tanlovchi router() qatorini yozing:</p>
      <div style="border-bottom:1px dashed var(--border); height:20px; margin:3px 0;"></div>

      <p style="margin:6px 0 4px; font-weight:700;" data-ru="Задание 3: AI Vibecoding Промпт для Анимации (2 балла)" data-en="Task 3: AI Vibecoding Transition Prompt (2 Pts)">3-Vazifa: AI ga Beriladigan Oltin Prompt (2 ball)</p>
      <p style="margin:2px 0 4px; font-size:8.5pt;" data-ru="Сформулируйте точный промпт для добавления в роутер плавной CSS анимации смены экранов (fade-in 0.2s):" data-en="Formulate the prompt to instruct AI to implement smooth view transition animations (fade-in 0.2s):">Sahifalar almashganda silliq fade-in (0.2s) animatsiyasini qo'shish uchun AI ga beriladigan promptni yozing:</p>
      <div style="border-bottom:1px dashed var(--border); height:20px; margin:3px 0;"></div>
    </div>
    """

    replacements = {
        "{{COHORT_LABEL_UZ}}": "9-sinf",
        "{{COHORT_LABEL_RU}}": "9 класс",
        "{{COHORT_LABEL_EN}}": "Grade 9",
        "{{LESSON_NUM}}": "33",
        "{{TITLE_UZ}}": "SPA Asoslari va Client-Side Routing",
        "{{TITLE_RU}}": "Основы SPA и Клиентский Роутинг",
        "{{TITLE_EN}}": "SPA Architecture & Client-Side Routing",
        "{{META_UZ}}": "9-sinf · 11-hafta · Vibecoding va Full-Stack DevOps",
        "{{META_RU}}": "9 класс · 11 неделя · Vibecoding и Full-Stack DevOps",
        "{{META_EN}}": "Grade 9 · Week 11 · Vibecoding & Full-Stack DevOps",
        "{{MISSION_UZ}}": "Toza JavaScript yordamida to'liq ishlaydigan SPA (Single Page Application) tizimini loyihalash: History API pushState, havolalarni qayta yuklashsiz tutib qolish va Cyber-OS boshqaruv panelini yaratish.",
        "{{MISSION_RU}}": "Построить полноценное одностраничное веб-приложение (SPA) на чистом JavaScript: клиентский роутер на History API, перехват кликов без перезагрузки страниц и панель Cyber-OS.",
        "{{MISSION_EN}}": "Architect a client-side Single Page Application (SPA) on Vanilla JS: History API routing, link interception with zero reloads, and the Cyber-OS dashboard.",
        "{{SEC1_TITLE_UZ}}": "SPA Arxitekturasining 4 Asosiy Ustuni",
        "{{SEC1_TITLE_RU}}": "4 Столпа Архитектуры SPA",
        "{{SEC1_TITLE_EN}}": "4 Pillars of SPA Architecture",
        "{{SEC1_CONTENT}}": sec1_html,
        "{{SEC2_TITLE_UZ}}": "Vanilla JS SPA Router Yadrosi va Sintaksisi",
        "{{SEC2_TITLE_RU}}": "Синтаксис Клиентского Роутера на Vanilla JS",
        "{{SEC2_TITLE_EN}}": "Vanilla JS Client-Side Router Syntax",
        "{{SEC2_CONTENT}}": sec2_html,
        "{{SEC3_TITLE_UZ}}": "Kiber-Laboratoriya: Cyber-OS SPA Marshrutlash Sinovi",
        "{{SEC3_TITLE_RU}}": "Кибер-Лаборатория: Тест Маршрутизации Cyber-OS SPA",
        "{{SEC3_TITLE_EN}}": "Cyber-Lab: Cyber-OS SPA Routing Evaluation",
        "{{SEC3_CONTENT}}": sec3_html,
        "{{SEC4_CONTENT}}": sec4_html,
    }
    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    tpl = tpl.replace("</body>", "<script src=\"../../../../assets/i18n-inspector.js\" defer></script>\n</body>")

    out_path = os.path.join(DEST_DIR, "varaqa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: varaqa.html")


def build_homework():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    tasks_html = """
    <!-- TASK 1 -->
    <div class="task-card">
      <div class="task-head">
        <span class="task-badge" data-ru="1-УРОВЕНЬ: БАЗА" data-en="TIER 1: BASE">1-BOSQICH: BAZA</span>
        <span class="task-score" data-ru="4 БАЛЛА" data-en="4 POINTS">4 BALL</span>
      </div>
      <h3 data-ru="Задание 1: Базовый Router и pushState" data-en="Task 1: Core Router Function">1-Topshiriq: Router va pushState</h3>
      <p data-ru="Напишите функцию navigateTo(url), которая обновляет адрес в строке браузера через pushState и вызывает router(), а также подпишитесь на событие popstate:" data-en="Write the navigateTo(url) function that pushes URL to history and triggers router(), plus register popstate listener:">URL manzilni pushState orqali o'zgartiruvchi va router() funksiyasini chaqiruvchi navigateTo kodini yozing hamda popstate hodisasiga obuna bo'ling:</p>
      <div class="code-box">
        <textarea id="ans1" class="answer-area" placeholder="Kodingizni bu yerga yozing..." data-placeholder-ru="Напишите ваш код здесь..." data-placeholder-en="Write your code here...">function navigateTo(url) {
  window.history.pushState(null, '', url);
  router();
}
window.addEventListener('popstate', router);</textarea>
      </div>
      <div class="btn-group">
        <button class="btn btn-outline" onclick="revealSolution(1)" data-ru="💡 Подсказка / Решение" data-en="💡 Hint / Solution">💡 Ko'rsatma / Yechim</button>
      </div>
      <div id="sol1" class="solution-box" hidden>
        <h4 data-ru="Эталонное решение:" data-en="Reference Solution:">Oltin Yechim:</h4>
        <pre><code>function navigateTo(url) {
  window.history.pushState(null, '', url);
  router();
}
window.addEventListener('popstate', router);</code></pre>
      </div>
    </div>

    <!-- TASK 2 -->
    <div class="task-card">
      <div class="task-head">
        <span class="task-badge" data-ru="2-УРОВЕНЬ: ПРОЕКТ" data-en="TIER 2: PROJECT">2-BOSQICH: AMALIY LOYIHA</span>
        <span class="task-score" data-ru="4 БАЛЛА" data-en="4 POINTS">4 BALL</span>
      </div>
      <h3 data-ru="Задание 2: Перехват Ссылок a[data-link]" data-en="Task 2: Link Interception">2-Topshiriq: Havolalarni Tutib Qolish</h3>
      <p data-ru="Реализуйте глобальный обработчик кликов для элементов a[data-link] с отменой перезагрузки через e.preventDefault():" data-en="Implement global click interceptor on a[data-link] with e.preventDefault():">a[data-link] atributiga ega havolalar bosilganda sahifa yangilanishini to'xtatuvchi delegat kodini yozing:</p>
      <div class="code-box">
        <textarea id="ans2" class="answer-area" placeholder="Kodingizni bu yerga yozing..." data-placeholder-ru="Напишите ваш код здесь..." data-placeholder-en="Write your code here...">document.addEventListener('click', (e) => {
  const link = e.target.closest('a[data-link]');
  if (link) {
    e.preventDefault();
    navigateTo(link.getAttribute('href'));
  }
});</textarea>
      </div>
      <div class="btn-group">
        <button class="btn btn-outline" onclick="revealSolution(2)" data-ru="💡 Подсказка / Решение" data-en="💡 Hint / Solution">💡 Ko'rsatma / Yechim</button>
      </div>
      <div id="sol2" class="solution-box" hidden>
        <h4 data-ru="Эталонное решение:" data-en="Reference Solution:">Oltin Yechim:</h4>
        <pre><code>document.addEventListener('click', (e) => {
  const link = e.target.closest('a[data-link]');
  if (link) {
    e.preventDefault();
    navigateTo(link.getAttribute('href'));
  }
});</code></pre>
      </div>
    </div>

    <!-- TASK 3 -->
    <div class="task-card">
      <div class="task-head">
        <span class="task-badge" data-ru="3-УРОВЕНЬ: ВЫЗОВ" data-en="TIER 3: CHALLENGE">3-BOSQICH: KIBER-CHAQIRUV</span>
        <span class="task-score" data-ru="2 БАЛЛА" data-en="2 POINTS">2 BALL</span>
      </div>
      <h3 data-ru="Задание 3: Vercel Rewrites Конфигурация" data-en="Task 3: Vercel Rewrites Rule">3-Topshiriq: Vercel Rewrites Konfiguratsiyasi</h3>
      <p data-ru="Напишите файл vercel.json, который перенаправляет все входящие запросы на /index.html, чтобы F5 не приводил к 404:" data-en="Write vercel.json configuration to route all paths to index.html preventing 404 errors on F5:">F5 bosilganda server 404 xatosini bermasligi uchun barcha so'rovlarni /index.html ga yo'naltiruvchi vercel.json faylini yozing:</p>
      <div class="code-box">
        <textarea id="ans3" class="answer-area" placeholder="Kodingizni bu yerga yozing..." data-placeholder-ru="Напишите ваш код здесь..." data-placeholder-en="Write your code here...">{\n  "rewrites": [\n    { "source": "/(.*)", "destination": "/index.html" }\n  ]\n}</textarea>
      </div>
      <div class="btn-group">
        <button class="btn btn-outline" onclick="revealSolution(3)" data-ru="💡 Подсказка / Решение" data-en="💡 Hint / Solution">💡 Ko'rsatma / Yechim</button>
      </div>
      <div id="sol3" class="solution-box" hidden>
        <h4 data-ru="Эталонное решение:" data-en="Reference Solution:">Oltin Yechim:</h4>
        <pre><code>{
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}</code></pre>
      </div>
    </div>
    """

    replacements = {
        "{{COHORT_LABEL_UZ}}": "9-sinf · Vibecoding",
        "{{HERO_TAG_UZ}}": "9-SINF · 11-HAFTA · 33-DARS",
        "{{TITLE_UZ}}": "SPA Asoslari va Client-Side Routing",
        "{{TITLE_RU}}": "Основы SPA и Клиентский Роутинг",
        "{{TITLE_EN}}": "SPA Architecture & Client-Side Routing",
        "{{HERO_DESC_UZ}}": "Ushbu mustaqil uy vazifasida siz toza JavaScript (Vanilla JS) yordamida History API bilan sahifani qayta yuklamasdan boshqarish va SPA arxitekturasini qurasiz.",
        "{{HERO_DESC_RU}}": "В этом домашнем задании вы построите полноценный клиентский роутер на History API без перезагрузок страниц на чистом JavaScript.",
        "{{HERO_DESC_EN}}": "In this homework assignment, you will build a clean Vanilla JS Single Page Application router using History API and link interception.",
        "{{RUBRIC_T1_UZ}}": "navigateTo(url) funksiyasi va pushState orqali manzilni yangilash.",
        "{{RUBRIC_T1_RU}}": "Функция navigateTo(url) и обновление URL через pushState.",
        "{{RUBRIC_T1_EN}}": "navigateTo(url) function and URL pushState updating.",
        "{{RUBRIC_T2_UZ}}": "a[data-link] bosilganda e.preventDefault() bilan tutish va router() chaqirish.",
        "{{RUBRIC_T2_RU}}": "Перехват кликов a[data-link] через e.preventDefault() и вызов router().",
        "{{RUBRIC_T2_EN}}": "Intercepting a[data-link] clicks via e.preventDefault() and calling router().",
        "{{RUBRIC_T3_UZ}}": "Vercel / Netlify rewrites konfiguratsiyasi bilan F5 xatosini tuzatish.",
        "{{RUBRIC_T3_RU}}": "Конфигурация rewrites в vercel.json для предотвращения 404 при F5.",
        "{{RUBRIC_T3_EN}}": "Configuring vercel.json rewrites rule to fix 404 error on F5 reload.",
        "{{TASKS_HTML}}": tasks_html,
        "{{LESSON_SLUG}}": "9-11-33-spa-client-side-routing"
    }
    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    tpl = tpl.replace("</body>", "<script src=\"../../../../assets/i18n-inspector.js\" defer></script>\n</body>")

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")


def build_teacher_reading():
    content = """# 9-sinf · 11-hafta · 33-dars: SPA va Client-Side Routing
## O'qituvchi Uchun Dars O'tish Qo'llanmasi (80 daqiqalik Juftlik Dars)

**O'qituvchi:** Ismoiljon Usmonov  
**Fan:** Vibecoding / Full-Stack & DevOps  
**Mavzu:** SPA (Single Page Application) Asoslari va Client-Side Routing  
**Dars turi:** Juftlik blok (Double Block — 80 daqiqa)

---

### 1. Darsning Asosiy Maqsadi va Metodikasi
O'quvchilar oldingi darslarda WebSockets va WebRTC orqali real-vaqt ma'lumotlarini almashishni o'rgandilar. Ammo klassik veb-saytlarda har safar havola bosilganda sahifa qayta yuklanadi va barcha socket/webrtc ulanishlari uzilib qoladi!
Bugungi darsda o'quvchilar:
1. Nega zamonaviy veb (Gmail, YouTube, Discord) **SPA** ga o'tganini;
2. **HTML5 History API** (`pushState`, `replaceState`, `popstate`) ichki ishlash mexanizmini;
3. `e.preventDefault()` orqali havolalarni tutib qolish va 0 ms da komponentlarni yangilashni;
4. F5 bosilganda serverdagi 404 xatosini bartaraf qilish (Vercel rewrites) amaliyotini o'zlashtiradilar.

---

### 2. 80 Daqiqalik Dars Pacing Xaritasi

| Bosqich | Vaqt | Faoliyat Mazmuni |
|:---:|:---:|---|
| **1-Bosqich** | 00:00–04:00 | **Titul va Darsga Kirish:** Nega sahifalar qayta yuklanmasligi kerakligi va SPA inqilobi. |
| **2-Bosqich** | 04:00–12:00 | **Uy Vazifasi Tahlili:** 32-darsdagi video treklarni to'xtatmaslik (camera LED leak) xatosi tahlili va blitz savol. |
| **3-Bosqich** | 12:00–20:00 | **MPA vs SPA Arxitekturasi:** FOUC (oq ekran) muammosi va tarmoq trafigini tejash. |
| **4-Bosqich** | 20:00–28:00 | **HTML5 History API:** pushState, replaceState va popstate hodisalarini jonli konsolda ko'rsatish. |
| **5-Bosqich** | 28:00–36:00 | **Hash vs Path Routing:** Nega zamonaviy veb toza Path (/about) marshrutlashni tanlaydi? |
| **6-Bosqich** | 36:00–44:00 | **Link Interception:** e.preventDefault() bilan a[data-link] havolalarni markaziy tutib qolish. |
| **7-Bosqich** | 44:00–50:00 | **Routes Map va View Rendiring:** Marshrutlar xaritasi va aktiv menyu indikatori. |
| **8-Bosqich** | 50:00–60:00 | **Jonli Test-Drayv:** Taqdimot ichidagi Cyber-OS SPA panelini ishlatib ko'rish. |
| **9-Bosqich** | 60:00–66:00 | **Dinamik Parametrlar va 404:** Regex bilan /user/:id ni ajratish va NotFoundView. |
| **10-Bosqich** | 66:00–70:00 | **F5 Tuzog'i va Server Fallback:** vercel.json rewrites va Nginx try_files siri. |
| **11-Bosqich** | 70:00–74:00 | **Vibecoding Prompt Arxitekturasi:** AI ga 4 bosqichli buyruqlar berish yo'riqnomasi. |
| **12-Bosqich** | 74:00–77:00 | **Juftlikda Kod Auditi:** Partadoshining routerni tekshirish (Back/Fwd va 404). |
| **13-Bosqich** | 77:00–79:00 | **Xulosa va Oltin Qoidalar:** SPA ning 4 ta oltin qoidasini mustahkamlash. |
| **14-Bosqich** | 79:00–80:00 | **3 Darajali Uy Vazifasi:** 10 ballik rubrika va topshiriq reglamenti. |

---

### 3. Keng Tarqalgan Xatolar (Pitfalls) va Oltin Yechimlar
* **Tuzoq 1: Tashqi havolalarning ham to'xtab qolishi:**
  * *Xato:* `document.addEventListener('click', ...)` barcha `<a>` teglarini to'xtatadi.
  * *Yechim:* Faqat ichki havolalarga `data-link` atributini qo'ying: `e.target.closest('a[data-link]')`.
* **Tuzoq 2: Orqaga qaytganda sahifa yangilanmasligi:**
  * *Xato:* `popstate` tinglovchisini qo'shish unutiladi, natijada brauzer tugmasi bosilsa ham eski sahifa qolaveradi.
  * *Yechim:* `window.addEventListener('popstate', router)` albatta yozilishi shart!
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Created: TEACHER_READING.md")


def build_standalone_studio():
    template = """<!DOCTYPE html>
<html lang="uz" data-theme="dark" data-lang="uz">
<head>
  <meta charset="UTF-8">
  <title data-ru="Кибер-ОС: Студия SPA Архитектуры" data-en="Cyber-OS: SPA Architecture Studio">Cyber-OS: SPA Arxitektura Studiyasi</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #070a0f;
      color: #e2e8f0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }
    header {
      background: #0f1623;
      border-bottom: 1px solid #1e293b;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }
    .brand {
      font-weight: 800;
      font-size: 15px;
      color: #00f2fe;
      letter-spacing: 1px;
    }
    .url-chip {
      background: #070a0f;
      border: 1px solid #1e293b;
      padding: 6px 14px;
      border-radius: 6px;
      font-family: monospace;
      font-size: 12px;
      color: #38bdf8;
    }
    .layout {
      display: flex;
      flex: 1;
    }
    aside {
      width: 240px;
      background: #0b1019;
      border-right: 1px solid #1e293b;
      padding: 20px 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .nav-link {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 14px;
      color: #94a3b8;
      text-decoration: none;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      transition: all 0.2s;
    }
    .nav-link:hover {
      background: rgba(0, 242, 254, 0.08);
      color: #00f2fe;
    }
    .nav-link.active {
      background: rgba(0, 242, 254, 0.15);
      color: #00f2fe;
      border-left: 3px solid #00f2fe;
    }
    .lg {
      background: #131d2e;
      border: 1px solid #1f2f47;
      color: #94a3b8;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
    }
    .lg.active {
      background: #00f2fe;
      color: #070a0f;
      border-color: #00f2fe;
    }
    main {
      flex: 1;
      padding: 28px;
      overflow-y: auto;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>
  <header>
    <div class="brand"><span data-ru="⚡ КИБЕР-ОС SPA" data-en="⚡ CYBER-OS SPA">⚡ CYBER-OS SPA</span></div>
    <div class="url-chip" id="spaUrlBar">https://target-os.local/dashboard</div>
    <div style="font-size:12px; color:#22c55e; font-weight:700;"><span data-ru="● РЕЖИМ БЕЗ ПЕРЕЗАГРУЗКИ" data-en="● ZERO RELOAD ACTIVE">● ZERO RELOAD ACTIVE</span></div>
    <div style="display:flex; gap:6px;">
      <button class="lg active" data-l="uz" onclick="setLang('uz')">UZ</button>
      <button class="lg" data-l="ru" onclick="setLang('ru')">RU</button>
      <button class="lg" data-l="en" onclick="setLang('en')">EN</button>
    </div>
  </header>

  <div class="layout">
    <aside>
      <div style="font-size:11px; font-weight:700; color:#475569; padding:0 12px; margin-bottom:8px;"><span data-ru="ОСНОВНЫЕ РАЗДЕЛЫ" data-en="MAIN SECTIONS">ASOSIY BO'LIMLAR</span></div>
      <a href="/dashboard" class="nav-link active" data-path="/dashboard" data-link><span data-ru="📊 Главная панель" data-en="📊 Main Dashboard">📊 Asosiy Panel</span></a>
      <a href="/traffic" class="nav-link" data-path="/traffic" data-link><span data-ru="📈 Живой трафик" data-en="📈 Live Traffic">📈 Jonli Trafik</span></a>
      <a href="/terminal" class="nav-link" data-path="/terminal" data-link><span data-ru="⚡ Кибер-терминал" data-en="⚡ Cyber-Terminal">⚡ Kiber-Terminal</span></a>
      <a href="/settings" class="nav-link" data-path="/settings" data-link><span data-ru="⚙️ Настройки" data-en="⚙️ Settings">⚙️ Sozlamalar</span></a>
    </aside>

    <main id="spaAppContainer">
      <!-- Dynamic View Injected Here -->
    </main>
  </div>

  <script>
    function setLang(lang) {
      document.documentElement.setAttribute('data-lang', lang);
      try { localStorage.setItem('vc-lang', lang); } catch (e) {}
      document.querySelectorAll('.lg').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-l') === lang);
      });
      document.querySelectorAll('[data-ru][data-en]').forEach(el => {
        const val = lang === 'uz' ? (el.dataset.uzOriginal || el.innerHTML) : el.getAttribute('data-' + lang);
        if (!el.dataset.uzOriginal && lang !== 'uz') el.dataset.uzOriginal = el.innerHTML;
        if (val) el.innerHTML = val;
      });
      if (typeof window.__renderSpa === 'function' && window.__currentSpaPath) {
        window.__renderSpa(window.__currentSpaPath);
      }
    }

    __SIMULATOR_JS__

    // Handle browser popstate
    window.addEventListener('popstate', () => {
      const p = window.location.pathname.startsWith('/traffic') || window.location.pathname.startsWith('/terminal') || window.location.pathname.startsWith('/settings') ? window.location.pathname : '/dashboard';
      if (typeof window.__renderSpa === 'function') window.__renderSpa(p);
    });
  </script>
  <script src="../../../../../assets/i18n-inspector.js" defer></script>
</body>
</html>"""
    html = template.replace("__SIMULATOR_JS__", SIMULATOR_JS)
    out_path = os.path.join(DEST_DIR, "studio", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: studio/index.html")


def main():
    print("🚀 Building 9th Grade Week 11 Lesson 33: SPA & Client-Side Routing...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_standalone_studio()
    print("✅ All SPA Lesson 33 files successfully compiled!")


if __name__ == "__main__":
    main()
