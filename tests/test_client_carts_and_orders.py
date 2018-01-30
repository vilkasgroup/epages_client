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

    # Get the directory where this file is located
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Set the resources directory where id files and test image are located
    resources = os.path.join(dir_path, "resources")

    # If the resources directory doesn't exist, raise an error
    if not os.path.exists(resources):
        raise OSError("Resources directory not found.")

    # Add cart.csv to the resources path
    cart_file = os.path.join(resources, "cart_resource.csv")

    def get_cart_resource(self):
        '''A function to get cart token and cart id from csv file.'''

        try:
            fh = open(self.cart_file, "r")
            line = fh.read()
            fh.close()
        except FileNotFoundError:
            raise FileNotFoundError("Cart file not found.")

        ids = line.split(";")
        return {
            'token': ids[0],
            'id': ids[1]
        }

    def save_cart_resource(self, response):
        '''Function to save cart token and cart_id to a text-file'''

        cart_token = response['X-ePages-Cart-Token']
        cart_id = response['cartId']

        try:
            fh = open(self.cart_file, "w")
            fh.write("%s;%s" % (cart_token, cart_id))
            fh.close()
        except IOError:
            print("Cart file couldn't be created.")


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
        cart = CartCreate()
        self.params["object"] = cart
        response = self.client.add_cart(self.params)
        self.assertEqual(isinstance(response, dict), True)

        # Save cartId details to text file
        self.save_cart_resource(response)

    # def test_0002_get_cart(self):
    #     cart_ids = self.get_cart_resource()
    #     pprint(cart_ids)
    #     self.params['param1'] = cart_ids['id']
    #     self.params['headers'] = {'X-ePages-Cart-Token': cart_ids['token']}

    #     response = self.client.get_cart(self.params)
    #     self.assertEqual(isinstance(response, dict), True)
    #     pprint(response)

    def test_0005_add_product_line(self):
        # Get created cart
        cart_ids = self.get_cart_resource()
        self.params["param1"] = cart_ids['id']
        self.params["headers"] = {'X-epages-Cart-Token': cart_ids['token']}

        # Get a product
        product_id = self.get_first_product()['productId']

        line = ProductLineItemCreate()
        line.productId = product_id
        line.quantity = 1

        self.params["object"] = line
        print('A!'*50, 'self.params["param1"]: ', self.params["param1"], 'self.params["headers"]: ', self.params["headers"], 'line: ', line)
        self.client.add_cart_line_item(self.params)


