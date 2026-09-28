# 13-Dars: O'qituvchi Uchun Tayyorgarlik Qo'llanmasi (Teacher Prep Guide)
**Target International School // 7–8-Sinflar // 3-Hafta (1-Soat: 40 daqiqa)**
**Mavzu:** Canvas va O'yin Tsikli — RAF, Delta Time, Fizika va AABB

> **METODIK ESLATMA:** 7–8-sinf kohortasi shu paytgacha DOM bilan ishlagan:
> tugma, klik, `innerHTML`. Bugun ular birinchi marta **haqiqiy o'yin dvigatelini**
> ko'radi. Darsning cho'qqisi — **Delta Time**: agar o'quvchi shuni tushunsa,
> dars muvaffaqiyatli o'tgan hisoblanadi. Qolgan hamma narsa — shunga tayyorgarlik.

---

## 1. Darsda Qaysi Vositalar Ishlatiladi?

1. **Laboratoriya stendi (Google Chrome):**
   * Fayl: `classes/7-8-sinf/3-hafta/13-dars-canvas-va-oyin-tsikli/lab/index.html`
   * Internet **talab qilinmaydi**, hech qanday kutubxona yo'q — sof Canvas API.
   * Stendda 4 ta jonli o'lchov ko'rsatkichi bor: **FPS**, **Kadr vaqti (ms)**,
     **Qahramon tezligi (px/s)**, **Sakrash balandligi (px)**.
   * Pastda — **kadr vaqti grafigi** 16.6 ms chizig'i bilan.
2. **Prezentatsiya:** `prezentatsiya.html` — 12 slayd, `N` — o'qituvchi izohlari.
3. **Varaqa:** `varaqa.html` — 1 varaq A4, **raqamli o'lchovlar jadvali**.

---

## 2. Darsning Asosiy Texnik Mazmuni (O'qituvchi Uchun)

### A. Nega Canvas, DOM emas?
DOM daraxtidagi har bir element — brauzer uchun alohida obyekt: uslub, geometriya,
hodisa tinglovchilari. Bitta elementni siljitish **reflow** ni qo'zg'atishi mumkin —
brauzer butun sahifa geometriyasini qayta hisoblaydi. 1000 ta `div` bilan 60 FPS
ushlab bo'lmaydi.

Canvas — bitta element va uning ichidagi piksel buferi. Brauzer u yerda hech narsani
"eslab turmaydi". Shuning uchun 10 000 obyektni chizish normal holat.

**Sinfda ishlatiladigan metafora:** DOM — magnit doska (har bir magnit alohida
eslab turiladi), Canvas — oddiy doska (har kadrda o'chirib qaytadan chiziladi).

### B. O'yin Tsiklining Uch Qadami
```
CLEAR  → ekranni o'chirish
UPDATE → faqat raqamlar o'zgaradi (chizish YO'Q)
DRAW   → faqat chizish (hisoblash YO'Q)
```
Bu shunchaki tartib emas — bu **arxitektura qoidasi**. Update va Draw ni aralashtirib
yuborgan kod keyinchalik tuzatib bo'lmas holga keladi. Bolalarga shuni aytib qo'ying:
bu qoida ularning kelajakdagi barcha loyihalariga taalluqli.

### C. requestAnimationFrame vs setInterval
| | `setInterval(loop,16)` | `requestAnimationFrame(loop)` |
|---|---|---|
| Ekran bilan sinxron | ❌ yo'q, tearing bo'ladi | ✅ ha, repaint oldidan |
| Fon vkladkasi | ❌ ishlashda davom etadi | ✅ avtomatik to'xtaydi |
| Monitor chastotasi | ❌ hisobga olmaydi | ✅ 60/120/144 Gts ga moslashadi |
| Vaqt kafolati | ❌ "iltimos", kafolat emas | ✅ vaqt argumenti beriladi |

### D. Delta Time — Darsning Yuragi
`requestAnimationFrame` turli kompyuterda turli chastotada ishlaydi. Agar kod
har **kadrda** qat'iy qadam qo'ysa (`hero.x += 5`), o'yin tezligi kompyuterga
bog'liq bo'lib qoladi.

Yechim: har **soniyada** qancha yurishni belgilash va o'tgan vaqtga ko'paytirish:
```js
hero.x += 300 * dt;          // soniyasiga 300 piksel
```
`dt` — oldingi kadrdan beri o'tgan vaqt, soniyada.

**Stendda o'lchangan haqiqiy raqamlar (o'quvchilar aynan shularni yozadi):**

| FPS | `dt` YONIQ | `dt` O'CHIQ |
|---|---|---|
| 60 | **300 px/s** | 300 px/s |
| 30 | **300 px/s** | 150 px/s *(2× sekin)* |
| 15 | **300 px/s** | 75 px/s *(4× sekin)* |

### E. AABB To'qnashuv
`Axis-Aligned Bounding Box` — to'rtta taqqoslash:
```js
a.x < b.x+b.w && a.x+a.w > b.x && a.y < b.y+b.h && a.y+a.h > b.y
```
Bittasi `false` bo'lsa — to'qnashuv yo'q. Bolalarga tanish savolga javob beradi:
"tegmaganday edim, lekin jon ketdi" — chunki **hitbox rasmdan kattaroq**.

---

## 3. 40 Daqiqalik Darsning Rejasi

### 00:00 – 06:00 | DOM ning Chegarasi (1–2-slayd)
* **O'qituvchi nima deydi:**
  > *"Ваши прошлые игры — это кнопки: клик, счёт вырос. Но это не игра, это форма.
  > В настоящей игре экран перерисовывается **60 раз в секунду**. Сегодня мы
  > откроем этот движок."*
* **Savol sinfga:** *"Почему если сделать 1000 div-ов, страница начнёт тормозить?"*

### 06:00 – 10:00 | Canvas Asoslari (3-slayd)
* Ikkita obyekt: `cv` va `ctx`.
* **🛑 Majburiy: doskada koordinata o'qlarini chizing.**
  `(0,0)` — yuqori chap burchakda, **Y pastga o'sadi**. Shuning uchun sakrash
  `y` ni **kamaytiradi**: `vy = -700`. Buni aytmasangiz, yarim sinf sakrash
  mantig'ida chalkashadi.

### 10:00 – 14:00 | O'yin Tsikli (4-slayd)
* Uch qadamni ajrating.
* **Jonli demo:** stendda `🧹 CLEAR` tugmasini **o'chiring**. Qahramon ekranda
  iz qoldira boshlaydi.
  > *"Видите? Мы забыли стереть экран. Иногда это спецэффект, но обычно это баг."*

### 14:00 – 18:00 | RAF vs setInterval (5-slayd)
* Jadvalni birma-bir ko'rib chiqing.
* Oxirida **tuzoqni** ayting — bu keyingi slaydga ko'prik:
  > *"Но вот проблема: если RAF на разных компьютерах даёт разную частоту, значит
  > и игра пойдёт с разной скоростью. На мощном ПК герой летит, на слабом — ползёт."*

### 18:00 – 24:00 | ⭐ DELTA TIME — DARSNING CHO'QQISI (6-slayd)

**Bu 6 daqiqa — butun darsning eng muhim qismi. Shoshilmang.**

**Jonli isbot (proyektorda, 3 qadamda):**
1. Stendda **`QAHRAMON TEZLIGI`** ko'rsatkichini ko'rsating: `300 px/s`, yashil.
2. FPS ni **15** ga tushiring. Tezlik hali ham `300 px/s` — chunki `dt` yoniq.
3. Tepadagi **`⏱ dt`** tugmasini **o'chiring**. Ko'rsatkich darhol **`75 px/s`**
   ga tushadi va qizaradi. Qahramon ko'z oldida sudralib qoladi.
   > *"Смотрите: код тот же самый. Компьютер тот же самый. Но игра стала
   > в четыре раза медленнее. Вот зачем нужен delta time."*
4. `dt` ni qayta yoqing — tezlik `300` ga qaytadi.

**Buni 2–3 marta takrorlang.** Bolalar raqamning sakrashini ko'rishi shart.

### 24:00 – 31:00 | Fizika va To'qnashuv (7–8-slayd)
* **Fizika uchta qator:** `a → v → s`. Bu fizika darsidagi formulaning aynan o'zi.
* **Jonli demo:** gravitatsiyani `300` ga tushiring — sakrash balandligi
  ko'rsatkichi keskin oshadi (**oy effekti**), garchi `Sakrash` slayderi
  tegilmagan bo'lsa ham.
* **AABB:** `📦 HITBOX` tugmasini yoqing. Qahramon to'pga tekkanda `AABB TRUE`
  yoziladi va qahramon qizaradi.

### 31:00 – 33:00 | Kadr Byudjeti (9-slayd)
* Doskaga **`16.6 ms`** deb yozib qo'ying.
* Stendda **Zarralar** slayderini oshiring. Grafik yashildan qizilga o'tishini
  va `KADR VAQTI` ko'rsatkichi qizarishini ko'rsating.

### 33:00 – 43:00 | Amaliyot: 4 Ta Sinov (10 daqiqa)

| # | Sinov | Yoziladigan raqam |
|---|---|---|
| 1 | **Delta Time** — FPS 15, `dt` o'chiq → yoniq | Ikkita `px/s` qiymati |
| 2 | **Hitbox** — `📦 HITBOX`, qahramonni to'pga yaqinlashtirish | Hitbox rasmdan katta/kichik/teng |
| 3 | **Oy effekti** — gravitatsiya 1600 → 300 | Balandlik `px` → `px` |
| 4 | **FPS byudjeti** — zarralarni oshirish | 16 ms dan oshgan zarralar soni |

**Siz nima qilasiz:** sinf bo'ylab yuring va bitta savolni takrorlang:
*"Какое число ты записал?"* — bu darsda **raqamsiz javob qabul qilinmaydi**.

### 43:00 – 45:00 | Yakun (11–12-slayd)
Varaqalarni yig'ing. Uy vazifasida **arkada g'oyasi** ham borligini eslating —
keyingi darsda aynan shu g'oya quriladi.

---

## 4. Stend Boshqaruvi (Shpargalka)

| Element | Vazifasi |
|---|---|
| `⏱ dt: YONIQ/O'CHIQ` | Delta Time ni yoqish/o'chirish — **1-sinov** |
| `📦 HITBOX` | AABB to'rtburchaklarini ko'rsatish — **2-sinov** |
| `🧹 CLEAR: YONIQ/O'CHIQ` | Ekranni o'chirishni o'tkazib yuborish (iz effekti) |
| `MAKS / 30 / 15` | Zaif kompyuter simulyatori (kadrlarni tashlab yuborish) |
| **Gravitatsiya** 300–3000 | `px/s²` — **3-sinov** |
| **Sakrash** 300–1200 | `px/s`, bir zumlik yuqoriga tezlik |
| **Yugurish tezligi** 60–700 | `px/s`, nazariy qiymat |
| **Zarralar** 0–20 000 | Kadr byudjetini yeydi — **4-sinov** |
| `Space` | Sakrash · `R` — qayta boshlash |

**Ko'rsatkich ranglari:** yashil — me'yorda, qizil — muammo
(kadr > 16.6 ms yoki tezlik nazariy qiymatdan 15% dan ko'p og'gan).

---

## 5. Ko'p Beriladigan Savollar

**"Nega 'MAKS' rejimda ham FPS 60 dan oshmayapti?"**
Monitor chastotasi cheklaydi. 60 Gts monitorda RAF sekundiga 60 marta chaqiriladi.
144 Gts monitorda 144 bo'ladi — bu RAF ning afzalligi.

**"dt yoqilganda ham tezlik biroz o'zgarib turibdi."**
Normal: bu real o'lchov, ±2–3 px/s tebranish tabiiy. Muhimi — 300 atrofida
qolishi, 75 ga tushmasligi.

**"Zarralarni maksimumga qo'ydim, lekin kadr vaqti oshmadi."**
Kompyuter kuchli. 20 000 yetmasa, brauzerda boshqa og'ir vkladkalarni oching
yoki `MAKS` o'rniga `30` ni tanlab, taqqoslashni shunda o'tkazing.

**"Sakrash balandligi 0 ko'rsatyapti."**
O'lchov qahramon **yerga qaytganda** yangilanadi. `Space` ni bosing va
qo'nishini kuting.

---

## 6. Uy Vazifasi va 10 Ballik Mezon

| Mezon | Ball |
|---|---|
| 4 sinov jadvali **raqamlar bilan** to'ldirilgan | 4 |
| O'yin tsiklining 3 qadami o'z so'zi bilan | 2 |
| Delta Time nega kerakligi (bitta gap) | 2 |
| Keyingi dars uchun arkada g'oyasi (nom, qahramon, maqsad) | 2 |
| **JAMI** | **10** |

**Baholash nuqtai nazari:** 4 ball faqat **raqam** uchun. "Sekinlashdi" degan
javob — 0 ball. "75 px/s bo'ldi" — to'liq ball. Bu darsning butun maqsadi —
o'quvchini mavhum tasavvurdan **o'lchovga** o'tkazish.

Delta Time izohida kutilayotgan javob:
> *"Чтобы игра шла с одинаковой скоростью на быстром и медленном компьютере."*

---

## 7. Keyingi Dars

**14-dars: Dushmanlar, Ochko va Leaderboard.** O'quvchilar bugungi dvigatel ustiga
o'z arkadasini quradi, `fetch` va JSON bilan ishlaydi va sinf **reyting jadvalini**
tuzadi. Uy vazifasidagi arkada g'oyasi aynan o'sha yerda ishlatiladi.
