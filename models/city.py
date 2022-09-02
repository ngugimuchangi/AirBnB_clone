#!/usr/bin/python3
""" City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class: a subclass of BaseModel
        Public class attributes:
            state.id (str): State's id
            name (str): City's name
    """
    state_id = ""
    name = ""
