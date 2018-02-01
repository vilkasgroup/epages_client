# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import unittest

# import the RestClient class
from epages_client.client import RestClient

# Import the contact info class
from epages_client.dataobjects.contact_info import ContactInfo

# Import the content page class
from epages_client.dataobjects.content_page import ContentPage

# import base class for unit testing
from .base_unit_test import BaseUnitTest

skip_test = unittest.skipUnless(
    os.environ.get('EPAGES_RUN_ALL_TESTS', False), 'Skipping test.'
)


class TestLegalMethods(BaseUnitTest):
    '''A class for testing legal text related methods on RestClient class'''

    def setUp(self):

        self.client = RestClient(
            os.environ["EPAGES_API_URL"], os.environ["EPAGES_API_TOKEN"])

        self.params = {
            "query": {},
            "param1": "",
            "param2": ""
        }

    def test_001_get_legal_information(self):

        legal_information = self.client.get_legal_information(self.params)

        self.assertEqual(isinstance(legal_information, dict), True)

    def test_002_get_contact_information(self):

        contact_information = self.client.get_contact_information(self.params)

        self.assertEqual(isinstance(contact_information, dict), True)

    def test_003_get_privacy_policy(self):

        privacy_policy = self.client.get_privacy_policy(self.params)

        self.assertEqual(isinstance(privacy_policy, dict), True)

    def test_004_get_terms_and_conditions(self):

        terms_and_conditions = self.client.get_terms_and_conditions(
            self.params)

        self.assertEqual(isinstance(terms_and_conditions, dict), True)

    @skip_test
    def test_005_get_rights_of_withdrawal(self):

        rights_of_withdrawal = self.client.get_rights_of_withdrawal(
            self.params)

        self.assertEqual(isinstance(rights_of_withdrawal, dict), True)

    def test_006_get_shipping_information(self):

        shipping_information = self.client.get_shipping_information(
            self.params)

        self.assertEqual(isinstance(shipping_information, dict), True)

    def test_007_update_contact_information_no_locale(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.update_contact_information(self.params)

    def test_008_update_contact_information_unsupported_locale(self):

        self.client.locale = "de_DE"

        with self.assertRaises(RuntimeError) as e:
            response = self.client.update_contact_information(self.params)

    def test_009_update_contact_information_invalid_object(self):

        self.client.locale = "fi_FI"
        self.params["object"] = None

        with self.assertRaises(TypeError) as e:
            response = self.client.update_category(self.params)

    def test_010_update_contact_information(self):

        self.client.locale = "en_GB"

        contact_info = ContactInfo()

        contact_info.name = "Contact information"
        contact_info.company = "Test shop"
        contact_info.address = "Finlaysoninkuja 19\n"
        contact_info.address += "33210 Tampere"

        self.params["object"] = contact_info

        response = self.client.update_contact_information(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_011_update_privacy_policy_no_locale(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.update_privacy_policy(self.params)

    def test_012_update_privacy_policy(self):

        self.client.locale = "en_GB"

        privacy_policy = self.client.get_privacy_policy(self.params)

        content_page = ContentPage()

        content_page.name = privacy_policy["name"]
        content_page.navigationCaption = privacy_policy["navigationCaption"]
        content_page.title = privacy_policy["title"]
        content_page.description = privacy_policy["description"]

        self.params["object"] = content_page

        response = self.client.update_privacy_policy(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_013_update_terms_and_conditions_no_locale(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.update_terms_and_conditions(self.params)

    def test_014_update_terms_and_conditions(self):

        self.client.locale = "en_GB"

        terms_and_conditions = self.client.get_terms_and_conditions(
            self.params)

        content_page = ContentPage()

        content_page.name = terms_and_conditions["name"]
        content_page.navigationCaption = terms_and_conditions["navigationCaption"]
        content_page.title = terms_and_conditions["title"]
        content_page.description = terms_and_conditions["description"]

        self.params["object"] = content_page

        response = self.client.update_terms_and_conditions(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_015_update_rights_of_withdrawal_no_locale(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.update_rights_of_withdrawal(self.params)

    @skip_test
    def test_016_update_rights_of_withdrawal(self):

        self.client.locale = "en_GB"

        content_page = ContentPage()

        content_page.name = "Rights of withdrawal"
        content_page.navigationCaption = "Rights of withdrawal"
        content_page.title = "Rights of withdrawal - Test shop"
        content_page.description = "There isn't any rights of withdrawal, deal with it :)"

        self.params["object"] = content_page

        response = self.client.update_rights_of_withdrawal(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_017_update_shipping_information_no_locale(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.update_shipping_information(self.params)

    def test_018_update_shipping_information(self):

        self.client.locale = "en_GB"

        content_page = ContentPage()

        content_page.name = "Shipping information"
        content_page.navigationCaption = "Shipping information"
        content_page.title = "Shipping information - Test shop"
        content_page.description = "Along the shipping information there should be also a boating information ;)"

        self.params["object"] = content_page

        response = self.client.update_shipping_information(self.params)

        self.assertEqual(isinstance(response, dict), True)
