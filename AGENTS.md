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
| 16 | 9 | 3 | SemVer, GitHub Releases va Open Source Hamkorlik | ✅ tayyor |
| 15 | 10-11 | 4 | RAG va Embeddinglar: Chunking, Vektor Qidiruv, Kosinus | ✅ tayyor |
| 16 | 10-11 | 4 | Prompt Injection va AI Xavfsizligi: Hujum, Himoya, Red Team | ✅ tayyor |
| 17 | 9 | 4 | Docker va Konteynerlar: Tizimlararo Moslik Kafolati | ✅ tayyor |
| 18 | 9 | 4 | Ma'lumotlar Bazasi va SQL: Relyatsion Sxema, Indekslar | ✅ tayyor |
| 19 | 9 | 4 | Backend Asoslari: Node.js, Express va REST API | ✅ tayyor |
| 20 | 9 | 4 | Full-Stack Deploy va Demo Day: Prodaction Muhandislik | ✅ tayyor |
| 21 | 9 | 5 | Linux Server Hardening: SSH, UFW va Fail2ban | ✅ tayyor |
| 22 | 9 | 5 | Tarmoq Xavfsizligi va Paket Tahlili: Wireshark & Nmap | ✅ tayyor |
| 23 | 9 | 5 | Veb Zaifliklari va OWASP Top 10: SQLi & XSS | ✅ tayyor |
| 24 | 9 | 5 | Autentifikatsiya Xavfsizligi: JWT, XSS/CSRF va 2FA | ✅ tayyor |
| 25 | 9 | 5 | Kiber-Hujum Simulyatsiyasi: CTF va Red/Blue Team | ✅ tayyor |
| 21 | 10-11 | 5 | Kriptografiya Asoslari: AES-256, RSA va ECC Shifrlash | ✅ tayyor |
| 22 | 10-11 | 5 | Zero Trust va IAM Arxitekturasi: RBAC, ABAC va mTLS | ✅ tayyor |
| 23 | 10-11 | 5 | API Xavfsizligi va Rate Limiting: Token Bucket & HMAC | ✅ tayyor |
| 24 | 10-11 | 5 | AI Model Xavfsizligi: FGSM, Data Poisoning & Red Teaming | ✅ tayyor |
| 25 | 10-11 | 5 | SOC Simulyatsiyasi: SIEM, Sigma Qoidalari & MTTR | ✅ tayyor |
| 17 | 5-6 | 5 | Parollar Jangi: Xakerlar Qanday Buzadi, Brute-Force | ✅ tayyor |
| 18 | 5-6 | 5 | Fishing Detektori: Soxta Havolalar, 'Bepul Robux', 2FA | ✅ tayyor |
| 19 | 5-6 | 5 | Zararli Dasturlar va Troyanlar: 'Troyalik Ot' va Tekin Modlar | ✅ tayyor |
| 21 | 7-8 | 5 | FUT Card Studio: File API va OVR Reyting | ✅ tayyor |
| 22 | 7-8 | 5 | FUT Squad Builder: Graf va Kimyo Algoritmi | ✅ tayyor |
| 23 | 7-8 | 5 | FUT Match Engine: Taktik Duel Simulyatori | ✅ tayyor |
| 24 | 7-8 | 5 | FUT Transfer Market: Talab-Taklif va 5% Soliq | ✅ tayyor |

> **Holat yangilanishi (2026-10-08):**
> - **10–11-sinf (5-hafta 23-dars API Xavfsizligi va Rate Limiting — Token Bucket & HMAC Studio):** O'quvchilar uchun murakkab terminal/Redis sozlashlari o'rniga to'liq brauzer ichidagi **API Defender Studio** (`classes/10-11-sinf/5-hafta/23-dars-api-xavfsizligi-va-rate-limiting/studio/index.html`) yaratildi: jonli fizika bilan to'lib turuvchi Token Bucket chelagi (refill rate va capacity boshqaruvi), 50 RPS DDoS portlash hujumi va avtomatik HTTP 429 Too Many Requests filtri, mahalliy `window.crypto.subtle` (WebCrypto API) orqali bank darajasidagi HMAC-SHA256 so'rov imzolash, pul o'tkazmasini soxtalashtirish (Tamper Attack: $100 -> $999,999) va HTTP 403 xatosi, bir martalik Nonce keshini tekshirish orqali Replay Attack fosh etilishi, OWASP API Top 10 inspektori hamda 4 ta amaliy kvest (10 ballik mezon). 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) yangilandi va portalga (`index.html`) ulandi.
> - **10–11-sinf (5-hafta 22-dars Zero Trust & IAM Arxitekturasi — Capital One Keysi va PDP Simulyatori):** Qog'ozda murakkab AWS IAM JSON yozish va quruq NIST SP 800-207 nazariyasi o'rniga to'liq brauzer ichidagi **Zero Trust & IAM Studio** (`classes/10-11-sinf/5-hafta/22-dars-zero-trust-va-iam-arxitekturasi/studio/index.html`) yaratildi: aeroport xavfsizligi analogiyasi (har bir darvoza va uchuvchi kabinasi alohida tekshirilishi), jonli Zero Trust PDP Gatekeeper (Alice, Bob, Eve xodimlarining qurilma holati, ofis IP-si, ish vaqti va MFA signallarini 5 bosqichli tahlil qilish), Capital One $80,000,000 kiber-halokati poligoni (zaif `Action: *, Resource: *` wildcard siyosatini Least Privilege ga o'tkazib, xakerning SSRF hujumini 0 talik zarar bilan qaytarish), RBAC vs ABAC matritsasi, 4 ta amaliy kvest (10 ballik mezon). 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) qayta ishlandi va portalga (`index.html`) ulandi.
> - **10–11-sinf (5-hafta 21-dars Kriptografiya Asoslari — AES-256, RSA va Bit Tamper):** Universitet darajasidagi quruq matematik formulalar va murakkab terminal/OpenSSL to'siqlari o'rniga to'liq brauzer ichidagi **Crypto Studio** (`classes/10-11-sinf/5-hafta/21-dars-kriptografiya-aes-va-rsa/studio/index.html`) yaratildi: mahalliy `window.crypto.subtle` (WebCrypto API) orqali AES-256-GCM shifrlash va 1-baytli Bit Tamper hujumi (AEAD Authentication Tag buzilishi), RSA-2048 ochiq/yopiq kalitlar juftligi va xabarlar almashinuvi (Alice & Bob), SHA-256 xeshlash va ko'chki effekti (Avalanche effect), 4 ta interaktiv kvest (10 ballik mezon). 12 slayddan iborat 100% trilingual taqdimot (`prezentatsiya.html`), 2 betlik A4 amaliy varaqa (`varaqa.html`) qayta ishlandi va portalga (`index.html`) ulandi.
> - **5–6-sinf (5-hafta 19-dars Zararli Dasturlar, Troyanlar va Tekin Modlar Qopqoni):** 5-haftaning yakunlovchi kiber-qalqon darsi sifatida to'liq **Malware Scanner Studio** (`classes/5-6-sinf/5-hafta/19-dars-zararli-dasturlar-va-troyanlar/scanner/index.html`) yaratildi: Qadimgi Troya afsonasi va dasturiy troyanlar mexanizmi, 4 ta malware yirtqichi (Trojan, InfoStealer/Lumma/RedLine, Ransomware, Keylogger), xakerlarning `.png.exe` ikki qavatli kengaytma (Double Extension) hiylasi, 'Antivirusni o'chir (False Positive)' yolg'oni fosh qilinishi, SHA-256 kriptografik barmoq izi, 70 dvigatelli VirusTotal tahlili, jonli Sandbox qumloq monitorida fayl tizimi, reestr va C2 tarmoq o'g'riliklarini fosh qilish, 6 ta realistik keys (APK, zip.exe, BAT, SCR, PDF, PNG) bo'yicha tergov va baholash. 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) tayyorlandi va portalga (`index.html`) ulandi.
> - **7–8-sinf (5-hafta 24-dars FUT Transfer Market & Virtual Iqtisodiyot):** O'yin ichidagi bozor iqtisodiyoti va auksion mexanikasini o'rgatuvchi to'liq **Transfer Market Studio** (`classes/7-8-sinf/5-hafta/24-dars-fut-transfer-market/market/index.html`) yaratildi: Talab va taklif qonuni (Supply & Demand), auksion savdolashuvi (Bid vs Buy Now), oxirgi soniyalarda botlardan himoya qiluvchi Anti-Sniping taymeri (+30s), giperinflyatsiyaga qarshi EA 5% Soliq algoritmi (Coin Sink), breakeven va Trade Profit hisob-kitobi, 1,000,000 tangalik byudjet, 6 ta amaliy kvest (10 ballik mezon). 12 slayddan iborat 100% trilingual prezentatsiya (`prezentatsiya.html`), 2 betlik A4 ishchi varaqa (`varaqa.html`) tayyorlandi va portalga (`index.html`) ulandi.
> - **7–8-sinf (5-hafta 23-dars FUT Match Engine & Taktik Duel Simulyatori):** 21 va 22-darslarning mantiqiy cho'qqisi sifatida to'liq 90 daqiqalik o'yin simulyatori yaratildi (`classes/7-8-sinf/5-hafta/23-dars-fut-match-engine/simulator/index.html`): Finite State Machine (FSM) o'yin hodisalari tsikli (`KICKOFF`, `BUILDUP`, `MIDFIELD_DUEL`, `ATTACK_THIRD`, `SHOT_EVENT`), stoxastik ehtimollik formulasi ($P = Stat_{Att} / (Stat_{Att} + Stat_{Def}) + \Delta Chem$), jonli xG (Expected Goals) hisobi, dinamik 2D radar maydoni, to'p harakati animatsiyasi, UZ/RU/EN tillarida sharhlovchi lentasi (Live Commentary Ticker), tezlik rejimlari (1x, 2x, 5x, Instant), 6 ta amaliy kvest (10 ballik mezon). Prezentatsiya va varaqa tayyor.
> - **7–8-sinf (5-hafta 22-dars FUT Squad Builder & Kimyo Algoritmi):** 21-darsning bevosita davomi sifatida to'liq 11 talik taktik tarkib qurish studiyasi yaratildi (`classes/7-8-sinf/5-hafta/22-dars-fut-squad-builder/builder/index.html`): EA Sports FC uslubidagi yashil taktik maydon, 4-3-3, 4-4-2 va 3-5-2 sxemalari, o'yinchilar orasidagi SVG dinamik kimyo zanjirlari (Strong, Good, Dead links), jamoaviy OVR kuchi va 33 ballik kimyo hisob-kitob algoritmi, o'yinchilar transfer bozori, pozitsiya xatoliklari tekshiruvi hamda 6 ta amaliy kvest (10 ballik mezon). Prezentatsiya va varaqa tayyor.
> - **9-sinf (4-hafta 19-dars Backend Asoslari — Node.js, Express va REST API):** 9-sinflar uchun mantiqiy bo'shliq to'ldirildi. O'quvchilar 18-darsda o'rgangan SQLite ma'lumotlar bazasini (`shop.db`) to'g'ridan-to'g'ri Express serveriga ulaydigan to'liq mustaqil **Express API Studio & Postman Simulyatori** (`classes/9-sinf/4-hafta/19-dars-backend-express-va-rest-api/lab/index.html`) yaratildi.
> - **7–8-sinf (5-hafta 21-dars FUT Card Studio):** EA Sports FC uslubidagi interaktiv o'yinchi kartochkalari studiyasi (`classes/7-8-sinf/5-hafta/21-dars-fut-card-studio/studio/index.html`), brauzer ichida `FileReader` orqali fotosurat yuklash, 6 ta asosiy stat slayderlari va pozitsiyaga asoslangan vaznli OVR reyting algoritmi. Prezentatsiya va varaqa tayyor.



