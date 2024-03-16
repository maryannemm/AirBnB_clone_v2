#!/usr/bin/python3
"""Module for Place class"""
import os
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """This class defines a place by various attributes"""

    __tablename__ = 'places'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)
        place_amenity = Table('place_amenity', Base.metadata,
            Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
        )
        user = relationship(
            'User',
            backref='user_places'
            )
        reviews = relationship('Review', cascade="all, delete, delete-orphan", backref='place')

        city = relationship("City", back_populates="places")

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

        @property
        def reviews(self):
            from models import storage
            reviews_dict = storage.all(Review)
            return [review for review in reviews_dict.values() if review.place_id == self.id]
        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

