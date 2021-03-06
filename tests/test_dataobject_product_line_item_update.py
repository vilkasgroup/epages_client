# -*- coding: utf-8 -*-
"""Tests for `epages_client.dataobjects.product_line_item_update` package."""
import unittest

# import the package
import epages_client

from epages_client.dataobjects.product_line_item_update import ProductLineItemUpdate

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def test_0001_test_property(self):
        line = ProductLineItemUpdate()
        line.quantity = 5
        self.assertEqual(line.get_dict(), {"quantity": 5})

    def test_0002_test_init_set(self):
        line = ProductLineItemUpdate(3.3)
        self.assertEqual(line.get_dict(), {"quantity": 3.3})

    def test_1001_invalid_inputs(self):
        line = ProductLineItemUpdate()
        with self.assertRaises(TypeError) as e:
            line.quantity = "4.0"

    def test_1002_invalid_init_set(self):
        line = ProductLineItemUpdate()
        with self.assertRaises(TypeError) as e:
            line.quantity = "2"


if __name__ == '__main__':
    unittest.main()
