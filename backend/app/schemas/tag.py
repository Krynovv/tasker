from pydantic import BaseModel, Field

class TagBase(BaseModel):
   name: str = Field(..., min_length=3, max_length=20, description="Tag name")
   slug: str = Field(..., min_length=3, max_length=20, description="slug")

class TagCreate(TagBase):
   pass

class TagResponse(TagBase):
   id: int = Field(..., description="Unique tag")

   class Config:
      from_attributes = True