from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.security import hash_password
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password_hash),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user