import os

file_path = os.getcwd()

recorded_tweets = f'{file_path}/stage_1/tweets.csv'
f = open(recorded_tweets, 'r+')
f.truncate(0) # need '0' when using r+

tweet_load = f'{file_path}/stage_2/tweet_load.csv'
f = open(tweet_load, 'r+')
f.truncate(0) # need '0' when using r+
