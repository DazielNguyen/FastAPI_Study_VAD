from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from .. repository import user

get_db = database.get_db
router  = APIRouter(
    prefix="/user",
    tags=['Users']
)
password_hash = PasswordHash.recommended()
@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.show(id, db)