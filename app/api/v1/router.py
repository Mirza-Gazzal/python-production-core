from fastapi import APIRouter
from app.api.v1.registry import ROUTES


router = APIRouter()

for r,prefix, tags in ROUTES :
    router.include_router(r, prefix=prefix, tags= tags)