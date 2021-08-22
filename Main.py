import tweepy
import News
from decouple import config
from random import randint
from time import sleep



# Authenticate to Twitter
auth = tweepy.OAuthHandler(config('consumer_key'), 
    config('consumer_secret'))
auth.set_access_token(config('key'), 
    config('secret'))

# Create API object
api = tweepy.API(auth)
# import news
title, url = News.NewsFromAPI()
# Adding random sleep function to tweet
sleep(randint(100,36000))
# Create a tweet
api.update_status(title + " " + url)


