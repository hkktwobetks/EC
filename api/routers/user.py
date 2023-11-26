# user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import cruds, models, schemas
from ..dependencies import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = cruds.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return cruds.create_user(db=db, user=user)

# その他のユーザー関連のルート...
