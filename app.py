import streamlit as st
from model_lr import lr_predicted_2026
from model_rf import rf_predicted_2026
from model_lstm import lstm_predicted_2026

st.title("TCS Stock Price Prediction (2026)")

st.write(
    "Models trained on the last five years of TCS stock data (2021–2025)."
)

st.subheader(f"Linear Regression Prediction: ₹{lr_predicted_2026:.2f}")
st.subheader(f"Random Forest Prediction: ₹{rf_predicted_2026:.2f}")
st.subheader(f"LSTM Prediction: ₹{lstm_predicted_2026:.2f}")

st.caption(
    "Comparison of traditional ML and deep learning models for stock price prediction."
)

