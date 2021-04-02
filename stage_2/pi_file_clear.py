import os

file_path = os.getcwd()

stage_1 = '/home/pi/twitter_bot_alert/stage_1/'
stage_2 = '/home/pi/twitter_bot_alert/stage_2/'

recorded_tweets = '/home/pi/twitter_bot_alert/stage_1/tweets.csv'
f = open(recorded_tweets, 'r+')
f.truncate(0) # need '0' when using r+

tweet_load = '/home/pi/twitter_bot_alert/stage_2/tweet_load.csv'
f = open(tweet_load, 'r+')
f.truncate(0) # need '0' when using r+
