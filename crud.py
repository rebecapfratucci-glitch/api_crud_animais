# app/crud.py

from sqlalchemy.orm import Session

import models
import schemas


def criar_animal(
    db: Session,
    animal: schemas.AnimalCreate
):

    novo_animal = models.Animal(
        **animal.model_dump()
    )

    db.add(novo_animal)

    db.commit()

    db.refresh(novo_animal)

    return novo_animal


def listar_animais(
    db: Session
):

    return db.query(
        models.Animal
    ).all()


def buscar_animal(
    db: Session,
    animal_id: int
):

    return db.query(
        models.Animal
    ).filter(
        models.Animal.id == animal_id
    ).first()


def atualizar_animal(
    db: Session,
    animal_id: int,
    dados: schemas.AnimalUpdate
):

    animal = buscar_animal(
        db,
        animal_id
    )

    if not animal:
        return None

    for campo, valor in dados.model_dump().items():
        setattr(animal, campo, valor)

    db.commit()

    db.refresh(animal)

    return animal


def excluir_animal(
    db: Session,
    animal_id: int
):

    animal = buscar_animal(
        db,
        animal_id
    )

    if not animal:
        return False

    db.delete(animal)

    db.commit()

    return True