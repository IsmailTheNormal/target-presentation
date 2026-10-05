# SQL Laboratoriyasi va Ma'lumotlar Bazasi Dvigatelini O'rnatish Qo'llanmasi
## Complete Installation & Beginner Workstation Guide · Grade 9 (Lesson 18)

Ushbu qo'llanma 9-sinf o'quvchilari va o'qituvchi uchun **18-dars (Ma'lumotlar Bazasi va SQL: Relyatsion Arxitektura, Indekslar va Xavfsizlik)** amaliy laboratoriya ishini har qanday kompyuterda (Windows, macOS, Linux, VS Code yoki brauzer) 2 daqiqa ichida xatosiz ishga tushirish uchun mo'ljallangan.

---

### 1. Nega Laboratoriya uchun SQLite Tanlandi? (Why SQLite?)

Katta serverli ma'lumotlar bazalari (masalan, to'liq PostgreSQL yoki MySQL serverlari) maktab darsida quyidagi jiddiy muammolarni keltirib chiqaradi:
- **Port to'qnashuvi:** `5432` yoki `3306` portlari boshqa dasturlar tomonidan band bo'lishi mumkin.
- **Admin huquqlari:** Maktab yoki shaxsiy noutbuklarda fon xizmatlarini (daemon/service) o'rnatish admin parolini talab qiladi.
- **Parol unutish:** O'quvchilar `root` yoki `postgres` parolini unutib qo'ysa, dars vaqti behuda sarflanadi.

**SQLite esa zamonaviy IT sanoatining oltin standartidir:**
- **Zero-Configuration:** Hech qanday server, port yoki parol talab qilinmaydi.
- **Yagona fayl:** Butun relyatsion baza bitta faylda saqlanadi (`shop.db`). Uni bemalol nusxalash, o'chirish yoki fleshkaga tashlash mumkin.
- **To'liq standart SQL:** Standart relyatsion SQL (`CREATE TABLE`, `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, `JOIN`, `INDEX`, `BEGIN...COMMIT`) 100% qo'llab-quvvatlanadi.
- **Hamma joyda ishlaydi:** Har bir iPhone, Android, Chrome brauzeri va Mac kompyuterida SQLite o'rnatilgan.

---

### 2. Operatsion Tizimlar Bo'yicha O'rnatish (Installation by OS)

#### A. Windows Kompyuterlarida (3 ta Qulay Yo'l)

##### 1-Usul: Rasmiy Windows Package Manager (Tavsiya etiladi)
PowerShell yoki VS Code terminalini oching va yozing:
```powershell
winget install SQLite.SQLite
```
*O'rnatilgach, terminalni yopib qayta oching va `sqlite3 --version` deb tekshiring.*

##### 2-Usul: Python orqali Bir Zumda Ishga Tushirish (O'rnatish shart emas!)
Agar kompyuterda Python o'rnatilgan bo'lsa, hech narsa yuklab olish shart emas. Python ichida SQLite CLI tayyor:
```powershell
python -m sqlite3 shop.db
```

##### 3-Usul: Portativ (Portable .exe — 1.5 MB)
1. [sqlite.org/download.html](https://www.sqlite.org/download.html) sahifasidan `sqlite-tools-win-x64-*.zip` faylini yuklab oling.
2. Arxiv ichidagi `sqlite3.exe` faylini dars loyihangiz papkasiga tashlang.
3. Terminalda `./sqlite3.exe shop.db` deb ishga tushiring.

---

#### B. macOS Tizimlarida
Barcha Mac kompyuterlarida (Apple Silicon M1/M2/M3 va Intel) SQLite allaqachon zavoddan o'rnatilgan:
```bash
# Terminalni oching va bazani yarating:
sqlite3 shop.db
```
*(Agar xatolik bersa: `xcode-select --install` yoki `brew install sqlite`)*

---

#### C. Linux (Ubuntu, Debian, Fedora) Tizimlarida
```bash
# Ubuntu / Debian:
sudo apt update && sudo apt install -y sqlite3

# Fedora / RedHat:
sudo dnf install -y sqlite
```

---

### 3. VS Code Bilan Ishlash (Eng Chiroyli Vizual Muhit)

O'quvchilar 11-darsda VS Code o'rnatgan. VS Code ichida qulay ishlash tartibi:

1. **Kengaytmani o'rnatish:**
   - VS Code da `Extensions` bo'limiga kiring (`Ctrl+Shift+X` / `Cmd+Shift+X`).
   - Qidiruvga **`SQLite Viewer`** (muallifi: *Florian Klampfer*) deb yozing va **Install** tugmasini bosing.
   - *(Natija: Istalgan `.db` fayl ustiga bosganingizda jadvallar Excel kabi vizual ochiladi!)*

2. **SQL Skript Yozish:**
   - Yangi `lab.sql` fayl oching.
   - Barcha DDL va DML kodlarini ushbu faylga yozing.
   - Terminalda bitta buyruq bilan bazaga yuboring:
     ```bash
     sqlite3 shop.db < lab.sql
     ```

---

### 4. Ilg'or O'quvchilar uchun Docker / PostgreSQL (Lesson 17)

17-darsda Docker o'rgangan o'quvchilar real PostgreSQL konteynerini 5 soniyada ko'tarishi mumkin:
```bash
# 1. Postgres konteynerini fonda ishga tushirish:
docker run --name target-db -e POSTGRES_PASSWORD=target123 -p 5432:5432 -d postgres:alpine

# 2. Konteyner ichidagi psql terminaliga kirish:
docker exec -it target-db psql -U postgres
```

---

### 5. Noutbukda Muammo Chiqqanda: 0-O'rnatish Interaktiv Laboratoriya (Built-in Simulator)

Agar o'quvchining kompyuterida drayver, ruxsat yoki tizim xatosi bo'lsa, darsdan qolib ketmasligi uchun brauzerda quyidagi vositalardan foydalaning:
- **[lab/index.html](lab/index.html)** — **Target CyberLab Rasmiy SQL Simulyatori:** O'rnatish umuman shart emas! To'liq ichki relyatsion dvigatel, 6 ta amaliy kvest, B-Tree tezlik dueli, SQL Injection arenasi va ACID bank crash simulyatori brauzerda 1 soniyada ochiladi.
- **[https://sqlime.org](https://sqlime.org)** — Brauzer ichida ishlovchi yengil, tezkor WebAssembly SQLite dvigateli.
- **[https://sqliteonline.com](https://sqliteonline.com)** — SQLite, PostgreSQL va MariaDB uchun qulay onlayn muhit.

---

### 6. Boshlovchilar uchun SQLite Buyruqlari Cheat-Sheet

SQLite terminaliga kirgandan so'ng (`sqlite>`), quyidagi maxsus boshqaruv buyruqlari ishlatiladi:

| Buyruq | Vazifasi | Izoh |
|---|---|---|
| `.headers on` | Ustun nomlarini ko'rsatish | Natijalar tushunarli bo'ladi |
| `.mode table` | Natijani toza jadvalga solish | Chiroyli ASCII ramka chizadi |
| `PRAGMA foreign_keys = ON;` | Bog'lanishlarni faollashtirish | SQLite da sukut bo'yicha o'chirilgan bo'ladi |
| `.tables` | Barcha jadvallarni ko'rish | `users`, `orders` borligini tekshirish |
| `.schema users` | Jadval tuzilmasini ko'rish | DDL kodini ko'rsatadi |
| `.read lab.sql` | Fayldan SQL ni yuklash | Skriptni to'g'ridan-to'g'ri bajaradi |
| `.quit` yoki `.exit` | Terminaldan chiqish | CLI dan chiqib bosh terminalga qaytadi |

---

### 7. Laboratoriya Topshiriqlarini Bosqichma-bosqich Bajarish

#### 1-Qadam: Terminalni ochish va bazani ulash
```bash
sqlite3 shop.db
```
Prompt ichida sozlamalarni kiriting:
```sql
.headers on
.mode table
PRAGMA foreign_keys = ON;
```

#### 2-Qadam: Relyatsion Jadvallarni Yaratish (DDL)
```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL CHECK(email LIKE '%@%'),
  balance INTEGER NOT NULL DEFAULT 0 CHECK(balance >= 0)
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  product_name TEXT NOT NULL,
  amount INTEGER NOT NULL CHECK(amount > 0),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

#### 3-Qadam: Test Ma'lumotlarini Kiritish (DML)
```sql
INSERT INTO users (full_name, email, balance) VALUES 
('Jasur Aliyev', 'jasur@target.uz', 500000),
('Malika Karimova', 'malika@target.uz', 1200000);

INSERT INTO orders (user_id, product_name, amount) VALUES 
(1, 'Logitech MX Master 3S', 120000),
(1, 'Keychron K2 Keyboard', 95000),
(2, 'Dell 27 4K Monitor', 450000);
```

#### 4-Qadam: Relyatsion JOIN va Tahlil
```sql
SELECT 
  users.full_name,
  COUNT(orders.id) AS total_orders,
  COALESCE(SUM(orders.amount), 0) AS total_spent
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id;
```

#### 5-Qadam: SQL Injection Hujumini va Himoyani Sinash
```sql
-- ❌ Hujumchi kiritganda nima bo'ladi:
SELECT * FROM users WHERE email = '' OR '1'='1';

-- ✅ Parametrlashtirilgan holatda:
SELECT * FROM users WHERE email = 'test'' OR ''1''=''1';
```

---

### 8. Tez-tez Uchraydigan Xatolar va Yechimlar (Troubleshooting)

1. **`sqlite3 : The term 'sqlite3' is not recognized`**
   - *Sabab:* Windows `PATH` o'zgaruvchisiga sqlite qo'shilmagan yoki terminal qayta ochilmagan.
   - *Yechim:* Terminalni butunlay yopib qayta oching. Yoki `python -m sqlite3 shop.db` buyrug'idan foydalaning.

2. **Terminalda `...>` belgisi chiqib qoldi va buyruq bajarmayapti**
   - *Sabab:* SQL so'rovi oxirida nuqta-vergul (`;`) qo'yish unutilgan yoki tirnoq (`'`) yopilmagan.
   - *Yechim:* Klaviatura orqali `;` yozib `Enter` bosing. Agar chiqmasa, `Ctrl+C` bosib bekor qiling.

3. **`FOREIGN KEY constraint failed` xatosi**
   - *Sabab:* `orders` jadvaliga mavjud bo'lmagan `user_id` bilan buyurtma qo'shishga urinyapsiz. Bu relyatsion bazaning to'g'ri ishlashidan darak beradi!
   - *Yechim:* Avval `users` jadvaliga foydalanuvchini qo'shing, so'ngra uning `id`si bilan buyurtma yarating.
