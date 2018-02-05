=======
Methods
=======

Here's a list of available methods to use with ePages Client.
Each method accepts a single dict parameter called params. The
more detailed description of the param is found in the usage document.

Customers
---------

get_customers
~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-customers.html>`_

This method fetches all customers from the shop.

Required parameters: none

get_customer
~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-customers-customerid.html>`_

This method fetches single customer from the shop.

Required parameters: Customer ID as param1

add_customer
~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/post-shopid-customers.html>`_

This method adds a customer to the shop.

Required parameters: Instance of CustomerCreate as object

**Note:** When adding a customer, only the Address object must have something in
*some instance variable*. It doesn't matter which variable it is. The Address object
is in the billingAddress instance variable of CustomerCreate.

update_customer
~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/patch-shopid-customers-customerid.html>`

Required parameters: Customer ID as param1

**Note:** When updating customer, the CustomerUpdate is not required. If an instance of
CustomerUpdate is not sent or it is empty, nothing is updated.