# 7–8-sinf · 11-hafta · 33-dars: GTA 2D: Cyber City
## O'qituvchi Uchun Dars O'tish Qo'llanmasi (80 daqiqalik Juftlik Dars)

**O'qituvchi:** Ismoiljon Usmonov  
**Fan:** Vibecoding / Game Dev  
**Mavzu:** GTA 2D: Cyber City — Kiber-Shahar Ochiq Dunyo O'yin Loyihasi  
**Dars turi:** Juftlik blok (Double Block — 80 daqiqa)

---

### 1. Darsning Pedagogik Maqsadi va Falsafasi
Bugungi darsda qorong'i yer osti zindonlari yoki quruq formulalar o'rniga, o'quvchilar hayrat bilan o'ynaydigan **GTA 2D ochiq kiber-shahar o'yini** noldan yig'iladi. 
O'quvchilar mustaqil ravishda:
1. WASD piyoda harakati va sichqoncha bilan 360° nishonga olish;
2. 'F' tugmasi bilan sportkarga o'tirish va asfaltdagi drift fizikasi;
3. 360° lazer blaster, o'qlar ballistikasi va orqaga tepish;
4. Qidiruv yulduzlari (⭐⭐⭐) va miltillovchi sirenali politsiya ta'qibi;
5. Kiber-kuryer yetkazib berish missiyalari va naqd pul ($$$) hisobini birlashtiradilar.

---

### 2. Dars Vaqti Taqsimoti (80 Daqiqalik Aniq Pacing)

| Bosqich | Vaqt | Faoliyat Mazmuni |
|:---:|:---:|---|
| **1-Bosqich** | 00:00–04:00 | **Titul va Darsga Kirish:** GTA 2D o'yin loyihasi konsepsiyasini e'lon qilish. |
| **2-Bosqich** | 04:00–12:00 | **Uy Vazifasi Tahlili:** 32-dars otishma kodidagi xotira oqishi (bullets memory leak) xatosi va toza filter(). |
| **3-Bosqich** | 12:00–20:00 | **Kiber-Shahar Arxitekturasi:** GTA 2D ning 5 asosiy yadrosi (Xarita, Avto, Politsiya, Qurollar, Missiyalar). |
| **4-Bosqich** | 20:00–28:00 | **Piyoda Harakati:** Math.atan2 bilan burilish va WASD vektorli siljish. |
| **5-Bosqich** | 28:00–36:00 | **Sportkar Fizikasi:** Tezlanish, inersiya (0.985) va asfaltdagi qora drift izlari. |
| **6-Bosqich** | 36:00–44:00 | **'F' Tugmasi Mantig'i:** Masofani tekshirib (Math.hypot < 50) mashinaga o'tirish / tushish. |
| **7-Bosqich** | 44:00–50:00 | **360° Qurollar:** Stvol chaqnashi, orqaga tepish va devorga urilganda uchqunlar. |
| **8-Bosqich** | 50:00–60:00 | **Jonli Test-Drayv:** Taqdimot ichidagi interaktiv GTA 2D simulyatorida poyga o'tkazish. |
| **9-Bosqich** | 60:00–66:00 | **Politsiya AI:** Qidiruv yulduzlari, miltillovchi qizil-ko'k sirena va ta'qib burchagi. |
| **10-Bosqich** | 66:00–70:00 | **Web Audio Sintezi:** Dvigatel guvillashi, shinalar g'iyqillashi va politsiya sirenasi. |
| **11-Bosqich** | 70:00–74:00 | **Vibecoding Prompt Arxitekturasi:** AI ga 4 bosqichli buyruqlar berish metodikasi. |
| **12-Bosqich** | 74:00–77:00 | **Juftlikda Playtesting:** Partadoshining o'yinini tekshirish va xatolarni topish. |
| **13-Bosqich** | 77:00–79:00 | **Xulosa va Oltin Qoidalar:** Ochiq dunyo arxitekturasining 4 ta oltin qoidasi. |
| **14-Bosqich** | 79:00–80:00 | **3 Darajali Uy Vazifasi:** 10 ballik rubrika va Pay'n'Spray neon garaj topshirig'i. |

---

### 3. Keng Tarqalgan Xatolar (Pitfalls) va Oltin Yechimlar
* **Tuzoq 1: Mashinadan tushganda bino ichiga tushib qolish:**
  * *Yechim:* O'yinchini mashinaning yon tomoniga chiqarishda devor chegarasi tekshiriladi: `checkBuildingCollide(player.x, player.y)`.
* **Tuzoq 2: Mashina burilganda joyida aylanib qolishi:**
  * *Yechim:* Mashina faqat tezlik mavjud bo'lganda burilishi kerak: `if (Math.abs(car.speed) > 0.2) { car.angle += turn; }`.
* **Tuzoq 3: Politsiyaning juda tez yetib olib o'yinni buzishi:**
  * *Yechim:* Politsiya tezligi (3.8 px) sportkar maksimal tezligidan (6.5 px) biroz sekinroq qilinadi, shunda o'yinchi drift qilib qochishi mumkin bo'ladi!
