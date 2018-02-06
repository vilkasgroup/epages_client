# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import validators
from .data_object import DataObject


class ContactInfo(DataObject):
    '''Data object for creating a Contact info to ePages webshop'''

    def __init__(self):
        # string The name that appears on the contact information page, e.g. Contact Us.
        self._name = None
        # string The name of the contact information page, that appears on the browser tab.
        self._title = None
        # string The name of the contact information page that appears in the navigation bar.
        self._navigationCaption = None
        # string Additional short information that can be given to e.g. better explain what’s on the contact information page.
        self._shortDescription = None
        # string Additional information that can be added to the contact information page, e.g. tax identification number or bank account.
        self._description = None
        # string The name of the shop.
        self._company = None
        # string The contact person for the shop, usually the shop owner.
        self._contactPerson = None
        # string The job title of the contact person.
        self._contactPersonJobTitle = None
        # string The postal address of the shop.
        self._address = None
        # string The phone number of the shop.
        self._phone = None
        # string The email address of the shop.
        self._email = None

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
        self._navigationCaption = self._check_str(value, "NavigationCaption has to be a str.")

    @property
    def shortDescription(self):
        return self._shortDescription

    @shortDescription.setter
    def shortDescription(self, value):
        self._shortDescription = self._check_str(value, "ShortDescription has to be a str.")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = self._check_str(value, "Description has to be a str.")

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = self._check_str(value, "Company has to be a str.")

    @property
    def contactPerson(self):
        return self._contactPerson

    @contactPerson.setter
    def contactPerson(self, value):
        self._contactPerson = self._check_str(value, "ContactPerson has to be a str.")

    @property
    def contactPersonJobTitle(self):
        return self._contactPersonJobTitle

    @contactPersonJobTitle.setter
    def contactPersonJobTitle(self, value):
        self._contactPersonJobTitle = self._check_str(value, "ContactPersonJobTitle has to be a str.")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = self._check_str(value, "Address has to be a str.")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = self._check_str(value, "Phone has to be a str.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = self._check_email(value, "Email has to be a valid email address.")

    def is_valid(self):
        return True
