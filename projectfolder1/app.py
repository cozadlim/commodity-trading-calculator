import streamlit as st
from base import calculate_trade, revenue, total_cost, net_profit

st.set_page_config(page_title = "Commodity Trading Calculator", layout = "wide")
st.title("Trade Calculator")
st.caption("commmodity trading calculator including freight, insurance and singapore PSA port cost. Easy aplication to see how much youve made.")

with st.sidebar:
    st.header("TRADE")
    qty = st.number_input("Enter cargo quantity:", min_value=0.1,value = 10.0, step=1.0)
    pp = st.number_input("Enter purchase price:", min_value=0.0,value =5.0, step=1.0)
    sp = st.number_input("enter selling price:", min_value =0.1, value =8.0, step=1.0)
    
with st.sidebar: 
    st.header("SHIPMENT COSTS")
    sfc = st.number_input("Enter sea freight costs:", min_value=0.0,value =10.0, step=1.0)
    insurance = st.number_input("enter insurance costs:", min_value=0.0,value =5.0, step=1.0)
    port_costs = st.number_input("Enter port costs:", min_value=0.0,value =5.0, step=1.0)
    additional_costs = st.number_input("Enter additional costs:", min_value=0.0,value =0.0, step=1.0)

result = calculate_trade(qty, pp, sp, sfc, insurance, port_costs, additional_costs)

if result["net_profit"] > 0:
    st.success("profitable trade")
else:
    st.error("made a loss")    
    
c1, c2, c3 = st.columns(3)
c1.metric("Revenue:",f"{result["revenue"]:,.2f}")
c2.metric("Purchase Cost:", f"{result['purchase_cost']:,.2f}")
c3.metric("Total Cost:", f"{result['total_cost']:,.2f}")
c4, c5, c6, c7 = st.columns(4)
c4.metric("Net Profit:", f"{result['net_profit']:,.2f}")
c5.metric("Break Even Price:", f"{result['break_even_price']:,.2f}")
c6.metric("Profit Margin:", f"{result['profit_margin']:,.2f}")
c7.metric("Profit Percentage:", f"{result['profit_percentage']:,.2f}")

st.subheader("selling price slider")
sp_slider = st.slider("adjust selling price:", min_value=0.8*sp, max_value=1.2*sp, value = sp, step=0.1)
st.bar_chart({"selling price":{
    "revenue": revenue(qty, sp_slider),
    "total cost": total_cost(result['purchase_cost'], sfc, insurance, port_costs, additional_costs),
    "net profit": net_profit(revenue(qty, sp_slider), total_cost(result['purchase_cost'], sfc, insurance, port_costs, additional_costs))
    }}, horizontal = True)


st.subheader("cost breakdown")
st.bar_chart({"costs":{
    "purchase cost": result["purchase_cost"],
    "sea freight costs": sfc,
    "insurance": insurance,
    "port costs": port_costs,
    "additional costs": additional_costs
}},horizontal = True)


