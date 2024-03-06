from flask import Blueprint, render_template, session, request, redirect, url_for
from models.user import User

analytics_bp = Blueprint('analytics', __name__, static_url_path='/static', template_folder='templates')


@analytics_bp.route('/analytics')
def analytics():
    users = User.find()
    session_name = session.get('username', 'Guest')
    return render_template('analytics.html', users=users, session_name=session_name)


@analytics_bp.route('/delete_user/', methods=['POST'])
def delete_user():
    if 'username' in session:
        username_to_delete = request.form['username']
        User.delete_user({'username': username_to_delete})
    return redirect(url_for('analytics.analytics'))


@analytics_bp.route('/update_password/', methods=['POST'])
def update_password():
    if 'username' in session:
        username = request.form['username']
        new_password = request.form['new_password']
        User.update_password({'username': username}, {'$set': {'password': new_password}})
    return redirect(url_for('analytics.analytics'))
