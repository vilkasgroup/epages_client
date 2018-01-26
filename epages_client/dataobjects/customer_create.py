# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject
from .address import Address


class CustomerCreate(DataObject):
    ''''Data object for creating a new customer to ePages webshop'''

    def __init__(self):
        # string The number by which the merchant tracks the customer. If provided, the customer number must be unique. If not provided, the customer number will be generated automatically.
        self._customerNumber = None
        # string Internal note for the customer done by the merchant.
        self._internalNote = None
        # address The billing address of the customer (mandatory).
        self.billingAddress = Address()

    @property
    def customerNumber(self):
        return self._customerNumber

    @customerNumber.setter
    def customerNumber(self, value):
        self._customerNumber = self._check_str(
            value, "customerNumber has to be str")

    @property
    def internalNote(self):
        return self._internalNote

    @internalNote.setter
    def internalNote(self, value):
        self._internalNote = self._check_str(
            value, "internalNote has to be str")

    def is_valid(self):
        return self.billingAddress.is_valid()
