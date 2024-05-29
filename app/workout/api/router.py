from typing import Any, List

from fastapi import APIRouter, HTTPException

from app.db import SessionDep
from app.workout.api import muscle_group
from app.workout.schemas.schemas import ExerciseRead, ExerciseCreate
from app.workout import service

router = APIRouter()


@router.post("/exercises/", response_model=ExerciseRead)
def create_exercise_route(
        *, session: SessionDep, exercise_in: ExerciseCreate
) -> Any:
    try:
        return service.create_exercise(session=session, exercise_in=exercise_in)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/exercises/", response_model=List[ExerciseRead])
def read_exercises_route(*, session: SessionDep) -> Any:
    return service.get_exercises(session=session)


@router.get("/exercises/{exercise_id}", response_model=ExerciseRead)
def read_exercise_route(*, session: SessionDep, exercise_id: int) -> Any:
    exercise = service.get_exercise(session=session, exercise_id=exercise_id)
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise


router.include_router(muscle_group.router)
