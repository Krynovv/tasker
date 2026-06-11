from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from passlib.context import CryptContext

from ..repositories.User_repositories import UserRepository
from ..schemas.user import UserCreate, UserResponse

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserServices:
   def __init__(self, db: Session):
      self.repository = UserRepository(db)

   def create_user(self, user_data: UserCreate) -> UserResponse:
      existing = self.repository.get_by_email(user_data.email)
      if existing:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

      password_hash = pwd_context.hash(user_data.password)

      user = self.repository.create(email=user_data.email, password_hash=password_hash)

      return UserResponse.model_validate(user)

   def get_user_by_id(self, user_id: int) -> UserResponse:
      user = self.repository.get_by_id(user_id)
      if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")

      return UserResponse.model_validate(user)

   def authenticate_user(self, email: str, password: str):
        user = self.repository.get_by_email(email)
        if not user:
            return None

        if not pwd_context.verify(password, user.password_hash):
            return None

        return user

