from fastapi import FastAPI
from app.workout.router import api_router as workout

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(
    workout, prefix="/workout", tags=["Workout"]
)