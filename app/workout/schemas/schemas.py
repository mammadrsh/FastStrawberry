from typing import List, Optional

import strawberry

from app.db import engine
from app.workout.models.models import MuscleGroup


@strawberry.type
class MuscleGroupType:
    id: strawberry.ID
    name: str


@strawberry.type
class Query:
    @strawberry.field
    async def muscle_groups(self, info, name: Optional[str] = None) -> List[MuscleGroupType]:
        if name:
            muscle_groups = await engine.find(MuscleGroup, MuscleGroup.name == name)
        else:
            muscle_groups = await engine.find(MuscleGroup)
        return [MuscleGroupType(id=muscle_group.id, name=muscle_group.name) for muscle_group in muscle_groups]


schema = strawberry.Schema(query=Query)