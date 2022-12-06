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
    # Obtain the recent price data (the current price and volume).
    recent_csv_data = recent_price()
    # Make the recent data csv into a dataframe.
    recent_data = pd.DataFrame(recent_csv_data)
    # Researched transpose function: https://www.w3resource.com/pandas/dataframe/dataframe-transpose.php#:
    # Tanspose the data frame to be compatible with the predicting model.
    recent_data = recent_data.T
    # Obtain the recent tweet history and corresponding price data.
    csv_data = twitter_stuff()
    # Make the price data from the tweets into a dataframe.
    data = pd.DataFrame(csv_data)
    # Create a new column that consists of the price change over the interval.
    data["change"] = data[1]-data[0]
    # Create list y of the price changes.
    y = data["change"]
    # Create data frame X of the opening prices and volumes.
    X = data[[0,2]]
    # Create the prediction regression model. Tuned depth to have relatively accurate results with balanced runtime.
    tree = DecisionTreeRegressor(max_depth = 3, min_samples_leaf = 0.1, random_state = 1)
    # Fit the model.
    tree.fit(X, y)
    # Use the most recent data to predict the effect of a new tweet.
    y_pred = tree.predict(recent_data)

    # Return the predicted change in price.
    return y_pred

    # https://realpython.com/train-test-split-python-data/
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = 1)
    # tree = DecisionTreeClassifier(max_depth = 1, random_state = 1)
    # tree.fit(X_train, y_train)
    # y_pred = tree.predict(X_test)
    # accuracy_score(y_test, y_pred)
    # print(accuracy_score)

    # mse_tree = MSE(y, y_pred)
    # rmse_tree = mse_tree**(0.5)
    # print(y_pred)
    # print(mse_tree)
    # print(rmse_tree)


    # Researched to fix issue: https://www.statology.org/valueerror-unknown-label-type-continuous/
