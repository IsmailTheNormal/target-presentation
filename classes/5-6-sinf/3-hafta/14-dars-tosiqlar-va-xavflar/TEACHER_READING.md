# 14-Dars: O'qituvchi Uchun Maxsus Qo'llanma (Teacher Prep Guide)
**Target International School // 5–6-Sinflar (10–12 yosh) // 3-Hafta (2-Soat: 40 daqiqa)**
**Mavzu:** To'siqlar Maydoni: Xavfli Tikanlar, Lazerlar, 3 Ta Jon (HP) va G'alaba Portali

> **ESLATMA:** Ushbu qo'llanma IT yoki geym-developerlik bo'yicha maxsus tayyorgarligi bo'lmagan o'qituvchi uchun yozilgan. Unda darsning har bir daqiqasi, doskada nima ko'rsatish va bolalarga rus tilida nima deyish so'zma-so'z berilgan.

---

## 1. Darsda Qaysi Dastur va AI Ishlatiladi?

1. **O'yin Darchasi (Google Chrome):**
   * Fayl: `classes/5-6-sinf/3-hafta/14-dars-tosiqlar-va-xavflar/game/index.html`
   * Bolalar ushbu faylni ochishadi. Ekranda 2D kiber-trassa chiqadi.
   * Yuqorida 3 ta qizil yurakcha (❤️❤️❤️), polda qizil tikanlar, harakatlanuvchi lazer va marrada yashil portal bor.
   * O'ng tomonda 3 ta tayyor rejim tugmasi bor: `[🟢 Легко] [🟡 Норма] [🔴 Хардкор]`.
2. **AI Darchasi (ChatGPT yoki Claude brauzerda):**
   * Sayt: `chatgpt.com` yoki `claude.ai`
   * Bolalar o'ng paneldagi tayyor prompitni nusxalab, AI ga tashlashadi. Masalan:
     > *"В игре Cyber Runner на JavaScript добавь звук сирены при столкновении с шипами и покачивание экрана (Screen Shake)"*
   * AI taklif qilgan sozlama raqamlarini slayderlar orqali tekshirishadi.

---

## 2. 40 Daqiqalik Darsning Bosqichma-Bosqich Rejasi

### 00:00 – 05:00 | Boshlash va 2-Soatga Qiziqtirish
* **Proyektorda:** `prezentatsiya.html` 1-slaydi.
* **O'qituvchi nima deydi (rus tilida):**
  > *"Ребята, отлично! В первой части урока наш герой научился бегать и прыгать. Но представьте: если бежать просто по пустой гладкой дороге — играть станет скучно уже через минуту! Чего не хватает настоящей игре? Правильно — препятствий, опасных шипов и финального портала победы! Сейчас мы превратим пустую дорогу в полосу препятствий как в настоящем Roblox Obby!"*

### 05:00 – 17:00 | Nazariya: To'qnashuv va 3 Ta Qoida
* **AABB Hitbox (3-slayd):**
  * *"Компьютер не видит глазами картинку. Герой и шип — это два невидимых прямоугольника. Если их координаты пересекаются — движок фиксирует удар!"*
* **3 ta xavf (4-slayd):**
  * Qizil tikanlar (Spikes) — polda turadi, ustidan sakrash kerak.
  * Harakatlanuvchi lazer (Moving Laser) — yuqoriga-pastga yuradi, vaqtni poylash kerak.
  * O'pqon (Void Pit) — platformalar orasidagi bo'shliq, yiqilsangiz jon ketadi!
* **i-Frames (6-slayd):**
  * Nega qahramon tikanga tekkanda oq rangda miltillaydi?
  * *"Если бы не было неуязвимости (i-Frames), персонаж на шипе потерял бы все 3 жизни за 0.05 секунды. Защита дает 1.2 секунды, чтобы отскочить в безопасное место!"*

### 17:00 – 35:00 | Amaliyot: Kiber-Trassa Sinovlari
* Bolalar noutbukda `game/index.html` ni ochishadi va qog'oz varaqani to'ldirishadi:
  1. **1-sinov (Tikan va i-Frames):** Tikanga tegib ko'rish. Qahramon orqaga otilib, miltillashini tekshirish. Varaqadagi katakka belgi qo'yish.
  2. **2-sinov (Lazer):** Lazer tepaga chiqqanda ostidan yugurib o'tish.
  3. **3-sinov (3 ta rejim):** `🟢 Легко`, `🟡 Норма`, `🔴 Хардкор` da o'tib, portalga yetgan vaqtini (sekund) varaqaga yozish.
  4. **4-sinov (Bonus):** Birorta ham yurak yo'qotmasdan (3/3 HP) yashil portalga yetib borgan o'quvchiga +2 rag'bat bali!

### 35:00 – 40:00 | Juft Dars Yakuni va 10 Ballik Baholash
* O'qituvchi o'quvchilar varaqalarini yig'ib oladi yoki stolida tekshirib ball qo'yadi:
  - Hitbox va xavflar tushunilgan: 3 ball
  - Kiber-trassa bosib o'tilgan: 3 ball
  - Shaxsiy balans topilgan va yozilgan: 4 ball
  - Talafotsiz o'tganlarga: +2 rag'bat ball!

---

## 3. Bolalar Berishi Aniq Bo'lgan Savollar va Sizning Javoblaringiz

1. **"Учитель, я нажал на шип и персонаж улетел назад!"**
   *Javob:* *"Всё верно! Это механика отдачи (Knockback). Код отталкивает героя назад, чтобы спасти его от повторного удара."*
2. **"Учитель, я упал в яму и появился в начале!"**
   *Javob:* *"Это зона пропасти (Void Pit). При падении за экран персонаж теряет 1 сердце и возвращается на чекпоинт."*
3. **"Как пройти лазер на Хардкоре? Он слишком быстрый!"**
   *Javob:* *"Подбегите вплотную, дождитесь пока луч пойдет вверх, и нажмите спринт [D]! В гейм-дизайне это называется Тайминг (Timing)."*
