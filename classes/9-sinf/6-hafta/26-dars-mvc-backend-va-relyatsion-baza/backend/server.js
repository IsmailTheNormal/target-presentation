// 9-sinf 26-dars: Asosiy Server Kirish Nuqtasi (Entry Point)
const express = require('express');
const cors = require('cors');
const path = require('path');

const userRoutes = require('./routes/userRoutes');
const orderRoutes = require('./routes/orderRoutes');

const app = express();
const PORT = process.env.PORT || 3000;

// 1. Middlewarelar
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// 2. Marshrutlarni ulash (Routing)
app.use('/api/users', userRoutes);
app.use('/api/orders', orderRoutes);

// 3. Xatoliklarni markazlashgan ushlash (Error Handling Middleware)
app.use((err, req, res, next) => {
  console.error("Server xatosi:", err.message);
  res.status(500).json({ error: "Ichki server xatoligi", details: err.message });
});

app.listen(PORT, () => {
  console.log(`🚀 Target MVC Server ishga tushdi: http://localhost:${PORT}`);
});
