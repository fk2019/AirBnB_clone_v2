#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


if getenv("HBNB_TYPE_STORAGE") == "db":
    class Place(BaseModel, Base):
        """ A place to stay """
        if getenv("HBNB_TYPE_STORAGE") == "db":
            __tablename__ = "places"
            city_id = Column(String(60), ForeignKey('cities.id'),
                             nullable=False)
            name = Column(String(128), nullable=False)
            user_id = Column(String(60), ForeignKey('users.id'),
                             nullable=False)
            description = Column(String(1024), nullable=True)
            number_rooms = Column(Integer(), nullable=False, default=0)
            number_bathrooms = Column(Integer(), nullable=False, default=0)
            price_by_night = Column(Integer(), nullable=False, default=0)
            max_guest = Column(Integer(), nullable=False, default=0)
            latitude = Column(Float(), nullable=True)
            longitude = Column(Float(), nullable=True)
            reviews = relationship(Review, backref="place",
                                   cascade="all, delete, delete-orphan")
            amenities = relationship("Amenity", secondary=place_amenity)
            amenity_ids = []
else:
    class Place(BaseModel):
        """ A place to stay """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Return list of Review instances
               with place_id = current Place.id
            """
            reviews_list = []
            for key, value in models.storage.all(Review):
                if value.place_id == self.id:
                    reviews_list.append(value)
            return reviews_list

        @property
        def amenities(self):
            """Return list of Amenity isntances based on
               amenity_ids that contain Amenity_id linked to
               Place
            """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Handle append method for adding an Amenity.id
               to attribute amenity_ids
            """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
