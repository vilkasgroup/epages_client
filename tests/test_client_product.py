# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import time
import unittest
import uuid

# import base class for unit testing
from .base_unit_test import BaseUnitTest

# import the package
import epages_client

# import the RestClient class
from epages_client.client import RestClient

# import the Category create class from dataobjects
from epages_client.dataobjects.category_create import CategoryCreate

# import the Category update class from dataobjects
from epages_client.dataobjects.category_update import CategoryUpdate

# import the Category sequence update class from dataobjects
from epages_client.dataobjects.category_sequence_update import CategorySequenceUpdate

# import the Product create class from dataobjects
from epages_client.dataobjects.product_create import ProductCreate

# import the Product patch class from dataobjects
from epages_client.dataobjects.product_update import ProductUpdate

# import the Product image sequence update class from dataobjects
from epages_client.dataobjects.product_slideshow_sequence_update import ProductSlideshowSequenceUpdate

from random import shuffle

skip_test = unittest.skipUnless(
    os.environ.get('EPAGES_RUN_ALL_TESTS', False), 'Skipping test.'
)


class TestProductMethods(BaseUnitTest):
    '''A class for testing product related methods on RestClient class'''

    # Get the directory where this file is located
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Set the resources directory where id files and test image are located
    resources = os.path.join(dir_path, "resources")

    # If the resources directory doesn't exist, raise an error
    if not os.path.exists(resources):
        raise OSError("Resources directory not found.")

    # Add category.txt to the resources path
    category_file = os.path.join(resources, "category.txt")

    # Add product.txt to the resources path
    product_file = os.path.join(resources, "product.txt")

    # The paths for the test images
    images = [
        os.path.join(resources, "test.jpg"),
        os.path.join(resources, "test2.jpg"),
        os.path.join(resources, "test3.jpg")
    ]

    # Loop images and check that every one of them is found
    for image in images:
        if not os.path.isfile(image):
            raise OSError("Image file '" + image + "' not found.")

    def get_category_ids(self):
        '''A function to get category ids from a text file.'''

        categories = []

        # Check if the category file is found and get the categories
        try:
            fh = open(self.category_file, "r")

            # Get lines to list
            lines = fh.read().splitlines()

            # Loop lines
            for line in lines:
                categories.append(line)

            fh.close()
        except FileNotFoundError:
            raise FileNotFoundError("Category file not found.")

        return categories

    def get_product_id(self):
        '''A function to get product id from a text file.'''

        product_id = ""

        try:
            fh = open(self.product_file, "r")
            product_id = fh.read()
            fh.close()
        except FileNotFoundError:
            raise FileNotFoundError("Product file not found.")

        return product_id

    def setUp(self):

        self.client = RestClient(
            os.environ["EPAGES_API_URL"], os.environ["EPAGES_API_TOKEN"])

        self.params = {
            "query": {},
            "param1": "",
            "param2": ""
        }

    def test_001_add_category_invalid_object(self):

        self.params["object"] = None

        with self.assertRaises(TypeError) as e:
            response = self.client.add_category(self.params)

    def test_002_add_category_no_root_category_id(self):

        category = CategoryCreate()
        self.params["object"] = category

        with self.assertRaises(ValueError) as e:
            response = self.client.add_category(self.params)

    def test_003_add_category(self):

        # Get categories
        categories = self.client.get_categories(self.params)

        # Get the id of the root category in the shop
        self.params["param1"] = categories[0]["categoryId"]

        category = CategoryCreate()
        self.params["object"] = category

        response = self.client.add_category(self.params)

        self.assertEqual(isinstance(response, dict), True)

        category_id = response["categoryId"]

        # Try to write the category id to the category file
        try:
            fh = open(self.category_file, "w")
            fh.write(category_id)
            fh.close()
        except IOError:
            print("Category file couldn't be created.")

    def test_004_add_category_2(self):

        # Wait for 1 second before creating a new category
        time.sleep(1)

        # Get categories
        categories = self.client.get_categories(self.params)

        # Get the id of the root category in the shop
        self.params["param1"] = categories[0]["categoryId"]

        category = CategoryCreate()
        self.params["object"] = category

        response = self.client.add_category(self.params)

        self.assertEqual(isinstance(response, dict), True)

        category_id = response["categoryId"]

        # Try to write the category id to the category file
        try:
            fh = open(self.category_file, "a")
            fh.write("\n" + category_id)
            fh.close()
        except IOError:
            print("Category file couldn't be opened.")

    def test_005_add_category_3(self):

        # Wait for 1 second before creating a new category
        time.sleep(1)

        # Get categories
        categories = self.client.get_categories(self.params)

        # Get the id of the root category in the shop
        self.params["param1"] = categories[0]["categoryId"]

        category = CategoryCreate()
        self.params["object"] = category

        response = self.client.add_category(self.params)

        self.assertEqual(isinstance(response, dict), True)

        category_id = response["categoryId"]

        # Try to write the category id to the category file
        try:
            fh = open(self.category_file, "a")
            fh.write("\n" + category_id)
            fh.close()
        except IOError:
            print("Category file couldn't be opened.")

    def test_006_add_product_no_object(self):

        with self.assertRaises(RuntimeError) as e:
            response = self.client.add_product(self.params)

    def test_007_add_product_invalid_object(self):

        self.params["object"] = None

        with self.assertRaises(TypeError) as e:
            response = self.client.add_product(self.params)

    def test_008_add_product_no_product_number(self):

        product = ProductCreate()

        self.params["object"] = product

        with self.assertRaises(ValueError) as e:
            response = self.client.add_product(self.params)

    def test_009_add_product(self):

        unique_id = str(uuid.uuid4())

        product = ProductCreate()
        product.productNumber = unique_id
        product.name = unique_id

        self.params["object"] = product

        response = self.client.add_product(self.params)

        self.assertEqual(isinstance(response, dict), True)

        product_id = response["productId"]

        # Try to write the product id to the product file
        try:
            fh = open(self.product_file, "w")
            fh.write(product_id)
            fh.close()
        except IOError:
            print("Product file couldn't be created.")

    def test_010_get_shop_info(self):

        shop_info = self.client.get_shop_info(self.params)

        self.assertEqual(isinstance(shop_info, dict), True)

    def test_011_get_categories(self):

        categories = self.client.get_categories(self.params)

        self.assertEqual(isinstance(categories, list), True)

    def test_012_get_category_no_id(self):

        with self.assertRaises(ValueError) as e:
            category = self.client.get_category(self.params)

    def test_013_get_category_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            category = self.client.get_category(self.params)

    def test_014_get_category_correct_id(self):

        # Get all categories
        categories = self.client.get_categories(self.params)

        # Set category id to be the id of the first category
        self.params["param1"] = categories[0]["categoryId"]

        category = self.client.get_category(self.params)

        self.assertEqual(isinstance(category, dict), True)

    def test_015_get_currencies(self):

        currencies = self.client.get_currencies(self.params)

        self.assertEqual(isinstance(currencies, dict), True)

    def test_016_get_locales(self):

        locales = self.client.get_locales(self.params)

        self.assertEqual(isinstance(locales, dict), True)

    def test_017_get_products(self):

        # Set currency just to test currency setter
        self.client.currency = "GBP"
        
        products = self.client.get_products(self.params)

        self.assertEqual(isinstance(products, dict), True)

    def test_018_get_product_no_id(self):

        with self.assertRaises(ValueError) as e:
            product = self.client.get_product(self.params)

    def test_019_get_product_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            product = self.client.get_product(self.params)

    def test_020_get_product_correct_id(self):

        product_id = self.get_product_id()

        self.params["param1"] = product_id

        product = self.client.get_product(self.params)

        self.assertEqual(isinstance(product, dict), True)

    def test_021_get_product_variations_no_id(self):

        with self.assertRaises(ValueError) as e:
            variations = self.client.get_product_variations(self.params)

    def test_022_get_product_variations_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            variations = self.client.get_product_variations(self.params)

    @skip_test
    def test_023_get_product_variations_correct_id(self):

        # Here the product id is hard-coded, because there
        # isn't a way to get a product with variations
        self.params["param1"] = "5A4B8CC7-B4F1-236C-5497-0A2810120FFD"

        variations = self.client.get_product_variations(self.params)

        self.assertEqual(isinstance(variations, dict), True)

    def test_024_upload_product_image_no_id(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.upload_product_image(self.params)

    def test_025_upload_product_image_no_data(self):

        product_id = self.get_product_id()

        self.params["param1"] = product_id

        with self.assertRaises(RuntimeError) as e:
            response = self.client.upload_product_image(self.params)

    def test_026_upload_product_image_1(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        image = open(self.images[0], 'rb')
        self.params["data"] = {'image': image}

        response = self.client.upload_product_image(self.params)

        image.close()

        self.assertEqual(isinstance(response, dict), True)

    def test_027_upload_product_image_2(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        image = open(self.images[1], 'rb')
        self.params["data"] = {'image': image}

        response = self.client.upload_product_image(self.params)

        image.close()

        self.assertEqual(isinstance(response, dict), True)

    def test_028_upload_product_image_3(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        image = open(self.images[2], 'rb')
        self.params["data"] = {'image': image}

        response = self.client.upload_product_image(self.params)

        image.close()

        self.assertEqual(isinstance(response, dict), True)

    def test_029_get_product_images_no_id(self):

        with self.assertRaises(ValueError) as e:
            images = self.client.get_product_images(self.params)

    def test_030_get_product_images_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            images = self.client.get_product_images(self.params)

    def test_031_get_product_images_correct_id(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        images = self.client.get_product_images(self.params)

        self.assertEqual(isinstance(images, dict), True)

    def test_032_get_product_image_names_no_id(self):

        with self.assertRaises(ValueError) as e:
            images = self.client.get_product_image_names(self.params)

    def test_033_get_product_image_names_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            images = self.client.get_product_image_names(self.params)

    def test_034_get_product_image_names_correct_id(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        images = self.client.get_product_image_names(self.params)

        self.assertEqual(isinstance(images, list), True)

    def test_035_get_product_custom_attributes_no_id(self):

        with self.assertRaises(ValueError) as e:
            attributes = self.client.get_product_custom_attributes(self.params)

    def test_036_get_product_custom_attributes_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            attributes = self.client.get_product_custom_attributes(self.params)

    @skip_test
    def test_037_get_product_custom_attributes_correct_id(self):

        # Get products
        products = self.client.get_products(self.params)

        # Set product id to be the id of the first product
        self.params["param1"] = products["items"][0]["productId"]

        attributes = self.client.get_product_custom_attributes(self.params)

        self.assertEqual(isinstance(attributes, dict), True)

    def test_038_get_product_lowest_price_no_id(self):

        with self.assertRaises(ValueError) as e:
            lowest_price = self.client.get_product_lowest_price(self.params)

    def test_039_get_product_lowest_price_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            lowest_price = self.client.get_product_lowest_price(self.params)

    @skip_test
    def test_040_get_product_lowest_price_correct_id(self):

        # Here the product id is hard-coded, because there
        # isn't a way to get a product with variations
        self.params["param1"] = "5A4B8CC7-B4F1-236C-5497-0A2810120FFD"

        lowest_price = self.client.get_product_lowest_price(self.params)

        self.assertEqual(isinstance(lowest_price, dict), True)

    def test_041_search_products_no_query(self):

        with self.assertRaises(ValueError) as e:
            search_results = self.client.search_products(self.params)

    def test_042_search_products_empty_query(self):

        self.params["query"] = {"query": ""}

        with self.assertRaises(ValueError) as e:
            search_results = self.client.search_products(self.params)

    def test_043_search_products(self):

        self.params["query"] = {"query": "snap"}

        search_results = self.client.search_products(self.params)

        self.assertEqual(isinstance(search_results, dict), True)

    def test_044_get_shipping_methods(self):

        shipping_methods = self.client.get_shipping_methods(self.params)

        self.assertEqual(isinstance(shipping_methods, list), True)

    def test_045_get_shipping_method_no_id(self):

        with self.assertRaises(ValueError) as e:
            shipping_method = self.client.get_shipping_method(self.params)

    def test_046_get_shipping_method_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            shipping_method = self.client.get_shipping_method(self.params)

    def test_047_get_shipping_method_correct_id(self):

        # Get all shipping methods
        shipping_methods = self.client.get_shipping_methods(self.params)

        # Set shipping method id to be the id of the first shipping method
        self.params["param1"] = shipping_methods[0]["shippingMethodId"]

        shipping_method = self.client.get_shipping_method(self.params)

        self.assertEqual(isinstance(shipping_method, dict), True)

    def test_048_get_tax_classes(self):

        tax_classes = self.client.get_tax_classes(self.params)

        self.assertEqual(isinstance(tax_classes, dict), True)

    def test_049_get_tax_class_no_id(self):

        with self.assertRaises(ValueError) as e:
            tax_class = self.client.get_tax_class(self.params)

    def test_050_get_tax_class_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            tax_class = self.client.get_tax_class(self.params)

    def test_051_get_tax_class_correct_id(self):

        # Get all tax classes
        tax_classes = self.client.get_tax_classes(self.params)

        # Set tax class id to be the id of the first tax class
        self.params["param1"] = tax_classes["items"][0]["taxClassId"]

        tax_class = self.client.get_tax_class(self.params)

        self.assertEqual(isinstance(tax_class, dict), True)

    def test_052_get_tax_model(self):

        tax_model = self.client.get_tax_model(self.params)

        self.assertEqual(isinstance(tax_model, dict), True)

    def test_053_update_category_no_id(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.update_category(self.params)

    def test_054_update_category_no_object(self):

        categories = self.get_category_ids()
        self.params["param1"] = categories[0]

        with self.assertRaises(RuntimeError) as e:
            response = self.client.update_category(self.params)

    def test_055_update_category_invalid_object(self):

        categories = self.get_category_ids()
        self.params["param1"] = categories[0]
        self.params["object"] = None

        with self.assertRaises(TypeError) as e:
            response = self.client.update_category(self.params)

    def test_056_update_category_empty_object(self):
        '''When updating a category, the object must have category id and
        alias set. The category id must be the same that is in the url for
        updating category.'''

        categories = self.get_category_ids()
        self.params["param1"] = categories[0]
        self.params["object"] = CategoryUpdate()

        with self.assertRaises(ValueError) as e:
            response = self.client.update_category(self.params)

    def test_057_update_category_object_without_alias(self):

        categories = self.get_category_ids()
        self.params["param1"] = categories[0]

        category = CategoryUpdate()
        category.categoryId = categories[0]

        self.params["object"] = category

        with self.assertRaises(ValueError) as e:
            response = self.client.update_category(self.params)

    def test_058_update_category_mismatching_ids(self):
        '''In this test, both required variables are set, but category id
        has wrong value.'''

        categories = self.get_category_ids()

        # Correct category id is set to the final API path
        self.params["param1"] = categories[0]

        category = CategoryUpdate()

        # False category id is set to the object, and it causes mismatching ids error
        category.categoryId = str(uuid.uuid4())
        category.alias = str(uuid.uuid4())

        self.params["object"] = category

        with self.assertRaises(RuntimeError) as e:
            response = self.client.update_category(self.params)

    def test_059_update_category(self):

        categories = self.get_category_ids()
        self.params["param1"] = categories[0]

        category = CategoryUpdate()
        category.categoryId = categories[0]
        category.alias = str(uuid.uuid4())

        self.params["object"] = category

        response = self.client.update_category(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_060_get_subcategory_sequence_no_id(self):

        with self.assertRaises(ValueError) as e:
            sequence = self.client.get_subcategory_sequence(self.params)

    def test_061_get_subcategory_sequence_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            sequence = self.client.get_subcategory_sequence(self.params)

    def test_062_get_subcategory_sequence_correct_id(self):

        # Get all categories
        categories = self.client.get_categories(self.params)

        # Set category id to be the id of the first category
        self.params["param1"] = categories[0]["categoryId"]

        sequence = self.client.get_subcategory_sequence(self.params)

        self.assertEqual(isinstance(sequence, list), True)

    def test_063_update_subcategory_sequence_no_id(self):

        with self.assertRaises(ValueError) as e:
            sequence = self.client.update_subcategory_sequence(self.params)

    def test_064_update_subcategory_sequence_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            sequence = self.client.update_subcategory_sequence(self.params)

    def test_065_update_subcategory_sequence_no_list(self):

        # Get all categories
        categories = self.client.get_categories(self.params)

        # Set category id to be the id of the first category
        self.params["param1"] = categories[0]["categoryId"]

        with self.assertRaises(RuntimeError) as e:
            response = self.client.update_subcategory_sequence(self.params)

    def test_066_update_subcategory_sequence_false_list(self):

        # Get all categories
        categories = self.client.get_categories(self.params)

        # Set category id to be the id of the first category
        self.params["param1"] = categories[0]["categoryId"]

        # Get the current subcategory sequence
        sequence = self.client.get_subcategory_sequence(self.params)

        # Add random item to the list to make sure this test fails
        sequence.append('testing')

        with self.assertRaises(RuntimeError) as e:
            response = self.client.update_subcategory_sequence(self.params)

    def test_067_update_subcategory_sequence_correct_id_and_list(self):

        # Get all categories
        categories = self.client.get_categories(self.params)

        # Set category id to be the id of the first category
        self.params["param1"] = categories[0]["categoryId"]

        # Get the category sequence
        sequence = self.client.get_subcategory_sequence(self.params)

        # Shuffle the sequence of categories
        shuffle(sequence)

        # Get the instance of category sequence update
        csu = CategorySequenceUpdate()

        # Loop shuffled categories and add them to the object
        for category in sequence:
            csu.add(category)

        # Add the object to the params
        self.params["object"] = csu

        response = self.client.update_subcategory_sequence(self.params)

        self.assertEqual(isinstance(response, list), True)

    def test_068_update_product_no_id(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.update_product(self.params)

    def test_069_update_product_no_object(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        with self.assertRaises(RuntimeError) as e:
            response = self.client.update_product(self.params)

    def test_070_update_product_invalid_object(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        self.params["object"] = None

        with self.assertRaises(TypeError) as e:
            response = self.client.update_product(self.params)

    def test_071_update_product(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        product = ProductUpdate()
        product.price = 29.90
        product.stocklevel = 5

        self.params["object"] = product

        response = self.client.update_product(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_072_update_product_image_sequence_no_id(self):

        with self.assertRaises(ValueError) as e:
            sequence = self.client.update_product_image_sequence(self.params)

    def test_073_update_product_image_sequence_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            sequence = self.client.update_product_image_sequence(self.params)

    def test_074_update_product_image_sequence_no_list(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        with self.assertRaises(RuntimeError) as e:
            response = self.client.update_product_image_sequence(self.params)

    def test_075_update_product_image_sequence_false_list(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        # Get the current subcategory sequence
        sequence = self.client.get_product_image_names(self.params)

        # Add random item to the list to make sure this test fails
        sequence.append('testing')

        with self.assertRaises(RuntimeError) as e:
            response = self.client.update_product_image_sequence(self.params)

    def test_076_update_product_image_sequence_correct_id_and_list(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        # Get the image sequence
        sequence = self.client.get_product_image_names(self.params)

        # Shuffle the sequence of images
        shuffle(sequence)

        # Get the instance of product slideshow sequence update
        pssu = ProductSlideshowSequenceUpdate()

        # Loop shuffled images and add them to the object
        for image in sequence:
            pssu.add(image)

        # Add the object to the params
        self.params["object"] = pssu

        response = self.client.update_product_image_sequence(self.params)

        self.assertEqual(isinstance(response, list), True)

    def test_077_delete_product_image_no_id(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.delete_product_image(self.params)

    def test_078_delete_product_image_false_id(self):

        self.params["param1"] = str(uuid.uuid4())
        self.params["param2"] = os.path.basename(self.images[0])

        with self.assertRaises(RuntimeError) as e:
            response = self.client.delete_product_image(self.params)

    def test_079_delete_product_image_no_name(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        with self.assertRaises(ValueError) as e:
            response = self.client.delete_product_image(self.params)

    def test_080_delete_product_image_false_name(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id
        self.params["param2"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            response = self.client.delete_product_image(self.params)

    def test_081_delete_product_image_1(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id
        self.params["param2"] = os.path.basename(self.images[0])

        response = self.client.delete_product_image(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_082_delete_product_image_2(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id
        self.params["param2"] = os.path.basename(self.images[1])

        response = self.client.delete_product_image(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_083_delete_product_image_3(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id
        self.params["param2"] = os.path.basename(self.images[2])

        response = self.client.delete_product_image(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_084_get_updated_products_no_product_property(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.get_updated_products(self.params)

    def test_085_get_updated_products_stocklevel(self):

        # Get products, whose stocklevel has been lately changed
        self.params["param1"] = "stocklevel"

        response = self.client.get_updated_products(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_086_connect_category_and_product_no_data(self):

        with self.assertRaises(RuntimeError) as e:
            response = self.client.connect_category_and_product(self.params)

    def test_087_connect_category_and_product_false_data(self):

        self.params["data"] = {'categoryId': str(
            uuid.uuid4()), 'productId': str(uuid.uuid4())}

        with self.assertRaises(RuntimeError) as e:
            response = self.client.connect_category_and_product(self.params)

    def test_088_connect_category_and_product(self):

        categories = self.get_category_ids()
        product_id = self.get_product_id()

        self.params["data"] = {
            'categoryId': categories[0], 'productId': product_id}

        response = self.client.connect_category_and_product(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_089_disconnect_product_and_category_no_data(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.disconnect_product_and_category(self.params)

    def test_090_disconnect_product_and_category_false_data(self):

        self.params["query"]["categoryId"] = str(uuid.uuid4())
        self.params["query"]["productId"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            response = self.client.disconnect_product_and_category(self.params)

    def test_091_disconnect_product_and_category(self):

        categories = self.get_category_ids()
        product_id = self.get_product_id()

        self.params["query"]["categoryId"] = categories[0]
        self.params["query"]["productId"] = product_id

        response = self.client.disconnect_product_and_category(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_092_get_watched_products(self):

        watched_products = self.client.get_watched_products(self.params)

        self.assertEqual(isinstance(watched_products, dict), True)

    def test_093_delete_product_no_id(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.delete_product(self.params)

    def test_094_delete_product_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            response = self.client.delete_product(self.params)

    def test_095_delete_product_correct_id(self):

        product_id = self.get_product_id()
        self.params["param1"] = product_id

        response = self.client.delete_product(self.params)

        self.assertEqual(isinstance(response, dict), True)

        # Remove the product file containing the product id/name
        os.remove(self.product_file)

    def test_096_delete_category_no_id(self):

        with self.assertRaises(ValueError) as e:
            response = self.client.delete_category(self.params)

    def test_097_delete_category_false_id(self):

        self.params["param1"] = str(uuid.uuid4())

        with self.assertRaises(RuntimeError) as e:
            response = self.client.delete_category(self.params)

    def test_098_delete_category(self):

        categories = self.get_category_ids()
        self.params["param1"] = categories[0]

        response = self.client.delete_category(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_099_delete_category(self):

        # Wait for 1 second before deleting a category
        time.sleep(1)

        categories = self.get_category_ids()
        self.params["param1"] = categories[1]

        response = self.client.delete_category(self.params)

        self.assertEqual(isinstance(response, dict), True)

    def test_100_delete_category(self):

        # Wait for 1 second before deleting a category
        time.sleep(1)

        categories = self.get_category_ids()
        self.params["param1"] = categories[2]

        response = self.client.delete_category(self.params)

        self.assertEqual(isinstance(response, dict), True)

        # Remove the category file containing the category ids
        os.remove(self.category_file)

    def tearDown(self):
        pass
