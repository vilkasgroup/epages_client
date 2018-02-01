# -*- coding: utf-8 -*-
import unittest
from pprint import pprint

# import the package
import epages_client

from epages_client.dataobjects.customer_update import CustomerUpdate
from epages_client.dataobjects.remove_value import RemoveValue

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def setUp(self):
        pass

    def test_0001_simple_correct_inputs(self):
        james = CustomerUpdate()
        james.internalNote = "WOW!"
        james.customerNumber = '007'
        self.assert_count_items_equal(james.get_patch(), [
                                      {'op': 'add', 'value': 'WOW!', 'path': '/internalNote'}, {'op': 'add', 'value': '007', 'path': '/customerNumber'}])

    def test_0002_correct_inputs(self):
        james = CustomerUpdate()
        james.internalNote = "WOW!"
        james.customerNumber = '007'
        james.billingAddress.birthday = '2018-01-02'
        james.billingAddress.gender = 'MALE'

        self.assert_count_items_equal(james.get_patch(), [{'op': 'add', 'value': 'WOW!', 'path': '/internalNote'}, {
                                      'op': 'add', 'value': '007', 'path': '/customerNumber'}, {'op': 'add', 'path': '/billingAddress', 'value': {'birthday': '2018-01-02', 'gender': 'MALE'}}])

    def test_0003_remove_values(self):
        james = CustomerUpdate()
        james.internalNote = RemoveValue()
        james.billingAddress = RemoveValue()

        correct_answer = [
            {'op': 'remove', 'path': '/billingAddress'},
            {'op': 'remove', 'path': '/internalNote'}
        ]

        self.assert_count_items_equal(james.get_patch(), correct_answer)


if __name__ == '__main__':
    unittest.main()
