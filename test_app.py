import tweepy
from config_twitter import Config_Twitter

#config params
my_config = Config_Twitter()
consumer_key = my_config.CONSUMER_KEY
consumer_secret = my_config.CONSUMER_SECRET
access_token = my_config.ACCESS_TOKEN
access_token_secret = my_config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline(tweet_mode='extended')
for tweet in public_tweets:
    print('{} ({}) \n {} \n +{} r:{}'.format(tweet.user.name,tweet.user.screen_name,
                            tweet.full_text,tweet.favorite_count,tweet.retweet_count))
    print('------')