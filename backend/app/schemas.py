# app/schemas.py

from pydantic import BaseModel, Field, BeforeValidator, ConfigDict
from typing import Literal, Annotated  # <-- Make sure Annotated is imported
from bson import ObjectId

# This validator function stays the same
PyObjectId = BeforeValidator(str)

class Task(BaseModel):
    # This model is already correct
    id: Annotated[str, PyObjectId] | None = Field(alias="_id", default=None)
    time: str
    task_name: str
    day_type: Literal["weekday", "sunday"]

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )

class CreateTaskModel(BaseModel):
    time: str
    task_name: str
    day_type: Literal["weekday", "sunday"]

class StudyRequest(BaseModel):
    topic: str

class TravelRequest(BaseModel):
    origin: str
    destination: str
    date: str

class BusRequest(BaseModel):
    route_number: str

# --- THIS IS THE FIX ---
class Exam(BaseModel):
    # Use Annotated[str, PyObjectId] | None, just like in the Task model
    id: Annotated[str, PyObjectId] | None = Field(alias="_id", default=None)
    subject: str
    date: str 

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )

class CreateExamModel(BaseModel):
    subject: str
    date: str

# Add to app/schemas.py
class RecommendationRequest(BaseModel):
    type: str # Will be "movie" or "learn"

class UserProfile(BaseModel):
    id: Annotated[str, PyObjectId] | None = Field(alias="_id", default=None)
    name: str | None = None
    goal: str | None = None # e.g., "Learn AI", "Get a new job"
    interests: str | None = None # e.g., "Python, Sci-fi movies"

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )

class CreateUserProfileModel(BaseModel):
    name: str | None = None
    goal: str | None = None
    interests: str | None = None