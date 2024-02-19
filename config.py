from functools import lru_cache

import secrets


@lru_cache(maxsize=1)
def get_config():
    return {
        'SECRET_KEY': secrets.token_hex(16),
        'MONGO_URI': 'mongodb://localhost:27017/your_database',
        'VERSION': "1.0.0.0"
    }


config = get_config()
