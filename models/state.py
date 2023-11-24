#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # Add primary key definition
    id = Column(String(60), nullable=False, primary_key=True)

    # Add relationship to City
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
