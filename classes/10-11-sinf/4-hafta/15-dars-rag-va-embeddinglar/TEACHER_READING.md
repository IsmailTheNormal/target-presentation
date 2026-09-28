# 15-Dars: O'qituvchi Uchun Tayyorgarlik Qo'llanmasi (Teacher Prep Guide)
**Target International School // 10–11-Sinflar (Senior Engineering) // 4-Hafta (1-Soat)**
**Mavzu:** RAG va Embeddinglar — Chunking, Vektor Qidiruv va Kosinus O'xshashlik

> **METODIK ESLATMA:** 13-darsda modelning ichki tuzilishi (kontekst oynasi,
> sampling, system prompt), 14-darsda Tool Calling o'rganilgan edi. Bugun uchinchi
> katta mavzu: modelga **o'z bilimingizni** berish. Darsning asosiy xabari —
> **RAG sifati generatsiyaga emas, qidiruvga bog'liq**. Bu 10–11-sinf uchun
> jiddiy muhandislik darsi, soddalashtirmang.

---

## 1. Darsda Qaysi Vositalar Ishlatiladi?

1. **RAG laboratoriya stendi (Google Chrome):**
   * Fayl: `classes/10-11-sinf/4-hafta/15-dars-rag-va-embeddinglar/lab/index.html`
   * **Internet va API kalit talab qilinmaydi.**
   * Stendda **to'liq ishlaydigan** RAG konveyeri: chunking → TF-IDF vektorlash →
     L2 normalizatsiya → kosinus qidiruv → top-K → kontekst yig'ish → javob.
   * Bilimlar bazasi — **maktabning ichki qoidalari** (imtihon, loyiha himoyasi,
     dars qoldirish, jihozlar). Bu ataylab shunday: hech bir model bu hujjatlarni
     o'qishdan bilmaydi, ya'ni RAG siz javob berib bo'lmaydi.
2. **Prezentatsiya:** `prezentatsiya.html` — 12 slayd, `N` — o'qituvchi izohlari.
3. **Varaqa:** `varaqa.html` — 1 varaq A4.

### ⚠️ Stend haqida halol ogohlantirish (buni o'quvchilarga ayting)
Stendda **soddalashtirilgan leksik embedding** (TF-IDF uslubidagi vektor +
prefiks-stemming) ishlatiladi, neyron embedding emas — chunki stend brauzerda,
internetsiz ishlashi kerak.

**Nima aynan real tizimdagidek:** chunking va overlap mantig'i, L2 normalizatsiya,
kosinus o'xshashlik formulasi, top-K tanlash, chegara (threshold) va grounding.

**Nima real emas:** semantik yaqinlik. Real neyron embedding "xodim kasal bo'lsa"
va "mehnatga layoqatsizlik varaqasi" ni bog'lay oladi, stend esa faqat leksik
ustma-tushishni ko'radi. Slaydda bu alohida aytilgan — uni o'qib bering,
bu ilmiy halollik masalasi.

---

## 2. O'qituvchi Uchun Texnik Mazmun

### A. Nega RAG kerak — uchta chegara
1. **Knowledge cutoff.** Model o'qitilgan sanadan keyingi hech narsani bilmaydi
   va **bilmasligini ham bilmaydi**.
2. **Gallyutsinatsiya.** LLM — keyingi tokenning ehtimolini hisoblovchi model.
   Fakt yo'q bo'lsa, u bo'shliq qoldirmaydi — eng ehtimolli matnni generatsiya
   qiladi. **Bu arxitektura xususiyati, xato emas.**
3. **Kontekst narxi.** Hamma hujjatni promptga solish ishlamaydi: oyna cheklangan,
   token pul turadi, va uzun kontekstda **lost in the middle** effekti paydo bo'ladi.

### B. Fine-tuning vs RAG
| | Fine-tuning | RAG |
|---|---|---|
| Bilim qayerda | Model vaznlarida | Tashqi bazada |
| Yangilash | Qayta o'qitish (soat, pul) | Hujjatni almashtirish (soniya) |
| Manba ko'rsatish | ❌ mumkin emas | ✅ mumkin |
| Kirish huquqi | ❌ | ✅ foydalanuvchi bo'yicha |
| Nima uchun yaxshi | **Uslub**, format, domen tili | **Faktlar** |

### C. Ikki bosqichli arxitektura
**A · Indekslash (oflayn, bir marta):** hujjat → matn → chunking → embedding →
vektor baza.
**B · So'rov (onlayn, har savolda):** savol → embedding → top-K qidiruv →
kontekst yig'ish → LLM → javob + manbalar.

**Eng muhim gap darsda:** LLM bu yerda **faqat oxirgi qadamda** qatnashadi.
Noto'g'ri parchalar topilsa, dunyodagi eng kuchli model ham to'g'ri javob bera
olmaydi — u faqat berilgan axlatni chiroyli qilib qaytaradi.

### D. Chunking — eng ko'p xato qilinadigan qadam
* **Juda kichik (<100 token):** parcha kontekstni yo'qotadi, olmoshlar
  oldingi chunkda qoladi.
* **Juda katta (>1000 token):** bitta vektor bir nechta mavzuning **o'rtachasiga**
  aylanadi — semantik suyultirish (dilution).
* **Amaliy oraliq:** 200–500 token + 10–20% overlap, **ma'no chegarasi bo'yicha**.
* **Oltin qoida:** bir chunk — bir tugallangan fikr.

### E. Kosinus o'xshashlik — nega burchak, masofa emas
```
cos(A,B) = (A·B) / (|A| × |B|)
```
Vektor **uzunligi** matn **hajmini** aks ettiradi, ma'nosini emas. Evklid masofasi
bilan qisqa savol uzun hujjatdan "uzoq" chiqadi, hatto mavzu bir xil bo'lsa ham.
Burchak esa **yo'nalishni**, ya'ni sof ma'noni o'lchaydi.

Amalda vektorlar normalizatsiya qilinadi (`|A| = 1`), shunda kosinus oddiy
skalyar ko'paytmaga aylanadi. **Stendda ham aynan shunday qilingan** — buni
ko'rsatsangiz bo'ladi.

### F. ANN va HNSW
Brute force: 10 mln vektor × 1536 o'lcham = so'rovga ~15 milliard ko'paytirish
(~10 soniya). Kerak: ~50 ms. **200 barobar farq.**

**HNSW** — ko'p qavatli graf: yuqori qavat "samolyot" (uzoq sakrashlar),
pastki qavat "piyoda" (aniq qidiruv). Natija: ~99% aniqlik, ~1000 barobar tezlik.

Sanoat: pgvector, Qdrant, Pinecone, Weaviate, Milvus, FAISS.

### G. To'rtta nosozlik (diagnostika jadvali)
| Nosozlik | Belgi | Yechim |
|---|---|---|
| Chunk chegarasi | "Yarim javob" | Overlap oshirish, ma'no bo'yicha bo'lish |
| Semantik bo'shliq | Aniq mavjud fakt topilmaydi | Gibrid qidiruv: vektor + BM25 |
| Eskirgan indeks | Ishonchli, lekin eski javob | Hujjat o'zgarishida qayta indekslash |
| Kontekstga qarshi | To'g'ri parcha, noto'g'ri javob | Qattiq system prompt + manba talabi |

---

## 3. Dars Rejasi (55–58 daqiqa material, 45 daqiqaga siqiladi)

### 00:00 – 07:00 | Uchta Chegara (1–2-slayd)
Gallyutsinatsiya tushuntirishiga alohida e'tibor bering — bu arxitektura
xususiyati ekanini ayting, "model yolg'on gapiradi" emas.

### 07:00 – 11:00 | Fine-tuning yoki RAG (3-slayd)
Sanoatdagi eng ko'p chalkashtiriladigan qaror. Mnemonika:
**fine-tuning — uslub uchun, RAG — faktlar uchun.**

### 11:00 – 16:00 | Ikki Bosqichli Arxitektura (4-slayd)
Doskada ikki bosqichni chizing. Asosiy gapni ayting: **RAG sifati 90% qidiruvga
bog'liq.**

### 16:00 – 21:00 | Chunking (5-slayd)
Doskaga yozib qo'ying: **200–500 token, 10–20% overlap.**
Stendda `chunk = 40` qo'yib, parchalar 49 taga ko'payishini va matn o'rtasidan
kesilishini ko'rsating.

### 21:00 – 26:00 | Embedding (6-slayd)
Kalit so'z qidiruvi bilan taqqoslash misolini **albatta** ko'rsating — u eng
ishonarli argument. **Va stend haqidagi ogohlantirishni o'qib bering.**

### 26:00 – 31:00 | ⭐ KOSINUS — MATEMATIK CHO'QQI (7-slayd)
Formulani doskada chiqaring. Savol bering: *"Почему угол, а не расстояние?"*
Javobni o'zlari topsin — 10–11-sinf buni uddalaydi.

### 31:00 – 35:00 | Vektor Baza va HNSW (8-slayd)
Raqamlarni doskaga yozing: 15 mlrd, 10 s, 50 ms, 200×, 99%, 1000×.

### 35:00 – 43:00 | Kontekst Yig'ish va Nosozliklar (9–10-slayd)
Prompt tuzilishidagi ikkita eng muhim qatorni ta'kidlang:
**"bilmayman deb ayt"** va **"manba ko'rsat"**.

### 43:00 – 55:00 | Amaliyot (12 daqiqa)

| # | Sinov | O'lchanadigan raqam |
|---|---|---|
| 1 | Chunk 40 → 400 | top-1 kosinus ikkala holatda |
| 2 | Kosinus taqsimoti | eng yuqori va eng past ball |
| 3 | Top-K = 1 → 3 → 8 | eng yaxshi K va sababi |
| 4 | **Grounding** | qattiq prompt bilan va usiz |

**🎯 4-sinov — darsning eng muhim qismi.** O'quvchi "Ertaga ob-havo qanday?"
degan savolni beradi:
* **Qattiq prompt YONIQ:** tizim halol *"bilimlar bazasida topilmadi, eng yaxshi
  kosinus 0.000"* deydi.
* **Qattiq prompt O'CHIQ:** tizim manbasiz javob beradi — **gallyutsinatsiya
  jonli ko'rinadi**.

> *"Способность ответить «не знаю» — это сила системы, а не слабость.
> Система, которая честно говорит «не найдено», гораздо ценнее той,
> что уверенно выдумывает."*

### 55:00 – 58:00 | Yakun
Varaqalarni yig'ing. Loyihalash topshirig'ini alohida e'lon qiling — u 3 ball.

---

## 4. Stend Boshqaruvi va Kutilayotgan Raqamlar

| Element | Vazifasi |
|---|---|
| **Chunk hajmi** 40–600 belgi | Indeks qayta quriladi |
| **Overlap** 0–50% | Chegarada qolgan jumlani qutqaradi |
| **Top-K** 1–8 | Promptga necha parcha kiradi |
| `🔒 Qattiq prompt` | Grounding ni yoqish/o'chirish — **4-sinov** |
| Tayyor savollar | Oxirgisi (❌ belgili) — bazada javobi yo'q |

**Kutilayotgan kosinus qiymatlari** (chunk 240, overlap 15%) — o'quvchi
raqamlari shu atrofda bo'lishi kerak:

| Savol | Topiladigan hujjat | cos ≈ |
|---|---|---|
| Imtihonga qo'yilish uchun nechta uy ishi? | D1 | **0.43** |
| Loyihada AI dan foydalansa bo'ladimi? | D2 | **0.27** |
| Kasal bo'lib dars qoldirsam? | D3 | **0.36** |
| Shaxsiy noutbuk olib kelsa bo'ladimi? | D4 | **0.16** |
| **Ertaga ob-havo qanday?** | — | **0.000** |

Oxirgi qatorga e'tibor bering: **aniq nol**. Bu tasodif emas — savolda bazadagi
birorta so'z yo'q, demak vektorlar ortogonal. Bu kosinus mexanikasining eng
yorqin namoyishi.

**1-sinov uchun:** "Loyihada AI dan foydalansa bo'ladimi?" savolida
chunk = 40 → **0.268**, chunk = 400 → **0.192**. Farqni o'quvchi izohlashi kerak:
kichik chunkda so'z zichligi yuqori (TF-IDF balli ko'tariladi), lekin **kontekst
yo'qoladi** — javob matni tushunarsiz bo'lib qoladi. Bu chunking savdosining
(trade-off) mohiyati.

---

## 5. Ko'p Beriladigan Savollar

**"Nega 'ob-havo' savoliga kosinus aynan 0?"**
Savoldagi birorta token bazadagi lug'atda yo'q. Skalyar ko'paytmada hamma
hadlar nolga teng. Bu ortogonal vektorlar — mukammal misol.

**"Chunk 40 da ball yuqoriroq chiqdi, demak kichik chunk yaxshiroqmi?"**
Yo'q — bu tuzoq savol, va uni o'zingiz berishingiz mumkin. Ball yuqori, chunki
qisqa matnda so'z **zichligi** katta. Lekin topilgan parcha matni tushunarsiz —
javob sifati pasayadi. **Qidiruv balli ≠ javob sifati.**

**"Stend haqiqiy embedding ishlatadimi?"**
Yo'q, TF-IDF + prefiks-stemming. Mexanika real, semantika soddalashtirilgan.
Buni ochiq ayting — bu ilmiy halollikning bir qismi.

**"Nega prefiks-stemming kerak bo'ldi?"**
Rus va o'zbek tillarida so'z oxiri o'zgaradi ("ноутбук" / "ноутбуки",
"loyiha" / "loyihada"). Aniq moslik ishlamaydi. Stend har so'zdan 5 harfli
o'zakni ham token sifatida chiqaradi. **Real tizimlarda bu muammo neyron
embedding bilan hal qilinadi** — mana shu yerda stendning chegarasi ko'rinadi.

---

## 6. Uy Vazifasi va 10 Ballik Mezon

| Mezon | Ball |
|---|---|
| 4 sinov jadvali **aniq raqamlar** bilan | 3 |
| Kosinus formulasi va "nega burchak" izohi | 2 |
| **Maktab uchun RAG loyihasi** | 3 |
| Nosozlik tahlili (belgi + yechim) | 2 |
| **JAMI** | **10** |

**Loyihalash topshirig'i (3 ball) — eng qimmatli qism.** Kutilayotgan javobda
bo'lishi kerak:
* qaysi hujjatlar indekslanadi (nizom, jadval, o'quv reja...);
* chunk hajmi **va nega aynan shunday** (masalan: "300 belgi, chunki nizom
  bandlari shu uzunlikda");
* K qiymati va sababi;
* **indeks qanday yangilanadi** — bu eng ko'p unutiladigan nuqta, lekin real
  tizimda eng ko'p muammo keltiradigan joy.

To'liq ball uchun **sabab** talab qiling, faqat raqam emas.

---

## 7. Keyingi Dars

**16-dars: Prompt Injection va AI Xavfsizligi.** O'quvchilar bugun qurgan RAG
tizimining **eng katta zaifligini** ko'radi: agar hujjatga zararli ko'rsatma
yozilgan bo'lsa, u to'g'ridan-to'g'ri model kontekstiga tushadi. Bugungi
"kontekstga ishonish" tamoyili ertaga hujum vektoriga aylanadi.
