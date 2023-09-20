#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        name = ""

    @property
    def cities(self):
        from models.city import City
        from models import storage
        """Get a list of all linked cities."""
        cities_list = []
        for city in list(storage.all(City).values()):
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
