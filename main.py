from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from datetime import datetime
from flask_migrate import Migrate
from config import DevelopmentConfig

app = Flask(__name__, static_url_path='/static')
app.config['MONGO_URI'] = 'mongodb://localhost:27017/yourdatabase'
mongo = PyMongo(app)

class Entry:
    def __init__(self, user_id):
        self.timestamp = datetime.utcnow()
        self.user_id = user_id

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/index/', methods=['POST'])
def index():
    if request.method == 'POST':
        username = request.form['nm']
        password = request.form['password']

        # Check if the user already exists
        user = mongo.db.users.find_one({'username': username})

        if user:
            # If the user exists, update the password
            mongo.db.users.update_one({'username': username}, {'$set': {'password': password}})
        else:
            # If the user doesn't exist, create a new user
            new_user = {'username': username, 'password': password}
            mongo.db.users.insert_one(new_user)

            # Create a new entry for the user
            entry = {'user_id': new_user['_id'], 'timestamp': datetime.utcnow()}  # Assuming _id is automatically generated
            mongo.db.entries.insert_one(entry)

        flash('Logged in successfully!')
        session['username'] = username

        return redirect(url_for('page1'))

    return redirect(url_for('login'))

@app.route('/page1/')
def page1():
    # Retrieve user information from the session
    username = session.get('username')
    password = None  # There's no 'password' in the session

    return render_template('page1.html', username=username, password=password)

@app.route('/analytics/')
def analytics():
    username = session.get('name', 'Guest')  # Access the username from the session
    print("Username:", username)  # Print for debugging

    # Retrieve all users from the MongoDB collection
    users = mongo.db.users.find()

    return render_template('analytics.html', users=users, session_name=username)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
