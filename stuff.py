# Reviewed old notes to refresh on pandas
# Supervised machine learning. Much of this is similar to what I did over the summer.
import numpy as np
import pandas as pd
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error as MSE
from twitter import twitter_stuff
from data import recent_price
def predicted_change():
    recent_csv_data = recent_price()
    # print(recent_csv_data)
    recent_data = pd.DataFrame(recent_csv_data)
    # Researched transpose function.
    recent_data = recent_data.T
    # print(recent_data)
    csv_data = twitter_stuff()
    # print(csv_data)
    data = pd.DataFrame(csv_data)
    data["change"] = data[1]-data[0]
    # print(data)
    y = data["change"]
    # print(y)
    X = data[[0,2]]
    # print(X)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = 1)
    # tree = DecisionTreeClassifier(max_depth = 1, random_state = 1)
    # tree.fit(X_train, y_train)
    # y_pred = tree.predict(X_test)
    # accuracy_score(y_test, y_pred)
    # print(accuracy_score)
    tree = DecisionTreeRegressor(max_depth = 3, min_samples_leaf = 0.1, random_state = 1)
    tree.fit(X, y)
    y_pred = tree.predict(recent_data)
    # mse_tree = MSE(y, y_pred)
    # rmse_tree = mse_tree**(0.5)
    # print(y_pred)
    # print(mse_tree)
    # print(rmse_tree)
    return y_pred
