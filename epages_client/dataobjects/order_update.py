# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject
from .enum_fetch_operator import FetchOperator
from .list_of_objects import ListOfObjects
from .address import Address


class OrderUpdate(DataObject):
    """Dataobject for updating order"""

    def __init__(self):
        self._orderNumber = None
        self._customerComment = None
        self._internalNote = None
        self.billingAddress = Address()
        self.shippingAddress = Address()
        self._viewedOn = None
        self._rejectedOn = None
        self._inProcessOn = None
        self._pendingOn = None
        self._readyForDispatchOn = None
        self._partiallyDispatchedOn = None
        self._dispatchedOn = None
        self._deliveredOn = None
        self._partiallyInvoicedOn = None
        self._invoicedOn = None
        self._partiallyPaidOn = None
        self._paidOn = None
        self._returnedOn = None
        self._closedOn = None
        self._archivedOn = None

        self.legals = {
            '/orderNumber': (FetchOperator.ADD,),
            '/customerComment': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/internalNote': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/billingAddress': (FetchOperator.ADD,),
            '/shippingAddress': (FetchOperator.ADD,),
            '/viewedOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/rejectedOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/inProcessOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/pendingOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/readyForDispatchOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/partiallyDispatchedOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/dispatchedOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/deliveredOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/partiallyInvoicedOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/invoicedOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/partiallyPaidOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/paidOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/returnedOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/closedOn': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/archivedOn': (FetchOperator.ADD, FetchOperator.REMOVE),
        }

    @property
    def orderNumber(self):
        return self._orderNumber

    @orderNumber.setter
    def orderNumber(self, value):
        self._orderNumber = self._check_str(
            value, 'OrderNumber has to be a str.', False)

    @property
    def customerComment(self):
        return self._customerComment

    @customerComment.setter
    def customerComment(self, value):
        self._customerComment = self._check_str(
            value, 'CustomerComment has to be a str or RemoveValue.', True)

    @property
    def internalNote(self):
        return self._internalNote

    @internalNote.setter
    def internalNote(self, value):
        self._internalNote = self._check_str(
            value, 'InternalNote has to be a str or RemoveValue.', True)

    @property
    def viewedOn(self):
        return self._viewedOn

    @viewedOn.setter
    def viewedOn(self, value):
        self._viewedOn = self._check_str(
            value, 'ViewedOn has to be a str or RemoveValue.', True)

    @property
    def rejectedOn(self):
        return self._rejectedOn

    @rejectedOn.setter
    def rejectedOn(self, value):
        self._rejectedOn = self._check_str(
            value, 'RejectedOn has to be a str or RemoveValue.', True)

    @property
    def inProcessOn(self):
        return self._inProcessOn

    @inProcessOn.setter
    def inProcessOn(self, value):
        self._inProcessOn = self._check_str(
            value, 'InProcessOn has to be a str or RemoveValue.', True)

    @property
    def pendingOn(self):
        return self._pendingOn

    @pendingOn.setter
    def pendingOn(self, value):
        self._pendingOn = self._check_str(
            value, 'PendingOn has to be a str or RemoveValue.', True)

    @property
    def readyForDispatchOn(self):
        return self._readyForDispatchOn

    @readyForDispatchOn.setter
    def readyForDispatchOn(self, value):
        self._readyForDispatchOn = self._check_str(
            value, 'ReadyForDispatchOn has to be a str or RemoveValue.', True)

    @property
    def partiallyDispatchedOn(self):
        return self._partiallyDispatchedOn

    @partiallyDispatchedOn.setter
    def partiallyDispatchedOn(self, value):
        self._partiallyDispatchedOn = self._check_str(
            value, 'PartiallyDispatchedOn has to be a str or RemoveValue', True)

    @property
    def dispatchedOn(self):
        return self._dispatchedOn

    @dispatchedOn.setter
    def dispatchedOn(self, value):
        self._dispatchedOn = self._check_str(
            value, 'DispatchedOn has to be a str or RemoveValue.', True)

    @property
    def deliveredOn(self):
        return self._deliveredOn

    @deliveredOn.setter
    def deliveredOn(self, value):
        self._deliveredOn = self._check_str(
            value, 'DeliveredOn has to be a str or RemoveValue.', True)

    @property
    def partiallyInvoicedOn(self):
        return self._partiallyInvoicedOn

    @partiallyInvoicedOn.setter
    def partiallyInvoicedOn(self, value):
        self._partiallyInvoicedOn = self._check_str(
            value, 'PartiallyInvoicedOn has to be a str or RemoveValue.', True)

    @property
    def invoicedOn(self):
        return self._invoicedOn

    @invoicedOn.setter
    def invoicedOn(self, value):
        self._invoicedOn = self._check_str(
            value, 'InvoicedOn has to be a str or RemoveValue.', True)

    @property
    def partiallyPaidOn(self):
        return self._partiallyPaidOn

    @partiallyPaidOn.setter
    def partiallyPaidOn(self, value):
        self._partiallyPaidOn = self._check_str(
            value, 'PartiallyPaidOn has to be a str or RemoveValue.', True)

    @property
    def paidOn(self):
        return self._paidOn

    @paidOn.setter
    def paidOn(self, value):
        self._paidOn = self._check_str(
            value, 'PaidOn has to be a str or RemoveValue.', True)

    @property
    def returnedOn(self):
        return self._returnedOn

    @returnedOn.setter
    def returnedOn(self, value):
        self._returnedOn = self._check_str(
            value, 'ReturnedOn has to be a str or RemoveValue.', True)

    @property
    def closedOn(self):
        return self._closedOn

    @closedOn.setter
    def closedOn(self, value):
        self._closedOn = self._check_str(
            value, 'ClosedOn has to be a str or RemoveValue.', True)

    @property
    def archivedOn(self):
        return self._archivedOn

    @archivedOn.setter
    def archivedOn(self, value):
        self._archivedOn = self._check_str(
            value, 'ArchivedOn has to be a str or RemoveValue.', True)

    def is_valid(self):
        return True

    def get_patch(self):
        return self.get_list_of_json_patches(self.legals)
