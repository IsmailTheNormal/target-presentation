# 29-Dars: O'qituvchi Uchun Metodik Qo'llanma va Yechimlar Kaliti
**Target International School // 9-Sinf // 10-Hafta (2-Chorak 1-Darsi: 40 daqiqa)**
**Mavzu:** Zamonaviy JavaScript (ES6+): Modullar va Asinxron Chuqurlik
**Kohorta:** `9A 9B` (Junior Vibecoders, Full-Stack & DevOps Track)

---

## 1. Asosiy Pedagogik Maqsad
Bugungi dars bilan 9-sinf o'quvchilari **2-Chorak: Agentik Dasturlash va Avtonom Tizimlar** bosqichiga kirishadilar:
1. **ES Modullar:** Global namespace to'qnashuvlaridan xoli bo'lgan mustaqil fayllar arxitekturasi (`export` va `import`).
2. **ES6+ Sintaksisi:** Destructuring (`const { id } = obj`) va Spread/Rest (`...`) yordamida ma'lumotlarni o'zgartirmasdan nusxalash (Immutability).
3. **Event Loop Mexanikasi:** Call Stack (sinxron), Microtask Queue (Promises) va Macrotask Queue (`setTimeout`) iyerarxiyasini tushunish.
4. **Xavfsiz Asinxron Oqim:** `try / catch / finally` bilan har qanday tarmoq va API xatolarini ushlash.

---

## 2. 40 Daqiqalik Dars Reglamenti

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 03:00** | Kirish & 2-Chorak Anonsi | 2-Chorakda AI agentlar va avtonom tizimlar yaratilishini e'lon qilish. | Noutbuklarni ochish, dars rejasini ko'rish. |
| **03:00 – 08:00** | Aqliy Hujum (Spaghetti Kod) | Nega 3000 qatorli bitta fayl loyihani halokatga yetaklashini savol-javob qilish. | Fikr bildirish, xatolar sababini tahlil qilish. |
| **08:00 – 18:00** | Nazariya va Arxitektura | 12 slaydli taqdimot, Named/Default export va Event Loop mexanizmini tushuntirish. | Asosiy qoidalarni konspekt qilish. |
| **18:00 – 23:00** | Jonli Kiber-Test (Event Loop) | Slayd 9 dagi kodning konsolga chiqish tartibini birgalikda yechish. | Tartibni aniqlash, to'g'ri variantni tanlash. |
| **23:00 – 36:00** | Amaliy Modulli Laboratoriya | O'quvchilar 3 ta modulli (api.js, format.js, app.js) valyuta dasturini quradilar. | Kod yozish, modullarni ulash, xatolarni sinash. |
| **36:00 – 40:00** | Xulosa & Baholash | 10 ballik mezon asosida toza modulli ishlarga baho qo'yish, `vazifa.html` ni berish. | Ishlarni ko'rsatish, vazifani saqlab olish. |

---

## 3. Viktorina va Topshiriqlar Yechimi (Teacher Fixes)

### Viktorina (Slayd 9):
* **Savol:** Konsolga qaysi tartibda chiqadi? (1, setTimeout 2, Promise 3, 4)
* **To'g'ri javob:** **B) 1 -> 4 -> 3 -> 2**
* **Izoh:** 1 va 4 darhol Call Stack-da bajariladi. Keyin Microtask navbati (Promise 3) tozalanadi. Eng oxirida Macrotask (setTimeout 2) ishga tushadi.

### Uy Vazifasi Yechimlari:
1. **Modullarga ajratish:** taxCalculator.js (`calcTax`), dbService.js (`Database`), notifyService.js (`sendSMS`).
2. **Microtasks vs Macrotasks:** Event Loop spetsifikatsiyasi bo'yicha har bir sinxron amaldan keyin Microtask-lar (Promise) to'liq bajarilishi shart, shundan so'ngгина Macrotask (setTimeout) olinadi.
3. **try/catch/finally:** `finally` bloki qanday xato bo'lishidan qat'i nazar loading spinnerrini o'chiradi.
4. **Spread nusxalash:** `user2 = user1` xotiradagi bitta linkka qaraydi (biri o'zgarsa ikkinchisi ham buziladi). `{ ...user1 }` esa mustaqil yangi klon hosil qiladi.

---

## 4. Baholash Mezoni (10 Ball)
* **3 Ball:** ES Modules (`export` va `import`) to'g'ri ajratilgan va ishlatilgan.
* **3 Ball:** `async/await` va `try/catch/finally` zanjiri to'liq sozlangan.
* **2 Ball:** Destructuring va Spread operatori o'rinli qo'llangan.
* **2 Ball:** Event Loop ketma-ketligi to'g'ri tahlil qilingan va interfeys qotmaydi.
