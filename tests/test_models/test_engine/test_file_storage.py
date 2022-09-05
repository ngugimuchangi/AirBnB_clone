#!/usr/bin/python3
""" File storage test module
"""
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage
from os import path, remove
import unittest


class TestStorage(unittest.TestCase):
    """ File storage test class
    """

    def setUp(self):
        """ Set up actions for tests
        """

        self.base = BaseModel()
        self.base_2 = BaseModel()

        self.user = User()
        self.user.email = 'airbnb@gmail.com'
        self.user.password = '1234'
        self.user.first_name = 'Home'
        self.user.last_name = 'Owner'

        self.user_2 = User()
        self.user_2.email = 'email@email.com'
        self.user_2.password = '5678'
        self.user_2.first_name = 'Amazing'
        self.user_2.last_name = 'Realtor'

        self.state = State()
        self.state.name = "Nairobi"
        self.state_2 = State()
        self.state_2.name = "Coast"

        self.city = City()
        self.city.state_id = self.state.id
        self.city_2 = City()
        self.city_2.state_id = self.state_2.id

        self.amenity = Amenity()
        self.amenity.name = "Wi-Fi"
        self.amenity_2 = Amenity()
        self.amenity_2.name = "Swimming pool"

        self.place = Place()
        self.place.city_id = self.city.id
        self.place.user_id = self.user.id
        self.place.name = 'Diani'
        self.place.description = 'Sandy beaches'
        self.place.number_rooms = 5
        self.place.number_bathrooms = 6
        self.place.max_guest = 12
        self.place.price_by_night = 60
        self.place.latitude = 4.35
        self.place.longitude = 13.07
        self.place.amenity_ids = [self.amenity.id, self.amenity_2.id]

        self.place_2 = Place()
        self.place_2.city_id = self.city.id
        self.place_2.user_id = self.user.id
        self.place_2.name = 'Naserian Palatial Homes'
        self.place_2.description = 'Chilled retreat'
        self.place_2.number_rooms = 4
        self.place_2.number_bathrooms = 3
        self.place_2.max_guest = 9
        self.place_2.price_by_night = 55
        self.place_2.latitude = 2.35
        self.place_2.longitude = 9.07
        self.place_2.amenity_ids = [self.amenity.id]

        self.review = Review()
        self.review.place_id = self.place.id
        self.review.user_id = self.user.id
        self.review.text = "Bad service"

        self.review_2 = Review()
        self.review_2.place_id = self.place.id
        self.review_2.user_id = self.user.id
        self.review_2.text = "Best staycation place"

    def tearDown(self):
        """ Clean up action at the end of each test
        """

        del self.base
        del self.base_2
        del self.user
        del self.user_2
        del self.city
        del self.city_2
        del self.state
        del self.state_2
        del self.amenity
        del self.amenity_2
        del self.place
        del self.place_2
        del self.review
        del self.review_2

        if path.exists(storage._FileStorage__file_path):
            remove(storage._FileStorage__file_path)

    def test_all(self):
        """ Test all function
        """
        my_dict = storage.all()
        my_objects = []
        for i in my_dict.keys():
            my_objects.append(my_dict[i])

        self.assertTrue(self.base in my_objects)
        self.assertTrue(self.base_2 in my_objects)
        self.assertTrue(self.user in my_objects)
        self.assertTrue(self.user_2 in my_objects)
        self.assertTrue(self.city in my_objects)
        self.assertTrue(self.city_2 in my_objects)
        self.assertTrue(self.state in my_objects)
        self.assertTrue(self.state_2 in my_objects)
        self.assertTrue(self.amenity in my_objects)
        self.assertTrue(self.amenity_2 in my_objects)
        self.assertTrue(self.place in my_objects)
        self.assertTrue(self.place_2 in my_objects)
        self.assertTrue(self.review in my_objects)
        self.assertTrue(self.review_2 in my_objects)

    def test_save(self):
        """ Test storage function
        """
        storage.save()
        self.assertTrue(path.exists(storage._FileStorage__file_path))

    def test_reload(self):
        """ Test reload function
        """
        with self.assertRaises(FileNotFoundError):
            open(storage._FileStorage__file_path, "r", encoding="UTF8")

        storage.save()
        storage.reload()
        my_objects = []
        for i in storage._FileStorage__objects.keys():
            my_objects.append(storage._FileStorage__objects[i])

        self.assertTrue(all(isinstance(i, BaseModel) for i in my_objects))
        self.assertTrue(any(isinstance(i, User) for i in my_objects))
        self.assertTrue(any(isinstance(i, State) for i in my_objects))
        self.assertTrue(any(isinstance(i, City) for i in my_objects))
        self.assertTrue(any(isinstance(i, Amenity) for i in my_objects))
        self.assertTrue(any(isinstance(i, Place) for i in my_objects))
        self.assertTrue(any(isinstance(i, Review) for i in my_objects))


if __name__ == "__main__":
    unittest.main()
