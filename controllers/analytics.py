from flask import Blueprint, render_template, session, request, redirect, url_for
from models.user import User  # Assuming you have a user model defined

analytics_bp = Blueprint('analytics', __name__, static_url_path='/static', template_folder='templates')

@analytics_bp.route('/analytics/')
def analytics():
    users = User.find()  # Assuming you have implemented a method to retrieve users asynchronously
    session_name = session.get('username', 'Guest')
    return render_template('analytics.html', users=users, session_name=session_name)

@analytics_bp.route('/delete_user/', methods=['POST'])
def delete_user():
    if 'username' in session:  # Ensure user is logged in
        username_to_delete = request.form.get('username')
        User.delete_one({'username': username_to_delete})  # Assuming you have implemented a method to delete a user asynchronously
    return redirect(url_for('analytics.analytics'))

@analytics_bp.route('/update_password/', methods=['POST'])
def update_password():
    if 'username' in session:  # Ensure user is logged in
        username = request.form.get('username')
        new_password = request.form.get('password')
        User.update_one({'username': username}, {'$set': {'password': new_password}})  # Assuming you have implemented a method to update password asynchronously
    return redirect(url_for('analytics.analytics'))
