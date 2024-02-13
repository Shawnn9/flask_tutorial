import secrets

class Config:
    DEBUG = False
    TESTING = False
    VERSION = "0.1.3"
    SECRET_KEY = secrets.token_hex(16)
    MONGO_URI = 'mongodb://localhost:27017/your_database'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    MONGO_URI = 'mongodb://user:password@localhost:27017/db_name'
