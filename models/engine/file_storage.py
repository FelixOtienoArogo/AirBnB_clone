#!/usr/bin/python3

"""
Now to serialises and deserialise JSON file

"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


class FileStorage:
    """
    A class that seralises instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """""Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """"Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """serialises __objects to the JSON file (path: __file_path)"""
        dic = {}
        for k, v in self.__objects.items():
            dic[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(dic))

    def reload(self):
        """deserialise the JSON file to __objects if the file exists"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                dic = json.loads(f.read())
                for k, v in dic.items():
                    self.__objects[k] = eval(v["__class__"])(**v)
