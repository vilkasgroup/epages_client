# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class ContentPage(DataObject):
    '''Data object for creating a content page to ePages webshop'''

    def __init__(self):
        # string The name that appears on the page.
        self._name = None
        # string The name of the page, that appears on the browser tab.
        self._title = None
        # string The name of the page, that appears in the navigation bar.
        self._navigationCaption = None
        # string Additional short information that can be given to better explain what’s on the page.
        self._shortDescription = None
        # string Information on the topic of the page.
        self._description = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._check_str(value, "Name has to be a str.")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = self._check_str(value, "Title has to be a str.")

    @property
    def navigationCaption(self):
        return self._navigationCaption

    @navigationCaption.setter
    def navigationCaption(self, value):
        self._navigationCaption = self._check_str(
            value, "NavigationCaption has to be a str.")

    @property
    def shortDescription(self):
        return self._shortDescription

    @shortDescription.setter
    def shortDescription(self, value):
        self._shortDescription = self._check_str(
            value, "ShortDescription has to be a str.")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = self._check_str(
            value,  "Description has to be a str.")

    def is_valid(self):
        return True
