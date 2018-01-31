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
from epages_client.dataobjects.product_line_item_update import ProductLineItemUpdate
from epages_client.dataobjects.address import Address
from epages_client.dataobjects.order_patch import OrderPatch


class TestCartsOrdersAndOrdersMethods(BaseUnitTest):
    '''A class for testing order related methods on RestClient class'''

    # filename for saving cart credential
    cart_file = "cart_credential.csv"

    # filename for saving couponLineItemId
    coupon_line_file = "cart_coupon_line.txt"

    # filename for saving lineItemId
    product_line_file = "cart_product_line_item_id.txt"

    # filename for saving order id
    order_id_file = "order_id.txt"

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

    def get_products(self):
        products = self.client.get_products({
            "query": {},
            "param1": "",
            "param2": ""
        })
        return products['items']

    def setUp(self):

        self.client = RestClient(
            os.environ["EPAGES_API_URL"], os.environ["EPAGES_API_TOKEN"])

        self.params = {
            "query": {},
            "param1": "",
            "param2": ""
        }

    def test_0001_create_empty_cart(self):
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
        product_id = self.get_products()[0]['productId']

        # Crate product order line
        line = ProductLineItemCreate()
        line.productId = product_id
        line.quantity = 1

        self.params["object"] = line

        response = self.client.add_cart_line_item(self.params)
        self.assertEqual(isinstance(response, dict), True)

        # We'll need lineItemId for updating and removing a product from the cart
        self.save_resource(
            self.product_line_file, response['lineItemContainer']['productLineItems'][0]['lineItemId'].strip())

    def test_0004_update_product_line(self):
        # Update quantity of product line

        line = ProductLineItemUpdate()
        line.quantity = 5

        # set credential of cart
        self.params = self.add_cart_credential(self.params)
        self.params["param2"] = self.get_resource(self.product_line_file)
        self.params["object"] = line

        response = self.client.update_cart_line_item(self.params)
        self.assertEqual(isinstance(response, dict), True)

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

    def test_0006_delete_product_line(self):
        # Removes a product line item from a cart.

        # set credentials of the cart
        self.params = self.add_cart_credential(self.params)
        self.params["param2"] = self.get_resource(self.product_line_file)

        response = self.client.delete_cart_line_item(self.params)
        self.assertEqual(isinstance(response, dict), True)

    def test_0007_add_billing_address(self):
        # Modifies the billing address for a cart.

        billing_address = Address()
        billing_address.firstName = "Äijö"
        billing_address.lastName = "Äälinen"
        billing_address.street = "Pellavatehtaankatu 19"
        billing_address.zipCode = "33210"
        billing_address.city = "Tampere"
        billing_address.country = "FI"
        billing_address.emailAddress = "aijo.aalinen@vilkas.invalid"

        # set credentials of the cart
        self.params = self.add_cart_credential(self.params)
        self.params["object"] = billing_address

        response = self.client.update_billing_address(self.params)
        self.assertEqual(isinstance(response, dict), True)

    def test_0008_delete_billing_address(self):
        # set credentials of the cart
        self.params = self.add_cart_credential(self.params)

        response = self.client.delete_billing_address(self.params)
        self.assertEqual(isinstance(response, dict), True)

    def test_0009_add_shipping_address(self):
        # Modifies the shipping address for a cart.

        shipping_address = Address()
        shipping_address.firstName = "Лев"
        shipping_address.lastName = "Толстой"
        shipping_address.street = "Pellavatehtaankatu 19"
        shipping_address.zipCode = "33210"
        shipping_address.city = "Tampere"
        shipping_address.country = "FI"
        shipping_address.emailAddress = "leo.tolstoy@vilkas.invalid"
        shipping_address.gender = "MALE"
        shipping_address.jobTitle = "writer"

        # set credentials of the cart
        self.params = self.add_cart_credential(self.params)
        self.params["object"] = shipping_address

        response = self.client.update_shipping_address(self.params)
        self.assertEqual(isinstance(response, dict), True)

    def test_0010_shipping_shipping_address(self):
        # set credentials of the cart
        self.params = self.add_cart_credential(self.params)

        response = self.client.delete_shipping_address(self.params)
        self.assertEqual(isinstance(response, dict), True)

    def test_1001_create_order(self):
        # create a cart
        cart = CartCreate()
        cart.currency = 'EUR'
        cart.locale = 'fi_fi'
        cart.taxType = 'NET'

        products = self.get_products()

        # Add products to the cart
        item1 = ProductLineItemCreate()
        item1.productId = products[0]['productId']
        item1.quantity = 2
        cart.lineItems.add(item1)

        item2 = ProductLineItemCreate()
        item2.productId = products[1]['productId']
        item2.quantity = 4
        cart.lineItems.add(item2)

        # send to a shop
        self.params["object"] = cart
        response = self.client.add_cart(self.params)
        self.save_cart_credential(response)

        basic_params = self.add_cart_credential({})

        # Add required billing address
        buyer = Address()
        buyer.country = "FI"
        buyer.emailAddress = "yrjo.aaninen@vilkas.invalid"

        # params for update billing address
        params = {'object': buyer}
        params.update(basic_params)

        response = self.client.update_billing_address(params)
        self.assertEqual(isinstance(response, dict), True)

        response = self.client.create_order(basic_params)
        self.assertEqual(isinstance(response, dict), True)

        self.save_resource(self.order_id_file, response['orderId'])

    def test_1002_get_orders(self):
        # Get orders

        # find all finnish and euro orders
        self.params['query'] = {
            'currency': 'EUR',
            'locale': 'fi_FI'
        }

        response = self.client.get_orders(self.params)
        self.assertEqual(isinstance(response, dict), True)

    def test_1003_get_the_order(self):
        # Get the order created before

        # Get order id
        self.params["param1"] = self.get_resource(self.order_id_file)

        response = self.client.get_order(self.params)
        self.assertEqual(isinstance(response, dict), True)

    def test_1003_update_order(self):
        # update the order created before

        order = OrderPatch()
        order.billingAddress.emailAddress = "my-new@email.address.invalid"
        order.billingAddress.firstName = "David"
        order.billingAddress.lastName = "Mattson"
        order.billingAddress.lastName = "MALE"

        # Get order id
        self.params["param1"] = self.get_resource(self.order_id_file)
        self.params["object"] = order

        response = self.client.update_order(self.params)
        self.assertEqual(isinstance(response, dict), True)

    def test_1004_get_order_documents(self):
        # Returns finalized invoice and credit note order documents by orderId.

        # Get order id
        self.params["param1"] = self.get_resource(self.order_id_file)

        response = self.client.get_order_documents(self.params)
        self.assertEqual(isinstance(response, dict), True)
