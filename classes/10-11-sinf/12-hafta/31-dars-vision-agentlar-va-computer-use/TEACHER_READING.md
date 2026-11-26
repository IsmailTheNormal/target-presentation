# O'qituvchi Qo'llanmasi (Teacher Reading)
## 10–11-sinf · 12-hafta · 31-dars
### Mavzu: Multi-Modal Vision Agentlar va Computer-Use: Ekran Boshqaruvi va Desktop Avtomatlashtirish
**Dars formati:** Yakka Dars (Single Block — 40 daqiqa)

---

### 1. Darsning Pedagogik Maqsadi va Falsafasi
O'tgan 30-darsda o'quvchilar brauzer ichida Playwright va Accessibility Tree orqali veb-sahifalarni tahlil qilishni o'rgandilar.
Bugungi 31-darsning vazifasi — o'quvchilarga DOM faqat brauzer bilan cheklanganini, ammo real biznesda korporativ dasturlar (Excel, Photoshop, Terminal, ERP, buxgalteriya dasturlari) mavjud bo'lib, ularda DOM umuman yo'qligini tushuntirishdir.
Anthropic tomonidan taqdim etilgan **Computer-Use** arxitekturasi AI agentga inson kabi ko'rish (Vision VLM) va klaviatura/sichqoncha orqali butun operatsion tizimni boshqarish imkonini beradi.

---

### 2. Vaqt Taqsimoti (40 Daqiqalik Aniq Reja)

| Daqiqa | Bosqich | O'qituvchi Faoliyati | O'quvchi Faoliyati |
|---|---|---|---|
| **00:00–04:00** | Kirish va Titul | Mavzuni e'lon qilish, dars maqsadi va kutilayotgan natijani ko'rsatish | Diqqatni jamlash, daftarga mavzuni yozish |
| **04:00–09:00** | 30-Dars Uy Vazifasi Tahlili | Keng tarqalgan xato (1.2 MB HTML yuborish), A11y afzalligi va 30 sek blitz savol | Blits savolga javob berish, xatolar tahlili |
| **09:00–14:00** | Nega DOM yetarli emas? | Canvas, Desktop dasturlar va OS chegaralarini tushuntirish | DOM va Vision farqlarini solishtirish |
| **14:00–19:00** | Computer-Use Tsikli | Screenshot -> VLM -> Action -> Observation zanjirini ko'rsatish | Tsikl ketma-ketligini tahlil qilish |
| **19:00–24:00** | Koordinatalar va HiDPI | Retina / 4K masshtab formulasi (scaleX, scaleY) va hisob-kitob | Formulani daftarga yozish, hisoblash |
| **24:00–28:00** | API Spetsifikatsiyasi | computer_20241022 JSON sxemasi va action turlari | Tool chaqiruv sintaksisini ko'rish |
| **28:00–32:00** | Kiberxavfsizlik va HITL | Docker izolyatsiyasi va inson tasdig'i (HITL) qoidalarini singdirish | Qaysi buyruqlar xavfli ekanini muhokama qilish |
| **32:00–35:00** | Python SDK Kodu | PyAutoGUI + Claude 3.5 Sonnet kodini ko'rsatish | Kod arxitekturasini o'rganish |
| **35:00–38:00** | Amaliy Simulyator | `simulator/index.html` da Kalkulyator va Notes missiyasini namoyish etish | Simulyatorda agent qadamlarini kuzatish |
| **38:00–40:00** | Xulosa va Uy Vazifasi | 3 darajali topshiriqni tushuntirish va darsni yakunlash | Vazifani belgilab olish |

---

### 3. Savol-Javob va Interaktiv Fikrlar

1. **Savol:** Nega neyrotarmoqqa 4K (3840×2160) tasvirni to'g'ridan-to'g'ri yuborish yomon g'oya?
   - **Javob:** Katta tasvirlar kontekst oynasini tezda to'ldiradi (har qadamda 2,000+ token), internet trafigini oshiradi va javob qaytish tezligini (latency) 5-10 soniyagacha sekinlashtiradi. Shu sababli 1024×768 ga siqiladi.
2. **Savol:** Nega agentni o'z shaxsiy Mac yoki Windows kompyuteringizda to'g'ridan-to'g'ri ishlatish xavfli?
   - **Javob:** Ko'rish xatosi yoki gallyutsinatsiya tufayli agent "Terminal" ochib tizim fayllarini o'chirib yuborishi (`rm -rf`) yoki shaxsiy xatlarni tarqatib yuborishi mumkin. Faqat Docker / Xvfb virtual qumloqda ishlatilishi shart.
3. **Savol:** Human-in-the-Loop (HITL) nima?
   - **Javob:** Agent moliyaviy operatsiya yoki fayllarni qaytarib bo'lmas darajada o'chirishdan oldin inson tasdig'ini (Confirmation Dialog) so'rashi shart bo'lgan xavfsizlik to'sig'i.
