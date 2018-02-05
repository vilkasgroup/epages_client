# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from pprint import pprint

# import the package
import epages_client

from epages_client.dataobjects.script_tag_create import ScriptTagCreate

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def setUp(self):
        pass

    def test_0001_dont_set_url_init(self):
        url = ScriptTagCreate()
        self.assertEqual(url.scriptUrl, None)
        self.assertEqual(url.is_valid(), False)

    def test_0002_set_valid_url_init(self):
        url = ScriptTagCreate(
            "https://ajax.googleapis.com/ajax/libs/dojo/1.13.0/dojo/dojo.js")
        self.assertEqual(
            url.scriptUrl, "https://ajax.googleapis.com/ajax/libs/dojo/1.13.0/dojo/dojo.js")
        self.assertEqual(url.is_valid(), True)

    def test_0003_set_valid_url(self):
        url = ScriptTagCreate()
        url.scriptUrl = "https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"
        self.assertEqual(
            url.scriptUrl, "https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js")
        self.assertEqual(url.is_valid(), True)

    def test_0004_set_invalid_url_init(self):
        url = ScriptTagCreate()
        with self.assertRaises(ValueError) as e:
            url = ScriptTagCreate(
                "://ajax.googleapis.com/ajax/libs/dojo/1.13.0/dojo/dojo.js")

    def test_0004_set_invalid_url(self):
        url = ScriptTagCreate()
        with self.assertRaises(ValueError) as e:
            url.scriptUrl = "://ajax.googleapis.com/ajax/libs/dojo/1.13.0/dojo/dojo.js"
