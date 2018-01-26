# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from six import string_types
from .data_object import DataObject
from .list_of_objects import ListOfObjects
from .price import Price


class CouponLineItem(DataObject):
    '''Data object for creating a coupon line to ePages webshop'''

    def __init__(self):
        # string The unique identifier of the coupon line item.
        self._couponLineItemId = None
        # string The unique identifier of the campaign the coupon belongs to.
        self._couponCampaignId = None
        # object of price The price of the line item.
        self.lineItemPrice = Price()
        # array of error strings The error that occurred when redeeming a coupon for this cart. Can be one of LineItemsSubTotalTooSmall, CouponIsInvalidated, ValidCouponCountReached, CouponNotEffective, PaymentMethodMisMatch, ShippingMethodMisMatch, ProductMisMatch.
        self.validationErrors = ListOfObjects(string_types)

    @property
    def couponLineItemId(self):
        return self._couponLineItemId

    @couponLineItemId.setter
    def couponLineItemId(self, value):
        self._couponLineItemId = self._check_str(value)

    @property
    def couponCampaignId(self):
        return self._couponCampaignId

    @couponCampaignId.setter
    def couponCampaignId(self, value):
        self._couponCampaignId = self._check_str(value)

    def is_valid(self):
        return self.lineItemPrice.is_valid() and self.validationErrors.is_valid()
