# app/core/database.py
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_ATLAS_URI = os.getenv("MONGO_ATLAS_URI")

# Create a single client instance
client = AsyncIOMotorClient(MONGO_ATLAS_URI)

# Get the database (it will be created if it doesn't exist)
database = client.personal_assistant

# Get the collection (like a table in SQL)
task_collection = database.get_collection("tasks")

exam_collection = database.get_collection("exams")

user_collection = database.get_collection("user_profile")