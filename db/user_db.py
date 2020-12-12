from typing import Dict
from pydantic import BaseModel


class UserInDB(BaseModel):
    username: str
    password: str
    estado: str
    

database_users = Dict[str, UserInDB]
database_users = {
    "janruva": UserInDB(**{"username": "janruva",
                           "password": "janruva92",
                           "estado": "Usuario registrado en la habitación Superior"}),
    "alexis": UserInDB(**{"username": "alexis",
                          "password": "alex256",
                          "estado": "Usuario registrado en la habitación Deluxe"}),
    "lorena": UserInDB(**{"username": "lorena",
                            "password": "lorena20",
                            "estado": "Usuario registrado en la habitación Junior"}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db