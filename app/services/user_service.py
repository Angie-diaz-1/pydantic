from app.repositories.user_repository import get_all_users
from app.schemas.user_schema import User


def get_users_services():
    return get_all_users()


def create_users_services(user: User):
    return user.add_user(user)
