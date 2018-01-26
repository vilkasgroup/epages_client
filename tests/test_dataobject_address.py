# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from pprint import pprint

# import the package
import epages_client

from epages_client.dataobjects.address import Address

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def setUp(self):
        pass

    def test_0001_simple_correct_inputs(self):
        address = Address()
        address.company = "Company"
        address.salutation = "Mr"
        address.title = "Agent"
        address.firstName = "James"
        address.lastName = "Körri"
        address.street = "Finlaysoninkuja 19"
        address.streetDetails = ""
        address.zipCode = "33210"
        address.city = "TAMPERE"
        address.state = "Pirkanmaa"
        address.country = "Finland"
        address.vatId = "vat_01"
        address.birthday = "04.04.2014"
        address.emailAddress = "invalid@email.adress"
        address.addressExtension = "C 2"
        address.bankAccountHolder = "James Körri"
        address.bankAccountNumber = "123456-789"
        address.bankName = "Big Bank"
        address.bankSortCode = "BB"
        address.businessEmailAddress = "email.address@business.invalid"
        address.businessPhoneNumber = "+358441111111"
        address.department = "IT"
        address.displayName = "James Körri"
        address.doorCode = "0000"
        address.faxNumber = "+35845000000"
        address.fiscalCode = "000000-000"
        address.gender = "MALE"
        address.jobTitle = "Secret Agent"
        address.middleName = "Kalle"
        address.mobilePhoneNumber = "+35844000000000"
        address.phoneNumber = "+3584413579"
        address.privateEmailAddress = "private@email.address.invalid"
        address.privatePhoneNumber = "+358441234567"
        address.websiteUrl = "http://websites.invalid"

        right_answer = {
            'company': 'Company',
            'salutation': 'Mr',
            'title': 'Agent',
            'firstName': 'James',
            'lastName': 'Körri',
            'street': 'Finlaysoninkuja 19',
            'streetDetails': '',
            'zipCode': '33210',
            'city': 'TAMPERE',
            'state': 'Pirkanmaa',
            'country': 'Finland',
            'vatId': 'vat_01',
            'birthday': '04.04.2014',
            'emailAddress': 'invalid@email.adress',
            'addressExtension': 'C 2',
            'bankAccountHolder': 'James Körri',
            'bankAccountNumber': '123456-789',
            'bankName': 'Big Bank',
            'bankSortCode': 'BB',
            'businessEmailAddress': 'email.address@business.invalid',
            'businessPhoneNumber': '+358441111111',
            'department': 'IT',
            'displayName': 'James Körri',
            'doorCode': '0000',
            'faxNumber': '+35845000000',
            'fiscalCode': '000000-000',
            'gender': 'MALE',
            'jobTitle': 'Secret Agent',
            'middleName': 'Kalle',
            'mobilePhoneNumber': '+35844000000000',
            'phoneNumber': '+3584413579',
            'privateEmailAddress': 'private@email.address.invalid',
            'privatePhoneNumber': '+358441234567',
            'websiteUrl': 'http://websites.invalid'
        }

        self.assertEqual(address.get_dict(), right_answer)

    def test_0002_incorrect_email_addresses(self):
        address = Address()

        with self.assertRaises(ValueError) as e:
            address.emailAddress = 'test(at)invalid.email'

        with self.assertRaises(ValueError) as e:
            address.businessEmailAddress = 'test(at)invalid.email'

        with self.assertRaises(ValueError) as e:
            address.privateEmailAddress = 'test(at)invalid.email'

    def test_0003_incorrect_website_url(self):
        address = Address()
        with self.assertRaises(ValueError) as e:
            address.websiteUrl = "www.website.invalid"


if __name__ == '__main__':
    unittest.main()
