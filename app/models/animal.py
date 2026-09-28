from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    species = Column(String, nullable=False)
    breed = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    owner_id = Column(Integer, ForeignKey("owners.id", ondelete="CASCADE"), nullable=False)

    # Relationships
    owner = relationship("Owner", back_populates="animals")
    vaccines = relationship("Vaccine", back_populates="animal", cascade="all, delete-orphan")