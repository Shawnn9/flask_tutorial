from flask import Flask
from controllers.analytics import analytics_bp
from config import config
from controllers.auth import auth_bp
from controllers.main import main_bp
from beanie import init_beanie

init_beanie()


app = Flask(__name__, static_url_path='/static')

app.secret_key = config['SECRET_KEY']

app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(analytics_bp)

if __name__ == '__main__':
    app.run(debug=True)
