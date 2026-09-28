# O'qituvchi uchun qo'llanma: 18-dars — Kamera Skrollingi va Procedural Dunyo Generatsiyasi

**Kohorta:** 7–8-sinf  
**Hafta / Dars:** 4-hafta / 18-dars  
**Mavzu:** Kamera Tizimi (Viewport / Camera Tracking), Silliq Ergashish (Lerp), Parallaks Fon Skrollingi va Cheksiz Procedural Platformalar Generatsiyasi  
**Davomiyligi:** 45 daqiqa  

---

## 1. Darsning Pedagogik Maqsadi va Muhandislik Falsafasi

Avvalgi darslarda o'quvchilar bitta statik 800x400 o'lchamdagi Canvas maydonida harakatlanishdi. O'yinchi o'ngga yugursa, ekranning chetiga urilib to'xtab qolardi.

Ushbu darsda o'quvchilar 2D o'yinlar olamidagi eng muhim fazoviy mexanizmni o'rganadilar: **Kamera va Cheksiz Dunyo (Endless Scrolling)**.

Darsning tub maqsadlari:
1. **Kamera Koordinatalari Transformatsiyasi:**
   - Aslida kompyuter kamerasini jismonan harakatlantirib bo'lmaydi; harakat illyuziyasi barcha obyektlarni `cameraX` masofasiga teskari siljitib chizish orqali hosil qilinadi:
     $$\text{screenX} = \text{worldX} - \text{cameraX}$$
   - Yoki Canvas transformatsiyasi: `ctx.save(); ctx.translate(-cameraX, 0); ... ctx.restore();`.
2. **Kameraning Silliq Ergashishi (Linear Interpolation - Lerp):**
   - Agar kamera qahramonga qo'pol yopishib olsa, har bir sakrashda ekran silkinib, o'yinchining ko'zini toliqtiradi.
   - Silliq ergashish (Lerp) matematikasi:
     $$\text{cameraX} += (\text{targetX} - \text{cameraX}) \times \text{lerpRate}$$
   - Bu yerda `lerpRate = 0.08` (8% silliq yaqinlashish har freymda).
3. **Parallaks Foni (Parallax Scrolling Layering):**
   - Inson ko'zi uzoqdagi narsalarni sekinroq siljiyotgandek idrok qiladi (masalan: mashinada ketayotganda uzoqdagi tog'lar deyarli qimirlamaydi, yo'l chetidagi ustunlar esa g'izillab o'tadi).
   - Qatlamlar tezligi koeffitsiyenti:
     - Osmon va yulduzlar: `cameraX * 0.1`
     - Kiber shahar binolari: `cameraX * 0.4`
     - Asosiy platformalar: `cameraX * 1.0`
4. **Procedural Dunyo Generatsiyasi (Avtomatik Xaritalash):**
   - Platformalar oldindan qo'lda chizilmaydi; qahramon yugurgan sari yangi platformalar avtomatik yaratiladi:
     `nextX = lastX + random(140, 240);`
     `nextY = clamp(lastY + random(-60, 60), 180, 360);`
   - Sakrab bo'lmaydigan jarliklar paydo bo'lmasligi uchun oraliq masofa fizik formulalarga ($v_{\text{jump}}, \text{gravity}$) mos chegaralarda saqlanadi.
5. **Culling (Ekrandan Chiqib Ketgan Obyektlarni Tozalash):**
   - Qahramon 10,000 metr yugurganda, orqada qolgan yuzlab platformalar xotirani to'ldirmasligi uchun ularni `splice` orqali tozalash.

---

## 2. 45 Daqiqalik Dars Taqsimoti

| Vaqt | Bosqich | O'qituvchi va O'quvchi Faoliyati |
|---|---|---|
| **00:00 – 03:00** | Kirish va Ko'rgazma | Statik kichik ekran vs Cheksiz yugurish. "Mario yoki Subway Surfers qanday qilib kilometrlab cheksiz dunyo yaratadi?" |
| **03:00 – 12:00** | Nazariya: Dunyo Koordinatalari va Kamera | World space vs Screen space tushunchasi. `cameraX` ning teskari siljish qoidasi. |
| **12:00 – 18:00** | Nazariya: Silliq Lerp va Parallaks | Lerp formulasi, kameraning orqada qolib silliq yetib olishi va 3 qatlamli fon parallaksi. |
| **18:00 – 24:00** | Procedural Generatsiya va Culling | Tasodifiy platformalar yaratish, balandlik chegaralari (`minY`, `maxY`) va xotiradan o'chirish. |
| **24:00 – 38:00** | Amaliy Laboratoriya (Infinite Runner Lab) | `lab/index.html` da: kamera silliqligi (lerp), fon parallaksi va platformalar oralig'ini sozlab, cheksiz yuguruvchi kiber-dunyoni sinab ko'rish! |
| **38:00 – 43:00** | Varaqa va Mustahkamlash | Koordinata hisoblash mashqlari va parallaks koeffitsiyentlarini varaqaga yozish. |
| **43:00 – 45:00** | Xulosa va Baholash | 10 ballik mezon bo'yicha baholash va keyingi 19-dars (Mobil Touch va Joystik) bilan bog'lash. |

---

## 3. O'quvchilar Ko'p Yo'l Qo'yadigan Xatolar (Tuzoqlar)

1. **Kamerani noto'g'ri ishora bilan qo'shish:**
   - O'quvchilar ko'pincha `drawX = obj.x + cameraX` deb yozib qo'yishadi. Natijada qahramon o'ngga yursa, dunyo ham o'ngga uchib ketadi! To'g'ri formula: `drawX = obj.x - cameraX`.
2. **Kamera Lerp koeffitsiyentini 1.0 dan katta qilish:**
   - Agar `lerpRate >= 1.0` bo'lsa, kamera o'qdek sakrab titraydi (overshoot). Optimal qiymat har doim $0.05 \dots 0.15$ oralig'ida bo'ladi.
3. **Imkonsiz platformalar oralig'i (Unreachable Gaps):**
   - Agar tasodifiy masofa o'yinchining maksimal sakrash masofasidan katta bo'lib qolsa, o'yinchi muqarrar jarlikka qulaydi. O'rganish paytida sakrash kengligi qat'iy tekshirilishi shart.
