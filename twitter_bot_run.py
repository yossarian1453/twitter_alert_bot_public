import os

# stage 1
tweet_pull = '/usr/local/bin/python3 /Users/robertness/twitter_bot_alert/stage_1/tweet_pull.py'
retweet = '/usr/local/bin/python3 /Users/robertness/twitter_bot_alert/stage_1/retweet.py'

# stage 2
double_quote_removal = '/usr/local/bin/python3 /Users/robertness/twitter_bot_alert/stage_2/double_quote_removal.py'
tweet_loader_pg = '/usr/local/bin/python3 /Users/robertness/twitter_bot_alert/stage_2/tweet_loader_pg.py'
file_clear = '/usr/local/bin/python3 /Users/robertness/twitter_bot_alert/stage_2/file_clear.py'

# stage 1
os.system(tweet_pull)
os.system(retweet)

# stage 2
os.system(double_quote_removal)
os.system(tweet_loader_pg)
os.system(file_clear)