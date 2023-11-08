#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime
"""class BaseModel defined"""


class BaseModel:
    """defining BaseModel for the AirBnB_clone project"""
    def __init__(self, *args, **kwargs):
        """Launch a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pair of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        name_of_class = self.__class__.__name__
        return "[{}] ({}) {}".format(name_of_class, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        _dict = self.__dict__.copy()
        _dict['__class__'] = self.__class__.__name__
        _dict['created_at'] = self.created_at.isoformat()
        _dict['updated_at'] = self.updated_at.isoformat()
        return _dict
