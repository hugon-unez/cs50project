# Reviewed old notes to refresh on pandas
# This is a python file
# https://www.r-bloggers.com/2022/03/how-to-use-r-and-python-together-try-these-2-packages/
# 
# Take in data from the twitter API
# import tweepy
# import datetime

# we decided to use a wrapper for twitter's api in order to easily import/use twitter data

# client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAI6BjwEAAAAAaSCf62jC8wxVlU0RphhCEvDxla0%3D0392CJtnYHJL1eA9TVoC6Tj84k347tiWMIXsPyHXehgUeni0sH")

#make a placeholder for the user
# query = 'from:elonmusk'
# tweets = client.search_recent_tweets(query=query, max_results=10, tweet_fields=["created_at"])

#make sure to account for user having less than 50 tweets, or

# time_data = []

# for tweet in tweets.data:
#     time_data.append(tweet.created_at)
# Clean the twitter data
# Select certain users
# workingdata = tdata["user_id"].isin(user_input)
# Select the time data
# time_data = workingdata["time"]
# Get the times of interest
# before_check_times = []
# after_check_times = []
# for time in time_data:
#     before_check_times.append(time - 1)
#     after_check_times.append(time + 5)
# Take in market data from the API
# mdata = MARKET_DATA
# mar_data = []
# Select the time data
# Obtain the share price of the associated company 1 minute before the tweet
# mdata["before_price"] = mdata[mdata["time"].isin(before_check_times)]
# Obtain the share price five minutes after the tweet
# mdata["after_price"] = mdata[mdata["time"].isin(after_check_times)]
# Make the change 
# mdata["percent_change"] = (mdata["before_price"]-mdata["after_price"])*100/mdata["before_price"]
# Select the share price data
# Determine which tweets to focus on
    # Iterate through each tweet
        
        
        
# fun part
# results = []
# results[0] = (mdata["percent_change"].sum())/mdata.rows()
# results[1] = mdata["percent_change"].mean()

# print(results)


# Supervised machine learning. Much of this is similar to what I did over the summer.
from twitter import twitter_stuff
import numpy as np
import pandas as pd
import sklearn
csv_data = twitter_stuff()
print(csv_data)
data = pd.DataFrame(csv_data)
data["change"] = data[1]-data[0]
print(data)
y = data["change"] 
print(y)
X = data[[0,1,2]]
print(X)
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state = 1)
# tree = DecisionTreeClassifier(max_depth = 1, random_state = 1)
# tree.fit(X_train, y_train)
# y_pred = tree.predict(X_test)
# accuracy_score(y_test, y_pred)

# print(accuracy_score)
tree = DecisionTreeClassifier(max_depth = 1, random_state = 1)
tree.fit(X, y)
y_pred = tree.predict(X[:][1])
print(y_pred)
