# 27-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Prep Guide)
**Target International School // 7–8-Sinflar (12–14 yosh) // 7-Hafta (1-Soat: 40 daqiqa)**
**Mavzu:** GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi: Google Maps va Yandex Go Qanday Ishlaydi?
**Kohorta:** `7A 7B 8A 8B` (Kompyuter Algoritmlari, Graflar va Qidiruv Tizimlari)

> **ASOSIY PEDAGOGIK MAQSAD:**
> Ushbu darsda 7–8-sinf o'quvchilari har kuni foydalanadigan smartfon navigatsiyalari (Google Maps, Yandex Go) va omborxona robotlari (Amazon Kiva) millionlab ko'chalar orasidan soniyaning mingdan bir ulushida eng qisqa yo'lni qanday topishini kashf etadilar. Ular shaharni 2D kataklar matritsasiga aylantirishni, Manxetten masofasi (Taxicab distance) formulasini ($|x_1 - x_2| + |y_1 - y_2|$) qo'llashni, ko'r to'lqinli qidiruv (BFS) bilan yo'naltirilgan aqlli qidiruv (A*) farqini amalda sinaydilar. Tirbandlik ko'rsatkichi (Traffic Delay) bo'lgan vaziyatda nima uchun kompyuter uzunroq, ammo tezroq yo'lni tanlashini matematik asoslab beradilar. Dars yakunida har bir o'quvchi 10 ballik natija bilan "Junior Route Engineer" diplomini himoya qiladi.

---

## 1. Darsda Ishlatiladigan Fayllar va Vositalar

1. **Interaktiv Studiya (Target GPS Pathfinding & Route Studio):**
   * Fayl manzili: `classes/7-8-sinf/7-hafta/27-dars-gps-navigatsiya-va-eng-qisqa-yol/studio/index.html`
   * Internet talab etilmaydi — to'liq lokal oflayn ishlaydi.
   * Studiya modullari:
     - **24x14 Shahar Koordinatalar Maydoni:** Start nuqtasi (Uy - Yashil), Maqsad nuqtasi (Maktab - Qizil).
     - **Chizish Asboblari:** Bino / Devor (O'tib bo'lmaydi), Tirbandlik (Og'irlik = 4), Tozalash (Erkin yo'l = 1).
     - **Xarita Shablonlari (Presets):** Bo'sh shahar (Clean Grid), Tirband markaz (Traffic Jam Bypass), Shahar labirinti (City Maze).
     - **Algoritm Duellari:** Ko'r BFS to'lqini (barcha tomonga kengayadi) vs A* Smart Kompas (faqat maqsad tomon intiladi).
     - **Jonli Telemetriya:** Ko'rib chiqilgan kataklar soni (Explored Nodes), Yo'l uzunligi (Path Length), Umumiy sarf-xarajat (Total Cost), Samaradorlik foizi (Efficiency).
     - **Export & Sertifikat:** `route.json` konfiguratsiyasini yuklab olish, 4 ta kvest (10 ballik mezon) va chop etiladigan "Junior Route Engineer" Diplomi.
2. **Prezentatsiya (12 Slayd):**
   * Fayl: `prezentatsiya.html` — Shahar grafigi, kombinatorik portlash, BFS to'lqini, A* formulasi $F = G + H$, Manxetten masofasi, tirbandlik og'irligi, Pac-Man va Amazon robotlari.
   * Boshqaruv: `→` keyingi, `←` oldingi, `N` o'qituvchi izohlari, `L` til (UZ/RU/EN), `T` mavzu, `H` boshqaruv panelini yashirish.
3. **Chop Etiladigan Ishchi Varaqa (2 Betlik A4):**
   * Fayl: `varaqa.html` — Shahar kataklari tahlili, Manxetten masofasi hisobi masalalari, BFS vs A* taqqoslash matritsasi, Yandex Go kuryer keysi va 10 ballik baholash rubrikasi.

---

## 2. 40 Daqiqalik Darsning Slaydma-Slayd Aniq Vaqt Taqsimoti (Pacing Clock)

| Vaqt | Bosqich & Slayd | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 02:00** (2 daq) | **Slayd 1: Kirish & Reja** | "Toshkentda 10 000 dan ortiq ko'cha bor. Yandex Go qanday qilib 0.05 soniyada uyingizdan maktabgacha eng tez yo'lni topadi?" deb savol berish. | Hayron bo'lishadi, o'z taxminlarini aytishadi (sun'iy yo'ldosh, xarita, kamera). |
| **02:00 – 05:00** (3 daq) | **Slayd 2: Muammo & Portlash** | Shaharni 2D kataklar (X, Y) matritsasi deb tasavvur qilish. Nega oddiy "hamma yo'lni tekshirish" koinot yoshidan ham ko'p vaqt olishini tushuntirish. | Varaqaning 1-kvestidagi kataklar jadvalini ko'rib chiqishadi. |
| **05:00 – 08:00** (3 daq) | **Slayd 3: Adjacency List (JS)** | Xarita JavaScript ob'ektida qanday yozilishini (Tugunlar va ulangan ko'chalar masofasi) ko'rsatish. | Varaqaga tugunlar va masofalar jadvalini yozadilar. |
| **08:00 – 11:00** (3 daq) | **Slayd 4: Dijkstra Algoritmi** | To'lqinli qidiruv va ustuvor navbat (Priority Queue) orqali eng qisqa yo'lni qanday kafolatlanishini tushuntirish. | Varaqadagi Dijkstra qadamlarini kuzatadilar. |
| **11:00 – 14:00** (3 daq) | **Slayd 5: Haversine & Manxetten** | Shahar uchun Manxetten masofasi ($H = \|x_1 - x_2\| + \|y_1 - y_2\|$) formulasini doskada yechib ko'rsatish. | Varaqadagi 3 ta nuqta orasidagi Manxetten masofasini hisoblaydilar. |
| **14:00 – 16:00** (2 daq) | **Slayd 6: W3C Geolocation API** | Brauzer qanday qilib `navigator.geolocation` orqali qurilma koordinatasini olishini ko'rsatish. | Smartfon va noutbuk qanday ruxsat so'rashini tahlil qilishadi. |
| **16:00 – 19:00** (3 daq) | **Slayd 7: A* ($F = G + H$)** | A* kompas formulasi: $F$ (jami narx) = $G$ (bosib o'tilgan yo'l) + $H$ (Manxetten evristikasi) mo'jizasini ochib berish. | BFS va A* farqini tushunadilar. |
| **19:00 – 22:00** (3 daq) | **Slayd 8: Route Studio Demo** | O'qituvchi ekranda `studio/index.html` ni ochib, start/finish, devorlar va tirbandlik chizib, A* poygasini ko'rsatadi. | Studiya interfeysi bilan tanishadilar. |
| **22:00 – 25:00** (3 daq) | **Slayd 9: Kiber-Test & Fix** | Slayddagi A dan D gacha bo'lgan yo'l testini birgalikda yechish va "Fix" tugmasi orqali to'g'ri hisobni ko'rish. | Test variantini tanlab, to'g'ri javobni mustahkamlaydilar. |
| **25:00 – 36:00** (11 daq) | **Slayd 10: Mustaqil Amaliyot** | O'quvchilar kompyuterlarida `studio/index.html` ni ochib, 4 ta kvestni bajarishadi, `route.json` yuklashadi va sertifikat oladilar. | Kataklar chizishadi, A* va BFS ni poyga qildirishadi, natijalarni solishtirishadi. |
| **36:00 – 38:00** (2 daq) | **Slayd 11: Baholash Mezoni** | 10 ballik mezon bo'yicha varaqalarni tekshirish va o'z-o'zini baholash. | Varaqadagi ballarini hisoblab, yakuniy xulosa yozadilar. |
| **38:00 – 40:00** (2 daq) | **Slayd 12: Yakun & Uy Vazifasi** | Darsning asosiy xulosasi, "Junior Route Engineer" diplomlarini tasdiqlash va vazifa.html ni topshirish. | Varaqalarni topshirib, darsni yakunlaydilar. |

---

## 3. O'qituvchi Uchun Jonli Muloqot Ssenariysi

### Darsni Boshlashdagi "Ilmoq" (Hook):
* **UZ:** "Tasavvur qiling: siz maktabga kechikayapsiz. Taksi chaqirdingiz. Yandex Go ekranda bir zumda uch xil yo'lni ko'rsatadi: biri markaz orqali qisqa, ammo tiqilinch, ikkinchisi aylanma, ammo yashil. Toshkentda millionlab burilishlar bor. Kompyuter bu millionlab kombinatsiyalar ichidan eng zo'rini qanday qilib soniyaning mingdan birida topdi? U hamma yo'llarni birma-bir tekshirib chiqqanmi? Yo'q! Chunki hamma yo'lni bittalab tekshirishga kompyuterning ham umri yetmasdi. Bugun biz Google Maps va Yandex Go ning yuragi bo'lgan A* algoritmining sirini ochamiz!"
* **RU:** "Представьте: вы опаздываете на первый урок. Заказываете такси, и Яндекс Go за долю секунды рассчитывает маршрут. В Ташкенте тысячи перекрестков и миллионы возможных путей. Как программа находит самый быстрый вариант почти мгновенно? Перебирает ли она все улицы подряд? Ни в коем случае — на полный перебор ушли бы недели даже у суперкомпьютера! Сегодня мы разберем секрет алгоритма A* и узнаем, как математика помогает не стоять в пробках!"

---

## 4. O'quvchilarda Uchraydigan Savollar va Ilmiy Javoblar

1. **"Nima uchun masofani to'g'ri chiziq bilan (Evklid masofasi $\sqrt{\Delta x^2 + \Delta y^2}$) o'lchamaymiz?"**
   * *Javob:* Shahar sharoitida to'g'ri chiziq faqat qushlar yoki dronlar uchun to'g'ri keladi. Mashina va piyodalar binolarni teshib o'ta olmaydi. Nyu-Yorkdagi Manxetten oroli to'rtburchak ko'chalardan iborat bo'lgani uchun harakat faqat o'ngga-chapga yoki tepaga-pastga bo'ladi. Shu sababli Manxetten masofasi shahar uchun eng to'g'ri evristikadir.
2. **"Agar A* algoritmi shunchalik zo'r bo'lsa, BFS algoritmi nima uchun kerak?"**
   * *Javob:* Agar xaritadagi barcha yo'llarning narxi bir xil bo'lsa va bizga nishongacha masofa noma'lum bo'lsa (masalan, labirintdan chiqish eshigining qayerdaligini bilmasak), BFS eng xavfsiz va ishonchli usuldir. Shuningdek, ijtimoiy tarmoqlarda (Instagram, LinkedIn) "sizning do'stingizning do'sti" (6 qo'l orqali bog'lanish) zanjirini topishda doimo BFS ishlatiladi.
3. **"Nima uchun A* ba'zan uzoqroq yo'lni tanlaydi?"**
   * *Javob:* Chunki A* algoritmi masofani (kilometrni) emas, sarf-xarajatni (vaqtni yoki yoqilg'ini) minimallashtiradi. 5 kilometrlik qizil tirbandlikda 40 daqiqa tiqilib turgandan ko'ra, 12 kilometrlik erkin trassa orqali 12 daqiqada yetib borish har qanday inson va algoritm uchun manfaatliroqdir.

---

## 5. Baholash Mezoni (10 Ballik Standart)

1. **Shahar Matritsasi va Koordinatalar (2 ball):** Kataklar turlarini (Ochiq, Bino, Tirbandlik) va harakat narxini to'g'ri tushunish.
2. **Manxetten Formulasi (2 ball):** Varaqadagi 3 ta masofani xatosiz hisoblash: $|x_1 - x_2| + |y_1 - y_2|$.
3. **Algoritmlar Duellari (2 ball):** BFS va A* ning farqlarini (tekshirilgan kataklar, xotira sarfi, yo'naltirilganlik) yoritish.
4. **Kuryer Keysi Tahlili (2 ball):** Tirbandlik va aylanma yo'l vaqtlarini hisoblab, A* algoritmining qarorini to'g'ri asoslash.
5. **Route Studio Amaliyoti & Sertifikat (2 ball):** Studiyadagi 4 ta kvestni bajarish, `route.json` faylini eksport qilish va 10 ball bilan sertifikatni himoya qilish.
