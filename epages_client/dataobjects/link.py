# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class Link(DataObject):
    """Data object for Link object"""

    def __init__(self):
        # string The link relation that describes how the link relates to the call.
        self._rel = None
        # string The URL of the related link that can be used for subsequent calls.
        self._href = None
        # string The title of the item that is linked. (optional)
        self._title = None

    @property
    def rel(self):
        return self._rel

    @rel.setter
    def rel(self, value):
        self._rel = self._check_str(value)

    @property
    def href(self):
        return self._href

    @href.setter
    def href(self, value):
        self._href = self._check_url(value)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = self._check_str(value)

    def is_valid(self):
        return self._rel != None and self._href != None
