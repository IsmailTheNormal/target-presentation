# O'qituvchi uchun qo'llanma: 15-dars — CI/CD, GitHub Actions va Avtomatlashtirish

**Kohorta:** Senior / Junior Vibecoder (9-sinf)  
**Hafta / Dars:** 3-hafta / 15-dars  
**Mavzu:** CI/CD (Continuous Integration / Continuous Deployment), GitHub Actions, YAML Konfiguratsiyasi, Avtomatlashtirilgan Testlar va Avto-Deploy  
**Davomiyligi:** 45 daqiqa  

---

## 1. Darsning Pedagogik Maqsadi va Muhandislik Falsafasi

O'quvchilar 13-darsda Git versiyalar nazorati (commit, branch, merge) va 14-darsda Pull Request hamda Kod Ko'rigi (Code Review) jarayonini chuqur o'zlashtirdilar.

Ammo zamonaviy korporativ IT olamida (Google, Meta, Amazon, Target IT) inson kodi har doim ham darhol production (jonli server)ga yuborilmaydi. Har bir `git push` yoki Pull Request ortidan **Avtomatlashtirilgan Robotlar (CI/CD)** ishga tushadi.

Darsning tub maqsadlari:
1. **CI/CD Falsafasi:**
   - **Continuous Integration (CI):** Yangi yozilgan kod omborga qo'shilishi bilanoq, avtomatik robotlar uni linterdan o'tkazadi va barcha testlarni yurgizib ko'radi.
   - **Continuous Deployment (CD):** Agar barcha testlar muvaffaqiyatli (yashil) o'tsa, dastur avtomatik ravishda Vercel yoki Cloud serverga deploy qilinadi (inson qo'li tegmasdan!).
2. **GitHub Actions Arxitekturasi:**
   - `.github/workflows/main.yml` fayli.
   - **Triggers (Hodisalar):** `on: [push, pull_request]`.
   - **Jobs (Vazifalar):** `build`, `lint`, `test`, `deploy`.
   - **Runners (Virtual mashinalar):** `ubuntu-latest`.
   - **Steps & Actions:** `uses: actions/checkout@v4`, `actions/setup-node@v4`.
3. **Avtomatlashtirilgan Testlar Nima Uchun Kerak?**
   - Inson xatoga moyil. CI esa har safar kodni 0 dan toza Linux muhitida yurgizib, regressiya (avval ishlagan kodning buzilishi) bor-yo'qligini tekshiradi.
4. **Yashil Qushcha (Green Checkmark) vs Qizil Xoch (Red Cross):**
   - Agar bitta test yiqilsa, PR merge qilinishiga yo'l qo'yilmaydi (Branch Protection).

---

## 2. 45 Daqiqalik Dars Taqsimoti

| Vaqt | Bosqich | O'qituvchi va O'quvchi Faoliyati |
|---|---|---|
| **00:00 – 03:00** | Kirish va Korporativ Holat | "Tasavvur qiling, 50 kishilik jamoada kimdir xato kodni production serverga push qilib yubordi va butun sayt quladi. Buni qanday oldini olamiz?" |
| **03:00 – 12:00** | Nazariya: CI/CD va GitHub Actions | Slaydlar orqali CI va CD farqi, YAML sintaksisi, runnerlar, job va steplar tushuntiriladi. |
| **12:00 – 18:00** | `.github/workflows/main.yml` Anatomiyasi | YAML indentatsiyasi (bo'sh joylar), triggerlar va buyruqlar (`run: npm test`). |
| **18:00 – 24:00** | Branch Protection va Green Checkmarks | PR sahifasida botlarning tekshiruvi: nega qizil xoch chiqqanda merge tugmasi bloklanadi. |
| **24:00 – 38:00** | Amaliy Laboratoriya (CI/CD Pipeline Simulator) | `lab/index.html` interaktiv trenajyorida virtual GitHub Actions pipeline'ini ishga tushirish: linter xatosini topish, testni to'g'rilash va yashil deployga erishish! |
| **38:00 – 43:00** | Varaqa va Mustahkamlash | Varaqadagi YAML sintaksis mashqlari va CI/CD bosqichlarini to'ldirish. |
| **43:00 – 45:00** | Xulosa va Baholash | 10 ballik tizim bo'yicha baholash va 3-hafta Git/DevOps bloki yakuni. |

---

## 3. O'quvchilar Ko'p Yo'l Qo'yadigan Xatolar (Tuzoqlar)

1. **YAML da TAB ishlatish:**
   - YAML tili TAB (`\t`) belgilarini mutlaqo qabul qilmaydi! Faqat 2 ta bo'sh joy (space) ishlatilishi shart.
2. **Joblar ketma-ketligi va `needs`:**
   - Agar `deploy` jobi `test` jobi o'tishini kutmasa, buzuq kod internetga chiqib ketadi (`needs: [lint, test]`).
3. **Sirlar (Secrets) va API Kalitlar:**
   - Hech qachon shaxsiy parollarni YAML ichida ochiq yozmaslik: `${{ secrets.VERCEL_TOKEN }}` dan foydalanish shart.
