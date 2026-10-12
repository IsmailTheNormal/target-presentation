# 20-Dars: O'qituvchi Uchun Tayyorgarlik Qo'llanmasi (Teacher Prep Guide)
**Target International School // 10–11-Sinflar (Senior Engineering) // 4-Hafta (4-Soat · Final)**
**Mavzu:** Multi-Agent Tizimlari Xavfsizligi, Egress Nazorati va Demo Day

> **METODIK ESLATMA:** Bu 1-chorakning (1–4-haftalar, 20 dars) kulminatsion final darsi!
> O'quvchilar LLM ichki arxitekturasi (13), Tool Calling (14), RAG va vektor qidiruv (17),
> Prompt Injection mudofaasi (18) hamda Sandboxing va gVisor izolyatsiyasi (19) bo'yicha
> to'plagan barcha amaliy bilimlarini bitta xavfsiz prodaction tizimga birlashtiradilar va
> **Senior Capstone Demo Day** da o'z loyihalarini himoya qiladilar.

---

## 1. Darsda Qaysi Vositalar Ishlatiladi?

1. **Multi-Agent Audit Console (Google Chrome):**
   * Fayl: `classes/10-11-sinf/4-hafta/20-dars-multi-agent-xavfsizligi-va-demo-day/lab/index.html`
   * Internet yoki tashqi API kalitlar talab qilinmaydi (brauzer ichida to'liq xavfsiz telemetriya).
   * Stendda: 4 ta agent tuguni (User -> Planner -> Coder Sandbox -> Deployer), 4 ta xavfsizlik shlyuzi (Egress DLP, Trust Boundary IAM, HashiCorp Vault dinamik tokenlar, Langfuse Immutable Audit Trail), 3 ta real vaqtli hujum ssenariysi va rasmiy Bitiruvchi Diplomi generatori.
2. **Prezentatsiya:** `prezentatsiya.html` — 12 slayd, `N` — spiker izohlari.
3. **Ishchi Varaqa:** `varaqa.html` — 2 betlik A4 chop etiladigan Demo Day baholash vedomosti.

---

## 2. Demo Day Vaqti Reglamenti (45 Daqiqa)

* **0–3 daqiqa:** Titul slayd: 20 darslik muhandislik yo'lini sarhisob qilish va Demo Day reglamentini e'lon qilish.
* **3–15 daqiqa:** Multi-agent tizimlaridagi yangi xavfsizlik arxitekturasi:
  - Confused Deputy va cross-agent huquqni oshirish tahdidi.
  - Ishonch chegaralari (Trust Boundaries) va Least Privilege.
  - Egress DLP (API kalitlar va PII ni qirqish) va HashiCorp Vault dinamik tokenlari (TTL 15 min).
  - Langfuse orqali har bir agent qadamini doimiy tekshirish (OpenTelemetry spans).
* **15–20 daqiqa:** Interaktiv stend (`lab/index.html`): Multi-agent konsolini sinab ko'rish.
* **20–38 daqiqa:** **JONLI DEMO DAY TAQDIMOTLARI (18 daqiqa):**
  - Har bir jamoa/o'quvchiga **4 daqiqa** vaqt:
    1. 1-daqiqa: Muammo va agentlar topologiyasi.
    2. 2-daqiqa: RAG va kosinus qidiruv (adashmasdan javob).
    3. 3-daqiqa: Kiber-hujum sinovi (Prompt injection va sandboxing).
    4. 4-daqiqa: O'qituvchi savoli va mudofaa.
* **38–42 daqiqa:** Hakamlik va baholash: 10 ballik mezon bo'yicha varaqalarni to'ldirish.
* **42–45 daqiqa:** Diplomlarni topshirish, g'oliblarni qutlash va 5-haftadagi Kriptografiya mavzusiga debocha.

---

## 3. Noutbuksiz O'quvchilar Uchun Alternativa (No-Laptop Path)

Demo Day kuni noutbuksiz o'quvchilar **Hakamlar Hay'ati Auditorlari (Security Review Board)** sifatida faoliyat yuritadi:
- Ular qo'llaridagi `varaqa.html` ning 2-sahifasidagi **3-bo'lim (Baholash jadvali)** va **4-bo'lim (Savol-javob bayonnomasi)** ni to'ldiradilar.
- Taqdimot qilayotgan jamoalarga "Sizning agentingizda Egress DLP qanday sozlangan?", "Agar Planner agent buzilsa, Deployer bazani o'chirib yubormasligiga qanday kafolat berasiz?" kabi jiddiy muhandislik savollarini beradilar.
- Noutbuksiz o'quvchining savol-javobdagi faolligi to'liq 10 ball bilan baholanadi.

---

## 4. O'quvchilarning Keng Tarqalgan Xatolari (Misconceptions)

1. *"Barcha agentlar bitta umumiy tizimda bo'lsa, ularni bir-biridan himoya qilish shart emas."*
   - **Tushuntirish:** Bu eng katta xato! Zero Trust qoidasiga ko'ra ichki tarmoqqa ham to'liq ishonilmaydi. Agar foydalanuvchi bilan muloqot qiluvchi agent aldansa, u orqali butun ichki infratuzilmani egallab olishi mumkin (Confused Deputy).
2. *"DLP faqat fayllarni skanerlaydi, chat javoblariga daxli yo'q."*
   - **Tushuntirish:** Model matn ko'rinishida `sk-ant-api03-...` kalitini foydalanuvchiga chiqarib bersa, bu ham ma'lumot sizishi hisoblanadi. Shuning uchun har bir chiquvchi token oqimi Egress DLP filtri orqali maskalanadi.
3. *"Demo Day da chiroyli slayd ko'rsatish yetarli."*
   - **Tushuntirish:** Senior Engineering darajasida slayd emas, **ishlayotgan mahsulot** talab qilinadi. Tizim jonli testda xakerlik so'rovini qaytara olishi kerak.
