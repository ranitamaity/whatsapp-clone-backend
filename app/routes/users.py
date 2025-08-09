from fastapi import APIRouter
from schemas import UserCreate
from crud import create_user, read_users

router = APIRouter()

@router.post("/")
async def register_user(user: UserCreate):
    return await create_user(user)

@router.get("/")
async def fetch_users():
    return await read_users()
