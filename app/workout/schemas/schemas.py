from typing import List, Optional

import strawberry

from app.db import engine
from app.workout.models.models import MuscleGroup, Exercise


# @strawberry.input
# class AddBookInput:
#     title: str
#     author: str

@strawberry.type
class MuscleGroupType:
    id: strawberry.ID
    name: str


@strawberry.type
class ExerciseType:
    id: strawberry.ID
    name: str
    description: str
    muscle_groups: List[MuscleGroupType]



@strawberry.type
class Query:
    @strawberry.field
    async def muscle_groups(self, name: Optional[str] = None) -> List[MuscleGroupType]:
        query = MuscleGroup.name == name if name else ()
        muscle_groups = await engine.find(MuscleGroup, query)
        return [MuscleGroupType(id=str(mg.id), name=mg.name) for mg in muscle_groups]

    @strawberry.field
    async def exercises(self, name: Optional[str] = None, description: Optional[str] = None) -> List[ExerciseType]:
        filters = []
        if name:
            filters.append(Exercise.name.regex(name, "i"))
        if description:
            filters.append(Exercise.description.regex(description, "i"))

        query = ()
        if filters:
            query = {"$and": filters}

        exercises = await engine.find(Exercise, query)
        return [ExerciseType(id=str(ex.id), name=ex.name, description=ex.description, muscle_groups= [MuscleGroupType(id=str(mg.id), name=mg.name) for mg in await getMuscleGroups(mg_ids = ex.muscle_group_ids)]) for ex in exercises]


async def getMuscleGroups(mg_ids: List[strawberry.ID]):
    if mg_ids is not None:
        return await engine.find(MuscleGroup, MuscleGroup.id.in_(mg_ids))
    else:
        return []


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_muscle_group(self, name: str) -> MuscleGroupType:
        muscle_group = await engine.save(MuscleGroup(name=name))
        return MuscleGroupType(id=str(muscle_group.id), name=name)

    @strawberry.mutation
    async def add_exercise(self, name: str, description: str, muscle_group_ids: List[strawberry.ID]) -> ExerciseType:
        exercise = await engine.save(Exercise(name=name, description=description, muscle_group_ids=muscle_group_ids))
        return ExerciseType(id=str(exercise.id), name=name, description=description, muscle_group_ids=exercise.muscle_group_ids)


schema = strawberry.Schema(query=Query, mutation=Mutation)
