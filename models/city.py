#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place

if getenv("HBNB_TYPE_STORAGE") == "db":
    class City(BaseModel, Base):
        """ The city class, contains tablename state ID and name """
        if getenv("HBNB_TYPE_STORAGE") == "db":
            __tablename__ = "cities"
            state_id = Column(String(60), ForeignKey('states.id'),
                              nullable=False)
            name = Column(String(128), nullable=False)
            places = relationship(Place, backref="cities",
                                  cascade="all, delete, delete-orphan")
else:
    class City(BaseModel):
        state_id = ""
        name = ""
