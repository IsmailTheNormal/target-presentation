# 27-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Prep Guide)
**Target International School // 7–8-Sinflar (12–14 yosh) // 7-Hafta (1-Soat: 40 daqiqa)**
**Mavzu:** Biometrik Kiber-Skaner: Yuz, Biometrika va Liveness Anti-Spoofing (Face ID Qanday Ishlaydi?)
**Kohorta:** `7A 7B 8A 8B` (Kiber-Xavfsizlik, Kompyuter Ko'rishi va Biometrik Autentifikatsiya)

> **ASOSIY PEDAGOGIK MAQSAD:**
> Ushbu darsda 7–8-sinf o'quvchilari har kuni smartfonlarini ochishda ishlatadigan Face ID va biometrik skanerlarning ichki muhandislik mexanizmini kashf etadilar. Ular yuz qanday qilib 68 ta tayanch nuqta (Landmarks) va 128 o'lchamli raqamli vektorga (Biometric Embedding) aylantirilishini, nega oddiy fotosurat yordamida Face ID ni aldab bo'lmasligini va kiber-xavfsizlikda eng muhim bo'lgan "Liveness Detection" (Tiriklikni tekshirish — ko'z miltillashi, bosh harakati va 3D chuqurlik tahlili) qanday ishlashini o'rganadilar. Dars yakunida har bir o'quvchi shaxsiy "Junior Biometrics Security Analyst" sertifikatiga ega bo'ladi.

---

## 1. Darsda Ishlatiladigan Fayllar va Vositalar

1. **Interaktiv Studiya (Target Cyber-BioScanner):**
   * Fayl manzili: `classes/7-8-sinf/7-hafta/27-dars-biometrik-kiber-skaner-yuz-va-anti-spoofing/studio/index.html`
   * Internet talab etilmaydi — to'liq lokal oflayn ishlaydi.
   * Studiya modullari:
     - **Webcam / 3D Synthetic Simulation:** Haqiqiy kamera bo'lsa jonli video, kamera bo'lmasa 3D sintetik kiber-yuz simulyatsiyasi.
     - **Cyber-HUD Face Mesh:** 68 ta biometrik nuqta, ko'zlararo masofa (IPD), yuz burchagi (Yaw/Pitch/Roll) telemetriyasi.
     - **Anti-Spoofing Liveness Engine:** 3 ta tiriklik testi — Blink (ko'z qisish), Head Turn (boshni burish) va Challenge-Response.
     - **Attack Simulator:** "2D Photo Spoofing Attack" tugmasi orqali statik surat bilan aldashga urinish va tizimning qizil rad javobi (`SPOOFING DETECTED! 2D Photo Rejected`).
     - **Export & Sertifikat:** `biometrics_audit.json` hisoboti va chop etiladigan "Junior Biometrics Security Analyst" Diplomi.
2. **Minimalist Tipografik Prezentatsiya (12 Slayd):**
   * Fayl: `prezentatsiya.html` — Face ID tarixi, Biometrik embeddinglar, 2D Photo Spoofing vs Liveness, Apple TrueDepth 3D to'ri, Jonli test va 10 ballik mezon.
   * Boshqaruv: `→` keyingi, `←` oldingi, `N` o'qituvchi izohlari, `L` til (UZ/RU/EN), `T` mavzu, `H` panelni yashirish.
3. **Chop Etiladigan Ishchi Varaqa (2 Betlik A4):**
   * Fayl: `varaqa.html` — Biometrik nuqtalar tahlili, Liveness 3 usuli, Photo Spoofing hisobi, BioScanner laboratoriyasi va 10 ballik baholash rubrikasi.
4. **Mustaqil Interaktiv Vazifa:**
   * Fayl: `vazifa.html` — 4 ta kiber-muhandislik topshirig'i, LocalStorage avto-saqlash va testlash.
5. **Onlayn Oraliq Kiber-Test:**
   * Fayl: `test.html` — Avtomatik baholovchi 4 ta tahliliy kiber-savol.

---

## 2. 40 Daqiqalik Darsning Slaydma-Slayd Aniq Vaqt Taqsimoti (Pacing Clock)

| Vaqt | Bosqich & Slayd | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 02:00** (2 daq) | **Slayd 1: Kirish & Reja** | "Smartfoningiz sizni qorong'ida ham qanday taniydi? Nega do'stingiz sizning suratingizni ko'rsatsa telefon ochilmaydi?" deb savol berish. | Hayron bo'lishadi, o'z taxminlarini aytishadi (kamera, infraqizil, ko'z qorachig'i). |
| **02:00 – 05:00** (3 daq) | **Slayd 2: Parol vs Biometrika** | Parol o'g'irlansa almashtirish mumkin, lekin barmoq izi yoki yuz sizib chiqsa uni almashtirib bo'lmaydi! Biometrika mas'uliyatini tushuntirish. | Varaqaning 1-kvestidagi taqqoslash jadvalini ko'rib chiqishadi. |
| **05:00 – 08:00** (3 daq) | **Slayd 3: Yuz Qanday Raqamga Aylanadi?** | 68 ta tayanch nuqta (Landmarks) va 128/512 o'lchamli vektor (Face Embedding) tushunchasini ko'rsatish. | Varaqaga yuz nuqtalari va ko'zlararo masofa hisobini yozadilar. |
| **08:00 – 11:00** (3 daq) | **Slayd 4: Kiber-Hujum: Yuzni Soxtalashtirish (Spoofing)** | 2D qog'oz surat, planshetdagi video (Replay Attack) va 3D silikon niqoblar bilan Face ID ni buzishga urinishlar tarixi. | Xakerlik usullarini tahlil qilishadi. |
| **11:00 – 14:00** (3 daq) | **Slayd 5: Liveness Detection (Tiriklik Testi)** | Passiv (tekstura, qon tomirlar mikropulsi) va Aktiv (ko'z miltillatish, boshni burish) liveness algoritmlarini tushuntirish. | Varaqadagi 2-kvest (Liveness 3 usuli)ni to'ldirishadi. |
| **14:00 – 16:00** (2 daq) | **Slayd 6: 3D TrueDepth va Infraqizil To'r** | Apple Face ID ning 30 000 ta ko'rinmas infraqizil nuqtasi va 3D chuqurlik xaritasi (Depth Map) qanday ishlashi. | 2D rasm bilan 3D yuz o'rtasidagi geometrik farqni anglashadi. |
| **16:00 – 19:00** (3 daq) | **Slayd 7: BioScanner Studio Demo** | O'qituvchi ekranda `studio/index.html` ni ochadi: kamera / 3D simulyatsiyani yoqadi, "Photo Spoofing" hujumini sinab qizil xatoni ko'rsatadi, so'ngra "Blink" qilib yashil ruxsat oladi. | Kiberpank HUD va liveness mexanikasini ko'rishadi. |
| **19:00 – 22:00** (3 daq) | **Slayd 8: Jonli Kiber-Test va Fix** | Slayddagi test savolini birgalikda yechish: "Xaker foydalanuvchining yuqori sifatli fotosuratini kameraga tutdi. Qaysi algoritm hujumni qaytaradi?" | Test variantini tanlab, "Fix" tugmasi bilan yechimni tekshiradilar. |
| **22:00 – 33:00** (11 daq) | **Slayd 9: Mustaqil Amaliyot (Route Studio)** | O'quvchilar kompyuterlarida `studio/index.html` ni ochib, 4 ta kvestni bajarishadi: mesh to'rini faollashtirish, spoofing hujumini qaytarish, liveness testidan o'tish va sertifikat olish. | Kameralar oldida ko'z qisishadi, boshlarini burishadi, audit hisobotini yuklab olishadi. |
| **33:00 – 36:00** (3 daq) | **Slayd 10: 10 Ballik Baholash Mezoni** | 10 ballik rubrika asosida varaqalarni tekshirish va o'quvchilar ishini baholash. | Varaqadagi ballarini hisoblab, yakuniy xulosa yozadilar. |
| **36:00 – 40:00** (4 daq) | **Slayd 11–12: Yakun, Sertifikatlar va Vazifa** | "Junior Biometrics Security Analyst" diplomlarini topshirish, xulosalarni mustahkamlash va vazifa.html uy topshirig'ini tushuntirish. | Varaqalarni topshirib, darsni a'lo kayfiyatda yakunlaydilar. |

---

## 3. O'qituvchi Uchun Jonli Muloqot Ssenariysi

### Darsni Boshlashdagi "Ilmoq" (Hook):
* **UZ:** "Tasavvur qiling: do'stingiz siz uxlab yotganingizda yoki suratingizni ushlab telefoningizga tutsa, Face ID ochiladimi? Birinchi avlod Android telefonlarida ochilardi! Chunki ular oddiy 2D surat bilan haqiqiy insonni farqlay olmasdi. Lekin zamonaviy Apple Face ID va kiber-skanerlar nega qog'ozdagi rasmga aldanmaydi? Qanday qilib kompyuter ko'zingiz qisilganini, yuzingiz tirik ekanini va qoningiz tomirlarda urayotganini taniy oladi? Bugun biz shaxsiy Biometrik Kiber-Skanerimizni quramiz va xakerlarning soxta surat hujumlarini (Spoofing) chilparchin qilamiz!"
* **RU:** "Представьте: если распечатать четкое фото человека на глянцевой бумаге и поднести к камере смартфона — сработает ли Face ID? Первые смартфоны попадались на эту уловку! Они не умели отличать плоское фото от живого человека. Но как современный Face ID за миллисекунды понимает, что перед ним не бумажка, а живое дышащее лицо? В чем секрет алгоритмов Liveness Detection? Сегодня мы запустим собственную биометрическую лабораторию и защитим Face ID от атак с поддельными фото!"

---

## 4. O'quvchilarda Uchraydigan Savollar va Ilmiy Javoblar

1. **"Nega Face ID qorong'ida ham yuzni taniy oladi?"**
   * *Javob:* Face ID oddiy xona chirog'iga qaramaydi. Uning tepasida ko'zga ko'rinmas infraqizil projektor (Flood Illuminator) va nuqtalar projektori (Dot Projector) bor. Ular yuzingizga 30 000 dan ortiq infraqizil nurlarni sochadi va infraqizil kamera orqali qop-qorong'i xonada ham mukammal 3D xarita oladi.
2. **"Deepfake videoni kameraga ko'rsatsa ochiladimi?"**
   * *Javob:* Oddiy veb-kameralarda bu xavfli (Video Replay Attack). Lekin ilg'or tizimlar buni ham fosh qiladi: planshet ekranining yaltirashi (screen glare), ekrandagi piksellar panjarasi (moiré effekti) va 3D chuqurlikning yo'qligi sababli Liveness filtrlari bunday urinishni zudlik bilan bloklaydi.
3. **"Egizaklar bir-birining telefonini ocha oladimi?"**
   * *Javob:* Bir tuxumli egizaklar (identical twins) yuz geometriyasi 99.9% bir xil bo'lgani sababli, ehtimollik biroz yuqoriroq (1:50,000 o'rniga 1:1,000). Aynan shu sababli bank ilovalarida faqat yuz bilan cheklanmasdan, qo'shimcha PIN-kod yoki 2FA talab qilinadi.

---

## 5. Baholash Mezoni (10 Ballik Standart)

1. **Biometrik Landmarklar va Embeddinglar (2 ball):** Yuz nuqtalari (68 ta) va vektorlar masofasini to'g'ri tushunish.
2. **Spoofing Hujumlari Turlari (2 ball):** 2D Photo, Replay video va 3D maskalar farqini asoslash.
3. **Liveness Detection Usullari (2 ball):** Ko'z qisish (Blink), Bosh burish (Head turn) va Challenge-Response tamoyilini yoritish.
4. **Anti-Spoofing Keysi Tahlili (2 ball):** Xakerning hujumini qaysi texnologiya qaytarganini to'g'ri tahlil qilish.
5. **BioScanner Studio Amaliyoti & Sertifikat (2 ball):** Studiyada 4 ta kiber-kvestni bajarish, `biometrics_audit.json` eksporti va 10 ball bilan diplomni himoya qilish.
