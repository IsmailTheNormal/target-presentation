# O'qituvchi uchun qo'llanma: 15-dars — O'yin Fizikasi: Gravitatsiya va Sakrash

**Kohorta:** Middle Web GameDev (7–8-sinflar)  
**Hafta / Dars:** 3-hafta / 15-dars  
**Mavzu:** 2D O'yin Fizikasi, Gravitatsiya (`gravity`), Tezlanish (`velocityY`), Sakrash Impulsi (`jumpForce`) va Platformaga Qo'nish (AABB Collision)  
**Davomiyligi:** 45 daqiqa  

---

## 1. Darsning Pedagogik Maqsadi va Falsafasi

O'quvchilar 13- va 14-darslarda HTML5 Canvas va `requestAnimationFrame` o'yin tsiklini, oddiy to'g'ri chiziqli harakatni va nishonlarni o'rgandilar. Ammo haqiqiy platformer yoki arkada o'yinlarida (masalan, Mario, Flappy Bird, Sonic) harakat doimiy emas, balki **fizika qonunlariga (gravitatsiya va inertsiya)** bo'ysunadi.

Darsning asosiy maqsadi:
1. **Gravitatsiya formulasi:** Nega qahramon pastga qarab tobora tezlashadi?
   - `velocityY += gravity;` (har bir kadrda tezlikka tortish kuchi qo'shiladi).
   - `y += velocityY;` (qahramon koordinatasi tezlik miqdoriga o'zgaradi).
2. **Sakrash impulsi:**
   - Sakrash — bu qahramonga bir lahzalik kuchli **manfiy tezlik** berishdir: `velocityY = -jumpForce`.
   - Shundan so'ng gravitatsiya bu tezlikni asta-sekin kamaytiradi (0 ga tushiradi) va qahramon yana pastga qulashni boshlaydi (parabola shakli!).
3. **Erkin qulash va Pol / Platforma bilan to'qnashuv:**
   - `if (player.y + player.height >= groundY) { player.y = groundY - player.height; player.velocityY = 0; player.isGrounded = true; }`.
4. **Havo sakrashi (Double Jump) nazorati:**
   - Qahramon havoda ekanligini bilish (`isGrounded` bayrog'i) orqali cheksiz parvoz qilish xatosini oldini olish.

---

## 2. 45 Daqiqalik Dars Taqsimoti

| Vaqt | Bosqich | O'qituvchi va O'quvchi Faoliyati |
|---|---|---|
| **00:00 – 03:00** | Kirish va Fizika Taassuroti | "Nega kosmosda suzamiz, Y奇rda esa sakraganimizda qaytib tushamiz? O'yinlarda Nyuton qonunlari qanday dasturlanadi?" |
| **03:00 – 12:00** | Nazariya: Gravitatsiya va Parabola | Slaydlar orqali `velocityY`, `gravity` va sakrash impulsi matematikasi. Doskada parabola traektoriyasini chizish. |
| **12:00 – 18:00** | AABB To'qnashuv va Platformaga Qo'nish | Qahramon pol tagiga o'tib ketmasligi uchun chegara shartlari. |
| **18:00 – 24:00** | Havo Boshqaruvi va Double Jump | Bo'shliq (Space) tugmasini bosganda faqat yerda bo'lsagina sakrash mantig'i. |
| **24:00 – 38:00** | Amaliy Laboratoriya (Cyber Jumper) | `lab/index.html` simulyatorida gravitatsiya parametrlarini sozlash (oy tortishi, yer tortishi, og'ir tortishish). |
| **38:00 – 43:00** | Varaqa va Mustahkamlash | Varaqadagi fizika formulalari va koordinata hisob-kitoblarini to'ldirish. |
| **43:00 – 45:00** | Xulosa va 16-dars Anonsi | Arkada yakuni: Boss Jangi, Lazerlar va Quvvatlantirgichlar anonsi. |

---

## 3. O'quvchilar Ko'p Yo'l Qo'yadigan Xatolar (Tuzoqlar)

1. **Y-o'qi yo'nalishi:**
   - Matematikada Y-o'qi tepaga qarab o'sadi, ammo **Kompyuter grafikasi va Canvas da Y-o'qi pastga qarab o'sadi!**
   - Shuning uchun sakrash — manfiy son (`-12`), yerga tushish esa musbat son (`+gravity`).
2. **Doimiy tezlik bilan sakratish:**
   - `y -= 10` deb yozish — bu robotdek bir xil harakat. Haqiqiy jism parabolik sekinlashishi shart.
3. **`isGrounded` bayrog'ini yangilamaslik:**
   - Agar yerga tekkanini tekshirmasangiz, o'yinchi probelni bosib cheksiz osmonga uchib ketadi.
