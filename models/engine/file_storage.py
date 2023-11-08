#!/usr/bin/python3
import json
from models.base_model import BaseModel
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
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def new(self, obj):
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def all(self):
        return FileStorage.__objects

    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
