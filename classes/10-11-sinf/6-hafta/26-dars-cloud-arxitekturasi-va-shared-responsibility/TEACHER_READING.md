# O'qituvchi Uchun Yo'riqnoma: 26-dars

## Dars Mavzusi
**Cloud Arxitekturasi va Umumiy Mas'uliyat Modeli (Shared Responsibility Model): IaaS, PaaS, SaaS va Bulut Xavfsizligi Posturasi (CSPM)**

- **Kohorta:** 10–11-sinflar (Senior Muhandislik & Kiberxavfsizlik treki)
- **Hafta:** 6-hafta (Cloud Security va DevSecOps)
- **Vaqt me'yori:** 45 daqiqa
- **Sana:** 12.10.2026

---

## 1. Dars Maqsadi va Natijalar

### Asosiy Maqsad:
O'quvchilarda bulutli muhitlarga (AWS, GCP, Azure) ko'chish xavfsizlikni avtomatik kafolatlamasligini tushuntirish, provayder va mijoz o'rtasidagi **Shared Responsibility** chegaralarini chuqur o'rgatish hamda haqiqiy kiber-halokatlar (Tesla Kubernetes Cryptojacking) orqali xavfsizlik posturasini (CSPM) to'g'ri o'rnatish ko'nikmasini shakllantirish.

### Kutilayotgan O'lchanadigan Natijalar (Success Criteria):
1. O'quvchi IaaS, PaaS va SaaS qatlamlarida provayder ("Security OF the Cloud") va mijoz ("Security IN the Cloud") javobgarligini adashmasdan ajrata oladi.
2. O'quvchi Gartner'ning 99% qoidasini va inson omili (misconfiguration) keltirib chiqaradigan oqibatlarni tushuntirib bera oladi.
3. Tesla keysi misolida parolsiz boshqaruv paneli va konteyner ichidagi ochiq IAM kalitlari oqibatlarini tahlil qilib, 3 ta aniq arxitekturaviy to'siqni taklif qiladi.
4. CIS AWS Foundation Benchmark bo'yicha Root account taqiqi, majburiy MFA va CloudTrail logging auditini asoslab beradi.

---

## 2. Vaqt Taqsimoti (45 daqiqa)

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchi Harakati |
|---|---|---|---|
| **0–4 daq** | **Kirish & Starter** | On-Premises podvaldagi serverlar va AWS/GCP bulutli dunyosi o'rtasidagi farqni so'rash. | Bulut afzalliklari va yangi xavf nuqtalarini muhokama qilish. |
| **4–10 daq** | **Tushuntirish (IaaS/PaaS/SaaS)** | 3 ta servis modelini va texnologik stak qatlamlari egaligini doskada chizish. | Slayd 3 jadvalini o'rganish va farqlarni ajratish. |
| **10–17 daq** | **Shared Responsibility & 99% Qoidasi** | "Security OF vs IN the Cloud" mantrasini tushuntirish. Gartner prognozini tahlil qilish. | Nega AWS ga o'tish ISO sertifikatini avtomatik bermasligini tushunish. |
| **17–25 daq** | **Keys Tahlili: Tesla Kripto-Xakerligi** | Tesla hodisasining 3 bosqichli hujum grafigini (No Auth Kubernetes &rarr; Pod Secrets &rarr; EC2 Monero Mining) ko'rsatish. | Xatolik AWS Nitro yoki ЦОД da emas, Tesla muhandisida ekanini xulosa qilish. |
| **25–38 daq** | **Amaliy Ish (Mustaqil)** | Ishchi varaqadagi 1-qism (Matritsa) va 2-qism (Tesla Root Cause) topshiriqlarini boshqarish. | Noutbukda yoki qog'ozda arxitektura tahlilini bajarish. |
| **38–42 daq** | **CIS Benchmark & Xatolar Tahlili** | CIS 1.1, 1.2, 2.1, 3.1 qoidalarini mustahkamlash. 0.0.0.0/0 xavfini uqtirish. | Javoblarni o'zaro solishtirish va to'g'rilash. |
| **42–45 daq** | **Xulosa & Uy Vazifasi** | 10 ballik rubrika va 3 ta oltin qoidani e'lon qilish. | Ishchi varaqani topshirish. |

---

## 3. Laptop Bor / Yo'q (Dual-Path) Metodikasi

- **Noutbuki bor o'quvchilar:**
  - AWS Console yoki Terraform IAM JSON siyosatidagi `Action: *` va `Resource: *` xatolarini tahlil qiladi.
  - Ochiq S3 chelaklar va Kubernetes podlarining xavfsizlik konfiguratsiyalarini o'rganadi.
- **Noutbuki yo'q o'quvchilar:**
  - 2 betlik A4 ishchi varaqada (`varaqa.html`) IaaS/PaaS/SaaS stak jadvalini to'ldiradi.
  - Tesla kiber-hujumi zanjirini daftarda chizib, 3 ta to'siqni yozma asoslaydi.
  - CIS Benchmark chek-listi bo'yicha audit xulosasini tayyorlaydi.

---

## 4. Javoblar Kaliti (Teacher Answer Key)

### 1-qism: Mas'uliyat Matritsasi
- **Bino, server tokchalari, elektr ta'minoti:** IaaS = Provayder, PaaS = Provayder, SaaS = Provayder.
- **Linux OS va xavfsizlik patchlari:** IaaS = **Mijoz (Siz)**, PaaS = Provayder, SaaS = Provayder.
- **Tarmoq xavfsizlik guruhlari (Ochiq portlar):** IaaS = **Mijoz (Siz)**, PaaS = **Mijoz (Siz)**, SaaS = Provayder.
- **Foydalanuvchi parollari va IAM huquqlari:** IaaS = **Mijoz (Siz)**, PaaS = **Mijoz (Siz)**, SaaS = **Mijoz (Siz)**.
- **Ma'lumotlar bazasi va fayllarni shifrlash:** IaaS = **Mijoz (Siz)**, PaaS = **Mijoz (Siz)**, SaaS = **Mijoz (Siz)**.

### 2-qism: Gartner 99% Qoidasi
1. Ommaviy S3 chelakda `Public Read` yoki `Public Write` ni ochiq qoldirish.
2. Security Group da 22-port (SSH) yoki 3389-port (RDP) ni butun dunyoga (`0.0.0.0/0`) ochib qo'yish.
3. GitHub ommaviy repozitoriyasiga `.env` yoki `AWS_ACCESS_KEY_ID` ni xatolik bilan yuklash.

### 3-qism: Tesla Kiber-Halokati
- **3.1-savol:** Qatlam — **Security IN the Cloud (Mijoz mas'uliyati)**. AWS infratuzilmasi buzilmagan; Tesla muhandislari Kubernetes boshqaruv panelini parolsiz qoldirgan.
- **3.2-savol 3 ta to'siq:**
  1. *Autentifikatsiya:* Kubernetes Dashboard ga majburiy OIDC / MFA kirishini o'rnatish.
  2. *Tarmoq Izolyatsiyasi:* Boshqaruv panelini faqat ichki VPN / Private Subnet orqali ochish (Public IP bermaslik).
  3. *IAM Least Privilege & Roles:* Konteyner ichiga statik uzoq muddatli AWS kalitlarini joylashtirmaslik; uning o'rniga qat'iy cheklangan vaqtinchalik IAM Role (IRSA / Instance Profile) berish.

---

## 5. Baholash Mezoni (10 Ball)
- **1-3 ball:** Matritsadagi IaaS/PaaS/SaaS qatlamlarining to'g'ri taqsimlanishi.
- **4-7 ball:** Tesla keysining chuqur texnik tahlili va 3 ta arxitektura to'sig'ining to'g'ri ko'rsatilishi.
- **8-10 ball:** CIS AWS Benchmark standartlari va Root account taqiqi mantiqining asoslanishi.
