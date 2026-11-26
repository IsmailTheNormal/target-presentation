# O'qituvchi Qo'llanmasi (Teacher Reading)
## 5–6-sinf · 12-hafta · 31-dars
### Mavzu: Xabarlar va Hodisalar (Broadcast Messages): Qahramonlar Muloqoti va Sehrli Kalit
**Dars formati:** Juftlik Dars (Double Block — 80 daqiqa / 2-soatlik dars)

---

### 1. Darsning Pedagogik Maqsadi va Metodikasi
O'tgan 30-darsda o'quvchilar bitta sprayt ichida o'zgaruvchilarni (tangalar, jonlar, taymer) boshqarishni o'rgandilar.
Bugungi 31-darsning asosiy maqsadi — bir nechta mustaqil spraytlarni yagona tizimga birlashtirishdir.
Scratch-dagi **Broadcast Messages** (Xabarlar) mexanizmi event-driven arxitekturaning (Publish-Subscribe Pattern) bolalar uchun eng sodda va kuchli namunasidir.

---

### 2. Darsning 80 Daqiqalik Aniq Xronometraji

#### 1-BOSQICH (40 daqiqa) — Tushuntirish, Sxema va Viktorina
- **00:00–04:00 (4 min):** Kirish, dars mavzusi va maqsadlarini e'lon qilish.
- **04:00–12:00 (8 min):** 30-dars uy vazifasi tahlili: tangaga tekkanda ball to'xtovsiz oshib ketishi xatosi, 'yashirinish'ning zarurligi va 30 sek blitz savol.
- **12:00–18:00 (6 min):** Broadcast nima? Maktab qo'ng'irog'i metaforasi: bitta signal butun o'yinga eshittiriladi.
- **18:00–24:00 (6 min):** Ikkita sariq blok: `[xabarni tarqatish]` (Sender) va `[men xabarni olganda]` (Receiver).
- **24:00–30:00 (6 min):** Signallar arxitekturasi: Kalit olinganda Darvoza ochilishi va sahna musiqasining yangrashi.
- **30:00–35:00 (5 min):** Katta xato: Xabarni `doim takrorlash` ichiga qo'yish o'yinni qotirishi (Spam qopqoni).
- **35:00–40:00 (5 min):** Dialoglar: `[xabarni tarqatish va kutish]` bloki.

#### 2-BOSQICH (40 daqiqa) — Amaliyot, Playtest va Baholash
- **40:00–45:00 (5 min):** 3 ta bosh signal: `StartGame`, `GameOver` va `Victory`.
- **45:00–50:00 (5 min):** Interaktiv Quiz: 4 ta tezkor savol bilan tushunchalarni mustahkamlash.
- **50:00–55:00 (5 min):** Sahna (Backdrop) ning xabarlarga javob qaytarishi.
- **55:00–65:00 (10 min):** Amaliy kiber-kvest: Ritsar, Kalit, Darvoza va Xazina qutisini kodlash.
- **65:00–72:00 (7 min):** Juftlikda Playtest: partadoshining o'yinini sinab ko'rish.
- **72:00–76:00 (4 min):** 2 nafar o'quvchining Smartboardda jonli demosi.
- **76:00–80:00 (4 min):** Dars xulosasi va 3 darajali uy vazifasi (vazifa.html).

---

### 3. O'qituvchi Uchun Chuqur Texnik Savollar va Javoblar

1. **Savol:** Bitta xabar yuborilganda uni bir vaqtda nechta sprayt eshita oladi?
   - **Javob:** Cheksiz miqdorda! Shu xabarni kutuvchi (`men [xabar] olganda`) barcha spraytlar bir soniyada bir vaqtda ishga tushadi.
2. **Savol:** Nega xabar yuborilgandan so'ng kalitni darhol yashirish (`yashirinish`) kerak?
   - **Javob:** Agar yashirilmasa, qahramon kalit ustida turgan har bir soniyada yangidan xabar tarqalaveradi va bu o'yinni qotirib qo'yadi.
3. **Savol:** Sahna (Backdrop) qanday qilib xabarni eshitadi?
   - **Javob:** Sahna ham xuddi spraytlar kabi o'z skript maydoniga ega va unda ham `men [xabar] olganda` blokini qo'yib, fonni o'zgartirish mumkin.
