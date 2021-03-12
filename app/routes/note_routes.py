from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.crud import note_crud
from app.dependencies import get_db
from app.schemas import note_schemas

router = APIRouter()


@router.get('/', response_model=List[note_schemas.Note])
def get_all(db: Session = Depends(get_db)):
    return note_crud.get_all(db)


@router.get('/{note_id}', response_model=note_schemas.Note)
def get_one(note_id: int, db: Session = Depends(get_db)):
    note = note_crud.get_one(db, note_id)
    if note:
        return note
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
