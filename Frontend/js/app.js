document.addEventListener('DOMContentLoaded', async () => {
  renderHeader();

  // Load quests from FastAPI database
  const backendQuests = await fetchQuests();
  if (backendQuests.length > 0) {
    state.quests = backendQuests;
  }
  renderQuests();

  // Load stashes from FastAPI database
  const backendStashes = await fetchStashes();
  if (backendStashes.length > 0) {
    state.stashes = backendStashes;
  }
  renderStashes();
});