# O'qituvchi Qo'llanmasi: 30-Dars — Kamera, Viewport va Fog of War

**Fan:** Vibecoding / Game Dev & Interaktiv Veb (7–8-sinf)  
**Davomiyligi:** 80 daqiqa (Juftlik blok / Double Block)  
**Sana/Vaqt:** Payshanba, 7–8-slotlar (14:15–15:40)  
**O'qituvchi:** Ismoiljon Usmonov  

---

## 1. Darsning Pedagogik Maqsadi va Dolzarbligi

Ushbu dars 29-darsda yaratilgan 2D matritsali xaritalarga dinamika va chuqur o'yin atmosferasini beradi. 
O'quvchilar:
1. World Space va Screen Space o'rtasidagi farqni tushunadilar.
2. Butun dunyoni `ctx.translate(-camera.x, -camera.y)` orqali surishni o'rganadilar.
3. Clamping yordamida kamerani xarita chegarasida qulflashni o'zlashtiradilar.
4. Canvasda `createRadialGradient` va `globalCompositeOperation = 'destination-out'` orqali professional Roguelike urush tumanini quradilar.

---

## 2. 80 Daqiqalik Aniq Vaqt Taqsimoti (Pacing Plan)

### 1-Bosqich (00:00 – 40:00): Nazariya, Xatolar Tahlili va Jonli Simulyator
* **00:00 – 04:00 (4 min):** Titul va dars maqsadlarini belgilash (Slayd 1).
* **04:00 – 10:00 (6 min):** 29-dars Uy vazifasi tahlili: `map[x][y]` vs `map[row][col]` xatosi. Blitz savol va kameraga ko'prik (Slayd 2).
* **10:00 – 18:00 (8 min):** World Coordinates vs Screen Coordinates. Nega har bir obyektni qayta hisoblamasdan `ctx.translate` ishlatilishi tushuntiriladi (Slayd 3).
* **18:00 – 26:00 (8 min):** Kamera markazlashtirish va `Math.max/Math.min` Clamping chegaralari (Slayd 4).
* **26:00 – 36:00 (10 min):** Doskada interaktiv simulyator orqali o'yinchini harakatlantirish, kamera qulfini o'chirish/yoqish va mash'ala nurini sinash (Slayd 5).
* **36:00 – 40:00 (4 min):** Silliq harakat (Lerp) va qaltiramaydigan kamera formulasi (Slayd 6).

### 2-Bosqich (40:00 – 80:00): Tuman Texnologiyasi, 25-Minutlik Kiber-Arena va Xulosa
* **40:00 – 48:00 (8 min):** Fog of War nima: 3 ta qatlam (Unexplored, Explored, Visible) (Slayd 7-8).
* **48:00 – 54:00 (6 min):** `destination-out` kompozit operatsiyasi va `explored[r][c]` matritsa xotirasi (Slayd 9-10).
* **54:00 – 74:00 (20 min):** Katta Kiber-Arena laboratoriyasi: O'quvchilar `simulator/index.html` da mustaqil dungeonga kamera va mash'ala qo'shadilar (Slayd 11).
* **74:00 – 77:00 (3 min):** Interaktiv Quiz: 3 ta savol bo'yicha tezkor blitz (Slayd 12).
* **77:00 – 80:00 (3 min):** 3 darajali uy vazifasi tushuntiriladi va 11-haftaga ko'prik tashlanadi (Slayd 13-14).

---

## 3. O'qituvchi Uchun Jonli Savollar va Tuzoqlar

1. **Kamerani surishda manfiy ishora:**
   * Nega `ctx.translate(camera.x, camera.y)` emas, balki `ctx.translate(-camera.x, -camera.y)`?
   * *Yechim:* O'yinchi o'ngga yursa, dunyo chapga surilishi kerak! Kamera musbat bo'lsa, fon manfiyga qarab siljiydi.
2. **Kamera clamping tartibi:**
   * `Math.max(0, Math.min(targetX, maxCamX))` ifodasida `Math.max` va `Math.min` ning vazifasi:
   * `Math.min(targetX, maxCamX)` — o'ng/pastki chegaradan chiqib ketmaslik.
   * `Math.max(0, ...)` — chap/yuqori chegaradan (0 dan kichik bo'lib ketmaslik).
3. **destination-out da reset qilishni unutish:**
   * Agar mash'alani o'yib bo'lgach `ctx.globalCompositeOperation = 'source-over'` qilinmasa, keyingi barcha chiziladigan narsalar o'chib ketadi!

---

## 4. 10 Ballik Baholash Rubrikasi

* **1-Daraja: Baza (4 ball):** Kamera qahramon ortidan yurishi va xarita chegarasida to'xtashi (`Clamping`).
* **2-Daraja: Muhandislik (4 ball):** `createRadialGradient` bilan mash'ala nuri va qorong'ilik pardasi o'yilishi (`destination-out`).
* **3-Daraja: Kiber-Chaqliriq (2 ball):** Yurib o'tilgan yo'llarning xotirada saqlanishi (`explored[row][col]`).
