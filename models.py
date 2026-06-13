# app/models.py

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from database import Base


class Animal(Base):

    __tablename__ = "animais"

    id = Column(Integer, primary_key=True, index=True)

    tipo = Column(String(50), nullable=False)

    status = Column(String(50), nullable=False)

    descricao = Column(String(500), nullable=False)

    localizacao = Column(String(255), nullable=False)

    data_registro = Column(
        DateTime,
        default=datetime.now
    )

    foto = Column(String(500))

    nome_contato = Column(String(100))

    telefone_contato = Column(String(30))

    email_contato = Column(String(150))