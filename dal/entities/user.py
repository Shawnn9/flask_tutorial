from datetime import datetime
from beanie import Document
from pydantic import EmailStr


class User(Document):
    username: str
    password: str
    email: EmailStr
    registration_date: datetime = datetime.utcnow()

