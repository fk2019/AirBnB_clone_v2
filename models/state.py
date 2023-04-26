#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models


if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(City, backref="state",
                              cascade="all, delete, delete-orphan")
else:
    class State(BaseModel):
        @property
        def cities(self):
            """Return list of City isntances with state.id=State.id"""
            cities = []
            all_list = models.storage.all(City)
            for key, value in all_list.items():
                if value.state.id == self.id:
                    city.append(value)
            return cities
#    name = ""
