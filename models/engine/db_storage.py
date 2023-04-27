#!/usr/bin/enb python3
"""DBStorage engine uses MySQL db
"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.amenity import Amenity

database = getenv("HBNB_MYSQL_DB")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
pwd = getenv("HBNB_MYSQL_PWD")
env = getenv("HBNB_ENV")


class DBStorage():
    """DBStorage class links with MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                                      (user, pwd, host, database),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query current db session all objects depending on cls"""
        db_objs = {}
        classes = ["City", "Place", "Review", "User", "State", "Ame\
    nity"]
        if cls is None:
            for el in classes:
                query = self.__session.query(el)
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    db_objs[key] = obj
        else:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                db_objs[key] = obj
        return db_objs

    def new(self, obj):
        """Add object to current db session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from current db session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in db
           Create current db session from the engine by using sessionmaker
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Terminate current db session"""
        self.__session.close()
