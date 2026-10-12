# O'qituvchi Uchun Yo'riqnoma: 30-dars

## Dars Mavzusi
**DevSecOps Quvuri va Cloud Audit Demo Day: CI/CD Security Gates, Trivy, Secret Scanning va Yakuniy Himoya**

- **Kohorta:** 10–11-sinflar (Senior Muhandislik & Kiberxavfsizlik treki)
- **Hafta:** 6-hafta (Cloud Security va DevSecOps — Capstone Demo Day)
- **Vaqt me'yori:** 45 daqiqa
- **Sana:** 12.10.2026

---

## 1. Dars Maqsadi va Natijalar

### Asosiy Maqsad:
O'quvchilarga zamonaviy DevSecOps falsafasini ("Xavfsizlik rivojlanish to'sig'i emas, avtomatlashtirilgan qalqondir") tushuntirish, GitHub Actions CI/CD quvurida 4 ta xavfsizlik darvozasini (Gitleaks, Semgrep SAST, Checkov IaC, Trivy Container CVE) o'rnatish, "Break the Build" (Exit Code 1) qoidasini amalda qo'llash hamda 6-hafta davomida o'rganilgan barcha mavzularni (Shared Responsibility, S3 BPA, Terraform, Vault) umumlashtirib, interaktiv **DevSecOps Studio** simulatorida Demo Day loyihalarini himoya qilish.

### Kutilayotgan O'lchanadigan Natijalar (Success Criteria):
1. O'quvchi DevOps va DevSecOps o'rtasidagi farqni hamda Shift-Left modelining iqtisodiy foydasini asoslay oladi.
2. O'quvchi CI/CD quvuridagi 4 ta avtomatlashgan darvozaning (Gitleaks, Semgrep, Checkov, Trivy) har birining vazifasini va "Break the Build" siyosatini bayon qiladi.
3. O'quvchi SolarWinds (2020) hujumini tahlil qilib, dasturiy ta'minot zanjiri xavfsizligini (SBOM, Cosign/Sigstore) tushuntiradi.
4. O'quvchi `studio/index.html` laboratoriyasida zaif PR #104 ni tahlil qilib, 4 ta zaiflikni bartaraf etadi, 100% yashil quvur bilan AWS Cloud ga deploy qiladi va **Master Cloud DevSecOps Auditor Diplomini** himoya qiladi.

---

## 2. Vaqt Taqsimoti (45 daqiqa)

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchi Harakati |
|---|---|---|---|
| **0–4 daq** | **Kirish & Starter** | DevOps va xavfsizlik jamoalari o'rtasidagi tarixiy ziddiyatni va nega xavfsizlik to'siq emas, avtomat quvur bo'lishi kerakligini tushuntirish. | "Security as a blocker" muammosini muhokama qilish. |
| **4–10 daq** | **4 Ta Security Gates Arxitekturasi** | GitHub Actions quvurida ketma-ket joylashgan 4 ta darvozani (Gitleaks &rarr; Semgrep &rarr; Checkov &rarr; Trivy) ko'rsatish. | Slayd 3 dagi me'moriy bloklarni o'rganish. |
| **10–16 daq** | **Break the Build & YAML Quvuri** | `exit-code: 1` qoidasi va nega `continue-on-error: true` kiber-xiyonat ekanini uqtirish. `.github/workflows/devsecops.yml` sintaksisini ko'rsatish. | Varaqaning 1 va 3-bo'limlariga javob yozish. |
| **16–22 daq** | **SolarWinds Keysi & Supply Chain** | 2020-yildagi Sunburst hujumi (CI/CD serverining o'zi buzilishi) saboqlarini tushuntirish. SBOM va Cosign imzosini ko'rsatish. | Varaqaning 4-bo'limini to'ldirish. |
| **22–37 daq** | **Capstone Demo Day Himoyasi (Studio)** | `studio/index.html` ni ochish. O'quvchilarga qizil quvurni yashilga aylantirib, AWS ga muvaffaqiyatli deploy qilish vazifasini berish. | Quvurni yurgizish, xatolarni tuzatish va diplomni himoya qilish. |
| **37–41 daq** | **Hafta Yakuni (Capstone Recount)** | 6-hafta davomida o'rganilgan 5 ta mavzuni (Shared Responsibility, S3 BPA, Terraform, Vault, DevSecOps) umumlashtirish. | 5 qatlamli mudofaa zanjirini takrorlash. |
| **41–45 daq** | **Xulosa & Baholash** | 10 ballik mezon bo'yicha baholash, diplomlarni topshirish va tabriklash. | Diplomlarni namoyish qilish. |

---

## 3. Laptop Bor / Yo'q (Dual-Path) Metodikasi

- **Noutbuki bor o'quvchilar:**
  - `classes/10-11-sinf/6-hafta/30-dars-devsecops-quvuri-va-cloud-audit-demo-day/studio/index.html` simulyatorida ishlaydi.
  - Zaif commit diff ni ko'radi, quvurni yurgizib 4 ta skanerning qizil xatolarini tekshiradi, tuzatishlarni qo'llab yashil deploy qiladi va Diplom oladi.
- **Noutbuki yo'q o'quvchilar:**
  - 2 betlik A4 ishchi varaqada (`varaqa.html`) 4 ta Security Gates spetsifikatsiyasi jadvalini to'ldiradi.
  - PR #104 refaktoring jadvalida zaif va to'g'ri kodlarni solishtirib yozadi.
  - SolarWinds kiber-halokati bo'yicha 2 ta himoya chorasini yozadi.

---

## 4. Javoblar Kaliti (Teacher Answer Key)

### 1-qism: "Break the Build" (Exit Code 1)
- Nega Exit Code 1 yagona kafolat: Chunki agar skaner zaiflik topganda quvurni qizil qilib to'xtatmasa, avtomatlashgan CD (Continuous Delivery) mexanizmi zaif kodni to'g'ridan-to'g'ri ishlab chiqarish serveriga (AWS) chiqarib yuboradi. Faqat `exit 1` deploy qadamining bajarilishiga jismonan to'sqinlik qiladi.

### 2-qism: `continue-on-error: true` Xatosi
- Bu xato qo'yilganda, GitHub Actions skaner topgan xatolarni "shunchaki ma'lumot" sifatida qabul qiladi va quvur yashil bo'lib qolaveradi. Dasturchilar xatolarni o'qimaydi, natijada barcha zaifliklar baribir ishlab chiqarishga chiqib ketadi.

### 3-qism: SolarWinds (2020) Keysi Saboqlari
1. **SBOM (Software Bill of Materials):** Dastur ichidagi barcha paketlar, ularning xesh qiymatlari va ochiq kodli kutubxonalarning to'liq inventar ro'yxatini yuritish.
2. **Kriptografik Raqamli Imzo (Sigstore / Cosign):** Kompilyatsiya qilingan har bir ikkilik fayl yoki Docker obrazini CI/CD quvuridan chiqishda apparat kaliti bilan imzolash. Imzosi bo'lmagan fayllarni serverlar ishga tushirmaydi.

---

## 5. Baholash Mezoni (10 Ball)
- **1-3 ball:** 4 ta Security Gates (Gitleaks, Semgrep, Checkov, Trivy) vazifalari to'g'ri yoritilgan.
- **4-6 ball:** "Break the Build" siyosati va SolarWinds dasturiy zanjir hujumi tahlil qilingan.
- **7-8 ball:** PR #104 refaktoring jadvali to'liq to'ldirilgan.
- **9-10 ball:** DevSecOps Studio dagi barcha kvestlar bajarilgan, 100% yashil quvur orqali deploy qilingan va Diplom himoya qilingan.
