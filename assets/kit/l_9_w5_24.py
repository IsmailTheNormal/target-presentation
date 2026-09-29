# -*- coding: utf-8 -*-
"""9-sinf · 5-hafta · 24-dars — Autentifikatsiya, JWT va 2FA: Xavfsiz Sessiyalar va Ikki Bosqichli Himoya."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/9-sinf/5-hafta/24-dars-autentifikatsiya-jwt-va-2fa"

TITLES = {
    "uz": "24-dars: Autentifikatsiya, JWT va 2FA — Xavfsiz Sessiyalar",
    "ru": "Урок 24: Аутентификация, JWT и 2FA — Защищённые Сессии",
    "en": "Lesson 24: Authentication, JWT & 2FA — Resilient Session Defense",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("CyberSecurity · 24-dars · 9-sinf (Identity & Auth Track)",
             "CyberSecurity · Урок 24 · 9 класс (Identity & Auth Track)",
             "CyberSecurity · Lesson 24 · Grade 9 (Identity & Auth Track)"),
    h1=("Autentifikatsiya, JWT va 2FA Himoyasi",
        "Аутентификация, JWT и Двухфакторная Защита (2FA)",
        "Modern Authentication, JWT Architecture & 2FA"),
    lede=("Parol kiritish — bu xavfsizlikning faqat birinchi va eng zaif qadami. Agar login tizimi xato qurilgan bo'lsa, "
          "xakerlar sizning parolingizni bilmasdan ham butun hisobingizni o'g'irlashi (Session Hijacking) mumkin. "
          "Zamonaviy bulutli tizimlarda identifikatsiyani tasdiqlash uchun <b>JSON Web Token (JWT)</b> va "
          "<b>Ikki bosqichli autentifikatsiya (2FA/TOTP)</b> qo'llaniladi. "
          "Bugungi darsda siz JWT ning kriptografik imzo mexanizmini, tokenlarni qayerda saqlash xavfsizligini "
          "va Google Authenticator qanday qilib internetsiz ham har 30 soniyada yangi 6 xonali kod yaratishini o'rganasiz.",
          "Ввод пароля — лишь первый и самый ненадежный рубеж защиты. При ошибках в архитектуре сессий "
          "злоумышленник может захватить ваш аккаунт без знания пароля. "
          "Современные системы используют криптографические токены <b>JSON Web Token (JWT)</b> и "
          "двухфакторную аутентификацию <b>2FA (TOTP)</b>. "
          "Сегодня вы разберёте цифровую подпись JWT, безопасное хранение в куках и математику работы Google Authenticator.",
          "Submitting a password is only the first and weakest line of identity defense. Flawed session architectures allow "
          "adversaries to hijack authenticated accounts without ever learning credentials. "
          "Modern enterprise platforms rely on <b>JSON Web Tokens (JWT)</b> and <b>Two-Factor Authentication (2FA/TOTP)</b>. "
          "Today you will master cryptographic JWT signatures, safe cookie storage strategies, "
          "and the offline mathematical algorithm powering Google Authenticator every 30 seconds."),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · Identity & Access Security",
           "<b>Предмет:</b> Кибербезопасность · Безопасность Идентификации",
           "<b>Subject:</b> CyberSecurity · Identity & Access Security"),
          ("<b>Kohorta:</b> 9-sinf Kiber-Muhandis",
           "<b>Когорта:</b> 9 класс Кибер-Инженер",
           "<b>Cohort:</b> Grade 9 Cyber-Engineer"),
          ("<b>Hafta:</b> 5 (4-soat)", "<b>Неделя:</b> 5 (4-й час)", "<b>Week:</b> 5 (Hour 4)")],
))

# 2. Authentication vs Authorization
S.append(slide(
    ph=("Konsepsiya", "Концепция", "Core Concepts"), time="3–6",
    eyebrow=("Asosiy tushunchalar", "Фундаментальные понятия", "Foundational Concepts"),
    title=("Autentifikatsiya vs Avtorizatsiya: 401 vs 403 Farqi",
           "Аутентификация против Авторизации: Разница 401 и 403",
           "Authentication vs Authorization: Dissecting 401 vs 403"),
    body='<div class="cols c2">\n'
         + box("accent", ("1. Autentifikatsiya (Authentication - 401)", "1. Аутентификация (401)", "1. Authentication (Who are you?)"),
               items=[
                   ("<b>Savol:</b> <i>\"Siz kimsiz? O'z shaxsingizni isbotlang!\"</i>",
                    "<b>Вопрос:</b> <i>«Кто вы? Докажите свою личность!»</i>",
                    "<b>Question:</b> <i>\"Who are you? Prove your identity!\"</i>"),
                   ("Login, Parol, Biometrika (Face ID, Barmoq izi), 2FA kod kiritish jarayoni.",
                    "Ввод логина, пароля, биометрии (Face ID) или одноразового кода 2FA.",
                    "Submitting credentials, biometrics, or dynamic 2FA tokens."),
                   ("Agar tasdiqlanmasa: <b>HTTP 401 Unauthorized</b> (Tizim sizni tanimadi).",
                    "При ошибке: <b>HTTP 401 Unauthorized</b> (Сервер вас не узнал).",
                    "Rejection outcome: <b>HTTP 401 Unauthorized</b> (Identity unverified)."),
               ])
         + box("purple", ("2. Avtorizatsiya (Authorization - 403)", "2. Авторизация (403)", "2. Authorization (What can you do?)"),
               items=[
                   ("<b>Savol:</b> <i>\"Siz tanildingiz, lekin bu amalga haqqingiz bormi?\"</i>",
                    "<b>Вопрос:</b> <i>«Вы опознаны, но имеете ли право на это действие?»</i>",
                    "<b>Question:</b> <i>\"Identity verified, but do you have permission?\"</i>"),
                   ("Foydalanuvchi roli: Oddiy talaba admin sahifasini o'chira olmasligi kerak.",
                    "Проверка прав: Обычный ученик не имеет права удалять базу данных школы.",
                    "Role enforcement: Regular student cannot delete database or change scores."),
                   ("Agar ruxsat bo'lmasa: <b>HTTP 403 Forbidden</b> (Siz kirdingiz, lekin taqiqlangan!).",
                    "При ошибке: <b>HTTP 403 Forbidden</b> (Вы опознаны, но доступ запрещён!).",
                    "Rejection outcome: <b>HTTP 403 Forbidden</b> (Identity valid, rights denied)."),
               ])
         + '\n</div>'
))

# 3. Anatomy of a JWT Token
S.append(slide(
    ph=("JWT Anatomiyasi", "Анатомия JWT", "JWT Architecture"), time="6–10",
    eyebrow=("Kriptografik token", "Криптографический токен", "Stateless Token Architecture"),
    title=("JSON Web Token (JWT) Anatomiyasi: 3 Ta Qism",
           "Анатомия JSON Web Token: 3 Составные Части",
           "The Tripartite Anatomy of a JSON Web Token"),
    body='<div class="cols c3">\n'
         + box("accent", ("1. Header (Qizil)", "1. Заголовок (Header)", "1. Header (Algorithm)"),
               p=("Token turi va ishlatilgan shifrlash algoritmi (masalan, HMAC-SHA256 yoki RSA):<br><br><code>{\n  \"alg\": \"HS256\",\n  \"typ\": \"JWT\"\n}</code>",
                  "Тип токена и алгоритм подписи (например, HS256):<br><br><code>{\n  \"alg\": \"HS256\",\n  \"typ\": \"JWT\"\n}</code>",
                  "Defines token metadata and signing algorithm (e.g. HS256):<br><br><code>{\n  \"alg\": \"HS256\",\n  \"typ\": \"JWT\"\n}</code>"))
         + box("purple", ("2. Payload (Binafsha)", "2. Полезная Нагрузка (Payload)", "2. Payload (Claims)"),
               p=("Foydalanuvchi ma'lumotlari (ID, ism, rol, amal qilish muddati <code>exp</code>):<br><br><code>{\n  \"sub\": \"user_42\",\n  \"role\": \"admin\",\n  \"exp\": 1769850000\n}</code>",
                  "Данные пользователя (ID, роли, срок жизни `exp`):<br><br><code>{\n  \"sub\": \"user_42\",\n  \"role\": \"admin\",\n  \"exp\": 1769850000\n}</code>",
                  "Embedded claims (user ID, permissions, expiration epoch):<br><br><code>{\n  \"sub\": \"user_42\",\n  \"role\": \"admin\",\n  \"exp\": 1769850000\n}</code>"))
         + box("green", ("3. Signature (Yashil)", "3. Цифровая Подпись (Signature)", "3. Cryptographic Signature"),
               p=("Serverdagi maxfiy kalit bilan hisoblangan imzo. <b>Agar xaker bitta harfni o'zgartirsa, imzo buziladi va token rad etiladi!</b>",
                  "Подпись, вычисленная секретным ключом сервера. Любая попытка подделать роль ломает подпись!",
                  "HMAC-SHA256 signature generated with server secret. Any tampering instantly invalidates verification!"))
         + '\n</div>'
))

# 4. Where to Store JWT: The Great Security Debate
S.append(slide(
    ph=("Saqlash Xavfsizligi", "Хранение Токена", "Storage Security"), time="10–14",
    eyebrow=("LocalStorage vs Cookie", "LocalStorage против Cookie", "LocalStorage vs Cookie"),
    title=("Katta Xavfsizlik Bahsi: JWT Qayerda Saqlanishi Kerak?",
           "Большой Спор: Где Безопасно Хранить JWT?",
           "The Storage Debate: LocalStorage vs HttpOnly Cookies"),
    body='<div class="cols c2">\n'
         + box("accent", ("❌ LocalStorage (Juda Xavfli!)", "❌ LocalStorage (Опасно!)", "❌ LocalStorage (Critical Vulnerability)"),
               items=[
                   ("<b>XSS ga o'ta zaif:</b> Saytdagi istalgan uchinchi tomon scripti yoki XSS zaifligi <code>localStorage.getItem('token')</code> qilib tokenni o'g'irlay oladi.",
                    "<b>Уязвимо для XSS:</b> Любой скрипт XSS крадёт токен через `localStorage.getItem('token')`.",
                    "<b>Trivially Stolen by XSS:</b> Any malicious script executes `localStorage.getItem('token')` and transmits it."),
                   ("Token o'g'irlansa, xaker foydalanuvchi hisobiga to'liq ega bo'ladi.",
                    "Украденный токен даёт взломщику полный контроль над сессией.",
                    "Exfiltrated bearer tokens grant total persistent session control."),
               ])
         + box("green", ("✅ HttpOnly & Secure Cookie (Sanoat Standarti)", "✅ HttpOnly Cookie (Индустриальный Стандарт)", "✅ HttpOnly & Secure Cookie (Gold Standard)"),
               items=[
                   ("<b>JavaScript o'qiy olmaydi:</b> <code>httpOnly: true</code> belgilangan cookie brauzer konsoli va JS ga ko'rinmaydi.",
                    "<b>Недоступно для JS:</b> Флаг `httpOnly: true` блокирует чтение через `document.cookie`.",
                    "<b>JavaScript Blind:</b> `httpOnly: true` flag strictly denies DOM read access."),
                   ("<b>Avtomatik yuboriladi:</b> Brauzer har bir so'rovda tokenni o'zi xavfsiz headerda serverga uzatadi.",
                    "<b>Автопередача:</b> Браузер сам передает куки на сервер в защищенном заголовке.",
                    "<b>Automatic transmission:</b> Browser securely manages payload transmission."),
                   ("<b>CSRF dan himoya:</b> <code>sameSite: 'strict'</code> flagi begonalar soxta so'rov yuborishini to'xtatadi.",
                    "<b>Защита от CSRF:</b> Флаг `sameSite: 'strict'` блокирует атаки подделки запросов.",
                    "<b>CSRF immunity:</b> `sameSite: 'strict'` blocks unauthorized cross-site requests."),
               ])
         + '\n</div>'
))

# 5. Token Rotation: Access vs Refresh Token
S.append(slide(
    ph=("Rotatsiya", "Ротация Токенов", "Token Rotation"), time="14–18",
    eyebrow=("Qisqa umrli tokenlar", "Короткоживущие токены", "Dual-Token Architecture"),
    title=("Access Token va Refresh Token Rotatsiyasi",
           "Архитектура Access и Refresh Токенов",
           "Dual-Token Architecture: Access & Refresh Token Rotation"),
    body='<div class="cols c2">\n'
         + box("", ("Ikki Tokenli Tizim Mexanikasi", "Механика Двойного Токена", "Dual-Token Lifecycle"),
               items=[
                   ("<b>Access Token:</b> Qisqa umr ko'radi (masalan, <b>15 daqiqa</b>). Har bir API so'rovida yuboriladi.",
                    "<b>Access Token:</b> Живёт всего <b>15 минут</b>. Передаётся с каждым запросом к API.",
                    "<b>Access Token:</b> Ephemeral lifetime (<b>15 minutes</b>). Authenticates daily API calls."),
                   ("<b>Refresh Token:</b> Uzoq umr ko'radi (<b>7 kun</b>). Faqat yangi Access token olish uchun ishlatiladi.",
                    "<b>Refresh Token:</b> Живёт <b>7 дней</b>. Используется только для выпуска нового Access Token.",
                    "<b>Refresh Token:</b> Long-lived (<b>7 days</b>). Strictly limited to minting fresh access tokens."),
                   ("<b>Rotatsiya:</b> Har safar Refresh ishlatilganda, eski Refresh o'chiriladi va yangisi beriladi.",
                    "<b>Ротация:</b> При каждом обновлении старый Refresh аннулируется.",
                    "<b>Rotation:</b> Single-use refresh token; consumed tokens are instantly invalidated."),
               ])
         + '<div class="box accent">\n'
         + el("h3", "Tokenni Tekshirish Kiber-Mantiqiy K獻i", "Проверка Токена в Express.js", "Express.js JWT Middleware")
         + code("""// Xavfsiz Middleware: Tokenni tekshirish
function verifyAuth(req, res, next) {
    const token = req.cookies.access_token;
    if (!token) return res.status(401).json({ error: 'Kirish rad etildi' });

    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
        if (err) return res.status(403).json({ error: 'Yaroqsiz token' });
        req.user = user;
        next();
    });
}""")
         + '</div>\n</div>'
))

# 6. Two-Factor Authentication (2FA / TOTP)
S.append(slide(
    ph=("2FA Mexanikasi", "Механика 2FA", "2FA & TOTP"), time="18–22",
    eyebrow=("RFC 6238 standarti", "Стандарт RFC 6238", "RFC 6238 Standard"),
    title=("2FA Qanday Ishlaydi? TOTP Algoritmining Sirlari",
           "Как Работает 2FA? Секреты Алгоритма TOTP",
           "How 2FA Works: Mathematics of Time-Based One-Time Passwords"),
    body='<div class="cols c3">\n'
         + box("purple", ("1. Umumiy Maxfiy Kalit (Shared Secret)", "1. Общий Секрет (Shared Secret)", "1. Shared Secret"),
               p=("2FA yoqilganda server QR kod ko'rsatadi. Bu QR kod ichida <b>maxfiy matn (Secret Key)</b> yashiringan. Telefon kamerasi uni o'qib, o'zida saqlaydi.",
                  "При настройке 2FA сервер показывает QR-код с общим секретным ключом. Приложение считывает и сохраняет его.",
                  "Server issues a QR code embedding a cryptographic secret key. Mobile authenticator scans and securely stores it."))
         + box("accent", ("2. Vaqt Bloki (30 Soniyalik Oyna)", "2. Временное Окно (30 Секунд)", "2. 30-Second Time Epoch"),
               p=("Telefon va server Unix vaqtini oladi va 30 ga bo'ladi: <code>T = Math.floor(UnixVaqt / 30)</code>. Har 30 soniyada T soni 1 taga oshadi.",
                  "Оба устройства берут текущее Unix-время и делят на 30. Каждые 30 секунд счётчик времени увеличивается на единицу.",
                  "Both endpoints divide current Unix epoch by 30: <code>T = floor(Epoch / 30)</code>. Step increments every 30 seconds."))
         + box("green", ("3. HMAC Hash -> 6 Xonali Kod", "3. Хэш HMAC -> 6 Цифр", "3. HMAC Truncation"),
               p=("Secret va T soni <b>HMAC-SHA1</b> algoritmi bilan xeshlanadi va 6 xonali qisqa kod olinadi. <b>Internetsiz ham telefon va serverda bir xil kod chiqadi!</b>",
                  "Секрет и счетчик хэшируются через HMAC-SHA1. И телефон, и сервер без интернета получают одинаковый 6-значный код!",
                  "HMAC-SHA1 hashes secret with time step, truncated to 6 digits. Phone and server compute identical codes offline!"))
         + '\n</div>'
))

# 7. MFA Fatigue Attack
S.append(slide(
    ph=("Hujum Tahlili", "Атака на 2FA", "MFA Attacks"), time="22–26",
    eyebrow=("2FA ni aldash yo'llari", "Обход двухфакторной защиты", "Bypassing Multi-Factor"),
    title=("MFA Fatigue: Xakerlar 2FA Ni Qanday Aylanib O'tadi?",
           "MFA Fatigue: Как Хакеры Обходят Двухфакторку?",
           "MFA Fatigue & Push Bombing: Exploiting Human Weakness"),
    body='<div class="cols c2">\n'
         + box("accent", ("MFA Fatigue (Push Bombing) Hujumi", "Атака Push Bombing", "Push Bombing Mechanics"),
               items=[
                   ("Xaker xodimning parolini o'g'irlaydi, lekin 2FA to'sig'iga duch keladi.",
                    "Взломщик узнаёт пароль сотрудника, но упирается в запрос 2FA.",
                    "Adversary compromises password but hits MFA push notification prompt."),
                   ("Xaker kechasi soat 03:00 da har 2 soniyada telefonga 2FA tasdiq so'rovini yuboradi (100+ push).",
                    "В 3 часа ночи хакер бомбардирует телефон жертвы сотнями пуш-уведомлений.",
                    "Attacker generates 100+ consecutive MFA push notifications at 3:00 AM."),
                   ("Uyqusiragan xodim telefon jiringlashini to'xtatish uchun tasodifan <b>'Ha, bu men'</b> tugmasini bosadi!",
                    "Уставший сотрудник нажимает «Одобрить», чтобы телефон перестал вибрировать!",
                    "Fatigued employee clicks 'Approve' to silence continuous notifications!"),
               ])
         + '<div class="box green">\n'
         + el("h3", "Zamonaviy Yechim: Number Matching (Fido2)", "Современное Решение", "Remediation: Number Matching") + "\n"
         + el("p", "Oddiy 'Ha/Yo'q' tugmalari o'rniga, ekranda 2 xonali tasodifiy raqam (masalan, <b>47</b>) ko'rsatiladi. Foydalanuvchi ushbu raqamni telefoniga o'zi qo'lda kiritishi shart. Bu tasodifiy bosishlarni 100% to'xtatadi!",
              "Вместо простой кнопки 'Одобрить' экран показывает 2-значное число (например, 47), которое нужно вручную ввести в телефон.",
              "Instead of binary 'Approve' prompts, modern auth presents a random challenge number (e.g. 47) that must be typed manually on mobile authenticator.") + "\n"
         + '</div>\n</div>'
))

# 8. Real-World Case Study: Uber Breach
S.append(slide(
    ph=("Real Keys", "Кейс из Жизни", "Case Study"), time="26–30",
    eyebrow=("2022-yilgi mashhur xakerlik", "Громкий взлом 2022 года", "The 2022 Uber Breach"),
    title=("Uber Kiber-Halokati: 18 Yoshli Xaker va MFA Fatigue",
           "Взлом Uber: 18-летний Хакер и Атака MFA Fatigue",
           "The 2022 Uber Cyber Breach: MFA Fatigue in Practice"),
    body='<div class="cols c2">\n'
         + box("accent", ("Uber Qanday Buzildi?", "Хроника Взлома Uber", "Uber Attack Chronology"),
               p=("2022-yilda 18 yoshli kiber-hujumchi (Lapsus$ guruhi) Uber xodimining parolini Darknetdan sotib oldi. Xodimning telefoniga tinimsiz 2FA so'rovlari yuborildi va WhatsApp orqali o'zini IT yordam xizmati deb tanishtirib: <i>'Agar tasdiqlasangiz, so'rovlar to'xtaydi'</i> deb aldadi. Xodim tasdiqlagach, xaker butun Uber ichki tarmog'iga, Slack va AWS hisoblariga ega bo'ldi.",
                  "В 2022 году 18-летний подросток из Lapsus$ купил пароль инженера Uber в даркнете, засыпал его пуш-запросами 2FA и в WhatsApp убедил подтвердить вход. Получив доступ, хакер захватил внутренний Slack, AWS и репозитории кода компании.",
                  "In 2022, an 18-year-old hacker purchased an Uber contractor's password, bombarded him with MFA push notifications, and persuaded him via WhatsApp IT support impersonation to accept. The breach exposed Uber's AWS, Slack, and code repositories."))
         + box("purple", ("Asosiy Xulosa", "Главный Вывод", "Strategic Takeaway"),
               items=[
                   ("<b>Texnologiya inson omiliga bog'liq:</b> Eng mukammal 2FA ham inson aldansa ojiz qolishi mumkin.",
                    "<b>Человеческий фактор:</b> Любая система безопасности уязвима перед социальной инженерией.",
                    "<b>Social engineering bypass:</b> The strongest crypto fails if human operators are tricked."),
                   ("<b>FIDO2 / Hardware Security Keys (YubiKey):</b> SMS va oddiy Push o'rniga jismoniy USB kalitlar eng ishonchli himoyadir.",
                    "<b>Аппаратные ключи FIDO2 (YubiKey):</b> Физические ключи делают фишинг и MFA Fatigue невозможными.",
                    "<b>Hardware FIDO2 Security Keys:</b> Physical security tokens eliminate MFA fatigue completely."),
               ])
         + '\n</div>'
))

# 9. Practical Mission (12 min timer)
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-On Lab"), time="30–42",
    eyebrow=("Mustaqil laboratoriya · 12 daqiqa", "Лабораторная работа · 12 минут", "Practical Lab · 12 Minutes"),
    title=("Amaliy Topshiriq: JWT Tahlili va TOTP 2FA Simulyatsiyasi",
           "Практическое Задание: Анализ JWT и Симуляция 2FA",
           "Mission: Dissecting JWT Signatures & Simulating 2FA TOTP"),
    body='<div class="cols c2">\n'
         + box("green", ("Laboratoriya Bosqichlari", "Шаги Лабораторной", "Mission Checkpoints"),
               items=[
                   ("<b>1. JWT Dekodlash:</b> jwt.io saytida yoki Node.js da namunaviy tokenni Header, Payload va Signature ga ajrating.",
                    "<b>1. Декодирование JWT:</b> Разберите токен на Header, Payload и Signature на jwt.io.",
                    "<b>1. Decode JWT:</b> Dissect bearer token into Header, Payload, and Signature components."),
                   ("<b>2. Imzo soxtalashtirish testi:</b> Payload dagi `role: 'user'` ni `role: 'admin'` ga o'zgartiring va imzo buzilganini ko'ring.",
                    "<b>2. Проверка подписи:</b> Измените роль на admin и убедитесь в невалидности подписи.",
                    "<b>2. Tamper verification:</b> Mutate payload to `role: 'admin'` and verify signature rejection."),
                   ("<b>3. TOTP Kodini hisoblash:</b> 30 soniyalik vaqt oynasi asosida 6 xonali 2FA kodini hisoblash formulasini sinang.",
                    "<b>3. Расчёт TOTP:</b> Проверьте генерацию 6-значного кода 2FA по формуле времени.",
                    "<b>3. TOTP derivation:</b> Verify dynamic 6-digit TOTP calculation from secret & time."),
                   ("<b>4. Xavfsiz Cookie sozlamasi:</b> Express.js da `httpOnly` va `sameSite` parametrlarini yozing.",
                    "<b>4. Настройка Cookie:</b> Задайте флаги `httpOnly` и `sameSite` в коде авторизации.",
                    "<b>4. Secure cookie flags:</b> Authorize session via `httpOnly` & `sameSite=Strict` options."),
               ])
         + box("accent", ("O'lchanadigan Natija", "Критерий Сдачи", "Deliverable Spec"),
               p=("Soxtalashtirilgan JWT token server tomonidan <b>\"403 Invalid Signature\"</b> bilan rad etilishi va 2FA kodi har 30 soniyada to'g'ri yangilanishini ko'rsatish!",
                  "Подтверждение отказа сервера <b>«403 Invalid Signature»</b> при модификации JWT и корректная генерация кодов 2FA каждые 30 секунд!",
                  "Verified server rejection <b>\"403 Invalid Signature\"</b> on modified token and successful 30-second TOTP synchronization!"))
         + '\n</div>'
))

# 10. Verification Checklist
S.append(slide(
    ph=("Tekshirish", "Чек-лист", "Verification"), time="42–43",
    eyebrow=("Xavfsizlik auditi", "Проверка защиты", "Security Audit"),
    title=("Autentifikatsiya Nazorat Cheklisti: 5 Ta Talab",
           "Чек-лист Безопасности Аутентификации",
           "Authentication Security Verification Checklist"),
    body='<div class="cols c3">\n'
         + box("", ("1. JWT Maxfiy Kalit", "1. Секрет JWT", "1. Secret Entropy"),
               p=("`JWT_SECRET` kamida 256-bitli tasodifiy murakkab kalitmi?",
                  "Используется ли надежный 256-битный секрет в `.env`?",
                  "Is `JWT_SECRET` high-entropy random 256-bit string?"))
         + box("", ("2. Token Saqlash", "2. Хранение Токена", "2. Token Storage"),
               p=("Token LocalStorage da emas, HttpOnly Cookie da saqlanmoqdami?",
                  "Токен хранится в HttpOnly Cookie, а не в LocalStorage?",
                  "Is token housed in HttpOnly cookie, avoiding LocalStorage?"))
         + box("", ("3. 2FA Vaqt Oynasi", "3. Окно 2FA", "3. 2FA Drift"),
               p=("TOTP kodi har 30 soniyada o'zgarishi tekshirildimi?",
                  "Меняется ли код 2FA каждые 30 секунд?",
                  "Does the TOTP token update strictly every 30 seconds?"))
         + '\n</div>'
))

# 11. Rubric (10-Ball)
S.append(slide(
    ph=("Mezon", "Критерии", "Evaluation"), time="43–44",
    eyebrow=("10 ballik tizim", "10-балльная шкала", "10-Point Rubric"),
    title=("Darsni Baholash Mezonlari (10 Ball)",
           "Критерии Оценки за Урок (10 Баллов)",
           "Lesson Evaluation Rubric (10 Points)"),
    body='<div class="cols c3">\n'
         + box("green", ("A'lo (9–10 Ball)", "Отлично (9–10)", "Exemplary (9–10)"),
               items=[
                   ("JWT tuzilishi va imzo himoyasi to'liq tushuntirilgan.", "Структура JWT и подпись разобраны полностью.", "JWT structure and signature defense mastered."),
                   ("LocalStorage vs HttpOnly farqi to'g'ri ko'rsatilgan.", "Разница LocalStorage и HttpOnly объяснена точно.", "LocalStorage vs HttpOnly trade-offs justified."),
                   ("2FA va TOTP algoritmi to'g'ri tahlil qilingan.", "Алгоритм 2FA TOTP рассчитан без ошибок.", "2FA & TOTP algorithm correctly computed."),
                   ("Varaqa 100% to'ldirilgan.", "Рабочий лист заполнен на 100%.", "Worksheet completed 100%."),
               ])
         + box("", ("Yaxshi (7–8 Ball)", "Хорошо (7–8)", "Proficient (7–8)"),
               items=[
                   ("JWT dekodlangan, lekin imzo soxtalashtirishda xato bor.", "JWT декодирован, но ошибка в тесте подписи.", "JWT decoded, minor flaws in signature testing."),
                   ("HttpOnly cookie afzalligi tushunilgan.", "Преимущества HttpOnly cookie поняты.", "HttpOnly cookie benefits understood."),
                   ("Varaqa 80% to'ldirilgan.", "Лист заполнен на 80%.", "Worksheet completed 80%."),
               ])
         + box("accent", ("Qoniqarli (5–6 Ball)", "Удовл. (5–6)", "Developing (5–6)"),
               items=[
                   ("Faqat JWT ko'rilgan, 2FA tushunarsiz qolgan.", "Разобран только JWT, 2FA не освоен.", "Only JWT reviewed, 2FA misunderstood."),
                   ("MFA Fatigue tushunchasi noaniq.", "Понятие MFA Fatigue не раскрыто.", "MFA Fatigue mechanics unclear."),
                   ("Varaqa to'liq emas.", "Лист заполнен частично.", "Worksheet incomplete."),
               ])
         + '\n</div>'
))

# 12. Summary & Homework
S.append(slide(
    ph=("Xulosa", "Итоги", "Summary"), time="44–45",
    eyebrow=("Uyga vazifa", "Домашнее задание", "Homework & Next Steps"),
    title=("Xulosa va Uy Vazifasi: Shaxsni Himoyalash",
           "Итоги и Домашнее Задание: Защита Личности",
           "Summary & Homework: Fortifying Digital Identities"),
    body='<div class="cols c2">\n'
         + box("purple", ("Dars Xulosasi", "Итоги Урока", "Core Summary"),
               p=("Xavfsiz autentifikatsiya — faqat parol bilan cheklanmaydi. Kriptografik imzolangan JWT, qisqa umrli Access Tokenlar, HttpOnly Cookielar va internetsiz ishlaydigan TOTP 2FA zamonaviy xavfsizlikning ajralmas poydevoridir.",
                  "Безопасная аутентификация выходит далеко за рамки пароля. Подписанный JWT, короткоживущие токены, HttpOnly cookie и 2FA TOTP — основа защиты современных систем.",
                  "Resilient authentication transcends simple passwords. Cryptographically signed JWTs, short-lived access tokens, HttpOnly cookies, and offline TOTP 2FA constitute the cornerstone of enterprise security."))
         + box("accent", ("Uy Vazifasi (10 Ball)", "Домашнее Задание (10 Баллов)", "Homework Assignment (10 Pts)"),
               items=[
                   ("<b>Amaliy:</b> O'z shaxsiy hisoblaringizda (Google, GitHub, Telegram) 2FA ni yoqing va zaxira kodlarini xavfsiz saqlang.",
                    "<b>Практика:</b> Включите 2FA на своих аккаунтах (GitHub, Google, Telegram) и сохраните бэкап-коды.",
                    "<b>Hands-on:</b> Enable 2FA on your accounts (GitHub, Google, Telegram) and secure backup keys."),
                   ("<b>Tahlil:</b> Nega SMS orqali 2FA kod olish (SIM swapping xavfi tufayli) ilova (Google Auth) orqali olishdan xavfliroq ekanini yozma asoslang.",
                    "<b>Анализ:</b> Опишите, почему 2FA через SMS опаснее приложений-аутентификаторов (риск SIM-swapping).",
                    "<b>Analysis:</b> Explain in writing why SMS-based 2FA is vulnerable to SIM-swapping compared to TOTP."),
                   ("<b>Varaqa:</b> Ish varaqasidagi barcha topshiriqlarni to'ldirib topshiring.",
                    "<b>Лист:</b> Заполните и сдайте печатный рабочий лист.",
                    "<b>Submission:</b> Complete and submit your printable lab worksheet."),
               ])
         + '\n</div>'
))

# Teacher Notes
N_UZ = [
    ["Kirish", "Darsni boshlash: Autentifikatsiya va 2FA mavzusi. Nega oddiy parol endi yetarli emas?", "Slaydni oching, sessiya tokenlari qanday ishlashini tushuntiring."],
    ["Konsepsiya", "Autentifikatsiya vs Avtorizatsiya: 401 va 403 farqi. Talaba va direktor huquqlari misolida.", "Misol keltiring: Talaba kimligini isbotladi (401 o'tdi), lekin direktor kabinetiga kirolmaydi (403)."],
    ["JWT Anatomiyasi", "JWT ning uch qismi: Header, Payload, Signature. Ranglar bilan ajratib ko'rsatish.", "jwt.io saytini ekranda ochib, jonli token qismlarini ko'rsating."],
    ["Saqlash Xavfsizligi", "LocalStorage va HttpOnly Cookie farqi. Nega LocalStorage XSS orqali o'g'irlanadi?", "LocalStorage xavfini ko'rsatib, HttpOnly flagini tushuntiring."],
    ["Rotatsiya", "Access va Refresh tokenlar. Nega Access token atigi 15 daqiqa yashashi kerak?", "Muddati o'tgan tokenning qanday yangilanishini chizib bering."],
    ["2FA Mexanikasi", "TOTP 2FA qanday ishlashi. Qanday qilib telefon internetsiz ham server bilan bir xil kod chiqaradi?", "Unix vaqti va 30 soniyalik qadam formulasi."],
    ["Hujum Tahlili", "MFA Fatigue (Push Bombing) nima? Inson psixologiyasidan foydalanish.", "Kechasi kelgan 100 ta xabarnoma keysini aytib bering."],
    ["Real Keys", "Uber kiber-halokati 2022. 18 yoshli xakerning Uber tarmog'ini qanday buzgani.", "Kompaniyalar xavfsizlik madaniyati haqida xulosa qiling."],
    ["Amaliyot", "12 daqiqalik laboratoriya. O'quvchilar JWT ni tahlil qiladilar va imzo soxtalashtirishni sinaydilar.", "Taymerni yoqing (12 daqiqa), o'quvchilarga yordam bering."],
    ["Tekshirish", "Nazorat tekshiruvi. Token imzosining buzilganini tasdiqlash.", "Natijalarni tekshiring."],
    ["Mezon", "10 ballik baholash mezoni tushuntiriladi.", "Talablarni eslatib o'ting."],
    ["Xulosa", "Dars yakuni va uy vazifasi. Kelgusi darsda CTF Kiber-Jang va Red/Blue team mudofaasini o'rganamiz!", "Varaqalarni yig'ing."]
]

N_RU = [
    ["Введение", "Старт урока: Почему обычного пароля уже недостаточно в современной безопасности.", "Откройте слайд, введите концепцию цифровой идентификации."],
    ["Концепция", "Аутентификация против Авторизации: разница между 401 и 403 кодами.", "Приведите пример с паспортом и пропуском в закрытую зону."],
    ["Анатомия JWT", "Разбор JWT: Header, Payload, Signature. Как цифровая подпись защищает токен.", "Продемонстрируйте jwt.io на проекторе."],
    ["Хранение Токена", "LocalStorage против HttpOnly Cookie. Почему токены нельзя хранить в LocalStorage.", "Объясните недоступность HttpOnly для вредоносных скриптов XSS."],
    ["Ротация Токенов", "Access и Refresh токены: ротация ключей и минимизация рисков компрометации.", "Объясните 15-минутный жизненный цикл Access токена."],
    ["Механика 2FA", "Алгоритм TOTP: генерация кодов на основе времени без подключения к сети.", "Разберите формулу T = floor(Epoch / 30)."],
    ["Атака на 2FA", "Атака MFA Fatigue (Push Bombing): психологическое давление на пользователя.", "Поясните уязвимость перед социальной инженерией."],
    ["Кейс из Жизни", "Кейс Uber 2022 года: как подросток обошёл 2FA через MFA Fatigue.", "Обсудите важность внедрения FIDO2 и аппаратных ключей."],
    ["Практика", "12 минут практики: разбор JWT, модификация роли и симуляция проверки 2FA.", "Запустите таймер, контролируйте корректность выполнения."],
    ["Проверка", "Чек-лист проверки: подтверждение ошибки 403 при подмене токена.", "Проверьте экраны учеников."],
    ["Критерии", "10-балльная шкала оценивания практической работы.", "Озвучьте правила начисления баллов."],
    ["Итоги", "Завершение урока и домашнее задание. На следующем занятии — CTF игра Red vs Blue Team!", "Соберите рабочие листы."]
]

N_EN = [
    ["Intro", "Lesson opening: Why passwords alone are defunct in zero-trust architectures.", "Introduce cryptographically attested sessions."],
    ["Core Concepts", "Authentication vs Authorization: Dissecting 401 Unauthorized vs 403 Forbidden.", "Analogize passport identity check vs security badge clearance."],
    ["JWT Architecture", "JWT anatomy: Header, Payload, Signature. How cryptographic HMAC prevents tampering.", "Live walkthrough on jwt.io debugger."],
    ["Storage Security", "LocalStorage vs HttpOnly Cookie. Why LocalStorage is lethal under XSS.", "Highlight browser isolation of HttpOnly cookies."],
    ["Token Rotation", "Dual-token architecture: Ephemeral Access tokens vs rotated Refresh tokens.", "Diagram token refreshing sequence on whiteboard."],
    ["2FA & TOTP", "Mathematical mechanics of TOTP (RFC 6238): Generating offline synchronized codes.", "Derive time epoch formula T = floor(UnixTime / 30)."],
    ["MFA Attacks", "MFA Fatigue & Push Bombing: Exploiting alert exhaustion to breach accounts.", "Discuss modern mitigations like Number Matching."],
    ["Case Study", "The 2022 Uber breach: Dissecting an 18-year-old hacker's social engineering bypass of MFA.", "Analyze corporate access governance lessons."],
    ["Hands-On Lab", "12-minute lab: Dissecting JWT signatures and testing tampered role payloads.", "Start 12-minute countdown timer and support students."],
    ["Verification", "Audit checklist: Confirming signature rejection upon payload tampering.", "Verify terminal console output."],
    ["Evaluation", "10-point evaluation rubric breakdown.", "Review grading thresholds."],
    ["Summary", "Wrap-up and homework preview. Next session: CTF Cyber Defense & Red/Blue Team battle!", "Collect worksheets."]
]

NOTES = {"uz": N_UZ, "ru": N_RU, "en": N_EN}

# ---------------------------------------------------------------- Varaqa Body
V = []
V.append(sheet_header(
    h1=("Kiberxavfsizlik: Autentifikatsiya va JWT",
        "Кибербезопасность: Аутентификация и JWT",
        "CyberSecurity: Authentication & JWT Defense"),
    sub=("Amaliy Laboratoriya Varaqasi · 9-sinf · 5-hafta · 24-dars",
         "Практический Рабочий Лист · 9 класс · Неделя 5 · Урок 24",
         "Hands-On Lab Worksheet · Grade 9 · Week 5 · Lesson 24")
))

V.append(mission(
    h=("Laboratoriya Vazifasi: JWT Imzosi va 2FA Tahlili",
       "Миссия Лабораторной: Анализ JWT и Симуляция 2FA",
       "Lab Mission: JWT Signature Integrity & 2FA Analysis"),
    p=("JSON Web Token (JWT) ichki tuzilishini tahlil qilish, uning imzosini soxtalashtirishga urinib ko'rish, "
       "va Google Authenticator ilovasidagi 30 soniyalik TOTP algoritmining ishlash matematikasini sinash.",
       "Проанализировать внутреннюю структуру JWT, попытаться подделать роль в токене, "
       "и проверить математику работы 30-секундного алгоритма TOTP в Google Authenticator.",
       "Analyze the tripartite structure of a JWT, execute a payload tampering experiment to trigger signature rejection, "
       "and test the 30-second time-step mathematics of the TOTP 2FA algorithm."))
)

V.append(table(
    headers=[
        ("Xavfsizlik Bosqichi", "Этап Безопасности", "Security Phase"),
        ("Tahlil / Buyruq", "Команда / Действие", "Action / Inspection"),
        ("Kutilgan Natija", "Ожидаемый Результат", "Expected Outcome"),
        ("Holat", "Статус", "Status")
    ],
    rows=[
        [("1. JWT Dekodlash", "1. Декод JWT", "1. Decode JWT"),
         ("`jwt.decode(token)`", "`jwt.decode(token)`", "`jwt.decode(token)`"),
         ("Header, Payload va Signature ajratildi", "Токен разбит на 3 части", "Token split into 3 parts"),
         ("✅ Bajarildi", "✅ Выполнено", "✅ Completed")],
        [("2. Imzo Tekshirish", "2. Проверка Подписи", "2. Verify Signature"),
         ("Payload da `role: admin` qilish", "Подмена роли на admin", "Mutate payload to `role: admin`"),
         ("`Invalid Signature` xatosi bilan rad etildi", "Отказ: Недействительная подпись", "Rejected: Invalid Signature"),
         None],
        [("3. 2FA TOTP Hisobi", "3. Расчёт 2FA", "3. TOTP Computation"),
         ("`T = Math.floor(now / 30)`", "`T = Math.floor(now / 30)`", "`T = Math.floor(now / 30)`"),
         ("6 xonali dinamik kod hisoblandi", "Сгенерирован 6-значный код", "6-digit dynamic code computed"),
         None],
        [("4. HttpOnly Cookie", "4. HttpOnly Cookie", "4. HttpOnly Cookie"),
         ("`document.cookie` konsolda", "Чтение `document.cookie`", "`document.cookie` console read"),
         ("Token ko'rinmaydi (Bo'sh satr)", "Токен скрыт от JavaScript", "Token inaccessible to JavaScript"),
         None],
    ]
))

V.append(sheet_box(
    h=("Xavfsizlik Tahlili va Nazariy Savollar", "Анализ Безопасности и Вопросы", "Security Analysis & Written Queries"),
    body_html=writelines(3, label=("1. Nega JWT tokenni LocalStorage-da saqlash XSS hujumi oldida xavfli hisoblanadi?",
                                   "1. Почему хранение JWT в LocalStorage делает систему уязвимой для атак XSS?",
                                   "1. Why is storing JWTs in LocalStorage a severe vulnerability against XSS attacks?"))
             + "<br>"
             + writelines(3, label=("2. Google Authenticator internetsiz (samolyot rejimida) qanday qilib server bilan bir xil kod yaratadi?",
                                   "2. Как Google Authenticator без интернета (в режиме полёта) генерирует верные коды?",
                                   "2. How does Google Authenticator compute valid verification codes completely offline?"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("JWT qismlari va imzo himoyasi to'g'ri tahlil qilingan", "Структура JWT и цифровая подпись разобраны верно", "JWT anatomy and signature security analyzed"), "3 ball"),
        (("LocalStorage vs HttpOnly Cookie farqi asoslangan", "Обоснована разница между LocalStorage и HttpOnly", "LocalStorage vs HttpOnly trade-offs justified"), "3 ball"),
        (("2FA va TOTP algoritmining matematikasi to'g'ri ko'rsatilgan", "Продемонстрирован расчёт алгоритма 2FA TOTP", "2FA TOTP mathematical computation verified"), "2 ball"),
        (("Nazariy savollarga to'liq va asosli javob yozilgan", "Даны развернутые ответы на теоретические вопросы", "Written analytical queries answered thoroughly"), "2 ball"),
    ], "10 ball")
))

V.append("</div>\n" + sign_box("Musulmonov Mamarajab"))

VARAQA_BODY = "\n".join(V)

lesson = Lesson(
    outdir=D,
    titles=TITLES,
    sheet_titles=SHEET_TITLES,
    key="vc-notes-9-24",
    slides=S,
    notes=NOTES,
    varaqa_body=VARAQA_BODY
)

if __name__ == "__main__":
    out = lesson.build()
    print("Created:", out)
