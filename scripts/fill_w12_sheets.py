#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/fill_w12_sheets.py — fills the two unfinished Week 12 worksheets and
homework apps (10-11 / Lesson 31 and 9 / Lesson 35) with real, topic-specific
trilingual content instead of {{PLACEHOLDER}} tokens.
"""

import os

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# =============================================================================
# 10–11-SINF · 12-HAFTA · 31-DARS — Multi-Modal Vision Agents & Computer-Use
# =============================================================================
L31 = {
    "LESSON_NUM": "31",
    "LESSON_SLUG": "w12-l31-vision-agentlar",
    "COHORT_LABEL_UZ": "10–11-sinf",
    "COHORT_LABEL_RU": "10–11 класс",
    "COHORT_LABEL_EN": "Grades 10–11",
    "TITLE_UZ": "Multi-Modal Vision Agentlar va Computer-Use: Ekran Boshqaruvi va Desktop Avtomatlashtirish",
    "TITLE_RU": "Мультимодальные Vision-Агенты и Computer-Use: Управление Экраном и Автоматизация Рабочего Стола",
    "TITLE_EN": "Multi-Modal Vision Agents & Computer-Use: Screen Control & Desktop Automation",
    "META_UZ": "10–11-sinf · 12-hafta · 31-dars · Yakka dars (40 daqiqa)",
    "META_RU": "10–11 класс · 12-я неделя · Урок 31 · Одиночный урок (40 минут)",
    "META_EN": "Grades 10–11 · Week 12 · Lesson 31 · Single block (40 min)",
    "MISSION_UZ": "DOM chegarasidan chiqib, ekran piksellarini ko'radigan va sichqonchani boshqaradigan Computer-Use agentini loyihalash: skrinshot → vision model → koordinata → harakat → tekshiruv tsiklini tushunish va xavfsiz sandboxda sinash.",
    "MISSION_RU": "Выйти за пределы DOM и спроектировать Computer-Use агента, который видит пиксели экрана и управляет мышью: понять цикл скриншот → vision-модель → координаты → действие → проверка и испытать его в безопасной песочнице.",
    "MISSION_EN": "Go beyond the DOM and design a Computer-Use agent that sees screen pixels and drives the mouse: understand the screenshot → vision model → coordinates → action → verification loop and test it in a safe sandbox.",
    "SEC1_TITLE_UZ": "Computer-Use Arxitekturasi: Ko'z, Qaror va Qo'l",
    "SEC1_TITLE_RU": "Архитектура Computer-Use: Глаза, Решение и Руки",
    "SEC1_TITLE_EN": "Computer-Use Architecture: Eyes, Decision & Hands",
    "SEC1_CONTENT": """
    <div class="box-grid">
      <div class="box">
        <h4 data-ru="1. Зрение (Screenshot)" data-en="1. Eyes (Screenshot)">1. Ko'z (Skrinshot)</h4>
        <p data-ru="Агент делает снимок экрана и отправляет его мультимодальной модели как изображение." data-en="The agent captures the screen and sends it to the multimodal model as an image.">Agent ekran suratini oladi va uni multimodelga rasm sifatida yuboradi.</p>
      </div>
      <div class="box">
        <h4 data-ru="2. Решение (Vision Model)" data-en="2. Decision (Vision Model)">2. Qaror (Vision Model)</h4>
        <p data-ru="Модель находит кнопку по пикселям, возвращает координаты [x, y] и выбранное действие." data-en="The model locates the button in pixels and returns [x, y] coordinates plus the chosen action.">Model tugmani piksellar bo'yicha topadi, [x, y] koordinatalari va tanlangan harakatni qaytaradi.</p>
      </div>
      <div class="box">
        <h4 data-ru="3. Руки (Driver)" data-en="3. Hands (Driver)">3. Qo'l (Drayver)</h4>
        <p data-ru="PyAutoGUI или драйвер ОС выполняет клик, ввод текста или нажатие клавиши." data-en="PyAutoGUI or an OS driver performs the click, text input, or key press.">PyAutoGUI yoki OS drayveri klik, matn kiritish yoki tugma bosishni bajaradi.</p>
      </div>
      <div class="box">
        <h4 data-ru="4. Проверка (Новый Скриншот)" data-en="4. Verification (Fresh Screenshot)">4. Tekshiruv (Yangi Skrinshot)</h4>
        <p data-ru="После каждого действия делается новый снимок: цикл повторяется, пока результат не подтверждён." data-en="A fresh capture follows every action: the loop repeats until the result is confirmed.">Har harakatdan keyin yangi surat olinadi: natija tasdiqlanmaguncha tsikl takrorlanadi.</p>
      </div>
    </div>
    <div class="code-snippet">
{ "type": "tool_use", "name": "computer",
  "input": { "action": "left_click", "coordinate": [512, 384] } }
    </div>
""",
    "SEC2_TITLE_UZ": "Visual Grounding: 1024×768 To'ridan Real Pikselga",
    "SEC2_TITLE_RU": "Visual Grounding: Из Сетки 1024×768 в Реальные Пиксели",
    "SEC2_TITLE_EN": "Visual Grounding: From the 1024×768 Grid to Real Pixels",
    "SEC2_CONTENT": """
    <div class="box-grid">
      <div class="box">
        <h4 data-ru="❌ Типичная ошибка" data-en="❌ Common mistake">❌ Oddiy xato</h4>
        <p data-ru="Сырые координаты модели передаются в pyautogui.click() без масштабирования. На Retina или 4K курсор промахивается на сотни пикселей." data-en="Raw model coordinates are passed into pyautogui.click() without scaling. On Retina or 4K the cursor misses by hundreds of pixels.">Model koordinatalari masshtablashsiz pyautogui.click() ga uzatiladi. Retina yoki 4K da kursor yuzlab pikselga xato qiladi.</p>
        <div class="code-snippet">pyautogui.click(apiX, apiY); // xato!</div>
      </div>
      <div class="box">
        <h4 data-ru="✅ Золотой стандарт" data-en="✅ Golden standard">✅ Oltin standart</h4>
        <p data-ru="Сначала вычисляем scaleX и scaleY, затем округляем результат через round() до целого пикселя." data-en="Compute scaleX and scaleY first, then round the result to a whole pixel.">Avval scaleX va scaleY hisoblanadi, so'ng natija round() bilan butun pikselga yaxlitlanadi.</p>
        <div class="code-snippet">const rx = Math.round(apiX * (screen.width / 1024));
const ry = Math.round(apiY * (screen.height / 768));</div>
      </div>
    </div>
    <p style="margin-top:8px;" data-ru="Формула: realX = round(apiX × screen.width / 1024), realY = round(apiY × screen.height / 768). Для HiDPI дополнительно учитывайте devicePixelRatio." data-en="Formula: realX = round(apiX × screen.width / 1024), realY = round(apiY × screen.height / 768). For HiDPI also account for devicePixelRatio.">Formula: realX = round(apiX × screen.width / 1024), realY = round(apiY × screen.height / 768). HiDPI uchun devicePixelRatio'ni ham hisobga oling.</p>
""",
    "SEC3_TITLE_UZ": "Amaliy Laboratoriya: Kalkulyator va Hisobot",
    "SEC3_TITLE_RU": "Практическая Лаборатория: Калькулятор и Отчёт",
    "SEC3_TITLE_EN": "Hands-on Lab: Calculator & Report",
    "SEC3_CONTENT": """
    <table style="width:100%; border-collapse:collapse; font-size:8pt;">
      <thead>
        <tr style="background:var(--panel-2);">
          <th style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Шаг" data-en="Step">Qadam</th>
          <th style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Действие агента" data-en="Agent action">Agent harakati</th>
          <th style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Ожидаемый результат" data-en="Expected result">Kutilgan natija</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="1" data-en="1">1</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Запустить контейнер с Xvfb и открыть виртуальный экран." data-en="Start the Xvfb container and open the virtual screen.">Xvfb konteynerini ishga tushirish va virtual ekranni ochish.</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Браузер показывает рабочий стол песочницы." data-en="The browser shows the sandbox desktop.">Brauzer sandbox ish stolini ko'rsatadi.</td>
        </tr>
        <tr>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="2" data-en="2">2</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Найти калькулятор по скриншоту и нажать 1, 2, 5, ×, 4, 8, =." data-en="Locate Calculator from the screenshot and press 1, 2, 5, ×, 4, 8, =.">Skrinshot bo'yicha kalkulyatorni topish va 1, 2, 5, ×, 4, 8, = ni bosish.</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="На дисплее появляется 6000." data-en="The display shows 6000.">Displeyda 6000 paydo bo'ladi.</td>
        </tr>
        <tr>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="3" data-en="3">3</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Сверить результат новым скриншотом и OCR." data-en="Verify the result with a fresh screenshot and OCR.">Natijani yangi skrinshot va OCR bilan solishtirish.</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Агент подтверждает: 125 × 48 = 6000." data-en="The agent confirms: 125 × 48 = 6000.">Agent tasdiqlaydi: 125 × 48 = 6000.</td>
        </tr>
        <tr>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="4" data-en="4">4</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Открыть текстовый редактор и записать отчёт." data-en="Open a text editor and write the report.">Matn muharririni ochish va hisobot yozish.</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Файл report.txt содержит строку 125 × 48 = 6000." data-en="The report.txt file contains 125 × 48 = 6000.">report.txt faylida 125 × 48 = 6000 satri bor.</td>
        </tr>
      </tbody>
    </table>
""",
    "SEC4_CONTENT": """
    <div class="box-grid">
      <div class="box">
        <h4 data-ru="Уровень 1 · 4 балла" data-en="Tier 1 · 4 pts">1-Daraja · 4 ball</h4>
        <p data-ru="Повторите демо в песочнице: агент считает 125 × 48 и записывает результат в файл." data-en="Repeat the sandbox demo: the agent computes 125 × 48 and writes the result to a file.">Sandboxda demoni takrorlang: agent 125 × 48 ni hisoblab, natijani faylga yozadi.</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="Уровень 2 · 4 балла" data-en="Tier 2 · 4 pts">2-Daraja · 4 ball</h4>
        <p data-ru="Считайте результат не с DOM, а с пикселей через OCR (Tesseract) и сравните оба способа." data-en="Read the result from pixels via OCR (Tesseract) instead of the DOM and compare both methods.">Natijani DOMdan emas, piksellardan OCR (Tesseract) orqali o'qing va ikkala usulni solishtiring.</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="Уровень 3 · 2 балла" data-en="Tier 3 · 2 pts">3-Daraja · 2 ball</h4>
        <p data-ru="Придумайте on-screen prompt injection и докажите, что sandbox + HITL его блокируют." data-en="Craft an on-screen prompt injection and prove that sandbox + HITL block it.">Ekranga on-screen prompt injection o'ylab toping va sandbox + HITL uni bloklashini isbotlang.</p>
        <div class="write-line"></div>
      </div>
      <div class="box" style="border-color:var(--accent);">
        <h4 data-ru="Рефлексия" data-en="Reflection">Refleksiya</h4>
        <p data-ru="Что оказалось сложнее: координаты, свежесть скриншота или защита? Запишите один вывод." data-en="What was harder: coordinates, screenshot freshness, or safety? Write one takeaway.">Nima qiyin bo'ldi: koordinatalar, skrinshot yangiligi yoki himoya? Bitta xulosa yozing.</p>
        <div class="write-line"></div>
      </div>
    </div>
""",
    # --- vazifa ---
    "HERO_TAG_UZ": "10–11-sinf · 12-hafta · 31-dars",
    "HERO_DESC_UZ": "Computer-Use agentining koordinata matematikasi, xavfsizlik qatlamlari va HITL mexanizmini mustahkamlaydigan 3 bosqichli amaliy topshiriq.",
    "HERO_DESC_RU": "Трёхуровневое практическое задание на координатную математику Computer-Use агента, слои безопасности и механизм HITL.",
    "HERO_DESC_EN": "A three-tier assignment reinforcing Computer-Use coordinate math, defense layers, and the HITL mechanism.",
    "RUBRIC_T1_UZ": "Функция пересчёта координат и JSON-схема tool_use.",
    "RUBRIC_T1_RU": "Функция пересчёта координат и JSON-схема tool_use.",
    "RUBRIC_T1_EN": "Coordinate mapping function and the tool_use JSON schema.",
    "RUBRIC_T2_UZ": "Цикл скриншот → действие → проверка в коде.",
    "RUBRIC_T2_RU": "Цикл скриншот → действие → проверка в коде.",
    "RUBRIC_T2_EN": "Screenshot → action → verification loop in code.",
    "RUBRIC_T3_UZ": "План защиты от prompt injection и разрушительного клика.",
    "RUBRIC_T3_RU": "План защиты от prompt injection и разрушительного клика.",
    "RUBRIC_T3_EN": "Defense plan against prompt injection and destructive clicks.",
    "TASKS_HTML": """
  <div class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="Уровень 1 · База" data-en="Tier 1 · Core">1-Daraja · Baza</span>
      <span class="task-score">4 BALL</span>
    </div>
    <h3 data-ru="Пересчёт координат Vision-модели" data-en="Vision Model Coordinate Mapping">Vision Model Koordinatalarini O'tkazish</h3>
    <p data-ru="Напишите функцию toScreen(apiX, apiY, screenW, screenH), которая переводит координаты сетки 1024×768 в реальные пиксели экрана и округляет результат." data-en="Write toScreen(apiX, apiY, screenW, screenH) that maps 1024×768 grid coordinates to real screen pixels and rounds the result.">1024×768 to'ri koordinatalarini real ekran piksellariga o'tkazadigan va natijani yaxlitlaydigan toScreen(apiX, apiY, screenW, screenH) funksiyasini yozing.</p>
    <textarea class="answer-area" rows="7" data-ru="function toScreen(apiX, apiY, screenW, screenH) { ... }" data-en="function toScreen(apiX, apiY, screenW, screenH) { ... }"></textarea>
    <div class="btn-group">
      <button class="btn btn-outline" onclick="toggleSolution('sol-l31-1')" data-ru="Показать решение" data-en="Show solution">Yechimni ko'rish</button>
    </div>
    <div class="solution-box" id="sol-l31-1" hidden>
      <h4 data-ru="Эталонное решение" data-en="Reference solution">Etalon yechim</h4>
      <pre>function toScreen(apiX, apiY, screenW, screenH) {
  const realX = Math.round(apiX * (screenW / 1024));
  const realY = Math.round(apiY * (screenH / 768));
  return { realX, realY };
}</pre>
    </div>
  </div>

  <div class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="Уровень 2 · Инженерия" data-en="Tier 2 · Engineering">2-Daraja · Muhandislik</span>
      <span class="task-score">4 BALL</span>
    </div>
    <h3 data-ru="Цикл Computer-Use с проверкой и HITL" data-en="Computer-Use Loop with Verification & HITL">Tekshiruv va HITL bilan Computer-Use Tsikli</h3>
    <p data-ru="Опишите псевдокодом цикл агента: скриншот, запрос к модели, выполнение действия, новый скриншот для проверки. Добавьте остановку на подтверждение человеком перед удалением или отправкой." data-en="Describe the agent loop in pseudocode: screenshot, model call, action execution, fresh screenshot for verification. Add a human approval stop before delete or send.">Agent tsiklini psevdokod bilan yozing: skrinshot, modelga so'rov, harakatni bajarish, tekshirish uchun yangi skrinshot. O'chirish yoki yuborishdan oldin inson tasdig'ida to'xtashni qo'shing.</p>
    <textarea class="answer-area" rows="9" data-ru="while (true) { ... }" data-en="while (true) { ... }"></textarea>
    <div class="btn-group">
      <button class="btn btn-outline" onclick="toggleSolution('sol-l31-2')" data-ru="Показать решение" data-en="Show solution">Yechimni ko'rish</button>
    </div>
    <div class="solution-box" id="sol-l31-2" hidden>
      <h4 data-ru="Эталонное решение" data-en="Reference solution">Etalon yechim</h4>
      <pre>for (let step = 0; step &lt; MAX_STEPS; step++) {
  const shot = captureScreen();
  const action = await visionModel(shot, task);

  if (action.type === "delete" || action.type === "send") {
    if (!(await askHuman(action))) break;   // HITL
  }

  const { realX, realY } = toScreen(action.x, action.y, W, H);
  driver.click(realX, realY);
  if (await verifyResult()) break;
}</pre>
    </div>
  </div>

  <div class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="Уровень 3 · Челлендж" data-en="Tier 3 · Challenge">3-Daraja · Kiber-Chaqiruv</span>
      <span class="task-score">2 BALL</span>
    </div>
    <h3 data-ru="Аудит безопасности экранного агента" data-en="Screen-Agent Security Audit">Ekran Agenti Xavfsizlik Auditi</h3>
    <p data-ru="Перечислите три угрозы (prompt injection на экране, разрушительный клик, утечка .env) и для каждой предложите конкретный технический контроль: sandbox, least privilege или HITL." data-en="List three threats (on-screen prompt injection, destructive click, .env leak) and propose a concrete technical control for each: sandbox, least privilege, or HITL.">Uch tahdidni sanang (ekranda prompt injection, vayronkor klik, .env sizib chiqishi) va har biriga aniq texnik nazorat taklif qiling: sandbox, least privilege yoki HITL.</p>
    <textarea class="answer-area" rows="8" data-ru="1. Угроза → контроль ..." data-en="1. Threat → control ..."></textarea>
    <div class="btn-group">
      <button class="btn btn-outline" onclick="toggleSolution('sol-l31-3')" data-ru="Показать решение" data-en="Show solution">Yechimni ko'rish</button>
    </div>
    <div class="solution-box" id="sol-l31-3" hidden>
      <h4 data-ru="Эталонное решение" data-en="Reference solution">Etalon yechim</h4>
      <pre>1. Prompt injection на экране → sandbox + белый список приложений.
2. Разрушительный клик → HITL перед delete/send/payment.
3. Утечка .env → запрет монтирования домашней папки, read-only secrets.</pre>
    </div>
  </div>
""",
}

# =============================================================================
# 9-SINF · 12-HAFTA · 35-DARS — NPM Ecosystem & Supply Chain Security
# =============================================================================
L35 = {
    "LESSON_NUM": "35",
    "LESSON_SLUG": "w12-l35-npm-xavfsizlik",
    "COHORT_LABEL_UZ": "9-sinf",
    "COHORT_LABEL_RU": "9 класс",
    "COHORT_LABEL_EN": "Grade 9",
    "TITLE_UZ": "NPM Ekotizimi va Ta'minot Zanjiri Xavfsizligi: package.json, Lockfile va npm audit",
    "TITLE_RU": "Экосистема NPM и Безопасность Цепочки Поставок: package.json, Lockfile и npm audit",
    "TITLE_EN": "NPM Ecosystem & Supply Chain Security: package.json, Lockfile & npm audit",
    "META_UZ": "9-sinf · 12-hafta · 35-dars · Juftlik dars (80 daqiqa)",
    "META_RU": "9 класс · 12-я неделя · Урок 35 · Парный урок (80 минут)",
    "META_EN": "Grade 9 · Week 12 · Lesson 35 · Double block (80 min)",
    "MISSION_UZ": "Loyiha bog'liqliklarini auditdan o'tkazish: shubhali paket va postinstall skriptini topish, zaifliklarni yopish, toza lockfile'ni commit qilish va npm ci ni CI quvuriga ulash.",
    "MISSION_RU": "Провести аудит зависимостей проекта: найти подозрительный пакет и postinstall-скрипт, закрыть уязвимости, закоммитить чистый lockfile и подключить npm ci к CI-конвейеру.",
    "MISSION_EN": "Audit project dependencies: find a suspicious package and postinstall script, patch vulnerabilities, commit a clean lockfile, and wire npm ci into the CI pipeline.",
    "SEC1_TITLE_UZ": "NPM Ta'minot Zanjiri: Niyat, Fakt va Ijro",
    "SEC1_TITLE_RU": "Цепочка Поставок NPM: Намерение, Факт и Исполнение",
    "SEC1_TITLE_EN": "The NPM Supply Chain: Intent, Reality & Execution",
    "SEC1_CONTENT": """
    <div class="box-grid">
      <div class="box">
        <h4 data-ru="package.json — Намерение" data-en="package.json — Intent">package.json — Niyat</h4>
        <p data-ru="Описывает, что вы хотите установить: диапазоны версий, скрипты и разделение dependencies / devDependencies." data-en="Describes what you want installed: version ranges, scripts, and the dependencies / devDependencies split.">Nimani o'rnatmoqchi ekaningizni yozadi: versiya diapazonlari, skriptlar va dependencies / devDependencies ajratmasi.</p>
      </div>
      <div class="box">
        <h4 data-ru="package-lock.json — Факт" data-en="package-lock.json — Reality">package-lock.json — Fakt</h4>
        <p data-ru="Фиксирует точные версии, дерево зависимостей и хеши целостности sha512. Обязателен в Git." data-en="Locks exact versions, the dependency tree, and sha512 integrity hashes. Must be committed to Git.">Aniq versiyalar, bog'liqlik daraxti va sha512 yaxlitlik xeshlarini qotiradi. Git'ga majburiy qo'shiladi.</p>
      </div>
      <div class="box">
        <h4 data-ru="node_modules — Исполнение" data-en="node_modules — Execution">node_modules — Ijro</h4>
        <p data-ru="Код, который реально запускается на вашей машине. postinstall-скрипт выполняется при установке." data-en="The code that actually runs on your machine. A postinstall script executes during install.">Mashinangizda haqiqatan ishlaydigan kod. postinstall skripti o'rnatish paytida bajariladi.</p>
      </div>
      <div class="box" style="border-color:var(--accent);">
        <h4 data-ru="Главный вывод" data-en="Key takeaway">Asosiy xulosa</h4>
        <p data-ru="npm install — это не скачивание файлов, а запуск чужого кода с вашими правами." data-en="npm install is not downloading files; it is executing someone else's code with your permissions.">npm install — fayl yuklab olish emas, boshqa birovning kodini sizning huquqlaringiz bilan ishga tushirish.</p>
      </div>
    </div>
""",
    "SEC2_TITLE_UZ": "SemVer va Hujum Vektorlari: ^, ~ va postinstall",
    "SEC2_TITLE_RU": "SemVer и Векторы Атак: ^, ~ и postinstall",
    "SEC2_TITLE_EN": "SemVer & Attack Vectors: ^, ~ and postinstall",
    "SEC2_CONTENT": """
    <table style="width:100%; border-collapse:collapse; font-size:8pt;">
      <thead>
        <tr style="background:var(--panel-2);">
          <th style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Запись" data-en="Spec">Yozuv</th>
          <th style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Что разрешает" data-en="What it allows">Nimaga ruxsat beradi</th>
          <th style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Риск" data-en="Risk">Xavf</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="1.2.3" data-en="1.2.3">1.2.3</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Только версию 1.2.3." data-en="Only version 1.2.3.">Faqat 1.2.3 versiyasi.</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Патчи безопасности не приходят автоматически." data-en="Security patches do not arrive automatically.">Xavfsizlik yamoqlari avtomatik kelmaydi.</td>
        </tr>
        <tr>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="~1.2.3" data-en="~1.2.3">~1.2.3</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Патчи: 1.2.4, 1.2.9." data-en="Patches: 1.2.4, 1.2.9.">Parchlar: 1.2.4, 1.2.9.</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Низкий: major и minor зафиксированы." data-en="Low: major and minor are pinned.">Past: major va minor qulflangan.</td>
        </tr>
        <tr>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="^1.2.3" data-en="^1.2.3">^1.2.3</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Минорные обновления: 1.3.0, 1.9.9." data-en="Minor updates: 1.3.0, 1.9.9.">Minor yangilanishlar: 1.3.0, 1.9.9.</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Средний: новая функциональность может сломать совместимость." data-en="Medium: new features may break compatibility.">O'rta: yangi funksiyalar moslikni buzishi mumkin.</td>
        </tr>
      </tbody>
    </table>
    <div class="box-grid" style="margin-top:8px;">
      <div class="box">
        <h4 data-ru="Typosquatting" data-en="Typosquatting">Typosquatting</h4>
        <p data-ru="Пакет crossenv вместо cross-env: одна буква — и вы запускаете чужой код." data-en="The package crossenv instead of cross-env: one letter and you run foreign code.">cross-env o'rniga crossenv paketi: bitta harf — va siz begona kodni ishga tushirasiz.</p>
        <div class="code-snippet">npm install crossenv  # xato!</div>
      </div>
      <div class="box">
        <h4 data-ru="postinstall" data-en="postinstall">postinstall</h4>
        <p data-ru="Скрипт установки читает .env и отправляет токены на сервер атакующего." data-en="The install script reads .env and sends tokens to the attacker's server.">O'rnatish skripti .env ni o'qib, tokenlarni hujumchi serveriga yuboradi.</p>
        <div class="code-snippet">"postinstall": "node ./collect.js"</div>
      </div>
    </div>
""",
    "SEC3_TITLE_UZ": "Amaliy Laboratoriya: Troyanni Top va Loyihani Tuzat",
    "SEC3_TITLE_RU": "Практическая Лаборатория: Найди Троян и Почини Проект",
    "SEC3_TITLE_EN": "Hands-on Lab: Find the Trojan & Fix the Project",
    "SEC3_CONTENT": """
    <table style="width:100%; border-collapse:collapse; font-size:8pt;">
      <thead>
        <tr style="background:var(--panel-2);">
          <th style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Шаг" data-en="Step">Qadam</th>
          <th style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Команда / действие" data-en="Command / action">Buyruq / harakat</th>
          <th style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Что записать в отчёт" data-en="What to record">Hisobotga nima yozish</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="1" data-en="1">1</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Открыть package.json и найти пакет с опечаткой." data-en="Open package.json and find the typo package.">package.json ni ochib, xatoli paketni topish.</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Имя пакета и чем он опасен." data-en="Package name and why it is dangerous.">Paket nomi va nima uchun xavfli.</td>
        </tr>
        <tr>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="2" data-en="2">2</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Удалить пакет и запретить install-скрипты." data-en="Remove the package and disable install scripts.">Paketni olib tashlash va install skriptlarini taqiqlash.</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Команда удаления и флаг --ignore-scripts." data-en="Removal command and the --ignore-scripts flag.">O'chirish buyrug'i va --ignore-scripts bayrog'i.</td>
        </tr>
        <tr>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="3" data-en="3">3</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Запустить npm audit и npm audit fix." data-en="Run npm audit and npm audit fix.">npm audit va npm audit fix ni ishga tushirish.</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Severity до и после исправления." data-en="Severity before and after the fix.">Tuzatishdan oldin va keyin severity.</td>
        </tr>
        <tr>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="4" data-en="4">4</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Закоммитить package.json и lockfile, проверить npm ci." data-en="Commit package.json and lockfile, verify npm ci.">package.json va lockfile'ni commit qilish, npm ci ni tekshirish.</td>
          <td style="border:1px solid var(--rule); padding:4px 6px;" data-ru="Diff lockfile и вывод npm ci." data-en="Lockfile diff and npm ci output.">Lockfile diffi va npm ci natijasi.</td>
        </tr>
      </tbody>
    </table>
""",
    "SEC4_CONTENT": """
    <div class="box-grid">
      <div class="box">
        <h4 data-ru="Уровень 1 · 4 балла" data-en="Tier 1 · 4 pts">1-Daraja · 4 ball</h4>
        <p data-ru="Запустите npm audit в своём проекте и выпишите все high/critical уязвимости." data-en="Run npm audit in your project and list every high/critical vulnerability.">Loyihangizda npm audit ishga tushiring va barcha high/critical zaifliklarni yozing.</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="Уровень 2 · 4 балла" data-en="Tier 2 · 4 pts">2-Daraja · 4 ball</h4>
        <p data-ru="Создайте проект, зафиксируйте версии, закоммитьте lockfile и подключите npm ci в CI." data-en="Create a project, pin versions, commit the lockfile, and wire npm ci into CI.">Loyiha yarating, versiyalarni qulflang, lockfile'ni commit qiling va CI'da npm ci ni ulang.</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="Уровень 3 · 2 балла" data-en="Tier 3 · 2 pts">3-Daraja · 2 ball</h4>
        <p data-ru="Опишите, как typosquatting + postinstall украдёт .env, и предложите три защиты." data-en="Describe how typosquatting + postinstall would steal .env and propose three defenses.">Typosquatting + postinstall .env ni qanday o'g'irlashini yozing va uchta himoya taklif qiling.</p>
        <div class="write-line"></div>
      </div>
      <div class="box" style="border-color:var(--accent);">
        <h4 data-ru="Рефлексия" data-en="Reflection">Refleksiya</h4>
        <p data-ru="Какой пакет в вашем проекте вы больше никогда не установите без проверки? Почему?" data-en="Which package in your project will you never install again without checking? Why?">Loyihangizdagi qaysi paketni endi tekshirmasdan o'rnatmaysiz? Nega?</p>
        <div class="write-line"></div>
      </div>
    </div>
""",
    # --- vazifa ---
    "HERO_TAG_UZ": "9-sinf · 12-hafta · 35-dars",
    "HERO_DESC_UZ": "Lockfile, SemVer, typosquatting va npm audit bo'yicha uch bosqichli amaliy topshiriq: nazariyadan haqiqiy audit hisobotigacha.",
    "HERO_DESC_RU": "Трёхуровневое практическое задание по lockfile, SemVer, typosquatting и npm audit: от теории до реального отчёта об аудите.",
    "HERO_DESC_EN": "A three-tier assignment on lockfile, SemVer, typosquatting, and npm audit: from theory to a real audit report.",
    "RUBRIC_T1_UZ": "package.json, lockfile и команда npm ci.",
    "RUBRIC_T1_RU": "package.json, lockfile и команда npm ci.",
    "RUBRIC_T1_EN": "package.json, lockfile, and the npm ci command.",
    "RUBRIC_T2_UZ": "Отчёт npm audit с классификацией severity и планом исправления.",
    "RUBRIC_T2_RU": "Отчёт npm audit с классификацией severity и планом исправления.",
    "RUBRIC_T2_EN": "An npm audit report with severity classification and a fix plan.",
    "RUBRIC_T3_UZ": "Сценарий атаки на цепочку поставок и три защиты.",
    "RUBRIC_T3_RU": "Сценарий атаки на цепочку поставок и три защиты.",
    "RUBRIC_T3_EN": "A supply-chain attack scenario and three defenses.",
    "TASKS_HTML": """
  <div class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="Уровень 1 · База" data-en="Tier 1 · Core">1-Daraja · Baza</span>
      <span class="task-score">4 BALL</span>
    </div>
    <h3 data-ru="Намерение и Факт: package.json + lockfile" data-en="Intent & Reality: package.json + lockfile">Niyat va Fakt: package.json + lockfile</h3>
    <p data-ru="Напишите фрагмент package.json с точной версией express и объясните, почему package-lock.json обязан быть в Git. Добавьте команду установки только рантайм-зависимостей." data-en="Write a package.json fragment pinning an exact express version and explain why package-lock.json must be committed. Add the command that installs only runtime dependencies.">Aniq express versiyasi bilan package.json fragmentini yozing va package-lock.json nima uchun Git'da bo'lishi shartligini tushuntiring. Faqat runtime bog'liqliklarini o'rnatadigan buyruqni qo'shing.</p>
    <textarea class="answer-area" rows="8" data-ru="{ &quot;dependencies&quot;: { ... } }" data-en="{ &quot;dependencies&quot;: { ... } }"></textarea>
    <div class="btn-group">
      <button class="btn btn-outline" onclick="toggleSolution('sol-l35-1')" data-ru="Показать решение" data-en="Show solution">Yechimni ko'rish</button>
    </div>
    <div class="solution-box" id="sol-l35-1" hidden>
      <h4 data-ru="Эталонное решение" data-en="Reference solution">Etalon yechim</h4>
      <pre>{
  "dependencies": { "express": "4.19.2" }
}
# lockfile фиксирует точные версии и хеши,
# поэтому у коллеги и на сервере одинаковый установ.
npm ci --omit=dev</pre>
    </div>
  </div>

  <div class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="Уровень 2 · Инженерия" data-en="Tier 2 · Engineering">2-Daraja · Muhandislik</span>
      <span class="task-score">4 BALL</span>
    </div>
    <h3 data-ru="Отчёт npm audit: severity и план исправления" data-en="npm audit Report: Severity & Fix Plan">npm audit Hisoboti: Severity va Tuzatish Rejasi</h3>
    <p data-ru="Запустите npm audit, выпишите одну critical и одну high уязвимость, укажите пакет, путь зависимости и команду исправления. Объясните, почему npm audit fix --force опасен." data-en="Run npm audit, list one critical and one high vulnerability, state the package, dependency path, and fix command. Explain why npm audit fix --force is dangerous.">npm audit ni ishga tushiring, bitta critical va bitta high zaiflikni yozing, paket, bog'liqlik yo'li va tuzatish buyrug'ini ko'rsating. npm audit fix --force nima uchun xavfli ekanini tushuntiring.</p>
    <textarea class="answer-area" rows="9" data-ru="CRITICAL: ... HIGH: ..." data-en="CRITICAL: ... HIGH: ..."></textarea>
    <div class="btn-group">
      <button class="btn btn-outline" onclick="toggleSolution('sol-l35-2')" data-ru="Показать решение" data-en="Show solution">Yechimni ko'rish</button>
    </div>
    <div class="solution-box" id="sol-l35-2" hidden>
      <h4 data-ru="Эталонное решение" data-en="Reference solution">Etalon yechim</h4>
      <pre>CRITICAL: lodash &lt; 4.17.21 → prototype pollution.
  Путь: express → lodash. Фикс: npm audit fix.
HIGH: minimist &lt; 1.2.6 → prototype pollution.
  Фикс: обновить зависимость, проверить тесты.

npm audit fix --force может поставить major-версию
и сломать API — сначала читаем отчёт и тесты.</pre>
    </div>
  </div>

  <div class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="Уровень 3 · Челлендж" data-en="Tier 3 · Challenge">3-Daraja · Kiber-Chaqiruv</span>
      <span class="task-score">2 BALL</span>
    </div>
    <h3 data-ru="Сценарий атаки на цепочку поставок" data-en="Supply-Chain Attack Scenario">Ta'minot Zanjiriga Hujum Ssenariysi</h3>
    <p data-ru="Опишите пошагово, как typosquatting и postinstall-скрипт могут украсть .env. Затем предложите три конкретные защиты и проверьте, какая из них блокирует атаку на каждом шаге." data-en="Describe step by step how typosquatting and a postinstall script could steal .env. Then propose three concrete defenses and check which one blocks the attack at each step.">Typosquatting va postinstall skripti .env ni qanday o'g'irlashini bosqichma-bosqich yozing. So'ng uchta aniq himoyani taklif qiling va qaysi biri har bir qadamda hujumni bloklashini tekshiring.</p>
    <textarea class="answer-area" rows="10" data-ru="1. Атакующий публикует ..." data-en="1. The attacker publishes ..."></textarea>
    <div class="btn-group">
      <button class="btn btn-outline" onclick="toggleSolution('sol-l35-3')" data-ru="Показать решение" data-en="Show solution">Yechimni ko'rish</button>
    </div>
    <div class="solution-box" id="sol-l35-3" hidden>
      <h4 data-ru="Эталонное решение" data-en="Reference solution">Etalon yechim</h4>
      <pre>1. Атакующий публикует crossenv (опечатка cross-env).
2. Разработчик ставит пакет: срабатывает postinstall.
3. Скрипт читает .env и отправляет токены на C2.

Защита:
- Проверка имени, загрузок и репозитория пакета.
- npm ci --ignore-scripts для пакетов без сборки.
- CI-секреты вне .env + npm audit --audit-level=high.</pre>
    </div>
  </div>
""",
}


def fill_template(path, mapping):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    for key, value in mapping.items():
        text = text.replace("{{" + key + "}}", value)
    leftovers = set()
    import re
    for match in re.finditer(r"\{\{[A-Z0-9_]+\}\}", text):
        leftovers.add(match.group(0))
    if leftovers:
        raise RuntimeError(f"{path}: unresolved placeholders {sorted(leftovers)}")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("filled", path)


def main():
    for cohort, lesson, data in (
        ("10-11-sinf", "31-dars-vision-agentlar-va-computer-use", L31),
        ("9-sinf", "35-dars-npm-ekotizimi-va-xavfsizlik-auditi", L35),
    ):
        base = os.path.join(REPO_ROOT, "classes", cohort, "12-hafta", lesson)
        fill_template(os.path.join(base, "varaqa.html"), data)
        fill_template(os.path.join(base, "vazifa.html"), data)


if __name__ == "__main__":
    main()
