# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class ProductLineItemCreate(DataObject):
    """Data object for ProductLineItemCreate"""

    def __init__(self):
        # string The unique identifier of the product.
        self._productId = None
        # number The product quantity of this line item displayed as a decimal number.
        self._quantity = None

    @property
    def productId(self):
        return self._productId

    @productId.setter
    def productId(self, value):
        self._productId = self._check_str(value, "ProductId has to be a str.")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = self._check_numeric(
            value, "Quantity has to be a numeric type.")

    def is_valid(self):
        return True
