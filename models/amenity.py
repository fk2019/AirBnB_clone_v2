#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place, place_amenity
from models.review import Review
from os import getenv
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship(Place, secondary=place_amenity,
                                       viewonly=True)
    else:
        name = ""
