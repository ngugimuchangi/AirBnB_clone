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
                obj (instance of BaseModel or its subclasses)
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
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.user import User

        classes = {'Amenity': Amenity, 'BaseModel': BaseModel, 'City': City,
                   'Place': Place, 'State': State, 'Review': Review,
                   'User': User}
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF8") as f:
                my_objects = load(f)
            for key in my_objects.keys():
                my_key = key.split('.')[0]
                FileStorage.__objects[key] = classes[my_key](**my_objects[key])
