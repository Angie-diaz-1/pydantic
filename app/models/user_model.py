
from sqlalchemy import Column, String, Integer

from app.config.config import Base


class UserORM(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index = True)
    name= Column(String, index=True)
    email = Column(String, unique=True)
    age = Column(Integer, nullable=True)
    city= Column(String)
    country=Column(String)


