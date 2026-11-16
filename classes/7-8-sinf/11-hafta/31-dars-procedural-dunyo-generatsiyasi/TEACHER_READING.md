# 7–8-sinf, 11-hafta, 31-dars: O'qituvchi Qo'llanmasi
## Procedural Dunyo Generatsiyasi: Tasodifiy Labirintlar va Xazinalar

### Dars Haqida Ma'lumot:
- **Kohorta:** 7–8-sinf (Game Dev, Interaktiv Veb & FUT Creator Track)
- **Format:** 40 daqiqalik Yakka Dars (Single Block)
- **Asosiy maqsad:** O'quvchilarga procedural dunyo generatsiyasi (PCG) tushunchasini o'rgatish, Random Walker (Mast konchi) algoritmi orqali doimo o'tib bo'ladigan xaritalar yasash, chegaralarni himoyalash va berk ko'chalarga xazinalar joylashtirish.

---

### 40 Daqiqalik Dars Pacing Xaritasi:

| Vaqt | Bosqich | Slayd | O'qituvchi Harakati | Kutiladigan Natija |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va PCG | 1 | Dars mavzusini e'lon qilish, Minecraft va Hades qanday qilib darajalarni avtomatik yasashini aytish. | O'quvchilar PCG ning o'yinlardagi ahamiyatini tushunishadi. |
| **04:00–08:00** | O'tgan Dars HW Tahlili | 2 | 30-darsdagi statik 2D massiv xatosini tahlil qilish. Blitz savoli. | O'quvchilar nega statik xaritalar zerikarli bo'lib qolishini anglaydilar. |
| **08:00–12:00** | PCG Falsafasi | 3 | Replayability va kichik fayl hajmi ustunliklarini doskada tushuntirish. | Algoritmik dunyo yaratish tamoyillari o'zlashtiriladi. |
| **12:00–16:00** | Random Walker Qadamlari | 4 | 4 ta qadam: 1 bilan to'ldirish, konchi spawn, tasodifiy burilish, xazinalar. Nega bu yo'l 100% bog'liq ekanini ko'rsatish. | Random Walker qoidalari o'rganiladi. |
| **16:00–20:00** | Chegaralar va Berk Ko'chalar | 5 | Chegaradan chiqmaslik sharti (1 &lt;= x &lt; cols - 1) va berk ko'cha (dead-end) tushunchasini chizib berish. | Sandiqlar va chiqish eshigi qayerga qo'yilishi tushuniladi. |
| **20:00–24:00** | Kod Mexanizmi | 6 | `generateDungeon()` kodini qatorma-qator tahlil qilish, `dx/dy` yo'nalishlar massivini ko'rsatish. | JavaScript generator sintaksisi o'rganiladi. |
| **24:00–28:00** | Jonli Smartboard Demo | 7 | Slayd ichidagi simulyatorda Avto-Qazish tugmasini bosib, konchining real-vaqtda yo'l ochishini ko'rsatish. | Vizual idrok mustahkamlanadi. |
| **28:00–32:00** | Bilimni Sinash (Quiz) | 8 | 3 ta savol bo'yicha interaktiv viktorina o'tkazish. | O'quvchilar tushunchalari mustahkamlanadi. |
| **32:00–37:00** | 15 Daqiqalik Arena | 9 | `simulator/index.html` ilovasida o'quvchilarga o'z generatorlarini yozishni buyurish. | Har bir o'quvchi o'z labirintini generatsiya qiladi. |
| **37:00–40:00** | Baholash va Keyingi Dars | 10 | 10 ballik mezonni e'lon qilish, 3 darajali uy vazifasini tushuntirish va dushman AI mavzusiga ko'prik. | Uy vazifasi tushuniladi. |

---

### Keng Tarqalgan Savollar va Pedagogik Ko'rsatmalar:
1. **"Nega konchi xaritadan chiqib ketmasligi kerak?"**
   - Javob: Agar konchi `x < 0` yoki `x >= cols` bo'lib qolsa, JavaScript `map[y][x]` da `undefined` xatolik beradi va o'yin qotib qoladi.
2. **"Dead-end (berk ko'cha) qanday aniqlanadi?"**
   - Javob: Katakning 4 ta qo'shnisi tekshiriladi: agar 3 tasi devor (1) bo'lsa va faqat bittasi yo'l (0) bo'lsa, bu katak berk ko'cha hisoblanadi. O'yinda o'yinchi berk ko'chaga borganda mukofot olishi uchun u yerga oltin sandiq qo'yiladi!
