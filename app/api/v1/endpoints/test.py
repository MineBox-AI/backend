from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.security import HTTPBearer

from app.services.auth.jwt_validation import VerifyToken
from app.utils.logger import create_log

router = APIRouter()


@router.post("/test")
async def test(request: Request, response: Response):
    data = await request.json()
    print("Received Auth0 user data:")
    print(f"Email: {data.get('email')}")
    print(f"Auth0 ID: {data.get('auth0Id')}")
    create_log("info", f"Auth0 webhook received for user {data.get('email')}")
    print("Full payload:", data)

    result = {
        "status": "success",
        "received_data": data,
    }

    return result


@router.get("/public")
def public(response: Response):
    create_log("info", "Public Endpoint")
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
