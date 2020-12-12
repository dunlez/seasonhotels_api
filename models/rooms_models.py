from pydantic import BaseModel
from datetime import datetime

class RoomsIn(BaseModel):
    username: str
    tipo_room: str

class RoomsOut(BaseModel):
    id_room: int
    username: str 
    tipo_room: str
    camas: str
    ocupacion: str
    superficie: str
    vistas: str
    tarifa_basica: int