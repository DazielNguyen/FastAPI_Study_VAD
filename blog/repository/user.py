from fastapi import HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def create(request: schemas.User, db: Session):
    hashed_password = password_hash.hash(request.password)
    new_user = models.User(name = request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with the id {id} is not available")
    return user