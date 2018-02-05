=======
Methods
=======

Here's a list of available methods to use with ePages Client. Each method accepts a
single dict parameter called params. The more detailed description of the param is
found in the usage document. Method descriptions have a link to the ePages API, too.

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

`API Docs <https://developer.epages.com/apps/api-reference/patch-shopid-customers-customerid.html>`_

This method updates an existing customer in the shop.

Required parameters: Customer ID as param1

**Note:** When updating customer, the CustomerUpdate is not required. If an instance of
CustomerUpdate is not sent or it is empty, nothing is updated.

Legal information
-----------------

get_legal_information
~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-legal.html>`_

This method gets hyperlinks of legal information for a shop.

Required parameters: none

get_contact_information
~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-legal-contact-information.html>`_

This method gets the contact information of a shop.

Required parameters: none

get_privacy_policy
~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-legal-privacy-policy.html>`_

This method gets the privacy policy of a shop.

Required parameters: none

get_terms_and_conditions
~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-legal-terms-and-conditions.html>`_

This method gets the terms and conditions of a shop.

Required parameters: none

get_rights_of_withdrawal
~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-legal-rights-of-withdrawal.html>`_

This method gets the customer rights of withdrawal of a shop.

Required parameters: none

get_shipping_information
~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-legal-shipping-information.html>`_

This method gets the detailed information on possible shipping types and the costs incurred.

Required parameters: none

update_contact_information
~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-legal-contact-information.html>`_

This method updates the contact information of a shop.

Required parameters: locale must be set

update_privacy_policy
~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-legal-privacy-policy.html>`_

This method updates the privacy policy of a shop.

Required parameters: locale must be set

update_terms_and_conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-legal-terms-and-conditions.html>`_

This method updates the terms and conditions of a shop.

Required parameters: locale must be set

update_rights_of_withdrawal
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-legal-rights-of-withdrawal.html>`_

This method updates the customer rights of withdrawal of a shop.

Required parameters: locale must be set

update_shipping_information
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-legal-shipping-information.html>`_

This method updates the shipping information of a shop.

Required parameters: locale must be set