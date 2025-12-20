import streamlit as st
from model import predicted_price

st.title("Stock Price Prediction")
st.write("This model predicts the stock price based on historical data.")

st.subheader(
    f"The predicted stock price for Reliance Industries is: ₹{predicted_price:.2f}"
)

st.caption("Prediction based on Linear Regression using historical closing prices.")
