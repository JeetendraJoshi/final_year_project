import tweepy
import initial
import pandas


ACCESS_TOKEN = '809507448809816065-XuOeTj6ONVj0PPTsGgXC6TS05DYJ64v'
ACCESS_TOKEN_SECRET = 'ZpV6p7XLKl4KUkr1LKJZ9ELPXeJzYyDGDHWR2aJLl9nzv'
CONSUMER_KEY = 'BU3OSxFQzVxtiLVqEOcVmFAZr'
CONSUMER_SECRET = '9Aqio6AnnyCQ2mQm0uVWSmCGmRgVYVC8FsOKnGtkK946WQSuuS'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#
# cursor = tweepy.Cursor(api.user_timeline, id = 'twitter', tweet_mode = 'extended').items(1) #<- Tweets from a user
# cursor = tweepy.Cursor(api.search, q = "Bitcoin", tweet_mode = 'extended').items(1) #<- Topic related tweet
# for i in cursor:
#     print(i.full_text)
#


number_of_tweets = 200
tweets = []
likes = []
time = []

for i in tweepy.Cursor(api.user_timeline, id = "twitter", tweet_mode = "extended").items(number_of_tweets):
    tweets.append(i.full_text)
    likes.append(i.favorite_count)
    time.append(i.created_at)

df = pd.DataFrame({'tweets': tweets, 'likes': likes, 'time': time})
