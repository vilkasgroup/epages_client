# -*- coding: utf-8 -*-
import unittest
from pprint import pprint

# import the package
import epages_client

from epages_client.dataobjects.order_update import OrderUpdate
from epages_client.dataobjects.remove_value import RemoveValue

# import base class for unit testing
from .base_unit_test import BaseUnitTest


class TestStringMethods(BaseUnitTest):
    def setUp(self):
        pass

    def test_0001_remove__values(self):
        order = OrderUpdate()
        order.customerComment = RemoveValue()
        order.internalNote = RemoveValue()
        order.viewedOn = RemoveValue()
        order.rejectedOn = RemoveValue()
        order.inProcessOn = RemoveValue()
        order.pendingOn = RemoveValue()
        order.readyForDispatchOn = RemoveValue()
        order.partiallyDispatchedOn = RemoveValue()
        order.dispatchedOn = RemoveValue()
        order.deliveredOn = RemoveValue()
        order.partiallyInvoicedOn = RemoveValue()
        order.invoicedOn = RemoveValue()
        order.partiallyPaidOn = RemoveValue()
        order.paidOn = RemoveValue()
        order.returnedOn = RemoveValue()
        order.closedOn = RemoveValue()
        order.archivedOn = RemoveValue()

        right_answer = [
            {'op': 'remove', 'path': '/deliveredOn'},
            {'op': 'remove', 'path': '/rejectedOn'},
            {'op': 'remove', 'path': '/archivedOn'},
            {'op': 'remove', 'path': '/internalNote'},
            {'op': 'remove', 'path': '/partiallyInvoicedOn'},
            {'op': 'remove', 'path': '/closedOn'},
            {'op': 'remove', 'path': '/pendingOn'},
            {'op': 'remove', 'path': '/viewedOn'},
            {'op': 'remove', 'path': '/readyForDispatchOn'},
            {'op': 'remove', 'path': '/returnedOn'},
            {'op': 'remove', 'path': '/partiallyPaidOn'},
            {'op': 'remove', 'path': '/dispatchedOn'},
            {'op': 'remove', 'path': '/partiallyDispatchedOn'},
            {'op': 'remove', 'path': '/paidOn'},
            {'op': 'remove', 'path': '/invoicedOn'},
            {'op': 'remove', 'path': '/inProcessOn'},
            {'op': 'remove', 'path': '/customerComment'}
        ]

        self.assert_count_items_equal(order.get_patch(), right_answer)

    def test_0002_change_address(self):
        order = OrderUpdate()
        order.shippingAddress.street = "Finlaysoninkuja 19"
        order.shippingAddress.zipCode = "33210"
        order.shippingAddress.city = "TAMPERE"

        right_answer = [
            {
                'op': 'add',
                'path': '/shippingAddress',
                'value': {
                    'street': "Finlaysoninkuja 19",
                    'zipCode': "33210",
                    'city': "TAMPERE"
                }
            }
        ]

        self.assertEqual(order.get_patch(), right_answer)

    def test_0003_illegals(self):
        order = OrderUpdate()
        with self.assertRaises(TypeError) as e:
            order.orderNumber = RemoveValue()


if __name__ == '__main__':
    unittest.main()
