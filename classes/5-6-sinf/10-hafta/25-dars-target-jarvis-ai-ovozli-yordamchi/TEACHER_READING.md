# 25-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Briefing)

**Kohorta:** 5–6-Sinf · Junior Creators & Kiber-Gigiyena Track  
**Mavzu:** Target Jarvis — AI Ovozli Yordamchi (Voice AI, Web Speech API va Scratch Boshqaruvi)  
**Ajratilgan vaqt:** 80 daqiqa (Juftlik blok / Double Block)  
**Amaliy natija:** Brauzerda ovozli buyruqlarni mikrofondan taniydigan (STT), niyatni anglovchi (NLP), o'zi insondek ovoz chiqarib javob qaytaruvchi (TTS) va Scratch mushugini ovoz bilan sakratuvchi shaxsiy AI yordamchi.

---

## 1. 5 Daqiqalik Darsoldi Konspekti (O'qituvchiga Eslatma)

Ushbu dars 5–6-sinf o'quvchilarida kompyuter bilan muloqot qilishning eng zamonaviy bosqichi — **Voice User Interface (VUI)** dunyosini ochib beradi.
Ko'pchilik bolalar Siri, Alisa yoki Alexani o'ta murakkab va faqat gigant korporatsiyalar qila oladigan "sehr" deb o'ylashadi.
Bugun ular o'z ko'zlari bilan ko'rishadi: **JavaScript va Web Speech API yordamida o'zlarining shaxsiy Target Jarvisini yaratish mumkin!**

### Darsning 3 ta asosiy ustuni:
1. **Speech-to-Text (`webkitSpeechRecognition`):** Mikrofondan kelgan tovush to'lqinlarini ushlab, `onresult` hodisasi orqali matn (`transcript`) ko'rinishida chiqarish.
2. **Intent Matching (Niyatni aniqlash):** `.toLowerCase()` va `.includes()` orqali gapirilgan gap ma'nosini tahlil qilib, qaysi buyruqni bajarishni belgilash.
3. **Text-to-Speech (`speechSynthesis`):** `SpeechSynthesisUtterance` orqali javob matnini insoniy nutqqa aylantirib, dinamikdan balandlik (`pitch`) va tezlik (`rate`) bilan eshittirish.

---

## 2. 80 Daqiqalik Dars Vaqt Xaritasi (Double Block Roadmap)

### 1-Bosqich: Nazariya, Tushuncha va Jonli Demo (40 daqiqa)
| Vaqt | Bosqich | O'qituvchi amali | O'quvchi harakati |
|---|---|---|---|
| **00–04 daq** | Titul & Motivatsiya | Proyektorda 1-slaydni ochish, Jarvis nimaligini tushuntirish | Ekranga qarab hayratlanish, maqsadni tushunish |
| **04–10 daq** | O'tgan Dars Tahlili (HW Review) | 24-darsdagi Scratch X va Y koordinatalari xatosini ko'rsatish | X gorizontal, Y vertikal ekanligini qaytarish |
| **10–16 daq** | VUI Evolyutsiyasi | CLI (1980) ➔ GUI (1990) ➔ VUI (Bugun) bosqichlarini tushuntirish | Daftarga 3 ta bosqichni yozish |
| **16–22 daq** | 3 Dvigatel Arxitekturasi | Quloq (STT) ➔ Miya (NLP) ➔ Til (TTS) zanjirini doskaga chizish | Sxemani daftarga tushirish |
| **22–30 daq** | Jonli Jarvis Simulyatori | 5-slaydda Smartboardda tugmalarni bosib, mushukni sakratish va gapirtirish | Smartboardga chiqib buyruqlarni bosish |
| **30–40 daq** | Dvigatellar Sintaksisi & Quiz | 6–8 slaydlar: `rec.start()`, `includes()`, `speechSynthesis` va 10-slayddagi kiber-test | Kiber-quiz javobini belgilash |

### 2-Bosqich: Katta Amaliy Laboratoriya (40 daqiqa)
| Vaqt | Bosqich | O'qituvchi amali | O'quvchi harakati |
|---|---|---|---|
| **40–65 daq (25 min)** | Katta Amaliy Arena | Har bir o'quvchi noutbukida `studio/index.html` ni ochish, 25 daqiqalik taymerni yoqish | 5 ta buyruqni sinash, yangi shaxsiy buyruq qo'shish |
| **65–72 daq (7 min)** | Juftlikda Sinov (Peer Review) | Partadoshlar bilan joy almashib, bir-birining Jarvisini mikrofonda sinash | Bir-birining yangi buyruqlarini sinovdan o'tkazish |
| **72–76 daq (4 min)** | Xatolar Tahlili (Bug Hunter) | `recognition already started` xatosi va mikrofon ruxsatini tushuntirish | Daftarga `isListening` himoyasini qayd etish |
| **76–80 daq (4 min)** | Baholash va Uy Vazifasi | 10 ballik mezon bo'yicha baholash, `vazifa.html` topshirig'ini tushuntirish | Ish varaqalarini topshirish |

---

## 3. O'quvchilar Eng Ko'p Yo'l Qo'yadigan 3 Ta Xato va Ularning Yechimi

### 1-Xato: Brauzerda mikrofon bloklanib qolishi (Permission Denied)
* **Muammo:** O'quvchi sahifa birinchi marta ochilganda tasodifan "Bloklash" (Block) tugmasini bosib yuboradi.
* **Yechim:** URL satrining chap tomonidagi qulf belgisini bosing, "Mikrofon" ruxsatini "Ruxsat berilgan" (Allow) qilib, `F5` bilan yangilang.

### 2-Xato: `recognition has already started` xatosi
* **Muammo:** O'quvchi mikrofon tugmasini ketma-ket bir necha marta tez-tez bosganda dastur qotib qoladi.
* **Yechim:** Tugma bosilganda doimo `isListening` bayrog'i tekshirilishi kerak: agar faol bo'lsa, `recognition.stop()`, aks holda `recognition.start()` chaqiriladi.

### 3-Xato: Shovqinli sinfda so'zlarning xato tanilishi
* **Muammo:** Sinfda 15 ta o'quvchi baravar gapirganda mikrofon atrofdagi tovushlarni ilib olishi mumkin.
* **Yechim:** Studiyada tayyor sensorli tugmalar (Touch Presets) va klaviatura maydoni mavjud — o'quvchilar shovqin bo'lganda ham barcha funksiyalarni 100% aniqlik bilan sinay oladilar.

---

## 4. Baholash Mezoni (10 Ballik Standart)

- **1–4 Ball (Baza):** Studiya ochildi, mikrofon ishga tushdi va aytilgan so'zlar ekranda matn ko'rinishida hosil bo'ldi.
- **5–7 Ball (Standart):** Jarvis ovoz chiqarib javob qaytardi, salomlashish, soat, mushuk sakrashi va mavzu almashtirish buyruqlari muvaffaqiyatli sinovdan o'tdi.
- **8–10 Ball (Junior Creator):** O'quvchi o'zining yangi 2 ta shaxsiy buyrug'ini (Custom Intents) kiritdi, Jarvis ovozi balandligini (`pitch`) robotga moslab sozlay oldi va varaqadagi barcha 5 ta sinovni to'ldirib topshirdi.
