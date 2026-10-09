/**
 * Target International School · Vibecoding (9-sinf · 4-hafta · 19.5-dars)
 * Mavzu: Vibecoding E-Commerce Backend — Users, Orders & Postman API Testing
 * Fayl: server.js
 */

const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware sozlamalari
app.use(cors());
app.use(express.json());

// In-Memory E-Commerce Relyatsion Ma'lumotlar Bazasi
let users = [
  { id: 1, full_name: "Jasur Aliyev", email: "jasur@target.uz", balance: 500000, created_at: "2026-10-01 09:00:00" },
  { id: 2, full_name: "Malika Karimova", email: "malika@target.uz", balance: 1200000, created_at: "2026-10-02 11:30:00" },
  { id: 3, full_name: "Azizbek Rahimov", email: "aziz@target.uz", balance: 250000, created_at: "2026-10-03 14:15:00" }
];

let orders = [
  { id: 1, user_id: 1, product_name: "Mexanik Klaviatura RGB", amount: 350000, status: "completed", created_at: "2026-10-04 10:10:00" },
  { id: 2, user_id: 1, product_name: "O'yin Sichqonchasi 16000 DPI", amount: 120000, status: "pending", created_at: "2026-10-05 12:40:00" },
  { id: 3, user_id: 2, product_name: "27' 4K IPS Monitor Pro", amount: 850000, status: "completed", created_at: "2026-10-06 16:20:00" }
];

let nextUserId = 4;
let nextOrderId = 4;

// -------------------------------------------------------------
// 0. HEALTH CHECK & STATUS
// -------------------------------------------------------------
app.get('/api/health', (req, res) => {
  res.json({
    status: "ok",
    service: "Target E-Commerce Backend",
    version: "1.0.0",
    uptime: process.uptime(),
    timestamp: new Date().toISOString()
  });
});

// -------------------------------------------------------------
// 1. USERS ENDPOINTS (GET, POST)
// -------------------------------------------------------------

// GET /api/users - Barcha foydalanuvchilar ro'yxati
app.get('/api/users', (req, res) => {
  res.status(200).json({
    success: true,
    count: users.length,
    users: users
  });
});

// GET /api/users/:id - Bitta foydalanuvchi ma'lumotlari va uning buyurtmalari
app.get('/api/users/:id', (req, res) => {
  const userId = parseInt(req.params.id, 10);
  const user = users.find(u => u.id === userId);

  if (!user) {
    return res.status(404).json({
      success: false,
      error: `ID=${userId} bo'lgan foydalanuvchi topilmadi`
    });
  }

  // Relyatsion bog'lanish: Foydalanuvchining barcha buyurtmalari
  const userOrders = orders.filter(o => o.user_id === userId);

  res.status(200).json({
    success: true,
    user: {
      ...user,
      orders: userOrders
    }
  });
});

// POST /api/users - Yangi mijoz ro'yxatdan o'tkazish
app.post('/api/users', (req, res) => {
  const { full_name, email, balance } = req.body;

  // 1. Validatsiya
  if (!full_name || !email) {
    return res.status(400).json({
      success: false,
      error: "full_name va email maydonlari to'ldirilishi shart!"
    });
  }

  // 2. Email unikalligi
  const existingUser = users.find(u => u.email.toLowerCase() === email.toLowerCase());
  if (existingUser) {
    return res.status(400).json({
      success: false,
      error: "Ushbu email bilan foydalanuvchi allaqachon mavjud!"
    });
  }

  const initialBalance = typeof balance === 'number' && balance >= 0 ? balance : 0;

  const newUser = {
    id: nextUserId++,
    full_name: full_name.trim(),
    email: email.trim().toLowerCase(),
    balance: initialBalance,
    created_at: new Date().toISOString().replace('T', ' ').slice(0, 19)
  };

  users.push(newUser);

  res.status(201).json({
    success: true,
    message: "Foydalanuvchi muvaffaqiyatli yaratildi",
    user: newUser
  });
});

// -------------------------------------------------------------
// 2. ORDERS ENDPOINTS (GET, POST, PATCH, DELETE)
// -------------------------------------------------------------

// GET /api/orders - Barcha buyurtmalar (filtrlar: ?user_id=1&status=pending)
app.get('/api/orders', (req, res) => {
  const { user_id, status } = req.query;
  let result = [...orders];

  if (user_id) {
    result = result.filter(o => o.user_id === parseInt(user_id, 10));
  }

  if (status) {
    result = result.filter(o => o.status.toLowerCase() === status.toLowerCase());
  }

  res.status(200).json({
    success: true,
    count: result.length,
    orders: result
  });
});

// POST /api/orders - Yangi buyurtma berish (Tranzaksiya mantiqi)
app.post('/api/orders', (req, res) => {
  const { user_id, product_name, amount } = req.body;

  // 1. Validatsiya
  if (!user_id || !product_name || typeof amount !== 'number') {
    return res.status(400).json({
      success: false,
      error: "user_id, product_name va son ko'rinishidagi amount maydonlari talab qilinadi!"
    });
  }

  if (amount <= 0) {
    return res.status(400).json({
      success: false,
      error: "Buyurtma summasi (amount) 0 dan katta bo'lishi shart!"
    });
  }

  // 2. Foydalanuvchini tekshirish (Foreign Key nazorati)
  const user = users.find(u => u.id === parseInt(user_id, 10));
  if (!user) {
    return res.status(404).json({
      success: false,
      error: `ID=${user_id} bo'lgan mijoz topilmadi! Buyurtma bekor qilindi.`
    });
  }

  // 3. Moliyaviy Balans Tekshiruvi
  if (user.balance < amount) {
    return res.status(400).json({
      success: false,
      error: `Hisobda mablag' yetarli emas! Mavjud balans: ${user.balance.toLocaleString()} so'm, talab qilinadi: ${amount.toLocaleString()} so'm.`
    });
  }

  // 4. Balansdan mablag' yechish va buyurtmani saqlash
  user.balance -= amount;

  const newOrder = {
    id: nextOrderId++,
    user_id: user.id,
    product_name: product_name.trim(),
    amount: amount,
    status: "pending",
    created_at: new Date().toISOString().replace('T', ' ').slice(0, 19)
  };

  orders.push(newOrder);

  res.status(201).json({
    success: true,
    message: "Buyurtma qabul qilindi va foydalanuvchi hisobidan mablag' yechildi",
    order: newOrder,
    user_updated_balance: user.balance
  });
});

// PATCH /api/orders/:id - Buyurtma holatini yangilash (pending -> completed / cancelled)
app.patch('/api/orders/:id', (req, res) => {
  const orderId = parseInt(req.params.id, 10);
  const { status } = req.body;

  const validStatuses = ['pending', 'completed', 'cancelled'];
  if (!status || !validStatuses.includes(status.toLowerCase())) {
    return res.status(400).json({
      success: false,
      error: `Yaroqsiz status! Faqat quyidagilardan biri bo'lishi mumkin: ${validStatuses.join(', ')}`
    });
  }

  const order = orders.find(o => o.id === orderId);
  if (!order) {
    return res.status(404).json({
      success: false,
      error: `ID=${orderId} bo'lgan buyurtma topilmadi`
    });
  }

  const oldStatus = order.status;
  order.status = status.toLowerCase();

  // Agar buyurtma bekor qilinsa (cancelled), mablag' foydalanuvchiga qaytariladi (Refund mantiqi)
  let refundMessage = "";
  if (oldStatus !== 'cancelled' && order.status === 'cancelled') {
    const user = users.find(u => u.id === order.user_id);
    if (user) {
      user.balance += order.amount;
      refundMessage = ` Qaytarilgan mablag': ${order.amount.toLocaleString()} so'm. Yangi balans: ${user.balance.toLocaleString()} so'm.`;
    }
  }

  res.status(200).json({
    success: true,
    message: `Buyurtma statusi o'zgartirildi: ${oldStatus} -> ${order.status}.${refundMessage}`,
    order: order
  });
});

// DELETE /api/orders/:id - Buyurtmani bekor qilish yoki tizimdan o'chirish
app.delete('/api/orders/:id', (req, res) => {
  const orderId = parseInt(req.params.id, 10);
  const index = orders.findIndex(o => o.id === orderId);

  if (index === -1) {
    return res.status(404).json({
      success: false,
      error: `ID=${orderId} bo'lgan buyurtma topilmadi`
    });
  }

  const deletedOrder = orders.splice(index, 1)[0];

  res.status(200).json({
    success: true,
    message: `ID=${orderId} bo'lgan buyurtma tizimdan o'chirildi`,
    deleted_order: deletedOrder
  });
});

// 404 Handler
app.use((req, res) => {
  res.status(404).json({
    success: false,
    error: `Marshrut topilmadi: ${req.method} ${req.url}`
  });
});

// Serverni ishga tushirish
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`[Target E-Commerce API] Server ishga tushdi: http://localhost:${PORT}`);
    console.log(`[Docs & Endpoints]`);
    console.log(` - GET    /api/users`);
    console.log(` - POST   /api/users`);
    console.log(` - GET    /api/orders`);
    console.log(` - POST   /api/orders`);
    console.log(` - PATCH  /api/orders/:id`);
    console.log(` - DELETE /api/orders/:id`);
  });
}

module.exports = app;
