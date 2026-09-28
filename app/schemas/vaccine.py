from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class VaccineBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, example="Foot-and-Mouth Disease")
    application_date: date = Field(..., example="2026-03-15")
    next_due_date: Optional[date] = Field(None, example="2026-09-15")


class VaccineCreate(VaccineBase):
    pass


class VaccineUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    application_date: Optional[date] = None
    next_due_date: Optional[date] = None


class VaccineResponse(VaccineBase):
    id: int
    animal_id: int

    model_config = ConfigDict(from_attributes=True)