import subprocess
import os

file_path = os.getcwd()

stage_1 = f'{file_path}/stage_1/'
stage_2 = f'{file_path}/stage_2/'

command = f'cat {stage_1}tweets.csv | sed \'s/\"//g\' | sed \'s/^/\"/\' |sed \'s/$/\"/\' | sed \'s/|/\"|\"/g\' >> {stage_2}tweet_load.csv'
subprocess.check_output(command, shell=True)