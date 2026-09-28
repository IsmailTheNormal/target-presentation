// MULTILINGUAL STRINGS (RU PRIMARY, EN, UZ)
let currentLang = 'ru';
const STRINGS = {
  ru: {
    title: "⚡ TARGET CYBER RUNNER // 2D ФИЗИЧЕСКИЙ ДВИЖОК",
    grounded: "НА ЗЕМЛЕ",
    airborne: "В ВОЗДУХЕ",
    controls: "🎮 <b>Управление:</b> [A] / [D] или [←] [→] — Бег &nbsp;|&nbsp; [ПРОБЕЛ] или [W] [↑] — Прыжок &nbsp;|&nbsp; [M] — Экран",
    sidebarTitle: "🛠️ Панель Гейм-Дизайна",
    sidebarSub: "Меняйте параметры физики и настраивайте ощущение от игры (Game Feel):",
    lblSpeed: "🏎️ Скорость (Speed):",
    lblJump: "🚀 Сила Прыжка (Jump):",
    lblGravity: "🌍 Гравитация (Gravity):",
    presets: "⚡ Готовые Пресеты:",
    pMoon: "🌕 Лунная Гравитация",
    pSonic: "⚡ Супер Молния",
    pHeavy: "🗿 Каменный Герой",
    pDefault: "🎯 Идеальный Баланс",
    aiTitle: "🤖 Промпт для AI (ChatGPT / Claude):",
    aiPrompt: '"В коде game.js добавь эффект двойного прыжка (Double Jump) и неоновые искры при прыжке"',
    fsEnter: "ЭКРАН",
    fsExit: "ВЫЙТИ"
  },
  en: {
    title: "⚡ TARGET CYBER RUNNER // 2D PHYSICS ENGINE",
    grounded: "GROUNDED",
    airborne: "AIRBORNE",
    controls: "🎮 <b>Controls:</b> [A] / [D] or [←] [→] — Run &nbsp;|&nbsp; [SPACE] or [W] [↑] — Jump &nbsp;|&nbsp; [M] — Fullscreen",
    sidebarTitle: "🛠️ Game Design Lab",
    sidebarSub: "Tweak physics parameters and dial in your custom Game Feel:",
    lblSpeed: "🏎️ Velocity (Speed):",
    lblJump: "🚀 Jump Impulse:",
    lblGravity: "🌍 Gravity Vector:",
    presets: "⚡ Physics Presets:",
    pMoon: "🌕 Low Moon Gravity",
    pSonic: "⚡ Super Sonic Dash",
    pHeavy: "🗿 Heavy Anvil",
    pDefault: "🎯 Balanced Feel",
    aiTitle: "🤖 AI Assistant Prompt (ChatGPT / Claude):",
    aiPrompt: '"In game.js, add a Double Jump feature and trigger neon sparks whenever the hero jumps"',
    fsEnter: "FULLSCREEN",
    fsExit: "EXIT"
  },
  uz: {
    title: "⚡ TARGET CYBER RUNNER // 2D FIZIKA DVIGATELI",
    grounded: "YERDA",
    airborne: "HAVODA",
    controls: "🎮 <b>Boshqaruv:</b> [A] / [D] yoki [←] [→] — Yurish &nbsp;|&nbsp; [SPACE] yoki [W] [↑] — Sakrash &nbsp;|&nbsp; [M] — To'liq ekran",
    sidebarTitle: "🛠️ Geym-Dizayn Paneli",
    sidebarSub: "Fizik parametrlarni o'zgartirib, o'yin hissini (Game Feel) sozlang:",
    lblSpeed: "🏎️ Tezlik (Speed):",
    lblJump: "🚀 Sakrash Kuchi (Jump):",
    lblGravity: "🌍 Gravitatsiya (Gravity):",
    presets: "⚡ Tayyor Shablonlar:",
    pMoon: "🌕 Oy Gravitatsiyasi",
    pSonic: "⚡ Super Chaqmoq",
    pHeavy: "🗿 Tosh Qahramon",
    pDefault: "🎯 Ideal Balans",
    aiTitle: "🤖 AI Yordamchiga Prompt:",
    aiPrompt: '"game.js da Double Jump imkoniyatini va sakrashda neon uchqun effektini qo\'sh"',
    fsEnter: "TO'LIQ EKRAN",
    fsExit: "CHIQISH"
  }
};

function setLang(l) {
  currentLang = l;
  const s = STRINGS[l] || STRINGS.ru;
  document.querySelectorAll('.btn-lang').forEach(b => {
    b.classList.toggle('is-active', b.id === 'btn-' + l);
  });
  if (document.getElementById('controls-text')) document.getElementById('controls-text').innerHTML = s.controls;
  if (document.getElementById('sidebar-title')) document.getElementById('sidebar-title').textContent = s.sidebarTitle;
  if (document.getElementById('sidebar-sub')) document.getElementById('sidebar-sub').textContent = s.sidebarSub;
  if (document.getElementById('lbl-speed')) document.getElementById('lbl-speed').textContent = s.lblSpeed;
  if (document.getElementById('lbl-jump')) document.getElementById('lbl-jump').textContent = s.lblJump;
  if (document.getElementById('lbl-gravity')) document.getElementById('lbl-gravity').textContent = s.lblGravity;
  if (document.getElementById('preset-title')) document.getElementById('preset-title').textContent = s.presets;
  if (document.getElementById('p-moon')) document.getElementById('p-moon').textContent = s.pMoon;
  if (document.getElementById('p-sonic')) document.getElementById('p-sonic').textContent = s.pSonic;
  if (document.getElementById('p-heavy')) document.getElementById('p-heavy').textContent = s.pHeavy;
  if (document.getElementById('p-default')) document.getElementById('p-default').textContent = s.pDefault;
  if (document.getElementById('ai-title')) document.getElementById('ai-title').textContent = s.aiTitle;
  if (document.getElementById('ai-prompt')) document.getElementById('ai-prompt').textContent = s.aiPrompt;
  updateGroundStatusText();
  updateFullscreenUI();
}

function toggleFullscreen() {
  const container = document.querySelector('.game-container');
  if (!container) return;
  if (!document.fullscreenElement && !document.webkitFullscreenElement) {
    if (container.requestFullscreen) {
      container.requestFullscreen();
    } else if (container.webkitRequestFullscreen) {
      container.webkitRequestFullscreen();
    }
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
    }
  }
}

function updateFullscreenUI() {
  const isFS = !!(document.fullscreenElement || document.webkitFullscreenElement);
  const container = document.querySelector('.game-container');
  const btn = document.getElementById('btn-fullscreen');
  const s = STRINGS[currentLang] || STRINGS.ru;

  if (container) {
    container.classList.toggle('is-fullscreen', isFS);
  }
  if (btn) {
    if (isFS) {
      btn.innerHTML = `🗗 <span id="fs-label">${s.fsExit || 'ВЫЙТИ'}</span>`;
      btn.classList.add('is-active');
    } else {
      btn.innerHTML = `⛶ <span id="fs-label">${s.fsEnter || 'ЭКРАН'}</span>`;
      btn.classList.remove('is-active');
    }
  }
}

document.addEventListener('fullscreenchange', updateFullscreenUI);
document.addEventListener('webkitfullscreenchange', updateFullscreenUI);

function updateGroundStatusText() {
  const s = STRINGS[currentLang] || STRINGS.ru;
  groundStatusDisplay.textContent = player.isGrounded ? s.grounded : s.airborne;
  groundStatusDisplay.className = player.isGrounded ? "tag-ground" : "";
}

// HUD ELEMENTS
const posXDisplay = document.getElementById("pos-x");
const posYDisplay = document.getElementById("pos-y");
const groundStatusDisplay = document.getElementById("ground-status");
const fpsDisplay = document.getElementById("fps-display");

// SLIDERS & CONTROLS
const sliderSpeed = document.getElementById("slider-speed");
const sliderJump = document.getElementById("slider-jump");
const sliderGravity = document.getElementById("slider-gravity");

const valSpeed = document.getElementById("val-speed");
const valJump = document.getElementById("val-jump");
const valGravity = document.getElementById("val-gravity");

// ==========================================
// 1. GEYM-DIZAYN FIZIK PARAMETRLARI
// ==========================================
let player = {
  x: 80,
  y: 300,
  width: 28,
  height: 42,
  speed: parseFloat(sliderSpeed.value),
  jumpForce: parseFloat(sliderJump.value),
  gravity: parseFloat(sliderGravity.value),
  vx: 0,
  vy: 0,
  isGrounded: false,
  color: "#00F0FF",
  jumpCount: 0,
  maxJumps: 2
};

// PLATFORMS
const platforms = [
  { x: 0, y: 380, width: 760, height: 60, color: "#162B4D" }, // Floor
  { x: 180, y: 280, width: 130, height: 16, color: "#00F0FF" },
  { x: 370, y: 210, width: 140, height: 16, color: "#00FF9D" },
  { x: 570, y: 150, width: 120, height: 16, color: "#FF2A1B" }
];

// COLLECTIBLE COINS
let coins = [
  { x: 235, y: 245, r: 8, collected: false },
  { x: 435, y: 175, r: 8, collected: false },
  { x: 625, y: 115, r: 8, collected: false }
];

// PARTICLES
let particles = [];

// ==========================================
// 2. INPUT BOSHQARUVI (KLAVIATURA)
// ==========================================
const keys = { left: false, right: false, up: false };

window.addEventListener("keydown", (e) => {
  if (e.code === "KeyA" || e.code === "ArrowLeft") keys.left = true;
  if (e.code === "KeyD" || e.code === "ArrowRight") keys.right = true;
  if (e.code === "Space" || e.code === "KeyW" || e.code === "ArrowUp") {
    e.preventDefault();
    handleJump();
  }
  if (e.code === "KeyM") {
    e.preventDefault();
    toggleFullscreen();
  }
});

window.addEventListener("keyup", (e) => {
  if (e.code === "KeyA" || e.code === "ArrowLeft") keys.left = false;
  if (e.code === "KeyD" || e.code === "ArrowRight") keys.right = false;
});

function handleJump() {
  if (player.isGrounded || player.jumpCount < player.maxJumps) {
    player.vy = -player.jumpForce;
    player.isGrounded = false;
    player.jumpCount++;
    spawnParticles(player.x + player.width / 2, player.y + player.height, "#00F0FF", 8);
  }
}

// ==========================================
// 3. SLIDER EVENTS & PRESETS
// ==========================================
sliderSpeed.addEventListener("input", () => {
  player.speed = parseFloat(sliderSpeed.value);
  valSpeed.textContent = player.speed;
});
sliderJump.addEventListener("input", () => {
  player.jumpForce = parseFloat(sliderJump.value);
  valJump.textContent = player.jumpForce;
});
sliderGravity.addEventListener("input", () => {
  player.gravity = parseFloat(sliderGravity.value);
  valGravity.textContent = player.gravity;
});

function setPreset(type) {
  if (type === "moon") {
    sliderSpeed.value = 5;
    sliderJump.value = 16;
    sliderGravity.value = 0.2;
  } else if (type === "sonic") {
    sliderSpeed.value = 14;
    sliderJump.value = 15;
    sliderGravity.value = 0.8;
  } else if (type === "heavy") {
    sliderSpeed.value = 4;
    sliderJump.value = 8;
    sliderGravity.value = 1.4;
  } else {
    sliderSpeed.value = 6;
    sliderJump.value = 13;
    sliderGravity.value = 0.6;
  }
  player.speed = parseFloat(sliderSpeed.value);
  player.jumpForce = parseFloat(sliderJump.value);
  player.gravity = parseFloat(sliderGravity.value);
  valSpeed.textContent = player.speed;
  valJump.textContent = player.jumpForce;
  valGravity.textContent = player.gravity;
}

// ==========================================
// 4. CORE GAME LOOP (UPDATE & RENDER)
// ==========================================
let lastTime = performance.now();
let frames = 0;
let lastFpsUpdate = performance.now();

function gameLoop(timestamp) {
  // Update Physics
  update();

  // Render Frame
  render();

  // FPS Counter
  frames++;
  if (timestamp - lastFpsUpdate >= 500) {
    fpsDisplay.textContent = Math.round((frames * 1000) / (timestamp - lastFpsUpdate));
    frames = 0;
    lastFpsUpdate = timestamp;
  }

  requestAnimationFrame(gameLoop);
}

function update() {
  // 1. Horizontal movement
  if (keys.left) player.vx = -player.speed;
  else if (keys.right) player.vx = player.speed;
  else player.vx = 0;

  player.x += player.vx;

  // Screen Boundaries
  if (player.x < 0) player.x = 0;
  if (player.x + player.width > canvas.width) player.x = canvas.width - player.width;

  // 2. Gravity & Vertical movement
  player.vy += player.gravity;
  player.y += player.vy;

  // 3. Platform Collision (Hitbox Ground Detection)
  player.isGrounded = false;
  platforms.forEach(plat => {
    if (
      player.x + player.width > plat.x &&
      player.x < plat.x + plat.width &&
      player.y + player.height >= plat.y &&
      player.y + player.height <= plat.y + 24 &&
      player.vy >= 0
    ) {
      player.y = plat.y - player.height;
      player.vy = 0;
      player.isGrounded = true;
      player.jumpCount = 0;
    }
  });

  // Coin Collection
  coins.forEach(c => {
    if (!c.collected) {
      const dx = (player.x + player.width / 2) - c.x;
      const dy = (player.y + player.height / 2) - c.y;
      if (Math.sqrt(dx * dx + dy * dy) < player.width / 2 + c.r) {
        c.collected = true;
        spawnParticles(c.x, c.y, "#FFD700", 12);
      }
    }
  });

  // Trail particles while running
  if (player.isGrounded && Math.abs(player.vx) > 0 && Math.random() < 0.3) {
    spawnParticles(player.x + player.width / 2, player.y + player.height, "#00F0FF", 1);
  }

  // Update particles
  particles.forEach((p, idx) => {
    p.x += p.vx;
    p.y += p.vy;
    p.alpha -= 0.03;
    if (p.alpha <= 0) particles.splice(idx, 1);
  });

  // Update HUD values
  posXDisplay.textContent = Math.round(player.x);
  posYDisplay.textContent = Math.round(player.y);
  groundStatusDisplay.textContent = player.isGrounded ? "YERDA" : "HAVODA";
  groundStatusDisplay.className = player.isGrounded ? "tag-ground" : "";
}

function spawnParticles(x, y, color, count) {
  for (let i = 0; i < count; i++) {
    particles.push({
      x, y,
      vx: (Math.random() - 0.5) * 4,
      vy: (Math.random() - 0.8) * 3,
      size: Math.random() * 4 + 2,
      color,
      alpha: 1
    });
  }
}

function render() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Background Grid Lines
  ctx.strokeStyle = "rgba(0, 240, 255, 0.05)";
  ctx.lineWidth = 1;
  for (let x = 0; x < canvas.width; x += 40) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
  }
  for (let y = 0; y < canvas.height; y += 40) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
  }

  // Draw Platforms
  platforms.forEach(plat => {
    ctx.fillStyle = plat.color;
    ctx.fillRect(plat.x, plat.y, plat.width, plat.height);
    // Neon top border
    ctx.fillStyle = "#00F0FF";
    ctx.fillRect(plat.x, plat.y, plat.width, 2);
  });

  // Draw Coins
  coins.forEach(c => {
    if (!c.collected) {
      ctx.fillStyle = "#FFD700";
      ctx.beginPath();
      ctx.arc(c.x, c.y, c.r, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#FFF";
      ctx.lineWidth = 2;
      ctx.stroke();
    }
  });

  // Draw Particles
  particles.forEach(p => {
    ctx.save();
    ctx.globalAlpha = p.alpha;
    ctx.fillStyle = p.color;
    ctx.fillRect(p.x, p.y, p.size, p.size);
    ctx.restore();
  });

  // Draw Player (Cyber Ninja Avatar)
  ctx.save();
  ctx.fillStyle = player.color;
  ctx.shadowColor = player.color;
  ctx.shadowBlur = 12;
  ctx.fillRect(player.x, player.y, player.width, player.height);
  // Visor
  ctx.fillStyle = "#FFFFFF";
  ctx.fillRect(player.x + 6, player.y + 8, player.width - 12, 6);
  ctx.restore();
}

// Initialize Language & Start Game Loop
setLang('ru');
requestAnimationFrame(gameLoop);
