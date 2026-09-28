# O'qituvchi uchun qo'llanma: 16-dars — SemVer, GitHub Releases va Open Source Hamkorlik

**Kohorta:** Senior / Junior Vibecoder (9-sinf)  
**Hafta / Dars:** 3-hafta / 16-dars  
**Mavzu:** SemVer (Semantic Versioning 2.0.0), Git Tags, GitHub Releases, Changelog yaratish, Open Source Litsenziyalari (MIT, Apache 2.0, GPL) va Jamoaviy Standartlar  
**Davomiyligi:** 45 daqiqa  

---

## 1. Darsning Pedagogik Maqsadi va Muhandislik Falsafasi

Ushbu dars 9-sinf uchun 3-haftaning (Git, GitHub, Code Review, CI/CD) mantiqiy cho'qqisi va yakuniy bosqichidir. 

Dastur yozildi (13-dars), PR orqali tekshirildi (14-dars), CI/CD orqali avtomatlashtirilgan testlardan o'tdi (15-dars). Endi navbatdagi katta savol: **"Bu dasturni dunyoga qanday rasman taqdim etamiz va versiyalarni qanday boshqaramiz?"**

Darsning tub maqsadlari:
1. **SemVer 2.0.0 Standarti (MAJOR.MINOR.PATCH):**
   - **MAJOR (1.0.0 -> 2.0.0):** Breaking changes. Eski kod bilan orqaga mos kelmaydigan (incompatible) o'zgarishlar. Masalan: API metodi nomi o'zgarishi, funksiya argumentlari olib tashlanishi.
   - **MINOR (1.0.0 -> 1.1.0):** Yangi imkoniyatlar qo'shildi, ammo orqaga mos (backward-compatible). Eski kod hech qanday muammosiz ishlashda davom etadi.
   - **PATCH (1.0.0 -> 1.0.1):** Xatoliklar (bugfix) tuzatildi, xavfsizlik yangilanishi, backward-compatible.
2. **Git Tags va GitHub Releases:**
   - Kommitlar o'tkinchi hashlar (`a3f91b2`), Release esa tarixiy verstak belgisidir (`v1.0.0`).
   - `git tag -a v1.0.0 -m "Release version 1.0.0"` va `git push origin v1.0.0`.
   - GitHub Releases sahifasida release notes, avtomatik `CHANGELOG.md` yaratish va binary / zip arxivlar.
3. **Open Source Madaniyati va Litsenziyalar:**
   - Dastur kodi shunchaki ochiq bo'lishi uning Open Source ekanligini anglatmaydi; litsenziyasiz kod qonunan himoyalanmagan!
   - **MIT License:** Eng ommabop, qisqa va erkin. Kim xohlasa tijoriy maqsadlarda ham o'zgartirib foydalanishi mumkin (mualliflik saqlanadi).
   - **Apache 2.0:** MIT ga o'xshash, ammo patent da'volaridan himoya qiladi (Google, Kubernetes, TensorFlow).
   - **GPL v3 (Copyleft):** Har qanday hosila loyiha ham ochiq kodli bo'lib qolishi shart (Linux, Blender).
4. **Professional Hujjatlashtirish:**
   - `README.md` — loyihaning vizitkasi (Badge'lar, skrinshot, tezkor start, arxitektura).
   - `CONTRIBUTING.md` — boshqa dasturchilar loyihaga qanday hissa qo'shishi mumkinligi.
   - `CHANGELOG.md` — har bir versiyadagi o'zgarishlar tarixi (Keep a Changelog standarti).

---

## 2. 45 Daqiqalik Dars Taqsimoti

| Vaqt | Bosqich | O'qituvchi va O'quvchi Faoliyati |
|---|---|---|
| **00:00 – 03:00** | Kirish va Muammo | "Tasavvur qiling, siz yaratgan kutubxonadan 10,000 dasturchi foydalanmoqda. Kichik o'zgarish qilib versiya chiqardingiz va ularning barchasining sayti quladi! Buni qanday oldini olamiz?" |
| **03:00 – 12:00** | Nazariya: SemVer Anatomiyasi | MAJOR, MINOR, PATCH mexanizmlari. `^1.2.3` va `~1.2.3` prefikslari (Caret vs Tilde). Nega versiya `1.9.0` dan keyin `1.10.0` bo'ladi (`2.0.0` emas!). |
| **12:00 – 18:00** | Git Tags va GitHub Releases | `git tag` buyrug'i, engil (lightweight) va izohli (annotated) teglar farqi. GitHub'da rasmiy Release yaratish. |
| **18:00 – 24:00** | Open Source Litsenziyalari | MIT, Apache 2.0 va GPL v3 solishtiruvi. GitHub da litsenziya qo'shish va README.md tuzilishi. |
| **24:00 – 38:00** | Amaliy Laboratoriya (Release Center Lab) | `lab/index.html` interaktiv trenajyorida: o'zgarishlar ssenariysiga qarab versiya hisoblash, `CHANGELOG.md` yozish, litsenziya tanlash va v1.0.0 release paketini chiqarish! |
| **38:00 – 43:00** | Varaqa va Mustahkamlash | Varaqadagi SemVer versiyalash topshiriqlari va litsenziya keyslarini tahlil qilish. |
| **43:00 – 45:00** | Xulosa va Baholash | 10 ballik tizim bo'yicha baholash va 3-hafta Git/DevOps to'liq tsikliga yakun yasash. |

---

## 3. O'quvchilar Ko'p Yo'l Qo'yadigan Xatolar (Tuzoqlar)

1. **SemVer ni o'nli kasr deb o'ylash:**
   - O'quvchilar ko'pincha `1.9.0` dan keyin `2.0.0` keladi deb o'ylashadi. Yo'q! SemVer o'nli kasr emas, butun sonlar triadasidir. `1.9.0` dan keyingi minor versiya `1.10.0`, keyin `1.11.0` bo'ladi. `2.0.0` faqat breaking change bo'lgandagina qo'yiladi.
2. **Git Tag va Branch chalkashishi:**
   - Branch — bu harakatlanuvchi ko'rsatkich (yangi kommitlar qo'shilganda siljiydi). Tag — toshga o'yilgan doimiy muzlatilgan kommit ko'rsatkichi.
3. **Litsenziyasiz Open Source:**
   - Ko'pchilik kodni GitHub'ga public qilib qo'yish kifoya deb biladi. Aslida esa litsenziyasiz public repo barcha mualliflik huquqlarini egasida saqlaydi ("All rights reserved"), boshqalar uni qonunan ishlata olmaydi. MIT litsenziyasi qo'yilsagina haqiqiy Open Source bo'ladi.
