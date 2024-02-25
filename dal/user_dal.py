from models.user import UserModel

async def fetch_user_by_username(username: str) -> UserModel:
    user = await UserModel.get_one({"username": username})
    return user

async def create_user(username: str, password: str) -> UserModel:
    user = UserModel(username=username, password=password)
    await user.insert()
    return user

async def get_all_users():
    users = await UserModel.find({}, {"password": 0}).to_list()
    return users
