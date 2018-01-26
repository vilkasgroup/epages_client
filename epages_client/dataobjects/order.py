# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject
from .address import Address
from .shipping_data import ShippingData
from .payment_data import PaymentData
from .line_item_container import LineItemContainer
from .price import Price
from .link import Link
from .list_of_objects import ListOfObjects


class Order(DataObject):
    ''''Data object for create a new order to ePages webshop'''

    def __init__(self):
        # string The unique identifier of the order.
        self._orderId = None
        # string The type of the order document. Can be Invoice or CreditNote.
        self._documentType = None
        # string The number of the order document.
        self._documentNumber = None
        # string The order number.
        self._orderNumber = None
        # string The date/time of order placement. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._creationDate = None
        # address The billing address for the order.
        self.billingAddress = Address()
        # address The shipping address for the order.
        self.shippingAddress = Address()
        # string The date/time the order was invoiced. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._invoicedOn = None
        # string The date/time a part of the order was paid. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._partiallyPaidOn = None
        # string The date/time the order was delivered. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._deliveredOn = None
        # string The date/time a part of the order was invoiced. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._partiallyInvoicedOn = None
        # string The date/time the order was set to pending. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._pendingOn = None
        # string The date/time the order was prepared for dispatching. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._readyForDispatchOn = None
        # string The date/time a part of the order was dispatched. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._partiallyDispatchedOn = None
        # string The date/time the order was archived. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._archivedOn = None
        # string The date/time the order was dispatched. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._dispatchedOn = None
        # string The date/time the order was viewed. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._viewedOn = None
        # string The unique identifier of the customer.
        self._customerId = None
        # string The number by which the merchant tracks the customer.
        self._customerNumber = None
        # string The locale that identifies the origin of the customer.
        self._locale = None
        # string The unique identifier of the currency used for payment.
        self._currencyId = None
        # string The taxmodel that applies for the order, e.g. gross.
        self._taxModel = None
        # string The total cost of the order.
        self._grandTotal = None
        # string The total cost of the order before tax is applied.
        self._totalBeforeTax = None
        # string Internal notes for the order done by the merchant.
        self._internalNote = None
        # string Notes on the order from the customer. Can also be amended by the merchant in the administration. Mainly used for order and delivery notes.
        self._customerComment = None
        # string The date/time the order was rejected. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._rejectedOn = None
        # string The date/time the order was put into process. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._inProcessOn = None
        # string The date/time the order was closed. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._closedOn = None
        # string The date/time the order was paid. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._paidOn = None
        # string The date/time the order was returned. Expressed according to ISO 8601. Example: 2015-11-04T08:42:49.000Z
        self._returnedOn = None
        # object of shippingData The shipping data of a cart or an order, i.e. short info on shipping method and price.
        self.shippingData = ShippingData()
        # object of paymentData The payment data of a cart or an order, i.e. short info on payment method and price.
        self.paymentData = PaymentData()
        # lineItemContainer Contains the line items of an order. Only included in GET/orders/{orderId}.
        self.lineItemContainer = LineItemContainer()
        # object of price The shipping price for the order.
        self.shippingPrice = Price()
        # array of link The links to the products of the order.
        self.links = ListOfObjects(Link)

        @property
        def orderId(self):
            return self._orderId

        @orderId.setter
        def orderId(self, value):
            self._orderId = self._check_str(value)

        @property
        def documentType(self):
            return self._documentType

        @documentType.setter
        def documentType(self, value):
            self._documentType = self._check_str(value)

        @property
        def documentNumber(self):
            return self._documentNumber

        @documentNumber.setter
        def documentNumber(self, value):
            self._documentNumber = self._check_str(value)

        @property
        def orderNumber(self):
            return self._orderNumber

        @orderNumber.setter
        def orderNumber(self, value):
            self._orderNumber = self._check_str(value)

        @property
        def creationDate(self):
            return self._creationDate

        @creationDate.setter
        def creationDate(self, value):
            self._creationDate = self._check_str(value)

        @property
        def invoicedOn(self):
            return self._invoicedOn

        @invoicedOn.setter
        def invoicedOn(self, value):
            self._invoicedOn = self._check_str(value)

        @property
        def partiallyPaidOn(self):
            return self._partiallyPaidOn

        @partiallyPaidOn.setter
        def partiallyPaidOn(self, value):
            self._partiallyPaidOn = self._check_str(value)

        @property
        def deliveredOn(self):
            return self._deliveredOn

        @deliveredOn.setter
        def deliveredOn(self, value):
            self._deliveredOn = self._check_str(value)

        @property
        def partiallyInvoicedOn(self):
            return self._partiallyInvoicedOn

        @partiallyInvoicedOn.setter
        def partiallyInvoicedOn(self, value):
            self._partiallyInvoicedOn = self._check_str(value)

        @property
        def pendingOn(self):
            return self._pendingOn

        @pendingOn.setter
        def pendingOn(self, value):
            self._pendingOn = self._check_str(value)

        @property
        def readyForDispatchOn(self):
            return self._readyForDispatchOn

        @readyForDispatchOn.setter
        def readyForDispatchOn(self, value):
            self._readyForDispatchOn = self._check_str(value)

        @property
        def partiallyDispatchedOn(self):
            return self._partiallyDispatchedOn

        @partiallyDispatchedOn.setter
        def partiallyDispatchedOn(self, value):
            self._partiallyDispatchedOn = self._check_str(value)

        @property
        def archivedOn(self):
            return self._archivedOn

        @archivedOn.setter
        def archivedOn(self, value):
            self._archivedOn = self._check_str(value)

        @property
        def dispatchedOn(self):
            return self._dispatchedOn

        @dispatchedOn.setter
        def dispatchedOn(self, value):
            self._dispatchedOn = self._check_str(value)

        @property
        def viewedOn(self):
            return self._viewedOn

        @viewedOn.setter
        def viewedOn(self, value):
            self._viewedOn = self._check_str(value)

        @property
        def customerId(self):
            return self._customerId

        @customerId.setter
        def customerId(self, value):
            self._customerId = self._check_str(value)

        @property
        def customerNumber(self):
            return self._customerNumber

        @customerNumber.setter
        def customerNumber(self, value):
            self._customerNumber = self._check_str(value)

        @property
        def locale(self):
            return self._locale

        @locale.setter
        def locale(self, value):
            self._locale = self._check_str(value)

        @property
        def currencyId(self):
            return self._currencyId

        @currencyId.setter
        def currencyId(self, value):
            self._currencyId = self._check_str(value)

        @property
        def taxModel(self):
            return self._taxModel

        @taxModel.setter
        def taxModel(self, value):
            self._taxModel = self._check_str(value)

        @property
        def grandTotal(self):
            return self._grandTotal

        @grandTotal.setter
        def grandTotal(self, value):
            self._grandTotal = self._check_str(value)

        @property
        def totalBeforeTax(self):
            return self._totalBeforeTax

        @totalBeforeTax.setter
        def totalBeforeTax(self, value):
            self._totalBeforeTax = self._check_str(value)

        @property
        def internalNote(self):
            return self._internalNote

        @internalNote.setter
        def internalNote(self, value):
            self._internalNote = self._check_str(value)

        @property
        def customerComment(self):
            return self._customerComment

        @customerComment.setter
        def customerComment(self, value):
            self._customerComment = self._check_str(value)

        @property
        def rejectedOn(self):
            return self._rejectedOn

        @rejectedOn.setter
        def rejectedOn(self, value):
            self._rejectedOn = self._check_str(value)

        @property
        def inProcessOn(self):
            return self._inProcessOn

        @inProcessOn.setter
        def inProcessOn(self, value):
            self._inProcessOn = self._check_str(value)

        @property
        def closedOn(self):
            return self._closedOn

        @closedOn.setter
        def closedOn(self, value):
            self._closedOn = self._check_str(value)

        @property
        def paidOn(self):
            return self._paidOn

        @paidOn.setter
        def paidOn(self, value):
            self._paidOn = self._check_str(value)

        @property
        def returnedOn(self):
            return self._returnedOn

        @returnedOn.setter
        def returnedOn(self, value):
            self._returnedOn = self._check_str(value)

        @property
        def shippingPrice(self):
            return self._shippingPrice

        def is_valid(self):
            return all(
                self.billingAddress.is_valid(),
                self.shippingAddress.is_valid(),
                self.shippingData.is_valid(),
                self.paymentData.is_valid(),
                self.lineItemContainer.is_valid(),
                self.shippingPrice.is_valid(),
                self.links.is_valid()
            )
