# O'qituvchi uchun qo'llanma: 16-dars — Boss Jangi, Power-uplar va Arkada Yakuni

**Kohorta:** Middle Web GameDev (7–8-sinflar)  
**Hafta / Dars:** 3-hafta / 16-dars (3-hafta Katta Finali)  
**Mavzu:** Boss AI Holatlari (State Machine), To'lqinli Lazer Hujumlari, Quvvatlantirgichlar (Power-ups: Tezlik, Qalqon), Jon Barlari (HP) va G'alaba Ekrani  
**Davomiyligi:** 45 daqiqa  

---

## 1. Darsning Pedagogik Maqsadi va Falsafasi

Ushbu dars 7–8-sinflar uchun 3-haftaning (Canvas GameDev) eng muhim va qiziqarli darsidir. Oldingi darslarda o'rganilgan barcha tushunchalar:
- HTML5 Canvas va `requestAnimationFrame` render tsikli
- Nyuton gravitatsiyasi va sakrash fizikasi
- AABB to'qnashuvlar (Collision Detection)
- Klaviatura hodisalari va `Date.now()`
- `localStorage` yuqori ballari

endi **yagona buyuk epik Boss Jangi o'yiniga (Boss Battle Arena)** birlashtiriladi!

Darsning asosiy maqsadlari:
1. **Dushman (Boss) AI Holat Mashinasi (State Machine):**
   - Boss shunchaki qotib turmaydi:
     * 1-Faza (PATROL): Chapga-o'ngga uchib patrul qiladi.
     * 2-Faza (ATTACK): Qahramonga qarab lazerlar yoki olov sharlari otadi.
     * 3-Faza (ENRAGE): Jon 30% dan kam qolganda tezlashadi va ikkitalik lazer chiqaradi.
2. **Jon (HP) Barlari va Zarar Hisobi:**
   - Boss HP (100) va Qahramon HP (3 ta jon).
   - Qahramon zarba olganda vaqtinchalik miltillash (Invulnerability frames / i-frames).
3. **Quvvatlantirgichlar (Power-ups):**
   - Osmondan tushadigan kiber-kristallar: Qalqon (Shield), Tezlik (Speed Boost), Jon tiklash (Heal).
4. **O'yinning 3 Holati (Game States):**
   - `START` -> `PLAYING` -> `GAME_OVER` / `VICTORY` (Buyuk G'alaba).

---

## 2. 45 Daqiqalik Dars Taqsimoti

| Vaqt | Bosqich | O'qituvchi va O'quvchi Faoliyati |
|---|---|---|
| **00:00 – 03:00** | Kirish va Epik Anons | "Har bir buyuk o'yinning cho'qqisi — bu Katta Boss Jangi. Bugun biz o'z 2D o'yinimizning buyuk finalini quramiz!" |
| **03:00 – 12:00** | Nazariya: Boss AI Faza Mashinasi | Slaydlar orqali Boss fazalari (Patrol, Laser Attack, Enrage), HP barlarini Canvas da chizish. |
| **12:00 – 18:00** | Power-uplar va Lazer Mexanikasi | Massivlar orqali lazerlar (`lasers.push()`) va kristallar generatsiyasi. |
| **18:00 – 24:00** | G'alaba va Mag'lubiyat Sikli | `if (boss.hp <= 0) gameState = 'VICTORY'`. |
| **24:00 – 38:00** | Amaliy O'yin (Cyber Boss Arena) | `game/index.html` to'liq 2D Canvas o'yinini o'ynash, bossni yengish va rekord o'rnatish. |
| **38:00 – 43:00** | Varaqa va Mustahkamlash | Varaqadagi Boss AI holatlari jadvali va HP algoritmini to'ldirish. |
| **43:00 – 45:00** | Xulosa va G'oliblarni Taqdirlash | 3-hafta Canvas bloki yakuni va 10 ballik baholash. |

---

## 3. O'quvchilar Ko'p Yo'l Qo'yadigan Xatolar (Tuzoqlar)

1. **Lazerlar massivini tozalamaslik:**
   - Ekrandan chiqib ketgan lazerlar xotirada qolib ketsa, bir necha daqiqadan so'ng o'yin qotishni (FPS tushishini) boshlaydi: `if (laser.y > canvas.height) lasers.splice(i, 1);`.
2. **I-Frames (Zarba daxlsizligi):**
   - Agar qahramon dushmanga tekkanda 1 soniya o'lmas qilib qo'yilmasa, 1 ta teginishning o'zida har bir kadrda 60 marta jon ketib, bir zumda o'lib qoladi!
