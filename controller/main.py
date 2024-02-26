from flask import Flask
from auth import auth_bp
from main import main_bp
from analytics import analytics_bp

app = Flask(__name__, static_url_path='../static')
app.secret_key = 'your_secret_key'
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(analytics_bp)

if __name__ == '__main__':
    app.run()


def main_bp():
    return None