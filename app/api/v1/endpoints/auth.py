from fastapi import APIRouter, Request, Response

from app.utils.logger import create_log

router = APIRouter()


@router.post("/register-user")
async def register_user(request: Request, response: Response):
    """
    Responsible for registering the user in DB when they login from the FE using auth0
    * If the user is already in the database, we do nothing and return success
    * If the user is not in the database, we add them and return success
    * If any error occurs, we return an error response
    """
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
