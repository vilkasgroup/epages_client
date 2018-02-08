=====
Usage
=====

Basic usage
-----------

To use ePages Client in a project:

.. code-block:: python

    from epages_client.client import RestClient

    # Set the api url and token for your shop
    api_url = "https://yourshop.vilkasstore.com/rs/shops/yourshop/"
    api_token = "shop_token_goes_here"

    # Get the instance of the client
    client = RestClient(api_url, api_token)

    # Example method: get shop info
    shop_info = client.get_shop_info()

The dictionary parameter
------------------------

Each method accepts a single dictionary parameter called params.
This parameter is not mandatory for all methods.

.. code-block:: python

    # params can have five different keys
    params = {
        "data": "",
        "param1": "",
        "param2": "",
        "query": {},
        "object": "",
    }

* data
    * The content here is usually a dictionary, but can have a binary file, too.

* param1
    * The first parameter to add to the api url.

* param2
    * The second parameter to add to the api url.

* query
    * A dictionary for query parameters, for example including hidden items in results.

* object
    * As the name implies, this gets an object as a value. Objects are located in the dataobjects directory.

Examples
~~~~~~~~

.. code-block:: python

    # Example 1

    # Set category id and product id
    params["data"] = {
            'categoryId': "5A41E34F-BAC7-8396-336A-0A2810152BBC",
            'productId': "5A497829-7619-ACCC-E487-0A281012346F"
    }

    # Connect category and product
    response = client.connect_category_and_product(params)

    # Example 2

    # Set product id
    # The api url will be:
    # https://yourshop.vilkasstore.com/rs/shops/yourshop/products/5A497829-7619-ACCC-E487-0A281012346F
    params["param1"] = "5A497829-7619-ACCC-E487-0A281012346F"

    # Get product data
    product = client.get_product(params)

    # Example 3

    # Set product id and image name
    # The api url will be:
    # https://yourshop.vilkasstore.com/rs/shops/yourshop/products/5A497829-7619-ACCC-E487-0A281012346F/slideshow/test.jpg
    params["param1"] = "5A497829-7619-ACCC-E487-0A281012346F"
    params["param2"] = "test.jpg"

    # Delete image from product
    response = client.delete_product_image(params)

    # Example 4

    # Find products where name contains the word 'laptop'
    # Limit search results to have 50 items
    params["query"] = {
        "query": "laptop",
        "limit": 50
    }

    # Search for the products
    results = self.client.search_products(self.params)

    # Example 5

    # Create a customer
    customer = CustomerCreate()
    customer.billingAddress.firstName = "John"
    customer.billingAddress.lastName = "Doe"
    customer.billingAddress.emailAddress = "john.doe@mail.com"

    # Add customer to params
    params["object"] = customer

    # Create a customer
    response = client.add_customer(params)

Currency and locale
-------------------

There are two ways to set currency and locale.

**Note:** If currency and locale are set using both setters and
params["query"], values of params["query"] are used.

.. code-block:: python

    # Currency and locale are set using client setters
    client.currency = "GBP"
    client.locale = "en_US"

    # Currency and locale are set using params["query"]
    params["query"] = {
        "currency": = "GBP",
        "locale": = "en_US"
    }