async def find_user_by_username(username: str):
    user = await db.users.find_one({'username': username})
    return user

async def update_user_password(username: str, new_password: str):
    await db.users.update_one({'username': username}, {'$set': {'password': new_password}})
