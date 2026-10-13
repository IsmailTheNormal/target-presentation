# 20-Dars: O'qituvchi Uchun Maxsus Metodik Qo'llanma (Teacher Prep Guide)
**Target International School // 5–6-Sinflar (10–12 yosh) // 6-Hafta (1-Soat: 40 daqiqa)**
**Mavzu:** Kiber-Firibgarlar Ertagi: Ijtimoiy Muhandislik va "Tekin Robux" Qopqoni
**Kohorta:** `5A 5B 6A 6B` (Kiberxavfsizlik va Raqamli Madaniyat)

> **METODIK QOIDALAR (MUHIM):**
> 1. Diniy va noo'rin metaforalar mutlaqo ishlatilmaydi. Faqat professional IT, psixologik tushunchalar va xavfsizlik terminologiyasi ishlatiladi.
> 2. Hazil va memlar qat'iy cheklangan (maksimal 2 ta, faqat emotsional tushunish nuqtasida).
> 3. Har bir o'quvchi dars oxirida o'lchanadigan natijaga ega bo'ladi: **Social Engineering Detective Studio** da 6 ta chat ssenariysini tahlil qilib, **Kiber-Himoyachi Audit Sertifikati** ni qo'lga kiritadi va shaxsiy **5 ta Oltin Qoida Eslatmasi** ni yozadi.

---

## 1. Darsda Qaysi Vositalar Ishlatiladi?

1. **Interaktiv Laboratoriya (Social Engineering Detective Studio):**
   * Fayl manzili: `classes/5-6-sinf/6-hafta/20-dars-ijtimoiy-muhandislik-va-kiber-aldovlar/studio/index.html`
   * Internet talab etilmaydi — to'liq oflayn ishlaydi.
   * Studio imkoniyatlari:
     - Real-vaqtli kiber-firibgar chatlar simulyatsiyasi (Discord, Roblox, Telegram, Onlayn O'yinlar).
     - 6 ta hayotiy kiber-aldov ssenariysi: "Tekin Robux Generator", "Men Roblox Adminiman", "Akkauntingni boost qilaylik", "Yashirin kod keldi, aytvor", "Do'sting falokatga uchradi, tez pul tashla", "Maktab olimpiadasi soxta anketasi".
     - 4 ta kiber-psixologik tuzoq detektori: Shoshiltirish (Urgency), Qo'rqitish (Fear/Authority), Ochko'zlik/Tekinga qiziqish (Greed), Ishonch/Do'stlik niqobi (Impersonation).
     - "Xavfli kalit so'zlarni belgilash" (Highlight Red Flags) interaktiv vositasi.
     - 10 ballik mezon bo'yicha avtomatik tekshiruv va chop etiladigan **Yosh Kiber-Detektiv Sertifikati**.
2. **Prezentatsiya:**
   * Fayl: `prezentatsiya.html` — 12 slayd.
   * Klaviatura boshqaruvi: `->` keyingi slayd, `<-` oldingi slayd, `N` o'qituvchi izohlari, `L` til almashtirish (UZ/RU/EN), `T` tema (light/dark).
3. **Chop Etiladigan Varaqa (Worksheet):**
   * Fayl: `varaqa.html` — 2 betlik A4 ishchi varaqa (Zero-Blank Fallback, @media print xatosiz).

---

## 2. Darsning Pedagogik Maqsadi va Asosiy Konsepsiyalari

Ko'pchilik bolalar xakerlikni "kompyuter ekranida yashil kodlar oqishi va serverlarni buzish" deb o'ylashadi. Biroq real hayotda xakerlik hujumlarining 90% dan ortig'i kompyuterni emas, **inson ruhiyati va ishonchini buzish** (Social Engineering — Ijtimoiy Muhandislik) orqali amalga oshiriladi.

| Bolalarga tushunarli nom | Professional IT / Xavfsizlik Atamasi | Real Hayotdagi Mexanizm |
|---|---|---|
| Kiber-Niqob (O'zini boshqa deb ko'rsatish) | **Impersonation / Spoofing** | O'zini o'yin admini, do'st, taniqli bloger yoki qo'llab-quvvatlash xizmati xodimi sifatida tanishtirish. |
| Shoshiltirish Qopqoni | **Artificial Urgency (Sun'iy Shoshilinch)** | "Faqat 5 daqiqa vaqting bor, tez ayt!", insonni mantiqiy o'ylashga qo'ymaslik. |
| Qo'rquv va Bosim | **Authority & Fear Attack** | "Aytmasang, profiling 10 yilga bloklanadi!" — vahima orqali qimmatli ma'lumotni undirish. |
| "Tekin Pishloq" Qopqoni | **Baiting (Xo'rak tashlash)** | "Tekin 10,000 Robux, V-Bucks yoki Telegram Premium" deb va'da berish, login/kodni o'g'irlash. |
| Ikki Bosqichli Himoya Qoidasi | **2FA / Secret Code Privacy** | SMS yoki Telegram orqali kelgan tasdiqlash kodini hech kimga (hatto adminga ham) aytmaslik. |

---

## 3. 40 Daqiqalik Darsning Bosqichma-Bosqich Vaqt Taqsimoti

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 03:00** | Kirish va Qiziqtirish | "Kim Roblox yoki Brawl Stars da tekin Robux/Gem va'da qilgan odamni ko'rgan?" deb savol berish. | Qo'l ko'tarishadi, o'z hayotlaridagi shubhali xabarlarni aytishadi. |
| **03:00 – 11:00** | Nazariya va Jonli Demo | 1–5-slaydlar: Ijtimoiy muhandislik nima? 4 ta asosiy qopqon (Shoshiltirish, Qo'rquv, Ochko'zlik, Niqob). Ekranda Studio namoyishi. | Ekranga diqqat qilishadi, varaqadagi 1-vazifani (atamalarni ulash) to'ldirishadi. |
| **11:00 – 30:00** | Amaliy Laboratoriya (Studio) | Studio ochiladi (`index.html`). O'quvchilar 6 ta firibgar chatini tekshiradi, qizil bayroqlarni belgilaydi. | Har bir o'quvchi chatlarni tahlil qilib, 100% detektiv balliga erishadi. |
| **30:00 – 36:00** | O'zaro Ko'rik va Tahlil | 2 ta eng hiylakor chatni sinfda birga muhokama qilish: "Nega do'stingning nomidan yozilgan xabar xavfli bo'lishi mumkin?" | O'z fikrlarini bildirishadi, "Akkaunt o'g'irlangan bo'lishi mumkin" xulosasiga kelishadi. |
| **36:00 – 40:00** | Xulosa va 10 Ballik Baholash | 5 ta Oltin Qoida eslatmasini yakunlash, varaqalarni baholash va keyingi 21-dars (Raqamli Iz) bilan bog'lash. | Ish varaqasini topshirishadi, uy vazifasini belgilab olishadi. |

---

## 4. O'qituvchi Uchun Jonli Dialog Ssenariysi (O'zbek va Rus tillarida)

### Boshlash (Qiziqtirish):
* **UZ:** "Tasavvur qiling, uyingizda dunyodagi eng qalin po'lat eshik va 10 ta kodli qulf bor. O'g'ri eshikni buzib kira olmaydi. Lekin agar u eshikni taqillatib, 'Salom, men xolangizman, eshikni oching, sizga sovg'a olib keldim' desa-chi? Siz o'z qo'lingiz bilan eshikni ochasiz. Kiber-firibgarlar aynan shunday ishlaydi: ular kompyuterni emas, sizning ishonchingizni buzadi! Bugun biz kiber-detektivlarga aylanamiz."
* **RU:** "Представьте, что у вас дома самая бронированная стальная дверь с 10 сложными замками. Вор не может её взломать. Но если он постучит и ласковым голосом скажет: «Привет, я друг твоей мамы, открой дверь, я принёс подарок!» — вы сами повернёте ключ. Социальная инженерия взламывает не пароли, а доверие человека! Сегодня мы станем кибер-детективами."

---

## 5. Baholash Mezoni (10 Ballik Standart Rubrika)

1. **Nazariy Tushunchalar (2 ball):** Ijtimoiy muhandislikning 4 ta tuzog'ini (Shoshiltirish, Qo'rqitish, Tekin pishloq, Niqob) to'g'ri ajrata olish.
2. **Kiber-Detektivlik Tahlili (4 ball):** Studiodagi 6 ta chat ssenariysidan kamida 5 tasini to'g'ri fosh etish va qizil bayroqlarni aniqlash.
3. **Kiber-Qalqon 5 Oltin Qoidasi (3 ball):** Varaqadagi 5 ta xavfsizlik qoidasini mustaqil tahlil qilib to'g'ri xulosalarni shakllantirish.
4. **Intizom va Himoya (1 ball):** Laboratoriya ishini o'z vaqtida yakunlab, o'zgalar ma'lumotlariga hurmat bilan yondashish.
