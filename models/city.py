#!/usr/bin/python3
""" City Module for HBNB project """

# from sqlalchemy import Column, String, ForeignKey
# from models.base_model import BaseModel, Base


# class City(BaseModel, Base):
#     __tablename__ = 'cities'
#     name = Column(String(128), nullable=False)
#     state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    __tablename__ = 'cities'

    # Assuming 'id' is the primary key column
    id = Column(String(60), primary_key=True)
    
    name = Column(String(128), nullable=False)
    
    # Assuming there's a relationship with the State model
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    state_relationship = relationship("State", back_populates="cities")
