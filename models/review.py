#!/usr/bin/python3
""" Review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class: a subclass of BaseModel
        Public class attributes:
            place (str): Place being reviewed
            user_id (str): User's identification
            text (str): Review
    """
    place_id = ""
    user_id = ""
    text = ""
