from pydantic import BaseModel, ValidationError, validator
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid

class ValidateId(BaseModel):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return uuid(str(v))
        except ValueError:
            raise ValueError('Not a valid UUID')

# Post Model
class Post(BaseModel):
    id: ValidateId
    title: str
    author: str
    content: Text
    create_at: datetime = datetime.now()
    published_at: datetime = datetime.now()
    published: bool = False

# Update Post Model
class UpdatePost(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    content: Optional[Text] = None
    