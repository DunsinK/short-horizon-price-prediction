Short Horizon Price Prediction 
---------
This project explores whether short-term stock price movements can be predicted using machine learning models trained on historical market data.

Using daily price data across multiple equities and cryptocurrencies, I engineered time-series features (returns, rolling statistics, momentum indicators) and trained both Logistic Regression and XGBoost classifiers to predict the direction of the next-day return.

The goal is not just to maximize accuracy, but to investigate whether any meaningful and stable predictive signal exists in noisy financial data. To do this, I evaluate model performance using time-aware train/test splits and compare results across different assets and market conditions.

Initial results show modest improvements over random guessing in some cases, but performance varies significantly across assets and degrades out-of-sample, highlighting the difficulty of extracting reliable signals from financial markets.

This project serves as a small-scale study in feature engineering, model validation, and the challenges of applying machine learning to non-stationary time series data.
