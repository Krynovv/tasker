from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlslchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Task(Base):
   __tablename__ = "tasks"

   id = Column(Integer, primary_key=True, index=True)
   name = Column(String, nullable=False)
   description = Column(Text)
   tag_ig = Column(Integer, ForeignKey("tags.id"), nullable=False)
   created_at = Column(DateTime, default=datetime.utcnow)
   date_end = Column(DateTime)
   is_done = Column(Boolean, default=False)

   tag = relationship("Tag", back_populates="task")

   def __repr__(self):
      return f"<Task(id={self.id}, name='{self.name}', maded={self.maded})>"