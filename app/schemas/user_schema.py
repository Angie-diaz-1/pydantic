from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class Adress(BaseModel):
    city:str
    country:str

class User(BaseModel):
    id:int=Field(...,gt=0) # ... quiere decir que el campo es obligatorio
    name:str = Field(...,min_length=3)
    email:EmailStr = Field(...,min_length=3)
    age: Optional[int]=Field(None, ge=18)
    addres:Addres=Field(...)