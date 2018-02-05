# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from six import string_types
from .data_object import DataObject
from .enum_fetch_operator import FetchOperator
from .list_of_objects import ListOfObjects
from .remove_value import RemoveValue


class ProductUpdate(DataObject):
    """Data object for updating a product"""

    def __init__(self):
        # Initialize product fields, when patching product.
        # Underscores in the middle of the variable name are replaced with slash "/"

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
        # string The Universal Product Code of the product.
        self._upc = None
        # string The European Article Number of the product, either EAN-8 or EAN-13.
        self._ean = None
        # string The essential features of the product.
        self._essentialFeatures = None
        # array of string The search terms for the product determined by the merchant in the administration.
        self.searchKeywords = ListOfObjects(string_types)
        # number The price of the product.
        self._priceInfo_price_amount = None
        # number The original price, if product own price is discounted
        self._priceInfo_manufacturerPrice_amount = None
        # number The deposit price for the product, e.g. bottle deposit.
        self._priceInfo_depositPrice_amount = None
        # string The average time of the product being delivered to the customer. By default, the delivery period is displayed in days, but this can be changed by the merchant.
        self._deliveryPeriod = None
        # number Indicates the minimum stock level of the product.
        self._minStocklevel = None
        # string The unique manufacturer identifier of the product.
        self._manufacturerProductNumber = None
        # number The length of the product in mm.
        self._productLength = None
        # number The width of the product in mm.
        self._productWidth = None
        # number The height of the product in mm.
        self._productHeight = None
        # string The unique identifier of the tax class.
        self._priceInfo_taxClass_taxClassId = None
        # string The name of the product image.
        self._productImage = None
        # number Indicates the stock level of the product.
        self._stocklevel = None
        # boolean Indicates if the product is displayed in the shop.
        self._visible = None

        # Available operations for fields
        self.legals = {
            '/productNumber': (FetchOperator.ADD,),
            '/name': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/shortDescription': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/description': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/manufacturer': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/upc': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/ean': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/essentialFeatures': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/searchKeywords': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/priceInfo/price/amount': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/priceInfo/manufacturerPrice/amount': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/priceInfo/depositPrice/amount': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/deliveryPeriod': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/minStocklevel': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/manufacturerProductNumber': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/productLength': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/productWidth': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/productHeight': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/priceInfo/taxClass/taxClassId': (FetchOperator.REMOVE, FetchOperator.REPLACE),
            '/productImage': (FetchOperator.ADD,),
            '/stocklevel': (FetchOperator.ADD, FetchOperator.REMOVE),
            '/visible': (FetchOperator.ADD,),
        }

    @property
    def productNumber(self):
        return self._productNumber

    @productNumber.setter
    def productNumber(self, value):
        self._productNumber = self._check_str(
            value, "ProductId has to be a str.", False)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._check_str(
            value, "Name has to be a str or RemoveValue.", True)

    @property
    def shortDescription(self):
        return self._shortDescription

    @shortDescription.setter
    def shortDescription(self, value):
        self._shortDescription = self._check_str(
            value, "ShortDescription has to be a str or RemoveValue.", True)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = self._check_str(
            value, "Description has to be a str or RemoveValue.", True)

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = self._check_str(
            value, "Manufacturer has to be a str or RemoveValue.", True)

    @property
    def upc(self):
        return self._upc

    @upc.setter
    def upc(self, value):
        self._upc = self._check_str(
            value, "Upc has to be a str or RemoveValue.", True)

    @property
    def ean(self):
        return self._ean

    @ean.setter
    def ean(self, value):
        self._ean = self._check_str(
            value, "Ean has to be a str or RemoveValue.", True)

    @property
    def essentialFeatures(self):
        return self._essentialFeatures

    @essentialFeatures.setter
    def essentialFeatures(self, value):
        self._essentialFeatures = self._check_str(
            value, "EssentialFeatures has to be a str or RemoveValue.", True)

    @property
    def price(self):
        return self._priceInfo_price_amount

    @price.setter
    def price(self, value):
        self._priceInfo_price_amount = self._check_numeric(
            value, 'Price has to be a numeric type or RemoveValue.', True)

    @property
    def manufacturerPrice(self):
        return self._priceInfo_manufacturerPrice_amount

    @manufacturerPrice.setter
    def manufacturerPrice(self, value):
        self._priceInfo_manufacturerPrice_amount = self._check_numeric(
            value, 'Manufacturer price has to be a numeric type or RemoveValue.', True)

    @property
    def depositPrice(self):
        return self._priceInfo_depositPrice_amount

    @depositPrice.setter
    def depositPrice(self, value):
        self._priceInfo_depositPrice_amount = self._check_numeric(
            value, 'DepositPrice has to be a numeric type or RemoveValue.', True)

    @property
    def deliveryPeriod(self):
        return self._deliveryPeriod

    @deliveryPeriod.setter
    def deliveryPeriod(self, value):
        self._deliveryPeriod = self._check_str(
            value, "DeliveryPeriod has to be a str or RemoveValue.", True)

    @property
    def minStocklevel(self):
        return self._minStocklevel

    @minStocklevel.setter
    def minStocklevel(self, value):
        self._minStocklevel = self._check_numeric(
            value, 'Minimum stocklevel has to be a numeric type or RemoveValue.', True)

    @property
    def manufacturerProductNumber(self):
        return self._manufacturerProductNumber

    @manufacturerProductNumber.setter
    def manufacturerProductNumber(self, value):
        self._manufacturerProductNumber = self._check_str(
            value, 'ManufacturerProductNumber has to be a str or RemoveValue.', True)

    @property
    def productLength(self):
        return self._productLength

    @productLength.setter
    def productLength(self, value):
        self._productLength = self._check_numeric(
            value, 'Product length has to be a numeric type or RemoveValue.', True)

    @property
    def productWidth(self):
        return self._productWidth

    @productWidth.setter
    def productWidth(self, value):
        self._productWidth = self._check_numeric(
            value, 'Product width has to be a numeric type or RemoveValue.', True)

    @property
    def productHeight(self):
        return self._productHeight

    @productHeight.setter
    def productHeight(self, value):
        self._productHeight = self._check_numeric(
            value, 'Product height has to be a numeric type or RemoveValue.', True)

    @property
    def taxClassId(self):
        return self._priceInfo_taxClass_taxClassId

    @taxClassId.setter
    def taxClassId(self, value):
        self._priceInfo_taxClass_taxClassId = self._check_str(
            value, 'TaxClassId has to be a numeric type or RemoveValue.', True)

    @property
    def productImage(self):
        return self._productImage

    @productImage.setter
    def productImage(self, value):
        self._productImage = self._check_str(
            value, "ProductImage has to be a str.", False)

    @property
    def stocklevel(self):
        return self._stocklevel

    @stocklevel.setter
    def stocklevel(self, value):
        self._stocklevel = self._check_numeric(
            value, 'Stocklevel has to be a numeric type or RemoveValue.', True)

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = self._check_bool(
            value, 'Visible has to be a bool.', False)

    def get_patch(self):
        return self.get_list_of_json_patches(self.legals)

    def is_valid(self):
        return self.searchKeywords.is_valid()
