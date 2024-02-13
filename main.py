from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from config import DevelopmentConfig

app = Flask(__name__, static_url_path='/static')
app.config.from_object(DevelopmentConfig)

client = MongoClient(app.config['MONGO_URI'])
db = client.get_default_database()

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index/', methods=['POST'])
def index():
    if request.method == 'POST':
        username = request.form['nm']
        password = request.form['password']

        user = db.users.find_one({'username': username})

        if user:
            db.users.update_one({'username': username}, {'$set': {'password': password}})
        else:
            new_user = {'username': username, 'password': password}
            db.users.insert_one(new_user)

            entry = {'user_id': new_user['_id'], 'timestamp': datetime.utcnow()}
            db.entries.insert_one(entry)

        flash('Logged in successfully!')
        session['username'] = username

        return redirect(url_for('mainPage'))

    return redirect(url_for('login'))

@app.route('/mainPage/')
def mainPage():
    username = session.get('username')
    password = session.get('password')

    return render_template('mainPage.html', username=username, password=password)

@app.route('/analytics/')
def analytics():
    username = session.get('name', 'Guest')
    users = db.users.find()

    return render_template('analytics.html', users=users, session_name=username)


if __name__ == '__main__':
    app.run(debug=True)
