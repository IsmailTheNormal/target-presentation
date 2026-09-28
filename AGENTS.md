# Target International School — dars materiallari

Bu repo IT o'qituvchisi uchun dars materiallarini saqlaydi: har bir dars —
mustaqil HTML fayl (prezentatsiya + chop etiladigan varaqa).

## Kim uchun

**Ismoil Usmonov** · Target International School, Yunusobod filiali · IT
o'qituvchisi · **24 dars/hafta**, 5–11-sinflar.

Kohortalar (jadval `timetable/new-timetable.pdf`):

| Kohorta | Slot/hafta |
|---|---|
| `10A 10B 11A 11B` | 6 |
| `9A 9B` | 6 |
| `7A 7B 8A 8B` | 6 |
| `5A 5B 6A 6B` | 6 |

Dars vaqtlari: 1) 09:00 · 2) 09:45 · 3) 10:30 · 4) 11:15 · 5) 12:00 ·
6) 13:30 · 7) 14:15 · 8) 15:00 · 9) 16:10 · 10) 16:55 (har biri 40 daqiqa,
material 45 daqiqaga mo'ljallanadi).

## Papka tuzilmasi

```
target/
├── AGENTS.md                  ← shu fayl
├── METODIKA.md                ← dars o'tish metodikasi va pedagogik standart
├── REJA.md                    ← 36 haftalik (108 dars) taqvim-mavzu rejasi
├── assets/
│   ├── STYLE.md               ← dizayn tizimi, MAJBURIY o'qish
│   ├── brand.css              ← rang tokenlari manbasi
│   ├── target-logo.png        ← logotip manbasi
│   ├── logo-light.txt         ← navy variant, data URI
│   ├── logo-dark.txt          ← oq variant, data URI
│   ├── myTimeTable.pdf        ← o'qituvchi jadvali
│   └── reja_vibecoding.docx   ← 108 darslik o'quv reja
└── classes/
    ├── 5-6-sinf/
    ├── 7-8-sinf/
    ├── 9-sinf/                ← 9-sinf Junior Vibecoder kohortasi
    │   ├── 1-hafta/
    │   └── 2-hafta/
    │       └── 12-dars-ai-bug-hunter/
    │           ├── arena/     ← o'quvchilar uchun buzilgan kiber-loyiha
    │           ├── TEACHER_BUGS.md ← o'qituvchining maxfiy kaliti
    │           ├── prezentatsiya.html
    │           └── varaqa.html
    └── 10-11-sinf/            ← 10-11-sinf Senior muhandislik kohortasi
        ├── 1-hafta/
        └── 2-hafta/
```

## Fan: Vibecoding

Manba: `assets/reja_vibecoding.docx` — 36 hafta, 108 dars, haftasiga 3 dars,
4 chorak:

1. Prompt engineering, AI dizayn, freelance (1–27)
2. Agentik dasturlash (28–54)
3. AI avtomatlashtirish — n8n, Make, MCP (55–81)
4. Amaliyot va yakuniy loyiha (82–108)

## Mazmun qoidalari — MUHIM

O'qituvchining bergan feedbacki, buzilmasin:

- **11-sinf uchun chuqur yozing.** "YouTube tavsiya qiladi" darajasidagi
  misollar past. Mexanizm ko'rsating: kontekst oynasi, system prompt,
  sampling, few-shot, nega prompt ishlamaydi.
- **Hazil qilinmaydi.** O'rniga real ish misollari: buyurtma, imtihon,
  portfolio, universitetga hujjat.
- **Material ko'p bo'lsin.** 45 daqiqaga yetmay qolgan holat bo'lgan.
  Har darsda 10–12 slayd, amaliy ish 11–14 daqiqa.
- **Har darsda o'lchanadigan natija.** Amaliy ish oxirida o'quvchida
  qo'lga ushlab ko'rsatiladigan narsa qolsin (jadval, prompt, sozlama).
- **Meme faqat kulgi nuqtasida.** Darsiga ikkitadan ko'p emas, jiddiy
  slaydda (qoida, xulosa, uy vazifasi) hech qachon. Batafsil:
  `assets/MEDIA.md`.
- **Uy vazifasi 10 ballik mezon bilan** — mezon slaydda ham, varaqada ham.
- **Diniy va noo'rin metaforalar ishlatilmaydi.** Darslarda "Bibliya", diniy atamalar yoki noo'rin taqqoslashlar mutlaqo taqiqlanadi. Faqat professional IT, muhandislik va korporativ terminologiya ishlatilsin (masalan: "Dasturchining Konstitutsiyasi", "Texnik Nizom", "Standart").

## Yangi dars qanday yaratiladi

Noldan yozilmaydi. Mavjud dars **shassi** sifatida nusxa qilinadi:

```bash
cp -r classes/9-11-sinf/1-hafta/01-dars-ai-nima \
      classes/9-11-sinf/2-hafta/04-dars-<nom>
```

Keyin faqat ikkita joy almashtiriladi:

1. `<div class="stage">` va `<div class="bar">` orasidagi `<section class="slide">` bloklari
2. JS ichidagi `var NOTES = { uz: [...], ru: [...], en: [...] }` massivi

CSS, tema tizimi, til almashtirish, taymer, logotip — **tegilmaydi**.
Uslub bo'yicha hamma narsa `assets/STYLE.md` da.

## Til (In-Place i18n Standarti)

Har bir matn **uch tilda**: UZ (birlamchi HTML matni), RU (`data-ru` atributi), EN (`data-en` atributi).

### Yangi Rasmiy Standart (In-Place data-ru / data-en):
DOM elementlarini 3 marta takrorlamaymiz! Bitta element yoziladi:
```html
<h2 data-ru="Русский заголовок" data-en="English Title">O'zbekcha sarlavha</h2>
<p data-ru="Русский текст" data-en="English text">O'zbekcha matn</p>
<li data-ru="Русский пункт" data-en="English bullet">O'zbekcha band</li>
<span class="t" data-ru="Русский" data-en="English">O'zbekcha</span>
```

**Afzalliklari va Qoidalari:**
1. **Zero-Blank Fallback Kafolati:** Agar biror elementda `data-ru` yoki `data-en` atributi tasodifan yozilmay qolsa, prezentatsiya shassisi avtomatik o'zbekcha birlamchi matnni ko'rsatadi. Ekranda hech qachon bo'sh nuqta yoki bo'sh joy qolmaydi!
2. **50% Ixcham HTML:** HTML kod hajmi sezilarli kamayadi, tahrirlash osonlashadi.
3. **Merosxurlik (Backwards-compatibility):** Eski `<span lang="uz">...</span><span lang="ru">...</span>` bloklari ham to'liq qo'llab-quvvatlanadi.
4. **`assets/convert_i18n.py`:** Eski formatdagi prezentatsiyalarni yangi in-place formatga avtomatik o'tkazuvchi skript.

Tarjima so'zma-so'z emas — har til uchun tabiiy va professional yoziladi.

**🛑 CRITICAL RULE AGAINST "LAZYING OFF" (Economizing):** 
AI agentlari vaqt yoki token tejash uchun hech qachon `data-ru` va `data-en` atributlarini tashlab ketmasligi shart. Har bir `<h2>`, `<p>`, `<li>`, `<th>`, `<td>` va teglarda `data-ru` va `data-en` to'liq to'ldirilsin.

`data-phase` va `data-time` atributlarida ajratgich `|`: `"Nazariy|Теория|Theory"`.

## Prezentatsiya klavishlari

`←` `→` slayd · `N` o'qituvchi izohlari · `Esc` izohni yopish ·
`R` javobni ochish · `L` til · `T` mavzu · `H` pastki panelni yashirish

## Ma'lum tuzoqlar — takrorlanmasin

Bular real xatolar, allaqachon tuzatilgan. Yangi sahifada takrorlanmasin:

1. **Grid ichidagi matn ustunga tushib ketadi.** `display:grid` bo'lgan
   `li` ichida `<b>Sarlavha</b> qolgan matn` yozsangiz, matn ikkinchi grid
   elementiga aylanadi va tor ustunda har so'z alohida qatorga tushadi.
   Yechim: butun matnni bitta `<span class="t">` ichiga oling.
2. **`hidden` atributi ishlamaydi.** `.notes{display:grid}` `hidden` dan
   kuchli. `.notes[hidden]{display:none}` yozilishi shart. Artifact
   sahifasida yashirin reset bor, lokal faylda yo'q — shuning uchun xato
   faqat lokal faylda ko'rinadi.
3. **Chop etishda qorong'i mavzu qog'ozga o'tib ketadi.** `@media print`
   ichidagi `:root{}` bloki `:root[data-theme="dark"]` dan kuchsiz.
   To'rtala selektor yozilishi shart — `assets/STYLE.md` ga qarang.
4. **Fon rasm chop etilmaydi.** Logotip `background-image` bilan emas,
   `<img>` bilan qo'yiladi.
5. **Bir xil rangdagi matn va fon.** `.noprint button` barcha tugmalarga
   fon berib, matn rangi bilan to'qnashgan edi. Element selektorlari bilan
   klass selektorlarini urishtirmang.

## Darslar holati

| # | Sinf | Hafta | Mavzu | Holat |
|---|------|-------|-------|-------|
| 01 | 9-11 | 1 | Sun'iy intellekt nima? AI vositalari | ✅ o'tildi |
| 02 | 9-11 | 1 | Vibecoding asoslari: UI/UX, Frontend & Backend | ✅ tayyor |
| 03 | 9-11 | 1 | IT Dunyosi: HTML, CSS, JS, Database va Cloud | ✅ tayyor |
| 04 | 9-11 | 1 | Frilans buyurtma: PRD, Grid, Flexbox, UI dizayn | ✅ tayyor |
| 05 | 9-11 | 1 | Frilans mantiq: JavaScript, Events va Dark Mode | ✅ tayyor |
| 06 | 9-11 | 1 | Deploy va Taqdimot: Vercel, SSL, QR Kod va Demo Day | ✅ tayyor |
| 07 | 9-11 | 2 | API va JSON asoslari: REST, HTTP statuslar va CORS | ✅ tayyor |
| 08 | 9-11 | 2 | Amaliy loyiha: Jonli Valyuta va Kripto Konverteri | ✅ tayyor |
| 09 | 9-11 | 2 | Doimiy xotira: LocalStorage, State va Tarix | ✅ tayyor |
| 10 | 9-11 | 2 | Kiberxavfsizlik: Auth, Parollar va .env himoyasi | ✅ tayyor |
| 11 | 9-11 | 2 | Mahalliy muhit: VS Code o'rnatish va Live Server | ✅ tayyor |
| 12 | 9 | 2 | AI Bug Hunter: Kiber-Detektivlik va Debugging | ✅ tayyor |
| 12 | 10-11 | 2 | Agentik AI: Mustaqil kod yozish va ReAct tsikli | ✅ tayyor |
| 13 | 5-6 | 3 | O'yin Mexanikasi: Qahramon Harakati va Boshqaruv | ✅ tayyor |
| 14 | 5-6 | 3 | To'siqlar Maydoni: Tikanlar, Lazerlar va Jonlar (HP) | ✅ tayyor |
| 13 | 10-11 | 3 | LLM Arxitekturasi: Kontekst, Sampling va Few-Shot | ✅ tayyor |
| 14 | 10-11 | 3 | Tool Calling va Funksiyalar: JSON Schema & ReAct | ✅ tayyor |
| 15 | 10-11 | 3 | RAG va Vektor Qidiruv: Semantik Indekslash va Embeddings | ✅ tayyor |
| 16 | 10-11 | 3 | Avtonom Agentlar va Doimiy Xotira: Multi-Agent Tizimlari | ✅ tayyor |
| 13 | 9 | 3 | AI Chat va Real-Vaqt Javob Oqimi (Streaming) | ✅ tayyor |
| 14 | 9 | 3 | Tizimli Promptlar va Rollar: Prompt Injection Himoyasi | ✅ tayyor |
| 08 | 7-8 | 2 | JavaScript Hodisalari: DOM va Interaktiv Tugmalar | ✅ tayyor |
| 09 | 7-8 | 2 | Mini-O'yin: Kiber-Reaksiya Tezlik Testi | ✅ tayyor |
| 15 | 5-6 | 3 | Kiber-Yuguruvchi 3.0: Kristalllar, Ballar va Vaqt | ✅ tayyor |
| 16 | 5-6 | 3 | Kiber-Yuguruvchi 4.0: Boss Jangi, Lazer Qalqoni va Buyuk G'alaba | ✅ tayyor |
| 15 | 5-6 | 4 | Dushman AI: Patrul, Ko'rish Radiusi va Ta'qib | ✅ tayyor |
| 16 | 5-6 | 4 | O'z Levelingni Qur: Redaktor, Level Kodi va Ulashish | ✅ tayyor |
| 10 | 7-8 | 2 | AI Debugging va Dastur Mantig'i: Stack Trace, Breakpoints | ✅ tayyor |
| 11 | 7-8 | 2 | LocalStorage va Doimiy Ma'lumotlar: JSON, High Score | ✅ tayyor |
| 12 | 7-8 | 2 | O'yin Turniri va Veb-Deploy: Vercel, SSL va QR Kod | ✅ tayyor |
| 13 | 7-8 | 3 | Canvas va O'yin Tsikli: RAF, Delta Time va Fizika | ✅ tayyor |
| 14 | 7-8 | 3 | Dushmanlar, Ochko va Leaderboard: JSON, Sort, Halollik | ✅ tayyor |
| 15 | 7-8 | 3 | O'yin Fizikasi: Gravitatsiya, Sakrash va AABB To'qnashuv | ✅ tayyor |
| 16 | 7-8 | 3 | Boss Jangi, Power-uplar va Arkada Yakuni | ✅ tayyor |
| 17 | 7-8 | 4 | Audio Sintezi, Web Audio API va Partikllar Tizimi | ✅ tayyor |
| 18 | 7-8 | 4 | Kamera Skrollingi va Procedural Dunyo Generatsiyasi | ✅ tayyor |
| 19 | 7-8 | 4 | Mobil Moslashuv, Touch Hodisalari va Virtual Joystik | ✅ tayyor |
| 20 | 7-8 | 4 | Kiber-Arkada Final Game Jam va Veb-Deploy | ✅ tayyor |
| 13 | 9 | 3 | Git va GitHub: Commit, Branch va Merge Konflikti | ✅ tayyor |
| 14 | 9 | 3 | Pull Request va Kod Ko'rigi: Diff, Izoh va Qaror | ✅ tayyor |
| 15 | 9 | 3 | CI/CD, GitHub Actions va Avtomatlashtirish | ✅ tayyor |
| 16 | 9 | 3 | SemVer, GitHub Releases va Open Source Hamkorlik | ✅ tayyor |
| 15 | 10-11 | 4 | RAG va Embeddinglar: Chunking, Vektor Qidiruv, Kosinus | ✅ tayyor |
| 16 | 10-11 | 4 | Prompt Injection va AI Xavfsizligi: Hujum, Himoya, Red Team | ✅ tayyor |
| 17 | 9 | 4 | Docker va Konteynerlar: Tizimlararo Moslik Kafolati | ✅ tayyor |
| 18 | 9 | 4 | Ma'lumotlar Bazasi va SQL: Relyatsion Sxema, Indekslar | ✅ tayyor |
| 19 | 9 | 4 | Vebhooklar va Avtomatlashtirish: Real-Vaqt Integratsiya | ✅ tayyor |
| 20 | 9 | 4 | Full-Stack Deploy va Demo Day: Prodaction Muhandislik | ✅ tayyor |

> **Holat yangilanishi (2026-09-28):**
> - **7–8-sinf:** 2-hafta (10, 11, 12), 3-hafta (13, 14, 15, 16) va 4-hafta (17, 18, 19, 20) to'liq 100% tayyor.
> - **9-sinf:** 3-hafta Git/DevOps to'liq tsikli (13, 14, 15, 16) va 4-hafta DevOps & Full-Stack Prodaction tsikli (17-Docker, 18-SQL & RDBMS, 19-Webhooks & Event-Driven, 20-Full-Stack Deploy & Demo Day) to'liq 100% tayyorlandi, trilingual in-place standartda tekshirildi.
> - **Global touch/swipe & navigation:** Barcha taqdimotlarda sensorli swipe va `.deck.is-clean` rejimida ekranning pastki qismida paydo bo'luvchi `▲ Panel` restore tugmasi to'liq integratsiya qilindi.
> - **Brandmark & Favicon:** Barcha taqdimotlarning pastki panelida qorong'i (dark) va yorug' (light) mavzuda to'liq moslashuvchi Target logotipi (dual `.on-light` / `.on-dark`) 100% tiklandi va brauzer sarlavhasi (Chrome tab) uchun dual-theme SVG/PNG Target favicon to'plami integratsiya qilindi.

