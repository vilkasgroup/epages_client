# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import time

# import the RestClient class
from epages_client.client import RestClient

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestClient(BaseUnitTest):
    '''A class for testing the RestClient class'''

    def setUp(self):

        self.client = RestClient(
            os.environ["EPAGES_API_URL"], os.environ["EPAGES_API_TOKEN"])

        self.params = {
            "query": {},
            "param1": "",
            "param2": ""
        }

    def test_001_use_undefined_command(self):

        with self.assertRaises(TypeError) as e:
            response = self.client.foobar()

    def test_002_set_and_get_currency(self):

        self.client.currency = "EUR"

        self.assertEqual(self.client.currency, "EUR")

    def test_003_set_and_get_locale(self):

        self.client.locale = "fi_FI"

        self.assertEqual(self.client.locale, "fi_FI")

    def test_004_method_mapping_not_found(self):

        # Get current directory
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Get one directory up, that is basically joining '..'
        # to the path and getting absolute path from it
        one_dir_up = os.path.abspath(os.path.join(dir_path, ".."))

        # Add the project name to the path to form the client directory
        client_dir = os.path.join(one_dir_up, "epages_client")

        # Create paths for correct and incorrect method mapping files
        correct_mapping = os.path.join(client_dir, "method_mapping.json")
        incorrect_mapping = os.path.join(client_dir, "method_rapping.json")

        # Rename method mapping to be a invalid one
        os.rename(correct_mapping, incorrect_mapping)

        # Reload client
        self.client = RestClient(
            os.environ["EPAGES_API_URL"], os.environ["EPAGES_API_TOKEN"])

        # When the method mapping file is not found, and the called method
        # is not found either, there raises a TypeError
        with self.assertRaises(TypeError) as e:
            self.client.get_shop_info()

        # Rename the method mapping file to its original name
        os.rename(incorrect_mapping, correct_mapping)

        time.sleep(1)
