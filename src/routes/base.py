from fastapi import FastAPI ,APIRouter
from helpers.config import app_settings

base_router = APIRouter(
    prefix='/api/v1',
    tags=['api-v1']
)

@base_router.get('/')
async def welcome(): # async functions let python run all functions in same time not one after another
    app = app_settings()
    app_name = app.APP_NAME.value
    app_version = app.APP_VERSION.value
    return {
        'app_name':app_name,
        'app_version':app_version
    }