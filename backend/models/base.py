#!/usr/bin/env python
"""Base model for all models in the application"""

from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

time = "%d-%m-%Y %H:%M:%S"
Base = declarative_base()


class BaseModel(Base):
    """ Abstraction model for all models in the application
        This class defines the basic attributes and methods that all models will have
        Don't use this class to create instances of models, use the inherited classes instead

        Attributes:
            id (str): The unique identifier for the model
            created_at (datetime): The date and time the model was created
            updated_at (datetime): The date and time the model was last updated
    """

    __abstract__ = True

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.now().isoformat())
    updated_at = Column(DateTime, default=datetime.now().isoformat())

    def __init__(self, *args, **kwargs):
        """Initialize the base model"""
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)

            if kwargs.get("id", None) is None:
                self.id = str(uuid4())

            self.created_at = datetime.strptime(
                self.created_at, time
            ) if "created_at" in kwargs else datetime.now()

            self.updated_at = datetime.strptime(
                self.updated_at, time
            ) if "updated_at" in kwargs else datetime.now()

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """Save the model to the database"""
        from backend.utils import STORAGE
        self.updated_at = datetime.now()
        STORAGE.new(self)
        STORAGE.save()

    def delete(self):
        """Delete the model from the database"""
        from backend.utils import STORAGE
        STORAGE.delete(self)

    def to_dict(self):
        """Return a dictionary representation of the model"""
        d = dict(self.__dict__).copy()
        if "_sa_instance_state" in d:
            del d["_sa_instance_state"]
        if "_password" in d:
            del d["_password"]
        if "created_at" in d:
            d["created_at"] = d["created_at"].strftime(time)
        if "updated_at" in d:
            d["updated_at"] = d["updated_at"].strftime(time)
        return d

    def __str__(self):
        """Return a string representation of the model"""
        return "[{:s}] ({})\n{}".format(self.__class__.__name__, self.id,
                                       self.to_dict())
