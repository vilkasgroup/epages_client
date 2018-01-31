# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

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
