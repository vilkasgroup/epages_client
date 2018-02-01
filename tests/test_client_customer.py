# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import uuid

# import the RestClient class
from epages_client.client import RestClient

# Import the customer create class
from epages_client.dataobjects.customer_create import CustomerCreate

# Import the customer patch class
from epages_client.dataobjects.customer_update import CustomerUpdate

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestCustomerMethods(BaseUnitTest):
    '''A class for testing customer related methods on RestClient class'''

    def setUp(self):

        self.client = RestClient(
            os.environ["EPAGES_API_URL"], os.environ["EPAGES_API_TOKEN"])

        self.params = {
            "query": {},
            "param1": "",
            "param2": ""
        }

    def test_001_add_customer_no_object(self):

        with self.assertRaises(RuntimeError) as e:
            response = self.client.add_customer(self.params)

    def test_002_add_customer_invalid_object(self):

        self.params["object"] = None

        with self.assertRaises(TypeError) as e:
            response = self.client.add_customer(self.params)

    def test_003_add_customer_empty_billing_address(self):

        customer = CustomerCreate()

        self.params["object"] = customer

        with self.assertRaises(ValueError) as e:
            response = self.client.add_customer(self.params)

    def test_004_add_customer(self):

        customer = CustomerCreate()
        customer.billingAddress.firstName = "John"
        customer.billingAddress.lastName = "Doe"
        customer.billingAddress.emailAddress = "john@whiners.co.uk"

        self.params["object"] = customer

        response = self.client.add_customer(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_005_get_customers(self):

        customers = self.client.get_customers(self.params)

        self.assertEqual(isinstance(customers, dict), True)

    def test_006_get_customer_no_id(self):

        with self.assertRaises(ValueError) as e:
            customer = self.client.get_customer(self.params)

    def test_007_get_customer_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            customer = self.client.get_customer(self.params)

    def test_008_get_customer_correct_id(self):

        customers = self.client.get_customers(self.params)

        customer_id = customers["items"][1]["customerId"]

        self.params["param1"] = customer_id

        customer = self.client.get_customer(self.params)

        self.assertEqual(isinstance(customer, dict), True)

    def test_009_update_customer_no_id(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.update_product(self.params)

    def test_010_update_customer_no_object(self):

        customers = self.client.get_customers(self.params)

        customer_id = customers["items"][1]["customerId"]

        self.params["param1"] = customer_id

        with self.assertRaises(RuntimeError) as e:
            response = self.client.update_customer(self.params)

    def test_011_update_customer_invalid_object(self):

        customers = self.client.get_customers(self.params)

        customer_id = customers["items"][1]["customerId"]

        self.params["param1"] = customer_id

        self.params["object"] = None

        with self.assertRaises(TypeError) as e:
            response = self.client.update_customer(self.params)

    def test_012_update_customer(self):

        customers = self.client.get_customers(self.params)

        customer_id = customers["items"][1]["customerId"]

        self.params["param1"] = customer_id

        customer = CustomerUpdate()
        customer.internalNote = "This customer whines a lot."

        self.params["object"] = customer

        response = self.client.update_customer(self.params)

        self.assertEqual(isinstance(response, dict), True)
