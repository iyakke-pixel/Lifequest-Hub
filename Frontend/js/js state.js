const state = {
  user: {
    level: 1,
    xp: 0,
    streak: 1,
    totalSaved: 0.00
  },
  quests: [
    { id: 1, title: "Math Assignment - Chapter 4", xp: 100, completed: false },
    { id: 2, title: "History Research Essay", xp: 100, completed: false }
  ],
  stashes: [
    { id: 1, name: "New Study Laptop", current: 100, target: 500 }
  ]
};

function addXP(amount) {
  state.user.xp += amount;
  if (state.user.xp >= 300) {
    state.user.level += 1;
    state.user.xp -= 300;
    alert(`🎉 LEVEL UP! You reached Level ${state.user.level}!`);
  }
  renderHeader();
}

function renderHeader() {
  document.getElementById('player-level').textContent = state.user.level;
  document.getElementById('xp-text').textContent = `${state.user.xp} / 300 XP`;
  document.getElementById('xp-bar').style.width = `${(state.user.xp / 300) * 100}%`;
  document.getElementById('streak-count').textContent = `${state.user.streak} Day${state.user.streak > 1 ? 's' : ''}`;
  document.getElementById('total-savings').textContent = `$${state.user.totalSaved.toFixed(2)}`;
}