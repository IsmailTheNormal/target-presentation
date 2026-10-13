# 26-Dars: O'qituvchi Uchun Tayyorgarlik Qo'llanmasi (Teacher Prep Guide)
**Target International School // 9-Sinf (Junior Vibecoder) // 6-Hafta (1-Soat: 40–45 daqiqa)**
**Mavzu:** Ilg'or Backend Muhandisligi: MVC Arxitekturasi, Relyatsion SQLite va REST API
**Kohorta:** `9A 9B` (Junior Vibecoders & AI Web Developers)

> **METODIK ASOS (MUHIM):**
> 4-haftada o'quvchilar barcha kodni bitta `server.js` fayliga yozishgan edi (monolit). Katta loyihalarda bu tartibsizlikka (Spaghetti Code) olib keladi.
> Bugungi darsning asosiy maqsadi — **kodni professional MVC (Model-View-Controller) qatlamlariga ajratish** va **SQLite relyatsion ma'lumotlar bazasida 1-to-Many bog'lanishlarni (Foreign Keys)** mustaqil qurish.
> Dars yakunida har bir o'quvchi o'z kompyuterida ishlovchi haqiqiy REST API va interaktiv Web Dashboardga ega bo'ladi!

---

## 1. Darsda Ishlatiladigan Vositalar

1. **Interaktiv Laboratoriya (MVC & SQLite Studio):**
   * Fayl manzili: `classes/9-sinf/6-hafta/26-dars-mvc-backend-va-relyatsion-baza/studio/index.html`
   * Internet talab qilinmaydi — brauzerda to'liq oflayn ishlaydi.
   * Studio imkoniyatlari:
     - Real-vaqtli MVC so'rov oqimi animatsiyasi (Client ➔ Router ➔ Controller ➔ Model ➔ SQLite).
     - Relyatsion jadvallar inspektori (`users`, `products`, `orders`) va Foreign Key (`orders.user_id ➔ users.id`).
     - Jonli SQL JOIN ijro etuvchi mexanizm (`GET /api/orders/details`).
     - REST API konsoli (GET, POST, DELETE so'rovlarini yuborish, status kodlar: `200`, `201`, `400 Bad Request`).
     - 4 ta amaliy kvest va 10 ballik tekshiruv bo'yicha **Junior MVC Backend Architect Sertifikati**.
2. **Prezentatsiya (12 Slayd):**
   * Fayl: `prezentatsiya.html` — Slaydlar, arxitektura diagrammalari, jonli kod bloklari va `NOTES` (o'qituvchi izohlari: UZ, RU, EN).
3. **Chop Etiladigan Varaqa (2 Betlik A4):**
   * Fayl: `varaqa.html` — Relyatsion ERD sxemasi, MVC qatlamlar tahlili, SQL JOIN topshiriqlari va 10 ballik rasmiy baholash mezoni.
4. **Haqiqiy Node.js Backend Kodlari:**
   * Papka: `backend/` (`server.js`, `models/`, `controllers/`, `routes/`, `package.json`).

---

## 2. O'qituvchi Uchun Texnik Mazmun (Chuqur Tushunchalar)

### A. Nega Aynan MVC (Model-View-Controller)?
1. **Model (Baza Qatlami):** Faqat ma'lumotlar bilan ishlaydi. SQL so'rovlar, jadvallar sxemasi va ma'lumotlar yaxlitligi (Integrity constraints). Model HTTP so'rovlar haqida hech narsa bilmaydi!
2. **View (Taqdimot Qatlami):** Foydalanuvchiga ko'rinadigan qism. Bizning holatda bu veb-dashboard yoki mijozga qaytariladigan toza JSON formati.
3. **Controller (Biznes Mantig'i):** Boshqaruvchi markaz. HTTP so'rovni qabul qiladi, ma'lumotlarni tekshiradi (Validation: miqdor musbatmi, foydalanuvchi mavjudmi?), Modelga murojaat qiladi va tegishli HTTP status kodi (`200 OK`, `201 Created`, `400 Bad Request`) bilan javob qaytaradi.

### B. Relyatsion Baza va Foreign Keys (Tashqi Kalitlar)
* `users` jadvali: Har bir xaridorning yagona `id` si (Primary Key) bor.
* `products` jadvali: Har bir tovarning yagona `id` si bor.
* `orders` jadvali: Har bir buyurtma xaridor va tovarni bog'laydi:
  ```sql
  CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    total_price INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
  );
  ```
* **SQL JOIN sehri:** Xaridor nomini va u sotib olgan mahsulot nomini bitta so'rovda olish:
  ```sql
  SELECT orders.id, users.name, products.title, orders.quantity, orders.total_price
  FROM orders
  INNER JOIN users ON orders.user_id = users.id
  INNER JOIN products ON orders.product_id = products.id;
  ```

---

## 3. 40 Daqiqalik Darsning Bosqichma-Bosqich Rejasi

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 03:00** | Kirish va Muammo | "Barcha kodni bitta server.js fayliga yozsak nima bo'ladi? 10,000 qatorli chalkashlik!" deb savol tashlash. | O'tgan darslardagi tajribalarini eslashadi, arxitekturaning muhimligini his qilishadi. |
| **03:00 – 10:00** | Nazariya & MVC Sxemasi | 1–4-slaydlar: MVC qatlamlari, Routerning vazifasi, Relyatsion bog'lanishlar (Foreign Key) va JOIN tushunchasi. | Varaqadagi 1-vazifani (MVC qatlamlarini bog'lash) to'ldirishadi. |
| **10:00 – 28:00** | Amaliy Laboratoriya (Studio) | `studio/index.html` ochiladi. O'quvchilar 4 ta muhandislik kvestini bajaradi (Buyurtma yaratish, JOIN, 400 Bad Request ushlash, O'chirish). | Har bir o'quvchi API so'rovlarini yuborib, SQLite bazasidagi bog'lanishlarni jonli tekshiradi. |
| **28:00 – 35:00** | Kod Tahlili & Backend Kengaytirish | `backend/controllers/orderController.js` kodini tahlil qilish. O'z loyihalariga yangi tekshiruv sharti qo'shish. | Kodni ko'zdan kechirib, partadoshi bilan API javoblarini taqqoslashadi. |
| **35:00 – 40:00** | Xulosa va Baholash | 10 ballik mezon asosida varaqalarni baholash va keyingi 27-dars (XSS & CSRF himoyasi) ga ko'prik. | Ish varaqasini topshirishadi, uy vazifasini belgilab olishadi. |

---

## 4. O'qituvchi Uchun Jonli Dialog Ssenariysi

### Darsni Boshlash:
* **UZ:** "Tasavvur qiling, restoranda oshpazning o'zi eshikda mehmon kutib olsa, o'zi buyurtma olsa, o'zi ovqat pishirsa va o'zi idish yuvsa nima bo'ladi? Restoran 1 soatda to'xtab qoladi! Dasturlashda ham xuddi shunday: router mehmonni qabul qiladi, kontroller buyurtmani tekshiradi, model esa ombordan masalliqlarni olib beradi. Bugun biz professional MVC arxitekturasida ishlaydigan haqiqiy backend tizimini quramiz!"
* **RU:** "Представьте ресторан, где один повар встречает гостей у двери, сам принимает заказ, сам жарит стейк и сам моет посуду. Ресторан захлебнется через час! В архитектуре бэкенда всё так же: Роутер встречает HTTP-запрос, Контроллер проверяет корректность данных, а Модель забирает записи из базы SQLite. Сегодня мы построим масштабируемый сервер по стандарту MVC!"

---

## 5. Baholash Mezoni (10 Ballik Standart Rubrika)

1. **MVC Arxitektura Tushunchasi (2 ball):** Model, View va Controller rollarini to'g'ri ajrata olish.
2. **Relyatsion Baza & Foreign Key (3 ball):** Jadvallarni o'zaro bog'lash, 1-to-Many aloqasini tushunish.
3. **REST API & HTTP Status Kodlari (3 ball):** `200 OK`, `201 Created` va `400 Bad Request` xatoliklarini to'g'ri boshqarish.
4. **SQL JOIN So'rovi va Amaliyot (2 ball):** Studiodagi 4 ta kvestni to'liq bajarib, 100 ballga erishish.
