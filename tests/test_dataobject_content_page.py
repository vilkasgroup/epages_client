# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest

# import the package
import epages_client

from epages_client.dataobjects.content_page import ContentPage

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def setUp(self):
        pass

    def test_0001_simple_correct_inputs(self):
        page = ContentPage()

        # string The name that appears on the page.
        page.name = "Cats"
        # string The name of the page, that appears on the browser tab.
        page.title = "Cats' toys"
        # string The name of the page, that appears in the navigation bar.
        page.navigationCaption = "Toys for cats"
        # string Additional short information that can be given to better explain what’s on the page.
        page.shortDescription = "short description"
        # string Information on the topic of the page.
        page.description = "long description"

        right_answer = {
            'name': 'Cats',
            'title': "Cats' toys",
            'navigationCaption': 'Toys for cats',
            'shortDescription': 'short description',
            'description': 'long description',
        }

        self.assertEqual(page.get_dict(), right_answer)

    def test_0002_incorrect_inputs(self):
        page = ContentPage()
        with self.assertRaises(TypeError) as e:
            page.name = 123


if __name__ == '__main__':
    unittest.main()
