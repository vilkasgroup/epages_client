# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class CategoryCreate(DataObject):
    '''Data object for creating a new category to ePages webshop'''

    def __init__(self):
        # string The name of the category.
        self._name = None
        # string The unique identifier of the new category. If already in use, the system will automatically increment by number, e.g. alias1, alias2.
        self._alias = None
        # string The page title of the category.
        self._pageTitle = None
        # string The description of the category.
        self._description = None
        # string The name of the category that appears in the navigation bar.
        self._navigationCaption = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._check_str(value, "Name has to be str.")

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = self._check_str(value, "Alias has to be str.")

    @property
    def pageTitle(self):
        return self._pageTitle

    @pageTitle.setter
    def pageTitle(self, value):
        self._pageTitle = self._check_str(value, "PageTitle has to be str.")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = self._check_str(
            value, "Description has to be str.")

    @property
    def navigationCaption(self):
        return self._navigationCaption

    @navigationCaption.setter
    def navigationCaption(self, value):
        self._navigationCaption = self._check_str(
            value, "NavigationCaption has to be str.")

    def is_valid(self):
        return True
