# -*- coding: utf-8 -*-
"""9-sinf · 4-hafta · 18-dars — Ma'lumotlar Bazasi va SQL: Relyatsion Arxitektura, Indekslar va Xavfsizlik."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/9-sinf/4-hafta/18-dars-malumotlar-bazasi-va-sql"

TITLES = {
    "uz": "18-dars: Ma'lumotlar Bazasi va SQL — Relyatsion Arxitektura, Indekslar va Xavfsizlik",
    "ru": "Урок 18: Базы Данных и SQL — Реляционная Архитектура, Индексы и Безопасность",
    "en": "Lesson 18: Databases and SQL — Relational Architecture, Indexing and Security",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("Vibecoding · 18-dars · 9-sinf (Backend & Data Track)",
             "Vibecoding · Урок 18 · 9 класс (Backend & Data Track)",
             "Vibecoding · Lesson 18 · Grade 9 (Backend & Data Track)"),
    h1=("Ma'lumotlar Bazasi va SQL: Relyatsion Arxitektura va Xavfsizlik",
        "Базы Данных и SQL: Реляционная Архитектура и Безопасность",
        "Databases & SQL: Relational Architecture, Indexing & Security"),
    lede=("Oddiy fayllar (JSON, CSV) millionlab foydalanuvchilar bir vaqtda yozganda buziladi, "
          "xotiradan toshib ketadi va ma'lumotlarni yo'qotadi. Bugungi darsda zamonaviy IT infratuzilmaning "
          "yuragi bo'lgan <b>Relyatsion Ma'lumotlar Bazasi (RDBMS)</b>, <b>ACID tamoyillari</b>, "
          "<b>SQL so'rovlari</b>, <b>B-Tree indekslar</b> va eng xavfli hujumlardan biri — "
          "<b>SQL Injection</b>dan 100% himoyalanishni o'rganamiz.",
          "Обычные файлы (JSON, CSV) ломаются при одновременной записи миллионами пользователей, "
          "переполняют память и теряют данные. Сегодня мы изучим сердце любой IT-инфраструктуры — "
          "<b>Реляционные СУБД (RDBMS)</b>, <b>принципы ACID</b>, <b>запросы SQL</b>, "
          "<b>B-Tree индексы</b> и абсолютную защиту от критической уязвимости — <b>SQL Injection</b>.",
          "Flat files (JSON, CSV) corrupt under concurrent multi-user writes, exhaust server RAM, and lose state. "
          "Today we explore the bedrock of enterprise infrastructure: <b>Relational DBMS (RDBMS)</b>, "
          "<b>ACID guarantees</b>, <b>relational SQL queries</b>, <b>B-Tree indexing</b>, and absolute protection "
          "against devastating <b>SQL Injection</b> attacks using parameterized statements."),
    meta=[("<b>Fan:</b> Vibecoding · Backend Muhandislik",
           "<b>Предмет:</b> Vibecoding · Backend-инженерия",
           "<b>Subject:</b> Vibecoding · Backend Engineering"),
          ("<b>Kohorta:</b> 9-sinf Junior Vibecoder",
           "<b>Когорта:</b> 9 класс Junior Vibecoder",
           "<b>Cohort:</b> Grade 9 Junior Vibecoder"),
          ("<b>Hafta:</b> 4 (2-soat)", "<b>Неделя:</b> 4 (2-й час)", "<b>Week:</b> 4 (Hour 2)")],
))

# 2. Problem: Why Files Fail & ACID Guarantees
S.append(slide(
    ph=("Arxitektura", "Архитектура", "Architecture"), time="3–6",
    eyebrow=("Ma'lumotlar yaxlitligi", "Целостность данных", "Data integrity fundamentals"),
    title=("Nega JSON Fayl Emas? ACID Standarti",
           "Почему Не JSON-Файлы? Стандарт ACID",
           "Why Not Plain JSON Files? The ACID Guarantee"),
    body='<div class="cols c2">\n'
         + box("accent", ("JSON/CSV fayllarning halokatli cheklovlari",
                          "Критические изъяны плоских файлов (JSON/CSV)",
                          "Fatal flaws of flat files (JSON/CSV)"),
               items=[
                   ("<b>Race Condition:</b> 2 kishi bir vaqtda faylga yozsa, birining ma'lumoti butunlay o'chib ketadi.",
                    "<b>Гонка данных:</b> При одновременной записи двумя клиентами файл перезаписывается и теряет данные.",
                    "<b>Race conditions:</b> Concurrent writes corrupt file descriptors and overwrite data."),
                   ("<b>Xotira to'lishi:</b> 500 MB fayldan 1 ta foydalanuvchini topish uchun butun fayl RAMga yuklanadi.",
                    "<b>Утечка памяти:</b> Поиск 1 записи требует парсинга всего 500 МБ JSON в оперативную память.",
                    "<b>RAM bottleneck:</b> Searching 1 record forces parsing the entire 500MB JSON into memory."),
                   ("<b>Munosabatlar yo'qligi:</b> Foydalanuvchi o'chsa, uning xaridlari faylda yetim (ghost) bo'lib qoladi.",
                    "<b>Нет связности:</b> Удаление юзера оставляет «висячие» заказы без целостности.",
                    "<b>No foreign keys:</b> Deleting a user leaves orphaned ghost records scattered across files."),
               ])
         + "\n"
         + box("green", ("RDBMS va ACID kafolatlari (PostgreSQL, SQLite)",
                         "Гарантии RDBMS и ACID (PostgreSQL, SQLite)",
                         "RDBMS and ACID guarantees (PostgreSQL, SQLite)"),
               items=[
                   ("<b>A — Atomicity:</b> Tranzaksiya yo 100% bajariladi, yoki butunlay bekor bo'ladi (ROLLBACK).",
                    "<b>A — Атомарность:</b> Транзакция выполняется либо на 100%, либо отменяется полностью (ROLLBACK).",
                    "<b>A — Atomicity:</b> All operations succeed completely, or the transaction rolls back cleanly."),
                   ("<b>C — Consistency:</b> Sxema qoidalari (NOT NULL, CHECK, FK) hech qachon buzilmaydi.",
                    "<b>C — Согласованность:</b> Ограничения схемы (NOT NULL, CHECK, FK) соблюдаются строго.",
                    "<b>C — Consistency:</b> Schema rules, unique constraints, and foreign keys are never violated."),
                   ("<b>I — Isolation:</b> Parallel so'rovlar bir-birining oraliq holatini ko'rmaydi.",
                    "<b>I — Изоляция:</b> Параллельные транзакции не видят незавершённых изменений друг друга.",
                    "<b>I — Isolation:</b> Concurrent transactions cannot read dirty or uncommitted state."),
                   ("<b>D — Durability:</b> Server o'chib qolsa ham, tasdiqlangan (COMMIT) ma'lumot diskda saqlanib qoladi.",
                    "<b>D — Долговечность:</b> Зафиксированные (COMMIT) данные выживают даже при отключении питания.",
                    "<b>D — Durability:</b> Committed transactions persist to non-volatile storage despite power loss."),
               ])
         + "\n</div>",
))

# 3. Relational Schema & Keys
S.append(slide(
    ph=("Modellashtirish", "Моделирование", "Data Modeling"), time="6–9",
    eyebrow=("Relyatsion tuzilma", "Реляционная структура", "Relational structure"),
    title=("Jadvallar, Primary Key va Foreign Key",
           "Таблицы, Primary Key и Foreign Key",
           "Tables, Primary Keys, and Foreign Keys"),
    body='<div class="cols c2">\n'
         + box("ink", ("Primary Key (Birlamchi Kalit — PK)",
                       "Primary Key (Первичный Ключ — PK)",
                       "Primary Key (PK)"),
               items=[
                   ("<b>Unikal identifikator:</b> Har bir satrni yagona qilib ajratib turadi (masalan: `id SERIAL` yoki `UUID`).",
                    "<b>Уникальный идентификатор:</b> Однозначно определяет каждую строку (например, `id SERIAL` или `UUID`).",
                    "<b>Unique ID:</b> Uniquely identifies each row in a table (`id SERIAL` or `UUID`)."),
                   ("<b>Takrorlanmaslik kafolati:</b> Baza bir xil PK ga ega ikki yozuv kiritilishiga yo'l qo'ymaydi.",
                    "<b>Защита от дублей:</b> База гарантирует невозможность создания двух строк с одинаковым PK.",
                    "<b>Uniqueness enforcement:</b> The engine blocks duplicate keys with hardware-level constraint checks."),
                   ("<b>Tezkor qidiruv:</b> PK avtomatik B-Tree indeks bilan himoyalanadi.",
                    "<b>Молниеносный поиск:</b> По первичному ключу автоматически создаётся B-Tree индекс.",
                    "<b>Clustered index:</b> Clustered index ensures O(log N) retrieval speed by default."),
               ])
         + "\n"
         + box("accent", ("Foreign Key (Tashqi Kalit — FK)",
                          "Foreign Key (Внешний Ключ — FK)",
                          "Foreign Key (FK)"),
               items=[
                   ("<b>Jadvallararo ko'prik:</b> Bir jadvaldagi satrni boshqa jadval PK si bilan bog'laydi.",
                    "<b>Мост между таблицами:</b> Связывает строку одной таблицы с первичным ключом другой.",
                    "<b>Relational glue:</b> References the primary key of another table to maintain lineage."),
                   ("<b>1-to-Many munosabat:</b> 1 ta mijoz (`users.id`) 100 ta buyurtma (`orders.user_id`) qilishi mumkin.",
                    "<b>Связь 1-ко-Многим:</b> Один пользователь (`users.id`) может иметь сотни заказов (`orders.user_id`).",
                    "<b>1-to-Many mapping:</b> One customer (`users.id`) owns many orders (`orders.user_id`)."),
                   ("<b>ON DELETE CASCADE:</b> Mijoz hisobi o'chirilganda, unga tegishli barcha buyurtmalar ham avtomatik tozalanadi.",
                    "<b>ON DELETE CASCADE:</b> При удалении клиента база может автоматически очистить все его заказы.",
                    "<b>Cascading actions:</b> `ON DELETE CASCADE` prunes child rows automatically when a parent is deleted."),
               ])
         + "\n</div>",
))

# 4. DDL & Schema Creation
S.append(slide(
    ph=("DDL", "DDL", "DDL"), time="9–12",
    eyebrow=("Sxema yaratish", "Создание схемы", "Schema definition"),
    title=("Jadvallar Tuzish: Cheklovlar va Turlar",
           "Создание Таблиц: Ограничения и Типы",
           "Table Definition: Types & Integrity Constraints"),
    body='<div class="cols c2">\n'
         + code("""-- 1. Foydalanuvchilar jadvali\n
CREATE TABLE users (\n
    id SERIAL PRIMARY KEY,\n
    email VARCHAR(255) NOT NULL UNIQUE,\n
    full_name VARCHAR(100) NOT NULL,\n
    balance NUMERIC(10, 2) DEFAULT 0.00 CHECK (balance >= 0),\n
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n
);\n\n
-- 2. Buyurtmalar jadvali (FK bilan)\n
CREATE TABLE orders (\n
    id SERIAL PRIMARY KEY,\n
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,\n
    total_price NUMERIC(10, 2) NOT NULL CHECK (total_price > 0),\n
    status VARCHAR(20) DEFAULT 'pending',\n
    ordered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n
);
""")
         + "\n"
         + box("ink", ("Sxema cheklovlarining vazifasi", "Назначение ограничений схемы", "Constraint architecture"),
               items=[
                   ("<b>NOT NULL:</b> Qiymatsiz (bo'sh) ustunlar kiritilishini qat'iy taqiqlaydi.",
                    "<b>NOT NULL:</b> Запрещает сохранение неопределённых пустых значений.",
                    "<b>NOT NULL:</b> Disallows insertion of null or uninitialized record attributes."),
                   ("<b>UNIQUE:</b> Tizimda bitta email bilan 2 marta ro'yxatdan o'tishning oldini oladi.",
                    "<b>UNIQUE:</b> Исключает регистрацию двух пользователей с одинаковым email.",
                    "<b>UNIQUE:</b> Enforces database-level uniqueness across email and identity columns."),
                   ("<b>CHECK:</b> Mantiqiy cheklov — balans yoki narx manfiy bo'lishiga aslo yo'l qo'ymaydi.",
                    "<b>CHECK:</b> Запрещает логические ошибки, например, отрицательный баланс.",
                    "<b>CHECK:</b> Validates business rules at engine level (e.g. balance cannot be negative)."),
               ])
         + "\n</div>",
))

# 5. DML: CRUD Operations
S.append(slide(
    ph=("DML", "DML", "DML"), time="12–15",
    eyebrow=("Ma'lumotlar bilan ishlash", "Манипуляция данными", "Data manipulation"),
    title=("CRUD Operatsiyalari va Tranzaksiyalar",
           "Операции CRUD и Транзакции",
           "CRUD Operations and Transactions"),
    body='<div class="cols c2">\n'
         + code("""-- C (Create): Ma'lumot kiritish\n
INSERT INTO users (email, full_name, balance)\n
VALUES ('jasur@target.uz', 'Jasur Aliyev', 500000.00);\n\n
-- R (Read): Tanlash va saralash\n
SELECT id, full_name, balance FROM users\n
WHERE balance > 100000\n
ORDER BY balance DESC LIMIT 10;\n\n
-- U (Update) & D (Delete)\n
UPDATE users SET balance = balance - 50000 WHERE id = 1;\n
DELETE FROM orders WHERE status = 'cancelled';
""")
         + "\n"
         + box("accent", ("Xavfsiz Tranzaksiya (BEGIN / COMMIT)",
                          "Безопасная Транзакция (BEGIN / COMMIT)",
                          "Atomic Transaction (BEGIN / COMMIT)"),
               items=[
                   ("<b>Bank o'tkazmasi muammosi:</b> 1-odamdan pul yechilib, 2-odamga yetmasdan server o'chsa nima bo'ladi?",
                    "<b>Проблема перевода:</b> Что если с баланса А списали, а на баланс Б зачислить не успели из-за сбоя?",
                    "<b>Transfer dilemma:</b> What if sender is debited, but recipient crashes before crediting?"),
                   ("<b>BEGIN TRANSACTION:</b> Tranzaksiya ochiladi, barcha oraliq hisob-kitoblar xavfsiz tamponda bajariladi.",
                    "<b>BEGIN:</b> Открывает транзакцию, изолируя все промежуточные действия.",
                    "<b>BEGIN:</b> Opens atomic boundary, staging operations in transactional memory."),
                   ("<b>COMMIT:</b> Hammasi muvaffaqiyatli o'tsagina diskka muhrlanadi. Xato bo'lsa: <b>ROLLBACK</b> barchasini orqaga qaytaradi.",
                    "<b>COMMIT:</b> Фиксирует результат на диск. При ошибке: <b>ROLLBACK</b> откатывает всё назад.",
                    "<b>COMMIT or ROLLBACK:</b> Persists atomically to disk; rolls back to pristine state upon any fault."),
               ])
         + "\n</div>",
))

# 6. JOINs: Connecting Data
S.append(slide(
    ph=("JOIN", "JOIN", "JOIN"), time="15–18",
    eyebrow=("Jadvallarni birlashtirish", "Объединение таблиц", "Relational joins"),
    title=("INNER JOIN va LEFT JOIN Farqi",
           "Разница Между INNER JOIN и LEFT JOIN",
           "Querying Across Tables: INNER vs LEFT JOIN"),
    body='<div class="cols c2">\n'
         + code("""-- INNER JOIN: Faqat buyurtmasi bor foydalanuvchilar\n
SELECT users.full_name, orders.id AS order_id, orders.total_price\n
FROM users\n
INNER JOIN orders ON users.id = orders.user_id;\n\n
-- LEFT JOIN: Barcha foydalanuvchilar (hatto buyurtmasi yo'qlar ham)\n
SELECT users.full_name, COUNT(orders.id) AS total_orders\n
FROM users\n
LEFT JOIN orders ON users.id = orders.user_id\n
GROUP BY users.id, users.full_name;
""")
         + "\n"
         + box("green", ("Qaysi birini qachon ishlatamiz?",
                         "Когда что применять?",
                         "Architectural selection criteria"),
               items=[
                   ("<b>INNER JOIN:</b> Faqat har ikki jadvalda ham mos keluvchi satrlar bo'lsa qaytaradi. Buyurtmasiz foydalanuvchilar chiqmaydi.",
                    "<b>INNER JOIN:</b> Возвращает только пересечение — пользователей, у которых точно есть заказы.",
                    "<b>INNER JOIN:</b> Strict intersection: returns records that match criteria on both sides."),
                   ("<b>LEFT JOIN:</b> Chap jadvaldagi barcha yozuvlarni oladi. Buyurtma bo'lmasa `NULL` qiymat qo'yadi. Foydalanuvchilar statistikasi uchun ideal.",
                    "<b>LEFT JOIN:</b> Берёт всех юзеров слева; если заказов нет, подставляет `NULL`. Идеально для отчётов.",
                    "<b>LEFT JOIN:</b> Preserves all parent rows from left table, inserting `NULL` for missing children."),
               ])
         + "\n</div>",
))

# 7. Performance & Indexing: B-Tree
S.append(slide(
    ph=("Indekslar", "Индексы", "Performance"), time="18–21",
    eyebrow=("Unumdorlik muhandisligi", "Инженерия скорости", "Performance engineering"),
    title=("B-Tree Indekslar: 800ms dan 1ms gacha",
           "B-Tree Индексы: Ускорение с 800мс до 1мс",
           "B-Tree Indexing: Slashing 800ms to 1ms"),
    body='<div class="cols c2">\n'
         + box("accent", ("Sequential Scan (Indekssiz — O(N))",
                          "Sequential Scan (Без индекса — O(N))",
                          "Sequential Scan (No Index — O(N))"),
               items=[
                   ("<b>To'liq ko'rib chiqish:</b> Agar email ustunida indeks bo'lmasa, baza 1 000 000 satrni diskdan birma-bir o'qiydi.",
                    "<b>Полное сканирование:</b> Без индекса СУБД считывает с диска все 1 000 000 строк по очереди.",
                    "<b>Full disk scan:</b> Without an index, the engine inspects all 1,000,000 rows sequentially."),
                   ("<b>CPU va Disk qizishi:</b> Har bir `SELECT` so'rovi server resurslarini so'rib oladi va 800–1200ms vaqt sarflaydi.",
                    "<b>Перегрузка CPU и диска:</b> Каждый запрос тратит сотни миллисекунд и забивает дисковый ввод-вывод.",
                    "<b>High latency:</b> Queries crawl at 800–1200ms under load, choking CPU and disk I/O."),
               ])
         + "\n"
         + box("green", ("B-Tree Index Scan (Indeksli — O(log N))",
                          "B-Tree Index Scan (С индексом — O(log N))",
                          "B-Tree Index Scan (With Index — O(log N))"),
               items=[
                   ("<b>B-Tree daraxti:</b> `CREATE INDEX idx_users_email ON users(email);` buyrug'i saralangan ko'rsatkich daraxti quradi.",
                    "<b>Дерево поиска:</b> Команда `CREATE INDEX` создаёт сбалансированное дерево указателей.",
                    "<b>Balanced tree:</b> `CREATE INDEX` builds a balanced B-Tree pointer structure."),
                   ("<b>Millisekundlik javob:</b> 1 million yozuv orasidan qidirish bor-yo'g'i ~20 ta taqqoslash bilan 1ms da bajariladi.",
                    "<b>1 миллисекунда:</b> Поиск среди миллиона записей требует всего ~20 сравнений и занимает 1мс.",
                    "<b>Sub-millisecond:</b> Finds any record out of 1,000,000 within ~20 comparisons in under 1ms."),
                   ("<b>Indeks to'lovi:</b> Indekslar diskdan qo'shimcha joy oladi va `INSERT` amalini biroz sekinlashtiradi. Faqat kerakli ustunlarga qo'yiladi.",
                    "<b>Цена индекса:</b> Замедляет вставку (`INSERT`) и занимает диск. Создаётся только на частые фильтры.",
                    "<b>Trade-off:</b> Adds storage overhead and slightly slows down `INSERT` operations."),
               ])
         + "\n</div>",
))

# 8. Cybersecurity: SQL Injection & Prepared Statements
S.append(slide(
    ph=("Kiberxavfsizlik", "Кибербезопасность", "Cybersecurity"), time="21–25",
    eyebrow=("Zararli so'rovlar", "Вредоносные запросы", "Exploit mechanics"),
    title=("SQL Injection: Buzg'unchilik va 100% Himoya",
           "SQL-Инъекция: Механизм Взлома и 100% Защита",
           "SQL Injection: Exploit Vectors and Parameterized Defense"),
    body='<div class="cols c2">\n'
         + code("""// ❌ XAVFLI: String konkatenatsiyasi (SQL Injection)\n
const userEmail = req.body.email; // Kiritildi: ' OR '1'='1\n
const query = `SELECT * FROM users WHERE email = '${userEmail}'`;\n
// Baza bajaradi: SELECT * FROM users WHERE email = '' OR '1'='1'\n
// NATIJA: Barcha foydalanuvchilar parollari o'g'irlanadi!\n\n
// ✅ 100% XAVFSIZ: Parameterized Query (Prepared Statement)\n
const safeQuery = 'SELECT * FROM users WHERE email = $1';\n
const result = await db.query(safeQuery, [userEmail]);\n
// Baza foydalanuvchi kiritgan matnni HECH QACHON kod deb o'ylamaydi!
""")
         + "\n"
         + box("accent", ("Nega Prepared Statement yengilmas?",
                          "Почему Параметризация абсолютно надёжна?",
                          "Why Prepared Statements are unassailable"),
               items=[
                   ("<b>Kod va Ma'lumot ajratiladi:</b> SQL mantiq serverda oldindan kompilyatsiya qilinadi.",
                    "<b>Разделение кода и данных:</b> SQL-шаблон компилируется сервером до подстановки данных.",
                    "<b>AST separation:</b> The SQL query AST is compiled before parameters are bound."),
                   ("<b>Belgilar zararsizlantiriladi:</b> Kiritilgan tirnoqlar (`'`), nuqta-vergul (`;`) faqat oddiy matn sifatida qabul qilinadi.",
                    "<b>Символы экранируются:</b> Кавычки и спецсимволы воспринимаются исключительно как текстовый литерал.",
                    "<b>Literal isolation:</b> Quotes, dashes, and semicolons are treated solely as raw text literals."),
                   ("<b>Sanoat standarti:</b> Hech bir professional dasturchi SQL so'rovini qo'lda matn qo'shib yozmaydi.",
                    "<b>Золотой стандарт:</b> Ни один профессиональный разработчик не склеивает SQL строками.",
                    "<b>Enterprise rule:</b> String concatenation in SQL statements is strictly barred by linters and CI/CD."),
               ])
         + "\n</div>",
))

# 9. Mission Briefing
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-on"), time="25–28",
    eyebrow=("12 daqiqalik laboratoriya", "12-минутная лаборатория", "12-minute lab"),
    title=("Amaliy Missiya: Relyatsion Baza Loyihalash va Xavfsiz Qidiruv",
           "Практическая Миссия: Реляционная База и Безопасный Поиск",
           "Hands-on Mission: Relational Modeling and Hardened Queries"),
    body='<div class="cols c2">\n'
         + box("accent", ("Missiya topshiriqlari", "Задачи миссии", "Mission requirements"),
               items=[
                   ("<b>1. DDL Sxema:</b> `users` va `orders` jadvallarini PK, FK va CHECK cheklovlari bilan yarating.",
                    "<b>1. DDL Схема:</b> Создайте таблицы `users` и `orders` с PK, FK и CHECK-ограничениями.",
                    "<b>1. DDL Schema:</b> Create `users` and `orders` tables with PK, FK, and CHECK constraints."),
                   ("<b>2. ACID Tranzaksiya:</b> `BEGIN ... COMMIT` bilan yangi buyurtma va balans yechish amalini yozing.",
                    "<b>2. ACID Транзакция:</b> Напишите атомарный перевод с `BEGIN ... COMMIT`.",
                    "<b>2. ACID Transaction:</b> Author an atomic transfer utilizing `BEGIN ... COMMIT`."),
                   ("<b>3. JOIN Tahlili:</b> Barcha foydalanuvchilar va ularning jami xarajatlarini hisoblovchi LEFT JOIN so'rovini quring.",
                    "<b>3. JOIN Анализ:</b> Напишите LEFT JOIN для подсчёта общей суммы заказов каждого пользователя.",
                    "<b>3. Relational Aggregation:</b> Write a LEFT JOIN with SUM/COUNT aggregating customer spending."),
                   ("<b>4. Kiber-Himoya:</b> Berilgan zaif so'rovni Prepared Statement holatiga o'tkazing.",
                    "<b>4. Защита:</b> Перепишите уязвимый конкатенированный запрос в безопасный параметризованный вид.",
                    "<b>4. Defense Refactor:</b> Refactor a vulnerable query into an exploit-proof prepared statement."),
               ])
         + "\n"
         + box("ink", ("Laboratoriya Ish Maydoni", "Рабочая лаборатория", "Workstation Lab"),
               items=[
                   ("<b>Muhit:</b> Terminalda PostgreSQL yoki SQLite CLI (`sqlite3 test.db`).",
                    "<b>Среда:</b> Терминал PostgreSQL или SQLite CLI (`sqlite3 test.db`).",
                    "<b>Environment:</b> PostgreSQL / SQLite CLI sandbox (`sqlite3 test.db`)."),
                   ("<b>Qog'oz varaqa:</b> Natijalarni ish varaqasiga qayd eting va xulosalarni yozing.",
                    "<b>Рабочий лист:</b> Фиксируйте этапы и SQL-запросы в распечатанном бланке.",
                    "<b>Telemetry worksheet:</b> Record query syntaxes and explain outputs on the physical sheet."),
               ])
         + "\n</div>",
))

# 10. Live Timer
S.append(slide(
    ph=("Taymer", "Таймер", "Timer"), time="28–37",
    eyebrow=("Mustaqil amaliy ish", "Самостоятельная работа", "Independent lab"),
    title=("Laboratoriya Ishi: 12 Daqiqa",
           "Лабораторная Работа: 12 Минут",
           "Laboratory Execution: 12 Minutes"),
    body='<div class="timer-card" data-timer="720">\n'
         + '  <div class="timer-display">12:00</div>\n'
         + '  <div class="timer-controls">\n'
         + '    <button class="navbtn" data-action="start" '
         + i18n("Boshlash", "Старт", "Start") + '>Boshlash</button>\n'
         + '    <button class="navbtn" data-action="pause" '
         + i18n("Pauza", "Пауза", "Pause") + '>Pauza</button>\n'
         + '    <button class="navbtn" data-action="reset" '
         + i18n("Qaytarish", "Сброс", "Reset") + '>Qaytarish</button>\n'
         + '  </div>\n'
         + '  <p style="color:var(--ink-2); font-size:13px; margin-top:14px;" '
         + i18n("Terminalda jadvallarni yarating, JOIN so'rovlarini tekshiring va varaqani to'ldiring.",
                "Создайте таблицы в терминале, протестируйте JOIN и заполните рабочий лист.",
                "Execute table creation, test JOIN queries, and complete your verification sheet.")
         + ">Terminalda jadvallarni yarating, JOIN so'rovlarini tekshiring va varaqani to'ldiring.</p>\n"
         + '</div>',
))

# 11. ORM vs Raw SQL
S.append(slide(
    ph=("Ilg'or", "Продвинутый", "Advanced"), time="37–41",
    eyebrow=("Zamonaviy backend vositalari", "Современный бэкенд стек", "Modern backend toolchain"),
    title=("Raw SQL vs ORM (Prisma / Drizzle / TypeORM)",
           "Чистый SQL против ORM (Prisma / Drizzle)",
           "Raw SQL vs Modern ORMs (Prisma / Drizzle)"),
    body='<div class="cols c2">\n'
         + code("""// Prisma ORM orqali turga mos (Type-safe) so'rov\n
const userWithOrders = await prisma.user.findUnique({\n
  where: { email: 'jasur@target.uz' },\n
  include: {\n
    orders: {\n
      where: { status: 'completed' },\n
      orderBy: { total_price: 'desc' }\n
    }\n
  }\n
});\n
// TypeScript xatolarni kod yozish jarayonidayoq ushlaydi!
""")
         + "\n"
         + box("ink", ("Taqqoslash va Tavsiyalar", "Сравнение и Рекомендации", "Trade-off analysis"),
               items=[
                   ("<b>Raw SQL (Sof SQL):</b> Eng yuqori tezlik va 100% nazorat. Murakkab hisobotlar va tahliliy so'rovlar uchun tengsiz.",
                    "<b>Чистый SQL:</b> Максимальная производительность и абсолютный контроль. Незаменим для сложных отчётов.",
                    "<b>Raw SQL:</b> Peak runtime performance and full query plan control. Optimal for analytical reporting."),
                   ("<b>Zamonaviy ORM:</b> Ishlab chiqish tezligi 3 barobar oshadi, avtomatik migratsiyalar va TypeScript tiplashtirish kafolati.",
                    "<b>ORM (Prisma/Drizzle):</b> Скорость разработки в 3 раза выше, авто-миграции и автодополнение типов.",
                    "<b>Modern ORMs:</b> 3x faster developer velocity, type safety, and painless schema migrations."),
                   ("<b>Qoida:</b> Oddiy CRUD uchun ORM, yuqori yuklamali va murakkab hisob-kitoblar uchun sof SQL.",
                    "<b>Правило:</b> Для стандартного CRUD — ORM, для высоконагруженных выборок — чистый SQL.",
                    "<b>Industry golden rule:</b> Use ORMs for day-to-day CRUD, lean on raw SQL for heavy query plans."),
               ])
         + "\n</div>",
))

# 12. Conclusion & 10-Point Rubric
S.append(slide(
    ph=("Xulosa", "Итоги", "Conclusion"), time="41–45",
    eyebrow=("Dars yakuni va baholash", "Итоги урока и оценка", "Lesson recap & grading"),
    title=("Xulosa va Baholash Mezoni (10 Ball)",
           "Итоги и Критерии Оценки (10 Баллов)",
           "Key Takeaways & 10-Point Rubric"),
    body='<div class="cols c2">\n'
         + box("green", ("Bugungi asosiy xulosalar", "Главные выводы урока", "Core engineering principles"),
               items=[
                   ("<b>RDBMS o'rnini hech narsa bosa olmaydi:</b> ACID kafolatlari ma'lumotlar yo'qolishiga yo'l qo'ymaydi.",
                    "<b>RDBMS незаменима:</b> Гарантии ACID обеспечивают надёжность сохранения данных под любой нагрузкой.",
                    "<b>RDBMS is irreplaceable:</b> ACID guarantees prevent corruption under severe concurrency."),
                   ("<b>Relyatsion aloqalar:</b> PK va FK jadvallar o'rtasida toza va yaxlit bog'lanish yaratadi.",
                    "<b>Реляционная целостность:</b> PK и FK связывают данные без образования мусорных строк.",
                    "<b>Integrity by design:</b> Primary and foreign keys maintain data lineage without orphan rows."),
                   ("<b>Indekslar — tezlik garovi:</b> B-Tree indekslar qidiruvni O(N) dan O(log N) ga tushiradi.",
                    "<b>Индексы дают скорость:</b> B-Tree снижает сложность поиска с линейной до логарифмической.",
                    "<b>B-Tree efficiency:</b> Strategic indexes collapse scan latency from linear O(N) to O(log N)."),
                   ("<b>Prepared Statements majburiy:</b> Foydalanuvchi ma'lumotini SQL so'roviga string qilib ulamang.",
                    "<b>Параметризация обязательна:</b> Никогда не склеивайте пользовательский ввод строками.",
                    "<b>Never concatenate SQL:</b> Always pass untrusted inputs through parameterized placeholders."),
               ])
         + "\n"
         + box("accent", ("10 Ballik Baholash Mezoni", "Критерии на 10 Баллов", "10-Point Grading Rubric"),
               items=[
                   ("<b>2 ball:</b> ACID tamoyillari va relyatsion model tushunchasi.",
                    "<b>2 балла:</b> Понимание принципов ACID и реляционной модели.",
                    "<b>2 points:</b> Articulation of ACID guarantees and relational modeling."),
                   ("<b>3 ball:</b> To'g'ri cheklovlar bilan DDL sxema yozish (PK, FK, CHECK).",
                    "<b>3 балла:</b> Написание корректной DDL схемы с PK, FK и CHECK.",
                    "<b>3 points:</b> Authoring valid DDL schema with proper constraints."),
                   ("<b>3 ball:</b> JOIN so'rovlari va agregatsiya (COUNT/SUM).",
                    "<b>3 балла:</b> Запросы JOIN и агрегация данных (COUNT/SUM).",
                    "<b>3 points:</b> Executing relational JOINs with aggregation logic."),
                   ("<b>2 ball:</b> SQL Injection tahlili va Prepared Statement himoyasi.",
                    "<b>2 балла:</b> Анализ SQL-инъекций и параметризованная защита.",
                    "<b>2 points:</b> Vulnerability analysis and prepared statement hardening."),
               ])
         + "\n</div>",
))

# ----------------- SPEAKER NOTES (O'QITUVCHI UCHUN QO'LLANMA) -----------------
NOTES = {
    "uz": [
        ["Kirish", "Darsni dasturiy ta'minotning eng qimmatli aktivi — foydalanuvchi ma'lumotlaridan boshlang.", "O'quvchilarga bank hisobidagi pul 1 soniyada yo'qolib qolsa nima bo'lishini so'rang."],
        ["ACID", "Fayllar (JSON) nima uchun katta tizimlarda ishlamasligini tushuntiring. ACID tamoyillarining har bir harfiga real misol keltiring.", "Doskada parallel 2 ta so'rov qanday to'qnashishini chizing."],
        ["PK va FK", "Primary key (pasport seriyasi) va Foreign key (otasi kimligi) misolida tushuntiring.", "ON DELETE CASCADE xususiyati ehtiyotkorlik bilan ishlatilishi kerakligini ta'kidlang."],
        ["DDL Sxema", "Sxemadagi CHECK (balance >= 0) va UNIQUE cheklovlariga urg'u bering.", "Dastur kodi xato qilsa ham, baza o'zi xatoni to'xtatib qolishini ko'rsating."],
        ["DML va CRUD", "INSERT, SELECT, UPDATE, DELETE sintaksisini ko'rsating. Tranzaksiya tushunchasini bering.", "BEGIN va COMMIT nima uchun bank tizimlarida qonun ekanligini ayting."],
        ["JOINlar", "INNER JOIN va LEFT JOIN orasidagi farqni Venn diagrammasi bilan tushuntiring.", "NULL qiymat qachon paydo bo'lishini ko'rsating."],
        ["Indekslar", "Kitob oxiridagi mundarija (alfavit ko'rsatkichi) misolida B-Tree indeksni tushuntiring.", "Indeks bo'lmasa butun kitobni boshidan oxirigacha o'qish kerakligini (Seq Scan) ayting."],
        ["SQL Injection", "Klassik ' OR '1'='1 hujumini ko'rsating. Baza qanday qilib aldanib qolishini tahlil qiling.", "Prepared Statements kod va ma'lumotni qanday ajratishini qat'iy uqtiring."],
        ["Missiya", "Amaliy topshiriq shartlarini tushuntiring. SQLite yoki PostgreSQL o'rnatilganligini tekshiring.", "12 daqiqalik taymerni yoqing."],
        ["Taymer", "Taymer vaqtida partalar orasida aylanib, SQL sintaksisi xatolariga yordam bering.", "JOIN qurganda ustun nomlari chalkashib ketmasligini nazorat qiling."],
        ["ORM", "Prisma va Drizzle zamonaviy kompaniyalarda qanday ishlatilishini qisqacha ko'rsating.", "Lekin sof SQLni bilmagan dasturchi yaxshi backendchi bo'la olmasligini uqtiring."],
        ["Baholash", "O'quvchilarning ish varaqalarini yig'ing va 10 ballik mezon bo'yicha baholang.", "Kelgusi darsda Vebhooklar va Avtomatlashtirish o'tilishini e'lon qiling."]
    ],
    "ru": [
        ["Введение", "Начните с ценности данных: почему данные — это главный актив любого цифрового бизнеса.", "Задайте вопрос: что произойдет, если баланс в банке внезапно обнулится из-за сбоя."],
        ["ACID", "Объясните крах плоских JSON-файлов при параллельной записи. Разберите каждую букву ACID.", "Покажите на доске проблему Race Condition."],
        ["PK и FK", "Первичный ключ (как номер паспорта) и внешний ключ (ссылка на родителя).", "Объясните каскадное удаление (ON DELETE CASCADE) и его риски."],
        ["DDL Схема", "Подчеркните важность ограничений CHECK (balance >= 0) и UNIQUE.", "Объясните, что база данных — это последний рубеж защиты от багов бэкенда."],
        ["DML и CRUD", "Синтаксис INSERT, SELECT, UPDATE, DELETE. Концепция транзакций.", "Продемонстрируйте, как ROLLBACK спасает систему при сбое оплаты."],
        ["JOINы", "Разница между INNER JOIN и LEFT JOIN через диаграммы Венна.", "Покажите, откуда берутся значения NULL при отсутствии связных данных."],
        ["Индексы", "Метафора предметного указателя в конце книги для объяснения B-Tree.", "Сравните чтение всей книги (Seq Scan) с мгновенным поиском по указателю."],
        ["SQL Injection", "Разберите атаку ' OR '1'='1. Объясните, как база путает код и данные.", "Внедрите понимание, что параметризация (Prepared Statements) — единственный верный путь."],
        ["Миссия", "Огласите требования лабораторной работы. Проверьте готовность CLI окружения.", "Включите 12-минутный таймер."],
        ["Таймер", "Контролируйте ход выполнения, помогайте исправлять синтаксические ошибки SQL.", "Следите за корректностью связи по внешнему ключу."],
        ["ORM", "Покажите роль Prisma и Drizzle в реальных проектах.", "Подчеркните: глубокое понимание SQL — фундамент для работы с любой ORM."],
        ["Итоги", "Соберите рабочие листы, оцените работы по 10-балльной шкале.", "Анонсируйте тему 19-го урока: Вебхуки и Автоматизация."]
    ],
    "en": [
        ["Introduction", "Frame data as the core asset of all enterprise software.", "Ask students how catastrophic a race condition would be for financial ledgers."],
        ["ACID Guarantees", "Contrast brittle flat files with industrial RDBMS ACID guarantees.", "Diagram concurrent write contention and race conditions on the board."],
        ["Keys & Lineage", "Primary keys as immutable identities; foreign keys as relational pointers.", "Explain cascading deletes and referential integrity constraints."],
        ["DDL Schema", "Highlight server-enforced business rules: CHECK and UNIQUE constraints.", "Show how the database prevents corrupt state even if application code fails."],
        ["CRUD & Transactions", "Review INSERT, SELECT, UPDATE, DELETE primitives and transaction boundaries.", "Emphasize atomic rollbacks during failure events."],
        ["Relational JOINs", "Contrast INNER JOIN vs LEFT JOIN using Venn intersection models.", "Examine NULL propagation when foreign key records are missing."],
        ["B-Tree Indexes", "Use book index analogy to illustrate balanced search trees.", "Contrast costly full sequential scans against logarithmic index lookups."],
        ["SQL Injection", "Deconstruct the ' OR '1'='1 injection payload and tokenizer confusion.", "Drill parameterized prepared statements as the non-negotiable industry defense."],
        ["Mission Brief", "Review the 4 lab deliverables. Verify terminal DB connectivity.", "Engage the 12-minute countdown timer."],
        ["Live Timer", "Walk the room assisting with SQL syntax and table constraints.", "Ensure foreign key references target valid primary key types."],
        ["ORM vs Raw SQL", "Present Prisma/Drizzle architectures in production TypeScript services.", "Reiterate that ORMs cannot rescue developers lacking raw SQL foundations."],
        ["Grading", "Collect physical worksheets and evaluate against the 10-point rubric.", "Tease Lesson 19: Webhooks and Event-Driven Automation."]
    ]
}

# ----------------- WORKSHEET (VARAQA) -----------------
VARAQA = (
    sheet_header(
        ("18-dars. Ma'lumotlar Bazasi va SQL: Relyatsion Arxitektura, Indekslar va Xavfsizlik",
         "Урок 18. Базы Данных и SQL: Реляционная Архитектура, Индексы и Безопасность",
         "Lesson 18. Databases & SQL: Relational Architecture, Indexing & Security"),
        ("9-sinf · 4-hafta (2-soat) · Backend & Data Track",
         "9 класс · 4-неделя (2-й час) · Backend & Data Track",
         "Grade 9 · Week 4 (Hour 2) · Backend & Data Track")
    )
    + "\n"
    + mission(
        ("Amaliy Missiya: Jadvallar Tuzish, JOIN Qidiruvi va SQL Injectiondan Himoyalanish",
         "Практическая Миссия: Создание Таблиц, JOIN-Запросы и Защита от SQL-Инъекций",
         "Hands-on Mission: Schema Design, Relational JOINs, and SQLi Hardening"),
        ("1. `users` va `orders` jadvallari uchun relyatsion DDL sxemasini yozing (PK, FK, CHECK).\n"
         "2. `INSERT` buyrug'i bilan har bir jadvalga kamida 2 tadan to'g'ri test ma'lumoti kiriting.\n"
         "3. Har bir mijozning buyurtmalar soni va jami summasini chiqaruvchi `LEFT JOIN` so'rovini quring.\n"
         "4. Zaif SQL so'rovini Prepared Statement ko'rinishiga o'tkazib, xavfsizlik testini o'tkazing.\n"
         "5. Barcha natijalarni quyidagi tekshiruv jadvaliga yozing.",
         "1. Напишите реляционную DDL-схему для таблиц `users` и `orders` (PK, FK, CHECK).\n"
         "2. Вставьте минимум по 2 тестовые записи в каждую таблицу через `INSERT`.\n"
         "3. Напишите запрос с `LEFT JOIN` для подсчёта заказов и суммы по каждому пользователю.\n"
         "4. Перепишите уязвимый конкатенированный запрос в безопасный Prepared Statement.\n"
         "5. Зафиксируйте результаты в контрольной таблице ниже.",
         "1. Author relational DDL schemas for `users` and `orders` tables (PK, FK, CHECK).\n"
         "2. Populate each table with at least 2 valid sample records via `INSERT`.\n"
         "3. Write a `LEFT JOIN` query aggregating customer order counts and sum totals.\n"
         "4. Refactor a vulnerable string-concatenated SQL query into a safe Prepared Statement.\n"
         "5. Record your queries and verification results in the table below.")
    )
    + "\n"
    + table(
        [("Bosqich", "Этап", "Stage"),
         ("SQL So'rovi / Terminal Buyrug'i", "SQL-Запрос / Команда Терминала", "SQL Query / Terminal Command"),
         ("Kutilgan Natija / Tekshiruv", "Ожидаемый Результат / Проверка", "Expected Output / Verification")],
        [
            [("1 · DDL", "1 · DDL", "1 · DDL"),
             ("CREATE TABLE users (...); CREATE TABLE orders (...);",
              "CREATE TABLE users (...); CREATE TABLE orders (...);",
              "CREATE TABLE users (...); CREATE TABLE orders (...);"),
             ("Jadvallar yaratildimi? [ HA / YO'Q ] · PK/FK: _____________",
              "Таблицы созданы? [ ДА / НЕТ ] · PK/FK: _____________",
              "Tables created? [ YES / NO ] · PK/FK constraints: _____________")],
            [("2 · DML", "2 · DML", "2 · DML"),
             ("INSERT INTO users VALUES (...); INSERT INTO orders VALUES (...);",
              "INSERT INTO users VALUES (...); INSERT INTO orders VALUES (...);",
              "INSERT INTO users VALUES (...); INSERT INTO orders VALUES (...);"),
             ("Kiritilgan satrlar soni (jami): __________________________",
              "Количество добавленных строк (всего): __________________________",
              "Total inserted rows: __________________________")],
            [("3 · JOIN", "3 · JOIN", "3 · JOIN"),
             ("SELECT users.full_name, COUNT(orders.id), SUM(...) FROM ...",
              "SELECT users.full_name, COUNT(orders.id), SUM(...) FROM ...",
              "SELECT users.full_name, COUNT(orders.id), SUM(...) FROM ..."),
             ("Chiqarilgan qatorlar soni: _____ · NULL qiymat bormi? [ HA / YO'Q ]",
              "Число строк в отчёте: _____ · Есть ли NULL? [ ДА / НЕТ ]",
              "Returned row count: _____ · Any NULLs present? [ YES / NO ]")],
            [("4 · Xavfsizlik", "4 · Защита", "4 · Security"),
             ("SELECT * FROM users WHERE email = $1",
              "SELECT * FROM users WHERE email = $1",
              "SELECT * FROM users WHERE email = $1"),
             ("' OR '1'='1 kiritilganda nima qaytdi: [ 0 ta satr / Xato / Barchasi ]",
              "Вывод при вводе ' OR '1'='1: [ 0 строк / Ошибка / Все данные ]",
              "Output when injected with ' OR '1'='1: [ 0 rows / Error / All rows ]")]
        ]
    )
    + "\n"
    + '    <div class="rubric-grid">\n'
    + sheet_box(
        ("✏️ Muhandislik Hisoboti",
         "✏️ Инженерный Отчёт",
         "✏️ Engineering Report"),
        writelines(2, ("ACID tamoyillari nima uchun muhim (Bank o'tkazmasi misolida):",
                       "Почему важны принципы ACID (на примере банковского перевода):",
                       "Why ACID guarantees are critical (using money transfer analogy):"))
        + "\n"
        + writelines(2, ("SQL Injection qanday ishlaydi va Prepared Statement uni qanday to'xtatadi:",
                         "Как работает SQL-инъекция и как Prepared Statements её нейтрализуют:",
                         "How SQL Injection exploits concat and how Prepared Statements stop it:"))
        + "\n"
        + writelines(2, ("B-Tree indeksning foydasi va narxi (qachon yaratish kerak va qachon yo'q):",
                         "Польза и цена B-Tree индекса (когда создавать, а когда избегать):",
                         "Benefits and costs of B-Tree indexing (when to create, when to avoid):"))
    )
    + "\n"
    + sheet_box(
        ("📊 Baholash Mezoni (10 Ball)",
         "📊 Критерии Оценки (10 Баллов)",
         "📊 Grading Rubric (10 Points)"),
        rubric([
            (("ACID va relyatsion model tushunchasi", "Понимание ACID и связей данных", "ACID guarantees & relational concepts"), "2"),
            (("Toza DDL sxema (PK, FK, CHECK)", "Корректная DDL-схема (PK, FK, CHECK)", "Clean DDL schema with constraints"), "3"),
            (("JOIN va agregat so'rovlari", "Запросы JOIN и агрегация данных", "JOIN queries with aggregations"), "3"),
            (("SQL Injection tahlili va Prepared Statement", "Анализ инъекций и параметризация", "SQLi analysis and parameterized fix"), "2"),
        ], "10")
    )
    + "\n    </div>\n  </div>\n"
    + sign_box()
)

if __name__ == "__main__":
    print(Lesson(D, TITLES, SHEET_TITLES, "vc-notes-9-18", S, NOTES, VARAQA).build())
