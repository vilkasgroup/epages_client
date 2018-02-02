# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import the Httphandler Class
from .http_handler import HttpHandler

# import the Product class from dataobjects
from .dataobjects.data_object import DataObject

from pprint import pprint
import json
import os


class RestClient(object):
    '''Client to connect to the ePages REST API'''

    def __init__(self, api_url, token="", verify=True, client_id="", client_secret="", beyond=False):

        # Get an instance of httphandler
        self.http = HttpHandler(api_url, token, verify,
                                client_id, client_secret, beyond)

        # Set currency and locale to be empty by default
        self._currency = ""
        self._locale = ""

        # Get the directory where this file is located
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Add the method mapping file to the directory path
        method_file = os.path.join(dir_path, "method_mapping.json")

        try:
            # Open the json file containing method mapping
            methods = open(method_file)

            # Load json to the dict
            self.mapping = json.load(methods)

            # Close the file handler
            methods.close()
        except IOError:
            print("Error: method mapping file not found.")
            self.mapping = {}

    def __getattr__(self, attr):
        '''A magic method to catch attributes that don't really exist'''

        # If called attribute is found on the mapping dictionary
        if attr in self.mapping:
            def build_request(params=None):
                '''Called attribute can have params dictionary as a parameter,
                that contains dictionaries for data and query, and variables
                for item id and image name'''

                if params is None:
                    params = {}

                # Get the nested dictionary for called attribute
                method = self.mapping[attr]

                # Check the sent parameters
                method = self.check_params(method, params)

                # Get the needed method function from HttpHandler
                method_func = getattr(self.http, method["method"])

                # Perform the API call
                response = method_func(method["api_dict"])

                return response

            return build_request
        else:
            print("Error: command '%s' not found." % (attr,))

    def check_params(self, method=None, params=None):
        '''
        A function for checking sent parameters; are required ones set
        and are parameters valid.
        '''

        if method is not None and params is not None:

            # If params dictionary doesn't have data and query, add them
            if "data" not in params:
                params["data"] = {}

            if "query" not in params:
                params["query"] = {}

            # If user has set headers
            if "headers" in params and params["headers"]:

                # If headers are found in api_dict, merge headers in params with them
                if "headers" in method["api_dict"] and method["api_dict"]["headers"]:
                    method["api_dict"]["headers"].update(params["headers"])
                else:
                    method["api_dict"]["headers"] = params["headers"]

            # If parameters has a data object
            if "object" in params:

                # Check if the object is an instance of DataObject class
                if not isinstance(params["object"], DataObject):
                    raise TypeError("Invalid object.")

                # Check object validity
                obj = params["object"]
                if not obj.is_valid():
                    raise ValueError("Validate object contents.")

                # If object is valid, get the data in form of dictionary
                # or json patch, and add it to the params
                if method["method"] == "patch":
                    params["data"] = obj.get_patch()
                else:
                    params["data"] = obj.get_dict()

            # If query has not currency or locale, use setted ones
            if "currency" not in params["query"] and self.currency != "":
                params["query"]["currency"] = self.currency

            if "locale" not in params["query"] and self.locale != "":
                params["query"]["locale"] = self.locale

            # Check if there's variable requirements and loop them
            if "require" in method:
                for var in method["require"]:
                    # If requirement has prefix q_, it's a requirement
                    # for query parameter
                    if var.startswith("q_"):
                        # Get the variable value without the prefix
                        missing = var[2:]

                        # If variable is not found in query parameters or it is empty,
                        # raise an error
                        if missing not in params["query"] or params["query"][missing] == "":
                            raise ValueError(
                                "Missing query parameter '" + missing + "'")

                    # Otherwise, it's a required variable
                    else:
                        if var not in params or params[var] == "":
                            raise ValueError("Missing variable '" + var + "'")

            # If there's the first parameter set, add it to the end of the path
            if "param1" in params and params["param1"] != "":
                method["api_dict"]["path"] += "/" + params["param1"]

            if "path2" in method and method["path2"] != "":
                method["api_dict"]["path"] += method["path2"]

            # If there's the second parameter set, add it to the end of the path
            if "param2" in params and params["param2"] != "":
                method["api_dict"]["path"] += "/" + params["param2"]

            # Add data and query dictionaries to the final api_dict
            method["api_dict"]["data"] = params["data"]
            method["api_dict"]["query"] = params["query"]

            return method

    @property
    def currency(self):
        '''Currency getter'''
        return self._currency

    @currency.setter
    def currency(self, value):
        '''Currency setter'''
        self._currency = value

    @property
    def locale(self):
        '''Locale getter'''
        return self._locale

    @locale.setter
    def locale(self, value):
        '''Locale setter'''
        self._locale = value
