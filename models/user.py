#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


if getenv("HBNB_TYPE_STORAGE") == "db":
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            __tablename__ = "users"
            email = Column(String(128), nullable=False)
            password = Column(String(128), nullable=False)
            first_name = Column(String(128), nullable=True)
            first_name = Column(String(128), nullable=True)
            places = relationship(Place, backref="user",
                                  cascade="all, delete, delete-orphan")
            reviews = relationship(Review, backref="user",
                                   cascade="all, delete, delete-orphan")
else:
    class User(BaseModel):
        """This class defines a user by various attributes"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
