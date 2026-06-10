from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Tag(Base):
   __tablename__ = "tags"

   id = Column(Integer, primary_key=True, index=True)
   name = Column(String, unique=True, nullable=False, index=True)
   slug = Column(String, unique=True, nullable=False, index=True)

   task = relationship("Task", back_populates="tag")

   def __repr__(self):
      return f"<Tag(id={self.id}, name='{self.name}')>"