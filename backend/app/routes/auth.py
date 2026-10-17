from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.security import hash_password, verify_password
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut, UserLogin

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login(credentials: UserLogin, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == credentials.email).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")

    if not verify_password(credentials.password, user.password_hash): 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials")

    return {"token": "pseudo token"}