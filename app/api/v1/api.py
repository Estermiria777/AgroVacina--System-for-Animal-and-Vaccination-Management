from fastapi import APIRouter
from app.api.v1.endpoints import owners, animals, vaccines

api_router = APIRouter()

api_router.include_router(owners.router, prefix="/owners", tags=["Owners"])
api_router.include_router(animals.router, prefix="/animals", tags=["Animals"])
api_router.include_router(vaccines.router, tags=["Vaccines"])