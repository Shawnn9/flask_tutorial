from datetime import datetime
from pymongo import MongoClient
from config import Config
from flask import  Flask, render_template,request,redirect, url_for, session, flash

from flask_pymongo import PyMongo
from config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index/', methods=['POST'])
def index():
    global new_user
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']

        user = mongo.db.users.find_one({'username': username})
        if user:
            mongo.db.users.update_one({'username': username}, {'$set': {'password': password}})
        else:
            new_user = {'username': username, 'password': password}
            mongo.db.users.insert_one(new_user)

            entry = {'user_id': str(new_user['_id']), 'timestamp': datetime.utcnow()}
            mongo.db.entries.insert_one(entry)

        flash('Logged in successfully!')
        session['user_id'] = str(new_user['_id'])

        return redirect(url_for('mainPage'))

    return redirect(url_for('login'))

@app.route('/mainPage/')
def page1():
    user_id = session.get('user_id')
    user = mongo.db.users.find_one({'_id': user_id})

    if user:
        username = user['username']
        password = None
    else:
        flash('User not found!')
        return redirect(url_for('login'))

    return render_template('mainPage.html', username=username, password=password)

@app.route('/analytics/')
def analytics():
    users = mongo.db.users.find()
    return render_template('analytics.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)