# TCS_Stock_Prediction
AI-based market trend analysis and stock price prediction for TCS
## Project Pipeline

1. Data Collection  
   - Collects last 5 years of TCS stock price data using Yahoo Finance (NSE: TCS.NS)

2. Exploratory Data Analysis (EDA)  
   - Visualizes price trends  
   - Detects missing values  
   - Identifies outliers using boxplots  

3. Data Preprocessing  
   - Cleans raw stock data  
   - Prepares features for modeling  

4. Modeling 
   - Stock price prediction using ML models
   - Linear Regression model used to predict TCS closing price  
   -Train-test split applied to preserve time-series order  
   - Model evaluated using actual vs predicted price trends
     
     ## User Interface (UI)

A web-based UI was developed using Streamlit to demonstrate model predictions
in an interactive manner.

Features:
- Model selection (Linear Regression / Random Forest)
- Visual comparison of predicted vs actual prices
- Trend visualization through charts

The UI is implemented in `app.py` and related source files.
This interface will be showcased as part of the next submission level.

  
## RESULTS AND INSIGHTS

- The linear regression model successfully captures the overall long-term trend of TCS stock prices.
- Predictions closely follow the general movement of the actual closing prices but fail to capture short-term fluctuations.
- This behavior is expected, as stock markets are influenced by sudden external factors such as news, macroeconomic events, and investor sentiment.
- The model performs better for trend analysis rather than precise short-term price forecasting.

## LIMITATIONS

- Linear regression assumes a linear relationship between time and price.
- The model does not account for market volatility, news sentiment, or sudden price shocks.
- Stock prices are inherently noisy and influenced by factors beyond historical data.

## FUTURE SCOPE

- Use advanced time-series models such as LSTM or GRU for better sequence learning.
- Integrate technical indicators like RSI, MACD, and Bollinger Bands.
- Incorporate sentiment analysis using financial news and social media data.
- Extend the model to predict short-term price movements.

## Project Structure

```text
data/
 ├── raw/                # Raw stock price data
 ├── processed/          # Cleaned and processed data

src/
 ├── data_collection.py  # Fetches stock data
 ├── eda.py              # Exploratory data analysis
 ├── preprocessing.py   # Data cleaning and preparation
 ├── modeling.py        # ML model training and prediction

results/
 ├── plots/              # Generated visualizations and results














