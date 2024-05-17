from pydantic import BaseModel, Field
from typing import List, Optional


class MuscleGroupBase(BaseModel):
    name: str = Field(..., max_length=100)


class MuscleGroupCreate(MuscleGroupBase):
    pass


class MuscleGroupResponse(MuscleGroupBase):
    pass
