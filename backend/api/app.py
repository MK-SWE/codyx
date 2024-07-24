#!/usr/bin/python3
""" Blueprint module """
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from utils import STORAGE
from flask_cors import CORS
from flask_session import Session
from flask_limiter import Limiter
from api.blueprints.views import views
from api.blueprints.config import Config
# from api.blueprints.auth import auth, Manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Manager.init_app(app)
    # Manager.login_view = 'auth.login'
    CORS(app)
    Session(app)
    Limiter(app, default_limits=["200 per day", "50 per hour"])
    app.register_blueprint(views)
    # app.register_blueprint(auth)

    @app.after_request
    def add_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Content-Security-Policy'] = "default-src 'self'"
        response.headers['Referrer-Policy'] = 'same-origin'
        return response

    @app.teardown_appcontext
    def teardown_db(exception):
        STORAGE.close()

    return app
