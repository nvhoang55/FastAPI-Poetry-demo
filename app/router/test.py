from fastapi import APIRouter, Depends

from app.dependencies.authentication.jwt import has_access

test_route = APIRouter(
    prefix="/security"
)


@test_route.post("/has-access")
async def test_security(payload=Depends(has_access)):
    return "accessed"
