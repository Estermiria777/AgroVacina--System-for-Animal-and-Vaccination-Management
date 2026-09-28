from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine

# Automatically create database tables if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    version="1.0.0",
    description="Production-ready RESTful API for Livestock Management and Vaccination Tracking.",
)

# Include API router version 1
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/", tags=["Health Check"])
def health_check():
    """Service status health check endpoint."""
    return {
        "status": "online",
        "service": settings.PROJECT_NAME,
        "docs_url": "/docs",
    }