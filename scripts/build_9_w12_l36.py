#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_9_w12_l36.py — Builder for 9th Grade, Week 12, Lesson 36

Mavzu: Veb-Ilova Tezligi: Kesh, Assetlar va Lighthouse Auditi (Core Web Vitals & Performance Optimization)
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 9-sinf (Junior Vibecoders, Full-Stack & DevOps Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "9-sinf", "12-hafta", "36-dars-veb-ilova-tezligi-kesh-assetlar-va-lighthouse-auditi")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "studio"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides for 80-min Double Block)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide is-on" data-phase="Kirish|Введение|Intro" data-time="00:00–05:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="9-КЛАСС · 12-Я НЕДЕЛЯ · УРОК 36" data-en="GRADE 9 · WEEK 12 · LESSON 36">9-SINF · 12-HAFTA · 36-DARS</span></div>
    <h1 class="display" data-ru="Скорость Веб-Приложений: Кэш, Ассеты и Аудит Lighthouse" data-en="Web App Performance: Caching, Assets & Lighthouse Audit">Veb-Ilova Tezligi: Kesh, Assetlar va Lighthouse Auditi</h1>
    <p class="lede" data-ru="Как 4-мегабайтный PNG-баннер убивает стартап за 8 секунд: метрики Core Web Vitals (LCP, INP, CLS), сжатие WebP/AVIF и Brotli, а также настройка вечного кэша браузера." data-en="How a 4 MB PNG banner kills a startup in 8 seconds: Core Web Vitals (LCP, INP, CLS), WebP/AVIF & Brotli compression, and immutable browser caching headers.">4 MB lik PNG rasm qanday qilib startapni 8 soniyada o'ldiradi: Core Web Vitals (LCP, INP, CLS) metrikalari, WebP/AVIF va Brotli siqish, hamda brauzer keshini mukammal sozlash.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Критический Путь Рендеринга" data-en="Critical Rendering Path">Tezlik Muhandisligi</h3>
        <p data-ru="Почему 53% пользователей закрывают сайт при загрузке дольше 3 секунд, и как превратить оценку Lighthouse 42 в идеальные 100." data-en="Why 53% of users bounce after 3 seconds, and how to turn a failing Lighthouse score of 42 into a blazing 100.">Nega foydalanuvchilarning 53% i 3 soniyadan kech ochilgan saytdan chiqib ketadi va qanday qilib 42 ballik saytni 100 ballga chiqarish mumkin.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Lighthouse Speed Studio</div>
        <h3 data-ru="Симулятор Оптимизации" data-en="Optimization Simulator">99+ Ball Chellenji</h3>
        <p data-ru="Живая лаборатория оптимизации: конвертация картинок, фиксация разметки CLS=0, подключение Brotli и immutable-кэширования." data-en="Interactive optimization lab: image transcoding, fixing CLS=0 layout shifts, enabling Brotli compression, and immutable caching.">Jonli optimizatsiya studiyasi: rasmlarni siqish, CLS=0 qilib sakrashni yo'qotish, Brotli va Cache-Control sarlavhalarini yoqish.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Tahlil|Разбор|Review" data-time="05:00–13:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ · УРОК 35" data-en="HOMEWORK REVIEW · LESSON 35">UY VAZIFASI TAHLILI · 35-DARS</span></div>
    <h2 data-ru="Разбор 35-урока: Безопасность NPM и Защита Lockfile" data-en="Lesson 35 Review: NPM Security & Lockfile Protection">35-dars Tahlili: NPM Xavfsizligi va Lockfile Himoyasi</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Типичная Ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Игнорирование npm ci и слепая установка" data-en="Skipping npm ci & Blind Installs">npm install --force bilan xavfni yashirish</h3>
        <p data-ru="Некоторые студенты при ошибках зависимостей использовали --force или удаляли package-lock.json, открывая дверь для вредоносных minor-версий и скриптов postinstall." data-en="Some students bypassed dependency errors using --force or deleted package-lock.json, exposing production builds to hijacked minor versions and postinstall trojans.">Ayrim o'quvchilar xato chiqqanda --force ishlatishdi yoki package-lock.json ni o'chirishdi. Bu esa zararli postinstall skriptlari va troyan versiyalarga eshik ochadi.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#ef4444;">// XATO: Serverda lockfile ni e'tiborsiz qoldirish</span>
$ rm package-lock.json && npm install <span style="color:#ef4444;">--force</span>
<span style="color:#64748b;">// Xavf: ^1.2.0 orqali buzilgan 1.2.9 troyani kirib keladi!</span>
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--ok);" data-ru="Золотой Стандарт" data-en="Golden Standard">Oltin Yechim (Golden Standard)</div>
        <h3 data-ru="Детерминированный деплой через npm ci" data-en="Deterministic Deploys with npm ci">npm ci --ignore-scripts va Audit</h3>
        <p data-ru="Production-сервер обязан устанавливать ровно те хэши SHA-512, которые зафиксированы в lockfile, блокируя выполнение сторонних хуков." data-en="Production servers must install exact SHA-512 hashes pinned inside package-lock.json while blocking arbitrary install hooks.">Production server faqat package-lock.json ichidagi aniq SHA-512 xeshlarni o'rnatishi va tashqi skriptlarni bloklashi shart.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#10b981;">// TO'G'RI: Qat'iy va xavfsiz pipeline</span>
$ npm ci <span style="color:#10b981;">--ignore-scripts --omit=dev</span>
$ npm audit <span style="color:#10b981;">--audit-level=high</span>
        </div>
      </div>
    </div>
    <div class="grid-2" style="margin-top:14px;">
      <div class="card">
        <strong style="color:var(--accent);" data-ru="⚡ 30-секундный Блиц:" data-en="⚡ 30-Second Blitz:">⚡ 30 Soniyalik Blitz:</strong>
        <span data-ru="Что делает флаг --omit=dev при деплое на сервер?" data-en="What does the --omit=dev flag prevent during production deployment?">Production serverga deploy qilayotganda --omit=dev bayrog'i nimani o'rnatmaydi?</span>
      </div>
      <div class="card">
        <strong style="color:var(--ok);" data-ru="🌉 Мост к новой теме:" data-en="🌉 Bridge to Today's Topic:">🌉 Bugungi Mavzuga Ko'prik:</strong>
        <span data-ru="Ваше приложение теперь безопасно, но из-за 150 тяжелых библиотек и огромных картинок оно открывается 9 секунд. Клиенты уходят!" data-en="Your app is now secure, yet 150 heavy bundles and huge images make it load in 9 seconds. Users are leaving!">Ilovangiz endi xavfsiz, lekin 150 ta og'ir kutubxona va katta rasmlar tufayli u 9 soniyada ochiladi. Foydalanuvchilar qochmoqda!</span>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: CORE WEB VITALS -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="13:00–20:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="МЕТРИКИ GOOGLE · CORE WEB VITALS" data-en="GOOGLE METRICS · CORE WEB VITALS">GOOGLE STANDARTI · CORE WEB VITALS</span></div>
    <h2 data-ru="Три Столпа Скорости: LCP, INP и CLS" data-en="Three Pillars of Speed: LCP, INP & CLS">Sayt Tezligining 3 Ustuni: LCP, INP va CLS</h2>
    <p data-ru="Google оценивает любой сайт по трем строгим метрикам пользовательского опыта (UX). Если они в красной зоне — сайт падает в поиске." data-en="Google grades every website on three strict UX metrics. Failing them tanks both user retention and SEO search rankings.">Google har bir veb-ilovani 3 ta qat'iy metrika bo'yicha baholaydi. Agar ular qizil zonada bo'lsa, sayt qidiruvda pastga tushadi.</p>
    <div class="grid-3" style="margin-top:16px;">
      <div class="card" style="border-top:3px solid var(--accent);">
        <div class="tag">LCP · &le; 2.5s</div>
        <h3 data-ru="Largest Contentful Paint" data-en="Largest Contentful Paint">Eng Katta Kontent Yuklanishi</h3>
        <p data-ru="Время до появления самого крупного видимого элемента (главного баннера или заголовка H1) на экране." data-en="Time until the largest visible element (hero image or main H1 banner) finishes rendering on screen.">Ekrandagi eng yirik element (Hero rasm yoki asosiy sarlavha) to'liq ko'ringuncha ketadigan vaqt.</p>
        <div style="margin-top:8px; font-size:12px; color:var(--ok);" data-ru="Норма: &lt; 2.5 сек | Плохо: &gt; 4.0 сек" data-en="Good: &lt; 2.5s | Poor: &gt; 4.0s">Yaxshi: &lt; 2.5s | Yomon: &gt; 4.0s</div>
      </div>
      <div class="card" style="border-top:3px solid var(--ok);">
        <div class="tag">INP · &le; 200ms</div>
        <h3 data-ru="Interaction to Next Paint" data-en="Interaction to Next Paint">Klickga Javob Tezligi</h3>
        <p data-ru="Задержка между кликом пользователя по кнопке и визуальной реакцией браузера. Тяжелый JS блокирует поток!" data-en="Delay between a user click/tap and the next visual frame. Heavy JS freezes the main thread!">Foydalanuvchi tugmani bosganidan ekranda javob chiqquncha o'tadigan vaqt. Og'ir JS ekranni qotiradi!</p>
        <div style="margin-top:8px; font-size:12px; color:var(--ok);" data-ru="Норма: &lt; 200 мс | Плохо: &gt; 500 мс" data-en="Good: &lt; 200ms | Poor: &gt; 500ms">Yaxshi: &lt; 200ms | Yomon: &gt; 500ms</div>
      </div>
      <div class="card" style="border-top:3px solid #f59e0b;">
        <div class="tag">CLS · &le; 0.1</div>
        <h3 data-ru="Cumulative Layout Shift" data-en="Cumulative Layout Shift">Maketning Sakrashi (CLS)</h3>
        <p data-ru="Эффект «прыгающей кнопки»: когда картинка прогружается позже текста и сдвигает экран прямо перед кликом." data-en="The 'jumping button' bug: when an image loads late without dimensions and pushes text down under your finger.">«Sakrash effekti»: rasm kech yuklanib, foydalanuvchi bosmoqchi bo'lgan tugmani pastga surib yuborishi.</p>
        <div style="margin-top:8px; font-size:12px; color:var(--ok);" data-ru="Норма: &lt; 0.1 | Идеал: 0.00" data-en="Good: &lt; 0.1 | Ideal: 0.00">Yaxshi: &lt; 0.1 | Ideal: 0.00</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: ASSET & IMAGE OPTIMIZATION -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="20:00–26:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="ОПТИМИЗАЦИЯ АССЕТОВ · ИЗОБРАЖЕНИЯ" data-en="ASSET OPTIMIZATION · IMAGES">ASSETLAR OPTIMIZATSIYASI · RASMLAR</span></div>
    <h2 data-ru="PNG (4 МБ) vs WebP/AVIF (120 КБ) и Защита от CLS" data-en="PNG (4 MB) vs WebP/AVIF (120 KB) & CLS Prevention">PNG (4 MB) vs WebP/AVIF (120 KB) va CLS Himoyasi</h2>
    <div class="grid-2" style="margin-top:14px;">
      <div class="card">
        <div class="tag" data-ru="Форматы Нового Поколения" data-en="Next-Gen Formats">Zamonaviy Formatlar</div>
        <ul class="clean">
          <li><span class="t" data-ru="<b>JPEG / PNG (Устарели для Web):</b> Фото с телефона весит 4.2 МБ. На мобильном 3G оно грузится 11 секунд." data-en="<b>JPEG / PNG (Legacy):</b> Raw photos weigh 4.2 MB, taking 11 seconds on mobile 3G."><b>JPEG / PNG (Eski):</b> Telefon kamerasidagi rasm 4.2 MB bo'ladi. Mobil 3G tarmoqda 11 soniyada ochiladi.</span></li>
          <li><span class="t" data-ru="<b>WebP (Google):</b> На 30–75% легче при том же визуальном качестве. Поддерживается 98% браузеров." data-en="<b>WebP (Google):</b> 30–75% smaller with identical visual quality. Supported by 98% of browsers."><b>WebP (Google):</b> Xuddi o'sha sifatni saqlagan holda 30–75% yengilroq. Barcha brauzerlar qo'llab-quvvatlaydi.</span></li>
          <li><span class="t" data-ru="<b>AVIF:</b> Ультра-сжатие до 90% экономии трафика (4.2 МБ ➔ 110 КБ)." data-en="<b>AVIF:</b> Ultra-compression saving up to 90% bandwidth (4.2 MB ➔ 110 KB)."><b>AVIF:</b> Eng kuchli siqish — trafikni 90% gacha tejaydi (4.2 MB ➔ 110 KB).</span></li>
          <li><span class="t" data-ru="<b>loading='lazy':</b> Загружает нижние картинки только когда пользователь до них доскроллит." data-en="<b>loading='lazy':</b> Defers offscreen images until the user actually scrolls down to them."><b>loading='lazy':</b> Sahifa pastidagi rasmlarni faqat foydalanuvchi skroll qilganda yuklaydi.</span></li>
        </ul>
      </div>
      <div class="card">
        <div class="tag" data-ru="Код Против Скачков (CLS = 0)" data-en="Anti-Shift Code (CLS = 0)">Sakrashga Qarshi Kod (CLS = 0)</div>
        <p data-ru="Всегда задавайте width и height на теге img! Браузер заранее зарезервирует пустое место." data-en="Always specify width and height on img tags! The browser reserves exact layout space before downloading.">Har doim img tegiga width va height bering! Brauzer rasm yuklanishidan oldin joy ajratib qo'yadi.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#ef4444;">&lt;!-- ❌ XATO: CLS = 0.42 (Matn sakrab ketadi!) --&gt;</span>
&lt;img src="hero-4mb.png" /&gt;

<span style="color:#10b981;">&lt;!-- ✅ TO'G'RI: LCP tez va CLS = 0.00 --&gt;</span>
&lt;img src="hero.avif"
     <span style="color:#38bdf8;">width="1200" height="630"</span>
     <span style="color:#a78bfa;">loading="lazy" decoding="async"</span>
     alt="Target Startup Hero" /&gt;
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: RENDER-BLOCKING JS & CSS -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="26:00–31:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="КРИТИЧЕСКИЙ ПУТЬ · JAVASCRIPT" data-en="CRITICAL PATH · JAVASCRIPT">KRITIK YO'L · JAVASCRIPT YUKLANISHI</span></div>
    <h2 data-ru="Блокировка Рендеринга: async vs defer" data-en="Render-Blocking Scripts: async vs defer">Ekranni Qotiruvchi Skriptlar: async vs defer</h2>
    <p data-ru="Когда браузер встречает обычный тег &lt;script&gt; в &lt;head&gt;, он полностью останавливает отрисовку HTML, пока не скачает и не выполнит JS!" data-en="When the HTML parser hits a normal &lt;script&gt; tag in &lt;head&gt;, it halts page rendering completely until the script downloads and executes!">Brauzer &lt;head&gt; ichida oddiy &lt;script&gt; ko'rsa, HTML chizishni butunlay to'xtatib, oq ekranni ushlab turadi!</p>
    <div class="grid-3" style="margin-top:16px;">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);">1. Oddiy &lt;script&gt;</div>
        <h3 data-ru="Остановка Парсера" data-en="Parser Blocked">HTML To'xtaydi ❌</h3>
        <p data-ru="HTML ждет скачивания и выполнения JS. Пользователь видит белый экран (высокий LCP)." data-en="HTML pauses for network download + execution. Users stare at a blank white screen.">HTML kutib turadi. Foydalanuvchi 3–5 soniya bo'm-bo'sh oq ekranga qarab o'tiradi.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(245,158,11,0.15); color:#f59e0b;">2. &lt;script async&gt;</div>
        <h3 data-ru="Параллельно (Хаотично)" data-en="Parallel (Unordered)">Parallel (Tartibsiz) ⚡</h3>
        <p data-ru="Скачивается в фоне, но запускается сразу после загрузки. Подходит только для счетчиков аналитики." data-en="Downloads in background, executes immediately when ready. Only safe for independent analytics.">Fonda yuklanadi, tayyor bo'lishi bilan ishga tushadi. Faqat mustaqil analitika skriptlari uchun.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--ok);">3. &lt;script defer&gt;</div>
        <h3 data-ru="Золотой Стандарт" data-en="Golden Standard">Oltin Standart ✅</h3>
        <p data-ru="Скачивается параллельно, но запускается строго ПОСЛЕ полной отрисовки HTML и в правильном порядке." data-en="Downloads in parallel, executes strictly AFTER HTML parsing completes, preserving script order.">Fonda yuklanadi va faqat HTML to'liq chizib bo'lingandan keyin tartib bilan ishga tushadi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: COMPRESSION (GZIP VS BROTLI) -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="31:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="СЕТЕВОЕ СЖАТИЕ · HTTP" data-en="NETWORK COMPRESSION · HTTP">TARMOQDA SIQISH · GZIP VA BROTLI</span></div>
    <h2 data-ru="Сжатие Трафика на Лету: Gzip vs Brotli" data-en="On-the-Fly Compression: Gzip vs Brotli">Trafikni Yo'lda Siqish: Gzip vs Brotli</h2>
    <div class="grid-2" style="margin-top:14px;">
      <div class="card">
        <h3 data-ru="Зачем сжимать HTML, CSS и JS?" data-en="Why Compress Text Payloads?">Nega matnli fayllarni siqamiz?</h3>
        <p data-ru="Текстовый код (HTML, CSS, JS, JSON) содержит тысячи повторяющихся слов. Сервер сжимает файл перед отправкой по сети, а браузер мгновенно распаковывает его." data-en="Code contains thousands of repeated tokens. The server compresses assets over the wire and browsers unpack them in milliseconds.">Kodlarda minglab takrorlanuvchi so'zlar bor. Server faylni zip qilib jo'natadi, brauzer esa millisekundda ochib oladi.</p>
        <ul class="clean" style="margin-top:10px;">
          <li><span class="t" data-ru="<b>Gzip (1992):</b> Стандарт, сжимает 1 МБ JS до ~300 КБ (70% экономии)." data-en="<b>Gzip (1992):</b> Classic standard compressing 1 MB JS down to ~300 KB (70% saved)."><b>Gzip:</b> Klassik standart, 1 MB JS kodni ~300 KB gacha siqadi (70% tejash).</span></li>
          <li><span class="t" data-ru="<b>Brotli — br (Google):</b> Современный алгоритм на 15–25% эффективнее Gzip (1 МБ ➔ ~210 КБ)." data-en="<b>Brotli — br (Google):</b> Modern standard 15–25% tighter than Gzip (1 MB ➔ ~210 KB)."><b>Brotli (br):</b> Google algoritmi, Gzip dan 20% kuchliroq (1 MB ➔ ~210 KB).</span></li>
        </ul>
      </div>
      <div class="card">
        <div class="tag" data-ru="HTTP Заголовки в DevTools" data-en="DevTools HTTP Headers">DevTools dagi HTTP Sarlavhalar</div>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#64748b;">// Brauzer so'rovi (Request):</span>
Accept-Encoding: gzip, deflate, <span style="color:#10b981;">br, zstd</span>

<span style="color:#64748b;">// Server javobi (Response):</span>
Content-Encoding: <span style="color:#10b981;">br</span>
Content-Length: 21400 <span style="color:#64748b;">// (Asl hajmi 105 KB edi!)</span>
        </div>
        <p style="margin-top:10px; font-size:13px;" data-ru="Vercel, Cloudflare и Nginx включают Brotli автоматически для HTTPS." data-en="Vercel, Cloudflare, and modern Nginx enable Brotli automatically over HTTPS.">Vercel, Cloudflare va zamonaviy Nginx serverlari HTTPS da Brotli ni avtomatik yoqadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: BROWSER CACHING & CONTENT HASHING -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="КЭШИРОВАНИЕ · CACHE-CONTROL" data-en="BROWSER CACHING · CACHE-CONTROL">BRAUZER KESHI · CACHE-CONTROL</span></div>
    <h2 data-ru="Самый Быстрый Запрос — Тот, Которого Не Было" data-en="The Fastest Request is the One Never Made">Eng Tez So'rov — Umuman Yuborilmagan So'rov</h2>
    <div class="grid-2" style="margin-top:14px;">
      <div class="card">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--ok);" data-ru="Вечный Кэш + Хэш Имени" data-en="Immutable Cache + Content Hash">Abadiy Kesh + Content Hashing</div>
        <p data-ru="Если файл стилей или JS не меняется, браузер не должен качать его заново при каждом визите. Мы добавляем хэш в имя файла (app.a8f3e.js) и ставим кэш на 1 год!" data-en="If CSS/JS hasn't changed, browsers shouldn't re-download it. We embed a hash in the filename (app.a8f3e.js) and cache it for 1 full year!">Agar CSS/JS o'zgarmasa, brauzer uni har safar yuklamasligi kerak. Fayl nomiga xesh qo'shib (app.a8f3e.js), keshni 1 yilga qulflaymiz!</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#64748b;">// Statik assetlar (app.a8f3e.js, logo.webp):</span>
Cache-Control: <span style="color:#10b981;">public, max-age=31536000, immutable</span>

<span style="color:#64748b;">// Asosiy index.html (doim yangilanishi shart!):</span>
Cache-Control: <span style="color:#f59e0b;">no-cache</span> <span style="color:#64748b;">// ETag orqali tekshiriladi</span>
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Опасная Ловушка" data-en="Cache Trap">Xavfli Kesh Tuzog'i</div>
        <h3 data-ru="Никогда не ставьте max-age=1 год на index.html!" data-en="Never Cache index.html for 1 Year!">Hech qachon index.html ni 1 yilga keshlamang!</h3>
        <p data-ru="Если закэшировать index.html на год, пользователи месяцами будут видеть старую версию вашего сайта, даже после деплоя багфиксов!" data-en="If index.html is cached for a year, returning users will see your broken old app for months even after you deploy fixes!">Agar index.html 1 yilga keshlansa, yangi kod deploy qilsangiz ham foydalanuvchilar eski buzilgan saytni ko'raveradi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: INTERACTIVE QUIZ -->
  <section class="slide" data-phase="Quiz|Квиз|Quiz" data-time="40:00–45:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ИНТЕРАКТИВНЫЙ ТЕСТ · ПРОВЕРКА" data-en="INTERACTIVE QUIZ · CHECK">INTERAKTIV QUIZ · BILIMNI TEKSHIRISH</span></div>
    <h2 data-ru="Блиц-Аудит Производительности" data-en="Performance Blitz Audit">Tezlik Auditi Boyicha 4 ta Savol</h2>
    <div class="quiz-box" style="margin-top:14px;">
      <div class="quiz-q" data-q="0">
        <p><strong data-ru="1. Картинка без width/height сдвинула кнопку вниз прямо перед кликом. Какая метрика пострадала?" data-en="1. An image without width/height pushed a button down right before a click. Which metric failed?">1. width/height berilmagan rasm yuklanib tugmani pastga surib yubordi. Qaysi metrika buzildi?</strong></p>
        <div class="quiz-opts">
          <button class="q-opt" onclick="checkQuiz(0, 0, false)" data-ru="LCP" data-en="LCP">LCP</button>
          <button class="q-opt" onclick="checkQuiz(0, 1, true)" data-ru="CLS (Cumulative Layout Shift)" data-en="CLS (Cumulative Layout Shift)">CLS (Cumulative Layout Shift)</button>
          <button class="q-opt" onclick="checkQuiz(0, 2, false)" data-ru="Brotli" data-en="Brotli">Brotli</button>
        </div>
      </div>
      <div class="quiz-q" data-q="1" style="margin-top:10px;">
        <p><strong data-ru="2. Какой атрибут позволяет скачать JS параллельно и запустить его строго ПОСЛЕ парсинга HTML?" data-en="2. Which attribute downloads JS in parallel and executes strictly AFTER HTML parsing?">2. Qaysi atribut JS ni fonda yuklab, faqat HTML chizib bo'lingach tartib bilan ishlatadi?</strong></p>
        <div class="quiz-opts">
          <button class="q-opt" onclick="checkQuiz(1, 0, true)" data-ru="defer" data-en="defer">defer</button>
          <button class="q-opt" onclick="checkQuiz(1, 1, false)" data-ru="async" data-en="async">async</button>
          <button class="q-opt" onclick="checkQuiz(1, 2, false)" data-ru="blocking" data-en="blocking">blocking</button>
        </div>
      </div>
      <div class="quiz-q" data-q="2" style="margin-top:10px;">
        <p><strong data-ru="3. Какой заголовок сжатия на 20% эффективнее классического Gzip?" data-en="3. Which compression encoding is ~20% tighter than classic Gzip?">3. Qaysi tarmoq siqish algoritmi oddiy Gzip dan ~20% kuchliroq?</strong></p>
        <div class="quiz-opts">
          <button class="q-opt" onclick="checkQuiz(2, 0, false)" data-ru="ZIP-99" data-en="ZIP-99">ZIP-99</button>
          <button class="q-opt" onclick="checkQuiz(2, 1, true)" data-ru="Brotli (Content-Encoding: br)" data-en="Brotli (Content-Encoding: br)">Brotli (Content-Encoding: br)</button>
          <button class="q-opt" onclick="checkQuiz(2, 2, false)" data-ru="Base64" data-en="Base64">Base64</button>
        </div>
      </div>
      <div class="quiz-q" data-q="3" style="margin-top:10px;">
        <p><strong data-ru="4. Для какого файла категорически НЕЛЬЗЯ ставить Cache-Control: max-age=31536000, immutable?" data-en="4. Which file should NEVER get Cache-Control: max-age=31536000, immutable?">4. Qaysi faylga hech qachon 1 yillik immutable kesh qo'yib bo'lmaydi?</strong></p>
        <div class="quiz-opts">
          <button class="q-opt" onclick="checkQuiz(3, 0, false)" data-ru="app.a8f3e.js" data-en="app.a8f3e.js">app.a8f3e.js</button>
          <button class="q-opt" onclick="checkQuiz(3, 1, false)" data-ru="hero-banner.webp" data-en="hero-banner.webp">hero-banner.webp</button>
          <button class="q-opt" onclick="checkQuiz(3, 2, true)" data-ru="index.html" data-en="index.html">index.html</button>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: STAGE 1 REFLECTION & BREAK -->
  <section class="slide" data-phase="Tanaffus|Перерыв|Reflection" data-time="45:00–50:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ 1-ГО ЭТАПА · 40 МИНУТ" data-en="STAGE 1 RECAP · 40 MINS">1-BOSQICH XULOSASI · 40 DAQIQA</span></div>
    <h2 data-ru="Стартап-Челлендж: Готовы к Ремонту «Умирающего» Сайта?" data-en="Startup Challenge: Ready to Rescue a Dying Website?">Startap Drama: «O'layotgan» Saytni Qutqarishga Tayyormisiz?</h2>
    <div class="card" style="margin-top:14px;">
      <p style="font-size:16px;" data-ru="Представьте: завтра запуск стартапа, инвесторы открывают сайт с телефона, а он весит 5 МБ, прыгает при загрузке и набирает жалкие 42 балла в Google Lighthouse. Во 2-м этапе мы запустим Lighthouse Speed Studio и выведем показатели в 99–100 баллов!" data-en="Imagine: launch day tomorrow, investors open your startup site on 4G, and it weighs 5 MB, jumps around, and scores a miserable 42/100 in Google Lighthouse. In Stage 2, we launch Lighthouse Speed Studio to hit 99–100!">Tasavvur qiling: ertaga startap taqdimoti, investorlar saytni telefondan ochishsa, u 5 MB og'irlikda, sahifa sakrab ketyapti va Google Lighthouse da sharmandali 42 ball olyapti! 2-bosqichda Lighthouse Speed Studio ni ochib, uni 99–100 ballga chiqaramiz!</p>
      <div class="grid-3" style="margin-top:16px;">
        <div class="box"><strong data-ru="1. Ассеты" data-en="1. Assets">1. Assetlar</strong><br><span style="font-size:13px;" data-ru="PNG ➔ AVIF/WebP + lazy" data-en="PNG ➔ AVIF/WebP + lazy">PNG ➔ AVIF/WebP + lazy</span></div>
        <div class="box"><strong data-ru="2. Разметка" data-en="2. Layout">2. Maket</strong><br><span style="font-size:13px;" data-ru="width/height + defer JS" data-en="width/height + defer JS">width/height + defer JS</span></div>
        <div class="box"><strong data-ru="3. Сеть" data-en="3. Network">3. Tarmoq</strong><br><span style="font-size:13px;" data-ru="Brotli (br) + immutable" data-en="Brotli (br) + immutable">Brotli (br) + immutable</span></div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: STAGE 2 HANDS-ON ARENA (LIGHTHOUSE STUDIO) -->
  <section class="slide" data-phase="Amaliyot|Практика|Lab" data-time="50:00–65:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКАЯ АРЕНА · 2-Й ЭТАП" data-en="HANDS-ON ARENA · STAGE 2">AMALIY ARENA · 2-BOSQICH</span></div>
    <h2 data-ru="Лаборатория: Target Lighthouse & Core Web Vitals Studio" data-en="Lab: Target Lighthouse & Core Web Vitals Studio">Laboratoriya: Target Lighthouse & Core Web Vitals Studio</h2>
    <div class="grid-2" style="margin-top:14px;">
      <div class="card">
        <div class="tag" data-ru="Задание на 15 минут" data-en="15-Min Mission">15 Daqiqalik Missiya</div>
        <p data-ru="Откройте studio/index.html. Перед вами исходный сайт со скоростью 42/100 (LCP 6.4с, CLS 0.42). Ваша цель — пошагово включить 5 инженерных оптимизаций и проследить за графиком Waterfall." data-en="Open studio/index.html. You start with a failing 42/100 site (LCP 6.4s, CLS 0.42). Toggle all 5 engineering optimizations step-by-step and watch the Network Waterfall transform.">studio/index.html ni oching. Boshida sayt atigi 42/100 ball (LCP 6.4s, CLS 0.42) olmoqda. 5 ta muhandislik tuzatishini birma-bir yoqib, Network Waterfall qanday tezlashishini kuzating.</p>
        <div style="margin-top:14px;">
          <a href="studio/index.html" target="_blank" style="display:inline-block; padding:10px 18px; background:var(--accent); color:#fff; border-radius:8px; text-decoration:none; font-weight:700;" data-ru="⚡ Открыть Lighthouse Studio" data-en="⚡ Launch Lighthouse Studio">⚡ Lighthouse Studioni Ochish</a>
        </div>
      </div>
      <div class="card">
        <div class="tag" data-ru="Чек-лист Победы" data-en="Victory Checklist">G'alaba Chek-listi</div>
        <ul class="clean">
          <li><span class="t" data-ru="1. Конвертировать Hero PNG (3.2 МБ) в WebP/AVIF (140 КБ)." data-en="1. Transcode Hero PNG (3.2 MB) into WebP/AVIF (140 KB).">1. Hero PNG (3.2 MB) rasmni WebP/AVIF (140 KB) ga o'tkazish.</span></li>
          <li><span class="t" data-ru="2. Зафиксировать width/height ➔ CLS падает с 0.42 до 0.00." data-en="2. Lock width/height ➔ CLS drops from 0.42 to 0.00.">2. width/height ni qulflash ➔ CLS 0.42 dan 0.00 ga tushadi.</span></li>
          <li><span class="t" data-ru="3. Добавить defer для снятия блокировки рендера." data-en="3. Add defer to unblock the critical rendering path.">3. Kritik yo'lni ochish uchun JS ga defer qo'shish.</span></li>
          <li><span class="t" data-ru="4. Активировать сжатие Brotli и 1-летний Cache-Control." data-en="4. Enable Brotli compression and 1-year Cache-Control.">4. Brotli siqish va 1 yillik Cache-Control ni yoqish.</span></li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: DEVTOOLS REAL AUDIT -->
  <section class="slide" data-phase="Amaliyot|Практика|Lab" data-time="65:00–72:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ХРОМ DEVTOOLS · РЕАЛЬНЫЙ АУДИТ" data-en="CHROME DEVTOOLS · REAL AUDIT">CHROME DEVTOOLS · JONLI AUDIT</span></div>
    <h2 data-ru="Как Проверить Любой Сайт За 30 Секунд в Chrome" data-en="How to Audit Any Live Website in 30 Seconds">Istalgan Saytni Chrome da 30 Soniyada Tekshirish</h2>
    <div class="grid-2" style="margin-top:14px;">
      <div class="card">
        <div class="tag">F12 ➔ Lighthouse Tab</div>
        <p data-ru="Откройте DevTools (F12) ➔ Вкладка Lighthouse ➔ Выберите Mobile + Performance ➔ Analyze page load." data-en="Open DevTools (F12) ➔ Lighthouse tab ➔ Select Mobile + Performance ➔ Click Analyze page load.">DevTools (F12) ➔ Lighthouse bo'limi ➔ Mobile + Performance ni tanlab ➔ Analyze page load tugmasini bosing.</p>
        <p style="margin-top:8px; font-size:13px; color:var(--ink-2);" data-ru="Совет: всегда тестируйте в режиме Инкогнито, чтобы расширения Chrome не занижали оценку!" data-en="Pro Tip: Always run Lighthouse in Incognito mode so Chrome extensions don't skew the score!">Maslahat: har doim Incognito rejimida tekshiring, aks holda Chrome kengaytmalari ballni pasaytirib ko'rsatadi!</p>
      </div>
      <div class="card">
        <div class="tag">F12 ➔ Network Tab</div>
        <ul class="clean">
          <li><span class="t" data-ru="<b>Disable cache:</b> Галочка для теста первого холодного визита." data-en="<b>Disable cache:</b> Checkbox to simulate a cold first visit."><b>Disable cache:</b> Birinchi sovuq tashrifni tekshirish uchun belgilang.</span></li>
          <li><span class="t" data-ru="<b>Fast 3G / Slow 4G:</b> Троттлинг сети, чтобы увидеть сайт глазами мобильного юзера." data-en="<b>Slow 4G Throttling:</b> Simulates real mobile data speeds."><b>Slow 4G Throttling:</b> Mobil internet tezligida sayt qanday ochilishini ko'rsatadi.</span></li>
          <li><span class="t" data-ru="<b>(memory/disk cache):</b> При повторном F5 статические файлы грузятся за 0 мс!" data-en="<b>(disk cache):</b> On reload, cached assets load in 0 ms!"><b>(disk cache):</b> F5 bosilganda keshlangan fayllar 0 ms da ochiladi!</span></li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: PEER REVIEW & STUDENT DEMO -->
  <section class="slide" data-phase="Demo|Демо|Demo" data-time="72:00–77:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ПАРНАЯ ПРОВЕРКА И ДЕМО" data-en="PEER REVIEW & DEMO">JUFTLIKDA TEKSHIRUV VA DEMO</span></div>
    <h2 data-ru="Взаимный Аудит (Peer Review) и Демонстрация" data-en="Pair Peer-Review & Live Showcase">Juftlikda Peer-Review va O'quvchilar Demosi</h2>
    <div class="grid-2" style="margin-top:14px;">
      <div class="card">
        <div class="tag" data-ru="Проверка Соседом" data-en="Peer Review">Qo'shni Bilan Tekshiruv (4 min)</div>
        <ul class="clean">
          <li><span class="t" data-ru="1. В Lighthouse Studio достигнута оценка 98–100 баллов?" data-en="1. Did your partner reach 98–100 in Lighthouse Studio?">1. Partnyoringiz Lighthouse Studio da 98–100 ballga chiqdimi?</span></li>
          <li><span class="t" data-ru="2. Общий вес страницы снижен с 4.8 МБ до менее 400 КБ?" data-en="2. Did total page weight drop from 4.8 MB to under 400 KB?">2. Sahifa og'irligi 4.8 MB dan 400 KB gacha kamaydimi?</span></li>
          <li><span class="t" data-ru="3. CLS равен ровно 0.00 при загрузке?" data-en="3. Is CLS strictly 0.00 on load?">3. Yuklanishda CLS aniq 0.00 ga tengmi?</span></li>
        </ul>
      </div>
      <div class="card">
        <div class="tag" data-ru="Выход к Доске" data-en="Smartboard Showcase">Doskada Demo (3 min)</div>
        <p data-ru="2 ученика выходят к Smartboard и показывают реальный аудит школьного или любимого сайта в Chrome DevTools, называя главную причину тормозов." data-en="Two students step up to the Smartboard and run a live DevTools audit on a real website, diagnosing its #1 performance bottleneck.">2 nafar o'quvchi Smartboard ga chiqib, istalgan real saytni Chrome DevTools da tekshiradi va uning #1 sekinlashish sababini aytib beradi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: ENTERPRISE BEST PRACTICES -->
  <section class="slide" data-phase="Xulosa|Итоги|Wrap-up" data-time="77:00–79:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ЧЕК-ЛИСТ ИНЖЕНЕРА" data-en="ENGINEER CHECKLIST">MUHANDIS XULOSASI</span></div>
    <h2 data-ru="Золотые Правила Веб-Производительности" data-en="Golden Rules of Web Performance">Veb-Tezlikning Oltin Qoidalari</h2>
    <div class="grid-2" style="margin-top:14px;">
      <div class="card">
        <h3 data-ru="Что мы делаем ДО деплоя:" data-en="Pre-Deploy Checklist:">Deploy dan OLDIN nima qilamiz:</h3>
        <ul class="clean">
          <li><span class="t" data-ru="Конвертируем все PNG/JPG в WebP или AVIF." data-en="Convert all heavy PNG/JPG assets into WebP or AVIF.">Barcha og'ir PNG/JPG rasmlarni WebP/AVIF ga o'giramiz.</span></li>
          <li><span class="t" data-ru="Добавляем width, height и loading='lazy' для картинок." data-en="Set width, height, and loading='lazy' on images.">Rasmlarga width, height va loading='lazy' yozamiz.</span></li>
          <li><span class="t" data-ru="Ставим defer на все теги &lt;script&gt;." data-en="Add defer to all &lt;script&gt; tags.">Barcha &lt;script&gt; teglariga defer qo'yamiz.</span></li>
        </ul>
      </div>
      <div class="card">
        <h3 data-ru="Что настраиваем НА сервере:" data-en="Server / CDN Config:">Server / CDN da nima yoqamiz:</h3>
        <ul class="clean">
          <li><span class="t" data-ru="Включаем сжатие Brotli (br) и Gzip." data-en="Enable Brotli (br) & Gzip text compression.">Brotli (br) va Gzip siqishini yoqamiz.</span></li>
          <li><span class="t" data-ru="Файлы с хэшами: max-age=31536000, immutable." data-en="Hashed assets: max-age=31536000, immutable.">Xeshli fayllar: max-age=31536000, immutable.</span></li>
          <li><span class="t" data-ru="Для index.html строго: Cache-Control: no-cache." data-en="For index.html strictly: Cache-Control: no-cache.">index.html uchun qat'iy: Cache-Control: no-cache.</span></li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: HOMEWORK (3-TIERED) -->
  <section class="slide" data-phase="Vazifa|Задание|Homework" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ДОМАШНЕЕ ЗАДАНИЕ · 10 БАЛЛОВ" data-en="HOMEWORK · 10 POINTS">UY VAZIFASI · 10 BALLIK MEZON</span></div>
    <h2 data-ru="3-Уровневая Миссия в vazifa.html" data-en="3-Tiered Mission in vazifa.html">vazifa.html dagi 3 Darajali Vazifa</h2>
    <div class="grid-3" style="margin-top:16px;">
      <div class="card">
        <div class="tag">1-Daraja · 4 ball</div>
        <h3 data-ru="База: Ассеты и Defer" data-en="Base: Assets & Defer">Baza: Assetlar va Defer</h3>
        <p data-ru="Исправьте тег &lt;img&gt; (WebP, width/height, lazy) и добавьте defer к блокирующему скрипту." data-en="Fix the broken &lt;img&gt; tag (WebP, width/height, lazy) and add defer to a render-blocking script.">Buzilgan &lt;img&gt; tegini (WebP, width/height, lazy) tuzating va bloklovchi skriptga defer qo'shing.</p>
      </div>
      <div class="card">
        <div class="tag">2-Daraja · 4 ball</div>
        <h3 data-ru="Инженерия: HTTP Кэш" data-en="Engineering: HTTP Cache">Muhandislik: HTTP Kesh</h3>
        <p data-ru="Напишите правильные заголовки Cache-Control для app.8c21.js и index.html в Express.js." data-en="Configure proper Cache-Control headers for app.8c21.js vs index.html in Express.js.">Express.js da app.8c21.js va index.html uchun to'g'ri Cache-Control sarlavhalarini yozing.</p>
      </div>
      <div class="card">
        <div class="tag">3-Daraja · 2 ball</div>
        <h3 data-ru="Вызов: Lighthouse 98+" data-en="Challenge: Lighthouse 98+">Chaqiruv: Lighthouse 98+</h3>
        <p data-ru="Проведите реальный аудит любого своего проекта в Chrome Lighthouse и запишите метрики LCP, INP, CLS." data-en="Audit any personal web project in Chrome Lighthouse and log its LCP, INP, and CLS scores.">O'z loyihangizni Chrome Lighthouse da tekshiring va LCP, INP, CLS natijalarini yozib topshiring.</p>
      </div>
    </div>
  </section>
"""

NOTES_DATA = {
  "uz": [
    ["Kirish va Startap Drama", "Bugun 9-sinflar bilan sayt tezligi, Core Web Vitals va Google Lighthouse auditini o'rganamiz. 4 MB rasm startapni qanday o'ldirishini misol qilib bering.", "1-slaydni ko'rsating va o'quvchilardan eng sekin ochilgan sayt tajribasini so'rang."],
    ["Uy vazifasi tahlili", "35-dars (NPM Security) bo'yicha xatolar: --force ishlatish va lockfile ni o'chirish xavfli. Oltin standart: npm ci --ignore-scripts.", "30 soniyalik blitz savolni bering (--omit=dev nima qiladi?)."],
    ["Core Web Vitals (3 Ustun)", "LCP (<=2.5s), INP (<=200ms) va CLS (<=0.1) tushunchalarini hayotiy misollar (sakrab ketadigan tugma!) bilan tushuntiring.", "Doskada 3 ta metrika chegaralarini yozib qo'ying."],
    ["Rasmlar Optimizatsiyasi", "PNG/JPG vs WebP/AVIF hajm farqini (4.2 MB -> 110 KB) ko'rsating. width/height atributi CLS=0 qilishini tushuntiring.", "loading='lazy' qanday ishlashini chizib ko'rsating."],
    ["Render-Blocking JS", "Oddiy script, async va defer o'rtasidagi farqni tushuntiring. Har doim defer ishlatish oltin qoida.", "Doskada 3 ta vaqt chizig'ini (timeline) chizing."],
    ["Gzip va Brotli Siqish", "Server matnli fayllarni tarmoqda siqib yuboradi. Brotli (br) Gzip dan ~20% kuchliroq.", "DevTools Network tabidagi Content-Encoding sarlavhasini tushuntiring."],
    ["Brauzer Keshi va Hash", "Eng tez so'rov — yuborilmagan so'rov. app.a8f3e.js uchun immutable (1 yil), index.html uchun no-cache qo'yiladi.", "Nega index.html ni 1 yilga keshlash xavfli ekanini muhokama qiling."],
    ["Interaktiv Quiz", "4 ta tezkor savol orqali nazariyani mustahkamlang.", "To'g'ri javoblarni ochib, xatolarni izohlang."],
    ["1-Bosqich Refleksiya", "40 daqiqalik 1-bosqich yakuni. Endi amaliy Lighthouse Studio ga o'tamiz.", "2 daqiqalik ko'z dam olish va 2-bosqichga tayyorgarlik."],
    ["Lighthouse Studio Laboratoriyasi", "O'quvchilar studio/index.html ni ochib, 42 ballik saytni 100 ballga chiqarishadi.", "Sinfni aylanib, har bir o'quvchi Waterfall grafigini kuzatayotganini tekshiring."],
    ["Chrome DevTools Jonli Audit", "Haqiqiy brauzerda F12 -> Lighthouse (Incognito!) va Network throttling qanday ishlatilishini ko'rsating.", "O'quvchilar o'z sevimli saytlarini tekshirib ko'rishsin."],
    ["Juftlikda Peer Review va Demo", "Juftliklar bir-birining Studio natijasini tekshiradi. 2 o'quvchi Smartboardda real saytni audit qiladi.", "Eng aniq tahlil qilgan o'quvchilarni rag'batlantiring."],
    ["Oltin Qoidalar Xulosasi", "Deploy dan oldingi va serverdagi 6 ta qat'iy qoidani takrorlang.", "Savol-javob o'tkazing."],
    ["3-Darajali Uy Vazifasi", "vazifa.html da 10 ballik topshiriqlar tayyor (4+4+2).", "Muddat va baholash mezonini eslating."]
  ],
  "ru": [
    ["Введение и Стартап-Драма", "Сегодня изучаем скорость веб-приложений, Core Web Vitals и аудит Google Lighthouse. Объясните на примере 4 МБ PNG-баннера.", "Покажите 1-й слайд и обсудите опыт медленных сайтов."],
    ["Разбор ДЗ (Урок 35)", "Разбираем ошибки прошлого урока: --force и удаление lockfile опасны. Эталон: npm ci --ignore-scripts.", "Задайте 30-секундный блиц-вопрос про --omit=dev."],
    ["Core Web Vitals (3 Столпа)", "Объясните LCP (<=2.5с), INP (<=200мс) и CLS (<=0.1) на примере «прыгающей кнопки».", "Выпишите пороговые значения на доске."],
    ["Оптимизация Картинок", "Сравните PNG/JPG (4.2 МБ) и WebP/AVIF (110 КБ). Объясните роль width/height для CLS=0.", "Нарисуйте схему работы loading='lazy'."],
    ["Блокировка JS: async vs defer", "Разница между обычным script, async и defer. Золотое правило — использовать defer.", "Нарисуйте временную шкалу парсинга HTML."],
    ["Сжатие Gzip и Brotli", "Сервер сжимает текстовые файлы перед отправкой. Brotli (br) эффективнее Gzip на ~20%.", "Покажите заголовок Content-Encoding: br."],
    ["Кэширование и Хэши", "Лучший запрос — тот, которого не было. Для app.a8f3e.js ставим immutable на год, для index.html — no-cache.", "Обсудите ловушку кэширования index.html."],
    ["Интерактивный Квиз", "Закрепляем материал с помощью 4 вопросов.", "Разберите ответы с классом."],
    ["Итоги 1-го Этапа", "Завершение первой 40-минутки. Переход к практической лаборатории.", "Короткая пауза перед практикой."],
    ["Лаборатория Lighthouse Studio", "Ученики открывают studio/index.html и доводят оценку с 42 до 100 баллов.", "Помогайте ученикам анализировать Waterfall."],
    ["Аудит в Chrome DevTools", "Покажите F12 -> Lighthouse (в Инкогнито!) и троттлинг сети в Network.", "Предложите проверить реальный сайт."],
    ["Взаимопроверка и Демо", "Пары проверяют результаты друг друга. 2 ученика проводят живой аудит у доски.", "Отметьте лучшие разборы."],
    ["Чек-лист Инженера", "Повторите 6 золотых правил до и после деплоя.", "Ответьте на вопросы."],
    ["Домашнее задание", "3-уровневое задание на 10 баллов ждет в vazifa.html.", "Напомните критерии оценки."]
  ],
  "en": [
    ["Intro & Startup Drama", "Today we master web performance, Core Web Vitals, and Google Lighthouse audits. Explain how a 4 MB PNG kills retention.", "Display slide 1 and ask about slow website experiences."],
    ["Homework Review (Lesson 35)", "Reviewing Lesson 35: using --force or deleting lockfiles is risky. Enforce npm ci --ignore-scripts.", "Ask the 30-second blitz question on --omit=dev."],
    ["Core Web Vitals", "Explain LCP (<=2.5s), INP (<=200ms), and CLS (<=0.1) using the 'jumping button' example.", "Write threshold targets on the board."],
    ["Asset Optimization", "Compare PNG/JPG (4.2 MB) vs WebP/AVIF (110 KB). Show how width/height locks CLS=0.", "Sketch loading='lazy' behavior."],
    ["Render-Blocking JS", "Contrast normal script, async, and defer. Emphasize defer as the default standard.", "Diagram the HTML parser timeline."],
    ["Gzip vs Brotli Compression", "Servers compress text payloads over the wire. Brotli (br) beats Gzip by ~20%.", "Inspect Content-Encoding: br headers."],
    ["Browser Caching & Hashing", "Fastest request is one never made. Cache hashed assets immutably for 1 year, keep index.html no-cache.", "Discuss the stale index.html cache trap."],
    ["Interactive Quiz", "Reinforce theory with a 4-question blitz quiz.", "Reveal answers and clarify edge cases."],
    ["Stage 1 Reflection", "End of first 40-min block. Transition to Lighthouse Speed Studio.", "Brief breather before Stage 2 lab."],
    ["Lighthouse Studio Lab", "Students open studio/index.html and optimize the failing 42/100 site up to 100/100.", "Circulate and check Waterfall charts."],
    ["Chrome DevTools Live Audit", "Demonstrate F12 -> Lighthouse (Incognito!) and Slow 4G Network throttling.", "Have students audit a real site."],
    ["Peer Review & Demo", "Pairs verify each other's Studio metrics. 2 students showcase live audits on the Smartboard.", "Highlight sharp diagnostics."],
    ["Engineer Checklist", "Review the 6 pre-deploy and server-side performance rules.", "Field final questions."],
    ["3-Tiered Homework", "10-point homework is live in vazifa.html (4+4+2).", "Confirm submission expectations."]
  ]
}

def build_presentation():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Taqdimot shabloni — Target Maktabi</title>", "<title data-ru=\"9-класс: Скорость Веб-Приложений и Lighthouse\" data-en=\"Grade 9: Web Performance & Lighthouse Audit\">9-sinf: Veb-Ilova Tezligi va Lighthouse Auditi</title>")
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

    tpl = tpl.replace("<title>Amaliy Ish Varaqasi — Target Maktabi</title>", "<title data-ru=\"Рабочий лист: Скорость Веб-Приложений — 9-класс\" data-en=\"Worksheet: Web Performance & Lighthouse — Grade 9\">Ish Varaqasi: Veb-Ilova Tezligi va Lighthouse Auditi — 9-sinf</title>")
    tpl = tpl.replace("1-AMALIY ISH VARAQASI", "36-AMALIY ISH VARAQASI")
    tpl = tpl.replace("Mavzu: Kirish va Vibecoding asoslari", "Mavzu: Veb-Ilova Tezligi, Kesh, Assetlar va Lighthouse Auditi")

    worksheet_body = """
  <div class="mission-box">
    <div class="mission-title" data-ru="МИССИЯ УРОКА: СПАСЕНИЕ СТАРТАПА (LIGHTHOUSE 99+)" data-en="LESSON MISSION: STARTUP RESCUE (LIGHTHOUSE 99+)">DARSNING KIBER-MISSIYASI: STARTAPNI QUTQARISH (LIGHTHOUSE 99+)</div>
    <p style="font-size:12px; margin-top:4px;" data-ru="Освоить 3 метрики Core Web Vitals (LCP, INP, CLS), перевести тяжелые картинки в WebP/AVIF, убрать блокирующие скрипты через defer и настроить HTTP-кэширование." data-en="Master the 3 Core Web Vitals (LCP, INP, CLS), optimize heavy images to WebP/AVIF, eliminate render-blocking JS with defer, and configure HTTP caching.">Core Web Vitals ning 3 ta asosiy metrikasini (LCP, INP, CLS) o'zlashtirish, og'ir rasmlarni WebP/AVIF ga siqish, bloklovchi JS ni defer bilan tuzatish va HTTP keshni sozlash.</p>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">1</span>
      <h3 data-ru="Метрики Core Web Vitals: Пороги и Диагностика (3 балла)" data-en="Core Web Vitals: Thresholds & Diagnostics (3 pts)">Core Web Vitals: Chegaralar va Diagnostika (3 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Заполните таблицу стандартов Google (зеленая зона) и укажите главную причину сбоя:" data-en="Complete the Google Green Zone targets and identify the primary cause of failure:">Google yashil zona mezonlarini va buzilish sababini yozing:</p>
    <table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:11px;">
      <thead>
        <tr style="background:var(--card-bg, #f1f5f9);">
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Метрика" data-en="Metric">Metrika</th>
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Зеленая зона (Норма)" data-en="Green Zone Target">Yashil Zona (Mezon)</th>
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Что ее портит?" data-en="Root Cause of Failure">Uni nima buzadi?</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<strong>LCP</strong> (Largest Contentful Paint)" data-en="<strong>LCP</strong> (Largest Contentful Paint)"><strong>LCP</strong> (Largest Contentful Paint)</td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="&le; ________ сек" data-en="&le; ________ sec">&le; ________ sek</td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="4 МБ PNG / блокирующий JS" data-en="4 MB PNG / blocking JS">________________________________</td>
        </tr>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<strong>INP</strong> (Interaction to Next Paint)" data-en="<strong>INP</strong> (Interaction to Next Paint)"><strong>INP</strong> (Interaction to Next Paint)</td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="&le; ________ мс" data-en="&le; ________ ms">&le; ________ ms</td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="Тяжелый JS в главном потоке" data-en="Heavy main-thread JS">________________________________</td>
        </tr>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<strong>CLS</strong> (Cumulative Layout Shift)" data-en="<strong>CLS</strong> (Cumulative Layout Shift)"><strong>CLS</strong> (Cumulative Layout Shift)</td>
          <td style="border:1px solid #cbd5e1; padding:6px;">&le; ________</td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="Картинки без width и height" data-en="Images missing width/height">________________________________</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">2</span>
      <h3 data-ru="Охота на Баги: Исправь Медленный HTML (3 балла)" data-en="Bug Hunt: Fix Slow HTML (3 pts)">Kod Tahlili: Sekin HTML ni Tuzatish (3 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Найдите 3 грубые ошибки производительности в этом фрагменте и напишите исправленный вариант:" data-en="Find 3 critical performance bugs in this snippet and write the fixed version:">Quyidagi kodda 3 ta jiddiy tezlik xatosini toping va to'g'ri variantini yozing:</p>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:8px; margin-top:6px; font-family:monospace; font-size:11px;">
      &lt;head&gt;<br>
      &nbsp;&nbsp;&lt;script src="analytics-heavy.js"&gt;&lt;/script&gt;<br>
      &lt;/head&gt;<br>
      &lt;body&gt;<br>
      &nbsp;&nbsp;&lt;img src="banner-4mb.png" /&gt;<br>
      &lt;/body&gt;
    </div>
    <div style="margin-top:8px; font-size:12px; line-height:1.9;">
      1. JS tuzatishi: ________________________________________________________________<br>
      2. Rasm formati va o'lchami: _____________________________________________________
    </div>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">3</span>
      <h3 data-ru="Стратегия HTTP Кэширования (2 балла)" data-en="HTTP Caching Strategy (2 pts)">HTTP Kesh Strategiyasi (2 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Укажите правильный заголовок Cache-Control для каждого файла:" data-en="Specify the proper Cache-Control header for each file:">Har bir fayl uchun to'g'ri Cache-Control sarlavhasini yozing:</p>
    <div style="margin-top:6px; font-size:12px; line-height:1.9; font-family:monospace;">
      app.a8f3e.js ➔ Cache-Control: ________________________________________________<br>
      index.html   ➔ Cache-Control: ________________________________________________
    </div>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">4</span>
      <h3 data-ru="Критерии Оценки (10 баллов)" data-en="Evaluation Rubric (10 pts)">Baholash Mezoni (10 ball)</h3>
    </div>
    <ul style="font-size:11px; margin-top:6px; padding-left:18px;">
      <li data-ru="4 балла (База): Найдены ошибки LCP/CLS и добавлен defer + WebP." data-en="4 pts (Base): LCP/CLS bugs identified, defer + WebP applied.">4 ball (Baza): LCP/CLS xatolari topilgan, defer va WebP to'g'ri yozilgan.</li>
      <li data-ru="4 балла (Проект): В Lighthouse Studio достигнута оценка 98+ и настроен Brotli/Cache-Control." data-en="4 pts (Project): Reached 98+ in Lighthouse Studio with Brotli & Cache-Control.">4 ball (Amaliyot): Lighthouse Studio da 98+ ball olingan va Brotli/Cache-Control sozlangan.</li>
      <li data-ru="2 балла (Вызов): Проведен реальный аудит сайта в Chrome DevTools (Incognito)." data-en="2 pts (Challenge): Completed a real Chrome DevTools Lighthouse audit (Incognito).">2 ball (Chaqiruv): Chrome DevTools da real sayt auditi (Incognito) muvaffaqiyatli bajarilgan.</li>
    </ul>
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

    tpl = tpl.replace("<title>Uy Vazifasi — Target Maktabi</title>", "<title data-ru=\"Домашнее задание: Скорость Веб-Приложений — 9-класс\" data-en=\"Homework: Web Performance & Lighthouse — Grade 9\">Uy Vazifasi: Veb-Ilova Tezligi va Lighthouse — 9-sinf</title>")

    hw_content = """
    <div class="hw-header">
      <div class="eyebrow" data-ru="9-КЛАСС · УРОК 36 · ДОМАШНЕЕ ЗАДАНИЕ" data-en="GRADE 9 · LESSON 36 · HOMEWORK">9-SINF · 36-DARS · MUSTAQIL UY VAZIFASI</div>
      <h1 data-ru="Оптимизация Скорости и Аудит Lighthouse" data-en="Performance Optimization & Lighthouse Audit">Tezlikni Optimizatsiya Qilish va Lighthouse Auditi</h1>
      <p data-ru="Выполните 3 уровня миссии (максимум 10 баллов). Ваши ответы автоматически сохраняются в браузере." data-en="Complete the 3-tier mission (10 points total). Your progress saves automatically in LocalStorage.">3 darajali missiyani bajaring (jami 10 ball). Javoblaringiz brauzerda avtomatik saqlanadi.</p>
    </div>

    <div class="tier-card">
      <div class="tier-badge" data-ru="Уровень 1 · База (4 балла)" data-en="Tier 1 · Base (4 pts)">1-Daraja · Baza (4 ball)</div>
      <h3 data-ru="1. Исправьте блокирующий HTML и тяжелый баннер" data-en="1. Fix Render-Blocking Script & Heavy Banner">1. Bloklovchi HTML va og'ir rasmni tuzating</h3>
      <p data-ru="Перепишите этот код так, чтобы CLS стал 0.00, картинка грузилась в WebP лениво, а скрипт не блокировал экран:" data-en="Rewrite this snippet so CLS=0.00, image loads lazily in WebP, and the script doesn't block rendering:">Quyidagi kodni CLS=0.00 bo'ladigan, rasm WebP da lazy yuklanadigan va skript ekranni to'smaydigan qilib qayta yozing:</p>
      <pre class="code-sample">&lt;script src="app.js"&gt;&lt;/script&gt;
&lt;img src="photo.png" /&gt;</pre>
      <textarea id="hw_q1" class="hw-input" rows="4" placeholder="Yechimingizni shu yerga yozing..." data-placeholder-ru="Напишите ваше решение здесь..." data-placeholder-en="Write your solution here..."></textarea>
      <button class="btn-hint" onclick="toggleHint('hint1')" data-ru="Показать Эталон (Fix)" data-en="Show Solution (Fix)">Yechimni ko'rish (Fix)</button>
      <div id="hint1" class="hint-box" hidden>
        <code>&lt;script src="app.js" defer&gt;&lt;/script&gt;<br>&lt;img src="photo.webp" width="1200" height="630" loading="lazy" alt="Banner" /&gt;</code>
      </div>
    </div>

    <div class="tier-card">
      <div class="tier-badge" data-ru="Уровень 2 · Практическая Инженерия (4 балла)" data-en="Tier 2 · Engineering (4 pts)">2-Daraja · Amaliy Muhandislik (4 ball)</div>
      <h3 data-ru="2. Настройка Cache-Control в Express.js" data-en="2. Configure Cache-Control in Express.js">2. Express.js da Cache-Control sozlash</h3>
      <p data-ru="Какой заголовок Cache-Control вы установите для файла style.f91a2.css, а какой для index.html? Почему?" data-en="What Cache-Control header will you set for style.f91a2.css vs index.html? Explain why.">style.f91a2.css va index.html fayllari uchun qanday Cache-Control sarlavhasini o'rnatasiz va nega?</p>
      <textarea id="hw_q2" class="hw-input" rows="4" placeholder="Cache-Control javobini yozing..." data-placeholder-ru="Напишите заголовки Cache-Control..." data-placeholder-en="Write Cache-Control headers..."></textarea>
      <button class="btn-hint" onclick="toggleHint('hint2')" data-ru="Показать Эталон (Fix)" data-en="Show Solution (Fix)">Yechimni ko'rish (Fix)</button>
      <div id="hint2" class="hint-box" hidden>
        <span data-ru="style.f91a2.css: public, max-age=31536000, immutable (имя с хэшем). index.html: no-cache (всегда проверять свежую версию)." data-en="style.f91a2.css: public, max-age=31536000, immutable (hashed filename). index.html: no-cache (always revalidate fresh HTML).">style.f91a2.css: public, max-age=31536000, immutable (nomida xesh bor). index.html: no-cache (doim yangi HTML ni tekshirish shart).</span>
      </div>
    </div>

    <div class="tier-card">
      <div class="tier-badge" data-ru="Уровень 3 · Кибер-Вызов (2 балла)" data-en="Tier 3 · Challenge (2 pts)">3-Daraja · Kiber-Chaqiruv (2 ball)</div>
      <h3 data-ru="3. Реальный Lighthouse Аудит" data-en="3. Live Lighthouse Audit">3. Real Lighthouse Auditi</h3>
      <p data-ru="Откройте любой свой прошлый сайт (или target.uz) в режиме Инкогнито, запустите F12 -> Lighthouse (Mobile) и запишите: Performance Ball, LCP и CLS." data-en="Open any previous project (or target.uz) in Incognito, run F12 -> Lighthouse (Mobile), and log: Performance Score, LCP, and CLS.">O'zingizning oldingi saytingizni (yoki target.uz ni) Incognito rejimida oching, F12 -> Lighthouse (Mobile) ni ishga tushiring va Performance balli, LCP hamda CLS natijalarini yozing.</p>
      <textarea id="hw_q3" class="hw-input" rows="3" placeholder="Performance: __ / 100 | LCP: __ s | CLS: __" data-placeholder-ru="Performance: __ / 100 | LCP: __ с | CLS: __" data-placeholder-en="Performance: __ / 100 | LCP: __ s | CLS: __"></textarea>
    </div>
"""

    tpl = re.sub(r'<div id="hw-container">[\s\S]*?</div>\s*<!-- #hw-container -->', lambda m: f'<div id="hw-container">\n{hw_content}\n    </div><!-- #hw-container -->', tpl)
    if 'id="hw-container"' not in tpl:
        tpl = re.sub(r'<main[^>]*>[\s\S]*?</main>', lambda m: f'<main class="hw-main">\n{hw_content}\n</main>', tpl)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_studio():
    studio_html = """<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Target Lighthouse & Core Web Vitals Studio" data-en="Target Lighthouse & Core Web Vitals Studio">Target Lighthouse & Core Web Vitals Studio</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap">
  <style>
    :root {
      --bg: #070d1a; --panel: #0f172a; --panel-2: #1e293b; --ink: #f8fafc; --ink-2: #94a3b8;
      --accent: #38bdf8; --ok: #10b981; --warn: #f59e0b; --danger: #ef4444; --border: #1e293b;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Manrope', sans-serif; background: var(--bg); color: var(--ink); min-height: 100vh; padding: 20px; }
    .container { max-width: 1120px; margin: 0 auto; }
    header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 16px; border-bottom: 1px solid var(--border); margin-bottom: 20px; flex-wrap: wrap; gap: 12px; }
    .brand { display: flex; align-items: center; gap: 12px; }
    .badge { background: rgba(56, 189, 248, 0.15); color: var(--accent); padding: 4px 10px; border-radius: 99px; font-size: 12px; font-weight: 700; }
    .lang-btns { display: flex; gap: 6px; }
    .lang-btn { background: var(--panel); color: var(--ink-2); border: 1px solid var(--border); padding: 6px 12px; border-radius: 8px; cursor: pointer; font-weight: 700; font-size: 12px; }
    .lang-btn.active { background: var(--accent); color: #020617; border-color: var(--accent); }
    .grid { display: grid; grid-template-columns: 1.1fr 1fr; gap: 20px; }
    @media (max-width: 840px) { .grid { grid-template-columns: 1fr; } }
    .card { background: var(--panel); border: 1px solid var(--border); border-radius: 14px; padding: 20px; }
    .score-wrap { display: flex; align-items: center; gap: 24px; margin-bottom: 20px; }
    .gauge { width: 110px; height: 110px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 36px; font-weight: 800; border: 8px solid var(--danger); transition: all 0.4s ease; flex-shrink: 0; }
    .vitals { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 20px; }
    .vital-box { background: var(--panel-2); padding: 12px; border-radius: 10px; text-align: center; }
    .vital-label { font-size: 11px; color: var(--ink-2); font-weight: 700; }
    .vital-val { font-family: 'JetBrains Mono', monospace; font-size: 20px; font-weight: 700; margin-top: 4px; }
    .toggle-list { display: flex; flex-direction: column; gap: 10px; }
    .toggle-item { display: flex; align-items: center; justify-content: space-between; background: var(--panel-2); padding: 12px 14px; border-radius: 10px; border: 1px solid transparent; cursor: pointer; transition: 0.2s; }
    .toggle-item.active { border-color: var(--ok); background: rgba(16, 185, 129, 0.08); }
    .toggle-info h4 { font-size: 14px; margin-bottom: 2px; }
    .toggle-info p { font-size: 12px; color: var(--ink-2); }
    .switch { width: 44px; height: 24px; background: #334155; border-radius: 99px; position: relative; transition: 0.2s; flex-shrink: 0; }
    .switch::after { content: ''; position: absolute; top: 3px; left: 3px; width: 18px; height: 18px; background: #fff; border-radius: 50%; transition: 0.2s; }
    .toggle-item.active .switch { background: var(--ok); }
    .toggle-item.active .switch::after { transform: translateX(20px); }
    .waterfall { display: flex; flex-direction: column; gap: 10px; margin-top: 12px; }
    .wf-row { display: grid; grid-template-columns: 120px 1fr 65px; align-items: center; gap: 10px; font-family: 'JetBrains Mono', monospace; font-size: 12px; }
    .wf-track { background: #020617; height: 16px; border-radius: 4px; overflow: hidden; position: relative; }
    .wf-bar { height: 100%; border-radius: 4px; transition: width 0.4s ease, background 0.3s; }
    .reset-btn { margin-top: 16px; width: 100%; padding: 10px; background: transparent; border: 1px solid var(--border); color: var(--ink-2); border-radius: 8px; cursor: pointer; font-weight: 700; }
    .reset-btn:hover { border-color: var(--accent); color: var(--ink); }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="brand">
        <span class="badge" data-ru="9-КЛАСС · УРОК 36" data-en="GRADE 9 · LESSON 36">9-SINF · 36-DARS</span>
        <h2 data-ru="Target Lighthouse & Core Web Vitals Studio" data-en="Target Lighthouse & Core Web Vitals Studio">Target Lighthouse & Core Web Vitals Studio</h2>
      </div>
      <div class="lang-btns">
        <button class="lang-btn active" onclick="setLang('uz')">UZ</button>
        <button class="lang-btn" onclick="setLang('ru')">RU</button>
        <button class="lang-btn" onclick="setLang('en')">EN</button>
      </div>
    </header>

    <div class="grid">
      <!-- LEFT: CONTROLS -->
      <div class="card">
        <h3 style="margin-bottom:12px;" data-ru="Инженерные Оптимизации (Включайте по очереди)" data-en="Engineering Optimizations (Toggle Step-by-Step)">Muhandislik Optimizatsiyalari (Ketma-ket Yoqing)</h3>
        <div class="toggle-list">
          <div class="toggle-item" id="opt-webp" onclick="toggleOpt('webp')">
            <div class="toggle-info">
              <h4 data-ru="1. Конвертировать Hero PNG (3.2 МБ) ➔ AVIF/WebP (140 КБ)" data-en="1. Convert Hero PNG (3.2 MB) ➔ AVIF/WebP (140 KB)">1. Hero PNG (3.2 MB) ➔ AVIF/WebP (140 KB)</h4>
              <p data-ru="Снижает вес картинки на 95% и ускоряет LCP" data-en="Cuts image payload by 95% and boosts LCP">Rasm hajmini 95% kamaytiradi va LCP ni tezlashtiradi</p>
            </div>
            <div class="switch"></div>
          </div>

          <div class="toggle-item" id="opt-cls" onclick="toggleOpt('cls')">
            <div class="toggle-info">
              <h4 data-ru="2. Задать width/height для <img>" data-en="2. Lock width/height on <img>">2. &lt;img&gt; ga width/height berish</h4>
              <p data-ru="Резервирует место в макете: устраняет скачки (CLS = 0)" data-en="Reserves layout space: eliminates jumps (CLS = 0)">Maketda joy ajratadi: sakrashni yo'qotadi (CLS = 0)</p>
            </div>
            <div class="switch"></div>
          </div>

          <div class="toggle-item" id="opt-defer" onclick="toggleOpt('defer')">
            <div class="toggle-info">
              <h4 data-ru="3. Добавить <script defer> на bundle.js" data-en="3. Add <script defer> to bundle.js">3. bundle.js ga &lt;script defer&gt; qo'shish</h4>
              <p data-ru="Убирает блокировку HTML-парсера и ускоряет INP" data-en="Unblocks HTML parser and improves INP">HTML chizilishini to'xtatmaydi va INP ni yaxshilaydi</p>
            </div>
            <div class="switch"></div>
          </div>

          <div class="toggle-item" id="opt-brotli" onclick="toggleOpt('brotli')">
            <div class="toggle-info">
              <h4 data-ru="4. Включить сжатие Brotli (Content-Encoding: br)" data-en="4. Enable Brotli Compression (br)">4. Brotli (Content-Encoding: br) siqishni yoqish</h4>
              <p data-ru="Сжимает JS/CSS/HTML по сети на 75%" data-en="Compresses JS/CSS/HTML over the wire by 75%">Tarmoqda JS/CSS/HTML ni 75% gacha siqadi</p>
            </div>
            <div class="switch"></div>
          </div>

          <div class="toggle-item" id="opt-cache" onclick="toggleOpt('cache')">
            <div class="toggle-info">
              <h4 data-ru="5. Cache-Control: max-age=31536000, immutable" data-en="5. Cache-Control: max-age=31536000, immutable">5. Cache-Control: max-age=31536000, immutable</h4>
              <p data-ru="Повторные визиты загружают статику из кэша за 0 мс" data-en="Repeat visits load static assets from disk cache in 0 ms">Qayta tashrifda statik fayllar keshdan 0 ms da ochiladi</p>
            </div>
            <div class="switch"></div>
          </div>
        </div>
        <button class="reset-btn" onclick="resetAll()" data-ru="↺ Сбросить все настройки" data-en="↺ Reset All Optimizations">↺ Barcha sozlamalarni tiklash</button>
      </div>

      <!-- RIGHT: LIGHTHOUSE GAUGE & WATERFALL -->
      <div class="card">
        <div class="score-wrap">
          <div class="gauge" id="lh-gauge">42</div>
          <div>
            <div style="font-size:12px; color:var(--ink-2); font-weight:700;" data-ru="ОЦЕНКА GOOGLE LIGHTHOUSE" data-en="GOOGLE LIGHTHOUSE SCORE">GOOGLE LIGHTHOUSE BALLI</div>
            <h3 id="lh-status" style="margin-top:4px; color:var(--danger);" data-ru="Критически Медленно (Стартап умирает)" data-en="Critically Slow (Startup Dying)">Juda Sekin (Startap xavf ostida)</h3>
            <div style="font-size:13px; color:var(--ink-2); margin-top:4px;" id="payload-total">Total Weight: 4.80 MB</div>
          </div>
        </div>

        <div class="vitals">
          <div class="vital-box">
            <div class="vital-label">LCP</div>
            <div class="vital-val" id="val-lcp" style="color:var(--danger);">6.4s</div>
          </div>
          <div class="vital-box">
            <div class="vital-label">INP</div>
            <div class="vital-val" id="val-inp" style="color:var(--danger);">480ms</div>
          </div>
          <div class="vital-box">
            <div class="vital-label">CLS</div>
            <div class="vital-val" id="val-cls" style="color:var(--danger);">0.42</div>
          </div>
        </div>

        <h4 style="font-size:13px; color:var(--ink-2); margin-bottom:8px;" data-ru="Сетевой Waterfall (Повторный/Холодный визит)" data-en="Network Waterfall Timeline">Tarmoq Waterfall Vaqt Chizig'i</h4>
        <div class="waterfall">
          <div class="wf-row">
            <span>index.html</span>
            <div class="wf-track"><div class="wf-bar" id="bar-html" style="width:12%; background:var(--accent);"></div></div>
            <span id="time-html">120ms</span>
          </div>
          <div class="wf-row">
            <span>style.css</span>
            <div class="wf-track"><div class="wf-bar" id="bar-css" style="width:28%; background:#a78bfa;"></div></div>
            <span id="time-css">450ms</span>
          </div>
          <div class="wf-row">
            <span>bundle.js</span>
            <div class="wf-track"><div class="wf-bar" id="bar-js" style="width:65%; background:var(--warn);"></div></div>
            <span id="time-js">1850ms</span>
          </div>
          <div class="wf-row">
            <span id="label-img">hero.png</span>
            <div class="wf-track"><div class="wf-bar" id="bar-img" style="width:95%; background:var(--danger);"></div></div>
            <span id="time-img">4100ms</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
    var state = { webp: false, cls: false, defer: false, brotli: false, cache: false };
    var currentLang = 'uz';

    var STATUS_TXT = {
      bad: { uz: "Juda Sekin (Startap xavf ostida)", ru: "Критически Медленно (Стартап умирает)", en: "Critically Slow (Startup Dying)" },
      mid: { uz: "O'rtacha (Yaxshilanmoqda)", ru: "Средне (Требует доработки)", en: "Needs Improvement" },
      good: { uz: "A'lo! Production Tayyor (99+)", ru: "Отлично! Готово к Production", en: "Blazing Fast! Production Ready" }
    };

    function toggleOpt(key) {
      state[key] = !state[key];
      document.getElementById('opt-' + key).classList.toggle('active', state[key]);
      recalc();
    }

    function resetAll() {
      for (var k in state) {
        state[k] = false;
        document.getElementById('opt-' + k).classList.remove('active');
      }
      recalc();
    }

    function recalc() {
      var score = 42;
      var lcp = 6.4;
      var inp = 480;
      var cls = 0.42;
      var weightKB = 4800;

      var tHtml = 120, tCss = 450, tJs = 1850, tImg = 4100;

      if (state.webp) {
        score += 22;
        lcp -= 2.8;
        weightKB -= 3060;
        tImg = 320;
        document.getElementById('label-img').textContent = 'hero.avif';
      } else {
        document.getElementById('label-img').textContent = 'hero.png';
      }

      if (state.cls) {
        score += 12;
        cls = 0.00;
      }

      if (state.defer) {
        score += 10;
        lcp -= 1.2;
        inp -= 260;
        tJs = 780;
      }

      if (state.brotli) {
        score += 8;
        lcp -= 0.9;
        inp -= 80;
        weightKB -= 1350;
        tHtml = 45;
        tCss = 110;
        tJs = Math.round(tJs * 0.35);
      }

      if (state.cache) {
        score += 6;
        lcp = Math.max(0.6, lcp - 0.8);
        tCss = 0; tJs = 0; tImg = 0;
      }

      score = Math.min(100, score);
      lcp = Math.max(0.6, lcp).toFixed(1);
      inp = Math.max(60, inp);
      cls = cls.toFixed(2);

      var gauge = document.getElementById('lh-gauge');
      var stEl = document.getElementById('lh-status');
      gauge.textContent = score;

      var color = score >= 90 ? 'var(--ok)' : (score >= 65 ? 'var(--warn)' : 'var(--danger)');
      var tier = score >= 90 ? 'good' : (score >= 65 ? 'mid' : 'bad');
      gauge.style.borderColor = color;
      gauge.style.color = color;
      stEl.style.color = color;
      stEl.textContent = STATUS_TXT[tier][currentLang];

      document.getElementById('val-lcp').textContent = lcp + 's';
      document.getElementById('val-lcp').style.color = parseFloat(lcp) <= 2.5 ? 'var(--ok)' : 'var(--danger)';

      document.getElementById('val-inp').textContent = inp + 'ms';
      document.getElementById('val-inp').style.color = inp <= 200 ? 'var(--ok)' : 'var(--danger)';

      document.getElementById('val-cls').textContent = cls;
      document.getElementById('val-cls').style.color = parseFloat(cls) <= 0.1 ? 'var(--ok)' : 'var(--danger)';

      var wStr = weightKB >= 1000 ? (weightKB / 1000).toFixed(2) + ' MB' : weightKB + ' KB';
      document.getElementById('payload-total').textContent = 'Total Weight: ' + wStr;

      document.getElementById('bar-html').style.width = Math.max(3, (tHtml / 4100) * 100) + '%';
      document.getElementById('time-html').textContent = tHtml + 'ms';

      document.getElementById('bar-css').style.width = (tCss === 0 ? 2 : Math.max(4, (tCss / 4100) * 100)) + '%';
      document.getElementById('time-css').textContent = tCss === 0 ? '0ms (cache)' : tCss + 'ms';

      document.getElementById('bar-js').style.width = (tJs === 0 ? 2 : Math.max(5, (tJs / 4100) * 100)) + '%';
      document.getElementById('time-js').textContent = tJs === 0 ? '0ms (cache)' : tJs + 'ms';

      document.getElementById('bar-img').style.width = (tImg === 0 ? 2 : Math.max(5, (tImg / 4100) * 100)) + '%';
      document.getElementById('time-img').textContent = tImg === 0 ? '0ms (cache)' : tImg + 'ms';
      document.getElementById('bar-img').style.background = tImg <= 350 ? 'var(--ok)' : 'var(--danger)';
    }

    function setLang(lang) {
      currentLang = lang;
      document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      document.querySelectorAll('[data-ru]').forEach(el => {
        if (!el.dataset.uz) el.dataset.uz = el.innerHTML;
        if (lang === 'uz') el.innerHTML = el.dataset.uz;
        else if (lang === 'ru') el.innerHTML = el.dataset.ru;
        else if (lang === 'en') el.innerHTML = el.dataset.en;
      });
      recalc();
    }
  </script>
</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "studio", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(studio_html)
    print("  ✓ Created: studio/index.html")

def build_teacher_guide():
    guide = """# O'qituvchi Qo'llanmasi — 9-sinf · 12-hafta · 36-dars

**Mavzu:** Veb-Ilova Tezligi: Kesh, Assetlar va Lighthouse Auditi (Core Web Vitals)  
**Davomiyligi:** 80 daqiqa (Juftlik Blok)  

## Vaqt Taqsimoti
### 1-Bosqich (40 daqiqa)
- **00:00–05:00 (Kirish):** Startap drama ssenariysi — 4 MB PNG tufayli sayt 8 soniya qotib investorlar oldida uyatga qoladi.
- **05:00–13:00 (HW Check - 35-dars):** `npm install --force` va lockfile ni o'chirish xatolari. `npm ci --ignore-scripts --omit=dev` oltin standarti.
- **13:00–40:00 (Nazariya):**
  - Core Web Vitals: LCP (`<=2.5s`), INP (`<=200ms`), CLS (`<=0.1`).
  - Rasmlar: PNG -> WebP/AVIF, `loading="lazy"`, `width`/`height` bilan CLS=0.
  - JS yuklanishi: `defer` vs `async` vs bloklash.
  - Tarmoq siqish (Brotli `br` vs Gzip) va `Cache-Control: max-age=31536000, immutable` vs `index.html: no-cache`.
- **40:00–45:00 (Quiz):** 4 ta tezkor savol.

### 2-Bosqich (40 daqiqa)
- **45:00–50:00 (Refleksiya):** 1-bosqich xulosasi va amaliyotga ko'prik.
- **50:00–72:00 (Amaliyot & DevTools):** `studio/index.html` da 42 balldan 100 ballga chiqish chellenji + Chrome DevTools (Incognito Lighthouse & Network throttling).
- **72:00–77:00 (Peer Review & Demo):** Juftliklar tekshiruvi + 2 o'quvchi Smartboardda jonli sayt auditi.
- **77:00–80:00 (Xulosa & Vazifa):** `vazifa.html` (4+4+2 = 10 ball).
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(guide)
    print("  ✓ Created: TEACHER_READING.md")

if __name__ == "__main__":
    print("📦 Building 9-sinf (Lesson 36: Web Performance & Lighthouse Audit)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_studio()
    build_teacher_guide()
    print("🎉 Done! Generated Grade 9 Lesson 36.")
