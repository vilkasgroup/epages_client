# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class Quantity(DataObject):
    """Dataobject for Quantity"""

    def __init__(self):

        # number The amount displayed as a decimal number.
        self._amount = None
        # string The unit displayed as abbreviated unit, if available. Can be one of Byte, kByte, MByte, GByte, TByte, l, ml, ft³, in³, m³, yd³, fl oz, gal, qt, m, cm, ft, in, km, mm, yd, s, min, m², cm², ft², in², mm² or yd². Otherwise a localised name of the unit is displayed. Can be piece(s), bottle(s), crate(s), can(s), capsule(s), box(es), glass(es), kit(s), pack(s), package(s), pair(s), roll(s), set(s), sheet(s), ticket(s), unit(s), day(s), hour(s), week(s), month(s), night(s) or year(s).
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
        self._unit = self._check_str(value)

    def is_valid(self):
        return True
