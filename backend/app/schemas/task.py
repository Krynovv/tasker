from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .tag import TagResponse

class TaskBase(BaseModel):
   name: str = Field(..., min_length=3, max_length=20, description="Task name")
   description: Optional[str] = Field(None, description="task description")
   tag_id: int = Field(..., description="Tag id")
   date_end: datetime = Field(..., description="date of end")
   is_done: bool = Field(None, description="done")

class TaskCreated(TaskBase):
   pass

class TaskResponse(BaseModel):
   id: int = Field(..., description="Unique task ID")
   name: str
   description: Optional[str]
   tag_id: int
   date_end: datetime
   is_done: bool
   created_at: datetime
   tag: TagResponse = Field(..., description="Tag of task")

   class Config:
      from_attributes = True

class TaskListResponse(BaseModel):
   tasks: list[TaskResponse]
   total: int = Field(..., description="Task")

