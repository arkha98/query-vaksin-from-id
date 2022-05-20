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
    acct_twitter_1 = pd.read_csv(auth_path+'arkha_analytics.csv')
    acct_twitter_2 = pd.read_csv(auth_path+'dummy_analytic.csv')
    acct_twitter_3 = pd.read_csv(auth_path+'arkha98-dev.csv')
    # Authorize our Twitter credentials
    auth = tweepy.OAuthHandler(acct_twitter_1.api_key.values[0], acct_twitter_1.api_key_secret.values[0])
    auth.set_access_token(acct_twitter_1.access_token.values[0], acct_twitter_1.access_token_secret.values[0])
    api = tweepy.API(auth)
    
    q = q.lower()
    q = q.split(' ')
    df = pd.DataFrame(columns=['id', 'tweet'])
    for id in tqdm(list_of_id):
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

list_ids = os.listdir(ids_path)
a = list_ids[234*0:234*1]
b = list_ids[234*1:234*2-1]

q="vaksin vaccine booster boster Sinovac Astrazeneca Moderna Sinopharm Pfizer BioNTech Novavax Sputnik Janssen Convidencia Zifivax"
for ids in a:
    print(ids)
    try:
        df_ids = pd.read_csv(ids_path+ids, header=None)
    except:
        print("NO ID")
        continue
    try:
        tweet = query_exist_tweet(q=q, list_of_id=df_ids.values)
    except:
        tweet = query_exist_tweet(q=q, list_of_id=df_ids.values)
    print("found {}".format(tweet.shape[0]))
    tweet.to_csv(main_path+'query_tweet/'+ids, index=False)