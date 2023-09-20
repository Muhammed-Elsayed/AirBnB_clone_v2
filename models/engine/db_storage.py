#!/usr/bin/python3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker

"""
db storage
"""


class DBStorage:
    """class"""
    __engine = None
    __session = None

    def __init__(self):
        """init"""
        self.__engine = create_engine(f'mysql+mysqldb://{getenv("HBNB_MYSQL_USER")}\
								:{getenv("HBNB_MYSQL_PWD")}\
									@{getenv("HBNB_MYSQL_HOST")}/{getenv("HBNB_MYSQL_DB")}'\
                                        ,pool_pre_ping=True)
        

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    
    def all(self, cls=None):
        """documentatoin"""
        if (cls == None):
            objs = self.__session.query()

        
        
        else:
            pass



        

        
