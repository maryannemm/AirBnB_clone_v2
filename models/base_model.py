#!/usr/bin/python3
""" Module for BaseModel class """

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """ Class for Base Model """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ Initializes the BaseModel instance """
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
            if 'created_at' not in kwargs:
                setattr(self, 'created_at', datetime.utcnow())
            if 'updated_at' not in kwargs:
                setattr(self, 'updated_at', datetime.utcnow())

    def save(self):
        """ Saves the current instance to the storage """
        from models import storage
        storage.new(self)
        storage.save()

    def delete(self):
        """ Deletes the current instance from the storage """
        storage.delete(self)

    def to_dict(self):
        """ Returns a dictionary representation of the instance """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict.pop('_sa_instance_state', None)
        return obj_dict

