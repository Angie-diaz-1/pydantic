from sqlalchemy.orm import Session

from app.repositories.user_repository import get_all_users, add_user
from app.schemas.user_schema import UserRequest


def get_users_services(db:Session):
    return get_all_users(db)


def create_users_services(db:Session, user: UserRequest):
    return add_user(db, user)
