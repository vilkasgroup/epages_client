# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

# import the RestClient class
from epages_client.client import RestClient

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestNewsletterMethods(BaseUnitTest):
    '''A class for testing newsletter related methods on RestClient class'''

    def setUp(self):

        self.client = RestClient(
            os.environ["EPAGES_API_URL"], os.environ["EPAGES_API_TOKEN"])

        self.params = {
            "query": {},
            "param1": "",
            "param2": ""
        }

    def test_001_get_newsletter_campaigns(self):

        newsletter_campaigns = self.client.get_newsletter_campaigns(self.params)

        self.assertEqual(isinstance(newsletter_campaigns, dict), True)

    def test_002_get_newsletter_campaign_subscribers(self):

        newsletter_subscribers = self.client.get_newsletter_campaign_subscribers(self.params)