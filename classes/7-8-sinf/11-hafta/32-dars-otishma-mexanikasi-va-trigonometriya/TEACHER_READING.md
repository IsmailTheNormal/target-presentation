# O'qituvchi Uchun Dars Qo'llanmasi (Teacher Reading Guide)

**Sinf:** 7–8-sinf · **Hafta:** 11-hafta · **Dars:** 32-dars  
**Mavzu:** O'yin Fizikasi va Otishma Mexanikasi: Trigonometriya, Traektoriya va Zarrachalar (Canvas Ballistics, Math.atan2 & Particle Sparks)  
**Format:** 80 daqiqalik Juftlik Dars (Double Block)  
**Uslub:** Vibecoding — AI bilan interaktiv dasturlash, prompt muhandisligi va kod auditi.

---

## 1. 80 Daqiqalik Darsning Daqiqama-Daqiqa Pacing Rejasi

### 1-Bosqich: Uy Vazifasi Tahlili va Nazariy Poydevor (40 daqiqa)
* **00:00–04:00 (Kirish):** Dars mavzusi va maqsadini e'lon qilish. Roguelike o'yinimizga bugun haqiqiy jangovar mexanika qo'shilishini tushuntirish.
* **04:00–12:00 (Uy Vazifasi Tahlili):** 
  - Keng tarqalgan xato (Pitfall): `Math.atan2(dx, dy)` emas, doim `Math.atan2(dy, dx)`! O'quvchilarga nega vertikal o'q (dy) birinchi kelishini doskada chizib ko'rsating.
  - 30 soniyalik blits savol: dy = 0, dx > 0 bo'lganda burchak necha radian? (0 rad).
* **12:00–24:00 (Nishonga Olish va Math.atan2):**
  - Ekranda sichqoncha koordinatalarini tutish (`e.clientX - rect.left`).
  - Radianlar aylanasi (-PI dan +PI gacha). Canvas da Y o'qi pastga qaragani uchun radianlar yo'nalishini ko'rsatish.
* **24:00–35:00 (Tezlik Vektorlari va Xotira Tozalash):**
  - `vx = cos(angle) * speed`, `vy = sin(angle) * speed`.
  - **Kritik nuqta (Memory Leak):** Agar o'qlar ekrandan chiqqanda o'chirilmasa, o'yin qotadi. Nega oddiy `for (i=0)` siklida `splice()` indekslarni buzib yuborishini, teskari sikl `for (let i = bullets.length - 1; i >= 0; i--)` esa xavfsiz ekanini tushuntiring.
* **35:00–40:00 (Zarrachalar — Game Juice):**
  - 8–12 ta uchqun sochish, havo qarshiligi (friction: 0.92) va shaffoflik (alpha) so'nishi.

### 2-Bosqich: Amaliyot, Kiber-Duel va Baholash (40 daqiqa)
* **40:00–48:00 (Smartboard Jonli Simulyatori):** Doskada o'quvchilar bilan interaktiv o'q otish, 360° salьyutni sinash.
* **48:00–55:00 (Kiber-Viktorina):** 3 ta savol bo'yicha tezkor musobaqa.
* **55:00–70:00 (Vibecoding Amaliy Arenasi — 15 daqiqa):**
  - O'quvchilar kompyuterlarini ochadi.
  - **Muhim Vibecoding qoidasi:** Kodni qo'lda yozmaslik, AI ga 4 bosqichli prompt berish!
  - 1-qadam: Boshlang'ich prompt orqali burchak va uchishni olish.
  - 2-qadam: Sinov va 360° nishonni tekshirish.
  - 3-qadam: Xotira oqishini AI ga tushuntirib, teskari siklni talab qilish (Critic prompt).
  - 4-qadam: Zarrachalar (sparks) yoki Drobovik rejimini qo'shish.
* **70:00–74:00 (Partadosh Auditi):** Partadoshlar o'rin almashib, 4 ta mezon bo'yicha bir-birining o'yinini test qiladi.
* **74:00–77:00 (Katta Ekran Showcasi):** Eng chiroyli otishma yoki qurol yaratgan 2 nafar o'quvchi ishini doskada ko'rsatish.
* **77:00–80:00 (Xulosa va Vazifa):** 10 ballik rubrika va ertangi darsga (Dushman AI va Pathfinding) ko'prik.

---

## 2. O'qituvchi Uchun Savol-Javob va Baholash Kaliti
* **Savol 1:** Math.atan2(dy, dx) nima qaytaradi?  
  *Javob:* Qahramondan kursorga yo'nalgan to'g'ri burchakni radianlarda (-3.14 dan +3.14 gacha) qaytaradi.
* **Savol 2:** Nega oddiy `bullets.push()` bilan birga `bullets.splice()` yozilmasa o'yin sekinlashadi?  
  *Javob:* Har bosilganda massivga yangi obyekt qo'shiladi. Ekrandan chiqqan o'qlar o'chirilmasa, 60 FPS sikli minglab o'qlarni hisoblashga majbur bo'ladi va xotira to'lib (Memory Leak) o'yin qotadi.
* **Savol 3:** Nega massivni orqadan oldinga tekshirish kerak?  
  *Javob:* Chunki 0-indeksdan boshlab o'chirilsa, qolgan elementlar bitta chapga siljiydi va keyingi o'q tekshirilmay o'tib ketadi.
