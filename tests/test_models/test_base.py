#!/usr/bin/python3
""" Base class test module
"""
import unittest
from datetime import datetime
from json import dumps
from models import storage
from models.base_model import BaseModel
from os import path, remove
import pycodestyle
from uuid import uuid4


class TestBaseModel(unittest.TestCase):
    """ Base class test cases
    """

    @classmethod
    def tearDownClass(self):
        """ Clean up actios at the end of test class
        """
        if path.exists(storage._FileStorage__file_path):
            remove(storage._FileStorage__file_path)

    def test_pycodestyle(self):
        """ Test if module follows pycodestyle
        """

    def test_default_constructor(self):
        """ Test instantiation of BaseModel objects
        """
        base = BaseModel()
        base_2 = BaseModel()
        self.assertNotEqual(base.id, base_2.id)
        self.assertTrue(type(base) is BaseModel)
        self.assertTrue('id' in base.__dict__)
        self.assertTrue('created_at' in base.__dict__)
        self.assertTrue('updated_at' in base.__dict__)

    def test_args(self):
        """ Test instatiation using args
        """
        my_id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        base = BaseModel(my_id, created_at, updated_at)
        self.assertNotEqual(base.id, my_id)
        self.assertNotEqual(base.created_at, created_at)
        self.assertNotEqual(base.updated_at, updated_at)

    def test_kwargs(self):
        """ Test instantiation using args
        """
        kwargs_0 = {'my_id': str(uuid4())}
        kwargs_1 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat()}
        kwargs_2 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat()}
        kwargs_3 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'name': "Base Model 1"}
        kwargs_4 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now()}
        kwargs_5 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now()}

        base = BaseModel(**kwargs_0)
        self.assertTrue(hasattr(base, 'my_id'))
        self.assertFalse(hasattr(base, 'created_at'))
        self.assertFalse(hasattr(base, 'updated_at'))

        base = BaseModel(**kwargs_1)
        self.assertTrue(hasattr(base, 'my_id'))
        self.assertTrue(hasattr(base, 'created_at'))
        self.assertFalse(hasattr(base, 'updated_at'))

        base = BaseModel(**kwargs_2)
        self.assertTrue(hasattr(base, 'my_id'))
        self.assertTrue(hasattr(base, 'created_at'))
        self.assertTrue(hasattr(base, 'updated_at'))

        base = BaseModel(**kwargs_3)
        self.assertTrue(hasattr(base, 'my_id'))
        self.assertTrue(hasattr(base, 'created_at'))
        self.assertTrue(hasattr(base, 'updated_at'))
        self.assertTrue(hasattr(base, 'name'))

        with self.assertRaises(TypeError):
            base = BaseModel(**kwargs_4)

        with self.assertRaises(TypeError):
            base = BaseModel(**kwargs_5)

    def test_attribute_addition(self):
        """ Test the addition of new attributes
            after instatiation
        """
        base = BaseModel()
        base.f_name = 'First'
        base.l_name = 'Second'
        self.assertTrue(hasattr(base, 'f_name'))
        self.assertTrue(hasattr(base, 'l_name'))
        self.assertEqual(base.f_name, 'First')
        self.assertEqual(base.l_name, 'Second')

    def test_attributes_types(self):
        """ Test default attributes types
        """
        base = BaseModel()
        self.assertTrue(type(base.id) is str)
        self.assertTrue(type(base.created_at) is datetime)
        self.assertTrue(type(base.updated_at) is datetime)

    def test_str(self):
        """ Test string magic method
        """
        base = BaseModel()
        base_str = base.__str__()
        self.assertTrue(type(base_str) is str)
        self.assertEqual(str(base), base_str)

        base.f_name = 'Son of'
        base.l_name = 'Kyrpton'
        base_str = base.__str__()
        self.assertEqual(str(base), base_str)

    def test_to_dict(self):
        """ Test to_dict method
        """
        base = BaseModel()
        base_dict = base.to_dict()

        self.assertNotEqual(base_dict, base.__dict__)
        self.assertTrue("__class__" in base_dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertTrue(type(base_dict["created_at"]) is str)
        self.assertTrue(type(base_dict["updated_at"]) is str)

        base.name = 'Base Model 1'
        base_dict = base.to_dict()
        self.assertTrue('name' in base_dict)

    def test_save(self):
        """ Test save method
        """
        base = BaseModel()
        time_1 = base.updated_at
        base.save()
        time_2 = base.updated_at
        self.assertNotEqual(time_1, time_2)

        my_json = dumps(base.to_dict())
        with open(storage._FileStorage__file_path, "r", encoding="UTF8") as f:
            read = f.read()
        self.assertTrue(my_json in read)

    def test_create(self):
        """ Test in new object is saved to list of object
        """
        base = BaseModel()
        key = ".".join([base.__class__.__name__, base.id])
        self.assertTrue(storage._FileStorage__objects[key] is base)


if __name__ == "__main__":
    unittest.main()
