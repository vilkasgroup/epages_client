# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class CategoryUpdate(DataObject):
    '''Data object for updating a category to ePages webshop'''

    def __init__(self):
        # string The unique identifier of the category a product is assigned to.
        self._categoryId = None
        # string The name of the category.
        self._name = None
        # string The unique identifier of the category.
        self._alias = None
        # string The page title of this category.
        self._pageTitle = None
        # string The description of the category.
        self._description = None
        # string The name of the category page that appears in the navigation bar.
        self._navigationCaption = None
        # boolean Indicates if the category is displayed in the shop.
        self._visible = None

    @property
    def categoryId(self):
        return self._categoryId

    @categoryId.setter
    def categoryId(self, value):
        self._categoryId = self._check_str(
            value, "CategoryId has to be a str.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._check_str(value, "Name has to be a str.")

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = self._check_str(value, "Alias has to be a str.")

    @property
    def pageTitle(self):
        return self._pageTitle

    @pageTitle.setter
    def pageTitle(self, value):
        self._pageTitle = self._check_str(value, "PageTitle has to be a str.")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = self._check_str(
            value, "Description has to be a str.")

    @property
    def navigationCaption(self):
        return self._navigationCaption

    @navigationCaption.setter
    def navigationCaption(self, value):
        self._navigationCaption = self._check_str(
            value, "NavigationCaption has to be a str.")

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = self._check_bool(value, 'Visible has to be a bool.')

    def is_valid(self):

        # Category id and alias must be sent always when updating
        if not self._categoryId or not self._alias:
            return False
        else:
            return True
