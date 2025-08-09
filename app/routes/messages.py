from fastapi import APIRouter
from schemas import MessageCreate
from crud import create_message, read_messages

router = APIRouter()

@router.post("/")
async def send_message(message: MessageCreate):
    return await create_message(message)

@router.get("/{sender_id}/{receiver_id}")
async def get_chat(sender_id: str, receiver_id: str):
    return await read_messages(sender_id, receiver_id)