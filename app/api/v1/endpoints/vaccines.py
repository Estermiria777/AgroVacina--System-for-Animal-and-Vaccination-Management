from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import get_db

router = APIRouter()


@router.post("/animals/{animal_id}/vaccines/", response_model=schemas.VaccineResponse, status_code=status.HTTP_201_CREATED)
def create_vaccine_for_animal(animal_id: int, vaccine_in: schemas.VaccineCreate, db: Session = Depends(get_db)):
    """Record a vaccine application for a specific animal."""
    db_animal = crud.animal.get_animal(db, animal_id=animal_id)
    if not db_animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Animal not found.",
        )
    return crud.vaccine.create_vaccine(db, vaccine_in=vaccine_in, animal_id=animal_id)


@router.get("/animals/{animal_id}/vaccines/", response_model=List[schemas.VaccineResponse])
def read_vaccines_for_animal(animal_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get complete vaccination history for a specific animal."""
    db_animal = crud.animal.get_animal(db, animal_id=animal_id)
    if not db_animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Animal not found.",
        )
    return crud.vaccine.get_vaccines_by_animal(db, animal_id=animal_id, skip=skip, limit=limit)


@router.put("/vaccines/{vaccine_id}", response_model=schemas.VaccineResponse)
def update_vaccine(vaccine_id: int, vaccine_in: schemas.VaccineUpdate, db: Session = Depends(get_db)):
    """Update vaccine record details."""
    db_vaccine = crud.vaccine.get_vaccine(db, vaccine_id=vaccine_id)
    if not db_vaccine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vaccine record not found.",
        )
    return crud.vaccine.update_vaccine(db, db_vaccine=db_vaccine, vaccine_in=vaccine_in)


@router.delete("/vaccines/{vaccine_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vaccine(vaccine_id: int, db: Session = Depends(get_db)):
    """Delete a vaccine record."""
    db_vaccine = crud.vaccine.get_vaccine(db, vaccine_id=vaccine_id)
    if not db_vaccine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vaccine record not found.",
        )
    crud.vaccine.delete_vaccine(db, vaccine_id=vaccine_id)
    return None