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
            value, "CustomerNumber has to be a str.")

    @property
    def internalNote(self):
        return self._internalNote

    @internalNote.setter
    def internalNote(self, value):
        self._internalNote = self._check_str(
            value, "InternalNote has to be a str.")

    def is_valid(self):
        # Get values for billing address
        billing_address_values = self.billingAddress.__dict__

        # Loop values and check, if there's even one set
        for key in billing_address_values:
            if billing_address_values[key] != None:
                return True

        return False
