# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from six import string_types
from .list_of_objects import ListOfObjects


class CategorySequenceUpdate(ListOfObjects):
    '''Data object for updating a catecory sequence to ePages webshop'''

    def __init__(self):
        super(CategorySequenceUpdate, self).__init__(string_types)

    def get_dict(self):
        return self.get()
