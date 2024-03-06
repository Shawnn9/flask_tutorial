from controllers.auth import connect_to_db
from models.user import User
from beanie import init_beanie
from typing import Optional

async def initialize_database() -> None:
    await connect_to_db()
    await init_beanie()

async def create_user(username: str, password: str, email: str) -> Optional[User]:
    try:
        user = User(username=username, password=password, email=email)
        await user.insert()
        return user
    except Exception as e:
        return None

async def get_user_by_id(user_id: str) -> Optional[User]:
    try:
        return await User.get_one({"_id": user_id})
    except Exception as e:
        return None

