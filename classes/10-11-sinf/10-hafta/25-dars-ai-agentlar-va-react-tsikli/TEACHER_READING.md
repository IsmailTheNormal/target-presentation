# 25-Dars: O'qituvchi Uchun Metodik Qo'llanma va Yechimlar Kaliti
**Target International School // 10–11-Sinf // 10-Hafta (2-Chorak 1-Darsi: 40 daqiqa)**
**Mavzu:** AI Agentlar Paradigmasi va ReAct Tsikli (Yao et al., 2022)
**Kohorta:** `10-11-sinf` (Senior AI & Enterprise Architecture Track)

---

## 1. Asosiy Pedagogik Maqsad
Bugungi dars bilan 10–11-sinflar **2-Chorak: Agentik Dasturlash va Avtonom Tizimlar** katta muhandislik siklini boshlaydilar:
1. **Passiv LLM dan Agentgacha:** Chatbotlarning gallyutsinatsiya chegaralarini tushunish va ReAct (Reasoning + Acting) paradigmasining zarurati.
2. **ReAct Zanjiri:** Har bir harakatdan oldin niyatni shakllantirish (Thought), standart JSON Schema orqali asbobni chaqirish (Action) va tashqi muhitdan faktni qabul qilish (Observation).
3. **Cheksiz Sikllardan Himoya:** MAX_ITERATIONS qat'iy chegarasi va xatoliklar yuz berganda strategiyani o'zgartirish (Loop Suppression).
4. **Sandboxing va Kiber-Xavfsizlik:** Agentga erkin terminal bermasdan, Docker konteynerlar va muhim amallarda Human-in-the-Loop (HITL) o'rnatish.

---

## 2. 40 Daqiqalik Dars Reglamenti

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 03:00** | Kirish & 2-Chorak Rejasi | 2-Chorakda n8n, LangGraph va avtonom agentlar quramiz deb e'lon qilish. | Noutbuklarni ochish, ReAct konsepsiyasini ko'rish. |
| **03:00 – 08:00** | Aqliy Hujum (Gallyutsinatsiya) | Nega model kalkulyatorsiz matematikada adashishini ko'rsatish. | Fikr bildirish, farqlarni aniqlash. |
| **08:00 – 18:00** | Nazariya va Arxitektura | 12 slaydli akademik taqdimot, Yao et al. tadqiqoti va JSON Schema spetsifikatsiyasi. | Arxitektura bloklarini tahlil qilish. |
| **18:00 – 23:00** | Jonli Kiber-Test (Loop Debug) | Slayd 9 dagi cheksiz takrorlanish xatosini sinf bilan yechish. | Xato sababini aniqlash, to'g'ri tashxis qo'yish. |
| **23:00 – 36:00** | Amaliy ReAct Laboratoriyasi | O'quvchilar simulator studiyasida ReAct siklini jonli kuzatadilar va asboblarni bog'laydilar. | Simulyatorni ishga tushirish, qadamma-qadam tahlil. |
| **36:00 – 40:00** | Xulosa & Baholash | 10 ballik mezon asosida eng yaxshi agent modellariga baho qo'yish, `vazifa.html` ni berish. | Ishlarni ko'rsatish, vazifani saqlab olish. |

---

## 3. Viktorina va Topshiriqlar Yechimi (Teacher Fixes)

### Viktorina (Slayd 9):
* **Savol:** ReAct siklidagi qaysi xatolik cheksiz takrorlanishga olib keldi?
* **To'g'ri javob:** **B) Observation (xato) model tarixiga qo'shilmayapti yoki MAX_STEPS cheklovi yo'q**
* **Izoh:** Modelga xato haqida signal bormasa, u avvalgi xato harakatini eslamaydi va 500 marta bir xil xato asbobni chaqiraveradi.

### Uy Vazifasi Yechimlari:
1. **JSON Schema:** `name`, `description`, `parameters` (type, properties, required) to'g'ri tuzilishi shart.
2. **Loop suppression:** Qat'iy `MAX_ITERATIONS = 5` va Observation ichiga strategiyani o'zgartirish bo'yicha ko'rsatma berish.
3. **Prompt Injection himoyasi:** Read-only rejim, System promptda Observation ma'lumotlarini "untrusted" deb belgilash va Human-in-the-Loop darvozasi.
4. **Multi-agent Supervisor:** Supervisor boshqaruvchi sifatida Researcher (qidiruvchi) va Analyst (hisobchi) agentlarini muvofiqlashtiradi.

---

## 4. Baholash Mezoni (10 Ball)
* **3 Ball:** ReAct tsikli (Thought $ightarrow$ Action $ightarrow$ Observation) qadamma-qadam to'g'ri amalga oshirilgan.
* **3 Ball:** Asboblar rasmiy JSON Schema spetsifikatsiyasiga to'liq mos yozilgan.
* **2 Ball:** Cheksiz sikllardan himoya (MAX_STEPS) qo'yilgan.
* **2 Ball:** Tashqi ma'lumotlar xotiraga (scratchpad) toza qo'shilgan va xavfsiz filtrdan o'tkazilgan.
