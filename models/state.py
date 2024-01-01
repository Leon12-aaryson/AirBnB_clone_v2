#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    from models import storage
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # Add primary key definition
    id = Column(String(60), nullable=False, primary_key=True)

    # Add relationship to City
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
    
    if storage.__class__.__name__ != 'DBStorage':
        @property
        def cities(self):
            """Returns the list of City objects linked to the current State."""
            cities_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list