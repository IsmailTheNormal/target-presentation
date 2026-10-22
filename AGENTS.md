# Target International School — dars materiallari

Bu repo IT o'qituvchisi uchun dars materiallarini saqlaydi: har bir dars —
mustaqil HTML fayl (prezentatsiya + chop etiladigan varaqa).

## Kim uchun

**Musulmonov Mamarajab** · Target International School, Yunusobod filiali · IT & CyberSecurity
o'qituvchisi · **31 dars/hafta**, 5–11-sinflar.

Kohortalar (yangi jadval `assets/photo_2026-09-29_09-19-52.jpg`):

| Kohorta | Fan yorlig'i | Slot/hafta | Kunlar va vaqtlar |
|---|---|---|---|
| `5A 5B 6A 6B` | CyberSecurity | 6 | Seshanba (3, 4) · Chorshanba (3, 4) · Payshanba (3, 4) |
| `10A 10B 11A 11B` | CyberSecurity | 5 | Seshanba (5) · Chorshanba (5, 6) · Payshanba (5, 6) |
| `9A 9B` | CyberSecurity | 5 | Dushanba (7) · Seshanba (6, 7) · Juma (7, 8) |
| `7A 7B 8A 8B` | CyberSecurity | 5 | Dushanba (8) · Chorshanba (7, 8) · Payshanba (7, 8) |
| `Choice: IT (9–11)` | Choice IT | 10 | Dushanba–Juma har kuni (9-dars 16:10, 10-dars 16:55) |

Dars vaqtlari: 1) 09:00 · 2) 09:45 · 3) 10:30 · 4) 11:15 · 5) 12:00 ·
6) 13:30 · 7) 14:15 · 8) 15:00 · 9) 16:10 · 10) 16:55 (har biri 40 daqiqa,
material 45 daqiqaga mo'ljallanadi). Jami: 31 dars/hafta.

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
- **Vizual zichlik — nafas oluvchi, zamonaviy mahsulot (commercial product / SaaS) estetikasi.** Varaqalar va laboratoriyalar hech qachon mayda shriftli, tiqilgan byurokratik shaklga aylanmasin. Varaqalarda matn `9.2pt–9.6pt`, qo'lda yozish chiziqlari `16pt–18pt`. Laboratoriyalarda `1400px` kenglik, `20px–24px` paddingli kartalar, pill tablar, o'qilishi oson keng jadvallar (Supabase/Linear darajasida). Batafsil: `assets/STYLE.md`.


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
AI agentlari vaqt yoki token tejash uchun hech qachon `data-ru` va `data-en` atributlarini tashlab ketmasligi shart. Har bir `<h2>`, `<p>`, `<li>`, `<th>`, `<td>` va interaktiv elementlarda `data-ru` va `data-en` to'liq to'ldirilsin.

`data-phase` va `data-time` atributlarida ajratgich `|`: `"Nazariy|Теория|Theory"`.

### Lokalizatsiyani Avtomatlashtirilgan Tekshirish (MAJBURIY):
Har qanday dars materiali (prezentatsiya, varaqa, laboratoriya) yaratilganda yoki tahrirlanganda commit qilishdan oldin tekshiruv skripti ishga tushirilishi SHART:

```bash
# 1. Bitta dars yoki papkani tekshirish:
python3 scripts/verify_i18n.py classes/9-sinf/4-hafta/18-dars-malumotlar-bazasi-va-sql

# 2. Git pre-commit hook orqali (avtomatik ishlaydi):
bash scripts/install_hooks.sh
python3 scripts/verify_i18n.py --staged

# 3. Butun repo bo'yicha to'liq audit:
python3 scripts/verify_i18n.py --all
```

**Brauzer ichidagi Real-Vaqt i18n Inspektori:**
Har qanday sahifada `Ctrl+Alt+L` (yoki `Alt+Shift+L`, yoxud URLga `?i18n=1` qo'shish) orqali jonli i18n HUD paneli ochiladi. U tarjima qilinmagan elementlarni qizil bilan belgilaydi va UZ -> RU -> EN avtomatik stress-testini o'tkazib, bo'sh qolgan joylarni fosh qiladi.


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
| 17 | 10-11 | 4 | RAG va Embeddinglar: Chunking, Vektor Qidiruv, Kosinus | ✅ tayyor |
| 18 | 10-11 | 4 | Prompt Injection va AI Xavfsizligi: Hujum, Himoya, Red Team | ✅ tayyor |
| 19 | 10-11 | 4 | AI Agent Sandboxing va RCE Himoyasi: Xavfsiz Kod Bajarish | ✅ tayyor |
| 20 | 10-11 | 4 | Multi-Agent Tizimlari Xavfsizligi, Egress DLP va Demo Day | ✅ tayyor |
| 17 | 9 | 4 | Docker va Konteynerlar: Tizimlararo Moslik Kafolati | ✅ tayyor |
| 18 | 9 | 4 | Ma'lumotlar Bazasi va SQL: Relyatsion Sxema, Indekslar | ✅ tayyor |
| 19 | 9 | 4 | Backend Asoslari: Node.js, Express va REST API | ✅ tayyor |
| 19.5 | 9 | 4 | Vibecoding E-Commerce Backend: Users, Orders & Postman | ✅ tayyor |
| 20 | 9 | 4 | Full-Stack Deploy va Demo Day: Prodaction Muhandislik | ✅ tayyor |
| 21 | 9 | 5 | Linux Server Hardening: SSH, UFW va Fail2ban | ✅ tayyor |
| 22 | 9 | 5 | Tarmoq Xavfsizligi va Paket Tahlili: Wireshark & Nmap | ✅ tayyor |
| 23 | 9 | 5 | Veb Zaifliklari va OWASP Top 10: SQLi & XSS | ✅ tayyor |
| 24 | 9 | 5 | Autentifikatsiya Xavfsizligi: JWT, XSS/CSRF va 2FA | ✅ tayyor |
| 25 | 9 | 5 | Kiber-Hujum Simulyatsiyasi: CTF va Red/Blue Team | ✅ tayyor |
| 21 | 10-11 | 5 | Kriptografiya Asoslari: AES-256, RSA va ECC Shifrlash | ✅ tayyor |
| 22 | 10-11 | 5 | Zero Trust va IAM Arxitekturasi: RBAC, ABAC va mTLS | ✅ tayyor |
| 23 | 10-11 | 5 | API Xavfsizligi va Rate Limiting: Token Bucket & HMAC | ✅ tayyor |
| 24 | 10-11 | 5 | Shaxsiy AI Telegram Bot: Webhooklar va Dev Tunnels | ✅ tayyor |
| 17 | 5-6 | 5 | Parollar Jangi: Xakerlar Qanday Buzadi, Brute-Force | ✅ tayyor |
| 18 | 5-6 | 5 | Fishing Detektori: Soxta Havolalar, 'Bepul Robux', 2FA | ✅ tayyor |
| 19 | 5-6 | 5 | Zararli Dasturlar va Troyanlar: 'Troyalik Ot' va Tekin Modlar | ✅ tayyor |
| 21 | 7-8 | 5 | FUT Card Studio: File API va OVR Reyting | ✅ tayyor |
| 22 | 7-8 | 5 | FUT Squad Builder: Graf va Kimyo Algoritmi | ✅ tayyor |
| 23 | 7-8 | 5 | FUT Match Engine: Taktik Duel Simulyatori | ✅ tayyor |
| 24 | 7-8 | 5 | FUT Transfer Market: Talab-Taklif va 5% Soliq | ✅ tayyor |
| 25 | 7-8 | 5 | Target Jarvis: AI Ovozli Yordamchi (Web Speech API) | ✅ tayyor |
| 26 | 7-8 | 6 | Kiber-Ko'z: Kompyuter Ko'rishi va Veb-kamera Harakat Detektori | ✅ tayyor |
| 20 | 5-6 | 6 | Kiber-Firibgarlar: Ijtimoiy Muhandislik & Cyber Detective Studio | ✅ tayyor |
| 26 | 9 | 6 | MVC Backend Asoslari: Relyatsion SQLite, Foreign Keys & REST API | ✅ tayyor |
| 21 | 5-6 | 7 | Raqamli Iz (Digital Footprint) va Shaxsiy Maxfiylik | ✅ tayyor |
| 27 | 9 | 7 | Veb Xavfsizlik: XSS, CSRF va Kiruvchi Ma'lumotlarni Tozalash (Sanitization) | ✅ tayyor |
| 28 | 9 | 8 | Full-Stack Xavfsiz Servis va CTF Kiber-Sinov — 1-Chorak Oraliq Nazorat | ✅ tayyor |
| 22 | 5-6 | 8 | Kiber-Qalqon Viktorinasi va Amaliy Sinov — 1-Chorak Oraliq Nazorat | ✅ tayyor |
| 01 (Exp) | 10-11 / Senior | Tajribaviy | Kompyuter Asosiy Xotirasi: RAM, ROM, EPROM, DRAM, VRAM va Xotira Arxitekturasi (Floating Glassmorphism UI & Academic Reference Style) | ✅ tayyor |

> - **Minimalist Tipografik Prezentatsiyalar, Interaktiv Testlar & Mustaqil Uy Vazifasi (`vazifa.html`) Yangi Standarti:** Foydalanuvchi talabi asosida barcha 4 ta kohorta uchun 1-chorak yakuniy tsiklini to'liq qamrab oluvchi yangi avlod dars materiallari yaratildi: ramkalar, konteyner qutilari (`.box`, `.card`, `.step`), ortiqcha padding va vizual shovqinsiz sof tipografik iyerarxiya (ulkan sarlavhalar `clamp(36px, 5.2vw, 72px)`, yirik lede `clamp(18px, 2vw, 26px)`, unboxed ro'yxatlar, yuqori kontrastli SVG diagrammalar, Zero Bottom Bar, suzuvchi oynaviy brend kapsulasi va `[UZ | RU | EN]` dok paneli hamda 100% in-place trilingual lokalizatsiya):
>   - **9-sinf (8-hafta 28-dars Full-Stack Xavfsiz Servis va CTF Kiber-Sinov):** 1-Chorak oraliq nazorati: MVC arxitekturasi, relyatsion SQLite, JWT autentifikatsiya, XSS/CSRF filtrlash, CTF sinovi, 12 slaydli prezentatsiya (`prezentatsiya.html`), 2 betlik A4 varaqa (`varaqa.html`), interaktiv uy vazifasi (`vazifa.html`), o'qituvchi tayyorgarlik qo'llanmasi (`TEACHER_READING.md`).
>   - **9-sinf (7-hafta 27-dars Veb Xavfsizlik: XSS, CSRF va Input Sanitization):** XSS 3 turi (Stored, Reflected, DOM-based), cookie `HttpOnly`, CSRF tokenlar, DOMPurify, Helmet sarlavhalari, 12 slaydli prezentatsiya (`prezentatsiya.html`), 2 betlik A4 amaliy ish varaqasi (`varaqa.html`), interaktiv uy vazifasi (`vazifa.html`), o'qituvchi qo'llanmasi (`TEACHER_READING.md`).
>   - **7–8-sinf (8-hafta 30-dars Sport Simulyatori va O'yin Fizikasi):** 1-Chorak oraliq nazorati: Karta OVR formulasi, 11 tugunli kimyo graflari (33 ballik sinergiya), Match Engine FSM tsikli, 2D to'qnashuv fizikasi (AABB, ishqalanish, elastik qaytish), EA 5% savdo solig'i (Coin Sink) va drop rate ehtimolligi, 12 slaydli taqdimot (`prezentatsiya.html`), 2 betlik A4 varaqa (`varaqa.html`), interaktiv uy vazifasi (`vazifa.html`), o'qituvchi qo'llanmasi (`TEACHER_READING.md`).
>   - **5–6-sinf (8-hafta 22-dars Kiber-Qalqon Viktorinasi va Amaliy Sinov):** 1-Chorak oraliq nazorati: 14+ belgili mustahkam parollar, fishing qopqonlarini fosh qilish (URL domain tekshiruvi), tekin modlar va troyan otlari, ijtimoiy muhandislik aldovlari, EXIF GPS tozalash va Katta Ekran qoidasi (Billboard Rule), 12 slaydli taqdimot (`prezentatsiya.html`), 2 betlik A4 varaqa (`varaqa.html`), interaktiv uy vazifasi (`vazifa.html`), o'qituvchi qo'llanmasi (`TEACHER_READING.md`).
>   - **Yangi Mustaqil Uy Vazifasi Ekotizimi (`vazifa.html`):** Har bir dars papkasida alohida fayl sifatida joylashgan interaktiv uy vazifasi ilovasi: 4 ta amaliy muhandislik topshirig'i, o'quvchi javobini yozish uchun keng matn maydonlari (textareas), brauzerda avtomatik saqlanish (LocalStorage auto-save), javoblarni tekshirish va "Yechimni ko'rish / Fix" interaktiv kaliti, 10 ballik rasmiy baholash mezonlari hamda bitta bosishda qog'ozga yoki PDF ga chiqarish (Print A4).
>   - **Prezentatsiyada Jonli Testlar va Kod Tuzatishlari (Quiz & Fixes):** Taqdimot slaydlari ichida variantli kiber-testlar (`.quiz-box`), real-vaqt to'g'ri/noto'g'ri fikr-mulohazasi hamda rasmiy yechimni ko'rsatuvchi "Yechimni ko'rish / Fix" interaktiv tugmasi.
>   - **O'qituvchi Metodik Qo'llanmasi (`TEACHER_READING.md`):** O'qituvchining dars oldi 5 daqiqalik konspekti, slaydlar arxitekturasi, testlarning to'liq javoblar kaliti, o'quvchilar yo'l qo'yadigan odatiy xatolar va ularni bartaraf etish (Remediation) bo'yicha ko'rsatmalar.
>   - Barcha 15 ta HTML fayllari `verify_i18n.py` orqali 100% auditdan o'tdi, `index.html` portaliga yangi `.btn-hw` tugmasi bilan ulandi hamda `REJA.md` va `reja.html` yangilandi.
>   - **Avtomatlashtirilgan Google Forms Ekosistemasi (`google_forms.html` & `google_form.gs`):** O'qituvchining barcha kohortalar uchun testlarni qo'lda bittalab Google Forms da terish ehtiyojini yo'qotuvchi 1-klikli avtomatlashtirish tizimi ishlab chiqildi. `scripts/generate_google_forms.py` orqali har bir dars papkasida tayyor `google_form.gs` (FormApp skripti), markaziy `scripts/all_google_forms.gs` hamda interaktiv `google_forms.html` vizual studiyasi yaratildi. O'qituvchi 1 ta bosishda kodni nusxalab, `https://script.new` da "Run" (▶️) tugmasini bosishi bilan 3 soniyada Google Drive da tayyor Quiz Form (ballar, avto-tekshirish, o'quvchi F.I.Sh., sinf tanlovi va izohlar) yaratiladi. Bosh portal (`index.html`), `REJA.md` va `reja.html` ga binafsharang `📋 Google Form` tugmalari bilan to'liq integratsiya qilindi.

> - **Tajribaviy Dars (Kompyuter Asosiy Xotirasi: RAM, ROM, EPROM, DRAM, VRAM va Xotira Arxitekturasi):** Universitet va akademik etalon taqdimot (`assets/reference/reference-presentation.pptx`) asosida yaratilgan to'liq eksperimental dars (`classes/experimental/01-dars-asosiy-xotira-ram-va-rom/`): pastki panelsiz (Zero Bottom Bar) 100% toza ekran, tepada o'ng burchakda suzuvchi oynaviy kapsula (Floating Glassmorphic Pill: `[UZ | RU | EN]`, mavzu, izohlar va yordamchi modallar), pastda o'ng burchakda suzuvchi slayd hisoblagichi (`‹ 01 / 16 ›`), 16 ta chuqur akademik slayd va haqiqiy kremniy eksponatlari (MROM chipi, Texas Instruments PROM chipi va interaktiv 15V sug'urta kuydirgichi, EPROM korpusi va shaffof kvarts darchasi orqali 254 nm UV fotonlar bilan fotoelektrik o'chirish simulyatori, 6-tranzistorli SRAM triggeri, 1T1C DRAM katakchasi va JEDEC 64 ms majburiy yangilanish simulyatori, VRAM Frame Buffer va Triple Buffering hisobi, SIMM 30/72 pin va 64-bit mustaqil DIMM shinalari, soat impulsining ikkala frontida ma'lumot uzatuvchi DDR evolyutsiyasi, 10 ballik mezon). 100% trilingual in-place i18n (`prezentatsiya.html`), 2 betlik chop etiladigan A4 ishchi varaqa (`varaqa.html`) va batafsil o'qituvchi metodik qo'llanmasi (`TEACHER_READING.md`). Bosh portalga (`index.html`) integratsiya qilindi.
> - **10–11-sinf (3-hafta 13-dars LLM Ichki Mexanikasi: Kontekst, KV Cache, Sampling va Few-Shot):** Yangi Floating Glassmorphic UI (Zero Bottom Bar, suzuvchi [UZ | RU | EN] va vositalar doki, suzuvchi hisoblagich va dars fazasi nishoni) hamda chuqur universitet/etalon darajasidagi arxitektura tushuntirish uslubiga to'liq o'tkazildi: BPE bayt tahlili va UTF-8 jarimasi (interaktiv jonli tokenizator stendi), Self-Attention $O(N^2)$ kvadratik masshtablanish fizikasi, KV Cache tenzorlarining GPU VRAM (HBM) xotirasini band qilish matematikasi (interaktiv 80GB A100 VRAM kalkulyatori), Stenfordning "Lost in the Middle" U-simon e'tibor pasayishi va "Sendvich" arxitekturasi, Model Konstitutsiyasi (System Prompt rollar vakolati), Masshtablangan Softmax va Temperature sampling matematikasi (interaktiv T=0 dan 1.5 gacha bo'lgan ehtimollik taqsimoti slayderi), Top-K va Top-P (Nucleus) dumni qirqish filtrlari, Few-Shot in-context vektor langari, DFA Constrained Decoding (100% kafolatlangan valid JSON), Prompt Injection kiber-hujumi va Dual-LLM himoya quvuri, Git va CI/CD da PromptOps avtomatik Evals testi hamda 10 ballik mezon. 14 ta 100% trilingual in-place slayddan iborat taqdimot (`prezentatsiya.html`), Trap #3 talablariga mos 2 betlik A4 varaqa (`varaqa.html`) va `lab/index.html` to'liq validatsiyadan o'tkazildi.

> - **7–8-sinf (7-hafta 29-dars GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi):** 7–8-sinflar uchun to'liq brauzer ichidagi **Target GPS Pathfinding & Route Studio** (`classes/7-8-sinf/7-hafta/29-dars-gps-navigatsiya-va-eng-qisqa-yol/studio/index.html`) yaratildi: 24x14 o'lchamli shahar koordinatalar matritsasi, Start (Uy) va Target (Maktab) nuqtalari, Binolar (Devorlar) va Tirbandlik (Traffic Jam, og'irlik = 4) chizish asboblari, shahar shablonlari (Clean Grid, Traffic Jam Bypass, City Maze), jonli poyga qildiruvchi Ko'r to'lqinli qidiruv (BFS) va Aqlli kompas ($F=G+H$, Manxetten evristikasi) algoritmlari, real-vaqt telemetriyasi (Explored nodes, Path length, Total cost, Efficiency %), `route.json` eksporti, 4 ta kvest (10 ballik mezon) va chop etiladigan "Junior Route Engineer" Sertifikati. 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) va o'qituvchi tayyorgarlik qo'llanmasi (`TEACHER_READING.md`) tayyorlandi, portalga (`index.html`) va o'quv rejasiga (`REJA.md`) to'liq integratsiya qilindi.
> - **5–6-sinf (7-hafta 21-dars Raqamli Iz va Shaxsiy Maxfiylik: Internet Biz Haqimizda Nimani Biladi?):** 5–6-sinflar uchun to'liq brauzer ichidagi **Target Privacy & Digital Footprint Studio** (`classes/5-6-sinf/7-hafta/21-dars-raqamli-iz-va-maxfiylik/studio/index.html`) yaratildi: fotosuratlar ichidagi yashirin EXIF metama'lumotlari detektori (kamera modeli, sana-vaqt va xaritadagi aniq GPS kenglik/uzunlik koordinatalari orqali uy manzilini fosh qilish hamda bir klikda "Strip EXIF" orqali tozalash), faol va nofaol raqamli izlar matritsasi, 3 ta sinfdosh profiling kiber-iz skaneri (Persona OSINT: `@gamer_sherzod2014`, `@anora_dance`, `@cyber_guard_pro`), 4 bosqichli Maxfiylik Qalqoni (Privacy Shield: 15% dan 100% gacha kuchaytirish), "Katta Ekran Qoidasi" (Billboard Rule), 4 ta kvest (10 ballik mezon) va chop etiladigan "Privacy Guardian" Sertifikati. 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) va o'qituvchi tayyorgarlik qo'llanmasi (`TEACHER_READING.md`) tayyorlandi, portalga (`index.html`) va o'quv rejasiga (`REJA.md`) to'liq integratsiya qilindi.
> - **10–11-sinf (7-hafta 31-dars Penetration Testing & Ethical Hacking: O'z Zaiflik Skaneringni Dasturlash):** 10–11-sinflar uchun to'liq brauzer ichidagi **Target Pentest Studio** (`classes/10-11-sinf/7-hafta/31-dars-penetration-testing-va-ethical-hacking/studio/index.html`) va avtonom CLI skaner dasturi (`classes/10-11-sinf/7-hafta/31-dars-penetration-testing-va-ethical-hacking/scanner/`) yaratildi: PTES 5 bosqichli metodologiyasi (Recon, Scanning, Exploitation, Reporting, Remediation), OWASP API Top 10 ning 1-raqamli bo'shlig'i BOLA/IDOR (Broken Object Level Authorization), 4 ta HTTP Security Headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options), RegEx orqali ochiq AWS kalitlari va JWT tokenlar sizishini fosh etish, SSRF va Cloud Metadata (`169.254.169.254`) xuruji (Capital One keysi), matematik CVSS v3.1 xavf kalkulyatori (Base score 0.0–10.0), rangli ANSI telemetriya terminali, `security-report.json` eksporti, 4 ta kvest (10 ballik mezon) va Ethical Hacker & Security Auditor Sertifikati. 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) va o'qituvchi tayyorgarlik qo'llanmasi (`TEACHER_READING.md`) tayyorlandi, portalga (`index.html`) va o'quv rejasiga (`REJA.md`) to'liq integratsiya qilindi.
> - **9-sinf (6-hafta 26-dars Ilg'or Backend Muhandisligi: MVC Arxitekturasi va Relyatsion SQLite):** 9-sinflar uchun to'liq brauzer ichidagi **MVC Backend & Relational Database Studio** (`classes/9-sinf/6-hafta/26-dars-mvc-backend-va-relyatsion-baza/studio/index.html`) va Node.js server starter loyihasi (`classes/9-sinf/6-hafta/26-dars-mvc-backend-va-relyatsion-baza/backend/`) yaratildi: Model-View-Controller (MVC) arxitekturasi, `Single Responsibility Principle` (SRP), SQLite reliesion ma'lumotlar bazasida `users`, `products` va `orders` jadvallari, Foreign Key (`orders.user_id ➔ users.id`) orqali 1-to-Many aloqalar, `INNER JOIN` so'rovlari orqali mijoz va tovar ma'lumotlarini birlashtirish, Express 4.19 da modulli marshrutlash (`routes/orderRoutes.js`), kontroller validatsiyasi va HTTP status kodlari (`200 OK`, `201 Created`, `400 Bad Request`), animatsiyali so'rov konveyeri, 4 ta muhandislik kvesti (10 ballik mezon) va chop etiladigan Junior MVC Backend Architect Sertifikati. 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) va o'qituvchi tayyorgarlik qo'llanmasi (`TEACHER_READING.md`) tayyorlandi, portalga (`index.html`) va o'quv rejasiga (`REJA.md`) to'liq integratsiya qilindi.

> - **7–8-sinf (6-hafta 28-dars FUT Katta Auksion Turniri, Web-Deploy & Game Jam Finali):** 6 haftalik butun modulning cho'qqisi bo'lgan **FUT Live Auction & Tournament Arena** (`classes/7-8-sinf/6-hafta/28-dars-fut-auksion-turniri-va-deploy/arena/index.html`) yaratildi: 1,500,000 tangalik boshlang'ich byudjet, real-vaqt auksion savdolashuvi (Bid vs Buy Now), +15 soniyalik Anti-Sniping bot himoyasi, Winner's Curse tahlili, 8 jamoalik pley-off to'ri (1/4 Final, 1/2 Final, Katta Final), stoxastik Match Engine, jonli sharhlar lentasi, Blob API orqali JSON eksporti, GitHub va Vercel ga deploy yo'riqnomasi, mobil smartfonlar uchun SVG QR-kod generatori, 4 ta amaliy kvest (10 ballik mezon) va chop etiladigan Chempionlik Diplomi. 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) tayyorlandi, portalga (`index.html`) va o'quv rejasiga (`REJA.md`, `reja.html`) to'liq ulandi.
> - **7–8-sinf (6-hafta 27-dars Squad Building Challenges — SBC Solver Studio & Predikatlar):** Keraksiz kartalarni saralab yoqish va eksklyuziv mukofot olish mexanikasini o'rgatuvchi to'liq **FUT SBC Solver Studio** (`classes/7-8-sinf/6-hafta/27-dars-sbc-kartalar-almashinuvi/studio/index.html`) yaratildi: Constraint Satisfaction Problem (CSP) muhandisligi, `Array.prototype.filter()`, `reduce()`, `every()` va `new Set()` predikatlari, 3 xil qiyinlikdagi SBC (Bronze Upgrade, PL Hybrid, Master Icon Zidane), 11 talik taktik maydon slotlari, real-vaqt talablar validatori (Requirements Checklist), aqlli avto-saralash CSP algoritmi, olovli "Burn Cards" animatsiyasi va Untradeable mukofot berilishi, 4 ta amaliy kvest (10 ballik mezon) va chop etiladigan SBC Master Sertifikati. 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) tayyorlandi, portalga (`index.html`) va o'quv rejasiga (`REJA.md`, `reja.html`) to'liq ulandi.

> - **5–6-sinf (6-hafta 20-dars Kiber-Firibgarlar Ertagi: Ijtimoiy Muhandislik va 'Tekin Robux' Qopqoni — Cyber Detective Studio):** 5–6-sinflar uchun to'liq brauzer ichidagi **Cyber Detective Studio** (`classes/5-6-sinf/6-hafta/20-dars-ijtimoiy-muhandislik-va-kiber-aldovlar/studio/index.html`) yaratildi: real chatlar simulyatsiyasi (Roblox, Discord, Telegram, Brawl Stars), 6 ta kiber-aldov ssenariysi ("Tekin 10,000 Robux", "Soxta Xavfsizlik Admini", "Do'stning O'g'irlangan Profili", "Pro Booster", "Soxta Olimpiada", "Telegram Premium QR Qopqoni"), 4 ta kiber-psixologik tuzoq detektori (Sun'iy shoshiltirish / Urgency, Tekin pishloq / Baiting, Qo'rqitish / Fear, Do'st niqobi / Impersonation), interaktiv xavfli so'zlarni belgilash (Highlight Red Flags), 10 ballik mezon bo'yicha baholash va chop etiladigan Kiber-Detektiv Sertifikati. 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`), o'qituvchi qo'llanmasi (`TEACHER_READING.md`) tayyorlandi, portalga (`index.html`) va o'quv rejasiga (`REJA.md`) to'liq integratsiya qilindi.

> - **10–11-sinf (6-hafta 26–30-darslar Cloud Security, S3 Buckets, Terraform, Vault & DevSecOps Capstone):** 10–11-sinflar uchun 6-haftaning 5 ta to'liq darsi yaratildi:
>   - **26-dars (Cloud Arxitekturasi va Umumiy Mas'uliyat Modeli):** NIST SP 800-145, IaaS vs PaaS vs SaaS, Gartner 99% qoidasi, Tesla Kubernetes breach tahlili, 12 slaydli taqdimot, 2 betlik A4 varaqa va yo'riqnoma.
>   - **27-dars (Ochiq S3 Chelaklar va S3 Defender Studio):** 4 ta BPA qalqoni (`BlockPublicAcls`, `IgnorePublicAcls`, `BlockPublicPolicy`, `RestrictPublicBuckets`), JSON siyosatidagi `aws:sourceVpce` sharti, interaktiv S3 Policy Defender Studio (`studio/index.html`) va botnet mudofaasi.
>   - **28-dars (IaC va Terraform Xavfsizligi):** HCL tili, `terraform.tfstate` dagi ochiq sirlar halokati, Checkov AST linteri, CIS AWS Benchmark 2.1, S3 Remote State + KMS, interaktiv Terraform Security Studio (`studio/index.html`).
>   - **29-dars (HashiCorp Vault va Maxfiy Kalitlar Boshqaruvi):** Secret Sprawl xavfi, Shamir's Secret Sharing (3/5 unseal), Dynamic Secrets with TTL (avtomatik `DROP USER`), AppRole mashina identifikatsiyasi, Uber 2022 tahlili, Vault Commander Studio (`studio/index.html`).
>   - **30-dars (DevSecOps Quvuri va Cloud Audit Demo Day):** GitHub Actions dagi 4 ta xavfsizlik darvozasi (Gitleaks, Semgrep SAST, Checkov IaC, Trivy Container CVE), "Break the Build" (Exit Code 1) qoidasi, SolarWinds Sunburst tahlili, DevSecOps CI/CD Simulator Studio (`studio/index.html`) va Master DevSecOps Diplomi.
>   - Barcha 14 ta fayl 100% trilingual in-place standartda tekshirildi (`verify_i18n.py`), portalga (`build_portal.py` orqali `index.html` 105 ta dars) va o'quv rejasiga (`REJA.md`) to'liq ulandi.

> - **7–8-sinf (6-hafta 26-dars Sport Iqtisodiyoti: Tangalar Balansi, Coin Sink & Inflyatsiya):** O'yin iqtisodiyoti muhandisligi va valyuta barqarorligini o'rgatuvchi to'liq **FUT Central Bank & Game Economy Simulator** (`classes/7-8-sinf/6-hafta/26-dars-sport-iqtisodiyoti-valyuta/lab/index.html`) yaratildi: pul massasi M2, o'yin mukofotlari orqali emissiya (Minting), EA 5% auksion savdo solig'i, paketlar va turnir to'lovlari orqali tangalarni yoqish (Coin Sinks), narxlar indeksi (CPI) telemetriyasi, Valve iqtisodchisi Yanis Varoufakis amaliy keysi, giperinflyatsiyaga qarshi avtomatik fiskal siyosat regulyatori, 4 ta kvest (10 ballik mezon) va Audit Sertifikati. 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) yaratildi, portalga (`index.html`) va o'quv rejasiga (`REJA.md`, `reja.html`) to'liq ulandi.
> - **7–8-sinf (6-hafta 25-dars FUT Pack Opening Studio & Ehtimolliklar Nazariyasi):** O'yinlardagi karta paketlari (Loot Boxes) mexanikasini o'rgatuvchi to'liq **FUT Pack Opening Studio** (`classes/7-8-sinf/6-hafta/25-dars-fut-pack-opening/studio/index.html`) yaratildi: Math.random() stoxastik generatori, CDF (Kumulyativ taqsimot funksiyasi) bo'yicha oraliqlar (Icon 0.5%, Walkout 4.5%, Rare Gold 20%, Common Gold 75%), Web Audio API orqali sintez qilingan real ovoz effektlari (fanfara, barabanlar, tangalar jarangi), 3D pack ochilish va 4 bosqichli Walkout sahnalashtirish shousi (chiroqlar &rarr; bayroq &rarr; pozitsiya &rarr; klub &rarr; yulduz), 45+ real o'yinchilar bazasi (Mbappé, Haaland, Bellingham, Rodri, Yamal, Pele va boshqalar), Qimorboz xatosi (Gambler's Fallacy) va Expected Value (EV -54% Coin Sink) tahlili, Yevropa Ittifoqi (EU) Loot Box shaffoflik qonunchiligi talabi, 50,000 tangalik boshlang'ich byudjet, Quick Sell orqali tanga qaytarish, Club ombori, 4 ta amaliy kvest (10 ballik mezon) va chop etiladigan Audit Sertifikati. 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) yaratildi, portalga (`index.html`), o'quv rejasiga (`REJA.md`, `reja.html`) to'liq ulandi.
> - **9-sinf (5-hafta 22-dars Tarmoq Xavfsizligi va Wireshark & Nmap Studio):** O'quvchilar noutbuklarida Wireshark o'rnatish huquqlari (root/pcap drayverlar) bo'lmasligi va maktab tarmog'ida Nmap port skanerining IDS blokirovkalariga tushish xavfini bartaraf etish uchun to'liq brauzer ichidagi **Wireshark & Nmap Studio** (`classes/9-sinf/5-hafta/22-dars-tarmoq-xavfsizligi-va-paket-tahlili/studio/index.html`) yaratildi: real vaqtli paketlar oqimi telemetriyasi, protokol ranglari (HTTP, TCP, TLS 1.3, DNS, ARP), qidiruv filtrlari (`http.request.method == "POST"`, `tcp.flags.syn == 1`, `tls`), daraxtsimon protokol tahlili (Ethernet II, IPv4, TCP, JSON payload), xom Hex & ASCII damplari, ochiq matndagi login/parol (`SuperSecret2026!`) o'g'irlanishi, TLS 1.3 shifrlangan ma'lumotlar bilan taqqoslash, interaktiv Nmap skaneri (22-SSH, 80-HTTP zaif ochiq port, 443-HTTPS, 3306-MySQL xavfli ochiq baza), 4 ta kvest (10 ballik mezon) hamda chop etiladigan Tarmoq Mudofaasi Audit Sertifikati. Prezentatsiya, varaqa, o'quv portali (`index.html`) va `REJA.md` ga to'liq integratsiya qilindi.
> - **9-sinf (5-hafta 21-dars Linux Server Hardening & SSH Defense Studio):** O'quvchilarda root huquqlari bo'lmasligi va maktab tarmog'idan uzilib qolish xavfini bartaraf etish uchun to'liq brauzer ichidagi **Linux Server Hardening Terminal Studio** (`classes/9-sinf/5-hafta/21-dars-linux-server-va-ssh-himoyasi/studio/index.html`) yaratildi: real vaqtda 22-portga tushayotgan botnet brute-force hujumlari telemetriyasi, bash terminal emulyatori (`xterm-256color`), Ed25519 kalit juftligini yaratish va yuklash (`ssh-keygen`, `ssh-copy-id`), interaktiv `nano /etc/ssh/sshd_config` muharriri (Port 2222, PermitRootLogin no, PasswordAuthentication no), UFW devori (Default Deny, Port 2222 allow), Fail2ban avtomatik iptables blokirovkasi, xavfsizlik bali (20/100 dan 100/100 gacha) va Audit Sertifikati eksporti. Prezentatsiya, varaqa, o'quv portali (`index.html`) va `REJA.md` ga to'liq integratsiya qilindi.
> - **9-sinf (4-hafta 19.5-dars Vibecoding E-Commerce Backend & Postman Studio):** 19-dars (Backend asoslari) va 20-dars (Full-Stack Deploy) orasidagi amaliy ko'prik sifatida to'liq brauzer ichidagi **E-Commerce Backend & Postman Studio** (`classes/9-sinf/4-hafta/19.5-dars-ecommerce-backend-va-postman/studio/index.html`) yaratildi: `users` va `orders` relying jadvallari, moliyaviy balans nazorati (`user.balance < amount` -> 400 Bad Request), to'liq CRUD (GET, POST, PATCH, DELETE) marshrutlari, buyurtma holatini PATCH orqali yangilash (`pending` -> `completed`), Postman simulyatori va avtotestlar runneri (`pm.test()`), tayyor kolleksiya fayli (`ecommerce_postman_collection.json`), to'liq ishchi `server.js` va `package.json`, 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) tayyorlandi, portalga (`index.html`) va o'quv rejasiga (`REJA.md`, `reja.html`, DOCX) ulandi.
> - **Yillik Taqvim-Mavzu Ish Rejasi (36 Hafta / 4 Chorak — 2026–2027 o'quv yili):** Maktab ma'muriyati va o'qituvchi uchun 36 haftalik to'liq yillik o'quv rejasi ishlab chiqildi: barcha 4 ta chorak (1-Chorak: 1–9, 2-Chorak: 10–18, 3-Chorak: 19–27, 4-Chorak: 28–36 haftalar), 4 ta kohorta (`10-11-sinf`, `9-sinf`, `7-8-sinf`, `5-6-sinf` — 31 soat/hafta, yillik ~1,116 akademik soat) va `assets/reja_vibecoding.docx` dagi 108 darslik Yagona Vibecoding Dasturi to'liq integratsiya qilindi. Rasmiy Microsoft Word hujjatlari (`TARGET_ISH_REJASI_2026_2027.docx`, `assets/TARGET_ISH_REJASI_2026_2027.docx`, sinflar bo'yicha alohida `.docx` fayllar va `assets/YILLIK_ISH_REJASI_36_HAFTA_108_DARS.docx`), rasmiy `REJA.md` (110 KB) hamda zamonaviy, interaktiv va trilingual `reja.html` (1.37 MB) portali yaratildi.
> - **10–11-sinf (5-hafta 25-dars SOC Simulyatsiyasi va Kiber-Insident Boshqaruvi — SOC Dashboard Studio):** Qog'ozda murakkab log o'qish va quruq nazariya o'rniga to'liq brauzer ichidagi **SOC Dashboard Simulator** (`classes/10-11-sinf/5-hafta/25-dars-soc-simulyatsiyasi-va-insident-boshqaruvi/studio/index.html`) yaratildi: jonli 12,000+ EPS telemetriya monitori, Tier 1 Triage signallar navbati, SSH Brute-Force IP-sini UFW orqali bloklash, Nginx web-shell orqali buzilgan `web-srv-01` xostini EDR orqali izolyatsiya qilish (Host Isolation), interaktiv YAML muharririda Nginx -> Bash qoidasini sinab, Splunk SPL va Elastic KQL ga kompilyatsiya qilish, NIST SP 800-61 bo'yicha 5 Whys (5 Nega?) ildiz tahlili va rasmiy Blameless Post-Mortem hisoboti (MTTD: 4 min, MTTR: 18 min), 4 ta amaliy kvest (10 ballik mezon). 12 slayddan iborat 100% trilingual taqdimot (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) yangilandi va portalga (`index.html`) ulandi.
> - **10–11-sinf (5-hafta 24-dars AI Model Xavfsizligi va Adversarial Hujumlar — AI Red Teaming Studio):** Murakkab Python/PyTorch sozlashlari va quruq formulalar o'rniga to'liq brauzer ichidagi **AI Red Teaming Studio** (`classes/10-11-sinf/5-hafta/24-dars-ai-model-xavfsizligi-va-adversarial-attacks/studio/index.html`) yaratildi: vizual FGSM (Fast Gradient Sign Method) shovqin laboratoriyasi (Epsilon &epsilon; slayderi orqali inson ko'zi sezmas 3% shovqin bilan avtopilot ko'rish modelini "Stop" belgisidan "80 km/soat tezlik"ka ag'darish simulyatsiyasi), modelni qayta mustahkamlovchi Adversarial Training himoyasi, korporativ LLM yordamchisi va 5 xil Red Teaming hujum ssenariysi (Direct DAN, Base64, Roleplay, Indirect injection), ko'p qatlamli NeMo Guardrails konfiguratsiyasi (Heuristic Regex, Shannon Entropiya, Output Canary Trap `CANARY_SEC_TARGET_99`, PII maskalash), MITRE ATLAS tahdidlar matritsasi hamda 4 ta amaliy kvest (10 ballik mezon). 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) yangilandi va portalga (`index.html`) ulandi.
> - **10–11-sinf (5-hafta 23-dars API Xavfsizligi va Rate Limiting — Token Bucket & HMAC Studio):** O'quvchilar uchun murakkab terminal/Redis sozlashlari o'rniga to'liq brauzer ichidagi **API Defender Studio** (`classes/10-11-sinf/5-hafta/23-dars-api-xavfsizligi-va-rate-limiting/studio/index.html`) yaratildi: jonli fizika bilan to'lib turuvchi Token Bucket chelagi (refill rate va capacity boshqaruvi), 50 RPS DDoS portlash hujumi va avtomatik HTTP 429 Too Many Requests filtri, mahalliy `window.crypto.subtle` (WebCrypto API) orqali bank darajasidagi HMAC-SHA256 so'rov imzolash, pul o'tkazmasini soxtalashtirish (Tamper Attack: $100 -> $999,999) va HTTP 403 xatosi, bir martalik Nonce keshini tekshirish orqali Replay Attack fosh etilishi, OWASP API Top 10 inspektori hamda 4 ta amaliy kvest (10 ballik mezon). 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) yangilandi va portalga (`index.html`) ulandi.
> - **10–11-sinf (5-hafta 22-dars Zero Trust & IAM Arxitekturasi — Capital One Keysi va PDP Simulyatori):** Qog'ozda murakkab AWS IAM JSON yozish va quruq NIST SP 800-207 nazariyasi o'rniga to'liq brauzer ichidagi **Zero Trust & IAM Studio** (`classes/10-11-sinf/5-hafta/22-dars-zero-trust-va-iam-arxitekturasi/studio/index.html`) yaratildi: aeroport xavfsizligi analogiyasi (har bir darvoza va uchuvchi kabinasi alohida tekshirilishi), jonli Zero Trust PDP Gatekeeper (Alice, Bob, Eve xodimlarining qurilma holati, ofis IP-si, ish vaqti va MFA signallarini 5 bosqichli tahlil qilish), Capital One $80,000,000 kiber-halokati poligoni (zaif `Action: *, Resource: *` wildcard siyosatini Least Privilege ga o'tkazib, xakerning SSRF hujumini 0 talik zarar bilan qaytarish), RBAC vs ABAC matritsasi, 4 ta amaliy kvest (10 ballik mezon). 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) qayta ishlandi va portalga (`index.html`) ulandi.
> - **10–11-sinf (5-hafta 21-dars Kriptografiya Asoslari — AES-256, RSA va Bit Tamper):** Universitet darajasidagi quruq matematik formulalar va murakkab terminal/OpenSSL to'siqlari o'rniga to'liq brauzer ichidagi **Crypto Studio** (`classes/10-11-sinf/5-hafta/21-dars-kriptografiya-aes-va-rsa/studio/index.html`) yaratildi: mahalliy `window.crypto.subtle` (WebCrypto API) orqali AES-256-GCM shifrlash va 1-baytli Bit Tamper hujumi (AEAD Authentication Tag buzilishi), RSA-2048 ochiq/yopiq kalitlar juftligi va xabarlar almashinuvi (Alice & Bob), SHA-256 xeshlash va ko'chki effekti (Avalanche effect), 4 ta interaktiv kvest (10 ballik mezon). 12 slayddan iborat 100% trilingual taqdimot (`prezentatsiya.html`), 2 betlik A4 amaliy varaqa (`varaqa.html`) qayta ishlandi va portalga (`index.html`) ulandi.
> - **5–6-sinf (5-hafta 19-dars Zararli Dasturlar, Troyanlar va Tekin Modlar Qopqoni):** 5-haftaning yakunlovchi kiber-qalqon darsi sifatida to'liq **Malware Scanner Studio** (`classes/5-6-sinf/5-hafta/19-dars-zararli-dasturlar-va-troyanlar/scanner/index.html`) yaratildi: Qadimgi Troya afsonasi va dasturiy troyanlar mexanizmi, 4 ta malware yirtqichi (Trojan, InfoStealer/Lumma/RedLine, Ransomware, Keylogger), xakerlarning `.png.exe` ikki qavatli kengaytma (Double Extension) hiylasi, 'Antivirusni o'chir (False Positive)' yolg'oni fosh qilinishi, SHA-256 kriptografik barmoq izi, 70 dvigatelli VirusTotal tahlili, jonli Sandbox qumloq monitorida fayl tizimi, reestr va C2 tarmoq o'g'riliklarini fosh qilish, 6 ta realistik keys (APK, zip.exe, BAT, SCR, PDF, PNG) bo'yicha tergov va baholash. 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) tayyorlandi va portalga (`index.html`) ulandi.
> - **7–8-sinf (5-hafta 24-dars FUT Transfer Market & Virtual Iqtisodiyot):** O'yin ichidagi bozor iqtisodiyoti va auksion mexanikasini o'rgatuvchi to'liq **Transfer Market Studio** (`classes/7-8-sinf/5-hafta/24-dars-fut-transfer-market/market/index.html`) yaratildi: Talab va taklif qonuni (Supply & Demand), auksion savdolashuvi (Bid vs Buy Now), oxirgi soniyalarda botlardan himoya qiluvchi Anti-Sniping taymeri (+30s), giperinflyatsiyaga qarshi EA 5% Soliq algoritmi (Coin Sink), breakeven va Trade Profit hisob-kitobi, 1,000,000 tangalik byudjet, 6 ta amaliy kvest (10 ballik mezon). 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) tayyorlandi va portalga (`index.html`) ulandi.
> - **7–8-sinf (5-hafta 23-dars FUT Match Engine & Taktik Duel Simulyatori):** 21 va 22-darslarning mantiqiy cho'qqisi sifatida to'liq 90 daqiqalik o'yin simulyatori yaratildi (`classes/7-8-sinf/5-hafta/23-dars-fut-match-engine/simulator/index.html`): Finite State Machine (FSM) o'yin hodisalari tsikli (`KICKOFF`, `BUILDUP`, `MIDFIELD_DUEL`, `ATTACK_THIRD`, `SHOT_EVENT`), stoxastik ehtimollik formulasi ($P = Stat_{Att} / (Stat_{Att} + Stat_{Def}) + \Delta Chem$), jonli xG (Expected Goals) hisobi, dinamik 2D radar maydoni, to'p harakati animatsiyasi, UZ/RU/EN tillarida sharhlovchi lentasi (Live Commentary Ticker), tezlik rejimlari (1x, 2x, 5x, Instant), 6 ta amaliy kvest (10 ballik mezon). Prezentatsiya va varaqa tayyor.
> - **7–8-sinf (5-hafta 22-dars FUT Squad Builder & Kimyo Algoritmi):** 21-darsning bevosita davomi sifatida to'liq 11 talik taktik tarkib qurish studiyasi yaratildi (`classes/7-8-sinf/5-hafta/22-dars-fut-squad-builder/builder/index.html`): EA Sports FC uslubidagi yashil taktik maydon, 4-3-3, 4-4-2 va 3-5-2 sxemalari, o'yinchilar orasidagi SVG dinamik kimyo zanjirlari (Strong, Good, Dead links), jamoaviy OVR kuchi va 33 ballik kimyo hisob-kitob algoritmi, o'yinchilar transfer bozori, pozitsiya xatoliklari tekshiruvi hamda 6 ta amaliy kvest (10 ballik mezon). Prezentatsiya va varaqa tayyor.
> - **9-sinf (4-hafta 19-dars Backend Asoslari — Node.js, Express va REST API):** 9-sinflar uchun mantiqiy bo'shliq to'ldirildi. O'quvchilar 18-darsda o'rgangan SQLite ma'lumotlar bazasini (`shop.db`) to'g'ridan-to'g'ri Express serveriga ulaydigan to'liq mustaqil **Express API Studio & Postman Simulyatori** (`classes/9-sinf/4-hafta/19-dars-backend-express-va-rest-api/lab/index.html`) yaratildi.
> - **7–8-sinf (5-hafta 21-dars FUT Card Studio):** EA Sports FC uslubidagi interaktiv o'yinchi kartochkalari studiyasi (`classes/7-8-sinf/5-hafta/21-dars-fut-card-studio/studio/index.html`), brauzer ichida `FileReader` orqali fotosurat yuklash, 6 ta asosiy stat slayderlari va pozitsiyaga asoslangan vaznli OVR reyting algoritmi. Prezentatsiya va varaqa tayyor.
> - **Minimalist Tipografik Prezentatsiyalar, Interaktiv Testlar & Mustaqil Uy Vazifasi (`vazifa.html`) 2-To'lqini:** 1-Chorak darslari uchun yangi avlod minimalist tipografik prezentatsiyalari, interaktiv uy vazifalari (`vazifa.html`) va avtomatlashtirilgan kiber-testlar (`test.html`) tizimi 4 ta qo'shimcha darsga kengaytirildi (jami 9 ta to'liq sinov tizimi):
>   - **10–11-sinf (7-hafta 31-dars Penetration Testing & Ethical Hacking):** 12 slaydli minimalist taqdimot, BOLA/IDOR zaifliklarini tuzatish (`Fix`), 4 ta amaliy vazifadan iborat interaktiv `vazifa.html` va 10 ta testdan iborat avtomatik `test.html`.
>   - **9-sinf (6-hafta 26-dars MVC Backend & Relyatsion Baza):** 12 slaydli minimalist taqdimot, SQL injection va MVC marshrutlash `Fix` kaliti, 4 ta amaliy vazifadan iborat `vazifa.html` va 10 ta testdan iborat `test.html`.
>   - **7–8-sinf (7-hafta 29-dars GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi):** 12 slaydli minimalist taqdimot, Manhattan evristikasi va Tirbandlik `Fix` kaliti, 4 ta amaliy vazifadan iborat `vazifa.html` va 10 ta testdan iborat `test.html`.
>   - **5–6-sinf (7-hafta 21-dars Raqamli Iz va Shaxsiy Maxfiylik):** 12 slaydli minimalist taqdimot, EXIF GPS va Katta Ekran qoidasi `Fix` kaliti, 4 ta amaliy vazifadan iborat `vazifa.html` va 10 ta testdan iborat `test.html`.
>   - **Avtomatik Baholash va Natijalarni O'qituvchiga Jo'natish:** Har bir `test.html` o'quvchi ism-familiyasi, sinfi, elektron pochtasi va to'plagan ballarini avtomatik baholab, to'liq hisobotni o'qituvchi pochtasiga (`usmonovismoiljon12@gmail.com`) jo'natish tizimi bilan ta'minlandi.
>   - Barcha prezentatsiyalar, varaqalar, vazifalar va testlar 100% in-place trilingual (UZ, RU, EN) talablariga to'liq mos kelishi `python3 scripts/verify_i18n.py` orqali tasdiqlandi va bosh portal (`index.html`) bilan integratsiya qilindi.



