from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlslchemy.orm import relationship
from datetime import datetime
from ..database import Base

class User(Base):
   __tablename__ = "users"

   id = Column(Integer, primarykey=True, index=True)
   email = Column(String, unique=True, nullable=False, index=True)
   password_hash = Column(String, nullable=False)
   created_at = Column(datetime, default=datetime.utcnow)
   username = Column(String, unique=True, nullable=False)

   tags = relationship("Tag", back_populates="user")
   tasks = relationship("Task", back_populates="user")

   def __repr__(self):
      return f"<User(id={self.id}, email='{self.email}')>"