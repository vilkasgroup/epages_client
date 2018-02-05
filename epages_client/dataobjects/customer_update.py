# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .customer_create import CustomerCreate
from .enum_fetch_operator import FetchOperator


class CustomerUpdate(CustomerCreate):
    '''Data object for updating a customer to ePages webshop'''

    def __init__(self):
        super(CustomerUpdate, self).__init__()
        self.legals = {
            '/customerNumber': (FetchOperator.ADD,),
            '/billingAddress': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/internalNote': (FetchOperator.ADD, FetchOperator.REMOVE),
        }

    @property
    def internalNote(self):
        return self._internalNote

    @internalNote.setter
    def internalNote(self, value):
        self._internalNote = self._check_str(value, "InternalNote has to be a str or RemoveValue.", True)

    def get_patch(self):
        return self.get_list_of_json_patches(self.legals)

    def is_valid(self):
        return self.billingAddress.is_valid()
