# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

# import the package
import epages_client

from epages_client.dataobjects.customer_create import CustomerCreate

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def setUp(self):
        pass

    def test_0001_correct_inputs(self):

        james = CustomerCreate()
        james.customerNumber = '007'
        james.billingAddress.gender = 'MALE'
        james.billingAddress.emailAddress = 'james@bond.uk'

        self.assertEqual(james.get_dict(), {'customerNumber': '007', 'billingAddress': {
                         'emailAddress': 'james@bond.uk', 'gender': 'MALE'}})

        maria = CustomerCreate()
        maria.customerNumber = '23'
        self.assertEqual(maria.customerNumber, '23')
        maria.internalNote = "What a customer!"
        self.assertEqual(maria.internalNote, 'What a customer!')
        maria.billingAddress.doorCode = "Simsalabim"
        self.assertEqual(maria.is_valid(), True)

        self.assertEqual(maria.billingAddress.get_dict(),
                         {'doorCode': 'Simsalabim'})

    def test_0002_invalid_inputs(self):
        bad_lad = CustomerCreate()

        with self.assertRaises(ValueError) as e:
            bad_lad.billingAddress.emailAddress = 'my(a)emailaddress.com'

        with self.assertRaises(ValueError) as e:
            bad_lad.billingAddress.gender = 'MAN'


if __name__ == '__main__':
    unittest.main()
