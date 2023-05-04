#!/bin/python3

# import web_scraping
from kivy.event import EventDispatcher
from kivy.properties import NumericProperty

from vandecalc import web_scraping


def main():
    h = HouseProperties()
    h.sales_price = 170000
    h.land_purchase_tax_percent = 6.5
    print(h.land_purchase_tax)


class HouseProperties(EventDispatcher):
    sales_price = NumericProperty(min=0, errorvalue=0)
    equity = NumericProperty(min=0, errorvalue=0)

    land_purchase_tax_percent = NumericProperty(6.5, min=0, errorvalue=0)
    brokerage_percent = NumericProperty(3.57, min=0, errorvalue=0)
    notary_fees_percent = NumericProperty(1.5, min=0, errorvalue=0)
    entry_land_register_percent = NumericProperty(0.5, min=0, errorvalue=0)

    interest_percent = NumericProperty(
        web_scraping.interest_percent, min=0, errorvalue=0
    )
    liquidation_percent = NumericProperty(2, min=0, errorvalue=0)

    land_purchase_tax = NumericProperty(min=0, errorvalue=0)
    brokerage = NumericProperty(min=0, errorvalue=0)
    notary_fees = NumericProperty(min=0, errorvalue=0)
    entry_land_register = NumericProperty(min=0, errorvalue=0)
    total_cost_to_be_financed = NumericProperty(min=0, errorvalue=0)
    interest_cost = NumericProperty(min=0, errorvalue=0)
    liquidation = NumericProperty(min=0, errorvalue=0)
    total_cost_for_credit = NumericProperty(min=0, errorvalue=0)

    energy_consumption = NumericProperty(min=0, errorvalue=0)
    living_space = NumericProperty(min=0, errorvalue=0)
    gas_price = NumericProperty(web_scraping.gas_price, min=0, errorvalue=0)
    heating_cost = NumericProperty(min=0, errorvalue=0)

    total_cost = NumericProperty(min=0, errorvalue=0)

    def on_sales_price(self, instance, value):
        self.calc_land_purchase_tax()
        self.calc_brokerage()
        self.calc_notary_fees()
        self.calc_entry_land_register()

    def on_equity(self, instance, value):
        self.calc_total_cost_to_be_financed()

    def on_land_purchase_tax_percent(self, instance, value):
        self.calc_land_purchase_tax()

    def on_brokerage_percent(self, instance, value):
        self.calc_brokerage()

    def on_notary_fees_percent(self, instance, value):
        self.calc_notary_fees()

    def on_entry_land_register_percent(self, instance, value):
        self.calc_entry_land_register()

    def on_land_purchase_tax(self, instance, value):
        self.calc_total_cost_to_be_financed()

    def on_brokerage(self, instance, value):
        self.calc_total_cost_to_be_financed()

    def on_notary_fees(self, instance, value):
        self.calc_total_cost_to_be_financed()

    def on_entry_land_register(self, instance, value):
        self.calc_total_cost_to_be_financed()

    def on_total_cost_to_be_financed(self, instance, value):
        self.calc_interest_cost()
        self.calc_liquidation()

    def on_interest_percent(self, instance, value):
        self.calc_interest_cost()

    def on_liquidation_percent(self, instance, value):
        self.calc_liquidation()

    def on_total_cost_for_credit(self, instance, value):
        self.calc_total_cost()

    def on_energy_consumption(self, instance, value):
        self.calc_heating_cost()

    def on_living_space(self, instance, value):
        self.calc_heating_cost()

    def on_gas_price(self, instance, value):
        self.calc_heating_cost()

    def on_heating_cost(self, instance, value):
        self.calc_total_cost()

    def on_interest_cost(self, instance, value):
        self.calc_total_cost_for_credit()

    def on_liquidation(self, instance, value):
        self.calc_total_cost_for_credit()

    def calc_land_purchase_tax(self):
        """calculates the purchase tax"""
        self.land_purchase_tax = self.sales_price * self.land_purchase_tax_percent / 100

    def calc_brokerage(self):
        """calculates the brokerage"""
        self.brokerage = self.sales_price * self.brokerage_percent / 100

    def calc_notary_fees(self):
        """calculates the notary fees"""
        self.notary_fees = self.sales_price * self.notary_fees_percent / 100

    def calc_entry_land_register(self):
        """calculates the entry in the land register"""
        self.entry_land_register = (
            self.sales_price * self.entry_land_register_percent / 100
        )

    def calc_total_cost_to_be_financed(self):
        """calculates the total cost to be financed"""
        self.total_cost_to_be_financed = (
            self.sales_price
            + self.land_purchase_tax
            + self.brokerage
            + self.notary_fees
            + self.entry_land_register
            - self.equity
        )

    def calc_interest_cost(self):
        """calculates the monthly interest_cost"""
        self.interest_cost = round(
            self.total_cost_to_be_financed * self.interest_percent / 100 / 12, 2
        )

    def calc_liquidation(self):
        """calculates the monthly liquidation"""
        self.liquidation = round(
            self.total_cost_to_be_financed * self.liquidation_percent / 100 / 12, 2
        )

    def calc_total_cost_for_credit(self):
        """calculates the total monthly cost for the credit"""
        self.total_cost_for_credit = round(self.interest_cost + self.liquidation, 2)

    def calc_heating_cost(self):
        """calculates the monthly heating cost"""
        self.heating_cost = round(
            self.energy_consumption * self.living_space * self.gas_price / 12, 2
        )

    def calc_total_cost(self):
        """calculates the total monthly cost"""
        self.total_cost = round(self.heating_cost + self.total_cost_for_credit, 2)


if __name__ == "__main__":
    main()
