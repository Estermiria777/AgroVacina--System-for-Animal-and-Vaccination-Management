from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=schemas.OwnerResponse, status_code=status.HTTP_201_CREATED)
def create_owner(owner_in: schemas.OwnerCreate, db: Session = Depends(get_db)):
    """Register a new owner in the system."""
    existing_owner = crud.owner.get_owner_by_email(db, email=owner_in.email)
    if existing_owner:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An owner with this email address already exists.",
        )
    return crud.owner.create_owner(db, owner_in=owner_in)


@router.get("/", response_model=List[schemas.OwnerResponse])
def read_owners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve all owners with optional pagination."""
    return crud.owner.get_owners(db, skip=skip, limit=limit)


@router.get("/{owner_id}", response_model=schemas.OwnerResponse)
def read_owner(owner_id: int, db: Session = Depends(get_db)):
    """Get owner details by ID."""
    db_owner = crud.owner.get_owner(db, owner_id=owner_id)
    if not db_owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found.",
        )
    return db_owner


@router.put("/{owner_id}", response_model=schemas.OwnerResponse)
def update_owner(owner_id: int, owner_in: schemas.OwnerUpdate, db: Session = Depends(get_db)):
    """Update owner information."""
    db_owner = crud.owner.get_owner(db, owner_id=owner_id)
    if not db_owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found.",
        )
    return crud.owner.update_owner(db, db_owner=db_owner, owner_in=owner_in)


@router.delete("/{owner_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_owner(owner_id: int, db: Session = Depends(get_db)):
    """Delete an owner record."""
    db_owner = crud.owner.get_owner(db, owner_id=owner_id)
    if not db_owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Owner not found.",
        )
    crud.owner.delete_owner(db, owner_id=owner_id)
    return None