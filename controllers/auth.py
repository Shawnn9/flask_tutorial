from flask import Blueprint, render_template, redirect, url_for
from models.user import User
from beanie import init_beanie

auth_bp = Blueprint('auth', __name__,url_prefix='/auth')

async def connect_to_db():
    await init_beanie(database='your_database_name', document_models=[User], uri="mongodb://localhost:27017/")

@auth_bp.route('/')
def login():
    return redirect(url_for('auth.login'))

@auth_bp.route('/index', methods=['POST'])
async def index():
    await connect_to_db()
    return redirect(url_for('auth.base'))
