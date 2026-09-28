# O'qituvchi uchun qo'llanma: 10-dars — AI Debugging va Dastur Mantig'i

**Kohorta:** Middle Web (7–8-sinflar)  
**Hafta / Dars:** 2-hafta / 10-dars  
**Mavzu:** AI Debugging, Brauzer DevTools, Xatolar Turlari (Syntax, Runtime, Logic) va Konsol Tahlili  
**Davomiyligi:** 45 daqiqa  

---

## 1. Darsning Pedagogik Maqsadi va Falsafasi

O'quvchilar oldingi darslarda HTML/CSS asoslarini va DOM hodisalarini (`click`, `input`, `Date.now()`) o'rgandilar. Ammo dasturlashda eng ko'p vaqt kod yozishga emas, **xatolarni topish va tuzatishga (Debugging)** sarflanadi.

Ushbu darsning tub maqsadi:
1. **Qo'rquvni yo'qotish:** Qizil xato yozuvlari (Error) — dushman emas, dasturchining eng sodiq maslahatchisidir.
2. **Uch asosiy xato toifasini ajrata olish:**
   - **Syntax Error (Sintaksis xatosi):** Qavs, nuqta-vergul yoki qo'shtirnoq yopilmagan. Kod umuman ishga tushmaydi.
   - **Runtime Error (Ijro xatosi):** `TypeError: Cannot read properties of null` yoki `ReferenceError: x is not defined`. Kod ishga tushadi, ammo ma'lum bosqichda to'xtab qoladi.
   - **Logic Error (Mantiqiy xato):** Kod xatosiz ishlaydi, ammo noto'g'ri natija beradi (masalan, ball qo'shilishi o'rniga ayriladi).
3. **DevTools Konsolini ochish va tahlil qilish:** `F12` yoki `Ctrl+Shift+I` orqali Console tabini o'qish, qator raqamini (line number) topish.
4. **AI Debugger Workflow:** Xato matnini va kod qismini AI ga to'g'ri berib, tushuntirish va yechim so'rash.

---

## 2. 45 Daqiqalik Dars Taqsimoti

| Vaqt | Bosqich | O'qituvchi va O'quvchi Faoliyati |
|---|---|---|
| **00:00 – 03:00** | Kirish va Psixologik Tayyorgarlik | "Eng zo'r dasturchi — xato qilmaydigan emas, xatoni tez topadigan dasturchidir". Birinchi bug (tarix: 1947-yil Grace Hopper va haqiqiy kuya/moth). |
| **03:00 – 10:00** | Nazariya: 3 Xato Turi | Slaydlar orqali Syntax, Runtime va Logic xatolarini solishtirish. Real kod misollari. |
| **10:00 – 16:00** | Brauzer DevTools va Konsol | `console.log()`, `console.error()`, `console.warn()`. Qator raqami va stack trace qanday o'qiladi. |
| **16:00 – 22:00** | AI bilan Debugging (Prompt Taktikasi) | Qanday qilib xatoni AI ga berish kerak? "Kodim ishlamayapti" EMAS, balki "Mana kod, mana xato matni, nega bu sodir bo'ldi?" |
| **22:00 – 38:00** | Amaliy Laboratoriya (Cyber Bug Lab) | `lab/index.html` interaktiv trenajyorida 3 ta buzuq reaktor modulini tuzatish. |
| **38:00 – 43:00** | Varaqa va Mustahkamlash | Varaqadagi xatolarni qo'lda topish va 10 ballik mezon bo'yicha baholash. |
| **43:00 – 45:00** | Xulosa va Keyingi Dars Anonsi | LocalStorage va doimiy ballar tizimiga o'tish anonsi. |

---

## 3. O'quvchilar Ko'p Yo'l Qo'yadigan Xatolar (Tuzoqlar)

1. **`document.querySelector` da `#` yoki `.` ni unutish:**
   - Xato: `document.getElementById('#btn')` yoki `document.querySelector('btn')`.
   - Natija: Element topilmaydi (`null`), keyingi satrda `Cannot read properties of null (reading 'addEventListener')` chiqadi.
2. **Katta-kichik harflar (Case Sensitivity):**
   - `onclick` o'rniga `onClick`, `addEventListener` o'rniga `addEventlistener`.
3. **Mantiqiy if shartlarida `=` bilan `===` ni adashtirish:**
   - `if (score = 100)` har doim rost bo'lib qoladi va qiymatni o'zgartirib yuboradi!

---

## 4. 10 Ballik Baholash Mezoni

- **1–3 ball:** Konsolni ochish, xatolar turlarini (Syntax, Runtime, Logic) to'g'ri ajratish.
- **4–7 ball:** DevTools konsolidagi qator raqamini topish va `lab/index.html` dagi 2 ta xatoni tuzatish.
- **8–10 ball:** Barcha 3 ta modulni to'liq tuzatish, AI ga to'g'ri tuzilgan prompt berib javob olish va varaqani to'ldirish.
