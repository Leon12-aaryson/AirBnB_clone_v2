#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        # from models import storage  # Import here, not at the top
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from models import storage, classes  # Import here, not at the top
        session = self.__session()
        if cls:
            objs = session.query(classes[cls]).all()
        else:
            objs = []
            for c in classes:
                objs += session.query(classes[c]).all()
        objs_dict = {}
        for obj in objs:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            objs_dict[key] = obj
        session.close()
        return objs_dict

    def new(self, obj):
        #from models import storage  # Import here, not at the top
        self.__session.add(obj)

    def save(self):
        #from models import storage  # Import here, not at the top
        self.__session.commit()

    def delete(self, obj=None):
        #from models import storage  # Import here, not at the top
        if obj:
            self.__session.delete(obj)

    def reload(self):
         """Create all tables in the database and initialize a new session."""
         Base.metadata.create_all(self.__engine)
         session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
         Session = scoped_session(session_factory)
         self.__session = Session()
