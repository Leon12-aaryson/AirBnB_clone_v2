#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

if models.storage_t == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))
class Place(BaseModel):
    """ A place to stay """

    if models.storage_t == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def reviews(self):
            """getter attribute returns the list of Review instances"""
            from models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances"""
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list
    
#""" Place Module for HBNB project """
#from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
#from sqlalchemy.orm import relationship
#from models.base_model import BaseModel, Base


#class Place(BaseModel, Base):
    #__tablename__ = 'places'

    #city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    #user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    #name = Column(String(128), nullable=False)
    #description = Column(String(1024), nullable=True)
    #number_rooms = Column(Integer, nullable=False, default=0)
    #number_bathrooms = Column(Integer, nullable=False, default=0)
    #max_guest = Column(Integer, nullable=False, default=0)
    #price_by_night = Column(Integer, nullable=False, default=0)
    #latitude = Column(Float, nullable=True)
    #longitude = Column(Float, nullable=True)

    #user = relationship("User", back_populates="places")
    #city = relationship("City", back_populates="places")
    
    #reviews = relationship("Review", back_populates="place", cascade="all, delete-orphan")
    
    #@property
    #def reviews(self):
        #from models import storage
        #reviews_list = []
        #for review in storage.all(Review).values():
            #if review.place_id == self.id:
                #reviews_list.append(review)
        #return reviews_list
    
    #place_amenity = Table('place_amenity', Base.metadata,
                      #Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      #Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
                      #)

    #class PlaceAmenity(Base):
        #__tablename__ = 'place_amenity'
        #place_id = Column(String(60), ForeignKey('places.id'), primary_key=True, nullable=False)
        #amenity_id = Column(String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
        #amenity = relationship("Amenity", back_populates="place_amenities")
        #place = relationship("Place", back_populates="amenities")
        
    #amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)

    #Base.metadata.create_all(iengine)

    #place_amenity = Table('place_amenity', Base.metadata, extend_existing=True,
                      #Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True),
                      #Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True)
                      #)


    # For FileStorage
    #@property
    #def amenities(self):
        #from models import storage
        #amenities_list = []
        #for amenity_id in getattr(self, 'amenity_ids', []):
            #amenity = storage.get('Amenity', amenity_id)
            #if amenity:
                #amenities_list.append(amenity)
        #return amenities_list

    #@amenities.setter
   # def amenities(self, amenity):
        #if isinstance(amenity, Amenity):
            #if not hasattr(self, 'amenity_ids'):
                #setattr(self, 'amenity_ids', [])
            #if amenity.id not in self.amenity_ids:
                #self.amenity_ids.append(amenity.id)
