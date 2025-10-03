from fastapi import FastAPI ,APIRouter
import os

base_router = APIRouter(
    prefix='/api/v1',
    tags=['api-v1']
)

@base_router.get('/')
async def welcome(): # async functions let python run all functions in same time not one after another
    app_name = os.getenv('APP_NAME')
    app_version = os.getenv('APP_VERSION')
    return {
        'app_name':app_name,
        'app_version':app_version
    }