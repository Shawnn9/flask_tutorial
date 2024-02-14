import secrets

class Config:
    SECRET_KEY = secrets.token_hex(16)
    MONGO_URI = 'mongodb://localhost:27017/your_database'
    VERSION = "1.0.0.0"
