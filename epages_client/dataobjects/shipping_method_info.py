# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class ShippingMethodInfo(DataObject):
    '''Dataobject for shipping method info'''

    def __init__(self):

        # string The unique identifier of the shipping method.
        self._id = None
        # string The name of the shipping method chosen by the customer.
        self._name = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = self._check_str(value)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._check_str(value)

    def is_valid(self):
        return True
