# 26-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Briefing)

**Kohorta:** 10–11-Sinf · Senior AI & Enterprise Kiberxavfsizlik Track  
**Mavzu:** Agentik Tool Calling, Funksiyalar va Xavfsiz Sandboxing  
**Ajratilgan vaqt:** 80 daqiqa (Juftlik blok / Double Block)  
**Amaliy natija:** LLM ga tashqi asboblarni (Tools) JSON Schema orqali ulash, deterministik argumentlar validatsiyasi, xavfli buyruqlarni bloklash va sandbox muhitida xavfsiz bajarish.

---

## 1. 5 Daqiqalik Darsoldi Konspekti (O'qituvchiga Eslatma)
Katta til modellari (LLM) o'zicha mustaqil hisob-kitob qila olmaydi yoki real vaqt ma'lumotlarini bilmaydi.
Ular **Tool Calling (Function Calling)** protokoli orqali tashqi dunyo bilan aloqa qiladi:
1. **JSON Schema:** Modelga funksiya qanday nomlanishi, nima vazifa bajarishi va qanday parametrlar qabul qilishi deklarativ ta'riflanadi.
2. **Argumentlar Validatsiyasi:** LLM bergan argumentlar xom holda ishlatilmaydi, Zod / Pydantic bilan qat'iy tekshiriladi.
3. **Sandboxing & RCE Mudofaasi:** Agentga hech qachon xom `eval()` yoki erkin bash berilmaydi. Buyruqlar izolyatsiyalangan konteynerda bajariladi.
4. **Observation Feedback:** Vosita xato qaytarsa, jarayon to'xtatilmaydi — xato matni modelga yuboriladi va u o'zini o'zi tuzatadi.

---

## 2. 80 Daqiqalik Vaqt Xaritasi (Double Block Roadmap)
| Vaqt | Bosqich | O'qituvchi amali | O'quvchi harakati |
|---|---|---|---|
| **00–04 daq** | Titul & Motivatsiya | Proyektorda 1-slaydni ochish, modelga 'qo'l' berish tushunchasini e'lon qilish | Muhandislik maqsadini tushunish |
| **04–10 daq** | O'tgan Dars Tahlili (HW Review) | 25-darsdagi ReAct tsikli va cheksiz aylanish (loop guard) xatolarini tahlil qilish | ReAct bosqichlarini qaytarish |
| **10–16 daq** | Parametrik Xotira Cheklovi | Nega LLM arifmetikada va yangi faktlarda yanglishishini ko'rsatish | Hallucination sababini yozish |
| **16–22 daq** | Tool Calling Konveyeri | 4 bosqichli oqimni (Prompt ➔ JSON ➔ Sandbox ➔ Observation) tushuntirish | Daftarga konveyerni chizish |
| **22–30 daq** | Jonli Simulyator (Slayd 5) | Smartboardda kalkulyator, ob-havo va xavfli bash buyruqlarini sinab ko'rsatish | Smartboardga chiqib asbob chaqirish |
| **30–40 daq** | JSON Schema & Sandboxing | 6–9 slaydlar: `name`, `description`, `required`, RCE xavfsizligi va 10-slayddagi kiber-test | Kiber-quiz javobini belgilash |
| **40–65 daq (25 min)** | Katta Amaliy Arena | Har bir o'quvchi kompyuterida `simulator/index.html` ni ochish, 25 daqiqalik taymerni yoqish | 3 ta asbob uchun sxema yozish |
| **65–72 daq (7 min)** | Juftlikda Peer Review | Partadoshlar bir-birining asboblar sxemasini xatolik va RCE zaifliklariga tekshiradi | Kodni audit qilish |
| **72–76 daq (4 min)** | Xatolar Tahlili (Bug Hunter) | Model o'ylab topgan soxta parametrlar va command injection himoyasini tushuntirish | Extra-forbid qoidasini yozish |
| **76–80 daq (4 min)** | Baholash va Vazifa | 10 ballik mezon asosida baholash, `vazifa.html` topshirig'ini tushuntirish | Ish varaqalarini topshirish |

---

## 3. Baholash Mezoni (10 Ballik Standart)
- **1–4 Ball (Baza):** 2 ta to'g'ri JSON Schema yozildi (`name`, `description`, `parameters`, `required`).
- **5–7 Ball (Standart):** Argumentlar validatsiyasi va xatolarni Observation ga xavfsiz qaytarish dasturlandi.
- **8–10 Ball (Senior AI Engineer):** Sandboxing filtri to'liq ishlaydi, xavfli buyruqlar bloklandi va ish varaqasi 100% to'ldirildi.
