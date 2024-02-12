import secrets

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = secrets.token_urlsafe(32)
    MONGO_URI = 'mongodb://localhost:27017/yourdatabase'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    MONGO_URI = 'mongodb://user:password@localhost:27017/db_name'
    # Add other production-specific configurations
