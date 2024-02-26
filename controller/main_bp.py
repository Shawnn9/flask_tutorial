from flask import Blueprint, render_template, session
from models.user import User

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/main/')
def main():
    username = session.get('username')
    return render_template('main.html', username=username)

