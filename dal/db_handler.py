from models.user import User

async def find_user_by_username(username: str):
    user = await User.get_one({"username": username})
    return user

async def update_user_password(username: str, new_password: str):
    user = await User.get_one({"username": username})
    if user:
        await user.update(password=new_password)
        return True
    return False
