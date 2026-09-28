(function (root) {
  const STORAGE_KEY = 'cyber-runner-leaderboard';
  const DEFAULT_ENTRIES = [
    { playerName: 'NEO', score: 9800 },
    { playerName: 'RIN', score: 7600 },
    { playerName: 'MIRA', score: 6200 },
    { playerName: 'JAX', score: 5400 },
    { playerName: 'KAI', score: 4100 }
  ];

  function normalizePlayerName(value) {
    const clean = String(value || '').trim();
    if (!clean) return 'PLAYER';
    const upper = clean.toUpperCase().replace(/[^A-Z0-9]/g, '');
    const finalName = upper.slice(0, 12) || 'PLAYER';
    return finalName;
  }

  function sortEntries(entries) {
    return [...entries]
      .filter(Boolean)
      .map(entry => ({
        playerName: normalizePlayerName(entry.playerName),
        score: Number(entry.score) || 0
      }))
      .sort((a, b) => b.score - a.score);
  }

  function getLeaderboard(entries, limit = 5) {
    const source = Array.isArray(entries) ? entries : loadLeaderboard();
    return sortEntries(source).slice(0, limit);
  }

  function loadLeaderboard() {
    try {
      if (typeof localStorage === 'undefined') return DEFAULT_ENTRIES;
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return DEFAULT_ENTRIES;
      const parsed = JSON.parse(raw);
      if (!Array.isArray(parsed) || parsed.length === 0) return DEFAULT_ENTRIES;
      return sortEntries(parsed);
    } catch (error) {
      return DEFAULT_ENTRIES;
    }
  }

  function persistLeaderboard(entries) {
    try {
      if (typeof localStorage !== 'undefined') {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(entries));
      }
    } catch (error) {
      // Ignore storage errors in private browsing or locked modes.
    }
    return entries;
  }

  function saveScoreEntry(existingEntries, nextEntry, limit = 5) {
    const list = Array.isArray(existingEntries) ? existingEntries : loadLeaderboard();
    const entry = nextEntry && typeof nextEntry === 'object' ? nextEntry : { playerName: 'PLAYER', score: 0 };
    const combined = [
      ...list,
      {
        playerName: normalizePlayerName(entry.playerName),
        score: Number(entry.score) || 0
      }
    ];

    const sorted = getLeaderboard(combined, limit);
    persistLeaderboard(sorted);
    return sorted;
  }

  const Leaderboard = {
    STORAGE_KEY,
    DEFAULT_ENTRIES,
    normalizePlayerName,
    getLeaderboard,
    loadLeaderboard,
    saveScoreEntry,
    persistLeaderboard
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = Leaderboard;
  }

  root.Leaderboard = Leaderboard;
})(typeof window !== 'undefined' ? window : globalThis);
