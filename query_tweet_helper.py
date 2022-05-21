import os
import pandas as pd
import numpy as np
from tqdm import tqdm
import tweepy

import warnings
warnings.filterwarnings("ignore")


# Import Path
main_path = './'
auth_path = './auth/'
ids_path = './covid19-indonesian-tweet/ids/'

# def query_exist_tweet(q, list_of_id, count_query):
def query_exist_tweet(q, list_of_id):
    count = 0
    # Load auth file
    # acct_twitter_1 = pd.read_csv(auth_path+'arkha_analytics.csv')
    # acct_twitter_2 = pd.read_csv(auth_path+'dummy_analytic.csv')
    acct_twitter_3 = pd.read_csv(auth_path+'arkha98-dev.csv')
    # Authorize our Twitter credentials
    auth = tweepy.OAuthHandler(acct_twitter_3.api_key.values[0], acct_twitter_3.api_key_secret.values[0])
    auth.set_access_token(acct_twitter_3.access_token.values[0], acct_twitter_3.access_token_secret.values[0])
    api = tweepy.API(auth)
    
    q = q.lower()
    q = q.split(' ')
    df = pd.DataFrame(columns=['id', 'tweet'])
    for id in list_of_id:
        # if count == count_query: continue
        try:
            tweet = api.get_status(id=int(id)).text.lower()
        except:
            continue
        check = False
        for query in q:
            if query in tweet:
                check = True
        if check:
            df2 = pd.DataFrame({"id":[id], "tweet":[tweet]})
            df = df.append(df2, ignore_index=True)
            # count += 1
    return df