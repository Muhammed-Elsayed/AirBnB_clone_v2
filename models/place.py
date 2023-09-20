#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


intermediate_table = Table("place_amenity", Base.metadata,
                           Column("place_id", String(60),
                                  ForeignKey("places.id"), nullable=False, primary_key=True),
                           Column("amenity_id", String(60),
                                  ForeignKey("amenities.id"), nullable=False,
                                  primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay for mysql database with variuos attributes"""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"),nullable=False)
    user_id = Column(String(60),ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) == "db":
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """getting linked amenities"""
            amenity_list = []

            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """setter method for amenity objects"""
            if (type(value) == Amenity):
                self.amenity_ids.append(value.id)
