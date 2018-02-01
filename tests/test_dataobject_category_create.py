# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

# import the package
import epages_client

from epages_client.dataobjects.category_create import CategoryCreate

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def setUp(self):
        pass

    def test_0001_simple_correct_inputs(self):
        category = CategoryCreate()
        # string The name of the category.
        category.name = "Cat"
        # string The unique identifier of the new category. If already in use, the system will automatically increment by number, e.g. alias1, alias2.
        category.alias = "pets_cats"
        # string The page title of the category.
        category.pageTitle = "Cats"
        # string The description of the category.
        category.description = "Products for cats"
        # string The name of the category that appears in the navigation bar.
        category.navigationCaption = "Navi Cat"

        right_answer = {
            'name': 'Cat',
            'alias': 'pets_cats',
            'pageTitle': 'Cats',
            'description': 'Products for cats',
            'navigationCaption': 'Navi Cat',
        }

        self.assertEqual(category.get_dict(), right_answer)

    def test_0002_incorrect_inputs(self):
        category = CategoryCreate()
        with self.assertRaises(TypeError) as e:
            category.name = 123456

if __name__ == '__main__':
    unittest.main()
