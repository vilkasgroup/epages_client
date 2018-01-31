# -*- coding: utf-8 -*-
import unittest
from pprint import pprint

# import the package
import epages_client

# import the RestClient class
from epages_client.client import RestClient

from epages_client.dataobjects.cart_create import CartCreate
from epages_client.dataobjects.product_line_item_create import ProductLineItemCreate

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestProductMethods(BaseUnitTest):
    '''A class for testing dataobject CartCreate'''

    def setUp(self):
        self.cart = CartCreate()

    def test_001_set_basic_data(self):

        self.cart.currency = 'EUR'
        self.cart.taxType = 'NET'
        self.cart.locale = 'fi_fi'

        right_answer = {
            'currency': 'EUR',
            'taxType': 'NET',
            'locale': 'fi_fi'
        }

        self.assertEqual(self.cart.get_dict(), right_answer)

    def test_002_add_Products(self):

        self.cart.currency = 'EUR'
        self.cart.taxType = 'NET'
        self.cart.locale = 'fi_fi'

        product = ProductLineItemCreate()
        product.productId = '00001Z'
        product.quantity = 5
        self.cart.lineItems.add(product)

        right_answer = {
            'currency': 'EUR',
            'taxType': 'NET',
            'locale': 'fi_fi',
            'lineItems': [
                {
                    'productId': '00001Z',
                    'quantity': 5
                }
            ]
        }

        self.assertEqual(self.cart.get_dict(), right_answer)

    def test_003_invalid_input_to_lineItems(self):
        with self.assertRaises(TypeError) as e:
            self.cart.lineItems.add('Product One')

    def tearDown(self):
        pass
