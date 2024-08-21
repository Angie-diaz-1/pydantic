from typing import List

from fastapi import APIRouter, HTTPException

from app.schemas.user_schema import User
from app.services.user_service import get_users_services, create_users_services

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

