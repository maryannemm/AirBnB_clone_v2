#!/usr/bin/python3
""" Module for State class """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Getter attribute that returns the list of City instances
        with state_id equals to the current State.id"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            from models import storage
            return [city for city in storage.all(City).values() if city.state_id == self.id]
        else:
            from models import storage
            return [city for city in storage.all(City).values() if city.state_id == self.id]

    def __str__(self):
        """Return string representation of the State object"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

