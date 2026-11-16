# 10–11-sinf: 27-dars — Agent Xotirasi va Doimiy Kontekst: Epizodik, Semantik va Vector Cache
**Target International School · Yunusobod Filiali**
**O'qituvchi:** Ismoiljon Usmonov · **Format:** 80 Daqiqa (Double Block / Juftlik dars)

---

## 🎯 Dars Maqsadi va Asosiy Mohiyati
Ushbu 80 daqiqalik darsda 10–11-sinf o'quvchilari LLM larning eng katta muammosi bo'lgan amneziya (xotirasizlik) va "Lost in the Middle" sindromini hal qiladilar.

O'quvchilar inson miyasiga o'xshash 3 qatlamli kognitiv xotira modelini o'rganadilar:
1. **Working Memory (Scratchpad in RAM):** Joriy ReAct qadami va qisqa muddatli kontekst.
2. **Episodic Memory (SQLite Event Log):** Foydalanuvchi afzalliklari va vositalar xatolari tarixi.
3. **Semantic Memory (ChromaDB / Vector Store):** 1536 o'lchamli vektorlar va Kosinus o'xshashlik Top-K saralash.

---

## ⏱️ 80 Daqiqalik Vaqt Taqsimoti (2 Bosqichli Reja)

### 1-Bosqich: Nazariya, Protokol va Jonli Simulyator (40 Daqiqa)
* **00:00 – 04:00 (4 min) | Kirish & Missiya:** Dars mavzusi va 10 ballik mezonni e'lon qilish.
* **04:00 – 10:00 (6 min) | 26-Dars Tahlili (HW Review):** Tool calling cheklovlari va doimiy xotira zaruriyati. 30 soniyalik blits savol.
* **10:00 – 16:00 (6 min) | Real Muammo:** LLM amneziyasi, 100K token isrofi va "Lost in the Middle" U-simon e'tibor pasayishi.
* **16:00 – 22:00 (6 min) | 3 Qatlamli Kognitiv Arxitektura:** Working, Episodic va Semantic qatlamlari.
* **22:00 – 28:00 (6 min) | Epizodik SQLite Xotirasi:** agent_memories jadvali va preferensiyalarni indekslash.
* **28:00 – 35:00 (7 min) | Semantik Vektor Qidiruv:** Kosinus o'xshashlik matematikasi va Top-K filtri.
* **35:00 – 40:00 (5 min) | Xotira Siqish (Compaction):** Summarization Buffer va Park et al. (2023) ahamiyat formulasi.

### 2-Bosqich: Jonli Tajriba, Kiber-Arena va Demos (40 Daqiqa)
* **40:00 – 48:00 (8 min) | Jonli Slayd Simulyatori:** Smartboardda xotiradan faktlarni izlash va Top-1 o'xshashlikni tekshirish.
* **48:00 – 54:00 (6 min) | Interaktiv Kiber-Quiz:** 3 ta savol bo'yicha blits o'tkazish.
* **54:00 – 69:00 (15 min) | Kiber-Arena (Amaliyot):** O'quvchilar `simulator/index.html` da xotira dvigatelini yozadilar.
* **69:00 – 74:00 (5 min) | Juftlikda Peer-Review:** 4 ta mezon bo'yicha xotira izolyatsiyasi va kosinus filtri auditi.
* **74:00 – 77:00 (3 min) | O'quvchilar Demosi:** 2 ta juftlik doskaga chiqib o'zlarining xotira dvigatelini namoyish etadi.
* **77:00 – 80:00 (3 min) | Xulosa & Uy Vazifasi:** 10 ballik `vazifa.html` ilovasini tushuntirish va Avtonom Kod Yozuvchi Agentlar mavzusini anons qilish.

---

## 🏆 10 Ballik Rasmiy Baholash Mezoni
1. **1-Daraja: Baza (4 ball):** SQLite da agent_memories jadvalini yaratish va preferensiyalarni olish.
2. **2-Daraja: Amaliyot (4 ball):** cosineSimilarity formulasini yozish va 0.75 dan yuqori Top-K xotirani ajratish.
3. **3-Daraja: Kiber-Sinov (2 ball):** Summarization Buffer orqali ko'p xabarlarni ixcham xulosaga siqish.
