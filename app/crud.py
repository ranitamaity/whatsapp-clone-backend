from database import db
from schemas import UserCreate, MessageCreate

async def create_user(user: UserCreate):
    user_data = user.dict()
    result = await db.users.insert_one(user_data)
    user_data["_id"] = str(result.inserted_id)
    return user_data

async def read_users(user_id: str = None):
    if user_id:
        user = await db.users.find_one({"_id": user_id})
        if user:
            user["_id"] = str(user["_id"])
            return user
        return None
    users = []
    async for u in db.users.find():
        u["_id"] = str(u["_id"])
        users.append(u)
    return users

async def update_user(user_id: str, user: UserCreate):
    updated = await db.users.update_one(
        {"_id": user_id},
        {"$set": user.dict()}
    )
    if updated.modified_count == 1:
        return await read_users(user_id)
    return None

async def delete_user(user_id: str):
    result = await db.users.delete_one({"_id": user_id})
    return result.deleted_count == 1


async def create_message(message: MessageCreate):
    message_data = message.dict()
    result = await db.messages.insert_one(message_data)
    message_data["_id"] = str(result.inserted_id)
    inserted_doc = await db.messages.find_one({"_id": result.inserted_id})
    timestamp = inserted_doc["timestamp"]
    message_data["timestamp"]= str(timestamp)
    return message_data

async def read_messages(sender_id: str, receiver_id: str):
    query = {
        "$or": [
            {"sender_id": sender_id, "receiver_id": receiver_id},
            {"sender_id": receiver_id, "receiver_id": sender_id}
        ]
    }
    messages = []
    async for msg in db.messages.find(query).sort("timestamp"):
        msg["_id"] = str(msg["_id"])
        messages.append(msg)
    return messages

async def update_message(message_id: str, message: MessageCreate):
    updated = await db.messages.update_one(
        {"_id": message_id},
        {"$set": message.dict()}
    )
    if updated.modified_count == 1:
        return await db.messages.find_one({"_id": message_id})
    return None

async def delete_message(message_id: str):
    result = await db.messages.delete_one({"_id": message_id})
    return result.deleted_count == 1
