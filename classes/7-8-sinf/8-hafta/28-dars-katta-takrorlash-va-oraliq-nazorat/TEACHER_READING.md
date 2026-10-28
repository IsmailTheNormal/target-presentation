# 28-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Prep Guide)
**Target International School // 7–8-Sinflar (12–14 yosh) // 8-Hafta (1-Soat: 40 daqiqa)**
**Mavzu:** 1-Chorak Katta Takrorlash va Oraliq Nazorat (Game Dev, Canvas 2D, O'yin Fizikasi, FUT va Web API)
**O'qituvchi:** **Ismoiljon Usmonov** · Yunusobod filiali
**Kohorta:** `7A 7B 8A 8B` (Vibecoding & Interactive Systems Track)

> **ASOSIY PEDAGOGIK MAQSAD:**
> Ushbu dars 7–8-sinf o'quvchilarining 1-chorak davomida (1–27-darslar) o'rgangan barcha fundamental ko'nikmalarini umumlashtirish, tizimlashtirish va rasmiy oraliq nazorat imtihoniga (`tests/TEST_7-8_SINF_VIBECODING.docx` va `test.html`) 100% tayyorlashga bag'ishlangan. Dars davomida o'quvchilar LLM prompt injiniringi, SVG vektor grafikasi, semantik HTML, CSS Flexbox markazlashtirish, JavaScript DOM hodisalari, `localStorage` doimiyligi, Canvas 2D 60 FPS o'yin tsikli (`requestAnimationFrame`), tortishish kuchi va AABB to'qnashuv fizikasi, Web Audio API, FUT kartochkalar matematikasi (OVR formulasi, 11 tugunli kimyo graflari, 5% savdo solig'i) hamda yuz biometriyasi (Face ID 68 nuqta va EAR liveness testi) bo'yicha mustahkam xulosalar hosil qiladilar.

---

## 1. Dars Materiallari va Ekosistema

1. **Minimalist Tipografik Prezentatsiya (12 Slayd):**
   * Manzil: `prezentatsiya.html`
   * Format: Minimalist Keynote dizayni, Zero Bottom Bar, suzuvchi oynaviy kapsula `[UZ | RU | EN]`, mavzu almashtirgich (Dark/Light), suzuvchi hisoblagich `‹ 01 / 12 ›` va dars fazasi nishoni.
   * Klaviatura boshqaruvi: `→` / `←` (slaydlar), `N` (o'qituvchi izohlari), `L` (til almashtirish: UZ / RU / EN), `T` (mavzu), `H` (panellarni yashirish).
2. **Chop Etiladigan Ishchi Varaqa (2 Betlik A4 Konspekt & Sinov):**
   * Manzil: `varaqa.html`
   * 1-bet: 4 ta modul bo'yicha formula va kod konspekti (CSS Flexbox, DOM & LocalStorage, Canvas 2D va fizika jadvali, FUT & Biometrika).
   * 2-bet: 4 ta amaliy imtihon topshirig'i (har biri 2.5 ball, jami 10 ball) va rasmiy baholash rubrikasi.
3. **Interaktiv Uy Vazifasi Ilovasi:**
   * Manzil: `vazifa.html`
   * 4 ta amaliy muhandislik topshirig'i, LocalStorage avto-saqlash, "Yechimni ko'rish (Fix)" kaliti va chop etish (Print to PDF) imkoniyati.
4. **Oraliq Nazorat Kiber-Testi (Onlayn Simulyator):**
   * Manzil: `test.html`
   * 25 ta rasmiy test savoli (A–E variantlar), har bir savol 1 balldan (jami 25 ball), avtomatik tekshirish, natijalar modali, baho nishoni (A'lo / Yaxshi / Qoniqarli / Qoniqarsiz) va batafsil xatolar tahlili.
5. **Google Forms Avtomatlashtirish Skripti:**
   * Manzil: `google_form.gs`
   * 1 bosishda Google Forms da tayyor test (UZ va RU variantlarida) yaratish funksiyasi.
6. **Chop Etiladigan Rasmiy Imtihon Fayli:**
   * Manzil: `tests/TEST_7-8_SINF_VIBECODING.docx` (Seed 708 asosida to'liq randomizatsiya qilingan javoblar kaliti bilan).

---

## 2. 40 Daqiqalik Darsning Aniq Vaqt Taqsimoti (Pacing Clock)

| Vaqt | Bosqich & Slayd | O'qituvchi (Ismoiljon Usmonov) Harakati | O'quvchilar Faoliyati |
|---|---|---|---|
| **00:00 – 03:00** (3 daq) | **Slayd 1: Kirish & Dars Xaritasi** | 1-chorakda bosib o'tilgan 27 ta dars yo'lini ko'rsatish: "Biz oddiy veb-matnlardan boshlab to'liq Canvas o'yinlari, FUT simulyatori va sun'iy intellektli kiber-skanerlargacha qurdik. Bugun bilimlarimizni to'liq tartibga solamiz va imtihonga tayyorlanamiz!" | Reja bilan tanishadilar, konspekt varaqasining (varaqa.html) 1-betini ochadilar. |
| **03:00 – 06:00** (3 daq) | **Slayd 2: AI Prompt va SVG Grafikasi** | Promptning 4 qismi: `[Rol] + [Kontekst] + [Vazifa] + [Format]`. Nega SVG formati kattalashtirilganda xiralashmasligini matematik tushuntirish (vektor koordinatalar vs piksellar). | Prompt formulasini va SVG afzalligini varaqaga yozib oladilar. |
| **06:00 – 09:00** (3 daq) | **Slayd 3: Semantik HTML va Flexbox** | `<main>` semantik tegi. CSS Flexbox: `display: flex; justify-content: center; align-items: center;` orqali gorizontal va vertikal markazlashtirish qoidasi. | Flexbox xossalarini tekshirib, varaqadagi 1-topshiriq kodi bilan bog'laydilar. |
| **09:00 – 12:00** (3 daq) | **Slayd 4: JavaScript DOM va Hodisalar** | `btn.addEventListener('click', fn)` sintaksisi. DevTools konsolida xatolarni o'qish (qizil xatolar, stack trace). `performance.now()` orqali millisoniyalarni o'lchash. | Konsol ochishni (F12) eslaydilar, klik hodisasini mustahkamlaydilar. |
| **12:00 – 15:00** (3 daq) | **Slayd 5: LocalStorage va Doimiy Xotira** | `localStorage.setItem('highScore', val)` va `getItem`. Brauzer yangilanganda ma'lumotlar saqlanib qolish sababi. JSON.stringify va JSON.parse. | Rekord saqlash mantig'ini qayd etadilar. |
| **15:00 – 19:00** (4 daq) | **Slayd 6: Canvas 2D va 60 FPS Game Loop** | `<canvas>` elementi, 2D kontekst. Nega har bir yangi kadrda `ctx.clearRect()` chaqirilishi shartligi (eski izlarni o'chirish) va `requestAnimationFrame(gameLoop)` ning 60 FPS roli. | O'yin tsikli ketma-ketligini (Tozalash -> Yangilash -> Chizish) yodga oladilar. |
| **19:00 – 23:00** (4 daq) | **Slayd 7: O'yin Fizikasi va AABB To'qnashuv** | Tortishish kuchi: har kadrda `vy += g`. Sakrash: `vy = -jumpPower`. To'g'ri to'rtburchaklar to'qnashuvi (AABB) formulasini tahlil qilish. | AABB formulasini varaqadagi jadvaldan ko'rib, matematik shartini tushunadilar. |
| **23:00 – 26:00** (3 daq) | **Slayd 8: Web Audio, Kamera va Touch** | Web Audio API (AudioContext va OscillatorNode — procedural tovushlar). Kamera skrollingi (dunyo siljishi). Sensor ekranlar uchun `touchstart` hodisasi. | Mobil o'yinlar va veb-audio arxitekturasini mustahkamlaydilar. |
| **26:00 – 30:00** (4 daq) | **Slayd 9: FUT Kimyo Graflari va Virtual Iqtisodiyot** | OVR vaznli reytingi. 11 tugunli jamoa kimyo graflari (klub, liga, millat bo'yicha maksimal 33 ball). EA ning 5% Transfer solig'i (Coin Sink — giperinflyatsiyani to'xtatuvchi soliq). | Futbol simulyatori va virtual iqtisod mexanikasini takrorlaydilar. |
| **30:00 – 34:00** (4 daq) | **Slayd 10: Kompyuter Ko'rishi va Biometrika** | Kiber-Ko'z: Frame Differencing (piksellar farqi orqali harakatni aniqlash). Face ID: 68 ta tayanch nuqta (Landmarks). EAR ko'z qisish formulasi va 2D soxta fotosuratlarni fosh etish (Anti-Spoofing). | EAR formulasi va liveness testini ko'rib chiqadilar. |
| **34:00 – 38:00** (4 daq) | **Slayd 11: Jonli Test va 4 Amaliy Topshiriq** | Slayddagi interaktiv testni yechish. Varaqaning 2-betidagi 4 ta amaliy kiber-topshiriqni mustaqil ishlash: 1) Flexbox, 2) addEventListener, 3) Canvas loop & AABB, 4) FUT & EAR. | 4 ta topshiriq javoblarini yozadilar, "Fix" tugmasi orqali tekshiradilar. |
| **38:00 – 40:00** (2 daq) | **Slayd 12: Yakun va Imtihon Ko'rsatmalari** | 25 ballik imtihon tuzilmasi, vaqtni to'g'ri taqsimlash (har savolga 1 daqiqa), vazifa.html va test.html orqali uyda tayyorgarlik ko'rish vazifasi. | Savollar beradilar, imtihonga to'liq shay holatda darsni yakunlaydilar. |

---

## 3. Rasmiy Oraliq Imtihonining 25 Savoli Uchun To'liq Javoblar Kaliti

Ushbu kalitlar `tests/TEST_7-8_SINF_VIBECODING.docx` va `test.html` simulyatoridagi **Seed 708** asosida aralashtirilgan tartib bilan 100% mos keladi:

| № | Mavzu / Dars | To'g'ri Kalit | Pedagogik Izoh va To'g'ri Javobning Mazmuni |
|---|---|:---:|---|
| **1** | 01-dars: LLM va Sun'iy Intellekt | **C** | LLM modellari promptdagi vazifalarni tushunib, HTML, CSS va JS kodlarini tezkor va aniq generatsiya qilib beradi. |
| **2** | 02-dars: Sifatli Prompt Tuzilishi | **C** | Eng sifatli natija: dastur nima qilishi, qaysi tilda yozilishi va qanday tugmalar bo'lishi aniq ko'rsatilgan promptdan olinadi. |
| **3** | 03-dars: SVG Vektor Grafikasi | **B** | SVG format piksellar emas, balki matematik vektor chiziqlardan iborat bo'lgani uchun qanchalik kattalashtirilsa ham xiralashmaydi. |
| **4** | 05-dars: Semantik HTML (`<main>` tegi) | **D** | `<main>` tegi sahifaning yagona, asosiy va markaziy mazmunini ifodalovchi rasmiy semantik teg hisoblanadi. |
| **5** | 07-dars: Flexbox va `justify-content` | **B** | CSS Flexbox da elementlarni asosiy gorizontal o'q bo'yicha markazlashtirish uchun `justify-content: center;` ishlatiladi. |
| **6** | 08-dars: addEventListener va Kliklar | **D** | Tugmaga bosish hodisasini tinglash uchun rasmiy sintaksis: `btn.addEventListener('click', () => { ... })`. |
| **7** | 09-dars: Kiber-Reaksiya va Reaksiya Vaqti | **C** | Millisoniyalarda o'lchanadigan reaksiya vaqti — ekran yashil rangga kirgan paytdan boshlab o'yinchi tugmani bosguncha o'tgan tezlikdir. |
| **8** | 10-dars: DevTools Konsoli | **B** | Brauzerda dasturdagi sintaktik va mantiqiy xatolar hamda `console.log` xabarlari DevTools Console (F12) oynasida ko'rinadi. |
| **9** | 11-dars: LocalStorage doimiyligi | **D** | LocalStorage doimiy brauzer xotirasi bo'lib, sahifa yangilanganda ham, brauzer yopilib qayta ochilganda ham ma'lumotlar o'chib ketmaydi. |
| **10** | 12-dars: Vercel Deploy va HTTPS | **D** | Vercel loyihani internetga bepul joylab, unga butun dunyo bo'ylab ochiladigan 24/7 xavfsiz HTTPS havola va QR kod beradi. |
| **11** | 13-dars: HTML5 Canvas | **A** | JavaScript yordamida 2D o'yin elementlari, qahramonlar va partikllar chiziladigan rasmiy HTML5 tegi — bu `<canvas>`. |
| **12** | 13-dars: `requestAnimationFrame` va 60 FPS | **A** | Soniyasiga 60 kadrli silliq Game Loop tsiklini monitor chastotasiga mos ravishda yurgizish uchun `requestAnimationFrame` ishlatiladi. |
| **13** | 14-dars: Massivga qo'shish (`push`) | **D** | JavaScript da massiv oxiriga yangi obyekt yoki dushmanni qo'shish uchun `enemies.push(newEnemy)` metodi qo'llaniladi. |
| **14** | 15-dars: O'yin Fizikasi va Gravitatsiya | **B** | Tortishish kuchi o'yin tsiklining har bir kadrida qahramonning vertikal tezligiga gravitatsiyani qo'shadi (`vy += gravity`). |
| **15** | 15-dars: To'qnashuv (Collision Detection) | **A** | Ikki to'rtburchak qahramon va to'siq bir-birining ustiga tushganini aniqlash jarayoni "Collision Detection" (AABB to'qnashuv) deb ataladi. |
| **16** | 17-dars: Web Audio API | **C** | Tashqi og'ir MP3 fayllarsiz, to'g'ridan-to'g'ri brauzerda tovush to'lqinlarini sintez qilish texnologiyasi — Web Audio API (`AudioContext`). |
| **17** | 18-dars: Kamera Skrollingi | **A** | Kamera skrollingi qahramon katta xarita bo'ylab yugurganida uni doim ekranning ko'rinadigan qismida saqlab turish uchun kerak. |
| **18** | 19-dars: Touch Hodisalari | **E** | Smartfon yoki planshet sensor ekraniga barmoq tekkan paytda `touchstart` hodisasi ishga tushadi. |
| **19** | 21-dars: FUT OVR Reytingi | **B** | FUT Card Studio da OVR — bu o'yinchining PAC, SHO, PAS, DRI, DEF va PHY ko'rsatkichlari asosida hisoblangan vaznli umumiy reytingdir. |
| **20** | 22-dars: FUT Kimyo Graflari | **E** | Bir xil klubdagi o'yinchilar o'rtasida yashil kimyo liniyasi bog'lanadi va o'yinchilarga qo'shimcha kimyo ballari (+1, +2, +3) beriladi. |
| **21** | 24-dars: FUT 5% Soliq va Iqtisodiyot | **D** | 5% EA savdo solig'i — virtual tangalarni "yoqib yuboruvchi" (Coin Sink) mexanizm bo'lib, bozorda giperinflyatsiyaning oldini oladi. |
| **22** | 25-dars: Target Jarvis va Ovoz | **C** | Brauzerda inson ovozini matnga o'giruvchi (Speech-to-Text) zamonaviy standart texnologiya — Web Speech API (`SpeechRecognition`). |
| **23** | 26-dars: Veb-kamera Harakat Detektori | **A** | Kiber-Ko'z loyihasida harakat videodagi ketma-ket kadrlar piksellarining o'zgarishini solishtirish (Frame Differencing) orqali aniqlanadi. |
| **24** | 27-dars: Biometrik Face ID | **E** | Zamonaviy Face ID insonning soch turmagi emas, 68 ta tayanch suyak nuqtalari (Landmarks), IPD masofasi va ko'z qisishi (EAR) ga tayanadi. |
| **25** | Xulosa: 7–8-sinf Dasturchi Ko'nikmasi | **E** | Haqiqiy Vibecoder — shunchaki AI ga prompt beruvchi emas, balki tizim arxitekturasini tushunuvchi, xatolarni tuzatuvchi va mustaqil dastur quruvchi muhandisdir. |

---

## 4. Amaliy Topshiriqlarni Baholash Qo'llanmasi (Worksheet & Homework)

Har bir topshiriq 2.5 balldan baholanadi (Jami: 10 ball):

### 1-Topshiriq: Flexbox Maketini Markazlashtirish (2.5 ball)
* **Kutilayotgan javob:**
  ```css
  .arena {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    gap: 20px;
  }
  ```
* **Baholash mezonlari:**
  - `display: flex;` ko'rsatilgan — **1.0 ball**
  - `justify-content: center;` (gorizontal markaz) — **0.75 ball**
  - `align-items: center;` (vertikal markaz) — **0.75 ball**

### 2-Topshiriq: addEventListener va LocalStorage (2.5 ball)
* **Kutilayotgan javob:**
  ```javascript
  saveBtn.addEventListener('click', function() {
    localStorage.setItem('highScore', score);
    console.log('Rekord saqlandi:', score);
  });
  ```
* **Baholash mezonlari:**
  - `saveBtn.addEventListener('click', ...)` sintaksisi to'g'ri — **1.25 ball**
  - `localStorage.setItem('highScore', score)` kalit va qiymati to'g'ri — **1.25 ball**

### 3-Topshiriq: Canvas 60 FPS Game Loop va AABB To'qnashuv (2.5 ball)
* **Kutilayotgan javob:**
  1. `ctx.clearRect(0, 0, w, h)` har bir kadrda eski tasvir qoldiqlarini tozalash va animatsiya silliq ko'rinishi (orqadan qora iz cho'zilib ketmasligi) uchun shart.
  2. 60 FPS chastota bilan yangilash uchun `requestAnimationFrame(gameLoop)` funksiyasi chaqiriladi.
  3. AABB to'qnashuv sharti:
     `r1.x < r2.x + r2.w && r1.x + r1.w > r2.x && r1.y < r2.y + r2.h && r1.y + r1.h > r2.y`
* **Baholash mezonlari:**
  - `clearRect` sababi tushuntirilgan — **0.75 ball**
  - `requestAnimationFrame` ko'rsatilgan — **0.75 ball**
  - AABB to'qnashuv formulasi to'liq yozilgan — **1.0 ball**

### 4-Topshiriq: FUT Kimyo Graflari va Liveness EAR Formulasi (2.5 ball)
* **Kutilayotgan javob:**
  1. O'yinchilarning bir xil klubda bo'lishi ularning o'rtasida yashil kimyo bog'lanishini (graf qovurg'asi) hosil qiladi va kimyoga maksimal +3 ball qo'shadi (jamoada maksimal 33 ball).
  2. EAR formulasi: `EAR = (dVert1 + dVert2) / (2.0 * dHoriz)`. Tirik inson tabiiy ravishda ko'zini miltillatganda EAR qiymati 0.30 dan 0.15 ga tushib qayta ko'tariladi. Statik 2D fotosuratda esa bu nisbat doimiy qotib turgani sababli tizim soxtalikni (Photo Spoofing) darhol aniqlaydi.
* **Baholash mezonlari:**
  - FUT klub kimyosi va sinergiya tushuntirilgan — **1.25 ball**
  - EAR formulasi va fotosuratni fosh qilish mexanizmi aniq yozilgan — **1.25 ball**

---

## 5. O'quvchilarning Odatiy Xatoliklari va Remediation (Tuzatish)

1. **AABB To'qnashuv formulasida xatolik:**
   * *Xato:* O'quvchilar faqat `r1.x == r2.x` yoki bitta o'q bo'yicha tenglikni tekshirishadi.
   * *Tuzatish:* Doskada 2 ta to'rtburchak chizib, to'qnashuv yuz berishi uchun ikkala o'q (ham X, ham Y) bo'yicha oraliqlar bir vaqtda kesishishi kerakligini ko'rsating.
2. **`requestAnimationFrame` o'rniga `setInterval` deb o'ylash:**
   * *Xato:* Ko'p o'quvchilar `setInterval(loop, 16)` deb yozishadi.
   * *Tuzatish:* `setInterval` brauzer foni holatida ham batareyani sarflab ishlashini, `requestAnimationFrame` esa monitor kadrlariga sinxronlashib ekranga silliqlik (60 FPS) berishini ta'kidlang.
3. **LocalStorage ma'lumot turlari:**
   * *Xato:* `localStorage.getItem` faqat string qaytarishini unutib, uni darhol son kabi solishtirishadi.
   * *Tuzatish:* `parseInt(localStorage.getItem('highScore') || '0', 10)` orqali butun songa o'girish shartligini eslating.
4. **Imtihonda vaqtni boy berish:**
   * *Tavsiya:* Agar savol murakkab tuyulsa, unga to'xtab qolmasdan keyingi savolga o'tish, barcha oson savollarni birinchi 15 daqiqada yechib olish tavsiya etiladi.
