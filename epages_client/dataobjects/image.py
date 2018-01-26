# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import validators
from .data_object import DataObject


class Image(DataObject):
    '''Data object for Image object'''

    def __init__(self):
        # string The URL of an image.
        self._url = None
        # string Specifies the image. Can be Thumbnail, Small, HotDeal, MediumSmall, Medium, MediumLarge, Large.
        self._classifier = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = self._check_url(value)

    @property
    def classifier(self):
        return self._classifier

    @classifier.setter
    def classifier(self, value):
        if value in ('Thumbnail', 'Small', 'HotDeal', 'MediumSmall', 'Medium', 'MediumLarge', 'Large'):
            self._classifier = value
        else:
            err_msg = "Classifier value must be: 'Thumbnail', 'Small', 'HotDeal', " \
                      "'MediumSmall', 'Medium', 'MediumLarge', or 'Large'"
            raise ValueError(err_msg)

    def is_valid(self):
        return self._url != None
