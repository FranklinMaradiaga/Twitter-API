from pytwitter import Api
from cryptography.x509 import load_pem_x509_certificate
# import requests
import pandas as pd

CONSUMER_KEY = 'UL1po4lsawfWRubl2ecIs16FP'
CONSUMER_SECRET = 'TkzqSUKd81xDuZr3pTR6kxgBZFhJiPM2XVz6OatBOkqaJL2dB5'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAGBLeQEAAAAAaHebLkgV5Z9RTfB9uh1u%2FZp3iKo%3DVVj15lNsi2yfaslS0l6CffwelmWPUCvNN4efJOfiRTxc7h9AeZ'
ACCESS_TOKEN = '1542548435819266055-giRnvWw97Pz0BNTTJ9wCV82yF71pwz'
ACCESS_TOKEN_SECRET = 'CAaqwq9fqYRDK1rjRghqtxlqnirtv7oIPwqZVcTnzKEoL'

my_api = Api(bearer_token = BEARER_TOKEN)

response = my_api.get_following(user_id="44196397", max_results=5)

ids = []
names = []
usernames = []

for data in response.data:
    ids.append(data.id)
    names.append(data.name)
    usernames.append(data.username)

followers = {
              'ids' : ids,
              'names' : names,
              'usernames' : usernames
            }

print("\nids:", followers['ids'])
print("\nnames:", followers['ids'])
print("\nusernames:", followers['ids'])










# print(my_api.get_user(user_id="44196397"))
# print(author_id("44196397"))
# print(type(my_api.get_following(user_id="3762209068")))
# following  pd.DataFrame.from_dict(response)
# l = list(response)











# import tweepy

# CONSUMER_KEY = 'UL1po4lsawfWRubl2ecIs16FP'
# CONSUMER_SECRET = 'TkzqSUKd81xDuZr3pTR6kxgBZFhJiPM2XVz6OatBOkqaJL2dB5'
# BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAGBLeQEAAAAAaHebLkgV5Z9RTfB9uh1u%2FZp3iKo%3DVVj15lNsi2yfaslS0l6CffwelmWPUCvNN4efJOfiRTxc7h9AeZ'
# ACCESS_TOKEN = '1542548435819266055-giRnvWw97Pz0BNTTJ9wCV82yF71pwz'
# ACCESS_TOKEN_SECRET = 'CAaqwq9fqYRDK1rjRghqtxlqnirtv7oIPwqZVcTnzKEoL'

# # create your client 
# client = tweepy.Client(bearer_token=BEARER_TOKEN)

# search_query = "#covid19 -in:retweets"

# query = "#covid19 lang:en -is:retweet"
