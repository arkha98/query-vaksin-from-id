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
a = list_ids[23*0:23*1]
b = list_ids[23*1:23*2]
c = list_ids[23*2:23*3]
d = list_ids[23*3:23*4]
e = list_ids[23*4:23*5]
f = list_ids[23*5:23*6]
g = list_ids[23*6:23*7]
h = list_ids[23*7:23*8]
i = list_ids[23*8:23*9]
j = list_ids[23*9:23*10]
k = list_ids[23*10:23*11]
l = list_ids[23*11:23*12]
m = list_ids[23*12:23*13]
n = list_ids[23*13:23*14]
o = list_ids[23*14:23*15]
p = list_ids[23*15:23*16]
q = list_ids[23*16:23*17]
r = list_ids[23*17:23*18]
s = list_ids[23*18:23*19]
t = list_ids[23*19:23*20-1]

# q="vaksin vaccine booster boster Sinovac Astrazeneca Moderna Sinopharm Pfizer BioNTech Novavax Sputnik Janssen Convidencia Zifivax"
query="vaksin"
for ids in f:
    try:
        df_ids = pd.read_csv(ids_path+ids, header=None)
    except:
        continue
    try:
        tweet = qt.query_exist_tweet(q=query, list_of_id=df_ids.values)
    except:
        tweet = qt.query_exist_tweet(q=query, list_of_id=df_ids.values)
    tweet.to_csv(main_path+'query_tweet/'+ids, index=False)