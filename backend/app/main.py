from fastapi import FastAPI

from backend.app.api.v1.routers import api_router
from backend.app.core.config import settings


app = FastAPI(
    titile='Food Delivery API',
    version='0.1.0',
    description='Бек для моего сайта',

)


app.include_router(api_router)


