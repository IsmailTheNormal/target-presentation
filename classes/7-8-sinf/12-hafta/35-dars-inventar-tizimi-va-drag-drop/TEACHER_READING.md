# O'qituvchi Qo'llanmasi (Teacher Reading)
## 7–8-sinf · 12-hafta · 35-dars
### Mavzu: Inventar va Buyumlar Tizimi: Drag-and-Drop, Artefaktlar va Qahramon Stats (Slotlar & RPG Inventory Engine)
**Dars formati:** Juftlik Dars (Double Block — 80 daqiqa / 2-soatlik dars)

---

### 1. Darsning Pedagogik Maqsadi va Falsafasi
7–8-sinf o'quvchilari (12–14 yosh) o'z tabiatiga ko'ra raqobatbardosh geymerlardir. Ular Minecraft, Diablo, Witcher yoki CS:GO o'yinlaridagi inventar va skinlar tizimini juda yaxshi bilishadi.
Ushbu darsning maqsadi — sevimli o'yinlaridagi inventar mexanikasini o'z qo'llari bilan HTML5 Drag-and-Drop API va JavaScript ob'ektlari orqali yaratishni o'rgatishdir.
O'quvchilar nafaqat vizual slotlarni, balki matematik stat hisob-kitoblarini (ATK/DEF stacking) va konsoldan aldashga qarshi `Object.freeze()` kiber-himoyasini o'rganadilar.

---

### 2. Darsning 80 Daqiqalik Aniq Xronometraji

#### 1-BOSQICH (40 daqiqa) — Konsept, API va Matematika
- **00:00–05:00 (5 min):** Kirish, dars mavzusi va maqsadlarini e'lon qilish.
- **05:00–13:00 (8 min):** 34-dars uy vazifasi tahlili: BFS qidiruvida visited to'plamini unutish va blitz savol.
- **13:00–19:00 (6 min):** Inventar arxitekturasi: Xalta (Backpack) vs Tana jihozlari (Equipped).
- **19:00–25:00 (6 min):** Buyumlar ma'lumot modeli (JSON): id, name, type, icon, rarity, stats.
- **25:00–31:00 (6 min):** HTML5 Drag & Drop API: `ondragstart`, `ondragover` va `ondrop`.
- **31:00–37:00 (6 min):** Slotlar validatsiyasi va tur mosligi (Qilichni boshga kiyib bo'lmaydi!).
- **37:00–40:00 (3 min):** Statlarni jamlash matematikasi (recalculateStats).

#### 2-BOSQICH (40 daqiqa) — Xavfsizlik, Laboratoriya va Yakun
- **40:00–45:00 (5 min):** Kiberxavfsizlik: F12 orqali xaltani buzish va `Object.freeze()` to'sig'i.
- **45:00–50:00 (5 min):** Interaktiv Quiz: 4 ta geymdev savoli.
- **50:00–55:00 (5 min):** LocalStorage da inventarni avtomatik saqlash.
- **55:00–68:00 (13 min):** Katta Amaliy Laboratoriya: `simulator/index.html` da RPG inventar tizimini sinash.
- **68:00–74:00 (6 min):** Juftlikda Playtest: partadoshining ritsari bilan statlar dueli va 2 nafar o'quvchining Smartboardda jonli demosi.
- **74:00–77:00 (3 min):** Set (To'plam) bonuslari haqida tushuncha.
- **77:00–80:00 (3 min):** Dars yakuni, 3 darajali uy vazifasi tushuntirilishi va baholash.

---

### 3. O'qituvchi Uchun Chuqur Texnik Savollar va Javoblar

1. **Savol:** Nega `ondragover` hodisasida `e.preventDefault()` chaqirilmasa, drop ishlamaydi?
   - **Javob:** Brauzerlar xavfsizlik sababli veb-sahifaga narsa tashlashni sukut bo'yicha (by default) taqiqlab qo'ygan. `e.preventDefault()` ushbu taqiqni bekor qilib, aynan shu slotga buyumni tashlashga ruxsat beradi.
2. **Savol:** Nega buyumlar xaltada turganda qahramonga hujum kuchini qo'shmaydi?
   - **Javob:** Bu geym-dizayn qoidasi. Xalta — faqat saqlash ombori. Faqat qahramonning tanasidagi faol slotlarga (Equipped) kiyilgan buyumlargina jangda ishlatiladi.
3. **Savol:** `Object.freeze()` qanday qilib o'yinni konsol cheatlaridan himoya qiladi?
   - **Javob:** `Object.freeze()` ob'ektning barcha maydonlarini 'read-only' (faqat o'qish uchun) qilib qo'yadi. Agar xaker F12 konsolini ochib `item.stats.atk = 99999` deb yozsa, brauzer bunga yo'l qo'ymaydi va xatoni qaytaradi.
