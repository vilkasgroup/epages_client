# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

# import the package
import epages_client

from epages_client.dataobjects.contact_info import ContactInfo

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def setUp(self):
        pass

    def test_0001_simple_correct_inputs(self):
        c_info = ContactInfo()

        # string The name that appears on the contact information page, e.g. Contact Us.
        c_info.name = 'New cat products'
        # string The name of the contact information page, that appears on the browser tab.
        c_info.title = 'Cat products'
        # string The name of the contact information page that appears in the navigation bar.
        c_info.navigationCaption = 'navigationCaption'
        # string Additional short information that can be given to e.g. better explain what’s on the contact information page.
        c_info.shortDescription = 'short description'
        # string Additional information that can be added to the contact information page, e.g. tax identification number or bank account.
        c_info.description = 'Description long'
        # string The name of the shop.
        c_info.company = 'Company Ltd'
        # string The contact person for the shop, usually the shop owner.
        c_info.contactPerson = 'Öölö Köölö'
        # string The job title of the contact person.
        c_info.contactPersonJobTitle = 'Director'
        # string The postal address of the shop.
        c_info.address = 'Street'
        # string The phone number of the shop.
        c_info.phone = '020 7431912'
        # string The email address of the shop.
        c_info.email = 'email@address.invalid'

        right_answer = {
            'name': 'New cat products',
            'title': 'Cat products',
            'navigationCaption': 'navigationCaption',
            'shortDescription': 'short description',
            'description': 'Description long',
            'company': 'Company Ltd',
            'contactPerson': 'Öölö Köölö',
            'contactPersonJobTitle': 'Director',
            'address': 'Street',
            'phone': '020 7431912',
            'email': 'email@address.invalid'
        }

        self.assertEqual(c_info.get_dict(), right_answer)

    def test_0002_incorrect_inputs(self):
        c_info = ContactInfo()
        with self.assertRaises(ValueError) as e:
            c_info.email = "email(at)address.fi"


if __name__ == '__main__':
    unittest.main()
