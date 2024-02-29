from flask import Blueprint, render_template, session


main_bp = Blueprint('main_bp', __name__, static_url_path='static',template_folder='templates')


@main_bp.route('/main/')
def main():
    username = session.get('username')
    return render_template('base.html', username=username)
