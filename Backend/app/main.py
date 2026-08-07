from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
import app.models

# Import route routers from the routes subfolder
from app.routes.auth_routes import router as auth_router
from app.routes.quest_routes import router as quest_router
from app.routes.stash_routes import router as stash_router
from app.routes.expense_routes import router as expense_router
from app.routes.finance_routes import router as finance_router
from app.routes.leaderboard_routes import router as leaderboard_router
from app.routes.boss_routes import router as boss_router
from app.routes.achievement_routes import router as achievement_router
from app.routes.user_routes import router as user_router
# Create database tables automatically
Base.metadata.create_all(bind=engine)

# Initialize FastAPI App
app = FastAPI(
    title="LifeQuest Student Hub API",
    description="Backend API powering quests, savings stashes, roommate expense splitting, and authentication.",
    version="1.0.0"
)

# Enable CORS middleware so your frontend HTML can communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth_router)
app.include_router(quest_router)
app.include_router(stash_router)
app.include_router(expense_router)
app.include_router(finance_router)
app.include_router(leaderboard_router)
app.include_router(boss_router)
app.include_router(achievement_router)
app.include_router(user_router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to LifeQuest Student Hub API! 🎮",
        "status": "Online",
        "docs_url": "/docs"
    }