#!/usr/bin/python3
"""Review"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Attributes
    ---------
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = Place.id
    user_id = User.id
    text = ""