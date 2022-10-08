#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""


from datetime import datetime
import uuid
import models

date_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            return

        for key, value in kwargs.items():
            if key != "__class__":
                setattr(self, key, value)

        if hasattr(self, "created_at") and type(self.created_at) is str:
            update = datetime.strptime(kwargs['updated_at'], date_format)
            kwargs['updated_at'] = update

        if hasattr(self, "created_at") and type(self.created_at) is str:
            create = datetime.strptime(kwargs['created_at'], date_format)
            kwargs['created_at'] = create

        del kwargs['__class__']
        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
