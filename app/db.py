from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine, select
from app.config import settings
from collections.abc import Generator

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
