from typing import Any

from fastapi import APIRouter, Depends
from sqlmodel import Field, Session, SQLModel

from app.db import SessionDep
from app.workout.models import MuscleGroup
from app.workout.schemas import MuscleGroupCreate
from app.workout import service

# Main Router
api_router = APIRouter()


@api_router.post("/muscle_groups/", response_model=MuscleGroup)
def createMuscleGroup(*, session: SessionDep, muscle_group_in: MuscleGroupCreate) -> Any:
    return service.create_muscle_group(session=session, muscle_group_in=muscle_group_in)
