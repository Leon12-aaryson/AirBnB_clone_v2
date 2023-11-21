#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
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

    user = relationship("User", back_populates="places")
    city = relationship("City", back_populates="places")
    
    reviews = relationship("Review", back_populates="place", cascade="all, delete-orphan")
    
    @property
    def reviews(self):
        from models import storage
        reviews_list = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                reviews_list.append(review)
        return reviews_list
    
    place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
                      )

    class PlaceAmenity(Base):
        __tablename__ = 'place_amenity'
        place_id = Column(String(60), ForeignKey('places.id'), primary_key=True, nullable=False)
        amenity_id = Column(String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
        amenity = relationship("Amenity", back_populates="place_amenities")
        place = relationship("Place", back_populates="amenities")
        
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)

    # For FileStorage
    @property
    def amenities(self):
        from models import storage
        amenities_list = []
        for amenity_id in getattr(self, 'amenity_ids', []):
            amenity = storage.get('Amenity', amenity_id)
            if amenity:
                amenities_list.append(amenity)
        return amenities_list

    @amenities.setter
    def amenities(self, amenity):
        if isinstance(amenity, Amenity):
            if not hasattr(self, 'amenity_ids'):
                setattr(self, 'amenity_ids', [])
            if amenity.id not in self.amenity_ids:
                self.amenity_ids.append(amenity.id)
