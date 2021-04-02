import tweepy as tw
import pandas as pd
import subprocess
from datetime import date
import os

today = date.today()
twitter_date = today.strftime('%Y-%m-%d')
column_date = today.strftime('%Y%m%d')

file_path = os.getcwd()
twitter_users = pd.read_csv('/home/pi/twitter_bot_alert/stage_1/twitter_handles.csv')
recorded_tweets = '/home/pi/twitter_bot_alert/stage_1/tweets.csv'


# select the column to pull
user_name = twitter_users['twitter_account']
state = twitter_users['state']

consumer_key = 'ney1nwRpY3gRxA5smXHdEEBQI'
consumer_secret = 'cdQYAGpkvL0nXoqcqCBdPMhSWM0C4R1bvUTa1qkmAJ7CpACREO'
access_token = '1358710907006779398-9phO9CQfaZMCxrJZ5LeSfFarfgi5jl'
access_token_secret = 'hjTHd4GO97ndZw4AcBmxiCeDZAjOTRBtlc8nuB4s3MYAM'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAE2cMgEAAAAA%2F09FeHOkK5mqers%2Fa32RLBOVkVk%3DFza0CBgM4qKFx81HDe28W6dJUHaimXCESmqYFEtmx2lRvtRfYK'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Post a tweet from Python
# api.update_status("Look, I'm tweeting from #Python in my #earthanalytics class! @EarthLabCU")
# Your tweet has been posted!

for i in range (len(user_name)):
    user = "{}".format(user_name[i])
    #print(directory)
    handle = user.split('/',3)
    last_portion = handle[3]
    state_abbrev = state
    # Define the search term and the date_since date as variables
    search_words = 'millions since:2020-01-01'
    keyword = 'redistricting'
    date_since = '2021-03-12'
    # twitter_date
    new_search = keyword + ' -filter:retweets' + f' from:{last_portion}'
    # users='from:TexasTribune'
    # recent = 'recent'

    # Collect tweets
    tweets = tw.Cursor(
                api.search,
                q=new_search,
                lang='en',
                since=date_since
                # tweet_mode='extended'
                #   result_type=recent
                ).items(1)

    # Iterate and print tweets
    # full_tweets = [[tweet.full_text] for tweet in tweets]
    for tweet in tweets:
        # print(tweet.text)
        with open(recorded_tweets, 'a+', newline='') as wf:
            # print(user_id)
            wf.write(column_date+'|'+last_portion+'|'+tweet.text+'\n')

