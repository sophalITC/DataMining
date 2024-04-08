#install tweepy, configparser, pandas
import pandas as pd
import os
import tweepy
import configparser
from datetime import datetime

print("start the tasks...")
# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d%m%Y%H%M%S")


#read credential 
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

Keyword = '#blockchain'
limit = 300

tweets = tweepy.Cursor(api.search_tweets, q = Keyword, count = 100, tweet_mode = 'extended').items(limit)

columns = ['Time', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.created_at, tweet.full_text])

df = pd.DataFrame(data, columns = columns)
cwd = os.getcwd()
path = cwd + "/blockchain" + dt_string + ".csv"
df.to_csv(path)
print(f"Finish the tasks and save csv file: %s" % (path))


Keyword = '#cryptocurrencies'

tweets = tweepy.Cursor(api.search_tweets, q = Keyword, 
count = 100, tweet_mode = 'extended').items(limit)

data = []

for tweet in tweets:
    data.append([tweet.created_at,  tweet.full_text])

df = pd.DataFrame(data, columns = columns)
cwd = os.getcwd()
path = cwd + "/crypto" + dt_string + ".csv"
df.to_csv(path)

print(f"Finish the tasks and save csv file: %s" % (path))