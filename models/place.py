#!/usr/bin/python3
""" Place module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class: a subclass of BaseModel
        Place class attributes:
            city_id (str): City's id
            user_id (str): User id
            name (str): Name of the place
            description (str): Description of the place
            number_rooms (int): Number of rooms
            number_bathrooms (int): Number of bathroms
            max_guest (int): Maximum number of guests
            price_by_night (int): Price per night
            latitude (float): :atitudinal coordinate
            longitude (float): Longitudinal coordinate
            amenity_ids (list): List of amenities ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
