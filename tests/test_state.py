#!/usr/bin/python3
""" State class test module
"""
import unittest
from datetime import datetime
from json import dumps
from models import storage
from models.state import State
from os import path, remove
import pycodestyle
from uuid import uuid4


class TestState(unittest.TestCase):
    """ State class test cases
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
        state = State()
        state_2 = State()

        self.assertNotEqual(state.id, state_2.id)

        self.assertTrue(hasattr(state, "name"))

        self.assertTrue(type(state) is State)
        self.assertTrue('id' in state.__dict__)
        self.assertTrue('created_at' in state.__dict__)
        self.assertTrue('updated_at' in state.__dict__)
        self.assertFalse('name' in state.__dict__)

    def test_args(self):
        """ Test instatiation using args
        """
        my_id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        state = State(my_id, created_at, updated_at, "Nairobi")
        self.assertNotEqual(state.id, my_id)
        self.assertNotEqual(state.created_at, created_at)
        self.assertNotEqual(state.updated_at, updated_at)

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
                    datetime.now().isoformat(), 'name': 'Nairobi'}
        kwargs_4 = {'my_id': str(uuid4()), 'created_at': datetime.now()}
        kwargs_5 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now()}

        state = State(**kwargs_0)
        self.assertTrue(hasattr(state, 'my_id'))
        self.assertFalse(hasattr(state, 'created_at'))
        self.assertFalse(hasattr(state, 'updated_at'))

        state = State(**kwargs_1)
        self.assertTrue(hasattr(state, 'my_id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertFalse(hasattr(state, 'updated_at'))

        state = State(**kwargs_2)
        self.assertTrue(hasattr(state, 'my_id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))

        state = State(**kwargs_3)
        self.assertTrue(hasattr(state, 'my_id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue('name' in state.__dict__)

        with self.assertRaises(TypeError):
            state = State(**kwargs_4)

        with self.assertRaises(TypeError):
            state = State(**kwargs_5)

    def test_attribute_addition(self):
        """ Test the addition of new attributes
            after instatiation
        """
        state = State()
        state.name = "Nairobi"
        self.assertTrue('name' in state.__dict__)
        self.assertEqual(state.name, "Nairobi")

        self.assertEqual(State.name, "")

    def test_attributes_types(self):
        """ Test default attributes types
        """
        state = State()
        self.assertTrue(type(state.id) is str)
        self.assertTrue(type(state.created_at) is datetime)
        self.assertTrue(type(state.updated_at) is datetime)

    def test_str(self):
        """ Test string magic method
        """
        state = State()
        state_str = state.__str__()
        self.assertTrue(type(state_str) is str)
        self.assertEqual(str(state), state_str)

        state.name = "Nairobi"
        state_str = state.__str__()
        self.assertEqual(str(state), state_str)

    def test_to_dict(self):
        """ Test to_dict method
        """
        state = State()
        state_dict = state.to_dict()

        self.assertNotEqual(state_dict, state.__dict__)
        self.assertTrue("__class__" in state_dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertTrue(type(state_dict["created_at"]) is str)
        self.assertTrue(type(state_dict["updated_at"]) is str)

        state.name = 'Nairobi'
        state_dict = state.to_dict()
        self.assertTrue('name' in state_dict)

    def test_save(self):
        """ Test save method
        """
        state = State()
        time_1 = state.updated_at
        state.save()
        time_2 = state.updated_at
        self.assertNotEqual(time_1, time_2)

        my_json = dumps(state.to_dict())
        with open(storage._FileStorage__file_path, "r", encoding="UTF8") as f:
            read = f.read()
        self.assertTrue(my_json in read)

    def test_create(self):
        """ Test in new object is saved to list of object
        """
        state = State()
        key = ".".join([state.__class__.__name__, state.id])
        self.assertTrue(storage._FileStorage__objects[key] is state)


if __name__ == "__main__":
    unittest.main()
