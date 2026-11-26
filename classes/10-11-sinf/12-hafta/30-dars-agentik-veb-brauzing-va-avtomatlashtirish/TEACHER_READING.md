# 30-dars: Agentik Veb-Brauzing va Headless Avtomatlashtirish (O'qituvchi Metodologiyasi)

## Darsning Pasporti
- **Sinf:** 10–11-sinf (Senior AI & Enterprise Cybersecurity Track)
- **Davomiyligi:** 80 daqiqa (Juftlik Dars / Double Block)
- **Asosiy maqsad:** O'quvchilarga AI agentlarni faqat qat'iy API-lar bilan cheklamay, ochiq internetda inson kabi harakatlanuvchi avtonom brauzer tizimlarini (Browser-Use, Stagehand, Playwright) loyihalashni o'rgatish. 1 MB xom HTML-ni 5 KB Accessibility Tree-ga qisqartirish, Set-of-Mark (SoM) orqali vizual elementlarni aniqlash va modal bannerlarni chetlab o'tuvchi chidamli veb-agentlarni dasturlash.

---

## 80 Daqiqalik Aniq Vaqt Taqsimoti (Pacing)

### 1-Qism: Nazariya, Xatolar Tahlili va Jonli Test (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Motivatsiya | 1 | Veb-agentlar nega 2026-yilda AI sohasining eng talabgir yo'nalishi ekanini tushuntirish. | Diqqat bilan tinglaydilar va dars maqsadini belgilaydilar. |
| **04:00–12:00** | 29-dars HW Tahlili | 2 | Coder-Critic tizimida bitta test yiqilganda butun modulni noldan yozish xatosi (regressiya) tahlili. | Blitz savolga javob beradilar, surgical diff qoidasini yozib oladilar. |
| **12:00–18:00** | Arxitektura To'sig'i | 3 | Nega oddiy curl/requests yoki LLM xom HTML-ni o'qiy olmasligini ko'rsatish (tokenlar portlashi, dinamik DOM). | Real veb-sahifa og'irligini tushunadilar. |
| **18:00–24:00** | Headless Brauzer | 4 | CDP (Chrome DevTools Protocol) soket mexanizmi va Playwright arxitekturasini tushuntirish. | Selenium bilan farqini ko'rib chiqadilar. |
| **24:00–30:00** | DOM Distillyatsiyasi | 5 | 1 MB HTML dan 95% stillarni tozalab, Accessibility Tree (5 KB) yasash tamoyili. | Tokenlarni 98% tejash sirini o'rganadilar. |
| **30:00–35:00** | Vision-Action Tsikli | 6 | Set-of-Mark (SoM) raqamlangan ramkalar va multimodal ko'rish modelining ishlash tartibi. | Observe -> Plan -> Act zanjirini o'rganadilar. |
| **35:00–40:00** | Kiber-Himoya & Anti-Bot | 7–8 | CAPTCHA paydo bo'lganda HITL (Human-in-the-Loop) qoidasi va WAF banlaridan himoya (jitter). | Xavfsizlik chegaralarini yozib oladilar. |

### 2-Qism: Smartboard Sinovi, Katta Arena va Showcase (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **40:00–48:00** | Smartboard Simulyatori | 9 | Slayddagi Browser-Use simulyatorini ishga tushirish (Reklama bannerini yopish, qidiruv berish). | Agent qanday qilib modal oynani yopganini kuzatadilar. |
| **48:00–55:00** | Viktorina (Quiz) | 10 | 3 ta nazorat savoli bo'yicha tezkor viktorina o'tkazish. | Faol javob beradilar va o'z bilimlarini tekshiradilar. |
| **55:00–70:00** | 25 Daqiqalik Arena | 11 | 25:00 taymerni yoqish, partalar bo'ylab yurib ko'maklashish. | simulator/index.html da noutbuk narxlarini yig'uvchi agentni dasturlaydilar. |
| **70:00–74:00** | Partadosh Auditi | 12 | O'rin almashishni e'lon qilish, max_steps va selektorlar mustahkamligini tekshirish. | Bir-birining agentiga modal to'siq qo'yib, chidamliligini sinaydilar. |
| **74:00–77:00** | Katta Ekran Showcasi | 13 | Eng kam token sarflagan veb-agentni katta ekranga chiqarib ko'rsatish. | Sinfdoshlari natijasini tahlil qiladilar. |
| **77:00–80:00** | Uy Vazifasi va Yakun | 14 | 10 ballik uy vazifasini tushuntirish va Computer-Use mavzusiga ko'prik! | Kundaliklariga vazifani belgilaydilar. |

---

## O'qituvchi Uchun Muhim Blitz Savollari
1. **"Nega veb-agent uchun xom HTML yuborish falokatli hisoblanadi?"**
   - Javob: Chunki zamonaviy sahifada 1 MB dan ortiq Tailwind klasslari, SVG koordinatalar va bo'sh divlar bor. Bu butun kontekst oynasini to'ldirib, bir urinishdayoq 30,000 tokenni yoqib yuboradi.
2. **"Agar agent saytda Cloudflare CAPTCHA ga duch kelsa, qanday yo'l tutishi shart?"**
   - Javob: Hech qachon avtomat yechishga urinmasligi kerak. Jarayonni muzlatib, insonga (HITL) signal berishi va inson real oynada klik qilgach davom etishi shart.

---

## 10 Ballik Baholash Rubrikasi
- **4 Ball (Baza):** Accessibility Tree tuzilmasini tushunadi va interaktiv elementlar ro'yxatini to'g'ri filtrlaydi.
- **4 Ball (Amaliy):** Agent reklama bannerini yopib, qidiruv beradi va jadval ma'lumotlarini JSON formatida ajratadi.
- **2 Ball (Challenge):** max_steps=10 cheklovi, tabiiy jitter kechikishi va CAPTCHA chiqqanda HITL signali qo'shilgan!
