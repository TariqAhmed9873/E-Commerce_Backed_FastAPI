# auth.py file

from jose import jwt, JWTError
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import Base, get_db
from models import User
import os
from dotenv import load_dotenv

load_dotenv()


# ================
# jwt configration

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = os.getenv(
    "ALGORITHM",
    "HS256"
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        "30"
    )
)

# ================
# password hashing

password_hash = PasswordHash.recommended()

def hashed_password(password: str):
    return password_hash.hash(password)


# ===============
# verify password

def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(
        plain_password,
        hashed_password
    )


# ================
# create jwt token

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = (
        datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    to_encode.update(
        {"exp": expire}
    )

    access_token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return access_token


# =======================================
# this tell from fastapi to get the token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login_user")


# ==================
# get user logged in

def get_current_user(token : str = Depends(oauth2_scheme), db : Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could Not vaidate credential", headers={
        "WWW-Authenticate":"Bearer"
    })

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        id = payload.get("id")

        if id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    current_user = (db.query(User).filter(User.id == id).first())

    if current_user is None:
        raise credentials_exception

    raise current_user