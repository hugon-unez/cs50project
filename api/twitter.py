from datetime import datetime, timedelta
#pytz to convert time zone
import pytz
import tweepy
from data import stock_data 

def twitter_stuff():
    # we decided to use a wrapper for twitter's api in order to easily import/use twitter data

    client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAI6BjwEAAAAAaSCf62jC8wxVlU0RphhCEvDxla0%3D0392CJtnYHJL1eA9TVoC6Tj84k347tiWMIXsPyHXehgUeni0sH")

    #make a placeholder for the user
    query = 'from:potus'
    tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["created_at"])

    #make sure to account for user having less than 50 tweets, or

    # cleaning data for outside market time/days. this was one of the hardest parts of implementation due to the types
    # type of created_at is datetime.datetime

    tweet_times = []

    # in clean_time the tweet times are converted to est
    def clean_time(tweet):
        # change time zone
        tweet = tweet.astimezone(pytz.timezone('US/Eastern'))
        # strip off time zone format and make the seconds equal to zero for financial data
        tweet = tweet.strftime("%Y-%m-%d %H:%M:00")
        tweet = datetime.fromisoformat(tweet)
        return str(tweet)

    for tweet in tweets.data:
        # if the tweet was after market closing set time to the last market close time
        twit = clean_time(tweet.created_at)
        tweet_times.append(str(twit))

    # at this stage, tweet_times should be cleaned and be ready to input to financial data
    return stock_data('SPY', tweet_times)


