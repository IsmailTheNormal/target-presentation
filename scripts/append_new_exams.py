#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

NEW_EXAMS = [
  {
    "cohort_id": "9-sinf",
    "cohort_name": {
      "uz": "9-Sinf · Junior Vibecoders & Full-Stack",
      "ru": "9-Класс · Junior Vibecoders & Full-Stack",
      "en": "Grade 9 · Junior Vibecoders & Full-Stack"
    },
    "classes": ["9-A", "9-B"],
    "week_id": "6-hafta",
    "lesson_id": "26-dars-mvc-backend-va-relyatsion-baza",
    "lesson_num": "26",
    "folder_path": "classes/9-sinf/6-hafta/26-dars-mvc-backend-va-relyatsion-baza",
    "title": {
      "uz": "9-Sinf: 26-Dars MVC Backend Asoslari va Relyatsion SQLite — Kiber-Test",
      "ru": "9-Класс: Урок 26 Архитектура MVC и Реляционная SQLite — Тест",
      "en": "Grade 9: Lesson 26 MVC Backend Architecture & Relational SQLite — Quiz"
    },
    "description": {
      "uz": "Target International School // 9-Sinf // 6-Hafta // 26-Dars\nMavzu: MVC Arxitekturasi, Relyatsion Jadvallar, Foreign Keys va REST API\nO'qituvchi: M. Musulmonov",
      "ru": "Target International School // 9-Класс // 6-я Неделя // Урок 26\nТема: Архитектура MVC, Реляционные Таблицы, Foreign Keys и REST API\nУчитель: М. Мусульмонов",
      "en": "Target International School // Grade 9 // Week 6 // Lesson 26\nTopic: MVC Architecture, Relational Tables, Foreign Keys & REST API\nInstructor: M. Musulmonov"
    },
    "questions": [
      {
        "id": "q1",
        "points": 3,
        "title": {
          "uz": "Professional MVC (Model-View-Controller) arxitekturasida har bir qatlamning vazifasi qanday to'g'ri taqsimlanadi?",
          "ru": "Как правильно распределяются обязанности между слоями в профессиональной архитектуре MVC?",
          "en": "How are responsibilities correctly distributed across layers in professional MVC architecture?"
        },
        "choices": [
          {
            "text": {
              "uz": "Model — faqat ma'lumotlar bazasi va SQL bilan ishlaydi; View — mijozga JSON/UI qaytaradi; Controller — HTTP so'rovni tekshirib biznes mantig'ini boshqaradi.",
              "ru": "Model — работает только с БД и SQL; View — отдает JSON/UI клиенту; Controller — валидирует запрос и управляет бизнес-логикой.",
              "en": "Model — handles only DB and SQL; View — returns JSON/UI to client; Controller — validates request and manages business logic."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "Model faqat CSS stillarini saqlaydi, Controller esa to'g'ridan-to'g'ri brauzerda animatsiyalarni chizadi.",
              "ru": "Model хранит только стили CSS, а Controller напрямую отрисовывает анимации в браузере.",
              "en": "Model only stores CSS styling, while Controller renders browser animations directly."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Barcha SQL so'rovlar, HTML sahifalar va autentifikatsiya bitta server.js faylida aralash yoziladi.",
              "ru": "Все SQL-запросы, HTML и аутентификация пишутся вперемешку в одном файле server.js.",
              "en": "All SQL queries, HTML pages, and auth logic are lumped together inside a single server.js file."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Controller faqat server xotirasini tozalaydi, SQL so'rovlarni esa View bajaradi.",
              "ru": "Controller только очищает память сервера, а SQL-запросы выполняет View.",
              "en": "Controller only purges server RAM while SQL queries are executed directly by the View."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "A'lo! MVC qatlamlarni ajratish orqali loyihani Spaghetti Code ga aylanishdan asraydi.",
          "ru": "Отлично! MVC предотвращает превращение проекта в спагетти-код за счет строгого разделения обязанностей.",
          "en": "Excellent! MVC prevents spaghetti code by enforcing clean separation of concerns."
        },
        "feedback_incorrect": {
          "uz": "Noto'g'ri. Model — Baza (SQL), Controller — Mantiq & Validatsiya, View — Taqdimot (JSON/UI).",
          "ru": "Неверно. Model отвечает за данные, Controller — за логику и валидацию, View — за представление.",
          "en": "Incorrect. Model manages data/SQL, Controller enforces logic/validation, View formats output."
        }
      },
      {
        "id": "q2",
        "points": 3,
        "title": {
          "uz": "Relyatsion SQLite ma'lumotlar bazasida Foreign Key (Tashqi Kalit) nima uchun xizmat qiladi?\n\nCREATE TABLE orders (\n  id INTEGER PRIMARY KEY,\n  user_id INTEGER NOT NULL,\n  FOREIGN KEY (user_id) REFERENCES users(id)\n);",
          "ru": "Для чего служит Foreign Key (Внешний ключ) в реляционной базе SQLite?\n\nCREATE TABLE orders (\n  id INTEGER PRIMARY KEY,\n  user_id INTEGER NOT NULL,\n  FOREIGN KEY (user_id) REFERENCES users(id)\n);",
          "en": "What is the primary purpose of a Foreign Key constraint in SQLite relational DB?\n\nCREATE TABLE orders (\n  id INTEGER PRIMARY KEY,\n  user_id INTEGER NOT NULL,\n  FOREIGN KEY (user_id) REFERENCES users(id)\n);"
        },
        "choices": [
          {
            "text": {
              "uz": "Buyurtmani aniq foydalanuvchiga 1-to-Many bog'lash va mavjud bo'lmagan soxta user_id kiritilishidan yaxlitlikni (Integrity) himoyalash uchun.",
              "ru": "Для связи заказа с конкретным пользователем (1-ко-многим) и защиты ссылочной целостности от несуществующих user_id.",
              "en": "To establish a 1-to-Many link between order and user, safeguarding relational integrity against nonexistent user_ids."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "Baza faylini qattiq diskdan butunlay o'chirib yuborish uchun.",
              "ru": "Для полного удаления файла базы данных с жесткого диска.",
              "en": "To permanently delete database files from the storage drive."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Faqat parollarni avtomatik ravishda SHA-256 bilan shifrlash uchun.",
              "ru": "Исключительно для автоматического шифрования паролей алгоритмом SHA-256.",
              "en": "Solely for automatically hashing passwords using SHA-256."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Serverda Node.js versiyasini yangilash uchun.",
              "ru": "Для обновления версии Node.js на сервере.",
              "en": "For upgrading Node.js versions on the host server."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! Foreign Key jadvallar o'rtasidagi mantiqiy aloqa va yaxlitlik kafolatidir.",
          "ru": "Верно! Внешний ключ гарантирует ссылочную целостность между таблицами.",
          "en": "Correct! Foreign keys enforce referential integrity across relational tables."
        },
        "feedback_incorrect": {
          "uz": "Xato. Foreign Key buyurtmani aniq mavjud foydalanuvchiga bog'lash uchun shart.",
          "ru": "Неверно. Внешний ключ связывает записи orders с существующими пользователями users.",
          "en": "Incorrect. A Foreign Key strictly ties order rows to existing user records."
        }
      },
      {
        "id": "q3",
        "points": 2,
        "title": {
          "uz": "REST API Controller qatlamida mijoz manfiy yoki noto'g'ri miqdor yuborganida qaysi HTTP status kodi qaytarilishi shart?\n\nif (!quantity || quantity <= 0) {\n  return res.status(...).json({ error: 'Noto\\'g\\'ri miqdor' });\n}",
          "ru": "Какой HTTP статус-код должен вернуть контроллер REST API при получении отрицательного или некорректного количества?\n\nif (!quantity || quantity <= 0) {\n  return res.status(...).json({ error: 'Некорректное количество' });\n}",
          "en": "Which HTTP status code must the REST API controller return when client submits an invalid or negative quantity?\n\nif (!quantity || quantity <= 0) {\n  return res.status(...).json({ error: 'Invalid quantity' });\n}"
        },
        "choices": [
          {
            "text": {
              "uz": "400 Bad Request — mijoz yuborgan ma'lumotlarda validatsiya xatosi borligini bildiradi.",
              "ru": "400 Bad Request — сигнализирует об ошибке клиентской валидации данных.",
              "en": "400 Bad Request — indicates client payload validation failed."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "200 OK — har qanday xatoda ham muvaffaqiyatli deb qaytarish.",
              "ru": "200 OK — сообщать об успехе даже при ошибке входных данных.",
              "en": "200 OK — reporting success despite erroneous input data."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "404 Not Found — sahifa topilmaganligini bildirish.",
              "ru": "404 Not Found — сообщение о том, что страница не найдена.",
              "en": "404 Not Found — declaring the requested resource missing."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "500 Internal Server Error — server kodi buzilib qulaganini bildirish.",
              "ru": "500 Internal Server Error — падение бэкенд сервера.",
              "en": "500 Internal Server Error — unhandled server crash."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! Mijoz noto'g'ri parametr berganda har doim 400 Bad Request qaytariladi.",
          "ru": "Правильно! Ошибки входных данных всегда сопровождаются статусом 400 Bad Request.",
          "en": "Correct! Client-side payload errors always warrant a 400 Bad Request response."
        },
        "feedback_incorrect": {
          "uz": "Xato. Validatsiya xatolarida 400 Bad Request standarti qo'llaniladi.",
          "ru": "Неверно. Стандартный статус для ошибок валидации входных данных — 400.",
          "en": "Incorrect. Standard status code for request validation failure is 400."
        }
      },
      {
        "id": "q4",
        "points": 2,
        "title": {
          "uz": "Buyurtmalar ro'yxatini xaridorning ismi va tovarning nomi bilan birgalikda yagona so'rovda olish uchun qaysi SQL operatori ishlatiladi?\n\nSELECT orders.id, users.name, products.title\nFROM orders\n... users ON orders.user_id = users.id;",
          "ru": "Какой SQL оператор используется для объединения таблицы заказов с именами пользователей и товаров в одном запросе?\n\nSELECT orders.id, users.name, products.title\nFROM orders\n... users ON orders.user_id = users.id;",
          "en": "Which SQL operator is used to combine the orders table with users and products in a single unified query?\n\nSELECT orders.id, users.name, products.title\nFROM orders\n... users ON orders.user_id = users.id;"
        },
        "choices": [
          {
            "text": {
              "uz": "INNER JOIN — jadvallardagi mos kalitlar bo'yicha qatorlarni birlashtiradi.",
              "ru": "INNER JOIN — объединяет строки таблиц по совпадающим ключевым полям.",
              "en": "INNER JOIN — joins table records matching corresponding foreign key fields."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "DROP TABLE — jadvalni o'chirib qayta yaratadi.",
              "ru": "DROP TABLE — удаляет таблицу перед чтением.",
              "en": "DROP TABLE — deletes tables prior to query reading."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "DELETE FROM — faqat bo'sh qatorlarni qoldiradi.",
              "ru": "DELETE FROM — удаляет все строки из таблицы.",
              "en": "DELETE FROM — purges data records."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "INSERT INTO — yangi ustun kiritadi.",
              "ru": "INSERT INTO — создает новую колонку в схеме.",
              "en": "INSERT INTO — adds a new column to schema."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! INNER JOIN relyatsion ma'lumotlar bazasining eng kuchli qurolidir.",
          "ru": "Верно! INNER JOIN позволяет собирать связанные сущности в один плоский отчет.",
          "en": "Correct! INNER JOIN compiles interconnected relational rows into a unified dataset."
        },
        "feedback_incorrect": {
          "uz": "Xato. Bog'langan jadvallardan ma'lumot olish uchun INNER JOIN qo'llaniladi.",
          "ru": "Неверно. Связывание таблиц выполняется с помощью INNER JOIN.",
          "en": "Incorrect. Table associations are queried utilizing INNER JOIN."
        }
      }
    ]
  },
  {
    "cohort_id": "10-11-sinf",
    "cohort_name": {
      "uz": "10–11-Sinf · Senior Engineering & Cloud Security",
      "ru": "10–11-Класс · Senior Engineering & Cloud Security",
      "en": "Grades 10–11 · Senior Engineering & Cloud Security"
    },
    "classes": ["10-A", "10-B", "11-A", "11-B"],
    "week_id": "7-hafta",
    "lesson_id": "31-dars-penetration-testing-va-ethical-hacking",
    "lesson_num": "31",
    "folder_path": "classes/10-11-sinf/7-hafta/31-dars-penetration-testing-va-ethical-hacking",
    "title": {
      "uz": "10–11-Sinf: 31-Dars Penetration Testing & Ethical Hacking — Kiber-Test",
      "ru": "10–11-Класс: Урок 31 Тестирование на Проникновение и Этичный Хакинг — Тест",
      "en": "Grades 10–11: Lesson 31 Penetration Testing & Ethical Hacking — Quiz"
    },
    "description": {
      "uz": "Target International School // 10–11-Sinf // 7-Hafta // 31-Dars\nMavzu: White Hat tamoyillari, BOLA/IDOR zaifligi, Security Headers va CVSS v3.1\nO'qituvchi: M. Musulmonov",
      "ru": "Target International School // 10–11-Класс // 7-я Неделя // Урок 31\nТема: Принципы White Hat, Уязвимость BOLA/IDOR, Security Headers и CVSS v3.1\nУчитель: М. Мусульмонов",
      "en": "Target International School // Grades 10–11 // Week 7 // Lesson 31\nTopic: White Hat Ethics, BOLA/IDOR Flaws, Security Headers & CVSS v3.1\nInstructor: M. Musulmonov"
    },
    "questions": [
      {
        "id": "q1",
        "points": 3,
        "title": {
          "uz": "OWASP API Security Top 10 ning #1 kritik zaifligi bo'lgan BOLA / IDOR qanday yuzaga keladi va uni qanday to'g'rilash kerak?\n\n// ZAIF KOD:\napp.get('/api/documents/:docId', (req, res) => {\n  const doc = db.find({ id: req.params.docId });\n  res.json(doc); // Muammo qayerda?\n});",
          "ru": "Как возникает критическая уязвимость BOLA / IDOR (#1 в OWASP API Top 10) и как её исправить в коде?\n\n// УЯЗВИМЫЙ КОД:\napp.get('/api/documents/:docId', (req, res) => {\n  const doc = db.find({ id: req.params.docId });\n  res.json(doc);\n});",
          "en": "How does the #1 OWASP API flaw BOLA / IDOR occur and how must it be patched?\n\n// VULNERABLE SNIPPET:\napp.get('/api/documents/:docId', (req, res) => {\n  const doc = db.find({ id: req.params.docId });\n  res.json(doc);\n});"
        },
        "choices": [
          {
            "text": {
              "uz": "Server ob'ekt egasini tekshirmaydi; Tuzatish: doc.owner_id === req.user.id tekshiruvini kiritish va mos kelmasa 403 Forbidden qaytarish.",
              "ru": "Сервер не проверяет владельца ресурса; Исправление: проверять doc.owner_id === req.user.id и возвращать 403 Forbidden при несовпадении.",
              "en": "Server fails to verify resource ownership; Fix: enforce doc.owner_id === req.user.id check and abort with 403 Forbidden."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "Hech qanday zaiflik yo'q, chunki docId unikal UUID raqam bo'lishi kifoya.",
              "ru": "Уязвимости нет, достаточно чтобы docId был уникальным UUID.",
              "en": "No vulnerability exists provided docId is a randomized UUID."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Faqat port raqamini 80 dan 443 ga o'zgartirish kifoya.",
              "ru": "Достаточно просто сменить сетевой порт с 80 на 443.",
              "en": "Simply changing server port from 80 to 443 eliminates the flaw."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Faqat GET o'rniga DELETE metodidan foydalanish zarur.",
              "ru": "Необходимо заменить HTTP метод GET на DELETE.",
              "en": "Replacing the HTTP GET method with DELETE resolves authorization."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! BOLA/IDOR — obyektga ruxsatni tekshirmaslikdir. Har doim owner_id tekshirilishi shart!",
          "ru": "Верно! BOLA возникает из-за отсутствия проверки владельца объекта. Проверка owner_id обязательна!",
          "en": "Correct! BOLA occurs when object ownership is neglected. Validating owner_id is imperative!"
        },
        "feedback_incorrect": {
          "uz": "Xato. Autentifikatsiya qilingan foydalanuvchi faqat o'ziga tegishli hujjatni ko'rishi shart.",
          "ru": "Неверно. Пользователь должен иметь доступ строго к своим объектам (проверка owner_id).",
          "en": "Incorrect. Access must be constrained strictly to records owned by req.user.id."
        }
      },
      {
        "id": "q2",
        "points": 3,
        "title": {
          "uz": "White Hat (Ethical Hacking) va Black Hat (kiberjinoyatchilik) o'rtasidagi asosiy qonuniy chegara nima?",
          "ru": "В чем заключается фундаментальная правовая граница между White Hat (этичным хакингом) и Black Hat?",
          "en": "What constitutes the fundamental legal boundary separating White Hat hacking from malicious Black Hat actions?"
        },
        "choices": [
          {
            "text": {
              "uz": "Tizim egasining oldindan bergan yozma ruxsati (Scope of Work / RoE); ruxsatsiz hatto bitta portni skanerlash ham O'zR JK 278-moddasi bo'yicha noqonuniydir.",
              "ru": "Письменное соглашение владельца (Scope of Work / RoE); несанкционированное сканирование незаконно (ст. 278 УК РУз).",
              "en": "Explicit written authorization (Scope of Work / RoE); unauthorized scanning violates CFAA and legal codes."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "Faqat ishlatiladigan dasturlash tilida: Python bo'lsa qonuniy, C++ bo'lsa noqonuniy.",
              "ru": "Исключительно в языке: Python легален, а C++ законен только для системщиков.",
              "en": "Strictly programming language choices: Python is legal, while C++ is unauthorized."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Hujumni tunda yoki kunduzi amalga oshirilganligida.",
              "ru": "В том, днем или ночью проводится аудит безопасности.",
              "en": "Whether the diagnostic scan is launched during daylight or nocturnal hours."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Agar tizimdan pul o'g'irlanmasa, har qanday saytni ruxsatsiz buzish qonuniydir.",
              "ru": "Если деньги не похищены, любой несанкционированный взлом законен.",
              "en": "Any penetration testing without authorization is permissible if no funds are stolen."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! Axloqiy xakerlikning oltin qoidasi — qat'iy yozma ruxsat va chegaralangan Scope of Work.",
          "ru": "Верно! Главный критерий White Hat — наличие письменного соглашения и утвержденных границ (Scope).",
          "en": "Correct! Legitimate ethical penetration mandates strict written Scope of Work."
        },
        "feedback_incorrect": {
          "uz": "Xato. Ruxsatsiz har qanday skanerlash yoki kiber-aralashuv jinoyat hisoblanadi.",
          "ru": "Неверно. Любые действия без официального разрешения преследуются по закону.",
          "en": "Incorrect. Any cyber interaction absent formal authorization constitutes unauthorized penetration."
        }
      },
      {
        "id": "q3",
        "points": 2,
        "title": {
          "uz": "Saytni Clickjacking (yashirin iframe orqali aldov) hujumlaridan himoyalash uchun qaysi HTTP sarlavhasi o'rnatiladi?",
          "ru": "Какой HTTP-заголовок предотвращает Clickjacking (встраивание сайта в скрытый iframe злоумышленника)?",
          "en": "Which HTTP security header guards web applications against Clickjacking iframe embedding attacks?"
        },
        "choices": [
          {
            "text": {
              "uz": "X-Frame-Options: DENY (yoki SAMEORIGIN) — saytni begonalar iframe ichida ochishini taqiqlaydi.",
              "ru": "X-Frame-Options: DENY (или SAMEORIGIN) — запрещает отображение страницы во фреймах сторонних сайтов.",
              "en": "X-Frame-Options: DENY (or SAMEORIGIN) — restricts the page from being rendered inside foreign iframes."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "Access-Control-Allow-Origin: * — barcha domenga to'liq ruxsat berish.",
              "ru": "Access-Control-Allow-Origin: * — разрешить запросы всем сайтам подряд.",
              "en": "Access-Control-Allow-Origin: * — unrestricted origin permissions."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Content-Type: text/plain — CSS stillarini o'chirib qo'yish.",
              "ru": "Content-Type: text/plain — отключение интерпретации HTML.",
              "en": "Content-Type: text/plain — disabling browser HTML rendering."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Cache-Control: no-cache — rasmlarni saqlamaslik.",
              "ru": "Cache-Control: no-cache — запрет кэширования медиафайлов.",
              "en": "Cache-Control: no-cache — preventing asset caching."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! X-Frame-Options va CSP frame-ancestors Clickjacking qopqonlarini butunlay to'xtatadi.",
          "ru": "Верно! X-Frame-Options: DENY гарантирует защиту от атак с кликджекингом.",
          "en": "Correct! X-Frame-Options: DENY thoroughly halts Clickjacking attacks."
        },
        "feedback_incorrect": {
          "uz": "Xato. Clickjacking ga qarshi X-Frame-Options: DENY sarlavhasi qo'yiladi.",
          "ru": "Неверно. Защиту от кликджекинга обеспечивает заголовок X-Frame-Options.",
          "en": "Incorrect. Clickjacking protection is enforced via X-Frame-Options."
        }
      },
      {
        "id": "q4",
        "points": 2,
        "title": {
          "uz": "Kiberxavfsizlikda zaiflik xavfini xalqaro baholovchi CVSS v3.1 tizimida maksimal ball nechaga teng va qaysi darajaga mos keladi?",
          "ru": "Чему равен максимальный балл в системе оценки уязвимостей CVSS v3.1 и какому уровню угрозы он соответствует?",
          "en": "What is the ceiling score in CVSS v3.1 rating system and which severity tier does it represent?"
        },
        "choices": [
          {
            "text": {
              "uz": "10.0 ball — eng yuqori Kritik (Critical) xavf darajasi.",
              "ru": "10.0 баллов — максимальный Критический (Critical) уровень опасности.",
              "en": "10.0 points — the maximum Critical vulnerability severity tier."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "100.0 ball — High darajasi.",
              "ru": "100.0 баллов — уровень High.",
              "en": "100.0 points — high severity level."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "5.0 ball — O'rtacha (Medium) darajasi.",
              "ru": "5.0 баллов — предел уровня Medium.",
              "en": "5.0 points — medium rating limit."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Cheksiz ball.",
              "ru": "Балл не имеет числового предела.",
              "en": "Scores scale infinitely without limits."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! CVSS shkalasi 0.0 dan 10.0 gacha bo'lib, 9.0–10.0 Kritik (Critical) hisoblanadi.",
          "ru": "Правильно! CVSS v3.1 оценивает уязвимости по шкале от 0.0 до 10.0 (9.0–10.0 — Critical).",
          "en": "Correct! CVSS v3.1 scales from 0.0 to 10.0, with 9.0–10.0 denoting Critical."
        },
        "feedback_incorrect": {
          "uz": "Xato. CVSS v3.1 ning eng yuqori ko'rsatkichi 10.0 (Critical) ball bilan chegaralangan.",
          "ru": "Неверно. Максимальный балл CVSS равен 10.0.",
          "en": "Incorrect. The top score of CVSS v3.1 is strictly 10.0."
        }
      }
    ]
  },
  {
    "cohort_id": "7-8-sinf",
    "cohort_name": {
      "uz": "7–8-Sinf · Game Dev & Algorithms",
      "ru": "7–8-Класс · Game Dev & Algorithms",
      "en": "Grades 7–8 · Game Dev & Algorithms"
    },
    "classes": ["7-A", "7-B", "8-A", "8-B"],
    "week_id": "7-hafta",
    "lesson_id": "29-dars-gps-navigatsiya-va-eng-qisqa-yol",
    "lesson_num": "29",
    "folder_path": "classes/7-8-sinf/7-hafta/29-dars-gps-navigatsiya-va-eng-qisqa-yol",
    "title": {
      "uz": "7–8-Sinf: 29-Dars GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi — Kiber-Test",
      "ru": "7–8-Класс: Урок 29 GPS Навигация и Алгоритм Кратчайшего Пути — Тест",
      "en": "Grades 7–8: Lesson 29 GPS Navigation & Shortest Path Algorithm — Quiz"
    },
    "description": {
      "uz": "Target International School // 7–8-Sinf // 7-Hafta // 29-Dars\nMavzu: Graf Nazariyasi, Dijkstra va A* Algoritmlari, Haversine Formulasi\nO'qituvchi: M. Musulmonov",
      "ru": "Target International School // 7–8-Класс // 7-я Неделя // Урок 29\nТема: Теория Графов, Алгоритмы Дейкстры и A*, Формула Гаверсинуса\nУчитель: М. Мусульмонов",
      "en": "Target International School // Grades 7–8 // Week 7 // Lesson 29\nTopic: Graph Theory, Dijkstra & A* Algorithms, Haversine Distance Formula\nInstructor: M. Musulmonov"
    },
    "questions": [
      {
        "id": "q1",
        "points": 3,
        "title": {
          "uz": "Google Maps yoki Yandex Go xaritasida shahar ko'chalari va chorrahalari qaysi ma'lumotlar tuzilmasi (Data Structure) yordamida dasturlanadi?",
          "ru": "С помощью какой структуры данных программируются улицы и перекрестки в Google Maps или Yandex Go?",
          "en": "Which fundamental Data Structure models street networks and intersections in navigation systems like Google Maps?"
        },
        "choices": [
          {
            "text": {
              "uz": "Vaznli yo'naltirilgan Graf (Weighted Directed Graph): chorrahalar — tugunlar (Vertices), ko'chalar — qirralar (Edges), masofa/tirbandlik — vaznlar (Weights).",
              "ru": "Взвешенный ориентированный Граф: перекрестки — вершины (Vertices), дороги — ребра (Edges), время/пробки — веса (Weights).",
              "en": "Weighted Directed Graph: intersections as vertices, streets as edges, travel distance/traffic as weights."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "Faqat bitta oddiy 1-o'lchamli massiv (Array).",
              "ru": "Обычный одномерный массив (Array).",
              "en": "A simple flat 1-dimensional array."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Oddiy matnli satr (String).",
              "ru": "Обычная строковая переменная (String).",
              "en": "A single continuous string scalar."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Faqat HTML jadvali (Table).",
              "ru": "Обычная HTML-таблица без логических связей.",
              "en": "An unstructured HTML table tag."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "Ofarin! Graf nazariyasi navigatsiya tizimlarining yuragi hisoblanadi.",
          "ru": "Отлично! Теория графов лежит в основе всех мировых систем навигации.",
          "en": "Bravo! Graph structures power global navigation engines."
        },
        "feedback_incorrect": {
          "uz": "Xato. Shahar navigatsiyasi vaznli yo'naltirilgan Graf orqali hisoblanadi.",
          "ru": "Неверно. Карта дорог моделируется в виде взвешенного графа.",
          "en": "Incorrect. Road networks are structured as weighted graphs."
        }
      },
      {
        "id": "q2",
        "points": 3,
        "title": {
          "uz": "Ikki nuqta orasidagi eng kam vaqt yoki eng qisqa masofani topishda qaysi mashhur kompyuter algoritmidan foydalaniladi?",
          "ru": "Какой знаменитый алгоритм используется для поиска быстрейшего или кратчайшего пути между двумя точками графа?",
          "en": "Which foundational computer algorithm discovers the optimal or shortest path between two graph nodes?"
        },
        "choices": [
          {
            "text": {
              "uz": "Dijkstra (Deykstra) va A* (A-Star) eng qisqa yo'l algoritmlari.",
              "ru": "Алгоритмы Дейкстры (Dijkstra) и A* (A-Star).",
              "en": "Dijkstra's shortest path and A* heuristic search algorithms."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "Bubble Sort (Pufakchali saralash).",
              "ru": "Пузырьковая сортировка (Bubble Sort).",
              "en": "Bubble Sort sorting algorithm."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Binary Search (ikkilik qidiruv).",
              "ru": "Бинарный поиск в массиве чисел.",
              "en": "Binary Search on sorted lists."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Math.random() orqali tasodifiy yo'l tanlash.",
              "ru": "Случайный выбор маршрута через Math.random().",
              "en": "Stochastic random path picking via Math.random()."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! Dijkstra algoritmi boshlang'ich nuqtadan barcha tugunlargacha bo'lgan optimal yo'lni aniqlaydi.",
          "ru": "Верно! Алгоритм Дейкстры математически гарантирует нахождение кратчайшего пути.",
          "en": "Correct! Dijkstra's algorithm mathematically guarantees optimal path traversal."
        },
        "feedback_incorrect": {
          "uz": "Xato. Eng qisqa yo'lni topish Dijkstra yoki A* algoritmi yordamida hisoblanadi.",
          "ru": "Неверно. Кратчайший путь рассчитывается алгоритмом Дейкстры или A*.",
          "en": "Incorrect. Shortest route discovery relies on Dijkstra or A*."
        }
      },
      {
        "id": "q3",
        "points": 2,
        "title": {
          "uz": "Yer sferik yuzasida ikki GPS koordinata (kenglik va uzunlik) orasidagi aniq masofani hisoblash formulasi nima deb ataladi?",
          "ru": "Как называется математическая формула для вычисления расстояния между двумя GPS координатами на сфере Земли?",
          "en": "What is the mathematical formula determining great-circle distance between two GPS coordinates across Earth's sphere?"
        },
        "choices": [
          {
            "text": {
              "uz": "Haversine (Gaversinus) formulasi — yer egriligini hisobga olgan holda to'g'ri chiziqli masofani beradi.",
              "ru": "Формула Гаверсинуса (Haversine) — учитывает сферическую кривизну Земли.",
              "en": "Haversine formula — accurately incorporates Earth's spherical curvature."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "Oddiy Pifagor teoremasi (a² + b² = c²) yer yuzida har doim 100% aniq ishlaydi.",
              "ru": "Обычная теорема Пифагора на плоской плоскости без погрешностей.",
              "en": "Simple planar Pythagorean theorem without any curvature adjustment."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Nyutonning butun olam tortishish qonuni.",
              "ru": "Закон всемирного тяготения Ньютона.",
              "en": "Newton's universal law of gravitation."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Eynshteynning E=mc² formulasi.",
              "ru": "Формула теории относительности Эйнштейна.",
              "en": "Einstein's mass-energy equivalence equation."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! Yer shar shaklida bo'lgani sababli GPS masofalari Haversine formulasi bilan hisoblanadi.",
          "ru": "Верно! Из-за сферической формы Земли точное расстояние рассчитывается по формуле Гаверсинуса.",
          "en": "Correct! Earth's spherical geometry necessitates the Haversine formula for exact distance."
        },
        "feedback_incorrect": {
          "uz": "Xato. Yer sferasidagi GPS masofasi Haversine formulasi orqali topiladi.",
          "ru": "Неверно. Расстояние между GPS точками рассчитывается по формуле Гаверсинуса.",
          "en": "Incorrect. GPS spherical distance calculation requires the Haversine formula."
        }
      },
      {
        "id": "q4",
        "points": 2,
        "title": {
          "uz": "Zamonaviy veb-brauzerda foydalanuvchining joriy GPS kenglik va uzunlik koordinatalarini olish uchun qaysi standart API chaqiriladi?",
          "ru": "Какой стандартный браузерный API используется для получения текущих GPS координат пользователя?",
          "en": "Which browser standard API retrieves the user's live GPS geographic coordinates?"
        },
        "choices": [
          {
            "text": {
              "uz": "navigator.geolocation.getCurrentPosition()",
              "ru": "navigator.geolocation.getCurrentPosition()",
              "en": "navigator.geolocation.getCurrentPosition()"
            },
            "correct": True
          },
          {
            "text": {
              "uz": "document.getElementById('gps').click()",
              "ru": "document.getElementById('gps').click()",
              "en": "document.getElementById('gps').click()"
            },
            "correct": False
          },
          {
            "text": {
              "uz": "window.localStorage.getItem('latitude')",
              "ru": "window.localStorage.getItem('latitude')",
              "en": "window.localStorage.getItem('latitude')"
            },
            "correct": False
          },
          {
            "text": {
              "uz": "console.log(process.env.GPS_COORDINATES)",
              "ru": "console.log(process.env.GPS_COORDINATES)",
              "en": "console.log(process.env.GPS_COORDINATES)"
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! W3C standarti bo'yicha Geolocation API navigator.geolocation orqali ishlaydi.",
          "ru": "Верно! Доступ к геолокации в браузере осуществляется через navigator.geolocation.",
          "en": "Correct! Browser GPS access is implemented via navigator.geolocation."
        },
        "feedback_incorrect": {
          "uz": "Xato. Geolokatsiya olish navigator.geolocation.getCurrentPosition() orqali bajariladi.",
          "ru": "Неверно. Стандартный метод геолокации — navigator.geolocation.getCurrentPosition().",
          "en": "Incorrect. Standard geolocation access requires navigator.geolocation.getCurrentPosition()."
        }
      }
    ]
  },
  {
    "cohort_id": "5-6-sinf",
    "cohort_name": {
      "uz": "5–6-Sinf · Kiber-Gigiyena & IT Asoslari",
      "ru": "5–6-Класс · Кибер-Гигиена и Основы IT",
      "en": "Grades 5–6 · Cyber Hygiene & IT Foundations"
    },
    "classes": ["5-A", "5-B", "6-A", "6-B"],
    "week_id": "7-hafta",
    "lesson_id": "21-dars-raqamli-iz-va-maxfiylik",
    "lesson_num": "21",
    "folder_path": "classes/5-6-sinf/7-hafta/21-dars-raqamli-iz-va-maxfiylik",
    "title": {
      "uz": "5–6-Sinf: 21-Dars Raqamli Iz va Shaxsiy Maxfiylik — Kiber-Test",
      "ru": "5–6-Класс: Урок 21 Цифровой След и Личная Конфиденциальность — Тест",
      "en": "Grades 5–6: Lesson 21 Digital Footprint & Personal Privacy — Quiz"
    },
    "description": {
      "uz": "Target International School // 5–6-Sinf // 7-Hafta // 21-Dars\nMavzu: Raqamli Iz, Katta Ekran Qoidasi, Fotosuratlardagi EXIF GPS Himoyasi\nO'qituvchi: M. Musulmonov",
      "ru": "Target International School // 5–6-Класс // 7-я Неделя // Урок 21\nТема: Цифровой След, Правило Большого Экрана, Защита EXIF GPS в Фотографиях\nУчитель: М. Мусульмонов",
      "en": "Target International School // Grades 5–6 // Week 7 // Lesson 21\nTopic: Digital Footprint, Billboard Rule, EXIF GPS Metadata Protection\nInstructor: M. Musulmonov"
    },
    "questions": [
      {
        "id": "q1",
        "points": 3,
        "title": {
          "uz": "Kiber-xavfsizlikdagi 'Katta Ekran Qoidasi' (Billboard Rule) nima haqida ogohlantiradi?",
          "ru": "О чем предупреждает «Правило Большого Экрана» (Billboard Rule) в кибербезопасности?",
          "en": "What does the 'Billboard Rule' in digital safety caution students about?"
        },
        "choices": [
          {
            "text": {
              "uz": "Internetga biron rasm yoki video joylashdan oldin: 'Agar bu rasm maktab darvozasidagi ulkan ekranda hamma ko'z o'ngida namoyish etilsa, uyalmaymanmi?' deb o'ylash kerak.",
              "ru": "Перед публикацией любого фото спросить себя: «Не будет ли мне стыдно, если этот снимок появится на гигантском билборде перед всей школой?».",
              "en": "Before posting, ask: 'Would I feel uncomfortable if this photo were displayed on a giant public billboard for the whole school to see?'."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "Faqat eng katta monitorli kompyuterlarni sotib olish kerakligini bildiradi.",
              "ru": "Означает, что нужно покупать мониторы только с максимальной диагональю.",
              "en": "Suggests buying strictly the largest computer monitors available."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Ijtimoiy tarmoqda hamma shaxsiy parollarni hammaga ko'rsatib qo'yish kerakligini.",
              "ru": "Требует открыто публиковать свои пароли на всеобщее обозрение.",
              "en": "Mandates posting your secret passwords openly on public walls."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Televizorni juda yaqindan ko'rmaslik qoidasini.",
              "ru": "Обычное правило не смотреть телевизор с близкого расстояния.",
              "en": "The general recommendation against sitting too close to a TV."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! Internetga kirgan narsa abadiy saqlanadi. Katta Ekran qoidasi sizni pushaymonlikdan asraydi.",
          "ru": "Верно! Все загруженное в сеть остается там навсегда. Это правило защищает репутацию.",
          "en": "Correct! Everything uploaded leaves a permanent trace. The billboard rule protects your future."
        },
        "feedback_incorrect": {
          "uz": "Xato. Katta Ekran qoidasi shaxsiy ma'lumotlarni ommaga o'ylamasdan tarqatmaslik haqida.",
          "ru": "Неверно. Правило учит взвешивать публичность каждого загружаемого файла.",
          "en": "Incorrect. The rule encourages prudent consideration before making media public."
        }
      },
      {
        "id": "q2",
        "points": 3,
        "title": {
          "uz": "Smartfonda rasmga olganda fotosurat ichiga yashirinib qoladigan va begonalarga uyingiz manzilini oshkor qiluvchi ma'lumot nima deb ataladi?",
          "ru": "Как называются скрытые метаданные внутри фотографии, сделанной на смартфон, которые могут раскрыть точный домашний адрес?",
          "en": "What is the hidden metadata embedded inside smartphone photos that can expose precise home coordinates to strangers?"
        },
        "choices": [
          {
            "text": {
              "uz": "EXIF Metama'lumotlari: unda aniq GPS koordinatalari, olingan sana, vaqt va telefon modeli yoziladi.",
              "ru": "EXIF Метаданные: содержат точные GPS координаты съемки, дату, время и модель устройства.",
              "en": "EXIF Metadata: records precise GPS coordinates, timestamp, and device hardware details."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "Faqat rasmning piksel o'lchamlari.",
              "ru": "Только визуальное разрешение картинки в пикселях.",
              "en": "Strictly the visual pixel resolution dimensions."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Kompyuter virusi.",
              "ru": "Обычный компьютерный вирус троян.",
              "en": "A malicious Trojan horse computer virus."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Wi-Fi paroli.",
              "ru": "Скрытый пароль от домашнего роутера.",
              "en": "The secret password of the home Wi-Fi."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! EXIF GPS metama'lumotlarini tarmoqqa yuklashdan oldin tozalash yoki kamerada joylashuvni o'chirib qo'yish kerak.",
          "ru": "Верно! EXIF-данные могут выдать домашний адрес. Всегда отключайте геолокацию камеры.",
          "en": "Correct! EXIF location tags leak residency coordinates. Strip EXIF before posting!"
        },
        "feedback_incorrect": {
          "uz": "Xato. Rasmdagi yashirin GPS koordinatalari EXIF deb ataladi.",
          "ru": "Неверно. Скрытые GPS координаты в фотографиях называются метаданными EXIF.",
          "en": "Incorrect. Hidden location coordinates in photos are called EXIF metadata."
        }
      },
      {
        "id": "q3",
        "points": 2,
        "title": {
          "uz": "Kafeda yoki bog'dagi ochiq bepul Wi-Fi tarmog'iga ulanganda shaxsiy hisob va parollarni o'g'irlanishdan asrashning eng ishonchli usuli qaysi?",
          "ru": "Какой самый надежный способ защитить пароли и переписку при подключении к открытому публичному Wi-Fi в кафе?",
          "en": "What is the most effective safeguard for protecting passwords and chats on open public Wi-Fi?"
        },
        "choices": [
          {
            "text": {
              "uz": "Ishonchli VPN (Virtual Private Network) yoqish va muhim bank ilovalariga kirmaslik.",
              "ru": "Включить проверенный VPN (Virtual Private Network) и не входить в банковские кабинеты.",
              "en": "Engage a trusted VPN (Virtual Private Network) and avoid logging into banking portals."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "Telefonni faqat quvvatlovchi simga ulab qo'yish.",
              "ru": "Подключить смартфон к кабелю быстрой зарядки.",
              "en": "Plugging the smartphone into a wall charger."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Ekran yorqinligini eng past darajaga tushirish.",
              "ru": "Снизить яркость экрана до минимума.",
              "en": "Dimming screen brightness to the minimum."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Bluetooth-ni o'chirib, ochiq saytlarda parollarni kiritaverish.",
              "ru": "Просто выключить Bluetooth и спокойно вводить пароли на незащищенных сайтах.",
              "en": "Disabling Bluetooth while submitting passwords over plain unencrypted web pages."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "To'g'ri! Ochiq Wi-Fi da ma'lumotlar shifrlanmagan bo'lishi mumkin. VPN trafikingizni shifrlangan tunnelga oladi.",
          "ru": "Правильно! В открытых сетях злоумышленники могут перехватить трафик. VPN шифрует весь канал.",
          "en": "Correct! Public Wi-Fi lacks encryption. A VPN secures your traffic through an encrypted tunnel."
        },
        "feedback_incorrect": {
          "uz": "Xato. Ochiq Wi-Fi da trafikni himoya qilish uchun VPN ishlatish shart.",
          "ru": "Неверно. Защиту трафика в публичных сетях обеспечивает VPN-туннелирование.",
          "en": "Incorrect. Safeguarding public Wi-Fi communication requires VPN tunneling."
        }
      },
      {
        "id": "q4",
        "points": 2,
        "title": {
          "uz": "Ijtimoiy tarmoqlarda profilingizni begona firibgarlardan himoyalashning eng samarali 2 ta kiber-qoidasi qaysi?",
          "ru": "Какие 2 ключевых правила кибербезопасности надежнее всего защищают аккаунты в соцсетях от мошенников?",
          "en": "Which 2 essential cybersecurity practices best shield social media profiles against bad actors?"
        },
        "choices": [
          {
            "text": {
              "uz": "Profilni 'Yopiq (Private)' rejimiga o'tkazish va ikki bosqichli autentifikatsiyani (2FA) yoqish.",
              "ru": "Сделать профиль «Закрытым (Private)» и включить двухфакторную аутентификацию (2FA).",
              "en": "Switch account visibility to 'Private' and enforce Two-Factor Authentication (2FA)."
            },
            "correct": True
          },
          {
            "text": {
              "uz": "Parolni '123456' qilib qo'yish va begona odamlarni do'stlikka qabul qilaverish.",
              "ru": "Установить пароль «123456» и принимать всех незнакомцев в друзья.",
              "en": "Setting password to '123456' and accepting all stranger requests."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Har kuni telefon raqami va uy manzilini statusga yozib borish.",
              "ru": "Ежедневно публиковать свой номер телефона и домашний адрес в статусе.",
              "en": "Posting home address and phone contact in status updates every day."
            },
            "correct": False
          },
          {
            "text": {
              "uz": "Profil rasmini umuman qo'ymaslik, lekin parolni do'stlarga aytish.",
              "ru": "Не ставить аватарку, но делиться паролем со всеми одноклассниками.",
              "en": "Leaving avatar blank while sharing credentials with classmates."
            },
            "correct": False
          }
        ],
        "feedback_correct": {
          "uz": "Ofarin! Yopiq profil va 2FA — profilingizni o'g'irlanishdan 99% asraydi.",
          "ru": "Превосходно! Закрытый профиль и 2FA предотвращают 99% попыток взлома.",
          "en": "Splendid! A private profile combined with 2FA repels 99% of hijacking attempts."
        },
        "feedback_incorrect": {
          "uz": "Xato. Kiber-gigiyena qoidasi: profilni yopiq qilish va 2FA ni faollashtirish.",
          "ru": "Неверно. Базовые правила: приватный профиль и обязательное включение 2FA.",
          "en": "Incorrect. Baseline digital hygiene prescribes private visibility and 2FA."
        }
      }
    ]
  }
]

with open('scripts/google_forms_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_ids = {item['lesson_id'] for item in data}

added = 0
for exam in NEW_EXAMS:
    if exam['lesson_id'] not in existing_ids:
        data.append(exam)
        existing_ids.add(exam['lesson_id'])
        added += 1

with open('scripts/google_forms_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {added} new exams to scripts/google_forms_data.json! Total now: {len(data)}")
