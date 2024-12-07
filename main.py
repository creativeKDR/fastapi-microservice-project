import os

from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.db import create_db_tables
from src.endpoints import order_router

app = FastAPI(title='OrderApp')
app.include_router(order_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
def create_db():
    return create_db_tables()


@app.get('/health')
async def index():
    return Response("Health okay", status_code=status.HTTP_200_OK)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info", reload=True)
