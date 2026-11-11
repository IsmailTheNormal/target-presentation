# Dizayn tizimi — Target International School

Har bir dars sahifasi shu tizimda quriladi. Yangi sahifa yozishdan oldin
shu faylni o'qing va bloklarni **nusxa qiling** — qayta o'ylab topmang.

## Ranglar

Logotipdan (`target-logo.png`) piksel darajasida olingan.

| Rol | Yorug' | Qorong'i | Nima uchun |
|---|---|---|---|
| Asosiy matn `--ink` | `#00214A` | `#E9EFF8` | Brend navy |
| Ikkilamchi `--ink-2` | `#46587A` | `#A2B4CE` | Izoh, tavsif |
| Uchinchi `--ink-3` | `#8496B0` | `#70859F` | Yorliq, eslatma |
| Fon `--bg` | `#F1F5FB` | `#061530` | Sahifa foni |
| Panel `--panel` | `#E6EDF7` | `#0E2249` | Karta foni |
| Panel-2 `--panel-2` | `#D5E1F0` | `#16305A` | Jadval sarlavhasi |
| Chiziq `--rule` | `#CBD7E7` | `#1E3A63` | Ramka, ajratgich |
| Urg'u `--accent` | `#FF1100` | `#FF3B26` | **Grafik**: chiziq, raqam, belgi |
| Urg'u matn `--accent-ink` | `#C21000` | `#FF7563` | **Matn**: yorliq, sarlavha |

**`--accent` va `--accent-ink` ni aralashtirmang.** Sof brend qizili
`#FF1100` oq fonda kichik matn uchun kontrast bo'yicha zaif. Chiziq va
belgilarga `--accent`, matnga `--accent-ink`.

Varaqa uchun qo'shimcha: `--sheet` (varaq foni: `#FFFFFF` / `#0A1D3D`),
`--hair` (nuqtali ajratgich), `--write` (yozish chizig'i).

## Shriftlar

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
```

| Rol | Shrift | Nima uchun |
|---|---|---|
| Sarlavha | **Manrope 800** | Logotipning geometrik shakliga yaqin |
| Matn | Source Sans 3 400/600 | Uzun matn uchun, kirill va lotin to'liq |
| Texnik | JetBrains Mono 400/700 | Vaqt, yorliq, prompt, raqam |

Sarlavhalarga `text-wrap: balance`, raqamli ustunlarga
`font-variant-numeric: tabular-nums`.

## Tema tizimi — uchta holat

Ko'ruvchida uch holat bor: aniq tanlangan yorug', aniq tanlangan qorong'i,
va **hech narsa tanlanmagan** (tizimga ergashadi — eng ko'p uchraydi).
Shuning uchun uchta blok ham yozilishi shart:

```css
:root{ /* to'liq yorug' palitra — HAR BIR token shu yerda e'lon qilinadi */ }

@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){ /* faqat tokenlar qayta e'lon qilinadi */ }
}

:root[data-theme="dark"]{ /* tugma bilan tanlangan qorong'i */ }
```

Rangni hech qachon faqat media yoki `[data-theme]` bloki ichida e'lon
qilmang — tanlanmagan holatda u umuman qo'llanmaydi.
`body` ga tokendan olingan `background` majburiy.

JS tomoni: `auto` → `data-theme` atributi **o'chiriladi**, `light`/`dark` →
o'rnatiladi. Tanlov `localStorage['vc-theme']` da.

## Til: In-Place i18n Standarti (data-ru va data-en)

Har bir matn bitta elementda uch tilda yoziladi:
```html
<h2 data-ru="Русский заголовок" data-en="English Title">O'zbekcha sarlavha</h2>
<p data-ru="Русский текст" data-en="English text">O'zbekcha matn</p>
<li data-ru="Русский пункт" data-en="English bullet">O'zbekcha band</li>
<span class="t" data-ru="Русский" data-en="English">O'zbekcha</span>
```

Standart — UZ (birlamchi HTML matni). JS `data-lang` atributini `<html>` ga qo'yadi va elementlarning matnini almashtiradi.
**Zero-blank fallback**: Agar `data-ru` yoki `data-en` yozilmagan bo'lsa, avtomatik UZ matni ko'rsatiladi — ekranda bo'sh joy qolmaydi.
Merosxurlik uchun eski `<span lang="ru">...</span>` ham qo'llab-quvvatlanadi:
```css
[lang="ru"], [lang="en"]{display:none}
html[data-lang="ru"] [lang="ru"]{display:inline}
html[data-lang="ru"] [lang="uz"]{display:none}
html[data-lang="en"] [lang="en"]{display:inline}
html[data-lang="en"] [lang="uz"]{display:none}
```
Tanlov `localStorage['vc-lang']` da; prezentatsiya va varaqa bir xil tilda sinxronlashadi.

## Logotip: Vektorli SVG Standarti (`assets/target-logo.svg`)

Logotip sifatida yengil (1.7KB) vektorli `assets/target-logo.svg` yoki to'g'ridan-to'g'ri inline `<svg class="brand-svg">` ishlatiladi.
SVG ichida matn qismlari CSS o'zgaruvchilari (`var(--ink)`) bilan, nishon esa (`var(--accent)`) bilan bo'yalgan. Bu orqali logotip yorug' mavzuda brend navy `#00214A`, qorong'i mavzuda och oq-ko'k `#E9EFF8` rangga filtrsiz va buzilmasdan tabiiy moslashadi.

### Prezentatsiya Dokidagi Kapsula (`.brand-pill`):
```html
<div class="brand-pill">
  <svg class="brand-svg" viewBox="0 0 710 160" width="130" height="30" aria-label="Target International School">
    <!-- SVG ichki yo'llari fill="var(--ink)" va fill="var(--accent)" bilan -->
  </svg>
  <span class="brand-tag">Vibecoding</span>
</div>
```

### Varaqa va Tashqi Resurslar uchun:
```html
<img src="../../../../assets/target-logo.svg" alt="Target International School" class="brandmark-img">
```
*(Chop etishda va oflayn ko'rishda doimo toza vektorli aniqlik saqlanadi).*

O'lchamlar: prezentatsiya sarlavhasida `clamp(190px,17vw,260px)`,
pastki panelda `84px`, varaqada `42mm` (chop etishda `38mm`).

## Brend chizig'i

Logotipning o'z tuzilishi: navy so'z + bitta qizil urg'u. Bezak emas —
shuning uchun sahifada tasodifiy ko'rinmaydi.

```css
.brandrule{height:5px; background:linear-gradient(to right,
  var(--ink) 0 64%, var(--accent) 64% 100%)}
```

Prezentatsiyada dekning eng tepasida, varaqada masthead ostida.
Chop etishda `height:1.2pt; background:#000`.

## Chop etish — siyoh tejash

O'qituvchining talabi: **fon va rang umuman ishlatilmaydi**. Faqat qora
matn va ingichka chiziq.

```css
@media print{
  /* To'rtala selektor SHART: aks holda qorong'i mavzu qog'ozga o'tadi.
     :root:not([data-theme="light"]) eng yuqori o'ziga xoslikka ega. */
  :root,
  :root:not([data-theme="light"]),
  :root[data-theme="dark"],
  :root[data-theme="light"]{
    --bg:#fff; --sheet:#fff; --panel:transparent; --panel-2:transparent;
    --grid:transparent; --ink:#000; --ink-2:#333; --ink-3:#5E5E5E;
    --rule:#8C8C8C; --hair:#C6C6C6;
    --accent:#000; --accent-soft:transparent; --write:#B4B4B4;
  }
  .key{background:none; border-left:2.2pt solid #000}
  th{background:none; border:0; border-bottom:1.2pt solid #000}
  td{border:.4pt solid #B4B4B4}
  .sec, .key, table, .crit{break-inside:avoid}
  .noprint{display:none}
}
@page{ size:A4; margin:12mm; }
```

Bezak chop etilganda **rang bilan emas, shakl bilan** ishlaydi: chiziq
qalinligi, harf og'irligi, bo'sh joy.

## Scrollbar

Brauzerning standart kulrang scrollbari brend bilan urishadi — har bir
sahifada qayta bo'yaladi. Ikkala mavzuda ham tokenlardan oladi:

```css
*{scrollbar-width:thin; scrollbar-color:var(--rule) transparent}
::-webkit-scrollbar{width:9px; height:9px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--rule); border-radius:99px}
::-webkit-scrollbar-thumb:hover{background:var(--ink-3)}
::-webkit-scrollbar-corner{background:transparent}
```

Aylanadigan konteynerlarga `scrollbar-gutter: stable` — scrollbar paydo
bo'lganda kontent yon tomonga sakramaydi.

## Komponentlar

| Klass | Vazifasi |
|---|---|
| `.eyebrow` | Slayd ustidagi kichik yorliq + chiziq |
| `.callout` | Chapda qizil chiziqli asosiy fikr |
| `.box` | Oddiy karta: `.tag` + `h3` + `p` |
| `.steps` | Raqamlangan ketma-ketlik — **faqat haqiqiy tartib bo'lsa** |
| `ul.plain > li > span.t` | Belgili ro'yxat, matn bitta `.t` ichida |
| `.compare .bad / .good` | Yomon va yaxshi variant yonma-yon |
| `.matrix` | Solishtirish jadvali, birinchi ustun `td.q` |
| `.prompt` | Nuqtali ramkali prompt matni, monospace |
| `.grade` | 10 ballik baholash mezoni |
| `.timer` | Amaliy ish taymeri |
| `.brandmark` `.brandrule` | Logotip va brend chizig'i |

## Bo'sh joy va tartib

- Yonma-yon elementlar `flex`/`grid` + `gap` bilan, alohida `margin` bilan emas
- Keng kontent (jadval, kod) `.scroll-x` ichida — sahifa o'zi yon tomonga siljimasin
- Ramka, fon, radius va soya **rol bo'yicha** beriladi: hamma narsa karta emas
- Raqamlar (01/02/03) faqat haqiqiy ketma-ketlikda ishlatiladi

## Zichlik va Vizual Nafas (Breathability & Commercial Product Standard)

Dars materiallari (chop etiladigan varaqalar, veb-simulyatorlar va prezentatsiyalar) hech qachon haddan tashqari zich, harflari maydalashgan "soliq deklaratsiyasi" yoki siqilgan byurokratik shaklga aylanmasligi shart. Mahsulot Linear, Supabase, Vercel yoki Apple dasturlari kabi zamonaviy, havodor, keng va nafas oluvchi bo'lishi kerak.

### 1. Chop etiladigan Varaqa (`varaqa.html`)
- **Shriftlar me'yori**: Asosiy matn hech qachon 8pt dan kichik bo'lmasin (`9.2pt–9.6pt`, `line-height: 1.42–1.5`). Sarlavha `13.5pt–14.5pt`.
- **Havo va bo'sh joy**: Elementlarni A4 sahifasiga tiqishtirmang. Agar joy kam bo'lsa, topshiriqlar sonini kamaytirib, ularning chuqurligi va o'qilish qulayligini oshiring (masalan, 3 ta tor savol o'rniga 2 ta keng va chuqur savol).
- **Yozish chiziqlari**: O'quvchi qo'lda bemalol yoza olishi uchun yozish chiziqlari orasidagi masofa kamida `16pt–18pt` bo'lishi shart.
- **Jadvallar**: Hujayralarda qulay nafas (`padding: 6px 8px` dan `8px 12px` gacha).
- **A4 1-sahifalik chegara**: Varaqa aniq 1 sahifa A4 ga sig'ishi kerak (`page-break-after: avoid; max-height: 297mm`), ammo ichidagi bo'sh joylardan qo'rqmaslik, har bir blok nafas oladigan masofada turishi shart.

### 2. Laboratoriya va Simulyatorlar (`lab/`)
- **SaaS Mahsulot Estetikasi**: Maksimal kenglik `1350px–1440px`, chekka paddinglar `clamp(16px, 2.5vw, 32px)`.
- **Kartalar**: Radius `12px–14px`, ichki padding `20px–24px`, yumshoq soya `box-shadow: 0 4px 18px rgba(0,20,50,.04)`.
- **Boshqaruv elementlari**: Tablar va tugmalar to'rtburchak emas, zamonaviy "pill" (tabletka) ko'rinishida (`border-radius: 6px–8px` yoki `99px`, `padding: 8px 16px`).
- **Kod Muharriri va Monospace Jadvallar**: Shrift `13px–14px`, `line-height: 1.65–1.7`, `padding: 16px 18px`. Jadval ustunlari torayib ketmasligi uchun `td` larda `padding: 10px 16px`.

### 3. Prezentatsiyalar (`prezentatsiya.html`)
- **Slayd Kengligi**: Keng ekranlar uchun `max-width: 1360px–1380px`, `padding: clamp(24px, 4vw, 56px) clamp(28px, 5vw, 76px)`.
- **Kartalar Ritmi**: Kartalar ichidagi matn qatorlari erkin (`line-height: 1.5–1.55`), bandlar orasidagi bo'shliq `gap: 10px–14px`.
- **Kod Bloklari**: `pre.code-block` ichida qulay `padding: 14px 18px`, `line-height: 1.5–1.6`, `border-radius: 8px`.

## Sensor Ekranlar va Smartboard Boshqaruvi (Touch Controller Standard)

Target maktabidagi barcha sinflar sensorli Smartboard va o'qituvchi planshetlari bilan jihozlangan. Shuning uchun barcha prezentatsiyalar **noldan sensorli boshqaruvni (Touch & Swipe)** qo'llab-quvvatlashi SHART:

1. **Gorizontal Surish (Swipe Navigation)**:
   - Barmoq yoki Smartboard stilusini gorizontal surish orqali slaydlar almashadi (`touchstart` va `touchend`).
   - Mezon: `dx > 40px`, vertikal harakat minimal (`Math.abs(dy) < Math.abs(dx) * 1.3`), vaqt `dt < 800ms`.
   - Interaktiv elementlar (matn maydonlari, tugmalar, `select`) ustida surilganda sahifa almashmaydi.

2. **Ekran Chetlaridagi Sensor Tugmalar (`.screen-edge-nav`)**:
   - Smartboard yonida turgan o'qituvchi uchun chap va o'ng qirralarda yarim-shaffof teginish zonalari:
   ```html
   <button type="button" class="screen-edge-nav prev-edge" id="edgePrev" aria-label="Oldingi slayd">‹</button>
   <button type="button" class="screen-edge-nav next-edge" id="edgeNext" aria-label="Keyingi slayd">›</button>
   ```
   - CSS: `position: fixed; top: 50%; transform: translateY(-50%); width: 44px; height: 80px; opacity: 0; transition: opacity .2s;` (sichqoncha yoki barmoq chetga yaqinlashganda `opacity: 0.7` ga chiqadi).

## 2-Slayd: Majburiy Uy Vazifasi Tahlili (HW Review Architecture)

Har qanday prezentatsiyaning 2-slaydi **istisnosiz** o'tgan dars uy vazifasining tahliliga bag'ishlanadi (`data-phase="Uy Vazifasi Tahlili|Разбор Д/З|HW Review"`):

- **4 Kartali Standart Grid (`.hw-review-grid`)**:
  1. `.hw-card.pitfall`: O'quvchilar yo'l qo'ygan eng ko'p tarqalgan xato (qizil border, noto'g'ri kod/prompt).
  2. `.hw-card.solution`: Oltin yechim va eng toza muhandislik amaliyoti (yashil border, to'g'ri kod).
  3. `.hw-card.blitz`: 30 soniyalik blits-nazorat (o'qituvchi sinfdan so'raydigan yoki partalarga qarab tekshiradigan asosiy belgi).
  4. `.hw-card.bridge`: Yangi darsga ko'prik — nega bugungi yangi mavzu aynan shu vazifa muammosini hal qilish uchun zarurligi.

## Interaktiv Viktorina va Yechimni Ochish (`.quiz-box` & `.reveal-btn`)

Dars o'rtasida o'quvchilarning fikrini jamlash uchun interaktiv kiber-viktorina ishlatiladi:
- `.quiz-opt` tugmalari bosilganda to'g'ri/noto'g'ri ko'rsatkich (`.correct` / `.wrong`) yonadi.
- Klaviatura `R` tugmasi yoki `.reveal-btn` bosilganda tushuntirish va yechim kodi (`.quiz-reveal`) ochiladi.

## Dars Davomiyligi va Slaydlar Zichligi

Prezentatsiya hajmi o'qituvchi dars jadvalidagi slot davomiyligiga qarab qat'iy rejalashtiriladi:
- **Yagona dars (40 daqiqa):** 8–10 ta slayd. Tezkor, yuqori dinamikali, bitta asosiy texnik ko'nikma.
- **Juftlik blok ("2 soatlik" / 80 daqiqa):** 13–16 ta slayd. 1-qism (40 daqiqa): HW Review + Yangi Nazariya + Viktorina; 2-qism (40 daqiqa): Katta Amaliy Laboratoriya (Cyber Arena / Simulator) + Himoya (Peer Review) + 10 ballik uy vazifasi.

## Pastki O'ng Panel va Vektorli Ikonkalar (Bottom-Right Dock & SVG Icons)

Boshqaruv paneli (`.floating-dock`) hech qachon ekranning o'rtasida turmasligi va matnlarni to'sib qo'ymasligi SHART:
1. **Joylashuvi — Pastki O'ng Burchak (Bottom-Right):**
   ```css
   .floating-dock {
     position: fixed;
     bottom: 20px;
     right: 24px;
     left: auto;
     transform: none;
     z-index: 100;
   }
   ```
   Bu orqali ekran markazidagi dars kontenti 100% ochiq va qulay o'qiladigan bo'ladi.
2. **Brauzerga Bog'liq Bo'lmagan Eksplitsit SVG Ikonkalar (No System Emojis):**
   - Brauzer va operatsion tizimga bog'liq bo'lgan emoji belgilar (`🌓`, `📝`, `⌨️`, `◀`, `▶`) taqiqlanadi (chunki ular har xil tizimlarda har xil rangda, qiyshiq yoki kesilib ko'rinadi).
   - O'rniga toza inline vektorli `<svg viewBox="0 0 24 24" stroke="currentColor">` ikonkalar ishlatiladi. Ular mavzuga qarab avtomatik ravishda to'g'ri rang oladi va barcha Smartboard va qurilmalarda 100% bir xil tiniqlikda render bo'ladi.

## Prezentatsiyani O'zidan Masshtablash Standarti (Direct Deck Scale Controller)

Barcha taqdimotlar har xil o'lchamdagi proyektorlar (1024x768, 1080p, 4K Smartboard) va auditoriya o'lchamlariga moslashishi uchun to'g'ridan-to'g'ri interfeysning o'zidan masshtabni o'zgartirishni qo'llab-quvvatlashi MAJBURIY:

1. **Masshtab Mexanizmi (`--deck-scale` va `zoom`)**:
   - `:root { --deck-scale: 1; }` o'zgaruvchisi orqali boshqariladi.
   - Slayd kontenti `.slide { zoom: var(--deck-scale, 1); }` orqali masshtablanadi. Bu slayd ichidagi matn, kod va kartalarni ravon kattalashtiradi/kichraytiradi.
   - Suzuvchi tashqi elementlar (`.floating-dock`, `.floating-brand`, `.floating-counter`, `.screen-edge-nav`) slayd tashqarisida bo'lgani sababli fizik piksel o'lchamida qoladi va hech qachon buzilmaydi.
2. **Dok Panelidagi Tugmalar (`.floating-dock`)**:
   - `[-]` tugmasi (`onclick="adjustScale(-0.1)"`): masshtabni 10% ga kichraytiradi (minimal 60%).
   - `[ 100% ]` nishoni (`onclick="cycleScale()"`): qulay presetlarni (100% → 115% → 130% → 150% → 85%) almashtiradi yoki tiklaydi.
   - `[+]` tugmasi (`onclick="adjustScale(0.1)"`): masshtabni 10% ga kattalashtiradi (maksimal 160%).
3. **Klaviatura va Sensorli Qisqa Yo'llar**:
   - Klaviatura: `+` yoki `=` — kattalashtirish; `-` yoki `_` — kichraytirish; `0` — 100% ga tiklash.
   - Smartboard / Planshet: Ikki barmoq bilan chimchilash (pinch-to-zoom) orqali sensorli doskada to'g'ridan-to'g'ri masshtablash.
4. **LocalStorage Doimiy Xotirasi**:
   - Tanlangan masshtab `localStorage.setItem('target_scale', currentScale)` orqali saqlanadi va sahifa qayta ochilganda avtomatik yuklanadi.




