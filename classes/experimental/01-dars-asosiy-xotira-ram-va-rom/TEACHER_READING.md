# 01-dars (Tajribaviy / Akademik Etalon): Kompyuter Asosiy Xotirasi (RAM, ROM va Xotira Arxitekturasi)

**Muallif va O'qituvchi:** Musulmonov Mamarajab · Target International School  
**Fan:** IT, Computer Science & Systems Engineering (10–11-sinf Senior Track)  
**Mavzu:** Kompyuter Asosiy Xotirasi: RAM, ROM, EPROM, DRAM, VRAM va Xotira Shinalari Arxitekturasi  
**Format:** Akademik Etalon Uslub (Zero Bottom Bar, Floating Glassmorphism Controls, Real Hardware Assets)  
**Davomiyligi:** 40 daqiqa (45 daqiqalik bufer bilan)

---

## 🎯 Darsning Bosh Maqsadi va O'quv Natijalari

Ushbu dars o'quvchilarda kompyuter xotirasiga nisbatan "abstrakt quti" sifatidagi yuzaki qarashni yo'qotib, kremniy kristali (silicon die), tranzistorlar va kondensatorlar darajasidagi qat'iy apparat fizikasini shakllantiradi.

Dars yakunida o'quvchi:
1. **Xotira Ierarxiyasi va Shinalar**ni tushuntira oladi: Protsessor registrlari (0.5 ns), SRAM Kesh (1–10 ns), Asosiy DRAM (50–70 ns) va Ikkilamchi NVMe SSD (10–50 µs) o'rtasidagi tezlik, narx va sig'im ziddiyatini asoslaydi.
2. **ROM Evolyutsiyasi va Fizikasi**ni biladi:
   - **MROM:** Kremniy fotolitografik niqobi (Mask) orqali metall kontaktlarning qotirilishi va mutlaq daxlsizligi.
   - **PROM:** 12V–21V kuchlanish impulsi yordamida mikroskopik eruvchan sug'urtalarni (fuse) kuydirish ("blown fuse") va qaytmaslik (OTP).
   - **EPROM:** Nega oddiy oyna emas, aynan **shaffof kvarts oyna** o'rnatilganligi (oddiy shisha qisqa to'lqinli UV nurni yutadi, kvarts esa 254 nm to'lqinni o'tkazadi) hamda fotoelektrik effekt orqali suzuvchi zatvor (floating gate) elektronlarining bo'shatilishini tushuntiradi.
   - **EEPROM & Flash:** Fowler-Nordheim kvant tunnel effekti, baytma-bayt yozish va oksid dielektrikining charchashi (100k sikl).
3. **SRAM va DRAM Muhandislik Janggi**ni tahlil qila oladi:
   - **SRAM:** 6 ta CMOS tranzistordan iborat bistabil multivibrator (flip-flop), nol yangilanish talabi va sub-10ns tezlik.
   - **DRAM:** 1 tranzistor + 1 kondensator (1T1C, ~30 fF), tranzistorning p-n o'tishidagi zaryad sizishi (leakage current) va JEDEC standarti bo'yicha har 64 ms da majburiy qayta zaryadlash (Refresh Cycle) sababi.
4. **VRAM va Frame Buffer Matematikasi**ni hisoblay oladi: Ekrandagi $3840 \times 2160$ piksel, 32-bit RGBA (4 bayt) va Triple Buffering uchun zarur 99.5 MB bufer hajmini formulada topadi.
5. **SIMM vs DIMM va DDR Fizikasi**ni ajratadi: 30/72 pinli birlashgan kontaktlardan 64-bitli mustaqil DIMM kontaktlariga o'tish hamda soat impulsining ham ko'tarilishida, ham tushishida ma'lumot uzatuvchi DDR tamoyili.

---

## ⏱️ 40 Daqiqalik Aniq Vaqt Taqsimoti

| Vaqt oralig'i | Bosqich | O'qituvchi Faoliyati | O'quvchi Faoliyati |
|---|---|---|---|
| **00:00 – 03:00** (3 daq) | **Kirish va Muammoli Savol** | Doskaga `RAM vs ROM` yozadi. "Kompyuter elektrdan uzilganda xotira qayerga ketadi va nima uchun CPU to'g'ridan-to'g'ri SSD dan kod bajara olmaydi?" savolini beradi. | Savol ustida fikrlaydi, 1-slayddagi suzuvchi boshqaruvli taqdimotga diqqat qaratadi. |
| **03:00 – 08:00** (5 daq) | **Xotira Ierarxiyasi va Piramida** | CPU shinalari (Address, Data, Control Bus) va registrlar, kesh, DRAM, SSD kechikishlarini diagramma (`img/memory-tree.png`) orqali tushuntiradi. | Ishchi varaqadagi 1-topshiriqni (kechikishlar moslashtiruvi) to'ldirishga kirishadi. |
| **08:00 – 16:00** (8 daq) | **ROM Oilasi: MROM, PROM, EPROM, EEPROM** | Haqiqiy chiplar (`img/mrom-chip.png`, `img/ti-prom-chip.png`, `img/eprom-window.png`, `img/eprom-die.png`) ni ko'rsatadi. PROM da sug'urta kuyishi va EPROM dagi 254 nm kvarts oyna fizikasini tushuntiradi. | Slayddagi interaktiv sug'urta kuydirgich va UV lampa simulyatorini sinab ko'radi. |
| **16:00 – 24:00** (8 daq) | **RAM, SRAM (6T) va DRAM (1T1C)** | SRAM triggerining yangilanishsiz ishlashini DRAM kondensatori sizishi bilan solishtiradi. Interaktiv zaryad simulyatorini ishga tushirib, 64 ms refresh zaruratini ko'rsatadi. | Ishchi varaqadagi 3-jadvalni (SRAM vs DRAM) to'ldiradi. |
| **24:00 – 30:00** (6 daq) | **VRAM, SIMM vs DIMM va DDR** | Kadrlar buferi (Frame Buffer) sxemasi (`img/vram-diagram.png`) va SIMM/DIMM pinlar chizmasi (`img/simm-dimm.png`) ni tushuntiradi. | 4K Triple Buffering va DRAM zaryad sizishi formulasini hisoblaydi. |
| **30:00 – 38:00** (8 daq) | **Mustaqil Amaliy Laboratoriya** | Sinf bo'ylab yurib, o'quvchilarning ishchi varaqadagi 4, 5 va 6-topshiriqlarini tekshiradi, individual savollarga javob beradi. | Ishchi varaqaning 2-betidagi hisoblashlarni yakunlaydi. |
| **38:00 – 40:00** (2 daq) | **Xulosa va Baholash** | 10 ballik mezon bo'yicha eng yaxshi javoblarni e'lon qiladi, varaqalarni yig'ib oladi. | Ishchi varaqani topshiradi. |

---

## 🎙️ O'qituvchi Uchun Nutq Ssenariysi (Spoken Script)

> *"Hurmatli bo'lajak muhandislar! Bugun biz siz bilan kompyuterning eng muqaddas, ammo ko'pincha noto'g'ri tushuniladigan qismi — **Asosiy Xotira (Primary Memory)** ning silikon ichiga sayohat qilamiz.*
>
> *Ko'pchilik 'Mening kompyuterimda 16 gigabayt operativka bor' yoki 'SSD xotiram 1 terabayt' deb gapiradi. Lekin protsessor nuqtai nazaridan olganda, sizning SSD diskingiz xotira emas, u shunchaki uzoqdagi omborxona! CPU o'z arifmetik buyruqlarini faqat va faqat Asosiy Xotiradan (RAM va ROM) to'g'ridan-to'g'ri o'qiy oladi.*
>
> *Qarang, ekranda haqiqiy chiplar turibdi:*
> 1. *Mana bu Mask ROM — 1980-yillardagi chip. Undagi dastur ishlab chiqaruvchi zavodda metall bilan qotirilgan. Bitta xato ketsa — butun millionlik partiya axlatga tashlangan!*
> 2. *Muhandislar buni yechish uchun PROM ni yaratdilar. U zavoddan bo'sh chiqadi. Siz unga 15 volt tok berib, ichidagi mikroskopik sug'urtalarni bittalab kuydirasiz! Kuygan sug'urta 0 bo'ladi va hech qachon ortga qaytmaydi.*
> 3. *Keyin esa mana bu mo''jiza — EPROM paydo bo'ldi. Uning ustidagi shaffof darchaga qarang. Nega oddiy oyna qo'yilmagan? Chunki oddiy oyna quyoshdagi ultrabinafshani yutib yuboradi! Kvarts oynasi esa 254 nanometrli qisqa to'lqinni o'tkazadi va fotonlar elektronlarni suzuvchi zatvordan urib chiqarib, barcha bitlarni yana 1 ga qaytaradi!*
> 4. *Va nihoyat, nima uchun kompyuterimizdagi operativ xotira (DRAM) har 64 millisekundda o'zini yangilab turishi shart? Chunki uning ichida milliardlab mitti kondensatorlar bor va ulardan mikroskopik zaryad sizib chiqib ketadi. Agar kontroller ularni har 64 ms da zaryadlab turmasa — kompyuteringiz ko'k ekran (BSOD) beradi!*
>
> *Keling, ishchi varaqalarni ochamiz va bu qonuniyatlarni formulalar orqali o'z qo'limiz bilan hisoblaymiz!"*

---

## ⚠️ O'quvchilarning Tipik Xatolari va Qopqonlar (Misconceptions)

1. **"Random Access" so'zining noto'g'ri talqini:**
   - *Xato:* O'quvchilar buni "tasodifiy xotira" deb o'ylashadi (go'yo ma'lumot qayerga tushishi tasodifdek).
   - *To'g'rilash:* "Random" bu yerda *Sequential* (ketma-ket) ga qarama-qarshi bo'lib, **"ixtiyoriy manzilga bir xil doimiy vaqtda kirish" ($O(1)$)** degan ma'noni bildiradi. Magnit lentadagi kabi oldingi qismlarni o'rash talab qilinmaydi.
2. **EPROM kvarts oynasini oddiy shisha deb hisoblash:**
   - *Xato:* "Oddiy oyna qo'ysa ham ichi ko'rinadi-ku, nega kvarts?"
   - *To'g'rilash:* Oddiy deraza shishasi UV-C (200–280 nm) nurlarini deyarli 100% yutadi va o'tkazmaydi. Faqat yuqori tozalikdagi kvarts kristalli (fused silica) 254 nm to'lqin uzunligini o'tkaza oladi.
3. **SRAM nega asosiy xotira bo'la olmasligini tushunmaslik:**
   - *Xato:* "SRAM tezroq ekan, nega hamma kompyuterga 32 GB SRAM qo'yilmaydi?"
   - *To'g'rilash:* SRAM bitta bit uchun 6 ta tranzistor talab qiladi, DRAM esa atigi 1 ta tranzistor va 1 ta kondensator (1T1C). 32 GB SRAM mikrosxemasi plastinada ulkan joy olgan, o'n minglab dollar turgan va kompyuter korpusida haddan tashqari qizib ketgan bo'lardi.
4. **SIMM va DIMM pinlarini shunchaki shakl deb o'ylash:**
   - *To'g'rilash:* SIMM da old va orqa kontaktlar birlashgan (faqat 32-bit), DIMM da esa old va orqa kontaktlar mustaqil elektr o'tkazgichlar (to'liq 64-bit ma'lumot shinasini beradi).

---

## 📋 Ishchi Varaqa Uchun To'liq Javoblar Kaliti (Teacher Answer Key)

### 1-Topshiriq: Xotira Ierarxiyasi va Kechikishlar (2 ball)
- **[ A ] CPU Registrlari** ➔ $\sim 0.5\text{ ns}$ ➔ Protsessor ALU yadrosi ichida (1 takt).
- **[ B ] SRAM Kesh (L1/L2)** ➔ $1 - 5\text{ ns}$ ➔ CPU kristalli ichidagi 6-tranzistorli triggerlar.
- **[ C ] Asosiy RAM (DRAM)** ➔ $50 - 70\text{ ns}$ ➔ Ona platadagi DIMM slotlari (1T1C).
- **[ D ] NVMe SSD** ➔ $10 - 50\text{ µs}$ ➔ PCIe / M.2 shinasidagi NAND Flash bloklari.

### 2-Topshiriq: ROM Oilasi Fizikasi (3 ball)
- **2.1 PROM Blown Fuses:** 15V kuchlanish berilganda yuqori tok mikroskopik nixrom sug'urtani jismonan eritib bug'lantiradi ("blown fuse"). Zanjir uzilib, bit 1 dan 0 ga aylanadi. Eritilgan metall qayta ulanmagani sababli jarayon qaytmas (One-Time Programmable).
- **2.2 EPROM Kvarts Oynasi:** Oddiy shisha 254 nm to'lqinli qisqa UV nurni yutadi, faqat toza optik kvarts uni o'tkazadi. 254 nm to'lqinli UV fotonlar suzuvchi zatvor (floating gate) dagi elektronlarga energiya beradi va ular fotoelektrik effekt orqali oksid to'sig'idan sakrab o'tib, zaryadsizlanadi (barcha bitlar 1 ga qaytadi).

### 3-Topshiriq: SRAM vs DRAM Taqqoslash (2 ball)
- Yacheyka: SRAM = 6 tranzistor (trigger), DRAM = 1 tranzistor + 1 kondensator (1T1C).
- Yangilanish: SRAM da kerak emas (0), DRAM da har 64 ms da majburiy.
- Qo'llanish: SRAM = L1/L2/L3 kesh, DRAM = Asosiy operativ xotira (DIMM).

### 4-Topshiriq: DRAM Kondensator Sizishi Hisobi (1.5 ball)
- Formula: $\Delta t = \frac{C \cdot \Delta V}{I_{\text{leak}}} = \frac{30 \times 10^{-15}\text{ F} \times 0.6\text{ V}}{0.5 \times 10^{-12}\text{ A}} = \frac{18 \times 10^{-15}}{0.5 \times 10^{-12}} = 36 \times 10^{-3}\text{ s} = 36\text{ millisekund}$.
- Xulosa: Kondensator atigi 36 ms ichida zaryadini yo'qotishi mumkin. Shuning uchun JEDEC standarti bo'yicha xotira kontrolleri har 64 ms da barcha satrlarni qayta zaryadlab (Refresh) turishi shart.

### 5-Topshiriq: VRAM Frame Buffer Hisobi (1.5 ball)
- 1 kadr hajmi: $3840 \times 2160 \times 4\text{ bayt} = 33,177,600\text{ bayt} \approx 31.64\text{ MB} \text{ (yoki } 33.18\text{ MB dec)}$.
- Triple Buffering (3 bufer): $31.64\text{ MB} \times 3 = 94.92\text{ MB} \text{ (yoki } 33.18 \times 3 = 99.54\text{ MB dec)}$.

---

## 🏆 Baholash Mezonlari (10 Ballik Shkala)

| To'plangan Ball | Daraja (Grade) | Rasmiy Kompetensiya Ta'rifi |
|---|---|---|
| **9.0 – 10.0 ball** | **A (A'lo)** | Barcha formulalar to'g'ri hisoblangan, EPROM kvarts oynasi va DRAM zaryad sizishi to'liq fizik asoslangan. |
| **7.0 – 8.5 ball** | **B (Yaxshi)** | Ierarxiya va ROM to'g'ri, VRAM yoki DRAM hisob-kitobida kichik arifmetik noaniqlik mavjud. |
| **5.0 – 6.5 ball** | **C (Qoniqarli)** | Asosiy atamalar to'g'ri, lekin 1T1C va EPROM kvarts fizikasi tushuntirilmagan. |
| **0.0 – 4.5 ball** | **D (Qayta topshirish)** | Varaqa to'ldirilmagan yoki xotira tushunchalarida jiddiy chalkashliklar mavjud. |
