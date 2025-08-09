import socketio

sio = socketio.AsyncServer(cors_allowed_origins="*")
socket_app = socketio.ASGIApp(sio)

connected_users = {}

@sio.event
def connect(sid, environ):
    print(f"User connected: {sid}")

@sio.event
def disconnect(sid):
    print(f"User disconnected: {sid}")
    for user_id in list(connected_users):
        if connected_users[user_id] == sid:
            del connected_users[user_id]

@sio.event
def register(sid, data):
    connected_users[data["user_id"]] = sid
    print(f"Registered user {data['user_id']} with SID {sid}")

@sio.event
def send_message(sid, data):
    receiver_sid = connected_users.get(data["receiver_id"])
    if receiver_sid:
        sio.emit("receive_message", data, to=receiver_sid)
