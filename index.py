from fastapi import FastAPI
from routes.index import router as main_router

app = FastAPI(
    title="My REST API",
    description="A simple FastAPI CRUD application",
    version="1.0.0"
)

app.include_router(main_router)

