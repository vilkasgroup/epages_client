# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .data_object import DataObject
from .price import Price
from .list_of_objects import ListOfObjects
from .deposit_line_item import DepositLineItem
from .line_item import LineItem
from .product_line_item import ProductLineItem
from .coupon_line_item import CouponLineItem


class LineItemContainer(DataObject):
    """Dataobject for LineItemContainer object"""

    def __init__(self):
        # object of price The total price including product price, shipping and tax.
        self.grandTotal = Price()
        # object of price The total price including product price, shipping excluding tax.
        self.totalBeforeTax = Price()
        # object of price The total amount of the tax.
        self.totalTax = Price()
        # object of price The sum of the line item price of all line items.
        self.lineItemsSubTotal = Price()
        # array of productLineItem A list of line items.
        self.productLineItems = ListOfObjects(ProductLineItem)
        # object of price The shipping price of the line item.
        self.shippingPrice = Price()
        # object of couponLineItem Contains the line items of a coupon.
        self.couponLineItem = CouponLineItem()
        # array of depositLineItem The deposits that apply for the order.
        self.deposits = ListOfObjects(DepositLineItem)
        # array of lineItem The recycling fees included in the order.
        self.ecoParticipations = ListOfObjects(LineItem)
        # array of lineItem The costs for the specific delivery options, such as greeting cards.
        self.shippingOptions = ListOfObjects(LineItem)
        # object of lineItem The overall discount for the order.
        self.basketDiscount = LineItem()

    def is_valid(self):
        return all(
            self.grandTotal.is_valid(),
            self.totalBeforeTax.is_valid(),
            self.totalTax.is_valid(),
            self.lineItemsSubTotal.is_valid(),
            self.productLineItems.is_valid(),
            self.shippingPrice.is_valid(),
            self.couponLineItem.is_valid(),
            self.deposits.is_valid(),
            self.ecoParticipations.is_valid(),
            self.shippingOptions.is_valid(),
            self.basketDiscount.is_valid()
        )
