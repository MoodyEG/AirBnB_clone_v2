#!/usr/bin/python3
""" DataBase Storage """
from os import getenv
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.orm import sessionmaker, scoped_session  # type: ignore
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ DataBase Storage Class """
    __engine = ""
    __session = ""

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        environ = getenv("HBNB_ENV", "none")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if environ == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session """
        new_dic = {}
        classes = {'State': State,
                   'City': City}
        if not cls or cls == "":
            for key, value in classes.items():
                query = self.__session.query(value)
                for data in query:
                    key = "{}.{}".format(data.__class__.__name__,
                                         data.id)
                    new_dic[key] = data
            return new_dic
        else:
            query = self.__session.query(classes[cls])
            for data in query:
                key = "{}.{}".format(data.__class__.__name__, data.id)
                new_dic[key] = data
            return new_dic

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()
