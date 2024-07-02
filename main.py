from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from datetime import datetime
import logging

from app.workout.api import router as workout

app = FastAPI()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your SvelteKit app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_user_agent(request: Request, call_next):
    logging.info(f"User-Agent: {request.headers.get('user-agent', 'unknown')}")
    # Process the request
    response = await call_next(request)
    return response

app.include_router(
    workout.router, prefix="/workout", tags=["Workout"]
)