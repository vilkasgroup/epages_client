# -*- coding: utf-8 -*-
import unittest

# import the package
import epages_client

from epages_client.dataobjects.category_sequence_update import CategorySequenceUpdate

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def setUp(self):
        pass

    def test_0101_simple_correct_inputs(self):
        csu = CategorySequenceUpdate()
        csu.add('cat')
        csu.add('doc')
        self.assert_count_items_equal(csu.get_dict(), ['cat', 'doc'])

    def test_0102_simple_correct_inputs_empty(self):
        csu = CategorySequenceUpdate()
        self.assert_count_items_equal(csu.get_dict(), [])

    def test_0200_simple_incorrect_inputs(self):
        csu = CategorySequenceUpdate()
        with self.assertRaises(TypeError) as e:
            csu.add(123)

        with self.assertRaises(TypeError) as e:
            csu.add(CategorySequenceUpdate())


if __name__ == '__main__':
    unittest.main()
