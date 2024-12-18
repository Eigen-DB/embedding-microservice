from fastapi import FastAPI, APIRouter
from routes import upload

app = FastAPI() 

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(upload.router)

app.include_router(api_v1_router)