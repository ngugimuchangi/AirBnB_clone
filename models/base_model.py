#!/usr/bin/python3
""" Airbnb Base Model
"""
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """ Base Model
        Public instance attributes:
            id (str): universally unique identifier (UUID) of the object
            created_at (datetime): when the object was created
            update_at (datetime): when the object was last updated

        Public instance methods:
            __init__: instantiation method
            __str__: string representation method
            save: update method
            to_dict: dictionary conversion method
    """

    def __init__(self, *args, **kwargs):
        """ Instantiation method
            Args: Uses keyword arguments if provided
                kwargs: keyword arguments
            Return: nothing
        """
        if type(kwargs) is dict and "id" in kwargs:
            self.id = kwargs["id"]
        else:
            self.id = str(uuid4())
        if type(kwargs) is dict and "created_at" in kwargs:
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
        else:
            self.created_at = datetime.now()
        if type(kwargs) is dict and "updated_at" in kwargs:
            self.created_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.updated_at = datetime.now()

    def __str__(self):
        """ String representation method
            Args: none
            Return: string representation of the
                    BaseModel instance
        """
        my_str = "[{}] ({}) ({})".format(self.__class__.__name__,
                                         self.id, self.__dict__)
        return my_str

    def save(self):
        """ Method to update updated_at attribute
            Args: none
            Return: nothing
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Dictionary representation method
            Args: none
            Return: dictionary representation of BaseModel
                    instance
        """
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict
