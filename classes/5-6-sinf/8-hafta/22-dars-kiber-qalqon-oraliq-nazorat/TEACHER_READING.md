# 22-Dars: O'qituvchi Uchun Metodik Qo'llanma va Imtihon Kaliti (Teacher Guide & Fixes)
**Target International School // 5–6-Sinf // 8-Hafta (1-Chorak Oraliq Nazorat: 40 daqiqa)**
**Mavzu:** Kiber-Qalqon Viktorinasi va Amaliy Sinov (Parollar, Fishing, Troyanlar va EXIF Maxfiylik)
**Kohorta:** `5A 5B 6A 6B` (Junior Cyber Guardians & Safe Internet)

---

## 1. Asosiy Pedagogik Maqsad
5–6-sinf o'quvchilari uchun 1-chorak oraliq imtihoni. O'quvchilar internetdagi 4 ta asosiy xavfni fosh etish ko'nikmalarini himoya qiladilar:
1. 14+ belgili mustahkam parollar tuzish va 2FA himoyasini tushunish.
2. Fishing havolalarini soxta harflar va shubhali domenlar orqali 3 soniyada aniqlash.
3. Tekin mod/cheat niqobi ostidagi troyan dasturlarini ochmaslik va VirusTotal da tekshirish.
4. Suratlardagi yashirin GPS koordinatalarini o'chirish va "Katta Ekran Qoidasi" (Billboard Rule) ga rioya qilish.

---

## 2. Test Savollari va O'qituvchi Yechimlar Kaliti (Test & Fixes Key)

### Test 1: Shubhali Fayl Tashxisi
* **Holat:** O'quvchiga do'sti nomidan «minecraft_skin_super.zip.exe» fayli yuborildi.
* **Tashxis:** Bu soxta ikki qavatli kengaytma (Double Extension) hiylasidir. Windows operatsion tizimi `.exe` kengaytmasini yashirishi mumkin, natijada foydalanuvchi uni oddiy `.zip` arxiv deb o'ylab ochadi va troyan stealer kompyuterdagi parollarni o'g'irlaydi.
* **To'g'ri Harakat (Fix):**
  1. Faylni aslo ochmaslik!
  2. Uni darhol `virustotal.com` saytiga yuklab 70 ta antivirus bilan tekshirish.
  3. Xavfli ekani tasdiqlangach, faylni butkul o'chirib tashlash.

---

## 3. Onlayn Kiber-Test (10 ta Savol — 10 Ball) Javoblar Kaliti (`test.html`)

| # | Mavzu | To'g'ri Javob | Kiber-Tushuntirish |
|---|---|---|---|
| **Q1** | Parollar va Entropiya | **A** (14+ belgi, katta/kichik, son, simvol) | Oddiy lug'at so'zlari va ismlar 1 millisekundda buziladi. 14+ belgili 3 ta so'z paroli asrlar davomida buzulmaydi. |
| **Q2** | Fishing (Bepul Robux) | **A** (Sahifani darhol yopish, parolni kiritmaslik) | Tekin pishloq faqat qopqonda bo'ladi. Begonalar qimmat o'yin pullarini bepul bermaydi. |
| **Q3** | Troyan (.png.exe) | **A** (Zararli .exe dastur rasm niqobida) | Windows kengaytmalarni yashirishi orqali aldov. Oxiri .exe bo'lgan fayl bu rasm emas, bajariluvchi dasturdir. |
| **Q4** | Antivirus yolg'oni | **A** (Antivirusni o'chirmaslik, VirusTotalda tekshirish) | Xakerlar virus tushirish uchun "bu xato signal, o'chirib qo'y" deb aldashadi. |
| **Q5** | Soxta Adminlar (Telegram/Roblox) | **A** (SMS kodni bermaslik, kontaktni bloklash) | SMS tasdiqlash kodi hisob kalitidir. Haqiqiy ma'muriyat kodni hech qachon so'ramaydi. |
| **Q6** | Shoshiltirish (Urgency) | **A** (Vahima uyg'otib, o'ylab ko'rishga bermaslik) | Psixologik bosim ostida o'quvchi xato qiladi. Bunday paytda "To'xta va O'yla" (Stop & Think) qoidasi ishlaydi. |
| **Q7** | EXIF GPS Manzili | **A** (Uyingiz va maktabingiz koordinatalari sizmasligi uchun) | Smartfon kamerasi surat ichiga aniq koordinatalarni yozadi. Tarmoqqa yuklashdan oldin EXIF tozalanadi. |
| **Q8** | Katta Ekran Qoidasi (Billboard) | **A** (Maktab ekranga chiqarishdan uyaladigan narsani qo'ymaslik) | Internetga tushgan ma'lumot abadiy qoladi (raqamli iz). |
| **Q9** | Ochiq Wi-Fi va VPN | **A** (Ishonchli VPN yoqish va maxfiy ma'lumot kiritmaslik) | Ochiq Wi-Fi da xakerlar trafikingizni ushlab olishi (sniffing) mumkin. VPN tunnel shifrlaydi. |
| **Q10** | Ransomware (Tovlamachi virus) | **A** (Muhim fayllarning zaxira nusxasini / Backup saqlash) | Zaxira nusxa (fleshka/bulut) bo'lsa, xakerlarga pul to'lamasdan barcha fayllarni qayta tiklash mumkin. |

---

## 4. Uy Vazifasi (`vazifa.html`) Baholash Mezoni (10 Ball)
* **Parol Formulalari (4 ball):** 14+ belgili, 3 ta so'z va maxsus simvollardan iborat mustahkam parol tuzilgan.
* **Fishing Detektori (3 ball):** Soxta harf, shubhali domen (.xyz) va soxta va'da aniq ko'rsatilgan.
* **Troyanlardan Himoya (2 ball):** Ikki qavatli kengaytma xavfi to'g'ri tushuntirilgan.
* **Maxfiylik va Katta Ekran Qoidasi (1 ball):** GPS manzillarini oshkor qilmaslik odobi shakllangan.
