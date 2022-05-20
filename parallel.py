import multiprocessing
import os
import subprocess
import glob

def execute(process):
    os.system(f'python3 {process}')

query_tweet = glob.glob('query_tweet*.py')
query_tweet.remove('query_tweet_helper.py')

process_pool = multiprocessing.Pool(processes = len(query_tweet))
process_pool.map(execute, query_tweet)