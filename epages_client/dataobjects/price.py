# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class Price(DataObject):
    """Data object for price"""

    def __init__(self):
        # string Indicates if the amount includes tax. Can be GROSS, NET or NONE.
        self._taxType = None
        # string The amount of the price with currency unit.
        self._formatted = None
        # number The amount of the price.
        self._amount = None
        # string The currency code of the price according to ISO 4217.
        self._currency = None

    @property
    def taxType(self):
        return self._taxType

    @taxType.setter
    def taxType(self, value):
        if value in ('GROSS', 'NET', 'NONE'):
            self._taxType = value
        else:
            raise ValueError("TaxType has to be GROSS, NET or NONE (str)")

    @property
    def formatted(self):
        return self._formatted

    @formatted.setter
    def formatted(self, value):
        self._formatted = self._check_str(value)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = self._check_numeric(value)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = self._check_str(value)

    def is_valid(self):
        return True
