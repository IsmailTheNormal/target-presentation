# O'qituvchi Uchun Dars Qo'llanmasi (Teacher Reading Guide)

**Sinf:** 7–8-sinf · **Hafta:** 11-hafta · **Dars:** 33-dars  
**Mavzu:** Dushman AI va Pathfinding: A* (A-Star) va BFS To'siqlarni Aylanib Quvish Algoritmi  
**Format:** 80 daqiqalik Juftlik Dars (Double Block)  
**Uslub:** Vibecoding — AI bilan interaktiv graf algoritmlari, prompt muhandisligi va vizual pathfinding.

---

## 1. 80 Daqiqalik Darsning Daqiqama-Daqiqa Pacing Rejasi

### 1-Bosqich: Uy Vazifasi Tahlili va Nazariy Poydevor (40 daqiqa)
* **00:00–04:00 (Kirish):** Dars mavzusi va maqsadini e'lon qilish. O'quvchilarga o'tgan darsdagi o'q otish modulidan so'ng, endi labirint dushmanlarini haqiqiy xavfli yirtqichga aylantirishimizni aytish.
* **04:00–12:00 (Uy Vazifasi Tahlili):** 
  - 32-darsdagi splice teskari sikli xatosini tahlil qilish.
  - 30 soniyalik blits savol: tosh devor turganda dushman nega qotib qoladi?
* **12:00–24:00 (Sodda Ta'qib vs Grid Matritsasi):**
  - Nega `enemy.x += dx` to'g'ri chiziqli harakat devor oldida abadiy tiqilib qolishini doskada chizib ko'rsating.
  - Canvas ni 20x13 lik kataklarga bo'lish: 0 - pol, 1 - tosh devor.
* **24:00–35:00 (BFS va A* Evristikasi):**
  - BFS (Breadth-First Search) qanday qilib Queue (navbat) orqali to'lqinsimon tarqalishini tushuntiring.
  - A* ning sehri: $f(n) = g(n) + h(n)$ formulasida $h(n)$ (Manhattan masofasi) orqali qidiruvni faqat qahramon tomonga yo'naltirish.
* **35:00–40:00 (Dushman Holatlari — FSM va Sight Cone):**
  - PATROL ➔ ALERT ('?' belgisi) ➔ CHASE (1.8x A* ta'qib) zanjiri.

### 2-Bosqich: Amaliyot, Kiber-Duel va Baholash (40 daqiqa)
* **40:00–48:00 (Smartboard Jonli Simulyatori):** Doskada devorlar chizib, A* va BFS qidiruvini solishtirish.
* **48:00–55:00 (Kiber-Viktorina):** 3 ta nazorat savoli bo'yicha tezkor musobaqa.
* **55:00–70:00 (Vibecoding Amaliy Arenasi — 15 daqiqa):**
  - O'quvchilar AI ga 4 ta promptni bosqichma-bosqich berishadi:
    1. Devorga tiqilish xatosini tahlil qilish.
    2. Grid va BFS funksiyasini yozdirish.
    3. Manhattan evristikali A* optimallashtirish promptini yuborish.
    4. Ko'rish nuri (Sight Cone) va '!' ogohlantirish belgisini qo'shish.
* **70:00–74:00 (Partadosh Auditi):** Partadoshlar o'rin almashib, 4 ta mezon bo'yicha bir-birining dushman AI sini sinashadi.
* **74:00–77:00 (Katta Ekran Showcasi):** Eng yaxshi dushman xulq-atvorini katta doskada ko'rsatish.
* **77:00–80:00 (Xulosa va Vazifa):** 10 ballik rubrika va keyingi darsga (Inventar va Buyumlar tizimi) ko'prik.

---

## 2. O'qituvchi Uchun Savol-Javob va Baholash Kaliti
* **Savol 1:** Nega BFS eng qisqa yo'lni topadi?  
  *Javob:* Chunki u qadamlarni bir tekis to'lqin qilib kengaytiradi va maqsadga birinchi yetib borgan qadam eng kam qadamli yo'l bo'ladi.
* **Savol 2:** A* nega BFS dan 5-10 barobar tezroq ishlaydi?  
  *Javob:* Chunki A* Manhattan masofasi orqali orqa va chetdagi keraksiz kataklarni tekshirmaydi, faqat maqsad tomon kataklarni ochadi.
* **Savol 3:** Manhattan masofasi qanday hisoblanadi?  
  *Javob:* `|x1 - x2| + |y1 - y2|` (gorizontal va vertikal delta qadamlar yig'indisi).
