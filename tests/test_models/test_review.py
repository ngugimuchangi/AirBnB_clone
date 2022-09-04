#!/usr/bin/python3
""" Review class test module
"""
import unittest
from datetime import datetime
from json import dumps
from models import storage
from models.place import Place
from models.review import Review
from models.user import User
from os import path, remove
import pycodestyle
from uuid import uuid4


class TestReview(unittest.TestCase):
    """ Review class test cases
    """

    @classmethod
    def tearDownClass(cls):
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
        review = Review()
        review_2 = Review()

        self.assertNotEqual(review.id, review_2.id)

        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

        self.assertTrue(type(review) is Review)
        self.assertTrue('id' in review.__dict__)
        self.assertTrue('created_at' in review.__dict__)
        self.assertTrue('updated_at' in review.__dict__)
        self.assertFalse('place_id' in review.__dict__)
        self.assertFalse('user_id' in review.__dict__)
        self.assertFalse('text' in review.__dict__)

    def test_args(self):
        """ Test instatiation using args
        """
        my_id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        review = Review(my_id, created_at, updated_at, str(uuid4()))
        review = Review(my_id, created_at, updated_at,
                        str(uuid4()), str(uuid4()))
        review = Review(my_id, created_at, updated_at, str(uuid4()),
                        str(uuid4()), "Best staycation spot ever")
        self.assertNotEqual(review.id, my_id)
        self.assertNotEqual(review.created_at, created_at)
        self.assertNotEqual(review.updated_at, updated_at)

    def test_kwargs(self):
        """ Test instantiation using args
        """
        user = User()
        place = Place()
        kwargs_0 = {'my_id': str(uuid4())}
        kwargs_1 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat()}
        kwargs_2 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat()}
        kwargs_3 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'place_id': place.id}
        kwargs_4 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'place_id': place.id,
                    'user_id': 'user.id'}
        kwargs_5 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'place_id': place.id,
                    'user_id': 'user.id', 'text': "Nice place"}
        kwargs_6 = {'my_id': str(uuid4()), 'created_at': datetime.now()}
        kwargs_7 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at': datetime.now()}

        review = Review(**kwargs_0)
        self.assertTrue(hasattr(review, 'my_id'))
        self.assertFalse(hasattr(review, 'created_at'))
        self.assertFalse(hasattr(review, 'updated_at'))

        review = Review(**kwargs_1)
        self.assertTrue(hasattr(review, 'my_id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertFalse(hasattr(review, 'updated_at'))

        review = Review(**kwargs_2)
        self.assertTrue(hasattr(review, 'my_id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))

        review = Review(**kwargs_3)
        self.assertTrue(hasattr(review, 'my_id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue('place_id' in review.__dict__)

        review = Review(**kwargs_4)
        self.assertTrue(hasattr(review, 'my_id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue('place_id' in review.__dict__)
        self.assertTrue('user_id' in review.__dict__)

        review = Review(**kwargs_5)
        self.assertTrue(hasattr(review, 'my_id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue('place_id' in review.__dict__)
        self.assertTrue('user_id' in review.__dict__)
        self.assertTrue('text' in review.__dict__)

        with self.assertRaises(TypeError):
            review = Review(**kwargs_6)

        with self.assertRaises(TypeError):
            review = Review(**kwargs_7)

    def test_attribute_addition(self):
        """ Test the addition of new attributes
            after instatiation
        """
        place = Place()
        user = User()
        review = Review()
        review.place_id = place.id
        review.user_id = user.id
        review.text = "Bad service"
        self.assertTrue('place_id' in review.__dict__)
        self.assertTrue('user_id' in review.__dict__)
        self.assertTrue('text' in review.__dict__)
        self.assertEqual(review.place_id, place.id)
        self.assertEqual(review.user_id, user.id)
        self.assertEqual(review.text, "Bad service")

        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

    def test_attributes_types(self):
        """ Test default attributes types
        """
        review = Review()
        self.assertTrue(type(review.id) is str)
        self.assertTrue(type(review.created_at) is datetime)
        self.assertTrue(type(review.updated_at) is datetime)

    def test_str(self):
        """ Test string magic method
        """
        place = Place()
        user = User()
        review = Review()
        review_str = review.__str__()
        self.assertTrue(type(review_str) is str)
        self.assertEqual(str(review), review_str)

        review.place_id = place.id
        review.user_id = user.id
        review.text = "Best vacation spot"
        review_str = review.__str__()
        self.assertEqual(str(review), review_str)

    def test_to_dict(self):
        """ Test to_dict method
        """
        place = Place()
        user = User()
        review = Review()
        review_dict = review.to_dict()

        self.assertNotEqual(review_dict, review.__dict__)
        self.assertTrue("__class__" in review_dict)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertTrue(type(review_dict["created_at"]) is str)
        self.assertTrue(type(review_dict["updated_at"]) is str)

        review.place_id = place.id
        review.user_id = user.id
        review.text = "Has nice views"
        review_dict = review.to_dict()
        self.assertTrue('place_id' in review_dict)
        self.assertTrue('user_id' in review_dict)
        self.assertTrue('text' in review_dict)

    def test_save(self):
        """ Test save method
        """
        review = Review()
        time_1 = review.updated_at
        review.save()
        time_2 = review.updated_at
        self.assertNotEqual(time_1, time_2)

        my_json = dumps(review.to_dict())
        with open(storage._FileStorage__file_path, "r", encoding="UTF8") as f:
            read = f.read()
        self.assertTrue(my_json in read)

    def test_create(self):
        """ Test in new object is saved to list of object
        """
        review = Review()
        key = ".".join([review.__class__.__name__, review.id])
        self.assertTrue(storage._FileStorage__objects[key] is review)


if __name__ == "__main__":
    unittest.main()
