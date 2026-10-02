-- =====================================================================
-- Target International School · Vibecoding (Grade 9 · Week 4 · Lesson 18)
-- Track: Backend & Data Track
-- Topic: Databases & SQL: Relational Architecture, Indexing & Security
-- File: starter_lab.sql
-- =====================================================================

-- 0. CLI Sozlamalari (Faqat SQLite terminalida ishlatilsa)
-- .headers on
-- .mode table
PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------------
-- 1. DDL: Relyatsion Sxemani Yaratish (Users va Orders)
-- ---------------------------------------------------------------------

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS users;

-- Users Jadvali: PK, UNIQUE email, CHECK cheklovlari
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%'),
  balance INTEGER NOT NULL DEFAULT 0 CHECK(balance >= 0),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Orders Jadvali: PK, FK (CASCADE), CHECK cheklovi
CREATE TABLE orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  product_name TEXT NOT NULL,
  amount INTEGER NOT NULL CHECK(amount > 0),
  status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'completed', 'cancelled')),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- B-Tree Indeks: user_id bo'yicha qidiruvni 800ms dan 1ms gacha tezlashtirish
CREATE INDEX idx_orders_user_id ON orders(user_id);


-- ---------------------------------------------------------------------
-- 2. DML: Test Ma'lumotlarini Kiritish (Seed Data)
-- ---------------------------------------------------------------------

INSERT INTO users (full_name, email, balance) VALUES 
('Jasur Aliyev', 'jasur@target.uz', 500000),
('Malika Karimova', 'malika@target.uz', 1200000),
('Bobur Mirzayev', 'bobur@target.uz', 0);

INSERT INTO orders (user_id, product_name, amount, status) VALUES 
(1, 'Logitech MX Master 3S', 120000, 'completed'),
(1, 'Keychron K2 Mechanical Keyboard', 95000, 'completed'),
(2, 'Dell UltraSharp 27 4K Monitor', 450000, 'completed');


-- ---------------------------------------------------------------------
-- 3. JOIN & Agregatsiya: Mijozlar va Ularning Jami Xaridlari
-- ---------------------------------------------------------------------

SELECT 
  users.id,
  users.full_name,
  users.email,
  COUNT(orders.id) AS total_orders,
  COALESCE(SUM(orders.amount), 0) AS total_spent
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id
ORDER BY total_spent DESC;


-- ---------------------------------------------------------------------
-- 4. Kiberxavfsizlik Tahlili: SQL Injection vs Parameterized Defense
-- ---------------------------------------------------------------------

-- A. XAVFLI STRING KONKATENATSIYASI SIMULYATSIYASI:
-- Foydalanuvchi kiritdi: ' OR '1'='1
-- So'rov butun jadvalni qaytaradi:
SELECT * FROM users WHERE email = '' OR '1'='1';

-- B. 100% XAVFSIZ PARAMETRLASHTIRILGAN SO'ROV SIMULYATSIYASI:
-- Foydalanuvchi kiritgan har qanday belgi faqat oddiy matn (literal) deb olinadi:
SELECT * FROM users WHERE email = 'test'' OR ''1''=''1';
-- Natija: 0 ta qator qaytadi! Tizim 100% xavfsiz.
