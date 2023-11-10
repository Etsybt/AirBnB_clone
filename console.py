#!/usr/bin/python3
import cmd
import shlex
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    Class = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Enter quit to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program"""
        print("")
        return True

    def emptyline(self):
        """Does nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        _input = arg.split()
        if len(_input) == 0:
            print("** class name missing **")
        elif _input[0] not in HBNBCommand.Class:
            print("** class doesn't exist **")
        else:
            new_instance = eval(_input[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of
        an instance based on class name and id
        """
        _input = arg.split()
        obj_dict = storage.all()

        if len(_input) == 0:
            print("** class name missing **")
        elif _input[0] not in HBNBCommand.Class:
            print("** class doesn't exist **")
        elif len(_input) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(_input[0], _input[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(_input[0], _input[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        _input = arg.split()

        if len(_input) == 0:
            print("** class name missing **")
        elif _input[0] not in HBNBCommand.Class:
            print("** class doesn't exist **")
        elif len(_input) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(_input[0], _input[1])
            obj_dict = storage.all()
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints string representations of instances
        based on class name or all instances.
        """
        _input = arg.split()
        obj_dict = storage.all()

        if len(_input) > 0 and _input[0] not in HBNBCommand.Class:
            print("** class doesn't exist **")
        else:
            result = []
            for key, value in obj_dict.items():
                if len(_input) == 0 or value.__class__.__name__ == _input[0]:
                    result.append(str(value))
            print(result)

    def do_update(self, arg):
        """
        Updates an instance based on class name
        and ID by adding or updating attribute.
        """
        _input = arg.split()
        obj_dict = storage.all()

        if len(_input) == 0:
            print("** class name missing **")
            return False
        if _input[0] not in HBNBCommand.Class:
            print("** class doesn't exist **")
            return False
        if len(_input) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(_input[0], _input[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(_input) == 2:
            print("** attribute name missing **")
            return False
        if len(_input) == 3:
            try:
                type(eval(_input[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(_input) == 4:
            obj = obj_dict["{}.{}".format(_input[0], _input[1])]
            if _input[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[_input[2]])
                obj.__dict__[_input[2]] = valtype(_input[3])
            else:
                obj.__dict__[_input[2]] = _input[3]
        elif type(eval(_input[2])) == dict:
            obj = obj_dict["{}.{}".format(_input[0], _input[1])]
            for k, v in eval(_input[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
