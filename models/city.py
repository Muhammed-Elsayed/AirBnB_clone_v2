#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
        name = Column(String(128), nullable=False)
        state = relationship('State', back_populates='cities')
        places = relationship("Place", backref="cities", cascade="delete")


    else:
        name = ""
        state_id = ""