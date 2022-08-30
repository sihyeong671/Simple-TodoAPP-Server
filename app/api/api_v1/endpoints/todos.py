from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import todos as crud
from app.schemas import todos as schemas
from app.db.base import SessionLocal, Base, engine

Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/{todo_id}', response_model=schemas.Todo)
async def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.get('/', response_model=list[schemas.Todo])
async def read_todos(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip, limit)
    return todos


@router.post('/', response_model=schemas.Todo)
async def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = crud.create_todo(db, todo)
    return db_todo

@router.put('/{todo_id}', response_model=schemas.Todo)
async def update_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id)
    return db_todo

@router.delete('/{todo_id}', response_model=list[schemas.Todo])
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    crud.delete_todo(db, todo_id)
    return {'messege':'delete success'}