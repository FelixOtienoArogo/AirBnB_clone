#!/usr/bin/python3
"""
This is the entry point of the command interpreter
"""

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import Amenity
import re
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Class is the entry point to the command
    interpreter
    """
    prompt = '(hbnb)'
    allowed_classes = ['BaseModel', 'User', 'State',
                       'City', 'Amenity', 'Place', 'Review']

    def do_quit(self, arg):
        """Quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit program"""
        return True

    def emptyline(self):
        """An empty line + ENTER won't execute anything"""
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        and print the id.
        """
        command = self.parseline(arg)[0]
        if command is None:
            print("** class name missing **")
        elif command not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            new = eval(command)()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        class_name = self.parseline(arg)[0]
        obj_id = self.parseline(arg)[1]
        if class_name is None:
            print("** class name missing **")
        elif class_name not in self.allowed_classes:
            print("** class doesn't exist **")
        elif obj_id == '':
            print("** instance id missing **")
        else:
            obj_data = models.storage.all().get(class_name + '.' + obj_id)
            if obj_data is None:
                print('** no instance found **')
            else:
                print(obj_data)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        class_name = self.parseline(arg)[0]
        obj_id = self.parseline(arg)[1]

        if class_name is None:
            print("** class name missing **")
        elif class_name not in self.allowed_classes:
            print("** class doesn't exist **")
        elif obj_id == '':
            print("** instance id missing **")
        else:
            key = class_name + '.' + obj_id
            obj_data = models.storage.all().get(key)
            if obj_data is None:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        class_name = self.parseline(arg)[0]
        objs = models.storage.all()
        if class_name is None:
            print([str(objs[obj]) for obj in objs])
        elif class_name in self.allowed_classes:
            keys = objs.keys()
            print([str(objs[key]) for key in keys
                   if key.startswith(class_name)])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = shlex.split(arg)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            if args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                try:
                    setattr(inst_data, args[2], args[3])
                    setattr(inst_data, 'updated_at', datetime.now())
                except AttributeError:
                    pass
                models.storage.save()

    def analyze_parameter_value(self, value):
        """
        Checks a parameter value for an update and
        analyse if is a string that needs conversion
        to a float or integer
        """
        if value.isdigit():
            return int(value)
        elif value.replace('.', '', 1).isdigit():
            return float(value)

        return value


if __name__ == '__main__':
    HBNBCommand().cmdloop()
