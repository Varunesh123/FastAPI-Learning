from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas  # Changed from ... to .. since we're going one level up
from ..database import get_db

router = APIRouter(
    prefix="/custodians",
    tags=["custodians"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Custodian)
def create_custodian_endpoint(custodian: schemas.CustodianCreate, db: Session = Depends(get_db)):
    return crud.create_custodian(db=db, custodian=custodian)

@router.get("/{custodian_id}", response_model=schemas.Custodian)
def read_custodian(custodian_id: int, db: Session = Depends(get_db)):
    db_custodian = crud.get_custodian(db=db, custodian_id=custodian_id)
    if db_custodian is None:
        raise HTTPException(status_code=404, detail="Custodian not found")
    return db_custodian

@router.get("/")
def read_custodians(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    custodians = crud.get_custodians(db=db, skip=skip, limit=limit)
    return custodians

@router.put("/{custodian_id}", response_model=schemas.Custodian)
def update_custodian_endpoint(custodian_id: int, custodian: schemas.CustodianUpdate, db: Session = Depends(get_db)):
    db_custodian = crud.update_custodian(db=db, custodian_id=custodian_id, custodian=custodian)
    if db_custodian is None:
        raise HTTPException(status_code=404, detail="Custodian not found")
    return db_custodian

@router.delete("/{custodian_id}", response_model=schemas.Custodian)
def delete_custodian_endpoint(custodian_id: int, db: Session = Depends(get_db)):
    db_custodian = crud.delete_custodian(db=db, custodian_id=custodian_id)
    if db_custodian is None:
        raise HTTPException(status_code=404, detail="Custodian not found")
    return db_custodian