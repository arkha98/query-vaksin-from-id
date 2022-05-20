import os
import pandas as pd
import numpy as np
from tqdm import tqdm
import tweepy
import query_tweet_helper as qt

import warnings
warnings.filterwarnings("ignore")


# Import Path
main_path = './'
auth_path = './auth/'
ids_path = './covid19-indonesian-tweet/ids/'

list_ids = os.listdir(ids_path)
a = list_ids[47*0:47*1]
b = list_ids[47*1:47*2]
c = list_ids[47*2:47*3]
d = list_ids[47*3:47*4]
e = list_ids[47*4:47*5]
f = list_ids[47*5:47*6]
g = list_ids[47*6:47*7]
h = list_ids[47*7:47*8]
i = list_ids[47*8:47*9]
j = list_ids[47*9:47*10-1]

# q="vaksin vaccine booster boster Sinovac Astrazeneca Moderna Sinopharm Pfizer BioNTech Novavax Sputnik Janssen Convidencia Zifivax"
q="vaksin"
for ids in e:
    try:
        df_ids = pd.read_csv(ids_path+ids, header=None)
    except:
        continue
    try:
        tweet = qt.query_exist_tweet(q=q, list_of_id=df_ids.values)
    except:
        tweet = qt.query_exist_tweet(q=q, list_of_id=df_ids.values)
    tweet.to_csv(main_path+'query_tweet/'+ids, index=False)