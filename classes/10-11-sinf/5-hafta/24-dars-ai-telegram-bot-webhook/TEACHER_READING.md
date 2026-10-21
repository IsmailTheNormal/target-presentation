# 24-Dars: O'qituvchi Uchun Metodik Qo'llanma va Texnik Kalit (Teacher Guide & Fixes)
**Target International School // 10–11-Sinf // 5-Hafta (40 daqiqa)**
**Mavzu:** Shaxsiy AI Telegram Bot: Webhooklar, VS Code Port Forwarding va LLM Integratsiyasi
**Kohorta:** `10A 10B 11A 11B` (Senior AI & Vibecoding)

---

## 1. Asosiy Pedagogik Maqsad
O'quvchilarni ChatGPT veb-saytidagi oddiy foydalanuvchilikdan chiqarib, Telegram platformasida o'zlarining shaxsiy sun'iy intellekt xizmatlarini ishlab chiquvchi dasturchi darajasiga ko'tarish. Darsda:
1. Long Polling va Event-Driven Webhook arxitekturasi farqini ko'rsatish;
2. VS Code Dev Tunnels yordamida `localhost:3000` ni global internetda rasmiy Microsoft SSL sertifikati bilan ommaviy HTTPS ga ochish;
3. Telegram `setWebhook` API chaqiruvi orqali xabarlarni tutish va Groq/DeepSeek LLM bilan jonli muloqotni yo'lga qo'yish.

---

## 2. 5 Daqiqalik Darsoldi Konspekti (Teacher Briefing)

* **00–05 daqiqa (Qiziqish uyg'otish):** 
  Sinfdan so'rang: *"Orangizda kim har kuni ChatGPT ishlatadi? Uni o'zingizning Telegramingizga ulab, do'stlaringizga yuborishni xohlaysizmi?"*.
* **05–15 daqiqa (Nazariya & BotFather):** 
  Doskaga Polling va Webhook chizmasini chizing. O'quvchilar telefonda `@BotFather` ga kirib `/newbot` buyrug'i orqali token olishadi.
* **15–28 daqiqa (VS Code Dev Tunnels):** 
  `bot/server.js` ni ishga tushirish (`npm start`). VS Code da "Ports" panelidan `3000` portini ochish va o'ng tugma bilan **"Port Visibility: Public"** qilish (eng ko'p xatolik shu yerda bo'ladi!).
* **28–38 daqiqa (Webhook ulash va Sinash):** 
  Brauzerda `https://api.telegram.org/bot<TOKEN>/setWebhook?url=<DEV_TUNNEL_URL>/webhook` ni ochish. Telefonda botga `/start` yozib, terminalda jonli JSON paketlarini kuzatish.
* **38–40 daqiqa (Baholash):** 
  Sinfdoshlar bir-birining botiga yozib ko'radi, 10 ballik baholash mezonlari to'ldiriladi.

---

## 3. O'quvchilar Yo'l Qo'yadigan 3 Ta Odatiy Xato va Yechim (Remediation)

### 1-Xato: Telegram `401 Unauthorized` yoki `Connection Refused` berishi
* **Sabab:** O'quvchi VS Code da portni ochgan, lekin **Port Visibility** ni `Private` holatda qoldirgan. Microsoft Dev Tunnels begona so'rovlarni (shu jumladan Telegramni) login oynasi bilan to'sib qo'yadi.
* **Yechim:** Ports panelida port ustiga sichqonchaning o'ng tugmasi bosiladi &rarr; `Port Visibility` &rarr; `Public` qilinadi.

### 2-Xato: Bot bitta xabarga 5 marta ketma-ket javob qaytaraverishi
* **Sabab:** Telegram serveri bizning serverimizdan 3–5 soniya ichida `HTTP 200 OK` olmasa, xabar yetib bormadi deb o'ylab, yana qayta yuboradi (Webhook Retry Policy).
* **Yechim:** Express marshrutining eng birinchi qatoriga `res.sendStatus(200);` qo'yilishi shart. AI javobi esa asinxron tarzda `sendMessage` orqali yuboriladi.

### 3-Xato: `TypeError: Cannot read properties of undefined (reading 'text')`
* **Sabab:** Foydalanuvchi botga rasm, stiker yoki ovozli xabar yuborganida `req.body.message.text` mavjud bo'lmaydi va server to'xtab qoladi.
* **Yechim:** Marshrut boshida himoya tekshiruvi:
  ```javascript
  if (!update || !update.message || !update.message.text) return;
  ```

---

## 4. Rasmiy 10 Ballik Baholash Mezoni (Rubric)
1. **BotFather Tokeni va .env himoyasi (2 ball):** Token to'g'ri olingan, `.env` faylida saqlangan va `.gitignore` ga kiritilgan.
2. **VS Code Dev Tunnels va Webhook (3 ball):** 3000-port Public qilingan, Webhook Telegram bilan muvaffaqiyatli ulangan (`result: true`).
3. **LLM Integratsiyasi va Tizimli Shaxsiyat (3 ball):** Groq / DeepSeek API ulangan, System Prompt botga aniq va do'stona xarakter bergan.
4. **Jonli Namoyish (2 ball):** Telefondan yuborilgan xabarlarga xatosiz va zudlik bilan javob qaytaradi.
