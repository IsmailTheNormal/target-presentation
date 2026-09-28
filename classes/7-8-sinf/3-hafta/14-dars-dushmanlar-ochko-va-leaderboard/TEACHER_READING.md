# 14-Dars: O'qituvchi Uchun Tayyorgarlik Qo'llanmasi (Teacher Prep Guide)
**Target International School // 7–8-Sinflar // 3-Hafta (2-Soat: 40 daqiqa)**
**Mavzu:** Dushmanlar, Ochko va Leaderboard — JSON, Sort va Halollik

> **METODIK ESLATMA:** Bu juft darsning **ikkinchi** soati. 13-darsda o'quvchilar
> dvigatel qurdi (tsikl, delta time, fizika, AABB). Bugun ular ustiga o'yin dizayni
> va ma'lumotlar bilan ishlash qo'shiladi. Darsning cho'qqisi — **halollik**:
> mijoz tomonidan kelgan ochkoga ishonib bo'lmasligi. Bu shunchaki o'yin mavzusi
> emas, bu **kiberxavfsizlikning asosiy tamoyili**.

---

## 1. Darsda Qaysi Vositalar Ishlatiladi?

1. **Laboratoriya stendi (Google Chrome):**
   * Fayl: `classes/7-8-sinf/3-hafta/14-dars-dushmanlar-ochko-va-leaderboard/lab/index.html`
   * To'liq o'ynaladigan arkada: qahramon yuguradi, sakraydi va dushmanning
     **boshiga sakrab** ularni yo'q qiladi. Yonidan tegsa — jon ketadi.
   * O'ng panelda: ism kiritish, **jonli reyting jadvali**, va halollik tajribasi
     uchun uchta tugma.
2. **Prezentatsiya:** `prezentatsiya.html` — 12 slayd, `N` — o'qituvchi izohlari.
3. **Varaqa:** `varaqa.html` — 1 varaq A4.
4. **Chrome DevTools (F12)** — 8-slayddagi jonli demo uchun.

**Internet talab qilinmaydi.** Reyting jadvali `localStorage` da saqlanadi,
ya'ni **har noutbukda o'ziniki**. Sinf umumiy jadvali uchun 6-bo'limga qarang.

---

## 2. Darsning Texnik Mazmuni

### A. O'yin Dizayni: Maqsad, Xavf, Natija
Dvigatel — bu hali o'yin emas. O'yin bo'lishi uchun uchta narsa kerak:
**maqsad** (ochko), **xavf** (yutqazish mumkinligi) va **natija** (taqqoslanadigan raqam).

### B. Kombo Mexanikasi
```js
kombo++;  ochko += 10 * kombo;   // ketma-ket urish
if (jarohat) kombo = 0;          // uzilish
```
5 ta ketma-ket: `10+20+30+40+50 = 150`. 5 ta uzilib: `10×5 = 50`.
**Uch baravar farq** — shuning uchun o'yinchi tavakkal qilishni tanlaydi.
Bitta qator kod butun xulq-atvorni o'zgartiradi.

### C. Holat Mashinasi
`MENU → PLAYING → GAME OVER`. Muhim detal — `update` ichidagi **erta chiqish**:
```js
if (state !== 'PLAYING') return;
```
Busiz GAME OVER ekranida dushmanlar harakatda qolib, ochko o'sishda davom etadi.
Bu real xato, va bolalar uni o'z o'yinlarida albatta uchratadi.

### D. JSON: `stringify` va `parse`
`localStorage` faqat **matn** saqlaydi. Eng ko'p uchraydigan xato:
```js
// ❌ parse ni unutish
var top = localStorage.getItem('top');
top.push(yangi);    // XATO: matnga push qilib bo'lmaydi
```

### E. `sort()` Tuzog'i — Doskada Ko'rsating
```js
[100, 9, 80].sort()              // [100, 80, 9]  ← MATN kabi saralaydi!
[100, 9, 80].sort((a,b) => b-a)  // [100, 80, 9]  ← to'g'ri, son kabi
```
Bu misolda natija **tasodifan bir xil** chiqadi — lekin sabab butunlay boshqa.
`[100, 9, 80].sort()` da `9` oxirida qoladi, chunki matn sifatida `"9" > "80"`.
Bolalarga `[5, 40, 300].sort()` ni ham ko'rsating → `[300, 40, 5]`. Mana shu yerda
xato yaqqol ko'rinadi.

### F. Halollik — Darsning Asosiy G'oyasi
Brauzerdagi butun kod **o'yinchi kompyuterida** ishlaydi. Demak o'yinchi:
* `localStorage` ni istalgancha o'zgartira oladi,
* JS o'zgaruvchilarini Console orqali qayta yoza oladi,
* kodning o'zini tahrirlay oladi.

`localStorage` — **himoya emas**, u parol bilan yopilmagan oddiy qulaylik.

**Uchta real himoya usuli:**
1. **Server hisoblaydi** — mijoz faqat harakatlarni yuboradi. Eng ishonchli.
2. **Replay tekshiruvi** — barcha tugma bosishlari saqlanadi, server qayta o'ynaydi.
3. **Mantiqiy tekshiruv (sanity check)** — "1 soniyada 999999 ochko olish mumkin emas".

Stenddagi `🛡 TEKSHIRISH` tugmasi uchinchi usulni amalga oshiradi. **Muhim:**
u saxiy — chegara ataylab yuqori qo'yilgan, chunki **haqiqiy o'yinchini xato bilan
jazolash — soxta natijani o'tkazib yuborishdan yomonroq**. Bu ham muhandislik qarori,
bolalarga shuni ayting.

---

## 3. 40 Daqiqalik Darsning Rejasi

### 00:00 – 07:00 | Dvigatel ≠ O'yin (1–2-slayd)
* **O'qituvchi nima deydi:**
  > *"В прошлый час вы построили движок. Но движок — это ещё не игра. Чтобы
  > получилась игра, нужны три вещи: **цель**, **риск** и **результат**."*
* **Savol sinfga:** *"Почему игра, в которой невозможно проиграть, быстро надоедает?"*
  (Javob: g'alaba qiymatini yo'qotadi.)

### 07:00 – 11:00 | Ochko va Kombo (3-slayd)
* Asosiy fikr: **ochko — mukofot emas, xabar.** U o'yinchiga qaysi harakat
  foydali ekanini aytadi.
* Doskada kombo arifmetikasini yozing: `150` va `50`. Uch baravar farq.
  > *"Одна строка кода — и игрок из осторожного превращается в рискующего."*

### 11:00 – 15:00 | To'lqinlar (4-slayd)
* Qiyinlikni oshirishning uch yo'li. **Eng yomonini alohida ta'kidlang:**
  > *"Худший способ — дать врагу много здоровья. Это не сложно, это просто долго
  > и скучно. Вы наверняка встречали такие игры."*
* Stendda to'lqin raqamini ko'rsating — u har 15 soniyada oshadi.

### 15:00 – 18:00 | Holat Mashinasi (5-slayd)
* Uchta ekran: MENU, PLAYING, GAME OVER.
* Kod blokidagi `return` ni ko'rsating va ayting: busiz GAME OVER ekranida
  dushmanlar yuraverdi.

### 18:00 – 23:00 | JSON (6-slayd)
* `stringify` / `parse`.
* **Jonli demo:** F12 → Console da yozing:
  ```js
  localStorage.getItem('vc-lb-7-14')
  ```
  Ekranda matn chiqadi. Keyin:
  ```js
  JSON.parse(localStorage.getItem('vc-lb-7-14'))
  ```
  Endi massiv chiqadi. Farqni ko'rsating.

### 23:00 – 27:00 | Leaderboard va `sort` (7-slayd)
* Uchta amal: `push` → `sort` → `slice(0,10)`.
* **🛑 Doskada albatta yozing:**
  ```
  [5, 40, 300].sort()   →  [300, 40, 5]
  ```
  Bolalar hayratlanadi. Sabab: sonlar matn sifatida taqqoslanadi.

### 27:00 – 33:00 | ⭐ HALOLLIK — DARSNING CHO'QQISI (8-slayd)

**Jonli demo proyektorda (bu darsning eng kuchli lahzasi):**
1. Stendda bir marta o'ynang, kichik natija qo'ying — jadvalda ko'rinsin.
2. F12 → Console oching va bitta qator yozing:
   ```js
   localStorage.setItem('vc-lb-7-14',
     JSON.stringify([{ism:'Men', ochko:999999, tolqin:1, dur:1, ts:Date.now()}]));
   ```
3. Sahifani yangilang. **Siz birinchi o'rindasiz.**
   > *"Я не взломал сервер. Я не использовал никаких секретов. Я просто открыл
   > вкладку, которая есть у каждого из вас. Вот почему настоящие игры никогда
   > не доверяют очкам от игрока."*
4. Keyin uchta himoya usulini ayting.

**Muhim pedagogik eslatma:** bu bolalarni aldashga o'rgatish emas — bu ularni
**himoyalanishga** o'rgatish. Shuni ochiq ayting:
> *"Теперь вы знаете, как это ломается. Значит, вы сможете построить так,
> чтобы не сломалось."*

### 33:00 – 45:00 | Turnir (12 daqiqa)

| Vaqt | Bosqich | Natija |
|---|---|---|
| 1 daq | **Ism** va 2 ta mashq o'yin | Boshqaruvni his qilish |
| 5 daq | **Rekord** — eng yaxshi natija | Ochko, to'lqin, maks kombo |
| 3 daq | **Tahlil** — jadvaldagi o'rin | O'rin va 1-o'rindan farq |
| 3 daq | **Cheat sinovi** — `💀 CHEAT` → `🛡 TEKSHIRISH` | O'chirilgan soxta natijalar soni |

**Siz nima qilasiz:** sinf bo'ylab yuring. Cheat bosqichini **tashlab ketmang** —
bu darsning eng qimmatli qismi.

### 45:00 – 48:00 | Yakun va Chempionlar
* Proyektorda stendni oching, `🛡 TEKSHIRISH` ni bosing — soxta natijalar
  o'chirilishini ko'rsating.
* Birinchi uch o'rinni e'lon qiling.
* Varaqalarni yig'ing.

---

## 4. Stend Boshqaruvi (Shpargalka)

| Element | Vazifasi |
|---|---|
| Ism maydoni + `▶ O'YINNI BOSHLASH` | MENU dan PLAYING ga o'tish (`Enter` ham ishlaydi) |
| `A` / `D`, `Space` | Harakat va sakrash |
| **Dushman boshiga sakrash** | Ochko: `10 × kombo` |
| **Yonidan tegish** | −1 jon, kombo nolga tushadi, 1.2 s himoya |
| `Space` (GAME OVER da) | Qaytadan boshlash |
| `💀 CHEAT` | Jadvalga soxta rekord qo'shadi (999 999 / 1 sek) |
| `🛡 TEKSHIRISH` | Mantiqiy tekshiruv: imkonsiz natijalarni topadi va o'chiradi |
| `🗑 Jadvalni tozalash` | Reyting jadvalini butunlay bo'shatish |

**Jadval ranglari:** yashil qator — sizning oxirgi natijangiz;
qizil chizilgan qator — tekshiruv soxta deb topgan natija.

---

## 5. Ko'p Beriladigan Savollar

**"Dushmanni qanday o'ldiraman?"**
Faqat **yuqoridan** — sakrab boshiga tushish kerak. Yonidan tegish jarohat beradi.
Bu Mario mexanikasi.

**"Jadvalda faqat mening natijalarim bor."**
To'g'ri: `localStorage` **har brauzerda alohida**. Sinf umumiy jadvali uchun
6-bo'limga qarang.

**"Tekshirish mening halol natijamni o'chirib yubordi."**
Deyarli bo'lmaydi — chegara juda saxiy (30 soniyada ~31 000 ochko). Agar shunday
bo'lsa, bu ham dars: **soxta ijobiy natija** (false positive) muammosi.

**"Cheat tugmasi ishlatish — bu yomonmi?"**
Yo'q. Bu boshqarilayotgan tajriba, xuddi kimyodagi xavfsiz reaksiya kabi.
Maqsad — zaiflikni **tushunish**, undan foydalanish emas.

---

## 6. Sinf Umumiy Jadvalini Qanday Tuzish (Ixtiyoriy)

`localStorage` har noutbukda alohida, shuning uchun sinf chempionini aniqlashning
eng oddiy yo'li — **qo'lda**:

1. Har bir o'quvchi o'z eng yaxshi natijasini varaqaga yozadi (bu baribir uy
   vazifasining bir qismi).
2. Siz doskada ustun chizasiz va raqamlarni yozasiz.
3. Doskada birgalikda **saralaysiz** — bu `sort()` ni jonli mashq qilish imkoni:
   > *"Как мы сейчас отсортировали? По убыванию. Ровно это делает
   > b.ochko - a.ochko."*

Bu usul texnik jihatdan soddaroq va pedagogik jihatdan **yaxshiroq** —
bolalar saralashni o'z qo'li bilan bajaradi.

---

## 7. Uy Vazifasi va 10 Ballik Mezon

| Mezon | Ball |
|---|---|
| Turnir natijalari jadvali (ochko, to'lqin, o'rin, cheat sinovi) | 3 |
| JSON izohi **misol bilan** | 3 |
| Cheat sinovi tavsifi | 2 |
| Himoyaning 2 ta usuli | 2 |
| **JAMI** | **10** |

**Baholashda:**
* JSON izohi uchun **misol majburiy**. "Obyektni matnga aylantiradi" — 1 ball.
  Misol bilan (`{ism:'Aziz'}` → `'{"ism":"Aziz"}'`) — 3 ball.
* Himoya usullari uchun darsda aytilgan uchtadan **ikkitasi** yetarli.
  O'z varianti (masalan, "vaqtni ham saqlab, tezlikni tekshirish") — to'liq ball
  va alohida maqtov.

---

## 8. Ikki Darsning Yakuniy Natijasi

13 va 14-darsdan keyin o'quvchi quyidagilarni **o'lchagan va qurgan** holda biladi:
Canvas, o'yin tsikli, delta time, AABB, ochko va kombo dizayni, holat mashinasi,
JSON, `sort`, va mijoz ma'lumotiga ishonmaslik tamoyili.

Keyingi hafta (15–16-darslar) shu bilimlar ustiga o'z arkadasini to'liq yig'ish
va uni internetga chiqarish rejalashtirilgan.
