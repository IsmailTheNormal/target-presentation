# 25-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Briefing)

**Kohorta:** 7–8-Sinf · Game Dev & Interactive Web  
**Mavzu:** Penalty Shootout & Goalkeeper AI — Penaltilar Seriyasi, To'p Traektoriyasi va Adaptiv Darvozabon AI  
**Ajratilgan vaqt:** 45 daqiqa  
**Amaliy natija:** Brauzerda ishlovchi interaktiv Penaltilar dueli, 3D LERP to'p fizikasi, odatlarni eslab qoluvchi sun'iy intellekt va 5 raundlik yakuniy hisobot.

---

## 1. 5 Daqiqalik Darsoldi Konspekti (O'qituvchiga Eslatma)

O'quvchilar 21–24-darslarda o'yinchi kartochkalarini yaratishdi, taktik tarkib tuzishdi, o'yin natijasini simulyatsiya qilishdi va transfer bozorida savdolashishdi.
Bugungi dars — 5-hafta futbol modulining eng hayajonli yakuniy cho'qqisi: **90 daqiqalik durangdan so'ng g'olibni aniqlab beruvchi Penaltilar Seriyasi (Shootout)**.

### Darsning 3 ta asosiy tayanchi:
1. **Darvoza koordinatalari (3x3 matritsa):** Darvoza to'ri 9 ta zonaga bo'linadi (Top-Left dan Low-Right gacha). Har bir zona markazga nisbatan ofsetga ega.
2. **LERP fizikasi va 3D masshtab:** To'p 11 metrlik nuqtadan to'rga uchganda uning o'lchami `scale(1.0)` dan `scale(0.45)` ga qisqaradi — bu o'yinda haqiqiy 3D chuqurlik illyuziyasini beradi.
3. **Adaptiv AI (Mashinali o'rganishning sodda asosi):** Darvozabon shunchaki `Math.random()` bilan sakramaydi. U o'quvchining oldingi barcha zarbalarini eslab qoladi va eng ko'p tepilgan burchakka sakrash ehtimolini **Laplas formulasi** ($P = \frac{N+1}{\text{Jami}+9}$) orqali dinamik oshirib boradi.

---

## 2. 45 Daqiqalik Dars Vaqt Xaritasi

| Vaqt | Bosqich | O'qituvchi amali | O'quvchi harakati |
|---|---|---|---|
| **00–05 daq** | Kirish & Kontekst | Katta ekranda `game/index.html` ni ochib, 1 ta zarba ko'rsatish | O'yin mexanikasiga qiziqish, muammoni anglash |
| **05–15 daq** | Nazariya & Fizika | 1–5 slaydlarni tushuntirish: LERP formulasi va 9 zonali darvoza | Daftarga LERP formulasini yozib olish |
| **15–23 daq** | AI Matematikasi | 6–9 slaydlar: Nega tasodifiy AI yomon? Laplas formulasi va Web Audio | Varaqaning 1-betidagi hisob-kitobni bajarish |
| **23–27 daq** | Kod Auditi & Test | 10-slayddagi `aiChoice == targetZone` xatosini fosh etish | Kod xatosini topib, varaqaga tuzatish kiritish |
| **27–40 daq** | Jonli Penaltilar Seriyasi | O'quvchilar kompyuterida studiyani ishga tushirish | 5 raundlik duel o'ynab, varaqadagi protokolni to'ldirish |
| **40–45 daq** | Xulosa & Baholash | Chempion bo'lgan o'quvchilarni taqdirlash, 10 ballik baholash | Varaqani tekshirishga topshirish |

---

## 3. O'quvchilar Yo'l Qo'yadigan 3 Ta Odatiy Xato va Ularning Yechimi

### 1-Xato: Bir burchakka ketma-ket tepib, darvozabon qaytarganiga hayron bo'lish
* **Sababi:** O'quvchi darvozabonning xotirasi (Adaptive Memory) borligini unutadi. Agar 3 marta o'ng pastga tepsa, AI o'sha burchakka sakrash ehtimolini 11% dan 33% ga oshirib olgan bo'ladi.
* **Yechim:** O'quvchiga: *"AI sizning odatingizni o'qib oldi! Endi uni aldang: o'ngga qaratib, so'nggi daqiqada chap yuqoriga teping"* deb tushuntiring.

### 2-Xato: Kodda taqqoslash (`==`) bilan o'zlashtirishni (`=`) adashtirish
* **Sababi:** Diagnostik testdagi `aiChoice == targetZone` qatori qiymatni o'zgartirmaydi, natijada darvozabon doim faqat markazda qotib qoladi.
* **Yechim:** Doskaga yozing: `==` bu savol beradi ("tengmi?"), `=` esa harakat qiladi ("qiymatni yukla!").

### 3-Xato: To'p uchishida 3D masshtabni hisobga olmaslik
* **Sababi:** Agar `scale(0.45)` qo'llanilmasa, to'p darvoza to'rida ham o'yinchining oldidagi kabi ulkan ko'rinib qoladi va vizual realizm yo'qoladi.
* **Yechim:** LERP dagi `scale: lerp(1.0, 0.45, t)` formulasining ahamiyatini ko'rsating.

---

## 4. Baholash Mezoni (10 Ballik Standart)

- **1–4 Ball (Baza):** O'yin maydoni ochiladi, to'p va darvoza ko'rinadi, burchakni bosganda to'p harakatga keladi.
- **5–7 Ball (Standart):** To'p silliq LERP bo'yicha uchadi va masshtabi kichrayadi, darvozabon burilib sakraydi, 1-betdagi hisob-kitoblar to'g'ri bajarilgan.
- **8–10 Ball (Senior):** Darvozabon AI o'quvchining zarbalari bo'yicha moslashadi (telemetriya logi ishlaydi), Web Audio ovozlari yangraydi, 5 raundlik duel yakunlanib, varaqadagi test protokoli 100% to'ldirilgan.
