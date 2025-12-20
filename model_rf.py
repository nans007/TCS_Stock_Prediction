import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load TCS data (2021–2025)
data = yf.download("TCS.NS", start="2021-01-01", end="2025-12-31")
data = data[['Close']].dropna()

# Lag feature
data['Lag1'] = data['Close'].shift(1)
data.dropna(inplace=True)

X = data[['Lag1']]
y = data['Close']

# Train RF model
rf_model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)
rf_model.fit(X, y)

# Predict 2026
last_price_2025 = X.iloc[-1].values.reshape(1, -1)
rf_predicted_2026 = rf_model.predict(last_price_2025)[0]
