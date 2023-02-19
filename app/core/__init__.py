from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'blank'
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