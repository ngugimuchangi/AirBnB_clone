#!/usr/bin/python3
""" State module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State class: a subclass of BaseModel
        Public class attributes:
            name (str): State's name
    """
    name = ""
