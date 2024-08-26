from typing import List, Optional
from app.schemas.user_schema import User

#simulador base de datos
fake_user_db: List[User] = []


#Obtener users
def get_all_users() -> List[User]:
    return fake_user_db


def add_user(user: User) -> User:
    fake_user_db.append(user)
    return fake_user_db[-1]


def delete_user(user_id: int) -> bool:
    for user in fake_user_db:
        if user.id == user_id:
            fake_user_db.remove(user)
            return True
    return False


def user_by_id(user_id: int) -> Optional[User]:
    for user in fake_user_db:
        if user.id == user_id:
            return user
    return None
