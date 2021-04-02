import shutil
import urllib.request as request
from contextlib import closing
import pandas as pd
import subprocess
import tweepy as tw

consumer_key = 'bCs3KjDixkdgew0WrHXTGDPe1'
consumer_secret = 'iCY2EIFUUOMzpAUEa7JXWYhu9xjg8gqXXp2rhacsAPGrqnaJ0Y'
access_token = '1358710907006779398-ztYTwvVQyJWKRKOqF4IaeHwhzfmtpz'
access_token_secret= 'cBqB48bge67Iysm10FJGqSdzo1WPkLrAu0HEjWfsPZ7mb'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAE2cMgEAAAAAxuksyrty6gvuuLMm6keHIr7cq8o%3DNMOcO1jCAKG4R22MPYQvFGJladaeGZDlPnUXDfNwj5HglKMJUS'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

twitter_users = pd.read_csv('/Users/robertness/Documents/Civitech/Python/twitter_alert_bot/twitter_handles.csv')

# url = f'https://api.twitter.com/2/users/by/username/{last_portion}'

screen_name = twitter_users['twitter_account']

for i in range (len(screen_name)):
    user = "{}".format(screen_name[i])
    #print(directory)
    handle = user.split('/',3)
    last_portion = handle[3]
    username = api.get_user(last_portion)
    print(username)
    # with open('/Users/robertness/Documents/Civitech/Python/twitter_alert_bot/test.csv', 'w') as wf:
    #     pulled_json = subprocess.Popen(command, shell=True)
    #     dataframe = pd.read_json(pulled_json)
    #     user_id = dataframe.iloc[0]['data']
    #     # print(user_id)
    #     wf.write(user_id)

