function renderQuests() {
  const container = document.getElementById('quest-list');
  if (!container) return;
  
  container.innerHTML = '';

  if (state.quests.length === 0) {
    container.innerHTML = `<p class="text-xs text-slate-500 italic">No quests active. Add one above!</p>`;
    return;
  }

  state.quests.forEach(quest => {
    container.innerHTML += `
      <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 flex justify-between items-center ${quest.completed ? 'opacity-50' : ''}">
        <div class="flex items-center gap-3">
          <input type="checkbox" ${quest.completed ? 'checked disabled' : ''} onclick="handleCompleteQuest(${quest.id})" class="w-5 h-5 accent-indigo-500 cursor-pointer">
          <span class="${quest.completed ? 'line-through text-slate-500' : 'text-slate-200'} font-medium text-sm">${quest.title}</span>
        </div>
        <span class="text-xs font-bold text-indigo-400 bg-indigo-950/60 px-2.5 py-1 rounded-md border border-indigo-900/50">+${quest.xp_reward || 100} XP</span>
      </div>
    `;
  });
}

async function handleCompleteQuest(id) {
  const updatedQuest = await completeQuestOnBackend(id);
  if (updatedQuest) {
    const quest = state.quests.find(q => q.id === id);
    if (quest) {
      quest.completed = true;
      addXP(quest.xp_reward || 100);
      renderQuests();
    }
  }
}

document.getElementById('quest-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const input = document.getElementById('quest-title');
  const title = input.value.trim();
  if (!title) return;

  // Send to FastAPI backend
  const newQuest = await createQuestOnBackend(title);
  
  if (newQuest) {
    state.quests.push(newQuest);
  } else {
    // Fallback if backend is offline
    state.quests.push({ id: Date.now(), title: title, xp_reward: 100, completed: false });
  }

  input.value = '';
  renderQuests();
});