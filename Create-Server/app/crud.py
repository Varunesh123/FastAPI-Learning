from sqlalchemy.orm import Session
from . import models, schemas

def get_custodian(db: Session, custodian_id: int):
    return db.query(models.Custodian).filter(models.Custodian.id == custodian_id).first()

def get_custodians(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Custodian).offset(skip).limit(limit).all()

def create_custodian(db: Session, custodian: schemas.CustodianCreate):
    db_custodian = models.Custodian(**custodian.dict())
    db.add(db_custodian)
    db.commit()
    db.refresh(db_custodian)
    return db_custodian

def update_custodian(db: Session, custodian_id: int, custodian: schemas.CustodianUpdate):
    db_custodian = db.query(models.Custodian).filter(models.Custodian.id == custodian_id).first()
    if db_custodian:
        for key, value in custodian.dict(exclude_unset=True).items():
            setattr(db_custodian, key, value)
        db_custodian.updated_on = func.now()
        db.commit()
        db.refresh(db_custodian)
    return db_custodian

def delete_custodian(db: Session, custodian_id: int):
    db_custodian = db.query(models.Custodian).filter(models.Custodian.id == custodian_id).first()
    if db_custodian:
        db.delete(db_custodian)
        db.commit()
    return db_custodian