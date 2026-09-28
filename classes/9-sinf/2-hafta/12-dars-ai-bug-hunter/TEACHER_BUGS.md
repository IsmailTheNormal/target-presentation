# Target Cyber Arena — Maxfiy Xatolar Dosyesi (Teacher Cheat Sheet)

> **DIQQAT: Ushbu fayl FAQAT O'QITUVCHI UCHUN.** O'quvchilarga ko'rsatilmaydi.
> Dars paytida proyektor ekranida `N` (Notes) tugmasi bosilganda ham ushbu xulosalar ko'rinadi.

---

## 🎯 Dars Konsepsiyasi: "AI Bug Bounty Tournament"
- **Kohorta:** 9-A va 9-B sinflar
- **Vaqt:** 40 daqiqa (Nazariya 15 daq, Amaliy Bug Hunting 20 daq, Xulosa 5 daq)
- **Vazifa:** VS Code da o'rnatilgan AI Agent (Cline, Copilot, Cursor va h.k.) yordamida `arena/` papkasidagi koddagi yashirin xatolarni topish va tuzatish.
- **Baholash:** Har bir to'liq topilgan va tuzatilgan xato uchun **2 ball** (Jami 5 ta xato = 10 ball, 6 va 7-xatolar bonus/extra ball).

---

## 🐞 7 Ta Maxfiy Xatolar Ro'yxati (Visual + Logic)

### 1. BUG 1 (UI Misalignment): Navbar "Reyting" ssilkasining qiyshayib tushib ketishi
- **Turi:** UI / CSS Flaw
- **Simptom:** Sayt ochilganda yuqori menyuda "🏆 Reyting" ssilkasi boshqa menyu elementlaridan 55px pastga tushib, xunuk qiyshayib turadi.
- **Fayl:** `style.css` (.broken-link)
- **Xato kod:**
  ```css
  .broken-link {
    margin-top: 55px;
    display: inline-block;
    color: var(--accent) !important;
    border: 1px dashed var(--accent);
  }
  ```
- **To'g'ri yechim:** `.broken-link` dagi `margin-top: 55px;` ni olib tashlash.
- **Agentga prompt:**
  > *"Sayt navbarida 'Reyting' tugmasi 55px pastga tushib ketgan. style.css dagi .broken-link marginini to'g'irla, barcha menyu elementlari bir tekis qatorda bo'lsin."*
- **Ball:** 2 ball

---

### 2. BUG 2 (UI Overlap / z-index): Xavfsizlik to'sig'i nishoni tugmani to'sib qo'yishi
- **Turi:** UI / Click Blocker Overlap
- **Simptom:** "ENERGIYA TO'PLASH" reaktor tugmasining ustiga "🛡️ XAVFSIZLIK TO'SIG'I (BLOKIROVKA)" nishoni chiqib olgan. Tugmaning yuqori qismini bosib bo'lmaydi, chunki klik nishonga uriladi!
- **Fayl:** `style.css` (.hero-badge.overlap-flaw)
- **Xato kod:**
  ```css
  .hero-badge.overlap-flaw {
    margin-bottom: -55px; /* Tugmaning ustiga tushib qolgan */
    position: relative;
    z-index: 25;
  }
  ```
- **To'g'ri yechim:** `margin-bottom: 20px;` qilib tugmadan ajratish.
- **Agentga prompt:**
  > *"Reaktor tugmasi ustiga .hero-badge nishoni minib olgan va kliklarni to'syapti. style.css da .overlap-flaw margin-bottom ni to'g'irla, reaktor tugmasi to'liq erkin bosilsin."*
- **Ball:** 2 ball

---

### 3. BUG 3 (UI Overflow / Truncation): 2-karta (Kvant Qalqoni) kesilib qolgan
- **Turi:** UI / Layout Truncation Flaw
- **Simptom:** Kiber-Do'konda 1 va 3-kartalar to'liq ko'rinyapti, lekin 2-karta ("Kvant Qalqoni") pastki qismi kesilib qolgan, "Xarid Qilish" tugmasi umuman ko'rinmaydi!
- **Fayl:** `style.css` (.card-broken-overflow)
- **Xato kod:**
  ```css
  .card-broken-overflow {
    height: 180px;
    overflow: hidden;
  }
  ```
- **To'g'ri yechim:** `height` va `overflow: hidden` ni o'chirib tashlash.
- **Agentga prompt:**
  > *"Do'kondagi ikkinchi karta (Kvant Qalqoni) balandligi qisqarib, xarid tugmasi kesilib ketgan. .card-broken-overflow dan height va overflow:hidden ni olib tashla."*
- **Ball:** 2 ball

---

### 4. BUG 4 (UI Contrast): Qorong'i rejimda energiya raqami ko'rinmay qolishi
- **Turi:** UI / Contrast Bug
- **Simptom:** Dark Mode rejimida "To'plangan Energiya" raqami qorong'i ko'k fonda to'q ko'k rang bo'lib, mutlaqo ko'rinmaydi (faqat kursor bilan belgilaganda ko'rinadi).
- **Fayl:** `style.css` (body.dark-theme .bug-contrast-box .stat-value)
- **Xato kod:**
  ```css
  body.dark-theme .bug-contrast-box .stat-value {
    color: #0d1e38; /* Qorong'i panelda qora rang! */
  }
  ```
- **To'g'ri yechim:** `color: var(--cyan);` yoki `#00F0FF;` qilish.
- **Agentga prompt:**
  > *"Dark mode da to'plangan energiya raqami qorong'i fonda ko'rinmay qolgan. style.css da energiya hisoblagich matn rangini neon moviy (#00F0FF) ga almashtir."*
- **Ball:** 2 ball

---

### 5. BUG 5 (Logic Flaw): Energiya hisoblagichida "NaN EP" chiqishi
- **Turi:** JavaScript Logic Bug
- **Simptom:** "ENERGIYA TO'PLASH" tugmasi bosilganda son ortish o'rniga `NaN EP` (Not a Number) yozuvi paydo bo'ladi.
- **Fayl:** `script.js` (40-qator atrofida)
- **Xato kod:**
  ```javascript
  let clickBonus; // e'lon qilingan lekin qiymati yo'q (undefined)
  mineBtn.addEventListener("click", () => {
    energyScore = energyScore + clickBonus + 10; // 0 + undefined + 10 = NaN
    updateUI();
  });
  ```
- **To'g'ri yechim:** `energyScore += 10;` yoki `clickBonus = 0;` deb belgilash.
- **Agentga prompt:**
  > *"Kiber-reaktor tugmasini bosganimda hisoblagich NaN EP deb ko'rsatyapti. script.js dagi click hodisasi mantiqini tekshir va har bosilganda +10 energiya to'g'ri qo'shiladigan qil."*
- **Ball:** 2 ball

---

### 6. BUG 6 (Console Crash / Audio): Ovoz tugmasi bosilganda konsol xatosi
- **Turi:** JavaScript Event Listener / DOM ID Mismatch
- **Simptom:** "🔊 Ovoz FX" tugmasi bosilsa hech narsa bo'lmaydi. DevTools (F12) konsolida qizil xato: `Uncaught TypeError: Cannot read properties of null (reading 'addEventListener')`.
- **Fayl:** `script.js` (15-qator atrofida) va `index.html` (20-qator)
- **Xato kod:**
  ```javascript
  // HTML da id="sound-btn", lekin JS da:
  const soundBtn = document.getElementById("audio-toggle"); // null qaytaradi!
  soundBtn.addEventListener("click", ...);
  ```
- **To'g'ri yechim:** `document.getElementById("sound-btn")` deb o'zgartirish.
- **Agentga prompt:**
  > *"Konsolda 'Cannot read properties of null (reading addEventListener)' degan xato chiqyapti va ovoz tugmasi ishlamayapti. index.html dagi ID bilan script.js dagi selektorni solishtir va moslashtir."*
- **Ball:** 2 ball (yoki Bonus)

---

### 7. BONUS BUG 7 (Game Economy): Artifakt sotib olganda energiya ko'payib ketishi
- **Turi:** Logic Bug (Iqtisodiy mantiq)
- **Simptom:** Do'kondan 50 EP lik Neon Katanani sotib olsangiz, energiyangiz 50 ga kamayish o'rniga, 50 ga ko'payib ketadi!
- **Fayl:** `script.js` (55-qator)
- **Xato kod:**
  ```javascript
  energyScore = energyScore + price; // Ayirish o'rniga qo'shilgan!
  ```
- **To'g'ri yechim:** `energyScore = energyScore - price;`
- **Agentga prompt:**
  > *"Do'kondan artifakt xarid qilganda ballarim kamaymayapti, aksincha ko'payib ketyapti. buyItem funksiyasidagi matematik hisob-kitobni tuzat."*
- **Ball:** +2 Bonus ball!

---

## 🏆 O'quvchilarni Baholash Qoidasi:
- **3 ta xato tuzatilsa:** 6 ball (Qoniqarli)
- **4 ta xato tuzatilsa:** 8 ball (Yaxshi)
- **5 ta xato tuzatilsa:** 10 ball (A'lo / Kiber-Detektiv Sertifikati!)
- **Bonus xatolarni ham topsa:** +2 qo'shimcha rag'bat bali va dars g'olibi!
