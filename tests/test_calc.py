#!/bin/python3
import unittest

from vandecalc.calc import HouseProperties


class HousePropertiesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.House = HouseProperties(sales_price=170000, equity=30000)

    def test_land_purchase_tax(self):
        self.assertEqual(self.House.land_purchase_tax, 11050)

    def test_brokerage(self):
        self.assertEqual(self.House.brokerage, 6069)

    def test_notary_fees(self):
        self.assertEqual(self.House.notary_fees, 2550)

    def test_entry_land_register(self):
        self.assertEqual(self.House.entry_land_register, 850)

    def test_total_cost_to_be_financed(self):
        self.assertEqual(self.House.total_cost_to_be_financed, 160519)
