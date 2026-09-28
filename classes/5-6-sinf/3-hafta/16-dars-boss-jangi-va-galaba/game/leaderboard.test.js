const test = require('node:test');
const assert = require('node:assert/strict');
const { normalizePlayerName, saveScoreEntry, getLeaderboard } = require('./leaderboard.js');

test('player names are normalized and trimmed', () => {
  assert.equal(normalizePlayerName('  neo  '), 'NEO');
  assert.equal(normalizePlayerName(''), 'PLAYER');
  assert.equal(normalizePlayerName('x'.repeat(20)), 'XXXXXXXXXXXX');
});

test('scores are stored sorted descending by value', () => {
  const entries = [
    { playerName: 'ALPHA', score: 1200 },
    { playerName: 'BETA', score: 3000 },
    { playerName: 'GAMMA', score: 1800 }
  ];

  const saved = saveScoreEntry(entries, { playerName: 'DELTA', score: 2500 });
  assert.equal(saved[0].playerName, 'BETA');
  assert.equal(saved[1].playerName, 'DELTA');
  assert.equal(saved[2].playerName, 'GAMMA');
});

test('leaderboard keeps the top five entries', () => {
  const entries = Array.from({ length: 6 }, (_, i) => ({
    playerName: `P${i + 1}`,
    score: 100 + i
  }));

  const saved = getLeaderboard(entries, 5);
  assert.equal(saved.length, 5);
  assert.equal(saved[0].score, 105);
});
