from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):
    username: str
    password: str
    email: EmailStr
