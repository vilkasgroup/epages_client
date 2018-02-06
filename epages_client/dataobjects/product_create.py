# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from six import string_types
from .data_object import DataObject
from .list_of_objects import ListOfObjects


class ProductCreate(DataObject):
    ''''Data object for create a new product to ePages webshop'''

    def __init__(self):
        # string The product number (mandatory).
        self._productNumber = None
        # string The name of the product.
        self._name = None
        # string The short description of the product.
        self._shortDescription = None
        # string The description of the product.
        self._description = None
        # string The manufacturer of the product.
        self._manufacturer = None
        # number The price of the product.
        self._price = None
        # string The essential features of the product.
        self._essentialFeatures = None
        # string The Universal Product Code of the product.
        self._upc = None
        # string The European Article Number of the product, either EAN-8 or EAN-13.
        self._ean = None
        # string The average time of the product being delivered to the customer. By default, the delivery period is displayed in days, but this can be changed by the merchant.
        self._deliveryPeriod = None
        # array of string The search terms for the product determined by the merchant in the administration.
        self.searchKeywords = ListOfObjects(string_types)
        # boolean Indicates if the product is displayed in the shop.
        self._visible = None
        # string The unique identifier of the tax class.
        self._taxClassId = None
        # number Indicates the stock level of the product.
        self._stocklevel = None
        # number The deposit price for the product, e.g. bottle deposit.
        self._depositPrice = None
        # number The sales price recommended by the manufacturer.
        self._manufacturerPrice = None

    @property
    def productNumber(self):
        return self._productNumber

    @productNumber.setter
    def productNumber(self, value):
        self._productNumber = self._check_str(
            value, "ProductNumber has to be a str.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._check_str(value, "Name has to be a str.")

    @property
    def shortDescription(self):
        return self._shortDescription

    @shortDescription.setter
    def shortDescription(self, value):
        self._shortDescription = self._check_str(
            value, "ShortDescription has to be a str.")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = self._check_str(value, "Description has to be a str.")

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = self._check_str(value, "Manufacturer has to be a str.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = self._check_numeric(
            value, "Price has to be a numeric type.")

    @property
    def essentialFeatures(self):
        return self._essentialFeatures

    @essentialFeatures.setter
    def essentialFeatures(self, value):
        self._essentialFeatures = self._check_str(value, "EssentialFeatures has to be a str.")

    @property
    def upc(self):
        return self._upc

    @upc.setter
    def upc(self, value):
        self._upc = self._check_str(value, "Upc has to be a str.")

    @property
    def ean(self):
        return self._ean

    @ean.setter
    def ean(self, value):
        self._ean = self._check_str(value, 'Ean has to be a str.')

    @property
    def deliveryPeriod(self):
        return self._deliveryPeriod

    @deliveryPeriod.setter
    def deliveryPeriod(self, value):
        self._deliveryPeriod = self._check_str(value, 'DeliveryPeriod has to be a str.')

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = self._check_bool(value, 'Visible has to be a bool type.')

    @property
    def taxClassId(self):
        return self._taxClassId

    @taxClassId.setter
    def taxClassId(self, value):
        self._taxClassId = self._check_str(value, 'TaxClassId has to be a str.')

    @property
    def stocklevel(self):
        return self._stocklevel

    @stocklevel.setter
    def stocklevel(self, value):
        self._stocklevel = self._check_numeric(
            value, 'Stocklevel has to be a numeric type.')

    @property
    def depositPrice(self):
        return self._depositPrice

    @depositPrice.setter
    def depositPrice(self, value):
        self._depositPrice = self._check_numeric(
            value, 'DepositPrice has to be a numeric type.')

    @property
    def manufacturerPrice(self):
        return self._manufacturerPrice

    @manufacturerPrice.setter
    def manufacturerPrice(self, value):
        self._manufacturerPrice = self._check_numeric(
            value, 'Stocklevel has to be a numeric type.')

    def is_valid(self):
        ''' Have all mandatory values set?
        '''
        return self._productNumber != None and self.searchKeywords.is_valid()
