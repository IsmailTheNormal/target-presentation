# 32-Dars: O'qituvchi Uchun Metodik Qo'llanma va Imtihon Kaliti (Teacher Guide & Fixes)
**Target International School // 10–11-Sinf // 8-Hafta (1-Chorak Oraliq Nazorat: 40 daqiqa)**
**Mavzu:** Korporativ Tarmoq Himoyasi va CTF Kiber-Turniri (NIST SP 800-61, Blue Team vs Red Team)
**Kohorta:** `10A 10B 11A 11B` (Senior AI & Enterprise Cybersecurity)

---

## 1. Asosiy Pedagogik Maqsad
10–11-sinf o'quvchilari uchun 1-chorak oraliq imtihoni. O'quvchilar xalqaro NIST SP 800-61 standarti bo'yicha kiber-hodisalarni boshqarish, UFW va Syslog orqali perimetrni himoyalash, Red Team ekspluatatsiyasi bilan bayroqlarni olish (Capture The Flag) hamda MTTR (Mean Time to Remediation) ko'rsatkichini hisoblashni himoya qiladilar.

---

## 2. Test Savollari va O'qituvchi Yechimlar Kaliti (Test & Fixes Key)

### Test 1: SSH Brute-Force Log Audit
* **Hodisa:** Syslog faylida 198.51.100.44 IP manzilidan sekundiga 80 ta muvaffaqiyatsiz root kirish urinishlari qayd etilmoqda.
* **Blue Team Tezkor Yechimi (Fix):**
  ```bash
  # 1. IP ni xavfsizlik devorida zudlik bilan bloklash:
  sudo ufw insert 1 deny from 198.51.100.44 to any
  # 2. Xizmatni qayta tekshirish:
  sudo ufw status numbered
  # 3. /etc/ssh/sshd_config da root kirishni butkul taqiqlash:
  PermitRootLogin no
  PasswordAuthentication no
  sudo systemctl reload sshd
  ```

### Test 2: MTTR Hisobi
* **Vaziyat:** Hujum boshlangan vaqt: `14:15:30 UTC`. Izolyatsiya va UFW bloklangan vaqt: `14:28:10 UTC`.
* **Hisob:** 14:28:10 - 14:15:30 = 12 daqiqa 40 soniya (760 soniya). MTTR = **12 min 40 s**.

---

## 3. Uy Vazifasi (`vazifa.html`) Baholash Mezoni (10 Ball)
* **NIST SP 800-61 Bosqichlari (4 ball):** 4 ta faza (Tayyorgarlik, Aniqlash, Izolyatsiya, Tahlil) to'liq yoritilgan.
* **MTTR Hisobi va Matematika (3 ball):** Vaqt oralig'i sekundigacha to'g'ri topilgan.
* **Blue Team Himoya Buyruqlari (2 ball):** UFW va SSH hardening buyruqlari xatosiz kiritilgan.
* **Post-Mortem Xulosalar (1 ball):** Korporativ tarmoq xavfsizligini ta'minlash choralari asoslangan.
