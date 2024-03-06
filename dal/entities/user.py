from beanie import Document
from beanie import init_beanie

from controllers.auth import connect_to_db

class User(Document):
    username: str
    password: str
    email: str
