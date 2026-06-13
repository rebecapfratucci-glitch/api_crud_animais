# app/schemas.py

from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime


class AnimalBase(BaseModel):

    tipo: str
    status: str
    descricao: str
    localizacao: str
    foto: str | None = None

    nome_contato: str
    telefone_contato: str
    email_contato: EmailStr


class AnimalCreate(AnimalBase):
    pass


class AnimalUpdate(AnimalBase):
    pass


class AnimalResponse(AnimalBase):

    id: int
    data_registro: datetime

    class Config:
        from_attributes = True