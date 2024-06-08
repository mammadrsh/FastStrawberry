from fastapi import FastAPI
from app.workout.api import router as workout

app = FastAPI()

app.include_router(
    workout.router, prefix="/workout", tags=["Workout"]
)