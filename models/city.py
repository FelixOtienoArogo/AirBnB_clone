#!/usr/bin/python3
"""This is the city"""


from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """
    Attributes
    ----------
    state_id:string-empty string, is the State.id
    name: string-empty string
    """
    state_id = ""
    name = ""
