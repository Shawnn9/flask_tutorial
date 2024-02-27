from controllers.auth import connect_to_db
from models.user import User

async def with_db_connection(func):
    async def wrapper(*args, **kwargs):
        await connect_to_db()
        return await func(*args, **kwargs)
    return wrapper

@with_db_connection
async def create_user(username: str, password: str, email: str) -> User:
    user = User(username=username, password=password, email=email)
    await user.insert()
    return user

@with_db_connection
async def get_user_by_id(user_id: str) -> User:
    return await User.get_one({"_id": user_id})

@with_db_connection
async def fetch_user_by_username(username: str) -> User:
    return await User.get_one({"username": username})

@with_db_connection
async def get_all_users() -> list[User]:
    return await User.find({}, {"password": 0}).to_list()

@with_db_connection
async def update_user_password(username: str, new_password: str) -> bool:
    user = await fetch_user_by_username(username)
    if user:
        await user.update(password=new_password)
        return True
    return False
