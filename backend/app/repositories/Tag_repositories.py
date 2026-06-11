from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.tag import Tag
from ..schemas.tag import TagCreate

class TagRepository:
   def __init__(self, db: Session):
      self.db = db

   def get_all(self) -> List[Tag]:
      return self.db.query(Tag).all()

   def get_by_id(self, tag_id: int) -> Optional[Tag]:
      return self.db.query(Tag).filter(Tag.id == tag_id).first()

   def get_by_slug(self, slug: str) -> Optional[Tag]:
      return self.db.query(Tag).filter(Tag.slug == slug).first()

   def create(self, tag_data: TagCreate) -> Tag:
      db_tag = Tag(**tag_data.model_dump())
      self.db.add(db_tag)
      self.db.commit()
      self.db.refresh(db_tag)
      return db_tag
