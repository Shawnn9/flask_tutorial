from beanie import Document
from beanie import init_beanie
from pydantic import EmailStr


class User(Document):
    username: str
    password: str
    email: EmailStr
