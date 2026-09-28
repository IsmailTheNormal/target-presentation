// ==========================================
// TARGET CYBER RUNNER 2.0: HAZARDS & LIVES
// 2D Physics, AABB Collisions, Hazards & Win State
// ==========================================

let currentLang = 'ru';

const STRINGS = {
  ru: {
    sidebarTitle: "⚙️ Полоса Препятствий",
    sidebarSub: "Настройте сложность и параметры ловушек для тестирования баланса:",
    lblDiff: "Режим сложности:",
    diffEasy: "🟢 Легко",
    diffNormal: "🟡 Норма",
    diffHard: "🔴 Хардкор",
    lblLaser: "⚡ Скорость лазера:",
    lblIframes: "🛡️ Неуязвимость (i-Frames):",
    lblJump: "🚀 Сила прыжка:",
    aiTitle: "🤖 Промпт для AI (ChatGPT / Claude):",
    aiPrompt: '"В игре Cyber Runner на JavaScript добавь звук сирены при столкновении с шипами и покачивание экрана (Screen Shake)"',
    controlsText: "🎮 <b>Управление:</b> [A] / [D] или [←] [→] — Бег &nbsp;|&nbsp; [ПРОБЕЛ] — Прыжок &nbsp;|&nbsp; [R] — Рестарт &nbsp;|&nbsp; [M] — Экран",
    checkpointHint: "🏁 <b>Цель:</b> Зелёный портал справа",
    statusSafe: "В НОРМЕ",
    statusDamage: "УРОН!",
    statusInvincible: "ЗАЩИТА",
    livesLabel: "ЖИЗНИ:",
    fsEnter: "ЭКРАН",
    fsExit: "ВЫЙТИ",
    goTitle: "СИСТЕМА ПОВРЕЖДЕНА!",
    goDesc: "Все жизни потрачены. Шипы или лазеры оказались сильнее. Попробуйте еще раз с новыми силами!",
    goRestart: "🔄 Повторить попытку",
    vicTitle: "УРОВЕНЬ ПРОЙДЕН! ПОБЕДА!",
    vicDesc: "Вы успешно преодолели все шипы, проскочили сквозь лазеры и добрались до квантового портала!",
    vicPlayAgain: "⭐ Пройти ещё раз",
    statTime: "Время:",
    statLives: "Осталось жизней:",
    statCoins: "Кристаллы:",
    unitSec: "сек"
  },
  en: {
    sidebarTitle: "⚙️ Obstacle Course Studio",
    sidebarSub: "Tweak hazard intensity and mechanics to benchmark game balance:",
    lblDiff: "Difficulty Mode:",
    diffEasy: "🟢 Easy",
    diffNormal: "🟡 Normal",
    diffHard: "🔴 Hardcore",
    lblLaser: "⚡ Laser Speed:",
    lblIframes: "🛡️ Invincibility (i-Frames):",
    lblJump: "🚀 Jump Impulse:",
    aiTitle: "🤖 Prompt for AI (ChatGPT / Claude):",
    aiPrompt: '"In our 2D Cyber Runner, add an audible warning siren when taking spike damage along with a violent screen shake"',
    controlsText: "🎮 <b>Controls:</b> [A] / [D] or [←] [→] — Run &nbsp;|&nbsp; [SPACE] — Jump &nbsp;|&nbsp; [R] — Restart &nbsp;|&nbsp; [M] — Fullscreen",
    checkpointHint: "🏁 <b>Goal:</b> Reach the green portal",
    statusSafe: "SAFE",
    statusDamage: "DAMAGE!",
    statusInvincible: "I-FRAMES",
    livesLabel: "LIVES:",
    fsEnter: "FULLSCREEN",
    fsExit: "EXIT",
    goTitle: "SYSTEM COMPROMISED!",
    goDesc: "All health points depleted! Trap hazards proved fatal. Regroup and attempt the trial again!",
    goRestart: "🔄 Retry Obstacle Run",
    vicTitle: "LEVEL CLEARED! VICTORY!",
    vicDesc: "Superb execution! You braved the spike beds, outmaneuvered pulsed lasers, and accessed the portal!",
    vicPlayAgain: "⭐ Play Again",
    statTime: "Time:",
    statLives: "Lives Remaining:",
    statCoins: "Crystals:",
    unitSec: "sec"
  },
  uz: {
    sidebarTitle: "⚙️ To'siqlar Maydoni Sozlamasi",
    sidebarSub: "Qiyinchilik darajasi va xavfli to'siq parametrlarini sozlang:",
    lblDiff: "Qiyinchilik rejimi:",
    diffEasy: "🟢 Oson",
    diffNormal: "🟡 O'rtacha",
    diffHard: "🔴 Qiyin",
    lblLaser: "⚡ Lazer tezligi:",
    lblIframes: "🛡️ O'lmaslik vaqti (i-Frames):",
    lblJump: "🚀 Sakrash kuchi:",
    aiTitle: "🤖 AI uchun Prompt (ChatGPT / Claude):",
    aiPrompt: '"JavaScript Cyber Runner o\'yinida tikanga tekkanda signal ovozi chiqsin va ekran larzaga kelsin (Screen Shake)"',
    controlsText: "🎮 <b>Boshqaruv:</b> [A] / [D] yoki [←] [→] — Yugurish &nbsp;|&nbsp; [BO'SHLIQ] — Sakrash &nbsp;|&nbsp; [R] — Qayta &nbsp;|&nbsp; [M] — To'liq ekran",
    checkpointHint: "🏁 <b>Maqsad:</b> O'ng tomondagi yashil portal",
    statusSafe: "XAVFSIZ",
    statusDamage: "ZARBA!",
    statusInvincible: "HIMOYA",
    livesLabel: "JONLAR:",
    fsEnter: "TO'LIQ EKRAN",
    fsExit: "CHIQISH",
    goTitle: "TIZIM ZARARLANDI!",
    goDesc: "Barcha jonlar tugadi. Tikanlar yoki lazer to'siqlari g'olib keldi. Qaytadan urinib ko'ring!",
    goRestart: "🔄 Qayta Boshlash",
    vicTitle: "BOSQICH BOSIB O'TILDI! G'ALABA!",
    vicDesc: "Ajoyib mahorat! Barcha xavfli tikanlar va lazerlardan o'tib, kvant portaliga yetib keldingiz!",
    vicPlayAgain: "⭐ Qayta O'ynash",
    statTime: "Vaqt:",
    statLives: "Qolgan jonlar:",
    statCoins: "Kristallar:",
    unitSec: "soniya"
  }
};

function setLang(l) {
  currentLang = l;
  document.querySelectorAll('.btn-lang').forEach(b => b.classList.remove('is-active'));
  const activeBtn = document.getElementById('btn-' + l);
  if (activeBtn) activeBtn.classList.add('is-active');

  const s = STRINGS[l] || STRINGS.ru;
  document.getElementById('sidebar-title').innerHTML = s.sidebarTitle;
  document.getElementById('sidebar-sub').innerHTML = s.sidebarSub;
  document.getElementById('lbl-diff').innerHTML = s.lblDiff;
  document.getElementById('d-easy').innerHTML = s.diffEasy;
  document.getElementById('d-normal').innerHTML = s.diffNormal;
  document.getElementById('d-hard').innerHTML = s.diffHard;
  document.getElementById('lbl-laser').innerHTML = s.lblLaser;
  document.getElementById('lbl-iframes').innerHTML = s.lblIframes;
  document.getElementById('lbl-jump').innerHTML = s.lblJump;
  document.getElementById('ai-title').innerHTML = s.aiTitle;
  document.getElementById('ai-prompt').innerText = s.aiPrompt;
  document.getElementById('controls-text').innerHTML = s.controlsText;
  const cpHint = document.getElementById('checkpoint-hint');
  if (cpHint) cpHint.innerHTML = s.checkpointHint;
  document.getElementById('lives-label').innerText = s.livesLabel;
  document.getElementById('go-title').innerText = s.goTitle;
  document.getElementById('go-desc').innerText = s.goDesc;
  document.getElementById('btn-restart').innerText = s.goRestart;
  document.getElementById('vic-title').innerText = s.vicTitle;
  document.getElementById('vic-desc').innerText = s.vicDesc;
  document.getElementById('btn-playagain').innerText = s.vicPlayAgain;

  updateHUD();
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

// CANVAS & CORE STATE
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let gameState = 'playing'; // 'playing', 'gameover', 'victory'
let startTime = Date.now();
let finishTime = 0;

// GAME CONFIG & VARIABLES
const config = {
  gravity: 0.65,
  speed: 6.0,
  jumpForce: 13.0,
  laserSpeed: 2.5,
  invincibilityDuration: 72 // frames (~1.2s at 60fps)
};

// PLAYER OBJECT
const player = {
  startX: 40,
  startY: 330,
  x: 40,
  y: 330,
  w: 28,
  h: 38,
  vx: 0,
  vy: 0,
  isGrounded: false,
  lives: 3,
  maxLives: 3,
  invincibleTimer: 0,
  facing: 1 // 1 = right, -1 = left
};

// CONTROLS
const keys = {
  left: false,
  right: false,
  jump: false
};

window.addEventListener('keydown', (e) => {
  if (['Space', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.code)) {
    e.preventDefault();
  }
  if (e.code === 'KeyD' || e.code === 'ArrowRight') keys.right = true;
  if (e.code === 'KeyA' || e.code === 'ArrowLeft') keys.left = true;
  if (e.code === 'Space' || e.code === 'KeyW' || e.code === 'ArrowUp') {
    if (!keys.jump && player.isGrounded && gameState === 'playing') {
      player.vy = -config.jumpForce;
      player.isGrounded = false;
      spawnJumpDust(player.x + player.w / 2, player.y + player.h);
    }
    keys.jump = true;
  }
  if (e.code === 'KeyR') {
    restartLevel();
  }
  if (e.code === 'KeyM') {
    e.preventDefault();
    toggleFullscreen();
  }
});

window.addEventListener('keyup', (e) => {
  if (e.code === 'KeyD' || e.code === 'ArrowRight') keys.right = false;
  if (e.code === 'KeyA' || e.code === 'ArrowLeft') keys.left = false;
  if (e.code === 'Space' || e.code === 'KeyW' || e.code === 'ArrowUp') keys.jump = false;
});

// PLATFORMS
// Notice: there is a pit gap between x: 290 and 370!
let platforms = [
  { x: 0, y: 390, w: 290, h: 50 },    // Start platform
  { x: 370, y: 390, w: 390, h: 50 },  // Main landing floor
  { x: 190, y: 300, w: 120, h: 18 },  // High ledge 1
  { x: 340, y: 240, w: 130, h: 18 },  // Mid float ledge
  { x: 500, y: 290, w: 110, h: 18 }   // High ledge 2
];

// HAZARDS: SPIKES
// Sharp deadly triangles. Touching without i-frames causes damage!
let spikes = [
  { x: 230, y: 390, w: 40, h: 20 },   // Spike cluster 1 near edge
  { x: 370, y: 240, w: 30, h: 18 },   // Spike on mid ledge
  { x: 540, y: 390, w: 50, h: 20 }    // Spike bed near finish
];

// HAZARDS: MOVING LASERS
let lasers = [
  {
    x: 480,
    y: 140,
    w: 8,
    h: 150,
    minY: 100,
    maxY: 240,
    vy: 2.5,
    dir: 1,
    color: '#ff2a5f'
  }
];

// COLLECTIBLES (Crystals)
let crystals = [
  { x: 245, y: 260, w: 18, h: 18, collected: false, floatOffset: 0 },
  { x: 405, y: 200, w: 18, h: 18, collected: false, floatOffset: 2 },
  { x: 550, y: 250, w: 18, h: 18, collected: false, floatOffset: 4 }
];

// FINISH PORTAL
const portal = {
  x: 700,
  y: 320,
  w: 36,
  h: 70,
  glow: 0
};

// VISUAL FX (Particles & Screen Shake)
let particles = [];
let screenShake = 0;

function spawnDamageSparks(x, y) {
  for (let i = 0; i < 20; i++) {
    const angle = Math.random() * Math.PI * 2;
    const speed = 2 + Math.random() * 5;
    particles.push({
      x: x,
      y: y,
      vx: Math.cos(angle) * speed,
      vy: Math.sin(angle) * speed,
      color: Math.random() > 0.5 ? '#ff2a5f' : '#ffd700',
      size: 3 + Math.random() * 3,
      alpha: 1.0,
      decay: 0.035
    });
  }
}

function spawnJumpDust(x, y) {
  for (let i = 0; i < 7; i++) {
    particles.push({
      x: x + (Math.random() - 0.5) * 14,
      y: y,
      vx: (Math.random() - 0.5) * 3,
      vy: -Math.random() * 1.5,
      color: '#00e5ff',
      size: 2.5,
      alpha: 0.8,
      decay: 0.04
    });
  }
}

function spawnPortalAura(x, y) {
  if (Math.random() > 0.4) {
    particles.push({
      x: x + (Math.random() - 0.5) * 20,
      y: y + Math.random() * 60,
      vx: (Math.random() - 0.5) * 1.5,
      vy: -1 - Math.random() * 1.5,
      color: '#00ff88',
      size: 3,
      alpha: 0.9,
      decay: 0.03
    });
  }
}

// TAKE DAMAGE MECHANISM
function takeDamage(pushbackDir = -1) {
  if (player.invincibleTimer > 0 || gameState !== 'playing') return;

  player.lives--;
  player.invincibleTimer = config.invincibilityDuration;
  screenShake = 14; // violent screen shake
  spawnDamageSparks(player.x + player.w / 2, player.y + player.h / 2);

  // Knockback physics impulse
  player.vy = -7.5;
  player.vx = pushbackDir * 6.5;
  player.isGrounded = false;

  updateHUD();

  if (player.lives <= 0) {
    triggerGameOver();
  }
}

// AABB COLLISION DETECTION
function checkAABB(r1, r2) {
  return (
    r1.x < r2.x + r2.w &&
    r1.x + r1.w > r2.x &&
    r1.y < r2.y + r2.h &&
    r1.y + r1.h > r2.y
  );
}

// GAME OVER & VICTORY HANDLERS
function triggerGameOver() {
  gameState = 'gameover';
  const overlay = document.getElementById('overlay-gameover');
  if (overlay) {
    overlay.hidden = false;
    const s = STRINGS[currentLang] || STRINGS.ru;
    const coinsCount = crystals.filter(c => c.collected).length;
    document.getElementById('go-distance').innerHTML = `${s.statLives} <b>0 / ${player.maxLives}</b>`;
    document.getElementById('go-coins').innerHTML = `${s.statCoins} <b>${coinsCount} / ${crystals.length}</b>`;
  }
}

function triggerVictory() {
  gameState = 'victory';
  finishTime = ((Date.now() - startTime) / 1000).toFixed(1);
  const overlay = document.getElementById('overlay-victory');
  if (overlay) {
    overlay.hidden = false;
    const s = STRINGS[currentLang] || STRINGS.ru;
    const coinsCount = crystals.filter(c => c.collected).length;
    document.getElementById('stat-time').innerText = finishTime + ' ' + s.unitSec;
    document.getElementById('stat-lives').innerText = `${player.lives} / ${player.maxLives}`;
    document.getElementById('stat-coins').innerText = `${coinsCount} / ${crystals.length}`;
  }
}

function restartLevel() {
  player.x = player.startX;
  player.y = player.startY;
  player.vx = 0;
  player.vy = 0;
  player.lives = player.maxLives;
  player.invincibleTimer = 0;
  player.isGrounded = false;
  gameState = 'playing';
  startTime = Date.now();
  particles = [];
  screenShake = 0;

  crystals.forEach(c => c.collected = false);

  document.getElementById('overlay-gameover').hidden = true;
  document.getElementById('overlay-victory').hidden = true;

  updateHUD();
}

// UPDATE HUD (HEARTS & STATS)
function updateHUD() {
  const heartWrap = document.getElementById('hud-lives');
  if (heartWrap) {
    let html = `<span id="lives-label">${(STRINGS[currentLang] || STRINGS.ru).livesLabel}</span> `;
    for (let i = 1; i <= player.maxLives; i++) {
      if (i <= player.lives) {
        html += `<span class="heart" id="heart-${i}">❤️</span> `;
      } else {
        html += `<span class="heart is-empty" id="heart-${i}">🖤</span> `;
      }
    }
    heartWrap.innerHTML = html;
  }

  const statusEl = document.getElementById('status-display');
  const s = STRINGS[currentLang] || STRINGS.ru;
  if (statusEl) {
    if (player.invincibleTimer > 0) {
      statusEl.innerText = s.statusInvincible;
      statusEl.className = 'tag-hazard';
    } else {
      statusEl.innerText = s.statusSafe;
      statusEl.className = 'tag-ground';
    }
  }
}

// DIFFICULTY PRESETS
function setDifficulty(level) {
  document.querySelectorAll('.btn-diff').forEach(b => b.classList.remove('is-active'));
  const btn = document.getElementById('d-' + level);
  if (btn) btn.classList.add('is-active');

  if (level === 'easy') {
    player.maxLives = 5;
    player.lives = 5;
    config.laserSpeed = 1.5;
    config.invincibilityDuration = 90; // 1.5s
    spikes = [
      { x: 230, y: 390, w: 35, h: 20 },
      { x: 540, y: 390, w: 40, h: 20 }
    ];
  } else if (level === 'normal') {
    player.maxLives = 3;
    player.lives = 3;
    config.laserSpeed = 2.5;
    config.invincibilityDuration = 72; // 1.2s
    spikes = [
      { x: 230, y: 390, w: 40, h: 20 },
      { x: 370, y: 240, w: 30, h: 18 },
      { x: 540, y: 390, w: 50, h: 20 }
    ];
  } else if (level === 'hard') {
    player.maxLives = 1;
    player.lives = 1;
    config.laserSpeed = 4.5;
    config.invincibilityDuration = 45; // 0.75s
    spikes = [
      { x: 190, y: 390, w: 70, h: 20 },
      { x: 370, y: 240, w: 45, h: 18 },
      { x: 520, y: 390, w: 75, h: 20 }
    ];
  }

  // Update slider UI
  document.getElementById('slider-laser').value = config.laserSpeed;
  document.getElementById('val-laser').innerText = config.laserSpeed;
  const u = (STRINGS[currentLang] || STRINGS.ru).unitSec;
  document.getElementById('slider-iframes').value = (config.invincibilityDuration / 60).toFixed(1);
  document.getElementById('val-iframes').innerText = (config.invincibilityDuration / 60).toFixed(1) + ' ' + u;

  restartLevel();
}

// SLIDER EVENT LISTENERS
document.getElementById('slider-laser').addEventListener('input', (e) => {
  config.laserSpeed = parseFloat(e.target.value);
  document.getElementById('val-laser').innerText = config.laserSpeed;
});

document.getElementById('slider-iframes').addEventListener('input', (e) => {
  const secs = parseFloat(e.target.value);
  config.invincibilityDuration = Math.round(secs * 60);
  const u = (STRINGS[currentLang] || STRINGS.ru).unitSec;
  document.getElementById('val-iframes').innerText = secs + ' ' + u;
});

document.getElementById('slider-jump').addEventListener('input', (e) => {
  config.jumpForce = parseFloat(e.target.value);
  document.getElementById('val-jump').innerText = config.jumpForce;
});

// MAIN GAME LOOP (60 FPS)
let lastFrameTime = performance.now();
let fpsCount = 0;
let fpsTimer = 0;

function updatePhysics() {
  if (gameState !== 'playing') return;

  // Horizontal motion (preserve knockback impulse during initial 10 frames of hit)
  const isKnockback = player.invincibleTimer > config.invincibilityDuration - 10;
  if (!isKnockback) {
    if (keys.right) {
      player.vx = config.speed;
      player.facing = 1;
    } else if (keys.left) {
      player.vx = -config.speed;
      player.facing = -1;
    } else {
      player.vx *= 0.75; // ground/air friction
      if (Math.abs(player.vx) < 0.2) player.vx = 0;
    }
  }

  player.x += player.vx;

  // Horizontal boundaries
  if (player.x < 0) player.x = 0;
  if (player.x + player.w > canvas.width) player.x = canvas.width - player.w;

  // Apply gravity
  player.vy += config.gravity;
  player.y += player.vy;

  // Invincibility countdown
  if (player.invincibleTimer > 0) {
    player.invincibleTimer--;
    if (player.invincibleTimer === 0) updateHUD();
  }

  // PLATFORM COLLISIONS
  player.isGrounded = false;
  for (const plat of platforms) {
    if (
      player.x + player.w > plat.x &&
      player.x < plat.x + plat.w &&
      player.y + player.h >= plat.y &&
      player.y + player.h <= plat.y + 16 &&
      player.vy >= 0
    ) {
      player.y = plat.y - player.h;
      player.vy = 0;
      player.isGrounded = true;
    }
  }

  // PIT HAZARD (Fell into the void!)
  if (player.y > canvas.height + 20) {
    takeDamage(-player.facing);
    player.x = 80;
    player.y = 300;
    player.vy = 0;
  }

  // MOVING LASERS UPDATE & COLLISION
  for (const laser of lasers) {
    laser.y += laser.vy * laser.dir * (config.laserSpeed / 2.5);
    if (laser.y > laser.maxY) {
      laser.y = laser.maxY;
      laser.dir = -1;
    } else if (laser.y < laser.minY) {
      laser.y = laser.minY;
      laser.dir = 1;
    }

    // Laser collision box
    if (checkAABB(player, laser)) {
      takeDamage(player.x < laser.x ? -1 : 1);
    }
  }

  // SPIKES COLLISION
  for (const spike of spikes) {
    // Tighten spike hitbox slightly so player doesn't clip on thin air
    const spikeHitbox = {
      x: spike.x + 4,
      y: spike.y - spike.h + 4,
      w: spike.w - 8,
      h: spike.h - 4
    };
    if (checkAABB(player, spikeHitbox)) {
      takeDamage(player.facing * -1);
    }
  }

  // CRYSTALS COLLECTION
  for (const c of crystals) {
    if (!c.collected) {
      c.floatOffset += 0.06;
      const crystalBox = {
        x: c.x,
        y: c.y + Math.sin(c.floatOffset) * 4,
        w: c.w,
        h: c.h
      };
      if (checkAABB(player, crystalBox)) {
        c.collected = true;
        for (let i = 0; i < 12; i++) {
          particles.push({
            x: c.x + c.w / 2,
            y: c.y + c.h / 2,
            vx: (Math.random() - 0.5) * 4,
            vy: (Math.random() - 0.5) * 4,
            color: '#ffd700',
            size: 3,
            alpha: 1,
            decay: 0.04
          });
        }
      }
    }
  }

  // FINISH PORTAL CHECK
  spawnPortalAura(portal.x + portal.w / 2, portal.y);
  if (checkAABB(player, portal)) {
    triggerVictory();
  }

  // PARTICLES UPDATE
  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.x += p.vx;
    p.y += p.vy;
    p.alpha -= p.decay;
    if (p.alpha <= 0) particles.splice(i, 1);
  }
}

// RENDER SCENE
function render() {
  ctx.save();

  // Screen shake effect
  if (screenShake > 0) {
    const ox = (Math.random() - 0.5) * screenShake;
    const oy = (Math.random() - 0.5) * screenShake;
    ctx.translate(ox, oy);
    screenShake *= 0.85;
    if (screenShake < 0.5) screenShake = 0;
  }

  // Clear Canvas
  ctx.fillStyle = '#050914';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Background Grid Lines
  ctx.strokeStyle = 'rgba(0, 229, 255, 0.04)';
  ctx.lineWidth = 1;
  for (let x = 0; x < canvas.width; x += 30) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, canvas.height);
    ctx.stroke();
  }
  for (let y = 0; y < canvas.height; y += 30) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(canvas.width, y);
    ctx.stroke();
  }

  // DRAW PIT HAZARD (Bottom void zone with red glowing gradient)
  const pitGrad = ctx.createLinearGradient(0, 390, 0, 440);
  pitGrad.addColorStop(0, 'rgba(255, 42, 95, 0.2)');
  pitGrad.addColorStop(1, 'rgba(255, 42, 95, 0.7)');
  ctx.fillStyle = pitGrad;
  ctx.fillRect(290, 410, 80, 30);

  // DRAW PLATFORMS
  for (const plat of platforms) {
    // Platform block
    ctx.fillStyle = '#0f1d33';
    ctx.fillRect(plat.x, plat.y, plat.w, plat.h);

    // Platform top neon trim
    ctx.fillStyle = '#00e5ff';
    ctx.fillRect(plat.x, plat.y, plat.w, 3);

    // Subtle edge highlight
    ctx.strokeStyle = '#1d3459';
    ctx.strokeRect(plat.x, plat.y, plat.w, plat.h);
  }

  // DRAW SPIKES (Red deadly neon triangles)
  for (const spike of spikes) {
    const spikeCount = Math.floor(spike.w / 12);
    const triWidth = spike.w / spikeCount;

    ctx.save();
    ctx.fillStyle = '#ff2a5f';
    ctx.shadowColor = '#ff2a5f';
    ctx.shadowBlur = 10;

    for (let k = 0; k < spikeCount; k++) {
      const sx = spike.x + k * triWidth;
      const sy = spike.y;
      ctx.beginPath();
      ctx.moveTo(sx, sy);
      ctx.lineTo(sx + triWidth / 2, sy - spike.h);
      ctx.lineTo(sx + triWidth, sy);
      ctx.closePath();
      ctx.fill();
    }
    ctx.restore();
  }

  // DRAW MOVING LASERS
  for (const laser of lasers) {
    ctx.save();
    // Emitter bases (top and bottom)
    ctx.fillStyle = '#223048';
    ctx.fillRect(laser.x - 6, laser.y - 8, laser.w + 12, 8);
    ctx.fillRect(laser.x - 6, laser.y + laser.h, laser.w + 12, 8);

    // Pulsing beam
    ctx.shadowColor = laser.color;
    ctx.shadowBlur = 15;
    ctx.fillStyle = laser.color;
    ctx.fillRect(laser.x, laser.y, laser.w, laser.h);

    // Inner bright core
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(laser.x + 2, laser.y, laser.w - 4, laser.h);
    ctx.restore();
  }

  // DRAW CRYSTALS
  for (const c of crystals) {
    if (!c.collected) {
      const cy = c.y + Math.sin(c.floatOffset) * 4;
      ctx.save();
      ctx.translate(c.x + c.w / 2, cy + c.h / 2);
      ctx.rotate(c.floatOffset * 0.5);
      ctx.shadowColor = '#ffd700';
      ctx.shadowBlur = 12;
      ctx.fillStyle = '#ffd700';

      // Diamond shape
      ctx.beginPath();
      ctx.moveTo(0, -c.h / 2);
      ctx.lineTo(c.w / 2, 0);
      ctx.lineTo(0, c.h / 2);
      ctx.lineTo(-c.w / 2, 0);
      ctx.closePath();
      ctx.fill();
      ctx.restore();
    }
  }

  // DRAW PORTAL (Green Dimensional Vortex)
  ctx.save();
  ctx.shadowColor = '#00ff88';
  ctx.shadowBlur = 20;
  ctx.strokeStyle = '#00ff88';
  ctx.lineWidth = 3;

  portal.glow += 0.05;
  const pulse = Math.sin(portal.glow) * 3;

  ctx.beginPath();
  ctx.ellipse(
    portal.x + portal.w / 2,
    portal.y + portal.h / 2,
    portal.w / 2 + pulse,
    portal.h / 2,
    0, 0, Math.PI * 2
  );
  ctx.stroke();

  // Swirling core
  ctx.fillStyle = 'rgba(0, 255, 136, 0.2)';
  ctx.fill();
  ctx.restore();

  // DRAW PARTICLES
  for (const p of particles) {
    ctx.save();
    ctx.globalAlpha = p.alpha;
    ctx.fillStyle = p.color;
    ctx.fillRect(p.x, p.y, p.size, p.size);
    ctx.restore();
  }

  // DRAW PLAYER (With i-Frames Flashing)
  if (gameState === 'playing' || gameState === 'victory') {
    ctx.save();

    // If in i-frames grace period, flash visibility
    if (player.invincibleTimer > 0) {
      const flash = Math.floor(player.invincibleTimer / 4) % 2;
      ctx.globalAlpha = flash === 0 ? 0.35 : 0.9;
    }

    // Player Body
    ctx.fillStyle = player.invincibleTimer > 0 ? '#ff2a5f' : '#00e5ff';
    ctx.shadowColor = player.invincibleTimer > 0 ? '#ff2a5f' : '#00e5ff';
    ctx.shadowBlur = 10;
    ctx.fillRect(player.x, player.y, player.w, player.h);

    // Player Visor
    ctx.fillStyle = '#ffffff';
    const visorX = player.facing === 1 ? player.x + player.w - 10 : player.x + 2;
    ctx.fillRect(visorX, player.y + 7, 8, 5);

    // Cyber Belt
    ctx.fillStyle = '#060c18';
    ctx.fillRect(player.x, player.y + 22, player.w, 4);

    ctx.restore();
  }

  ctx.restore();
}

function gameLoop(timestamp) {
  // Calculate FPS
  fpsCount++;
  if (timestamp - fpsTimer >= 1000) {
    document.getElementById('fps-display').innerText = fpsCount;
    fpsCount = 0;
    fpsTimer = timestamp;
  }

  updatePhysics();
  render();

  requestAnimationFrame(gameLoop);
}

// START ENGINE
setLang('ru');
updateHUD();
requestAnimationFrame(gameLoop);
