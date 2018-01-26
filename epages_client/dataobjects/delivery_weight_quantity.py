# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class DeliveryWeightQuantity(DataObject):
    '''Data object for DeliveryWeightQuantity'''

    def __init__(self):
        # number The amount displayed as a decimal number.
        self._amount = None
        # string The abbreviation of the delivery weight unit. Can be g, kg, mg, oz, lb or t.
        self._unit = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = self._check_numeric(value)

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        if value in ('g', 'kg', 'mg', 'oz', 'lb', 't'):
            self._unit = value
        else:
            raise ValueError("Unit value can be g, kg, mg, oz, lb or t (str).")

    def is_valid(self):
        return True
