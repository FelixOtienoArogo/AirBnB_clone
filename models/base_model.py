#!/usr/bin/python3
"""
This is the BaseModel to define all common methods for other classes
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """
    We house all common attributes of other classes
    """
    def __init__(self, *args, **kwargs):
        """
        This is the constructor for this class

        Arguments:
            *args:list arguments
            **kwargs: dictionary arguments
        """
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(value, time_format)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """This prints the details about the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        key_value = {}

        for key, value in self.__dict__.items():
            if key == "my_number" or key == "name":
                key_value[key] = value
        key_value["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "updated_at" or key == "created_at":
                key_value[key] = value.isoformat()
            elif key == "id":
                key_value[key] = value
            elif key == "created_at":
                key_value[key] = value.isoformat()

        key_value["__class__"] = self.__class__.__name__
        return key_value
