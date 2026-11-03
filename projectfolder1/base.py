#supporting functions 
def revenue(cargo_quantity, selling_price):
    return cargo_quantity * selling_price 

def purchase_costs(cargo_quantity, purchase_price):
    return cargo_quantity * purchase_price

def total_cost(PC,sea_freight_costs,insurance, SG_PSA_port, additional_costs):
    return PC + sea_freight_costs + insurance + SG_PSA_port + additional_costs

def net_profit(rev,TC):
    return rev - TC

def break_even_price(TC, cargo_quantity):
    return (TC)/cargo_quantity
    
def profit_margin(NP, rev):
    return (NP/rev)*100

def profit_percentage(NP,TC):
    return (NP/(TC))


#main programme + input validation 
def main():
#input collection: 
    cargo_quantity = float(input("cargo quantity(tonnes): "))
    purchase_price = float(input("purchase price(per tonne): "))
    selling_price = float(input("selling price(per tonne): "))
    sea_freight_costs = float(input("total fright costs: "))
    insurance = float(input("insurance costs (standard): "))
    SG_PSA_port = float(input("cost of using SG PSA port: "))
    additional_costs = float(input("additional costs: "))
#supporting varibles 
    rev = revenue(cargo_quantity, selling_price)
    PC = purchase_costs(cargo_quantity, purchase_price)
    TC = total_cost(PC,sea_freight_costs,insurance, SG_PSA_port, additional_costs)
    NP = net_profit(rev,TC)
    print(f"revenue: {rev:,.2f}")
    print(f"purchase cost: {PC:,.2f}")
    print(f"net profit: {NP:,.2f}")
    print(f"break even price/tonne: {break_even_price(TC, cargo_quantity):,.2f}")
    print(f"profit margin: {profit_margin(NP, rev)}")
    print(f"profit percentage: {profit_percentage(NP, TC):,.2f}")


if __name__ == "__main__":
    main()