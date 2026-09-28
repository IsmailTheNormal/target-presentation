# 15-Dars: O'qituvchi Uchun Maxsus Qo'llanma (Teacher Prep Guide)
**Target International School // 5–6-Sinflar (10–12 yosh) // 4-Hafta (1-Soat: 40 daqiqa)**
**Mavzu:** Dushman AI — Patrul, Ko'rish Radiusi va Ta'qib

> **ESLATMA:** Ushbu qo'llanma geym-developerlik bo'yicha maxsus tayyorgarligi bo'lmagan
> o'qituvchi uchun yozilgan. Darsning har bir daqiqasi, doskada nima ko'rsatish va
> bolalarga rus tilida nima deyish so'zma-so'z berilgan. Kod yozish talab qilinmaydi.

---

## 1. Darsda Qaysi Dastur Ishlatiladi?

1. **O'yin stendi (Google Chrome):**
   * Fayl: `classes/5-6-sinf/4-hafta/15-dars-dushman-ai-va-tagib/game/index.html`
   * Bolalar shu faylni brauzerda ochishadi (yoki VS Code da `Live Server`).
   * Ekranda 2D kiber-maydon: yashil qahramon, qizil dushman va dushmanning
     **sariq ko'rish konusi**.
   * O'ng panelda 4 ta slayder (Dushman tezligi, Ko'rish radiusi, Xotira, Patrul
     kengligi), 3 ta tayyor rejim tugmasi va sekundomer bor.
   * Yuqorida 3 ta tugma: `🧱 DEVOR`, `👁 KONUS`, `↺ QAYTADAN`.
2. **Prezentatsiya:** `prezentatsiya.html` — 12 slayd. `N` tugmasi — o'qituvchi izohlari.
3. **Chop etiladigan varaqa:** `varaqa.html` — 1 varaq A4.

**Internet talab qilinmaydi.** Stend to'liq oflayn ishlaydi.

---

## 2. Bu Dars Nimani O'rgatadi (Pedagogik Maqsad)

Bolalar sirtdan "o'yin dushmanini sozlaydi". Aslida ular uchta jiddiy
informatika tushunchasini o'zlashtiradi:

| O'yindagi nom | Haqiqiy tushuncha |
|---|---|
| 3 ta kayfiyat (patrul / sezdi / ta'qib) | **Holat mashinasi** (state machine) |
| "Yaqinmi?" va "shu tomondami?" | **Shartlar va mantiqiy VA** (`&&`) |
| Devor ko'rishni to'sadi | **Line of Sight** (ko'rish chizig'i) |
| Dushman 3 soniya eslab turadi | **Taymer va holat o'zgaruvchisi** |

Yakuniy o'lchanadigan natija: o'quvchida to'ldirilgan jadval va **uchta
raqam** (tezlik, radius, xotira) qoladi — bu uning shaxsiy dizayn qarori.

---

## 3. 40 Daqiqalik Darsning Bosqichma-Bosqich Rejasi

### 00:00 – 03:00 | Boshlash va Qiziqtirish
* **Proyektorda:** `prezentatsiya.html`, 1–2-slayd.
* **O'qituvchi nima deydi:**
  > *"Ребята, на прошлом уроке мы сделали полосу препятствий: шипы, лазер, три
  > жизни. Но скажите честно — если пробежать её пять раз, станет скучно? Да.
  > Почему? Потому что шип всегда стоит на одном месте. Сегодня мы поставим на
  > трассу того, кто **думает**: он ходит, замечает вас и бежит за вами."*
* **Savol sinfga:** *"В какую игру вы играли сто раз и не надоело? Почему?"*
  (Javoblar deyarli har doim: "потому что каждый раз по-разному").

### 03:00 – 10:00 | Asosiy G'oya: Uchta Kayfiyat
* **3-slayd.** Bu darsning eng muhim slaydi.
* Proyektorda stendni oching va dushmanning boshidagi belgini **jonli** ko'rsating:
  * belgi yo'q → 😴 patrul
  * sariq **❓** → sezdi (dushman to'xtaydi!)
  * qizil **❗** → ta'qib
* **O'qituvchi nima deydi:**
  > *"Смотрите на значок над врагом. Сейчас его нет — враг спокоен. Я подхожу...
  > видите жёлтый вопрос? Он **остановился и думает** полсекунды. А теперь —
  > красный восклицательный знак. Побежал!"*
* **Muhim:** ayting-ki, bu uchta kayfiyat almashuvi — **машина состояний**, va
  xuddi shu narsa svetoforni boshqaradi.

### 10:00 – 13:00 | Qoida 1: Patrul
* **4-slayd.** Kodni o'qishga majburlamang — faqat mantiqni ayting:
  > *"Дошёл до границы — развернулся. Всё. Патруль — это три строчки."*
* Stendda **Patrul kengligi** slayderini tor (60) va keng (700) holatga suring.
  Bolalar dushman "bir joyda tebranishi" va "butun xonani aylanishi"ni ko'radi.

### 13:00 – 20:00 | Qoida 2: Ko'rish Radiusi (ENG YAXSHI QISM)
* **5-slayd.** Ikkita savol: *yaqinmi?* va *shu tomondami?*
* **🎓 Sinfda jonli ko'rgazma (majburiy, 1 daqiqa):**
  1. Bitta o'quvchini doskaga chaqiring, sinfga qarab tursin.
  2. Uning **orqasiga** o'ting va so'rang: *"Ты меня видишь?"* — "Нет".
  3. Old tomoniga o'ting: *"А сейчас?"* — "Да".
  > *"Вот именно так устроен враг в игре. У него **нет глаз на затылке**.
  > Поэтому в играх можно прокрасться сзади!"*
* **6-slayd — devor.** Stendda `🧱 DEVOR` tugmasini yoqing. Ustun ortiga o'ting va
  sariq konus devorda **kesilishini** ko'rsating.
  > *"Если бы враг видел сквозь стену, прятаться было бы бессмысленно, и игра
  > стала бы нечестной."*

### 20:00 – 26:00 | Qoida 3 va 4: Ta'qib va Xotira
* **7-slayd.** Ta'qib — atigi to'rt qator: *"он слева или справа?"*
  > *"Тот сложный «искусственный интеллект», который вы представляли, — это
  > обычное сравнение двух чисел."*
* **8-slayd — xotira.** Uchta variantni solishtiring (0 sek / cheksiz / 3 sek).
  Stendda **Xotira** slayderini 0 → 3 → 10 ga qo'yib sinab ko'rsating.
  * 0 → dushman ahmoq, bir qadam orqaga tisarilsangiz unutadi.
  * 10 → dushman shafqatsiz, dam olishga imkon yo'q.
  * 3 → eng qiziqarli.

### 26:00 – 29:00 | Adolat Qoidalari (Dizayn Darsi)
* **9-slayd.** Bu darsdagi eng muhim **fikrlash** nuqtasi.
* **Jonli sinov:** `🔴 Nohalol` rejim tugmasini bosing va 20 soniya o'ynang.
  Dushman qahramondan tez, radiusi butun ekran, xotirasi 10 soniya.
  * Bolalar darhol norozi bo'ladi: *"так нечестно!"*
* **O'qituvchi nima deydi:**
  > *"Вот! Вы сейчас сами почувствовали главное правило геймдизайна:
  > **сильный враг — это плохой враг**. Хороший враг — честный."*
* Keyin `🟡 Halol` rejimini bosing va farqni his qildiring.

### 29:00 – 40:00 | Amaliyot: 4 Ta Sinov (11 daqiqa)
Bolalar noutbukda `game/index.html` ni ochib, varaqani to'ldirishadi:

| # | Sinov | Nima o'lchanadi |
|---|---|---|
| 1 | **Orqadan o'tish** — dushman teskari qaraganda orqasidan o'tish | Nechanchi urinishda muvaffaqiyat |
| 2 | **Devor ortida** — `🧱 DEVOR` yoqib, ustun ortiga yashirish | Konus kesildimi: HA / YO'Q |
| 3 | **Xotira sinovi** — ta'qibni boshlatib, yashirinish | O'ng paneldagi **sekundomer** raqami |
| 4 | **Adolat sozlamasi** — slayderlarni "qiyin, lekin halol" holatga keltirish | Uchta raqam |

**Siz nima qilasiz:** sinf bo'ylab yuring. Javobni **aytmang** — savol bering:
*"А что будет, если ты подойдёшь сзади?"*, *"Почему конус обрезался?"*

**Agar vaqt yetmasa:** 1, 3 va 4-sinovlar majburiy, 2-sinovni uyga bering.

---

## 4. O'quvchilar AI ga Nima Deb Yozadi

Stendning o'ng pastki burchagida **tayyor prompt** va `📋 Nusxa olish` tugmasi bor
(til almashtirilsa prompt ham almashadi). Bolalar uni `chatgpt.com` yoki
`claude.ai` ga tashlashadi:

> *"У меня 2D-игра на JavaScript. Скорость героя = 4. Враг патрулирует между
> двумя точками, имеет радиус зрения и память 3 секунды. Какие значения скорости
> и радиуса поставить, чтобы было сложно, но честно? Объясни простыми словами,
> я в 6 классе."*

**🛑 Darsdagi eng muhim hayotiy saboq:**
AI bergan raqamni **tekshirmasdan ishlatmaslik**. Bolalar raqamni slayderga
qo'yib, o'zlari o'ynab ko'rishadi. Ko'pincha AI bergan qiymat juda qiyin yoki
juda oson chiqadi — va bolalar buni o'z ko'zi bilan ko'radi.

> *"Искусственный интеллект не может сыграть за вас. Весело или не весело —
> это решает только человек."*

---

## 5. Stenddagi Boshqaruv (Shpargalka)

| Element | Vazifasi |
|---|---|
| `A` / `←` · `D` / `→` | Qahramon harakati (tezlik doimiy = 4) |
| `Space` | Sakrash — devor tepasidan sakrasangiz dushman sizni **yana ko'radi** |
| `R` | O'yinni qaytadan boshlash |
| **Dushman tezligi** | 0.5 – 7.0. Qahramon tezligi 4 — undan yuqorisi adolatsiz |
| **Ko'rish radiusi** | 40 – 600 piksel |
| **Xotira** | 0 – 10 soniya |
| **Patrul kengligi** | 60 – 700 piksel |
| `🟢 Oson` · `🟡 Halol` · `🔴 Nohalol` | Tayyor rejimlar |
| **Sekundomer** | Dushman sizni yo'qotgandan patrulga qaytgunicha o'tgan vaqt |
| **Sezilgan** | Necha marta patruldan ❓ holatiga o'tgani |

Ekrandagi **punktir chiziq va `px` raqami** — qahramon bilan dushman orasidagi
masofa. Bolalarga ayting: *"Компьютер видит вот это число, а не картинку."*

---

## 6. Ko'p Beriladigan Savollar

**"Nega dushman meni devor orqali ko'rdi?"**
Sakrab devor tepasiga chiqqansiz. Devor faqat **yerda turganda** to'sadi —
bu ataylab shunday qilingan, sakrash xavfli bo'lsin deb.

**"Nega dushman meni sezdi, lekin darhol yugurmadi?"**
Bu ❓ holati — 0.5 soniyalik "o'ylash" pauzasi. U ataylab qo'yilgan, o'yinchiga
qochish imkoni berish uchun.

**"Sekundomer nega 0 ni ko'rsatyapti?"**
U faqat dushman **ta'qibda bo'lib, sizni ko'rmay qolganda** yuradi. Agar dushman
sizni hali ham ko'rib tursa — hisob nolga qaytadi.

**"Men o'yinni yuta olmayapman."**
`🟢 Oson` rejimini bosing. Bu kamchilik emas — dizayner o'z o'yinini turli
qiyinlik darajasida sinaydi.

---

## 7. Uy Vazifasi va 10 Ballik Mezon

| Mezon | Ball |
|---|---|
| 4 sinov jadvali to'ldirilgan | 4 |
| Dushman chizmasi va uning 3 kayfiyati yozilgan | 3 |
| Slayder qiymatlari va **nega shunday** degan izoh | 2 |
| Ozodalik va tartib | 1 |
| **JAMI** | **10** |

**Baholashda nimaga e'tibor berasiz:** 2 ball izoh uchun beriladi — bola
"3 soniya qo'ydim" deb yozsa 1 ball, "3 soniya qo'ydim, chunki 10 da qochib
bo'lmaydi" deb yozsa — to'liq 2 ball. Bizga **sabab** kerak, raqam emas.

---

## 8. Keyingi Dars

**16-dars: O'z Levelingni Qur — Level Redaktor va Ulashish.** Bolalar sichqoncha
bilan o'z maydonini chizadi, level kodini oladi va uni sinfdoshiga beradi.
Bugungi dushman o'sha levelga qo'yiladi.
