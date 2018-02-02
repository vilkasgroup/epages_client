# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""Tests for `epages_client.dataobjects.product_create` package."""
import unittest

# import the package
import epages_client

from epages_client.dataobjects.product_update import ProductUpdate
from epages_client.dataobjects.remove_value import RemoveValue

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def setUp(self):
        pass

    def test_1001_correct_inputs(self):
        product = ProductUpdate()

        product.productNumber = "prod_1"
        self.assertEqual(product.productNumber, "prod_1")

        product.name = "Deddy Bear"
        self.assertEqual(product.name, "Deddy Bear")

        product.shortDescription = "Soft Deddy Bear"
        self.assertEqual(product.shortDescription, "Soft Deddy Bear")

        product.description = "Tom’s 18″ Teddy Bear"
        self.assertEqual(product.description, "Tom’s 18″ Teddy Bear")

        product.manufacturer = "Christopher Robin"
        self.assertEqual(product.manufacturer, "Christopher Robin")

        product.upc = "9501101530003"
        self.assertEqual(product.upc, "9501101530003")

        product.ean = "0012345678905"
        self.assertEqual(product.ean, "0012345678905")

        product.essentialFeatures = "yellow eyes"
        self.assertEqual(product.essentialFeatures, "yellow eyes")

        product.price = 29.99
        self.assertEqual(product.price, 29.99)

        product.manufacturerPrice = 49.90
        self.assertEqual(product.manufacturerPrice, 49.90)

        product.depositPrice = 0.00
        self.assertEqual(product.depositPrice, 0.00)

        product.deliveryPeriod = "5 days"
        self.assertEqual(product.deliveryPeriod, "5 days")

        product.minStocklevel = 6
        self.assertEqual(product.minStocklevel, 6)

        product.manufacturerProductNumber = "00000001ZDEDDY"
        self.assertEqual(product.manufacturerProductNumber, "00000001ZDEDDY")

        product.productLength = 50
        self.assertEqual(product.productLength, 50)

        product.productWidth = 60
        self.assertEqual(product.productWidth, 60)

        product.productHeight = 457
        self.assertEqual(product.productHeight, 457)

        product.taxClassId = "tax01"
        self.assertEqual(product.taxClassId, "tax01")

        product.productImage = "teddy0001_big.jpg"
        self.assertEqual(product.productImage, "teddy0001_big.jpg")

        product.stocklevel = 5
        self.assertEqual(product.stocklevel, 5)

        product.visible = True
        self.assertEqual(product.visible, True)

        product.searchKeywords.add('deddy')
        self.assertEqual(product.searchKeywords.get(), ['deddy'])

        product.searchKeywords.add('toy')
        self.assertEqual(product.searchKeywords.get(), ['deddy', 'toy'])

        patch_values = [
            {'op': 'replace', 'path': '/priceInfo/taxClass/taxClassId', 'value': 'tax01'},
            {'op': 'add', 'path': '/visible', 'value': True},
            {'op': 'add', 'path': '/productNumber', 'value': 'prod_1'},
            {'op': 'add', 'path': '/productImage', 'value': 'teddy0001_big.jpg'},
            {'op': 'add', 'path': '/deliveryPeriod', 'value': '5 days'},
            {'op': 'add', 'path': '/essentialFeatures', 'value': 'yellow eyes'},
            {'op': 'add', 'path': '/description', 'value': 'Tom’s 18″ Teddy Bear'},
            {'op': 'add', 'path': '/shortDescription', 'value': 'Soft Deddy Bear'},
            {'op': 'add', 'path': '/productWidth', 'value': 60},
            {'op': 'add', 'path': '/upc', 'value': '9501101530003'},
            {'op': 'add', 'path': '/searchKeywords',
                'value': ['deddy', 'toy']},
            {'op': 'add', 'path': '/priceInfo/manufacturerPrice/amount', 'value': 49.9},
            {'op': 'add', 'path': '/manufacturerProductNumber',
                'value': '00000001ZDEDDY'},
            {'op': 'add', 'path': '/priceInfo/price/amount', 'value': 29.99},
            {'op': 'add', 'path': '/productLength', 'value': 50},
            {'op': 'add', 'path': '/name', 'value': 'Deddy Bear'},
            {'op': 'add', 'path': '/manufacturer', 'value': 'Christopher Robin'},
            {'op': 'add', 'path': '/ean', 'value': '0012345678905'},
            {'op': 'add', 'path': '/priceInfo/depositPrice/amount', 'value': 0.0},
            {'op': 'add', 'path': '/stocklevel', 'value': 5},
            {'op': 'add', 'path': '/productHeight', 'value': 457},
            {'op': 'add', 'path': '/minStocklevel', 'value': 6}
        ]

        self.assert_count_items_equal(product.get_patch(), patch_values)

    def test_1201_correct_removes(self):
        product = ProductUpdate()
        product.name = RemoveValue()

        # test str
        patch_value = [{'op': 'remove', 'path': '/name'}]
        self.assert_count_items_equal(product.get_patch(), patch_value)

        # test numeric
        product.minStocklevel = RemoveValue()
        patch_value = [{'op': 'remove', 'path': '/name'},
                       {'op': 'remove', 'path': '/minStocklevel'}]
        self.assert_count_items_equal(product.get_patch(), patch_value)

        # ListOfObject - user overwrites when he/she wants to remove values
        product.searchKeywords = RemoveValue()
        self.assertIsInstance(product.searchKeywords, RemoveValue)
        patch_value = [{'op': 'remove', 'path': '/name'}, {'op': 'remove',
                                                           'path': '/minStocklevel'}, {'op': 'remove', 'path': "/searchKeywords"}]
        self.assert_count_items_equal(product.get_patch(), patch_value)

    def test_2000_invalid_inputs(self):
        product = ProductUpdate()

        with self.assertRaises(TypeError) as e:
            product.price = "12.21 €"

        with self.assertRaises(TypeError) as e:
            product.visible = "True"


if __name__ == '__main__':
    unittest.main()
