# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import logging


class HttpHandler(object):
    '''Handles HTTP-requests'''
    _URI_separator = '/'

    def __init__(self, api_url, token, verify, client_id, client_secret, beyond):
        self.api_url = api_url
        self.token = token
        self.verify = verify
        self.client_id = client_id
        self.client_secret = client_secret
        self.beyond = beyond

        self._default_headers = {}
        self.api_url = api_url
        self.token = token
        self.verify = verify
        self.client_id = client_id
        self.client_secret = client_secret
        self.beyond = beyond

        self._set_headers()

        # Remove trailing / from api_url
        if self.api_url.endswith(HttpHandler._URI_separator):
            self.api_url = self.api_url[:-1]

    def get(self, dict_data):

        # If headers are given in dict_data, merge them with current headers
        if "headers" in dict_data and dict_data["headers"]:
            self._default_headers.update(dict_data["headers"])

        # If there isn't already a content type header, add it
        if "Content-Type" not in self._default_headers:
            self._default_headers["Content-Type"] = "application/json"

        """Do GET request"""
        return self._request(requests.get, dict_data)

    def post(self, dict_data):

        # If headers are given in dict_data, merge them with current headers
        # Note: In all current post method situations there are custom Content-Type
        # given. This if-else here assumes, that Content-Type is always given with
        # the custom headers and it's only set in the else section.
        if "headers" in dict_data and dict_data["headers"]:
            self._default_headers.update(dict_data["headers"])
        # If there isn't file going to be uploaded, set the default
        # content type header. For file uploads there should be none.
        elif "use_files" not in dict_data:
            # Add default content type header
            self._default_headers["Content-Type"] = "application/json"

        """Do POST request"""
        return self._request(requests.post, dict_data)

    def put(self, dict_data):
        # Add content type header
        self._default_headers["Content-Type"] = "application/json"

        """Do PUT request"""
        return self._request(requests.put, dict_data)

    def delete(self, dict_data):
        # Add content type header
        self._default_headers["Content-Type"] = "application/json"

        """Do delete HTTP-request"""
        return self._request(requests.delete, dict_data)

    def patch(self, dict_data):
        # Add content type header
        self._default_headers["Content-Type"] = "application/json-patch+json"

        """Do patch HTTP-patch"""
        return self._request(requests.patch, dict_data)

    def _set_headers(self):
        """Sets default headers"""

        if self.beyond:
            self._default_headers["Accept"] = "application/hal+json"
        else:
            self._default_headers["Accept"] = "application/vnd.epages.v1+json"

        # If token is set, add it to the Authorization header
        if self.token != "":
            self._default_headers["Authorization"] = "Bearer " + self.token

    def _check_input_dictionary(self, dict_data):
        '''Check that path, query and data are set in request dictionary and return values as list
        Args:
            dict_data request dictionary
        Return:
            a list of values
        '''
        if 'path' in dict_data:
            path = dict_data['path']
            logging.debug('path: ' + str(path))
        else:
            raise ValueError("Path was not set in the request dictionary")

        if 'query' in dict_data:
            query = dict_data['query']
            logging.debug('query: ' + str(path))
        else:
            raise ValueError("Query was not set in the request dictionary")

        if 'data' in dict_data:
            data = dict_data['data']
            logging.debug('data: ' + str(data))
        else:
            raise ValueError("Data was not set in the request dictionary")

        return (path, query, data)

    def _request(self, http_method_func, dict_data):
        """Executes a HTTP request.
        Args:
            http_method_func (object): HTTP request method for requests.
            dict_data (dict): Data to a server.
        Return:
            Dictionary
        """

        path, query, data = self._check_input_dictionary(dict_data)
        headers = self._default_headers
        request_url = self.api_url + path
        logging.debug('request_url: ' + request_url)

        # If use_data is specified for this particular request, the data must
        # be sent using the data argument.
        if "use_data" in dict_data and dict_data["use_data"] == 1:
            response = http_method_func(
                request_url, params=query, data=data, headers=headers)

        # If use_files is specified or this particular request, the data must
        # be sent using the files argument
        elif "use_files" in dict_data and dict_data["use_files"] == 1:
            response = http_method_func(
                request_url, params=query, files=data, headers=headers)

        # The default and most used way is to send data using json argument.
        else:
            response = http_method_func(
                request_url, params=query, json=data, headers=headers)

        # Accepted when status in 2xx
        if str(response.status_code)[0] == '2':
            # If status code is 204 ("No content"), don't try to convert it to json,
            # because there isn't anything to convert.
            if str(response.status_code)[:3] == "204":
                response_dictionary = {
                    "Message": "Operation completed succesfully."}
            else:
                response_dictionary = response.json()
                # Some special cases will be added to the responce dictionary from response header
                if 'X-ePages-Cart-Token' in response.headers.keys():
                    response_dictionary['X-ePages-Cart-Token'] = response.headers['X-ePages-Cart-Token']
        else:
            error_message = "HTTP-request failed. Response status was " + \
                str(response.status_code)
            logging.error(error_message)
            raise RuntimeError(error_message)

        return response_dictionary
