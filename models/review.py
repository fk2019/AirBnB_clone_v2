#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey


if getenv("HBNB_TYPE_STORAGE") == "db":
    class Review(BaseModel, Base):
        """ Review class to store review information """
        if getenv("HBNB_TYPE_STORAGE") == "db":
            __tablename__ = "reviews"
            place_id = Column(String(60), ForeignKey('places.id'),
                              nullable=False)
            user_id = Column(String(60), ForeignKey('users.id'),
                             nullable=False)
            text = Column(String(1024), nullable=False)
else:
    class Review(BaseModel):
        """ Review class to store review information """
        place_id = ""
        user_id = ""
        text = ""
