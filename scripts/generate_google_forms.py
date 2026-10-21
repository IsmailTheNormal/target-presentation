#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Google Forms Generator
Avtomatik Google Forms (Quiz) yaratuvchi Google Apps Script (.gs) va interaktiv HTML vositasi.
"""

import json
import os
import re

QUIZ_DATA = [
    {
        "cohort_id": "9-sinf",
        "cohort_name": {
            "uz": "9-Sinf · Junior Vibecoders & Full-Stack",
            "ru": "9-Класс · Junior Vibecoders & Full-Stack",
            "en": "Grade 9 · Junior Vibecoders & Full-Stack"
        },
        "classes": ["9-A", "9-B"],
        "week_id": "8-hafta",
        "lesson_id": "28-dars-fullstack-xavfsiz-servis-oraliq-nazorat",
        "lesson_num": "28",
        "folder_path": "classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat",
        "title": {
            "uz": "9-Sinf: 28-Dars Full-Stack Xavfsiz Servis va CTF — Oraliq Nazorat Kiber-Testi",
            "ru": "9-Класс: Урок 28 Полностековый Безопасный Сервис и CTF — Рубежный Тест",
            "en": "Grade 9: Lesson 28 Full-Stack Secure Service & CTF — Midterm Security Quiz"
        },
        "description": {
            "uz": "Target International School // 9-Sinf // 1-Chorak Oraliq Nazorat Imtihoni\nMavzu: Express MVC, SQLite Relyatsion Sxema, JWT, XSS/CSRF va Docker Sandbox\nO'qituvchi: M. Musulmonov",
            "ru": "Target International School // 9-Класс // Рубежный контроль 1-й четверти\nТема: Express MVC, SQLite, JWT, защита от XSS/CSRF и Docker Sandbox\nУчитель: М. Мусульмонов",
            "en": "Target International School // Grade 9 // Quarter 1 Midterm Exam\nTopic: Express MVC, SQLite Relational Schema, JWT, XSS/CSRF Defense & Docker Sandbox\nInstructor: M. Musulmonov"
        },
        "questions": [
            {
                "id": "q1",
                "points": 3,
                "title": {
                    "uz": "Quyidagi Express server kodida qaysi kritik zaiflik mavjud?\n\napp.post('/api/profile', (req, res) => {\n  const query = \"UPDATE users SET bio = '\" + req.body.bio + \"' WHERE id = \" + req.user.id;\n  db.run(query);\n  res.send('<h1>Updated:</h1><div>' + req.body.bio + '</div>');\n});",
                    "ru": "Какая критическая уязвимость присутствует в следующем фрагменте кода Express?\n\napp.post('/api/profile', (req, res) => {\n  const query = \"UPDATE users SET bio = '\" + req.body.bio + \"' WHERE id = \" + req.user.id;\n  db.run(query);\n  res.send('<h1>Updated:</h1><div>' + req.body.bio + '</div>');\n});",
                    "en": "Which critical vulnerability exists in the following Express server snippet?\n\napp.post('/api/profile', (req, res) => {\n  const query = \"UPDATE users SET bio = '\" + req.body.bio + \"' WHERE id = \" + req.user.id;\n  db.run(query);\n  res.send('<h1>Updated:</h1><div>' + req.body.bio + '</div>');\n});"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Kritik zaiflik: bir vaqtning o'zida ham SQL Injection (satr qo'shish), ham Stored/Reflected XSS (sanitizatsiyasiz HTML) mavjud!",
                            "ru": "Критическая уязвимость: одновременный SQL Injection (конкатенация) и XSS (вывод без санитизации)!",
                            "en": "Critical vulnerability: simultaneous SQL Injection (string concatenation) and XSS (unsanitized HTML output)!"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Kod mutlaqo xavfsiz, chunki GET o'rniga POST metodi qo'llanilgan.",
                            "ru": "Код полностью безопасен, так как применен POST вместо GET.",
                            "en": "The code is completely secure because POST is used instead of GET."
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Yagona xato — Content-Type sarlavhasi yozilmaganligida.",
                            "ru": "Единственная ошибка — отсутствие заголовка Content-Type.",
                            "en": "The only flaw is the missing Content-Type header."
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Faqat server xotirasida (RAM) resurs yetishmovchiligi yuz beradi.",
                            "ru": "Произойдет только утечка оперативной памяти (RAM) на сервере.",
                            "en": "Only a memory leak (RAM exhaustion) will occur on the server."
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "To'g'ri! Satrlarni birlashtirish (' + req.body.bio + ') SQL Injection ochadi, to tozalanmagan matnni res.send() bilan qaytarish esa XSS xurujiga sabab bo'ladi.",
                    "ru": "Правильно! Конкатенация строк ведет к SQL Injection, а отправка несанитизированного ввода через res.send() создает XSS.",
                    "en": "Correct! String concatenation causes SQL Injection, and outputting unsanitized input via res.send() enables XSS."
                },
                "feedback_incorrect": {
                    "uz": "Xato. Bu yerda bir vaqtning o'zida ham SQL Injection, ham XSS xavfi mavjud. Parametrlangan so'rovlar (?) va DOMPurify/res.json ishlatilishi shart.",
                    "ru": "Неверно. Здесь присутствуют одновременно SQL Injection и XSS. Необходимо использовать параметризованные запросы (?) и санитизацию.",
                    "en": "Incorrect. Both SQL Injection and XSS are present. Parameterized queries (?) and sanitization via DOMPurify/res.json are required."
                }
            },
            {
                "id": "q2",
                "points": 2,
                "title": {
                    "uz": "SQLite relyatsion ma'lumotlar bazasida 'orders' jadvalidagi 'user_id' ustuniga nima uchun FOREIGN KEY cheklovi qo'yiladi?",
                    "ru": "Зачем в реляционной базе SQLite на столбец 'user_id' таблицы 'orders' накладывается ограничение FOREIGN KEY?",
                    "en": "Why is a FOREIGN KEY constraint applied to the 'user_id' column of the 'orders' table in an SQLite relational database?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Faqat mavjud bo'lgan foydalanuvchilar buyurtma bera olishini kafolatlash (Referential Integrity)",
                            "ru": "Гарантировать, что заказы могут создавать только существующие пользователи (Referential Integrity)",
                            "en": "To guarantee that only existing users can place orders (Referential Integrity)"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Foydalanuvchi parolini SHA-256 orqali avtomatik shifrlash uchun",
                            "ru": "Для автоматического шифрования паролей пользователей по SHA-256",
                            "en": "To automatically encrypt user passwords using SHA-256"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Server diskida fayl hajmini 50% gacha tejash uchun",
                            "ru": "Для уменьшения размера файла базы данных на диске на 50%",
                            "en": "To reduce database file size on disk by up to 50%"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Faqat SELECT so'rovlarini keshlab olish uchun",
                            "ru": "Исключительно для кэширования запросов SELECT",
                            "en": "Exclusively to cache SELECT queries"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "A'lo! FOREIGN KEY jadvallar o'rtasidagi bog'liqlik va referensial yaxlitlikni saqlaydi, mavjud bo'lmagan id ga buyurtma yozilishiga yo'l qo'ymaydi.",
                    "ru": "Отлично! Внешний ключ гарантирует ссылочную целостность между таблицами.",
                    "en": "Excellent! Foreign keys maintain referential integrity across related tables."
                },
                "feedback_incorrect": {
                    "uz": "Xato. FOREIGN KEY — ma'lumotlar bazasida referensial yaxlitlik (Referential Integrity) kafolatidir.",
                    "ru": "Неверно. Внешний ключ необходим для обеспечения ссылочной целостности данных.",
                    "en": "Incorrect. A foreign key enforces referential integrity across relational data."
                }
            },
            {
                "id": "q3",
                "points": 2,
                "title": {
                    "uz": "JWT (JSON Web Token) autentifikatsiyasida tokenni XSS skriptlaridan o'g'irlanishiga yo'l qo'ymaslik uchun eng xavfsiz saqlash usuli qaysi?",
                    "ru": "Какой способ хранения JWT токена наиболее безопасен против кражи через XSS атаки?",
                    "en": "Which storage mechanism is most secure for JWT tokens to prevent theft via XSS attacks?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Brauzer kuki faylida 'HttpOnly; Secure; SameSite=Strict' bayroqlari bilan saqlash",
                            "ru": "Хранить в cookies с флагами 'HttpOnly; Secure; SameSite=Strict'",
                            "en": "Storing inside cookies with 'HttpOnly; Secure; SameSite=Strict' flags"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Brauzerning LocalStorage xotirasida ochiq saqlash",
                            "ru": "Хранить в открытом виде в LocalStorage браузера",
                            "en": "Storing as plaintext inside browser LocalStorage"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Tokinni har bir URL manzilida query parametr (?token=...) sifatida uzatish",
                            "ru": "Передавать токен как GET query параметр (?token=...)",
                            "en": "Passing token as a GET query parameter (?token=...)"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "HTML tegidagi data-* atributi ichida qoldirish",
                            "ru": "Записывать в data-* атрибуты HTML разметки",
                            "en": "Writing token into HTML data-* attributes"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "To'g'ri! HttpOnly bayrog'i JavaScript document.cookie buyrug'iga to'siq qo'yadi va XSS kiber-xurujlarida tokenni o'g'irlashni imkonsiz qiladi.",
                    "ru": "Верно! Флаг HttpOnly запрещает доступ к куки из клиентского JavaScript (document.cookie).",
                    "en": "Correct! The HttpOnly flag prevents client-side JavaScript access via document.cookie."
                },
                "feedback_incorrect": {
                    "uz": "Xato. LocalStorage ga XSS skripti osongina kira oladi. Eng xavfsiz yo'l — HttpOnly; Secure; SameSite=Strict kuki.",
                    "ru": "Неверно. LocalStorage уязвим к XSS. Стандарт безопасности — HttpOnly куки.",
                    "en": "Incorrect. LocalStorage is vulnerable to XSS. The industry standard is HttpOnly cookies."
                }
            },
            {
                "id": "q4",
                "points": 3,
                "title": {
                    "uz": "Dockerfile da nima sababdan 'USER node' (non-root) direktivasi yozilishi xavfsizlik standarti hisoblanadi?",
                    "ru": "Почему директива 'USER node' (non-root) в Dockerfile является обязательным стандартом безопасности?",
                    "en": "Why is the 'USER node' (non-root) directive in a Dockerfile an essential security standard?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Konteyner ichida RCE (masofaviy kod bajarish) zaifligi yuz berganda xakerga xost operatsion tizimining root huquqlari o'tib ketmasligi uchun",
                            "ru": "Чтобы при уязвимости RCE злоумышленник не получил права суперпользователя (root) на хост-системе",
                            "en": "To prevent an attacker from gaining host superuser (root) privileges in the event of an RCE exploit"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Node.js serverining ishlash tezligini 2 barobar oshirish uchun",
                            "ru": "Для ускорения работы Node.js сервера в 2 раза",
                            "en": "To increase Node.js server performance by 2x"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Konteyner fayl hajmini MB larda qisqartirish uchun",
                            "ru": "Для сжатия размера контейнера",
                            "en": "To compress the container image size"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Faqat Vercel yoki AWS platformalarida deploy qilish imkoniyatini ochish uchun",
                            "ru": "Исключительно для возможности деплоя на Vercel или AWS",
                            "en": "Exclusively to enable deployment on Vercel or AWS"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "To'g'ri! Minimal imtiyozlar printsipi (Principle of Least Privilege) konteyner sindirilganda xost serverini to'liq egallashdan asraydi.",
                    "ru": "Верно! Принцип наименьших привилегий предотвращает побег из контейнера с root правами.",
                    "en": "Correct! The Principle of Least Privilege prevents container escape attacks with root privileges."
                },
                "feedback_incorrect": {
                    "uz": "Xato. Agar Docker konteyneri root foydalanuvchida ishlasa, xaker serverni to'liq boshqaruvga oladi. USER node non-root huquq beradi.",
                    "ru": "Неверно. Запуск под root создает критический риск захвата хоста. USER node ограничивает привилегии.",
                    "en": "Incorrect. Running containers as root creates container breakout risks. USER node limits privileges."
                }
            }
        ]
    },
    {
        "cohort_id": "9-sinf",
        "cohort_name": {
            "uz": "9-Sinf · Junior Vibecoders & Full-Stack",
            "ru": "9-Класс · Junior Vibecoders & Full-Stack",
            "en": "Grade 9 · Junior Vibecoders & Full-Stack"
        },
        "classes": ["9-A", "9-B"],
        "week_id": "7-hafta",
        "lesson_id": "27-dars-veb-xavfsizlik-xss-va-csrf",
        "lesson_num": "27",
        "folder_path": "classes/9-sinf/7-hafta/27-dars-veb-xavfsizlik-xss-va-csrf",
        "title": {
            "uz": "9-Sinf: 27-Dars Veb Xavfsizlik: XSS, CSRF va Input Sanitization — Kiber-Test",
            "ru": "9-Класс: Урок 27 Веб-Безопасность: XSS, CSRF и Санитизация — Кибер-Тест",
            "en": "Grade 9: Lesson 27 Web Security: XSS, CSRF & Input Sanitization — Quiz"
        },
        "description": {
            "uz": "Target International School // 9-Sinf // 7-Hafta Kiber-Xavfsizlik Testi\nMavzu: XSS turlari (Stored, Reflected, DOM), Anti-CSRF tokenlar, DOMPurify va Helmet sarlavhalari\nO'qituvchi: M. Musulmonov",
            "ru": "Target International School // 9-Класс // Тест по кибербезопасности 7-й недели\nТема: Виды XSS, CSRF токены, DOMPurify и заголовки Helmet\nУчитель: М. Мусульмонов",
            "en": "Target International School // Grade 9 // Week 7 Web Security Quiz\nTopic: XSS Vectors (Stored, Reflected, DOM), Anti-CSRF Tokens, DOMPurify & Helmet Headers\nInstructor: M. Musulmonov"
        },
        "questions": [
            {
                "id": "q1",
                "points": 2,
                "title": {
                    "uz": "XSS (Cross-Site Scripting) kiber-hujumining qaysi turi ma'lumotlar bazasida saqlanib, sahifani ochgan barcha foydalanuvchilarga doimiy zarar yetkazadi?",
                    "ru": "Какой тип XSS сохраняется в базе данных и поражает каждого пользователя при открытии страницы?",
                    "en": "Which type of XSS is persisted in the database and impacts every user loading the page?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Stored (Persistent) XSS",
                            "ru": "Stored (Хранимый / Постоянный) XSS",
                            "en": "Stored (Persistent) XSS"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Reflected (Aks etuvchi) XSS",
                            "ru": "Reflected (Отраженный) XSS",
                            "en": "Reflected XSS"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "DOM-based XSS",
                            "ru": "DOM-based XSS",
                            "en": "DOM-based XSS"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Blind SQL Injection",
                            "ru": "Слепая SQL-инъекция",
                            "en": "Blind SQL Injection"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "To'g'ri! Stored XSS ma'lumotlar bazasiga (masalan sharhlar yoki profil bio ga) yoziladi va saytga kirgan barcha odamlarda ishga tushadi.",
                    "ru": "Верно! Stored XSS сохраняется в БД и выполняется в браузере любого посетителя страницы.",
                    "en": "Correct! Stored XSS persists in the database and executes for every client requesting that page."
                },
                "feedback_incorrect": {
                    "uz": "Xato. Bazada saqlanuvchi va hammaga ta'sir qiluvchi XSS turi — bu Stored (Persistent) XSS.",
                    "ru": "Неверно. Постоянный XSS в базе данных — это Stored XSS.",
                    "en": "Incorrect. The persistent database vector is Stored XSS."
                }
            },
            {
                "id": "q2",
                "points": 3,
                "title": {
                    "uz": "Veb-ilovada foydalanuvchining sessiyasini aldov yo'li bilan ishlatuvchi CSRF (Cross-Site Request Forgery) xurujiga qarshi qaysi himoya eng samarali?",
                    "ru": "Какая защита наиболее эффективна против атак CSRF (межсайтовая подделка запроса)?",
                    "en": "Which defense mechanism is most effective against CSRF (Cross-Site Request Forgery) attacks?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Kriptografik Anti-CSRF tokenlar va cookie uchun 'SameSite=Strict' rejimi",
                            "ru": "Криптографические Anti-CSRF токены и режим 'SameSite=Strict' для куки",
                            "en": "Cryptographic Anti-CSRF tokens and 'SameSite=Strict' cookie configuration"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Faqat HTTPS shifrlash sertifikatini yoqish",
                            "ru": "Использование исключительно HTTPS протокола",
                            "en": "Relying solely on HTTPS transport encryption"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Foydalanuvchi parolini har 15 daqiqada yangilatish",
                            "ru": "Требование смены пароля каждые 15 минут",
                            "en": "Enforcing password resets every 15 minutes"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Foydalanuvchining IP manzilini tekshirish",
                            "ru": "Проверка IP адреса пользователя",
                            "en": "Validating client IP addresses"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "To'g'ri! Anti-CSRF token taxmin qilib bo'lmaydigan maxfiy kalit bo'lib, SameSite=Strict esa begona saytlardan kuki yuborilishini man etadi.",
                    "ru": "Верно! Anti-CSRF токены и SameSite=Strict блокируют несанкционированную отправку запросов.",
                    "en": "Correct! Anti-CSRF tokens and SameSite=Strict eliminate cross-origin unauthorized requests."
                },
                "feedback_incorrect": {
                    "uz": "Xato. HTTPS protokoli CSRF dan asramaydi, chunki brauzer kukilarni avtomatik qo'shib yuboradi. Anti-CSRF token shart.",
                    "ru": "Неверно. HTTPS защищает канал, но браузер все равно прикрепит куки. Нужен CSRF токен.",
                    "en": "Incorrect. HTTPS protects data in transit, but browsers still send cookies unless tokens are enforced."
                }
            },
            {
                "id": "q3",
                "points": 3,
                "title": {
                    "uz": "JavaScript da foydalanuvchi kiritgan matnni xavfsiz render qilishda XSS dan xalos bo'lish uchun qaysi vosita qo'llaniladi?",
                    "ru": "Какой инструмент используется в JavaScript для безопасного рендеринга и очистки пользовательского HTML от XSS?",
                    "en": "Which tool is used in JavaScript to safely sanitize user-supplied HTML against XSS?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "DOMPurify kutubxonasi (DOMPurify.sanitize) yoki element.textContent xususiyati",
                            "ru": "Библиотека DOMPurify (DOMPurify.sanitize) или свойство textContent",
                            "en": "DOMPurify library (DOMPurify.sanitize) or the element.textContent property"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "To'g'ridan-to'g'ri element.innerHTML ga tenglashtirish",
                            "ru": "Прямая вставка в element.innerHTML",
                            "en": "Direct assignment into element.innerHTML"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "eval() funksiyasi orqali matnni tahlil qilish",
                            "ru": "Парсинг через функцию eval()",
                            "en": "Evaluating strings using the eval() function"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Faqat regex orqali <script> so'zini qirqib tashlash",
                            "ru": "Простая замена слова <script> через RegEx",
                            "en": "Simple RegEx replacement of the word <script>"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "A'lo! DOMPurify zararli onload, onerror va script xurujlarini tozalaydi, textContent esa matnni HTML emas, oddiy string sifatida xavfsiz chiqaradi.",
                    "ru": "Отлично! DOMPurify удаляет уязвимые обработчики событий и скрипты, а textContent трактует ввод как чистый текст.",
                    "en": "Excellent! DOMPurify strips event-based vectors and scripts, while textContent safely escapes raw text."
                },
                "feedback_incorrect": {
                    "uz": "Xato. innerHTML eng xavfli XSS manbasidir. DOMPurify yoki textContent ishlatish shart.",
                    "ru": "Неверно. innerHTML открывает прямую уязвимость к XSS. Используйте DOMPurify или textContent.",
                    "en": "Incorrect. innerHTML is the primary cause of XSS. Always use DOMPurify or textContent."
                }
            },
            {
                "id": "q4",
                "points": 2,
                "title": {
                    "uz": "Express.js backend serverida Content-Security-Policy (CSP), HSTS va X-Frame-Options sarlavhalarini avtomatik ulovchi middleware qaysi?",
                    "ru": "Какой middleware автоматически настраивает заголовки CSP, HSTS и X-Frame-Options в Express.js?",
                    "en": "Which middleware automatically configures CSP, HSTS, and X-Frame-Options security headers in Express.js?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Helmet.js (app.use(helmet()))",
                            "ru": "Helmet.js (app.use(helmet()))",
                            "en": "Helmet.js (app.use(helmet()))"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Morgan logger",
                            "ru": "Morgan logger",
                            "en": "Morgan logger"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Nodemon",
                            "ru": "Nodemon",
                            "en": "Nodemon"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Babel compiler",
                            "ru": "Babel compiler",
                            "en": "Babel compiler"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "To'g'ri! Helmet.js 15 ta xavfsizlik HTTP sarlavhasini bir qatorda faollashtiradi.",
                    "ru": "Верно! Helmet.js устанавливает важнейшие заголовки HTTP безопасности.",
                    "en": "Correct! Helmet.js secures Express apps by setting various HTTP headers."
                },
                "feedback_incorrect": {
                    "uz": "Xato. Express da sanoat standarti — bu Helmet.js middleware kutubxonasidir.",
                    "ru": "Неверно. Общепринятый стандарт защиты заголовков Express — Helmet.js.",
                    "en": "Incorrect. The industry standard middleware for HTTP headers is Helmet.js."
                }
            }
        ]
    },
    {
        "cohort_id": "7-8-sinf",
        "cohort_name": {
            "uz": "7–8-Sinf · Game Dev, Interaktiv Veb & FUT Creator",
            "ru": "7–8-Класс · Game Dev, Веб-игры & FUT Creator",
            "en": "Grades 7–8 · Game Dev, Interactive Web & FUT Creator"
        },
        "classes": ["7-A", "7-B", "8-A", "8-B"],
        "week_id": "8-hafta",
        "lesson_id": "30-dars-sport-simulyatori-oraliq-nazorat",
        "lesson_num": "30",
        "folder_path": "classes/7-8-sinf/8-hafta/30-dars-sport-simulyatori-oraliq-nazorat",
        "title": {
            "uz": "7–8-Sinf: 30-Dars Sport Simulyatori va O'yin Fizikasi — Oraliq Nazorat Testi",
            "ru": "7–8-Класс: Урок 30 Спортивный Симулятор и Игровая Физика — Рубежный Тест",
            "en": "Grades 7–8: Lesson 30 Sports Simulator & Game Physics — Midterm Exam"
        },
        "description": {
            "uz": "Target International School // 7–8-Sinf // 1-Chorak Oraliq Nazorat Imtihoni\nMavzu: Tarkib Kimyosi Graflari, Match Engine FSM, 2D To'qnashuv Fizikasi va 5% Soliq\nO'qituvchi: M. Musulmonov",
            "ru": "Target International School // 7–8-Класс // Рубежный контроль 1-й четверти\nТема: Граф химии состава, движок симуляции матча (FSM), 2D физика и налог 5%\nУчитель: М. Мусульмонов",
            "en": "Target International School // Grades 7–8 // Quarter 1 Midterm Exam\nTopic: Squad Chemistry Graphs, Match Engine FSM, 2D Collision Physics & EA 5% Tax\nInstructor: M. Musulmonov"
        },
        "questions": [
            {
                "id": "q1",
                "points": 2,
                "title": {
                    "uz": "FUT kartasining umumiy reytingi (OVR) qaysi usulda hisoblab chiqariladi?",
                    "ru": "Каким образом рассчитывается общий рейтинг (OVR) футбольной карточки в симуляторе?",
                    "en": "How is the overall rating (OVR) of a player card calculated in the simulator?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Futbolchining ampluasiga qarab uning muhim ko'rsatkichlariga yuqori koeffitsient beruvchi vaznli formula (Weighted Average) orqali",
                            "ru": "По взвешенной формуле, где ключевые для амплуа параметры имеют максимальный коэффициент",
                            "en": "Using a position-dependent weighted average formula where primary attributes carry higher coefficients"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Barcha 6 ta ko'rsatkichning (PAC, SHO, PAS, DRI, DEF, PHY) oddiy arifmetik o'rtachasi orqali",
                            "ru": "Простым средним арифметическим всех 6 параметров",
                            "en": "By taking the simple unweighted arithmetic mean of all 6 stats"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Faqat futbolchining bo'yi va yoshiga qarab",
                            "ru": "Исключительно по росту и возрасту футболиста",
                            "en": "Solely based on the player's physical height and age"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Math.random() orqali tasodifiy son berish bilan",
                            "ru": "Случайным числом через Math.random()",
                            "en": "By generating a random integer with Math.random()"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "To'g'ri! Masalan hujumchi uchun PAC va SHO 70% vaznga ega bo'lsa, himoyachi uchun DEF va PHY asosiy rol o'ynaydi.",
                    "ru": "Верно! Для нападающего важны PAC и SHO, для защитника — DEF и PHY.",
                    "en": "Correct! Different positions weight stats according to positional relevance."
                },
                "feedback_incorrect": {
                    "uz": "Xato. OVR oddiy o'rtacha emas, balki ampluaga mos vaznli o'rtacha (Weighted Average) hisoblanadi.",
                    "ru": "Неверно. OVR — это взвешенное среднее, зависимое от позиции игрока.",
                    "en": "Incorrect. OVR is computed as a position-based weighted average."
                }
            },
            {
                "id": "q2",
                "points": 3,
                "title": {
                    "uz": "Tarkib kimyosi (Chemistry) algoritmining to'liq 33 ballik sinergiyasiga qaysi shartlar orqali erishiladi?",
                    "ru": "При каких условиях достигается максимальный показатель в 33 балла химии состава?",
                    "en": "Under which conditions is the maximum 33 chemistry score achieved in squad building?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "11 ta o'yinchining to'g'ri pozitsiyada turishi hamda bir xil klub, liga va millat bo'yicha bog'lanishlarining to'liq qanoatlantirilishi",
                            "ru": "11 игроков на своих позициях с максимальными связями по клубу, лиге и национальности",
                            "en": "All 11 players in their primary positions satisfying club, league, and national synergy thresholds"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Faqat eng qimmat narxdagi oltin kartalarni sotib olish orqali",
                            "ru": "Покупкой самых дорогих золотых карточек",
                            "en": "By purchasing only the most expensive gold cards on the transfer market"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Barcha o'yinchilarning yoshi teng bo'lishi orqali",
                            "ru": "Если все игроки одного года рождения",
                            "en": "If all players share the identical birth year"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Tarkibda faqat hujumchilarni qoldirish orqali",
                            "ru": "Если в составе оставить только форвардов",
                            "en": "If the lineup consists solely of attackers"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "A'lo! 11 ta pozitsiyadagi o'yinchilarning har biri 3 tagacha kimyo yulduzchasiga ega bo'lib, jami 33 ball beradi.",
                    "ru": "Отлично! 11 игроков дают максимум 3 звезды химии каждый, суммарно 33 очка.",
                    "en": "Excellent! Each of the 11 positions can earn up to 3 stars, totaling 33 points."
                },
                "feedback_incorrect": {
                    "uz": "Xato. Kimyo kartaning narxiga bog'liq emas. Klub, liga va millat aloqalari (Graf sinergiyasi) zarur.",
                    "ru": "Неверно. Химия не зависит от цены, важны связи клуба, лиги и страны.",
                    "en": "Incorrect. Chemistry depends on relational graph synergy (club, league, nation)."
                }
            },
            {
                "id": "q3",
                "points": 3,
                "title": {
                    "uz": "2D o'yin fizikasi dvigatelida to'p va darvoza to'sini to'qnashuvini hisoblashda qaysi algoritm qo'llaniladi?",
                    "ru": "Какой алгоритм используется в 2D физическом движке для определения столкновения мяча со штангой ворот?",
                    "en": "Which algorithm is utilized in a 2D physics engine to detect ball collisions with the goal post?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "AABB (Axis-Aligned Bounding Box) to'rtburchaklar keshishishi formulasi",
                            "ru": "AABB (Axis-Aligned Bounding Box) — пересечение ограничивающих прямоугольников",
                            "en": "AABB (Axis-Aligned Bounding Box) rectangular intersection testing"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Nyutonning 1-harakat qonuni",
                            "ru": "Первый закон Ньютона",
                            "en": "Newton's First Law of Motion"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Faqat Pifagor gipotenuzasi formulasi",
                            "ru": "Исключительно формула теоремы Пифагора",
                            "en": "Exclusively the Pythagorean hypotenuse formula"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "CSS margin va padding qiymatlarini solishtirish",
                            "ru": "Сравнение CSS отступов",
                            "en": "Comparing CSS margin and padding properties"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "To'g'ri! AABB algoritmi x va y koordinatalari bo'yicha min va max chegaralarni taqqoslab, to'qnashuvni millisekundlarda fosh qiladi.",
                    "ru": "Верно! AABB быстро определяет коллизии через сравнение проекций на оси X и Y.",
                    "en": "Correct! AABB detects overlaps efficiently along the X and Y coordinate axes."
                },
                "feedback_incorrect": {
                    "uz": "Xato. O'yin grafikasi va fizikasida standart to'qnashuv tekshiruvi — bu AABB (Bounding Box) algoritmidir.",
                    "ru": "Неверно. Базовый алгоритм коллизий в 2D играх — AABB.",
                    "en": "Incorrect. The fundamental 2D collision algorithm is AABB."
                }
            },
            {
                "id": "q4",
                "points": 2,
                "title": {
                    "uz": "FUT auksion bozoridagi har bir bitimdan olinadigan 5% savdo solig'i (EA Tax) virtual o'yinda qanday iqtisodiy vazifani bajaradi?",
                    "ru": "Какую экономическую функцию выполняет 5% налог с продаж (EA Tax) на виртуальном трансферном рынке?",
                    "en": "What economic purpose does the 5% transaction tax (EA Tax) serve in a virtual transfer market?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Tizimdan ortiqcha tangalarni doimiy yoqish (Coin Sink) orqali inflyatsiyani to'xtatish va bozor narxlarini barqaror saqlash",
                            "ru": "Служит механизмом сжигания монет (Coin Sink) для борьбы с инфляцией и стабилизации цен",
                            "en": "Acts as a Coin Sink to drain excess currency from circulation, mitigating hyperinflation"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "O'yin yaratuvchilarining real boyishi uchun",
                            "ru": "Для реального обогащения создателей игры",
                            "en": "To generate real cash revenue for developers"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Kartalarni avtomatik o'chirib yuborish uchun",
                            "ru": "Для удаления случайных карточек",
                            "en": "To randomly delete unused player cards"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "O'yin yuklanishini tezlashtirish uchun",
                            "ru": "Для ускорения загрузки приложения",
                            "en": "To speed up network application loading"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "A'lo! O'yinchilar mukofotlar orqali uzluksiz tanga ishlab chiqaradilar (Minting). 5% soliq (Coin Sink) bo'lmasa, pul qadrsizlanadi va giperinflyatsiya boshlanadi.",
                    "ru": "Отлично! Налог является монетарным регулятором (Coin Sink), сдерживающим денежную массу M2.",
                    "en": "Excellent! Taxes act as deflationary Coin Sinks counterbalancing continuous minting rewards."
                },
                "feedback_incorrect": {
                    "uz": "Xato. 5% auksion solig'i — o'yin iqtisodiyotidagi giperinflyatsiyaning oldini oluvchi Coin Sink mexanizmidir.",
                    "ru": "Неверно. 5% налог сжигает монеты для защиты от гиперинфляции.",
                    "en": "Incorrect. The 5% tax is an essential monetary Coin Sink preventing hyperinflation."
                }
            }
        ]
    },
    {
        "cohort_id": "5-6-sinf",
        "cohort_name": {
            "uz": "5–6-Sinf · Junior Creators & Kiber-Xavfsizlik",
            "ru": "5–6-Класс · Junior Creators & Кибербезопасность",
            "en": "Grades 5–6 · Junior Creators & CyberSecurity"
        },
        "classes": ["5-A", "5-B", "6-A", "6-B"],
        "week_id": "8-hafta",
        "lesson_id": "22-dars-kiber-qalqon-oraliq-nazorat",
        "lesson_num": "22",
        "folder_path": "classes/5-6-sinf/8-hafta/22-dars-kiber-qalqon-oraliq-nazorat",
        "title": {
            "uz": "5–6-Sinf: 22-Dars Kiber-Qalqon Viktorinasi — Oraliq Nazorat Testi",
            "ru": "5–6-Класс: Урок 22 Викторина Кибер-Щит — Рубежный Тест",
            "en": "Grades 5–6: Lesson 22 Cyber Shield Security Quiz — Midterm Exam"
        },
        "description": {
            "uz": "Target International School // 5–6-Sinf // 1-Chorak Kiber-Qalqon Viktorinasi\nMavzu: Mustahkam Parollar, Fishing Qopqonlari, Troyanlar va Shaxsiy Maxfiylik\nO'qituvchi: M. Musulmonov",
            "ru": "Target International School // 5–6-Класс // Викторина безопасности 1-й четверти\nТема: Надежные пароли, фишинг, троянские программы и цифровая приватность\nУчитель: М. Мусульмонов",
            "en": "Target International School // Grades 5–6 // Quarter 1 Security Quiz\nTopic: Strong Passwords, Phishing Detection, Trojan Defense & Digital Privacy\nInstructor: M. Musulmonov"
        },
        "questions": [
            {
                "id": "q1",
                "points": 2,
                "title": {
                    "uz": "Kiber-xavfsizlik qoidalariga ko'ra, eng mustahkam va xakerlar buza olmaydigan parol qanday tuziladi?",
                    "ru": "По правилам кибербезопасности, как составляется наиболее стойкий пароль?",
                    "en": "According to cybersecurity rules, how is the strongest, uncrackable password formulated?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Kamida 14+ ta belgi, katta va kichik harflar, raqamlar hamda maxsus belgilar (#, $, !) aralashmasidan",
                            "ru": "Не менее 14+ знаков, включая заглавные и строчные буквы, цифры и символы (#, $, !)",
                            "en": "At least 14+ characters mixing uppercase, lowercase, numbers, and special symbols (#, $, !)"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "O'z ismi va tug'ilgan yili (masalan: ali2014)",
                            "ru": "Имя и год рождения (например: ali2014)",
                            "en": "Personal name and birth year (e.g., ali2014)"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Klaviaturadagi ketma-ket harflar (12345678 yoki qwerty)",
                            "ru": "Последовательность клавиш (12345678 или qwerty)",
                            "en": "Sequential keyboard characters (12345678 or qwerty)"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Faqat 4 xonali oddiy PIN-kod",
                            "ru": "Простой 4-значный PIN-код",
                            "en": "A simple 4-digit numeric PIN"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "Barakalla! 14+ belgili murakkab parolni superkompyuterlar ham yuzlab yillar davomida buza olmaydi.",
                    "ru": "Молодец! Длинный сложный пароль из 14+ символов невозможно взломать брутфорсом.",
                    "en": "Well done! A 14+ character complex passphrase withstands brute-force attempts for centuries."
                },
                "feedback_incorrect": {
                    "uz": "Xato. Ism, tug'ilgan yil va 123456 parolini xakerlar 1 soniyada buzib kiradilar. Parol 14+ belgili bo'lishi shart.",
                    "ru": "Неверно. Простые пароли и даты взламываются мгновенно по словарю.",
                    "en": "Incorrect. Names and sequential numbers are cracked within seconds via dictionary attacks."
                }
            },
            {
                "id": "q2",
                "points": 3,
                "title": {
                    "uz": "Internetda 'Shoshiling! Bepul 10,000 Robux yoki Telegram Premium beramiz, parolingizni kiriting' degan havolani ko'rsangiz nima qilishingiz kerak?",
                    "ru": "Что нужно сделать, если вы увидели ссылку 'Бесплатные 10,000 Robux или Telegram Premium, введите пароль'?",
                    "en": "What must you do if you encounter a link claiming 'Free 10,000 Robux or Telegram Premium, enter your password'?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Sahifani darhol yopish va parolni kiritmaslik — bu xakerlarning fishing (aldov) qopqoni!",
                            "ru": "Немедленно закрыть страницу и ничего не вводить — это фишинговая ловушка мошенников!",
                            "en": "Immediately close the webpage and never enter credentials — it is a phishing trap!"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Tezda profilingiz parolini kiritib, bepul mukofotni kutish",
                            "ru": "Быстро ввести пароль и ждать приз",
                            "en": "Quickly input account credentials and await the prize"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Havolani barcha sinfdoshlar va guruhlarga tarqatish",
                            "ru": "Переслать ссылку друзьям во все группы",
                            "en": "Forward the link to all school chat groups"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Kompyuter ekranini o'chirib qo'yish",
                            "ru": "Выключить монитор",
                            "en": "Turn off the computer screen"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "To'g'ri! 'Tekin pishloq faqat qopqonda bo'ladi'. Hech kim internetda bepul robux yoki pul bermaydi, bu profilni o'g'irlash usulidir.",
                    "ru": "Верно! Бесплатный сыр бывает только в мышеловке. Это фишинг для угона аккаунтов.",
                    "en": "Correct! Free handouts are classic lures. This is credential phishing designed to steal accounts."
                },
                "feedback_incorrect": {
                    "uz": "Xato. Agar parolni kiritib yuborsangiz, profilingiz xakerlar qo'liga o'tadi. Soxta havolalarni aslo ochmang.",
                    "ru": "Неверно. Ввод данных на таких сайтах ведет к полной потере доступа к аккаунту.",
                    "en": "Incorrect. Submitting credentials on untrusted domains results in immediate account takeover."
                }
            },
            {
                "id": "q3",
                "points": 3,
                "title": {
                    "uz": "Fotosuratni internetga joylashdan oldin nega undagi yashirin GPS (EXIF) metama'lumotlarni tozalash zarur?",
                    "ru": "Почему перед публикацией фото в интернет нужно стирать скрытые GPS (EXIF) метаданные?",
                    "en": "Why should hidden GPS location (EXIF) metadata be stripped before publishing photos online?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Notanish odamlar va firibgarlar sizning uyingiz, maktabingiz yoki qayerda ekanligingizni xaritada aniqlay olmasligi uchun",
                            "ru": "Чтобы посторонние и злоумышленники не смогли вычислить точный адрес вашего дома или школы по карте",
                            "en": "To prevent strangers and adversaries from tracking your exact home or school coordinates on a map"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Suratning ranglarini yanada yorqinroq qilish uchun",
                            "ru": "Чтобы сделать цвета фотографии ярче",
                            "en": "To enhance photo colors and brightness"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Faqat smartfon xotirasini tejash uchun",
                            "ru": "Исключительно для экономии памяти смартфона",
                            "en": "Solely to free up storage on the smartphone"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Surat internetda tezroq ochilishi uchun",
                            "ru": "Чтобы фотография быстрее загружалась",
                            "en": "To speed up image rendering"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "Barakalla! EXIF fotosurat olingan aniq kenglik va uzunlik koordinatalarini saqlaydi. Uni o'chirish orqali shaxsiy xavfsizligingizni ta'minlaysiz.",
                    "ru": "Верно! Данные EXIF содержат точные координаты съемки. Их удаление защищает приватность.",
                    "en": "Correct! EXIF tags hold precise GPS coordinates. Removing them preserves physical safety and privacy."
                },
                "feedback_incorrect": {
                    "uz": "Xato. EXIF geolokatsiyasi orqali uyingiz manzilini topib olishlari mumkin. Doim rasmlarni tozalab yuklang.",
                    "ru": "Неверно. GPS метки раскрывают местоположение вашего дома.",
                    "en": "Incorrect. GPS metadata discloses exact physical residential locations."
                }
            },
            {
                "id": "q4",
                "points": 2,
                "title": {
                    "uz": "Internetda xavfsiz yashashning 'Katta Ekran Qoidasi' (Billboard Rule) nimani anglatadi?",
                    "ru": "Что означает 'Правило Большого Экрана' (Billboard Rule) безопасного поведения в интернете?",
                    "en": "What does the 'Billboard Rule' teach about safe online conduct?"
                },
                "choices": [
                    {
                        "text": {
                            "uz": "Shaharning eng gavjum ko'chasidagi ulkan ekranga chiqarishdan uyaladigan shaxsiy ma'lumot yoki rasmlarni internetga aslo yuklamaslik",
                            "ru": "Никогда не выкладывать в интернет то, что вы постеснялись бы показать на огромном экране в центре города",
                            "en": "Never upload personal photos or data that you would feel uncomfortable displaying on a giant public billboard"
                        },
                        "correct": True
                    },
                    {
                        "text": {
                            "uz": "Faqat katta televizor va monitordan foydalanish",
                            "ru": "Работать только за большим экраном",
                            "en": "Only using large desktop monitors"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Xabarlarni faqat KATTA HARFLARDA yozish",
                            "ru": "Писать сообщения только ЗАГЛАВНЫМИ БУКВАМИ",
                            "en": "Writing chat messages strictly in ALL CAPS"
                        },
                        "correct": False
                    },
                    {
                        "text": {
                            "uz": "Kinoteatrga borib film tomosha qilish",
                            "ru": "Ходить в кинотеатр на фильмы",
                            "en": "Going to movie theaters regularly"
                        },
                        "correct": False
                    }
                ],
                "feedback_correct": {
                    "uz": "To'g'ri! Internetga tushgan har qanday narsa abadiy qoladi va butun dunyoga ko'rinishi mumkin. Shuning uchun o'zingizni ehtiyot qiling!",
                    "ru": "Верно! Цифровой след остается навсегда. То, что попало в сеть, может стать доступно каждому.",
                    "en": "Correct! The digital footprint lasts indefinitely. Treat all online postings as visible to the whole world."
                },
                "feedback_incorrect": {
                    "uz": "Xato. 'Billboard Rule' — shaxsiy sir va noqulay narsalarni internetga qo'ymaslik qoidasidir.",
                    "ru": "Неверно. Правило учит осмотрительности при публикации личной информации.",
                    "en": "Incorrect. The Billboard Rule cautions against uploading any material you wouldn't share publicly."
                }
            }
        ]
    }
]

def generate_apps_script_for_quiz(quiz, lang="uz"):
    """
    Generates ready-to-run Google Apps Script code using FormApp.
    """
    fn_name = "createGoogleForm_" + quiz["lesson_id"].replace("-", "_") + f"_{lang}"
    title = quiz["title"].get(lang, quiz["title"]["uz"]).replace('"', '\\"').replace("\n", " ")
    desc = quiz["description"].get(lang, quiz["description"]["uz"]).replace('"', '\\"').replace("\n", "\\n")
    
    classes_json = json.dumps(quiz["classes"], ensure_ascii=False)
    
    name_label = "O'quvchining F.I.Sh. (Familiya, Ism)" if lang == "uz" else ("Ф.И.О. Учащегося" if lang == "ru" else "Student Full Name")
    class_label = "Sinfingizni tanlang:" if lang == "uz" else ("Выберите ваш класс:" if lang == "ru" else "Select your class:")

    script = []
    script.append(f"/**")
    script.append(f" * Target International School — Google Form Generator")
    script.append(f" * Dars: {quiz['title']['uz']}")
    script.append(f" * Til / Language: {lang.upper()}")
    script.append(f" */")
    script.append(f"function {fn_name}() {{")
    script.append(f"  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish")
    script.append(f'  var form = FormApp.create("{title}");')
    script.append(f'  form.setDescription("{desc}");')
    script.append(f"  form.setIsQuiz(true);")
    script.append(f"  form.setRequireLogin(false);")
    script.append(f"  form.setCollectEmail(true);")
    script.append(f"  form.setShowLinkToRespondAgain(false);")
    script.append(f"  form.setProgressBar(true);")
    script.append(f"  form.setShuffleQuestions(false);")
    script.append(f"")
    script.append(f"  // 2. O'quvchi ma'lumotlarini to'plash")
    script.append(f'  form.addTextItem().setTitle("{name_label}").setRequired(true);')
    script.append(f'  form.addListItem().setTitle("{class_label}").setChoiceValues({classes_json}).setRequired(true);')
    script.append(f"")

    for i, q in enumerate(quiz["questions"], start=1):
        q_title = q["title"].get(lang, q["title"]["uz"]).replace('"', '\\"').replace("\n", "\\n")
        q_points = q["points"]
        fb_correct = q["feedback_correct"].get(lang, q["feedback_correct"]["uz"]).replace('"', '\\"').replace("\n", "\\n")
        fb_incorrect = q["feedback_incorrect"].get(lang, q["feedback_incorrect"]["uz"]).replace('"', '\\"').replace("\n", "\\n")

        script.append(f"  // Savol {i} ({q_points} ball)")
        script.append(f"  var q{i} = form.addMultipleChoiceItem();")
        script.append(f'  q{i}.setTitle("{i}. {q_title}");')
        script.append(f"  q{i}.setPoints({q_points});")
        script.append(f"  q{i}.setChoices([")
        
        choice_lines = []
        for c in q["choices"]:
            c_text = c["text"].get(lang, c["text"]["uz"]).replace('"', '\\"').replace("\n", " ")
            is_correct = "true" if c["correct"] else "false"
            choice_lines.append(f'    q{i}.createChoice("{c_text}", {is_correct})')
        
        script.append(",\n".join(choice_lines))
        script.append(f"  ]);")
        script.append(f'  q{i}.setFeedbackForCorrect(FormApp.createFeedback().setText("{fb_correct}").build());')
        script.append(f'  q{i}.setFeedbackForIncorrect(FormApp.createFeedback().setText("{fb_incorrect}").build());')
        script.append(f"  q{i}.setRequired(true);")
        script.append(f"")

    script.append(f'  Logger.log("=========================================");')
    script.append(f'  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");')
    script.append(f'  Logger.log("📌 Form Nomi: " + form.getTitle());')
    script.append(f'  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());')
    script.append(f'  Logger.log("🌐 O\'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());')
    script.append(f'  Logger.log("=========================================");')
    script.append(f"}}")
    return "\n".join(script)

def generate_csv_for_quiz(quiz, lang="uz"):
    """
    Generates CSV compatible with Form Builder and Quiz import tools.
    Format: Question,Type,Option 1,Option 2,Option 3,Option 4,Correct Answer,Points
    """
    lines = []
    lines.append("Question,Question Type,Option 1,Option 2,Option 3,Option 4,Correct Option,Points")
    for q in quiz["questions"]:
        q_title = '"' + q["title"].get(lang, q["title"]["uz"]).replace('"', '""').replace("\n", " ") + '"'
        opts = []
        correct_idx = 1
        for idx, c in enumerate(q["choices"], start=1):
            c_text = '"' + c["text"].get(lang, c["text"]["uz"]).replace('"', '""') + '"'
            opts.append(c_text)
            if c["correct"]:
                correct_idx = idx
        while len(opts) < 4:
            opts.append('""')
        lines.append(f"{q_title},Multiple Choice,{opts[0]},{opts[1]},{opts[2]},{opts[3]},{correct_idx},{q['points']}")
    return "\n".join(lines)

def main():
    print("Generating Google Apps Script files for each lesson...")
    master_scripts = []

    for quiz in QUIZ_DATA:
        folder = quiz["folder_path"]
        os.makedirs(folder, exist_ok=True)

        # Generate individual google_form.gs (uz, ru, en in one file)
        uz_code = generate_apps_script_for_quiz(quiz, "uz")
        ru_code = generate_apps_script_for_quiz(quiz, "ru")
        en_code = generate_apps_script_for_quiz(quiz, "en")

        lesson_script = f"""/**
 * Target International School — Google Forms Generator Script
 * Dars: {quiz['title']['uz']}
 * 
 * QO'LLANMA:
 * 1. https://script.new sahifasini oching.
 * 2. Ushbu fayl kodini to'liq nusxalab, script.new tahrirchisiga qo'ying.
 * 3. Tepada funksiyani tanlang (masalan, createGoogleForm_{quiz['lesson_id'].replace('-', '_')}_uz) va "Run" (▶️) tugmasini bosing.
 * 4. Google Drive ichingizda test avtomatik yaratiladi va konsolda havola chiqadi!
 */

{uz_code}

{ru_code}

{en_code}
"""
        gs_file_path = os.path.join(folder, "google_form.gs")
        with open(gs_file_path, "w", encoding="utf-8") as f:
            f.write(lesson_script)
        print(f"Generated {gs_file_path}")

        master_scripts.append(uz_code)

    # Master all_google_forms.gs
    master_path = "scripts/all_google_forms.gs"
    with open(master_path, "w", encoding="utf-8") as f:
        f.write("/**\n * Target International School — Barcha Darslar Google Forms Yaratuvchisi\n */\n\n" + "\n\n".join(master_scripts))
    print(f"Generated {master_path}")

    # Generate JSON database for web studio
    json_path = "scripts/google_forms_data.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(QUIZ_DATA, f, ensure_ascii=False, indent=2)
    print(f"Generated {json_path}")

if __name__ == "__main__":
    main()
