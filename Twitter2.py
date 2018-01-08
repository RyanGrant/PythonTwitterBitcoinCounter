import tweepy
import sys
from TwitterAPI import TwitterRestPager
import TwitterAPI

print("Begin")
consumer_key = 'insert'
consumer_secret = 'your'
access_token = 'keys'
access_token_secret = 'here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = TwitterAPI.TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

# This is a dictionary that holds the amount of mentions in a given hour
dictionary = {"Jan":{8:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, \
                        11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, \
                        22:0, 23:0}, \
                     7:{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, \
                        11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, \
                        22:0, 23:0}}}

api = TwitterAPI.TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

# Using Ethereum because it's a little bit less well known than bitcoin and
# and should have far fewer tweets, thus more manageable for me to test
# Also, the Twitter API limits the amount of queries per second, so this
# is capped out to run 100 every 6 seconds.  Kinda slow to run on something
# with as many mentions as bitcoin
r = TwitterRestPager(api, 'search/tweets', {'q':'ethereum', 'count':100})
for item in r.get_iterator(wait=6):
    time_stamp = item['created_at']
    month = time_stamp[4:7]
    day = int(time_stamp[8:10])
    hour = int(time_stamp[11:13])
    if ('text' in item):
        dictionary[month][day][hour] += 1
    elif 'message' in item and item['code'] == 88:
        print('SUSPEND, RATE LIMIT EXCEEDED: %s' % item['message'])
        break
    print(dictionary)
