# O'qituvchi Uchun Yo'riqnoma: 29-dars

## Dars Mavzusi
**HashiCorp Vault va Maxfiy Kalitlar Boshqaruvi: Secret Sprawl, Dinamik Sirlar va TTL**

- **Kohorta:** 10–11-sinflar (Senior Muhandislik & Kiberxavfsizlik treki)
- **Hafta:** 6-hafta (Cloud Security va DevSecOps)
- **Vaqt me'yori:** 45 daqiqa
- **Sana:** 12.10.2026

---

## 1. Dars Maqsadi va Natijalar

### Asosiy Maqsad:
O'quvchilarga an'anaviy statik parollar va `.env` fayllarining zaifligini (Secret Sprawl muammosi) tushuntirish, HashiCorp Vault markaziy seyf arxitekturasini o'rgatish, Shamir's Secret Sharing algoritmi (3 of 5 unseal) yordamida seyfni xavfsiz ochishni, vaqtinchalik dinamik hisoblar yaratishni (Dynamic Secrets with TTL) va avtomatlashgan mashinalar uchun AppRole autentifikatsiyasini amalda qo'llashni o'rgatish.

### Kutilayotgan O'lchanadigan Natijalar (Success Criteria):
1. O'quvchi statik sirlar nima uchun vaqt o'tishi bilan o'g'irlanishi muqarrar ekanini va Vault ning "Secrets as a Service" yechimini tushuntira oladi.
2. O'quvchi Shamir's Secret Sharing matematik formulasining afzalligini (ichki xiyonatga qarshi konsensus talabi) asoslab beradi.
3. O'quvchi Dynamic Secrets mexanizmini bayon qiladi: har bir mijoz uchun alohida foydalanuvchi yaratilishi va TTL tugagach avtomatik `DROP USER` bajarilishi.
4. O'quvchi `studio/index.html` laboratoriyasida 4 ta kvestni (Unseal, KV v2 put, Dynamic Postgres creds, Emergency Revocation) to'liq bajarib, HashiCorp Vault Arxitektori Sertifikatiga ega bo'ladi.

---

## 2. Vaqt Taqsimoti (45 daqiqa)

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchi Harakati |
|---|---|---|---|
| **0–4 daq** | **Kirish & Muammo** | Secret Sprawl epidemiyasini (statik parollar Slack, `.env`, Git da qolib ketishi) tushuntirish. | Nega bitta o'g'irlangan parol 5 yil ishlab turishini tahlil qilish. |
| **4–10 daq** | **Vault Arxitekturasi & Storage Barrier** | Vault ning "Secrets as a Service" modeli va AES-256-GCM shifrlangan Storage Barrier mexanizmini ko'rsatish. | Slayd 3 dagi me'moriy bloklarni o'rganish. |
| **10–16 daq** | **Shamir's Secret Sharing (Unsealing)** | Master kalitni 5 bo'lakka bo'lish va kamida 3 nafar ofitser kaliti kiritilmaguncha seyf ochilmasligini uqtirish. | Varaqaning 2-bo'limidagi savolga javob yozish. |
| **16–22 daq** | **Dynamic Secrets & TTL Inqilobi** | Doimiy parollar o'rniga 10–60 daqiqalik vaqtinchalik DB hisoblarini yaratish va avtomatik o'chirishni ko'rsatish. | Statik vs Dinamik jadvalini to'ldirish. |
| **22–37 daq** | **Amaliy Laboratoriya (Vault Studio)** | `studio/index.html` ni ochish. O'quvchilarga Unseal qilish, Stripe kalitini saqlash, dinamik foydalanuvchi yaratish va favqulodda bekor qilish vazifasini berish. | CLI buyruqlarini bajarish va 4/4 kvestni yopish. |
| **37–41 daq** | **Keys Tahlili: Uber (2022)** | Uber tarmog'iga kirgan xaker PowerShell skriptidagi ochiq parol orqali butun PAM seyfini qo'lga kiritganini aytib berish. | AppRole himoyasini varaqada tahlil qilish. |
| **41–45 daq** | **Xulosa & Baholash** | 10 ballik mezon bo'yicha baholash, sertifikatlarni qabul qilish. | Sertifikatlarni namoyish qilish. |

---

## 3. Laptop Bor / Yo'q (Dual-Path) Metodikasi

- **Noutbuki bor o'quvchilar:**
  - `classes/10-11-sinf/6-hafta/29-dars-hashicorp-vault-va-maxfiy-kalitlar/studio/index.html` interaktiv muhitida ishlaydi.
  - 3 ta Shamir kalitini kiritib Vault ni unseal qiladi, dinamik Postgres hisobini chiqaradi, TTL taymerini kuzatadi va `vault lease revoke` qiladi.
- **Noutbuki yo'q o'quvchilar:**
  - 2 betlik A4 ishchi varaqada (`varaqa.html`) Shamir algoritmi xavfsizligini yozma bayon qiladi.
  - Statik va Dinamik sirlar taqqoslash jadvalini to'ldiradi.
  - Uber 2022 keysida PowerShell skripti o'rniga AppRole qanday xavfni to'xtatgan bo'lishini tahlil qiladi.

---

## 4. Javoblar Kaliti (Teacher Answer Key)

### 1-qism: Secret Sprawl va Downtime
- Nega statik parolni almashtirish downtime keltiradi: Chunki 50 ta mikroservisning konfiguratsiyasini bir vaqtda yangilab qayta ishga tushirish (restart) kerak bo'ladi. Agar bitta servis yangilanmay qolsa, u bazadan uziladi.
- Vault yechimi: Ilovalar parolni o'zida saqlamaydi, Vault dan oladi. Vault parolni yangilasa, barcha ilovalar navbatdagi so'rovida yangi kalitni avtomatik oladi.

### 2-qism: Shamir's Secret Sharing (3 of 5)
- Nega 2 ta kalit 0 ta ma'lumot beradi: Shamir algoritmi $k$-darajali ko'phadga (polynomial) asoslangan. 2 ta nuqta orqali 3-darajali parabolaning $y$-o'qidagi kesishish nuqtasini ($x=0$, ya'ni maxfiy kalitni) matematik jihatdan hisoblab bo'lmaydi.
- Ichki xiyonatdan himoya: Bitta g'arazgo'y admin kalitni o'g'irlasa ham, yana 2 nafar mas'ul shaxsning kalitisiz seyfni ocha olmaydi.

### 3-qism: Uber 2022 Kiber-Buzilishi va AppRole
- Agar Uber da HashiCorp Vault bo'lganida, PowerShell skriptida ochiq parol yozilmagan bo'lardi.
- Skript faqat qisqa muddatli AppRole tokeni orqali kirgan va har bir so'rovga 15 daqiqalik vaqtinchalik huquq berilgan bo'lardi. O'g'irlangan taqdirda ham token 15 daqiqada yonib bitar va boshqa tizimlarga kirish imkonsiz bo'lardi.

---

## 5. Baholash Mezoni (10 Ball)
- **1-3 ball:** Shamir algoritmining 3/5 chegarasi va Vault unsealing to'g'ri tushuntirilgan.
- **4-6 ball:** Statik vs Dinamik sirlar jadvali to'liq to'ldirilgan, TTL mohiyati yoritilgan.
- **7-8 ball:** AppRole mexanikasi va Uber 2022 kiber-buzilishi saboqlari tahlil qilingan.
- **9-10 ball:** Vault Studio dagi barcha 4 ta kvest bajarilgan va Sertifikat taqdim etilgan.
