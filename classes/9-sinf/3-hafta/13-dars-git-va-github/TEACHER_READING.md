# 13-Dars: O'qituvchi Uchun Tayyorgarlik Qo'llanmasi (Teacher Prep Guide)
**Target International School // 9-Sinf (Junior Vibecoder) // 3-Hafta (1-Soat: 40–50 daqiqa)**
**Mavzu:** Git va GitHub — Commit, Branch va Merge Konflikti

> **METODIK ESLATMA:** 11-darsda o'quvchilar VS Code o'rnatdi, 12-darsda
> (AI Bug Hunter) xato topishni o'rgandi. Git — shu ikkalasini bog'laydigan
> muhandislik jarayoni. Darsning cho'qqisi — **merge konflikti**: ko'pchilik
> undan qo'rqadi, chunki uni "xato" deb o'ylaydi. Sizning vazifangiz —
> konflikt **xato emas, savol** ekanini ko'rsatish.

---

## 1. Darsda Qaysi Vositalar Ishlatiladi?

1. **Git simulyatori (Google Chrome):**
   * Fayl: `classes/9-sinf/3-hafta/13-dars-git-va-github/lab/index.html`
   * **Git o'rnatilishi shart emas. Internet kerak emas.**
   * Simulyator **haqiqiy Git sintaksisini** qabul qiladi: `git add`, `git commit -m`,
     `git switch -c`, `git merge`, `git log`, `git branch -d`.
   * Xato buyruqqa **Git ning haqiqiy xato xabarini** qaytaradi.
   * Ekranda uchta panel: **commit grafi** (chapda), **fayl muharriri + terminal**
     (o'rtada), **shpargalka** (o'ngda).
   * `⚡ Konflikt stsenariysi` tugmasi — bir bosishda tayyor konflikt holatini quradi
     (vaqt yetmay qolganda juda foydali).
2. **Prezentatsiya:** `prezentatsiya.html` — 13 slayd, `N` — o'qituvchi izohlari.
3. **Varaqa:** `varaqa.html` — 1 varaq A4.

---

## 2. O'qituvchi Uchun Texnik Mazmun

### A0. Git tarixi va Linus Torvalds — 2005-yilgi chaqiruv
Git qanday va nega paydo bo'lganini bilish o'quvchilarda vositaga nisbatan chuqur muhandislik hurmati uyg'otadi:
* **BitKeeper inqirozi (2005):** Linux yadrosi o'sha paytda yopiq manbali tijorat BitKeeper tizimidan bepul foydalanardi. Jamiyat a'zosi Andrew Tridgell uning protokolini teskari muhandislik (reverse engineering) qilgani sababli, BitKeeper egasi bepul litsenziyani bekor qildi.
* **Mavjud vositalarning ojizligi:** CVS va SVN markazlashgan, nihoyatda sekin va har bir harakatda markaziy server bilan doimiy ulanishni talab qilardi. Minglab xalqaro dasturchilarning ulkan patchlar oqimiga dosh berolmasdi.
* **10 kunlik jasorat:** Linus Torvalds: *"Agar mos vosita bo'lmasa, uni o'zim yarataman"* deb qaror qildi. U Linux yadro ishlarini vaqtincha to'xtatib, Git'ning yadro arxitekturasini to'liq **C tilida 10 kun ichida** noldan yozib chiqdi.
* **3 ta asosiy ustun:**
  1. **Taqsimlanganlik (Fully Distributed):** Markaziy serverga qaramlik yo'q. Har bir dasturchining noutbukida butun loyihaning 100% to'liq tarixi saqlanadi.
  2. **Tezlik:** C tilida to'g'ridan-to'g'ri xotira va fayl bloklari bilan ishlash orqali patchlar millisekundlarda birlashtiriladi.
  3. **Kriptografik butunlik (SHA-1):** Har bir commit va fayl xeshlanadi — tarixni orqaga qaytib o'zgartirish yoki soxtalashtirish matematik jihatdan imkonsiz.
* **Nomlanishi:** Linus Torvalds hazilomuz tarzda: *"Men barcha loyihalarimni o'z nomim bilan atayman: avval Linux, endi esa Git"* degan (ingliz jargonida *git* — "o'jar, murosa qilmaydigan odam").

### A. Git nima saqlaydi — eng ko'p uchraydigan noto'g'ri tasavvur
Ko'pchilik (shu jumladan ko'p o'qituvchilar) Git **o'zgargan qatorlarni** saqlaydi
deb o'ylaydi. Aslida har commit — loyihaning **to'liq surati** (snapshot).
O'zgarmagan fayllar uchun Git nusxa yaratmaydi, balki oldingi obyektga
**ishora** qoldiradi. Shuning uchun tarix katta joy egallamaydi.

Har commitda: **muallif, sana, xabar, ota-commit(lar), surat** va noyob **hash**.

**Ota-bola zanjiri — darsning asosiy g'oyasi.** Branch va merge butunlay shu
zanjir ustida qurilgan. Doskada albatta chizing:
```
o ← o ← o ← o   (main)
        ↖ o ← o (yangi-dizayn)
```

### B. Uchta zona
| Zona | Buyruq | Ma'nosi |
|---|---|---|
| Working Directory | — | Papkangiz. Git ko'radi, lekin eslab qolmaydi |
| Staging Area | `git add` | Commitga **nima kirishini siz tanlaysiz** |
| Repository | `git commit` | Tarixga yozildi, endi yo'qolmaydi |

**Nega staging kerak?** Bu eng ko'p beriladigan savol. Javob: bitta ish seansini
**ikkita toza commitga** ajratish uchun. Slaydda aniq misol bor.

### C. Branch — nusxa emas, ko'rsatkich
Branch — bu 40 belgidan iborat faylcha, u bitta commit hash ini saqlaydi.
Shuning uchun branch yaratish **bir zumda** bo'ladi va joy egallamaydi.

### D. Merge ikki xil bo'ladi
* **Fast-forward** — `main` o'zgarmagan bo'lsa, Git shunchaki ko'rsatkichni
  oldinga suradi. **Yangi commit yaratilmaydi.**
* **Merge commit** — ikkala branch ham o'zgargan bo'lsa, **ikkita otasi bor**
  maxsus commit yaratiladi.

Git **merge base** (umumiy ajdod) ni topadi va undan keyin har ikki tomonda
nima o'zgarganini solishtiradi.

### E. Konflikt qachon va nega
**Faqat bitta holatda:** ikkala branchda **aynan bir xil qator** boshqacha
o'zgartirilgan. Turli fayllar yoki turli qatorlar o'zgarsa — Git hammasini
avtomatik qiladi.

Konflikt — Git ning **kamchiligi emas**. Bu Git ning halolligi: u mazmunga oid
qarorni o'zi qabul qilmaydi, chunki qaysi variant to'g'ri ekanini faqat inson biladi.

```
<<<<<<< HEAD
<h1>Mening Portfoliom</h1>          ← siz turgan branch
=======
<h1>Aziz Karimov — Dasturchi</h1>   ← olib kelinayotgan branch
>>>>>>> yangi-dizayn
```

**Yechish — 4 qadam:** ikkala variantni o'qing → qaror qiling (yoki birlashtiring)
→ uchala belgi qatorini o'chiring → `git add` va `git commit`.

### F. Git vs GitHub — klassik chalkashlik
* **Git** — kompyuteringizdagi dastur, internetsiz ishlaydi.
* **GitHub** — sayt, Git repozitoriyalarini saqlaydi va ulashadi.
* GitHub o'rnida GitLab yoki Bitbucket bo'lishi mumkin — **Git bitta**.

---

## 3. Dars Rejasi

### 00:00 – 06:00 | Muammo (1–2-slayd)
* Sarlavhani o'qing: `loyiha_final_v2_FINAL_oxirgi(1).html`
* **Savol sinfga:** *"У кого на компьютере есть файлы с такими именами?"*
  Deyarli hamma qo'l ko'taradi — bu darsning eng yaxshi kirishi.
* To'rtta savolni ayting: qaysi biri oxirgi, nima o'zgardi, **nega** o'zgardi,
  ikki kishi ishlasa nima bo'ladi.

### 06:00 – 10:00 | Git tarixi va Linus Torvalds (3-slayd)
* **Tarixiy kontekst:** 2005-yilgi BitKeeper inqirozi va Linus Torvaldsning 10 kunda C tilida Git'ni yaratishi.
* **Uchta ustun:** Taqsimlangan arxitektura, C tezligi va SHA-1 kriptografik xesh.
* Doskaga yozing: `Linus Torvalds · 2005 · C · Distributed`.

### 10:00 – 14:00 | Git modeli (4-slayd)
* **Doskada commit zanjirini chizing.** Bu darsning vizual tayanchi — uni
  dars oxirigacha o'chirmang.
* Ayting: Git farqlarni emas, **suratlarni** saqlaydi.

### 14:00 – 18:00 | Uchta zona (5-slayd)
* Simulyatorda `git status` → fayl tahriri → `git add .` → `git status` →
  `git commit -m "..."` ketma-ketligini **jonli** bajaring.
* Har qadamdan keyin o'ng paneldagi holat yozuvi o'zgarishini ko'rsating.

### 18:00 – 21:00 | Commit xabari (6-slayd)
* Ikki ustunni solishtiring.
* **Asosiy fikr:** commit xabari — **kelajakdagi o'zingizga xat**.
* Conventional Commits (`feat:`, `fix:`, `docs:`) ni doskada yozing. Ular ishga
  kirganda birinchi kundan shu formatni uchratadi.

### 21:00 – 25:00 | Branch (7-slayd)
* **Asosiy fikr:** branch — nusxa emas, **ko'rsatkich**.
* Simulyatorda `git switch -c yangi-dizayn` bajaring va **chapdagi graf ikkiga
  bo'linishini** ko'rsating. Bu juda ta'sirli vizual.

### 25:00 – 29:00 | Merge (8-slayd)
* Ikki xil merge. Fast-forward ni simulyatorda ko'rsating — yangi commit
  yaratilmaganini ta'kidlang.
* Oxirida ko'prik: *"А что, если обе ветки изменили одну и ту же строку?"*

### 29:00 – 34:00 | ⭐ KONFLIKT — DARSNING CHO'QQISI (9-slayd)

**Jonli demo (eng muhim 5 daqiqa):**
1. `⚡ Konflikt stsenariysi` tugmasini bosing — tayyor holat quriladi.
2. `git switch main` → `git merge yangi-dizayn`
3. Terminalda qizil KONFLIKT xabari chiqadi, muharrir qizarib ketadi,
   faylda belgilar paydo bo'ladi.
4. **Asosiy gap:**
   > *"Обратите внимание: Git не сломался и ничего не потерял. Он **остановился
   > и спросил вас**. Потому что какой заголовок правильный — это смысловое
   > решение, и его может принять только человек. Конфликт — это не ошибка.
   > Это вопрос."*
5. Faylni tahrirlang, belgilarni o'chiring, `git add .` va
   `git commit -m "konflikt yechildi"`. Grafda **ikki otali merge-commit**
   paydo bo'lishini ko'rsating.

**Qo'shimcha demo (agar vaqt bo'lsa):** belgilarni o'chirmasdan `git add .`
bosing — simulyator rad etadi. Bu real Git xatti-harakati.

### 34:00 – 37:00 | GitHub (10-slayd)
* Git va GitHub farqini aniq ajrating.
* **9-sinf uchun kuchli motivatsiya:**
  > *"Ваш профиль на GitHub — это ваше портфолио. Университеты и работодатели
  > смотрят именно туда. Каждый коммит сегодня — это строчка в вашем будущем CV."*

### 37:00 – 47:00 | Amaliyot (11 daqiqa)

| # | Bosqich | Yoziladigan narsa |
|---|---|---|
| 1 | Commit: `git add .` → `git commit -m "..."` | Commit hash |
| 2 | Branch: `git switch -c yangi-dizayn` + 2 commit | Branch nomi, commitlar soni |
| 3 | **Konflikt**: ikkala branchda 1-qator → `git merge` | Konflikt chiqdimi |
| 4 | `git log` | Jami commitlar, oxirgi hash |

**🛑 Muhim:** ko'p o'quvchi 3-bosqichni chetlab o'tmoqchi bo'ladi. Majburlang —
**ikkala branchda ham aynan 1-qatorni** o'zgartirish kerak. Konfliktsiz o'tgan
o'quvchi darsning yarmini o'tkazib yuborgan bo'ladi.

**Vaqt yetmasa:** `⚡ Konflikt stsenariysi` tugmasidan foydalanishni ayting —
u 1, 2 va 3-bosqichni avtomatik quradi, o'quvchi faqat yechishni bajaradi.

### 47:00 – 50:00 | AI yordamchi va Yakun (12–13-slayd)
* AI taklif qiladigan xavfli buyruqlar (`--force`, `reset --hard`) dan ogohlantiring: *"Tushunmagan buyruqni bajarma"*.
* Xulosa: Git — suratlar zanjiri, branch — ko'rsatkich, konflikt — savol.
* Varaqalarni yig'ing. Keyingi dars — **Pull Request va kod ko'rigi**.

---

## 4. Simulyator Buyruqlari (Shpargalka)

| Buyruq | Natija |
|---|---|
| `git status` | Joriy branch va fayl holati |
| `git add .` | O'zgarishni staging ga o'tkazish |
| `git commit -m "xabar"` | Tarixga yozish |
| `git log` | Butun tarix (hash + xabar) |
| `git branch` | Branchlar ro'yxati (`*` — joriy) |
| `git branch <nom>` | Branch yaratish (o'tmasdan) |
| `git branch -d <nom>` | Branchni o'chirish |
| `git switch <nom>` | Branchga o'tish |
| `git switch -c <nom>` | Yaratish + o'tish |
| `git checkout -b <nom>` | Eski uslub, xuddi shu ish |
| `git merge <nom>` | Branchni joriysiga birlashtirish |

**Klaviatura:** `↑` `↓` — buyruqlar tarixi. `⚡` — tayyor konflikt stsenariysi.
`↺` — hammasini qayta boshlash.

**Simulyator ataylab rad etadigan holatlar** (bu real Git xatti-harakati):
* `add` qilmasdan `commit` — rad etiladi;
* iflos papkada `switch` yoki `merge` — rad etiladi;
* faylda konflikt belgilari qolsa `add` — rad etiladi.

---

## 5. Ko'p Beriladigan Savollar

**"Nega `git switch` ishlamayapti, 'закоммитьте изменения' deydi?"**
Ishchi papkada saqlanmagan o'zgarish bor. Avval `git add .` va
`git commit -m "..."`. Bu real Git ning aynan shunday xatti-harakati —
u sizning ishingizni yo'qotib qo'yishdan saqlaydi.

**"Merge qildim, lekin konflikt chiqmadi."**
Demak siz **turli qatorlarni** o'zgartirgansiz — Git hammasini o'zi birlashtirdi.
Konflikt olish uchun **aynan bir xil qatorni** ikkala branchda boshqacha
o'zgartirish kerak.

**"Fast-forward nima degani?"**
`main` siz branchda ishlaganingizda umuman o'zgarmagan. Shuning uchun Git yangi
commit yaratmay, shunchaki `main` ko'rsatkichini oldinga suradi.

**"Hash raqamlari har safar boshqacha."**
To'g'ri, shunday bo'lishi kerak. Haqiqiy Git da hash commit mazmunidan
hisoblanadi va har doim noyob bo'ladi.

**"Bu haqiqiy Git mi?"**
Sintaksis — haqiqiy. Ichki mexanizm soddalashtirilgan (bitta fayl, qatorlar
bo'yicha birlashtirish). Bugun o'rgangan buyruqlar terminalda to'g'ridan-to'g'ri
ishlaydi.

---

## 6. Uy Vazifasi va 10 Ballik Mezon

| Mezon | Ball |
|---|---|
| 4 bosqich jadvali (hash, branch, konflikt, log) | 3 |
| 3 ta commit xabari Conventional Commits formatida | 3 |
| Konflikt yechimi **va sababi** | 2 |
| Uchta zona tavsifi | 2 |
| **JAMI** | **10** |

**Baholashda eng muhimi — konflikt sababi (2 ball).**
* "Ikkinchi variantni tanladim" → **1 ball**. Sabab yo'q.
* "Ikkinchi variantni tanladim, chunki unda ism bor va bu portfolio uchun
  aniqroq" → **2 ball**. Mana shu muhandislik fikrlashi.

Commit xabarlarida `feat:` / `fix:` / `docs:` prefiksi **majburiy** — bu darsda
alohida ko'rsatilgan.

---

## 7. Keyingi Dars

**14-dars: Pull Request va Kod Ko'rigi.** O'quvchilar bugungi branch bilishlari
ustiga PR jarayonini o'rganadi: diff o'qish, inline izoh yozish, "approve" va
"changes requested", hamda AI reviewer bilan ishlash. Bugungi konflikt
tajribasi u yerda to'g'ridan-to'g'ri ishlatiladi.
