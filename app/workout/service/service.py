from typing import List

from sqlmodel import Session, select

from app.workout.models.models import MuscleGroup, Exercise, ExerciseMuscleGroup
from app.workout.schemas.schemas import ExerciseCreate, ExerciseRead, ExerciseMuscleGroupRead, MuscleGroupRead


def create_exercise(*, session: Session, exercise_in: ExerciseCreate) -> ExerciseRead:
    db_exercise = Exercise(
        name=exercise_in.name,
        description=exercise_in.description
    )
    session.add(db_exercise)
    session.commit()
    session.refresh(db_exercise)

    for muscle_group in exercise_in.muscle_groups:
        db_link = ExerciseMuscleGroup(
            exercise_id=db_exercise.id,
            muscle_group_id=muscle_group.muscle_group_id,
            volume=muscle_group.volume
        )
        session.add(db_link)

    session.commit()
    exercise_read = ExerciseRead(
        id=db_exercise.id,
        name=db_exercise.name,
        description=db_exercise.description,
        muscle_groups=[
            ExerciseMuscleGroupRead(
                muscle_group=MuscleGroupRead(
                    id=mg.muscle_group_id,
                    name=session.get(MuscleGroup, mg.muscle_group_id).name,
                ),
                volume=mg.volume
            ) for mg in
            session.exec(select(ExerciseMuscleGroup).where(ExerciseMuscleGroup.exercise_id == db_exercise.id)).all()
        ]
    )

    return exercise_read


def get_exercises(*, session: Session) -> List[ExerciseRead]:
    exercises = session.exec(select(Exercise)).all()
    exercise_reads = []

    for exercise in exercises:
        muscle_groups = session.exec(
            select(ExerciseMuscleGroup).where(ExerciseMuscleGroup.exercise_id == exercise.id)).all()
        exercise_reads.append(
            ExerciseRead(
                id=exercise.id,
                name=exercise.name,
                description=exercise.description,
                muscle_groups=[
                    ExerciseMuscleGroupRead(
                        muscle_group=MuscleGroupRead(
                            id=mg.muscle_group_id,
                            name=session.get(MuscleGroup, mg.muscle_group_id).name
                        ),
                        volume=mg.volume
                    ) for mg in muscle_groups
                ]
            )
        )

    return exercise_reads


def get_exercise(*, session: Session, exercise_id: int) -> ExerciseRead | None:
    exercise = session.get(Exercise, exercise_id)
    if not exercise:
        return None

    muscle_groups = session.exec(
        select(ExerciseMuscleGroup).where(exercise.id == ExerciseMuscleGroup.exercise_id)).all()

    return ExerciseRead(
        id=exercise.id,
        name=exercise.name,
        description=exercise.description,
        muscle_groups=[
            ExerciseMuscleGroupRead(
                muscle_group=MuscleGroupRead(
                    id=mg.muscle_group_id,
                    name=session.get(MuscleGroup, mg.muscle_group_id).name
                ),
                volume=mg.volume
            ) for mg in muscle_groups
        ]
    )
