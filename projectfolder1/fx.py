import json
import urllib.request
from base import get_float

def USD_to_SGD(amount, usd_to_sgd_rate):
    if usd_to_sgd_rate <= 0.0:
        raise ValueError("Exchange rate must be greater than zero.")
    return amount * usd_to_sgd_rate

def SGD_to_USD(amount, usd_to_sgd_rate):
    if usd_to_sgd_rate <= 0.0:
        raise ValueError("Exchange rate must be greater than zero.")
    return amount / usd_to_sgd_rate

def fetch_usd_to_sgd_rate():
    """ Fetches the current USD to SGD exchange rate from an external API."""
    URL = "https://api.frankfurter.dev/v2/rate/USD/SGD"
    with urllib.request.urlopen(URL, timeout = 5) as response:
        return float(json.load(response)["rate"])