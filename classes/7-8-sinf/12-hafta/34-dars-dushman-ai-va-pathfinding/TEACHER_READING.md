# 34-dars: Dushman AI va Pathfinding: To'siqlarni Aylanib Quvish (O'qituvchi Metodologiyasi)

## Darsning Pasporti
- **Sinf:** 7–8-sinf (Game Dev, Interaktiv Veb & FUT Creator Track)
- **Davomiyligi:** 40 daqiqa (Yakka Dars / Single Block)
- **Asosiy maqsad:** O'quvchilarga Canvas 2D o'yinlarida ko'r-ko'rona koordinatalarga intiluvchi sodda dushmanlar o'rniga to'siqlarni aylanib o'tuvchi fazoviy intellektga ega sun'iy intellekt (Pathfinding) yaratishni o'rgatish. 2D xaritani grafga aylantirish, BFS (Breadth-First Search) kenglik bo'yicha qidiruv, parent backtracking va o'yin qotib qolmasligi uchun 500 ms kesh optimizatsiyasini dasturlash.

---

## 40 Daqiqalik Aniq Vaqt Taqsimoti (Pacing)

| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Motivatsiya | 1 | Pac-Man va zamonaviy o'yinlardagi dushmanlar qanday qilib o'yinchini aylanib topishini tushuntirish. | Diqqat bilan tinglaydilar va dars maqsadini belgilaydilar. |
| **04:00–08:00** | 33-dars HW Tahlili | 2 | GTA 2D o'yinida dushmanlarning devorga botib, qaltirab qolishi xatosini tahlil qilish. | Blitz savolga javob beradilar, navbat FIFO mexanizmini yozadilar. |
| **08:00–14:00** | Xaritani Grafga Aylantirish | 3 | Canvas piksellarini 2D sonlar massiviga (0 yo'l, 1 devor) o'tkazish va 4 tomonlama qo'shnilarni ko'rsatish. | Graf matritsasi tuzilishini tushunadilar. |
| **14:00–20:00** | BFS Mexanikasi | 4 | FIFO navbati (queue.shift) va visited to'plami yordamida to'lqinsimon tarqalishni doskaga chizish. | Nega BFS eng qisqa yo'lni kafolatlashini anglaydilar. |
| **20:00–25:00** | Yo'lni Qayta Tiklash | 5 | O'yinchidan dushmanga qarab orqaga parent zanjiri bo'yicha qaytish va path.reverse() qilishni o'rgatish. | Yo'l tiklash kodini ko'rib chiqadilar. |
| **25:00–29:00** | Holat Mashinasi (FSM) | 6 | PATROL (sokin yurish), CHASE (quvish) va ATTACK (hujum) holatlarini tahlil qilish. | 8 katakli ko'rish radiusini o'rganadilar. |
| **29:00–33:00** | 60 FPS Optimizatsiyasi | 7 | Har kadrda BFS chaqirish o'yinni qotirib qo'yishini ko'rsatish. 500 ms lik kesh taymerini joriy etish. | O'yin optimizatsiyasi sirini yozib oladilar. |
| **33:00–37:00** | Smartboard Sinovi | 8 | Slayddagi simulyatorda devorlar chizib, BFS to'lqini qanday tarqalishini jonli ko'rsatish. | Ekranda dushman harakatini kuzatadilar. |
| **37:00–39:00** | Viktorina (Quiz) | 9 | 3 ta nazorat savoli bo'yicha tezkor blitz o'tkazish. | Faol javob beradilar va o'z bilimlarini tekshiradilar. |
| **39:00–40:00** | Xulosa va Uy Vazifasi | 10 | 10 ballik uy vazifasini tushuntirish va Inventar mavzusiga ko'prik! | Kundaliklariga vazifani yozib oladilar. |

---

## O'qituvchi Uchun Muhim Blitz Savollari
1. **"Nega BFS algoritmi doim eng qisqa yo'lni topishga kafolat beradi?"**
   - Javob: Chunki u to'lqin kabi har tomonlama teng tezlikda (avval 1 qadam, keyin 2 qadam, keyin 3 qadam) kengayadi. Nishonga birinchi yetib borgan to'lqin zanjiri eng qisqa yo'l bo'ladi.
2. **"Agar visited to'plamini qo'shishni unutib qoldirsak nima bo'ladi?"**
   - Javob: Algoritm ikkita qo'shni katak o'rtasida abadiy navbatga qo'shilib, cheksiz siklga (Infinite Loop) tushadi va brauzerni qotirib qo'yadi.

---

## 10 Ballik Baholash Rubrikasi
- **4 Ball (Baza):** 2D massivda to'siqlarni tekshirib, 4 tomonlama qo'shnilarni to'g'ri filtrlaydi.
- **4 Ball (Amaliy):** FIFO navbati bilan BFS algoritmini to'liq ishga tushirib, eng qisqa yo'lni orqaga tiklay oladi.
- **2 Ball (Challenge):** PATROL / CHASE holatlarini ajratadi va yo'lni har kadrda emas, faqat kerak paytda hisoblovchi 500 ms kesh kiritadi!
