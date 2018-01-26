# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject
from .price import Price


class DepositLineItem(DataObject):
    def __init__(self):
        # string The name of the line item.
        self._name = None
        # object of price The price of the line item.
        self.lineItemPrice = Price()
        # string The identifier of the related product line item. A deposit is always bound to a product.
        self._lineItemProductGuid = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._check_str(value)

    @property
    def lineItemProductGuid(self):
        return self._lineItemProductGuid

    @lineItemProductGuid.setter
    def lineItemProductGuid(self, value):
        self._lineItemProductGuid = self._check_str(value)

    def is_valid(self):
        return self.lineItemPrice.is_valid()
