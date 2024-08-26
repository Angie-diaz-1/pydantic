from app.repositories.user_repository import get_all_users, add_user, delete_user, user_by_id
from app.schemas.user_schema import User


def get_users_services():
    return get_all_users()


def create_users_services(user: User):
    return add_user(user)

def delete_users_services(id_user : int):
    return  delete_user(id_user)

def  user_by_id_services(id_user : int):
    return  user_by_id(id_user)

