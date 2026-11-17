# 29-dars: Avtonom Kod Yozuvchi Agentlar: Coder, Critic va TDD Tsikli (O'qituvchi Metodologiyasi)

## Darsning Pasporti
- **Sinf:** 10–11-sinf (Senior AI & Enterprise Architecture Track)
- **Davomiyligi:** 80 daqiqa (Juftlik Dars / Double Block)
- **Asosiy maqsad:** O'quvchilarga LLM ko'r-ko'rona kod yozishidan Test-Driven Development (TDD) asosidagi avtonom o'z-o'zini tuzatuvchi tizimlarga o'tishni o'rgatish. Coder (kod generatsiyasi), Sandbox Runner (xavfsiz test bajarilishi) va Critic (traceback tahlili va nuqtali diff tuzatish) arxitekturasini kodlash.

---

## 80 Daqiqalik Aniq Vaqt Taqsimoti (Pacing)

### 1-Qism: Nazariya, Xatolar Tahlili va Jonli Test (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Motivatsiya | 1 | TDD va avtonom kod agentlari nima uchun enterprise standart ekanini tushuntirish. | Diqqat bilan tinglaydilar va dars maqsadini belgilaydilar. |
| **04:00–12:00** | 28-dars HW Tahlili | 2 | Supervisor agentida FINISH sharti bo'lmaganda cheksiz token sarflanishi xatosini tahlil qilish. | Blitz savolga javob beradilar, loop guard qoidasini yozib oladilar. |
| **12:00–18:00** | One-Shot Muammosi | 3 | Nega bitta prompt bilan olingan kod productionda yiqilishini ko'rsatish (AST va runtime yo'qligi). | Real arxitektura kamchiliklarini tushunadilar. |
| **18:00–24:00** | TDD Paradigmasi | 4 | RED ➔ GREEN ➔ REFACTOR zanjirini tushuntirish. Nega testlar koddan oldin yozilishini asoslash. | PyTest sintaksisini eslab qoladilar. |
| **24:00–30:00** | Coder Arxitekturasi | 5 | Coder tizimli prompti, Type Hints va toza funksiyalar talabini tushuntirish. | Coder cheklovlarini ko'rib chiqadilar. |
| **30:00–35:00** | Sandbox Runner | 6 | Xavfsiz subprocess, exit code 0/1 va 3.0s timeout mexanizmini ko'rsatish. | Host xavfsizligi nega muhimligini anglaydilar. |
| **35:00–40:00** | Critic va Refleksiya | 7 | Tracebackdan Root Cause topish va nuqtali diff generatsiyasini o'rgatish. | Qayta noldan yozmaslik tamoyilini o'rganadilar. |

### 2-Qism: Smartboard Sinovi, Katta Arena va Showcase (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **40:00–48:00** | Smartboard Simulyatori | 8 | Slayddagi Coder-Runner-Critic tsiklini doskada ishga tushirish (Fibonacci / Rate Limiter). | 1-urinishda yiqilish, Critic tahlili va yashil bo'lishni kuzatadilar. |
| **48:00–55:00** | Viktorina (Quiz) | 9 | 3 ta nazorat savoli bo'yicha viktorina o'tkazish. | Faol javob beradilar va o'z bilimlarini tekshiradilar. |
| **55:00–70:00** | 25 Daqiqalik Arena | 10 | 25:00 taymerni yoqish, partalar bo'ylab yurib ko'maklashish. | simulator/index.html da o'z Coder-Critic agentlarini dasturlaydilar. |
| **70:00–74:00** | Partadosh Auditi | 11 | O'rin almashishni e'lon qilish, 4 mezonli sinovni nazorat qilish. | Bir-birining tizimiga cheksiz sikl berib, timeoutni tekshiradilar. |
| **74:00–77:00** | Katta Ekran Showcasi | 12 | Eng zo'r avtonom agentni katta doskaga chiqarib jonli test qilish. | Sinfdoshlari natijasini tahlil qiladilar. |
| **77:00–80:00** | Uy Vazifasi va Yakun | 13–14 | 10 ballik uy vazifasini tushuntirish va Playwright veb-agentlariga ko'prik! | Kundaliklariga vazifani belgilaydilar. |

---

## O'qituvchi Uchun Muhim Blitz Savollari
1. **"Nega test yiqilganda Coderga butun kodni noldan qayta yozdirish xavfli?"**
   - Javob: Chunki model ilgari muvaffaqiyatli o'tgan boshqa testlarni buzib qo'yishi (regression) va yana yangi gallyutsinatsiyalar kiritishi mumkin. Critic faqat xato qatorni nuqtali tuzatishi shart.
2. **"Sandboxda subprocess nima uchun timeout bilan o'ralishi kerak?"**
   - Javob: Agar model xatoni tuzatish paytida `while True` yoki qotuvchi rekursiya kiritib qo'ysa, server abadiy muzlab qolmasligi uchun SIGKILL beriladi.

---

## 10 Ballik Baholash Rubrikasi
- **4 Ball (Baza):** Coder Type Hints bilan toza Python kodini generatsiya qiladi.
- **4 Ball (Amaliy):** Sandbox Runner xavfsiz muhitda testlarni bajaradi va stderr tracebackni ajratadi.
- **2 Ball (Challenge):** Critic xatoni aniqlab, 2-urinishda inson aralashuvisiz kodni 100% yashil testlarga yetkazadi!
