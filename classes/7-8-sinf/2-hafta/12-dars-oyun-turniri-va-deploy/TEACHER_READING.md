# O'qituvchi uchun qo'llanma: 12-dars — O'yin Turniri va Veb-Deploy

**Kohorta:** Middle Web (7–8-sinflar)  
**Hafta / Dars:** 2-hafta / 12-dars (2-hafta yakuniy darsi / Game Jam)  
**Mavzu:** Global Deploy (Vercel, GitHub Pages), Mobil QR-kod, Playtesting va Sinf Kiber-Turniri  
**Davomiyligi:** 45 daqiqa  

---

## 1. Darsning Pedagogik Maqsadi va Falsafasi

Ushbu dars 2-haftaning kulminatsion cho'qqisi hisoblanadi. O'quvchilar HTML, CSS, JavaScript hodisalari, vaqt o'lchovi (`Date.now`), xatolarni to'g'rilash (Debugging) va doimiy xotira (`localStorage`) asosida yaratgan o'yinlarini endi **dunyo bilan baham ko'radilar**.

Darsning asosiy maqsadlari:
1. **Lokal vs Global Tushunchasi:** `http://localhost:5500` faqat o'z kompyuterida ishlaydi, do'stlari bu manzilni o'z telefonlarida ocha olmaydi.
2. **Statik Veb-Deploy:** Kodni internet serveriga joylashtirish (Vercel orqali 30 soniyada yoki GitHub Pages orqali).
3. **QR Kod Yaratish:** Har bir o'quvchi o'z o'yinining havolasini QR-kodga aylantiradi va partadoshiga ko'rsatadi.
4. **Peer Review va Game Jam Turniri:** O'quvchilar bir-birlarining o'yinlarini sinab ko'radi (Playtesting), o'zaro rekordlar o'rnatadi va halol feedback beradi.
5. **Baholash Mezonlari:** 10 ballik tizim bo'yicha loyiha sifatini himoya qilish.

---

## 2. 45 Daqiqalik Dars Taqsimoti

| Vaqt | Bosqich | O'qituvchi va O'quvchi Faoliyati |
|---|---|---|
| **00:00 – 03:00** | Kirish va G'alaba Ruhiyati | 2-hafta davomida bosib o'tilgan yo'lni e'tirof etish. "Bugun siz nafaqat o'quvchi, balki o'z o'yinini dunyoga chiqargan Game Developer hisoblanasiz". |
| **03:00 – 10:00** | Nazariya: Deploy nima? | Server, DNS domen, HTTPS (yashil qulf) va Vercel / GitHub Pages mexanizmi. |
| **10:00 – 16:00** | QR-kod va Mobil Moslashuv | Sayt havolasini QR kodga aylantirish, smartfon kamerasida ochish sirlari. |
| **16:00 – 22:00** | Turnir Nizomi va Baholash Qoidalari | Varaqadagi 4 mezon: Mexanika (3 b.), Vizual (2 b.), Barqarorlik (3 b.), Deploy & QR (2 b.). |
| **22:00 – 38:00** | Amaliy Turnir (Game Jam Arena) | O'quvchilar bir-birlarining kompyuter yoki telefonlaridagi o'yinlarini o'ynab, varaqaga ball yozishadi. |
| **38:00 – 43:00** | G'oliblarni E'lon Qilish | Sinf bo'yicha eng yuqori ball to'plagan va eng yaxshi o'yin yaratgan 3 nafar g'olibni taqdirlash. |
| **43:00 – 45:00** | 2-Hafta Yakuni va 3-Hafta Anonsi | Keyingi haftada HTML5 Canvas grafikasi, delta-time va haqiqiy 2D fizika dvijogiga o'tish anonsi! |

---

## 3. O'qituvchi Uchun Tavsiyalar

- Agar sinfdagi kompyuterlarda tashqi internetga ulanish cheklangan bo'lsa, o'yinlarni lokal tarmoqdagi IP-manzil orqali ochishni yoki o'rnatilgan demo loyihani (`game/index.html`) ko'rsatishni tavsiya eting.
- Playtesting paytida o'quvchilarga konstruktiv fikr bildirishni o'rgating: "Yomon ekan" emas, balki "Tugma juda kichik, kattaroq qilinsa bosish osonlashadi" kabi professional tavsiyalar berilsin.
