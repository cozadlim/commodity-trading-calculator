from fx import fetch_usd_to_sgd_rate, USD_to_SGD, SGD_to_USD
import pytest

def test_USD_to_SGD_vice_versa():
    assert USD_to_SGD(100, 1.35) == 135.0, "USD to SGD conversion failed"
    assert SGD_to_USD(135, 1.35) == 100.0, "SGD to USD conversion failed"
    
def test_zero_amount_conversion():
    assert USD_to_SGD(0, 1.35) == 0.0, "USD to SGD conversion failed"
    assert SGD_to_USD(0, 1.35) == 0.0, "SGD to USD conversion failed"

def test_negative_exchange_rate():
    with pytest.raises(ValueError):
        USD_to_SGD(100, -1.35)
    with pytest.raises(ValueError):
        SGD_to_USD(135, -1.35)