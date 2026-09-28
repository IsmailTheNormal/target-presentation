# 13-Dars: O'qituvchi Uchun Tayyorgarlik Qo'llanmasi (Teacher Prep Guide)
**Target International School // 10–11-Sinflar (Senior Engineering) // 3-Hafta (1-Soat)**
**Mavzu:** LLM Ichki Mexanikasi: Kontekst Oynasi, System Prompt, Sampling va Few-Shot Muhandisligi

> **ESLATMA:** 10–11-sinf o'quvchilari uchun darslar yuqori akademik va professional muhandislik darajasida o'tiladi. "AI bilan gaplashish" emas, balki real IT korporatsiyalarida qo'llaniladigan arxitektura printsiplari (BPE tokenizatsiya, Temperature, Top-P, JSON Schema va Prompt Injection) o'rgatiladi.

---

## 1. Darsda Qaysi Dasturiy Vositalar Ishlatiladi?

1. **O'quvchi Laboratoriya Stendi (Brauzer):**
   * Fayl: `classes/10-11-sinf/3-hafta/13-dars-llm-arxitekturasi-va-prompt-muhandisligi/lab/index.html`
   * Internet yoki qimmat pullik API kaliti kerak emas! Stendda real Transformer inference simulyatsiyasi o'rnatilgan.
   * Unda:
     - `System Prompt` (Model Konstitutsiyasi)
     - `User Prompt` (Mijozning so'rovi)
     - `Temperature` slayderi (0.0 dan 1.5 gacha)
     - `Top-P` slayderi (0.1 dan 1.0 gacha)
     - Jonli telemetriya: Latency (ms), Prompt Tokens, Completion Tokens, Hisoblangan narx ($).
     - JSON Schema validatori va Prompt Injection hujumini sinovchi maxsus tugma.
2. **Katta Til Modellari (Ixtiyoriy qo'shimcha):**
   * Agar noutbuklarda internet bo'lsa: `chatgpt.com` yoki `claude.ai` yoki VS Code da o'rnatilgan AI yordamchi.

---

## 2. Asosiy Texnik Konsepsiyalarning Qisqa va Oddiy Mazmuni

* **BPE Tokenizatsiya:** Model harflar yoki so'zlar bilan emas, sonli tokenlar bilan ishlaydi. Ingliz tilida 1 so'z ≈ 1.3 token bo'lsa, o'zbek va rus tillarida (kirill/lotin bayt zichligi sababli) 1 ta so'z 3–5 token sarflaydi. Shuning uchun token byudjetini hisoblash juda muhim.
* **Kontekst Oynasi (Context Window):** Modelning bir martalik tezkor e'tibor xotirasi. Kontekst to'lib borsa, eski ma'lumotlar o'chib ketadi. "Lost in the Middle" hodisasiga ko'ra, model hujjat o'rtasidagi ma'lumotlarni chetdagilarga qaraganda tezroq unutadi.
* **System Prompt:** Modelning "Konstitutsiyasi". U oddiy User so'rovidan ustun turadi va xavfsizlik cheklovlari hamda qat'iy javob formatini (masalan, faqat JSON) belgilaydi.
* **Temperature (0.0 – 1.5):** Keyingi tokenni tanlashdagi ehtimollik taqsimoti.
  - $T = 0.0$ (Greedy Decoding) — har doim eng yuqori ehtimolli tokenni tanlaydi. Kod, JSON va hisob-kitoblar uchun shart!
  - $T = 1.2+$ — yuqori xaos va kreativlik.
* **Few-Shot Prompting:** Modelga quruq tushuntirish berish o'rniga 2–3 ta aniq Kirish $\rightarrow$ Chiqish namunasini ko'rsatish. Attention mexanizmi namunalarga qarab bir zumda kerakli qolipga tushadi.

---

## 3. 40 Daqiqalik Dars Ssenariysi

### 00:00 – 05:00 | Kirish va Muammoni Qo'yish
* **Slayd:** 1–2-slaydlar (`prezentatsiya.html`).
* **O'qituvchi nima deydi (rus tilida):**
  > *"Коллеги-инженеры, добрый день! Забудьте наивные ролики с YouTube в духе «Напиши секретный промпт и стань миллионером». В реальных IT-проектах такие промпты ломаются в первую же секунду, потому что модель выдает лишний текст вместо чистого JSON, и сервер падает с ошибкой. Сегодня мы разберем, как LLM устроена изнутри: математику токенов, контекстное окно, вероятностный сэмплинг и защиту системного промпта от взлома!"*

### 05:00 – 18:00 | Nazariya: Tokenlar, Kontekst va Sampling
* **BPE va Tokenlar (3-slayd):** Nega kirill alifbosi va o'zbek tili 3 barobar ko'proq token sarflashini ko'rsating.
* **Lost in the Middle (4-slayd):** Eng muhim qoidalar doim System Promptda — boshida va oxirida bo'lishi shart.
* **Temperature va Top-P (6-slayd):** Doskaga grafik chizib ko'rsating: $T=0$ da faqat 1 ta cho'qqi (eng ehtimolli so'z), $T=1.5$ da esa barcha so'zlar ehtimolligi tenglashib ketadi (xaos).
* **Few-Shot kuchi (7-slayd):** Zero-shot va Few-shot o'rtasidagi farqni namunalar bilan tushuntiring.

### 18:00 – 33:00 | Amaliy Laboratoriya (`lab/index.html`)
* O'quvchilar noutbuklarida `lab/index.html` ni ochishadi va qog'oz varaqani to'ldirishadi:
  1. **1-mashq:** Temperature = 0.0 va Temperature = 1.5 da bir xil so'rovni yuborib, JSON formatining buzilishini o'z ko'zlari bilan ko'rishadi.
  2. **2-mashq:** "Fintech API" andozasini tanlab, toza JSON chiqishini tekshirishadi.
  3. **3-mashq:** "⚠️ Симуляция Prompt Injection Атаки" tugmasini bosib, System Prompt xakerlik hujumini to'xtatganini audit qilishadi.
  4. **4-mashq:** O'z natijalaridagi Latency (ms), Tokens va Cost ($) qiymatlarini ish varaqasiga yozishadi.

### 33:00 – 40:00 | Tahlil va 10 Ballik Baholash
* O'quvchilar bilan Prompt Injection himoyasi natijalarini muhokama qilish va varaqalarga baho qo'yish:
  - Tokenlar va kontekst tushunilgan: 3 ball
  - Temperature va Top-P laboratoriyasi: 3 ball
  - Fintech System Prompt & JSON: 4 ball
  - Prompt Injection himoyasi: +2 rag'bat ball!

---

## 4. O'quvchilar Berishi Mumkin Bo'lgan Savollar va Javoblar

1. **"Nega kod yozishda Temperature = 0.7 qo'yib bo'lmaydi?"**  
   *Javob:* *"Chunki 0.7 haroratda model har safar har xil kod yoki sintaktik xatolar chiqarishi mumkin. Kod va API larda 100% qaytariluvchanlik (determinizm) talab qilinadi, shuning uchun faqat 0.0 ishlatiladi."*
2. **"Prompt Injection xavfi qayerdan keladi?"**  
   *Javob:* *"Model uchun System Prompt ham, User matni ham bitta kontekst oqimidagi tokenlardir. Agar System Promptda qat'iy cheklov bo'lmasa, foydalanuvchi buyrug'i tizim qoidalarini siqib chiqarishi mumkin."*
3. **"Nega JSON.parse() xatosi bunchalik xavfli?"**  
   *Javob:* *"Agar LLM javobiga bitta so'z yoki markdown belgisi qo'shilsa, backend server uni massivga yoki obyektga aylantira olmaydi va butun veb-xizmat 500 Internal Server Error bilan to'xtab qoladi."*
