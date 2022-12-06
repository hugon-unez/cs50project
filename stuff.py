# Reviewed old notes to refresh on pandas
# Supervised machine learning. Much of this is similar to what I did over the summer.
import numpy as np
# https://www.w3schools.com/python/pandas/pandas_getting_started.asp
import pandas as pd
# https://scikit-learn.org/stable/install.html
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
    recent_data = pd.DataFrame(recent_csv_data)
    # Researched transpose function: https://www.w3resource.com/pandas/dataframe/dataframe-transpose.php#:~:text=The%20transpose()%20function%20is,as%20columns%20and%20vice%2Dversa.&text=If%20True%2C%20the%20underlying%20data,copy%20is%20made%20if%20possible.
    recent_data = recent_data.T
    csv_data = twitter_stuff()
    data = pd.DataFrame(csv_data)
    data["change"] = data[1]-data[0]
    y = data["change"]
    X = data[[0,2]]
    tree = DecisionTreeRegressor(max_depth = 3, min_samples_leaf = 0.1, random_state = 1)
    tree.fit(X, y)
    y_pred = tree.predict(recent_data)
    # mse_tree = MSE(y, y_pred)
    # rmse_tree = mse_tree**(0.5)
    # print(y_pred)
    # print(mse_tree)
    # print(rmse_tree)
    return y_pred


    # https://realpython.com/train-test-split-python-data/
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = 1)
    # tree = DecisionTreeClassifier(max_depth = 1, random_state = 1)
    # tree.fit(X_train, y_train)
    # y_pred = tree.predict(X_test)
    # accuracy_score(y_test, y_pred)
    # print(accuracy_score)


    # Researched to fix issue: https://www.statology.org/valueerror-unknown-label-type-continuous/
