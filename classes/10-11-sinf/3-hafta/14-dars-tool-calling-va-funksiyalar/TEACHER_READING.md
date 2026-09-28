# 14-Dars: O'qituvchi Uchun Tayyorgarlik Qo'llanmasi (Teacher Prep Guide)
**Target International School // 10–11-Sinflar (Senior Engineering) // 3-Hafta (2-Soat / Juft Dars)**
**Mavzu:** Tool Calling va Funksiyalarni Bajarish: Fikrlashdan Real Amallargacha (Function Calling, ReAct Loop, JSON Schema & MCP)

> **METODIK ESLATMA:** 13-darsda biz modelning ichki "miyasini" (tokenizatsiya, kontekst oynasi, sampling va System Prompt) o'rgandik. 14-dars — bu juft darsning mantiqiy cho'qqisi bo'lib, unda modelga "qo'llar beriladi". Oddiy chatbordan farqli o'laroq, real IT tizimlarida LLM faqat matn yozmaydi, balki tashqi API larni chaqiradi, ma'lumotlar bazasiga so'rov yuboradi va dasturlarni boshqaradi.

---

## 1. Darsda Qaysi Dasturiy Vositalar Ishlatiladi?

1. **O'quvchi Laboratoriya Stendi (Brauzer):**
   * Fayl: `classes/10-11-sinf/3-hafta/14-dars-tool-calling-va-funksiyalar/lab/index.html`
   * Internet yoki pullik OpenAI API kalitlari mutlaqo talab qilinmaydi! Stendda to'liq detallashtirilgan Function Calling Runtime simulyatori ishlaydi.
   * Stend imkoniyatlari:
     - 3 ta real asbob: `get_stock_price`, `convert_currency`, `execute_sql_query`.
     - JSON Schema spetsifikatsiyasi ko'rinishi (OpenAPI formati).
     - 3 bosqichli vizual ijro zanjiri (Step 1: Model Chaqiruvi JSON $\rightarrow$ Step 2: Runtime API Kuzatuvi $\rightarrow$ Step 3: Faktlarga tayangan Grounded Javob).
     - Telemetriya: Latency (ms), Ijro Qadamlari, Tokenlar va Xarajat ($).
     - Xavfsizlik stress-testi: Buzg'unchi `DROP TABLE users;` so'rovini bloklash mexanizmi.
     - RU / EN / UZ tillarini bir zumda almashtirish.
2. **Prezentatsiya:**
   * Fayl: `classes/10-11-sinf/3-hafta/14-dars-tool-calling-va-funksiyalar/prezentatsiya.html` (12 slayd, rus tili birlamchi, o'qituvchi izohlari `N` tugmasida).
3. **Chop etiladigan Ish Varaqasi:**
   * Fayl: `classes/10-11-sinf/3-hafta/14-dars-tool-calling-va-funksiyalar/varaqa.html` (1 varaq A4 format).

---

## 2. Asosiy Texnik Tushunchalarning Muhandislik Mohiyati

### A. Nega Yolg'iz LLM Tashqi Dunyoga Bog'lana Olmaydi?
Til modellari faqat matnli tokenlar ehtimolligini hisoblaydigan matritsadir.
1. **Knowledge Cutoff (Bilimlar chegarasi):** Model o'rganilgan vaqtdan keyingi yangiliklarni, bugungi valyuta kursini yoki ombordagi tovar sonini bilmaydi.
2. **Arifmetik noaniqlik:** LLM kalkulyator emas. U $4928.31 \times 1.15$ kabi amallarni hisoblamaydi, balki o'xshash raqamlar ketma-ketligini taxmin qiladi.
3. **Dunyoga ta'sir qila olmaslik:** Model operatsion tizim terminaliga to'g'ridan-to'g'ri ulana olmaydi.

### B. Tool Calling Oltin Qoidasi: Model Kodni O'zi Bajarmaydi!
Bu darsdagi eng muhim kontseptual tushuncha:
* Model **HECH QACHON** Python yoki SQL kodini o'zida bajarmaydi.
* Model faqat maxsus to'xtash belgisi (`finish_reason: "tool_calls"`) bilan qat'iy JSON parametrlarini generatsiya qiladi:
  `{"name": "convert_currency", "arguments": {"amount": 1500, "from": "USD", "to": "UZS"}}`
* Haqiqiy dasturiy kodni sizning **backend serveringiz** (Python, Node.js yoki Go) xavfsiz muhitda bajaradi va natijani modelga qaytaradi!

### C. JSON Schema — Model va Server O'rtasidagi Rasmiy Shartnoma
Har bir asbob modelga OpenAPI standarti bo'yicha beriladi:
* `name`: Funksiya nomi (masalan, `get_stock_price`).
* `description`: **Eng muhim maydon!** Model aynan shu matnni semantik jihatdan tahlil qilib, foydalanuvchi savoliga qaysi asbob kerakligini aniqlaydi.
* `parameters`: Qat'iy ma'lumot turlari (`string`, `number`, `boolean`) va majburiy maydonlar (`required`).

### D. ReAct (Reasoning + Acting) Tsikli
1. **Fikrlash va Chaqiruv (Thought & Action):** Model so'rovni ko'rib, asbob chaqiruvchi JSON chiqaradi.
2. **Kuzatuv (Observation):** Backend API so'rov yuborib, xom ma'lumotni (masalan, `{"price": 234.85}`) kontekstga `role: "tool"` sifatida kiritadi.
3. **Sintez (Grounded Synthesis):** Model faktlarga tayanib foydalanuvchiga to'liq, xatosiz javob qaytaradi.

### E. Xavfsizlik: Read-Only vs Destructive va Human-in-the-Loop
* **Read-Only (Xavfsiz):** Valyuta kursi, ob-havo, qidiruv. Fonda avtomatik bajariladi.
* **Destructive (Xavfli / Mutatsiya):** Bazani o'chirish (`DROP TABLE`), pul o'tkazish, tizim kodini deploy qilish.
* **Human-in-the-Loop (HITL):** Xavfli amallar oldidan agentlik tizimi to'xtaydi va administrator ruxsatini (`[Approve] / [Reject]`) talab qiladi.
* **PoLP (Principle of Least Privilege):** Agentning bazadagi foydalanuvchisiga faqat `SELECT` ruxsati beriladi.

### F. Sanoat Standarti: MCP (Model Context Protocol)
Anthropic tomonidan 2024-yilda chiqarilgan ochiq standart. U har bir API uchun alohida kod yozish o'rniga, AI agentlarni tashqi manbalarga (GitHub, PostgreSQL, Slack, Google Drive) xuddi universal USB shnuri kabi ulash imkonini beradi.

---

## 3. 40 Daqiqalik Darsning Bosqichma-Bosqich Ssenariysi

### 00:00 – 05:00 | Kirish va Fikr Uygotish (Slayd 1–3)
* **Prezentatsiya:** 1-slaydni oching.
* **O'qituvchi nima deydi (rus tilida):**
  > *"Господа инженеры, в первой части нашего блока мы изучили внутреннее устройство мозга LLM. Но представьте гениального математика, которого заперли в комнате без окон, без часов и без интернета. Сможет ли он сказать, какая погода на улице или сколько стоят акции Apple прямо сейчас? Нет! Он начнет фантазировать и угадывать. Сегодня мы даем модели руки — изучаем механизм Tool Calling. Мы научим нейросеть вызывать реальные API, читать базы данных и защищать прод от опасных команд!"*

### 05:00 – 18:00 | Nazariy Tahlil: Sxema, ReAct va Xavfsizlik (Slayd 4–8)
* **JSON Schema (Slayd 4):** Doskada ko'rsating — agar `description` bo'lmasa, model qaysi funksiya nima qilishini tushunmaydi.
* **ReAct 3 bosqichli tsikli (Slayd 5):** O'quvchilardan ReAct tsiklining 3 bosqichini ketma-ket aytib berishlarini so'rang:
  1. Model Tool Call JSON yuboradi.
  2. Server API ni chaqirib natijani oladi.
  3. Model fakt asosida javob yozadi.
* **Read-Only vs Destructive (Slayd 7–8):** Sinfga savol bering:
  > *"Представьте, что наш AI-ассистент подключен к базе данных школы. Пользователь пишет: 'Очисти базу плохих оценок'. Если у модели есть полный доступ, она отправит `DROP TABLE grades;`! Как мы, как Senior-архитекторы, защитим систему?"*
  *(Kutilayotgan javob: 1. Human-in-the-Loop tasdig'i; 2. Bazada agentga faqat SELECT huquqini berish).*

### 18:00 – 33:00 | Amaliy Laboratoriya (`lab/index.html`) va Varaqa To'ldirish
* O'quvchilar noutbuklarida `lab/index.html` ni ochishadi va qog'oz ish varaqasidagi 4 bosqichni bajarishadi:
  1. **Aksiya narxi:** "Пресеты: 📈 Курс акций AAPL" tugmasini bosishadi $\rightarrow$ Model qanday qilib `get_stock_price` JSON chaqiruvini shakllantirganini va birja javobini ko'rishadi $\rightarrow$ Narx va Latency ni varaqaga yozishadi.
  2. **Valyuta konvertatsiyasi:** "💱 Конвертер 1500 USD" tugmasi $\rightarrow$ `amount: 1500` raqam turi ekanini va hisoblangan so'm summasini qayd qilishadi.
  3. **SQL Ma'lumotlar bazasi:** "🗄️ База пользователей" tugmasi $\rightarrow$ `SELECT` buyrug'i 3 ta qator qaytarganini ko'rishadi.
  4. **Xavfsizlik Stress-Testi:** "⚠️ Атака: DROP TABLE users;" tugmasi $\rightarrow$ Qizil ogohlantirish (`SECURITY ALERT: Destructive query rejected!`) paydo bo'lishini va baza himoyalanganini audit qilishadi.

### 33:00 – 40:00 | Tahlil, Savol-Javob va Baholash (Slayd 9–12)
* O'quvchilar bilan xatolar sodir bo'lganda nima qilish kerakligini (Self-Healing Loop) muhokama qiling.
* Ish varaqalarini yig'ib oling va 10 ballik rubrika bo'yicha baholang:
  - ReAct va JSON Schema nazariyasi: 3 ball
  - Laboratoriya telemetriyasi (Stock, FX, SQL): 3 ball
  - Xavfsizlik auditi (DROP TABLE & HITL): 4 ball
  - Self-Healing & MCP himoyasi (Bonus): +2 ball

---

## 4. O'quvchilarning Ehtimoliy Qaltis Savollari va Aniq Javoblar

**1-Savol: "Nega model shunchaki Python kodini o'zida yozib, o'zining GPU sida ishga tushirib qo'ya qolmaydi?"**
* **Javob:** Neyrotizim — bu faqat matritsali ehtimollik hisoblagichi, operatsion tizim emas. Agar modelga terminalga to'g'ridan-to'g'ri kirish berilsa, har qanday xaker Prompt Injection orqali butun serverni format qilib tashlashi yoki ma'lumotlarni o'g'irlashi mumkin. Shuning uchun model faqat JSON talab qiladi, kodni esa izolyatsiyalangan Docker konteynerida xavfsiz server bajaradi.

**2-Savol: "RAG (Retrieval-Augmented Generation) va Tool Calling o'rtasida qanday farq bor?"**
* **Javob:** RAG — bu asboblarning bir xususiy ko'rinishi xolos. RAG da faqat hujjatlardan qidiruv (`search_documents`) asbobi ishlatiladi. Tool Calling esa ancha kengroq: u nafaqat o'qiydi, balki matematik hisoblaydi, buyurtma yaratadi, Telegramga xabar jo'natadi va tizimlarni boshqaradi.

**3-Savol: "Agar biz modelga 100 ta har xil asbob berib yuborsak nima bo'ladi?"**
* **Javob:** Bu holat muhandislikda "Tool Bloat" va "Tool Confusion" deb ataladi. Birinchidan, 100 ta funksiya sxemasi kontekst oynasining 20–30 ming tokenini shunchaki yeb qo'yadi (har bir so'rov pul turadi!). Ikkinchidan, o'xshash funksiyalar (masalan, `search_user` va `find_account`) orasida model chalkashib, noto'g'ri asbobni chaqira boshlaydi. Yechim: Semantic Router orqali modelga faqat hozir kerakli 3–5 ta asbob uzatiladi.

---

## 5. Dars Jihozlari Nazorati
- [ ] `classes/10-11-sinf/3-hafta/14-dars-tool-calling-va-funksiyalar/prezentatsiya.html` brauzerda tekshirildi (RU tili, 12 slayd).
- [ ] `classes/10-11-sinf/3-hafta/14-dars-tool-calling-va-funksiyalar/lab/index.html` ochilib, barcha 4 ta tugma tekshirildi.
- [ ] `classes/10-11-sinf/3-hafta/14-dars-tool-calling-va-funksiyalar/varaqa.html` chop etishga tayyor (1 varaq A4, `@media print`).
