from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from sqlalchemy.orm import Session
from app.core.security import get_password_hash

def create_user(db: Session, user: UserCreate):
    new_user = User(
        email=user.email,
        hashed_password=get_password_hash(user.password),
        full_name=user.full_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()