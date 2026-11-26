#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_7_8_w12_l35.py — Builder for 7–8th Grade, Week 12, Lesson 35

Mavzu: Inventar va Buyumlar Tizimi: Drag-and-Drop, Artefaktlar va Qahramon Stats
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 7-8-sinf (Game Dev, Interaktiv Veb & FUT Creator Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "7-8-sinf", "12-hafta", "35-dars-inventar-tizimi-va-drag-drop")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "simulator"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides for 80-min Double Block)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide is-on" data-phase="Kirish|Введение|Intro" data-time="00:00–05:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="7–8-КЛАСС · 12-Я НЕДЕЛЯ · УРОК 35" data-en="GRADES 7–8 · WEEK 12 · LESSON 35">7–8-SINF · 12-HAFTA · 35-DARS</span></div>
    <h1 class="display" data-ru="Система Инвентаря: Drag-and-Drop, Артефакты и Статы Героя" data-en="Inventory System: Drag-and-Drop, Artifacts & Hero Stats">Inventar va Buyumlar Tizimi: Drag-and-Drop, Artefaktlar va Qahramon Stats</h1>
    <p class="lede" data-ru="Создаем профессиональный RPG-инвентарь на HTML5 и JS: перемещение предметов Drag-and-Drop, сетка слотов 4×4, расчет боевых баффов (ATK, DEF, SPD), сохранение в LocalStorage и защита от читерства." data-en="Engineering a professional RPG inventory engine in HTML5 & JS: HTML5 Drag-and-Drop API, 4×4 slot grid, combat stat buff calculations (ATK, DEF, SPD), LocalStorage persistence, and anti-cheat validation.">HTML5 va JS yordamida professional RPG inventar tizimini yaratamiz: buyumlarni Drag-and-Drop orqali surish, 4×4 slotlar matritsasi, jangovar kuchaytirgichlar (ATK, DEF, SPD) hisobi, LocalStorage saqlash va cheatlardan himoya.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="HTML5 Drag & Drop" data-en="HTML5 Drag & Drop">Drag-and-Drop API</h3>
        <p data-ru="Как браузер захватывает предмет, передает данные через dataTransfer и роняет в нужный слот экипировки." data-en="How the browser grabs items, transfers data via dataTransfer, and drops them into equipment slots.">Brauzer qanday qilib buyumni ushlaydi, dataTransfer orqali ma'lumot uzatadi va jihozlash slotiga tashlaydi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">RPG Inventory Studio</div>
        <h3 data-ru="Боевой Инвентарь" data-en="Combat Inventory">Haqiqiy RPG Xalta</h3>
        <p data-ru="Интерактивная панель: надевание меча и щита, мгновенный пересчет урона героя и сохранение экипировки." data-en="Interactive HUD: equipping swords and shields, real-time stat recalculations, and persistent gear saves.">Qilich va qalqonni taqish, qahramon zarba kuchini avtomatik oshirish va jihozlarni saqlash tizimi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Tahlil|Разбор|Review" data-time="05:00–13:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 34-УРОКА" data-en="LESSON 34 HOMEWORK REVIEW">34-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Разбор 34-урока: Ошибки в Очереди BFS и Застревание Врагов" data-en="Lesson 34 Review: BFS Queue Mistakes & Frozen Enemies">34-dars Tahlili: BFS Navbatidagi Xatolar va Dushman Qotishi</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Типичная Ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Забытый массив visited (Утечка Памяти)" data-en="Missing visited Set (Infinite Loop)">visited to'plamini unutish (Cheksiz Sikl)</h3>
        <p data-ru="Если при поиске в ширину (BFS) не помечать посещенные клетки в visited, алгоритм начинает бесконечно ходить по кругу между двумя соседними точками, вызывая зависание вкладки!" data-en="Omitting the visited coordinate set in BFS causes the queue to bounce infinitely between adjacent tiles, locking up the browser thread!">Agar BFS qidiruvida borilgan kataklarni visited to'plamiga saqlash unutilsa, navbat ikkita qo'shni nuqta orasida cheksiz aylanib, brauzerni qotirib qo'yadi!</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#ef4444;">// XATO: visited yo'q, xotira to'lib ketadi</span>
queue.push(neighbor); <span style="color:#ef4444;">// Qayta-qayta qo'shilaveradi!</span>
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Золотой Стандарт" data-en="Golden Standard">Oltin Standart (Best Practice)</div>
        <h3 data-ru="Set() для быстрой проверки O(1)" data-en="Instant O(1) visited Set Check">Set() bilan lahzalik tekshiruv</h3>
        <p data-ru="Использование new Set() с ключом 'x,y' гарантирует мгновенную проверку O(1) и исключает повторное посещение клеток, обеспечивая стабильные 60 FPS." data-en="Using a new Set() keyed by 'x,y' guarantees instant O(1) lookup, preventing duplicate tile processing and securing 60 FPS.">Set() dan foydalanib 'x,y' koordinatani saqlash O(1) tezlikda tekshiradi, takroriy kataklarni qo'shmaydi va silliq 60 FPS ni kafolatlaydi.</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#22c55e;">// TO'G'RI: visited tekshiruvi</span>
const key = `${nx},${ny}`;
if (!visited.has(key)) {
  visited.add(key);
  queue.push({ x: nx, y: ny, path: [...cur.path, {x: nx, y: ny}] });
}
        </div>
      </div>
    </div>
    <div class="grid-2" style="margin-top:14px;">
      <div class="box">
        <span class="badge" data-ru="Блиц-вопрос (30 сек)" data-en="Blitz Question (30s)">Blitz Savol</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="Когда умный враг побежден, что из него выпадает и где игрок должен это хранить?" data-en="When an enemy is defeated, what loot drops and where does the player stash it?">Dushman mag'lub bo'lgach, undan nima tushadi va o'yinchi uni qayerda saqlashi kerak?</p>
      </div>
      <div class="box">
        <span class="badge" data-ru="Мост к теме" data-en="Bridge to Today">Bugungi Mavzuga Ko'prik</span>
        <p style="margin-top:4px; font-size:13px;" data-ru="Побежденный босс роняет редкий лут! Сегодня мы построим систему инвентаря с Drag-and-Drop, чтобы экипировать трофеи и усиливать статы." data-en="Bosses drop legendary loot! Today we build a full Drag-and-Drop inventory engine to equip spoils and multiply hero stats.">Mag'lub dushmandan afsonaviy o'lja tushadi! Bugun biz buyumlarni xaltadan olib qahramonga taqadigan professional Drag-and-Drop inventar tizimini quramiz.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: RPG INVENTORY ARCHITECTURE -->
  <section class="slide" data-phase="Konsept|Концепт|Concept" data-time="13:00–19:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="АРХИТЕКТУРА ИНВЕНТАРЯ · ГЕЙМ-ДИЗАЙН" data-en="INVENTORY ARCHITECTURE · GAME DESIGN">INVENTAR ARXITEKTURASI · GEYM-DIZAYN</span></div>
    <h2 data-ru="Анатомия Инвентаря: Рюкзак против Экипировки" data-en="Inventory Anatomy: Backpack vs Equipment Slots">Inventar Anatomiyasi: Xalta (Backpack) vs Jihozlar (Equipped)</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="1. Сетка Рюкзака (Backpack)" data-en="1. Backpack Grid">1. Xalta Slotlari (Backpack 4×4)</div>
        <h3 data-ru="16 Ячеек Хранения" data-en="16 Storage Cells">16 Ta Zaxira Sloti</h3>
        <p data-ru="Хранилище предметов, найденных в подземелье: зелья, свитки, руны, запасное оружие. Предметы в рюкзаке НЕ дают боевых бонусов, пока не надеты!" data-en="Storage cells holding collected dungeon loot: potions, runes, spare weapons. Inactive items grant zero stat buffs until equipped!">Yer osti labirintidan yig'ilgan zaxira buyumlar ombori: eliksirlar, zaxira qurollar. Xaltada turgan buyumlar taqilmaguncha qahramonga kuch bermaydi!</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
const backpack = [ item1, null, item2, null, ... ]; // 16 slot
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="2. Слоты Экипировки (Equipped)" data-en="2. Equipment Slots">2. Jihozlash Slotlari (Paperdoll)</div>
        <h3 data-ru="Тело Персонажа" data-en="Character Body Slots">Qahramon Tanasi</h3>
        <p data-ru="Активные ячейки тела: Шлем, Нагрудник, Оружие (Weapon) и Щит (Shield). Только надетые сюда предметы увеличивают урон (ATK) и броню (DEF)!" data-en="Active body sockets: Helmet, Chestplate, Weapon, and Shield. Only items placed here amplify hero Attack (ATK) and Defense (DEF)!">Qahramon ustidagi faol slotlar: Bosh kiyim, Zirh, Qurol va Qalqon. Faqat shu yerga kiyilgan buyumlar zarba kuchi (ATK) va himoyani (DEF) oshiradi!</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
const equipped = { head: null, chest: null, weapon: itemSword, shield: itemShield };
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: ITEM DATA SCHEMA -->
  <section class="slide" data-phase="Sxema|Структура|Schema" data-time="19:00–25:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="СТРУКТУРА ПРЕДМЕТА · ITEM SCHEMA" data-en="ITEM DATA SCHEMA · OBJECT MODEL">BUYUM STRUKTURASI · DATA MODEL</span></div>
    <h2 data-ru="Модель Данных: Как Предмет Описывается в Коде" data-en="Item Data Model: Representing Artifacts in Code">Buyum Modeli: Artefakt Kodda Qanday Saqlanadi?</h2>
    <div class="grid-2">
      <div class="card">
        <div class="code-block" style="font-size:11.5px; line-height:1.5;">
<span style="color:#64748b;">// Afsonaviy Kiber-Qilich ob'ekti</span>
const cyberKatana = {
  <span style="color:#3b82f6;">id</span>: <span style="color:#22c55e;">"wpn_katana_01"</span>,
  <span style="color:#3b82f6;">name</span>: <span style="color:#22c55e;">"Kiber-Katana v2"</span>,
  <span style="color:#3b82f6;">type</span>: <span style="color:#22c55e;">"weapon"</span>,       <span style="color:#64748b;">// Faqat 'weapon' slotiga tushadi</span>
  <span style="color:#3b82f6;">icon</span>: <span style="color:#22c55e;">"⚔️"</span>,
  <span style="color:#3b82f6;">rarity</span>: <span style="color:#a855f7;">"legendary"</span>, <span style="color:#64748b;">// Binafsha hoshiya</span>
  <span style="color:#3b82f6;">stats</span>: {
    <span style="color:#eab308;">atk</span>: +35,            <span style="color:#64748b;">// Hujum kuchi +35</span>
    <span style="color:#eab308;">spd</span>: +5              <span style="color:#64748b;">// Harakat tezligi +5</span>
  }
};
        </div>
      </div>
      <div class="card">
        <h3 data-ru="Грейды Редкости (Rarity Tiers)" data-en="Rarity Tiers & Colors">Nodirlik Darajalari (Rarity):</h3>
        <ul style="font-size:12px; line-height:1.8; margin-top:8px;">
          <li data-ru="⚪ <strong>Common (Обычный):</strong> стартовые предметы (+2..+5 статов)." data-en="⚪ <strong>Common:</strong> starter gear (+2..+5 stats).">⚪ <strong style="color:#94a3b8;">Common (Oddiy):</strong> boshlang'ich buyumlar (+2..+5 stat).</li>
          <li data-ru="🟢 <strong>Rare (Редкий):</strong> выпадает из стражи замка (+10..+15 статов)." data-en="🟢 <strong>Rare:</strong> drops from castle guards (+10..+15 stats).">🟢 <strong style="color:#22c55e;">Rare (Noyob):</strong> qasr dushmanlaridan tushadi (+10..+15 stat).</li>
          <li data-ru="🟣 <strong>Epic (Эпический):</strong> трофеи мини-боссов (+20..+30 статов)." data-en="🟣 <strong>Epic:</strong> mini-boss loot drops (+20..+30 stats).">🟣 <strong style="color:#a855f7;">Epic (Epik):</strong> minion-bosslardan tushadi (+20..+30 stat).</li>
          <li data-ru="🟡 <strong>Legendary (Легендарный):</strong> добыча главного дракона (+35..+60 статов)." data-en="🟡 <strong>Legendary:</strong> cyber-dragon boss loot (+35..+60 stats).">🟡 <strong style="color:#eab308;">Legendary (Afsonaviy):</strong> bosh kiber-ajdarho o'ljasi (+35..+60 stat).</li>
        </ul>
        <p style="font-size:11px; margin-top:10px; color:var(--ink-secondary);" data-ru="Цвет рамки слота меняется автоматически через класс: .slot.legendary { border-color: #facc15; }" data-en="Slot border color shifts automatically via CSS: .slot.legendary { border-color: #facc15; }">Slot hoshiyasi CSS klassi orqali avtomatik bo'yaladi: <code>.slot.legendary { border-color: #facc15; }</code></p>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: HTML5 DRAG AND DROP API -->
  <section class="slide" data-phase="Standart|Стандарт|Standard" data-time="25:00–31:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="HTML5 DRAG AND DROP · ЦИКЛ СОБЫТИЙ" data-en="HTML5 DRAG AND DROP · EVENT LIFECYCLE">HTML5 DRAG AND DROP · HODISALAR ZANJIRI</span></div>
    <h2 data-ru="Анатомия Drag & Drop: 3 Ключевых События" data-en="Anatomy of Drag & Drop: 3 Essential Events">Drag & Drop Anatomiyasi: 3 Ta Asosiy Hodisa</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="1. Старт захвата" data-en="1. Grab Event">1. ondragstart</div>
        <h3 data-ru="Захват Мышью" data-en="Drag Origin">Buyumni Ko'tarish</h3>
        <p data-ru="Срабатывает на перетаскиваемом предмете. Записываем ID предмета в dataTransfer:" data-en="Fires on the dragged item. Stores the item's unique ID into dataTransfer:">Sichqoncha bilan buyumni ushlaganda ishlaydi. dataTransfer xotirasiga buyum ID-sini yozamiz:</p>
        <div class="code-block" style="font-size:10.5px; margin-top:6px;">
e.dataTransfer.setData(
  "text/plain", item.id
);
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(234,179,8,0.15); color:var(--warning);" data-ru="2. Полет над слотом" data-en="2. Hover Event">2. ondragover</div>
        <h3 data-ru="Разрешение Сброса" data-en="Allowing Drop">Tashlashga Ruxsat</h3>
        <p data-ru="По умолчанию браузер ЗАПРЕЩАЕТ сброс! Нужно обязательно вызвать e.preventDefault():" data-en="Browsers prohibit dropping by default! You MUST invoke e.preventDefault():">Brauzer odatda tashlashni taqiqlaydi! Tashlashga ruxsat berish uchun preventDefault() shart:</p>
        <div class="code-block" style="font-size:10.5px; margin-top:6px;">
slot.ondragover = (e) =&gt; {
  e.preventDefault(); // Ruxsat!
};
        </div>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="3. Падение в слот" data-en="3. Drop Event">3. ondrop</div>
        <h3 data-ru="Финальный Сброс" data-en="Final Drop">Slotga Tushish</h3>
        <p data-ru="Срабатывает на целевом слоте. Читаем ID предмета, проверяем тип слота и экипируем:" data-en="Fires on destination slot. Reads item ID, validates slot type, and equips:">Maqsadli slotda ishlaydi. ID-ni o'qib olib, slot turi to'g'ri kelsa, buyumni kiygizadi:</p>
        <div class="code-block" style="font-size:10.5px; margin-top:6px;">
const id = e.dataTransfer
  .getData("text/plain");
equipItem(id, slotType);
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: SLOT VALIDATION & TYPE MATCHING -->
  <section class="slide" data-phase="Muhandislik|Инженерия|Engineering" data-time="31:00–37:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="ВАЛИДАЦИЯ СЛОТОВ · ЗАЩИТА ТИПОВ" data-en="SLOT VALIDATION · TYPE INTEGRITY">SLOT VALIDATSIYASI · TURLAR MOSLIGI</span></div>
    <h2 data-ru="Защита от Дурака: Нельзя Надеть Меч на Голову!" data-en="Type Safety: You Cannot Equip a Sword as a Helmet!">Qoidalar Nazorati: Qilichni Boshga Kiyib Bo'lmaydi!</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Правило валидации типов" data-en="Type Matching Logic">Turlar Mosligi Qoidasi</h3>
        <p data-ru="Если игрок пытается перетащить Меч (type: 'weapon') в слот Шлема (accepts: 'head'), система должна отклонить действие и подсветить слот красным:" data-en="If a player drags a sword into a helmet slot, the engine rejects the drop and flashes red:">Agar o'yinchi Qilichni ('weapon') Bosh kiyim slotiga ('head') tashlamoqchi bo'lsa, tizim buni rad etishi va slotni qizil rangda ogohlantirishi kerak:</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
function canEquip(item, targetSlotType) {
  // Agar xalta sloti bo'lsa - istalgan buyum tushadi
  if (targetSlotType === "backpack") return true;
  // Agar tanadagi slot bo'lsa - turlar 100% mos bo'lishi shart!
  return item.type === targetSlotType;
}
        </div>
      </div>
      <div class="card">
        <h3 data-ru="Автоматическая смена (Swap)" data-en="Automatic Slot Swap">Avtomatik O'rin Almashish (Swap)</h3>
        <p data-ru="Если в слоте Оружия уже был старый топор, а игрок надел меч — топор не исчезает, а автоматически возвращается в освободившийся слот рюкзака!" data-en="If a weapon slot already holds an axe and you drop a sword, the axe isn't deleted — it seamlessly swaps into the freed backpack slot!">Agar qo'lda eski boltacha turgan bo'lsa va uning ustiga yangi qilich qo'yilsa — bolta yo'qolmaydi, balki xaltaning bo'shagan katagiga qaytariladi (Swap mexanizmi)!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: STAT RECALCULATION FORMULA -->
  <section class="slide" data-phase="Matematika|Математика|Math" data-time="37:00–43:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="МАТЕМАТИКА RPG · ПЕРЕСЧЕТ СТАТОВ" data-en="RPG MATHEMATICS · STAT RECALCULATION">RPG MATEMATIKASI · STATLARNI QAYTA HISOBLASH</span></div>
    <h2 data-ru="Формула Баффов: Как Экипировка Усиливает Героя" data-en="Stat Buff Formula: How Gear Amplifies Combat Power">Kuchaytirgichlar Formulasi: Jihozlar Qahramonni Qanday Kuchaytiradi?</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Формула Суммирования Статов" data-en="Stat Aggregation Formula">Statlarni Jamlash Formulasi</h3>
        <div style="font-family:monospace; font-size:14px; color:var(--accent); margin:10px 0; background:#090d16; padding:10px; border-radius:6px;">
          Total_ATK = Base_ATK + Σ(Equipped.atk)<br>
          Total_DEF = Base_DEF + Σ(Equipped.def)<br>
          Total_SPD = Base_SPD + Σ(Equipped.spd)
        </div>
        <p style="font-size:12px;" data-ru="При каждом надевании или снятии предмета вызывается чистая функция recalculateStats():" data-en="Whenever an item is equipped or removed, invoke the pure recalculateStats() helper:">Har safar buyum taqilganda yoki yechilganda toza recalculateStats() funksiyasi ishga tushadi:</p>
      </div>
      <div class="card">
        <div class="code-block" style="font-size:11px; line-height:1.5;">
function recalculateStats() {
  let atk = hero.baseAtk; // 10
  let def = hero.baseDef; // 5
  
  // Barcha faol jihozlar statlarini qo'shamiz
  Object.values(equipped).forEach(item =&gt; {
    if (item &amp;&amp; item.stats) {
      if (item.stats.atk) atk += item.stats.atk;
      if (item.stats.def) def += item.stats.def;
    }
  });

  // UI dagi raqamlarni bir zumda yangilaymiz!
  document.getElementById("statAtk").textContent = atk;
  document.getElementById("statDef").textContent = def;
}
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: ANTI-CHEAT & INTEGRITY -->
  <section class="slide" data-phase="Xavfsizlik|Безопасность|Security" data-time="43:00–48:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="КИБЕРБЕЗОПАСНОСТЬ · ЗАЩИТА ОТ ЧИТЕРОВ" data-en="CYBERSECURITY · ANTI-CHEAT INTEGRITY">KIBERXAVFSIZLIK · CHEAT ENGINE VA XAKERLARDAN HIMOYA</span></div>
    <h2 data-ru="Защита от Читеров: Взлом Инвентаря Через Консоль F12" data-en="Anti-Cheat Defense: Tampering Inventory via F12 Console">Kiber-Himoya: F12 Konsoli Orqali Xaltani Buzish</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Вектор Атаки" data-en="Exploit Vector">Xaker Qanday Buzadi?</div>
        <h3 data-ru="Подмена atk = 999999 в консоли" data-en="Direct Memory Tampering in Console">Konsolda atk = 999999 deb yozish</h3>
        <p data-ru="Любой хитрый игрок может открыть DevTools (F12) и напрямую переписать переменную: hero.baseAtk = 999999 или cyberKatana.stats.atk = 500000. Босс умирает с одного удара." data-en="A clever player opens DevTools (F12) and overrides values: hero.baseAtk = 999999. Bosses die in 1 hit.">Har qanday ayyor o'yinchi F12 konsolini ochib, o'zgaruvchini o'zgartirib qo'yishi mumkin: hero.baseAtk = 999999. Natijada boss bitta urishda qulaydi.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Линия Защиты" data-en="Defense Mechanism">Himoya Qalqoni: Object.freeze()</div>
        <h3 data-ru="Запечатывание Объектов" data-en="Freezing Item Objects">Buyumlarni Muzlatish</h3>
        <p data-ru="Метод Object.freeze() навсегда запрещает изменять свойства предмета в браузере. Попытка читерства выдаст ошибку:" data-en="Object.freeze() permanently locks item properties in memory. Tampering triggers strict errors:">Object.freeze() usuli buyumning xususiyatlarini konsoldan o'zgartirishni butunlay taqiqlab, muzlatib qo'yadi:</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
<span style="color:#22c55e;">// Xavfsiz buyum: xususiyatlarni muzlatish</span>
Object.freeze(cyberKatana.stats);
cyberKatana.stats.atk = 99999; <span style="color:#ef4444;">// XATO: TypeError! Muzlagan!</span>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: INTERACTIVE BLITZ QUIZ -->
  <section class="slide" data-phase="Viktorina|Викторина|Quiz" data-time="48:00–53:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="БЛИЦ-ПРОВЕРКА ЗНАНИЙ · 4 ВОПРОСА" data-en="KNOWLEDGE CHECK · 4 BLITZ QUESTIONS">BLITZ KIBER-TEST · 4 TA TEZKOR SAVOL</span></div>
    <h2 data-ru="Интерактивный Квиз: Проверь Свой Геймдев-Инстинкт" data-en="Interactive Quiz: Test Your Gamedev Instincts">Interaktiv Quiz: Geymdev Sezgisini Sinash</h2>
    <div class="grid-2">
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:var(--accent); color:#fff;">1</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Какое событие нужно отменить через e.preventDefault(), чтобы разрешить Drop?" data-en="Which event requires e.preventDefault() to permit Drop?">Drop tashlashiga ruxsat berish uchun qaysi hodisada e.preventDefault() chaqiriladi?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) dragstart | B) dragover | C) dragend" data-en="A) dragstart | B) dragover | C) dragend">A) dragstart | B) dragover | C) dragend</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: B (dragover по умолчанию блокирует сброс)" data-en="Answer: B (dragover blocks drop by default)">Javob: B (dragover hodisasida to'siq olib tashlanadi)</div>
      </div>
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:#a855f7; color:#fff;">2</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Где передаются данные (ID предмета) между источником и слотом?" data-en="Where is transfer data (item ID) carried during drag?">Drag paytida buyum ma'lumoti (ID) qaysi ob'ekt orqali uzatiladi?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) dataTransfer | B) localStorage | C) console.log" data-en="A) dataTransfer | B) localStorage | C) console.log">A) dataTransfer | B) localStorage | C) console.log</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: A (e.dataTransfer.setData / getData)" data-en="Answer: A (e.dataTransfer.setData / getData)">Javob: A (e.dataTransfer ob'ekti orqali)</div>
      </div>
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:var(--warning); color:#fff;">3</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Дают ли предметы в рюкзаке (Backpack) прибавку к характеристикам?" data-en="Do items lying inside the backpack contribute to active stats?">Xaltada (Backpack) yotgan zaxira buyumlar qahramonning hujum kuchini oshiradimi?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) Да, всегда | B) Нет, только когда надеты в слот экипировки" data-en="A) Yes | B) No, strictly when equipped in active slot">A) Ha, doim | B) Yo'q, faqat tanaga (Equipped slotiga) taqilgandagina</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: B (Только экипированные предметы дают бафф)" data-en="Answer: B (Only equipped items yield buffs)">Javob: B (Faqat taqilgan faol buyumlar kuch qo'shadi)</div>
      </div>
      <div class="card" style="padding:14px;">
        <span class="badge" style="background:var(--danger); color:#fff;">4</span>
        <strong style="font-size:12px; display:block; margin:6px 0;" data-ru="Какой метод JS защищает статы предмета от читерского изменения в F12?" data-en="Which JS method freezes item stats preventing console cheats?">Qaysi JS metodi buyum statlarini F12 konsolida o'zgartirishdan muzlatadi?</strong>
        <p style="font-size:11px; color:var(--ink-secondary);" data-ru="A) Object.freeze() | B) JSON.parse() | C) Math.random()" data-en="A) Object.freeze() | B) JSON.parse() | C) Math.random()">A) Object.freeze() | B) JSON.parse() | C) Math.random()</p>
        <div style="margin-top:6px; font-weight:700; color:var(--success); font-size:11px;" data-ru="Ответ: A (Запечатывает свойства объекта от записи)" data-en="Answer: A (Seals object properties against mutation)">Javob: A (Object.freeze() xususiyatlarni qulflaydi)</div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: LOCALSTORAGE PERSISTENCE -->
  <section class="slide" data-phase="Doimiylik|Память|Storage" data-time="53:00–58:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="СОХРАНЕНИЕ ПРОГРЕССА · LOCALSTORAGE" data-en="DATA PERSISTENCE · LOCALSTORAGE">XOTIRA VA SAQLASH · LOCALSTORAGE INTEGRATSIYASI</span></div>
    <h2 data-ru="Сохранение Лута: Как Не Потерять Меч При Перезагрузке" data-en="Loot Persistence: Saving Your Swords Across Reloads">O'ljani Saqlash: Sahifa Yangilanganda Buyumlar Yo'qolmasligi</h2>
    <div class="grid-2">
      <div class="card">
        <h3 data-ru="Сериализация инвентаря в JSON" data-en="JSON Serialization">Inventarni JSON Qilish</h3>
        <p data-ru="При каждом изменении слотов сохраняем массив экипировки в постоянную память браузера:" data-en="On any slot update, serialize the equipped state into browser LocalStorage:">Har safar buyum joyi o'zgarganda xotirani brauzer LocalStorage-ga avtomatik yozib qo'yamiz:</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
function saveInventory() {
  const data = JSON.stringify({ backpack, equipped });
  localStorage.setItem("hero_inventory", data);
}
        </div>
      </div>
      <div class="card">
        <h3 data-ru="Загрузка при старте игры" data-en="Boot Initialization">O'yin Boshlanganda Tiklash</h3>
        <p data-ru="При открытии страницы считываем JSON, восстанавливаем слоты и сразу пересчитываем статы:" data-en="On page load, parse JSON string and recompute combat stats immediately:">Sahifa ochilishi bilanoq JSON ni o'qib, slotlarga buyumlarni joylaymiz va statlarni hisoblaymiz:</p>
        <div class="code-block" style="margin-top:10px; font-size:11px;">
function loadInventory() {
  const raw = localStorage.getItem("hero_inventory");
  if (raw) {
    const parsed = JSON.parse(raw);
    backpack = parsed.backpack;
    equipped = parsed.equipped;
    recalculateStats();
  }
}
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: HANDS-ON LAB INTRODUCTION -->
  <section class="slide" data-phase="Amaliyot|Практика|Practice" data-time="58:00–68:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКАЯ АРЕНА · RPG INVENTORY STUDIO" data-en="HANDS-ON LAB · RPG INVENTORY STUDIO">AMALIY ARENA · RPG INVENTORY STUDIO</span></div>
    <h2 data-ru="Лаборатория: Сборка и Экипировка Кибер-Рыцаря" data-en="Hands-on Lab: Gearing Up the Cyber Knight">Laboratoriya: Kiber-Ritsarni Jihozlash va Jangovar Stats</h2>
    <div class="hero-split">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Сценарий Миссии" data-en="Mission Scenario">Kiber-Topshiriq</div>
        <h3 data-ru="Экипировка Перед Битвой с Боссом" data-en="Gearing Before the Boss">Boss Jangi Oldidan Tayyorgarlik</h3>
        <p data-ru="В вашем рюкзаке лежат 4 предмета: Кинжал (+5 ATK), Кiber-Katana (+35 ATK), Эгида (+40 DEF) и Зелье. Ваша задача — правильно экипировать их в слоты тела, поднять атаку выше 40 и активировать защиту от читов Object.freeze." data-en="Your backpack holds 4 items: Dagger (+5 ATK), Cyber Katana (+35 ATK), Aegis (+40 DEF), and Potion. Equip them to boost Attack above 40 and freeze stats.">Xaltangizda 4 ta buyum bor. Ularni to'g'ri slotlarga Drag-and-Drop orqali kiygizib, qahramon hujum kuchini 40 dan oshirishingiz va Object.freeze himoyasini yoqishingiz kerak.</p>
        <div class="box" style="margin-top:12px;">
          <strong data-ru="Шаги в симуляторе:" data-en="Simulator Steps:">Amallar ketma-ketligi:</strong>
          <ul style="font-size:12px; line-height:1.6; margin-top:4px;">
            <li data-ru="1. Перетащить Katana в слот Weapon ➔ ATK вырастет до 45." data-en="1. Drag Katana into Weapon slot ➔ ATK leaps to 45.">1. Katana ni Weapon slotiga tortish ➔ ATK 45 ga yetadi.</li>
            <li data-ru="2. Перетащить Aegis в слот Shield ➔ DEF вырастет до 45." data-en="2. Drag Aegis into Shield slot ➔ DEF leaps to 45.">2. Aegis ni Shield slotiga tortish ➔ DEF 45 ga chiqadi.</li>
            <li data-ru="3. Нажать 'Muzlatish (Anti-Cheat)' va saqlash." data-en="3. Click 'Freeze Stats' and save to storage.">3. 'Muzlatish (Anti-Cheat)' tugmasini bosib saqlash.</li>
          </ul>
        </div>
      </div>
      <div class="card" style="display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:rgba(15,23,42,0.6);">
        <div style="font-size:42px; margin-bottom:10px;">🎒 ⚔️ 🛡️ 💎</div>
        <h3 data-ru="Запуск Инвентарь Студии" data-en="Launch Inventory Studio">RPG Inventory Studio</h3>
        <p style="font-size:13px; max-width:320px; color:var(--ink-secondary);" data-ru="Откройте simulator/index.html для интерактивной работы со слотами и перетаскиванием." data-en="Open simulator/index.html for interactive slot drag-and-drop gameplay.">Interaktiv Drag-and-Drop xalta tizimini sinash uchun studiyani oching.</p>
        <a href="simulator/index.html" target="_blank" style="display:inline-block; margin-top:14px; padding:10px 20px; border-radius:10px; background:var(--accent); color:#fff; text-decoration:none; font-weight:700; font-size:13px;" data-ru="🚀 Открыть Студию" data-en="🚀 Launch Studio">🚀 Studiyani Ochish</a>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: PEER-REVIEW & BUILD DUEL -->
  <section class="slide" data-phase="Taqdimot|Баттл|Duel" data-time="68:00–74:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМНАЯ ПРОВЕРКА · ДУЭЛЬ СТАВОВ" data-en="PEER PLAYTEST · STAT BUILD DUEL">JUFTLIKDA PLAYTEST · STATLAR DUELI</span></div>
    <h2 data-ru="Баттл Билдов: Сравни Силу Своего Рыцаря с Соседом" data-en="Build Duel: Compare Your Knight's Power with Teammate">Statlar Duela: Partadoshingiz Bilan Qahramon Kuchini Solishtiring</h2>
    <div class="grid-2">
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Чек-лист Тестера" data-en="Tester Checklist">Sifat Nazorati (Checklist)</div>
        <ul style="font-size:12px; line-height:1.7; margin-top:8px;">
          <li data-ru="[ ] Работает ли перетаскивание предметов между слотами?" data-en="[ ] Does drag-and-drop work cleanly between slots?">[ ] Buyumlar slotlar orasida bexato surilmoqdami?</li>
          <li data-ru="[ ] Блокируется ли попытка надеть меч в слот шлема?" data-en="[ ] Is equipping a sword into a helmet slot blocked?">[ ] Qilichni bosh kiyim slotiga qo'yish taqiqlanganmi?</li>
          <li data-ru="[ ] Пересчитываются ли статы ATK и DEF мгновенно?" data-en="[ ] Do ATK & DEF stats recalculate instantly?">[ ] ATK va DEF statlari real-vaqtda o'zgarmoqdami?</li>
          <li data-ru="[ ] Сохраняются ли надежные вещи после F5 (Refresh)?" data-en="[ ] Do equipped items persist after F5 page refresh?">[ ] F5 bosilganda kiyilgan buyumlar joyida qoladimi?</li>
        </ul>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Демо на Смартборде" data-en="Smartboard Demo">Smartboard Demosi</div>
        <h3 data-ru="Показ Легендарного Билда" data-en="Legendary Build Showcase">Afsonaviy Qahramon Taqdimoti</h3>
        <p data-ru="Два ученика с самым высоким боевым рейтингом (Combat Rating) выводят свой экран на смартборд и демонстрируют свой билд с защитой от читов." data-en="Two students boasting highest Combat Rating project their inventory setups live on the smartboard.">Eng yuqori jangovar reytingga erishgan 2 nafar o'quvchi o'z kiber-ritsarining inventarini katta doskaga chiqaradi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 13: ADVANCED ITEM EFFECTS -->
  <section class="slide" data-phase="Kengaytirish|Эффекты|Effects" data-time="74:00–77:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ПРОДВИНУТЫЙ УРОВЕНЬ · СЕТОВЫЕ БОНУСЫ" data-en="ADVANCED CONCEPT · SET BONUSES">MURAKKAB TIZIM · TO'PLAM (SET) BONUSLARI</span></div>
    <h2 data-ru="Сет-Бонусы: Надень Весь Комплект и Получи +100%!" data-en="Set Bonuses: Full Armor Sets Granting +100% Buffs!">Set Bonusi: Butun To'plamni Kiy va 2x Kuchga Ega Bo'l!</h2>
    <div class="card">
      <div class="code-block" style="font-size:12px; line-height:1.7;">
<span style="color:#64748b;">// Agar qahramon 2 ta Kiber-buyumni bir vaqtda kiysa:</span>
if (equipped.weapon?.set === "cyber" &amp;&amp; equipped.shield?.set === "cyber") {
  totalAtk *= 1.5; <span style="color:#22c55e;">// +50% Hujum bonusi!</span>
  showBanner("🔥 CYBER SET BONUS ACTIVATED!");
}
      </div>
      <p style="font-size:12px; margin-top:8px; color:var(--ink-secondary);" data-ru="Именно так работают MMORPG вроде World of Warcraft и Genshin Impact: комбинации экипировки заставляют игрока продумывать стратегию." data-en="This is the exact game design logic powering WoW and Genshin Impact: set synergies reward tactical planning.">Genshin Impact va World of Warcraft kabi katta o'yinlar aynan shunday mantiqda ishlaydi: buyumlarning uyg'unligi o'yinchini strategik fikrlashga o'rgatadi.</p>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & 3-TIER HOMEWORK -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="77:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ УРОКА И ДОМАШНЕЕ ЗАДАНИЕ · 10 БАЛЛОВ" data-en="SUMMARY & 3-TIER HOMEWORK · 10 POINTS">XULOSA VA 3 DARAJALI UY VAZIFASI · 10 BALL</span></div>
    <h2 data-ru="Итоги Урока и Домашнее Задание" data-en="Lesson Summary & Homework">Xulosa va 3 Darajali Uy Vazifasi</h2>
    <div class="grid-3">
      <div class="card">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);" data-ru="Уровень 1: База (4 балла)" data-en="Tier 1: Core (4 pts)">1-Daraja: Baza (4 ball)</div>
        <h3 data-ru="Сетка и Drag & Drop" data-en="Grid & Drag & Drop">Slotlar va Drag-Drop</h3>
        <p data-ru="Создать HTML-сетку рюкзака 3×3 и реализовать события ondragstart, ondragover и ondrop для перемещения предметов." data-en="Build 3×3 backpack HTML grid and wire up ondragstart, ondragover, and ondrop events.">3×3 o'lchamdagi xalta slotlarini yasash va buyumlarni surish uchun ondragstart, ondragover, ondrop hodisalarini ulash.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(34,197,94,0.15); color:var(--success);" data-ru="Уровень 2: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</div>
        <h3 data-ru="Пересчет Статов и Слот Weapon" data-en="Stat Math & Weapon Slot">Statlar va Qurol Sloti</h3>
        <p data-ru="Сделать слот Weapon: при надевании меча увеличивать ATK героя, а при снятии — корректно уменьшать." data-en="Implement Weapon slot: bumping hero ATK upon equipping sword, and deducting stats on unequip.">Alohida Qurol slotini qilish: qilich taqilganda ATK oshishi, yechib olinganda esa avvalgi holatga qaytishi kerak.</p>
      </div>
      <div class="card">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--danger);" data-ru="Уровень 3: Челлендж (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</div>
        <h3 data-ru="Защита Object.freeze()" data-en="Object.freeze Security">Anti-Cheat Himoyasi</h3>
        <p data-ru="Применить Object.freeze() к статам всех артефактов и настроить авто-сохранение инвентаря в LocalStorage." data-en="Apply Object.freeze() to lock artifact stats against F12 tampering and auto-save state to LocalStorage.">Barcha buyumlarga Object.freeze() qo'yib konsoldan buzishni to'sish va LocalStorage orqali avto-saqlashni sozlash.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px; text-align:center;">
      <p style="font-size:13px;" data-ru="💡 Практическое домашнее задание доступно в файле vazifa.html с авто-проверкой и сохранением в LocalStorage." data-en="💡 Interactive homework is bundled in vazifa.html with instant client-side testing and LocalStorage persistence.">💡 Interaktiv uy vazifasi <a href="vazifa.html" style="color:var(--accent); font-weight:700;">vazifa.html</a> faylida joylashgan bo'lib, avtomatik testlar va LocalStorage saqlash tizimiga ega.</p>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. TEACHER NOTES JSON (Triplets: [title, say, do])
# -----------------------------------------------------------------------------
NOTES_DATA = {
  "uz": [
    ["Kirish va Maqsad", "Bugun professional RPG o'yinlarining asosi bo'lgan Drag-and-Drop inventar tizimini yaratamiz. Qilich va qalqonlarni taqib, qahramon kuchini hisoblaymiz.", "Doskaga mavzuni yozing va slaydni oching."],
    ["Uy Vazifasi Tahlili", "O'tgan 34-darsda BFS qidiruvida visited to'plamini unutish brauzerni qotirib qo'ygan edi. Oltin standart bo'lgan Set() tekshiruvini eslatamiz.", "O'quvchilardan blitz savolga javob oling."],
    ["Inventar Arxitekturasi", "Xalta (Backpack) va Jihozlar (Equipped) farqini tushuntiring. Xaltada turgan narsa kuch bermaydi, faqat taqilgandagina ishlaydi.", "Doskada tana va xalta slotlarini taqqoslang."],
    ["Buyum Modeli", "Har bir buyum JSON ob'ekti: id, name, type, icon, rarity va stats (atk, def, spd). Rarity ranglarini ko'rsating.", "Slayddagi kod namunasini tahlil qiling."],
    ["HTML5 Drag & Drop", "3 ta asosiy hodisa: ondragstart (ko'tarish), ondragover (ruxsat berish) va ondrop (slotga tashlash). dataTransfer rolini tushuntiring.", "3 bosqichli voqealar zanjirini doskaga yozing."],
    ["Slotlar Validatsiyasi", "Qilichni bosh kiyim slotiga kiyib bo'lmaydi! Har bir slot o'z turiga mos buyumni tekshirishi shart. Swap mexanizmini ko'rsating.", "Noto'g'ri kiyish holatlarini muhokama qiling."],
    ["Statlar Matematikasi", "Qahramon umumiy kuchi = Baza kuchi + barcha taqilgan buyumlar yig'indisi. recalculateStats funksiyasi formulasini tushuntiring.", "Formulani doskada birgalikda hisoblang."],
    ["Kiberxavfsizlik", "O'yinchilar F12 konsolidan atk = 999999 deb yozishlari mumkin. Bunga qarshi Object.freeze() himoya qalqonini qo'llaymiz.", "Konsol orqali aldash xavfini tushuntiring."],
    ["Interaktiv Quiz", "4 ta geymdev savoli orqali tushunchalarni mustahkamlaymiz. O'quvchilardan tezkor javoblar oling.", "To'g'ri javoblarni ochib, tushuntiring."],
    ["LocalStorage Xotirasi", "Sahifa yangilanganda kiyilgan qilich yo'qolib qolmasligi uchun JSON.stringify orqali LocalStorage ga saqlaymiz.", "LocalStorage buyruqlarini ko'rsating."],
    ["Amaliy Topshiriq", "Endi simulyatorda qahramonni jihozlab, hujum kuchini 40 dan oshiramiz va Object.freeze himoyasini yoqamiz.", "O'quvchilarni simulator/index.html ga yo'naltiring."],
    ["Juftlikda Duel", "Partadoshlar bir-birining qahramon statlarini va Drag-and-Drop ishlashini tekshirib chiqishadi.", "Sinf bo'ylab eng kuchli kiber-ritsarlarni aniqlang."],
    ["Set Bonusi", "Bir xil to'plamdagi 2 ta buyum kiyilsa qo'shimcha +50% kuch berilishi mumkin (WoW va Genshin Impact kabi).", "Geym-dizayn qoidalarini umumlashtiring."],
    ["Xulosa va Uy Vazifasi", "Bugun to'liq ishlaydigan RPG inventar tizimini yaratdik. 3 darajali topshiriq vazifa.html da mavjud, 10 ballik mezonni bajaring.", "Uy vazifasi talablarini eslatib, darsni yakunlang."]
  ],
  "ru": [
    ["Введение и Цель", "Сегодня мы создаем полноценную систему инвентаря RPG на HTML5 Drag-and-Drop: перетаскивание предметов, баффы статов и защита от читеров.", "Запишите тему на доске и откройте первый слайд."],
    ["Разбор Домашнего Задания", "Главная ошибка 34-го урока — забытый visited в BFS, приводивший к зависанию браузера. Разбираем проверку через Set().", "Примите ответы на блиц-вопрос."],
    ["Архитектура Инвентаря", "Разделяем рюкзак (Backpack) и тело (Equipped). Предметы в рюкзаке не дают бонусов, пока не надеты в слот тела.", "Изобразите схему слотов на доске."],
    ["Модель Предмета", "Каждый предмет — это объект: id, name, type, icon, rarity и stats (atk, def, spd). Цветовая дифференциация редкости.", "Разберите структуру JSON предмета."],
    ["HTML5 Drag & Drop", "3 ключевых события: ondragstart (захват), ondragover (разрешение сброса) и ondrop (сброс в слот). Объект dataTransfer.", "Поясните последовательность событий."],
    ["Валидация Слотов", "Нельзя надеть меч в слот шлема! Проверка type === slotType и логика авто-замены (Swap) старого предмета.", "Разберите функцию проверки слота."],
    ["Математика Статов", "Итоговая сила = Базовые статы + сумма статов всех надетых предметов. Функция recalculateStats().", "Вычислите урон героя вместе с классом."],
    ["Кибербезопасность", "Защита от читерства через DevTools F12: запечатывание характеристик предметов через Object.freeze().", "Продемонстрируйте защиту от взлома."],
    ["Интерактивный Квиз", "Закрепляем механику инвентаря с помощью 4 геймдев-вопросов.", "Обсудите ответы и похвалите активных."],
    ["Память LocalStorage", "Сохранение экипировки между сессиями через JSON.stringify и восстановление при старте.", "Поясните работу браузерного хранилища."],
    ["Практическая Арена", "В симуляторе ученики надевают меч и щит, поднимают атаку выше 40 и включают защиту Object.freeze.", "Контролируйте работу в simulator/index.html."],
    ["Парная Дуэль", "Напарники тестируют инвентари друг друга и сравнивают боевой рейтинг рыцарей.", "Отметьте лучших геймдев-инженеров."],
    ["Сет-Бонусы", "Комплектные бонусы при ношении 2 предметов одной серии (как в Genshin Impact и WoW).", "Поясните синергию экипировки."],
    ["Итоги и Задание", "Мы построили рабочий движок инвентаря. Домашнее задание на 10 баллов готово в vazifa.html.", "Напомните дедлайн и завершите урок."]
  ],
  "en": [
    ["Intro & Mission", "Today we build a production-grade RPG inventory engine using HTML5 Drag-and-Drop: gear sockets, combat buffs, and anti-cheat defenses.", "Write topic on board and project slide 1."],
    ["Homework Review", "The major bug in lesson 34 was forgetting the visited set in BFS. Reviewing O(1) Set lookups.", "Collect answers to the blitz question."],
    ["Inventory Architecture", "Distinguish Backpack storage from Equipped sockets. Stashed items grant zero combat stat buffs until equipped.", "Diagram backpack vs paperdoll sockets."],
    ["Item Data Model", "Every artifact is a structured object: id, name, type, icon, rarity, and stats (atk, def, spd). Rarity color coding.", "Inspect the item JSON snippet."],
    ["HTML5 Drag & Drop", "The 3 vital events: ondragstart (drag initiation), ondragover (drop permission), and ondrop (socket reception).", "Walk through event lifecycles on the board."],
    ["Slot Validation", "Swords cannot be equipped as helmets! Strict type matching and seamless slot swapping logic.", "Review type validation helpers."],
    ["Stat Calculation Math", "Total power = Base Stats + Sum of all equipped stat modifiers. The recalculateStats() loop.", "Calculate combat ratings with the room."],
    ["Cybersecurity & Anti-Cheat", "Neutralizing console tampering (F12) using Object.freeze() to lock item stat properties in memory.", "Demonstrate memory freezing mechanics."],
    ["Interactive Quiz", "Reinforce inventory mechanics with 4 rapid gamedev questions.", "Reveal correct answers and explain."],
    ["LocalStorage Persistence", "Persisting inventory layouts across page reloads using JSON.stringify & parse.", "Explain storage serialization."],
    ["Hands-on Lab", "In the simulator, students gear up their cyber knight, exceed 40 ATK, and freeze stats.", "Guide students in simulator/index.html."],
    ["Peer Stat Duel", "Partners playtest each other's drag-and-drop systems and compare hero combat ratings.", "Highlight top cyber builds in class."],
    ["Set Bonuses", "Full equipment synergies granting +50% multipliers (like WoW and Genshin Impact).", "Discuss strategic game design."],
    ["Summary & Homework", "We engineered a complete RPG inventory engine. The 3-tier homework is ready in vazifa.html for 10 total points.", "Summarize key rules and conclude."]
  ]
}

def build_presentation():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Taqdimot shabloni — Target Maktabi</title>", "<title>7-8-sinf: Inventar Tizimi va Drag-Drop</title>")
    tpl = re.sub(r'name="total-slides"\s+content="\d+"', 'name="total-slides" content="14"', tpl)
    tpl = re.sub(r'id="totalSlides">0</span>', 'id="totalSlides">14</span>', tpl)

    stage_regex = r'<div class="stage">[\s\S]*?</div><!-- /stage -->'
    new_stage = f'<div class="stage">\n{SLIDES_HTML}\n</div><!-- /stage -->'
    tpl = re.sub(stage_regex, lambda m: new_stage, tpl)

    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    notes_regex = r'var NOTES\s*=\s*\{[\s\S]*?\};'
    tpl = re.sub(notes_regex, lambda m: f'var NOTES = {notes_json};', tpl)

    out_path = os.path.join(DEST_DIR, "prezentatsiya.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

def build_worksheet():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Amaliy Ish Varaqasi — Target Maktabi</title>", "<title>Ish Varaqasi: Inventar Tizimi va Drag-Drop — 7-8-sinf</title>")
    tpl = tpl.replace("1-AMALIY ISH VARAQASI", "35-AMALIY ISH VARAQASI")
    tpl = tpl.replace("Mavzu: Kirish va Vibecoding asoslari", "Mavzu: Inventar va Buyumlar Tizimi: Drag-and-Drop, Artefaktlar va Qahramon Stats")

    worksheet_body = """
  <div class="mission-box">
    <div class="mission-title" data-ru="МИССИЯ УРОКА: ИНЖЕНЕРИЯ RPG ИНВЕНТАРЯ" data-en="LESSON MISSION: RPG INVENTORY SYSTEM">DARSNING KIBER-MISSIYASI: RPG INVENTAR TIZIMI</div>
    <p style="font-size:12px; margin-top:4px;" data-ru="Освоить HTML5 Drag-and-Drop API, запрограммировать сетку рюкзака 4×4 и слоты экипировки, рассчитать суммарные статы атаки/защиты и защитить данные от консольного читерства через Object.freeze." data-en="Master HTML5 Drag-and-Drop API, engineer 4×4 backpack grids and equipment sockets, compute aggregated ATK/DEF stats, and secure inventory against F12 cheats via Object.freeze.">HTML5 Drag-and-Drop API ni o'rganish, 4×4 xalta slotlari va jihozlash maydonlarini dasturlash, qahramonning umumiy hujum/himoya kuchini hisoblash va Object.freeze yordamida konsoldan buzishni to'sish.</p>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">1</span>
      <h3 data-ru="События Drag-and-Drop API (2 балла)" data-en="Drag-and-Drop Event Lifecycle (2 pts)">Drag-and-Drop API Hodisalari Zanjiri (2 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Соедините событие с его технической ролью в браузере:" data-en="Match each Drag & Drop event with its browser behavior:">Hodisani uning brauzerdagi vazifasi bilan tutashtiring:</p>
    <table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:11px;">
      <thead>
        <tr style="background:var(--card-bg, #f1f5f9);">
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Событие" data-en="Event">Hodisa</th>
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Где срабатывает?" data-en="Target">Qayerda ishlaydi?</th>
          <th style="border:1px solid #cbd5e1; padding:6px;" data-ru="Обязательное действие" data-en="Mandatory Action">Majburiy amal</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<code>ondragstart</code>" data-en="<code>ondragstart</code>"><code>ondragstart</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="На предмете" data-en="On item">Ko'chirilayotgan buyumda</td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Записать e.dataTransfer.setData()" data-en="Call e.dataTransfer.setData()">________________________</td>
        </tr>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<code>ondragover</code>" data-en="<code>ondragover</code>"><code>ondragover</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="На слоте" data-en="On slot">Maqsadli slotda</td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Вызвать e.preventDefault()" data-en="Call e.preventDefault()">________________________</td>
        </tr>
        <tr>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="<code>ondrop</code>" data-en="<code>ondrop</code>"><code>ondrop</code></td>
          <td style="border:1px solid #cbd5e1; padding:6px;" data-ru="На слоте" data-en="On slot">Qabul qiluvchi slotda</td>
          <td style="border:1px solid #cbd5e1; padding:6px; color:#64748b;" data-ru="Прочитать ID и пересчитать статы" data-en="Read ID & recalculate stats">________________________</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">2</span>
      <h3 data-ru="Математика Боевых Статов Героя (3 балла)" data-en="Combat Stat Math Calculation (3 pts)">Jangovar Statlar Matematikasi (3 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Базовые характеристики Рыцаря: Base_ATK = 15, Base_DEF = 10, Base_SPD = 20. Игрок экипировал 3 предмета:" data-en="Knight base stats: Base_ATK = 15, Base_DEF = 10, Base_SPD = 20. Player equips 3 artifacts:">Ritsarning boshlang'ich statlari: Base_ATK = 15, Base_DEF = 10, Base_SPD = 20. O'yinchi 3 ta buyumni kiydi:</p>
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:10px; margin-top:8px; font-family:monospace; font-size:11px;">
      1) Qilich (Katana): { atk: +35, spd: +5 }<br>
      2) Qalqon (Aegis): { def: +40, spd: -3 }<br>
      3) Bosh kiyim (Kask): { def: +15, hp: +50 }<br>
      <span style="color:#3b82f6;">// Qahramonning umumiy ko'rsatkichlarini hisoblang:</span><br>
      Jami ATK = 15 + _____ = _____<br>
      Jami DEF = 10 + _____ + _____ = _____<br>
      Jami SPD = 20 + _____ - _____ = _____
    </div>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">3</span>
      <h3 data-ru="Кибербезопасность: Защита от F12 Читеров (3 балла)" data-en="Cybersecurity: F12 Anti-Cheat Protection (3 pts)">Kiberxavfsizlik: F12 Cheatlaridan Himoyalanish (3 ball)</h3>
    </div>
    <p style="font-size:12px;" data-ru="Объясните, почему метод Object.freeze() важен в браузерных играх и что произойдет, если читер попытается изменить замороженный объект в консоли:" data-en="Explain why Object.freeze() is vital in web games and what happens if a cheater mutates frozen objects in F12:">Nega brauzer o'yinlarida Object.freeze() muhim va xaker konsolda muzlatilgan ob'ektni o'zgartirmoqchi bo'lsa nima sodir bo'ladi?</p>
    <div style="margin-top:6px; font-size:12px; line-height:1.8;">
      Tushuntirish: ____________________________________________________________________<br>
      Natija: ____________________________________________________________________
    </div>
  </div>

  <div class="task-card">
    <div class="task-header">
      <span class="task-num">4</span>
      <h3 data-ru="Критерии Оценки и Рефлексия (2 балла)" data-en="Evaluation Rubric & Reflection (2 pts)">Baholash Mezoni va Xulosa (2 ball)</h3>
    </div>
    <div style="display:flex; justify-content:space-between; font-size:11px; margin-top:6px;">
      <span>[ ] 1-Daraja: Drag-Drop Slotlar (4 ball)</span>
      <span>[ ] 2-Daraja: Stat Buffs & Weapon (4 ball)</span>
      <span>[ ] 3-Daraja: Object.freeze (2 ball)</span>
    </div>
  </div>
"""
    tpl = re.sub(r'<!-- PAGE 1:[\s\S]*?(?=\n<script>)', lambda m: f'<div class="sheet">\n{worksheet_body}\n</div>', tpl)

    out_path = os.path.join(DEST_DIR, "varaqa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: varaqa.html")

def build_homework():
    tpl_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("<title>Vazifa Shabloni — Target Maktabi</title>", "<title>Uy Vazifasi: Inventar Tizimi va Drag-Drop — 7-8-sinf</title>")
    tpl = tpl.replace("1-AMALIY VAZIFA", "35-AMALIY VAZIFA")
    tpl = tpl.replace("Mavzu: Kirish va Vibecoding Asoslari", "Mavzu: Inventar va Buyumlar Tizimi: Drag-and-Drop, Artefaktlar va Qahramon Stats")

    hw_body = """
  <div class="hw-card">
    <div class="hw-header">
      <span class="badge" style="background:var(--accent); color:#fff;" data-ru="Уровень 1: База (4 балла)" data-en="Tier 1: Core (4 pts)">1-Daraja: Baza (4 ball)</span>
      <h3 data-ru="События Drag-and-Drop в JS" data-en="Drag-and-Drop JS Events">Drag-and-Drop Hodisalari Kodi</h3>
    </div>
    <p style="font-size:13px;" data-ru="Напишите функцию allowDrop(e) и dropItem(e), разрешающую сброс предмета в слот:" data-en="Code allowDrop(e) and dropItem(e) permitting item drops into slots:">Slotga buyum tashlashga ruxsat beruvchi va ID-ni o'quvchi funksiyalarni yozing:</p>
    <div class="code-area">
      <textarea id="codeTier1" rows="8" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="function allowDrop(e) { ... }" data-placeholder-en="function allowDrop(e) { ... }">
function allowDrop(e) {
    e.preventDefault(); // Ruxsat berish
}

function dropItem(e) {
    e.preventDefault();
    const itemId = e.dataTransfer.getData("text/plain");
    return itemId;
}
</textarea>
    </div>
    <button onclick="testTier1()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--accent); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить события" data-en="Verify Events">Tekshirish</button>
    <span id="resTier1" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <div class="hw-card" style="margin-top:16px;">
    <div class="hw-header">
      <span class="badge" style="background:var(--success); color:#fff;" data-ru="Уровень 2: Инженерия (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Muhandislik (4 ball)</span>
      <h3 data-ru="Функция Пересчета Статов (recalculateStats)" data-en="Stat Recalculation Engine">Statlarni Qayta Hisoblash Funksiyasi</h3>
    </div>
    <p style="font-size:13px;" data-ru="Напишите функцию recalculateStats(baseAtk, equippedList), которая суммирует атаку героя со всеми надетыми предметами:" data-en="Write recalculateStats(baseAtk, equippedList) summing hero base attack with all equipped modifiers:">Baza hujum kuchiga barcha kiyilgan buyumlar stats.atk qiymatini qo'shib jami hujum kuchini qaytaruvchi funksiya yozing:</p>
    <div class="code-area">
      <textarea id="codeTier2" rows="8" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="function recalculateStats(baseAtk, equipped) { ... }" data-placeholder-en="function recalculateStats(baseAtk, equipped) { ... }">
function recalculateStats(baseAtk, equippedList) {
    let totalAtk = baseAtk;
    for (let item of equippedList) {
        if (item && item.stats && item.stats.atk) {
            totalAtk += item.stats.atk;
        }
    }
    return totalAtk;
}
</textarea>
    </div>
    <button onclick="testTier2()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--success); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить расчет" data-en="Test Math">Hisobni Sinash</button>
    <span id="resTier2" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <div class="hw-card" style="margin-top:16px;">
    <div class="hw-header">
      <span class="badge" style="background:var(--danger); color:#fff;" data-ru="Уровень 3: Челлендж (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</span>
      <h3 data-ru="Защита от Читеров: Object.freeze" data-en="Object.freeze Security Guard">Muzlatish va Anti-Cheat Qalqoni</h3>
    </div>
    <p style="font-size:13px;" data-ru="Реализуйте функцию secureItem(item), которая замораживает объект предмета и его вложенный объект stats с помощью Object.freeze():" data-en="Implement secureItem(item) deeply freezing the item and its nested stats object via Object.freeze():">Buyum va uning ichidagi stats ob'ektini Object.freeze yordamida konsoldan o'zgartirishdan to'liq muzlatuvchi funksiya yozing:</p>
    <div class="code-area">
      <textarea id="codeTier3" rows="7" style="width:100%; font-family:monospace; font-size:12px; padding:10px; border-radius:6px; border:1px solid #cbd5e1;" data-placeholder-ru="function secureItem(item) { ... }" data-placeholder-en="function secureItem(item) { ... }">
function secureItem(item) {
    if (item && item.stats) {
        Object.freeze(item.stats);
    }
    return Object.freeze(item);
}
</textarea>
    </div>
    <button onclick="testTier3()" class="btn" style="margin-top:8px; padding:6px 14px; background:var(--danger); color:#fff; border:none; border-radius:6px; cursor:pointer;" data-ru="Проверить защиту" data-en="Test Anti-Cheat">Qalqonni Sinash</button>
    <span id="resTier3" style="margin-left:10px; font-weight:700;"></span>
  </div>

  <script>
    function testTier1() {
      var txt = document.getElementById('codeTier1').value;
      var res = document.getElementById('resTier1');
      if (txt.includes('preventDefault()') && txt.includes('dataTransfer.getData')) {
        res.textContent = "✅ To'g'ri! Drag & Drop hodisalari xatosiz ulandi (+4 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: e.preventDefault() va dataTransfer.getData dan foydalaning!";
        res.style.color = "var(--danger)";
      }
    }

    function testTier2() {
      var txt = document.getElementById('codeTier2').value;
      var res = document.getElementById('resTier2');
      if (txt.includes('totalAtk') && (txt.includes('stats.atk') || txt.includes('atk')) && txt.includes('return')) {
        res.textContent = "✅ Ajoyib! Qahramon hujum kuchi aniq jamlandi (+4 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: baza hujumiga har bir buyumning stats.atk qiymatini qo'shing!";
        res.style.color = "var(--danger)";
      }
    }

    function testTier3() {
      var txt = document.getElementById('codeTier3').value;
      var res = document.getElementById('resTier3');
      if (txt.includes('Object.freeze') && txt.includes('stats')) {
        res.textContent = "✅ Mukammal! Buyum va statlar xakerlikdan to'liq muzlatildi (+2 ball)";
        res.style.color = "var(--success)";
      } else {
        res.textContent = "❌ Xatolik: Object.freeze(item.stats) va Object.freeze(item) ni qo'llang!";
        res.style.color = "var(--danger)";
      }
    }
  </script>
"""
    tpl = re.sub(r'<main class="container">[\s\S]*?</main>', lambda m: f'<main class="container">\n{hw_body}\n</main>', tpl)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    doc = """# O'qituvchi Qo'llanmasi (Teacher Reading)
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
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("  ✓ Created: TEACHER_READING.md")

def build_simulator():
    html = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="RPG Инвентарь Студия: Drag & Drop и Статы" data-en="RPG Inventory Studio: Drag & Drop & Stats">RPG Inventar Studiyasi: Drag & Drop va Statlar</title>
  <style>
    :root {
      --bg: #0b0f19;
      --panel: #111827;
      --card: #1f2937;
      --border: #374151;
      --ink: #f9fafb;
      --ink-dim: #9ca3af;
      --accent: #3b82f6;
      --success: #22c55e;
      --danger: #ef4444;
      --warning: #eab308;
      --legendary: #facc15;
      --epic: #a855f7;
      --rare: #38bdf8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace;
      background: var(--bg);
      color: var(--ink);
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    header {
      background: var(--panel);
      border-bottom: 1px solid var(--border);
      padding: 10px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .badge-sub {
      background: rgba(59,130,246,0.2);
      color: var(--accent);
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 11px;
      font-weight: 700;
    }
    .main-grid {
      flex: 1;
      display: grid;
      grid-template-columns: 300px 1fr 300px;
      overflow: hidden;
    }
    /* Hero Paperdoll Pane */
    .hero-pane {
      background: var(--panel);
      border-right: 1px solid var(--border);
      padding: 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .hero-avatar {
      font-size: 56px;
      margin: 10px 0;
      filter: drop-shadow(0 0 10px rgba(59,130,246,0.4));
    }
    .paperdoll-slots {
      display: grid;
      grid-template-columns: repeat(2, 64px);
      gap: 12px;
      margin: 14px 0;
    }
    .slot {
      width: 64px;
      height: 64px;
      background: #0f172a;
      border: 2px dashed #475569;
      border-radius: 8px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      position: relative;
      transition: all 0.2s;
    }
    .slot.dragover { border-color: var(--accent); background: rgba(59,130,246,0.2); }
    .slot.filled { border-style: solid; }
    .slot.legendary { border-color: var(--legendary); box-shadow: 0 0 8px rgba(250,204,21,0.4); }
    .slot.epic { border-color: var(--epic); box-shadow: 0 0 8px rgba(168,85,247,0.4); }
    .slot.rare { border-color: var(--rare); box-shadow: 0 0 8px rgba(56,189,248,0.4); }
    .slot-label { font-size: 9px; color: #64748b; text-transform: uppercase; margin-top: 2px; }

    /* Stats Panel */
    .stats-card {
      width: 100%;
      background: #090d16;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px;
      margin-top: auto;
      font-size: 11px;
    }
    .stat-row { display: flex; justify-content: space-between; margin-bottom: 6px; }

    /* Backpack Grid Area */
    .backpack-pane {
      background: #000;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      overflow-y: auto;
    }
    .backpack-grid {
      display: grid;
      grid-template-columns: repeat(4, 68px);
      gap: 10px;
      background: #111827;
      padding: 16px;
      border: 1px solid var(--border);
      border-radius: 12px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }
    .item-icon {
      font-size: 28px;
      user-select: none;
      cursor: grab;
      transition: transform 0.1s;
    }
    .item-icon:active { cursor: grabbing; transform: scale(1.15); }

    /* Inspector & Log Console */
    .side-pane {
      background: var(--panel);
      border-left: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      padding: 14px;
    }
    .log-box {
      flex: 1;
      background: #090d16;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 10px;
      font-family: monospace;
      font-size: 11px;
      overflow-y: auto;
      line-height: 1.6;
      color: #94a3b8;
    }
    .btn {
      background: #374151;
      color: #fff;
      border: none;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 11px;
      cursor: pointer;
      font-weight: 700;
    }
    .btn.op { background: var(--accent); }
    .btn.danger { background: var(--danger); }
    .btn:hover { opacity: 0.9; }
  </style>
</head>
<body>

<header>
  <div style="display:flex; align-items:center; gap:12px;">
    <strong data-ru="RPG Инвентарь Студия" data-en="RPG Inventory Studio">RPG Inventar Studiyasi</strong>
    <span class="badge-sub" data-ru="HTML5 Drag & Drop Engine" data-en="HTML5 Drag & Drop Engine">HTML5 Drag & Drop Dvigateli</span>
  </div>
  <div style="display:flex; gap:10px;">
    <button onclick="toggleLang()" class="btn" id="langBtn" data-ru="UZ / RU / EN" data-en="UZ / RU / EN">UZ / RU / EN</button>
    <button onclick="freezeStats()" class="btn danger" id="btnFreeze" data-ru="🛡️ Запечатать (Anti-Cheat)" data-en="🛡️ Freeze (Anti-Cheat)">🛡️ Muzlatish (Anti-Cheat)</button>
    <button onclick="resetLab()" class="btn" data-ru="Сброс" data-en="Reset">Qayta yuklash</button>
  </div>
</header>

<div class="main-grid">
  <!-- Left: Paperdoll & Stats -->
  <div class="hero-pane">
    <h3 style="font-size:12px;" data-ru="Экипировка Героя" data-en="Hero Equipment">Qahramon Jihozlari</h3>
    <div class="hero-avatar">🛡️</div>
    
    <div class="paperdoll-slots">
      <div class="slot" id="slotHead" data-slot="head" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)" ondrop="handleDrop(event)">
        <span class="slot-label" data-ru="Шлем" data-en="Helmet">Bosh</span>
      </div>
      <div class="slot" id="slotChest" data-slot="chest" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)" ondrop="handleDrop(event)">
        <span class="slot-label" data-ru="Броня" data-en="Armor">Zirh</span>
      </div>
      <div class="slot" id="slotWeapon" data-slot="weapon" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)" ondrop="handleDrop(event)">
        <span class="slot-label" data-ru="Оружие" data-en="Weapon">Qurol</span>
      </div>
      <div class="slot" id="slotShield" data-slot="shield" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)" ondrop="handleDrop(event)">
        <span class="slot-label" data-ru="Щит" data-en="Shield">Qalqon</span>
      </div>
    </div>

    <div class="stats-card">
      <div style="font-weight:700; margin-bottom:8px; color:var(--accent);" data-ru="Характеристики Героя:" data-en="Hero Combat Stats:">Jangovar Ko'rsatkichlar:</div>
      <div class="stat-row"><span>⚔️ Hujum (ATK):</span> <strong id="valAtk" style="color:#ef4444;">15</strong></div>
      <div class="stat-row"><span>🛡️ Himoya (DEF):</span> <strong id="valDef" style="color:#38bdf8;">10</strong></div>
      <div class="stat-row"><span>❤️ Hayot (HP):</span> <strong id="valHp" style="color:#22c55e;">100</strong></div>
      <div class="stat-row"><span>⚡ Tezlik (SPD):</span> <strong id="valSpd" style="color:#facc15;">20</strong></div>
      <div style="margin-top:8px; border-top:1px solid #1f2937; padding-top:6px; display:flex; justify-content:space-between;">
        <span data-ru="Рейтинг Силы:" data-en="Power Rating:">Umumiy Kuch:</span>
        <strong id="valPower" style="color:#a855f7;">145</strong>
      </div>
    </div>
  </div>

  <!-- Center: Backpack Grid -->
  <div class="backpack-pane">
    <h3 style="font-size:13px; margin-bottom:14px;" data-ru="Рюкзак (16 Слотов)" data-en="Backpack (16 Slots)">Xalta (16 Ta Zaxira Sloti)</h3>
    <div class="backpack-grid" id="backpackGrid">
      <!-- Generated via JS -->
    </div>
    <div style="margin-top:14px; font-size:11px; color:#64748b;" data-ru="Подсказка: перетащите Меч или Щит мышкой в соответствующие слоты слева!" data-en="Tip: drag items from backpack into equipment sockets on the left!">Maslahat: xaltadagi Qilich yoki Qalqonni chap tomondagi slotlarga suring!</div>
  </div>

  <!-- Right: Inspector & Telemetry -->
  <div class="side-pane">
    <h3 style="font-size:13px;" data-ru="Лог Событий и Безопасность" data-en="Event Log & Security">Hodisalar Jurnali</h3>
    <div class="log-box" id="logBox" style="margin-top:8px;">
      <div style="color:#64748b;">[Tizim tayyor] Drag & Drop harakatlarini kuting.</div>
    </div>
    <div style="margin-top:10px; display:flex; gap:8px;">
      <button onclick="saveStorage()" class="btn op" style="flex:1;" data-ru="Сохранить" data-en="Save">Saqlash (Storage)</button>
      <button onclick="loadStorage()" class="btn" style="flex:1;" data-ru="Загрузить" data-en="Load">Yuklash</button>
    </div>
  </div>
</div>

<script>
var curLang = 'uz';

var hero = {
  baseAtk: 15,
  baseDef: 10,
  baseHp: 100,
  baseSpd: 20
};

var items = {
  katana: { id: "katana", name: "Kiber-Katana", type: "weapon", icon: "⚔️", rarity: "legendary", stats: { atk: 35, spd: 5 } },
  aegis: { id: "aegis", name: "Aegis Qalqoni", type: "shield", icon: "🛡️", rarity: "epic", stats: { def: 40, spd: -3 } },
  helm: { id: "helm", name: "Kiber-Shlem", type: "head", icon: "🪖", rarity: "rare", stats: { def: 15, hp: 50 } },
  armor: { id: "armor", name: "Titan Zirh", type: "chest", icon: "🥋", rarity: "rare", stats: { def: 25, hp: 80 } }
};

var equipped = { head: null, chest: null, weapon: null, shield: null };
var backpack = [ "katana", "aegis", "helm", "armor", null, null, null, null, null, null, null, null, null, null, null, null ];

function toggleLang() {
  if (curLang === 'uz') curLang = 'ru';
  else if (curLang === 'ru') curLang = 'en';
  else curLang = 'uz';
  document.getElementById('langBtn').textContent = curLang.toUpperCase();
  applyLang();
}

function applyLang() {
  var els = document.querySelectorAll('[data-ru]');
  els.forEach(function(el) {
    if (curLang === 'ru') el.textContent = el.getAttribute('data-ru');
    else if (curLang === 'en') el.textContent = el.getAttribute('data-en');
  });
}

function logEvent(msg) {
  var b = document.getElementById('logBox');
  var d = document.createElement('div');
  d.innerHTML = msg;
  b.appendChild(d);
  b.scrollTop = b.scrollHeight;
}

function renderBackpack() {
  var grid = document.getElementById('backpackGrid');
  grid.innerHTML = '';
  
  for (var i = 0; i < 16; i++) {
    var slot = document.createElement('div');
    slot.className = 'slot';
    slot.dataset.index = i;
    slot.dataset.slot = 'backpack';
    slot.ondragover = handleDragOver;
    slot.ondragleave = handleDragLeave;
    slot.ondrop = handleDrop;

    var itemId = backpack[i];
    if (itemId && items[itemId]) {
      var it = items[itemId];
      slot.classList.add('filled', it.rarity);
      var icon = document.createElement('div');
      icon.className = 'item-icon';
      icon.draggable = true;
      icon.textContent = it.icon;
      icon.dataset.itemId = it.id;
      icon.dataset.from = 'backpack';
      icon.dataset.index = i;
      icon.ondragstart = handleDragStart;
      slot.appendChild(icon);
    }
    grid.appendChild(slot);
  }
}

function renderEquipped() {
  var slotMap = { head: 'slotHead', chest: 'slotChest', weapon: 'slotWeapon', shield: 'slotShield' };
  
  for (var type in slotMap) {
    var el = document.getElementById(slotMap[type]);
    el.className = 'slot';
    var itemId = equipped[type];
    if (itemId && items[itemId]) {
      var it = items[itemId];
      el.classList.add('filled', it.rarity);
      el.innerHTML = '<div class="item-icon" draggable="true" data-item-id="' + it.id + '" data-from="equipped" data-slot-type="' + type + '">' + it.icon + '</div><span class="slot-label">' + type + '</span>';
      el.querySelector('.item-icon').ondragstart = handleDragStart;
    } else {
      el.innerHTML = '<span class="slot-label">' + type + '</span>';
    }
  }
}

function handleDragStart(e) {
  var id = e.target.dataset.itemId;
  var from = e.target.dataset.from;
  var idx = e.target.dataset.index;
  var slotType = e.target.dataset.slotType;
  
  e.dataTransfer.setData('text/plain', JSON.stringify({ id: id, from: from, index: idx, slotType: slotType }));
  logEvent('⚡ <strong>ondragstart:</strong> ' + items[id].name + ' ushlandi.');
}

function handleDragOver(e) {
  e.preventDefault();
  e.currentTarget.classList.add('dragover');
}

function handleDragLeave(e) {
  e.currentTarget.classList.remove('dragover');
}

function handleDrop(e) {
  e.preventDefault();
  e.currentTarget.classList.remove('dragover');
  
  var raw = e.dataTransfer.getData('text/plain');
  if (!raw) return;
  var data = JSON.parse(raw);
  var it = items[data.id];
  var targetSlot = e.currentTarget.dataset.slot;

  // Type Validation
  if (targetSlot !== 'backpack' && it.type !== targetSlot) {
    logEvent('<span style="color:#ef4444;">❌ XATO: ' + it.name + ' (' + it.type + ') ' + targetSlot + ' slotiga tushmaydi!</span>');
    return;
  }

  // Remove from old place
  if (data.from === 'backpack') {
    backpack[data.index] = null;
  } else if (data.from === 'equipped') {
    equipped[data.slotType] = null;
  }

  // Place in target
  if (targetSlot === 'backpack') {
    var targetIdx = e.currentTarget.dataset.index;
    backpack[targetIdx] = it.id;
    logEvent('🎒 <strong>ondrop:</strong> ' + it.name + ' xaltaga joylandi.');
  } else {
    equipped[targetSlot] = it.id;
    logEvent('<span style="color:#22c55e;">⚔️ <strong>ondrop:</strong> ' + it.name + ' ' + targetSlot + ' slotiga kiyildi!</span>');
  }

  recalculateStats();
  renderBackpack();
  renderEquipped();
}

function recalculateStats() {
  var atk = hero.baseAtk;
  var def = hero.baseDef;
  var hp = hero.baseHp;
  var spd = hero.baseSpd;

  for (var k in equipped) {
    var id = equipped[k];
    if (id && items[id]) {
      var st = items[id].stats;
      if (st.atk) atk += st.atk;
      if (st.def) def += st.def;
      if (st.hp) hp += st.hp;
      if (st.spd) spd += st.spd;
    }
  }

  document.getElementById('valAtk').textContent = atk;
  document.getElementById('valDef').textContent = def;
  document.getElementById('valHp').textContent = hp;
  document.getElementById('valSpd').textContent = spd;
  document.getElementById('valPower').textContent = atk + def + hp + spd;
}

function freezeStats() {
  for (var k in items) {
    Object.freeze(items[k].stats);
    Object.freeze(items[k]);
  }
  logEvent('<span style="color:#facc15; font-weight:700;">🛡️ [Anti-Cheat]: Object.freeze() faollashtirildi. Barcha buyumlar xotirada muzlatildi!</span>');
  alert('Anti-Cheat yoqildi! Buyum statlarini konsolda buzish imkonsiz.');
}

function saveStorage() {
  localStorage.setItem('target_hero_backpack', JSON.stringify(backpack));
  localStorage.setItem('target_hero_equipped', JSON.stringify(equipped));
  logEvent('<span style="color:#38bdf8;">💾 [LocalStorage]: Xalta va jihozlar saqlandi.</span>');
}

function loadStorage() {
  var b = localStorage.getItem('target_hero_backpack');
  var eq = localStorage.getItem('target_hero_equipped');
  if (b && eq) {
    backpack = JSON.parse(b);
    equipped = JSON.parse(eq);
    recalculateStats();
    renderBackpack();
    renderEquipped();
    logEvent('<span style="color:#22c55e;">📂 [LocalStorage]: Xalta qayta tiklandi.</span>');
  }
}

function resetLab() {
  equipped = { head: null, chest: null, weapon: null, shield: null };
  backpack = [ "katana", "aegis", "helm", "armor", null, null, null, null, null, null, null, null, null, null, null, null ];
  recalculateStats();
  renderBackpack();
  renderEquipped();
  document.getElementById('logBox').innerHTML = '<div style="color:#64748b;">[Qayta yuklandi] Drag & Drop harakatlarini kuting.</div>';
}

renderBackpack();
renderEquipped();
recalculateStats();
</script>

</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "simulator", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: simulator/index.html")

def main():
    print("📦 Building 7-8-sinf (Lesson 35: Inventory System & Drag-and-Drop)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_simulator()
    print("🎉 Done! Generated Grade 7–8 Lesson 35.")

if __name__ == "__main__":
    main()
