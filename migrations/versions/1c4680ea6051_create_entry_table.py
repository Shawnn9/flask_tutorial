from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['yourdatabase']

# Define a collection name
entry_collection = db['entry']

# Define a function to insert an entry
def insert_entry(user_id):
    entry_data = {
        'timestamp': datetime.utcnow(),
        'user_id': user_id
    }
    entry_collection.insert_one(entry_data)

# Define a function to retrieve entries
def get_entries():
    return entry_collection.find()

# Example usage
if __name__ == '__main__':
    # Insert an entry
    insert_entry(123)

    # Retrieve entries
    entries = get_entries()
    for entry in entries:
        print(entry)
