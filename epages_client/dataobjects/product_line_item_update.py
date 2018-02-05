# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class ProductLineItemUpdate(DataObject):
    """Data object for ProductLineItemUpdate"""

    def __init__(self, quantity=None):
        self._quantity = None if quantity == None else self._check_numeric(
            quantity, "Quantity has to be a numeric type.")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = self._check_numeric(
            value, "Quantity has to be a numeric type.")

    def is_valid(self):
        return self._quantity != None
