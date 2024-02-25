from models.user import UserModel

async def fetch_user_by_username(username: str) -> UserModel:
    user = await UserModel.find_one({"username": username})
    return user

async def create_user(username: str, password: str) -> UserModel:
    user = UserModel(username=username, password=password)
    await user.insert()
    return user
