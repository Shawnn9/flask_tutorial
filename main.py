from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from dal.user_dal import fetch_user_by_username, create_user
from models.user import User
from beanie import init_beanie
from beanie.mongodb.client import MongoDBClient
from dal.user_dal import get_all_users

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'

async def connect_to_db():
    await init_beanie(database='your_database_name', document_models=[User], client=MongoDBClient())

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index/', methods=['POST'])
async def index():
    await connect_to_db()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = await fetch_user_by_username(username)

        if user:
            await user.update(password=password)
        else:
            user = await create_user(username, password)

            entry = {'user_id': user.id, 'timestamp': datetime.utcnow()}
            await db.entries.insert_one(entry)

        flash('Logged in successfully!')
        session['username'] = username

        return redirect(url_for('main_page'))

    return redirect(url_for('login'))

@app.route('/main/')
def main_page():
    username = session.get('username')
    return render_template('main_page.html', username=username)

@app.route('/analytics/')
async def analytics():
    username = session.get('username', 'Guest')
    users = await User.find().to_list()
    return render_template('analytics.html', users=users, session_name=username)

if __name__ == '__main__':
    import asyncio
    asyncio.run(connect_to_db())
    app.run()
