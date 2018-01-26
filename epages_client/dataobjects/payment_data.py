# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject
from .payment_method_info import PaymentMethodInfo
from .price import Price
from .tax_info import TaxInfo
from .list_of_objects import ListOfObjects


class PaymentData(DataObject):
    """Data object for payment data object"""

    def __init__(self):
        # object of paymentMethodInfo Information on the payment type chosen by the customer.
        self.paymentMethod = PaymentMethodInfo()
        # object of price The costs for the payment method.
        self.price = Price()
        # string Indicates the status of the payment. Can be either CANCELED, FAILED or null.
        self._status = None
        # array of taxInfo Information on the taxes for the payment.
        self.taxes = ListOfObjects(TaxInfo)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value in (None, 'CANCELED', 'FAILED'):
            self._status = value
        else:
            raise ValueError("Status has to be CANCELED, FAILED or null")

    def is_valid(self):
        return self.taxes.is_valid() and self.paymentMethod.is_valid() and self.price.is_valid()
