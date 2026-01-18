from fastapi import APIRouter
from .menu import router as menu_router
from .orders import router as orders_router

api_router = APIRouter(prefix="/api/v32")


api_router.include_router(menu_router)
api_router.include_router(orders_router)