from typing import List

from sqlalchemy.orm import session, Session

from app.models.user_model import UserORM
from app.schemas.user_schema import UserRequest


#Obtener users
def get_all_users(bd: session) -> List[UserORM]:
    return bd.query(UserORM).all()


def add_user(bd: Session, user: UserRequest) -> UserORM:
    bd_user = UserORM(
        name=user.name,
        email=user.email,
        age=user.age,
        city=user.address.city,
        country=user.address.country,
    )
    bd.add(bd_user)
    bd.commit()
    return bd_user
