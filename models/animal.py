from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .base import Base


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    species = Column(String(50), nullable=False)
    birthday = Column(Date)
    breed = Column(String(100))
    owner_id = Column(Integer, ForeignKey("owners.id"), nullable=False)