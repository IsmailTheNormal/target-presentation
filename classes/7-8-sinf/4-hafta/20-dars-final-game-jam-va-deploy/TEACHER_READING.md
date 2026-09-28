# O'qituvchi uchun qo'llanma: 20-dars — Kiber-Arkada Final Game Jam va Veb-Deploy

**Kohorta:** 7–8-sinf  
**Hafta / Dars:** 4-hafta / 20-dars  
**Mavzu:** 4-Haftalik O'yin Dasturlash Moduli Yakuni: O'yin Polirovkasi (Polishing), Doimiy Rekordlar (LocalStorage), Veb-Deploy, QR Kod va Sinf Chempionati  
**Davomiyligi:** 45 daqiqa  

---

## 1. Darsning Pedagogik Maqsadi va Muhandislik Falsafasi

Ushbu dars 7–8-sinf o'quvchilari uchun butun o'yin muhandisligi modulining (Canvas, Tsikl, Fizika, Boss, Ovoz, Partikllar, Kamera, Touch) tantanali yakunidir. 

Dasturchi uchun yozilgan kod faqat o'z noutbukida qolib ketmasligi, balki butun dunyoga — do'stlari, ota-onasi va xalqaro internetga taqdim etilishi shart!

Darsning tub maqsadlari:
1. **O'yin Polirovkasi (Game Polishing & UX):**
   - Boshlang'ich menyu ("START GAME").
   - Ovoz sozlamasi (Mute / Unmute Audio Toggle).
   - Doimiy xotira (LocalStorage High Score): eng yuqori rekord brauzerda doimiy saqlanadi.
   - O'yin tugashi va qayta boshlash ("GAME OVER" & "RETRY").
2. **Bulutli Deploy (Cloud Hosting):**
   - Vercel va GitHub Pages platformalarida bitta buyruq yoki fayl tashlash orqali jonli HTTPS domeniga ega bo'lish (`https://cyber-arcade.vercel.app`).
   - Mobil telefonda ochish uchun dinamik QR Kod hosil qilish.
3. **Peer-Review Madaniyati va Sinf Chempionati (Target Game Jam):**
   - O'quvchilar bir-birlarining o'yinlarini telefonlarida QR kod orqali ochib o'ynaydilar.
   - Xolis muhandislik baholash mezonlari:
     - 🎮 Boshqaruv qulayligi (Touch va klaviatura sezgirligi).
     - 🔊 Ovoz va Visual FX sifati (Web Audio va neon partikllar).
     - ⚡ O'yin barqarorligi va tezligi (60 FPS, qotishlarsiz).

---

## 2. 45 Daqiqalik Dars Taqsimoti

| Vaqt | Bosqich | O'qituvchi va O'quvchi Faoliyati |
|---|---|---|
| **00:00 – 03:00** | Kirish va Game Jam Starti | "Bugun — Game Jam Finali! 4 hafta davomida o'rgangan barcha bilimlaringiz jamlangan yakuniy o'yinni chiqaramiz va sinf chempionatini o'tkazamiz!" |
| **03:00 – 10:00** | Nazariya: O'yin Polirovkasi va UX | Boshlang'ich menyu, Audio sozlamasi, High Score saqlash mexanizmi va Vercel deploy qoidalari. |
| **10:00 – 28:00** | Amaliy Game Jam (Cheksiz Kiber-Arkada Finali) | `game/index.html` da: to'liq jamlangan Kiber-Arkada o'yinini ishga tushirish, o'z parametrlarini sozlash (tezlik, ranglar, ovoz) va deploy oynasida QR kod hosil qilish! |
| **28:00 – 38:00** | Sinf Turniri va O'zaro Sinov (Peer Review) | O'quvchilar qo'shnilarining QR kodini skaner qilib, ularning o'yinini telefonlarida sinab ko'radilar va varaqa kartochkasiga ball qo'yadilar. |
| **38:00 – 43:00** | Varaqa va Mustahkamlash | Varaqadagi baholash kartasi va loyiha xulosasini to'ldirish. |
| **43:00 – 45:00** | G'oliblarni E'lon Qilish va Taqdirlash | 10 ballik tizim bo'yicha baholash, eng yaxshi o'yin mualliflarini tabriklash va 4-haftalik modulni muvaffaqiyatli yakunlash. |

---

## 3. O'quvchilar Ko'p Yo'l Qo'yadigan Xatolar (Tuzoqlar)

1. **Deploy fayl nomining `index.html` bo'lmasligi:**
   - Serverlar veb-saytning bosh sahifasi sifatida aynan `index.html` faylini qidiradi. Agar fayl nomi `game.html` yoki `main.html` bo'lsa, server 404 Not Found xatosini beradi.
2. **Audio Autoplay blokirovkasini menyusiz ishlatish:**
   - Agar o'yin ochilishi bilanoq fonda musiqa chalishga urinsa, mobil Safari/Chrome uni bloklaydi. Shuning uchun o'yin har doim "START" tugmasi bosilgandan keyin ovoz chiqarishi shart.
3. **Rekordni saqlashda `parseInt` ni unutish:**
   - LocalStorage ma'lumotlarni qat'iy matn (string) formatida saqlaydi. Agar `parseInt(score, 10)` qilinmasa, `'50' > '100'` taqqoslashida xato yuz beradi.
