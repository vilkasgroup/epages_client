# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import uuid

# import the RestClient class
from epages_client.client import RestClient

# import the script tag create class
from epages_client.dataobjects.script_tag_create import ScriptTagCreate

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestScriptTagMethods(BaseUnitTest):
    '''A class for testing script tag related methods on RestClient class'''

    def setUp(self):

        self.client = RestClient(
            os.environ["EPAGES_API_URL"], os.environ["EPAGES_API_TOKEN"])

        self.params = {
            "query": {},
            "param1": "",
            "param2": ""
        }

    def test_001_add_script_tag_no_object(self):

        with self.assertRaises(RuntimeError) as e:
            response = self.client.add_script_tag(self.params)

    def test_002_add_script_tag_invalid_object(self):

        self.params["object"] = None

        with self.assertRaises(TypeError) as e:
            response = self.client.add_script_tag(self.params)

    def test_003_add_script_tag_no_script_url(self):

        script_tag = ScriptTagCreate()

        self.params["object"] = script_tag

        with self.assertRaises(ValueError) as e:
            response = self.client.add_script_tag(self.params)

    def test_004_add_script_tag_false_url(self):

        script_tag = ScriptTagCreate()

        with self.assertRaises(ValueError) as e:
            script_tag.scriptUrl = "foobar"

    def test_005_add_script_tag(self):

        script_tag = ScriptTagCreate()

        script_tag.scriptUrl = "https://code.jquery.com/jquery-3.3.1.min.js"

        self.params["object"] = script_tag

        response = self.client.add_script_tag(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_006_get_script_tags(self):

        script_tags = self.client.get_script_tags(self.params)

        self.assertEqual(isinstance(script_tags, dict), True)

    def test_007_delete_script_tag_no_id(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.delete_script_tag(self.params)

    def test_008_delete_script_tag_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            response = self.client.delete_script_tag(self.params)

    def test_009_delete_script_tag(self):

        script_tags = self.client.get_script_tags()
        script_tag_id = script_tags["items"][0]["scriptTagId"]

        self.params["param1"] = script_tag_id

        response = self.client.delete_script_tag(self.params)

        self.assertEqual(isinstance(response, dict), True)
