from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class UserBase(BaseModel):
   email: EmailStr
   username: str = Field(..., min_length=2, max_length=30, descriptiom="username")

class UserCreate(UserBase):
   password: str = Field(..., min_length=8)

class UserResponse(UserBase):
   id: int = Field(..., description="user ID")
   created_at = datetime

   class Config:
      from_attributes = True
