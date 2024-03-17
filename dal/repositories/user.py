from models.user import User
from typing import Optional


async def create_user(username: str, password: str, email: str) -> Optional[User]:
    try:
        user = User(username=username, password=password, email=email)
        await user.insert()
        return user
    except Exception as e:
        print(f"An error occurred while creating user: {e}")
        return None

async def get_user_by_id(user_id: str) -> Optional[User]:
    try:
        return await User.get_one({"_id": user_id})
    except Exception as e:
        print(f"An error occurred while getting user by ID: {e}")
        return None
