from pydantic import BaseModel,Field
from datetime import datetime
import pytz

def get_ist_time():
    ist = pytz.timezone("Asia/Kolkata")
    return datetime.now(ist)

class UserCreate(BaseModel):
    name: str
    phone: str
    email: str

class MessageCreate(BaseModel):
    sender_id: str
    receiver_id: str
    content: str
    timestamp: datetime = Field(default_factory=get_ist_time)