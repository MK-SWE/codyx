import bcrypt
from flask_user import UserMixin
from .base import BaseModel, Base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Boolean
from datetime import datetime
from backend.engine.execEngine import DOCKER
import json

db = SQLAlchemy()

class User(BaseModel, Base, UserMixin, db.Model):
    """User class to interact with the API."""

    __tablename__ = 'users'

    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    _password = Column('password', String(128), nullable=False)
    full_name = Column(String(60), nullable=False)
    badges = Column(String(1024), default='[]')
    points = Column(Integer, default=0)
    starred_challenges = Column(String(1024), default='[]')
    active = Column(Boolean, default=True)
    authenticated = Column(Boolean, default=False)
    role = Column(String(60), default='user')

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }

    def __init__(self, *args, **kwargs):
        """User class constructor"""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        """Password getter method."""
        return self._password

    @password.setter
    def password(self, value):
        """Password setter method """
        value = value.encode() if isinstance(value, str) else value
        self._password = bcrypt.hashpw(value, bcrypt.gensalt())

    def check_password(self, password):
        """Password validation method """
        return bcrypt.checkpw(password.encode(), self._password.encode())

    def edit_profile(self, **kwargs):
        """ Edit user profile """
        for k, v in kwargs.items():
            if k in ['username', 'email', 'full_name']:
                setattr(self, k, v)
        self.updated_at = datetime.now()
        self.save()
    
    def edit_password(self, password):
        """ Edit user password """
        self.password = password
        self.updated_at = datetime.now()
        self.save()
    
    def delete_account(self):
        """ Delete user account """
        self.delete()
    
    def submit_challenge(self, challenge, code: str, lang: str):
        """ Submit challenge """
        if challenge:
            res = DOCKER.run_tests(self.id, challenge.name, code, lang)
            if res:
                res = json.loads(res)
            else:
                res = {}
            failed_tests = []
            for k, v in res.items():
                if v["status"] != 'OK':
                    failed_tests.append(k)
            if len(failed_tests) > 0:
                score = (100 - ((len(failed_tests) / len(res.keys())) * 100)) / 100
            else:
                score = 1
            if challenge.difficulty == 'easy':
                self.points += 10 * score
            elif challenge.difficulty == 'medium':
                self.points += 20 * score
            else:
                self.points += 30 * score
            self.save()
            return f'{score}%', failed_tests

    def star_challenge(self, challenge):
        # Star challenge logic (placeholder)
        if challenge:
            if challenge.id not in self.starred_challenges:
                self.starred_challenges.append(challenge.id)
                self.save()

    @property
    def is_authenticated(self):
        """User authentication method."""
        return self.authenticated

    @property
    def is_active(self):
        """User active method."""
        return self.active

    @classmethod
    def query(cls):
        """User query method."""
        return db.session.query
