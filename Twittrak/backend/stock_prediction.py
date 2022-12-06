# Reviewed old notes to refresh on pandas
# Supervised machine learning. Much of this is similar to what I did over the summer.
# https://www.w3schools.com/python/pandas/pandas_getting_started.asp
import pandas as pd
# https://scikit-learn.org/stable/install.html
from sklearn.tree import DecisionTreeRegressor
from twitter import twitter_stuff
from data import recent_price
def predicted_change():
    # Obtain the recent price data (the current price and volume).
    recent_csv_data = recent_price()
    # Make the recent data csv into a dataframe.
    recent_data = pd.DataFrame(recent_csv_data)
    # Researched transpose: https://www.w3resource.com/pandas/dataframe/dataframe-transpose.php#:
    # Tanspose the data frame to be compatible with the predicting model.
    recent_data = recent_data.T
    # Obtain the recent tweet history and corresponding price data.
    csv_data = twitter_stuff()
    # Make the price data from the tweets into a dataframe.
    data = pd.DataFrame(csv_data)
    # Create a new column that consists of the price change over the interval.
    data["change"] = data[1]-data[0]
    # Create list y of the price changes.
    changes = data["change"]
    # Create data frame X of the opening prices and volumes.
    inputs = data[[0,2]]
    # Create the prediction regression model.
    # Researched to fix issue: https://www.statology.org/valueerror-unknown-label-type-continuous/
    tree = DecisionTreeRegressor(max_depth = 3, min_samples_leaf = 0.1, random_state = 1)
    # Fit the model.
    tree.fit(inputs, changes)
    # Use the most recent data to predict the effect of a new tweet.
    predicted = tree.predict(recent_data)

    # Return the predicted change in price.
    return predicted
