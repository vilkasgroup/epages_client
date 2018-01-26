# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class TaxClassInfo(DataObject):
    """Data object for TaxClassInfo"""

    def __init__(self):
        # string The unique identifier of the tax class.
        self._taxClassId = None
        # string The name of the tax class.
        self._name = None
        # number The percentage the product is taxed with.
        self._percentage = None

    @property
    def taxClassId(self):
        return self._taxClassId

    @taxClassId.setter
    def taxClassId(self, value):
        self._taxClassId = self._check_str(value)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._check_str(value)

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        self._percentage = self._check_numeric(value)

    def is_valid(self):
        return True
