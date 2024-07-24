#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import sqlalchemy
import sqlalchemy.exc
from os import getenv, path
from backend.models.base import Base
from backend.models.user import User
from backend.models.admin import Admin
from backend.models.challenge import Challenge
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from flask_sqlalchemy import SQLAlchemy


parent_dir = path.dirname(path.abspath(__file__))
dotenv_path = path.join(parent_dir, '.utils.env')
load_dotenv(dotenv_path=dotenv_path, override=True)

CLASSES = {'User': User, 'Admin': Admin, 'Challenge': Challenge}


class DBStorage():
    """MySQL database storage class"""
    __engine = None
    __session = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Create a new instance of DBStorage"""
        if not cls._instance:
            cls._instance = super(DBStorage, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """Instantiate a DBStorage object"""
        ENV = getenv('ENV')
        try:
            self.__engine = create_engine(self.get_database_uri(), pool_pre_ping=True)
        except sqlalchemy.exc.SQLAlchemyError and sqlalchemy.exc.OperationalError as e:
            print(f"Error creating engine: {e}")

        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    @property
    def session(self):
        """returns the session attribute"""
        return self.__session

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        if cls is None:
            for cl in CLASSES.values():
                objs = self.query(cl).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        else:
            objs = self.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is None:
            return
        self.__session.delete(obj)
        self.save()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        create_session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(create_session)
        self.__session = Session

    def get(self, cls, id):
        """retrieve one object"""
        if cls is None or cls not in CLASSES.values():
            return None

        all_objs = self.all(cls)
        for val in all_objs.values():
            if val.id == id:
                return val
        return None

    def count(self, cls=None):
        """count the number of objects in storage"""
        all_cls = CLASSES.keys()
        count = self.query(cls).count() if cls else sum(
            self.query(cl).count() for cl in all_cls
            )
        return count

    def query(self, cls):
        """query on the current database session"""
        return self.__session.query

    def rollback(self):
        """rollback a transaction"""
        self.__session.rollback()

    def close(self):
        """close the session"""
        self.__session.close()

    def get_database_uri(self):
        """return the database URI"""
        MYSQL_USER = getenv('DBUSER')
        MYSQL_PWD = getenv('DBPWD')
        MYSQL_HOST = getenv('HOST')
        MYSQL_DB = getenv('DB')
        URI = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}/{MYSQL_DB}'
        return URI