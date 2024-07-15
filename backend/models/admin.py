from .base import BaseModel
from sqlalchemy import Column, String

class Admin(BaseModel):
    """Admin model that inherits from BaseModel"""
    
    __tablename__ = 'admins'
    
    username = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    
    def add_challenge(self, challenge):
        # Add challenge to database (placeholder)
        print(f"Adding challenge: {challenge}")
    
    def edit_challenge(self, challenge):
        # Edit challenge in database (placeholder)
        print(f"Editing challenge: {challenge}")
    
    def remove_challenge(self, challenge):
        # Remove challenge from database (placeholder)
        print(f"Removing challenge: {challenge}")
    
    def suspend_account(self, user):
        # Suspend user account (placeholder)
        print(f"Suspending account for user: {user}")
