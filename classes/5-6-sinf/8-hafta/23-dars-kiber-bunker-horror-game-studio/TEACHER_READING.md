# O'qituvchi Uchun Maxsus Qo'llanma: Kiber-Bunker 404 (23-dars)
**Target International School · Vibecoding 5–6-sinf · 1-Chorak Maxsus Yakuniy Missiyasi**

---

## 🎯 Darsning Asosiy Maqsadi va Falsafasi
Ushbu dars **1-chorakning eng esda qolarli, hissiyotga boy yakuniy loyihasidir**.
Bu darsda **hech qanday yangi qiyin nazariya yo'q**. Darsning bosh vazifasi:
1. 5–6-sinf o'quvchilarining eng sevimli janri (**3D Horror / Survival**) orqali **Frontend (Three.js)** va **Backend (Node.js)** farqini amalda ko'rsatish.
2. Sinfdagi **"qisman noutbuk bor, qisman yo'q"** muammosini **Asimmetrik Jamoaviy O'yin (Pilot + Dispetcher + Kriptograf)** orqali 100% yechish.

---

## 🚀 Serverni Ishga Tushirish (2 Daqiqalik Tayyorgarlik)

### 1-Usul: Haqiqiy Tarmoq Rejimi (Tavsiya etiladi)
O'qituvchining kompyuterida bitta terminal ochiladi:
```bash
cd classes/5-6-sinf/8-hafta/23-dars-kiber-bunker-horror-game-studio/server
npm start
```
Terminalda quyidagi xabar chiqadi:
```
=======================================================
🎮 KIBER-BUNKER HORROR ENGINE SERVER IS RUNNING!
📍 3D Client (Laptops):      http://localhost:3000
📡 CCTV Terminal (Phones):    http://localhost:3000/cctv
⚡ WebSocket Server:          ws://localhost:3000
=======================================================
```

**Sinfga Wi-Fi orqali ulashish:**
Terminalda `hostname -I` (yoki `ip a`) buyrug'ini yozing. Masalan: `192.168.1.45`.
Doskaga yozib qo'ying:
- **Noutbuki borlar uchun (3D Pilot):** `http://192.168.1.45:3000`
- **Telefoni/Plansheti borlar uchun (CCTV Dispetcher):** `http://192.168.1.45:3000/cctv`

### 2-Usul: Oflyayn / Mahalliy Rejim (Server kerak bo'lmasa)
Agar sinfda Wi-Fi bo'lmasa yoki server ishga tushmasa, o'quvchi shunchaki noutbukda `client/index.html` faylini brauzerda ochadi. Dvigatel avtomatik ravishda **Oflyayn Simulyatsiya** rejimiga o'tadi va Three.js to'liq ishlayveradi!

---

## 👥 Sinfdagi Rollar Taqsimoti (2–3 kishilik jamoalar)

| Rol | Qaysi qurilma? | Real vazifasi |
|---|---|---|
| **3D Pilot (Operativchi)** | 💻 Noutbuk + Naushnik | Zulmatdagi 3D bunkerni kezadi, chiroqni boshqaradi, kristallar (yadrolar)ni yig'adi. 5 metrdan uzoqni ko'ra olmaydi! |
| **CCTV Dispetcher** | 📱 Telefon / Planshet / 2-oyna | Radarda butun bunkerni ko'rib turadi. Eshiklarni ochadi, sirenani yoqadi va o'yinchiga radio xabarlarini yuboradi. |
| **Kriptograf / Muhandis** | 📝 Qog'oz dosye (`varaqa.html`) | Qog'ozdagi shifrni yechadi, eshik kodini dispetcherga aytadi, xaritada maxluq harakatini qalam bilan belgilaydi. |

---

## 🎭 Sinf Teatri va Atmosfera (O'qituvchining Katta Sirlari!)
1. **Chiroqlarni o'chiring!** Darsning 25-daqiqasida amaliy o'yin boshlanganda sinf chiroqlarini o'chiring. Pardalarni yoping. Bolalarning emotsiyasi va qiziqishi 10 barobar oshadi!
2. **Katta ekranga (Proyektorga) CCTV Terminalini qo'ying!** O'qituvchi kompyuteridagi proyektorda `http://localhost:3000/cctv` radari yonib tursin. Butun sinf har bir jamoaning jonli radardagi qochishini ko'rib, hayajon bilan muxlislik qiladi!
3. **Naushnik taqing:** 3D Pilot qulog'iga naushnik taqsa, Web Audio API orqali maxluq yaqinlashganda yurak urishini (`60 -> 175 BPM`) eshitib, haqiqiy kiber-dunyoni his qiladi.

---

## 🔑 Shifrlar va Kalitlar (O'qituvchi uchun javoblar)

### Varaqadagi 1-sahifa shifrlari:
- **Shifr qoidasi:** `A=1, B=2, C=4, D=5, E=7, F=8, R=3, Y=0, O=9`
- **Eshik A kodi (C-R-Y-O):** `4 - 3 - 0 - 9`
- **Eshik B kodi (F-A-C-E):** `8 - 1 - 4 - 7`

### O'yindagi g'alaba sharti:
1. Eshik A ni ochib, Krio-Lab ichidagi 1-yadroni olish.
2. Eshik B ni ochib, Reaktor ichidagi 2-yadroni olish.
3. Server Omboriga kirib, 3-yadroni olish.
4. Barcha 3 ta yadro yig'ilgach, tepada `SURFACE EXIT` eshigi avtomatik ochiladi. O'yinchi `Z < -19` ga yugurib chiqishi bilan g'alaba ekrani porlaydi!

---

## 📊 10 Ballik Baholash Mezonlari
- **3 Ball — Shifr va Xarita:** Varaqadagi `F-A-C-E` kodi (8147) to'g'ri yechilgan va sektorlar belgilangan.
- **3 Ball — Jamoaviy Radio Aloqa:** Dispetcher va Pilot xotirjam va aniq muloqot qilgan (sarosimasiz).
- **2 Ball — Tizim Arxitekturasi:** Frontend (Three.js) va Backend (Node.js) farqi to'g'ri aytilgan.
- **2 Ball — Omon Qolish Natijasi:** Bunkerdan 3 ta yadro bilan muvaffaqiyatli qochilgan yoki voqealar hisoboti to'ldirilgan.
