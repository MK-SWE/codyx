#!/usr/bin/python3
""" Configuration module """

from os import getenv, path
from redis import StrictRedis as Redis
from dotenv import load_dotenv
from datetime import timedelta
from backend.utils import STORAGE

parent_dir = path.dirname(path.dirname(path.abspath(__file__)))
dotenv_path = path.join(parent_dir, '.api.env')
load_dotenv(dotenv_path=dotenv_path)


class Config(object):
    """ Parent configuration class """
    # APP SETTINGS
    DEBUG = False
    APP_NAME = 'CodyX'
    SSL_REDIRECT = True
    CSRF_ENABLED = True
    SECRET_KEY = getenv('SECRET_KEY')
    SECURITY_PASSWORD_SALT = getenv('SECURITY_PASSWORD_SALT')

    # DATABASE SETTINGS
    SQLALCHEMY_DATABASE_URI = STORAGE.get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # LOGIN MANAGER SETTINGS
    LOGIN_VIEW = 'auth.login'
    LOGOUT_VIEW = 'auth.logout'
    REFRESH_VIEW = 'auth.login'
    USE_SESSION_FOR_NEXT = True
    SESSION_PROTECTION = 'strong'
    REMEMBER_COOKIE_NAME = 'session_id'
    USE_SESSION_FOR_NEXT = True
    REMEBER_COOKIE_DURATION = timedelta(days=1)
    LOGIN_MESSAGE = 'You Are Not Logged In, Please Log In To Continue.'
    REFRESH_MESSAGE = 'Your Session Has Expired, Please Log In To Continue.'

    # SESSION SETTINGS
    REDIS_URL = getenv('REDIS_URL')
    SESSION_PERMANENT = True
    SESSION_USE_SIGNER = True
    SESSION_COOKIE_SECURE = True
    SESSION_FILE_THRESHOLD = 500
    SESSION_COOKIE_SAMESITE='Lax'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_KEY_PREFIX = 'session:'
    SESSION_CLEANUP_N_REQUESTS = 1000
    SESSION_COOKIE_NAME = 'session_id'
    SESSION_REFRESH_EACH_REQUEST = True
    SESSION_PERMANENT = True
    SESSION_FILE_DIR = '/tmp/flask_session'
    SESSION_TYPE = 'redis' if REDIS_URL else 'filesystem'
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    SESSION_REDIS = Redis.from_url(REDIS_URL) if REDIS_URL else None
