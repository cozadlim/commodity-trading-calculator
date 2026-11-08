from base import (revenue, purchase_costs, total_cost, net_profit, break_even_price, profit_margin, profit_percentage)
import pytest
# supporting functions input validation 
def test_revenue():
    assert revenue(8, 10) == 80
    
def test_purchase_costs():
    assert purchase_costs(8, 8) == 64
    
def test_total_cost():
    assert total_cost(50,10,5,5,0) == 70
   
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
    
#negative profit margin test
def test_negative_profit_margin():
    assert profit_margin(-10,50) == pytest.approx(-20.0, rel=1e-2)

# zero quantity break even price edge case  
def test_zero_quantity_break_even_price():
    assert break_even_price(70,0) == 0
    
#final end to end check 
def test_end_to_end():
    rev = revenue(10, 8)
    PC = purchase_costs(10, 5)
    TC = total_cost(PC,10,5, 5, 0)
    NP = net_profit(rev,TC)
    BEP = break_even_price(TC,10)
    PM = profit_margin(NP,rev)
    PP = profit_percentage(NP,TC)
    assert rev == 80
    assert PC == 50
    assert TC == 70
    assert NP == 10
    assert BEP == 7
    assert PM == pytest.approx(12.5, rel=1e-2)
    assert PP == pytest.approx(0.142857, rel=1e-2)