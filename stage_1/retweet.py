import tweepy as tw
import pandas as pd
import subprocess
from datetime import date
import os

today = date.today()
twitter_date = today.strftime('%Y-%m-%d')
column_date = today.strftime('%Y%m%d')

file_path = os.getcwd()
twitter_users = pd.read_csv(f'{file_path}/stage_1/twitter_handles.csv')
recorded_tweets = f'{file_path}/stage_1/tweets.csv'

# select the column to pull
user_name = twitter_users['twitter_account']
state = twitter_users['state']

consumer_key = 'insert consumer key here'
consumer_secret = 'insert consumer secret here'
access_token = 'insert access token here'
access_token_secret = 'insert access token secret here'
bearer_token = 'insert bearer token here'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

user = api.me()

for i in range (len(user_name)):
    user = "{}".format(user_name[i])
    #print(directory)
    handle = user.split('/',3)
    last_portion = handle[3]
    state_abbrev = state
    # Define the search term and the date_since date as variables
    search_words = 'millions since:2020-01-01'
    keyword = 'redistricting'
    date_since = twitter_date
    new_search = keyword + ' -filter:retweets' + f' from:{last_portion}'
    # users='from:TexasTribune'
    # recent = 'recent'

    # Collect tweets
    tweets = tw.Cursor(
                api.search,
                q=new_search,
                lang='en',
                since=date_since
                #   result_type=recent
                ).items(1)

    def main():
        search = new_search
        for tweet in tweets:
            try:
                tweet.retweet()
                print('Tweet Retweeted')
                # item.clear()
            except tw.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    main()




