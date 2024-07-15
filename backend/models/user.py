from base import BaseModel
from sqlalchemy import Column, String, Integer
from datetime import datetime

class UserModel(BaseModel):
    """User model that inherits from BaseModel"""
    
    __tablename__ = 'users'
    
    name = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    challenges_solved = Column(Integer, default=0)
    challenges_history = Column(String(1024), default="")
    badges = Column(String(1024), default="")
    points_collected = Column(Integer, default=0)
    starred_challenges = Column(String(1024), default="")
    
    def edit_profile(self, name=None):
        if name:
            self.name = name
        self.updated_at = datetime.now()
        self.save()
    
    def edit_password(self, password):
        self.password = password
        self.updated_at = datetime.now()
        self.save()
    
    def delete_account(self):
        self.delete()
    
    def submit_challenge(self, challenge):
        # Submit challenge logic (placeholder)
        print(f"Submitting challenge: {challenge}")
    
    def star_challenge(self, challenge):
        # Star challenge logic (placeholder)
        print(f"Starring challenge: {challenge}")
