from beanie import Document
from pydantic import EmailStr


class User(Document):
    username: str
    password: str
    email: EmailStr
