from typing import List
from app.workout.models.models import MuscleGroup
from app.workout.repository.MuscleGroupRepository import MuscleGroupRepository


class MuscleGroupService:
    def __init__(self, repository: MuscleGroupRepository):
        self.repository = repository

    def getAll(self) -> List[MuscleGroup]:
        return self.repository.getAll()