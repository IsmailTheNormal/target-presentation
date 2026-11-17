# 10–11-sinf, 11-hafta, 28-dars: O'qituvchi Qo'llanmasi
## Multi-Agent Tizimlari: Supervisor va Worker Naqshlari (LangGraph)

### Dars Haqida Ma'lumot:
- **Kohorta:** 10–11-sinf (Senior AI & Enterprise Kiberxavfsizlik Track)
- **Format:** 40 daqiqalik Yakka Dars (Single Block)
- **Asosiy maqsad:** O'quvchilarga monolit agentlar cheklovlarini tushuntirish, mas'uliyatni ajratish (Separation of Concerns) orqali Supervisor va ixtisoslashgan Workerlar (Researcher, Coder, Reviewer) arxitekturasini o'rgatish, LangGraph StateGraph va conditional edges orqali xavfsiz marshrutlashni kodlash.

---

### 40 Daqiqalik Dars Pacing Xaritasi:

| Vaqt | Bosqich | Slayd | O'qituvchi Harakati | Kutiladigan Natija |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Maqsad | 1 | Dars mavzusini e'lon qilish, monolit vs multi-agent jamoalarini solishtirish. | O'quvchilar multi-agent zarurligini tushunishadi. |
| **04:00–08:00** | O'tgan Dars HW Tahlili | 2 | 27-darsdagi to'liq DB dump xatosini tahlil qilish. Blitz savol. | Nega semantik qidiruv kerakligi mustahkamlanadi. |
| **08:00–12:00** | Monolit Agent Muammosi | 3 | Diqqat chalkashishi (attention collapse) va ortiqcha vositalar oqibatlarini tushuntirish. | Mas'uliyatni ajratish tamoyili o'zlashtiriladi. |
| **12:00–16:00** | Supervisor-Worker Naqshi | 4 | Supervisor, Researcher, Coder, Reviewer rollarini doskada chizib ko'rsatish. | Rolli jamoa tuzilmasi tushuniladi. |
| **16:00–20:00** | LangGraph va StateGraph | 5 | Shared State, Nodes va Conditional Edges sintaksisini tahlil qilish. | Holat grafigi mantig'i o'rganiladi. |
| **20:00–24:00** | Deadlock va Kiberxavfsizlik | 6 | Max Iterations cheklovi va Human-in-the-Loop darvozasini tushuntirish. | Byudjet va xavfsizlik himoyasi anglanadi. |
| **24:00–28:00** | Jonli Smartboard Demo | 7 | Slayd ichidagi simulyatorda vazifani ishga tushirib, agentlar o'rtasida ma'lumot oqimini ko'rsatish. | Vizual idrok mustahkamlanadi. |
| **28:00–32:00** | Bilimni Sinash (Quiz) | 8 | 3 ta savol bo'yicha interaktiv viktorina o'tkazish. | O'quvchilar bilimi mustahkamlanadi. |
| **32:00–37:00** | 15 Daqiqalik Arena | 9 | `simulator/index.html` ilovasida o'quvchilarga o'z routerlarini kodlashni topshirish. | Har bir o'quvchi ishchi router yozadi. |
| **37:00–40:00** | Baholash va Ertangi Dars | 10 | 10 ballik mezonni e'lon qilish, 3 darajali uy vazifasini tushuntirish va ertangi 80 daqiqalik juftlik darsiga ko'prik. | Uy vazifasi tushuniladi. |

---

### Keng Tarqalgan Savollar va Pedagogik Ko'rsatmalar:
1. **"Nega LangGraph ishlatiladi, oddiy Python funksiyalari yetarli emasmi?"**
   - Javob: Oddiy Python funksiyalarida oraliq xatolik yuz bersa, agentning holati (state) yo'qoladi. LangGraph har bir qadamni xotirada saqlaydi, istalgan nuqtadan qayta tiklash (time-travel debugging) va inson ruxsatini (human-in-the-loop) ta'minlaydi.
2. **"Deadlock nima va undan qanday saqlaniladi?"**
   - Javob: Coder xato kod yozadi, Reviewer rad etadi; Coder yana tuzatib yuboradi, Reviewer yana rad etadi. Bu sikl cheksiz aylanib, barcha API pullarni tugatib yuborishi mumkin. Bunga qarshi `iterations >= 5` bo'lganda majburiy to'xtatish (circuit breaker) qo'yiladi.
