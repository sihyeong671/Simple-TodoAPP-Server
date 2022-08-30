from fastapi import APIRouter

from app.api.api_v1.endpoints import todos

api_router = APIRouter()

api_router.include_router(todos.router, prefix='/todos', tags=['todo'])