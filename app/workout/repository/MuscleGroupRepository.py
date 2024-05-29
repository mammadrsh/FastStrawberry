from typing import List
from odmantic import AIOEngine
from app.workout.models.models import MuscleGroup


class MuscleGroupRepository:
    def __init__(self, engine: AIOEngine):
        self.engine = engine

    async def getAll(self) -> List[MuscleGroup]:
        return await self.engine.find(MuscleGroup)