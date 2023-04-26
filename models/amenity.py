#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place, place_amenity


if getenv("HBNB_TYPE_STORAGE") == "db":
    class Amenity(BaseModel, Base):
        """This class defines a user by various attributes"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            __tablename__ = "amenities"
            name = Column(String(128), nullable=False)
            place_amenities = relationship(Place, secondary=place_amenity,
                                           viewonly=True)
else:
    class Amenity(BaseModel):
        """Define amenity class"""
        name = ""
