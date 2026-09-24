# user login file

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import CreateUser, ResponceUser, Token
from auth import(hashed_password, verify_password, create_access_token)

router = APIRouter(prefix="/auth", tags=["Authentication"])

# adding user
@router.post("/add_user", response_model=ResponceUser, status_code = status.HTTP_201_CREATED)
async def add_user(user : CreateUser, db: Session = Depends(get_db)):
    adduser = db.query(User).filter(User.user_name == user.user_name).first()
    if adduser:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exist"
        )

    email = db.query(User).filter(User.user_email == user.user_email).first()
    if email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Useremail already exist"
        )

    add_user = User(
            username = user.username,
            email = user.user_email,
            hashed_password=hashed_password(user.password),
            createad_at = user.createad_at
        )
    
    db.add(add_user)
    db.commit()
    db.refresh(add_user)

    return add_user
