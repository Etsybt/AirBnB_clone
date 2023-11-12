#!/usr/bin/python3
""" defining file storage """
from models.base_model import BaseModel
import json
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.state import State


class FileStorage:
    """Describe abstract storage engine"""

    __file_path = "file.json"
    __objects = {}

    def save(self):
        _dict = FileStorage.__objects
        obj_dict = {obj: _dict[obj].to_dict() for obj in _dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def new(self, obj):
        obj_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def all(self):
        return FileStorage.__objects

    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    classe_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(classe_name)(**o))
        except FileNotFoundError:
            return
