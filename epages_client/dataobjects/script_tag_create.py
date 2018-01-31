# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class ScriptTagCreate(DataObject):
    ''''Data object for creating a new script tag to ePages webshop'''

    def __init__(self):

        # string The URL of the script.
        self._scriptUrl = None

    @property
    def scriptUrl(self):
        return self._scriptUrl

    @scriptUrl.setter
    def scriptUrl(self, value):
        self._scriptUrl = self._check_url(value)

    def is_valid(self):

        # Script url must be set always
        if not self._scriptUrl:
            return False
        else:
            return True
