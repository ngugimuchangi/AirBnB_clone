#!/usr/binn/python3
""" User class test module
"""
import unittest
from datetime import datetime
from json import dumps
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from os import path, remove
import pycodestyle
from uuid import uuid4


class TestPlace(unittest.TestCase):
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
        place = Place()
        place_2 = Place()

        self.assertNotEqual(place.id, place_2.id)

        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

        self.assertTrue(type(place) is Place)
        self.assertTrue('id' in place.__dict__)
        self.assertTrue('created_at' in place.__dict__)
        self.assertTrue('updated_at' in place.__dict__)
        self.assertFalse('city_id' in place.__dict__)
        self.assertFalse('user_id' in place.__dict__)
        self.assertFalse('name' in place.__dict__)
        self.assertFalse('description' in place.__dict__)
        self.assertFalse('number_rooms' in place.__dict__)
        self.assertFalse('number_bathrooms' in place.__dict__)
        self.assertFalse('max_guest' in place.__dict__)
        self.assertFalse('price_by_night' in place.__dict__)
        self.assertFalse('latitude' in place.__dict__)
        self.assertFalse('longitude' in place.__dict__)
        self.assertFalse('amenity_ids' in place.__dict__)

    def test_args(self):
        """ Test instatiation using args
        """
        my_id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        city = City()
        user = User()

        place = Place(my_id)
        self.assertNotEqual(place.id, my_id)

        place = Place(my_id, created_at, updated_at)
        self.assertNotEqual(place.id, my_id)
        self.assertNotEqual(place.created_at, created_at)

        place = Place(my_id, created_at, updated_at)
        self.assertNotEqual(place.id, my_id)
        self.assertNotEqual(place.created_at, created_at)
        self.assertNotEqual(place.updated_at, updated_at)

        place = Place(my_id, created_at, updated_at, city.id)
        place = Place(my_id, created_at, updated_at, city.id, user.id)
        place = Place(my_id, created_at, updated_at, city.id, user.id,
                      "Warm weather destination")
        place = Place(my_id, created_at, updated_at, city.id, user.id,
                      "Warm weather destination", 3)
        place = Place(my_id, created_at, updated_at, city.id, user.id,
                      "Warm weather destination", 3, 4)
        place = Place(my_id, created_at, updated_at, city.id, user.id,
                      "Warm weather destination", 3, 4, 6)
        place = Place(my_id, created_at, updated_at, city.id, user.id,
                      "Warm weather destination", 3, 4, 6, 36)
        place = Place(my_id, created_at, updated_at, city.id, user.id,
                      "Warm weather destination", 3, 4, 6, 36, 14.01)
        place = Place(my_id, created_at, updated_at, city.id, user.id,
                      "Warm weather destination", 3, 4, 6, 36, 14.01, 23.51)

    def test_kwargs(self):
        """ Test instantiation using args
        """
        city = City()
        user = User()
        amenity = Amenity()
        amenity_2 = Amenity()
        kwargs_0 = {'my_id': str(uuid4())}
        kwargs_1 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat()}
        kwargs_2 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat()}
        kwargs_3 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'name':
                    'Diani Beach'}
        kwargs_4 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'name': 'Diani Beach',
                    'description': 'summer time destination'}
        kwargs_5 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'name': 'Diani Beach',
                    'description': 'summer time destination',
                    'number_rooms': 4}
        kwargs_6 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'name': 'Diani Beach',
                    'description': 'summer time destination',
                    'number_rooms': 4, 'number_bathrooms': 5}
        kwargs_7 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'name': 'Diani Beach',
                    'description': 'summer time destination',
                    'number_rooms': 4, 'number_bathrooms': 5,
                    'max_guest': 10}
        kwargs_8 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'name': 'Diani Beach',
                    'description': 'summer time destination',
                    'number_rooms': 4, 'number_bathrooms': 5,
                    'max_guest': 10, 'price_by_night': 45}
        kwargs_9 = {'my_id': str(uuid4()), 'created_at':
                    datetime.now().isoformat(), 'updated_at':
                    datetime.now().isoformat(), 'name': 'Diani Beach',
                    'description': 'summer time destination',
                    'number_rooms': 4, 'number_bathrooms': 5,
                    'max_guest': 10, 'price_by_night': 45, 'latitude': 14.01}
        kwargs_10 = {'my_id': str(uuid4()), 'created_at':
                     datetime.now().isoformat(), 'updated_at':
                     datetime.now().isoformat(), 'name': 'Diani Beach',
                     'description': 'summer time destination',
                     'number_rooms': 4, 'number_bathrooms': 5,
                     'max_guest': 10, 'price_by_night': 45, 'latitude': 14.01,
                     'longitude': 23.51}
        kwargs_10 = {'my_id': str(uuid4()), 'created_at':
                     datetime.now().isoformat(), 'updated_at':
                     datetime.now().isoformat(), 'name': 'Diani Beach',
                     'description': 'summer time destination',
                     'number_rooms': 4, 'number_bathrooms': 5,
                     'max_guest': 10, 'price_by_night': 45, 'latitude': 14.01,
                     'longitude': 23.51}
        kwargs_11 = {'my_id': str(uuid4()), 'created_at':
                     datetime.now().isoformat(), 'updated_at':
                     datetime.now().isoformat(), 'name': 'Diani Beach',
                     'description': 'summer time destination',
                     'number_rooms': 4, 'number_bathrooms': 5,
                     'max_guest': 10, 'price_by_night': 45, 'latitude': 14.01,
                     'longitude': 23.51, 'amenity_ids':
                     [amenity.id, amenity_2.id]}
        kwargs_12 = {'my_id': str(uuid4()), 'created_at': datetime.now()}
        kwargs_13 = {'my_id': str(uuid4()), 'created_at':
                     datetime.now().isoformat(), 'updated_at': datetime.now()}

        place = Place(**kwargs_0)
        self.assertTrue(hasattr(place, 'my_id'))
        self.assertFalse(hasattr(place, 'created_at'))
        self.assertFalse(hasattr(place, 'updated_at'))

        place = Place(**kwargs_1)
        self.assertTrue(hasattr(place, 'my_id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertFalse(hasattr(place, 'updated_at'))

        place = Place(**kwargs_2)
        self.assertTrue(hasattr(place, 'my_id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))

        place = Place(**kwargs_3)
        self.assertTrue(hasattr(place, 'my_id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue('name' in place.__dict__)

        place = Place(**kwargs_4)
        self.assertTrue(hasattr(place, 'my_id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue('name' in place.__dict__)
        self.assertTrue('description' in place.__dict__)

        place = Place(**kwargs_5)
        self.assertTrue(hasattr(place, 'my_id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue('name' in place.__dict__)
        self.assertTrue('description' in place.__dict__)
        self.assertTrue('number_rooms' in place.__dict__)

        place = Place(**kwargs_6)
        self.assertTrue(hasattr(place, 'my_id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue('name' in place.__dict__)
        self.assertTrue('description' in place.__dict__)
        self.assertTrue('number_rooms' in place.__dict__)
        self.assertTrue('number_bathrooms' in place.__dict__)

        place = Place(**kwargs_7)
        self.assertTrue(hasattr(place, 'my_id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue('name' in place.__dict__)
        self.assertTrue('description' in place.__dict__)
        self.assertTrue('number_rooms' in place.__dict__)
        self.assertTrue('number_bathrooms' in place.__dict__)
        self.assertTrue('max_guest' in place.__dict__)

        place = Place(**kwargs_8)
        self.assertTrue(hasattr(place, 'my_id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue('name' in place.__dict__)
        self.assertTrue('description' in place.__dict__)
        self.assertTrue('number_rooms' in place.__dict__)
        self.assertTrue('number_bathrooms' in place.__dict__)
        self.assertTrue('max_guest' in place.__dict__)
        self.assertTrue('price_by_night' in place.__dict__)

        place = Place(**kwargs_9)
        self.assertTrue(hasattr(place, 'my_id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue('name' in place.__dict__)
        self.assertTrue('description' in place.__dict__)
        self.assertTrue('number_rooms' in place.__dict__)
        self.assertTrue('number_bathrooms' in place.__dict__)
        self.assertTrue('max_guest' in place.__dict__)
        self.assertTrue('price_by_night' in place.__dict__)
        self.assertTrue('latitude' in place.__dict__)

        place = Place(**kwargs_10)
        self.assertTrue(hasattr(place, 'my_id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue('name' in place.__dict__)
        self.assertTrue('description' in place.__dict__)
        self.assertTrue('number_rooms' in place.__dict__)
        self.assertTrue('number_bathrooms' in place.__dict__)
        self.assertTrue('max_guest' in place.__dict__)
        self.assertTrue('price_by_night' in place.__dict__)
        self.assertTrue('longitude' in place.__dict__)

        place = Place(**kwargs_11)
        self.assertTrue(hasattr(place, 'my_id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue('name' in place.__dict__)
        self.assertTrue('description' in place.__dict__)
        self.assertTrue('number_rooms' in place.__dict__)
        self.assertTrue('number_bathrooms' in place.__dict__)
        self.assertTrue('max_guest' in place.__dict__)
        self.assertTrue('price_by_night' in place.__dict__)
        self.assertTrue('longitude' in place.__dict__)
        self.assertTrue('amenity_ids' in place.__dict__)

        with self.assertRaises(TypeError):
            user = User(**kwargs_12)

        with self.assertRaises(TypeError):
            user = User(**kwargs_13)

    def test_attribute_addition(self):
        """ Test the addition of new attributes
            after instatiation
        """
        city = City()
        user = User()
        amenity = Amenity()
        amenity_2 = Amenity()
        place = Place()
        place_2 = Place()

        place.city_id = city.id
        place.user_id = user.id
        place.name = 'Diani'
        place.description = 'Sandy beaches'
        place.number_rooms = 5
        place.number_bathrooms = 6
        place.max_guest = 12
        place.price_by_night = 60
        place.latitude = 4.35
        place.longitude = 13.07
        place.amenity_ids = [amenity.id, amenity_2.id]

        self.assertTrue('name' in place.__dict__)
        self.assertTrue('description' in place.__dict__)
        self.assertTrue('number_rooms' in place.__dict__)
        self.assertTrue('number_bathrooms' in place.__dict__)
        self.assertTrue('max_guest' in place.__dict__)
        self.assertTrue('price_by_night' in place.__dict__)
        self.assertTrue('latitude' in place.__dict__)
        self.assertTrue('longitude' in place.__dict__)
        self.assertTrue('amenity_ids' in place.__dict__)

        place_2.city_id = city.id
        place_2.user_id = user.id
        place_2.name = 'Naserian Palatial Homes'
        place_2.description = 'Chilled retreat'
        place_2.number_rooms = 4
        place_2.number_bathrooms = 3
        place_2.max_guest = 9
        place_2.price_by_night = 55
        place_2.latitude = 2.35
        place_2.longitude = 9.07
        place_2.amenity_ids = [amenity.id]

        self.assertTrue('name' in place.__dict__)
        self.assertTrue('description' in place.__dict__)
        self.assertTrue('number_rooms' in place.__dict__)
        self.assertTrue('number_bathrooms' in place.__dict__)
        self.assertTrue('max_guest' in place.__dict__)
        self.assertTrue('price_by_night' in place.__dict__)
        self.assertTrue('latitude' in place.__dict__)
        self.assertTrue('longitude' in place.__dict__)
        self.assertTrue('amenity_ids' in place.__dict__)

        self.assertNotEqual(place.name, place_2.name)
        self.assertNotEqual(place.description, place_2.description)
        self.assertNotEqual(place.number_rooms, place_2.number_rooms)
        self.assertNotEqual(place.number_bathrooms, place_2.number_bathrooms)
        self.assertNotEqual(place.max_guest, place_2.max_guest)
        self.assertNotEqual(place.price_by_night, place_2.price_by_night)
        self.assertNotEqual(place.latitude, place_2.latitude)
        self.assertNotEqual(place.longitude, place_2.longitude)
        self.assertNotEqual(place.amenity_ids, place_2.amenity_ids)

        self.assertEqual(Place.city_id,  "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms,  0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

    def test_attributes_types(self):
        """ Test default attributes types
        """
        city = City()
        user = User()
        amenity = Amenity()
        amenity_2 = Amenity()
        place = Place()

        place.city_id = city.id
        place.user_id = user.id
        place.name = 'Diani'
        place.description = 'Sandy beaches'
        place.number_rooms = 5
        place.number_bathrooms = 6
        place.max_guest = 12
        place.price_by_night = 60
        place.latitude = 4.35
        place.longitude = 13.07
        place.amenity_ids = [amenity.id, amenity_2.id]

        self.assertTrue(type(place.id) is str)
        self.assertTrue(type(city.id) is str)
        self.assertTrue(type(user.id) is str)
        self.assertTrue(type(place.created_at) is datetime)
        self.assertTrue(type(place.updated_at) is datetime)

    def test_str(self):
        """ Test string magic method
        """
        city = City()
        user = User()
        amenity = Amenity()
        amenity_2 = Amenity()
        place = Place()
        place_str = place.__str__()
        self.assertTrue(type(place_str) is str)
        self.assertEqual(str(place), place_str)

        place.city_id = city.id
        place.user_id = user.id
        place.name = 'Diani'
        place.description = 'Sandy beaches'
        place.number_rooms = 5
        place.number_bathrooms = 6
        place.max_guest = 12
        place.price_by_night = 60
        place.latitude = 4.35
        place.longitude = 13.07
        place.amenitiy_ids = [amenity.id, amenity_2.id]

        place_str = place.__str__()
        self.assertEqual(str(place), place_str)

    def test_to_dict(self):
        """ Test to_dict method
        """
        city = City()
        user = User()
        amenity = Amenity()
        amenity_2 = Amenity()
        place = Place()
        place_dict = place.to_dict()

        self.assertNotEqual(place_dict, place.__dict__)
        self.assertTrue("__class__" in place_dict)
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertTrue(type(place_dict["created_at"]) is str)
        self.assertTrue(type(place_dict["updated_at"]) is str)

        place.city_id = city.id
        place.user_id = user.id
        place.name = 'Diani'
        place.description = 'Sandy beaches'
        place.number_rooms = 5
        place.number_bathrooms = 6
        place.max_guest = 12
        place.price_by_night = 60
        place.latitude = 4.35
        place.longitude = 13.07
        place.amenity_ids = [amenity.id, amenity_2.id]

        place_dict = place.to_dict()
        self.assertTrue('city_id' in place_dict)
        self.assertTrue('user_id' in place_dict)
        self.assertTrue('name' in place_dict)
        self.assertTrue('number_rooms' in place_dict)
        self.assertTrue('number_bathrooms' in place_dict)
        self.assertTrue('max_guest' in place_dict)
        self.assertTrue('price_by_night' in place_dict)
        self.assertTrue('latitude' in place_dict)
        self.assertTrue('longitude' in place_dict)
        self.assertTrue('amenity_ids' in place_dict)

    def test_save(self):
        """ Test save method
        """
        place = Place()
        time_1 = place.updated_at
        place.save()
        time_2 = place.updated_at
        self.assertNotEqual(time_1, time_2)

        my_json = dumps(place.to_dict())
        with open(storage._FileStorage__file_path, "r", encoding="UTF8") as f:
            read = f.read()
        self.assertTrue(my_json in read)

    def test_create(self):
        """ Test in new object is saved to list of object
        """
        place = Place()
        self.assertEqual(place.__class__.__name__, 'Place')

        key = ".".join([place.__class__.__name__, place.id])
        self.assertTrue(storage._FileStorage__objects[key] is place)


if __name__ == "__main__":
    unittest.main()
