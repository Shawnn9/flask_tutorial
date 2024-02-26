from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    password: str
    email: EmailStr

class UserModel(BaseModel, EmailStr):
    pass
