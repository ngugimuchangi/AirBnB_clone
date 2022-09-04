#!/usr/bin/python3
""" City class test module
"""
import unittest
from datetime import datetime
from json import dumps
from models import storage
from models.city import City
from models.state import State
from os import path, remove
import pycodestyle
from uuid import uuid4


class TestCity(unittest.TestCase):
    """ City class test cases
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
        city = City()
        city_2 = City()

        self.assertNotEqual(city.id, city_2.id)

        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

        self.assertTrue(type(city) is City)
        self.assertTrue('id' in city.__dict__)
        self.assertTrue('created_at' in city.__dict__)
        self.assertTrue('updated_at' in city.__dict__)
        self.assertFalse('state_id' in city.__dict__)
        self.assertFalse('name' in city.__dict__)

    def test_args(self):
        """ Test instatiation using args
        """
        my_id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        city = City(my_id, created_at, updated_at)
        self.assertNotEqual(city.id, my_id)
        self.assertNotEqual(city.created_at, created_at)
        self.assertNotEqual(city.updated_at, updated_at)

    def test_kwargs(self):
        """ Test instantiation using args
        """
        state = State()
        kwargs_0 = {'my_id': str(uuid4())}
        kwargs_1 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat()}
        kwargs_2 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat()}
        kwargs_3 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'state_id': state.id}
        kwargs_4 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'state_id': state.id,
                    'name': 'Nairobi'}
        kwargs_5 = {'my_id': str(uuid4()), 'created_at': datetime.now()}
        kwargs_6 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now()}

        city = City(**kwargs_0)
        self.assertTrue(hasattr(city, 'my_id'))
        self.assertFalse(hasattr(city, 'created_at'))
        self.assertFalse(hasattr(city, 'updated_at'))

        city = City(**kwargs_1)
        self.assertTrue(hasattr(city, 'my_id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertFalse(hasattr(city, 'updated_at'))

        city = City(**kwargs_2)
        self.assertTrue(hasattr(city, 'my_id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))

        city = City(**kwargs_3)
        self.assertTrue(hasattr(city, 'my_id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue('state_id' in city.__dict__)

        city = City(**kwargs_4)
        self.assertTrue(hasattr(city, 'my_id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue('state_id' in city.__dict__)
        self.assertTrue('name' in city.__dict__)

        with self.assertRaises(TypeError):
            city = City(**kwargs_5)

        with self.assertRaises(TypeError):
            city = City(**kwargs_6)

    def test_attribute_addition(self):
        """ Test the addition of new attributes
            after instatiation
        """
        state = State()
        city = City()
        city.state_id = state.id
        city.name = "Nairobi"
        self.assertTrue('state_id' in city.__dict__)
        self.assertTrue('name' in city.__dict__)
        self.assertEqual(city.state_id, state.id)
        self.assertEqual(city.name, "Nairobi")

        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def test_attributes_types(self):
        """ Test default attributes types
        """
        city = City()
        self.assertTrue(type(city.id) is str)
        self.assertTrue(type(city.created_at) is datetime)
        self.assertTrue(type(city.updated_at) is datetime)

    def test_str(self):
        """ Test string magic method
        """
        state = State()
        city = City()
        city_str = city.__str__()
        self.assertTrue(type(city_str) is str)
        self.assertEqual(str(city), city_str)

        city.state_id = state.id
        city.name = "Nairobi"
        city_str = city.__str__()
        self.assertEqual(str(city), city_str)

    def test_to_dict(self):
        """ Test to_dict method
        """
        state = State()
        city = City()
        city_dict = city.to_dict()

        self.assertNotEqual(city_dict, city.__dict__)
        self.assertTrue("__class__" in city_dict)
        self.assertEqual(city_dict["__class__"], "City")
        self.assertTrue(type(city_dict["created_at"]) is str)
        self.assertTrue(type(city_dict["updated_at"]) is str)

        city.state_id = state.id
        city.name = 'Nairobi'
        city_dict = city.to_dict()
        self.assertTrue('state_id' in city_dict)
        self.assertTrue('name' in city_dict)

    def test_save(self):
        """ Test save method
        """
        city = City()
        time_1 = city.updated_at
        city.save()
        time_2 = city.updated_at
        self.assertNotEqual(time_1, time_2)

        my_json = dumps(city.to_dict())
        with open(storage._FileStorage__file_path, "r", encoding="UTF8") as f:
            read = f.read()
        self.assertTrue(my_json in read)

    def test_create(self):
        """ Test in new object is saved to list of object
        """
        city = City()
        key = ".".join([city.__class__.__name__, city.id])
        self.assertTrue(storage._FileStorage__objects[key] is city)


if __name__ == "__main__":
    unittest.main()
