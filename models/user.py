#!/usr/bin/python3
"""
A class that inherits form BaseModel
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    A User inherits from BaseModel

    Attributes
    ----------
    email: string-empty string
    password: string-empty string
    first_name: string-empty string
    last_name: string-empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
