from __future__ import annotations  # 1. Permite referências do Pydantic/Python sem travar o carregamento
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field

# 2. Em vez de importar 'from app.schemas.animal import AnimalResponse',
# importamos o módulo de schemas ou o próprio modelo diretamente com suporte a 'from __future__'
from app.schemas.animal import AnimalResponse


class OwnerBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, example="John Doe")
    email: EmailStr = Field(..., json_schema_extra={"example": "johndoe@example.com"})
    phone: Optional[str] = Field(None, example="+1234567890")


class OwnerCreate(OwnerBase):
    pass


class OwnerUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = None


class OwnerResponse(OwnerBase):
    id: int
    animals: List[AnimalResponse] = []

    model_config = ConfigDict(from_attributes=True)