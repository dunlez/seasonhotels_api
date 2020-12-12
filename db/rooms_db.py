from typing import Dict
from pydantic import BaseModel

class RoomsInDB(BaseModel):
    id_room: int
    username: str 
    tipo_room: str
    camas: str
    ocupacion: str
    superficie: str
    vistas: str
    tarifa_basica: int

database_rooms = Dict[str, RoomsInDB]
database_rooms = {
    "Superior": RoomsInDB(**{"id_room": 101,
                            "username": "janruva",
                            "tipo_room": "Superior",
                           "camas": "Cama medida doble",
                           "ocupacion": "2 personas",
                           "superficie": "25 mt2",
                           "vistas": "Patio",
                           "tarifa_basica": 100000,
                           }),
    "Deluxe": RoomsInDB(**{"id_room": 201,
                            "username": "alexis",
                            "tipo_room": "Deluxe",
                           "camas": "Cama medida queen",
                           "ocupacion": "2 personas",
                           "superficie": "30 mt2",
                           "vistas": "Museo, plaza o jardines",
                           "tarifa_basica": 200000,
                           }),
     "Junior": RoomsInDB(**{"id_room": 301,
                            "username": "lorena",
                            "tipo_room": "Junior",
                           "camas": "Cama medida king",
                           "ocupacion": "2 personas",
                           "superficie": "45 mt2",
                           "vistas": "Mar, playa",
                           "tarifa_basica": 300000,
                           }),
}

def get_room(tipo_room: str):
    if tipo_room in database_rooms.keys():
        return database_rooms[tipo_room]
    else:
        return None

def update_room(room_in_db: RoomsInDB):
    database_rooms[room_in_db.id_room] = room_in_db
    return room_in_db