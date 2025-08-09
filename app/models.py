from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import pytz

india_timezone = pytz.timezone("Asia/Kolkata")

def get_ist_time():
    return datetime.now(pytz.timezone("Asia/Kolkata"))

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return str(v)

class User(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    name: str
    phone: str
    email: str

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

class Message(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    sender_id: str
    receiver_id: str
    content: str
    timestamp: datetime = Field(default_factory=get_ist_time)


    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.strftime("%d-%b-%Y %I:%M:%S %p %Z")  
        }
