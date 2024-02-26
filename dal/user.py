from models.user import User

async def fetch_user_by_username(username: str) -> User:
    user = await User.get_one({"username": username})
    return user

async def create_user(username: str, password: str) -> User:
    user = User(username=username, password=password)
    await user.insert()
    return user

async def get_all_users():
    users = await User.find({}, {"password": 0}).to_list()
    return users

async def find_user_by_username(username: str):
    user = await User.get_one({"username": username})
    return user

async def update_user_password(username: str, new_password: str):
    user = await User.get_one({"username": username})
    if user:
        await user.update(password=new_password)
        return True
    else:
        return False
