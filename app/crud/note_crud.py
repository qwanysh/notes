from sqlalchemy.orm import Session

from app import models


def get_all(db: Session):
    return db.query(models.Note).order_by(models.Note.created_at.desc()).all()


def get_one(db: Session, note_id):
    return db.query(models.Note).get(note_id)
