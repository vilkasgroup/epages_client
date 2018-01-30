# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import uuid

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

        newsletter_campaigns = self.client.get_newsletter_campaigns(
            self.params)

        self.assertEqual(isinstance(newsletter_campaigns, dict), True)

    def test_002_get_newsletter_campaign_subscribers_no_id(self):

        with self.assertRaises(ValueError) as e:
            newsletter_subscribers = self.client.get_newsletter_campaign_subscribers(
                self.params)

    def test_003_get_newsletter_campaign_subscribers_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            newsletter_subscribers = self.client.get_newsletter_campaign_subscribers(
                self.params)

    def test_004_get_newsletter_campaign_subscribers(self):

        newsletter_campaigns = self.client.get_newsletter_campaigns(
            self.params)

        # If there are some newsletters, check if the first one has subscribers
        if newsletter_campaigns["results"] > 0:

            campaign_id = newsletter_campaigns["items"][0]["campaignId"]
            self.params["param1"] = campaign_id

            newsletter_subscribers = self.client.get_newsletter_campaign_subscribers(
                self.params)

            self.assertEqual(isinstance(newsletter_subscribers, dict), True)
