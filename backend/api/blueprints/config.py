#!/usr/bin/python3
""" Configuration module """

from os import getenv, path
from redis import Redis
from dotenv import load_dotenv
from datetime import timedelta

parent_dir = path.dirname(path.dirname(path.abspath(__file__)))
dotenv_path = path.join(parent_dir, '.api.env')
load_dotenv(dotenv_path=dotenv_path)


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = getenv('SECRET_KEY')
    SECURITY_PASSWORD_SALT = getenv('SECURITY_PASSWORD_SALT')
    REDIS_URL = getenv('REDIS_URL')
    SESSION_TYPE = 'redis' if REDIS_URL else 'filesystem'
    SESSION_REDIS = Redis.from_url(REDIS_URL) if REDIS_URL else None
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE='Lax'
    SESSION_COOKIE_NAME = 'session_id'
    SESSION_REFRESH_EACH_REQUEST = True
