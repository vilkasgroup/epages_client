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

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-customers.html>`__

This method fetches all customers from the shop.

Required parameters: none

get_customer
~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-customers-customerid.html>`__

This method fetches single customer from the shop.

Required parameters: Customer id in param1

add_customer
~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/post-shopid-customers.html>`__

This method adds a customer to the shop.

Required parameters: Instance of CustomerCreate in object

**Note:** When adding a customer, only the Address object must have something in
*some instance variable*. It doesn't matter which variable it is. The Address object
is in the billingAddress instance variable of CustomerCreate.

update_customer
~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/patch-shopid-customers-customerid.html>`__

This method updates an existing customer in the shop.

Required parameters: Customer id in param1

**Note:** When updating customer, an instance of CustomerUpdate is not required. If the 
instance of CustomerUpdate is not sent or it is empty, nothing is updated.

Legal information
-----------------

get_legal_information
~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-legal.html>`__

This method gets hyperlinks of legal information for a shop.

Required parameters: none

get_contact_information
~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-legal-contact-information.html>`__

This method gets the contact information of a shop.

Required parameters: none

get_privacy_policy
~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-legal-privacy-policy.html>`__

This method gets the privacy policy of a shop.

Required parameters: none

get_terms_and_conditions
~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-legal-terms-and-conditions.html>`__

This method gets the terms and conditions of a shop.

Required parameters: none

get_rights_of_withdrawal
~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-legal-rights-of-withdrawal.html>`__

This method gets the customer rights of withdrawal of a shop.

Required parameters: none

get_shipping_information
~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-legal-shipping-information.html>`__

This method gets the detailed information on possible shipping types and the costs incurred.

Required parameters: none

update_contact_information
~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-legal-contact-information.html>`__

This method updates the contact information of a shop.

Required parameters: locale must be set

update_privacy_policy
~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-legal-privacy-policy.html>`__

This method updates the privacy policy of a shop.

Required parameters: locale must be set

update_terms_and_conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-legal-terms-and-conditions.html>`__

This method updates the terms and conditions of a shop.

Required parameters: locale must be set

update_rights_of_withdrawal
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-legal-rights-of-withdrawal.html>`__

This method updates the customer rights of withdrawal of a shop.

Required parameters: locale must be set

update_shipping_information
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-legal-shipping-information.html>`__

This method updates the shipping information of a shop.

Required parameters: locale must be set

Newsletters
-----------

get_newsletter_campaigns
~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-newsletter-campaigns.html>`__

This method gets the newsletter campaigns from a shop.

Required parameters: none

get_newsletter_campaign_subscribers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-newsletter-campaigns-campaignid-subscribers.html>`__

This method gets the subscribers of a newsletter campaign from a shop.

Required parameters: Newsletter campaign id in param1

Orders and carts
----------------

get_orders
~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-orders.html>`__

This method gets the orders from a shop.

Required parameters: none

get_order
~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-orders-orderid.html>`__

This method gets the information of a single order.

Required parameters: Order id in param1

get_order_documents
~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-orders-orderid-documents.html>`__

This method gets finalized invoice and credit note order documents of a single order.

Required parameters: Order id in param1

get_sales
~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-sales.html>`__

This method gets the summary of sales figures.

Required parameters: none

get_cart
~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-carts-cartid.html>`__

This method gets a single cart from a shop.

Required parameters: Cart id in param1

add_cart
~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/post-shopid-carts.html>`__

This method adds a cart for a shop.

Required parameters: none

add_coupon
~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/post-shopid-carts-cartid-coupon.html>`__

This method applies a coupon code on a cart of a shop.

Required parameters: Cart id in param1, coupon code in data

delete_coupon
~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/delete-shopid-carts-cartid-coupon-couponlineitemid.html>`__

This method deletes a coupon from a cart and recalculates cart.

Required parameters: Cart id in param1, coupon line item id in param2

add_cart_line_item
~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/post-shopid-carts-cartid-line-items.html>`__

This method adds a product line item in a cart.

Required parameters: Cart id in param1, instance of ProductLineItemCreate in object

update_cart_line_item
~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-carts-cartid-line-items-lineitemid.html>`__

This method updates a product line item in a cart.

Required parameters: Cart id in param1, product line item id in param2, instance of
ProductLineItemUpdate in object

delete_cart_line_item
~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/delete-shopid-carts-cartid-line-items-lineitemid.html>`__

This method deletes a product line item from a cart.

Required parameters: Cart id in param1, product line item id in param2

add_order
~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/post-shopid-carts-cartid-order.html>`__

This method adds an order to a shop.

Required parameters: Cart id in param1

**Note:** Before creating an order, the billing address must be set in a cart. Billing address can
be set after cart creation using the update_billing_address method.

update_order
~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/patch-shopid-orders-orderid.html>`__

This method updates an order.

Required parameters: Order id in param1

update_billing_address
~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-carts-cartid-billing-address.html>`__

This method updates the billing address for a cart.

Required parameters: Cart id in param1

delete_billing_address
~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/delete-shopid-carts-cartid-billing-address.html>`__

This method deletes the billing address from a cart.

Required parameters: Cart id in param1

update_shipping_address
~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-carts-cartid-shipping-address.html>`__

This method updates the shipping address for a cart.

Required parameters: Cart id in param1

delete_shipping_address
~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/delete-shopid-carts-cartid-shipping-address.html>`__

This method deletes the shipping address from a cart.

Required parameters: Cart id in param1

Products
--------

get_shop_info
~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid.html>`__

This method gets the public information of a shop, like name, slogan and logo.

Required parameters: none

get_categories
~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-categories.html>`__

This method gets the product categories of a shop.

Required parameters: none

get_category
~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-categories-categoryid.html>`__

This method gets a single product category of a shop.

Required parameters: Category id in param1

get_currencies
~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-currencies.html>`__

This method gets the currency information from a shop.

Required parameters: none

get_locales
~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-locales.html>`__

This method gets the locale information from a shop.

Required parameters: none

get_products
~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-products.html>`__

This method gets all of the products from a shop.

Required parameters: none

get_product
~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-products-productid.html>`__

This method gets a single product from a shop.

Required parameters: Product id in param1

get_product_variations
~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-products-productid-variations.html>`__

This method gets links to product variations.

Required parameters: Product id in param1

get_product_images
~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-products-productid-slideshow.html>`__

This method gets product images with links to different sizes of the images.

Required parameters: Product id in param1

get_product_image_names
~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-products-productid-slideshow-sequence.html>`__

This method gets product image names in the order they appear in a shop.

Required parameters: Product id in param1

get_product_custom_attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-products-productid-custom-attributes.html>`__

This method gets the user-defined product attributes with their values.

Required parameters: Product id in param1

get_product_lowest_price
~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-products-productid-lowest-price.html>`__

This method gets the lowest price of all variations of a product.

Required parameters: Product id in param1

search_products
~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-search-product-suggest.html>`__

This method searches products with a query.

Required parameters: Query string in query

get_shipping_methods
~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-shipping-methods.html>`__

This method gets the shipping methods of a shop.

Required parameters: none

get_shipping_method
~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-shipping-methods-shippingmethodid.html>`__

This method gets a single shipping method of a shop.

Required parameters: Shipping method id in param1

get_tax_classes
~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-tax-classes.html>`__

This method gets the tax classes of a shop.

Required parameters: none

get_tax_class
~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-tax-classes-taxclassid.html>`__

This method gets a single tax class of a shop.

Required parameters: Tax class id in param1

get_tax_model
~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-tax-model.html>`__

This method gets the tax model of a shop.

Required parameters: none

add_category
~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/post-shopid-categories-categoryid.html>`__

This method adds a subcategory to existing main category.

Required parameters: Main category id in param1, instance of CategoryCreate in object

update_category
~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-categories-categoryid.html>`__

This method updates a single category.

Required parameters: Category id in param1, instance of CategoryUpdate

**Note:** When updating a category, at least category id and category alias must be set. Category
id must be the same that is set in param1, and alias can't be the same than some other category has.
So, alias must be set always and it must be the same it was or something else that other categories
have.

delete_category
~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/delete-shopid-categories-categoryid.html>`__

This method deletes a single category.

Required parameters: Category id in param1

get_subcategory_sequence
~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-categories-categoryid-sequence.html>`__

This method gets the order of subcategories for the main category.

Required parameters: Main category id in param1

update_subcategory_sequence
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-categories-categoryid-sequence.html>`__

This method updates the order of subcategories.

Required parameters: Main category id in param1, instance of CategorySequenceUpdate in object

add_product
~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/post-shopid-products.html>`__

This method adds a new product for a shop.

Required parameters: Instance of ProductCreate

update_product
~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/patch-shopid-products-productid.html>`__

This method updates an existing product of a shop.

Required parameters: Product id in param1, instance of ProductUpdate

delete_product
~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/delete-shopid-products-productid.html>`__

This method deletes a product from a shop.

Required parameters: Product id in param1

upload_product_image
~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/post-shopid-products-productid-slideshow.html>`__

This method uploads an image for a product.

Required parameters: Product id in param1, image file in binary in data

**Note:** This doesn't set the uploaded image in the main image of a product, even if uploaded
image is the first image of the product. It must be set using update_product method.

delete_product_image
~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/delete-shopid-products-productid-slideshow-imagename.html>`__

This method deletes a image from a product.

Required parameters: Product id in param1, image name in param2

update_product_image_sequence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/put-shopid-products-productid-slideshow-sequence.html>`__

This method updates the order of product images.

Required parameters: Product id in param1, instance of ProductSlideshowSequenceUpdate in object

get_updated_products
~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-products-updated-productproperty.html>`__

This method gets updated products by product attributes.

Required parameters: Product attribute in param1

**Note:** At the time of writing only stocklevel attribute works for this.

connect_category_and_product
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/post-shopid-product-category-assignments.html>`__

This method connects categories and products.

Required parameters: Category and product id in data

**Note:** There can be more than one category or product id when connecting them to each other.
Category id and product id values can be a list of ids, too.

disconnect_product_and_category
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/delete-shopid-product-category-assignments.html>`__

This method disconnects categories and products.

Required parameters: Category and product id in query

**Note:** There can be more than one category or product id when disconnecting them from each other.
Category id and product id values can be a list of ids, too.

get_watched_products
~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-watched-products.html>`__

This method lists products that are watched by customers.

Required parameters: none

get_product_csv
~~~~~~~~~~~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-products-export.html>`__

This method returns a CSV file with all products of the shop. This doesn't work at the time
of writing.

Required parameters: none

Script tags
-----------

get_script_tags
~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/get-shopid-script-tags.html>`__

This method gets a list of all script tags for a shop.

Required parameters: none

add_script_tag
~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/post-shopid-script-tags.html>`__

This method adds a new script tag.

Required parameters: Instance of ScriptTagCreate in object

delete_script_tag
~~~~~~~~~~~~~~~~~

`API Docs <https://developer.epages.com/apps/api-reference/delete-shopid-script-tags-scripttagid.html>`__

This method deletes a script tag from a shop.

Required parameters: Script tag id in param1
