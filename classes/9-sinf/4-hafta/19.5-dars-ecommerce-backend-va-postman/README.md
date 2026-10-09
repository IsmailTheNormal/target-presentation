# Target International School · 9-sinf · 4-hafta · 19.5-dars
## Vibecoding E-Commerce Backend: Users, Orders, CRUD & Postman API Testing

Ushbu dars 9-sinf o'quvchilari uchun **19-dars (Backend Asoslari)** va **20-dars (Full-Stack Deploy)** oralig'idagi amaliy ko'prik hisoblanadi. O'quvchilar Vibecoding usulida haqiqiy E-Commerce backendini (`users` va `orders` relying jadvallari, balans nazorati, status tranzaksiyalari) yaratadilar va barcha CRUD harakatlarini (GET, POST, PATCH, DELETE) **Postman** vositasi yordamida avtomatlashtirilgan testlar bilan sinovdan o'tkazadilar.

---

### 🚀 Tezkor Ishga Tushirish (Local Environment)

```bash
# 1. Kutubxonalarni o'rnatish
npm install

# 2. Serverni ishga tushirish (port: 3000)
npm run dev
# yoki
node server.js
```

Server ishga tushgach: `http://localhost:3000/api/health`

---

### 📦 API Marshrutlari (Endpoints)

| Method | Marshrut | Tavsif | Status Kodlar |
|---|---|---|---|
| `GET` | `/api/users` | Barcha foydalanuvchilar va ularning balanslari | `200 OK` |
| `GET` | `/api/users/:id` | Bitta foydalanuvchi va uning barcha buyurtmalari | `200 OK`, `404 Not Found` |
| `POST` | `/api/users` | Yangi xaridor ro'yxatdan o'tkazish (`full_name`, `email`, `balance`) | `201 Created`, `400 Bad Request` |
| `GET` | `/api/orders` | Buyurtmalar ro'yxati (filtrlar: `?user_id=1&status=pending`) | `200 OK` |
| `POST` | `/api/orders` | Yangi buyurtma yaratish (Mablag' yetarliligini tekshirib yechadi) | `201 Created`, `400 Bad Request`, `404 Not Found` |
| `PATCH` | `/api/orders/:id` | Buyurtma holatini yangilash (`pending` -> `completed` / `cancelled`) | `200 OK`, `400 Bad Request`, `404 Not Found` |
| `DELETE` | `/api/orders/:id` | Buyurtmani bekor qilish yoki o'chirish | `200 OK`, `404 Not Found` |

---

### 📮 Postman Kolleksiyasini Yuklash

1. Postman dasturini oching.
2. `Import` tugmasini bosing.
3. Ushbu papkadagi `ecommerce_postman_collection.json` faylini tanlang.
4. Barcha 7 ta tayyor so'rov va `pm.test` avtomatlashtirilgan testlari bir zumda tayyor bo'ladi!
