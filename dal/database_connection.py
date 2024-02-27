from beanie import init_beanie
from models.user import UserModel
from config import config

async def connect_to_db():
    await init_beanie(
        database=config['MONGO_URI'],
        document_models=[UserModel],
        uri=config['MONGO_URI']
    )
