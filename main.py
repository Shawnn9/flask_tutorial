from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient

app = Flask(__name__, static_url_path='/static')
client = MongoClient(app.config['MONGO_URI'])
db = client.get_default_database()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/index/', methods=['POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
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

        return redirect(url_for('main_page'))

    return redirect(url_for('login'))


@app.route('/main/')
def main_page():
    username = session.get('username')

    return render_template('main_page.html', username=username)


@app.route('/analytics/')
def analytics():
    username = session.get('name', 'Guest')
    users = db.users.find()

    return render_template('analytics.html', users=users, session_name=username)


if __name__ == '__main__':
    app.run()
