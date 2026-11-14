import streamlit as st
from base import calculate_trade, revenue, total_cost, net_profit
from fx import fetch_usd_to_sgd_rate, USD_to_SGD, SGD_to_USD

st.set_page_config(page_title = "Commodity Trading Calculator", layout = "wide")
st.title("Trade Calculator")
st.caption("commmodity trading calculator including freight, insurance and singapore PSA port cost. Easy aplication to see how much youve made.")

@st.cache_data(ttl=3600)
def get_exchange_rate():
    return fetch_usd_to_sgd_rate()

with st.sidebar.expander("Currency converter (SGD ⇄ USD)"):
    try:
        usd_to_sgd_rate = fetch_usd_to_sgd_rate()
        st.caption(f"Current USD to SGD exchange rate: {usd_to_sgd_rate:.4f}")
    except Exception:
        usd_to_sgd_rate = None
        st.warning("Unable to fetch exchange rate. Please check your internet connection or enter one manually.")
    
    rate = st.number_input("Exchange rate (USD to SGD):", min_value=0.0, value=usd_to_sgd_rate if usd_to_sgd_rate else 1.30, step=0.001)
    direction = st.radio("Conversion direction:", ("USD to SGD", "SGD to USD"))
    amount = st.number_input("Amount:", min_value=0.0, value=1.0)
    if direction == "USD to SGD":
        st.write(f"{amount} USD is equal to {USD_to_SGD(amount, rate):.2f} SGD")
    else:
        st.write(f"{amount} SGD is equal to {SGD_to_USD(amount, rate):.2f} USD")

with st.sidebar:
    st.header("TRADE IN USD")
    qty = st.number_input("Enter cargo quantity (metric tons):", min_value=0.1,value = 10.0, step=1.0)
    pp = st.number_input("Enter purchase price (USD/ton):", min_value=0.0,value =5.0, step=1.0)
    sp = st.number_input("enter selling price (USD/ton):", min_value =0.1, value =8.0, step=1.0)
    
with st.sidebar: 
    st.header("SHIPMENT COSTS in USD")
    sfc = st.number_input("Enter sea freight costs (USD/ton):", min_value=0.0,value =10.0, step=1.0)
    insurance = st.number_input("enter insurance costs (USD/ton):", min_value=0.0,value =5.0, step=1.0)
    port_costs = st.number_input("Enter port costs (USD):", min_value=0.0,value =5.0, step=1.0)
    additional_costs = st.number_input("Enter additional costs (USD):", min_value=0.0,value =0.0, step=1.0)

result = calculate_trade(qty, pp, sp, sfc, insurance, port_costs, additional_costs)

if result["net_profit"] > 0:
    st.success("profitable trade")
else:
    st.error("made a loss")    
    
c1, c2, c3 = st.columns(3)
c1.metric("Revenue (USD):",f"{result["revenue"]:,.2f}")
c2.metric("Purchase Cost (USD):", f"{result['purchase_cost']:,.2f}")
c3.metric("Total Cost (USD):", f"{result['total_cost']:,.2f}")
c4, c5, c6, c7 = st.columns(4)
c4.metric("Net Profit (USD):", f"{result['net_profit']:,.2f}")
c5.metric("Break Even Price (USD/ton):", f"{result['break_even_price']:,.2f}")
c6.metric("Profit Margin (USD/ton):", f"{result['profit_margin']:,.2f}")
c7.metric("Profit Percentage:", f"{result['profit_percentage']:,.2f}")

st.subheader("selling price slider in USD")
sp_slider = st.slider("adjust selling price:", min_value=0.8*sp, max_value=1.2*sp, value = sp, step=0.1)
st.bar_chart({"selling price":{
    "revenue": revenue(qty, sp_slider),
    "total cost": total_cost(result['purchase_cost'], sfc, insurance, port_costs, additional_costs),
    "net profit": net_profit(revenue(qty, sp_slider), total_cost(result['purchase_cost'], sfc, insurance, port_costs, additional_costs))
    }}, horizontal = True)


st.subheader("cost breakdown in USD")
st.bar_chart({"costs":{
    "purchase cost": result["purchase_cost"],
    "sea freight costs": sfc,
    "insurance": insurance,
    "port costs": port_costs,
    "additional costs": additional_costs
}},horizontal = True)


