# 13–14-Darslar: O'qituvchi Uchun Maxsus Qo'llanma (Teacher Master Prep Guide)
**Target International School // 5–6-Sinflar (10–12 yosh) // 3-Hafta (Juft Dars: 2 x 40 daqiqa)**

> **ESLATMA:** Ushbu qo'llanma IT, o'yin yoki AI bo'yicha chuqur bilimga ega bo'lmagan o'qituvchi uchun yozilgan. Uni o'qib chiqsangiz, darsni bexato va ishonch bilan o'tasiz.

---

## 1. Sinfda Qaysi Dastur va AI Vositasidan Foydalaniladi? (Aniq Platforma)

O'quvchilar noutbuklarida 2 ta asosiy darcha ochiladi:

### 1-Darcha: O'yin Maydoni (Brauzer)
*   O'quvchilar `classes/5-6-sinf/3-hafta/13-dars-oyin-mexanikasi-va-boshqaruv/game/index.html` faylini Google Chrome yoki boshqa brauzerda ochishadi (yoki VS Code da `Live Server` tugmasini bosishadi).
*   Ekranda darhol 2D kiber-o'yin ochiladi. O'quvchi `A`, `D` va `Space` tugmalari bilan o'ynab ko'radi.
*   O'ng tomonda qulay slayderlar bor (Tezlik, Sakrash, Gravitatsiya). Dasturlashni bilmagan bola ham slayderni surib, o'yin qanday o'zgarishini o'z ko'zi bilan ko'radi!

### 2-Darcha: AI Yordamchi (AI Chatbot)
*   **Qaysi AI:** Maktabda noutbuklarda o'rnatilgan yoki brauzerda ochiladigan:
    1. **Variant A (Eng osoni):** Brauzerda **ChatGPT** (`chatgpt.com`) yoki **Claude** (`claude.ai`).
    2. **Variant B:** Agar VS Code da AI o'rnatilgan bo'lsa (Cline / Copilot / Cursor).
*   **O'quvchilar AI ga nima deb yozadi:** Bolalar murakkab kod yozmaydi! Ular quyidagi tayyor ruscha yoki o'zbekcha prompitlardan nusxa olib, AI ga jo'natishadi:
    - *"Я делаю 2D платформер на JavaScript. Подскажи, какие параметры скорости (speed) и силы прыжка (jumpForce) поставить, чтобы герой прыгал высоко как на Луне?"*
    - *"Добавь в функцию handleJump() эффект золотых искр (particles), когда герой отталкивается от земли."*
*   AI bergan javobdagi raqamni bolalar o'yindagi slayderga yoki `game.js` dagi songa qo'yib tekshirishadi!

---

## 2. Juft Darsning 80 Daqiqalik Aniq Rejasi (Double Lesson Workflow)

Sizda ketma-ket 2 ta dars (juft dars):

```
┌───────────────────────────────────────┬───────────────┬───────────────────────────────────────┐
│     13-DARS: 1-SOAT (40 daqiqa)       │   TANAFFUS    │     14-DARS: 2-SOAT (40 daqiqa)       │
│  Qahramon Harakati va Fizika         │   (5 daq)     │  To'siqlar, Tikanlar va G'alaba      │
│  - Boshqaruv (A, D, Space)           │               │  - Xavfli tikanlar va lazerlar       │
│  - Tezlik, Sakrash, Gravitatsiya     │               │  - Jon (HP) ketishi va Game Over     │
│  - 3 ta fizik rejim sinovi           │               │  - Finish bayrog'i (Win State)       │
└───────────────────────────────────────┴───────────────┴───────────────────────────────────────┘
```

---

### 1-SOAT: 13-DARS — QAHRAMON HARAKATI VA CORE GAME LOOP (40 daqiqa)

#### 00:00 – 05:00 | Boshlash va Diqqatni Tortish
*   **O'qituvchi nima deydi (rus tilida):**
    > *"Ребята, открываем ноутбуки! Сегодня мы превращаем наши 3D-модели и звуки в настоящую живую игру. Кто играл в Subway Surfers или Brawl Stars? Задумывались ли вы, как компьютер понимает, что вы нажали пробел и герой должен прыгнуть? Сегодня вы сами настроите физику своего первого кибер-раннера!"*
*   **Proyektorda:** `prezentatsiya.html` 1-slaydi.

#### 05:00 – 18:00 | Nazariya (Oddiy tushuntirish)
*   **Game Loop (60 FPS):** Kompyuter har soniyada 60 marta: 1) Tugmani eshitadi $\rightarrow$ 2) Fizikani hisoblaydi $\rightarrow$ 3) Yangi kadrni chizadi.
*   **Tezlik va Gravitatsiya:**
    - Tezlik ($X$ o'qi): Oldinga va orqaga yurish.
    - Gravitatsiya ($Y$ o'qi): Qahramon havoda ekan, yer uni pastga tortadi. Agar gravitatsiya bo'lmasa, qahramon koinotga uchib ketadi!
*   **Hitbox:** Qahramon polni teshib pastga tushib ketmasligi uchun uning oyog'i ostida yer tekshiruvi bor.

#### 18:00 – 35:00 | Amaliyot (Laboratoriya)
*   Bolalar `game/index.html` ni ochishadi.
*   Topshiriq: Slayderlar yordamida 3 ta rejimni sinab ko'rish:
    1. **Oy Gravitatsiyasi (Moon):** Sakrash 16, Gravitatsiya 0.2 (parvoz hissi).
    2. **Tosh Qahramon (Heavy):** Sakrash 8, Gravitatsiya 1.4 (sakrash juda qiyin).
    3. **Shaxsiy Balans (Ideal):** O'zlariga eng qulay parametrni topib, varaqaga yozish.
*   Kim 3 ta tangani yig'a olsa — qo'shimcha rag'bat oladi!

#### 35:00 – 40:00 | 1-Soat Yakuni va Baholash
*   Varaqaga 1-soat natijalari bo'yicha ball qo'yiladi.

---

### TANAFFUS (5 daqiqa)
*   Bolalarga ko'z mashqlarini qildiring, turib harakatlanishsin.

---

### 2-SOAT: 14-DARS — TO'SIQLAR, JON (HP) VA G'ALABA (40 daqiqa)

#### 00:00 – 05:00 | 2-Soatga Kirish
*   **O'qituvchi nima deydi:**
    > *"В первой части наш герой научился идеально бегать и прыгать. Но согласитесь, если бежать просто по пустой дороге — играть станет скучно уже через минуту! Чего не хватает? Опасностей, шипов и цели! Во второй части мы добавим красные лазеры, ловушки и финишный флаг!"*

#### 05:00 – 18:00 | Nazariya: To'qnashuv va O'yin Qoidalari
*   **Hazard Collision (Xavfli to'qnashuv):** Agar qahramon qizil tikanga tegsa — nima bo'ladi?
    - Jon yo'qotish: `lives = lives - 1` (3 ta jondan 1 tasi ketadi).
    - Orqaga otilish (Knockback effekti) yoki startga qaytish.
*   **Win State (G'alaba sharti):** Yashil portal yoki bayroqqa yetib borganda `VICTORY!` ekrani chiqadi.
*   **Game Over (Mag'lubiyat):** Agar jonlar 0 ga teng bo'lsa, `RESTART` tugmasi chiqadi.

#### 18:00 – 35:00 | Amaliyot: O'yin Trassasini Bosib O'tish
*   Bolalar o'yindagi yangilangan 2-darajani ochishadi (tikanlar va lazerlar bilan).
*   Topshiriq:
    1. Tikanlardan sakrab o'tish.
    2. Jonlar tugamasdan barcha 3 ta platformadan o'tib, yashil portalga yetib borish!
    3. AI Agentdan yordam olish: *"Как добавить звуковой сигнал, когда персонаж наступает на шипы?"*

#### 35:00 – 40:00 | Umumiy Xulosa va Juft Dars Yakuni
*   G'olib o'quvchilarni tabriklash va varaqalarga yakuniy 10 ballik baholarni qo'yish.

---

## 3. O'quvchilar So'rashi Aniq Bo'lgan Savollar va Sizning Tayyor Javoblaringiz

1. **"Учитель, почему при нажатии на пробел персонаж летит вверх, а потом падает?"**  
   *Javob:* *"Когда вы нажимаете пробел, код дает персонажу мгновенную силу вверх (прыжок). Но в каждом кадре сила тяжести (гравитация) тянет его вниз, пока он снова не коснется земли."*
2. **"Учитель, персонаж касается шипа, но не погибает!"**  
   *Javob:* *"Проверьте условие столкновения (Hitbox). Координата X и Y героя должна пересекаться с координатами шипа."*
3. **"Как в Roblox делают такие игры?"**  
   *Javob:* *"Точно так же! В Roblox это называется Obby (Obstacle Course). Там используются точно такие же зоны смерти (KillBrick) и финишные чекпоинты."*
