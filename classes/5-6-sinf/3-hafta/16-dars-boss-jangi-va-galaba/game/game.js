// ==========================================
// TARGET CYBER RUNNER 4.0: BOSS BATTLE & VICTORY
// Boss AI Phases, Lasers, Shields, Blasters & Fireworks
// ==========================================

let currentLang = 'ru';

const STRINGS = {
  ru: {
    sidebarTitle: "⚡ Битва с Боссом",
    sidebarSub: "Настройте параметры босса и вооружения героя для тестирования баланса:",
    lblDiff: "Режим битвы:",
    diffEasy: "🟢 Обычный",
    diffNormal: "🟡 Боевой",
    diffHard: "🔴 Рейд-Босс",
    lblBossHp: "👾 Здоровье босса:",
    lblBossRate: "⚡ Частота атак босса:",
    lblBlaster: "💥 Урон бластера игрока:",
    aiTitle: "🤖 Промпт для AI (ChatGPT / Claude):",
    aiPrompt: '"В игре на Canvas добавь 3-ю фазу босса: когда у него меньше 30% HP, он вызывает двух мини-дронов и экран мигает красным"',
    controlsText: "🎮 <b>Управление:</b> [A]/[D] — Бег &nbsp;|&nbsp; [ПРОБЕЛ] — Прыжок &nbsp;|&nbsp; [F] / Клик — Бластер &nbsp;|&nbsp; [E] — Щит &nbsp;|&nbsp; [M] — Экран",
    bossWeaknessHint: "🎯 <b>Совет:</b> Стреляйте снизу или прыгайте на голову босса!",
    livesLabel: "ЖИЗНИ:",
    shieldLabel: "ЩИТ [E]:",
    shieldReady: "ГОТОВ",
    shieldActive: "АКТИВЕН",
    shieldWait: "ОТКАТ...",
    fsEnter: "ЭКРАН",
    fsExit: "ВЫЙТИ",
    bossTitlePhase1: "⚠️ БОСС: КИБЕР-ГОЛИАФ (ФАЗА 1: ПАТРУЛЬ)",
    bossTitlePhase2: "🔥 БОСС: КИБЕР-ГОЛИАФ (ФАЗА 2: ЛАЗЕРНЫЙ ЗАЛП)",
    bossTitlePhase3: "⚡ БОСС: КИБЕР-ГОЛИАФ (ФАЗА 3: ЯРОСТЬ В ПОЛЁТЕ)",
    goTitle: "СИСТЕМА УНИЧТОЖЕНА!",
    goDesc: "Кибер-Голиаф сокрушил вашу оборону. Изучите траекторию его лазеров и попробуйте снова!",
    goRestart: "🔄 Начать бой заново [R]",
    goBossHp: "Осталось у босса:",
    goTime: "Время битвы:",
    vicTitle: "КИБЕР-ГОЛИАФ ПОВЕРЖЕН! ПОБЕДА!",
    vicDesc: "Вы сокрушили главного стража системы! Все квантовые порталы разблокированы! Поздравляем юного инженера!",
    vicPlayAgain: "⭐ Сыграть ещё раз [R]",
    statTime: "Время победы:",
    statLives: "Осталось жизней:",
    statAccuracy: "Меткость выстрелов:",
    unitSec: "сек"
  },
  en: {
    sidebarTitle: "⚡ Boss Battle Studio",
    sidebarSub: "Calibrate drone attack patterns, blaster stats, and shield parameters:",
    lblDiff: "Battle Difficulty:",
    diffEasy: "🟢 Casual",
    diffNormal: "🟡 Standard",
    diffHard: "🔴 Raid Boss",
    lblBossHp: "👾 Boss Max HP:",
    lblBossRate: "⚡ Boss Salvo Rate:",
    lblBlaster: "💥 Blaster Damage:",
    aiTitle: "🤖 Prompt for AI (ChatGPT / Claude):",
    aiPrompt: '"In our 2D HTML5 canvas game, design an enrage Phase 3 for the boss drone that drops quantum cluster bombs and flashes neon alert rings"',
    controlsText: "🎮 <b>Controls:</b> [A]/[D] — Run &nbsp;|&nbsp; [SPACE] — Jump &nbsp;|&nbsp; [F] / Click — Fire Blaster &nbsp;|&nbsp; [E] — Energy Shield &nbsp;|&nbsp; [M] — Fullscreen",
    bossWeaknessHint: "🎯 <b>Tactics:</b> Blast from below or stomp the drone chassis!",
    livesLabel: "LIVES:",
    shieldLabel: "SHIELD [E]:",
    shieldReady: "READY",
    shieldActive: "ACTIVE",
    shieldWait: "COOLDOWN",
    fsEnter: "FULLSCREEN",
    fsExit: "EXIT",
    bossTitlePhase1: "⚠️ BOSS: CYBER GOLIATH (PHASE 1: SWEEP)",
    bossTitlePhase2: "🔥 BOSS: CYBER GOLIATH (PHASE 2: BARRAGE)",
    bossTitlePhase3: "⚡ BOSS: CYBER GOLIATH (PHASE 3: ENRAGED)",
    goTitle: "SYSTEM COMPROMISED!",
    goDesc: "The Goliath neutralized your agent. Anticipate the vertical salvos and execute retaliation!",
    goRestart: "🔄 Restart Battle [R]",
    goBossHp: "Boss HP Left:",
    goTime: "Battle Time:",
    vicTitle: "CYBER GOLIATH DEFEATED! TRIUMPH!",
    vicDesc: "Phenomenal mastery! You extinguished the defense drone and unlocked the quantum terminus!",
    vicPlayAgain: "⭐ Play Again [R]",
    statTime: "Clear Time:",
    statLives: "Remaining Lives:",
    statAccuracy: "Blaster Accuracy:",
    unitSec: "sec"
  },
  uz: {
    sidebarTitle: "⚡ Boss Jangi Sozlamasi",
    sidebarSub: "Boss hujum chastotasi, qahramon blastek kuchi va qalqon vaqtini sozlang:",
    lblDiff: "Jang rejimi:",
    diffEasy: "🟢 Oson",
    diffNormal: "🟡 Jangovar",
    diffHard: "🔴 Reyd-Boss",
    lblBossHp: "👾 Bossning joni (HP):",
    lblBossRate: "⚡ Boss hujum tezligi:",
    lblBlaster: "💥 Blaster zarbasi kuchi:",
    aiTitle: "🤖 AI uchun Prompt (ChatGPT / Claude):",
    aiPrompt: `"Canvas o'yinida bossning 3-bosqichini qo'sh: jon 30% dan kam qolganda u pastga tushsin va lazerli klaster bombalar yog'dirsin"`,
    controlsText: "🎮 <b>Boshqaruv:</b> [A]/[D] — Yugurish &nbsp;|&nbsp; [BO'SHLIQ] — Sakrash &nbsp;|&nbsp; [F] / Bosish — Blaster &nbsp;|&nbsp; [E] — Qalqon &nbsp;|&nbsp; [M] — To'liq ekran",
    bossWeaknessHint: "🎯 <b>Maslahat:</b> Pastdan o'q uzing yoki bossning ustiga sakrab bosing!",
    livesLabel: "JONLAR:",
    shieldLabel: "QALQON [E]:",
    shieldReady: "TAYYOR",
    shieldActive: "FAOL",
    shieldWait: "KUTILMOQDA",
    fsEnter: "TO'LIQ EKRAN",
    fsExit: "CHIQISH",
    bossTitlePhase1: "⚠️ BOSS: KIBER-GIGANT (1-BOSQICH: PATRUL)",
    bossTitlePhase2: "🔥 BOSS: KIBER-GIGANT (2-BOSQICH: LAZER HUJUMI)",
    bossTitlePhase3: "⚡ BOSS: KIBER-GIGANT (3-BOSQICH: G'AZAB REJIMI)",
    goTitle: "TIZIM ZARARLANDI!",
    goDesc: "Kiber-Gigant himoyangizni yorib o'tdi. Lazerlar traektoriyasini tahlil qilib, qaytadan jangga kiring!",
    goRestart: "🔄 Qaytadan Boshlash [R]",
    goBossHp: "Bossning qolgan joni:",
    goTime: "Jang vaqti:",
    vicTitle: "KIBER-GIGANT MAG'LUB ETILDI! G'ALABA!",
    vicDesc: "Bosh dushman yo'q qilindi! Barcha kvant portallari ochildi! Yosh muhandisni buyuk g'alaba bilan tabriklaymiz!",
    vicPlayAgain: "⭐ Yana O'ynash [R]",
    statTime: "G'alaba vaqti:",
    statLives: "Qolgan jonlar:",
    statAccuracy: "O'q aniqligi:",
    unitSec: "soniya"
  }
};

function setLang(lang) {
  currentLang = lang;
  document.querySelectorAll('.btn-lang').forEach(b => b.classList.remove('is-active'));
  const btn = document.getElementById(`btn-${lang}`);
  if (btn) btn.classList.add('is-active');

  const s = STRINGS[lang];
  document.getElementById('sidebar-title').textContent = s.sidebarTitle;
  document.getElementById('sidebar-sub').textContent = s.sidebarSub;
  document.getElementById('lbl-diff').textContent = s.lblDiff;
  document.getElementById('d-easy').textContent = s.diffEasy;
  document.getElementById('d-normal').textContent = s.diffNormal;
  document.getElementById('d-hard').textContent = s.diffHard;
  document.getElementById('lbl-bosshp').textContent = s.lblBossHp;
  document.getElementById('lbl-bossrate').textContent = s.lblBossRate;
  document.getElementById('lbl-blaster').textContent = s.lblBlaster;
  document.getElementById('ai-title').textContent = s.aiTitle;
  document.getElementById('ai-prompt').textContent = s.aiPrompt;
  document.getElementById('controls-text').innerHTML = s.controlsText;
  document.getElementById('boss-weakness-hint').innerHTML = s.bossWeaknessHint;
  document.getElementById('lives-label').textContent = s.livesLabel;
  document.getElementById('shield-label').textContent = s.shieldLabel;
  document.getElementById('go-title').textContent = s.goTitle;
  document.getElementById('go-desc').textContent = s.goDesc;
  document.getElementById('btn-restart').textContent = s.goRestart;
  document.getElementById('vic-title').textContent = s.vicTitle;
  document.getElementById('vic-desc').textContent = s.vicDesc;
  document.getElementById('btn-playagain').textContent = s.vicPlayAgain;

  const goBossVal = document.getElementById('go-boss-val');
  const goTimeVal = document.getElementById('go-time-val');
  if (document.getElementById('go-boss-hp')) {
    document.getElementById('go-boss-hp').innerHTML = `${s.goBossHp} <b id="go-boss-val">${goBossVal ? goBossVal.textContent : Math.ceil(bossHP) + ' HP'}</b>`;
  }
  if (document.getElementById('go-time')) {
    document.getElementById('go-time').innerHTML = `${s.goTime} <b id="go-time-val">${goTimeVal ? goTimeVal.textContent : gameTime.toFixed(1) + ' ' + s.unitSec}</b>`;
  }

  const statTime = document.getElementById('stat-time');
  const statLives = document.getElementById('stat-lives');
  const statAcc = document.getElementById('stat-accuracy');
  if (document.getElementById('vic-time')) {
    document.getElementById('vic-time').innerHTML = `${s.statTime} <b id="stat-time">${statTime ? statTime.textContent : gameTime.toFixed(1) + ' ' + s.unitSec}</b>`;
  }
  if (document.getElementById('vic-lives')) {
    document.getElementById('vic-lives').innerHTML = `${s.statLives} <b id="stat-lives">${statLives ? statLives.textContent : playerLives + ' / 3'}</b>`;
  }
  if (document.getElementById('vic-accuracy')) {
    const acc = shotsFired > 0 ? Math.round((shotsHit / shotsFired) * 100) : 100;
    document.getElementById('vic-accuracy').innerHTML = `${s.statAccuracy} <b id="stat-accuracy">${statAcc ? statAcc.textContent : acc + '%'}</b>`;
  }
  document.getElementById('val-bossrate').textContent = bossAttackInterval.toFixed(1) + ' ' + s.unitSec;

  updateHudShield();
  updateBossUI();
  updateFullscreenUI();
}

// ---------------- FULLSCREEN LOGIC ----------------
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

// ---------------- GAME CORE SETUP ----------------
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let maxBossHP = 100;
let bossHP = 100;
let bossAttackInterval = 1.8; // seconds
let blasterDamage = 10;

let selectedLevel = 1;
let gameState = 'menu';
let playerLives = 3;
let isGameOver = false;
let isVictory = false;
let gameTime = 0;
let shotsFired = 0;
let shotsHit = 0;
let score = 0;
let resultSaved = false;

let screenShake = 0;
let blasterCooldown = 0;

// Player Shield
let shieldActive = false;
let shieldTimer = 0; // seconds remaining
let shieldCooldown = 0; // seconds remaining

// Player Object
const player = {
  x: 80,
  y: 352,
  width: 28,
  height: 38,
  vx: 0,
  vy: 0,
  speed: 4.5,
  jumpForce: 13.5,
  isGrounded: true,
  invincibleTimer: 0,
  color: '#00e5ff'
};

// Boss Object
const boss = {
  x: 480,
  y: 80,
  width: 90,
  height: 55,
  vx: 2.2,
  minX: 280,
  maxX: 680,
  attackTimer: 1.0,
  phase: 1,
  hoverOffset: 0
};

// Projectiles & Arrays
let playerBlasters = [];
let bossLasers = [];
let particles = [];
let fireworks = [];
let damageFloats = [];

// Static Platforms
const platforms = [
  { x: 0, y: 390, width: 760, height: 50, color: '#101d33' }, // Ground floor
  { x: 60, y: 280, width: 140, height: 16, color: '#1a2e4d' }, // Left ledge
  { x: 280, y: 240, width: 180, height: 16, color: '#1a2e4d' }, // Center ledge
  { x: 540, y: 280, width: 150, height: 16, color: '#1a2e4d' }, // Right ledge
  { x: 380, y: 140, width: 100, height: 14, color: '#1f385c' }  // High vantage
];

// Input handling
const keys = {};
window.addEventListener('keydown', e => {
  if (['Space', 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.code)) {
    e.preventDefault();
  }
  keys[e.code] = true;
  if (e.code === 'KeyR') restartLevel();
  if (e.code === 'KeyF' && !isGameOver && !isVictory) fireBlaster();
  if (e.code === 'KeyE' && !isGameOver && !isVictory) activateShield();
  if (e.code === 'KeyM') {
    e.preventDefault();
    toggleFullscreen();
  }
});
window.addEventListener('keyup', e => { keys[e.code] = false; });
window.addEventListener('blur', () => {
  for (const k in keys) keys[k] = false;
});

function handleCanvasFire(clientX, clientY) {
  if (isGameOver || isVictory) return;
  const rect = canvas.getBoundingClientRect();
  const scaleX = canvas.width / rect.width;
  const scaleY = canvas.height / rect.height;
  const mx = (clientX - rect.left) * scaleX;
  const my = (clientY - rect.top) * scaleY;
  fireBlaster(mx, my);
}

canvas.addEventListener('mousedown', e => {
  handleCanvasFire(e.clientX, e.clientY);
});

canvas.addEventListener('touchstart', e => {
  if (e.touches && e.touches.length > 0) {
    e.preventDefault();
    handleCanvasFire(e.touches[0].clientX, e.touches[0].clientY);
  }
}, { passive: false });

// UI Sliders
const sliderBossHP = document.getElementById('slider-bosshp');
const sliderBossRate = document.getElementById('slider-bossrate');
const sliderBlaster = document.getElementById('slider-blaster');

sliderBossHP.addEventListener('input', e => {
  maxBossHP = parseInt(e.target.value);
  document.getElementById('val-bosshp').textContent = maxBossHP + ' HP';
  bossHP = Math.min(bossHP, maxBossHP);
  updateBossUI();
});

sliderBossRate.addEventListener('input', e => {
  bossAttackInterval = parseFloat(e.target.value);
  document.getElementById('val-bossrate').textContent = bossAttackInterval.toFixed(1) + ' ' + STRINGS[currentLang].unitSec;
});

sliderBlaster.addEventListener('input', e => {
  blasterDamage = parseInt(e.target.value);
  document.getElementById('val-blaster').textContent = blasterDamage + ' HP';
});

function setDifficulty(mode) {
  document.querySelectorAll('.btn-diff').forEach(b => b.classList.remove('is-active'));
  document.getElementById(`d-${mode}`).classList.add('is-active');

  if (mode === 'easy') {
    maxBossHP = 60;
    bossAttackInterval = 2.5;
    blasterDamage = 15;
    boss.vx = 1.6;
  } else if (mode === 'normal') {
    maxBossHP = 100;
    bossAttackInterval = 1.8;
    blasterDamage = 10;
    boss.vx = 2.4;
  } else if (mode === 'hard') {
    maxBossHP = 180;
    bossAttackInterval = 1.0;
    blasterDamage = 8;
    boss.vx = 3.6;
  }
  bossHP = maxBossHP;
  sliderBossHP.value = maxBossHP;
  sliderBossRate.value = bossAttackInterval;
  sliderBlaster.value = blasterDamage;
  document.getElementById('val-bosshp').textContent = maxBossHP + ' HP';
  document.getElementById('val-bossrate').textContent = bossAttackInterval.toFixed(1) + ' ' + STRINGS[currentLang].unitSec;
  document.getElementById('val-blaster').textContent = blasterDamage + ' HP';
  updateBossUI();
}

function setLevelButtons(level) {
  selectedLevel = level;
  document.querySelectorAll('.level-btn').forEach(btn => {
    btn.classList.toggle('is-selected', Number(btn.dataset.level) === level);
  });
}

function applyLevelConfig(level) {
  if (level === 1) {
    setDifficulty('easy');
  } else if (level === 2) {
    setDifficulty('normal');
  } else {
    setDifficulty('hard');
  }
  setLevelButtons(level);
}

function startGame(level = selectedLevel) {
  selectedLevel = level;
  gameState = 'playing';
  applyLevelConfig(level);
  document.getElementById('overlay-menu').hidden = true;
  restartLevel();
}

function getPlayerName() {
  const input = document.getElementById('player-name');
  return input ? Leaderboard.normalizePlayerName(input.value) : 'PLAYER';
}

function updateScoreDisplay() {
  const el = document.getElementById('score-display');
  if (el) el.textContent = Math.max(0, Math.round(score));
}

function refreshLeaderboard() {
  const list = document.getElementById('leaderboard-list');
  if (!list) return;
  const entries = Leaderboard.loadLeaderboard();
  list.innerHTML = entries.map((entry, index) => `
    <li><span>${index + 1}. ${entry.playerName}</span><strong>${entry.score}</strong></li>
  `).join('');
}

function saveCurrentScore() {
  if (resultSaved) return;
  const playerName = getPlayerName();
  const updated = Leaderboard.saveScoreEntry(Leaderboard.loadLeaderboard(), { playerName, score });
  if (updated && Array.isArray(updated)) {
    const list = document.getElementById('leaderboard-list');
    if (list) {
      list.innerHTML = updated.map((entry, index) => `
        <li><span>${index + 1}. ${entry.playerName}</span><strong>${entry.score}</strong></li>
      `).join('');
    }
  }
  resultSaved = true;
}

function updateBossUI() {
  const fill = document.getElementById('boss-bar-fill');
  const text = document.getElementById('boss-hp-text');
  const title = document.getElementById('boss-title');
  const pct = Math.max(0, Math.min(100, (bossHP / maxBossHP) * 100));
  fill.style.width = pct + '%';
  text.textContent = `${Math.ceil(bossHP)} / ${maxBossHP} HP`;

  const s = STRINGS[currentLang];
  if (pct > 60) {
    boss.phase = 1;
    title.textContent = s.bossTitlePhase1;
    fill.style.background = 'linear-gradient(90deg, #ff2a5f, #ff7a00)';
  } else if (pct > 25) {
    boss.phase = 2;
    title.textContent = s.bossTitlePhase2;
    fill.style.background = 'linear-gradient(90deg, #ff0055, #ff00ea)';
  } else {
    boss.phase = 3;
    title.textContent = s.bossTitlePhase3;
    fill.style.background = 'linear-gradient(90deg, #ff0000, #ffff00)';
  }
}

function updateHudShield() {
  const status = document.getElementById('shield-status');
  const s = STRINGS[currentLang];
  if (shieldActive) {
    status.className = 'shield-active';
    status.textContent = `${s.shieldActive} (${shieldTimer.toFixed(1)}s)`;
    status.style.color = 'var(--neon-blue)';
  } else if (shieldCooldown > 0) {
    status.className = 'shield-cooldown';
    status.textContent = `${s.shieldWait} (${Math.ceil(shieldCooldown)}s)`;
    status.style.color = 'var(--neon-yellow)';
  } else {
    status.className = 'shield-ready';
    status.textContent = s.shieldReady;
    status.style.color = 'var(--neon-green)';
  }
}

function activateShield() {
  if (shieldCooldown <= 0 && !shieldActive) {
    shieldActive = true;
    shieldTimer = 2.5;
    shieldCooldown = 6.0;
    spawnParticles(player.x + player.width/2, player.y + player.height/2, '#00e5ff', 20);
    updateHudShield();
  }
}

function fireBlaster(targetX, targetY) {
  if (blasterCooldown > 0) return;
  blasterCooldown = 0.2;
  shotsFired++;

  const startX = player.x + player.width / 2;
  const startY = player.y + 6;
  let vx = 0;
  let vy = -11;

  if (targetX !== undefined && targetY !== undefined && targetY < startY) {
    const dx = targetX - startX;
    const dy = targetY - startY;
    const dist = Math.hypot(dx, dy);
    if (dist > 0) {
      const speed = 11;
      vx = (dx / dist) * speed;
      vy = (dy / dist) * speed;
    }
  } else {
    vx = (keys['ArrowRight'] || keys['KeyD']) ? 3.5 : (keys['ArrowLeft'] || keys['KeyA']) ? -3.5 : 0;
    vy = -11;
  }

  playerBlasters.push({
    x: startX,
    y: startY,
    vx: vx,
    vy: vy,
    radius: 5,
    color: '#00e5ff',
    damage: blasterDamage
  });
  spawnParticles(startX, startY, '#00e5ff', 4);
}

function restartLevel() {
  lastTime = performance.now();
  bossHP = maxBossHP;
  playerLives = 3;
  isGameOver = false;
  isVictory = false;
  gameTime = 0;
  shotsFired = 0;
  shotsHit = 0;
  score = 0;
  resultSaved = false;
  shieldActive = false;
  shieldTimer = 0;
  shieldCooldown = 0;
  blasterCooldown = 0;
  screenShake = 0;

  player.x = 80;
  player.y = 390 - player.height;
  player.vx = 0;
  player.vy = 0;
  player.isGrounded = true;
  player.invincibleTimer = 0;

  boss.x = 480;
  boss.y = 80;
  boss.vx = Math.abs(boss.vx);
  boss.attackTimer = 1.0;
  boss.phase = 1;

  playerBlasters = [];
  bossLasers = [];
  particles = [];
  fireworks = [];
  damageFloats = [];

  document.getElementById('overlay-gameover').hidden = true;
  document.getElementById('overlay-victory').hidden = true;
  document.querySelectorAll('.heart').forEach(h => h.textContent = '❤️');

  if (document.getElementById('overlay-menu')) {
    document.getElementById('overlay-menu').hidden = gameState === 'menu';
  }

  updateBossUI();
  updateHudShield();
  updateScoreDisplay();
}

function damagePlayer() {
  if (shieldActive) {
    // Shield blocks damage entirely!
    spawnParticles(player.x + player.width/2, player.y + player.height/2, '#00e5ff', 15);
    screenShake = 3;
    return;
  }
  if (player.invincibleTimer > 0) return;

  playerLives--;
  player.invincibleTimer = 1.5;
  screenShake = 10;
  spawnParticles(player.x + player.width/2, player.y + player.height/2, '#ff2a5f', 25);

  for (let i = 1; i <= 3; i++) {
    const heart = document.getElementById(`heart-${i}`);
    heart.textContent = i <= playerLives ? '❤️' : '🖤';
  }

  if (playerLives <= 0) {
    triggerGameOver();
  }
}

function damageBoss(amount, isCrit = false) {
  if (isVictory || isGameOver) return;
  bossHP = Math.max(0, bossHP - amount);
  shotsHit++;
  score += Math.round(amount * 10 + (isCrit ? 50 : 0));
  updateScoreDisplay();
  screenShake = isCrit ? 8 : 4;
  updateBossUI();

  damageFloats.push({
    x: boss.x + boss.width/2 + (Math.random()*40 - 20),
    y: boss.y + 10,
    text: (isCrit ? 'CRIT! -' : '-') + amount,
    color: isCrit ? '#ffd700' : '#ff2a5f',
    life: 1.0
  });

  spawnParticles(boss.x + boss.width/2, boss.y + boss.height/2, isCrit ? '#ffd700' : '#ff7a00', isCrit ? 22 : 10);

  if (bossHP <= 0) {
    triggerVictory();
  }
}

function triggerGameOver() {
  isGameOver = true;
  document.getElementById('overlay-gameover').hidden = false;
  document.getElementById('go-boss-val').textContent = `${Math.ceil(bossHP)} HP`;
  document.getElementById('go-time-val').textContent = `${gameTime.toFixed(1)} ${STRINGS[currentLang].unitSec}`;
  saveCurrentScore();
}

function triggerVictory() {
  isVictory = true;
  document.getElementById('overlay-victory').hidden = false;
  document.getElementById('stat-time').textContent = `${gameTime.toFixed(1)} ${STRINGS[currentLang].unitSec}`;
  document.getElementById('stat-lives').textContent = `${playerLives} / 3`;
  const acc = shotsFired > 0 ? Math.round((shotsHit / shotsFired) * 100) : 100;
  document.getElementById('stat-accuracy').textContent = `${acc}%`;
  saveCurrentScore();

  // Massive celebration fireworks
  for (let i = 0; i < 8; i++) {
    setTimeout(() => {
      spawnFirework(Math.random() * 700 + 30, Math.random() * 200 + 50);
    }, i * 250);
  }
}

function spawnParticles(x, y, color, count) {
  for (let i = 0; i < count; i++) {
    const angle = Math.random() * Math.PI * 2;
    const speed = Math.random() * 5 + 1;
    particles.push({
      x, y,
      vx: Math.cos(angle) * speed,
      vy: Math.sin(angle) * speed,
      life: 1.0,
      color,
      size: Math.random() * 3 + 2
    });
  }
}

function spawnFirework(x, y) {
  const colors = ['#00e5ff', '#ff2a5f', '#00ff88', '#ffd700', '#b537f2'];
  const color = colors[Math.floor(Math.random() * colors.length)];
  for (let i = 0; i < 40; i++) {
    const angle = Math.random() * Math.PI * 2;
    const speed = Math.random() * 7 + 2;
    fireworks.push({
      x, y,
      vx: Math.cos(angle) * speed,
      vy: Math.sin(angle) * speed,
      life: 1.5,
      color,
      size: Math.random() * 4 + 2
    });
  }
}

// ---------------- GAME LOOP ----------------
let lastTime = performance.now();
let fpsCounter = 0;
let fpsTimer = 0;

function gameLoop(now) {
  const dt = Math.min((now - lastTime) / 1000, 0.1);
  lastTime = now;

  // FPS
  fpsCounter++;
  fpsTimer += dt;
  if (fpsTimer >= 1.0) {
    document.getElementById('fps-display').textContent = fpsCounter;
    fpsCounter = 0;
    fpsTimer = 0;
  }

  if (gameState === 'playing' && !isGameOver && !isVictory) {
    gameTime += dt;
    if (blasterCooldown > 0) blasterCooldown -= dt;
    updateShield(dt);
    updatePlayer(dt);
    updateBoss(dt);
    updateProjectiles(dt);
  }

  updateParticles(dt);
  render();

  requestAnimationFrame(gameLoop);
}

function updateShield(dt) {
  if (shieldActive) {
    shieldTimer -= dt;
    if (shieldTimer <= 0) {
      shieldActive = false;
      shieldTimer = 0;
    }
    updateHudShield();
  } else if (shieldCooldown > 0) {
    shieldCooldown -= dt;
    if (shieldCooldown <= 0) {
      shieldCooldown = 0;
    }
    updateHudShield();
  }
}

function updatePlayer(dt) {
  // Movement
  if (keys['ArrowLeft'] || keys['KeyA']) player.vx = -player.speed;
  else if (keys['ArrowRight'] || keys['KeyD']) player.vx = player.speed;
  else player.vx = 0;

  // Jump
  if ((keys['Space'] || keys['ArrowUp'] || keys['KeyW']) && player.isGrounded) {
    player.vy = -player.jumpForce;
    player.isGrounded = false;
    spawnParticles(player.x + player.width/2, player.y + player.height, '#ffffff', 5);
  }

  // Gravity
  player.vy += 26 * dt;

  // Apply velocities
  player.x += player.vx;
  player.y += player.vy;

  // Boundaries
  if (player.x < 0) player.x = 0;
  if (player.x + player.width > canvas.width) player.x = canvas.width - player.width;

  // Platform Collisions (AABB)
  player.isGrounded = false;
  for (const plat of platforms) {
    if (player.x < plat.x + plat.width && player.x + player.width > plat.x) {
      // Solid bottom ground floor safety check
      if (plat.y >= 380 && player.y + player.height >= plat.y) {
        player.y = plat.y - player.height;
        player.vy = 0;
        player.isGrounded = true;
      } else if (player.vy >= 0 &&
                 player.y + player.height >= plat.y &&
                 player.y + player.height <= plat.y + Math.max(18, player.vy + 6)) {
        player.y = plat.y - player.height;
        player.vy = 0;
        player.isGrounded = true;
      }
    }
  }

  // Absolute bottom clamp to avoid falling through screen
  if (player.y + player.height > 390) {
    player.y = 390 - player.height;
    player.vy = 0;
    player.isGrounded = true;
  }

  // Boss Collision & Stomp Check
  if (!isVictory && !isGameOver) {
    const bossY = boss.y + boss.hoverOffset;
    const isXOverlap = (player.x + player.width > boss.x) && (player.x < boss.x + boss.width);
    const isYOverlap = (player.y + player.height > bossY) && (player.y < bossY + boss.height);

    if (isXOverlap && isYOverlap) {
      // Check if player is falling downwards onto boss top (Mario-style Stomp)
      if (player.vy > 0 && player.y + player.height <= bossY + 28) {
        // Stomp success! 35 damage defeats 100 HP boss in 3 stomps as per curriculum
        damageBoss(35, true);
        player.vy = -player.jumpForce * 1.1; // Big rebound spring
        player.y = bossY - player.height;
        spawnParticles(player.x + player.width / 2, player.y + player.height, '#ffd700', 20);
      } else {
        // Body collision from side or bottom: player takes damage unless shielded/invincible
        damagePlayer();
        // Knockback away from boss
        player.vx = player.x < boss.x ? -4.5 : 4.5;
        player.vy = -3;
      }
    }
  }

  if (player.invincibleTimer > 0) {
    player.invincibleTimer -= dt;
    if (player.invincibleTimer < 0) player.invincibleTimer = 0;
  }
}

function updateBoss(dt) {
  // Horizontal sweeping movement with boundary clamping
  boss.x += boss.vx;
  if (boss.x <= boss.minX) {
    boss.x = boss.minX;
    boss.vx = Math.abs(boss.vx);
  } else if (boss.x + boss.width >= boss.maxX) {
    boss.x = boss.maxX - boss.width;
    boss.vx = -Math.abs(boss.vx);
  }

  // Floating bobbing effect
  boss.hoverOffset = Math.sin(gameTime * 3) * 8;

  // Attack timer
  boss.attackTimer -= dt;
  if (boss.attackTimer <= 0) {
    boss.attackTimer = bossAttackInterval / (boss.phase === 3 ? 1.6 : boss.phase === 2 ? 1.2 : 1.0);

    // Fire laser barrage according to phase
    const bx = boss.x + boss.width / 2;
    const by = boss.y + boss.height + boss.hoverOffset;

    if (boss.phase === 1) {
      // Single laser beam downwards
      bossLasers.push({ x: bx, y: by, vx: (Math.random() - 0.5) * 2, vy: 5.5, width: 8, height: 18, color: '#ff2a5f' });
    } else if (boss.phase === 2) {
      // Twin lasers angled
      bossLasers.push({ x: bx - 20, y: by, vx: -1.8, vy: 5.5, width: 8, height: 18, color: '#ff00ea' });
      bossLasers.push({ x: bx + 20, y: by, vx: 1.8, vy: 5.5, width: 8, height: 18, color: '#ff00ea' });
    } else {
      // Triple barrage enrage
      bossLasers.push({ x: bx - 25, y: by, vx: -2.5, vy: 6.5, width: 9, height: 20, color: '#ffff00' });
      bossLasers.push({ x: bx, y: by, vx: 0, vy: 7.0, width: 9, height: 20, color: '#ff0000' });
      bossLasers.push({ x: bx + 25, y: by, vx: 2.5, vy: 6.5, width: 9, height: 20, color: '#ffff00' });
    }
  }
}

function updateProjectiles(dt) {
  // Player Blasters
  for (let i = playerBlasters.length - 1; i >= 0; i--) {
    const b = playerBlasters[i];
    b.x += b.vx;
    b.y += b.vy;

    // Boss hit test
    if (b.x > boss.x && b.x < boss.x + boss.width &&
        b.y > boss.y + boss.hoverOffset && b.y < boss.y + boss.height + boss.hoverOffset) {
      damageBoss(b.damage, Math.random() < 0.25);
      playerBlasters.splice(i, 1);
      continue;
    }

    // Offscreen test
    if (b.y < 0 || b.x < 0 || b.x > canvas.width) {
      playerBlasters.splice(i, 1);
    }
  }

  // Boss Lasers
  for (let i = bossLasers.length - 1; i >= 0; i--) {
    const l = bossLasers[i];
    l.x += l.vx;
    l.y += l.vy;

    // Player hit test
    if (l.x < player.x + player.width &&
        l.x + l.width > player.x &&
        l.y < player.y + player.height &&
        l.y + l.height > player.y) {
      damagePlayer();
      bossLasers.splice(i, 1);
      continue;
    }

    // Ground or offscreen test
    if (l.y + l.height >= 390 || l.x < 0 || l.x > canvas.width) {
      spawnParticles(l.x + l.width / 2, Math.min(l.y + l.height, 390), l.color, 4);
      bossLasers.splice(i, 1);
    }
  }
}

function updateParticles(dt) {
  // Sparks
  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.x += p.vx;
    p.y += p.vy;
    p.life -= dt * 2;
    if (p.life <= 0) particles.splice(i, 1);
  }

  // Fireworks
  for (let i = fireworks.length - 1; i >= 0; i--) {
    const f = fireworks[i];
    f.x += f.vx;
    f.y += f.vy;
    f.vy += 3 * dt; // gravity
    f.life -= dt * 0.8;
    if (f.life <= 0) fireworks.splice(i, 1);
  }

  // Damage Floats
  for (let i = damageFloats.length - 1; i >= 0; i--) {
    const d = damageFloats[i];
    d.y -= 25 * dt;
    d.life -= dt;
    if (d.life <= 0) damageFloats.splice(i, 1);
  }

  if (screenShake > 0) {
    screenShake = Math.max(0, screenShake - 30 * dt);
  }
}

// ---------------- RENDERING ----------------
function render() {
  ctx.save();

  // Screen shake
  if (screenShake > 0) {
    const ox = (Math.random() - 0.5) * screenShake;
    const oy = (Math.random() - 0.5) * screenShake;
    ctx.translate(ox, oy);
  }

  // Clear Canvas
  ctx.fillStyle = '#060c18';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Background Grid Matrix
  ctx.strokeStyle = 'rgba(26, 41, 66, 0.4)';
  ctx.lineWidth = 1;
  for (let x = 0; x < canvas.width; x += 40) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, canvas.height);
    ctx.stroke();
  }
  for (let y = 0; y < canvas.height; y += 40) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(canvas.width, y);
    ctx.stroke();
  }

  // Platforms
  for (const p of platforms) {
    ctx.fillStyle = p.color;
    ctx.fillRect(p.x, p.y, p.width, p.height);
    ctx.strokeStyle = '#00e5ff33';
    ctx.lineWidth = 1;
    ctx.strokeRect(p.x, p.y, p.width, p.height);
  }

  // Render Boss Drone
  if (!isVictory) {
    const by = boss.y + boss.hoverOffset;
    ctx.save();
    ctx.translate(boss.x, by);

    // Boss Core Glow
    const coreColor = boss.phase === 3 ? '#ff0000' : boss.phase === 2 ? '#ff00ea' : '#ff2a5f';
    ctx.shadowColor = coreColor;
    ctx.shadowBlur = 20;

    // Main Chassis
    ctx.fillStyle = '#0e1a2f';
    ctx.strokeStyle = coreColor;
    ctx.lineWidth = 3;
    ctx.beginPath();
    if (typeof ctx.roundRect === 'function') {
      ctx.roundRect(0, 10, boss.width, boss.height - 10, 12);
    } else {
      ctx.rect(0, 10, boss.width, boss.height - 10);
    }
    ctx.fill();
    ctx.stroke();

    // Wings / Thrusters
    ctx.fillStyle = '#1c2f4e';
    ctx.fillRect(-15, 20, 15, 18);
    ctx.fillRect(boss.width, 20, 15, 18);

    // Animated Thruster Jets
    const jetLen = Math.random() * 8 + 8;
    ctx.fillStyle = '#00e5ff';
    ctx.fillRect(-12, 38, 9, jetLen);
    ctx.fillRect(boss.width + 3, 38, 9, jetLen);

    // Glowing Eye / Scanner
    ctx.fillStyle = coreColor;
    ctx.beginPath();
    const eyeX = boss.width / 2 + Math.sin(gameTime * 4) * 20;
    ctx.arc(eyeX, 28, 8, 0, Math.PI * 2);
    ctx.fill();

    // Crown / Spikes
    ctx.fillStyle = coreColor;
    ctx.beginPath();
    ctx.moveTo(15, 10); ctx.lineTo(25, -2); ctx.lineTo(35, 10);
    ctx.moveTo(boss.width - 35, 10); ctx.lineTo(boss.width - 25, -2); ctx.lineTo(boss.width - 15, 10);
    ctx.fill();

    ctx.restore();
  }

  // Render Boss Lasers
  for (const l of bossLasers) {
    ctx.save();
    ctx.shadowColor = l.color;
    ctx.shadowBlur = 12;
    ctx.fillStyle = l.color;
    ctx.fillRect(l.x, l.y, l.width, l.height);
    ctx.restore();
  }

  // Render Player Blasters
  for (const b of playerBlasters) {
    ctx.save();
    ctx.shadowColor = b.color;
    ctx.shadowBlur = 14;
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(b.x, b.y, b.radius, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = b.color;
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.restore();
  }

  // Render Player
  if (playerLives > 0) {
    ctx.save();
    // Invincibility flash
    if (player.invincibleTimer > 0 && Math.floor(gameTime * 15) % 2 === 0) {
      ctx.globalAlpha = 0.4;
    }

    // Body
    ctx.shadowColor = '#00e5ff';
    ctx.shadowBlur = 10;
    ctx.fillStyle = player.color;
    ctx.fillRect(player.x, player.y, player.width, player.height);

    // Cyber Visor
    ctx.fillStyle = '#060c18';
    ctx.fillRect(player.x + 4, player.y + 6, player.width - 8, 8);
    ctx.fillStyle = '#00ff88';
    ctx.fillRect(player.x + (player.vx < 0 ? 5 : 12), player.y + 8, 10, 4);

    // Energy Shield Visual
    if (shieldActive) {
      ctx.strokeStyle = '#00e5ff';
      ctx.shadowColor = '#00e5ff';
      ctx.shadowBlur = 25;
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.arc(player.x + player.width/2, player.y + player.height/2, 32 + Math.sin(gameTime * 8) * 3, 0, Math.PI * 2);
      ctx.stroke();
    }

    ctx.restore();
  }

  // Particles
  for (const p of particles) {
    ctx.fillStyle = p.color;
    ctx.globalAlpha = p.life;
    ctx.fillRect(p.x, p.y, p.size, p.size);
  }

  // Fireworks
  for (const f of fireworks) {
    ctx.save();
    ctx.shadowColor = f.color;
    ctx.shadowBlur = 10;
    ctx.fillStyle = f.color;
    ctx.globalAlpha = f.life;
    ctx.beginPath();
    ctx.arc(f.x, f.y, f.size, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }

  // Damage Floats
  for (const d of damageFloats) {
    ctx.save();
    ctx.font = 'bold 15px "JetBrains Mono"';
    ctx.fillStyle = d.color;
    ctx.shadowColor = d.color;
    ctx.shadowBlur = 8;
    ctx.globalAlpha = d.life;
    ctx.fillText(d.text, d.x, d.y);
    ctx.restore();
  }

  ctx.restore();
}

const playerNameInput = document.getElementById('player-name');
if (playerNameInput) {
  playerNameInput.addEventListener('input', () => {
    const value = Leaderboard.normalizePlayerName(playerNameInput.value);
    playerNameInput.value = value;
  });
}

applyLevelConfig(selectedLevel);
refreshLeaderboard();
updateScoreDisplay();

// Start Loop
setLang('ru');
requestAnimationFrame(gameLoop);
