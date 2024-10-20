from pydantic import BaseModel, model_validator
from datetime import datetime


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: str | None

    @model_validator(mode='before')
    def generate_slug(cls, values):
        if 'title' in values:
            values['slug'] = values.get('title').replace(' ','-').lower()
        return values

class UpdateBlog(CreateBlog):
    pass

class ShowBlog(BaseModel):
    title: str
    content: str | None
    created_at: datetime

    class ConfigDict:
        from_attributes = True
