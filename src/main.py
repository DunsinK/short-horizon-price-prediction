#Getting Data from yahoo finance
import yfinance as yf 
from data.yfinance_loader import get_stock_data 
from data.coingecko_loader import get_crypto_data 


data = get_stock_data("AAPL", "1y", "1d")
data = get_crypto_data(days = "1000")
print(data)


data["return"] = data["Close"].pct_change()
data["target"] = (data["return"].shift(-1) > 0).astype(int)


data["ma_5"] = data["Close"].rolling(5).mean()
data["ma_10"] = data["Close"].rolling(10).mean()
data["volatility"] = data["Close"].rolling(5).std()
data["momentum"] = data["Close"] - data["Close"].shift(5)
data["lag_1"] = data["return"].shift(1)
data["lag_2"] = data["return"].shift(2)
data = data.dropna()

split_index = int(len(data) * 0.8)
trainingData = data[:split_index] # train on first 80% 
testingData = data[split_index:] # testingData on last 20%

from sklearn.linear_model import LogisticRegression
# from scikit-learn.linear_model

features = ["ma_5", "ma_10", "volatility", "momentum", "lag_1", "lag_2"]

X_train = trainingData[features]
y_train = trainingData["target"]

X_testingData = testingData[features]
y_testingData = testingData["target"]

lr = LogisticRegression()
lr.fit(X_train, y_train)


from xgboost import XGBClassifier

xgb = XGBClassifier(n_estimators=100, max_depth=3)
xgb.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, precision_score, recall_score

y_pred_lr = lr.predict(X_testingData)
y_pred_xgb = xgb.predict(X_testingData)

print("LR Accuracy:", accuracy_score(y_testingData, y_pred_lr))
print("XGB Accuracy:", accuracy_score(y_testingData, y_pred_xgb))


#print(data)
#print(type(data))