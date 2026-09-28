# 16-Dars: O'qituvchi Uchun Maxsus Qo'llanma (Teacher Prep Guide)
**Target International School // 5–6-Sinflar (10–12 yosh) // 4-Hafta (2-Soat: 40 daqiqa)**
**Mavzu:** O'z Levelingni Qur — Redaktor, Level Kodi va Ulashish

> **ESLATMA:** Bu 4-haftaning **ikkinchi** soati. Birinchi soatda (15-dars) bolalar
> dushman AI ni sozlagan edi. Endi ular o'sha dushmanni **o'zlari qurgan** maydonga
> qo'yadi. Kod yozish talab qilinmaydi — hammasi sichqoncha bilan.

---

## 1. Darsda Qaysi Dastur Ishlatiladi?

1. **Level redaktori (Google Chrome):**
   * Fayl: `classes/5-6-sinf/4-hafta/16-dars-level-redaktor-va-ulashish/editor/index.html`
   * Ochilganda ekranda **tayyor namuna level** turadi — bo'sh ekran emas. Bu ataylab:
     bolalar darhol `▶ O'YNASH` ni bosib, nima qurishlari kerakligini ko'radi.
   * Chapda — panjara (20 × 10 = 200 katak), o'ngda — 6 ta bo'yoq, level kodi va
     tekshiruv paneli.
2. **Prezentatsiya:** `prezentatsiya.html` — 12 slayd, `N` — o'qituvchi izohlari.
3. **Varaqa:** `varaqa.html` — 1 varaq A4. **Muhim:** varaqada level kodi uchun maxsus
   qizil ramka bor. Kodsiz uy vazifasi 3 balldan mahrum bo'ladi.

**Internet talab qilinmaydi.**

---

## 2. Bu Dars Nimani O'rgatadi

Bolalar "level quradi". Aslida ular to'rtta jiddiy tushunchani o'zlashtiradi:

| O'yindagi nom | Haqiqiy tushuncha |
|---|---|
| Panjara va kataklardagi raqamlar | **Ikki o'lchovli massiv** (2D array) |
| Jadvalni matnga aylantirish | **Serializatsiya** |
| `0000000` → `7a` | **Siqish** (RLE compression) |
| "O'tish yo'li bormi?" tekshiruvi | **Graf bo'yicha qidiruv** (BFS) |

Yakuniy o'lchanadigan natija: o'quvchida **o'z levelining kodi** qoladi — uni
istalgan kompyuterda ochish mumkin. Bu darsdagi eng qimmatli narsa.

---

## 3. 40 Daqiqalik Darsning Bosqichma-Bosqich Rejasi

### 00:00 – 03:00 | Rol Almashadi
* **1–2-slayd.**
* **O'qituvchi nima deydi:**
  > *"Ребята, первый час вы настраивали врага. А теперь самое интересное: сегодня
  > вы **не играете**. Сегодня вы — строители. Каждый из вас построит свою
  > площадку, и в конце урока вы поменяетесь ими с соседом."*
* **Kuchli motivatsiya (albatta ayting):**
  > *"Кто построил большинство игр в Roblox? Не взрослые программисты. **Дети.**
  > Они начинали ровно так же, как вы сегодня."*

### 03:00 – 10:00 | Panjara: Kompyuter Levelni Qanday Ko'radi
* **3-slayd.** Asosiy g'oya: kompyuter uchun level — bu **raqamlar jadvali**.
* Proyektorda redaktorni oching va bir nechta katakni bo'yang. O'ngdagi
  **level kodi** real vaqtda o'zgarishini ko'rsating.
  > *"Смотрите на код справа. Я нажимаю одну клетку — и код меняется. Уровень для
  > компьютера это не картинка, это числа."*

### 10:00 – 14:00 | Beshta Bo'yoq
* **4-slayd.** Har bir bo'yoqni redaktorda bosib ko'rsating.
* **🛑 Eng muhim ogohlantirish (buni aytmasangiz yarim sinf xato qiladi):**
  > *"Не ставьте много шипов! 50 шипов — это **не сложно**, это раздражает.
  > 8–12 шипов на весь уровень — более чем достаточно."*
* Start va Finish **bittadan** bo'lishini ayting. Redaktor buni o'zi nazorat
  qiladi: yangi Start qo'ysangiz, eskisi avtomatik o'chadi.

### 14:00 – 18:00 | Level Kodi (SEHRLI LAHZA)
* **5-slayd.** Bu darsning eng yorqin nuqtasi.
* **Proyektorda ko'rsating:**
  1. `📋 Kodni ko'chirish` ni bosing.
  2. `🗑 Tozalash` ni bosing — maydon bo'shab qoladi, bolalar "voy!" deydi.
  3. Kodni `📥 Yuklash` katagiga qo'ying va bosing — **level qaytib keladi**.
  > *"Вся площадка — 200 клеток — поместилась вот в эту короткую строчку.
  > Именно так ваш телефон отправляет фотографии в интернет: превращает картинку
  > в текст и сжимает повторы."*
* Slaydda `0000000` → `7a` misoli bor. Doskada bir marta yozib ko'rsating.

### 18:00 – 23:00 | Uchta Dizayn Qoidasi
* **6-slayd.**
  1. **Boshlanish xavfsiz** — start atrofida 3 katak bo'sh.
  2. **Qiyinlik asta oshadi** — chapda oson, o'ngda qiyin.
  3. **Har doim yo'l bor** — qahramon 3 katak balandlikka sakraydi.
* **Doskada chizing:** yomon start (tikan yonida) va yaxshi start (bo'sh joyda).
* `🔎 Tekshirish` tugmasini ko'rsating. Ataylab buzuq level yarating
  (finishni devor bilan to'sing) va qizil xabar chiqishini ko'rsating.

### 23:00 – 26:00 | Sinov (Playtesting)
* **7-slayd.** Kalit fikr:
  > *"Вы **знаете** свой уровень наизусть, поэтому он кажется вам лёгким.
  > А сосед видит его в первый раз!"*
* **Doskaga yozib qo'ying: «3–5 попыток».** Bu dars davomida ko'rinib tursin.
  * O'ta olmadi → juda qiyin, tuzating.
  * Birinchi urinishda o'tdi → juda oson, to'siq qo'shing.

### 26:00 – 38:00 | Amaliyot: Level Qurish (12 daqiqa)

**Doskaga to'rt bosqichni vaqti bilan yozib qo'ying va har bosqich oxirida
vaqtni ovoz chiqarib e'lon qiling.** Bu darsning muvaffaqiyati shu tartibga bog'liq.

| Vaqt | Bosqich | Nima qilinadi |
|---|---|---|
| 3 daq | **Skelet** | 🚩 Start chapga, 🏁 Finish o'ngga, pastki qator 🟦 platforma |
| 4 daq | **Qiyinlik** | 8–12 🔺 tikan, 1–3 🤖 dushman, chapdan o'ngga qiyinlashtirish |
| 2 daq | **Tekshirish** | `🔎 Tekshirish` — qizil xabar qolmasin. Keyin `▶ O'ynash` |
| 3 daq | **Almashish** | `📋 Kodni ko'chirish` → varaqaga yozish → qo'shniga berish |

**Siz nima qilasiz:** sinf bo'ylab yuring. Ikki tipik muammo:
* *"У меня не проходится!"* → `🔎 Tekshirish` ni bosishni aytng, xabarni birga o'qing.
* *"Я всё закрасил шипами"* → `🗑 Tozalash` va `🎲 Namuna` dan qayta boshlash.

**Agar vaqt yetmasa:** almashish bosqichini qisqartiring, lekin **kodni varaqaga
yozishni tashlab ketmang** — bu uy vazifasining asosi.

### 38:00 – 40:00 | Yakun
* **8–12-slaydlar** qisqacha. Varaqalarni yig'ing.
* **Har bir varaqada level kodi yozilganini tekshiring.** Bu 30 soniya oladi va
  uy vazifasini baholashni ancha osonlashtiradi.

---

## 4. Redaktor Boshqaruvi (Shpargalka)

| Element | Vazifasi |
|---|---|
| Sichqoncha chap tugmasi | Bosib turib **chizish** (drag bilan bir nechta katak) |
| `▶ O'YNASH` / `✏️ REDAKTOR` | Rejimni almashtirish |
| `Esc` | O'yindan redaktorga qaytish |
| `A` / `D`, `Space` | O'yin rejimida harakat va sakrash |
| `🔎 TEKSHIRISH` | Start, finish, yo'l va tikan sonini tekshirish |
| `🗑 TOZALASH` | Butun maydonni bo'shatish |
| `📋 Kodni ko'chirish` | Level kodini buferga olish |
| `📥 Yuklash` | Boshqaning kodini ochish |
| `🎲 Namuna` | Tayyor namuna levelni qaytarish |

**Bo'yoqlar:** ⬜ 0 bo'shliq · 🟦 1 platforma · 🔺 2 tikan · 🤖 3 dushman ·
🏁 4 finish · 🚩 5 start.

---

## 5. Tekshiruv Paneli Nima Deydi

| Xabar rangi | Ma'nosi | Nima qilish kerak |
|---|---|---|
| 🔴 **Qizil** | Level **ishlamaydi** | Tuzatish shart, o'ynab bo'lmaydi |
| 🟡 **Sariq** | Dizayn maslahati | Tuzatish tavsiya etiladi, lekin majburiy emas |
| 🟢 **Yashil** | Hammasi joyida | `▶ O'ynash` ga o'ting |

Qizil xabarlar: start yo'q, finish yo'q, ikkitadan ko'p, platforma yo'q,
**yo'l yo'q**. Sariq xabarlar: start yonida tikan, tikan ko'p (>14),
dushman ko'p (>3).

> **Diqqat:** "yo'l bor" tekshiruvi biroz **saxiy** — u qahramon 3 katak
> sakrashini hisobga oladi, lekin dushmanlarni hisobga olmaydi. Shuning uchun
> haqiqiy sinov — `▶ O'ynash` tugmasi. Bolalarga shuni aytib qo'ying:
> *"Зелёная галочка — это ещё не победа. Настоящая проверка — сыграть самому."*

---

## 6. Ko'p Beriladigan Savollar

**"Kodni yuklaganda 'kod to'g'ri emas' deyapti."**
Kod **to'liq** ko'chirilmagan. Kod 200 katakni tasvirlaydi — bitta belgi
yetishmasa ham ishlamaydi. Qo'lda ko'chirganda xato bo'lishi tabiiy;
`📋 Kodni ko'chirish` tugmasidan foydalanish ishonchliroq.

**"Nega qahramon devordan o'tib ketdi?"**
O'tmaydi. Lekin juda tor joyda (1 katak) sakrasa, u shiftga urilib qolishi mumkin —
bu haqiqiy o'yinlarda ham bor. Bolalarga 2 katak keng yo'l qoldirishni ayting.

**"Dushman platformadan tushib ketmayapti."**
To'g'ri — dushman patrulda **o'z platformasidan chiqmaydi** (chekkaga yetganda
buriladi). Lekin ta'qibga o'tganda tushishi mumkin. Bu ataylab shunday.

**"Men 200 ta katakni ham tikan qildim."**
`🗑 Tozalash` va qaytadan. Bu xato emas — bu tajriba. Lekin `🔎 Tekshirish`
darhol sariq ogohlantirish beradi.

---

## 7. Uy Vazifasi va 10 Ballik Mezon

| Mezon | Ball |
|---|---|
| Level kodi to'liq ko'chirilgan | 3 |
| Levelning nomi va 3 ta to'siq tavsifi | 2 |
| Sinov natijasi (o'zi va qo'shnisi necha urinishda o'tgani) | 2 |
| Qo'shniga berilgan 2 ta **aniq** fikr | 2 |
| Ozodalik va tartib | 1 |
| **JAMI** | **10** |

**Baholashda eng muhimi — fikr-mulohaza (2 ball).**
* "Zo'r" / "Yomon" → **0 ball**. Bu fikr emas.
* "Bu yerda tikan ko'p" → **1 ball**. Joy aniq emas.
* "O'rtadagi ikkita tikan orasida sakrash juda tor, bittasini olib tashla"
  → **2 ball**. Aniq joy + aniq taklif.

Bu mezonni bolalarga **oldindan** ayting — shunda ular aniq yozishga harakat qiladi.

---

## 8. Kelasi Hafta

5-hafta 17–18-darslar: bolalar bir nechta leveldan **to'liq o'yin** yig'adi —
levellar ketma-ketligi, umumiy ochko va yakuniy g'alaba ekrani.
