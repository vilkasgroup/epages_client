# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from six import string_types
from .list_of_objects import ListOfObjects

class ProductSlideshowSequenceUpdate(ListOfObjects):
    """Data object for updating product slideshow sequence"""

    def __init__(self):
        super(ProductSlideshowSequenceUpdate, self).__init__(string_types)

    def get_dict(self):
        return self.get()
