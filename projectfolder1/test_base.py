from base import (revenue, purchase_costs, total_cost, net_profit, break_even_price, profit_margin, profit_percentage)
import pytest
# supporting functions input validation 
def test_revenue():
    assert revenue(8, 10) == 80
    
def test_purchase_costs():
    assert purchase_costs(8, 8) == 64
    
def test_total_cost():
    assert total_cost(1,1,1,1,1) == 5
   
def test_net_profit():
    assert net_profit(20,5) == 15

def test_break_even_price():
    assert break_even_price(70,10) == 7 

def test_profit_margin():
    assert profit_margin(10,50) == pytest.approx(20.0, rel=1e-2)  # Allowing for floating point precision
    
def test_profit_percentage():
    assert profit_percentage(10,70) == pytest.approx(0.142857, rel=1e-2)  # Allowing for floating point precision

# negative profit edge case
def test_negative_net_profit():
    assert net_profit(20,30) == -10

# zero quantity break even price edge case  
def test_zero_quantity_break_even_price():
    assert break_even_price(70,0) == 0