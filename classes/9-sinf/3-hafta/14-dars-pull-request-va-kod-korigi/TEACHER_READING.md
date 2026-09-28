# 14-Dars: O'qituvchi Uchun Tayyorgarlik Qo'llanmasi (Teacher Prep Guide)
**Target International School // 9-Sinf (Junior Vibecoder) // 3-Hafta (2-Soat: 40–50 daqiqa)**
**Mavzu:** Pull Request va Kod Ko'rigi — Diff, Izoh va Qaror

> **METODIK ESLATMA:** Bu juft darsning **ikkinchi** soati. 13-darsda o'quvchilar
> branch va merge ni o'rgandi. Endi savol: **kod `main` ga qanday tushadi?**
> Darsning cho'qqisi — stenddagi **to'rtinchi xato**: uni AI reviewer topa olmaydi,
> chunki u biznes mantiqiga tegishli. Bu darsning butun ma'nosi shu yerda.

---

## 1. Darsda Qaysi Vositalar Ishlatiladi?

1. **Kod ko'rigi stendi (Google Chrome):**
   * Fayl: `classes/9-sinf/3-hafta/14-dars-pull-request-va-kod-korigi/lab/index.html`
   * Ekranda haqiqiy GitHub PR ga o'xshash sahifa: sarlavha, tavsif, diff.
   * O'quvchi **istalgan qatorni bosib** izoh qoldiradi va uni
     `blocking` / `savol` / `nit` deb belgilaydi.
   * Oxirida uchta qarordan birini tanlaydi — stend **qaror izohlarga mos
     kelishini** tekshiradi.
   * `🤖 AI reviewer` tugmasi — AI ko'rigini ishga tushiradi va farqni ko'rsatadi.
2. **Prezentatsiya:** `prezentatsiya.html` — 12 slayd, `N` — o'qituvchi izohlari.
3. **Varaqa:** `varaqa.html` — 1 varaq A4.

**Internet talab qilinmaydi.**

---

## 2. 🔑 O'QITUVCHINING MAXFIY KALITI — Stenddagi 4 Xato

> **Bu bo'limni o'quvchilarga ko'rsatmang.** Stend PR: valyuta konverteriga
> komissiya va nol kursdan himoya qo'shish.

### Xato 1 — `3-qator`: kod ichida API kaliti
```js
const API_KEY = "sk_live_9f3a2b8c1d4e77";
```
Kalit brauzer kodida qoladi — saytni ochgan har kim uni ko'radi.
10-darsdagi (`.env` va maxfiy ma'lumotlar) mavzuning davomi.
**Belgi: `blocking`. AI buni topadi.**

### Xato 2 — `8–10-qator`: server javobi tekshirilmaydi
```js
const javob = await fetch(url);
const data = await javob.json();
return data.rate;
```
`javob.ok` tekshirilmagan. API 500 qaytarsa yoki `rate` maydoni bo'lmasa,
`data.rate` → `undefined` bo'ladi va xato **jimgina** tarqaladi.
**Belgi: `blocking`. AI buni topadi.**

### Xato 3 — `13–14-qator`: nol kursdan himoya yo'q
```js
function konvertatsiya(summa, kurs) {
  return summa * kurs;
}
```
PR sarlavhasida "nol kursdan himoya" **va'da qilingan**, lekin kodda yo'q.
`kurs` 0 yoki `undefined` bo'lsa natija `0` yoki `NaN`.
**Belgi: `blocking`. AI buni topadi.**

### ⭐ Xato 4 — `23–24-qator`: BIZNES MANTIQI (AI topa olmaydi)
```js
const natija = konvertatsiya(summa, kurs);
return komissiyaOl(natija);
```
**PR tavsifida buyurtmachi talabi aniq yozilgan:**
> *"Komissiya 2% mijoz **beradigan** summadan ushlanadi — ya'ni **boshlang'ich**
> valyutada, konvertatsiyadan **OLDIN**."*

Kodda esa komissiya **konvertatsiyadan keyin**, boshqa valyutadagi natijadan
ayirilmoqda. **Kod xatosiz ishlaydi, sintaksis toza, test yiqilmaydi — lekin
u noto'g'ri narsani hisoblaydi.**

To'g'ri tartib: `komissiyaOl(summa)` avval, keyin `konvertatsiya`.

**Nega AI topa olmaydi:** AI reviewer faqat **kodni** ko'radi. Talab kodda emas,
**PR tavsifida** yozilgan. Kodni talab bilan solishtirish — insonning ishi.
**Belgi: `blocking`. AI buni topa olmaydi.**

---

## 3. Dars Rejasi

### 00:00 – 07:00 | Xatoning Narxi (1–2-slayd)
* To'rtta ustunni ketma-ket oching va narxlarni **ovoz chiqarib** ayting:
  1 daqiqa → 10 daqiqa → 1 kun → 1 hafta.
* Keyin ayting: kod ko'rigi faqat xato uchun emas — **bilim tarqalishi**,
  **yagona standart**, **mas'uliyatning bo'linishi** uchun ham.

### 07:00 – 11:00 | PR Jarayoni (3-slayd)
* To'qqiz qadam. **Ta'kidlang:** 5 va 6-qadam (ko'rik → tuzatish) bir necha marta
  takrorlanishi mumkin. Bu **normal**, bu muvaffaqiyatsizlik emas. Yosh
  dasturchilar buni shaxsiy tanqid deb qabul qiladi — buni oldindan aytib qo'ying.

### 11:00 – 16:00 | Diff O'qish (4-slayd)
* `-` qizil, `+` yashil, kulrang — kontekst.
* `@@ -14,7 +14,9 @@` qatorini ham tushuntiring — o'quvchilar undan qo'rqadi.
* **Tuzoqni ayting:** diff faqat o'zgargan joyni ko'rsatadi, xato esa ko'pincha
  o'zgarish bilan **qolgan kod o'rtasidagi bog'liqlikda** bo'ladi.

### 16:00 – 20:00 | Yaxshi PR (5-slayd)
* **Asosiy raqam: 50–200 qator.** Doskaga yozib qo'ying.
* **Oltin qoida:** sarlavhada "va" so'zi bo'lsa — PR ni ikkiga bo'lish kerak.

### 20:00 – 25:00 | To'rt Daraja (6-slayd)
* Tartib: **to'g'rimi → xavfsizmi → o'qiladimi → kerakmi**.
* **Muhim:** agar bo'sh joy va nuqta-vergul haqida izohdan boshlasangiz,
  mantiqiy xatoni o'tkazib yuborasiz — diqqat tugaydi.
* Formatlashni odam emas, **Prettier** tekshirsin.

### 25:00 – 31:00 | Izoh Yozish (7-slayd)
* Ikki ustunni solishtiring. **Asosiy gap:** izoh **kodga** yoziladi, odamga emas.
* Uchta belgini doskaga yozing: `nit:` / `savol:` / `blocking:` — ular stendda
  ishlatiladi, shuning uchun bu slaydni tashlab ketmang.

### 31:00 – 34:00 | Uchta Qaror (8-slayd)
* **Oltin qoidani ikki tomonlama ayting:**
  * Sababsiz `Request changes` — jamoadagi ishonchni buzadi.
  * O'qimasdan `Approve` — reviewer qila oladigan eng yomon ish.

### 34:00 – 38:00 | ⭐ AI REVIEWER (9-slayd)
* Ikki ustun: AI nimani topadi va nimani ko'rmaydi.
* **Amaliyotga tayyorlovchi gap (aynan shunday ayting):**
  > *"AI не знает бизнес-логику, потому что он **не видел требований заказчика**.
  > Он читает только код. Сейчас на стенде вы увидите ровно такую ошибку —
  > и это главное задание сегодняшнего урока."*

### 38:00 – 50:00 | Amaliyot: Siz — Reviewer (12 daqiqa)

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 3 daq | **O'qish** | PR tavsifi va diff. **Hech narsa yozilmaydi!** |
| 5 daq | **Xato topish** | Qatorni bosib izoh + belgi |
| 2 daq | **Qaror** | Uchta tugmadan biri |
| 2 daq | **AI bilan solishtirish** | `🤖 AI reviewer` tugmasi |

**🛑 Birinchi 3 daqiqa — eng muhim pedagogik detal.** O'quvchilar darhol yozishni
boshlaydi. To'xtating: *"Три минуты только читаем. Это профессиональная привычка:
сначала понять изменение целиком, потом комментировать."*

**🛑 AI tugmasini erta bosishga yo'l qo'ymang.** Agar o'quvchi avval AI ni ishga
tushirsa, u shunchaki ko'chirib oladi va darsning ma'nosi yo'qoladi.
Stendda bu haqda ogohlantirish bor, lekin siz ham nazorat qiling.

**Siz nima qilasiz:** sinf bo'ylab yuring va bitta savol bering:
*"Ты сравнил код с описанием PR?"* — bu 4-xatoga olib boradigan yagona yo'l.

### 50:00 – 53:00 | Yakun
* Proyektorda stendni oching, to'rtta xatoni birma-bir ko'rsating.
* **4-xatoga alohida to'xtang** — u darsning yakuniy xulosasi:
  > *"Три ошибки нашёл бы и AI. Четвёртую — только человек, который прочитал
  > требование заказчика. Вот за что платят инженерам."*
* Varaqalarni yig'ing.

---

## 4. Stend Boshqaruvi (Shpargalka)

| Element | Vazifasi |
|---|---|
| Diffdagi qatorni bosish | Izoh oynasini ochish |
| `blocking` / `savol` / `nit` | Izoh belgisini tanlash |
| `Yuborish` / `Bekor` | Izohni saqlash yoki bekor qilish |
| Izohdagi `✕` | Izohni o'chirish |
| `✅ Approve` / `💬 Comment` / `🔁 Request changes` | Yakuniy qaror |
| `🤖 AI reviewer` | AI ko'rigi (o'z ko'rigingizdan **keyin**) |
| `↺ Qaytadan` | Hammasini tozalash |

Qarordan keyin qator raqamlari ranglanadi: **yashil** — topilgan xato,
**qizil** — o'tkazib yuborilgan.

**Stend qarorni ham baholaydi:**
* `Approve` + topilmagan xatolar → tanqid;
* `Request changes` + `blocking` izoh yo'q → tanqid (muallif nimani
  tuzatishni bilmaydi);
* `Request changes` + `blocking` bor → to'g'ri qaror.

---

## 5. Ko'p Beriladigan Savollar

**"Men xatoni topdim, lekin stend hisobga olmadi."**
Izoh **o'sha qatorga** qoldirilganini tekshiring. Har xato aniq qatorlarga
bog'langan (masalan, 2-xato — 8, 9 yoki 10-qator).

**"Kod ishlayapti-ku, qanday xato?"**
Bu 4-xatoning aynan mohiyati. Kod **ishlaydi**, lekin **noto'g'ri narsani**
hisoblaydi. PR tavsifini qayta o'qing: komissiya qaysi valyutada olinishi kerak?

**"AI nega buni ko'rmadi?"**
AI faqat kodni o'qidi. Buyurtmachi talabi kodda emas, **tavsifda**. Kodni talab
bilan solishtirish — insonning ishi.

**"Request changes bosish qo'pollik emasmi?"**
Yo'q, agar sabab aniq yozilgan bo'lsa. Qo'pollik — **sababsiz** rad etish yoki
odamga baho berish ("sen bilmaysan"). Kodga izoh — bu normal ish jarayoni.

---

## 6. Uy Vazifasi va 10 Ballik Mezon

| Mezon | Ball |
|---|---|
| 4 ta xato jadvali (qator, muammo, belgi) | 4 |
| AI topa olmagan xato **va nega** | 2 |
| Bitta to'liq izoh (muammo + sabab + taklif) | 2 |
| O'z loyihasi uchun PR tavsifi | 2 |
| **JAMI** | **10** |

**Baholashda eng muhimi — 2-mezon.** Kutilayotgan javob:
> *"AI видит только код, а требование заказчика записано в описании PR.
> Сравнить код с требованием может только человек."*

**To'liq izoh mezoni (2 ball):**
* Faqat muammo ("bu yerda xato") → **0.5 ball**
* Muammo + sabab → **1 ball**
* Muammo + sabab + **taklif** → **2 ball**

Namuna to'liq izoh:
> *"Agar `kurs` nol bo'lsa, bu yer `0` qaytaradi va foydalanuvchi buni to'g'ri
> natija deb qabul qiladi. Bo'lishdan oldin `if (!kurs) return xato;` qo'shsak
> bo'ladimi?"*

---

## 7. Juft Darsning Yakuniy Natijasi

13 va 14-darsdan keyin o'quvchi **butun muhandislik jarayonini** biladi:
branch → commit → konflikt → PR → diff → ko'rik → qaror → CI → merge → deploy.

Bu 9-sinf uchun jiddiy yutuq: ular endi real IT jamoasida nima bo'layotganini
tushunadi va o'z GitHub profilini professional tarzda yuritishi mumkin.

**Keyingi hafta (15–16-darslar):** jamoaviy loyiha — o'quvchilar juftlikda
ishlaydi, bir-biriga PR yuboradi va bir-birining kodini ko'rikdan o'tkazadi.
