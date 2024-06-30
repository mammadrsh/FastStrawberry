from typing import List, Optional

from bson import ObjectId
from odmantic import Field, Model


class MuscleGroup(Model):
    name: str = Field(max_length=200)
    exercise_ids: List[ObjectId] = []

    model_config = {
            "collection": "muscle_groups"
        }


class Exercise(Model):
    name: str = Field(max_length=200)
    description: str = Field(default="")
    muscle_group_ids: Optional[List[ObjectId]] = None
    # splits: List["Split"] = Relationship(back_populates="exercises")
    model_config = {
            "collection": "exercises"
        }

# class ExerciseMuscleGroup(SQLModel, table=True):
#     exercise_id: int = Field(foreign_key="exercise.id", primary_key=True)
#     muscle_group_id: int = Field(foreign_key="muscle_group.id", primary_key=True)
#     volume: float = Field(default=0.0, description="Ratio of muscle group involvement (0 to 1)")
#
#     exercise: Exercise = Relationship(back_populates="muscle_groups")
#     muscle_group: MuscleGroup = Relationship(back_populates="exercises")
#
#
# class Split(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str = Field(max_length=100)
#     exercises: List[Exercise] = Relationship(back_populates="splits")
#     workouts: List["Workout"] = Relationship(back_populates="splits")
#
#
# class Workout(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str = Field(max_length=200)
#     description: str = Field(default="")
#     splits: List[Split] = Relationship(back_populates="workouts")
#     sessions: List["Session"] = Relationship(back_populates="workout")
#
#
# class Session(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     workout_id: int = Field(foreign_key="workout.id")
#     exercise_id: int = Field(foreign_key="exercise.id")
#     reps: int
#     weight: Optional[int] = None
#     note: Optional[str] = None
#     date: datetime = Field(default_factory=datetime.utcnow)
#
#     workout: Workout = Relationship(back_populates="sessions")
#     exercise: Exercise = Relationship(back_populates="sessions")
