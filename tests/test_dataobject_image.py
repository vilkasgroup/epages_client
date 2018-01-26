# -*- coding: utf-8 -*-
"""Tests for `epages_client.dataobjects.image` package."""
import unittest

# import the package
import epages_client

from epages_client.dataobjects.image import Image

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def test_0001_correct_inputs(self):
        img = Image()
        img.url = "https://www.linux.fi/w/skins/common/images/linux.png"
        img.classifier = 'Small'

    def test_0002_invalid_url(self):
        img = Image()
        with self.assertRaises(ValueError) as e:
            img.url = "/linux.png"


if __name__ == '__main__':
    unittest.main()
