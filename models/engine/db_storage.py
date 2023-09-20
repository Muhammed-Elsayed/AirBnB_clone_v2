#!/usr/bin/python3
"""represents db storage"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session

from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from models.user import User


class DBStorage:
    """class"""
    __engine = None
    __session = None

    def __init__(self):
        """init"""
        self.__engine = create_engine(f'mysql+mysqldb://\
                                      {getenv("HBNB_MYSQL_USER")}\
                                      :{getenv("HBNB_MYSQL_PWD")}\
                                      @{getenv("HBNB_MYSQL_HOST")}\
                                      /{getenv("HBNB_MYSQL_DB")}',
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """documentatoin"""
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(Amenity).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """add obj"""
        self.__session.add(obj)

    def save(self):
        """commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj if not none"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """jjjjj"""
        Base.metadata.create_all(self.__engine)
        Session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(Session_factory)
        self.__session = Session()
