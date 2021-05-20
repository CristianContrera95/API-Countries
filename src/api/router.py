from fastapi import APIRouter
from api.views import countries_view


api_router = APIRouter()
api_router.include_router(countries_view.router, prefix="/countries")


@api_router.get("/")
async def hello():
    return {"server": "API Working"}
