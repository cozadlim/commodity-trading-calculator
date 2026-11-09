# Commodity Trading Calculator
A command-line tool that works out whether a physical commodity trade
is profitable, including shipping and Singapore PSA port costs.

# What it calculates
- Revenue and purchase cost
- Total costs (purchase, freight, insurance, PSA port, additional costs)
- Net profit
- Break-even price per tonne
- Profit margin (% of revenue) and profit percentage (% return on cost)

#run it 
git clone https://github.com/cozadlim/<commodity-trading-calculator>.git
cd <commodity-trading-calculator>/projectfolder1
python base.py

## Example run
```
cargo quantity(tonnes): 10
purchase price(per tonne): 5
selling price(per tonne): 8
total freight costs: 10
insurance costs (standard): 5
cost of using SG PSA port: 5
additional costs: 0
revenue: 80.00
purchase cost: 50.00
net profit: 10.00
break even price/tonne: 7.00
profit margin: 12.50
profit percentage: 14.3%
```
run the tests
cd <commodity-trading-calculator>/projectfolder1
pip install pytest
python -m pytest -v

