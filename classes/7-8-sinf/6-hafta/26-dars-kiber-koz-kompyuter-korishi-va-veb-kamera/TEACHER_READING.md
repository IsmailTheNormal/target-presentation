# O'qituvchi Uchun Tezkor Qo'llanma (Teacher Briefing)
## 26-dars: Kiber-Ko'z — Kompyuter Ko'rishi va Veb-kamera Harakat Detektori

---

### 🎯 Darsning Asosiy Maqsadi va Falsafasi
Bugungi darsda 7–8-sinf o'quvchilari klaviatura va sichqonchadan xalos bo'lib, **Kompyuter Ko'rishi (Computer Vision)** olamiga qadam qo'yadilar. Ular noutbuk kamerasidagi video oqimini Canvasda tahlil qilishni, har bir pikselning RGBA baytlarini xotiradan o'qishni va **Frame Differencing (Kadrlar Farqi)** matematik algoritmi yordamida havoda qo'l silkitib o'yinlarni boshqarishni o'rganadilar.

> [!IMPORTANT]
> **Hech qanday og'ir sun'iy intellekt kutubxonalarisiz (TensorFlow/OpenCV'siz)!** Algoritm 100% sof JavaScript va Canvas API yordamida mahalliy (offline) ishlaydi. Bu o'quvchilarga kompyuter ko'rishi ortida qanday matematika yotganini kristaldek tiniq tushunishga yordam beradi.

---

### ⏱️ 45 Daqiqalik Dars Xaritasi

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchi Natijasi |
|---|---|---|---|
| **00–05 min** | **Kirish va Namoyish** | Proyektorda `studio/index.html` ni oching, kamerani yoqing va havoda qo'lingizni ko'rsatib, piksellar yashil nurlanishini ko'rsating. | O'quvchilarda yuqori qiziqish paydo bo'ladi. |
| **05–15 min** | **Nazariya & Matematika** | Video nima? 30 FPS, RGBA 4 baytli tuzilma, Frame Differencing formulasi ($Diff = \|R_2-R_1\| + \|G_2-G_1\| + \|B_2-B_1\|$) va Threshold tushuntiriladi. | Piksellar massivi va kadrlar ayirmasi formulasini tushunishadi. |
| **15–22 min** | **Havo Zonalari & O'yin** | 640px enidagi Canvas qanday qilib Zone A, B, C ga bo'linishi va Air Bubble Pop o'yini mexanikasi tushuntiriladi. | Virtual sensorlar qanday ishlashini o'rganishadi. |
| **22–25 min** | **Diagnostik Test** | Slayd 8 dagi tsikl xatosini (stride `i += 4`) sinfda birgalikda muhokama qilish va "Fix" tugmasini bosib tekshirish. | Odatiy xatolarni tahlil qilishadi. |
| **25–40 min** | **Amaliy Ish (Laboratoriya)** | O'quvchilar o'z noutbuklarida `studio/index.html` ni ochadilar, 4 ta kiber-missiyani bajaradilar va varaqadagi 5 ta test jurnali qatorini to'ldiradilar. | Havoda qo'l bilan 50+ ball to'plashadi va o'lchovlarni yozishadi. |
| **40–45 min** | **Baholash va Xulosa** | 10 ballik mezon asosida o'quvchilar ishini baholash va varaqalarni qabul qilish. | O'lchanadigan 10 ballik baho. |

---

### ⚠️ O'quvchilar Yo'l Qo'yadigan 3 Ta Odatiy Xato va Ularning Yechimi

#### 1. Veb-kameraga Ruxsat Berilmasligi (Qora Ekran / NotAllowedError)
- **Muammo:** O'quvchi xato qilib brauzer so'raganda "Block" tugmasini bosib yuboradi yoki noutbukning xavfsizlik dasturi kamerani bloklaydi.
- **Yechim:** Brauzer manzil satrining chap tomonidagi qulf (padlock) belgisini bosing &rarr; "Camera" sozlamasini "Allow" ga o'tkazing &rarr; sahifani yangilang (`Ctrl + R`). Agar kamerasi umuman yo'q bo'lsa, studiyadagi **"Test Simulyatsiyasi"** tugmasidan foydalanishni ayting.

#### 2. Tsikl Qadamida `i++` Deb Yozish (Performance Drop / 2 FPS)
- **Muammo:** O'quvchilar odatdagi tsikllarga o'rganib qolgani uchun `for (var i = 0; i < data.length; i++)` deb yozishadi.
- **Yechim:** 1 ta piksel 4 ta baytdan iborat: `[R, G, B, A]`. Shuning uchun tsikl har doim `i += 4` qadami bilan yurishi shart. Aks holda har bir kanal aralashib ketadi va dastur 4 barobar sekinlashadi.

#### 3. Ko'zgu Effekti (Mirror Flip) Chalkashligi
- **Muammo:** O'quvchi qo'lini o'ng tomonga ko'tarsa, oddiy videoda u chap tomonda ko'rinadi.
- **Yechim:** Canvasga `transform: scaleX(-1)` ko'zgu effekti beriladi. Shunda foydalanuvchi xuddi oynaga qarab turgandek tabiiy harakat qiladi.

---

### 📝 Diagnostik Test Javoblar Kaliti (Slayd 8)
- **Savol:** Nima uchun kadrlar tahlili tsiklida video qotib qolmoqda?
- **To'g'ri javob:** **B) Tsikl qadami `i += 4` bo'lishi kerak, chunki 1 piksel 4 baytdan iborat (RGBA)!**
- **Izoh:** `i++` qadami baytlarni aralashtirib, keraksiz hisoblashlarni ko'paytiradi.

---

### 💯 10 Ballik Baholash Mezoni
1. **3 ball:** Veb-kamerani yoqish va video oqimini 30 FPS da barqaror chiqarish.
2. **3 ball:** Frame Differencing orqali harakat zonalarini (Zone A, B, C) faollashtirish.
3. **2 ball:** Air Bubble Pop o'yinida havoda qo'l silkitib kamida 50 ball to'plash.
4. **2 ball:** Amaliy ish varaqasidagi 5 ta sinov jurnali qatorini to'liq to'ldirish.
