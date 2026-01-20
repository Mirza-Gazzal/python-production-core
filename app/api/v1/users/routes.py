from fastapi import  APIRouter
from app.system.responses.api_response import ok

router = APIRouter()


@router.get("/health")
def users_health():
     return ok({"module": "users"}, message="Users module is healthy")