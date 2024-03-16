#!/usr/bin/python3
"""Module for User class"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))

        places = relationship("Place", cascade="all, delete", backref='user_places')
        reviews = relationship('Review', cascade="all, delete, delete-orphan", backref='user')

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

