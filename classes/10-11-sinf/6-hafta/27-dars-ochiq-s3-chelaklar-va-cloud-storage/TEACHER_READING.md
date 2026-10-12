# O'qituvchi Uchun Yo'riqnoma: 27-dars

## Dars Mavzusi
**Ochiq S3 Chelaklar va Cloud Storage Zaifliklari: Bucket ACLs, IAM Policies va Kiber-Szishlar**

- **Kohorta:** 10–11-sinflar (Senior Muhandislik & Kiberxavfsizlik treki)
- **Hafta:** 6-hafta (Cloud Security va DevSecOps)
- **Vaqt me'yori:** 45 daqiqa
- **Sana:** 12.10.2026

---

## 1. Dars Maqsadi va Natijalar

### Asosiy Maqsad:
O'quvchilarga AWS S3 ob'ektlar xotirasining ichki ishlash mexanizmini tushuntirish, ochiq chelaklar (Exposed S3 Buckets) qanday qilib o'nlab gigabayt shaxsiy ma'lumotlar va parollarning tarqalib ketishiga sabab bo'lishini ko'rsatish, AWS Block Public Access (BPA) ning 4 ta qalqonini o'rgatish hamda interaktiv **S3 Defender Studio** laboratoriyasida zaif chelaklarni himoyalash ko'nikmasini shakllantirish.

### Kutilayotgan O'lchanadigan Natijalar (Success Criteria):
1. O'quvchi AWS S3 da ACL (Access Control Lists) va JSON Bucket Policy o'rtasidagi farqni tushuntira oladi.
2. O'quvchi `"Principal": "*"` va `"Action": "s3:GetObject"` kombinatsiyasi nima uchun xavfli ekanini ko'rsatib, uni `aws:sourceVpce` VPC Endpoint sharti bilan xavfsiz holatga o'tkazadi.
3. O'quvchi Block Public Access ning 4 ta flagi (`BlockPublicAcls`, `IgnorePublicAcls`, `BlockPublicPolicy`, `RestrictPublicBuckets`) vazifasini to'g'ri bayon qiladi.
4. O'quvchi `studio/index.html` laboratoriyasida 4 ta chelakni audit qilib, botnet hujumlarini `HTTP 403 Forbidden` bilan qaytaradi va Auditor Sertifikatini oladi.

---

## 2. Vaqt Taqsimoti (45 daqiqa)

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchi Harakati |
|---|---|---|---|
| **0–4 daq** | **Kirish & Starter** | Accenture (137 GB) va Verizon kiber-falokatlarini aytib, xakerlar qanday qilib bitta buyruq bilan hamma narsani yuklab olganini so'rash. | `aws s3 sync --no-sign-request` mexanizmini muhokama qilish. |
| **4–10 daq** | **S3 Arxitekturasi & ACL vs Policy** | S3 yassi ob'ektlar fazosi va global unikal URL ekanini tushuntirish. Eski ACL lar nima uchun bekor qilinayotganini ko'rsatish. | Slayd 3 va 4 dagi taqqoslashni o'rganish. |
| **10–16 daq** | **Zaif Siyosat & BPA Qalqonlari** | JSON siyosatdagi `"Principal": "*"` qopqonini tahlil qilish. Block Public Access (BPA) ning 4 ta qutqaruv tugmasini tushuntirish. | Varaqadagi 1-jadvalni to'ldirish. |
| **16–22 daq** | **Shifrlash (SSE-S3 vs SSE-KMS)** | Shifrlash turlarini va KMS kalitlarining 2 bosqichli himoyasini (CloudTrail audit izi bilan) tushuntirish. | `kms:Decrypt` ruxsatisiz xaker faylni o'qiy olmasligini uqish. |
| **22–37 daq** | **Amaliy Laboratoriya (S3 Defender Studio)** | `studio/index.html` ni ishga tushirish. KYC pasportlar va baza zaxiralarini himoyalash kvestlarini berish. | BPA ni yoqish, JSON siyosatni tuzatish va xaker bot hujumini qaytarish. |
| **37–41 daq** | **CIS Benchmark & Xatolar Tahlili** | `AuthenticatedUsers` tuzog'ini (bu xodimlar emas, butun dunyodagi har qanday AWS egasi) fosh qilish. | CIS S3 2.1 qoidalarini mustahkamlash. |
| **41–45 daq** | **Xulosa & Baholash** | 10 ballik rubrika bo'yicha laboratoriya va varaqalarni baholash. | Sertifikatlarni namoyish qilish. |

---

## 3. Laptop Bor / Yo'q (Dual-Path) Metodikasi

- **Noutbuki bor o'quvchilar:**
  - `classes/10-11-sinf/6-hafta/27-dars-ochiq-s3-chelaklar-va-cloud-storage/studio/index.html` simulyatorida ishlaydi.
  - S3 chelaklarida BPA ni yoqadi, JSON siyosatni tahrirlaydi, live terminalda hujumlarni sinaydi va Sertifikat oladi.
- **Noutbuki yo'q o'quvchilar:**
  - 2 betlik A4 ishchi varaqada (`varaqa.html`) 4 ta BPA qalqonini tahlil qiladi.
  - Berilgan zaif JSON siyosatdan xatoni topib, o'ng tomonga qalam bilan to'g'ri `Condition: { StringEquals: { aws:sourceVpce: ... } }` siyosatini yozadi.
  - S3 Audit hisoboti jadvalini to'ldiradi.

---

## 4. Javoblar Kaliti (Teacher Answer Key)

### 1-qism: S3 BPA ning 4 ta Qalqoni
1. **BlockPublicAcls:** Yangi yuklanayotgan fayllarga ommaviy ACL qo'yilishini to'xtatadi.
2. **IgnorePublicAcls:** Chekdagi barcha mavjud ommaviy ACL larni rad etadi va hisobga olmaydi.
3. **BlockPublicPolicy:** Ommaviy kirish beruvchi har qanday yangi Bucket Policy saqlanishiga yo'l qo'ymaydi.
4. **RestrictPublicBuckets:** Kirishni faqat AWS hisob egasi va ichki servislarga cheklaydi.

### 2-qism: 'AuthenticatedUsers' Tuzog'i
- `AuthenticatedUsers` — bu kompaniya xodimlari EMAS! Bu dunyodagi istalgan odam bo'lib, o'zining shaxsiy bepul AWS hisobiga ega bo'lsa kifoya. Agar chelakka `AuthenticatedUsers` ruxsati berilsa, dunyodagi har qanday xaker o'z AWS CLI orqali barcha fayllarni erkin o'g'irlay oladi!

### 3-qism: Tuzatilgan JSON Siyosat
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::kyc/*",
      "Condition": {
        "StringEquals": {
          "aws:sourceVpce": "vpce-1a2b3c4d"
        }
      }
    }
  ]
}
```

---

## 5. Baholash Mezoni (10 Ball)
- **1-3 ball:** 4 ta BPA qalqonining to'g'ri bayon qilinishi va ACL farqining tushuntirilishi.
- **4-7 ball:** `aws:sourceVpce` shartiga ega bo'lgan to'g'ri JSON siyosatining yozilishi.
- **8-10 ball:** S3 Defender Studio dagi 4 ta kvestning to'liq bajarilishi va xaker hujumining HTTP 403 bilan to'xtatilishi.
