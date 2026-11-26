# O'qituvchi Qo'llanmasi (Teacher Reading)
## 10–11-sinf · 12-hafta · 32-dars
### Mavzu: Avtonom Kod Yozuvchi Agentlar va CLI Vositalari: OpenCode, Claude Code va TDD Refaktoring
**Dars formati:** Juftlik Dars (Double Block — 80 daqiqa / 2-soatlik dars)

---

### 1. Darsning Pedagogik Maqsadi va Falsafasi
Bugungi 32-darsda 10–11-sinf o'quvchilari zamonaviy dasturlashning eng ilg'or paradigmasiga qadam qo'yadilar: **Terminal-First AI Agentlari**.
O'tgan 31-darsda o'rganilgan Computer-Use ko'rish tizimidan farqli ravishda, bu yerda agent to'g'ridan-to'g'ri fayllar tizimi va terminal bilan ishlaydi.
O'quvchilar **OpenCode** CLI agentidan foydalangan holda TDD (Test-Driven Development) usulida dastur yaratishni va Git orqali nazorat qilishni o'rganadilar.

---

### 2. Darsning 80 Daqiqalik Aniq Xronometraji

#### 1-BOSQICH (40 daqiqa) — Teoriya, Arxitektura va Viktorina
- **00:00–05:00 (5 min):** Kirish, dars mavzusi va maqsadlarini e'lon qilish.
- **05:00–13:00 (8 min):** 31-dars uy vazifasi tahlili: Retina koordinatalar masshtabi xatosi va blitz savol.
- **13:00–19:00 (6 min):** Nega IDE plaginlari o'rniga CLI agentlari (OpenCode)? Terminal-first paradigmasi.
- **19:00–25:00 (6 min):** OpenCode ning 5 ta asosiy vositasi: `read_file`, `edit_file`, `run_command`, `search_files`, `git_diff`.
- **25:00–31:00 (6 min):** TDD metodologiyasi: Qizil (RED) -> Yashil (GREEN) -> Refaktor.
- **31:00–37:00 (6 min):** Ko'p faylli refaktoring va importlar yaxlitligi.
- **37:00–40:00 (3 min):** Git checkpoints va `git reset --hard HEAD` xaloskor qalqoni.

#### 2-BOSQICH (40 daqiqa) — Xavfsizlik, Laboratoriya va Yakun
- **40:00–45:00 (5 min):** Kiberxavfsizlik: Shell buyruqlarini tekshirish va Human-in-the-Loop (HITL) ruxsat tizimi.
- **45:00–50:00 (5 min):** Interaktiv Quiz: 4 ta muhandislik savoli.
- **50:00–55:00 (5 min):** `AGENTS.md` loyiha konstitutsiyasini yozish.
- **55:00–68:00 (13 min):** Katta Amaliy Laboratoriya: `simulator/index.html` da OpenCode orqali TDD kalkulyator yaratish.
- **68:00–74:00 (6 min):** Juftlikda Peer-Review: git diff tekshiruvi va 2 nafar o'quvchining Smartboardda jonli demosi.
- **74:00–77:00 (3 min):** Subagentlar me'morchiligi haqida tushuncha.
- **77:00–80:00 (3 min):** Dars yakuni, 3 darajali uy vazifasi tushuntirilishi va baholash.

---

### 3. O'qituvchi Uchun Chuqur Texnik Savollar va Javoblar

1. **Savol:** Nega TDD (Test-Driven Development) da avval test yozilishi shart?
   - **Javob:** Agar kod yozilgandan keyin test yozilsa, test qasddan kodga moslab qo'yilishi (confirmation bias) mumkin. Avval yozilgan test qat'iy talabni belgilaydi va avval xato (RED) berib, so'ng to'g'ri kod bilan yashil (GREEN) bo'lishi sifat kafolatidir.
2. **Savol:** Agent loyihadagi fayllarni o'zgartirganda nega `git status` va `git diff` ni tekshirish shart?
   - **Javob:** Agent so'ralmagan boshqa fayllarni yoki o'chirmaslik kerak bo'lgan funksiyalarni tasodifan o'zgartirib yubormaganligini ko'rish uchun. Har bir qator o'zgarish inson ko'rigidan (Code Review) o'tishi kerak.
3. **Savol:** Nega OpenCode kabi CLI agentlariga `rm -rf` kabi buyruqlarga avtomatik ruxsat berish xavfli?
   - **Javob:** Prompt injection yoki xato fikrlash tufayli agent butun repozitoriyni yoki operatsion tizim ildizini o'chirib yuborishi mumkin. Har doim Human-in-the-Loop (inson tasdig'i) yoqilgan bo'lishi shart.
