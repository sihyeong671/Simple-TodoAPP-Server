
from sqlalchemy.orm import Session

from app.models import todo as model
from app.schemas import todo as schema



def get_todo(db: Session, todo_id: int):
    return db.query(model.Todo).filter(model.Todo.id == todo_id).first()


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Todo).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: schema.TodoCreate):

    # date_string = '%Y-%m-%d'
    # date = datetime.strptime(date, date_string)

    db_todo = model.Todo(
        date=todo.date,
        content=todo.content,
        is_done=todo.is_done
    )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo



def update_todo(db: Session, todo_id: int):
    db_todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    db_todo.is_done = not db_todo.is_done
    db.commit()
    db.refresh(db_todo)

    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    db.delete(db_todo)
    db.commit()
    return None
