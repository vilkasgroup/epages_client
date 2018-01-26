# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject
from .price import Price


class LineItem(DataObject):
    """"Data object for LineItem object"""

    def __init__(self):
        # string The name of the line item.
        self._name = None
        # object of price The price of the line item.
        self.lineItemPrice = Price()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._check_str(value)

    def is_valid(self):
        return True
