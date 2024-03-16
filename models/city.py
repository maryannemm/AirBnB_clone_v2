#!/usr/bin/python3
"""Module for City class"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """This class defines a city by various attributes"""
    __tablename__ = 'cities'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        places = relationship(
        'Place',
        cascade="all, delete, delete-orphan",
        backref='cities'  # Change 'city' to 'cities'
        )

    else:
        name = ""

