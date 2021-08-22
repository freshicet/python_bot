import tweepy
import News
from decouple import config


# Authenticate to Twitter
auth = tweepy.OAuthHandler(config('consumer_key'), 
    config('consumer_secret'))
auth.set_access_token(config('key'), 
    config('secret'))

# Create API object
api = tweepy.API(auth)
# import news
title, url = News.NewsFromAPI()
# Create a tweet
api.update_status(title + " " + url)


