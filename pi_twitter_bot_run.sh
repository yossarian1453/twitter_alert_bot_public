#!/bin/bash
# -x to print commands before executing them
set -x
# stage 1
/usr/bin/python3.7 /home/pi/twitter_bot_alert/stage_1/pi_tweet_pull.py
/usr/bin/python3.7 /home/pi/twitter_bot_alert/stage_1/pi_retweet.py

# stage 2
/usr/bin/python3.7 /home/pi/twitter_bot_alert/stage_2/pi_double_quote_removal.py
/usr/bin/python3.7 /home/pi/twitter_bot_alert/stage_2/pi_tweet_loader_pg.py
/usr/bin/python3.7 /home/pi/twitter_bot_alert/stage_2/pi_file_clear.py
