# 32-dars: O'yin Fizikasi va Otishma Mexanikasi: Trigonometriya, Traektoriya va Zarrachalar (O'qituvchi Metodologiyasi)

## Darsning Pasporti
- **Sinf:** 7–8-sinf (Game Dev & Creative Coding Track)
- **Davomiyligi:** 80 daqiqa (Juftlik Dars / Double Block)
- **Asosiy maqsad:** 2D Canvas o'yinlarida otishma fizikasi va ballistika mexanikasini o'rgatish. Math.atan2 orqali burchakni hisoblash, tezlikni cos/sin vektorlariga ajratish, o'qlar massivini xavfsiz boshqarish (Memory leakning oldini olish) va devorga urilganda uchqunlar (particle sparks) tizimini dasturlash.

---

## 80 Daqiqalik Aniq Vaqt Taqsimoti (Pacing)

### 1-Qism: Nazariya, Xatolar Tahlili va Jonli Test (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Motivatsiya | 1 | Ballistika va otishma fizikasining video o'yinlardagi rolini tushuntirish. | Diqqat bilan tinglaydilar va maqsadni belgilaydilar. |
| **04:00–12:00** | 31-dars HW Tahlili | 2 | Random Walker devorlarni teshib o'tishi va clamping xatolarini tahlil qilish. | Blitz savolga javob beradilar, clamping qoidasini yozib oladilar. |
| **12:00–18:00** | Otishma Arxitekturasi | 3 | Kursor bosilishidan to'qnashuvgacha bo'lgan 4 bosqichni chizib ko'rsatish. | Otishma zanjirini tushunadilar. |
| **18:00–24:00** | Math.atan2 Sehri | 4 | Nega atan emas, Math.atan2(dy, dx) ishlatilishini asoslash. Argumentlar tartibini ta'kidlash. | Radiandagi burchak tushunchasini o'rganadilar. |
| **24:00–30:00** | Tezlik Vektorlari | 5 | cos va sin proeksiyalarini Pifagor teoremasi orqali isbotlash. | vx va vy formulalarini yozib oladilar. |
| **30:00–35:00** | Xotirani Tozalash | 6 | Memory leak muammosi va nega teskari tartibda (length-1 dan 0 gacha) splice qilish zarurligini tushuntirish. | Xavfsiz tozalash siklini o'zlashtiradilar. |
| **35:00–40:00** | Zarrachalar Tizimi | 7 | Uchqunlar sochilishi, 0.92 ishqalanish kuchi va alpha so'nishi mexanikasini ko'rsatish. | Vizual effektlar fizikasini o'rganadilar. |

### 2-Qism: Smartboard Sinovi, Katta Arena va Showcase (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **40:00–48:00** | Smartboard Simulyatori | 8 | Slayddagi simulyatorda bolalar bilan doskaga bosib lazer uzish va 360° salyutni ko'rsatish. | Doskada lazer uzib, zarrachalar sochilishini kuzatadilar. |
| **48:00–55:00** | Viktorina (Quiz) | 9 | 3 ta nazorat savoli bo'yicha viktorina o'tkazish. | Faol javob beradilar va o'z bilimlarini tekshiradilar. |
| **55:00–70:00** | 25 Daqiqalik Arena | 10 | 25:00 taymerni yoqish, partalar bo'ylab yurib ko'maklashish. | simulator/index.html da o'z Roguelike o'yinlariga otishma tizimini ulaydilar. |
| **70:00–74:00** | Partadosh Auditi | 11 | O'rin almashishni e'lon qilish, 4 mezonli sinovni nazorat qilish. | Bir-birining tizimiga to'xtovsiz o'q uzib, xotira tozalanishini tekshiradilar. |
| **74:00–77:00** | Katta Ekran Showcasi | 12 | Eng zo'r otishma tizimini katta doskaga chiqarib sinash (drobovik / rikoshet). | Sinfdoshlari natijasini olqishlaydilar. |
| **77:00–80:00** | Uy Vazifasi va Yakun | 13–14 | 10 ballik uy vazifasini tushuntirish va Dushman AI (A* qidiruv) mavzusiga ko'prik! | Kundaliklariga vazifani belgilaydilar. |

---

## O'qituvchi Uchun Muhim Blitz Savollari
1. **"Nega Math.atan2(dx, dy) deb yozsak xato bo'ladi?"**
   - Javob: Chunki funksiya birinchi argument sifatida Y o'qidagi siljishni (dy), ikkinchi bo'lib X o'qidagi siljishni (dx) kutadi. Agar adashtirsak, o'qlar 90 daraja noto'g'ri tomonga uchadi!
2. **"O'qlarni boshidan (i=0 dan) splice qilsak nega ba'zi o'qlar o'chmay qoladi?"**
   - Javob: Chunki splice qilinganda massivdagi qolgan elementlar bitta chapga suriladi. Natijada keyingi elementning indeksi o'tib ketilib, tekshirilmay qoladi (indeks sakrashi xatosi).

---

## 10 Ballik Baholash Rubrikasi
- **4 Ball (Baza):** O'qlar kursor bosilgan tomonga Math.atan2 va cos/sin orqali to'g'ri uchadi.
- **4 Ball (Amaliy):** Devorga urilganda o'q to'xtaydi va teskari sikl orqali massivdan xatosiz o'chiriladi.
- **2 Ball (Challenge):** Zarrachalar (uchqunlar) portlashi yoki rikoshet/drobovik mexanikasi ishlaydi!
