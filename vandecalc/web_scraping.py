#!/bin/python3

import re

import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
from urllib3.exceptions import MaxRetryError, NewConnectionError


def main():
    print(interest_percent)
    print(gas_price)


INTERNET_PERCENT_URL = "https://www.drklein.de/"
GAS_PRICE_URL = "https://www.ndr.de/nachrichten/info/Gaspreis-aktuell-wie-viel-kostet-Kilowattstunde,gaspreis142.html"


def convert_coma_string_to_float(string: str) -> float:
    """takes a number with an coma as decimal separator and returns a float"""
    return float(".".join(string.split(",")))


try:
    interest_percent_response = requests.get(INTERNET_PERCENT_URL)
    gas_price_response = requests.get(GAS_PRICE_URL)

    interest_percent_soup = BeautifulSoup(interest_percent_response.text, "html.parser")
    gas_price_soup = BeautifulSoup(gas_price_response.text, "html.parser")

    interest_percent_span = str(
        interest_percent_soup.find_all("span", {"class": "topzins-plugin_zinsNumber"})
    )
    gas_price_p = str(gas_price_soup.find_all("p")[2])

    interest_percent_regex = r"\b(?<=data-to=\")\d*,\d*"
    gas_price_regex = r"\b(?<=Mittel )\d*,\d*"

    interest_percent = convert_coma_string_to_float(
        re.findall(interest_percent_regex, interest_percent_span)[0]
    )
    gas_price = round(
        convert_coma_string_to_float(re.findall(gas_price_regex, gas_price_p)[0]) / 100,
        4,
    )
except (ConnectionError, NewConnectionError, MaxRetryError) as e:
    interest_percent = 4
    gas_price = 0.1
    print(e)


if __name__ == "__main__":
    main()
