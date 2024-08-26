from typing import List

from fastapi import APIRouter, HTTPException

from app.schemas.user_schema import User
from app.services.user_service import get_users_services, create_users_services, delete_users_services, \
    user_by_id_services

router=APIRouter()

@router.get("/", response_model=List[User])
def get_users():
    users=get_users_services()
    if not users:
        raise HTTPException(status_code=404, detail="NO HAY USUARUOS")
    return users

@router.post("/", response_model=User)
def create_user(user: User):
    create_user=create_users_services(user)
    return create_user

@router.delete("/{id_user}", response_model=bool)
def  delete_user (id_user:int):
    delete_user  =delete_users_services(id_user)
    if not delete_user:
        raise HTTPException(status_code=404, detail="NO LO PUEDE ELIMINAR USUARIO NO ENCONTRADO")
    return delete_user

@router.get("/searchUid/{id_user}", response_model=User)
def get_user_by_id(id_user:int):
    users=user_by_id_services(id_user)
    if not users:
        raise HTTPException(status_code=404, detail="NO EXISTE ESE USUARIO REGISTRADO CON ESE CODGIO")
    return users