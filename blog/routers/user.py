from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from pwdlib import PasswordHash


get_db = database.get_db
router  = APIRouter()

password_hash = PasswordHash.recommended()

@router.post("/user", response_model=schemas.ShowUser, tags=["users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = password_hash.hash(request.password)
    new_user = models.User(name = request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/user/{id}", response_model=schemas.ShowUser, tags=["users"])
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with the id {id} is not available")
    return user