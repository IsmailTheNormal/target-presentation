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

## Til: uch til bitta faylda

```css
[lang="ru"], [lang="en"]{display:none}
html[data-lang="ru"] [lang="ru"]{display:inline}
html[data-lang="ru"] [lang="uz"]{display:none}
html[data-lang="en"] [lang="en"]{display:inline}
html[data-lang="en"] [lang="uz"]{display:none}
```

Standart — UZ, JS ishlamasa ham to'g'ri ko'rinadi.
`<span lang="...">` faqat **inline** elementlar ichida ishlatiladi.
Tanlov `localStorage['vc-lang']` da; prezentatsiya va varaqa bir kalitni
baham ko'radi, shuning uchun til ikkalasida birga o'zgaradi.

## Logotip

Ikki variant, mavzuga qarab almashadi. **`<img>` bilan**, `background-image`
bilan emas — brauzerlar chop etishda fon rasmlarni chiqarmaydi.

```html
<span class="brandmark sheet-mark">
  <img class="on-light" src="data:image/png;base64,…">  <!-- assets/logo-light.txt -->
  <img class="on-dark"  src="data:image/png;base64,…">  <!-- assets/logo-dark.txt -->
</span>
```

```css
.brandmark{display:block; line-height:0}
.brandmark img{display:block; width:100%; height:auto}
.brandmark .on-dark{display:none}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]) .brandmark .on-light{display:none}
  :root:not([data-theme="light"]) .brandmark .on-dark{display:block}
}
:root[data-theme="dark"] .brandmark .on-light{display:none}
:root[data-theme="dark"] .brandmark .on-dark{display:block}
@media print{
  .brandmark .on-light{display:block !important}
  .brandmark .on-dark{display:none !important}
}
```

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
