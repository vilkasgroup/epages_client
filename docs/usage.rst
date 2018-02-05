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
    * The first parameter to add to the api url

* param2
    * The second parameter to add to the api url

* query
    * A dictionary for query parameters, for example currency or locale

* object
    * As the name implies, this gets an object as a value.