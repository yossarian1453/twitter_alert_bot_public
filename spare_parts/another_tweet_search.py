import urllib.request as request
from contextlib import closing
import pandas as pd
import subprocess

consumer_key = 'insert consumer key here'
consumer_secret = 'insert consumer secret here'
access_token = 'insert access token here'
access_token_secret = 'insert access token secret here'
bearer_token = 'insert bearer token here'

twitter_users = pd.read_csv('/repo/location/twitter_alert_bot/twitter_handles.csv')
user_name = twitter_users['twitter_account']
url = 'https://api.twitter.com/1.1/search/tweets.json?q=from%3Ahansilowang%20%22redistricting%22&result_type=recent'
test_url = 'https://api.twitter.com/1.1/search/tweets.json?q=from%3ACmdr_Hadfield%20%23nasa&result_type=popular'

command = f'twurl "{test_url}" -H "Authorization: Bearer {bearer_token}"'
command2 = f'twurl "{test_url}"'
subprocess.check_output(command2, shell=True)
print(command2)

# url = "https://api.twitter.com/2/tweets.josn?q={}&{}&{}".format(ids, tweet_fields, text)
# 'https://api.twitter.com/1.1/search/tweets.json?q=from%3ACmdr_Hadfield%20%23nasa'

# for i in range (len(user_name)):
#     user = "{}".format(user_name[i])
#     #print(directory)
#     handle = user.split('/',3)
#     last_portion = handle[3]
#     command = f'curl "https://api.twitter.com/2/users/by/username/{last_portion}" -H "Authorization: Bearer {bearer_token}"'
    # def append_list_as_row(file_name, list_of_elem):
    # with open(test_csv, 'a+', newline='') as wf:
    #     pulled_json = subprocess.check_output(command, shell=True)
    #     dataframe = pd.read_json(pulled_json)
    #     user_id = dataframe.iloc[0]['data']
    #     # print(user_id)
    #     wf.write(last_portion+','+user_id+'\n')
