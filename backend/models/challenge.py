import json
from models.base import BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.mysql import JSON

class Challenge(BaseModel):
    """Challenge model that inherits from BaseModel"""
    
    __tablename__ = 'challenges'
    
    name = Column(String(128), nullable=False, unique=True)
    description = Column(String(4096), nullable=False)
    ex_input = Column(String(1024), nullable=False)
    output = Column(String(1024), nullable=False)
    difficulty = Column(String(128), nullable=False)
    _starter_function = Column('template', JSON, nullable=False)
    examples = Column(String(1024), nullable=False)
    stars = Column(Integer, default=0)
    solved = Column(Integer, default=0)

    def __init__(self, *args, **kwargs):
        """Challenge class constructor"""
        super().__init__(*args, **kwargs)

    @property
    def starter_function(self):
        """Starter function getter method."""
        return self._starter_function

    @starter_function.setter
    def starter_function(self, value):
        """Starter function setter method."""
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON string")
        self._starter_function = json.dumps(value)
