# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from six import string_types
from .remove_value import RemoveValue
from .enum_fetch_operator import FetchOperator
import validators


class DataObject(object):
    '''Base class for all data_object classes'''

    def get_dict(self):
        '''
        Go over all values of object's _-named variables (and not None) and creates dictionary.
        The keys of the dictionary are variable names without "_"-mark.
        Return:
            Disctionary
        '''
        self_values = self.__dict__
        data_dict = {}

        for key in self_values:
            if key[0] == '_' and self_values[key] != None:
                # Removes "_" from a variable name
                data_dict[key[1:]] = self_values[key]
            elif type(self_values[key]) in (RemoveValue,):
                data_dict[key] = self_values[key]
            elif isinstance(self_values[key], DataObject):
                obj_contents = self_values[key].get_dict()

                if obj_contents:  # pass empty lists and dictonaries
                    data_dict[key] = obj_contents

        return data_dict

    def get_list_of_json_patches(self, legal_operations):
        '''Go over all the variables of the data_object and return it like json_patch commands
        Return:
            A list of objects
        '''
        list_of_json_patches = []
        for key, value in self.get_dict().items():
            if value != {}:  # pass empty dict
                json_patch = {}

                # Replace underscores on key with a slash
                key = key.replace("_", "/")

                path = "/" + key
                json_patch['path'] = path
                if isinstance(value, RemoveValue):
                    if FetchOperator.REMOVE in legal_operations[path]:
                        json_patch['op'] = "remove"
                    else:
                        raise ValueError(path + " cannot remove")
                else:
                    if FetchOperator.ADD in legal_operations[path]:
                        json_patch['op'] = "add"
                        json_patch['value'] = value
                    elif FetchOperator.REPLACE in legal_operations[path]:
                        json_patch['op'] = "replace"
                        json_patch['value'] = value
                    else:
                        raise ValueError(
                            "There is not a valid fetch operator for " + path)
                list_of_json_patches.append(json_patch)
        return list_of_json_patches

    def _check_email(self, value, error_msg=None, allow_remove_value=False):
        '''Return given value as str (email) if the value is valid e-mail address. Otherwise throws ValueError.'''

        if validators.email(value) or (allow_remove_value and isinstance(value, RemoveValue)):
            return value
        else:
            error_msg = error_msg or "The given value is not a valid email address"
            raise ValueError(error_msg)

    def _check_url(self, value, error_msg=None, allow_remove_value=False):
        '''Return given value as str (URL) if the value is valid url. Otherwise throws ValueError.'''

        if validators.url(value):
            return value
        else:
            error_msg = error_msg or "A given value is not a valid url."
            raise ValueError(error_msg)

    def _check_str(self, value, error_msg=None, allow_remove_value=False):
        '''Return given value if the value is type of str. Otherwise throws TypeError.'''
        error_msg = error_msg or 'A given value is not str'  # TODO: str(value)
        allow_types = string_types
        return self._check_type(value, error_msg, allow_types, allow_remove_value)

    def _check_bool(self, value, error_msg=None, allow_remove_value=False):
        '''Return given value if the value is type of bool. Otherwise throws TypeError.'''
        error_msg = error_msg or 'A given value is not bool.'  # TODO: str(value)
        allow_types = (bool,)
        return self._check_type(value, error_msg, allow_types, allow_remove_value)

    def _check_numeric(self, value, error_msg=None, allow_remove_value=False):
        '''Return given value if the value is type of int or float. Otherwise throws TypeError.'''
        error_msg = error_msg or 'A given value is not numeric'  # TODO: str(value)
        allow_types = (int, float)
        return self._check_type(value, error_msg, allow_types, allow_remove_value)

    def _check_type(self, value, error_msg, allowed_types, allow_remove_value):
        '''Return given value if the value is type of allowed types or allow_remove_value is true and value is instance of RemoveValue. Otherwise throws TypeError.'''
        if isinstance(value, allowed_types) or (allow_remove_value and isinstance(value, RemoveValue)):
            return value
        else:
            raise TypeError(error_msg)

    def is_valid(self):
        '''Remember overwrite'''
        pass
