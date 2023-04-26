#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from .state import State
from .city import City
from .place import Place
from .user import User
from .review import Review
from .amenity import Amenity

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
