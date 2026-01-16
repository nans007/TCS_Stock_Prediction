# 📈 AI-Based Stock Trend Analysis for TCS

## Project Overview
This project focuses on analyzing and predicting stock price trends of Tata Consultancy Services (TCS) using Machine Learning techniques. It combines data analysis, model comparison, and an interactive application to demonstrate both analytical understanding and practical deployment of AI-based trend analysis.

The project is developed under the TCS AI Track – Trend Analysis.

---

## Problem Definition & Objective
Stock market prices are highly dynamic and influenced by multiple economic and external factors, making it difficult to identify meaningful trends using raw historical data alone.

### Objectives
- Analyze historical stock price data of TCS
- Identify long-term trends and patterns
- Compare different Machine Learning models for prediction
- Demonstrate real-world applicability through an interactive system

---

## Dataset
- Source: Yahoo Finance API  
- Stock: TCS (TCS.NS)  
- Time Period: 10 years of historical data  
- Features: Open, High, Low, Close, Volume  
- Primary Feature Used: Closing Price  

Missing values were handled using forward-fill and data cleaning techniques to ensure consistency and reliability.

---

## Models Implemented

### Linear Regression
- Used as a baseline model
- Effective for capturing long-term linear trends
- Limited in modeling short-term price fluctuations

### Random Forest Regressor
- Ensemble-based model
- Captures non-linear relationships in stock price movements
- Demonstrates significantly better predictive accuracy

---

## Methodology
The workflow of the system follows a structured pipeline:
Data Collection
↓
Data Cleaning & Preparation
↓
Feature Engineering (Time Index)
↓
Model Training (Linear Regression / Random Forest)
↓
Prediction & Evaluation
↓
Visualization & User Interaction

---

## Evaluation & Analysis
Model performance was analyzed using quantitative metrics and visual comparison.

- Linear Regression captures the overall trend but shows higher error due to its linear assumptions.
- Random Forest achieves lower prediction error by learning complex, non-linear patterns.
- Visual comparison of actual vs predicted prices highlights the strengths and limitations of each model.

In the interactive application, a train–test evaluation was performed using historical test data from 2018–2024, and metrics such as Mean Absolute Error (MAE) and accuracy were computed. Random Forest consistently outperformed Linear Regression.

**Key Insight:**  
Linear Regression is suitable for baseline trend analysis, while Random Forest provides more accurate predictions for real-world stock price behavior.

---

## User Interface
An interactive user interface was developed to demonstrate the practical application of the trained models.

### Key Features
- Model selection and comparison
- Stock price prediction
- Performance metrics display
- Visual comparison of actual and predicted prices

The interface allows users to interact with the system and observe how different models behave under the same data conditions.

---

## Results & Insights
- Random Forest shows superior performance in modeling stock price movements.
- Linear Regression remains useful for understanding long-term trends.
- Combining analytical modeling with an interactive system provides a comprehensive view of both model behavior and usability.

> This project is intended for educational and analytical purposes only and does not constitute financial advice.

---

## Project Structure
├── TCS_AI_Trend_Analysis.ipynb # Main analysis notebook
├── app.py # Interactive application
├── src/ # Model and preprocessing modules
├── data/ # Dataset (CSV)
├── docs/ # documentation
├── results/ # Outputs and visualizations
└── README.md

---

## Ethical Considerations
- Stock market predictions are inherently uncertain and influenced by external factors.
- Historical data may not reflect future market behavior.
- Responsible use of AI is essential to avoid misleading conclusions.

---

## Conclusion & Future Scope
This project demonstrates an end-to-end AI-based trend analysis system, integrating data analysis with practical application.

### Future Enhancements
- Time-series cross-validation
- Incorporation of technical indicators
- Deep learning models such as LSTM
- Real-time data integration

















