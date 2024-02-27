from beanie import init_beanie
from models.user import UserModel

async def connect_to_db():
    await init_beanie(
        database='your_database_name',
        document_models=[UserModel],
        uri="mongodb://localhost:27017/"
    )
