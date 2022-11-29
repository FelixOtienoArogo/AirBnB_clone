#!/usr/bin/python3
"""
This is the entry point of the command interpreter
"""

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
import re
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Class is the entry point to the command
    interpreter
    """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit program"""
        return True

    def emptyline(self):
        """An empty line + ENTER won't execute anything"""
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
