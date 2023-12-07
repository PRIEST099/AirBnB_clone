#!/usr/bin/python3
"""a model representing a base through a class"""
import uuid
from datetime import datetime


class BaseModel():
    """a representation of a base"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """updates the updated_at variable"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary representation of the class"""
        obj = self.__dict__.copy()

        obj['__class__'] = self.__class__.__name__

        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()

        return obj

