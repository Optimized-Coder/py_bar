from flask import Flask
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get("secret_key")
    app.config['FLASK_ENV'] = 'development'
    
    # define BP's
    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    # import models

    # test route
    @app.route('/test')
    def test():
        return '<h1>Test Successful</h1>'

    return app