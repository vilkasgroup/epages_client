# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject
from .shippingmethodinfo import ShippingMethodInfo
from .price import Price
from .tax_info import TaxInfo
from .list_of_objects import ListOfObjects


class ShippingData(DataObject):
    def __init__(self):
        # object of shippingMethodInfo Information on the shipping method chosen by the customer.
        self.shippingMethod = ShippingMethodInfo()
        # object of price The costs for the shipping.
        self.price = Price()
        # array of taxInfo Information on the taxes for the shipping.
        self.taxes = ListOfObjects(TaxInfo)

    def get_dict(self):
        pass

    def is_valid(self):
        ''''''
        return self.taxes.is_valid() and self.price.is_valid() and self.shippingMethod.is_valid()
