from beanie import Document
from beanie import StringProperty

class UserModel(Document):
    username = StringProperty(required=True)
    password = StringProperty(required=True)
    email = StringProperty(required=True)


class User:
    pass