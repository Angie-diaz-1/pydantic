
from pydantic import BaseModel, Field, EmailStr
from typing_extensions import Optional

class Address(BaseModel):
    city:str
    country:str
class UserRequest(BaseModel):
    name:str = Field(..., min_length=3)
    email: EmailStr
    age:Optional[int]=Field(None, ge=18)
    address:Address

class UserDTO(BaseModel):
    id:int
    name:str
    email:EmailStr
    age:Optional[int]
    city:str
    country:str

    class Config:
        orm_mode=True
