# O'qituvchi uchun qo'llanma: 11-dars — LocalStorage va Doimiy Ma'lumotlar

**Kohorta:** Middle Web (7–8-sinflar)  
**Hafta / Dars:** 2-hafta / 11-dars  
**Mavzu:** Brauzer Xotirasi (LocalStorage), JSON (stringify, parse), Holat Saqlanishi (State Persistence) va O'yin Rekordlari  
**Davomiyligi:** 45 daqiqa  

---

## 1. Darsning Pedagogik Maqsadi va Falsafasi

Har bir o'yin yoki dasturda foydalanuvchi erishgan natijalar, sozlamalar (masalan, Dark Mode) va rekordlar sahifa yangilanganda (F5) yoki brauzer yopilganda o'chib ketmasligi kerak.

Ushbu darsning asosiy maqsadi:
1. **Muammoni his qilish:** O'zgaruvchilar (`let score = 500`) faqat operativ xotirada (RAM) yashaydi. F5 bosilishi bilan RAM tozalanadi va hamma narsa 0 ga tushadi.
2. **LocalStorage arxitekturasi:** Brauzer har bir domen (masalan, `localhost` yoki saytingiz) uchun alohida 5MB gacha bo'lgan doimiy kalit-qiymat (Key-Value) omborini beradi.
3. **Asosiy metodlar:**
   - `localStorage.setItem('bestScore', 950)` — qiymatni saqlash.
   - `localStorage.getItem('bestScore')` — qiymatni o'qib olish.
   - `localStorage.removeItem('key')` va `localStorage.clear()` — tozalash.
4. **JSON Serialization:** Murakkab ma'lumotlar (massivlar, o'yinchi profillari) faqat matn ko'rinishida saqlanadi: `JSON.stringify(player)` va `JSON.parse(stored)`.
5. **Yuqori Ball (High Score) Algoritmi:** `if (currentScore > savedBest) { localStorage.setItem('best', currentScore); }`.

---

## 2. 45 Daqiqalik Dars Taqsimoti

| Vaqt | Bosqich | O'qituvchi va O'quvchi Faoliyati |
|---|---|---|
| **00:00 – 03:00** | Kirish va Provokatsion Tajriba | O'yinni o'ynatish, 500 ball to'platish va to'satdan F5 (sahifani yangilash) tugmasini bosish! Ball yo'qoldi. O'quvchilarda haqli savol: "Qanday qilib saqlab qolamiz?" |
| **03:00 – 11:00** | Nazariya: RAM vs Doimiy Brauzer Xotirasi | Slaydlar orqali `localStorage` qanday ishlashi, Key-Value juftliklari, DevTools Application tabida xotirani jonli ko'rish. |
| **11:00 – 18:00** | JSON Sirlari: Ob'yektlarni Saqlash | Nega `localStorage.setItem('user', {name:'Ali'})` yozilsa `[object Object]` bo'lib qoladi? `JSON.stringify` va `JSON.parse` sehrini ochish. |
| **18:00 – 24:00** | High Score Mantiqiy Algoritmi | Yangi rekord o'rnatilganda eski rekord bilan solishtirish mantig'i. |
| **24:00 – 38:00** | Amaliy Laboratoriya (Cyber Vault) | `lab/index.html` trenajyorida shaxsiy kiber-ombor yaratish, F5 qilib tekshirish, rekordlarni saqlash. |
| **38:00 – 43:00** | Varaqa va Mustahkamlash | Varaqadagi test va amaliy topshiriqlarni to'ldirish. |
| **43:00 – 45:00** | Xulosa va Baholash | 10 ballik mezon bo'yicha baholash va keyingi 12-dars — Veb-Deploy va Katta O'yin Turniri anonsi. |

---

## 3. O'quvchilar Ko'p Yo'l Qo'yadigan Xatolar (Tuzoqlar)

1. **LocalStorage har doim String (Matn) qaytaradi:**
   - Xato: `let best = localStorage.getItem('best'); best + 10;`
   - Natija: `"50" + 10 = "5010"` (matn qo'shilishi sodir bo'ladi!).
   - Yechim: `Number(best)` yoki `parseInt(best, 10)` orqali songa o'tkazish.
2. **Bo'sh qiymatni tekshirmaslik:**
   - Birinchi marta o'yinga kirganda xotira bo'sh bo'ladi va `null` qaytadi. Shuning uchun `localStorage.getItem('best') || 0` deb yozish shart.
3. **`JSON.stringify` ni unutish:**
   - Ob'yekt yoki massivni to'g'ridan-to'g'ri saqlab qo'yish.
