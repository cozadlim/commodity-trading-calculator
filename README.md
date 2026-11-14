# Commodity Trading Calculator
A web app that works out whether a physical commodity trade
is profitable, including shipping and Singapore PSA port costs.

**[try the live app!](https://commodity-trading-calculator-fiy5bbbwyqgsduifdlwqzn.streamlit.app/)**
<img width="2827" height="1516" alt="screenshot of the calculator web app" src="https://github.com/user-attachments/assets/9fdfebb3-0282-428d-9c50-821569bf8d8b" />

# What it calculates
- Revenue and purchase cost
- Total costs (purchase, freight, insurance, PSA port, additional costs)
- Net profit
- Break-even price per tonne
- Profit margin (% of revenue) and profit percentage (% return on cost)
- USD/SGD converter using the latest daily rate, with a manual override

# Run it
```bash
git clone https://github.com/cozadlim/commodity-trading-calculator.git
cd commodity-trading-calculator
python -m pip install -r requirements.txt
cd projectfolder1
python -m streamlit run app.py
```

# Example run
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
# Run the tests
```bash
cd commodity-trading-calculator/projectfolder1
pip install pytest
python -m pytest -v
```
## Notes
- All prices in the calculator are in USD; use the sidebar converter for SGD quotes.
- Exchange rates come from the Frankfurter API and are daily reference rates, not live market prices.
