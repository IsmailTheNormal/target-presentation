# O'qituvchi Uchun Yo'riqnoma: 28-dars

## Dars Mavzusi
**Infratuzilma Kod Sifatida (IaC) va Terraform Xavfsizligi: HCL, tfstate Sirlari va Trivy/Checkov Skanerlash**

- **Kohorta:** 10–11-sinflar (Senior Muhandislik & Kiberxavfsizlik treki)
- **Hafta:** 6-hafta (Cloud Security va DevSecOps)
- **Vaqt me'yori:** 45 daqiqa
- **Sana:** 12.10.2026

---

## 1. Dars Maqsadi va Natijalar

### Asosiy Maqsad:
O'quvchilarga Infratuzilma Kod Sifatida (Infrastructure as Code - IaC) paradigmasini tushuntirish, HashiCorp Terraform va uning konfiguratsiya tili HCL (HashiCorp Configuration Language) sintaksisini o'rgatish, Terraform ning eng katta zaifligi bo'lgan `terraform.tfstate` faylidagi ochiq sirlar (Plaintext Secret Sprawl) xavfini tahlil qilish hamda Checkov / Trivy statik kod tahlili vositalari orqali Shift-Left xavfsizlik darvozalarini qurish.

### Kutilayotgan O'lchanadigan Natijalar (Success Criteria):
1. O'quvchi ClickOps (qo'lda sozlash) va Deklarativ IaC o'rtasidagi farqni hamda avtomatlashtirish xatarlarni ham masshtablashini tushuntira oladi.
2. O'quvchi `terraform.tfstate` fayli nima uchun barcha resurs parollarini ochiq matnda saqlashini va uni himoyalashning 3 ta ustunini (S3 Remote State, KMS CMK shifrlash, DynamoDB State Locking) asoslab beradi.
3. O'quvchi CIS AWS Benchmark 2.1 bo'yicha Checkov qoidalarini (`CKV_AWS_24`, `CKV_AWS_20`, `CKV_AWS_145`, `CKV_AWS_17`) tushunib, zaif HCL kodini xavfsiz holatga keltiradi.
4. O'quvchi `studio/index.html` laboratoriyasida zaif `main.tf` faylini tahlil qilib, 5 ta qoidabuzarlikni bartaraf etadi va 100% natija bilan DevSecOps IaC Auditor Sertifikatini qo'lga kiritadi.

---

## 2. Vaqt Taqsimoti (45 daqiqa)

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchi Harakati |
|---|---|---|---|
| **0–4 daq** | **Kirish & Muammo** | ClickOps falokatini (50 ta chekbox va inson omili) va IaC ning ikki tomonlama tig'ini (bitta xato git commit 100 ta serverni ochib qo'yishi) tushuntirish. | Slayd 2 dagi taqqoslashni muhokama qilish. |
| **4–10 daq** | **HCL Anatomiyasi & Ishlash Tsikli** | `resource "aws_security_group" "web_sg"` sintaksisini, `init`, `plan`, `apply`, `destroy` bosqichlarini ko'rsatish. | Quruq sinov (`plan`) mohiyatini tushunish. |
| **10–16 daq** | **`terraform.tfstate` Falokati** | Terraform ning eng katta sirini fosh qilish: `tfstate` JSON faylida barcha parollar ochiq matnda saqlanadi. `sensitive = true` faqat CLI stdout da yashirishini uqtirish. | Varaqaning 1-bo'limidagi savolga javob yozish. |
| **16–22 daq** | **Xavfli Standartlar & Checkov Qoidalari** | 0.0.0.0/0 dan SSH 22-port ochiq qolishi, ommaviy RDS va shifrlanmagan EBS disklarni tahlil qilish. Checkov AST tahlilini tushuntirish. | Varaqadagi Checkov qoidalari jadvalini to'ldirish. |
| **22–37 daq** | **Amaliy Laboratoriya (Terraform Studio)** | `studio/index.html` ni ochish. O'quvchilarga 5 ta zaiflikni tuzatish va `Run Checkov Scan` ni ishga tushirish vazifasini berish. | HCL kodni to'g'rilash, skanerlash va 100% reytingga erishish. |
| **37–41 daq** | **Keys Tahlili: Code Spaces (2014)** | Code Spaces kompaniyasi AWS kalitlari sizishi oqibatida 12 soatda butunlay yo'q qilinganini aytib berish. Zaxira nusxalar va MFA Delete ahamiyati. | Varaqaning 5-bo'limini to'ldirish. |
| **41–45 daq** | **Xulosa & Baholash** | 10 ballik rubrika bo'yicha baholash, sertifikatlarni tekshirish va xulosa qilish. | Sertifikatlarni topshirish. |

---

## 3. Laptop Bor / Yo'q (Dual-Path) Metodikasi

- **Noutbuki bor o'quvchilar:**
  - `classes/10-11-sinf/6-hafta/28-dars-infratuzilma-kod-sifatida-terraform-xavfsizligi/studio/index.html` muhitida ishlaydi.
  - HCL kod muharririda zaifliklarni to'g'rilaydi, `checkov -f main.tf` skanerini yurgizadi va 100% natija bilan Sertifikat eksport qiladi.
- **Noutbuki yo'q o'quvchilar:**
  - 2 betlik A4 ishchi varaqada (`varaqa.html`) `.tfstate` xavflarini yozma tahlil qiladi.
  - Berilgan zaif HCL bloklarini (Security Group va RDS) qalam bilan xavfsiz HCL sintaksisiga o'zgartiradi.
  - Code Spaces falokati bo'yicha 2 ta himoya chorasini yozadi.

---

## 4. Javoblar Kaliti (Teacher Answer Key)

### 1-qism: `terraform.tfstate` va S3 Remote Backend
- Nega ochiq Git omboriga `.tfstate` tushishi falokat: Chunki Terraform barcha ma'lumotlar bazasi parollari, IAM sirlari va API kalitlarini shifrlanmagan holatda `attributes` bloki ichida saqlaydi. Git ga tushgan zahoti xakerlar parollarni o'qiydi.
- S3 Remote State + KMS yechimi: `.tfstate` fayli dasturchi noutbukida emas, xavfsiz markaziy S3 chelagida saqlanadi, har bir bayt AWS KMS apparat kaliti bilan shifrlanadi va unga faqat avtomatlashgan CI/CD serveri kira oladi.

### 2-qism: To'g'rilangan HCL Kodi
1. **Security Group:**
```hcl
resource "aws_security_group" "sg" {
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.50.0/24"] # Faqat ichki VPN CIDR
  }
}
```
2. **RDS Instance:**
```hcl
resource "aws_db_instance" "db" {
  manage_master_user_password = true # Parol kodda emas, AWS Secrets Manager da
  publicly_accessible         = false
}
```

### 3-qism: Code Spaces Halokati Saboqlari
1. **Zaxiralarni izolyatsiya qilish va MFA Delete:** Hech qachon ishlab chiqarish va zaxira serverlarini bitta AWS hisobida boshqarmaslik, zaxiralarda MFA Delete ni majburiy qilish.
2. **Statik Root kalitlarni yo'qotish:** Kodda hech qachon uzoq muddatli `AKIA...` root kalitlarini saqlamaslik, faqat qisqa muddatli IAM AssumeRole va Vault tokenlaridan foydalanish.

---

## 5. Baholash Mezoni (10 Ball)
- **1-3 ball:** `.tfstate` ochiq matn muammosi va S3 Remote State mohiyati to'g'ri yoritilgan.
- **4-6 ball:** HCL refaktoringi to'g'ri bajarilgan, CKV qoidalari aniq tushuntirilgan.
- **7-8 ball:** Shift-Left tamoyili va Code Spaces keysi tahlili chuqur yozilgan.
- **9-10 ball:** Terraform Studio laboratoriyasida barcha 5 ta xato tuzatilgan va 100% li Sertifikat ilova qilingan.
