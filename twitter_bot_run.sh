#!/bin/bash
# -x to print commands before executing them
set -x
# stage 1
/usr/local/bin/python3 /locataion/of/repo/twitter_bot_alert/stage_1/tweet_pull.py
/usr/local/bin/python3 /locataion/of/repo/twitter_bot_alert/stage_1/retweet.py

# stage 2
/usr/local/bin/python3 /locataion/of/repo/twitter_bot_alert/stage_2/double_quote_removal.py
/usr/local/bin/python3 /locataion/of/repo/twitter_bot_alert/stage_2/tweet_loader_pg.py
/usr/local/bin/python3 /locataion/of/repo/twitter_bot_alert/stage_2/file_clear.py
