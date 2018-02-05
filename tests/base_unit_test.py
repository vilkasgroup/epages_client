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

    def get_resources_path(self):
        # Return path for resource files

        # Get the directory where this file is located
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Set the resources directory where id files and test image are located
        resources_path = os.path.join(dir_path, "resources")

        # If the resources directory doesn't exist, raise an error
        if not os.path.exists(resources_path):
            raise OSError("Resources directory %s not found." %
                          (resources_path,))

        return resources_path

    def save_resource(self, filename, content, overwrite=True):
        # Save file to resource path

        file_path = os.path.join(self.get_resources_path(), filename)

        if overwrite == False and os.path.isfile(file_path):
            raise RuntimeError("File %s already exists" % (file_path,))

        try:
            fh = open(file_path, "w")
            fh.write(content)
            fh.close()
        except IOError:
            print("File %s couldn't be created." % (file_path,))

    def get_resource(self, filename):

        file_path = os.path.join(self.get_resources_path(), filename)

        if os.path.isfile(file_path) == False:
            raise RuntimeError("File %s not found" % (file_path,))

        with open(file_path, 'r') as read_file:
            content = read_file.read()

        return content
