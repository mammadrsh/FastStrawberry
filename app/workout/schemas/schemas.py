from pydantic import BaseModel, Field
from typing import List, Optional


class ExerciseMuscleGroupCreate(BaseModel):
    muscle_group_id: int
    volume: float

    class Config:
        orm_mode = True


class ExerciseCreate(BaseModel):
    name: str
    description: str
    muscle_groups: List[ExerciseMuscleGroupCreate]

    class Config:
        orm_mode = True


class MuscleGroupRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ExerciseMuscleGroupRead(BaseModel):
    muscle_group: MuscleGroupRead
    volume: float

    class Config:
        orm_mode = True


class ExerciseRead(BaseModel):
    id: int
    name: str
    description: str
    muscle_groups: List[ExerciseMuscleGroupRead]

    class Config:
        orm_mode = True
