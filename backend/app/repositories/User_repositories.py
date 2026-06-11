from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.user import User
from ..schemas.user import UserCreate

class UserRepository:
   def __init__(self, db: Session):
      self.db = db

   def get_all(self) -> List[User]:
      return self.db.query(User).all()

   def get_by_id(self, user_id: int) -> Optional[User]:
      return self.db.query(User).filter(User.id == user_id).first()

   def get_by_username(self, username: str) -> Optional[User]:
      return self.db.query(User).filter(User.username == username).first()

   def get_by_email(self, email: str) -> Optional[User]:
      return self.db.query(User).filter(User.email == email).first()

   def create(self, email: str, password_hash: str) -> User:
      db_user = User(email=email, password_hash=password_hash)
      self.db.add(db_user)
      self.db.commit()
      self.db.refresh(db_user)
      return db_user
