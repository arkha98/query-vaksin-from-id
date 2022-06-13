import os
import pandas as pd
import numpy as np
from tqdm import tqdm
import tweepy

import warnings
warnings.filterwarnings("ignore")


# Import Path
main_path = '../../'
auth_path = main_path+'auth/'
ids_path = main_path+'covid19-indonesian-tweet/ids/'
merge_path = './'

def query_username(list_of_id):
    count = 0
    # Load auth file
    # acct_twitter_1 = pd.read_csv(auth_path+'arkha_analytics.csv')
    # acct_twitter_2 = pd.read_csv(auth_path+'dummy_analytic.csv')
    acct_twitter_3 = pd.read_csv(auth_path+'arkha98-dev.csv')
    # Authorize our Twitter credentials
    auth = tweepy.OAuthHandler(acct_twitter_3.api_key.values[0], acct_twitter_3.api_key_secret.values[0])
    auth.set_access_token(acct_twitter_3.access_token.values[0], acct_twitter_3.access_token_secret.values[0])
    api = tweepy.API(auth)
    
    df = pd.DataFrame(columns=['tweet_id', 'username'])
    for id in tqdm(list_of_id):
        try:
            user = api.lookup_users()
        except:
            continue
        df2 = pd.DataFrame({"tweet_id":[id], "username":[user]})
        df = df.append(df2, ignore_index=True)
    return df

df_merge_tweet = pd.read_csv('merge_tweet.csv')
df_all_user = query_username(df_merge_tweet['id'].values[0])
df_all_user.to_csv('all_user.csv',index=False)