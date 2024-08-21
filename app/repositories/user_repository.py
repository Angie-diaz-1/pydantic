from typing import List
from app.schemas.user_schema import User

#simulador base de datos
fake_user_db:List[User]=[]

#Obtener users
def get_all_users()-> List[User]:
    return fake_user_db

def add_user(user:User)->User:
    fake_user_db.append(user)
    return fake_user_db[-1]