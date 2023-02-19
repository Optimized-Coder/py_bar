from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'blank'
    app.config['FLASK_ENV'] = 'development'
    

    # define BP's

    # import models

    # test route
    @app.route('/test')
    def test():
        return '<h1>Test Successful</h1>'

    return app