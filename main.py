# app/main.py

from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

import models
import crud
import schemas

from database import engine
from database import SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Cadastro de Animais",
    version="1.0.0"
)

# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, PUT, DELETE, OPTIONS, etc.
    allow_headers=["*"]   # Permite todos os headers
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.get("/")
def home():

    return {
        "nome": "API Cadastro de Animais",
        "versao": "1.0.0",
        "docs": "/docs"
    }


@app.post(
    "/animais",
    response_model=schemas.AnimalResponse
)
def criar_animal(
    animal: schemas.AnimalCreate,
    db: Session = Depends(get_db)
):

    return crud.criar_animal(
        db,
        animal
    )


@app.get(
    "/animais",
    response_model=list[schemas.AnimalResponse]
)
def listar_animais(
    db: Session = Depends(get_db)
):

    return crud.listar_animais(db)


@app.get(
    "/animais/{animal_id}",
    response_model=schemas.AnimalResponse
)
def buscar_animal(
    animal_id: int,
    db: Session = Depends(get_db)
):

    animal = crud.buscar_animal(
        db,
        animal_id
    )

    if not animal:
        raise HTTPException(
            status_code=404,
            detail="Animal não encontrado"
        )

    return animal


@app.put(
    "/animais/{animal_id}",
    response_model=schemas.AnimalResponse
)
def atualizar_animal(
    animal_id: int,
    dados: schemas.AnimalUpdate,
    db: Session = Depends(get_db)
):

    animal = crud.atualizar_animal(
        db,
        animal_id,
        dados
    )

    if not animal:
        raise HTTPException(
            status_code=404,
            detail="Animal não encontrado"
        )

    return animal


@app.delete("/animais/{animal_id}")
def excluir_animal(
    animal_id: int,
    db: Session = Depends(get_db)
):

    sucesso = crud.excluir_animal(
        db,
        animal_id
    )

    if not sucesso:
        raise HTTPException(
            status_code=404,
            detail="Animal não encontrado"
        )

    return {
        "mensagem": "Animal removido com sucesso"
    }
