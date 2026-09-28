const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreEl = document.getElementById('score');
const livesEl = document.getElementById('lives');
const highScoreEl = document.getElementById('highScore');
const overlayEl = document.getElementById('overlay');
const startBtn = document.getElementById('startBtn');

const WIDTH = canvas.width;
const HEIGHT = canvas.height;
const playerWidth = 54;
const playerHeight = 28;

const state = {
  running: false,
  score: 0,
  lives: 3,
  highScore: Number(localStorage.getItem('star-runner-high-score') || 0),
  gameOver: false,
  spawnTimer: 0,
  fireCooldown: 0,
  objects: [],
  projectiles: [],
  stars: [],
  keys: {
    left: false,
    right: false,
    shoot: false,
  },
  player: {
    x: WIDTH / 2 - playerWidth / 2,
    y: HEIGHT - 54,
    width: playerWidth,
    height: playerHeight,
    speed: 390,
  },
};

function resetGame() {
  state.running = true;
  state.gameOver = false;
  state.score = 0;
  state.lives = 3;
  state.spawnTimer = 0;
  state.fireCooldown = 0;
  state.objects = [];
  state.projectiles = [];
  state.stars = Array.from({ length: 50 }, () => ({
    x: Math.random() * WIDTH,
    y: Math.random() * HEIGHT,
    radius: Math.random() * 2 + 1,
    speed: 20 + Math.random() * 30,
    alpha: 0.4 + Math.random() * 0.6,
  }));

  state.player.x = WIDTH / 2 - state.player.width / 2;
  state.player.y = HEIGHT - 54;

  scoreEl.textContent = '0';
  livesEl.textContent = '3';
  highScoreEl.textContent = String(state.highScore);
  overlayEl.classList.remove('visible');
}

function showMenu() {
  state.running = false;
  state.gameOver = false;
  overlayEl.innerHTML = `
    <div class="panel">
      <h1>Star Runner</h1>
      <p>Управление: стрелки влево/вправо или A/D</p>
      <p>Стреляй по кометам клавишей Space и собирай звёзды</p>
      <button id="startBtn">Играть</button>
    </div>
  `;
  overlayEl.classList.add('visible');

  const menuBtn = document.getElementById('startBtn');
  menuBtn.addEventListener('click', resetGame, { once: true });
}

function endGame() {
  state.running = false;
  state.gameOver = true;
  if (state.score > state.highScore) {
    state.highScore = state.score;
    localStorage.setItem('star-runner-high-score', String(state.highScore));
    highScoreEl.textContent = String(state.highScore);
  }

  overlayEl.innerHTML = `
    <div class="panel">
      <h1>Поражение</h1>
      <p>Итоговый счёт: ${state.score}</p>
      <p>Попробуй ещё раз и сбивай кометы лазером!</p>
      <button id="startBtn">Играть снова</button>
    </div>
  `;
  const restartBtn = document.getElementById('startBtn');
  restartBtn.addEventListener('click', resetGame);
}

function spawnObject() {
  const chance = Math.random();
  const type = chance < 0.7 ? 'star' : 'comet';
  const width = type === 'star' ? 18 : 28 + Math.random() * 24;
  const height = type === 'star' ? 18 : width * 0.8;

  state.objects.push({
    type,
    x: Math.random() * (WIDTH - width),
    y: -height,
    width,
    height,
    speed: type === 'star' ? 180 + Math.random() * 100 : 180 + Math.random() * 160 + state.score * 0.5,
    value: type === 'star' ? 10 : 25,
    rotation: Math.random() * Math.PI * 2,
    spin: (Math.random() - 0.5) * 2.4,
  });
}

function shootLaser() {
  if (!state.running || state.fireCooldown > 0) return;

  const x = state.player.x + state.player.width / 2 - 3;
  const y = state.player.y - 12;

  state.projectiles.push({
    x,
    y,
    width: 6,
    height: 18,
    speed: 540,
  });

  state.fireCooldown = 0.22;
}

function updateBackground() {
  state.stars.forEach((star) => {
    star.y += star.speed * 0.016;
    if (star.y > HEIGHT + 5) {
      star.y = -10;
      star.x = Math.random() * WIDTH;
    }
  });
}

function updatePlayer(dt) {
  if (state.keys.left) {
    state.player.x -= state.player.speed * dt;
  }
  if (state.keys.right) {
    state.player.x += state.player.speed * dt;
  }

  state.player.x = Math.max(0, Math.min(WIDTH - state.player.width, state.player.x));
}

function updateProjectiles(dt) {
  state.fireCooldown = Math.max(0, state.fireCooldown - dt);

  for (let i = state.projectiles.length - 1; i >= 0; i -= 1) {
    const shot = state.projectiles[i];
    shot.y -= shot.speed * dt;

    if (shot.y + shot.height < 0) {
      state.projectiles.splice(i, 1);
      continue;
    }

    for (let j = state.objects.length - 1; j >= 0; j -= 1) {
      const target = state.objects[j];
      if (target.type !== 'comet') continue;

      if (checkCollision(shot, target)) {
        state.objects.splice(j, 1);
        state.projectiles.splice(i, 1);
        state.score += target.value;
        scoreEl.textContent = String(state.score);
        break;
      }
    }
  }
}

function updateObjects(dt) {
  for (let i = state.objects.length - 1; i >= 0; i -= 1) {
    const item = state.objects[i];
    item.y += item.speed * dt;
    item.rotation += item.spin * dt;

    if (item.type === 'star') {
      if (checkCollision(item, state.player)) {
        state.score += item.value;
        state.objects.splice(i, 1);
        scoreEl.textContent = String(state.score);
        continue;
      }
    } else if (checkCollision(item, state.player)) {
      state.objects.splice(i, 1);
      state.lives -= 1;
      livesEl.textContent = String(state.lives);

      if (state.lives <= 0) {
        endGame();
        return;
      }
      continue;
    }

    if (item.y > HEIGHT + item.height) {
      state.objects.splice(i, 1);
    }
  }
}

function checkCollision(a, b) {
  return (
    a.x < b.x + b.width &&
    a.x + a.width > b.x &&
    a.y < b.y + b.height &&
    a.y + a.height > b.y
  );
}

function drawBackground() {
  ctx.clearRect(0, 0, WIDTH, HEIGHT);

  const gradient = ctx.createLinearGradient(0, 0, 0, HEIGHT);
  gradient.addColorStop(0, '#020617');
  gradient.addColorStop(1, '#0b1120');
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, WIDTH, HEIGHT);

  state.stars.forEach((star) => {
    ctx.beginPath();
    ctx.fillStyle = `rgba(255,255,255,${star.alpha})`;
    ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
    ctx.fill();
  });
}

function drawPlayer() {
  const { x, y, width, height } = state.player;
  ctx.save();
  ctx.translate(x + width / 2, y + height / 2);

  ctx.fillStyle = '#7dd3fc';
  ctx.beginPath();
  ctx.moveTo(0, -height / 2);
  ctx.lineTo(width / 2, height / 2);
  ctx.lineTo(0, height / 4);
  ctx.lineTo(-width / 2, height / 2);
  ctx.closePath();
  ctx.fill();

  ctx.fillStyle = '#fbbf24';
  ctx.fillRect(-4, height / 2 - 6, 8, 12);
  ctx.restore();
}

function drawProjectiles() {
  state.projectiles.forEach((shot) => {
    ctx.fillStyle = '#38bdf8';
    ctx.fillRect(shot.x, shot.y, shot.width, shot.height);

    ctx.fillStyle = 'rgba(125, 211, 252, 0.5)';
    ctx.fillRect(shot.x - 2, shot.y - 8, shot.width + 4, 14);
  });
}

function drawStar(item) {
  ctx.save();
  ctx.translate(item.x + item.width / 2, item.y + item.height / 2);
  ctx.rotate(item.rotation);

  ctx.fillStyle = '#facc15';
  ctx.beginPath();
  for (let i = 0; i < 10; i += 1) {
    const outerRadius = item.width / 2;
    const innerRadius = outerRadius / 2.6;
    const angle = (Math.PI / 5) * i - Math.PI / 2;
    const x = Math.cos(angle) * (i % 2 === 0 ? outerRadius : innerRadius);
    const y = Math.sin(angle) * (i % 2 === 0 ? outerRadius : innerRadius);
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  }
  ctx.closePath();
  ctx.fill();
  ctx.restore();
}

function drawComet(item) {
  ctx.save();
  ctx.translate(item.x + item.width / 2, item.y + item.height / 2);
  ctx.rotate(item.rotation);

  ctx.fillStyle = '#94a3b8';
  ctx.beginPath();
  for (let i = 0; i < 8; i += 1) {
    const angle = (Math.PI * 2 / 8) * i;
    const radius = item.width / 2 + Math.sin(i * 2.1) * 4;
    const px = Math.cos(angle) * radius;
    const py = Math.sin(angle) * radius;
    if (i === 0) ctx.moveTo(px, py);
    else ctx.lineTo(px, py);
  }
  ctx.closePath();
  ctx.fill();

  ctx.fillStyle = 'rgba(15, 23, 42, 0.35)';
  ctx.beginPath();
  ctx.arc(-item.width * 0.15, -item.height * 0.15, item.width * 0.22, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
}

function drawObjects() {
  state.objects.forEach((item) => {
    if (item.type === 'star') drawStar(item);
    else drawComet(item);
  });
}

function loop(timestamp) {
  if (!state.lastTime) state.lastTime = timestamp;
  const dt = Math.min((timestamp - state.lastTime) / 1000, 0.033);
  state.lastTime = timestamp;

  if (state.running) {
    updateBackground();
    updatePlayer(dt);
    if (state.keys.shoot) {
      shootLaser();
    }
    state.spawnTimer += dt;
    if (state.spawnTimer >= 0.9) {
      spawnObject();
      state.spawnTimer = 0;
    }
    updateProjectiles(dt);
    updateObjects(dt);
  }

  drawBackground();
  drawObjects();
  drawProjectiles();
  drawPlayer();

  requestAnimationFrame(loop);
}

window.addEventListener('keydown', (event) => {
  if (event.key === 'ArrowLeft' || event.key.toLowerCase() === 'a') {
    state.keys.left = true;
  }
  if (event.key === 'ArrowRight' || event.key.toLowerCase() === 'd') {
    state.keys.right = true;
  }
  if (event.code === 'Space') {
    state.keys.shoot = true;
    shootLaser();
  }
});

window.addEventListener('keyup', (event) => {
  if (event.key === 'ArrowLeft' || event.key.toLowerCase() === 'a') {
    state.keys.left = false;
  }
  if (event.key === 'ArrowRight' || event.key.toLowerCase() === 'd') {
    state.keys.right = false;
  }
  if (event.code === 'Space') {
    state.keys.shoot = false;
  }
});

highScoreEl.textContent = String(state.highScore);
showMenu();
requestAnimationFrame(loop);
