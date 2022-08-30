#!/usr/bin/python3
""" File Storage Module
"""
from json import dump, load
from os import path


class FileStorage():
    """ File Storage Class
        Private class attributes:
            __file_path: path to storage file engine
            __objects: dictionary of existing objects with the following
                      key/value pair - '<class name>.id': obj.__dict__
        Public instance methods:
            all: returns a dictionary of all objects created i.e __objects
            new: adds a new object to the dictionary __objects
            save: save objects to a json file
            reload: reloads objects from a json file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Dictionary method
            Args: none
            Return: class attribute __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Method that adds new instance to __objects
            Args:
                obj (instance of BaseModel)
            Return: nothing
        """
        key = ".".join([obj.__class__.__name__, obj.id])
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialization method that saves instances to json file
            Args: none
            Return: nothing
        """
        json_dict = {i: FileStorage.__objects[i].to_dict()
                     for i in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w", encoding="UTF8") as f:
            dump(json_dict, f)

    def reload(self):
        """ Deserialization method that reloads instances from json file
            Args: none
            Return: nothing
        """
        from models.base_model import BaseModel

        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF8") as f:
                my_objects = load(f)
            FileStorage.__objects = {i: BaseModel(my_objects[i])
                                     for i in my_objects.keys()}
