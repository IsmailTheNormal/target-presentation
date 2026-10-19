# 28-Dars: O'qituvchi Uchun Metodik Qo'llanma va Imtihon Kaliti (Teacher Guide & Fixes)
**Target International School // 9-Sinf // 8-Hafta (1-Chorak Oraliq Nazorat: 40 daqiqa)**
**Mavzu:** Full-Stack Xavfsiz Servis Imtihoni (Frontend UI, Express MVC, SQLite, XSS/CSRF va Docker)
**Kohorta:** `9A 9B` (Junior Vibecoders, Full-Stack & CyberSecurity)

---

## 1. Asosiy Pedagogik Maqsad
Ushbu oraliq nazorat darsida 9-sinf o'quvchilari 1-chorak davomida bosqichma-bosqich o'rgangan barcha modullarini yagona ishlaydigan Full-Stack xizmatida sinovdan o'tkazadilar:
1. **Frontend:** Vanilla JS interfeysi va DOMPurify orqali XSS xavfidan tozalangan render.
2. **Backend:** Express.js MVC arxitekturasi va xavfsizlik middleware zanjiri (Helmet, CORS, Rate Limiting).
3. **Database:** SQLite reliesion jadvalida `users` va `orders` ma'lumotlarini parametrlangan Prepared Statements (`?` placeholder) orqali SQL Injection dan 100% himoyalash.
4. **DevOps & Sandbox:** Servisni yengil `node:alpine` tasvirida va xavfsiz `USER node` (non-root) direktivasi bilan Docker konteynerida izolyatsiya qilish.

---

## 2. 40 Daqiqalik Dars Reglamenti

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 03:00** | Kirish va Reglament | Oraliq nazoratning 4 ta muhandislik kvesti va 10 ballik mezonini e'lon qilish. | Noutbuklarni ochish, test varaqalarini tayyorlash. |
| **03:00 – 09:00** | Nazariya va Arxitektura Tahlili | Slaydlar orqali Middleware zanjiri, Prepared Statements va Docker perimetrini ko'rsatish. | Interaktiv savol-javobda qatnashish. |
| **09:00 – 15:00** | Jonli Kiber-Test Tahlili | Slayd 9 dagi kod zaifligini sinf bilan birga tekshirish va "Fix" tugmasini ochib tushuntirish. | O'z fikrlarini aytish, to'g'ri tashxisni aniqlash. |
| **15:00 – 35:00** | Amaliy Nazorat va Varaqa Bajarilishi | O'quvchilar shaxsiy `varaqa.html` va kod muharririda 4 ta kvestni mustaqil yechadilar. | Kodni yozish, testlarni topshirish va natijalarni qayd etish. |
| **35:00 – 40:00** | Xulosa va Uy Vazifasini Tushuntirish | 1-chorak natijalarini sarhisob qilish, `vazifa.html` dagi mustaqil uy topshirig'ini topshirish. | Varaqalarni topshirish, uy vazifasini saqlab olish. |

---

## 3. Test Savollari va O'qituvchi Yechimlar Kaliti (Test & Fixes Key)

### Test 1: Express Serverdagi Kritik Zaiflik
* **Savol:** Quyidagi kodda qanday xavf bor?
  ```javascript
  app.post('/api/profile', (req, res) => {
    const query = "UPDATE users SET bio = '" + req.body.bio + "' WHERE id = " + req.user.id;
    db.run(query);
    res.send("<h1>Updated:</h1><div>" + req.body.bio + "</div>");
  });
  ```
* **To'g'ri tashxis:** Bir vaqtning o'zida ham **SQL Injection** (satr birlashtirish orqali), ham **Stored/Reflected XSS** (innerHTML orqali to'g'ridan-to'g'ri chiqarish)!
* **Etalon Yechim (Teacher Fix):**
  ```javascript
  app.post('/api/profile', (req, res) => {
    // 1. SQLi tuzatmasi: Parametrlangan so'rov
    const query = "UPDATE users SET bio = ? WHERE id = ?";
    db.run(query, [req.body.bio, req.user.id], function(err) {
      if (err) return res.status(500).json({ error: "Baza xatosi" });
      // 2. XSS tuzatmasi: JSON qaytarish yoki DOMPurify tozalash
      res.json({ success: true, message: "Profil muvaffaqiyatli yangilandi" });
    });
  });
  ```

---

## 4. Uy Vazifasi (`vazifa.html`) Baholash Mezoni (10 Ball)
1. **Express & SQLite Integratsiyasi (4 ball):** Parametrlangan Prepared Statement (`?`) xatosiz qo'llangan, tashqi kalitlar yaxlitligi buzilmagan.
2. **XSS va CSRF Qalqoni (3 ball):** DOMPurify va textContent to'g'ri tushuntirilgan, HttpOnly va SameSite cookie bayroqlari asoslangan.
3. **Docker Izolyatsiyasi (2 ball):** Dockerfile da node:alpine va USER node direktivalari xatosiz kiritilgan.
4. **Analitik Xulosa va Toza Kod (1 ball):** Texnik atamalarning aniqligi va savollarga to'liq javob berilganligi.
