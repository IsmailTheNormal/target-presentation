# 21-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Prep Guide)
**Target International School // 5–6-Sinflar (10–12 yosh) // 7-Hafta (1-Soat: 40 daqiqa)**
**Mavzu:** Raqamli Iz (Digital Footprint) va Shaxsiy Maxfiylik: Internet Biz Haqimizda Nimani Biladi?
**Kohorta:** `5A 5B 6A 6B` (Kiber-Xavfsizlik & Raqamli Savodxonlik)

> **ASOSIY PEDAGOGIK MAQSAD:**
> Ushbu darsda 5–6-sinf o'quvchilari internetdagi shaxsiy mavjudliklarining ko'rinmas oqibatlarini chuqur anglaydilar. Ular fotosuratlar ichiga yoziladigan EXIF metama'lumotlaridagi aniq GPS koordinatalari orqali uy manzilining qanday oshkor bo'lishini ko'radilar, faol va nofaol izlarni tahlil qiladilar, ochiq profiling zaifliklarini fosh etib, shaxsiy hisoblarida 100% maxfiylik qalqonini o'rnatadilar. Dars oxirida har bir o'quvchi 10 ballik natija bilan "Kiber-Maxfiylik Qo'riqchisi" diplomini himoya qiladi.

---

## 1. Darsda Ishlatiladigan Fayllar va Vositalar

1. **Interaktiv Studiya (Target Privacy & Digital Footprint Studio):**
   * Fayl manzili: `classes/5-6-sinf/7-hafta/21-dars-raqamli-iz-va-maxfiylik/studio/index.html`
   * Internet talab qilinmaydi — to'liq lokal oflayn ishlaydi.
   * Studiya modullari:
     - **Tab 1: EXIF Fotosurat Detektori:** 3 ta real keys (Maktab, Uy, Kafe). Smartfon modeli, sana-vaqt va xaritadagi aniq GPS koordinatalarni fosh etish hamda bir klik bilan tozalash (`Strip EXIF`).
     - **Tab 2: Kiber-Iz Skanneri (Persona OSINT):** 3 ta sinfdosh profili (`@gamer_sherzod2014`, `@anora_dance`, `@cyber_guard_pro`). Bio, sharhlar va postlardagi sizib chiqqan shaxsiy ma'lumotlarni tahlil qilish.
     - **Tab 3: Maxfiylik Simulyatori (Privacy Shield):** 4 ta asosiy himoya tugmasi (Yopiq profil, GPS o'chirish, Google qidiruvini to'sish, Do'stlar filtri). Qalqon darajasi 15% dan 100% gacha ko'tariladi.
     - **Tab 4: 4 ta Detektiv Kvest (10 ballik mezon):** Avtomatik ball hisoblagich va nom yoziladigan rasmiy Chop Etiladigan Sertifikat.
2. **Prezentatsiya (12 Slayd):**
   * Fayl: `prezentatsiya.html` — Qor ustidagi izlar analogiyasi, faol vs nofaol izlar, EXIF xavfi, Wayback Machine, "Google Yourself" sinovi, 5 oltin qoida.
   * Boshqaruv: `→` keyingi, `←` oldingi, `N` o'qituvchi izohlari, `L` til, `T` tema, `H` toza ekran.
3. **Chop Etiladigan Ishchi Varaqa (2 Betlik A4):**
   * Fayl: `varaqa.html` — EXIF laboratoriya jadvallari, izlar matritsasi, profil auditi va 10 ballik rasmiy baholash rubrikasi.

---

## 2. 40 Daqiqalik Darsning Vaqt Taqsimoti

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 03:00** | Kirish va Missiya | "Bugun biz o'zimiz bilmagan holda internetda qoldirayotgan ko'rinmas izlarimizni fosh qilamiz!" deb e'lon qilish. | Daftarlarini ochishadi, yangi mavzuni belgilashadi. |
| **03:00 – 07:00** | Nazariya: Qorda Qolgan Izlar | Faol (biz qo'yadigan postlar) va nofaol (saytlar yozib oladigan IP, cookies) izlarni doskada tushuntirish. | Varaqadagi 2-kvest matritsasini to'ldirishadi. |
| **07:00 – 12:00** | EXIF Sirlari & Uy Manzili | Smartfon kamerasining yashirin GPS yozuvi qanday ishlashini ekranda jonli ko'rsatish. | Suratlar uy manzilini qanday ochib qo'yishini ko'rib hayratlanishadi. |
| **12:00 – 16:00** | Nega Internet Unutmaydi? | Skrinshotlar, Wayback Machine va Google keshining ishlash mexanizmini tushuntirish. | 1-kvestdagi tahlil savoliga javob yozishadi. |
| **16:00 – 20:00** | 5 Oltin Qoida | "Katta Ekran Qoidasi" (Billboard Rule) va GPSni o'chirish usullarini ko'rsatish. | Qasamyod bandlarini birgalikda o'qishadi. |
| **20:00 – 32:00** | Amaliy Laboratoriya (Studio) | Kompyuterlarda `studio/index.html` ni ochish, 4 ta kvestni navbatma-navbat bajarish. | EXIF ni tozalashadi, profilni skanerlashadi va qalqonni 100% ga yetkazishadi. |
| **32:00 – 36:00** | Sertifikat Himoyasi | 10 ball to'plagan o'quvchilarning diplomlarini ekranda tekshirish va tasdiqlash. | O'z ism-familiyasini yozib sertifikatni namoyish qilishadi. |
| **36:00 – 40:00** | Xulosa va Uy Vazifasi | Ota-onalar bilan birga o'z ismini "Google Yourself" qilish vazifasini berish va baholash. | Varaqalarni topshirishadi. |

---

## 3. O'qituvchi Uchun Jonli Muloqot Ssenariysi

### Darsni Boshlashdagi "Ilmoq" (Hook):
* **UZ:** "Tasavvur qiling: siz oppoq qor ustida yurib bordingiz va orqangizga qarasangiz — har bir qadamingiz muhrlanib qolgan. Internetda ham har bir klik, har bir ko'rilgan video va har bir yozilgan sharh serverlarda xuddi shunday abadiy iz qoldiradi! Bugun biz fotosuratlaringiz qanday qilib uyingiz qaysi ko'chada joylashganini begonalarga aytib berayotganini aniqlaymiz va internetdagi izlarimizni 100% xavfsiz qilishni o'rganamiz!"
* **RU:** "Представьте, что вы идёте по свежему белому снегу. Оглянитесь назад — каждый ваш шаг четко виден. В интернете каждый клик, каждый ролик и комментарий оставляет такой же вечный след на серверах! Сегодня мы узнаем, как обычная фотография выдает незнакомцам координаты вашего дома и квартиры, и научимся защищать свой профиль на 100%!"

---

## 4. Baholash Mezoni (10 Ballik Standart)

1. **EXIF Ekspertizasi (2 ball):** Tab 1 da yashirin GPS metama'lumotlarni tahlil qilish va "Strip EXIF" orqali tozalash.
2. **Faol vs Nofaol Izlar Matritsasi (2 ball):** Varaqadagi 4 ta amalni to'g'ri tasniflash.
3. **Ochiq Profil Auditi (3 ball):** Tab 2 da @gamer_sherzod2014 profilining 3 ta kritik xatosini aniqlash va tuzatish usulini yozish.
4. **Kiber-Qalqon 100% & Sertifikat (3 ball):** Tab 3 dagi 4 ta tugmani to'g'ri faollashtirish va "Privacy Guardian" diplomini qo'lga kiritish.
