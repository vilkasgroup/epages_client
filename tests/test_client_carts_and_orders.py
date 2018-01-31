# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import time
import uuid
from pprint import pprint

# import base class for unit testing
from .base_unit_test import BaseUnitTest

# import the package
import epages_client

# import the RestClient class
from epages_client.client import RestClient

# import Dataobjects
from epages_client.dataobjects.cart_create import CartCreate
from epages_client.dataobjects.product_line_item_create import ProductLineItemCreate


class TestCartsOrdersAndOrdersMethods(BaseUnitTest):
    '''A class for testing order related methods on RestClient class'''

    # filename for saving cart credential
    cart_file = "cart_credential.csv"

    # filename for saving couponLineItemId
    coupon_line_file = "cart_coupon_line.txt"

    # filename for saving lineItemId
    product_line_file = "cart_product_line_item_id.txt"

    # Code for a coupon
    coupun_code = 'TEST-CODE-ABC123'

    def add_cart_credential(self, params):
        '''This function adds cart token and cart id to params from csv file.'''

        content = self.get_resource(self.cart_file)

        ids = content.split(";")

        params.update({
            'param1': ids[0],
            'headers': {'X-ePages-Cart-Token': ids[1]}
        })

        return params

    def save_cart_credential(self, response):
        '''Function to save cart token and cart_id to csv-file'''

        content = "%s;%s" % (
            response['X-ePages-Cart-Token'], response['cartId'])

        self.save_resource(self.cart_file, content)

    def get_first_product(self):
        products = self.client.get_products({
            "query": {},
            "param1": "",
            "param2": ""
        })
        return products['items'][0]

    def setUp(self):

        self.client = RestClient(
            os.environ["EPAGES_API_URL"], os.environ["EPAGES_API_TOKEN"])

        self.params = {
            "query": {},
            "param1": "",
            "param2": ""
        }

    def test_0001_create_cart(self):
        # create a cart
        cart = CartCreate()
        cart.currency = 'EUR'
        cart.locale = 'fi_fi'
        cart.taxType = 'NET'

        # Add a product to the cart
        line = ProductLineItemCreate()
        line.productId = self.get_first_product()['productId']
        line.quantity = 1
        cart.lineItems.add(line)

        self.params["object"] = cart

        response = self.client.add_cart(self.params)
        self.assertEqual(isinstance(response, dict), True)

    def test_0002_create_empty_cart(self):
        # Create a cart without products

        # Create a new cart
        cart = CartCreate()
        self.params["object"] = cart
        response = self.client.add_cart(self.params)
        self.assertEqual(isinstance(response, dict), True)

        # Save cartId credentials to csv file
        self.save_cart_credential(response)

    def test_0002_get_cart(self):
        # Returns a specific cart from a shop

        # set credential of cart
        self.params = self.add_cart_credential(self.params)

        response = self.client.get_cart(self.params)
        self.assertEqual(isinstance(response, dict), True)

    def test_0003_add_product_line(self):
        # Creates a product line item in a cart.

        # set credential of cart
        self.params = self.add_cart_credential(self.params)

        # Get one product
        product_id = self.get_first_product()['productId']

        # Crate product order line
        line = ProductLineItemCreate()
        line.productId = product_id
        line.quantity = 1

        self.params["object"] = line

        response = self.client.add_cart_line_item(self.params)
        self.assertEqual(isinstance(response, dict), True)

        # We'll need lineItemId for removing a product from the cart
        self.save_resource(
            self.product_line_file, response['lineItemContainer']['productLineItems'][0]['lineItemId'].strip())

    def test_0005_add_coupon_to_cart(self):
        # Applies a coupon code on a cart

        # set credential of cart
        self.params = self.add_cart_credential(self.params)
        # x-www-form-urlencoded
        self.params["data"] = {'code': self.coupun_code}

        response = self.client.add_coupon(self.params)
        self.assertEqual(isinstance(response, dict), True)

        self.save_resource(
            self.coupon_line_file, response['lineItemContainer']['couponLineItem']['couponLineItemId'].strip())

    def test_0005_delete_coupon_from_cart(self):
        # Deletes a coupon from a cart

        # set credential of cart
        self.params = self.add_cart_credential(self.params)
        self.params["param2"] = self.get_resource(self.coupon_line_file)
        # x-www-form-urlencoded
        self.params["data"] = {'code': self.coupun_code}

        response = self.client.delete_coupon(self.params)
        self.assertEqual(isinstance(response, dict), True)

    def test_0006_remove_product_line(self):
        # Removes a product line item from a cart.

        # set credentials of the cart
        self.params = self.add_cart_credential(self.params)
        self.params["param2"] = self.get_resource(self.product_line_file)

        response = self.client.delete_cart_line_item(self.params)
        self.assertEqual(isinstance(response, dict), True)
