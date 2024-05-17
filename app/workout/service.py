from sqlmodel import Session, select

from app.workout.models import MuscleGroup
from app.workout.schemas import MuscleGroupCreate


def create_muscle_group(*, session: Session, muscle_group_in: MuscleGroupCreate) -> MuscleGroup:
    db_muscle_group = MuscleGroup.from_orm(muscle_group_in)
    session.add(db_muscle_group)
    session.commit()
    session.refresh(db_muscle_group)
    return db_muscle_group
