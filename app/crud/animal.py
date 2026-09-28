from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.animal import Animal
from app.schemas.animal import AnimalCreate, AnimalUpdate


def get_animal(db: Session, animal_id: int) -> Optional[Animal]:
    """Retrieve a single animal by ID."""
    return db.query(Animal).filter(Animal.id == animal_id).first()


def get_animals(db: Session, skip: int = 0, limit: int = 100) -> List[Animal]:
    """Retrieve a list of animals with pagination."""
    return db.query(Animal).offset(skip).limit(limit).all()


def get_animals_by_owner(db: Session, owner_id: int, skip: int = 0, limit: int = 100) -> List[Animal]:
    """Retrieve all animals belonging to a specific owner."""
    return db.query(Animal).filter(Animal.owner_id == owner_id).offset(skip).limit(limit).all()


def create_animal(db: Session, animal_in: AnimalCreate) -> Animal:
    """Create a new animal record."""
    db_animal = Animal(**animal_in.model_dump())
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal


def update_animal(db: Session, db_animal: Animal, animal_in: AnimalUpdate) -> Animal:
    """Update an existing animal record."""
    update_data = animal_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_animal, field, value)
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal


def delete_animal(db: Session, animal_id: int) -> Optional[Animal]:
    """Delete an animal record."""
    db_animal = get_animal(db, animal_id)
    if db_animal:
        db.delete(db_animal)
        db.commit()
    return db_animal