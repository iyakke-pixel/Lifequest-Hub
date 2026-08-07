const API_BASE_URL = "http://127.0.0.1:8000/api";

// --- QUEST API CALLS ---

// Fetch all quests from backend
async function fetchQuests() {
  try {
    const response = await fetch(`${API_BASE_URL}/quests/`);
    if (!response.ok) throw new Error("Failed to fetch quests");
    return await response.json();
  } catch (error) {
    console.error("API Error (fetchQuests):", error);
    return [];
  }
}

// Create a new quest on backend
async function createQuestOnBackend(title, course = "General", xpReward = 100) {
  try {
    const response = await fetch(`${API_BASE_URL}/quests/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title: title,
        course: course,
        xp_reward: xpReward
      })
    });
    if (!response.ok) throw new Error("Failed to create quest");
    return await response.json();
  } catch (error) {
    console.error("API Error (createQuest):", error);
    return null;
  }
}

// Mark a quest completed on backend
async function completeQuestOnBackend(questId) {
  try {
    const response = await fetch(`${API_BASE_URL}/quests/${questId}/complete`, {
      method: "PATCH"
    });
    if (!response.ok) throw new Error("Failed to complete quest");
    return await response.json();
  } catch (error) {
    console.error("API Error (completeQuest):", error);
    return null;
  }
}

// --- STASH API CALLS ---

// Fetch all savings stashes from backend
async function fetchStashes() {
  try {
    const response = await fetch(`${API_BASE_URL}/stashes/`);
    if (!response.ok) throw new Error("Failed to fetch stashes");
    return await response.json();
  } catch (error) {
    console.error("API Error (fetchStashes):", error);
    return [];
  }
}

// Create a new stash on backend
async function createStashOnBackend(name, targetAmount) {
  try {
    const response = await fetch(`${API_BASE_URL}/stashes/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: name,
        target_amount: targetAmount
      })
    });
    if (!response.ok) throw new Error("Failed to create stash");
    return await response.json();
  } catch (error) {
    console.error("API Error (createStash):", error);
    return null;
  }
}

async function depositStashOnBackend(stashId, amount = 25.0) {
  try {
    const response = await fetch(`${API_BASE_URL}/stashes/${stashId}/deposit?amount=${amount}`, {
      method: "PATCH"
    });
    if (!response.ok) throw new Error("Failed to deposit to stash");
    return await response.json();
  } catch (error) {
    console.error("API Error (depositStash):", error);
    return null;
  }
}