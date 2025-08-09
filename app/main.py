from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import users, messages
from socketio_server import socket_app
from datetime import datetime
import pytz

app = FastAPI()
app.mount("/ws", socket_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(messages.router, prefix="/messages", tags=["Messages"])

@app.get("/test-time")
def test_time():
    india_timezone = pytz.timezone("Asia/Kolkata")
    ist_time = datetime.now(india_timezone)
    return {
        "time": ist_time.strftime("%d-%b-%Y %I:%M:%S %p %Z")
    }