#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cohort 7-8-sinf planned weeks (Weeks 6–36) for Target International School.
5 hours/week. Game Development, Interactive Canvas 2D/3D & CyberSecurity.
"""

WEEKS_7_8_PLANNED = {
    6: {
        "title": {"uz": "Sport Iqtisodiyoti va Auksion Bozorlari: Karta Paketlari va Ehtimollik", "ru": "Спортивная Экономика и Аукционы: Паки Карт и Вероятности", "en": "Sports Economics and Auction Markets: Card Packs and Probabilities"},
        "type": {"uz": "Iqtisodiy Studio", "ru": "Экономическая Студия", "en": "Economics Studio"},
        "skills": {"uz": "Virtual valyuta balansi, Ehtimolliklar nazariyasi (Drop Rates), Karta paketlarini ochish (Pack Opening), Inflyatsiyadan himoya", "ru": "Баланс виртуальной валюты, теория вероятностей (Drop Rates), открытие паков карт, защита от инфляции", "en": "Virtual currency sinks, drop rate probability math, pack opening mechanics, anti-inflation market balancing"},
        "deliverable": {"uz": "O'yin tangalariga paketlar ochiladigan va ehtimolligi shaffof ko'rinadigan mini-iqtisodiyot studiyasi", "ru": "Студия открытия паков с прозрачной вероятностью выпадения редких карт", "en": "Card pack opening simulator with transparent probability curves and currency sink mechanics"},
        "tools": "FUT Pack Opening Simulator, Math.random"
    },
    7: {
        "title": {"uz": "Taktika va O'yinchi AI: Taktik Sxemalar va Pozitsiya Algoritmi", "ru": "Тактика и AI Игроков: Тактические Схемы и Позиционирование", "en": "Tactics and Player AI: Tactical Formations and Positioning Logic"},
        "type": {"uz": "Taktik Lab", "ru": "Тактическая Лаб", "en": "Tactics Lab"},
        "skills": {"uz": "4-3-3 va 3-5-2 taktik sxemalari, Maydonda avtomatik joylashish (Vector Math), Hujum va himoya xulq-atvori AI", "ru": "Тактические схемы 4-3-3 и 3-5-2, автоматическое позиционирование (векторная математика), AI атаки и защиты", "en": "4-3-3 and 3-5-2 tactical setups, vector-based pitch positioning, autonomous attacking and defensive AI"},
        "deliverable": {"uz": "Taktik sxema o'zgarganda o'yinchilar avtomatik o'z o'rnini to'g'ri egallaydigan 2D taktik doska", "ru": "Интерактивная 2D доска с автоматическим позиционированием игроков при смене схемы", "en": "Interactive tactical whiteboard dynamically animating player positions based on formation choices"},
        "tools": "SVG Pitch, Canvas 2D, Vector Math"
    },
    8: {
        "title": {"uz": "1-Chorak Oraliq Nazorat: Sport Simulyatori va O'yin Fizikasi Sinovi", "ru": "Промежуточный Контроль 1-й Четверти: Спортивный Симулятор и Физика", "en": "Quarter 1 Midterm Exam: Sports Simulator and Game Physics"},
        "type": {"uz": "Oraliq Imtihon", "ru": "Промежуточный Экзамен", "en": "Midterm Examination"},
        "skills": {"uz": "FUT kartalari, Kimyo graflari, Match Engine va Transfer Market integratsiyasi, Sinov va testlash", "ru": "Интеграция карточек FUT, графов сыгранности, движка матча и трансферного рынка", "en": "Full integration of card attributes, chemistry graph, 90-min match engine, and auction economics"},
        "deliverable": {"uz": "To'liq integratsiya qilingan va sinflararo turnirda ishlaydigan FUT Sports portali (10 ballik mezon)", "ru": "Работающий портал FUT Sports, протестированный в школьном турнире (10-балльная шкала)", "en": "Fully integrated FUT Sports engine successfully deployed and tournament-verified (10-point rubric)"},
        "tools": "FUT Suite, VS Code, Browser DevTools"
    },
    9: {
        "title": {"uz": "1-Chorak Demo Day: Target Futbol Simulyatori va Kiber-Arkada Ko'rgazmasi", "ru": "Demo Day 1-й Четверти: Выставка Симулятора Футбола и Кибераркады", "en": "Quarter 1 Demo Day: Target Sports Simulator and Cyber-Arcade Showcase"},
        "type": {"uz": "Demo Day / Turnir", "ru": "Demo Day / Турнир", "en": "Demo Day / Tournament"},
        "skills": {"uz": "O'yin loyihasini omma oldida namoyish qilish, Do'stlar bilan jonli turnir o'tkazish, O'yin muvozanatini tushuntirish", "ru": "Публичная презентация игры, проведение турнира с одноклассниками, защита игрового баланса", "en": "Public game showcase, hosting a live classroom esports tournament, explaining game balance math"},
        "deliverable": {"uz": "Maktab chempionati o'tkazilgan shaxsiy interaktiv sport o'yini va 1-Chorak Geym-Dizayn Sertifikati", "ru": "Интерактивная спортивная игра с проведенным турниром и сертификат гейм-дизайна 1-й четверти", "en": "Published interactive sports game utilized in school tournament, plus Quarter 1 Certificate"},
        "tools": "Live Tournament Arena, Projector, QR Game Link"
    },
    10: {
        "title": {"uz": "Matritsalar va Xaritalar (Tilemaps): 2D Labirint va Platformalar", "ru": "Матрицы и Карты (Tilemaps): 2D Лабиринт и Платформы", "en": "Matrices and Tilemaps: 2D Maze and Platform Layouts"},
        "type": {"uz": "Geym-Dizayn Lab", "ru": "Гейм-Дизайн Лаб", "en": "Game Design Lab"},
        "skills": {"uz": "2D massivlar orqali xarita chizish (Grid system), Tayllar turlari (Devor, Yo'l, Xazina), Qahramonni to'siqlardan o'tkazmaslik", "ru": "Отрисовка карты через 2D массивы (Grid), типы тайлов (стена, путь, сундук), коллизии со стенами", "en": "2D array matrix maps, grid coordinate systems, tile types (wall, floor, chest), tile-based collision physics"},
        "deliverable": {"uz": "Sonlar matritsasi o'zgarishi bilan ekranda yangi xarita chiziladigan dinamik Tilemap tizimi", "ru": "Динамическая система Tilemap, генерирующая игровую карту на основе числовой матрицы", "en": "Dynamic Tilemap rendering engine transforming 2D integer matrices into playable level maps"},
        "tools": "Canvas 2D, 2D Arrays, Tile Sheet"
    },
    11: {
        "title": {"uz": "Kamera va Ko'rish Maydoni: Fog of War (Urush Tumani) Effekti", "ru": "Камера и Поле Зрения: Эффект Fog of War (Туман Войны)", "en": "Camera and Line of Sight: Fog of War and Dynamic Lighting"},
        "type": {"uz": "Vizual Effekt Lab", "ru": "Лаб Визуальных Эффектов", "en": "Visual Effects Lab"},
        "skills": {"uz": "Ko'rish radiusi, Raycasting asoslari, Qorong'i xonalarni yoritish, Ko'rinmaydigan dushmanlar siri", "ru": "Радиус видимости, основы Raycasting, освещение темных комнат, сокрытие невидимых врагов", "en": "Line of sight algorithms, basic raycasting, radial dynamic darkness masking, fog of war revealing"},
        "deliverable": {"uz": "Qahramon mash'ala bilan yurganda faqat atrofi ko'rinadigan qorong'i yer osti labirinti", "ru": "Темный подземный лабиринт с факелом, освещающим только область вокруг персонажа", "en": "Atmospheric dungeon crawl scene where player's torch reveals tiles dynamically in real time"},
        "tools": "Canvas GlobalCompositeOperation, Radial Gradients"
    },
    12: {
        "title": {"uz": "Procedural Dunyo Yaratilishi: Tasodifiy Labirintlar Generatsiyasi", "ru": "Процедурный Мир: Генерация Случайных Лабиринтов", "en": "Procedural Generation: Randomized Dungeon Maze Algorithms"},
        "type": {"uz": "Algoritmik Lab", "ru": "Алгоритмическая Лаб", "en": "Algorithmic Lab"},
        "skills": {"uz": "Procedural kontent generatsiyasi (PCG), Tasodifiy xonalar qurish, Xazinalar va eshiklarni joylashtirish algoritmi", "ru": "Процедурная генерация контента (PCG), случайные комнаты, алгоритм размещения сундуков и дверей", "en": "Procedural dungeon generation algorithms, room placement heuristics, item and exit distribution"},
        "deliverable": {"uz": "Har safar 'Qayta boshlash' bosilganda butunlay yangi va o'tib bo'ladigan labirint yasovchi generator", "ru": "Генератор, создающий совершенно новый проходимый лабиринт при каждом перезапуске", "en": "Algorithmic dungeon generator guaranteeing solvable procedural maze layouts on every game start"},
        "tools": "Random Walker, Binary Space Partitioning, JS"
    },
    13: {
        "title": {"uz": "Qurollar va O'qlar Fizikasi: Trigonometriya va Traektoriya", "ru": "Физика Оружия и Снарядов: Тригонометрия и Траектории", "en": "Weapons and Projectile Physics: Trigonometry and Trajectories"},
        "type": {"uz": "Fizika Lab", "ru": "Физика Лаб", "en": "Physics Lab"},
        "skills": {"uz": "Math.atan2 yordamida nishon burchagini topish, Math.cos va Math.sin bilan o'q tezligini hisoblash, O'qlarni o'chirish (Memory cleanup)", "ru": "Вычисление угла цели через Math.atan2, расчет скорости снаряда по синусу и косинусу, очистка памяти", "en": "Angle calculation using Math.atan2, directional velocity via sin/cos, projectile pools and memory pruning"},
        "deliverable": {"uz": "Sichqoncha ko'rsatkichiga qarab o'q uzuvchi va dushmanlarni nishonga oluvchi kiber-otishma tizimi", "ru": "Система стрельбы, выпускающая снаряды точно в сторону курсора мыши", "en": "Precise directional shooting system firing projectiles towards mouse coordinates with impact physics"},
        "tools": "Canvas Trigonometry, Math.atan2, Particle Array"
    },
    14: {
        "title": {"uz": "Dushman AI va Pathfinding: To'siqlarni Aylanib Quvish Algoritmi", "ru": "AI Врагов и Pathfinding: Алгоритм Обхода Препятствий", "en": "Enemy AI and Pathfinding: Obstacle Avoidance and Chase Logic"},
        "type": {"uz": "AI Geym-Dizayn", "ru": "AI Гейм-Дизайн", "en": "AI Game Design"},
        "skills": {"uz": "A* (A-Star) qidiruv algoritmi asoslari, Graf tugunlari, Devorlarni aylanib o'tish, Ta'qib qilish va qochish rejimlari", "ru": "Основы алгоритма поиска пути A*, графы, обход стен, режимы преследования и побега", "en": "Pathfinding fundamentals, Manhattan distance heuristics, navigating around maze walls, pursuit behaviors"},
        "deliverable": {"uz": "Qahramon qayerga yashirinmasin, labirint bo'ylab eng qisqa yo'l bilan quvuvchi aqlli dushman", "ru": "Умный противник, находящий кратчайший путь к игроку через лабиринт", "en": "Autonomous enemy finding the shortest path to player around complex dungeon obstacles"},
        "tools": "Breadth-First Search (BFS) / A*, Canvas 2D"
    },
    15: {
        "title": {"uz": "Inventar va Buyumlar Tizimi: Drag-and-Drop va Artefaktlar", "ru": "Система Инвентаря: Drag-and-Drop и Артефакты", "en": "Inventory and Item Systems: Drag-and-Drop and Artifacts"},
        "type": {"uz": "UI/UX Lab", "ru": "UI/UX Лаб", "en": "UI/UX Lab"},
        "skills": {"uz": "Slotlar tizimi, Buyumlar massivi, Kuchaytirgichlar (Qilich +10 kuch, Qalqon +20 himoya), Drag-and-drop buyum siljitish", "ru": "Система слотов инвентаря, баффы (меч +10 к силе, щит +20 к броне), перетаскивание предметов (Drag-and-Drop)", "en": "Grid inventory slots, item stat modifiers (attack/defense buffs), drag-and-drop slot swapping"},
        "deliverable": {"uz": "Xazinalardan olingan buyumlarni taqish, ishlatish va almashtirish imkonini beruvchi to'liq inventar paneli", "ru": "Полноценный инвентарь для экипировки, использования и перетаскивания найденных предметов", "en": "RPG inventory interface allowing equipping items, drinking potions, and organizing slots"},
        "tools": "HTML5 Drag and Drop API, CSS Flex Grid"
    },
    16: {
        "title": {"uz": "O'yin Kiberxavfsizligi: Cheat Engine va Ochkolarni Soxtalashtirishdan Himoya", "ru": "Кибербезопасность Игр: Защита от Чит-Кодов и Подделки Очков", "en": "Game CyberSecurity: Anti-Cheat Protection and Integrity Checks"},
        "type": {"uz": "Kiberxavfsizlik", "ru": "Кибербезопасность", "en": "CyberSecurity"},
        "skills": {"uz": "Xotira o'zgaruvchilarini konsoldan buzish (Variable Tampering), Xesh summasi bilan qiymatni himoyalash, Server validatsiyasi", "ru": "Взлом очков через консоль браузера, защита значений через контрольные суммы, серверная валидация", "en": "Preventing client-side memory manipulation, checksum state hashing, rate checks, anti-cheat validation"},
        "deliverable": {"uz": "O'yinchi konsol orqali ochkolarni oshirishga harakat qilsa, uni fosh qiluvchi Kiber-Qalqon moduli", "ru": "Модуль защиты, блокирующий попытки накрутки очков через консоль разработчика", "en": "Tamper-resistant anti-cheat layer detecting console variable hacks and preventing fraudulent scores"},
        "tools": "HMAC / Hash Verification, Obfuscation, DevTools"
    },
    17: {
        "title": {"uz": "2-Chorak Oraliq Nazorat: Roguelike Dungeon O'yinini Ishlab Chiqish", "ru": "Промежуточный Контроль 2-й Четверти: Создание Roguelike Игры", "en": "Quarter 2 Midterm Exam: Roguelike Dungeon Crawler Engine"},
        "type": {"uz": "Oraliq Imtihon", "ru": "Промежуточный Экзамен", "en": "Midterm Examination"},
        "skills": {"uz": "Tilemap, Dushman AI, Otishma fizikasi, Inventar va xavfsizlik modullarini to'liq yagona o'yinga jamlash", "ru": "Объединение Tilemap, AI врагов, физики стрельбы, инвентаря и защиты в единую игру", "en": "End-to-end evaluation combining procedural dungeons, enemy AI, inventory slots, and sound FX"},
        "deliverable": {"uz": "Imtihon mezonlari bo'yicha to'liq o'ynaladigan yer osti qasri Roguelike o'yini (10 ballik mezon)", "ru": "Полноценная игра Roguelike Dungeon, соответствующая всем критериям (10-балльная шкала)", "en": "Fully playable Roguelike Dungeon Crawler game submitted with rubric requirements (10-point rubric)"},
        "tools": "Canvas 2D Engine, Web Audio, VS Code"
    },
    18: {
        "title": {"uz": "2-Chorak Demo Day: Qishki Roguelike O'yin Jam Ko'rgazmasi", "ru": "Demo Day 2-й Четверти: Зимний Roguelike Game Jam", "en": "Quarter 2 Demo Day: Winter Roguelike Game Jam Expo"},
        "type": {"uz": "Demo Day / Game Jam", "ru": "Demo Day / Game Jam", "en": "Demo Day / Game Jam"},
        "skills": {"uz": "Geympley ko'rigi, Do'stlarga o'ynatib fikr olish, O'yin atmosferasini namoyish etish, Qiziqarli treyler", "ru": "Презентация геймплея, плейтестинг с одноклассниками, демонстрация атмосферы игры", "en": "Live playtesting showcase, gathering gameplay telemetry, defending balance decisions"},
        "deliverable": {"uz": "Sinfdoshlar zavq bilan o'ynagan va yuqori baholagan yakuniy Roguelike o'yini va 2-Chorak Sertifikati", "ru": "Готовая игра Roguelike, получившая высокие оценки одноклассников, и сертификат 2-й четверти", "en": "Published Roguelike game title with high peer rating, plus Quarter 2 Game Dev Honors Diploma"},
        "tools": "Live Game Station, Presentation Rig, Gamepad Support"
    },
    19: {
        "title": {"uz": "3D Dunyoga Qadam: Three.js, Vektorlar va 3D Fazosi", "ru": "Шаг в 3D Мир: Three.js, Векторы и 3D Пространство", "en": "Stepping into 3D: Three.js, Vectors, and 3D Coordinates"},
        "type": {"uz": "3D Asos", "ru": "3D База", "en": "3D Foundation"},
        "skills": {"uz": "X, Y, Z koordinatalari, Sahna (Scene), Kamera (PerspectiveCamera), Renderer, Mesh va Materiallar", "ru": "Координаты X, Y, Z, сцена (Scene), камера, рендерер, сетки (Mesh) и материалы", "en": "3D spatial axes (X, Y, Z), Scene graph, Perspective Camera, WebGL Renderer, Mesh and Material basics"},
        "deliverable": {"uz": "Brauzerda sichqoncha bilan 360 daraja aylanadigan va chiroqlari tovlanadigan birinchi 3D sahna", "ru": "Первая 3D сцена в браузере, вращающаяся на 360 градусов с динамическим освещением", "en": "Interactive 3D WebGL scene rendering textured geometries with interactive 360 camera controls"},
        "tools": "Three.js, WebGL, OrbitControls"
    },
    20: {
        "title": {"uz": "Three.js Chiroqlar va Soya Fizikasi (Lighting & Shadows)", "ru": "Свет и Тени в Three.js (Lighting & Shadows)", "en": "Three.js Lighting and Shadow Physics"},
        "type": {"uz": "3D Vizual Lab", "ru": "3D Визуальная Лаб", "en": "3D Visuals Lab"},
        "skills": {"uz": "AmbientLight, DirectionalLight, SpotLight, Soyalar tushishi (Cast & Receive Shadows), Materiallar yaltirashi (Roughness/Metalness)", "ru": "AmbientLight, направленный свет, прожекторы, отбрасывание теней, параметры шероховатости и металла", "en": "Ambient, directional, and spotlight sources, shadow maps casting, PBR roughness and metalness tuning"},
        "deliverable": {"uz": "Haqiqiy quyosh nuri tushib polga chiroyli soyalar hosil qiluvchi fotorealistik 3D kiber-baza", "ru": "Фотореалистичная 3D кибер-база с реалистичными солнечными лучами и мягкими тенями", "en": "Atmospheric 3D sci-fi outpost with dynamic shadows, spotlights, and PBR metallic reflections"},
        "tools": "Three.js PBR, ShadowMap, Dat.GUI"
    },
    21: {
        "title": {"uz": "3D Modellar Dunyosi: GLTF/GLB Modellarni Yuklash va Boshqarish", "ru": "Мир 3D Моделей: Загрузка и Управление GLTF/GLB Моделями", "en": "3D Model Pipeline: Loading and Animating GLTF/GLB Models"},
        "type": {"uz": "3D Modellashtirish Lab", "ru": "3D Лаб Моделирования", "en": "3D Modeling Lab"},
        "skills": {"uz": "GLTFLoader, 3D kiber-qahramon va kosmik kema modellarini o'yinga qo'shish, Skeletli animatsiyalarni o'ynatish (AnimationMixer)", "ru": "GLTFLoader, добавление 3D персонажей и кораблей в игру, запуск скелетных анимаций", "en": "GLTFLoader integration, importing low-poly 3D sci-fi models, playing rigged animations via AnimationMixer"},
        "deliverable": {"uz": "Klaviatura strelkalari bilan 3D maydonda yuguruvchi va sakrovchi to'liq 3D qahramon", "ru": "Полноценный 3D персонаж, бегающий и прыгающий по 3D локации с анимациями", "en": "Controllable 3D character with running and jumping animation states navigated through 3D terrain"},
        "tools": "Three.js GLTFLoader, Blender low-poly models, Mixamo"
    },
    22: {
        "title": {"uz": "3D Kosmik Kema Simulyatori: Asteroidlar Poygasi", "ru": "Симулятор Космического Корабля 3D: Гонка через Астероиды", "en": "3D Spaceship Simulator: Asteroid Field Racing"},
        "type": {"uz": "3D O'yin Lab", "ru": "3D Игровая Лаб", "en": "3D Gaming Lab"},
        "skills": {"uz": "6 erkinlik darajasi (Roll, Pitch, Yaw), Yulduzlar changi partikllari, Asteroidlar bilan 3D to'qnashuv (BoundingSphere)", "ru": "Управление кораблем (Roll, Pitch, Yaw), частицы звездного пространства, 3D столкновения со сферами", "en": "Spaceship flight kinematics (Pitch/Roll/Yaw), starry particle systems, 3D sphere collision checks"},
        "deliverable": {"uz": "Kosmik kemada asteroidlar orasidan uchib o'tib marraga yetib boruvchi 3D arkada o'yini", "ru": "3D космическая аркада с полетом через пояс астероидов на скорость", "en": "Thrilling 3D space flight runner dodging procedural asteroids with engine glow particle trails"},
        "tools": "Three.js Particles, Vector3 Math, Audio SFX"
    },
    23: {
        "title": {"uz": "Fazoviy Ovoz (Spatial 3D Audio) va Atmosferik Saundtrek", "ru": "Пространственный Звук (3D Audio) и Саундтрек", "en": "Spatial 3D Audio and Atmospheric Soundscapes"},
        "type": {"uz": "Audio Muhandislik", "ru": "Аудио Инженерия", "en": "Audio Engineering"},
        "skills": {"uz": "Web Audio API PannerNode, Quloqchinlarda yaqinlashganda chap yoki o'ngdan eshitiluvchi tovushlar, Fon musiqasi sintezi", "ru": "Web Audio API PannerNode, позиционный 3D звук в наушниках, синтез фоновой музыки", "en": "Web Audio API PositionalAudio and PannerNode, directional sound physics, dynamic tension music layers"},
        "deliverable": {"uz": "Obyektga yaqinlashganda ovozi balandlashuvchi va fazoviy joylashuvni his qildiruvchi audio tizim", "ru": "Аудиосистема с позиционным звуком, меняющим громкость и направление при приближении", "en": "True spatial 3D audio environment where sound cues guide player perception through 3D space"},
        "tools": "Three.js PositionalAudio, Web Audio API"
    },
    24: {
        "title": {"uz": "Ko'p O'yinchili (Multiplayer) Asoslari: Ikki O'yinchi Maydonda", "ru": "Основы Мультиплеера: Два Игрока на Одной Карте", "en": "Multiplayer Game Basics: Synchronizing Multiple Players"},
        "type": {"uz": "Tarmoqli O'yin", "ru": "Сетевая Игра", "en": "Multiplayer Game"},
        "skills": {"uz": "WebSockets orqali o'yinchilar koordinatalarini almashish, Lag (kechikish) kompensatsiyasi, Interpolatsiya (silliq siljish)", "ru": "Синхронизация координат игроков через WebSockets, компенсация лагов, интерполяция движения", "en": "Player coordinate exchange over WebSockets, tick rate optimization, linear interpolation (lerp) smoothing"},
        "deliverable": {"uz": "Ikki xil kompyuterdan kirgan o'yinchilar bir-birining harakatini ekranda ko'radigan jonli prototip", "ru": "Прототип сетевой игры, где два игрока с разных компьютеров видят перемещения друг друга", "en": "Live dual-client multiplayer game arena rendering peer movements smoothly across network"},
        "tools": "WebSockets, Node.js Relay Server, Canvas/Three.js"
    },
    25: {
        "title": {"uz": "Jonli Multiplayer Duel: Kiber-Poyga yoki Duel Maydoni", "ru": "Живой Мультиплеерный Поединок: Кибер-Гонка или Дуэль", "en": "Live Multiplayer Showdown: Cyber Racing or Arena Duel"},
        "type": {"uz": "Multiplayer Lab", "ru": "Мультиплеер Лаб", "en": "Multiplayer Lab"},
        "skills": {"uz": "O'yinchi to'qnashuvlari, Ballar hisobi serverda yuritilishi, Server-authoritative arxitektura, G'olibni aniqlash", "ru": "Столкновения игроков, серверный подсчет очков, серверная архитектура игры, определение победителя", "en": "Server-authoritative game state, collision arbitration, fair score calculation, victory podium broadcast"},
        "deliverable": {"uz": "Sinfdoshlar o'zaro musobaqalashadigan va real vaqtda ball yoziladigan to'liq ikki kishilik o'yin", "ru": "Сетевая игра для соревнований одноклассников с подсчетом очков в реальном времени", "en": "Playable 2-player real-time arena duel with authoritative scorekeeping and live match HUD"},
        "tools": "Node.js WebSocket Server, Canvas 2D / Three.js"
    },
    26: {
        "title": {"uz": "3-Chorak Oraliq Nazorat: 3D Sahna yoki Multiplayer O'yin Sinovi", "ru": "Промежуточный Контроль 3-й Четверти: 3D Сцена или Сетевая Игра", "en": "Quarter 3 Midterm Exam: 3D Environment or Multiplayer Arena"},
        "type": {"uz": "Oraliq Imtihon", "ru": "Промежуточный Экзамен", "en": "Midterm Examination"},
        "skills": {"uz": "Three.js 3D grafika yoki WebSockets tarmoq kodini barqaror ishlatish, Xatolarni bartaraf etish", "ru": "Стабильная работа 3D графики Three.js или сетевого кода WebSockets, устранение багов", "en": "Rigorous technical audit of 3D WebGL rendering performance or multiplayer socket synchronization"},
        "deliverable": {"uz": "Imtihon talablariga mos keluvchi mustaqil 3D yoki ko'p o'yinchili loyiha (10 ballik mezon)", "ru": "Рабочий 3D или мультиплеерный проект по критериям экзамена (10-балльная шкала)", "en": "Verified 3D graphics experience or stable multiplayer game prototype (10-point rubric)"},
        "tools": "Three.js, WebSockets, Chrome DevTools"
    },
    27: {
        "title": {"uz": "3-Chorak Demo Day: 3D Vizual Dunyolar va Multiplayer O'yinlar Festivali", "ru": "Demo Day 3-й Четверти: Фестиваль 3D Миров и Сетевых Игр", "en": "Quarter 3 Demo Day: 3D Worlds and Multiplayer Game Festival"},
        "type": {"uz": "Demo Day / Festival", "ru": "Demo Day / Фестиваль", "en": "Demo Day / Festival"},
        "skills": {"uz": "O'yinni sahnada namoyish qilish, Tomoshabinlar bilan jonli o'yin o'tkazish, Ovoz va grafika uyg'unligi", "ru": "Демонстрация игры на сцене, живой матч со зрителями, гармония звука и графики", "en": "Live stage demonstration, conducting live tournament matches with audience, audio-visual defense"},
        "deliverable": {"uz": "Maktab o'quvchilari o'rtasida katta ekranda o'ynalgan shaxsiy o'yin va 3-Chorak Diplomi", "ru": "Собственная игра, продемонстрированная на большом экране школы, и диплом 3-й четверти", "en": "Staged multiplayer gaming showcase and Quarter 3 Game Engineering Diploma"},
        "tools": "Big Screen Rig, Network Router, Gamepad Setup"
    },
    28: {
        "title": {"uz": "GDD (Game Design Document): O'yin Konsepsiyasi, Syujet va Qoidalar", "ru": "GDD (Game Design Document): Концепция, Сюжет и Правила Игры", "en": "GDD (Game Design Document): Concept, Lore, and Core Mechanics"},
        "type": {"uz": "Geym-Dizayn Asos", "ru": "База Гейм-Дизайна", "en": "Game Design Blueprint"},
        "skills": {"uz": "Game Design Document (GDD) yozish, O'yin syujeti, Qahramonlar va raqiblar, Asosiy o'yin sikli (Core Loop), Balans", "ru": "Составление Game Design Document (GDD), сюжет игры, персонажи и враги, базовый цикл (Core Loop), баланс", "en": "Authoring professional Game Design Documents (GDD), character lore, core gameplay loop, difficulty pacing"},
        "deliverable": {"uz": "Kelgusi katta loyihaning barcha qoidalarini tasvirlab beruvchi rasmiy GDD hujjati va eskizlar", "ru": "Официальный документ GDD и скетчи, описывающие все правила будущей игры", "en": "Comprehensive Game Design Document (GDD) with level flowcharts and character attribute matrices"},
        "tools": "Notion GDD Template, Sketches, Figma"
    },
    29: {
        "title": {"uz": "Asosiy Mexanika va Game Feel: Silliq Boshqaruv va Kamera Dinamikasi", "ru": "Базовая Механика и Game Feel: Плавное Управление и Камера", "en": "Core Mechanics and Game Feel: Juice, Feedback, and Camera Physics"},
        "type": {"uz": "Geympley Sifat", "ru": "Качество Геймплея", "en": "Game Feel Lab"},
        "skills": {"uz": "Game Feel (o'yin zavqi), Screen shake (ekran titrashi), Qahramon sakrashidagi inersiya, To'qnashuv zarbi", "ru": "Game Feel (удовольствие от игры), тряска экрана (Screen shake), инерция прыжка, сила отдачи при ударе", "en": "Game feel techniques, camera shake trauma curves, jump apex hang time, impact freeze frames"},
        "deliverable": {"uz": "Tugmachalar bosilganda o'yinchiga maksimal zavq beruvchi silliq va dinamik qahramon harakati", "ru": "Отзывчивое и плавное управление персонажем с сочной отдачей на каждое действие", "en": "Deeply satisfying player character controller featuring screen shake, squash/stretch, and tight physics"},
        "tools": "Canvas 2D / Three.js, Easing Functions"
    },
    30: {
        "title": {"uz": "Level Dizayn va Qiyinchilik Egri Chizig'i (Difficulty Curve)", "ru": "Левел-Дизайн и Кривая Сложности (Difficulty Curve)", "en": "Level Design and Progressive Difficulty Curve"},
        "type": {"uz": "Level Dizayn", "ru": "Левел-Дизайн", "en": "Level Design"},
        "skills": {"uz": "3 ta unikal bosqich yaratish (O'rmon, Kiber-baza, Boss zali), Dushmanlar sonini me'yorda oshirish, Yashirin sirlar", "ru": "Создание 3 уникальных уровней (Лес, База, Зал Босса), балансировка количества врагов, секретные зоны", "en": "Multi-stage level design (3 unique biomes), tuning enemy spawn density, pacing checkpoints and secrets"},
        "deliverable": {"uz": "Bosqichdan bosqichga o'tish imkoniyatiga ega bo'lgan 3 bosqichli mukammal o'yin xaritasi", "ru": "Игровая карта из 3 проработанных уровней с плавным переходом между ними", "en": "Polished 3-tier campaign featuring progressive biome themes and checkpoint auto-saving"},
        "tools": "Level Editor, Tilemaps, JSON Data"
    },
    31: {
        "title": {"uz": "Vizual Effektlar (VFX), Partikllar va Boshqaruv Menyulari (UI)", "ru": "Визуальные Эффекты (VFX), Частицы и Меню Управления (UI)", "en": "Visual Effects (VFX), Particle Systems, and Game UI"},
        "type": {"uz": "VFX & UI Lab", "ru": "VFX и UI Лаб", "en": "VFX and UI Lab"},
        "skills": {"uz": "Portlash partikllari, Yulduzlar yog'dusi, Bosh sahifa menyusi, Pauza ekrani, Sozlamalar va Ovoz slayderi", "ru": "Частицы взрывов, искры, главное меню игры, экран паузы, настройки и регулятор громкости", "en": "Complex particle emitters (sparks, explosions, smoke), polished start menu, pause modal, volume controls"},
        "deliverable": {"uz": "Bosh sahifasi, sozlamalari va ajoyib portlash effektlari bilan bezatilgan to'liq o'yin qobig'i", "ru": "Красивая обертка игры с главным меню, паузой, настройками и зрелищными спецэффектами", "en": "Complete game frontend featuring animated title screen, pause menu, audio settings, and vivid VFX"},
        "tools": "Particle System, CSS Glassmorphism UI"
    },
    32: {
        "title": {"uz": "Musiqiy Atmosfera va Tovushlar Dizayni (SFX & BGM)", "ru": "Музыкальная Атмосфера и Саунд-Дизайн (SFX & BGM)", "en": "Sound Design and Dynamic Background Music (SFX & BGM)"},
        "type": {"uz": "Audio Dizayn", "ru": "Аудио Дизайн", "en": "Audio Design"},
        "skills": {"uz": "O'yin vaziyatiga mos fon musiqasi (Tinchlik vs Jang), Harakat tovushlari (Qadam, sakrash, yutish), Ovoz balansi", "ru": "Фоновая музыка, меняющаяся по ситуации (покой vs бой), звуки шагов и прыжков, баланс звука", "en": "Adaptive background music crossfading, footstep/jump/coin audio synthesis, mix balance"},
        "deliverable": {"uz": "Har bir harakatiga jarangdor ovoz va ajoyib saundtrek jo bo'lgan to'laqonli audio tizim", "ru": "Богатый саундтрек и звуковые эффекты для всех игровых событий", "en": "Fully scored soundscape with synchronized Foley effects and contextual battle soundtrack"},
        "tools": "Web Audio API, Chiptune / SFX Generator"
    },
    33: {
        "title": {"uz": "Mobil Moslashuv, Touch Virtual Joystik va Responsivlik", "ru": "Мобильная Адаптация, Виртуальный Джойстик и Адаптивность", "en": "Mobile Optimization, Virtual Touch Controls, and Responsive Layout"},
        "type": {"uz": "Mobil Lab", "ru": "Мобильная Лаб", "en": "Mobile Lab"},
        "skills": {"uz": "Ekran o'lchamlariga moslashish (Viewport Resize), Sensorli barmoq boshqaruvi, Virtual joystik va A/B tugmalari", "ru": "Адаптация под любые экраны (Resize), сенсорное управление, виртуальный джойстик и кнопки A/B", "en": "Responsive viewport scaling, multi-touch virtual thumbstick, on-screen action buttons, mobile fullscreen"},
        "deliverable": {"uz": "Smartfonda ham, planshetda ham hech qanday kamchiliksiz barmog'i bilan o'ynaladigan o'yin", "ru": "Игра, в которую одинаково удобно играть и на смартфоне, и на компьютере", "en": "Cross-platform touch-ready build playing smoothly on mobile phones and tablets via responsive layout"},
        "tools": "Touch Events API, Fullscreen API, CSS Media Queries"
    },
    34: {
        "title": {"uz": "Playtesting Sinovlari va O'yin Balansini Mukammallashtirish", "ru": "Плейтестинг и Балансировка Игрового Процесса", "en": "Playtesting Iterations and Gameplay Balance Tuning"},
        "type": {"uz": "Sifat Sinovi", "ru": "Тест Качества", "en": "Quality Testing"},
        "skills": {"uz": "Sinfdoshlar o'rtasida o'yinni sinash, O'yinchilar qayerda yutqazayotganini kuzatish, Dushman kuchini sozlash", "ru": "Плейтестинг с одноклассниками, анализ мест гибели игроков, точная балансировка урона и здоровья", "en": "Formal playtesting feedback sessions, death heatmaps observation, fine-tuning HP and speed values"},
        "deliverable": {"uz": "Barcha o'yinchilar uchun qiziqarli va adolatli bo'lgan mukammal sozlangan o'yin balansi", "ru": "Сбалансированная игра, исправленная по итогам тестирования реальными игроками", "en": "Finely balanced final build eliminating frustrating bottlenecks based on real player telemetry"},
        "tools": "Analytics Logger, Balance Tuning Sheet"
    },
    35: {
        "title": {"uz": "O'yin Afishasi (Cover Art), Treyler va Internetga Deploy", "ru": "Постер Игры (Cover Art), Трейлер и Релиз в Интернете", "en": "Game Packaging, Cover Art, Trailer, and Web Publishing"},
        "type": {"uz": "Nashr Qilish", "ru": "Публикация", "en": "Publishing"},
        "skills": {"uz": "O'yin posterini yasash (Canva/Photoshop), 1 daqiqalik qiziqarli o'yin treyleri, Vercel/GitHub orqali global e'lon qilish", "ru": "Создание постера игры, 1-минутный трейлер, публикация в глобальной сети через Vercel/GitHub", "en": "Designing promotional cover art, editing a 60-second gameplay video trailer, publishing with custom URL"},
        "deliverable": {"uz": "Dunyoning istalgan joyidan havolaga kirib o'ynasa bo'ladigan rasmiy internet o'yini va QR kod", "ru": "Официальная опубликованная игра с работающей ссылкой и QR-кодом для смартфона", "en": "Published web game with promotional cover poster, mobile QR code card, and trailer video"},
        "tools": "Vercel, Canva, Screen Recorder, QR Code"
    },
    36: {
        "title": {"uz": "Target Game Awards: Yillik O'yin Festivali va G'oliblarni Taqirlash", "ru": "Target Game Awards: Годовой Фестиваль Игр и Награждение Победителей", "en": "Target Game Awards: Annual Game Festival Gala and Honors Defense"},
        "type": {"uz": "Grand Demo Day", "ru": "Grand Demo Day", "en": "Grand Demo Day"},
        "skills": {"uz": "Maktab hay'ati oldida o'yinni himoya qilish, Eng yaxshi geym-dizayn nominatsiyasida qatnashish, Bitiruv", "ru": "Защита игры перед жюри школы, участие в номинациях за лучший дизайн и геймплей, выпуск", "en": "Formal championship defense before School Board, competing for Game of the Year honors, diploma award"},
        "deliverable": {"uz": "Target International School Game Jam kubogi va Target IT Geym-Dizayn Oltin Diplomi", "ru": "Кубок фестиваля игр Target International School и золотой диплом гейм-дизайнера Target IT", "en": "Successfully defended annual Master Game Title and Target IT Game Engineer Honors Diploma"},
        "tools": "Gala Stage, Game Booth, Honors Diploma"
    }
}
