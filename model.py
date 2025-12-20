import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Download data
data = yf.download("RELIANCE.NS", start="2018-01-01", end="2024-01-01")
data = data[['Close']]
data.dropna(inplace=True)

# Create target
data['Target'] = data['Close'].shift(-1)
data.dropna(inplace=True)

X = data[['Close']]
y = data['Target']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict next price
latest_price = X.iloc[-1].values.reshape(1, -1)
predicted_price = model.predict(latest_price)[0]
