from app.services.auth.jwt_validation import VerifyToken
from fastapi import APIRouter, Depends, Response, status
from fastapi.security import HTTPBearer

router = APIRouter()


@router.get("/public")
def public(response: Response):
    result = {"status": "success"}
    return result


@router.get("/private")
def private(response: Response, token: str = Depends(HTTPBearer())):
    result = VerifyToken(token.credentials).verify()

    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    # result = {"status": "success"}
    return result
