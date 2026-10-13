# Target Custom Pentest CLI & Vulnerability Scanner
> Target International School — Senior Cybersecurity & Penetration Testing Cohort (10-11-sinf, 31-dars)

---

## [UZ] O'zbekcha Yo'riqnoma

Ushbu loyiha 10-11-sinf o'quvchilari uchun maxsus tayyorlangan avtomatlashtirilgan kiberxavfsizlik va zaifliklarni qidirish vositasi (Vulnerability Scanner CLI) hisoblanadi.

### 1. Ishga tushirish
Har qanday qo'shimcha npm kutubxonalarisiz, sof Node.js orqali ishga tushadi:
```bash
# Demo rejimida skanerlash (simulyatsiya qilingan zaif target):
node scanner.js --demo

# Jonli serverni tekshirish:
node scanner.js --target=http://localhost:3000
```

### 2. Tekshiriladigan 4 ta asosiy zaiflik:
1. **Missing HTTP Security Headers:** CSP, X-Frame-Options, HSTS, X-Content-Type-Options sarlavhalari mavjudligini audit qiladi.
2. **Sensitive Data Exposure:** JSON yoki HTML ichida ochiq AWS kalitlari (`AKIA...`), JWT tokenlar yoki ochiq parollar sizib chiqqanini RegEx orqali fosh etadi.
3. **BOLA / IDOR (Broken Object Level Authorization):** Foydalanuvchi hisob parametrlari manipulyatsiyasini tekshiradi.
4. **SSRF & Cloud Metadata Access:** Ichki AWS metadata IP `169.254.169.254` va `127.0.0.1` filtrlarini tekshiradi.

### 3. Natija va Hisobot:
Audit yakunlangach, avtomatik ravishda `security-report.json` fayli shakllanadi. Unda CVSS v3.1 ko'rsatkichlari va tuzatish tavsiyalari joy oladi.

---

## [RU] Русская Инструкция

Автоматизированный CLI сканер уязвимостей для аудита веб-приложений и API.

### 1. Запуск
```bash
# Запуск демо-режима:
node scanner.js --demo

# Аудит реального сервера:
node scanner.js --target=http://localhost:3000
```

### 2. Проверяемые векторы атак:
1. Отсутствие защитных HTTP-заголовков (CSP, HSTS, X-Frame-Options).
2. Утечка конфиденциальных данных и API ключей через регулярные выражения.
3. Ошибки контроля доступа BOLA / IDOR.
4. Уязвимости Server-Side Request Forgery (SSRF) к метаданным облака.

---

## [EN] English Guide

Lightweight, zero-dependency Node.js CLI vulnerability scanner for OWASP API Top 10 penetration testing.

### 1. Quick Start
```bash
# Run simulated scan:
node scanner.js --demo

# Scan live target:
node scanner.js --target=http://localhost:3000
```

### 2. Audit Features:
- HTTP Security Headers inspector (CSP, HSTS, Clickjacking defense)
- Regex-based Secret & Token exposure detector
- BOLA / IDOR boundary fuzzer
- Cloud metadata SSRF exploit detector
- Automated JSON audit report generation (`security-report.json`)
