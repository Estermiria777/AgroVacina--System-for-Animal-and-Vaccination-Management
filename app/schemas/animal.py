from datetime import date
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from app.schemas.vaccine import VaccineResponse


class AnimalBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, example="Bella")
    species: str = Field(..., min_length=2, max_length=50, example="Bovine")
    breed: str = Field(..., min_length=2, max_length=50, example="Nelore")
    birth_date: date = Field(..., example="2023-05-10")


class AnimalCreate(AnimalBase):
    owner_id: int = Field(..., example=1)


class AnimalUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    species: Optional[str] = Field(None, min_length=2, max_length=50)
    breed: Optional[str] = Field(None, min_length=2, max_length=50)
    birth_date: Optional[date] = None
    owner_id: Optional[int] = None


class AnimalResponse(AnimalBase):
    id: int
    owner_id: int
    vaccines: List[VaccineResponse] = []

    model_config = ConfigDict(from_attributes=True)