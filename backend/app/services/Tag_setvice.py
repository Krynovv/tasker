from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException, status

from ..repositories.Tag_repositories import TagRepository
from ..schemas.tag import TagCreate, TagResponse


class TagService:
   def __init__(self, db: Session):
      self.repository = TagRepository(db)

   def get_all_tags(self) -> List[TagResponse]:
      tag = self.repository.get_all()
      return [TagResponse.model_validate(tg) for tg in tag]

   def get_tag_by_id(self, tag_id: int) -> TagResponse:
      tag = self.repository.get_by_id(tag_id)
      if not tag:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Tag with id {tag_id} not found')

      return TagResponse.model_validate(tag)

   def create_tag(self, tag_data: TagCreate) -> TagResponse:
      tag = self.repository.create(tag_data)
      return TagResponse.model_validate(tag)
