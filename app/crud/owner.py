from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.owner import Owner
from app.schemas.owner import OwnerCreate, OwnerUpdate


def get_owner(db: Session, owner_id: int) -> Optional[Owner]:
    """Retrieve a single owner by ID."""
    return db.query(Owner).filter(Owner.id == owner_id).first()


def get_owner_by_email(db: Session, email: str) -> Optional[Owner]:
    """Retrieve an owner by email address."""
    return db.query(Owner).filter(Owner.email == email).first()


def get_owners(db: Session, skip: int = 0, limit: int = 100) -> List[Owner]:
    """Retrieve a list of owners with pagination."""
    return db.query(Owner).offset(skip).limit(limit).all()


def create_owner(db: Session, owner_in: OwnerCreate) -> Owner:
    """Create a new owner record."""
    db_owner = Owner(**owner_in.model_dump())
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner


def update_owner(db: Session, db_owner: Owner, owner_in: OwnerUpdate) -> Owner:
    """Update an existing owner record."""
    update_data = owner_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_owner, field, value)
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner


def delete_owner(db: Session, owner_id: int) -> Optional[Owner]:
    """Delete an owner record."""
    db_owner = get_owner(db, owner_id)
    if db_owner:
        db.delete(db_owner)
        db.commit()
    return db_owner