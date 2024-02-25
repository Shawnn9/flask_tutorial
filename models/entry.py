from datetime import datetime


class Entry:
    def __init__(self, user_id: str):
        self.timestamp = datetime.utcnow()
        self.user_id = user_id
