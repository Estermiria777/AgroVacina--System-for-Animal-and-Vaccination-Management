from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, EmailStr

class OwnerBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, json_schema_extra={"example": "John Doe"})
    email: Optional[EmailStr] = Field(None, json_schema_extra={"example": "john@example.com"})
    phone: Optional[str] = Field(None, json_schema_extra={"example": "+1234567890"})

class OwnerCreate(OwnerBase):
    pass

class OwnerUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class OwnerResponse(OwnerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)