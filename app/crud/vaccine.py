from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.vaccine import Vaccine
from app.schemas.vaccine import VaccineCreate, VaccineUpdate


def get_vaccine(db: Session, vaccine_id: int) -> Optional[Vaccine]:
    """Retrieve a single vaccine record by ID."""
    return db.query(Vaccine).filter(Vaccine.id == vaccine_id).first()


def get_vaccines_by_animal(db: Session, animal_id: int, skip: int = 0, limit: int = 100) -> List[Vaccine]:
    """Retrieve all vaccination records for a specific animal."""
    return db.query(Vaccine).filter(Vaccine.animal_id == animal_id).offset(skip).limit(limit).all()


def create_vaccine(db: Session, vaccine_in: VaccineCreate, animal_id: int) -> Vaccine:
    """Record a new vaccination for an animal."""
    db_vaccine = Vaccine(**vaccine_in.model_dump(), animal_id=animal_id)
    db.add(db_vaccine)
    db.commit()
    db.refresh(db_vaccine)
    return db_vaccine


def update_vaccine(db: Session, db_vaccine: Vaccine, vaccine_in: VaccineUpdate) -> Vaccine:
    """Update an existing vaccine record."""
    update_data = vaccine_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_vaccine, field, value)
    db.add(db_vaccine)
    db.commit()
    db.refresh(db_vaccine)
    return db_vaccine


def delete_vaccine(db: Session, vaccine_id: int) -> Optional[Vaccine]:
    """Delete a vaccine record."""
    db_vaccine = get_vaccine(db, vaccine_id)
    if db_vaccine:
        db.delete(db_vaccine)
        db.commit()
    return db_vaccine