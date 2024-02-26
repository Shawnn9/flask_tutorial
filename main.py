from flask import Flask
from controller import main_bp
from controller.analytics import analytics_bp
from controller.auth import auth_bp


app = Flask(__name__, static_url_path='static')
app.secret_key = 'your_secret_key'
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(analytics_bp)

if __name__ == '__main__':
    app.run()

