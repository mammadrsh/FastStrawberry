from fastapi import FastAPI
from app.workout.api import router as workout

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(
    workout.router, prefix="/workout", tags=["Workout"]
)