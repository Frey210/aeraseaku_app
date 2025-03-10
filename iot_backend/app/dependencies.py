from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app import database, models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    # Di sini harus ada proses validasi token
    user = db.query(models.User).filter(models.User.token == token).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user
