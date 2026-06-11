from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from ..repositories.Task_repositories import TaskRepository
from ..repositories.Tag_repositories import TagRepository
from ..schemas.task import TaskCreate, TaskListResponse, TaskResponse


class TaskService():
   def __init__(self, db: Session):
      self.task_repository = TaskRepository(db)
      self.tag_repository = TagRepository(db)

   def get_all_task(self) -> TaskListResponse:
      task = self.task_repository.get_all()
      task_response = [TaskResponse.model_validate(tsk) for tsk in task ]
      return TaskListResponse(task=task_response, total=len(task_response))

   def get_task_by_id(self, task_id: int) -> TaskResponse:
      task = self.task_repository.get_by_id(task_id)
      if not task:
         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'Task with id {task_id} not found')

      return TaskResponse.model_validate(task)

   def get_task_by_tag(self, tag_id: int) -> TaskListResponse:
      tag = self.tag_repository.get_by_id(tag_id)
      if not tag:
         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Tag with id {tag_id} not found")

      tasks = self.task_repository.get_by_tag(tag_id)
      task_response = [TaskResponse.model_validate(tsk) for tsk in tasks]
      return TaskListResponse(tasks=task_response, total=len(task_response))

   def create_task(self, task_data: TaskCreate) -> TaskResponse:
      task = self.task_repository.create(task_data)
      return TaskResponse.model_validate(task)
