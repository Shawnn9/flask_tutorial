import secrets
import string

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(32))
    MONGO_URI = 'mongodb://localhost:27017/your_database'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    MONGO_URI = 'mongodb://user:password@localhost:27017/db_name'
