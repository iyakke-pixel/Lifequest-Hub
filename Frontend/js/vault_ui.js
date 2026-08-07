function renderStashes() {
  const container = document.getElementById('stash-list');
  container.innerHTML = '';

  let calculatedTotal = 0;

  state.stashes.forEach(stash => {
    calculatedTotal += stash.current;
    container.innerHTML += `
      <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex justify-between items-center">
        <div>
          <h3 class="font-bold text-slate-200 text-sm">${stash.name}</h3>
          <span class="text-xs text-slate-500">$${stash.current.toFixed(2)} / $${stash.target.toFixed(2)} saved</span>
        </div>
        <button onclick="stashDeposit(${stash.id}, 25)" class="bg-emerald-600/20 hover:bg-emerald-600 text-emerald-400 hover:text-white border border-emerald-500/40 font-bold text-xs px-3 py-2 rounded-lg transition cursor-pointer">
          + $25
        </button>
      </div>
    `;
  });

  state.user.totalSaved = calculatedTotal;
  renderHeader();
}

function stashDeposit(id, amount) {
  const stash = state.stashes.find(s => s.id === id);
  if (stash) {
    stash.current += amount;
    addXP(50); // financial reward
    renderStashes();
  }
}

document.getElementById('stash-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const name = document.getElementById('stash-name');
  const target = document.getElementById('stash-target');

  if (!name.value || !target.value) return;

  state.stashes.push({
    id: Date.now(),
    name: name.value.trim(),
    current: 0,
    target: parseFloat(target.value)
  });

  name.value = '';
  target.value = '';
  renderStashes();
})