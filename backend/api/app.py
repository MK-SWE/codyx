#!/usr/bin/python3
""" App module """
from flask import *
from flask_cors import CORS
from flask_session import Session
from flask_limiter import Limiter
from backend.utils import STORAGE as db
from backend.api.blueprints.views import views
from backend.api.blueprints.config import Config
from backend.api.blueprints.auth import auth, Manager
from backend.api.blueprints.error_handler import errors


def create_app():
    """ Create and configure the app """
    from backend.utils import STORAGE
    # create the app
    app = Flask(__name__)

    # load the config
    app.config.from_object(Config)

    # register the blueprints
    app.register_blueprint(views)
    app.register_blueprint(auth)
    app.register_blueprint(errors)
    

    # create app extensions
    CORS(app)
    Session(app)

    # create the user manager
    Manager.init_app(app)

    # setup the rate limiter
    Limiter(app, default_limits=["200 per day", "50 per hour"])

    @app.before_request
    def before_request():
        """ Create a session for each request """
        session_id = request.cookies.get('session_id')
        if not session_id:
            return
        return session.get(session_id)

    @app.after_request
    def add_security_headers(response):
        """ Add security headers to the response """
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Content-Security-Policy'] = "default-src 'self'"
        response.headers['Referrer-Policy'] = 'same-origin'
        return response

    @app.teardown_appcontext
    def teardown_db(exception):
        """ Closes the database again at the end of the request """
        db.close()

    return app
