# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .data_object import DataObject
from .tax_class_info import TaxClassInfo
from .price import Price


class TaxInfo(DataObject):
    """Data object for tax info"""

    def __init__(self):
        # object of taxClassInfo The information on the tax class.
        self.taxClass = TaxClassInfo()
        # object of price The amount of the charged tax.
        self.price = Price()

    def get_dict(self):
        return {
            'price': self.price.get_dict(),
            'taxClass': self.taxClass.get_dict()
        }

    def is_valid(self):
        return self.taxClass.is_valid() and self.price.is_valid()
