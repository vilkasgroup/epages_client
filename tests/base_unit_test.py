# -*- coding: utf-8 -*-
import os
import unittest

# Check if environment variables are set
envcheck = unittest.skipUnless(
    os.environ.get('EPAGES_API_URL', False) and
    os.environ.get('EPAGES_API_TOKEN', False), 'Environment variables not set'
)


@envcheck
class BaseUnitTest(unittest.TestCase):

    def assert_count_items_equal(self, param_1, param_2):
        '''
        A function to use either assertCountEqual or assertItemsEqual
        depending on Python version.
        '''

        try:
            # Python 3.x
            self.assertCountEqual(param_1, param_2)
        except AttributeError:
            # Python 2.x
            self.assertItemsEqual(param_1, param_2)
