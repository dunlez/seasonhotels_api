from db.user_db import UserInDB
from typing import Dict
from db.user_db import update_user, get_user
from db.rooms_db import RoomsInDB
from db.rooms_db import get_room, update_room
from models.user_models import UserIn, UserOut
from models.rooms_models import RoomsIn, RoomsOut
from fastapi import FastAPI, HTTPException

seasonhotels = FastAPI()

@seasonhotels.get("/home")
async def root():
    return ("Bienvenido a nuestro Season Hotels")

@seasonhotels.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return  ("Usuario no registrado en nuestro sistema")
    return  ("Usuario registrado en Season Hotels")

@seasonhotels.get("/user/room/{username}")
async def get_reserva(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return  user_out

@seasonhotels.get("/room/{tipo_room}")
async def get_roomuser(tipo_room: str):
    room_in_db = get_room(tipo_room)
    if room_in_db == None:
        raise HTTPException(status_code=404, detail="La habitación no existe")
    room_out = RoomsOut(**room_in_db.dict())
    return room_out
