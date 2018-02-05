# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class ListOfObjects(DataObject):
    '''Allow insert only one type items to a list'''

    def __init__(self, type_of_object):
        self._list = []
        self._type_of_object = type_of_object

    def add(self, obj):
        """Add a new item to the list. If the item is not type of set in the constructor, throw Type error"""
        if isinstance(obj, self._type_of_object):
            self._list.append(obj)
        else:
            raise TypeError(type(
                obj).__name__ + " is not instance of " + type(self._type_of_object).__name__)

    def get(self):
        """Returns a list"""
        return self._list

    def __str__(self):
        """string representation of a list"""
        return self._list.__str__()

    def get_dict(self):
        if not isinstance(self._type_of_object, tuple) and issubclass(self._type_of_object, DataObject):
            return [x.get_dict() for x in self._list]
        else:
            return self._list

    def is_valid(self):
        '''
        Check the validity of every item if item is a DataObject.
        First we have to check if item is not a tuple, because issubclass
        needs the first argument to be a class. And if type_of_object is
        a string, it is actually string_types from library six, and it is a tuple.
        '''
        if not isinstance(self._type_of_object, tuple):
            if issubclass(self._type_of_object, DataObject):
                for item in self._list:
                    if item.is_valid() == False:
                        return False
        return True
