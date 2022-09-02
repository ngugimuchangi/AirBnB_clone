#!/urs/bin/python3
""" User module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class
        Public class attributes:
            email
            password
            first_name
            last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
