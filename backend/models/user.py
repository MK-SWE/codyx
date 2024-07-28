import bcrypt
from flask_login import UserMixin
from .base import BaseModel, Base
from sqlalchemy import Column, String, Integer, Boolean
from datetime import datetime
from backend.engine.execEngine import DOCKER
import json
import ast



class User(BaseModel, Base, UserMixin):
    """User class to interact with the API.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        _password (str): The hashed password of the user.
        full_name (str): The full name of the user.
        badges (str): A JSON string representing the badges earned by the user.
        points (int): The total points earned by the user.
        starred_challenges (str): A JSON string representing the IDs of the challenges starred by the user.
        active (bool): Indicates whether the user is active or not.
        authenticated (bool): Indicates whether the user is authenticated or not.
        role (str): The role of the user.
    """

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
    
    def submit_challenge(self, challenge, code: str, lang: str) -> dict:
        """Submit a challenge and calculate the score.

        Args:
            challenge (Challenge): The challenge object to submit.
            code (str): The code to be tested.
            lang (str): The programming language of the code.

        Returns:
            dict: A dictionary containing the score and a list of failed tests.
        """
        if challenge:
            res = DOCKER.run_tests(self.id, challenge.name, code, lang)
            res = ast.literal_eval(res)
            failed_tests = []
            for k, v in res.items():
                if v["status"] != 'OK':
                    failed_tests.append(k)
            if len(failed_tests) > 0:
                score = 1 - (len(failed_tests) / len(res.keys()))
            else:
                score = 1
            if challenge.difficulty == 'easy':
                self.points += 10 * score
            elif challenge.difficulty == 'medium':
                self.points += 20 * score
            else:
                self.points += 30 * score
            self.save()
            res = {
                "score": f"{score * 100:.2f}%",
                "failed_tests": failed_tests
            }
            return res

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
        from backend.utils import STORAGE as db
        return db.session.query

    def get(user_id):
        """User get method."""
        from backend.utils import STORAGE as db
        return db.query(User).get(user_id)