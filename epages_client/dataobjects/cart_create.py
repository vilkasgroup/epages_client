# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .data_object import DataObject
from .list_of_objects import ListOfObjects
from .product_line_item_create import ProductLineItemCreate


class CartCreate(DataObject):
    '''Data object for creating a new cart to ePages webshop'''

    def __init__(self):
        # string The currency code of the price according to ISO 4217.
        self._currency = None
        # string Indicates if the amount includes tax. Can be gross, net or none.
        self._taxType = None
        # string The locale that identifies the origin of the customer.
        self._locale = None
        # array of productLineItem (create request) The product line items in the basket.
        self.lineItems = ListOfObjects(ProductLineItemCreate)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = self._check_str(value, "Currency has to be a str.")

    @property
    def taxType(self):
        return self._taxType

    @taxType.setter
    def taxType(self, value):
        if value in ('GROSS', 'NET', 'NONE'):
            self._taxType = value
        else:
            raise ValueError('TaxType must be GROSS, NET or NONE (str).')

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = self._check_str(value, "Locale has to be a str.")

    def is_valid(self):
        return self.lineItems.is_valid()
