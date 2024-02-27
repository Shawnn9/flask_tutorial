from flask import Blueprint, render_template, session
from models.user import User

analytics_bp = Blueprint('analytics', __name__, static_url_path='static',template_folder='templates')


@analytics_bp.route('/analytics/')
async def analytics():
    users = await User.find().to_list()
    session_name = session.get('username', 'Guest')
    return render_template('analytics.html', users=users, session_name=session_name)
