# 29-Dars: O'qituvchi Uchun Metodik Qo'llanma va Yechimlar Kaliti
**Target International School // 7–8-Sinf // 10-Hafta (2-Chorak 1-Darsi: 40 daqiqa)**
**Mavzu:** Matritsalar va Xaritalar (Tilemaps): 2D Labirint va Platformalar
**Kohorta:** `7-8-sinf` (Game Dev, Interactive Web & Physics Track)

---

## 1. Asosiy Pedagogik Maqsad
Bugungi dars bilan 7–8-sinflar **2-Chorak: Roguelike O'yin Dvigateli** katta amaliy modulini boshlaydilar:
1. **2D Massivlar:** Xarita geometriyasini raqamli matritsa ko'rinishida saqlash (0 = yo'l, 1 = devor, 2 = tanga, 3 = portal).
2. **Ichma-ich Sikllar:** `for(row)` va `for(col)` orqali butun xaritani Canvas-ga $O(N)$ tezlikda chizish.
3. **Piksellarni Indeksga Aylantirish:** `Math.floor(x / TILE_SIZE)` formulasi yordamida o'yinchi turgan katakni aniqlash.
4. **O(1) To'qnashuv Qalqoni:** Barcha devorlarni aylanib chiqmasdan, faqatgina borilayotgan bitta katakni `map[nextRow][nextCol] === 1` orqali tekshirish.

---

## 2. 40 Daqiqalik Dars Reglamenti

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 03:00** | Kirish & 2-Chorak Rejasi | 2-Chorakda to'liq Roguelike o'yini yaratilishini e'lon qilish. | Noutbuklarni ochish, dars mavzusini qayd etish. |
| **03:00 – 08:00** | Aqliy Hujum (Xotira va RAM) | Nega 400 MB rasm o'rniga 2 KB massiv ishlatilishini savol-javob qilish. | O'z fikrlarini bildirish, farqlarni aniqlash. |
| **08:00 – 18:00** | Nazariya va Arxitektura | 12 slaydli prezentatsiyani namoyish etish, ichma-ich sikl va O(1) to'qnashuvni tushuntirish. | Bloklar va formulalarni daftarga qayd qilish. |
| **18:00 – 23:00** | Jonli Kiber-Test (Quiz & Fix) | Slayd 9 dagi matematik formulani sinf bilan hisoblash. | Hisob-kitob qilish, to'g'ri variantni tanlash. |
| **23:00 – 36:00** | Amaliy Dvigatel Laboratoriyasi | O'quvchilar shaxsiy 10x10 massiv labirintini tuzadilar va WASD bilan o'yinchini yurgizadilar. | Kod yozish, labirintdan chiqish, tangalarni yig'ish. |
| **36:00 – 40:00** | Xulosa & Baholash | 10 ballik mezon asosida eng yaxshi labirintlarga baho qo'yish, `vazifa.html` ni berish. | Ishlarni ko'rsatish, vazifani saqlab olish. |

---

## 3. Viktorina va Topshiriqlar Yechimi (Teacher Fixes)

### Viktorina (Slayd 9):
* **Savol:** Qaysi formula o'yinchi piksellarini matritsa indekslariga aylantiradi?
* **To'g'ri javob:** **B) col = Math.floor(player.x / 32), row = Math.floor(player.y / 32)**
* **Izoh:** 75 / 32 = 2.34 -> yaxlitlasak 2 (col=2). 100 / 32 = 3.12 -> yaxlitlasak 3 (row=3).

### Uy Vazifasi Yechimlari:
1. **Piksellar hisobi:** x=210 uchun col=Math.floor(210/32)=6. y=145 uchun row=Math.floor(145/32)=4. Katak: `map[4][6]`.
2. **O(1) vs O(N):** AABB 2000 ta devorni for tsiklida aylanib chiqadi (og'ir). Tilemap to'g'ridan-to'g'ri katak manziliga murojaat qiladi (bitta amal).
3. **Chegaralar himoyasi:** `row < 0 || row >= map.length || col < 0 || col >= map[0].length` shartlari qo'yiladi.
4. **Devor buzilishi:** `map[row][col] = 0;` qilib yangilanadi va keyingi kadrda devor yo'qoladi.

---

## 4. Baholash Mezoni (10 Ball)
* **3 Ball:** 10x10 lik 2D massiv sintaksis xatosiz e'lon qilingan.
* **3 Ball:** Ichma-ich `for` sikllari orqali Canvas-da barcha tayllar to'g'ri chizilgan.
* **2 Ball:** Panjara to'qnashuvi (`map[nextRow][nextCol] !== 1`) qahramonni devorga urilishdan saqlaydi.
* **2 Ball:** Oltin tangalar yig'ilganda `map[row][col] = 0` bo'lib yangilanadi va ball qo'shiladi.
