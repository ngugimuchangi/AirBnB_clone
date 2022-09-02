#!/usr/bin/python3
""" Amenity module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class: a subclass of BaseModel
        Public class attributes:
            name (str): Amenity's name
    """
    name = ""
