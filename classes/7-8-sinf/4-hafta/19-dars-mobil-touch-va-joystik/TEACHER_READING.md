# O'qituvchi uchun qo'llanma: 19-dars — Mobil Moslashuv, Touch Hodisalari va Virtual Joystik

**Kohorta:** 7–8-sinf  
**Hafta / Dars:** 4-hafta / 19-dars  
**Mavzu:** Touch Events API (touchstart, touchmove, touchend), Multi-Touch boshqaruvi, `touch-action: none` va Virtual Analog Joystik Matematikasi  
**Davomiyligi:** 45 daqiqa  

---

## 1. Darsning Pedagogik Maqsadi va Muhandislik Falsafasi

Statistika bo'yicha dunyodagi veb-o'yinlarning 70% dan ortig'i smartfon va planshetlarda o'ynaladi. Ammo maktab o'quvchilari o'yin yaratganda uni faqat noutbuk klaviaturasi (`keydown ArrowRight`, `Space`) bilan cheklab qo'yishadi. Smartfonda esa klaviatura yo'q!

Ushbu darsda o'quvchilar kompyuter o'yinini to'laqonli mobil qurilmalarga moslashtirishni (Mobile First Game Architecture) o'rganadilar:
1. **Touch Events API:**
   - `touchstart` — barmoq sensorli ekranga tekkan lahza.
   - `touchmove` — barmoq ekranda siljishi (analog boshqaruv).
   - `touchend` — barmoq ekrandan ko'tarilishi (harakatni to'xtatish).
   - `e.touches` (ekrandagi barcha barmoqlar) va `e.changedTouches` (aynan shu hodisaga sabab bo'lgan barmoqlar).
2. **Brauzer Parazit Harakatlarini Bloklash:**
   - Ekranni tortganda sahifa pastga aylanib ketmasligi (scroll) va kattalashib ketmasligi (pinch-to-zoom) uchun:
     CSS: `touch-action: none; user-select: none;`
     JS: `e.preventDefault()`.
3. **Virtual Analog Joystik Matematikasi:**
   - Joystik bazasi markazi $(x_0, y_0)$ va radiusi $R$.
   - Foydalanuvchi barmog'i $(x, y)$ koordinataga borganda, masofa hisoblanadi:
     $$dist = \sqrt{(x - x_0)^2 + (y - y_0)^2}$$
   - **Vektorni Cheklash (Clamping):** Agar $dist > R$ bo'lsa, tutqich doira ichida qolishi shart:
     $$\text{knobX} = x_0 + \frac{x - x_0}{dist} \times R, \quad \text{knobY} = y_0 + \frac{y - y_0}{dist} \times R$$
   - **Normalizatsiya:** O'yin dvijogiga $-1.0 \dots +1.0$ oralig'idagi silliq qiymat uzatiladi:
     $$\text{inputX} = \frac{\text{knobX} - x_0}{R}, \quad \text{inputY} = \frac{\text{knobY} - y_0}{R}$$
4. **Multi-Touch (Ikki Qo'l bilan Boshqaruv):**
   - Chap barmoq — qahramonni joystik bilan yurgizish.
   - O'ng barmoq — "JUMP" yoki "BLASTER" tugmasini bosish. Har bir barmoq o'zining noyob `identifier` ID raqamiga ega.

---

## 2. 45 Daqiqalik Dars Taqsimoti

| Vaqt | Bosqich | O'qituvchi va O'quvchi Faoliyati |
|---|---|---|
| **00:00 – 03:00** | Kirish va Mobil Savol | "O'yiningizni do'stlaringizga yubordingiz. Ular telefonida ochishdi, ammo klaviatura yo'qligi uchun qahramon qimirlamadi! Buni qanday hal qilamiz?" |
| **03:00 – 12:00** | Nazariya: Touch Events | `touchstart`, `touchmove`, `touchend`. Sichqoncha (`mousedown`) va Barmoq (`touch`) o'rtasidagi farqlar. |
| **12:00 – 18:00** | Nazariya: Virtual Joystik | Joystik bazasi, doira radiusi $R$, Pifagor teoremasi orqali masofani cheklash va normalizatsiya. |
| **18:00 – 24:00** | Multi-Touch va Parazit Scroll | Nega `touch-action: none` va `e.preventDefault()` bo'lmasa o'yin o'rniga sayt aylanib ketadi. |
| **24:00 – 38:00** | Amaliy Laboratoriya (Mobile Touch Studio) | `lab/index.html` interaktiv trenajyorida: virtual joystik va sensorli sakrash tugmalarini sozlash, barmog'i bilan qahramonni boshqarish! |
| **38:00 – 43:00** | Varaqa va Mustahkamlash | Joystik vektor cheklash formulalarini va Touch hodisalari ketma-ketligini varaqaga yozish. |
| **43:00 – 45:00** | Xulosa va Baholash | 10 ballik mezon bo'yicha baholash va oxirgi 20-dars (Kiber-Arkada Final Game Jam va Deploy) bilan bog'lash. |

---

## 3. O'quvchilar Ko'p Yo'l Qo'yadigan Xatolar (Tuzoqlar)

1. **`e.clientX` o'rniga `e.touches[0].clientX` ni unutish:**
   - Sichqoncha hodisasida koordinata to'g'ridan-to'g'ri `e.clientX` da bo'ladi. Touch hodisasida esa birdaniga 5 ta barmoq tegishi mumkin, shuning uchun koordinata `e.touches[0].clientX` massivida saqlanadi.
2. **`touchend` da `e.touches[0]` ga murojaat qilish:**
   - Barmoq ekrandan ko'tarilganda, `e.touches` massivi bo'shab qoladi (`length == 0`). Shuning uchun `touchend` da `e.changedTouches[0]` dan foydalanish shart!
3. **Joystik tutqichi cheksiz uchib ketishi:**
   - Agar $dist > R$ tekshiruvi (clamping) qo'yilmasa, barmoq ekranning boshqa burchagiga borganida joystik tutqichi o'z bazasidan chiqib ketadi.
