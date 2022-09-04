#!/usr/bin/python3
""" Amenity class test module
"""
import unittest
from datetime import datetime
from json import dumps
from models import storage
from models.amenity import Amenity
from os import path, remove
import pycodestyle
from uuid import uuid4


class TestAmenity(unittest.TestCase):
    """ Amenity class test cases
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
        amenity = Amenity()
        amenity_2 = Amenity()

        self.assertNotEqual(amenity.id, amenity_2.id)

        self.assertTrue(hasattr(amenity, "name"))

        self.assertTrue(type(amenity) is Amenity)
        self.assertTrue('id' in amenity.__dict__)
        self.assertTrue('created_at' in amenity.__dict__)
        self.assertTrue('updated_at' in amenity.__dict__)
        self.assertFalse('name' in amenity.__dict__)

    def test_args(self):
        """ Test instatiation using args
        """
        my_id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        amenity = Amenity(my_id, created_at, updated_at, "Swimming Pool")
        self.assertNotEqual(amenity.id, my_id)
        self.assertNotEqual(amenity.created_at, created_at)
        self.assertNotEqual(amenity.updated_at, updated_at)

    def test_kwargs(self):
        """ Test instantiation using args
        """
        state = Amenity()
        kwargs_0 = {'my_id': str(uuid4())}
        kwargs_1 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat()}
        kwargs_2 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat()}
        kwargs_3 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'name': 'Swimming Pool'}
        kwargs_4 = {'my_id': str(uuid4()), 'created_at': datetime.now()}
        kwargs_5 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now()}

        amenity = Amenity(**kwargs_0)
        self.assertTrue(hasattr(amenity, 'my_id'))
        self.assertFalse(hasattr(amenity, 'created_at'))
        self.assertFalse(hasattr(amenity, 'updated_at'))

        amenity = Amenity(**kwargs_1)
        self.assertTrue(hasattr(amenity, 'my_id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertFalse(hasattr(amenity, 'updated_at'))

        amenity = Amenity(**kwargs_2)
        self.assertTrue(hasattr(amenity, 'my_id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))

        amenity = Amenity(**kwargs_3)
        self.assertTrue(hasattr(amenity, 'my_id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue('name' in amenity.__dict__)

        with self.assertRaises(TypeError):
            amenity = Amenity(**kwargs_4)

        with self.assertRaises(TypeError):
            amenity = Amenity(**kwargs_5)

    def test_attribute_addition(self):
        """ Test the addition of new attributes
            after instatiation
        """
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertTrue('name' in amenity.__dict__)
        self.assertEqual(amenity.name, "Swimming Pool")

        self.assertEqual(Amenity.name, "")

    def test_attributes_types(self):
        """ Test default attributes types
        """
        amenity = Amenity()
        self.assertTrue(type(amenity.id) is str)
        self.assertTrue(type(amenity.created_at) is datetime)
        self.assertTrue(type(amenity.updated_at) is datetime)

    def test_str(self):
        """ Test string magic method
        """
        amenity = Amenity()
        amenity_str = amenity.__str__()
        self.assertTrue(type(amenity_str) is str)
        self.assertEqual(str(amenity), amenity_str)

        amenity.name = "Swimming Pool"
        amenity_str = amenity.__str__()
        self.assertEqual(str(amenity), amenity_str)

    def test_to_dict(self):
        """ Test to_dict method
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()

        self.assertNotEqual(amenity_dict, amenity.__dict__)
        self.assertTrue("__class__" in amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertTrue(type(amenity_dict["created_at"]) is str)
        self.assertTrue(type(amenity_dict["updated_at"]) is str)

        amenity.name = 'Swimming Pool'
        amenity_dict = amenity.to_dict()
        self.assertTrue('name' in amenity_dict)

    def test_save(self):
        """ Test save method
        """
        amenity = Amenity()
        time_1 = amenity.updated_at
        amenity.save()
        time_2 = amenity.updated_at
        self.assertNotEqual(time_1, time_2)

        my_json = dumps(amenity.to_dict())
        with open(storage._FileStorage__file_path, "r", encoding="UTF8") as f:
            read = f.read()
        self.assertTrue(my_json in read)

    def test_create(self):
        """ Test in new object is saved to list of object
        """
        amenity = Amenity()
        key = ".".join([amenity.__class__.__name__, amenity.id])
        self.assertTrue(storage._FileStorage__objects[key] is amenity)


if __name__ == "__main__":
    unittest.main()
