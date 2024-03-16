#!/usr/bin/python3
""" Module for State class """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Getter attribute that returns the list of City instances
        with state_id equals to the current State.id"""
        cities_list = []
        for city in list(models.storage.all(City).values()):
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list

    def __str__(self):
        """Return string representation of the State object"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

