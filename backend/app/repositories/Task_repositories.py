from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from ..models.task import Task
from ..schemas.task import TaskCreate

class TaskRepository:
   def __init__(self, db: Session):
      self.db = db

   def get_all(self) -> List[Task]:
      return self.db.query(Task).options(joinedload(Task.tag)).all()

   def get_by_id(self, task_id: int) -> Optional[Task]:
      return self.db.query(Task).options(joinedload(Task.tag)).filter(Task.id == task_id).first()

   def get_by_tag(self, tag_id: int) -> List[Task]:
      return self.db.query(Task).options(joinedload(Task.tag)).filter(Task.tag_id == tag_id).all()

   def create(self, task_data: TaskCreate) -> Task:
      db_task = Task(**task_data.model_dump())
      self.db.add(db_task)
      self.db.commit()
      self.db.refresh(db_task)
      return db_task
