import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load data
data = yf.download("TCS.NS", start="2021-01-01", end="2025-12-31")
close_prices = data[['Close']].dropna().values

# Scale
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(close_prices)

# Create sequences
X, y = [], []
window = 60

for i in range(window, len(scaled_data)):
    X.append(scaled_data[i-window:i])
    y.append(scaled_data[i])

X, y = np.array(X), np.array(y)

# Build LSTM
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(window, 1)),
    LSTM(50),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=10, batch_size=32, verbose=0)

# Predict 2026
last_seq = scaled_data[-window:].reshape(1, window, 1)
lstm_pred = model.predict(last_seq)
lstm_predicted_2026 = scaler.inverse_transform(lstm_pred)[0][0]
