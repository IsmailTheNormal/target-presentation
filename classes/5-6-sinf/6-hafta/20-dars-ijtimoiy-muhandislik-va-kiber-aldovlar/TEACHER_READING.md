# 20-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Prep Guide)
**Target International School // 5–6-Sinflar (10–12 yosh) // 6-Hafta (1-Soat: 40 daqiqa)**
**Mavzu:** O'z Kiber-Detektor Web-Ilovangni Qur: "Cyber Shield" Loyihasi
**Kohorta:** `5A 5B 6A 6B` (Kiber-Xavfsizlik & Vibe Coding)

> **ASOSIY PEDAGOGIK MAQSAD:**
> Ushbu darsda o'quvchilar shunchaki tayyor dasturni tomosha qilmaydi. Ular o'zlarining shaxsiy **"Cyber Shield: Scam Detector"** veb-ilovasini (HTML + CSS + JavaScript) o'z qo'llari bilan yaratadilar. Dars oxirida har bir bolaning kompyuterida o'zi yaratgan, ishlaydigan `index.html` fayli paydo bo'ladi!

---

## 1. Darsda Ishlatiladigan Fayllar va Vositalar

1. **O'quvchilar Qiradigan Veb-Ilova (Starter & Reference App):**
   * Fayl manzili: `classes/5-6-sinf/6-hafta/20-dars-ijtimoiy-muhandislik-va-kiber-aldovlar/app/index.html`
   * Internet talab qilinmaydi — to'liq oflayn ishlaydi.
   * Ilova imkoniyatlari:
     - HTML matn maydoni (`<textarea>`) va Skaner qilish tugmasi (`<button>`).
     - CSS kiber-temasi: qorong'i kosmik fon (`#07152B`), neon tugma, yashil va qizil qalqon animatsiyalari.
     - JavaScript miyasi: `includes()` orqali matndagi xavfli so'zlarni (`"tekin"`, `"robux"`, `"parol"`, `"sms"`, `"5 daqiqa"`) topish.
     - Xavf topilsa: Qizil qalqon va sirena (`🚨 DIQQAT! KIBER-XAVF!`).
     - Toza bo'lsa: Yashil qalqon (`✅ XABAR XAVFSIZ`).
     - Shaxsiy kastomizatsiya: O'z sevimli o'yinlari (Roblox, Brawl Stars) so'zlarini massivga qo'shish imkoniyati.
2. **Prezentatsiya (12 Slayd):**
   * Fayl: `prezentatsiya.html` — Veb-arxitektura, bosqichma-bosqich konstruktor (HTML -> CSS -> JS) va detektivlar sinov jangi.
   * Boshqaruv: `->` keyingi slayd, `<-` oldingi slayd, `N` o'qituvchi izohlari, `L` til, `T` tema.
3. **Chop Etiladigan Varaqa (2 Betlik A4):**
   * Fayl: `varaqa.html` — Veb-arxitektor loyiha chizmasi, interfeys eskizi, shaxsiy so'zlar bazasi va o'zaro test bayonnomasi.

---

## 2. 40 Daqiqalik Darsning Vaqt Taqsimoti

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 03:00** | Kirish va Missiya | "Bugun biz foydalanuvchi emasmiz, kiber-muhandismiz! O'z dasturimizni quramiz" deb e'lon qilish. | Daftarlarini ochishadi, bugungi missiyaga qiziqish uyg'onadi. |
| **03:00 – 06:00** | Jonli Mahsulot Demosi | Tayyor `app/index.html` ilovasini proyektorda ko'rsatish: aldov xabarini tashlab, skaner tugmasini bosish. | Ekranda qizil sirena va yashil qalqon qanday ishlashini ko'rib zavqlanishadi. |
| **06:00 – 12:00** | Vebning 3 Ustuni & Mantiq | HTML (skelet), CSS (dizayn), JavaScript (aql) va `includes()` usulini tushuntirish. | Varaqadagi 1-vazifani to'ldirishadi (eskiz chizishadi). |
| **12:00 – 18:00** | 1-Qurilish: HTML Skelet | Doskada HTML teglarini ko'rsatish (`textarea`, `button`, `div#result`). | O'z kompyuterlarida `index.html` ochib, sahifa skeletini yozishadi. |
| **18:00 – 23:00** | 2-Qurilish: CSS Kiber-Uslub | Qorong'i fon, neon hoshiya va kartalar dizaynini kiritish. | O'z saytlariga yoqqan ranglarini berishadi. |
| **23:00 – 30:00** | 3-Qurilish: JavaScript Aqli | `scanMessage()` funksiyasini yozish va `DANGEROUS_WORDS` massivini ulash. | Kodni yozib, birinchi xabarni tekshirib ko'rishadi. |
| **30:00 – 35:00** | Detektivlar Jangi (Playtest) | Partadoshlar joy almashib, bir-birining detektorini hiylakor xabar bilan aldashga urinadi. | O'zaro test o'tkazishadi, yangi so'zlarni kodga qo'shishadi. |
| **35:00 – 40:00** | Xulosa va 10 Ballik Baholash | 10 ballik mezon bo'yicha varaqalarni baholash va keyingi 21-darsga ko'prik. | Loyihalarini saqlab, varaqani topshirishadi. |

---

## 3. O'qituvchi Uchun Jonli Dialog Ssenariysi

### Darsni Boshlash:
* **UZ:** "Bolalar, kim o'zining shaxsiy dasturiga ega bo'lishni xohlaydi? Bugun biz shunchaki boshqalar yaratgan o'yinni o'ynamaymiz. Bugun har biringiz kiber-muhandisga aylanasiz va firibgarlarni fosh qiluvchi **Cyber Shield** nomli shaxsiy veb-saytingizni qurasiz! 40 daqiqadan so'ng bu sayt sizning kompyuteringizda ishga tushadi!"
* **RU:** "Ребята, кто хочет иметь собственную программу? Сегодня мы не просто пользователи. Каждый из вас станет кибер-инженером и напишет собственное веб-приложение **Cyber Shield**, которое ловит мошенников в Roblox и Telegram! Через 40 минут это приложение будет работать на ваших экранах!"

---

## 4. Baholash Mezoni (10 Ballik Standart Rubrika)

1. **Sayt Skeleti (HTML — 3 ball):** To'g'ri ochilgan teglar, sarlavha, matn maydoni, tugma va natija bloki.
2. **Dastur Mantiqi (JavaScript — 4 ball):** `includes()` orqali so'zlarni qidirish va xavf signallarini to'g'ri chiqarish.
3. **So'zlar Bazasi & CSS (2 ball):** O'z sevimli o'yinlaridan kamida 3 ta yangi xavfli so'z qo'shish va kiber-uslub berish.
4. **O'zaro Sinov (Playtest — 1 ball):** Partadoshi bilan dasturni sinab ko'rish va kamchiliklarni tuzatish.
