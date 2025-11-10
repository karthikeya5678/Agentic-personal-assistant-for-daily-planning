# app/main.py

# --- FIX 2: Load .env at the very top ---
from dotenv import load_dotenv
load_dotenv()

# --- Original Imports ---
from fastapi import FastAPI, Body, status
from fastapi.middleware.cors import CORSMiddleware
import os
from typing import List
from contextlib import asynccontextmanager

from .schemas import Task, CreateTaskModel, StudyRequest, TravelRequest
from .core.database import task_collection
from .core.scheduler import scheduler, setup_scheduler, send_task_notification # <-- Import send_task_notification
from .agents.study_agent import get_study_materials
from .agents.travel_agent import get_travel_plan

from .schemas import BusRequest
from .agents.bus_agent import get_bus_information
from .schemas import Exam, CreateExamModel
from .core.database import exam_collection
from .schemas import RecommendationRequest
from .agents.recommendation_agent import get_recommendation

from .schemas import UserProfile, CreateUserProfileModel
from .core.database import user_collection
from bson import ObjectId

# --- Lifespan Manager (No changes here) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting up application...")
    await setup_scheduler()
    scheduler.start()
    yield
    print("🌙 Shutting down application...")
    scheduler.shutdown()

app = FastAPI(
    title="Personal AI Assistant API",
    lifespan=lifespan
)

# --- CORS Middleware (No changes here) ---
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
]

# Allow additional origins via env var (comma-separated), and include common production frontends.
# Example: FRONTEND_ORIGINS="https://agentic-personal-assistant-for-daily.vercel.app,https://your-other-domain.com"
env_frontends = os.getenv("FRONTEND_ORIGINS")
if env_frontends:
    origins += [o.strip() for o in env_frontends.split(",") if o.strip()]

# Backwards-compatible: include likely Vercel hostnames that may be used (including a miss-typed variant)
origins += [
    "https://agentic-personal-assistant-for-daily.vercel.app",
    "https://agentic-personal-assistant-for-dail.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Welcome to your Personal AI Assistant Backend!"}

# --- FIX 1: MODIFIED add_task endpoint ---
@app.post("/api/v1/schedule", response_model=Task, status_code=status.HTTP_201_CREATED)
async def add_task(task: CreateTaskModel = Body(...)):
    """
    Adds a new task to the schedule and dynamically adds it to the running scheduler.
    """
    task_dict = task.model_dump()
    new_task_result = await task_collection.insert_one(task_dict)
    created_task = await task_collection.find_one({"_id": new_task_result.inserted_id})

    # Dynamically add the new job to the running scheduler
    if created_task:
        task_id = str(created_task["_id"])
        task_name = created_task["task_name"]
        task_time = created_task["time"]
        day_type = created_task["day_type"]
        
        day_mapping = {"weekday": "mon-sat", "sunday": "sun"}
        hour, minute = map(int, task_time.split(':'))
        day_of_week = day_mapping.get(day_type)

        scheduler.add_job(
            send_task_notification,
            'cron',
            day_of_week=day_of_week,
            hour=hour,
            minute=minute,
            args=[task_name],
            id=f"task_{task_id}", # Use the database ID for a unique job ID
            replace_existing=True
        )
        print(f"✅ Dynamically scheduled job for '{task_name}' at {task_time}.")

    return created_task

# --- Other endpoints (No changes here) ---
@app.get("/api/v1/schedule", response_model=List[Task])
async def get_schedule():
    tasks = await task_collection.find().to_list(1000)
    return tasks

@app.post("/api/v1/study-assistant")
async def find_study_materials(request: StudyRequest = Body(...)):
    materials = get_study_materials(topic=request.topic)
    return {"topic": request.topic, "materials": materials}

@app.post("/api/v1/plan-trip")
async def plan_trip(request: TravelRequest = Body(...)):
    plan = get_travel_plan(
        origin=request.origin,
        destination=request.destination,
        date=request.date
    )
    return {"plan": plan}

@app.post("/api/v1/track-bus")
async def track_bus(request: BusRequest = Body(...)):
    """
    Takes a bus route number, scrapes the website, and returns the status.
    """
    info = get_bus_information(route_number=request.route_number)
    return {"info": info}

# --- Add these new endpoints at the end of the file ---
@app.post("/api/v1/exams", response_model=Exam, status_code=status.HTTP_201_CREATED)
async def add_exam(exam: CreateExamModel = Body(...)):
    """Adds a new exam to the schedule."""
    exam_dict = exam.model_dump()
    new_exam_result = await exam_collection.insert_one(exam_dict)
    created_exam = await exam_collection.find_one({"_id": new_exam_result.inserted_id})
    # We don't need to dynamically schedule this, the daily job will find it.
    return created_exam

@app.get("/api/v1/exams", response_model=List[Exam])
async def get_exams():
    """Returns all upcoming exams."""
    exams = await exam_collection.find().to_list(1000)
    return exams

# --- Add this new endpoint at the end of the file ---
@app.post("/api/v1/recommendations")
async def recommend(request: RecommendationRequest = Body(...)):
    """
    Takes a recommendation type and returns a suggestion from the AI agent.
    """
    recommendation = get_recommendation(recommend_type=request.type)
    return {"recommendation": recommendation}

# We use a fixed ID so there is only ever ONE profile document
PROFILE_ID = "my_user_profile"

@app.get("/api/v1/profile", response_model=UserProfile)
async def get_profile():
    """Fetches the user's profile. Creates a blank one if it doesn't exist."""
    profile = await user_collection.find_one({"_id": PROFILE_ID})
    if profile is None:
        await user_collection.insert_one({"_id": PROFILE_ID, "name": "", "goal": "", "interests": ""})
        profile = await user_collection.find_one({"_id": PROFILE_ID})
    return profile

@app.post("/api/v1/profile", response_model=UserProfile)
async def update_profile(profile_data: CreateUserProfileModel = Body(...)):
    """Updates (or creates) the user's profile."""
    update_data = profile_data.model_dump(exclude_unset=True)

    await user_collection.update_one(
        {"_id": PROFILE_ID},
        {"$set": update_data},
        upsert=True # This creates the document if it doesn't exist
    )
    updated_profile = await user_collection.find_one({"_id": PROFILE_ID})
    return updated_profile