# 31-dars: Penetration Testing & Ethical Hacking: O'z Zaiflik Skaneringni Dasturlash
> **O'qituvchi uchun pedagogik yo'riqnoma va dars ssenariysi**  
> **Kohorta:** 10–11-sinf (Senior Engineering Cohort)  
> **Fan:** Kiberxavfsizlik va Vibecoding  
> **Dars davomiyligi:** 40 daqiqa (Nazariya 8 daq / 20%, Amaliyot 32 daq / 80%)

---

## 🎯 Darsning Asosiy Maqsadi va O'lchanadigan Natija

Har bir o'quvchi dars oxirida:
1. **White Hat (Etik Xakerlik)** tamoyillarini va **PTES (Penetration Testing Execution Standard)** ning 5 ta bosqichini tushunadi.
2. OWASP API Top 10 ning 1-raqamli kritik xatosi bo'lgan **BOLA / IDOR (Broken Object Level Authorization)** mexanizmini va uni kod darajasida tuzatishni o'rganadi.
3. Brauzer xavfsizlik sarlavhalari (**CSP, HSTS, X-Frame-Options**) ning ahamiyatini va RegEx orqali **AWS kalitlari va JWT tokenlar** sizishini aniqlashni biladi.
4. **Target Pentest Studio** orqali interaktiv audit o'tkazadi va **Node.js** da shaxsiy CLI skanerini (`scanner/scanner.js`) muvaffaqiyatli ishga tushirib, `security-report.json` hisobotini oladi.

---

## ⏱️ Darsning 40 Daqiqalik Taqsimoti (Pacing)

| Vaqt | Bosqich | O'qituvchi Faoliyati | O'quvchi Faoliyati |
|---|---|---|---|
| **00:00 – 03:00** (3 daq) | **Kirish va Reja** | DevSecOps Capstone natijalarini eslaydi, bugungi "Ethical Hacking" va o'z skanerimizni qurish mavzusini e'lon qiladi. | Ishchi varaqani oladi, ism-familiyasini yozadi. |
| **03:00 – 11:00** (8 daq) | **Nazariya & Jonli Demo** | White vs Black Hat farqi, BOLA/IDOR mexanizmi, 169.254.169.254 (Capital One keysi) va CVSS v3.1 hisobini doskada jonli ko'rsatadi. | Slaydlarni kuzatadi, asosiy atamalarni qayd qiladi. |
| **11:00 – 33:00** (22 daq) | **Mustaqil Amaliyot (80%)** | Sinf bo'ylab yuradi, o'quvchilarga Studio kvestlari va CLI skanerini yurgizishda ko'maklashadi. | **Path A:** Studio da 4 ta modulni skanerlaydi.<br>**Path B:** Terminalda `node scanner.js` ni ishga tushiradi va JSON hisobot oladi. |
| **33:00 – 38:00** (5 daq) | **Ko'rik va Tahlil** | 2 nafar o'quvchining skaner natijasini va CVSS ballini ekranga chiqarib tahlil qiladi. | Topilgan zaifliklar va patch kodini taqdim qiladi. |
| **38:00 – 40:00** (2 daq) | **Uy Vazifasi** | Yangi RegEx qo'shish va hisobotni commit qilish topshirig'ini tushuntiradi. | Vazifani belgilab oladi. |

---

## 🗣️ O'qituvchining Nutq Ssenariysi (Verbal Script)

### O'zbekcha:
> *"Hurmatli bo'lajak kiber-xavfsizlik muhandislari! O'tgan darsda biz DevSecOps quvurini qurib, kodni deploy qilish darvozalarini qo'ygan edik. Lekin tasavvur qiling: siz barcha eshiklarni qulfladingiz, ammo xakerlar baribir yangi teshik topishdi. Nima uchun? Chunki himoyachi hamma joyni yopishi kerak, hujumchiga esa atigi bitta xato yetarli!  
> Bugun biz mudofaadan hujumga — ya'ni Ethical Hacking olamiga o'tamiz. Biz o'zimiz tizimimizni sinovdan o'tkazuvchi avtomatlashtirilgan CLI skaner dasturini yaratamiz. Skanerimiz OWASP Top 10 ning eng mashhur xatosi bo'lgan BOLA/IDOR ni, yetishmayotgan brauzer qalqonlarini va ochiq qolib ketgan AWS kalitlarini qidiradi. Keling, terminalni ochamiz va birinchi testni boshlaymiz!"*

### Русский:
> *"Приветствую, будущие инженеры безопасности! На прошлом уроке мы построили DevSecOps конвейер с жесткими гейтами. Но реальность такова: защитнику нужно обезопасить 100% периметра, а злоумышленнику достаточно найти всего одну брешь.  
> Сегодня мы переходим на сторону этичного хакинга (White Hat). Мы напишем собственный легковесный CLI сканер на Node.js, который без внешних библиотек найдет критические ошибки BOLA/IDOR, отсутствие CSP заголовков и утечки приватных AWS ключей. Открываем терминалы и запускаем первый аудит!"*

---

## 🛠️ Ikki Yo'nalishli Amaliyot (Dual-Path Pedagogy)

1. **Path A — GUI Pentest Studio (`studio/index.html`)**:
   - Vizual o'rganuvchilar uchun qulay. Brauzerda ochiladi, 4 ta modulni tanlab "Skanerlashni Boshlash" bosiladi.
   - Real-vaqtli ANSI telemetriyasini ko'radi va CVSS v3.1 interaktiv slayderi orqali xavf darajasini hisoblaydi.
2. **Path B — Professional CLI Scanner (`scanner/scanner.js`)**:
   - Chuqur muhandislik yo'li. Terminalda `node scanner.js --demo` buyrug'i yurgiziladi.
   - O'quvchi kod ichiga kirib, `SECRET_PATTERNS` massiviga yangi qoidalar (masalan, GitHub tokenlari) qo'shishi mumkin.
   - Natija `security-report.json` faylida saqlanadi.

---

## ⚠️ Ehtimoliy Xatolar va Bartaraf Qilish

1. **Xato:** O'quvchi skanerni ruxsatsiz ommaviy saytlarga (`google.com`, `bank.uz`) qarshi ishga tushirishga urinishi mumkin.
   - **Yechim:** Qat'iy taqiqlanadi! Axloq kodeksini eslating (CFAA va O'zbekiston Jinoyat Kodeksi 278-moddasi). Faqat `localhost` yoki darsdagi simulyator target tekshiriladi.
2. **Xato:** `node: command not found` xatoligi.
   - **Yechim:** Kompyuterda Node.js o'rnatilganini tekshiring yoki brauzerdagi `studio/index.html` ga yo'naltiring.
3. **Xato:** CVSS kalkulyatorida nima uchun ball 10 dan oshib ketmasligi tushunilmasligi.
   - **Yechim:** CVSS formulasi normallashtirilgan bo'lib, uning maksimal qiymati 10.0 (Critical) bilan cheklanganini doskada tushuntiring.
