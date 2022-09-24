
from typing import Union

from pydantic import BaseModel

class TodoBase(BaseModel):
    date: str
    content: Union[str, None] = None
    is_done: bool

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    class Config:
        orm_mode = True
