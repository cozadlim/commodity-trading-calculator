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

#input validation helper function
def get_float(prompt, allow_zero = True):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("please enter a number")
            continue 
    
        if value < 0:
            print("value has to be positive")
            continue 
        
        if value == 0 and not allow_zero:
            print("value cannot be zero")
            continue    
        return value 

#main programme + input validation 
def main():
#input collection:  
    cargo_quantity = get_float("cargo quantity(tonnes): ", allow_zero = False)
    purchase_price = get_float("purchase price(per tonne): ", allow_zero = False)
    selling_price = get_float("selling price(per tonne): ", allow_zero = False)
    sea_freight_costs = get_float("total fright costs: ")
    insurance = get_float("insurance costs (standard): ")
    SG_PSA_port = get_float("cost of using SG PSA port: ")
    additional_costs = get_float("additional costs: ")
#supporting varibles 
    rev = revenue(cargo_quantity, selling_price)
    PC = purchase_costs(cargo_quantity, purchase_price)
    TC = total_cost(PC,sea_freight_costs,insurance, SG_PSA_port, additional_costs)
    NP = net_profit(rev,TC)
    print(f"revenue: {rev:,.2f}")
    print(f"purchase cost: {PC:,.2f}")
    print(f"net profit: {NP:,.2f}")
    print(f"break even price/tonne: {break_even_price(TC, cargo_quantity):,.2f}")
    print(f"profit margin: {profit_margin(NP, rev):,.2f}")
    print(f"profit percentage: {profit_percentage(NP, TC):,.2f}")


if __name__ == "__main__":
    main()