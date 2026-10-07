from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class AnimalBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, json_schema_extra={"example": "Bella"})
    species: str = Field(..., min_length=2, max_length=50, json_schema_extra={"example": "Bovine"})
    breed: str = Field(..., min_length=2, max_length=50, json_schema_extra={"example": "Nelore"})
    birth_date: date = Field(..., json_schema_extra={"example": "2023-05-10"})

class AnimalCreate(AnimalBase):
    owner_id: int = Field(..., json_schema_extra={"example": 1})

class AnimalUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    species: Optional[str] = Field(None, min_length=2, max_length=50)
    breed: Optional[str] = Field(None, min_length=2, max_length=50)
    birth_date: Optional[date] = None

class AnimalResponse(AnimalBase):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)