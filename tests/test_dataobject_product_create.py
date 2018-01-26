# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""Tests for `epages_client.dataobjects.product` package."""
import unittest

# import the package
import epages_client

from epages_client.dataobjects.product_create import ProductCreate

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def setUp(self):
        self.product = ProductCreate()

    def test_0001_correct_inputs(self):

        # product_number missing
        self.assertEqual(self.product.is_valid(), False)

        self.product.productNumber = "ZZZ-ZZZ-2"
        self.assertEqual(self.product.productNumber, "ZZZ-ZZZ-2")

        # product_number set
        self.assertEqual(self.product.is_valid(), True)

        self.product.name = "product 1"
        self.assertEqual(self.product.name, "product 1")

        self.product.shortDescription = "A nice product"
        self.assertEqual(self.product.shortDescription, "A nice product")

        self.product.description = "Very nice and cool product"
        self.assertEqual(self.product.description,
                         "Very nice and cool product")

        self.product.manufacturer = "Busines Oy"
        self.assertEqual(self.product.manufacturer, "Busines Oy")

        self.product.price = 2
        self.assertEqual(self.product.price, 2)

        self.product.price = 2.30
        self.assertEqual(self.product.price, 2.30)

        self.product.essentialFeatures = "Jump and speak"
        self.assertEqual(self.product.essentialFeatures, "Jump and speak")

        self.product.upc = '614141000036'
        self.assertEqual(self.product.upc, '614141000036')

        self.product.ean = '9501101530003'
        self.assertEqual(self.product.ean, '9501101530003')

        self.product.deliveryPeriod = '1 day'
        self.assertEqual(self.product.deliveryPeriod, '1 day')

        self.product.visible = True
        self.assertEqual(self.product.visible, True)

        self.product.taxClassId = '2'
        self.assertEqual(self.product.taxClassId, '2')

        self.product.stocklevel = 1000
        self.assertEqual(self.product.stocklevel, 1000)

        self.product.depositPrice = 0.49
        self.assertEqual(self.product.depositPrice, 0.49)

        self.product.manufacturerPrice = 5.99
        self.assertEqual(self.product.manufacturerPrice, 5.99)

        self.product.searchKeywords.add('cat')
        self.product.searchKeywords.add('doc')
        self.assertEqual(self.product.searchKeywords.get(), ['cat', 'doc'])

        self.assertEqual(self.product.get_dict(), {'taxClassId': '2', 'shortDescription': 'A nice product', 'price': 2.3, 'essentialFeatures': 'Jump and speak', 'visible': True, 'depositPrice': 0.49, 'stocklevel': 1000, 'manufacturer': 'Busines Oy', 'searchKeywords': [
                         'cat', 'doc'], 'manufacturerPrice': 5.99, 'productNumber': 'ZZZ-ZZZ-2', 'upc': '614141000036', 'ean': '9501101530003', 'name': 'product 1', 'deliveryPeriod': '1 day', 'description': 'Very nice and cool product'})

    def test_0002_invalid_inputs(self):
        product = ProductCreate()

        with self.assertRaises(TypeError) as e:
            product.price = '2.20 €'

        with self.assertRaises(TypeError) as e:
            product.visible = 'True'

        with self.assertRaises(TypeError) as e:
            product.stocklevel = '2000 pcs.'

        with self.assertRaises(TypeError) as e:
            product.depositPrice = 5, 59

        with self.assertRaises(TypeError) as e:
            product.manufacturerPrice = '1.85'

        self.assertEqual(product.get_dict(), {})
        self.assertEqual(product.is_valid(), False)


if __name__ == '__main__':
    unittest.main()
