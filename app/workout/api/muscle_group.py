from typing import List

from fastapi import APIRouter

from app.db import SessionDep
from app.workout.models.models import MuscleGroup
from app.workout.service.MuscleGroupService import MuscleGroupService

router = APIRouter(
    prefix="/muscle_groups",
)


@router.get("", status_code=200, response_model=List[MuscleGroup])
def getAll(
        session: SessionDep,
) -> List[MuscleGroup] | None:
    _service = MuscleGroupService(session)
    return _service.getAll()
