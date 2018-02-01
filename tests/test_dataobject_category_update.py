# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

# import the package
import epages_client

from epages_client.dataobjects.category_update import CategoryUpdate

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def setUp(self):
        pass

    def test_0001_simple_correct_inputs(self):
        category = CategoryUpdate()
        # string The unique identifier of the category a product is assigned to.
        category.categoryId = '111-222-333-444'
        # string The name of the category.
        category.name = 'Cat'
        # string The unique identifier of the category.
        category.alias = 'pets_cats'
        # string The page title of this category.
        category.pageTitle = 'Cats'
        # string The description of the category.
        category.description = 'Products for cats'
        # string The name of the category page that appears in the navigation bar.
        category.navigationCaption = 'Navi Cat'
        # boolean Indicates if the category is displayed in the shop.
        category.visible = False

        right_answer = {
            'categoryId': '111-222-333-444',
            'name': 'Cat',
            'alias': 'pets_cats',
            'pageTitle': 'Cats',
            'description': 'Products for cats',
            'navigationCaption': 'Navi Cat',
            'visible': False
        }

        self.assertEqual(category.get_dict(), right_answer)

    def test_0002_incorrect_inputs(self):
        category = CategoryUpdate()
        with self.assertRaises(TypeError) as e:
            category.categoryId = 111-222-333-444


if __name__ == '__main__':
    unittest.main()
