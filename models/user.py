#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
import models
from sqlalchemy import Column, String, ForeignKey
from os import getenv
import sqlalchemy
from sqlalchemy.orm import relationship


class User(BaseModel):

    """This class defines a user by various attributes"""

    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
#"""This module defines a class User"""

#from sqlalchemy import Column, String, Integer
#from sqlalchemy.orm import relationship
#from models.base_model import BaseModel, Base

#class User(BaseModel, Base):
    #__tablename__ = 'users'

    #id = Column(Integer, primary_key=True)
    #email = Column(String(128), nullable=False)
    #password = Column(String(128), nullable=False)
    #first_name = Column(String(128), nullable=True)
    #last_name = Column(String(128), nullable=True)

    #places = relationship("Place", back_populates="user", cascade="all, delete-orphan")
    #reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")
