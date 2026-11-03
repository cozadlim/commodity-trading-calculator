#input collection: 
cargo_quantity = input("cargo quantity(tonnes): ")
purchase_price = input("purchase price(per tonne): ")
selling_price = input("selling price(per tonne): ")
sea_fright_costs = input("fright costs(per container): ")
innsurance = input("insurance costs (standard): ")
SG_PSA_port = input("cost of using SG PSA port: ")
additional_costs = input("additional costs: ")

#supporting functions 
def revenue():
    revenue = cargo_quantity * selling_price
    return revenue  
    
def purchase_costs():
    purchase_cost = cargo_quantity * purchase_price
    return purchase_cost

def net_profit():
    net_profit = revenue - total_cost - additional_costs
    return net_profit 

def break_even_price():
   BE_price = purchase_cost + (additional_costs/cargo_quantity)
   return BE_price
    
def profit_margin():
    profit_margin = (net_profit/revenue)*100
    return profit_margin 

def profit_percentage():
    profit_percentage = (net_profit/(total_costs + additional_costs))
    return profit_percentage

#main programme + input validation 
def main():
    ...

if __name__ == "__main__":
    main()
