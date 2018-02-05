# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject


class Address(DataObject):
    '''Data object for creating an address object to ePages webshop api'''

    def __init__(self):
        self._company = None  # string The customer’s company.
        # string The customer’s salutation, e.g. Mr or Mrs.
        self._salutation = None
        # string The customer’s academic title, e.g. professor or PhD.
        self._title = None
        # string The customer’s first name.
        self._firstName = None
        # string The customer’s last name.
        self._lastName = None
        # string The street name of the customer’s address.
        self._street = None
        # string An additional field for the street address.
        self._streetDetails = None
        # string The zip or postal code of the address.
        self._zipCode = None
        # string The name of the city.
        self._city = None
        # string The name of the state.
        self._state = None
        # string The name of the country.
        self._country = None
        # string The Id of the VAT.
        self._vatId = None
        # string The customer’s date of birth.
        self._birthday = None
        # string The customer’s primary email address. This email address will be used by the merchant if the customer does not have a user account.
        self._emailAddress = None
        # string Further address details of the customer.
        self._addressExtension = None
        # string The name of the bank account holder.
        self._bankAccountHolder = None
        # string The bank account number.
        self._bankAccountNumber = None
        # string The name of the bank that holds the bank account.
        self._bankName = None
        # string The bank identifier code.
        self._bankSortCode = None
        # string The customer’s business email address.
        self._businessEmailAddress = None
        # string The customer’s business phone number.
        self._businessPhoneNumber = None
        # string The department of the company associated with the customer’s address.
        self._department = None
        # string Specifies the name to display for the customer name.
        self._displayName = None
        # string The door code associated with the customer’s address.
        self._doorCode = None
        # string The customer’s fax number.
        self._faxNumber = None
        # string The customer’s fiscal code.
        self._fiscalCode = None
        # string The customer’s gender. Can be either MALE or FEMALE.
        self._gender = None
        # string The customer’s job title.
        self._jobTitle = None
        # string The customer’s middle name.
        self._middleName = None
        # string The customer’s mobile phone number.
        self._mobilePhoneNumber = None
        # string The customer’s landline number.
        self._phoneNumber = None
        # string The customer’s private email address.
        self._privateEmailAddress = None
        # string The customer’s private phone number
        self._privatePhoneNumber = None
        # string The customer’s website URL.
        self._websiteUrl = None

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = self._check_str(value, "Company has to be a str.")

    @property
    def salutation(self):
        return self._salutation

    @salutation.setter
    def salutation(self, value):
        self._salutation = self._check_str(value, "Salutation has to be a str.")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = self._check_str(value, "Title has to be a str.")

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        self._firstName = self._check_str(value, "FirstName has to be a str.")

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        self._lastName = self._check_str(value, "LastName has to be a str.")

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = self._check_str(value, "Street has to be a str.")

    @property
    def streetDetails(self):
        return self._streetDetails

    @streetDetails.setter
    def streetDetails(self, value):
        self._streetDetails = self._check_str(
            value, "StreetDetails has to be a str.")

    @property
    def zipCode(self):
        return self._zipCode

    @zipCode.setter
    def zipCode(self, value):
        self._zipCode = self._check_str(value, "ZipCode has to be a str.")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = self._check_str(value, "City has to be a str.")

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = self._check_str(value, "State has to be a str.")

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = self._check_str(value, "Country has to be a str.")

    @property
    def vatId(self):
        return self._vatId

    @vatId.setter
    def vatId(self, value):
        self._vatId = self._check_str(value, "VatId has to be a str.")

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = self._check_str(value, "Birthday has to be a str.")

    @property
    def emailAddress(self):
        return self._emailAddress

    @emailAddress.setter
    def emailAddress(self, value):
        self._emailAddress = self._check_email(
            value, "EmailAddress has to be a valid email address.")

    @property
    def addressExtension(self):
        return self._addressExtension

    @addressExtension.setter
    def addressExtension(self, value):
        self._addressExtension = self._check_str(
            value, "AddressExtension has to be a str.")

    @property
    def bankAccountHolder(self):
        return self._bankAccountHolder

    @bankAccountHolder.setter
    def bankAccountHolder(self, value):
        self._bankAccountHolder = self._check_str(
            value, "BankAccountHolder has to be a str.")

    @property
    def bankAccountNumber(self):
        return self._bankAccountNumber

    @bankAccountNumber.setter
    def bankAccountNumber(self, value):
        self._bankAccountNumber = self._check_str(
            value, "BankAccountNumber has to be a str.")

    @property
    def bankName(self):
        return self._bankName

    @bankName.setter
    def bankName(self, value):
        self._bankName = self._check_str(value, "BankName has to be a str.")

    @property
    def bankSortCode(self):
        return self._bankSortCode

    @bankSortCode.setter
    def bankSortCode(self, value):
        self._bankSortCode = self._check_str(
            value, "BankSortCode has to be a str.")

    @property
    def businessEmailAddress(self):
        return self._businessEmailAddress

    @businessEmailAddress.setter
    def businessEmailAddress(self, value):
        self._businessEmailAddress = self._check_email(
            value, "BusinessEmailAddress has to be a valid email address.")

    @property
    def businessPhoneNumber(self):
        return self._businessPhoneNumber

    @businessPhoneNumber.setter
    def businessPhoneNumber(self, value):
        self._businessPhoneNumber = self._check_str(
            value, "BusinessPhoneNumber has to be a str.")

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = self._check_str(value, "Department has to be a str.")

    @property
    def displayName(self):
        return self._displayName

    @displayName.setter
    def displayName(self, value):
        self._displayName = self._check_str(
            value, "DisplayName has to be a str.")

    @property
    def doorCode(self):
        return self._doorCode

    @doorCode.setter
    def doorCode(self, value):
        self._doorCode = self._check_str(value, "DoorCode has to be a str.")

    @property
    def faxNumber(self):
        return self._faxNumber

    @faxNumber.setter
    def faxNumber(self, value):
        self._faxNumber = self._check_str(value, "FaxNumber has to be a str.")

    @property
    def fiscalCode(self):
        return self._fiscalCode

    @fiscalCode.setter
    def fiscalCode(self, value):
        self._fiscalCode = self._check_str(value, "FiscalCode has to be a str.")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value in ('MALE', 'FEMALE'):
            self._gender = value
        else:
            raise ValueError(
                "The customer’s gender can be either MALE or FEMALE (str).")

    @property
    def jobTitle(self):
        return self._jobTitle

    @jobTitle.setter
    def jobTitle(self, value):
        self._jobTitle = self._check_str(value, "JobTitle has to be a str.")

    @property
    def middleName(self):
        return self._middleName

    @middleName.setter
    def middleName(self, value):
        self._middleName = self._check_str(value, "MiddleName has to be a str.")

    @property
    def mobilePhoneNumber(self):
        return self._mobilePhoneNumber

    @mobilePhoneNumber.setter
    def mobilePhoneNumber(self, value):
        self._mobilePhoneNumber = self._check_str(
            value, "MobilePhoneNumber has to be a str.")

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, value):
        self._phoneNumber = self._check_str(
            value, "PhoneNumber has to be a str.")

    @property
    def privateEmailAddress(self):
        return self._privateEmailAddress

    @privateEmailAddress.setter
    def privateEmailAddress(self, value):
        self._privateEmailAddress = self._check_email(
            value, "PrivateEmailAddress has to be a valid email address.")

    @property
    def privatePhoneNumber(self):
        return self._privatePhoneNumber

    @privatePhoneNumber.setter
    def privatePhoneNumber(self, value):
        self._privatePhoneNumber = self._check_str(
            value, "PrivatePhoneNumber has to be a str.")

    @property
    def websiteUrl(self):
        return self._websiteUrl

    @websiteUrl.setter
    def websiteUrl(self, value):
        self._websiteUrl = self._check_url(
            value, "WebsiteUrl has to be a valid url address.")

    def is_valid(self):
        return True
