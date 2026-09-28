from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=schemas.AnimalResponse, status_code=status.HTTP_201_CREATED)
def create_animal(animal_in: schemas.AnimalCreate, db: Session = Depends(get_db)):
    """Register a new animal assigned to an existing owner."""
    db_owner = crud.owner.get_owner(db, owner_id=animal_in.owner_id)
    if not db_owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found. An animal must belong to a valid owner.",
        )
    return crud.animal.create_animal(db, animal_in=animal_in)


@router.get("/", response_model=List[schemas.AnimalResponse])
def read_animals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve all animals with optional pagination."""
    return crud.animal.get_animals(db, skip=skip, limit=limit)


@router.get("/{animal_id}", response_model=schemas.AnimalResponse)
def read_animal(animal_id: int, db: Session = Depends(get_db)):
    """Get animal details by ID."""
    db_animal = crud.animal.get_animal(db, animal_id=animal_id)
    if not db_animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Animal not found.",
        )
    return db_animal


@router.put("/{animal_id}", response_model=schemas.AnimalResponse)
def update_animal(animal_id: int, animal_in: schemas.AnimalUpdate, db: Session = Depends(get_db)):
    """Update animal information."""
    db_animal = crud.animal.get_animal(db, animal_id=animal_id)
    if not db_animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Animal not found.",
        )
    return crud.animal.update_animal(db, db_animal=db_animal, animal_in=animal_in)


@router.delete("/{animal_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_animal(animal_id: int, db: Session = Depends(get_db)):
    """Delete an animal record."""
    db_animal = crud.animal.get_animal(db, animal_id=animal_id)
    if not db_animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Animal not found.",
        )
    crud.animal.delete_animal(db, animal_id=animal_id)
    return None