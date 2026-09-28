# O'qituvchi uchun Qo'llanma — 16-Dars: Avtonom Agentlar va Kengaytirilgan Xotira

## 1. Darsning Pedagogik Maqsadi
O'quvchilarga sun'iy intellektning oddiy chatbot darajasidan mustaqil agentlik darajasiga (L1 dan L5 gacha) o'tish mexanizmini ko'rsatish. Agent arxitekturasining 4 tayanchi (Planning, Memory, Tools, Action/Reflection), STM va LTM xotira tizimlari, ReAct va Multi-Agent (Supervisor-Worker) orkestratsiyasini hamda avtonom tizimlarni jilovlash (Circuit Breaker, Human-in-the-Loop) usullarini amaliyotda o'rgatish.

## 2. Dars Vaqti Taqsimoti (40 daqiqa)
- **0–3 daq:** Tashkiliy qism. Chatbot vs Avtonom Agent darajalari.
- **3–13 daq:** Nazariya: 4 tayanch modul, STM vs LTM xotira (Semantik, Epizodik, Protsedural).
- **13–23 daq:** Arxitektura: Subgoal Decomposition, Multi-Agent Supervisor modeli, Circuit Breaker va HITL chegaralari.
- **23–33 daq:** Amaliyot: `lab/index.html` da avtonom missiyani ishga tushirish, epizodik xotirani kuzatish va HITL tasdig'ini berish.
- **33–37 daq:** Tahlil: LangSmith va Tracing orqali agentlarni nosozliklardan tozalash (debugging).
- **37–40 daq:** Xulosa va 10 ballik mezon bo'yicha baholash.

## 3. O'quvchilarga beriladigan savollar
1. "Nega Cursor yoki Devin kabi agentlar oddiy ChatGPT dan 10 barobar qimmatroq hisoblanadi?"
2. "Agar agent cheksiz xatoga tushib qolsa (Infinite loop), kompaniyaga qanday zarar yetkazishi mumkin?"
3. "Qaysi amallarni hech qachon agentga 100% ishonib topshirib bo'lmaydi va nima uchun?"
