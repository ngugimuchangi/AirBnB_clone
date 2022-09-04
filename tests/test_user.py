#!/usr/binn/python3
""" User class test module
"""
import unittest
from datetime import datetime
from json import dumps
from models import storage
from models.user import User
from os import path, remove
import pycodestyle
from uuid import uuid4


class TestUser(unittest.TestCase):
    """ User class test cases
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
        """ Test instantiation of User objects
        """
        user = User()
        user_2 = User()

        self.assertNotEqual(user.id, user_2.id)

        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

        self.assertTrue(type(user) is User)
        self.assertTrue('id' in user.__dict__)
        self.assertTrue('created_at' in user.__dict__)
        self.assertTrue('updated_at' in user.__dict__)
        self.assertFalse('email' in user.__dict__)
        self.assertFalse('password' in user.__dict__)
        self.assertFalse('first_name' in user.__dict__)
        self.assertFalse('last_name' in user.__dict__)

    def test_args(self):
        """ Test instatiation using args
        """
        my_id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        user = User(my_id, created_at, updated_at)
        self.assertNotEqual(user.id, my_id)
        self.assertNotEqual(user.created_at, created_at)
        self.assertNotEqual(user.updated_at, updated_at)

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
                    datetime.now().isoformat(), 'email':
                    'airbnb@gmail.com'}
        kwargs_4 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'email':
                    'airbnb@gmail.com', 'password': 'root'}
        kwargs_5 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'email':
                    'airbnb@gmail.com', 'password': 'root',
                    'first_name': 'Home'}
        kwargs_6 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'email': 'airbnb@gmail.com',
                    'password': 'root', 'first_name': 'Home', 'last_name':
                    'Owner'}
        kwargs_7 = {'my_id': str(uuid4()), 'created_at': datetime.now()}
        kwargs_8 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at': datetime.now()}

        user = User(**kwargs_0)
        self.assertTrue(hasattr(user, 'my_id'))
        self.assertFalse(hasattr(user, 'created_at'))
        self.assertFalse(hasattr(user, 'updated_at'))

        user = User(**kwargs_1)
        self.assertTrue(hasattr(user, 'my_id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertFalse(hasattr(user, 'updated_at'))

        user = User(**kwargs_2)
        self.assertTrue(hasattr(user, 'my_id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))

        user = User(**kwargs_3)
        self.assertTrue(hasattr(user, 'my_id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue('email' in user.__dict__)

        user = User(**kwargs_4)
        self.assertTrue(hasattr(user, 'my_id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue('email' in user.__dict__)
        self.assertTrue('password' in user.__dict__)

        user = User(**kwargs_5)
        self.assertTrue(hasattr(user, 'my_id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue('email' in user.__dict__)
        self.assertTrue('password' in user.__dict__)
        self.assertTrue('first_name' in user.__dict__)

        user = User(**kwargs_6)
        self.assertTrue(hasattr(user, 'my_id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue('email' in user.__dict__)
        self.assertTrue('password' in user.__dict__)
        self.assertTrue('first_name' in user.__dict__)
        self.assertTrue('last_name' in user.__dict__)

        with self.assertRaises(TypeError):
            a = User(**kwargs_7)

        with self.assertRaises(TypeError):
            a = User(**kwargs_8)

    def test_attribute_addition(self):
        """ Test the addition of new attributes
            after instatiation
        """
        user = User()
        user_2 = User()

        user.email = 'airbnb@gmail.com'
        user.password = '1234'
        user.first_name = 'Home'
        user.last_name = 'Owner'
        self.assertTrue('email' in user.__dict__)
        self.assertTrue('password' in user.__dict__)
        self.assertTrue('first_name' in user.__dict__)
        self.assertTrue('last_name' in user.__dict__)

        user_2.email = 'email@email.com'
        user_2.password = '5678'
        user_2.first_name = 'Amazing'
        user_2.last_name = 'Realtor'
        self.assertNotEqual(user.email, user_2.email)
        self.assertNotEqual(user.password, user_2.password)
        self.assertNotEqual(user.first_name, user_2.first_name)
        self.assertNotEqual(user.last_name, user_2.last_name)

        self.assertEqual(User.email,  "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.password, "")

    def test_attributes_types(self):
        """ Test default attributes types
        """
        user = User()
        self.assertTrue(type(user.id) is str)
        self.assertTrue(type(user.created_at) is datetime)
        self.assertTrue(type(user.updated_at) is datetime)

    def test_str(self):
        """ Test string magic method
        """
        user = User()
        user_str = user.__str__()
        self.assertTrue(type(user_str) is str)
        self.assertEqual(str(user), user_str)

        user.email = 'airbnb@gmail.com'
        user.password = 'root'
        user.first_name = 'Home'
        user.last_name = 'Owner'
        user_str = user.__str__()
        self.assertEqual(str(user), user_str)

    def test_to_dict(self):
        """ Test to_dict method
        """
        user = User()
        user_dict = user.to_dict()

        self.assertNotEqual(user_dict, user.__dict__)
        self.assertTrue("__class__" in user_dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertTrue(type(user_dict["created_at"]) is str)
        self.assertTrue(type(user_dict["updated_at"]) is str)

        user.email = 'airbnb@gmail.com'
        user.password = 'root'
        user.first_name = 'Home'
        user.last_name = 'Owner'
        user_dict = user.to_dict()

        self.assertTrue('email' in user_dict)
        self.assertTrue('password' in user_dict)
        self.assertTrue('first_name' in user_dict)
        self.assertTrue('last_name' in user_dict)

    def test_save(self):
        """ Test save method
        """
        user = User()
        time_1 = user.updated_at
        user.save()
        time_2 = user.updated_at
        self.assertNotEqual(time_1, time_2)

        my_json = dumps(user.to_dict())
        with open(storage._FileStorage__file_path, "r", encoding="UTF8") as f:
            read = f.read()
        self.assertTrue(my_json in read)

    def test_create(self):
        """ Test in new object is saved to list of object
        """
        user = User()
        self.assertEqual(user.__class__.__name__, 'User')

        key = ".".join([user.__class__.__name__, user.id])
        self.assertTrue(storage._FileStorage__objects[key] is user)


if __name__ == "__main__":
    unittest.main()
