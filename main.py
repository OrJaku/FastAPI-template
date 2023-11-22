import uvicorn
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from configuration import conf
from routers.routers import router as api_router
from database.connection import engine
from models.models import Base
# from exceptions.handlers import app_handler # Error exceptions handler

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(api_router)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# app_handler(app) # Error exceptions handler

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)