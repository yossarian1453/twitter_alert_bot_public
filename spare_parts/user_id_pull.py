import urllib.request as request
from contextlib import closing
import pandas as pd
import subprocess

twitter_users = pd.read_csv('/Users/robertness/Documents/Civitech/Python/twitter_alert_bot/twitter_handles.csv')
test_csv = '/Users/robertness/Documents/Civitech/Python/twitter_alert_bot/test.csv'

bearer_token = 'INSERT BEARER TOKEN HERE'

# select the column to pull
user_name = twitter_users['twitter_account']

with open(test_csv, 'a+', newline='') as wf:
    wf.write('user_name'+','+'user_id'+'\n')

for i in range (len(user_name)):
    user = "{}".format(user_name[i])
    #print(directory)
    handle = user.split('/',3)
    last_portion = handle[3]
    command = f'curl "https://api.twitter.com/2/users/by/username/{last_portion}" -H "Authorization: Bearer {bearer_token}"'
    # def append_list_as_row(file_name, list_of_elem):
    with open(test_csv, 'a+', newline='') as wf:
        pulled_json = subprocess.check_output(command, shell=True)
        dataframe = pd.read_json(pulled_json)
        user_id = dataframe.iloc[0]['data']
        # print(user_id)
        wf.write(last_portion+','+user_id+'\n')


