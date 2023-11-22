#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """
    >>City inherits from BaseModel and Base (respect the order)
    >>class attribute __tablename__ -
            represents the table name, cities
    >>class attribute name
            represents a column containing a string (128 characters)
            cant be null
    >>class attribute state_id
            represents a column containing a string (60 characters)
            cant be null
            is a foreign key to states.id
    """
    __tablename__ = "cities"
    id = Column(String(60), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
#""" City Module for HBNB project """

# from sqlalchemy import Column, String, ForeignKey
# from models.base_model import BaseModel, Base


# class City(BaseModel, Base):
#     __tablename__ = 'cities'
#     name = Column(String(128), nullable=False)
#     state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

#from sqlalchemy import Column, String, ForeignKey
#from sqlalchemy.orm import relationship
#from models.base_model import BaseModel, Base

#class City(BaseModel, Base):
    #__tablename__ = 'cities'

    # Assuming 'id' is the primary key column
    #id = Column(String(60), primary_key=True)
    
    #name = Column(String(128), nullable=False)
    
    # Assuming there's a relationship with the State model
    #state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    #state_relationship = relationship("State", back_populates="cities")
    
    #places = relationship("Place", back_populates="city", cascade="all, delete-orphan")
