# O'qituvchi Qo'llanmasi (Teacher Reading)
## 9-sinf · 12-hafta · 35-dars
### Mavzu: NPM Ekotizimi, Tashqi Paketlar va Ta'minot Zanjiri Xavfsizligi (Supply Chain Security & Audit)
**Dars formati:** Juftlik Dars (Double Block — 80 daqiqa / 2-soatlik dars)

---

### 1. Darsning Pedagogik Maqsadi va Metodikasi
Zamonaviy veb-ishlab chiqishda hech kim barcha kodni noldan yozmaydi — 80% dan ortiq dasturiy ta'minot ochiq manbali NPM paketlaridan tashkil topadi.
Biroq bu qulaylik ulkan kiberxavf tug'diradi: ta'minot zanjiri hujumlari (Supply Chain Attacks).
Ushbu 80 daqiqalik juftlik darsida o'quvchilar:
1. `package.json` va `package-lock.json` orasidagi keskin farqni va SHA-512 nazoratini anglaydilar.
2. SemVer qoidalarini va karetka (`^`) orqali yovuz kod kiritilish xavfini o'rganadilar.
3. Typosquatting klonlarini va `postinstall` troyanlarini fosh qilishni o'rganadilar.
4. `npm audit` va `npm audit fix` buyruqlari yordamida real loyihadagi CVE xavflarini bartaraf etadilar.

---

### 2. Darsning 80 Daqiqalik Aniq Xronometraji

#### 1-BOSQICH (40 daqiqa) — Teoriya, Arxitektura va Viktorina
- **00:00–05:00 (5 min):** Kirish, dars mavzusi va maqsadlarini e'lon qilish.
- **05:00–13:00 (8 min):** 34-dars uy vazifasi tahlili: sodda replace('<', '') ning zaifligi, HTML Entity encoding oltin standarti va 30 sek blitz savol.
- **13:00–18:00 (5 min):** NPM ekotizimi nima? 2.5 mln paketlar, `node_modules` va tranzitiv bog'liqliklar daraxti.
- **18:00–24:00 (6 min):** SemVer formulasi: MAJOR, MINOR, PATCH hamda `^` (karetka) va `~` (tilda) qoidalari.
- **24:00–29:00 (5 min):** `package-lock.json` nega kerak? `npm install` vs `npm ci` farqlari va SHA-512 hash yaxlitligi.
- **29:00–34:00 (5 min):** `dependencies` vs `devDependencies`: Production serverni toza saqlash (`--omit=dev`).
- **34:00–40:00 (6 min):** Ta'minot zanjiri xavflari: Typosquatting (`cross-env` vs `crossenv`) va `postinstall` troyanlari.

#### 2-BOSQICH (40 daqiqa) — Laboratoriya, Peer-Review va Yakun
- **40:00–45:00 (5 min):** Xavfli skriptlarni bloklash: `--ignore-scripts` va `.npmrc` konfiguratsiyasi.
- **45:00–50:00 (5 min):** Interaktiv Quiz: 4 ta tezkor savol orqali tushunchalarni mustahkamlash.
- **50:00–56:00 (6 min):** Zaifliklar auditi: `npm audit` va `npm audit fix` orqali CVE darajalarini bartaraf etish.
- **56:00–61:00 (5 min):** Korporativ himoya: Socket.dev, Snyk va CI/CD avtomatik tekshiruvlari.
- **61:00–71:00 (10 min):** Katta Amaliy Laboratoriya: `studio/index.html` da soxta crossenv paketini olib tashlash va toza audit yaratish.
- **71:00–76:00 (5 min):** Juftlikda Peer-Review va 2 nafar o'quvchining Smartboardda jonli demosi.
- **76:00–80:00 (4 min):** Dars xulosasi, 3 darajali uy vazifasi tushuntirilishi va baholash.

---

### 3. O'qituvchi Uchun Chuqur Texnik Savollar va Javoblar

1. **Savol:** Nega `npm install` buyrug'ini Docker yoki CI/CD muhitida ishlatish taqiqlanadi?
   - **Javob:** `npm install` buyrug'i agar versiyalar karetka (`^`) bilan belgilangan bo'lsa, yangiroq MINOR yoki PATCH versiyani yuklab olishga urinadi va `package-lock.json` ni qayta yozib yuborishi mumkin. Natijada test qilingan kod bilan serverdagi kod farq qiladi. `npm ci` esa lockfile-dagi SHA-512 hashni qat'iy tekshiradi va lockfile-ni aslo o'zgartirmaydi.
2. **Savol:** Typosquatting qanday xavf tug'diradi?
   - **Javob:** Dasturchi shoshilib `npm install cross-env` o'rniga `npm install crossenv` deb yozsa, xakerning troyan paketi o'rnatiladi. Uning `postinstall` skripti kompyuterdagi barcha `.env` parollarini xakerning serveriga jo'natib yuboradi.
3. **Savol:** Nega `npm audit fix --force` dan ehtiyotkorlik bilan foydalanish kerak?
   - **Javob:** `--force` kaliti zaiflikni tuzatish uchun paketning MAJOR versiyasini (masalan, 2.x dan 4.x ga) yangilab yuborishi mumkin. Bu esa API sintaksisini buzib, loyihaning butunlay ishlamay qolishiga olib keladi.
