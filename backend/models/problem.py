from base import BaseModel
from sqlalchemy import Column, String, Integer

class ChallengeModel(BaseModel):
    """Challenge model that inherits from BaseModel"""
    
    __tablename__ = 'challenges'
    
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    input = Column(String(1024), nullable=False)
    output = Column(String(1024), nullable=False)
    difficulty = Column(String(128), nullable=False)
    starter_function = Column(String(1024), nullable=False)
    examples = Column(String(1024), nullable=False)
    stars = Column(Integer, default=0)
    solved = Column(Integer, default=0)
