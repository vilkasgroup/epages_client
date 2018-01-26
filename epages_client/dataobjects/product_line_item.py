# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject
from .list_of_objects import ListOfObjects
from .quantity import Quantity
from .price import Price
from .tax_class_info import TaxClassInfo
from .delivery_weight_quantity import DeliveryWeightQuantity
from .image import Image
from .link import Link


class ProductLineItem(DataObject):
    """Data object for ProductLineItem"""

    def __init__(self):
        # string The unique identifier of the line item.
        self._lineItemId = None
        # string The stock keeping unit (SKU) corresponding to the line item.
        self._sku = None
        # string The name of the line item.
        self._name = None
        # string The unique identifier of the product.
        self._productId = None
        # object of quantity The quantity of the line item.
        self.quantity = Quantity()
        # object of price The price of the line item.
        self.lineItemPrice = Price()
        # object of price The price for a single item.
        self.singleItemPrice = Price()
        # string The essential features of the line item.
        self._essentialFeatures = None
        # array of image The image of the line item.
        self.images = ListOfObjects(Image)
        # array of link The links to the product line item.
        self.links = ListOfObjects(Link)
        # object of taxClassInfo The tax that applies for the product.
        self.taxClass = TaxClassInfo()
        # object of deliveryWeightQuantity The delivery weight of the product line item.
        self.deliveryWeight = DeliveryWeightQuantity()
        # string The description of the selected variation.
        self._variationString = None

    @property
    def lineItemId(self):
        return self._lineItemId

    @lineItemId.setter
    def lineItemId(self, value):
        self._lineItemId = self._check_str(value)

    @property
    def sku(self):
        return self._sku

    @sku.setter
    def sku(self, value):
        self._sku = self._check_str(value)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._check_str(value)

    @property
    def productId(self):
        return self._productId

    @productId.setter
    def productId(self, value):
        self._productId = self._check_str(value)

    @property
    def essentialFeatures(self):
        return self._essentialFeatures

    @essentialFeatures.setter
    def essentialFeatures(self, value):
        self._essentialFeatures = self._check_str(value)

    @property
    def variationString(self):
        return self._variationString

    @variationString.setter
    def variationString(self, value):
        self._variationString = self._check_str(value)

    def is_valid(self):
        return all(
            self.quantity.is_valid(),
            self.lineItemPrice.is_valid(),
            self.singleItemPrice.is_valid(),
            self.images.is_valid(),
            self.links.is_valid(),
            self.taxClass.is_valid(),
            self.deliveryWeight.is_valid()
        )
