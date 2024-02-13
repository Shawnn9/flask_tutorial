import os

class Config:
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_secret_key'
    MONGO_URI = 'mongodb://localhost:27017/yourdatabase'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    MONGO_URI = 'mongodb://user:password@localhost:27017/db_name'
