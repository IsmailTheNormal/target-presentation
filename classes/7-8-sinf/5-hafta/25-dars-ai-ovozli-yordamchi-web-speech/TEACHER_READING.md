# 25-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Briefing)

**Kohorta:** 7–8-Sinf · AI & Game Development  
**Mavzu:** Target Jarvis — AI Ovozli Yordamchi (Web Speech API, STT va TTS)  
**Ajratilgan vaqt:** 45 daqiqa  
**Amaliy natija:** Brauzerda ovozli buyruqlarni mikrofondan taniydigan, niyatni anglovchi (NLP), o'zi ovoz chiqarib javob qaytaruvchi va sahifani ovoz bilan boshqaruvchi shaxsiy AI yordamchi.

---

## 1. 5 Daqiqalik Darsoldi Konspekti (O'qituvchiga Eslatma)

Ushbu dars o'quvchilarda kompyuter bilan muloqot qilishning yangi bosqichi — **Voice User Interface (VUI)** dunyosini ochib beradi.
Ko'pchilik bolalar Siri yoki Alisani o'ta murakkab va faqat gigant korporatsiyalar qila oladigan sehr deb o'ylashadi.
Bugun ular o'z ko'zlari bilan ko'rishadi: **bor-yo'g'i 15-20 qator JavaScript kodi orqali brauzer ichida xuddi shunday ovozli yordamchi yaratish mumkin!**

### Darsning 3 ta asosiy ustuni:
1. **Speech-to-Text (`webkitSpeechRecognition`):** Mikrofondan kelgan ovoz to'lqinlarini ushlab, `onresult` hodisasi orqali toza matn (`transcript`) ga aylantirish.
2. **Intent Matching (Niyatni aniqlash):** `toLowerCase()` va `includes()` orqali gapirilgan gap ma'nosini chaqib, qaysi dasturiy buyruqni bajarishni belgilash.
3. **Text-to-Speech (`speechSynthesis`):** `SpeechSynthesisUtterance` orqali javob matnini insoniy nutqqa aylantirib, dinamikdan balandlik (`pitch`) va tezlik (`rate`) bilan eshittirish.

---

## 2. 45 Daqiqalik Dars Vaqt Xaritasi

| Vaqt | Bosqich | O'qituvchi amali | O'quvchi harakati |
|---|---|---|---|
| **00–05 daq** | Kirish & Demo | Proyektorda `studio/index.html` ni ochib, "Salom Jarvis, soat necha?" deb gapirish | Ovozli yordamchining jonli javobini eshitib hayratlanish |
| **05–15 daq** | Nazariya & Dvigatellar | 1–5 slaydlarni ko'rsatish: VUI nima, STT (quloq) va TTS (til) qanday ulanadi | Daftarga `onresult` va `SpeechSynthesis` sintaksisini yozish |
| **15–22 daq** | NLP va DOM Boshqaruvi | 6–8 slaydlar: "Mavzuni almashtir" va "Musiqa chal" buyruqlari bilan sahifani boshqarish | Varaqadagi 1-bet qiyosiy jadvalini to'ldirish |
| **22–26 daq** | Diagnostik Kod Testi | 10-slayd: `recognition.start()` xatosini tahlil qilish va fosh etish | Kod xatosini topib, varaqadagi 5-qismga to'g'ri kodni yozish |
| **26–40 daq** | Jonli Studiya Laboratoriyasi | Har bir o'quvchi o'z noutbukida studiyani ishga tushirishi | 5 ta ovozli buyruqni sinab, varaqadagi sinov jadvalini to'ldirish |
| **40–45 daq** | Yangi Buyruq & Baholash | O'quvchilar o'ylab topgan shaxsiy buyruqlarni tinglash, 10 ballik mezon | Varaqani baholashga topshirish |

---

## 3. O'quvchilar Eng Ko'p Yo'l Qo'yadigan 3 Ta Xato va Ularning Yechimi

### 1-Xato: Brauzerda mikrofon bloklanib qolishi
* **Muammo:** O'quvchi sahifa birinchi marta ochilganda tasodifan "Bloklash" (Block) tugmasini bosib yuboradi va keyin mikrofon ishlamaydi.
* **Yechim:** Brauzerning manzil satri (URL) chap tomonidagi qulf (yoki sozlamalar) belgisini bosing, "Mikrofon" ruxsatini "Ruxsat berilgan" (Allow) holatiga o'tkazing va sahifani `F5` bilan yangilang.

### 2-Xato: `recognition has already started` xatosi
* **Muammo:** O'quvchi mikrofon tugmasini ketma-ket bir necha marta bosganda dastur qotib qoladi.
* **Yechim:** Diagnostik testda ko'rsatilganidek, tugma bosilganda doimo `isListening` bayrog'i tekshirilishi kerak: agar faol bo'lsa, `recognition.stop()`, aks holda `recognition.start()` chaqiriladi.

### 3-Xato: Shovqinli sinfda so'zlarning noto'g'ri tanilishi
* **Muammo:** Sinfda bir vaqtda 15 ta o'quvchi gapirganda mikrofon atrofdagi shovqinni ilib olishi mumkin.
* **Yechim:** Studiyada matn maydoni (Fallback input) mavjud — o'quvchilar mikrofon bilan birga klaviaturada yozib ham barcha intentlarni 100% aniqlik bilan sinashlari mumkin.

---

## 4. Baholash Mezoni (10 Ballik Standart)

- **1–4 Ball (Baza):** Studiya ochildi, mikrofon ishga tushdi va aytilgan so'zlar ekranda matn ko'rinishida hosil bo'ldi.
- **5–7 Ball (Standart):** Jarvis ovoz chiqarib javob qaytardi, salomlashish, soat va mavzu almashtirish buyruqlari muvaffaqiyatli sinovdan o'tdi.
- **8–10 Ball (Senior):** O'quvchi o'zining yangi shaxsiy buyrug'ini (Custom Intent) JavaScript shartida yozdi, Web Audio musiqa bitini yoqdi va varaqadagi barcha 5 ta sinovni to'ldirib topshirdi.
