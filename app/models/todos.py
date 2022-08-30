from sqlalchemy import Boolean, Column, Integer, String, Date
from app.db.base import Base

class Todo(Base):

    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    content = Column(String(50))
    is_done = Column(Boolean, default=False)